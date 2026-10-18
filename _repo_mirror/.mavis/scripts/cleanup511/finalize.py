# -*- coding: utf-8 -*-
"""Finalize the execution list: four-channel clean set + rule-4 __pycache__ + rule-5 empty dirs.

Emits .mavis/scripts/cleanup511/exec_list.json  (kept OUT of .tmp so it can never be
mistaken for a deletion candidate).
"""
import io, os, json, hashlib

REPO = r"_repo_mirror"
MAN  = os.path.join(REPO, ".tmp", "cleanup511_manifest_2026_10_17.json")
OUT  = os.path.join(REPO, ".mavis", "scripts", "cleanup511", "exec_list.json")
EMPTY_SHA = hashlib.sha256(b"").hexdigest()

m = json.load(io.open(MAN, encoding="utf-8"))

# ---- Cat 1: four-channel clean set from the manifest, plus the Channel-D empty-hash fix ----
cat1, seen = [], set()
for c in m["clean"]:
    cat1.append({"abs": c["abs"], "rel": c["rel"], "bytes": c["bytes"],
                 "sha12": c["sha12"], "cat": "C1_fourchannel"})
    seen.add(os.path.normcase(c["abs"]))

d_fix = []
for h in m["held"]:
    if (h["bytes"] == 0 and h["blocked_channels"] == ["D"]
            and h["sha12"] == EMPTY_SHA[:12] and "R3_sameday" not in h["excl"]):
        d_fix.append({"abs": h["abs"], "rel": h["rel"], "bytes": h["bytes"],
                      "sha12": h["sha12"], "cat": "C1_Dfix_zerobyte"})
if d_fix:
    cat1 += d_fix
    for d in d_fix:
        seen.add(os.path.normcase(d["abs"]))

# ---- Cat 4: rule-4 __pycache__ .pyc not already in Cat 1 ----
cat4 = []
for dp, dns, fns in os.walk(REPO, followlinks=False):
    dn = os.path.normcase(dp)
    if os.path.basename(dp) != "__pycache__":
        continue
    if not dn.startswith(os.path.normcase(os.path.join(REPO, ".tmp")) + os.sep) and \
       not dn.startswith(os.path.normcase(os.path.join(REPO, "results")) + os.sep):
        continue
    for fn in fns:
        p = os.path.join(dp, fn)
        if os.path.normcase(p) in seen:
            continue
        h = hashlib.sha256()
        with open(p, "rb") as f:
            for b in iter(lambda: f.read(1 << 20), b""):
                h.update(b)
        cat4.append({"abs": p, "rel": os.path.relpath(p, REPO).replace("\\", "/"),
                     "bytes": os.path.getsize(p), "sha12": h.hexdigest()[:12],
                     "cat": "C4_pycache"})
        seen.add(os.path.normcase(p))

# ---- Cat 5: rule-5 empty dirs ----
cat5 = []
for d in (r".tmp\numaudit_20261013", r"results\_archive_2026_09_20", r"results\_archive_2026_09_21"):
    p = os.path.join(REPO, d)
    if os.path.isdir(p) and not os.listdir(p):
        cat5.append({"abs": p, "rel": d.replace("\\", "/"), "bytes": 0,
                     "sha12": "(empty-dir)", "cat": "C5_emptydir"})

files = cat1 + cat4
missing = [f["abs"] for f in files if not os.path.isfile(f["abs"])]

out = {
    "meta": {
        "rod": "CLEANUP-EXEC-511",
        "built": __import__("time").strftime("%Y-%m-%d %H:%M:%S"),
        "manifest_clean_strict": m["meta"]["clean_count"],
        "cat1_total": len(cat1),
        "cat1_dfix": len(d_fix),
        "cat4_pycache_extra": len(cat4),
        "cat5_emptydirs": len(cat5),
        "files_total": len(files),
        "bytes_total": sum(f["bytes"] for f in files),
        "missing_at_build": missing,
        "manifest_clean_day_layers": m["meta"]["clean_day_layers"],
    },
    "files": files,
    "dirs": cat5,
}
with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(out, ensure_ascii=False, indent=1))
print(json.dumps(out["meta"], ensure_ascii=False, indent=1))
print("\nCat4 extras:", json.dumps([f["rel"] for f in cat4], ensure_ascii=False))
print("Cat5 dirs  :", json.dumps([d["rel"] for d in cat5], ensure_ascii=False))
