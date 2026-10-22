# -*- coding: utf-8 -*-
"""Step 4 - recycle-bin record retention audit (all records this task produced)."""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recycle_channel as rc

SID = r"S-1-5-21-1515631758-409240343-2904948024-500"
S2 = r"_repo_mirror/readout/final/step2_sample_verify.json"
S3 = r"_repo_mirror/readout/final/step3_bulk_result.json"
OUT = r"_repo_mirror/readout/final/step4_bin_audit.json"


def main():
    s2 = json.load(io.open(S2, encoding="utf-8"))
    s3 = json.load(io.open(S3, encoding="utf-8"))
    expected = []
    expected.append((s2["i_name"], s2["r_name"], "SAMPLE:" + s2["sample_rel"]))
    for row in s3["rows"]:
        if row.get("i_name"):
            expected.append((row["i_name"], row["r_name"], "FILE:" + row["rel"]))
    for row in s3["dir_rows"]:
        if row.get("i_name"):
            expected.append((row["i_name"], row["r_name"], "DIR:" + row["abs"]))

    binp = rc.sid_bin_dir(SID)
    live = set(os.listdir(binp))
    i_live = [n for n in live if n[:2].upper() == "$I"]
    r_live = [n for n in live if n[:2].upper() == "$R"]
    other = sorted(n for n in live if n[:2].upper() not in ("$I", "$R"))

    missing = []
    for i, r, label in expected:
        mi = i not in live
        mr = r not in live
        if mi or mr:
            missing.append({"label": label, "i_name": i, "r_name": r,
                            "i_missing": mi, "r_missing": mr})

    res = {
        "sid_bin": binp,
        "expected_pairs": len(expected),
        "pairs_complete_in_bin": len(expected) - len(missing),
        "pairs_evicted_or_missing": len(missing),
        "missing_detail": missing[:50],
        "missing_total": len(missing),
        "bin_now_I": len(i_live), "bin_now_R": len(r_live), "bin_other": other,
    }
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
    print("expected pairs = %d | complete = %d | missing = %d"
          % (res["expected_pairs"], res["pairs_complete_in_bin"], res["pairs_evicted_or_missing"]))
    print("bin now: $I=%d $R=%d other=%s" % (len(i_live), len(r_live), other))
    for m in missing[:10]:
        print("  MISSING:", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
