#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 子棒版·主会话对话面扫描器（独立读取·mtime/时点窗·去重取并）
纪律：⛔0 读 key/.env；⛔0 修改会话存储；只读。
"""
import os, sys, json, io, datetime, hashlib

MAIN = r"〔本地绝对路径·脱敏略:02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5〕"
WIN_START_MS = 1792510813000  # 2026-10-20 15:40:13 CST
OUT = r"〔幽灵引用·原件已缺席·未上传:_s14_session_scan_out_2026_10_21.md〕"

def ts_ms(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return int(v if v > 1e11 else v * 1000)
    return None

def main():
    p = os.path.join(MAIN, "messages.jsonl")
    total = 0
    inwin = 0
    rows = []
    bad = 0
    with io.open(p, "r", encoding="utf-8", errors="replace") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                o = json.loads(line)
            except Exception:
                bad += 1
                continue
            t = None
            for k in ("createdAtMs", "created_at_ms", "timestampMs", "ts", "createdAt"):
                if k in o:
                    t = ts_ms(o[k]); 
                    if t: break
            if t is None and isinstance(o.get("meta"), dict):
                for k in ("createdAtMs", "timestampMs"):
                    if k in o["meta"]:
                        t = ts_ms(o["meta"][k])
                        if t: break
            if t is None:
                continue
            if t < WIN_START_MS:
                continue
            inwin += 1
            role = o.get("role") or (o.get("meta") or {}).get("role") or "?"
            # content text extraction
            txt = ""
            c = o.get("content")
            if isinstance(c, str):
                txt = c
            elif isinstance(c, list):
                parts = []
                for seg in c:
                    if isinstance(seg, dict):
                        parts.append(str(seg.get("text") or seg.get("content") or seg.get("type") or ""))
                    else:
                        parts.append(str(seg))
                txt = " ".join(parts)
            elif c is None:
                for k in ("text", "body", "message"):
                    if isinstance(o.get(k), str):
                        txt = o[k]; break
            txt = txt.replace("\r", "")
            rows.append((t, ln, role, txt, o))
    rows.sort(key=lambda r: (r[0], r[1]))
    lines = []
    lines.append("# §14 子棒版·主会话对话面扫描 · 观测时点 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("# 源 = %s" % p)
    lines.append("# 窗口下界 = 2026-10-20 15:40:13 CST（=%d ms）" % WIN_START_MS)
    lines.append("# messages.jsonl 总行数=%d · 窗内行数=%d · 解析失败=%d" % (total, inwin, bad))
    lines.append("")
    for t, ln, role, txt, o in rows:
        stamp = datetime.datetime.fromtimestamp(t / 1000).strftime("%m-%d %H:%M:%S")
        first = " ".join(txt.split())[:700]
        keys = sorted(o.keys())
        lines.append("### [%s] line=%d role=%s len=%d keys=%s" % (stamp, ln, role, len(txt), ",".join(keys)))
        if first:
            lines.append(first)
        lines.append("")
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("total=", total, "inwin=", inwin, "bad=", bad, "->", OUT)

if __name__ == "__main__":
    main()
