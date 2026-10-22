#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
审计扫描器 v13 · 子棒版备忘录续修用 · 2026-10-20
用途：提取主会话存储面（快照 g000000000091 + messages.jsonl）在续修窗
      （2026-10-19 23:56:47 → 2026-10-20）内之对话面事件锚。
纪律：只读；⛔0 读任何 key／.env；⛔0 输出凭据明文；⛔0 写既有件。
输出：UTF-8（no BOM）文本转储，供落笔时引用。
"""
import json, os, re, sys, io

SNAP = r"〔本地绝对路径·脱敏略:g000000000091--ctx_d4bd8bf7-b129-4390-8e0a-db3c34364a1e.jsonl〕"
MSGS = r"〔本地绝对路径·脱敏略:messages.jsonl〕"
OUT = r"〔幽灵引用·原件已缺席·未上传:_audit_s13_conv_out_2026_10_20.txt〕"

# 窗起点：2026-10-19 23:56:47 UTC+8 -> epoch ms
# 复算锚：v145 卡 submittedAt 1792459851984 == 2026-10-20 09:30:51.984 CST
#         ⇒ 2026-10-20 00:00:00 CST == 1792459851984 - 34251984 == 1792425600000
#         ⇒ 2026-10-19 23:56:47 CST == 1792425600000 - 193000 == 1792425407000
WIN_START_MS = 1792425407000
WIN_END_MS = 9999999999999

TS_RE = re.compile(r"\b(1[78]\d{11})\b")

def iter_records(path):
    if not os.path.exists(path):
        return
    with io.open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except Exception:
                continue

def text_of(rec):
    """尽最大努力提取一条记录的文本内容（兼容多种 schema）。"""
    msg = rec.get("message") if isinstance(rec, dict) else None
    if not isinstance(msg, dict):
        msg = rec if isinstance(rec, dict) else {}
    content = msg.get("content")
    if isinstance(content, str):
        return content
    out = []
    if isinstance(content, list):
        for c in content:
            if not isinstance(c, dict):
                continue
            t = c.get("type")
            if t == "text":
                out.append(c.get("text") or c.get("value") or "")
            elif t == "thinking":
                out.append("[THINKING]")
            elif t == "tool_use":
                out.append("[TOOL_USE:%s]" % (c.get("name") or ""))
            elif t == "tool_result":
                out.append("[TOOL_RESULT]")
            elif t == "compactionSummary":
                out.append("[COMPACTION_SUMMARY]")
    return "\n".join(x for x in out if x)

def ts_of(rec):
    msg = rec.get("message") if isinstance(rec, dict) else None
    if not isinstance(msg, dict):
        msg = rec if isinstance(rec, dict) else {}
    for k in ("timestamp", "createdAt", "ts", "time"):
        v = msg.get(k)
        if isinstance(v, (int, float)):
            return int(v)
    return None

def role_of(rec):
    msg = rec.get("message") if isinstance(rec, dict) else None
    if not isinstance(msg, dict):
        msg = rec if isinstance(rec, dict) else {}
    return msg.get("role") or rec.get("role") or rec.get("kind") or "?"

def sanitize(s, limit):
    s = s.replace("\r\n", "\n")
    s = re.sub(r"[ \t]+\n", "\n", s)
    if len(s) > limit:
        s = s[:limit] + "\n...[TRUNC limit=%d]" % limit
    return s

def main():
    lines = []
    lines.append("# 审计扫描器 v13 之输出 · 续修窗对话面 · 2026-10-20")
    lines.append("# 窗：2026-10-19 23:56:47 → 2026-10-20（epoch ms >= %d）" % WIN_START_MS)
    lines.append("# 面一：主会话快照 g000000000091（mtime 2026-10-20 14:47:19）")
    lines.append("# 面二：主会话 messages.jsonl（mtime 2026-10-20 15:19:41·含压缩后 14:41→ 段）")
    lines.append("")

    for tag, path in (("SNAP", SNAP), ("MSGS", MSGS)):
        n_total = n_win = 0
        lines.append("=" * 100)
        lines.append("### 面：%s" % tag)
        lines.append("=" * 100)
        for rec in iter_records(path):
            n_total += 1
            ts = ts_of(rec)
            if ts is None:
                continue
            if ts < WIN_START_MS or ts > WIN_END_MS:
                continue
            n_win += 1
            role = role_of(rec)
            body = sanitize(text_of(rec), 2200)
            if not body.strip():
                continue
            lines.append("-" * 90)
            lines.append("[%s] ts=%d role=%s" % (tag, ts, role))
            lines.append(body)
            lines.append("")
        lines.append(">>> %s 总记录=%d 窗内记录=%d" % (tag, n_total, n_win))
        lines.append("")

    data = "\n".join(lines) + "\n"
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(data)
    print("WROTE", OUT, len(data.encode("utf-8")), "bytes")

if __name__ == "__main__":
    main()
