"""Generic continuity of accepted project obligations across AP bindings.

This is a cooperative engineering process check, not a forgery detector.
The accepted projection is separately selected and is not the candidate policy.
"""
from __future__ import annotations


FIELDS = (
    "spine_source", "active_baseline", "baseline_review", "policy",
    "vo_ledger", "ad_ledger", "approved_ap_authority", "reviewed_as",
    "required_validators",
)


def _required_names(items):
    if not isinstance(items, list):
        raise ValueError("Required validators must be a list")
    names = []
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("requirement"), str):
            raise ValueError("Malformed protected validator declaration")
        names.append(item["requirement"])
    if len(names) != len(set(names)):
        raise ValueError("Duplicate protected validator declaration")
    return names


def compare(projection, candidate, transition=None):
    """Return authorized effective binding, never invent a transition.

    Only exact field replacements enumerated in a separately accepted
    transition can change the accepted projection's protected contract.
    """
    if not isinstance(projection, dict) or projection.get("schema") != "pc-project-ap-continuity/v1":
        raise ValueError("Missing accepted project continuity projection")
    if projection.get("status") not in ("candidate_for_independent_review", "accepted_for_trial"):
        raise ValueError("Unrecognized project continuity status")
    for key in ("project_id", "spine", "stage"):
        if not isinstance(projection.get(key), str) or candidate.get(key) != projection[key]:
            raise ValueError("Project continuity identity mismatch: " + key)
    if not projection.get("id"):
        raise ValueError("Project continuity projection has no identity")

    replacements = {}
    if transition is not None:
        if (not isinstance(transition, dict) or
                transition.get("schema") != "pc-project-authority-transition/v1" or
                transition.get("status") != "accepted" or
                transition.get("project_id") != projection["project_id"] or
                transition.get("previous_projection_id") != projection["id"] or
                transition.get("previous_baseline") != projection["active_baseline"]["path"] or
                not transition.get("approved_by") or
                not transition.get("approval_evidence")):
            raise ValueError("Authority transition not approved for this baseline")
        replacements = transition.get("replacements")
        if not isinstance(replacements, dict) or not replacements:
            raise ValueError("Authority transition has no explicit replacements")
        if not set(replacements).issubset(FIELDS):
            raise ValueError("Authority transition changes unsupported contract field")
        if all(projection.get(k) == v for k, v in replacements.items()):
            raise ValueError("Authority transition does not change any obligation")

    for key in FIELDS:
        target = replacements.get(key, projection.get(key))
        if candidate.get(key) != target:
            raise ValueError("Accepted project baseline continuity mismatch: " + key)

    _required_names(projection.get("required_validators"))
    _required_names(candidate.get("required_validators"))
    return candidate
