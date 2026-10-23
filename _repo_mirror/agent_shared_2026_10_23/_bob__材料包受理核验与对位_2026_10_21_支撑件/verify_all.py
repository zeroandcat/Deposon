# -*- coding: utf-8 -*-
import hashlib, os, re, json, sys

EXTRACT = "/home/z/my-project/shared/鲍勃_deliverable_pack_v2解开_2026_10_21"
MANIFEST = os.path.join(EXTRACT, "_deliverable_pack_v2_manifest_2026_10_21.md")
UPLOAD_MANIFEST = "/home/z/my-project/upload/6ad87e67ff367d3e299816c9__deliverable_pack_v2_manifest_2026_10_21.md"
SELFEXTRACT = "/home/z/my-project/upload/6ad87e54ff367d3e29981668__deliverable_pack_v2_selfextract_2026_10_21.py"

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

# ---- 1. walk extracted dir ----
entries = {}
for root, dirs, files in os.walk(EXTRACT):
    for fn in files:
        full = os.path.join(root, fn)
        rel = os.path.relpath(full, EXTRACT).replace(os.sep, "/")
        entries[rel] = os.path.getsize(full)
print("extracted files:", len(entries))

# ---- 2. parse INDEX from selfextract script ----
idx = {}
with open(SELFEXTRACT, "r", encoding="utf-8") as f:
    src = f.read()
m = re.search(r"INDEX = \{(.*?)\n\}\n", src, re.S)
for line in re.findall(r'"((?:[^"\\]|\\.)*)": \("([0-9a-f]{64})", (\d+)\)', m.group(1)):
    name = line[0].encode().decode("unicode_escape") if "\\u" in line[0] else line[0]
    idx[name] = (line[1], int(line[2]))
print("INDEX entries:", len(idx))

# ---- 3. parse manifest §4 table (92 payload) ----
man_rows = {}
with open(MANIFEST, "r", encoding="utf-8") as f:
    md = f.read()
# §4 rows: | # | path | orig | SHA-12 | bytes | lines | mtime | note |
pat = re.compile(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`[^`]*`\s*\|\s*`([0-9a-f]{12})`\s*\|\s*([\d,]+)\s*\|", re.M)
sec4 = md.split("## §4")[1].split("### §4-1")[0]
for num, path, sha12, byt in pat.findall(sec4):
    man_rows[path] = (sha12, int(byt.replace(",", "")))
print("manifest §4 rows:", len(man_rows))
# §2-1 rows (2 items, same format)
sec21 = md.split("### §2-1")[1].split("### §2-2")[0]
for num, path, sha12, byt in pat.findall(sec21):
    man_rows[path] = (sha12, int(byt.replace(",", "")))
print("manifest §4+§2-1 unique rows:", len(man_rows))

# ---- 4. verify each extracted entry vs INDEX and manifest ----
results = []
mismatch = 0
for rel in sorted(entries):
    full = os.path.join(EXTRACT, rel)
    actual_sha = sha256_file(full)
    actual_b = entries[rel]
    idx_hit = idx.get(rel)
    idx_ok = (idx_hit is not None and idx_hit[0] == actual_sha and idx_hit[1] == actual_b)
    man_hit = man_rows.get(rel)
    man_ok = None
    if rel == "_deliverable_pack_v2_manifest_2026_10_21.md":
        # manifest 自身不在 §4/§2-1；指纹以 INDEX + upload 实测对
        man_ok = "SELF"
    elif man_hit is not None:
        man_ok = (man_hit[0] == actual_sha[:12] and man_hit[1] == actual_b)
    results.append({
        "rel": rel, "bytes": actual_b, "sha12": actual_sha[:12], "sha256": actual_sha,
        "idx_ok": idx_ok, "manifest_ok": man_ok,
    })
    if not idx_ok or man_ok is False:
        mismatch += 1
        print("MISMATCH:", rel, "idx_ok=", idx_ok, "manifest_ok=", man_ok)

# manifest 件指纹两源对（INDEX vs 解包实测 vs upload 原件实测）
man_full = os.path.join(EXTRACT, "_deliverable_pack_v2_manifest_2026_10_21.md")
man_extracted_sha = sha256_file(man_full)
man_upload_sha = sha256_file(UPLOAD_MANIFEST)
print("manifest extracted sha256:", man_extracted_sha)
print("manifest upload    sha256:", man_upload_sha)
print("manifest two-source equal:", man_extracted_sha == man_upload_sha == idx["_deliverable_pack_v2_manifest_2026_10_21.md"][0])

# ---- 5. archive-entry set vs INDEX set ----
set_ok = set(entries) == set(idx)
print("entry-name sets equal (extracted vs INDEX):", set_ok)

# ---- 6. 包指纹复算（载荷 92 件·0 自指·路径|sha256[:12]|bytes 逐行 LF·Unicode 码点序）----
payload = [r for r in results if r["rel"] != "_deliverable_pack_v2_manifest_2026_10_21.md"]
lines = []
for r in sorted(payload, key=lambda x: [ord(c) for c in x["rel"]]):
    lines.append("%s|%s|%d" % (r["rel"], r["sha12"], r["bytes"]))
canon = ("\n".join(lines) + "\n").encode("utf-8")
pack_fp = hashlib.sha256(canon).hexdigest()
print("payload count for pack fp:", len(payload))
print("recomputed PACK_SHA256:", pack_fp)
print("declared  PACK_SHA256: 45930381276adc5dc6f4434b201527b69171a66064fccaa4592c63c309f6bb2f")
print("PACK_FP match:", pack_fp == "45930381276adc5dc6f4434b201527b69171a66064fccaa4592c63c309f6bb2f")

# ---- 7. 载荷总字节 ----
payload_bytes_sum = sum(r["bytes"] for r in payload)
print("payload bytes sum (92):", payload_bytes_sum, "declared 2,385,602 ->", payload_bytes_sum == 2385602)

# ---- 8. JPEG 结构核验 ----
jpg = os.path.join(EXTRACT, "G-30-a_脑图_AI应当如何思考_从仿生向到仿物理向_2026_10_21.jpg")
with open(jpg, "rb") as f:
    jb = f.read()
magic = jb[:4].hex()
eoi = jb[-2:].hex()
print("JPEG magic:", magic, "(declared ffd8ffe0)")
print("JPEG EOI  :", eoi, "(declared ffd9)")
# SOF0/SOF2 marker scan
sof_info = None
i = 2
while i < len(jb) - 1:
    if jb[i] == 0xFF and jb[i+1] in (0xC0, 0xC1, 0xC2):
        h = (jb[i+5] << 8) | jb[i+6]
        w = (jb[i+7] << 8) | jb[i+8]
        sof_info = ("SOF%d" % (jb[i+1] - 0xC0), w, h)
        break
    elif jb[i] == 0xFF and jb[i+1] not in (0xD8, 0x00) and 0xD0 <= jb[i+1] <= 0xD9:
        i += 2
        continue
    elif jb[i] == 0xFF:
        seglen = (jb[i+2] << 8) | jb[i+3]
        i += 2 + seglen
    else:
        i += 1
print("JPEG SOF:", sof_info, "(declared 1596x1280)")

# ---- save full table ----
out = {"results": results, "pack_fp": pack_fp, "payload_bytes_sum": payload_bytes_sum,
       "jpg": {"magic": magic, "eoi": eoi, "sof": sof_info},
       "manifest_sha256": man_extracted_sha, "entry_set_ok": set_ok, "mismatch": mismatch}
with open("/home/z/my-project/agents/6a962cc259312f271f3f1e73/pack_v2_check/verify_all_result.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("TOTAL mismatch:", mismatch, "/ 93")
