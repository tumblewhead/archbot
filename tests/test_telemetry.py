"""Run telemetry tests: offline, local, no Codex account required."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import telemetry as tel


class TelemetryTests(unittest.TestCase):
    def test_jsonl_counts_usage_and_command_activity(self):
        with tempfile.TemporaryDirectory() as tmp:
            stream = Path(tmp) / 'events.jsonl'
            events = [
                {'type': 'thread.started', 'thread_id': 'example-session'},
                {'type': 'turn.completed', 'usage': {'input_tokens': 10, 'cached_input_tokens': 4, 'output_tokens': 3}},
                {'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'python tools/pc.py view --emit', 'exit_code': 0}},
                {'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'python tools/pc.py check', 'exit_code': 1}},
                {'type': 'turn.completed', 'usage': {'input_tokens': 20, 'cached_input_tokens': 5, 'output_tokens': 7}},
            ]
            stream.write_text('\n'.join(json.dumps(e) for e in events) + '\nnot-json\n')
            out = tel.parse_events(stream)
            self.assertEqual(out['token_usage']['input_tokens'], 30)
            self.assertEqual(out['token_usage']['output_tokens'], 10)
            self.assertEqual(out['turns_completed'], 2)
            self.assertEqual(out['command_failures'], 1)
            self.assertEqual(out['invalid_json_lines'], 1)
            self.assertEqual(out['observed_view_commands'], 1)
            self.assertEqual(out['observed_check_commands'], 1)
            self.assertEqual(out['session_id'], 'example-session')

    def test_changes_use_hash_not_timestamp_for_small_files(self):
        a = {'x.md': {'bytes': 5, 'mtime_ns': 1, 'sha256': 'aaa'}}
        b = {'x.md': {'bytes': 5, 'mtime_ns': 2, 'sha256': 'aaa'},
             'y.md': {'bytes': 1, 'mtime_ns': 3, 'sha256': 'bbb'}}
        self.assertEqual(tel.changes(a, b)[0]['path'], 'y.md')
        self.assertEqual(len(tel.changes(a, b)), 1)

    def test_manual_run_export_never_includes_raw_logs(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(tel, 'RUNS', Path(tmp) / 'runs'):
                rid, _ = tel.initial_state('proof-scout', None, 'manual-demo', 'manual',
                                           '/architecture/AS-001/spine.md')
                rd = tel.RUNS / rid
                (rd / 'codex.events.jsonl').write_text('{"type":"turn.completed","usage":{"input_tokens":25}}\n')
                (rd / 'codex.stderr.log').write_text('DO-NOT-EXPORT')
                d = tel.finalize(rd, exit_code=None, elapsed=5, run_checks=False)
                self.assertEqual(d['status'], 'unobserved')
                self.assertEqual(d['gate_decision'], 'not_evaluated')
                self.assertEqual(d['codex']['token_usage']['input_tokens'], 25)
                out = Path(tmp) / 'review.zip'
                args = type('Args', (), {'run': rid, 'out': str(out), 'overwrite': False, 'no_context': False})()
                self.assertEqual(tel.export(args), 0)
                with zipfile.ZipFile(out) as z:
                    self.assertIn('summary.json', z.namelist())
                    self.assertIn('review.md', z.namelist())
                    self.assertIn('context/knowledge/architecture/AS-001/spine.md', z.namelist())
                    self.assertFalse(any(n.endswith('.csv') for n in z.namelist()))
                    self.assertFalse(any('events' in n or 'stderr' in n for n in z.namelist()))
                    self.assertNotIn('DO-NOT-EXPORT', z.read('review.md').decode())

    def test_context_profile_excludes_raw_from_proof_scout(self):
        profile = tel.context_profile('proof-scout', '/architecture/AS-001/spine.md')
        self.assertTrue(profile['available'])
        self.assertEqual(profile['nonconcept_artifacts'], 0)
        self.assertGreater(profile['eligible_text_bytes_within_budget'], 0)

    def test_fake_codex_batch_run_and_local_aggregation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / 'fake-codex'
            script.write_text('''#!/usr/bin/env python3
import json,sys
assert sys.argv[1:3] == ['exec','--json']
assert sys.stdin.read()
print(json.dumps({'type':'thread.started','thread_id':'fake-123'}))
print(json.dumps({'type':'turn.completed','usage':{'input_tokens':123,'output_tokens':9}}))
''')
            script.chmod(0o755)
            prompt = root / 'prompt.md'
            prompt.write_text('Toy task.\n')
            with patch.object(tel, 'RUNS', root / 'runs'):
                args = type('Args', (), dict(role='proof-scout', spine='/architecture/AS-001/spine.md',
                                             prompt=str(prompt), label='offline-test',
                                             codex_bin=str(script), sandbox='workspace-write',
                                             model=None, no_checks=True))()
                self.assertEqual(tel.run_codex(args), 0)
                rid = next(tel.RUNS.iterdir()).name
                d = tel.load(tel.RUNS / rid / 'run.json')
                self.assertEqual(d['codex']['token_usage']['input_tokens'], 123)
                self.assertEqual(d['codex']['session_id'], 'fake-123')
                self.assertEqual(d['status'], 'completed')
                self.assertEqual(d['gate_decision'], 'not_evaluated')


    def _setup_two_projects(self, root: Path):
        import textwrap
        (root / 'process').mkdir()
        (root / 'process/views.yaml').write_text(
            'roles:\n  proof-scout:\n    follow: [results]\n'
            '    max_depth: 2\n    max_bytes: 28000\n'
            'mandatory_closure: [assumes]\n', encoding='utf-8')
        (root / 'knowledge').mkdir()
        (root / 'knowledge/index.md').write_text('Demo index\n', encoding='utf-8')
        for name in ('alpha', 'beta'):
            folder = root / 'knowledge/architecture' / name
            folder.mkdir(parents=True)
            (folder / 'spine.md').write_text(
                '---\ntype: Architecture Spine\nid: ' + name.upper() +
                '\nrelations:\n  - kind: results\n    target: /architecture/' +
                name + '/result.md\n---\n' + name + ' root\n', encoding='utf-8')
            (folder / 'result.md').write_text(
                '---\ntype: Result\nid: ' + name.upper() +
                '-RESULT\n---\n' + name + ' only\n', encoding='utf-8')

    def test_explicit_projects_isolate_estimate_and_export(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'), \
                    patch.object(tel, 'RUNS', root / 'runs'):
                for name, other in (('alpha', 'beta'), ('beta', 'alpha')):
                    spine = f'/architecture/{name}/spine.md'
                    profile = tel.context_profile('proof-scout', spine)
                    self.assertTrue(profile['available'], profile)
                    self.assertEqual(profile['spine'], spine)
                    selected = {p for p, _ in tel.selected_context('proof-scout', spine)}
                    self.assertIn(f'knowledge/architecture/{name}/result.md', selected)
                    self.assertFalse(any(f'/architecture/{other}/' in p for p in selected))
                    rid, state = tel.initial_state('proof-scout', None, 'isolated', 'manual', spine)
                    self.assertEqual(state['spine'], spine)
                    tel.finalize(tel.RUNS / rid, exit_code=0, elapsed=0, run_checks=False)
                    output = root / f'{name}.zip'
                    args = type('Args', (), {'run': rid, 'out': str(output),
                                               'overwrite': False, 'no_context': False})()
                    self.assertEqual(tel.export(args), 0)
                    with zipfile.ZipFile(output) as archive:
                        names = archive.namelist()
                        self.assertIn(f'context/knowledge/architecture/{name}/result.md',
                                      names)
                        self.assertFalse(any(f'/architecture/{other}/' in p for p in names))
                        receipt = json.loads(archive.read('summary.json'))
                        self.assertEqual(receipt['telemetry']['spine'], spine)

    def test_missing_unsafe_and_cross_project_spines_are_rejected(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'), \
                    patch.object(tel, 'RUNS', root / 'runs'):
                self.assertFalse(tel.context_profile('proof-scout')['available'])
                for bad in (None, '', 'architecture/alpha/spine.md',
                            '/architecture/../beta/spine.md',
                            '/architecture/missing/spine.md', '/../../etc/passwd'):
                    with self.subTest(bad=bad):
                        with self.assertRaises(ValueError):
                            tel.initial_state('proof-scout', None, 'reject', 'manual', bad)
                self.assertFalse((root / 'runs').exists())
                beta = root / 'knowledge/architecture/beta/spine.md'
                beta.write_text(beta.read_text().replace(
                    '/architecture/beta/result.md',
                    '/architecture/alpha/result.md'), encoding='utf-8')
                self.assertFalse(tel.context_profile(
                    'proof-scout', '/architecture/beta/spine.md')['available'])
                with self.assertRaisesRegex(ValueError, 'Cross-project'):
                    tel.selected_context('proof-scout', '/architecture/beta/spine.md')
                with self.assertRaisesRegex(ValueError, 'Cross-project'):
                    tel.initial_state('proof-scout', None, 'reject', 'manual',
                                      '/architecture/beta/spine.md')
                self.assertFalse((root / 'runs').exists())

    def test_historical_run_context_cannot_fall_back_to_as001(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'), \
                    patch.object(tel, 'RUNS', root / 'runs'):
                with self.assertRaisesRegex(ValueError, 'no project spine'):
                    tel.selected_context('proof-scout', None)



    def test_fr001_r1_symlink_spine_does_not_substitute_project(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            alpha = root / 'knowledge/architecture/alpha/spine.md'
            beta = root / 'knowledge/architecture/beta/spine.md'
            alpha.unlink()
            alpha.symlink_to(beta)
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'), \
                    patch.object(tel, 'RUNS', root / 'runs'):
                self.assertFalse(tel.context_profile(
                    'proof-scout', '/architecture/alpha/spine.md')['available'])
                with self.assertRaisesRegex(ValueError, 'symlink'):
                    tel.initial_state('proof-scout', None, 'forbidden', 'manual',
                                      '/architecture/alpha/spine.md')
                self.assertFalse((root / 'runs').exists())

    def test_fr001_r1_symlink_dependency_does_not_alias_project(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            alpha_result = root / 'knowledge/architecture/alpha/result.md'
            beta_result = root / 'knowledge/architecture/beta/result.md'
            alpha_result.unlink()
            alpha_result.symlink_to(beta_result)
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'):
                profile = tel.context_profile('proof-scout', '/architecture/alpha/spine.md')
                self.assertFalse(profile['available'], profile)
                with self.assertRaises(ValueError):
                    tel.selected_context('proof-scout', '/architecture/alpha/spine.md')

    def test_fr001_r2_other_collection_cannot_supply_project_evidence(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            foreign = root / 'knowledge/history/beta'
            foreign.mkdir(parents=True)
            (foreign / 'result.md').write_text(
                '---\ntype: Result\nid: BETA-FOREIGN\n---\nnot alpha\n',
                encoding='utf-8')
            alpha = root / 'knowledge/architecture/alpha/spine.md'
            alpha.write_text(alpha.read_text().replace(
                '/architecture/alpha/result.md', '/history/beta/result.md'),
                encoding='utf-8')
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'), \
                    patch.object(tel, 'RUNS', root / 'runs'):
                self.assertFalse(tel.context_profile(
                    'proof-scout', '/architecture/alpha/spine.md')['available'])
                with self.assertRaisesRegex(ValueError, 'Cross-project'):
                    tel.initial_state('proof-scout', None, 'forbidden', 'manual',
                                      '/architecture/alpha/spine.md')
                self.assertFalse((root / 'runs').exists())

    def test_fr001_r3_missing_mandatory_edge_is_not_silently_omitted(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            alpha = root / 'knowledge/architecture/alpha/spine.md'
            alpha.write_text(alpha.read_text().replace(
                '---\nalpha root\n',
                '  - kind: assumes\n'
                '    target: /architecture/alpha/missing-assumption.md\n'
                '---\nalpha root\n'),
                encoding='utf-8')
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'), \
                    patch.object(tel, 'RUNS', root / 'runs'):
                profile = tel.context_profile('proof-scout', '/architecture/alpha/spine.md')
                self.assertFalse(profile['available'])
                self.assertIn('Missing mandatory dependency', profile['reason'])
                with self.assertRaisesRegex(ValueError, 'Missing mandatory'):
                    tel.initial_state('proof-scout', None, 'forbidden', 'manual',
                                      '/architecture/alpha/spine.md')
                self.assertFalse((root / 'runs').exists())

    def test_fr001_explicit_shared_bkp_keeps_mandatory_closure(self):
        import pc
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._setup_two_projects(root)
            shared = root / 'knowledge/bkp'
            shared.mkdir()
            (shared / 'assumption.md').write_text(
                '---\ntype: BackgroundKnowledge\nid: SHARED-ASSUMPTION\n---\ncommon\n',
                encoding='utf-8')
            alpha = root / 'knowledge/architecture/alpha/spine.md'
            alpha.write_text(alpha.read_text().replace(
                '---\nalpha root\n',
                '  - kind: assumes\n'
                '    target: /bkp/assumption.md\n'
                '---\nalpha root\n'), encoding='utf-8')
            with patch.object(tel, 'REPO', root), patch.object(pc, 'KB', root / 'knowledge'):
                selected = {p for p, _ in tel.selected_context(
                    'proof-scout', '/architecture/alpha/spine.md')}
                self.assertIn('knowledge/bkp/assumption.md', selected)
                self.assertNotIn('knowledge/architecture/beta/result.md', selected)



if __name__ == '__main__':
    unittest.main()
