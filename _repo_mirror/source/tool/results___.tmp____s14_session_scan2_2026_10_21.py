#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 子棒版·会话存储面扫描器 v2（正确嵌套时点取用）
纪律：只读；⛔0 改会话存储；⛔0 读 key/.env。
记录形态：{"message_id","turn_id","message":{"role","timestamp","content",...}}
"""
import os, sys, json, io, datetime, glob

SESS = r"〔本地绝对路径·脱敏略:2026〕"
MAIN = os.path.join(SESS, "09", "01", "02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5")
WIN_START_MS = 1792482013000  # 2026-10-20 15:40:13 CST·复核修正：首版误设 1792510813000（=23:40:13·偏 +8h）已改
OUT = r"〔幽灵引用·原件已缺席·未上传:_s14_session_scan_out_2026_10_21.md〕"

BRANCH_GLOBS = [
    os.path.join(SESS, "10", "20", "*"),
    os.path.join(SESS, "10", "21", "*"),
    os.path.join(SESS, "09", "01", "02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5"),
]

def get_ts(o):
    m = o.get("message") if isinstance(o.get("message"), dict) else o
    for k in ("timestamp", "createdAtMs", "created_at_ms", "ts"):
        v = m.get(k)
        if isinstance(v, (int, float)) and v > 1e11:
            return int(v)
    return None

def get_role(o):
    m = o.get("message") if isinstance(o.get("message"), dict) else o
    return m.get("role") or o.get("role") or "?"

def get_text(o):
    m = o.get("message") if isinstance(o.get("message"), dict) else o
    c = m.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        parts = []
        for seg in c:
            if isinstance(seg, dict):
                parts.append(str(seg.get("text") or seg.get("content") or seg.get("type") or ""))
            else:
                parts.append(str(seg))
        return " ".join(parts)
    if isinstance(m.get("summary"), str):
        return m["summary"]
    return ""

def scan_dir(d):
    p = os.path.join(d, "messages.jsonl")
    if not os.path.isfile(p):
        return []
    rows = []
    with io.open(p, "r", encoding="utf-8", errors="replace") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            t = get_ts(o)
            if t is None or t < WIN_START_MS:
                continue
            rows.append((t, ln, get_role(o), get_text(o), o))
    rows.sort(key=lambda r: (r[0], r[1]))
    return rows

def main():
    dirs = []
    for g in BRANCH_GLOBS:
        for d in sorted(glob.glob(g)):
            if os.path.isdir(d) and os.path.isfile(os.path.join(d, "manifest.json")):
                dirs.append(d)
    lines = []
    lines.append("# §14 子棒版·会话存储面扫描 v2 · 观测时点 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("# 窗口下界 = 2026-10-20 15:40:13 CST（=%d ms）·只读" % WIN_START_MS)
    lines.append("# 会话目录数 = %d" % len(dirs))
    lines.append("")
    grand = 0
    for d in dirs:
        rows = scan_dir(d)
        grand += len(rows)
        sid = "?"
        mp = os.path.join(d, "manifest.json")
        try:
            sid = json.load(io.open(mp, encoding="utf-8"))["sessionId"]
        except Exception:
            pass
        lines.append("## SESSION %s" % sid)
        lines.append("### dir = %s" % os.path.relpath(d, SESS).replace("\\", "/"))
        lines.append("### 窗内记录数 = %d" % len(rows))
        for t, ln, role, txt, o in rows:
            stamp = datetime.datetime.fromtimestamp(t / 1000).strftime("%m-%d %H:%M:%S")
            flat = " ".join(txt.split())
            head = flat[:900]
            lines.append("- [%s] L%d role=%s len=%d :: %s" % (stamp, ln, role, len(txt), head))
        lines.append("")
    lines.append("# 窗内记录合计 = %d" % grand)
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("sessions=", len(dirs), "inwin_total=", grand, "->", OUT)

if __name__ == "__main__":
    main()
