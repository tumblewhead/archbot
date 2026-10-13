#!/usr/bin/env python3
"""Idempotently attach the process spine without replacing the user's evolving AS spine."""
from pathlib import Path
import sys
import yaml
ROOT = Path(__file__).resolve().parents[1]
SPINE = ROOT / 'knowledge/architecture/AS-001/spine.md'
TARGET = '/architecture/AS-001/decisions/PC-002-spine.md'


def main():
    text = SPINE.read_text(encoding='utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise SystemExit('Spine is not YAML-frontmatter Markdown')
    _, header, body = text.split('---\n', 2)
    data = yaml.safe_load(header)
    rels = data.setdefault('relations', [])
    if not any(edge.get('kind') == 'specifies' and edge.get('target') == TARGET for edge in rels):
        rels.append({'kind': 'specifies', 'target': TARGET})
        SPINE.write_text('---\n' + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + '---\n' + body, encoding='utf-8')
        print('Attached process spine')
    else:
        print('Process spine already attached')
    return 0


if __name__ == '__main__':
    sys.exit(main())
