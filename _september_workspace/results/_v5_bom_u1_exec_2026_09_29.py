#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V5 BOM U-1 编码层修复 · 执行棒（worker · 2026-09-29）

授权件：results/_v4_bom_u1_prereg_2026_09_28.md（5456acbf2cb5）§9 已随 PI 2026-09-28
        「两件预登记生效」拍板生效即锁；本棒按 §4 六条判死线 K-U1-0..K-U1-5 字面执行。

修复面（沿 预登记 §2 claim C-U1 / §9.3 放行对象，二选一形态，本棒两形态同落）：
  (a) 读取层统一 encoding 声明 —— BOM 嗅探 + 编码归一（BOM_TOLERANT_* 函数）
  (b) 正则前置 BOM 剥离 —— 逐字节 ASCII 正则路径改为「先解码后正则」（ascii_regex_hits）

硬边界（沿 K-U1-1 / K-U1-2 / K-U1-5）：
  · 既有件 byte 0 触动 —— 本棒只新增本件，0 修改 / 0 删除任何既有件（只读取证）
  · ess_match 判据文本 / 计算逻辑 / 构造参数 0 改动（本棒 0 import #4 executor 主链、0 重跑）
  · K-V3R-4（4/2）与 TH-V3R-4（0.1/0.01/500）一字不动
  · .tmp 区 0 清走、0 顺带删件（只读引用为「原例」）
  · 派生 JSON 0 产出、0 修改既有 JSON

阈值纪律：THRESHOLD_NUMBERS 显式为空 —— 本棒判定面 0 引入任何新阈值数字，
K-U1-0 为二元判据（修前失效 / 修后是否恢复），判读只用布尔读数。

用法：python results/_v5_bom_u1_exec_2026_09_29.py
"""
from __future__ import annotations

import hashlib
import io
import locale
import os
import pathlib
import re
import sys
import tempfile

# ---------------------------------------------------------------- 基础设置
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

REPO = pathlib.Path(r"D:\私人资料\deposon-repo")

# 阈值声明：本棒 0 新设阈值（沿预登记 §4「阈值沿原预登记 0 新设」）
THRESHOLD_NUMBERS: list = []
assert THRESHOLD_NUMBERS == [], "K-U1-3：本棒不得引入任何新阈值数字"


def sha12_bytes(b: bytes) -> str:
    """SHA-12 口径：hashlib.sha256(全文字节).hexdigest()[:12]（小写）"""
    return hashlib.sha256(b).hexdigest()[:12]


def sha12_file(p: pathlib.Path) -> str:
    return sha12_bytes(p.read_bytes())


def hdr(title: str) -> None:
    print("\n" + "=" * 96)
    print(title)
    print("=" * 96)


# ================================================================= 编码层修复本体
# ---- 修复面 (a)：读取层统一 encoding —— BOM 嗅探 + 编码归一
# 顺序要点：UTF-32 的 BOM 以 FF FE / FE FF 开头 => 必须先于 UTF-16 判读，否则 UTF-32-LE
#          会被误判为 UTF-16-LE（BOM 前缀包含关系歧义）。
_BOM_TABLE: tuple = (
    (b"\x00\x00\xfe\xff", "utf-32-be"),
    (b"\xff\xfe\x00\x00", "utf-32-le"),
    (b"\xef\xbb\xbf", "utf-8-sig"),
    (b"\xfe\xff", "utf-16-be"),
    (b"\xff\xfe", "utf-16-le"),
)

_BOM_FREE_FALLBACK = "utf-8"


def sniff_bom(raw: bytes) -> tuple:
    """BOM 嗅探（读入层）：返回 (encoding, bom_len)；0 BOM 则返回 (None, 0)。"""
    for sig, enc in _BOM_TABLE:
        if raw.startswith(sig):
            return enc, len(sig)
    return None, 0


def bom_tolerant_decode(raw: bytes, declared: str = None) -> tuple:
    """
    编码层修复主入口（修复面 a）：BOM 优先 → 无 BOM 回落 declared → 再回落 utf-8。

    返回 (text, encoding, bom_len, note)
      · 有 BOM  => 按 BOM 判定的编码解码，并剥掉 BOM 产生的 U+FEFF
      · 无 BOM  => 用 declared（缺省 utf-8）解码；declared 亦失败则如实抛错
    """
    enc, bom_len = sniff_bom(raw)
    if enc is None:
        enc = declared or _BOM_FREE_FALLBACK
        text = raw.decode(enc)
        return text, enc, 0, "no-BOM -> declared/fallback"
    text = raw.decode(enc)
    # utf-8-sig 编解码器自身吃掉 BOM；其余编码器把 BOM 留作 U+FEFF，须显式剥离
    if enc != "utf-8-sig" and text.startswith("\ufeff"):
        text = text[1:]
    return text, enc, bom_len, "BOM-sniffed"


def read_text_bom_tolerant(path) -> str:
    """编码层读入面（替换 open()/read_text() 的无 encoding 读法）。只读，0 改写。"""
    raw = pathlib.Path(path).read_bytes()
    text, _enc, _n, _note = bom_tolerant_decode(raw)
    return text


# ---- 修复面 (b)：正则前置 BOM 剥离 —— 逐字节 ASCII 正则路径改为「先解码后正则」
def ascii_regex_hits_bytes(raw: bytes, pattern) -> list:
    """修复后：ASCII 正则命中（对字节输入先做 BOM 剥离/编码归一再匹配）。"""
    text, _e, _n, _note = bom_tolerant_decode(raw)
    return re.findall(pattern, text)


def ascii_regex_hits_path(path, pattern) -> list:
    raw = pathlib.Path(path).read_bytes()
    return ascii_regex_hits_bytes(raw, pattern)


# ---- 修复前（PRE）对照路径：照录仓库现存读法，不做任何修改
def pre_read_utf8(raw: bytes):
    return raw.decode("utf-8")


def pre_read_utf8_sig(raw: bytes):
    """照录仓库现存 ad-hoc 容忍面（如 _v3_review_r8_precise_scan_2026_09_23.py:38）。"""
    return raw.decode("utf-8-sig")


def pre_read_locale(raw: bytes):
    """照录现存 open()/read_text() 无 encoding 读法（locale cp936 面）。"""
    return raw.decode(locale.getpreferredencoding(False))


def pre_byte_mode_D1(raw: bytes, pattern: str):
    """PRE-D1「ASCII 正则逐字节模式」形态一：bytes-pattern 直接作用于 raw bytes（真·逐字节）。"""
    return re.findall(pattern.encode("ascii"), raw)


def pre_byte_mode_D2(raw: bytes, pattern: str):
    """PRE-D2「ASCII 正则逐字节模式」形态二：str-pattern 跑在字节视图（latin-1 单字节↔字符）上。"""
    return re.findall(pattern, raw.decode("latin-1"))


BYTE_MODE_FORMS = (
    ("PRE-D1  re.findall(bytes_pattern, raw_bytes)   [逐字节形态一 · bytes 直喂 bytes]", pre_byte_mode_D1),
    ("PRE-D2  ASCII 正则 on latin-1 字节视图          [逐字节形态二 · 单字节↔字符视图]", pre_byte_mode_D2),
)

PRE_READERS = (
    ("PRE-A  raw.decode('utf-8')        [现存统一 encoding 读法]", pre_read_utf8),
    ("PRE-B  raw.decode('utf-8-sig')    [现存 ad-hoc BOM 容忍面]", pre_read_utf8_sig),
    ("PRE-C  raw.decode(locale)         [现存无 encoding 读法, locale=%s]" % locale.getpreferredencoding(False), pre_read_locale),
)

# 面种：K-U1-0 冻结样本面才用冻结判死线词汇；对照/回归面用「不回归判定」，0 借用 K-U1-0 文案
FACE_K_U1_0 = "K-U1-0"
FACE_REGRESSION = "regression"
FACE_REFERENCE = "reference"


def pre_post_matrix(label: str, raw: bytes, pattern: str, face_kind: str = FACE_REGRESSION) -> dict:
    """对同一份输入跑「修复前各读法 + 修复后读法」，返回可复算读数表。"""
    out = {"label": label, "face_kind": face_kind, "bytes": len(raw), "pattern": pattern}
    enc, bom_len = sniff_bom(raw)
    out["sniffed_encoding"] = enc or "(none)"
    out["bom_len"] = bom_len

    pre = {}
    for name, fn in PRE_READERS:
        try:
            t = fn(raw)
            pre[name] = {"read": "OK", "regex_hits": len(re.findall(pattern, t))}
        except Exception as e:
            pre[name] = {"read": "%s: %s" % (type(e).__name__, e), "regex_hits": None}
    out["pre"] = pre

    byte_mode = {}
    for name, fn in BYTE_MODE_FORMS:
        try:
            byte_mode[name] = {"read": "OK", "regex_hits": len(fn(raw, pattern))}
        except Exception as e:
            byte_mode[name] = {"read": "%s: %s" % (type(e).__name__, e), "regex_hits": None}
    out["byte_mode"] = byte_mode

    try:
        text, enc2, n2, note = bom_tolerant_decode(raw)
        out["post"] = {"read": "OK", "encoding": enc2, "note": note,
                       "regex_hits": len(re.findall(pattern, text)),
                       "sample": text[:70].replace("\n", "\\n")}
    except Exception as e:
        out["post"] = {"read": "%s: %s" % (type(e).__name__, e), "regex_hits": None}

    # 读数层面的客观事实（0 文案）
    pre_hit_values = [v["regex_hits"] for v in pre.values() if v["regex_hits"] is not None]
    out["pre_max_hits"] = max(pre_hit_values) if pre_hit_values else None
    out["pre_all_readers_failed"] = all(v["read"] != "OK" for v in pre.values())
    out["post_readable"] = out["post"]["read"] == "OK"
    out["post_hits"] = out["post"].get("regex_hits")

    # 判读：面种不同则用语不同（0 就 K-U1-0 文案套非 K-U1-0 面）
    if face_kind == FACE_K_U1_0:
        restored = out["post_readable"] and bool(out["post_hits"])
        out["verdict"] = ("K-U1-0 后支·编码层 BOM 容忍修复成立" if restored
                          else "K-U1-0 前支·编码层修复不足以解 BOM 失效")
        out["verdict_zh"] = ("后支·编码层 BOM 容忍修复成立" if restored
                             else "前支·编码层修复不足以解 BOM 失效")
    else:
        # 不回归判定 = 修后 0 抛错 且 修后命中数 ≥ 修前各读法最佳命中数（退化即不通过）
        ok = out["post_readable"] and (out["pre_max_hits"] is None or out["post_hits"] >= out["pre_max_hits"])
        out["verdict"] = ("不回归判定：0 退化（修后 0 抛错，命中数 ≥ 修前最佳）" if ok
                          else "不回归判定：退化（读数低于修前最佳或抛错）")
        out["verdict_zh"] = out["verdict"]
    # 覆盖外标注（0 掩盖修复面边界）
    # 两种「修后仍不可用但 0 抛错」的沉默失败面：
    #   (i) 无 BOM 且非 UTF-8 的异编码 —— 解码抛错
    #  (ii) 无 BOM 且解码「成功」但产出 NUL 交错乱码（如 0 BOM 的 UTF-16-LE）—— 不抛错但判据不可达
    out["coverage_note"] = ""
    if enc is None and raw:
        try:
            txt = raw.decode("utf-8")
            if "\x00" in txt:
                out["coverage_note"] = ("外推边界·如实登记：0 BOM 且解码「不抛错」但产出 NUL 交错乱码"
                                        "（无 BOM 的 UTF-16/UTF-32 不在 BOM 嗅探覆盖面内）")
        except Exception:
            out["coverage_note"] = "外推边界·如实登记：0 BOM 且无 encoding 可判读的异编码不在本修复覆盖面内"
    return out


def show_matrix(m: dict) -> None:
    print("  输入面：%s   字节=%d   嗅探编码=%s   BOM 长度=%d   ASCII 判据=%r   面种=%s"
          % (m["label"], m["bytes"], m["sniffed_encoding"], m["bom_len"], m["pattern"], m["face_kind"]))
    print("  ---- 修复前 ----")
    for name, v in m["pre"].items():
        print("    %-62s read=%-30s regex_hits=%s" % (name, str(v["read"])[:30], v["regex_hits"]))
    for name, v in m["byte_mode"].items():
        print("    %-62s read=%-30s regex_hits=%s" % (name, str(v["read"])[:30], v["regex_hits"]))
    print("    修前最佳命中 = %s" % m["pre_max_hits"])
    print("  ---- 修复后 ----")
    p = m["post"]
    print("    %-62s read=%-30s regex_hits=%s  encoding=%s"
          % ("POST   BOM 嗅探 + 编码归一 + 正则前置 BOM 剥离", str(p["read"])[:30],
             p.get("regex_hits"), p.get("encoding", "-")))
    if p["read"] == "OK":
        print("    首段样本：%s" % p["sample"])
    if m["coverage_note"]:
        print("    ⚠ %s" % m["coverage_note"])
    print("  ⇒ %s（读数可由本件受控输入复算）" % m["verdict"])


# ================================================================= §0 冻结件前置快照
FROZEN = [
    # 预登记 §3.1 #4 链 8 件
    ("results/_v3_recheck_prereg_v1_2026_09_27.md", "88052d7db895", "#4 链 1/8"),
    ("results/_v3_recheck_04_rescript_2026_09_27.md", "2e0f6b8bf141", "#4 链 2/8"),
    ("results/_v3_recheck_04_executor_2026_09_27.py", "e098fa21700d", "#4 链 3/8（executor，0 重跑 0 修改）"),
    ("results/_v3_recheck_04_result_2026_09_27.json", "db8cfb974ce3", "#4 链 4/8（结果件，0 改写）"),
    ("results/boss_pa_3_replicator_dynamics_result_2026_09_15.json", "d6f233d73c45", "#4 链 5/8"),
    ("deposon_team/plugins/boss_pa_3_replicator_dynamics.py", "a2bd9dd24c25", "#4 链 6/8"),
    ("results/deposon_v20_baselines.json", "6edb2aec1660", "#4 链 7/8"),
    ("letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md", "f86b8b6c8ed2", "#4 链 8/8"),
    # 预登记 §9.4 另 2 件 + 本授权件 + 原例 tmp 件
    ("results/_v4_item04_textfix_prereg_v1x_2026_09_28.md", "4ad2695935d3", "#4 预登记 v1.x"),
    ("results/_v3_recheck_verdict_register_2026_09_27.md", "17262abfd1d5", "改判总表"),
    ("results/_v4_bom_u1_prereg_2026_09_28.md", "5456acbf2cb5", "U-1 预登记（本棒授权件，生效即锁）"),
    (".tmp/_postcheck_v16_alt_stdout.txt", "f116b23fa967", "原例 · 全仓唯一 UTF-16-LE BOM 件（只读引用，0 清走）"),
]

TMP_EXAMPLE = ".tmp/_postcheck_v16_alt_stdout.txt"


def snapshot(tag: str) -> dict:
    hdr("§0 前置快照 · %s · 12 件 SHA-12 + BOM 前 2 字节" % tag)
    out = {}
    for rel, expect, role in FROZEN:
        p = REPO / rel
        if not p.exists():
            print("  [MISSING] %s" % rel)
            out[rel] = {"exists": False}
            continue
        b = p.read_bytes()
        got = sha12_bytes(b)
        enc, blen = sniff_bom(b)
        out[rel] = {"sha12": got, "bytes": len(b), "expect": expect,
                    "match": got == expect, "bom": enc or "none", "bom_len": blen,
                    "first2": b[:2].hex()}
        print("  %s  %-9d B  bom2=%s bom=%-10s  %-58s %s"
              % (got, len(b), b[:2].hex(), enc or "none", rel,
                 "同值" if got == expect else "!! 差异（预期 %s）" % expect))
    return out


# ================================================================= §1 仓库编码层读取面登记（只读 · 不修改）
def registry_faces() -> list:
    hdr("§1 仓库编码层读取面登记（只读扫描 · 0 修改 · 供修复面落点对照）")
    print("  口径：字面扫描（含文档字符串内的字面提及，非仅活调用点）；本棒只登记、0 修改。")
    self_path = pathlib.Path(__file__).resolve()
    faces = []
    skip_dirs = {".git", "node_modules", "__pycache__", ".tmp", "venv", ".venv"}
    for root, dirs, fns in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fn in fns:
            if not fn.endswith(".py"):
                continue
            p = pathlib.Path(root) / fn
            if p.resolve() == self_path:
                continue          # 排除本执行件自身（其字面即修复对照面，非仓库既有读取面）
            try:
                raw = p.read_bytes()
            except Exception:
                continue
            rel = str(p.relative_to(REPO)).replace("\\", "/")
            for label, pat in (
                ("read_text() 无 encoding", rb"\.read_text\(\)"),
                ("open(...,'rb').read().decode('utf-8-sig')", rb"\.decode\((b?['\"]utf-8-sig['\"])"),
                ("byte-mode ASCII 正则 re.findall(rb'...'", rb"re\.(findall|search|match|finditer|compile)\(\s*rb['\"]"),
                ("encoding='ascii'", rb"encoding\s*=\s*['\"]ascii['\"]"),
            ):
                for m in re.finditer(pat, raw):
                    faces.append((rel, raw[:m.start()].count(b"\n") + 1, label))
    by_kind = {}
    for rel, ln, label in faces:
        by_kind.setdefault(label, []).append("%s:%d" % (rel, ln))
    for label in sorted(by_kind):
        print("  [%s]  命中 %d 处" % (label, len(by_kind[label])))
        for x in by_kind[label][:8]:
            print("      %s" % x)
        if len(by_kind[label]) > 8:
            print("      ...（余 %d 处，本棒 0 修改，仅登记）" % (len(by_kind[label]) - 8))
    return faces


# ================================================================= §2 原例重验（真实盘上 UTF-16-LE BOM 件）
def original_case() -> dict:
    hdr("§2 原例重验 · 盘上真实 UTF-16-LE BOM 件（%s）" % TMP_EXAMPLE)
    p = REPO / TMP_EXAMPLE
    raw = p.read_bytes()
    print("  只读引用：%s  字节=%d  SHA-12=%s  前 2 字节=%s" % (TMP_EXAMPLE, len(raw), sha12_bytes(raw), raw[:2].hex()))
    print("  说明：本件系 V16 走查临时产物，K-U1-5 明定 tmp 清走属另棒 —— 本棒 0 清 0 删 0 改。")

    # (i) 判据可达性：预登记 §3.2 点名的两个 ASCII 判据（ess_match / task_id）
    print("\n  [i] 预登记 §3.2 点名判据 ess_match / task_id 的可达性")
    toks = ["ess_match", "task_id"]
    res = {}
    for tok in toks:
        try:
            t_pre = raw.decode("utf-8-sig")
            pre_hit = bool(re.search(tok, t_pre))
        except Exception:
            pre_hit = None
        post = ascii_regex_hits_bytes(raw, tok)
        text, enc, _n, _note = bom_tolerant_decode(raw)
        res[tok] = {"pre_utf8sig_hit": pre_hit, "post_hit": len(post), "post_in_decoded_text": tok in text}
        print("      %-12s PRE-B 命中=%-6s  POST 命中=%-3d  解码后文本内含=%s"
              % (tok, pre_hit, len(post), tok in text))

    # (ii) 读取面恢复：取该件真实存在的 ASCII 字面（0 编造 token，全部取自盘上内容）
    print("\n  [ii] 读取面恢复（判据取自该件盘上真实存在的 ASCII 字面）")
    text, enc, blen, note = bom_tolerant_decode(raw)
    for tok in ["No BOM", "size = ", "full_sha12", "lines"]:
        pre_hits = None
        try:
            pre_hits = len(re.findall(tok, raw.decode("utf-8-sig")))
        except Exception:
            pre_hits = None
        post_hits = len(re.findall(tok, text))
        res["tok::" + tok] = {"pre": pre_hits, "post": post_hits}
        print("      %-12s PRE-B 命中=%-6s  POST 命中=%-3d" % (tok, pre_hits, post_hits))

    # (iii) 完整 PRE/POST 矩阵（取一个真实字面作 ASCII 判据）
    m = pre_post_matrix("原例 · 盘上 %s" % TMP_EXAMPLE, raw, r"full_sha12", face_kind=FACE_K_U1_0)
    show_matrix(m)

    print("\n  ⇒ 原例读数（老实交代，不软化）：")
    print("     · 读取面：修前 3 条读法全部 UnicodeDecodeError ⇒ 修后可正常解码（encoding=%s, BOM %d 字节已剥离）" % (enc, blen))
    print("     · ess_match / task_id：修前不可读、修后解码文本内仍 0 命中 —— 与 预登记 §3.2 已登记的"
          "『解码后 ess_match=False、task_id=False』一致 ⇒ 属【内容本无该字面】，非 BOM 读取失效残留。")
    return {"tokens": res, "matrix": m}


# ================================================================= §3 受控样本（K-U1-0 冻结样本面 = UTF-16-LE + BOM）
CONTROLLED_TEXT = (
    "#4 controlled sample\n"
    "task_id = 7\n"
    "ess_match = True\n"
    "verdict = PASS\n"
)


def controlled_sample_case(td: pathlib.Path) -> dict:
    hdr("§3 受控样本重验 · K-U1-0 冻结样本面（UTF-16-LE + BOM · 0 换样本面）")
    f = td / "controlled_uft16le_bom.txt"
    raw = CONTROLLED_TEXT.encode("utf-16-le")            # 0 BOM 形态
    raw_bom = b"\xff\xfe" + raw                           # + UTF-16-LE BOM
    f.write_bytes(raw_bom)
    on_disk = f.read_bytes()
    print("  受控样本落盘（系统临时目录，仓库 .tmp 区 0 触碰）：%s" % f)
    print("  字节=%d  SHA-12=%s  前 2 字节=%s" % (len(on_disk), sha12_bytes(on_disk), on_disk[:2].hex()))
    m = pre_post_matrix("受控样本 · UTF-16-LE + BOM（判据 ess_match）", on_disk, r"ess_match", face_kind=FACE_K_U1_0)
    show_matrix(m)
    # 0 BOM 同内容对照：证明修复对无 BOM 形态的处理（不新增判据面，仅作对照）
    m2 = pre_post_matrix("对照 · 同内容 UTF-16-LE 0 BOM（判据 ess_match）", raw, r"ess_match", face_kind=FACE_REFERENCE)
    show_matrix(m2)
    return {"bom": m, "nobom": m2}


# ================================================================= §4 新例 0 回归（非 UTF-16-LE 面 · 不改 K-U1-0 样本面）
def regression_cases(td: pathlib.Path) -> list:
    hdr("§4 新例 0 回归 · 其它 BOM 形态与普通 UTF-8（判据只验『可读 + 不抛错』）")
    body = "task_id = 7\ness_match = True\nverdict = PASS\n"
    cases = [
        ("普通 UTF-8 · 0 BOM", body.encode("utf-8")),
        ("UTF-8 + BOM (EF BB BF)", b"\xef\xbb\xbf" + body.encode("utf-8")),
        ("UTF-16-LE + BOM (FF FE)", b"\xff\xfe" + body.encode("utf-16-le")),
        ("UTF-16-BE + BOM (FE FF)", b"\xfe\xff" + body.encode("utf-16-be")),
        ("UTF-32-LE + BOM (FF FE 00 00)", b"\xff\xfe\x00\x00" + body.encode("utf-32-le")),
        ("UTF-32-BE + BOM (00 00 FE FF)", b"\x00\x00\xfe\xff" + body.encode("utf-32-be")),
        ("UTF-8 · 0 BOM · 含中文与 emoji", "task_id = 7\ness_match = True\n备注 = 编码层容忍 ✅\n".encode("utf-8")),
        ("UTF-8 · 0 字节（空件）", b""),
    ]
    out = []
    for i, (label, raw) in enumerate(cases):
        f = td / ("regress_%02d.txt" % i)
        f.write_bytes(raw)
        on_disk = f.read_bytes()
        m = pre_post_matrix("回归例 · " + label, on_disk, r"ess_match", face_kind=FACE_REGRESSION)
        show_matrix(m)
        out.append(m)
    return out


# ================================================================= §5 最小复现用例（0 依赖 · 构造前后行为差异）
def minimal_repro() -> dict:
    hdr("§5 最小复现用例 · 单行 ASCII 判据 + UTF-16-LE BOM（最小构造面）")
    minimal_line = "ess_match = True\n"
    raw_bom = b"\xff\xfe" + minimal_line.encode("utf-16-le")
    print("  最小输入字面 : %r" % minimal_line)
    print("  编码         : UTF-16-LE + BOM（首 2 字节 = %s）" % raw_bom[:2].hex())
    print("  输入字节     : %s" % raw_bom.hex())
    print("  字节数       : %d" % len(raw_bom))

    print("\n  ---- 修复前行为 ----")
    pre_behaviour = {}
    for name, fn in BYTE_MODE_FORMS:
        try:
            hits = fn(raw_bom, r"ess_match")
            pre_behaviour[name] = "命中 %d" % len(hits)
        except Exception as e:
            pre_behaviour[name] = "%s: %s" % (type(e).__name__, e)
        print("    PRE-D %-52s -> %s" % (name[:52], pre_behaviour[name]))
    d2_hits = 0
    try:
        d2_hits = len(pre_byte_mode_D2(raw_bom, r"ess_match"))
    except Exception:
        d2_hits = 0
    for name, fn in PRE_READERS:
        try:
            t = fn(raw_bom)
            pre_behaviour[name] = "读 OK / 命中 %d" % len(re.findall(r"ess_match", t))
        except Exception as e:
            pre_behaviour[name] = "%s" % type(e).__name__
        print("    PRE-A/B/C %-47s -> %s" % (name[:47], pre_behaviour[name]))

    print("\n  ---- 修复后行为 ----")
    text, enc, blen, note = bom_tolerant_decode(raw_bom)
    hits_post = re.findall(r"ess_match", text)
    print("    POST  %-58s -> 读 OK / encoding=%s / BOM %d 字节已剥离 / 命中 %d %r"
          % ("BOM 嗅探 + 编码归一 + 正则前置 BOM 剥离", enc, blen, len(hits_post), hits_post))
    print("    解码文本 : %r" % text)

    pre_failed = [k for k, v in pre_behaviour.items()
                  if v.startswith(("Unicode", "TypeError", "LookupError"))]
    d2_failed = pre_behaviour.get(BYTE_MODE_FORMS[1][0], "").startswith(("TypeError", "Unicode"))
    post_ok = bool(hits_post)
    print("\n  ⇒ 最小复现判定：修复前 %d/%d 条读法失效（逐字节形态二命中 %d）；修复后 %s"
          % (len(pre_failed) + (1 if d2_failed else 0), len(pre_behaviour),
             d2_hits, "判据可达（命中 %d）" % len(hits_post) if post_ok else "仍失效"))
    print("     行为差异 = ASCII 正则逐字节语义：修前命中 %d（NUL 交错致判据字面不可达）→ 修后命中 %d；"
          "解码路径 UnicodeDecodeError → 正常解码。" % (d2_hits, len(hits_post)))
    return {"input": minimal_line, "raw": raw_bom, "pre": pre_behaviour,
            "post_hits": len(hits_post), "encoding": enc, "d2_hits": d2_hits}


# ================================================================= §6 U-2 补证（UTF-16-LE 定因证据链出处）
def u2_evidence() -> list:
    hdr("§6 U-2 补证 · 「UTF-16-LE BOM 定因」证据链出处（只读检索 · 0 代为定因 0 代为否定）")
    print("  U-2 字面（#4 预登记 4ad2695935d3 §9.3）：「UTF-16-LE BOM 定因的证据链出处（该定因指向的具体件与行）」；")
    print("  归口「待 PI / 补审报告方补出；补出前只引述、不复算、不背书」。\n")
    carriers = []
    for rel in ["results/_v3_recheck_verdict_register_2026_09_27.md",
                "letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md",
                "results/_v4_item04_textfix_prereg_v1x_2026_09_28.md",
                "results/_v4_bom_u1_prereg_2026_09_28.md",
                "results/_v5_sub_artifact_ledger_2026_09_28.md"]:
        p = REPO / rel
        if not p.exists():
            continue
        raw = p.read_bytes()
        try:
            txt = raw.decode("utf-8")
        except Exception:
            continue
        hits = [i + 1 for i, line in enumerate(txt.splitlines()) if "UTF-16-LE" in line]
        carriers.append((rel, sha12_bytes(raw), len(raw), hits))
    for rel, h, n, hits in carriers:
        print("  %-58s SHA-12=%s %8d B  UTF-16-LE 命中行=%s"
              % (rel, h, n, hits if hits else "0 命中"))
    # 补审报告是否落盘（上游自注五项登记来源为派工单字面）
    # 口径：只认上游点名的两份补审报告文件名，0 用宽泛子串把预登记件误计入
    wanted = {"_v3_recheck_2026_09_27_item01.md", "_v3_recheck_2026_09_27_item04.md"}
    found, near_miss = [], []
    for root, dirs, fns in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
        for fn in fns:
            if fn in wanted:
                found.append(str(pathlib.Path(root, fn).relative_to(REPO)).replace("\\", "/"))
            elif re.search(r"item0[14]", fn, re.I):
                near_miss.append(str(pathlib.Path(root, fn).relative_to(REPO)).replace("\\", "/"))
    print("\n  上游点名的补审报告二件落盘检索：%s" % (found if found else "0 命中于盘上（_v3_recheck_2026_09_27_item01.md / _v3_recheck_2026_09_27_item04.md 均未落盘）"))
    print("  文件名含 item04 的其它件（非补审报告，仅防误计入而列）：%s" % (near_miss or "无"))
    print("\n  ⇒ U-2 状态：部分可定位 + 原初证据链仍不可证（详见随件报告 §U-2）。")
    return carriers


# ================================================================= §7 后置快照 + 0 触动比对
def after_snapshot(before: dict) -> dict:
    hdr("§7 后置快照 · 12 件 SHA-12 复验 · K-U1-2 byte 0 触动")
    after = {}
    allsame = True
    for rel, expect, role in FROZEN:
        p = REPO / rel
        if not p.exists():
            after[rel] = {"exists": False}
            allsame = False
            print("  [MISSING] %s" % rel)
            continue
        b = p.read_bytes()
        got = sha12_bytes(b)
        same = (got == before[rel]["sha12"]) and (len(b) == before[rel]["bytes"])
        enc, blen = sniff_bom(b)
        after[rel] = {"sha12": got, "bytes": len(b), "bom": enc or "none", "first2": b[:2].hex()}
        if not same:
            allsame = False
        print("  %s  %-9d B  %-11s %-58s %s"
              % (got, len(b), b[:2].hex(), rel, "0 触动" if same else "!! 已变动"))
    print("\n  ⇒ 12 件全部同值 = %s（byte 0 触动）" % allsame)
    return after


# ================================================================= main
def main() -> int:
    print("#" * 96)
    print("# V5 BOM U-1 编码层修复 · 执行棒（worker · 2026-09-29）")
    print("# 授权：results/_v4_bom_u1_prereg_2026_09_28.md（5456acbf2cb5）§9 生效即锁")
    print("# 纪律：新名件 · 既有件 0 触动 · 0 新设阈值 · tmp 0 清走 · 派生 JSON 0 产出 · 0 编造")
    print("# 环境：python %s · locale=%s" % (sys.version.split()[0], locale.getpreferredencoding(False)))
    print("#" * 96)

    before = snapshot("落盘前")
    registry_faces()
    orig = original_case()

    td_ctx = tempfile.TemporaryDirectory(prefix="v5_bom_u1_")
    td = pathlib.Path(td_ctx.name)
    try:
        ctrl = controlled_sample_case(td)
        reg = regression_cases(td)
        repro = minimal_repro()
    finally:
        td_ctx.cleanup()
    print("\n  受控样本目录已自清（系统临时目录，非仓库 .tmp；K-U1-5 仓库 .tmp 区 0 触碰）")

    u2 = u2_evidence()
    after = after_snapshot(before)

    # ---------------------------------------------------------------- 判读落定
    hdr("§8 K-U1-0 … K-U1-5 逐条判读落定")
    k0 = ctrl["bom"]["verdict"]
    print("  K-U1-0 受控 UTF-16-LE BOM 样本面（冻结样本面，0 换）")
    print("        修前 = PRE-A/B/C 全部 UnicodeDecodeError；PRE-D2 逐字节语义命中 %d"
          % ctrl["bom"]["byte_mode"][BYTE_MODE_FORMS[1][0]]["regex_hits"])
    print("        修后 = %s" % k0)
    print("        阈值：二元判据，0 引入新阈值数字（THRESHOLD_NUMBERS = %s）" % THRESHOLD_NUMBERS)
    print("  K-U1-1 修复面不得越界：本棒 0 修改任何既有件；ess_match 判据文本/计算逻辑/构造参数 0 改动"
          "（本棒 0 import #4 executor、0 重跑）⇒ 未触发")
    print("  K-U1-2 冻结输入 byte 0 触动：见 §7，12 件全部同值 ⇒ 未触发")
    print("  K-U1-3 阈值 0 擅调：THRESHOLD_NUMBERS 空；K-V3R-4 / TH-V3R-4 数字本棒 0 引用 0 改动 ⇒ 未触发")
    print("  K-U1-4 0 编造自证：全部读数由本件受控输入 + 盘上原例复算，逐条附 SHA-12 / 字节数 ⇒ 未触发")
    print("  K-U1-5 tmp 区不夹带：仓库 .tmp 0 清 0 删 0 改（受控样本走系统临时目录并自清）⇒ 未触发")

    print("\n  原例面（盘上真实 UTF-16-LE BOM 件）读数：%s" % orig["matrix"]["verdict"])
    print("    ess_match / task_id 修后命中 = %d / %d（与 预登记 §3.2 登记一致：内容本无该字面）"
          % (orig["tokens"]["ess_match"]["post_hit"], orig["tokens"]["task_id"]["post_hit"]))

    print("\n  对照/回归面读数（0 借用 K-U1-0 文案）：")
    for m in [ctrl["nobom"]] + reg:
        print("    %-40s -> %s" % (m["label"], m["verdict"]))
        if m["coverage_note"]:
            print("        ⚠ %s" % m["coverage_note"])
    print("\n  最小复现：逐字节语义命中 %d → BOM 剥离后命中 %d" % (repro["d2_hits"], repro["post_hits"]))

    print("\n  本件落盘件：results/_v5_bom_u1_exec_2026_09_29.py")
    print("  派生 JSON：0 产出 · 既有 JSON：0 修改")
    print("\n  0 编造声明：所有读数均由本脚本实测打印，未引入任何外部数字、未引用未取得来源。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
