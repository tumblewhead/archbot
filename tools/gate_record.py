#!/usr/bin/env python3
"""Create a traceable *reported* proof-review disposition, never an automatic approval."""
from __future__ import annotations
import argparse, json, re, sys
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATTERN=re.compile(r'^##\s+Disposition:\s*(ACCEPT_WITH_CLARIFICATIONS|ACCEPT|REVISE|REJECT)\s*$',re.M)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--review', required=True, help='Markdown proof-review artifact relative to repository')
    p.add_argument('--output', default='reviews/gates/proof-PR-002.json')
    a=p.parse_args()
    review=(ROOT/a.review).resolve()
    if not review.is_relative_to(ROOT) or not review.is_file():
        p.error('review missing or outside repository')
    data=review.read_bytes()
    matches=PATTERN.findall(data.decode('utf-8'))
    if len(matches)!=1:
        p.error('review must contain exactly one ## Disposition: ... heading')
    disposition=matches[0]
    record={'schema':'pc.proof-review-disposition.v1',
       'source':str(review.relative_to(ROOT)),
       'source_sha256':sha256(data).hexdigest(),
       'reviewer_reported_disposition':disposition,
       'accepted_scope':'abstract_mathematics_only' if disposition.startswith('ACCEPT') else 'none',
       'implementation_approved':False,'architecture_selected':False,
       'gate_automatically_approved':False,
       'unresolved':['C implementation mapping','input validation','concurrency','WCET','SRAM/flash measurements']}
    dest=(ROOT/a.output).resolve()
    if not dest.is_relative_to(ROOT): p.error('output outside repository')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print('RECORDED:',dest.relative_to(ROOT),'DISPOSITION:',disposition,'GATE: not automatically approved')
    return 0
if __name__=='__main__': sys.exit(main())
