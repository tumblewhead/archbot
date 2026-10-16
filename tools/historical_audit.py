#!/usr/bin/env python3
"""FR-003: read-only historical source-byte audit, not an acceptance gate.

Git source identity, present worktree correspondence, and reviewer disposition
are separate questions. No shell commands, network requests, or file writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REV = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
SHA1 = re.compile(r"^[0-9a-f]{40}$")
MAX_SOURCE = 2_000_000
MAX_RECEIPT = 2_000_000
MAX_ITEMS = 128

SUPPORTED = {
    "pc-framework-repair-test-evidence/v1":
        ("source_revision", "source_sha256", "source_git_blob_sha1"),
    "pc-framework-repair-review/v1":
        ("reviewed_source_revision", "verified_source_sha256",
         "verified_source_sha1"),
    "pc-verification/v1": ("source_revision", "source_sha256", None),
}


class AuditInputError(ValueError):
    pass


def path_ref(ref):
    """Canonical repository-relative path, never a Git revision expression."""
    if (not isinstance(ref, str) or not ref or len(ref) > 1024 or
            ref.startswith("/") or "\\" in ref or ":" in ref or
            any(ord(c) < 32 or ord(c) == 127 for c in ref) or
            ref != PurePosixPath(ref).as_posix() or
            any(p in ("", ".", "..", ".git") for p in ref.split("/"))):
        raise AuditInputError("Unsafe repository-relative path")
    return ref


def local_file(root, ref, maximum=MAX_RECEIPT):
    path = root / path_ref(ref)
    if path.resolve() != path or not path.is_file() or path.stat().st_size > maximum:
        raise AuditInputError("Missing, aliased or oversized current input: " + ref)
    return path


def unique_pairs(pairs):
    doc = {}
    for key, value in pairs:
        if key in doc:
            raise ValueError("Duplicate JSON key: " + key)
        doc[key] = value
    return doc


def load_json(root, ref):
    raw = local_file(root, ref).read_bytes()
    try:
        obj = json.loads(
            raw.decode("utf-8"), object_pairs_hook=unique_pairs,
            parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)),
        )
    except (ValueError, UnicodeError) as exc:
        raise AuditInputError("Invalid JSON input: " + ref) from exc
    if not isinstance(obj, dict):
        raise AuditInputError("Receipt must be a JSON object")
    return obj, hashlib.sha256(raw).hexdigest()


def git(root, *args):
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), *args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=False, timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise AuditInputError("Historical Git lookup unavailable") from exc
    if proc.returncode:
        raise AuditInputError("Historical Git object unavailable")
    return proc.stdout


def historical_blob(root, revision, ref):
    """Return bounded regular-file bytes at exact commit/path, no symlinks."""
    if git(root, "cat-file", "-t", revision).strip() != b"commit":
        raise AuditInputError("Historical revision is not a commit")
    rows = git(root, "ls-tree", "-r", "-z", revision, "--", ref).split(b"\0")
    matches = []
    for line in rows:
        if not line:
            continue
        try:
            meta, item_path = line.split(b"\t", 1)
            mode, kind, oid = meta.split(b" ")
        except ValueError as exc:
            raise AuditInputError("Invalid historical tree entry") from exc
        if item_path == ref.encode("utf-8"):
            matches.append((mode, kind, oid))
    if len(matches) != 1:
        raise AuditInputError("Historical source path missing or ambiguous")
    mode, kind, oid = matches[0]
    if mode not in (b"100644", b"100755") or kind != b"blob":
        raise AuditInputError("Historical source is not a regular file")
    size = git(root, "cat-file", "-s", oid.decode("ascii")).strip()
    if not size.isdigit() or int(size) > MAX_SOURCE:
        raise AuditInputError("Historical source exceeds bounded reader limit")
    raw = git(root, "cat-file", "blob", oid.decode("ascii"))
    if len(raw) != int(size):
        raise AuditInputError("Historical blob length disagrees with Git")
    return raw


def git_blob_sha1(raw):
    header = b"blob " + str(len(raw)).encode("ascii") + b"\0"
    return hashlib.sha1(header + raw).hexdigest()


def not_resolved(message, receipt_ref, *, revision=None):
    return {
        "schema": "pc-historical-source-audit/v1",
        "historical_status": "UNRESOLVED",
        "source_revision": revision,
        "receipt": receipt_ref,
        "evidence_class": "SOURCE_BYTE_CORRESPONDENCE_ONLY",
        "reason": message,
        "items": [],
        "current_correspondence": {"status": "NOT_CHECKED", "items": []},
        "present_applicability": "NOT_EVALUATED",
        "authoring_review_state": None,
        "review_overlay": {"status": "NOT_CHECKED"},
        "product_verified": False,
        "authority_changed": False,
    }


def overlay(root, ref, receipt_path, revision):
    if ref is None:
        return {"status": "NOT_CHECKED"}
    try:
        doc, digest = load_json(root, ref)
        if doc.get("schema") != "pc-framework-repair-review/v1":
            raise AuditInputError("Unsupported independent review schema")
        if (doc.get("submitted_evidence_path") != receipt_path or
                doc.get("reviewed_source_revision") != revision):
            raise AuditInputError("Independent review does not match source receipt")
        if doc.get("disposition") not in (
                "ACCEPT", "ACCEPT_WITH_CLARIFICATIONS", "REVISE", "UNRESOLVED"):
            raise AuditInputError("Independent review has no supported disposition")
        return {
            "status": "LINKED_REVIEW_REPORTED",
            "path": ref,
            "sha256": digest,
            "disposition": doc["disposition"],
            "disposition_scope": doc.get("disposition_scope"),
            "independent_of_authoring_invocation":
                doc.get("independent_of_authoring_invocation"),
            "note": "Linked review is reported separately, not validated as acceptance",
        }
    except AuditInputError as exc:
        return {"status": "UNRESOLVED", "reason": str(exc)}


def inspect(root, receipt_ref, *, revision=None, check_current=False, review_ref=None):
    """Audit only declared historical source bytes. No authoritative promotion."""
    root = Path(root).resolve()
    try:
        path_ref(receipt_ref)
        if review_ref is not None:
            path_ref(review_ref)
        receipt, receipt_sha = load_json(root, receipt_ref)
        spec = SUPPORTED.get(receipt.get("schema"))
        if spec is None:
            raise AuditInputError("Unsupported historical receipt schema")
        rev_key, digest_key, blob_key = spec
        source_revision = receipt.get(rev_key)
        if not isinstance(source_revision, str) or not REV.fullmatch(source_revision):
            raise AuditInputError("Receipt lacks exact source-time Git revision")
        if revision is not None and (not REV.fullmatch(revision) or
                                     revision != source_revision):
            raise AuditInputError("Requested revision conflicts with source receipt")
        pins = receipt.get(digest_key)
        if not isinstance(pins, dict) or not 0 < len(pins) <= MAX_ITEMS:
            raise AuditInputError("Missing or unbounded source SHA-256 mapping")
        blobs = receipt.get(blob_key, {}) if blob_key else {}
        if blobs is None:
            blobs = {}
        if not isinstance(blobs, dict) or not set(blobs).issubset(pins):
            raise AuditInputError("Malformed optional Git blob SHA-1 mapping")
        for ref, expected in pins.items():
            path_ref(ref)
            if not isinstance(expected, str) or not SHA256.fullmatch(expected):
                raise AuditInputError("Malformed declared source SHA-256")
        for expected in blobs.values():
            if not isinstance(expected, str) or not SHA1.fullmatch(expected):
                raise AuditInputError("Malformed declared Git blob SHA-1")
    except AuditInputError as exc:
        result = not_resolved(str(exc), receipt_ref, revision=revision)
        return result

    result = not_resolved("", receipt_ref, revision=source_revision)
    result["receipt_sha256"] = receipt_sha
    result["receipt_schema"] = receipt["schema"]
    result["authoring_review_state"] = receipt.get("review_state")
    result["review_overlay"] = overlay(root, review_ref, receipt_ref, source_revision)
    unknown = False
    mismatch = False
    current_unknown = False
    current_different = False
    current_rows = []
    for ref, expected in sorted(pins.items()):
        item = {"path": ref, "expected_sha256": expected,
                "expected_git_blob_sha1": blobs.get(ref)}
        try:
            raw = historical_blob(root, source_revision, ref)
            sha = hashlib.sha256(raw).hexdigest()
            blob = git_blob_sha1(raw)
            item.update(historical_sha256=sha, historical_git_blob_sha1=blob,
                        size_bytes=len(raw))
            good = sha == expected and (ref not in blobs or blob == blobs[ref])
            item["status"] = "MATCH" if good else "MISMATCH"
            mismatch |= not good
        except AuditInputError as exc:
            item.update(status="UNRESOLVED", reason=str(exc))
            unknown = True
        result["items"].append(item)

        if check_current:
            present = {"path": ref}
            try:
                raw_now = local_file(root, ref, MAX_SOURCE).read_bytes()
                present["sha256"] = hashlib.sha256(raw_now).hexdigest()
                present["status"] = (
                    "MATCH" if present["sha256"] == expected else "DIFFERENT")
                current_different |= present["status"] == "DIFFERENT"
            except AuditInputError as exc:
                present.update(status="UNRESOLVED", reason=str(exc))
                current_unknown = True
            current_rows.append(present)
    if unknown:
        result["historical_status"] = "UNRESOLVED"
        result["reason"] = "At least one historical source cannot be resolved"
    elif mismatch:
        result["historical_status"] = "HISTORICAL_MISMATCH"
        result["reason"] = "At least one original source digest differs"
    else:
        result["historical_status"] = "HISTORICAL_MATCH"
        result.pop("reason")
    if check_current:
        result["current_correspondence"] = {
            "status": ("UNRESOLVED" if current_unknown else
                       "DIFFERENT" if current_different else "ALL_MATCH"),
            "items": current_rows,
        }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inspect",))
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--revision")
    parser.add_argument("--check-current", action="store_true")
    parser.add_argument("--review")
    args = parser.parse_args(argv)
    report = inspect(ROOT, args.receipt, revision=args.revision,
                     check_current=args.check_current, review_ref=args.review)
    print(json.dumps(report, indent=2, sort_keys=True))
    return {"HISTORICAL_MATCH": 0, "HISTORICAL_MISMATCH": 2,
            "UNRESOLVED": 3}[report["historical_status"]]


if __name__ == "__main__":
    raise SystemExit(main())
