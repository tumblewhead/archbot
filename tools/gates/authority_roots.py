"""Engine-owned trust roots for explicitly reviewed AP gate authorities.

Unlike candidate bindings, this registry is part of the reviewed engine
source. A new project cannot grant itself authority by rehashing its files.
Adding or changing a root requires a separately authorized source revision
and independent review. These source pins are *not* digital signatures,
and do not prove authenticity if the engine itself is replaced.
"""
from __future__ import annotations

_TRUSTED = {
    "AS-001": {
        "project_id": "AS-001",
        "spine": "/architecture/AS-001/spine.md",
        "stage": "AP",
        "protected_requirements": [
            "C-002"
        ],
        "accepted_validator": {
            "id": "TOY1_C002_CHARGED_SRAM",
            "requirement": "C-002",
            "scope": {
                "path": "process/decisions/C-002-scope.yaml",
                "git_blob_sha1": "91b2bef7e01e2e96579bd46ab9acbcd5c2f55217"
            },
            "implementation": {
                "path": "tools/gates/toy1_c002.py",
                "git_blob_sha1": "18ae2486bc62dca3d6ee9046c602d2ceb859c06c"
            }
        },
        "sources": {
            "spine_source": {
                "path": "knowledge/architecture/AS-001/spine.md",
                "git_blob_sha1": "f5f39f48c69a8e6017ad7d93a2aeae88575eaf7c"
            },
            "active_baseline": {
                "path": "process/baselines/AS-001-v2-active.yaml",
                "git_blob_sha1": "a2b470a806c9970ff06e5eb4f309cf97b656a108"
            },
            "baseline_review": {
                "path": "reviews/gates/TOY1-BASELINE002-independent-review.json",
                "git_blob_sha1": "8e07069f9d9c8627c17f96f366f5df55ad071988"
            },
            "policy": {
                "path": "process/policies/AP_SELECTION_v2.yaml",
                "git_blob_sha1": "0419a6951b8e3e713c174cc19339145decc3c260"
            },
            "vo_ledger": {
                "path": "process/ledgers/vo_ledger-AS-001-v2-active.yaml",
                "git_blob_sha1": "a19cafd1fdccaaa363ef493d22e5a282cea29d02"
            },
            "ad_ledger": {
                "path": "process/ledgers/ad_ledger.yaml",
                "git_blob_sha1": "e375786bac3216567c672b44cde1d246e446165a"
            },
            "approved_ap_authority": {
                "path": "process/decisions/AP-002-AS-V2-RECONFIRMATION-001.yaml",
                "git_blob_sha1": "8cacc4e5d5f9ba5afea270166d528302404a41fe"
            },
            "reviewed_as": {
                "path": "reviews/gates/TOY1-AS002-independent-review-v3.json",
                "git_blob_sha1": "d026f227efead5134597b7f088a43726a3b268c1"
            }
        }
    }
}

# Copy-on-load callers never receive a mutable reference to this data.
def trusted_root(project_id: str):
    """Return a detached trusted project anchor, or fail closed."""
    import copy
    record = _TRUSTED.get(project_id)
    if record is None:
        raise ValueError('Untrusted project authority root: ' + str(project_id))
    return copy.deepcopy(record)
