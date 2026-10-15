#!/usr/bin/env python3
"""Local-only run telemetry for Progressive Concretization.

No network, analytics SDK, environment dumps, or background service. Raw Codex
JSONL and stderr stay in ignored runs/. Exports contain bounded review data.
This is *observability*, not architectural/proof gate approval.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid
import zipfile

REPO = Path(__file__).resolve().parents[1]
RUNS = REPO / 'runs'
SCHEMA = 'pc-run-telemetry/v1'
REPORT_SCHEMA = 'pc-review-packet/v1'
SNAPSHOT_ROOTS = ('knowledge', 'reviews', 'process', 'agents', 'tools', 'tests', 'prompts', 'firmware')
MAX_HASH = 2 * 1024 * 1024
MAX_EXPORT_FILE = 48 * 1024
MAX_EXPORT_TOTAL = 192 * 1024
MAX_CONTEXT_TOTAL = 96 * 1024
SAFE_EXPORT_EXTS = {'.md', '.yaml', '.yml', '.json', '.c', '.h', '.py', '.toml', '.txt'}
FIELDS = ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens')
RUN_ID_RE = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._-]{0,96}$')


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def dump(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')
    tmp.replace(path)


def load(path: Path) -> dict:
    result = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(result, dict):
        raise ValueError('Expected JSON object: ' + str(path))
    return result


def git(*args: str) -> str | None:
    p = subprocess.run(['git', *args], cwd=REPO, capture_output=True, text=True, check=False)
    return p.stdout.strip() if p.returncode == 0 else None


def snapshot() -> dict:
    """Snapshot relevant artifacts, never opening multi-megabyte raw captures."""
    result = {}
    for root in SNAPSHOT_ROOTS:
        parent = REPO / root
        if not parent.exists():
            continue
        for folder, dirs, files in os.walk(parent, followlinks=False):
            dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', '.venv')
                       and not (Path(folder) / d).is_symlink()]
            for name in files:
                path = Path(folder) / name
                if path.is_symlink() or not path.is_file():
                    continue
                relative = path.relative_to(REPO).as_posix()
                try:
                    st = path.stat()
                    record = {'bytes': st.st_size, 'mtime_ns': st.st_mtime_ns}
                    if st.st_size <= MAX_HASH:
                        record['sha256'] = file_hash(path)
                    result[relative] = record
                except OSError:
                    continue
    return result


def changes(before: dict, after: dict) -> list[dict]:
    rows = []
    for name in sorted(set(before) | set(after)):
        a, b = before.get(name), after.get(name)
        if a is None:
            kind = 'added'
        elif b is None:
            kind = 'deleted'
        elif 'sha256' in a and 'sha256' in b:
            if a['sha256'] == b['sha256']:
                continue
            kind = 'modified'
        elif a['bytes'] != b['bytes'] or a['mtime_ns'] != b['mtime_ns']:
            kind = 'modified'
        else:
            continue
        rows.append({'path': name, 'change': kind,
                     'bytes_before': a['bytes'] if a else None,
                     'bytes_after': b['bytes'] if b else None,
                     'sha256_after': b.get('sha256') if b else None})
    return rows


def require_spine(spine: str | None) -> Path:
    """Validate a declared project spine; never select a default project."""
    if (not isinstance(spine, str) or not spine.startswith('/')
            or spine.startswith('//') or '?' in spine or '#' in spine):
        raise ValueError('An explicit project knowledge-root spine is required')
    parts = Path(spine.lstrip('/')).parts
    if len(parts) < 3 or any(part in ('.', '..') for part in parts):
        raise ValueError('Spine must identify a project and a Markdown concept')
    root = (REPO / 'knowledge').resolve()
    candidate = (root / Path(*parts)).resolve()
    if not candidate.is_relative_to(root) or candidate.suffix != '.md' or not candidate.is_file():
        raise ValueError('Project spine missing, unsafe, or not Markdown')
    return candidate


def context_nodes(role: str, spine: str) -> tuple[dict, dict, dict, list, list]:
    """Select role context only from an explicit project and shared collections."""
    import pc
    start = require_spine(spine)
    cfg = pc.load_yaml(REPO / 'process/views.yaml')
    view = cfg.get('roles', {}).get(role)
    if not isinstance(view, dict):
        raise ValueError('No context view defined for role: ' + str(role))
    docs = pc.catalog()
    allowed = set(view['follow'])
    required = set(cfg.get('mandatory_closure', []))
    depth = int(view['max_depth'])
    nodes = pc.traverse(start, allowed, depth, required, docs,
                        include_nonconcept=bool(view.get('include_nonconcept', False)))
    all_refs = pc.traverse(start, allowed, depth, required, docs,
                           include_nonconcept=True)
    # Project roots are the first two segments, e.g. architecture/AS-001.
    # Optional and mandatory edges cannot import an adjacent project.
    root = (REPO / 'knowledge').resolve()
    relative = start.relative_to(root)
    collection = root / relative.parts[0]
    project = collection / relative.parts[1]
    for path, _, _ in all_refs:
        if path.is_relative_to(collection) and not path.is_relative_to(project):
            raise ValueError('Cross-project context dependency rejected')
    return cfg, view, docs, nodes, all_refs


def context_profile(role: str, spine: str | None = None) -> dict:
    """Estimate role-eligible content, not what Codex actually read."""
    if spine is None:
        return {'available': False, 'reason': 'project_spine_not_declared'}
    try:
        cfg, view, docs, nodes, all_refs = context_nodes(role, spine)
        import pc
        selected = {path for path, _, _ in nodes}
        excluded = [path.relative_to(pc.KB).as_posix() for path, _, _ in all_refs
                    if path not in docs and path not in selected]
        limit = int(view['max_bytes'])
        remaining = limit
        emit = omitted = raw = 0
        for path, _, _ in nodes:
            if path not in docs:
                raw += 1
            elif path.stat().st_size <= remaining:
                emit += path.stat().st_size
                remaining -= path.stat().st_size
            else:
                omitted += 1
        return {'available': True, 'spine': spine,
                'eligible_artifacts': len(nodes), 'nonconcept_artifacts': raw,
                'excluded_nonconcept_references': len(excluded),
                'excluded_nonconcept_examples': excluded[:8],
                'over_budget_concepts': omitted,
                'eligible_text_bytes_within_budget': emit, 'role_body_budget_bytes': limit,
                'note': 'Graph selection estimate, not measured Codex context ingestion'}
    except (ValueError, OSError, ImportError, KeyError, TypeError) as exc:
        return {'available': False, 'spine': spine, 'reason': str(exc)}


def initial_state(role: str, prompt: Path | None, label: str, mode: str,
                  spine: str | None = None) -> tuple[str, dict]:
    require_spine(spine)
    eligible = context_profile(role, spine)
    if not eligible['available']:
        raise ValueError('Project context unavailable: ' + eligible['reason'])
    RUNS.mkdir(parents=True, exist_ok=True)
    rid = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    run_dir = RUNS / rid
    run_dir.mkdir(mode=0o700)
    pmeta = None
    if prompt:
        source = prompt.resolve()
        if not source.is_file():
            raise ValueError(f'Prompt missing: {prompt}')
        pmeta = {'path': source.relative_to(REPO).as_posix() if source.is_relative_to(REPO) else source.name,
                 'sha256': file_hash(source), 'bytes': source.stat().st_size}
    state = {'schema': SCHEMA, 'run_id': rid, 'role': role, 'spine': spine, 'label': label,
             'mode': mode, 'started_at': now_iso(), 'finished_at': None,
             'status': 'in_progress', 'exit_code': None, 'prompt': pmeta,
             'git_before': git('rev-parse', 'HEAD'), 'git_after': None,
             'context_before': eligible,
             'changed_files': [], 'source': 'local',
             'note': 'This telemetry does not certify architectural gates or proofs.'}
    dump(run_dir / 'run.json', state)
    dump(run_dir / 'snapshot_before.json', snapshot())
    return rid, state


def resolve_run(run: str) -> Path:
    if run == 'latest':
        all_runs = sorted(p for p in RUNS.glob('*/run.json') if p.is_file()) if RUNS.is_dir() else []
        if not all_runs:
            raise ValueError('No recorded runs yet')
        return all_runs[-1].parent
    if not RUN_ID_RE.fullmatch(run):
        raise ValueError('Invalid run ID')
    candidate = RUNS / run
    if not candidate.is_dir() or not (candidate / 'run.json').is_file():
        raise ValueError(f'Run not found: {run}')
    return candidate


def parse_events(event_file: Path) -> dict:
    """Capture stable counters from Codex JSONL; preserve unknown events as counts."""
    event_counts = Counter()
    item_counts = Counter()
    token_sum = Counter()
    commands_failed = 0
    view_commands = 0
    check_commands = 0
    session_id = None
    turns = 0
    invalid_lines = 0
    errors = 0
    if not event_file.is_file():
        return {'available': False, 'token_usage': None, 'event_counts': {},
                'item_counts': {}, 'turns_completed': 0, 'command_failures': 0,
                'event_errors': 0, 'invalid_json_lines': 0, 'session_id': None,
                'observed_view_commands': 0, 'observed_check_commands': 0}
    with event_file.open('r', encoding='utf-8', errors='replace') as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                invalid_lines += 1
                continue
            if not isinstance(obj, dict):
                invalid_lines += 1
                continue
            typ = obj.get('type', 'unknown')
            if not isinstance(typ, str):
                typ = 'unknown'
            event_counts[typ] += 1
            if typ == 'thread.started':
                session_id = obj.get('thread_id') if isinstance(obj.get('thread_id'), str) else session_id
            if typ == 'turn.completed':
                turns += 1
                usage = obj.get('usage')
                if isinstance(usage, dict):
                    for key in FIELDS:
                        val = usage.get(key)
                        if type(val) is int and val >= 0:
                            token_sum[key] += val
            if typ in ('turn.failed', 'error'):
                errors += 1
            if typ == 'item.completed':
                item = obj.get('item')
                if isinstance(item, dict):
                    item_type = item.get('type', 'unknown')
                    item_counts[str(item_type)] += 1
                    if item_type == 'command_execution':
                        command = item.get('command', '')
                        if isinstance(command, str):
                            # Store only safe counters, not potentially sensitive command text.
                            if re.search(r'tools/pc\.py\s+view\b', command):
                                view_commands += 1
                            if re.search(r'tools/pc\.py\s+check\b', command):
                                check_commands += 1
                        if isinstance(item.get('exit_code'), int) and item['exit_code'] != 0:
                            commands_failed += 1
    return {'available': True, 'token_usage': dict(token_sum) if turns else None,
            'event_counts': dict(event_counts), 'item_counts': dict(item_counts),
            'turns_completed': turns, 'command_failures': commands_failed,
            'event_errors': errors, 'invalid_json_lines': invalid_lines,
            'session_id': session_id,
            'observed_view_commands': view_commands, 'observed_check_commands': check_commands}


def validation(command: list[str], dest: Path) -> dict:
    try:
        start = time.monotonic()
        p = subprocess.run(command, cwd=REPO, capture_output=True, text=True,
                           errors='replace', timeout=120, check=False)
        output = p.stdout + ('\n' if p.stdout and p.stderr else '') + p.stderr
        dest.write_text(output, encoding='utf-8')
        result = {'exit_code': p.returncode, 'duration_seconds': round(time.monotonic() - start, 3)}
        if 'pc.py' in command and 'check' in command:
            m = re.search(r'CHECK:\s*(\d+) concepts, (\d+) typed links, (\d+) raw bytes hashed, (\d+) warnings, (\d+) errors', output)
            if m:
                result.update(dict(zip(('concepts', 'typed_links', 'raw_bytes_hashed', 'warnings', 'errors'), map(int, m.groups()))))
            result['raw_sha256_checked'] = '--fast' not in command
        if 'unittest' in command:
            m = re.search(r'Ran (\d+) tests? in [\d.]+s', output)
            if m:
                result['tests_run'] = int(m.group(1))
        return result
    except (OSError, subprocess.TimeoutExpired) as exc:
        dest.write_text(str(exc) + '\n', encoding='utf-8')
        return {'exit_code': None, 'error': type(exc).__name__}


def summarize_artifact_changes(rows: list[dict]) -> dict:
    """Counts only; no attempt to grade mathematical or architecture correctness."""
    stats = Counter(item['change'] for item in rows)
    return {'added': stats['added'], 'modified': stats['modified'],
            'deleted': stats['deleted'],
            'proof_opportunity_files': sum('/proofs/opportunities/PO-' in r['path'] for r in rows),
            'review_receipt_files': sum(r['path'].startswith('reviews/') and r['path'].endswith('.md') for r in rows),
            'knowledge_concepts_changed': sum(r['path'].startswith('knowledge/') and r['path'].endswith('.md') for r in rows)}


def finalize(run_dir: Path, *, exit_code: int | None, elapsed: float | None,
             events: Path | None = None, run_checks: bool = True) -> dict:
    state = load(run_dir / 'run.json')
    if state.get('finished_at'):
        raise ValueError('Already finalized: ' + state['run_id'])
    if events is not None:
        dest = run_dir / 'codex.events.jsonl'
        if events.resolve() != dest.resolve():
            shutil.copyfile(events, dest)
    state['finished_at'] = now_iso()
    if elapsed is not None:
        state['wall_seconds'] = round(elapsed, 3)
    else:
        state['wall_seconds'] = round((datetime.fromisoformat(state['finished_at']) -
                                       datetime.fromisoformat(state['started_at'])).total_seconds(), 3)
    state['exit_code'] = exit_code
    state['status'] = 'completed' if exit_code == 0 else ('failed' if exit_code is not None else 'unobserved')
    state['git_after'] = git('rev-parse', 'HEAD')
    after = snapshot()
    dump(run_dir / 'snapshot_after.json', after)
    state['changed_files'] = changes(load(run_dir / 'snapshot_before.json'), after)
    state['artifact_counts'] = summarize_artifact_changes(state['changed_files'])
    state['context_after'] = context_profile(state['role'], state.get('spine'))
    state['codex'] = parse_events(run_dir / 'codex.events.jsonl')
    state['validation'] = {}
    if run_checks:
        state['validation']['structure'] = validation([sys.executable, 'tools/pc.py', 'check', '--fast'], run_dir / 'structure.log')
        state['validation']['unit_tests'] = validation([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], run_dir / 'unit_tests.log')
    else:
        state['validation'] = {'skipped': 'requested by operator'}
    # Distinguish structural checks from approval even when both tools exit 0.
    state['gate_decision'] = 'not_evaluated'
    dump(run_dir / 'run.json', state)
    (run_dir / 'review.md').write_text(review_markdown(state), encoding='utf-8')
    return state


def format_value(value: object) -> str:
    return 'unavailable' if value is None else str(value)


def review_markdown(data: dict) -> str:
    codex = data.get('codex', {})
    usage = codex.get('token_usage') or {}
    val = data.get('validation', {})
    s = val.get('structure', {})
    t = val.get('unit_tests', {})
    modified = data.get('changed_files', [])
    artifact_counts = data.get('artifact_counts', {})
    lines = [f'# Run review: {data["run_id"]}', '',
             f'- Role: `{data["role"]}`; project spine: `{data.get("spine") or "not recorded"}`; label: {data.get("label", "") or "none"}',
             f'- Execution: `{data["mode"]}`; status: `{data["status"]}`; exit code: {format_value(data["exit_code"])}',
             f'- Start (UTC): {data["started_at"]}; duration: {format_value(data.get("wall_seconds"))} s',
             f'- Git HEAD: {format_value(data.get("git_before"))} -> {format_value(data.get("git_after"))}',
             f'- Prompt: `{(data.get("prompt") or {}).get("path", "not provided")}`; SHA-256: `{(data.get("prompt") or {}).get("sha256", "unknown")}`',
             '', '## Codex execution telemetry', '',
             f'- Session ID: {format_value(codex.get("session_id"))}; completed turns: {format_value(codex.get("turns_completed"))}',
             f'- Token usage (input / cached input / output / reasoning output): '
             f'{" / ".join(format_value(usage.get(k)) for k in FIELDS)}',
             f'- Completed tools: {json.dumps(codex.get("item_counts", {}), sort_keys=True)}',
             f'- Command failures: {format_value(codex.get("command_failures"))}; event errors: {format_value(codex.get("event_errors"))}; invalid JSONL: {format_value(codex.get("invalid_json_lines"))}',
             f'- Observed spine-view calls: {format_value(codex.get("observed_view_commands"))}; structural-check calls: {format_value(codex.get("observed_check_commands"))}',
             '', '## Spine projection (eligibility estimate, not actual context read)', '',
             f'- Before: {json.dumps(data.get("context_before", {}), sort_keys=True)}',
             f'- After: {json.dumps(data.get("context_after", {}), sort_keys=True)}',
             '', '## Deterministic checks (not proof or architecture approval)', '',
             f'- OKF structural check: {format_value(s.get("exit_code"))} (0=pass); concepts={format_value(s.get("concepts"))}; links={format_value(s.get("typed_links"))}; warnings={format_value(s.get("warnings"))}; errors={format_value(s.get("errors"))}; raw SHA-256 checked={format_value(s.get("raw_sha256_checked"))}',
             f'- Unit tests: {format_value(t.get("exit_code"))} (0=pass); ran={format_value(t.get("tests_run"))}',
             f'- Formal gate decision: `{data.get("gate_decision", "not_evaluated")}`',
             '', '## Artifact output counts (not quality scores)', '',
             f'- {json.dumps(artifact_counts, sort_keys=True)}',
             '', '## Files changed during run', '']
    if modified:
        for row in modified:
            lines.append(f'- `{row["change"]}` `{row["path"]}` ({format_value(row.get("bytes_after"))} bytes after)')
    else:
        lines.append('No relevant file-content changes detected.')
    lines += ['', '## Questions for review', '',
              '- What new claims, proof opportunities, or decisions were introduced?',
              '- Which supporting sources and assumptions were actually inspected?',
              '- Are any claims stronger than the evidence or deterministic checks justify?',
              '- Which unresolved obligations or changes require a new verification gate?',
              '', 'This report is local telemetry. It does not certify proofs, hardware performance, or gate approval.', '']
    return '\n'.join(lines)


def task_start(args: argparse.Namespace) -> int:
    rid, _ = initial_state(args.role, Path(args.prompt) if args.prompt else None,
                           args.label, 'manual', args.spine)
    print(f'STARTED {rid}')
    print(f'After your interactive Codex session: python tools/telemetry.py finish --run {rid}')
    return 0


def task_finish(args: argparse.Namespace) -> int:
    rd = resolve_run(args.run)
    state = finalize(rd, exit_code=args.exit_code, elapsed=None,
                     events=Path(args.events) if args.events else None,
                     run_checks=not args.no_checks)
    print(f'FINISHED {state["run_id"]} status={state["status"]}; changed={len(state["changed_files"])}')
    print('REVIEW:', rd / 'review.md')
    return 0


def run_codex(args: argparse.Namespace) -> int:
    prompt = Path(args.prompt)
    if not prompt.is_file():
        raise ValueError('Prompt missing: ' + str(prompt))
    executable = shutil.which(args.codex_bin)
    if not executable:
        raise ValueError(f'Codex CLI not found: {args.codex_bin} (use start/finish for interactive sessions)')
    rid, _ = initial_state(args.role, prompt, args.label, 'codex-exec-jsonl', args.spine)
    rd = RUNS / rid
    cmd = [executable, 'exec', '--json', '--sandbox', args.sandbox,
           '--output-last-message', str(rd / 'last-message.txt')]
    if args.model:
        cmd.extend(['--model', args.model])
    cmd.append('-')
    start = time.monotonic()
    try:
        # Do not echo event bodies or capture environment variables in the report.
        with (rd / 'codex.events.jsonl').open('w', encoding='utf-8') as out, \
             (rd / 'codex.stderr.log').open('w', encoding='utf-8') as err:
            proc = subprocess.Popen(cmd, cwd=REPO, stdin=subprocess.PIPE,
                                    stdout=out, stderr=err, text=True)
            # Prompt goes to stdin so it is not exposed through argv/process listings.
            proc.communicate(input=prompt.read_text(encoding='utf-8'))
        code = proc.returncode
    except (OSError, KeyboardInterrupt):
        code = 130
    data = finalize(rd, exit_code=code, elapsed=time.monotonic()-start, run_checks=not args.no_checks)
    print(f'RUN {rid} status={data["status"]} exit={code} elapsed={data["wall_seconds"]}s')
    print(f'TOKENS: {data["codex"]["token_usage"] if data["codex"]["token_usage"] is not None else "unavailable"}')
    print('REVIEW:', rd / 'review.md')
    print(f'EXPORT: python tools/telemetry.py export --run {rid}')
    return code


def selected_context(role: str, spine: str | None) -> list[tuple[str, Path]]:
    """Export only the role-projected context for the run's recorded spine."""
    if spine is None:
        raise ValueError('Cannot export context: no project spine was recorded')
    _, _, docs, nodes, _ = context_nodes(role, spine)
    return [(path.relative_to(REPO).as_posix(), path)
            for path, _, _ in nodes if path in docs]


def export(args: argparse.Namespace) -> int:
    rd = resolve_run(args.run)
    data = load(rd / 'run.json')
    if not data.get('finished_at'):
        raise ValueError('Cannot export a run still in progress')
    out = Path(args.out) if args.out else (REPO / f'pc-review-{data["run_id"]}.zip')
    out = out.resolve()
    if out.exists() and not args.overwrite:
        raise ValueError(f'Refusing to overwrite existing file: {out} (use --overwrite)')
    out.parent.mkdir(parents=True, exist_ok=True)
    packet = {'schema': REPORT_SCHEMA, 'telemetry': data, 'artifact_exports': [],
              'context_exports': [],
              'export_policy': 'No raw JSONL, stderr, prompts, large/binary datasets, or environment are copied. No automated secret detection: inspect the ZIP before uploading.'}
    selected: list[tuple[str, bytes]] = []
    total = 0
    for item in data.get('changed_files', []):
        path = REPO / item['path']
        if item['change'] == 'deleted' or not path.is_file() or path.is_symlink():
            continue
        if not item['path'].startswith(('knowledge/', 'reviews/')) or path.suffix.lower() not in SAFE_EXPORT_EXTS:
            continue
        size = path.stat().st_size
        if size > MAX_EXPORT_FILE or total + size > MAX_EXPORT_TOTAL:
            packet['artifact_exports'].append({'path': item['path'], 'status': 'omitted_size_budget', 'bytes': size})
            continue
        payload = path.read_bytes()
        # Preserve exactly the bytes we hashed during finalization. If edited since, omit.
        if item.get('sha256_after') != hashlib.sha256(payload).hexdigest():
            packet['artifact_exports'].append({'path': item['path'], 'status': 'omitted_changed_since_run'})
            continue
        selected.append((item['path'], payload))
        packet['artifact_exports'].append({'path': item['path'], 'status': 'included', 'bytes': size,
                                           'sha256': hashlib.sha256(payload).hexdigest()})
        total += size
    context: list[tuple[str, bytes]] = []
    context_total = 0
    if not args.no_context:
        final_snapshot = load(rd / 'snapshot_after.json')
        for name, path in selected_context(data['role'], data.get('spine')):
            if path.is_symlink() or not path.is_file():
                continue
            size = path.stat().st_size
            if size > MAX_EXPORT_FILE or context_total + size > MAX_CONTEXT_TOTAL:
                packet['context_exports'].append({'path': name, 'status': 'omitted_size_budget', 'bytes': size})
                continue
            blob = path.read_bytes()
            known = final_snapshot.get(name, {}).get('sha256')
            if known is None or known != hashlib.sha256(blob).hexdigest():
                packet['context_exports'].append({'path': name, 'status': 'omitted_changed_since_run'})
                continue
            context.append((name, blob))
            context_total += size
            packet['context_exports'].append({'path': name, 'status': 'included', 'bytes': size,
                                              'sha256': known,
                                              'qualification': 'Eligible role context, not evidence this file was read by Codex'})
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('review.md', review_markdown(data))
        archive.writestr('summary.json', json.dumps(packet, indent=2, sort_keys=True) + '\n')
        for name, payload in selected:
            archive.writestr('artifacts/' + name, payload)
        for name, payload in context:
            archive.writestr('context/' + name, payload)
    print('EXPORTED:', out)
    print(f'ARTIFACTS_INCLUDED={len(selected)} BYTES={total}; '
          f'CONTEXT_INCLUDED={len(context)} BYTES={context_total} (inspect archive before uploading)')
    return 0


def listing(args: argparse.Namespace) -> int:
    if not RUNS.is_dir():
        print('No runs recorded')
        return 0
    for path in sorted(RUNS.glob('*/run.json')):
        d = load(path)
        print(f'{d["run_id"]} {d["role"]:25s} {d["status"]:12s} '
              f'{format_value(d.get("wall_seconds")):>8s}s '
              f'changes={len(d.get("changed_files", []))} '
              f'tokens={format_value((d.get("codex") or {}).get("token_usage"))}')
    return 0


def compare(args: argparse.Namespace) -> int:
    a = load(resolve_run(args.baseline) / 'run.json')
    b = load(resolve_run(args.candidate) / 'run.json')
    print(f'COMPARISON: {a["run_id"]} -> {b["run_id"]}')
    for key in ('wall_seconds',):
        x, y = a.get(key), b.get(key)
        print(f'{key}: {x} -> {y}' + (f' (delta={round(y-x, 3):+})' if x is not None and y is not None else ''))
    for key in FIELDS:
        x = ((a.get('codex') or {}).get('token_usage') or {}).get(key)
        y = ((b.get('codex') or {}).get('token_usage') or {}).get(key)
        print(f'{key}: {format_value(x)} -> {format_value(y)}' +
              (f' (delta={y-x:+})' if isinstance(x, int) and isinstance(y, int) else ''))
    for tag, rec in [('baseline', a), ('candidate', b)]:
        v = rec.get('validation', {})
        print(f'{tag}: changed_files={len(rec.get("changed_files", []))}; '
              f'structure_exit={(v.get("structure") or {}).get("exit_code")}; '
              f'unit_test_exit={(v.get("unit_tests") or {}).get("exit_code")}')
    print(f'artifact_counts: {a.get("artifact_counts")} -> {b.get("artifact_counts")}')
    print('Comparison is descriptive; differing tasks/prompts are not controlled experiments.')
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sp = p.add_subparsers(dest='action', required=True)
    start = sp.add_parser('start', help='Mark start of interactive Codex session')
    start.add_argument('--role', required=True)
    start.add_argument('--spine', required=True, help='Explicit project knowledge-root spine')
    start.add_argument('--prompt')
    start.add_argument('--label', default='')
    start.set_defaults(fn=task_start)
    finish = sp.add_parser('finish', help='Mark end of interactive Codex session')
    finish.add_argument('--run', required=True)
    finish.add_argument('--events', help='Optional Codex exec --json output file')
    finish.add_argument('--exit-code', type=int, help='Observed exit code; omit when unknown')
    finish.add_argument('--no-checks', action='store_true')
    finish.set_defaults(fn=task_finish)
    execute = sp.add_parser('run', help='Launch codex exec --json and record locally')
    execute.add_argument('--role', required=True)
    execute.add_argument('--spine', required=True, help='Explicit project knowledge-root spine')
    execute.add_argument('--prompt', required=True)
    execute.add_argument('--label', default='')
    execute.add_argument('--model', help='Optional Codex model override')
    execute.add_argument('--sandbox', choices=['read-only', 'workspace-write', 'danger-full-access'], default='workspace-write')
    execute.add_argument('--codex-bin', default='codex', help='Codex executable or test harness')
    execute.add_argument('--no-checks', action='store_true')
    execute.set_defaults(fn=run_codex)
    pack = sp.add_parser('export', help='Write small packet to upload into ChatGPT')
    pack.add_argument('--run', default='latest')
    pack.add_argument('--out')
    pack.add_argument('--overwrite', action='store_true')
    pack.add_argument('--no-context', action='store_true', help='Omit role-projected OKF context')
    pack.set_defaults(fn=export)
    ls = sp.add_parser('list', help='List previous local runs')
    ls.set_defaults(fn=listing)
    diff = sp.add_parser('compare', help='Compare two runs without declaring equivalence')
    diff.add_argument('--baseline', required=True)
    diff.add_argument('--candidate', required=True)
    diff.set_defaults(fn=compare)
    args = p.parse_args(argv)
    try:
        return args.fn(args)
    except (ValueError, FileNotFoundError, PermissionError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
