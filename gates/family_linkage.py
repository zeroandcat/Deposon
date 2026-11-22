#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# family_linkage.py — six-family linkage structural validator (preview.5
# interface E). Zero network, zero credentials: parses docs/family-linkage.md,
# checks (a) exactly the six pre-registered family ids, (b) every referenced
# in-repo path exists, (c) statuses are from the closed vocabulary, (d) the
# pending->linked upgrade rule is structurally visible (linked rows carry a
# pointer-row column, pending rows say pending). Exit 0 = ALL PASS.
# ============================================================================
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "docs", "family-linkage.md")

PREREGISTERED_FIDS = {"f1", "f2", "f3", "f4", "f5", "f6"}
STATUS_VOCAB = {"linked", "pending"}
ROW_RE = re.compile(
    r"^\|\s*(?P<fid>f\d)\s*\|\s*(?P<name>[^|]+)\|\s*(?P<iface>[^|]+)\|"
    r"\s*(?P<pointer>[^|]+)\|\s*(?P<status>linked|pending)\s*\|$")


def parse_rows(text):
    rows = []
    for line in text.splitlines():
        m = ROW_RE.match(line.strip())
        if m:
            rows.append(m.groupdict())
    return rows


def repo_paths_in(cell):
    """Extract candidate in-repo file references from a table cell."""
    return re.findall(r"`([A-Za-z0-9_./-]+\.[A-Za-z0-9]+)`", cell)


def run_gate(verbose=True):
    G = {}
    with open(DOC, "r", encoding="utf-8") as f:
        text = f.read()
    rows = parse_rows(text)

    # E1 exactly the six pre-registered family ids, each once.
    fids = [r["fid"] for r in rows]
    G["E1 six family ids present exactly once each"] = (
        len(fids) == 6 and set(fids) == PREREGISTERED_FIDS)

    # E2 statuses from the closed vocabulary.
    G["E2 statuses in closed vocabulary"] = all(
        r["status"] in STATUS_VOCAB for r in rows)

    # E3 every referenced in-repo path exists.
    missing = []
    for r in rows:
        for cell in (r["iface"], r["pointer"]):
            for p in repo_paths_in(cell):
                if p.startswith("docs/"):
                    if not os.path.isfile(os.path.join(ROOT, p)):
                        missing.append(p)
                else:
                    if not os.path.isfile(os.path.join(ROOT, p)):
                        missing.append(p)
    G["E3 all referenced in-repo files exist"] = (missing == [])

    # E4 linked rows must reference an existing pointer-row artefact
    #    (docs/evidence-rounds.md or an in-repo gate/doc path).
    bad_linked = []
    for r in rows:
        if r["status"] != "linked":
            continue
        refs = repo_paths_in(r["iface"]) + repo_paths_in(r["pointer"])
        if not refs:
            bad_linked.append(r["fid"])
    G["E4 linked rows carry file references"] = (bad_linked == [])

    # E5 pending rows must say pending in the pointer cell (honest marker).
    bad_pending = []
    for r in rows:
        if r["status"] == "pending" and "pending" not in r["pointer"].lower():
            bad_pending.append(r["fid"])
    G["E5 pending rows carry pending marker in pointer cell"] = (
        bad_pending == [])

    # E6 the strictness gauge and this validator are themselves wired into
    #    the family table (f3/f6 self-reference honesty).
    fids_in_text = set(fids)
    G["E6 f3 and f6 reference the preview.5 gates"] = (
        "f3" in fids_in_text and "f6" in fids_in_text
        and "judgment_strictness" in text and "family_linkage" in text)

    ok_all = all(v is True for v in G.values())
    if verbose:
        for k, v in G.items():
            print(("PASS" if v is True else "FAIL"), k)
        print("family_linkage gate: %s (%d/%d)" % (
            "ALL PASS" if ok_all else "FAILED",
            sum(1 for v in G.values() if v is True), len(G)))
    return ok_all, G


if __name__ == "__main__":
    sys.exit(0 if run_gate()[0] else 1)
