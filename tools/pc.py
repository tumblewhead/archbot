#!/usr/bin/env python3
"""Small OKF v0.2 spine explorer for the Progressive Concretization demo.

Checks are structural; they do not verify proofs, physical evidence, or requirements.
"""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
import hashlib
import json
from pathlib import Path
import re
import sys

try:
    import yaml
except ModuleNotFoundError:
    raise SystemExit("PyYAML missing. Run: python -m pip install -r requirements.txt")

REPO = Path(__file__).resolve().parents[1]
KB = REPO / "knowledge"
URL_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.I)
FOOTNOTE_REF_RE = re.compile(r"\[\^([\w-]+)\](?!:)")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def load_yaml(path: Path) -> dict:
    result = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict):
        raise ValueError(f"Expected YAML mapping: {path}")
    return result


def read_concept(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise ValueError(f"Missing opening YAML frontmatter: {path}")
    parts = content.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError(f"Missing closing YAML frontmatter: {path}")
    meta = yaml.safe_load(parts[0][4:])
    if not isinstance(meta, dict):
        raise ValueError(f"Frontmatter must be mapping: {path}")
    return meta, parts[1]


def resolve_target(source: Path, target: str) -> Path | None:
    """Resolve only local bundle resources. Refuse path escapes, even via symlinks."""
    if not isinstance(target, str) or not target.strip():
        raise ValueError(f"Invalid target in {source}: {target!r}")
    if URL_RE.match(target) or target.startswith(('mailto:', '#')):
        return None
    # Query/fragment suffixes are not meaningful in local file checking.
    target = target.split('#', 1)[0].split('?', 1)[0]
    base = KB if target.startswith('/') else source.parent
    resolved = (base / target.lstrip('/')).resolve()
    if not resolved.is_relative_to(KB.resolve()):
        raise ValueError(f"Target escapes knowledge bundle: {target} from {source}")
    return resolved


def rels(meta: dict) -> list[dict]:
    value = meta.get('relations', [])
    if not isinstance(value, list):
        raise ValueError('relations must be a list')
    for edge in value:
        if not isinstance(edge, dict) or not isinstance(edge.get('kind'), str) or not isinstance(edge.get('target'), str):
            raise ValueError(f"Invalid relation: {edge!r}")
    return value


def catalog() -> dict[Path, tuple[dict, str]]:
    result = {}
    for path in sorted(KB.rglob('*.md')):
        if path.name == 'index.md':
            continue  # OKF index files need not have frontmatter.
        result[path.resolve()] = read_concept(path)
    return result


def check(*, hash_raw: bool = True) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    vocab = set(load_yaml(REPO / 'process/relationships.yaml')['relations'])
    try:
        concepts = catalog()
    except (ValueError, yaml.YAMLError, UnicodeError) as ex:
        print('ERROR:', ex)
        return 1
    seen_ids: dict[str, Path] = {}
    links_checked = 0
    raw_checked = 0
    root_index = KB / 'index.md'
    if not root_index.exists():
        errors.append('Missing knowledge/index.md')
    else:
        try:
            root_meta, _ = read_concept(root_index)
            if str(root_meta.get('okf_version')) != '0.2':
                errors.append('Bundle index must set okf_version: "0.2"')
        except (ValueError, yaml.YAMLError) as ex:
            errors.append(str(ex))
    for path, (meta, body) in concepts.items():
        name = path.relative_to(KB)
        if not isinstance(meta.get('type'), str) or not meta['type'].strip():
            errors.append(f'{name}: missing required OKF type')
        if meta.get('status', 'stable') not in ('draft', 'stable', 'deprecated'):
            errors.append(f'{name}: invalid OKF lifecycle status')
        ident = meta.get('id')
        if ident:
            if not isinstance(ident, str):
                errors.append(f'{name}: id must be string')
            elif ident in seen_ids:
                errors.append(f'{name}: duplicate id {ident} also in {seen_ids[ident]}')
            else:
                seen_ids[ident] = path
        try:
            edges = rels(meta)
        except ValueError as ex:
            errors.append(f'{name}: {ex}')
            edges = []
        for edge in edges:
            if edge['kind'] not in vocab:
                errors.append(f'{name}: undefined relation kind {edge["kind"]}')
            try:
                target = resolve_target(path, edge['target'])
                if target is None or not target.is_file():
                    errors.append(f'{name}: broken typed edge {edge["kind"]} -> {edge["target"]}')
                else:
                    links_checked += 1
            except ValueError as ex:
                errors.append(f'{name}: {ex}')
        sources = meta.get('sources', [])
        if not isinstance(sources, list):
            errors.append(f'{name}: sources must be a list')
            sources = []
        source_ids = set()
        for source in sources:
            if not isinstance(source, dict) or not isinstance(source.get('resource'), str):
                errors.append(f'{name}: invalid OKF source entry')
                continue
            if source.get('id'):
                source_ids.add(source['id'])
            try:
                if source['resource'].startswith(('/', './', '../')):
                    target = resolve_target(path, source['resource'])
                    if target is not None and not target.is_file():
                        errors.append(f'{name}: missing local source {source["resource"]}')
            except ValueError as ex:
                errors.append(f'{name}: {ex}')
        for key in FOOTNOTE_REF_RE.findall(body):
            if key not in source_ids:
                errors.append(f'{name}: claim footnote [^{key}] lacks matching sources[].id')
        for match in MD_LINK_RE.finditer(body):
            link = match.group(1).split(' ', 1)[0]
            try:
                target = resolve_target(path, link)
                if target is not None and not target.is_file():
                    warnings.append(f'{name}: unresolved Markdown link {link}')
            except ValueError as ex:
                errors.append(f'{name}: {ex}')
    # The single deliberately large fixture has an independently checkable manifest.
    manifest_file = KB / 'architecture/AS-001/evidence/manifest.json'
    if manifest_file.exists():
        try:
            manifest = json.loads(manifest_file.read_text(encoding='utf-8'))
            dataset = resolve_target(manifest_file, manifest['dataset'])
            if dataset is None or not dataset.is_file():
                errors.append('Manifest dataset not found')
            else:
                dataset_bytes = dataset.stat().st_size
                if dataset_bytes != manifest['byte_count']:
                    errors.append('Raw dataset length does not match manifest')
                if hash_raw:
                    digest = hashlib.sha256()
                    with dataset.open('rb') as handle:
                        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
                            raw_checked += len(chunk)
                            digest.update(chunk)
                    if digest.hexdigest() != manifest['sha256']:
                        errors.append('Raw dataset SHA256 does not match manifest')
        except (ValueError, KeyError, OSError, json.JSONDecodeError) as ex:
            errors.append(f'Invalid raw dataset manifest: {ex}')
    for problem in warnings:
        print('WARNING:', problem)
    for problem in errors:
        print('ERROR:', problem)
    print(f'CHECK: {len(concepts)} concepts, {links_checked} typed links, '
          f'{raw_checked} raw bytes hashed, {len(warnings)} warnings, {len(errors)} errors')
    if not hash_raw:
        print('RAW HASH SKIPPED (manifest file size checked; SHA-256 not checked)')
    if not errors:
        print('STRUCTURE PASS (not a proof, gate approval, or empirical validation)')
    return 1 if errors else 0


def traverse(start: Path, allowed: set[str], max_depth: int, mandatory: set[str],
             concepts: dict[Path, tuple[dict, str]]) -> list[tuple[Path, int, str]]:
    queue = deque([(start, 0, 'root')])
    visited: set[Path] = set()
    output: list[tuple[Path, int, str]] = []
    while queue:
        path, depth, via = queue.popleft()
        if path in visited:
            continue
        visited.add(path)
        output.append((path, depth, via))
        if path not in concepts:
            continue
        for edge in rels(concepts[path][0]):
            kind = edge['kind']
            # Optional edges obey max_depth; mandatory obligations close regardless of depth.
            if kind not in mandatory and (depth >= max_depth or kind not in allowed):
                continue
            dest = resolve_target(path, edge['target'])
            if dest is not None and dest.is_file() and dest not in visited:
                queue.append((dest, depth+1, kind + (' [required]' if kind in mandatory and kind not in allowed else '')))
    return output


def view(args: argparse.Namespace) -> int:
    views = load_yaml(REPO / 'process/views.yaml')
    role = views['roles'].get(args.role)
    if role is None:
        print(f'Unknown role: {args.role}. Choose: {", ".join(views["roles"])}', file=sys.stderr)
        return 2
    try:
        root = resolve_target(KB / 'index.md', args.spine)
        if root is None or not root.is_file() or not root.name.endswith('.md'):
            raise ValueError('spine not found or not a Markdown concept')
        concepts = catalog()
        allowed = set(args.follow.split(',')) if args.follow else set(role['follow'])
        known = set(load_yaml(REPO / 'process/relationships.yaml')['relations'])
        if not allowed.issubset(known):
            raise ValueError(f'Unknown relation kinds: {sorted(allowed-known)}')
        mandatory = set(views.get('mandatory_closure', []))
        nodes = traverse(root, allowed, int(role['max_depth']), mandatory, concepts)
    except (ValueError, yaml.YAMLError) as ex:
        print('ERROR:', ex, file=sys.stderr)
        return 2
    budget = int(args.max_bytes or role['max_bytes'])
    print(f'ROLE={args.role} SPINE={args.spine} DEPTH={role["max_depth"]} '
          f'BODY_BYTE_BUDGET={budget} EMIT={args.emit} FOLLOW={",".join(sorted(allowed))}')
    for path, depth, via in nodes:
        size = path.stat().st_size
        kind = concepts[path][0]['type'] if path in concepts else f'NON_OKF:{path.suffix}'
        print(f'{"  "*depth}{path.relative_to(KB)} [{kind}; {size} bytes; via={via}]')
    print(f'SELECTED={len(nodes)} (context selection does not verify evidence)')
    if args.emit:
        remaining = budget
        for path, depth, via in nodes:
            # Explicitly selected binary/raw files may be listed; only text Markdown is emitted.
            if path not in concepts:
                print(f'OMITTED BINARY/NON-CONCEPT: {path.relative_to(KB)}')
                continue
            body_bytes = path.stat().st_size
            if body_bytes > remaining:
                print(f'OMITTED OVER BUDGET: {path.relative_to(KB)} ({body_bytes} bytes)')
                continue
            print(f'\n===== BEGIN {path.relative_to(KB)} =====')
            print(path.read_text(encoding='utf-8'))
            print(f'===== END {path.relative_to(KB)} =====')
            remaining -= body_bytes
        print(f'EMITTED_BUDGET_REMAINING={remaining}')
    return 0


def impact(args: argparse.Namespace) -> int:
    try:
        changed = resolve_target(KB / 'index.md', args.changed)
        if changed is None or not changed.exists():
            raise ValueError('changed path not found')
        concepts = catalog()
        incoming: dict[Path, list[tuple[Path, str]]] = defaultdict(list)
        for src, (meta, _) in concepts.items():
            for edge in rels(meta):
                target = resolve_target(src, edge['target'])
                if target is not None:
                    incoming[target].append((src, edge['kind']))
        queue = deque([(changed, 0, 'changed')])
        seen: set[Path] = set()
        while queue:
            path, depth, cause = queue.popleft()
            if path in seen:
                continue
            seen.add(path)
            print('  '*depth + str(path.relative_to(KB)) + f' ({cause})')
            if depth >= args.max_depth:
                continue
            for src, kind in incoming.get(path, []):
                queue.append((src, depth+1, f'inbound {kind}'))
        print(f'POTENTIALLY AFFECTED={len(seen)-1}; review required, not automatically invalidated')
        return 0
    except (ValueError, yaml.YAMLError) as ex:
        print('ERROR:', ex, file=sys.stderr)
        return 2


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    ch = sub.add_parser('check', help='Structural OKF and project-edge checks; not proof validation')
    ch.add_argument('--fast', action='store_true', help='Skip raw data SHA-256 hashing (size still checked)')
    v = sub.add_parser('view', help='Show selective spine view for a role')
    v.add_argument('--role', required=True)
    v.add_argument('--spine', required=True)
    v.add_argument('--follow', help='Comma-separated relationship allowlist overriding the role view')
    v.add_argument('--emit', action='store_true', help='Print bounded Markdown contents, never raw files')
    v.add_argument('--max-bytes', type=int, help='Override body byte budget')
    i = sub.add_parser('impact', help='Conservative reverse-edge impact report')
    i.add_argument('--changed', required=True)
    i.add_argument('--max-depth', type=int, default=8)
    args = p.parse_args()
    if args.command == 'check':
        return check(hash_raw=not args.fast)
    if args.command == 'view':
        return view(args)
    return impact(args)


if __name__ == '__main__':
    sys.exit(main())
