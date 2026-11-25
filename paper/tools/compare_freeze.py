#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# compare_freeze.py — 两版冻结清单逐位比对（v4 重冻令的「重出比对 0 失配」证据件）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-25 12:05:07「只重冻这一行，其余 40 项指纹不动；FREEZE 版本递增
#       v3→v4，重出比对 0 失配。」
# 用法：python3 paper/tools/compare_freeze.py <旧 FREEZE.json> [新 FREEZE.json]
#   默认新件 = paper/evidence/FREEZE_v5preR2.json
# 口径：只比「冻结项」（记忆帐树 rows ＋ 实验帐树 rows ＋ 两套 RAG），不比 version/head/
#       时刻/说明字段——那些是重冻本身，不是冻结对象。
# 纪律：只读·0 改源文件·凭据 0 入册。
# ============================================================================
import json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NEW_DEFAULT = os.path.join(HERE, "paper/evidence/FREEZE_v5preR2.json")


def items(d):
    out = {}
    for r in d["memory_tree"]["rows"] + d["experiment_tree"]["rows"]:
        out[(r.get("tree", ""), r["path"])] = (r["sha12"], r["lines"], r["bytes"])
    for r in d["rag"]:
        out[(r.get("rag", ""), r["path"])] = (r["sha12"], r["lines"], r["bytes"])
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    old = json.load(open(sys.argv[1], encoding="utf-8"))
    new = json.load(open(sys.argv[2] if len(sys.argv) > 2 else NEW_DEFAULT, encoding="utf-8"))
    o, n = items(old), items(new)
    added = [k for k in n if k not in o]
    removed = [k for k in o if k not in n]
    changed = [(k, o[k], n[k]) for k in n if k in o and o[k] != n[k]]
    unchanged = [k for k in n if k in o and o[k] == n[k]]
    report = {
        "old": {"version": old["version"], "head": old["head"], "items": len(o)},
        "new": {"version": new["version"], "head": new["head"], "items": len(n)},
        "item_sets_equal": set(o) == set(n),
        "added": [{"tree": k[0], "path": k[1]} for k in added],
        "removed": [{"tree": k[0], "path": k[1]} for k in removed],
        "changed": [{"tree": k[0], "path": k[1], "old": list(a), "new": list(b)} for k, a, b in changed],
        "n_changed": len(changed),
        "n_unchanged": len(unchanged),
        "verdict": ("0 失配" if (not added and not removed and len(changed) == 1
                                and changed[0][0][1] == "docs/thermo-generation.md")
                    else "失配·须处置"),
    }
    print(json.dumps(report, ensure_ascii=False, indent=1))
    return 0 if report["verdict"] == "0 失配" else 1


if __name__ == "__main__":
    sys.exit(main())
