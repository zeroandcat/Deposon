# -*- coding: utf-8 -*-
"""Step 2b - re-judge the ALREADY executed sample against the corrected pairing rule.

No new deletion happens here. The sample file `docwriter_v46_card_raw.txt` was already
sent to the recycle bin by step2_sample.py; this only re-evaluates the $I/$R pair
that was produced, using the corrected pairing key (shared base name after the
$I/$R prefix, since the prefix differs by design).
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recycle_channel as rc

SID = r"S-1-5-21-1515631758-409240343-2904948024-500"
REP = r"_repo_mirror\tools\_archive_purge_2026_10_17\step2_sample_verify.json"


def bin_base(name):
    return name[2:] if name[:2].upper() in ("$I", "$R") else name


def main():
    rep = json.load(io.open(REP, encoding="utf-8"))
    i_name = rep.get("i_name")
    r_name = rep.get("r_name")
    binp = rc.sid_bin_dir(SID)
    live = os.path.isfile(os.path.join(binp, i_name or "$I__none__")) and \
           os.path.isfile(os.path.join(binp, r_name or "$R__none__"))

    old = [c for c in rep["checks"] if c["check"] == "I_R_stem_paired"]
    old_pass = old[0]["pass"] if old else False
    paired = bool(i_name and r_name and bin_base(i_name) == bin_base(r_name))
    report = {
        "rejudge_of": "step2_sample_verify.json",
        "i_name": i_name, "r_name": r_name,
        "pairing_key_I": bin_base(i_name or ""),
        "pairing_key_R": bin_base(r_name or ""),
        "pair_key_equal": paired,
        "records_still_live_in_bin": live,
        "old_check_pass": old_pass,
        "old_check_defect": "os.path.splitext() compares '$I'-prefixed vs '$R'-prefixed names; "
                            "the prefixes differ by design so equality can never hold",
    }
    if old:
        old[0]["pass"] = paired
        old[0]["detail"] = "%s <-> %s (key=%s)" % (i_name, r_name, bin_base(i_name or ""))
    rep["checks_rejudged"] = True
    rep["ok"] = all(c["pass"] for c in rep["checks"])
    rep["verdict"] = "CHANNEL_VERIFIED" if rep["ok"] else "CHANNEL_FAILED_STOP"
    with io.open(REP, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rep, ensure_ascii=False, indent=1, sort_keys=True))
    with io.open(os.path.splitext(REP)[0] + "_rejudge.json", "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(report, ensure_ascii=False, indent=1, sort_keys=True))
    print(json.dumps(report, ensure_ascii=False, indent=1, sort_keys=True))
    print("FINAL VERDICT:", rep["verdict"])
    return 0 if rep["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
