#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 · 主会话窗内事件锚 v2（修正窗下界 ＋ 修正内容取用：list/str 双径）
"""
import os, io, json, datetime

MAIN = r"〔本地绝对路径·脱敏略:02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5〕"
OUTB = r"〔幽灵引用·原件已缺席·未上传:_s14_main_events2_2026_10_21.md〕"
WIN_START_MS = 1792482013000

def get_text(m):
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

def main():
    p = os.path.join(MAIN, "messages.jsonl")
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
            m = o.get("message") if isinstance(o.get("message"), dict) else o
            t = m.get("timestamp")
            if not isinstance(t, (int, float)) or t < WIN_START_MS:
                continue
            rows.append((int(t), ln, m.get("role"), get_text(m), m))
    rows.sort(key=lambda r: (r[0], r[1]))
    L = []
    L.append("# §14 · 主会话窗内事件锚 v2（窗下界 2026-10-20 15:40:13 CST）· 观测时点 %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    L.append("# 源 = %s" % p)
    L.append("# 窗内记录数 = %d" % len(rows))
    L.append("")
    for t, ln, role, txt, m in rows:
        stamp = datetime.datetime.fromtimestamp(t / 1000).strftime("%m-%d %H:%M:%S")
        flat = " ".join(txt.split())
        if role == "assistant" and flat:
            L.append("[%s] L%d assistant :: %s" % (stamp, ln, flat[:700]))
        elif role == "toolResult" and flat and ("wrote" in flat.lower() or "SHA12" in flat or "Successfully" in flat):
            L.append("[%s] L%d toolResult :: %s" % (stamp, ln, flat[:260]))
        elif role == "user" and "background-task-finished" in flat:
            L.append("[%s] L%d user(bg-finished) :: %s" % (stamp, ln, flat[:260]))
    with io.open(OUTB, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("records=", len(rows), "->", OUTB)

if __name__ == "__main__":
    main()
