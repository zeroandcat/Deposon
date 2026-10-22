#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 · 主会话 messages.jsonl 时点分布诊断（只读）
目的：核实 10-20 15:40 → 23:41 之段是否真为记录空白·抑或为时点解析漏取。
"""
import os, io, json, datetime, collections

MAIN = r"〔本地绝对路径·脱敏略:02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5〕"
OUT = r"〔幽灵引用·原件已缺席·未上传:_s14_msgdist_2026_10_21.md〕"

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

def main():
    p = os.path.join(MAIN, "messages.jsonl")
    per_hour = collections.Counter()
    roles = collections.Counter()
    nots = 0
    tot = 0
    first_t = None
    last_t = None
    buckets = collections.OrderedDict()
    with io.open(p, "r", encoding="utf-8", errors="replace") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            tot += 1
            try:
                o = json.loads(line)
            except Exception:
                nots += 1
                continue
            t = get_ts(o)
            if t is None:
                nots += 1
                continue
            roles[get_role(o)] += 1
            if first_t is None or t < first_t:
                first_t = t
            if last_t is None or t > last_t:
                last_t = t
            d = datetime.datetime.fromtimestamp(t / 1000)
            key = d.strftime("%m-%d %H")
            per_hour[key] += 1
    L = []
    L.append("# 主会话 messages.jsonl · 时点分布诊断 · 观测时点 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    L.append("# 源 = %s" % p)
    L.append("# 总行数 = %d · 无时点/解析失败 = %d" % (tot, nots))
    L.append("# 最早时点 = %s" % (datetime.datetime.fromtimestamp(first_t/1000).strftime("%Y-%m-%d %H:%M:%S") if first_t else "N/A"))
    L.append("# 最晚时点 = %s" % (datetime.datetime.fromtimestamp(last_t/1000).strftime("%Y-%m-%d %H:%M:%S") if last_t else "N/A"))
    L.append("")
    L.append("## role 分布")
    for k, v in roles.most_common():
        L.append("- %s : %d" % (k, v))
    L.append("")
    L.append("## 每时点条数（10-19 之后）")
    for k in sorted(per_hour):
        if k.startswith("10-19") or k.startswith("10-20") or k.startswith("10-21"):
            L.append("- %s : %d" % (k, per_hour[k]))
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:8]))
    print("->", OUT)

if __name__ == "__main__":
    main()
