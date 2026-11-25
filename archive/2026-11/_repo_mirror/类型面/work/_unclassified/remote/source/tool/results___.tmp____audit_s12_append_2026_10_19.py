# -*- coding: utf-8 -*-
"""§12 夜链补录 · append-only 追加落盘器
纪律：⛔ 0 回改历史行一字（纯追加）· 0 覆盖 · 0 移动/改名/删除
停手闸：落笔前独立复测基线，不符则停手
自证：落盘后独立亲测（SHA-12/bytes/LF/前缀字节 SHA-256/BOM/CR/末字节）
"""
import io, os, hashlib, time

MEMO = r"_repo_mirror/work/note/_root_session_history_memo_2026_10_14.md"
BODY = r"〔幽灵引用·原件已缺席·未上传:_s12_body_2026_10_19.md〕"

EXP_SHA12 = "fa5145d90fe4"
EXP_BYTES = 215131
EXP_LF = 1755

def sha256(b):
    return hashlib.sha256(b).hexdigest()

# ---------- 停手闸 ----------
b = open(MEMO, "rb").read()
cur_sha = sha256(b)
checks = [
    ("SHA-12", cur_sha[:12], EXP_SHA12),
    ("bytes", len(b), EXP_BYTES),
    ("LF", b.count(b"\n"), EXP_LF),
    ("CR", b.count(b"\r"), 0),
    ("BOM", b[:3] == b"\xef\xbb\xbf", False),
    ("末字节0x0A", b[-1:] == b"\n", True),
]
for name, got, exp in checks:
    if got != exp:
        print("停手闸未过：%s 实测=%r 期望=%r ⇒ 停手，0 落盘" % (name, got, exp))
        raise SystemExit(1)
print("停手闸 ✅ 全部通过（%s）" % time.strftime("%Y-%m-%d %H:%M:%S"))
print("  基线 SHA-12 = %s ｜ bytes = %d ｜ LF = %d ｜ CR = 0 ｜ BOM = False" % (cur_sha[:12], len(b), b.count(b"\n")))

# ---------- 本体检查 ----------
body = open(BODY, "rb").read()
assert body[:3] != b"\xef\xbb\xbf", "本体含 BOM"
assert b"\r" not in body, "本体含 CR"
assert body.endswith(b"\n"), "本体未以 LF 收束"
text = body.decode("utf-8")
assert "§12" in text and len(text) > 20000
print("本体检查 ✅ bytes=%d ｜ LF=%d ｜ 无 BOM ｜ 无 CR" % (len(body), body.count(b"\n")))

# ---------- 追加（纯 append） ----------
with io.open(MEMO, "a", encoding="utf-8", newline="\n") as f:
    f.write(text)
print("追加完成 ✅")

# ---------- 落盘后独立亲测回读 ----------
nb = open(MEMO, "rb").read()
prefix = nb[:EXP_BYTES]
post = {
    "bytes": len(nb),
    "lf": nb.count(b"\n"),
    "cr": nb.count(b"\r"),
    "crlf": nb.count(b"\r\n"),
    "bom": nb[:3] == b"\xef\xbb\xbf",
    "fffd": nb.decode("utf-8", errors="replace").count("\ufffd"),
    "last_byte": hex(nb[-1]),
    "sha12": sha256(nb)[:12],
    "sha256": sha256(nb),
    "prefix_sha256": sha256(prefix),
    "delta_bytes": len(nb) - EXP_BYTES,
    "delta_lf": nb.count(b"\n") - EXP_LF,
}
print("落盘后独立亲测回读：")
for k in ("sha12", "bytes", "lf", "delta_bytes", "delta_lf", "cr", "crlf", "bom", "fffd", "last_byte"):
    print("  %-12s = %s" % (k, post[k]))
print("  prefix_sha256 = %s" % post["prefix_sha256"])
assert post["prefix_sha256"] == cur_sha, "前缀字节校验未过：历史字节被动过！"
assert post["cr"] == 0 and post["bom"] is False and post["fffd"] == 0
assert post["last_byte"] == "0xa"
print("前缀字节校验 ✅ 历史 215,131 字节 SHA-256 与落笔前基线逐位一致 ⇒ 历史字节 0 触动")
print("字节级自报：bytes=%d ｜ LF=%d ｜ CR=0 ｜ CRLF=0 ｜ BOM=False ｜ U+FFFD=0 ｜ 末字节=0x0A" % (post["bytes"], post["lf"]))
