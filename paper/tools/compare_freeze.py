#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# compare_freeze.py — 两版冻结清单逐位比对（verdict 判据 v5 口径·PI 18:08 C5）
# ----------------------------------------------------------------------------
# v5 口径修复（2026-11-25 18:08 令 C5·群管理员 18:43:49 派单；工具件·非已验代码）：
#   v4 时代 verdict 为单事件硬编码（「恰 1 行变更且路径 == docs/thermo-generation.md」），
#   只适配 v3→v4 那一次重冻；v5 时代重冻是规例（合流重冻／改名路径互换／活件行每轮重测），
#   硬编码会把规例内变更误报 失配、也可能放过别处的单行变更。v5 口径改为机械归因分类：
#     path_swap        — 增/删成对·同树同 sha12/行/字节·仅路径不同（改名互换）→ 规例内
#     kind_normalized  — 同键同指纹·仅 kind 字段规范化 → 规例内
#     live_remeasured  — kind ∈ {live, active} 行指纹更新（活件行按规例每轮重测）→ 规例内
#     content_changed  — 其余类（frozen/source/index/tree/machine/rag）内容变更 → 须处置
#   verdict：全部变更 ∈ 规例内三类 → 「0 失配（v5 口径·逐项归因）」；否则
#   「失配·须处置」（含任一 frozen 类内容变更、净增删、项数不等）。退出码 0/1。
#   注：被裁决记录过的 content_changed 重冻（如 v4→v5 合流重冻）由裁决层归因，
#   工具职责是让「无归因的内容变更」无法静默通过。
# 沿革：v4 令源（前轮留档）＝群管理员 2026-11-25 12:05:07「只重冻这一行，其余 40 项指纹
#   不动；FREEZE 版本递增 v3→v4，重出比对 0 失配。」
# 用法：python3 paper/tools/compare_freeze.py <旧 FREEZE.json> [新 FREEZE.json]
#   默认新件 = paper/evidence/FREEZE_v5preR2.json
# 口径：只比「冻结项」（记忆帐树 rows ＋ 实验帐树 rows ＋ 两套 RAG），不比 version/head/
#       时刻/说明字段——那些是重冻本身，不是冻结对象。
# 纪律：只读·0 改源文件·凭据 0 入册。
# ============================================================================
import json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NEW_DEFAULT = os.path.join(HERE, "paper/evidence/FREEZE_v5preR2.json")

LIVE_KINDS = {"live", "active"}      # 每轮重测为规例的行类
FROZEN_KINDS = {"frozen", "source", "index", "tree", "machine", "rag"}  # 内容变更即须处置


def items(d):
    """key (tree, path) -> (kind, sha12, lines, bytes)；rag 行以 rag 名为类。"""
    out = {}
    for r in d["memory_tree"]["rows"] + d["experiment_tree"]["rows"]:
        kind = r.get("kind") or ("live" if r.get("tree") == "帐树现态面" else "frozen")
        out[(r.get("tree", ""), r["path"])] = (kind, r["sha12"], r["lines"], r["bytes"])
    for r in d["rag"]:
        out[(r.get("rag", ""), r["path"])] = ("rag", r["sha12"], r["lines"], r["bytes"])
    return out


def classify(o, n):
    """返回 (attributed[], violations[], counts)；只做机械分类，不读任何外部裁决。"""
    attributed, violations = [], []
    added = [k for k in n if k not in o]
    removed = [k for k in o if k not in n]
    # 增删成对且四元组全等 → path_swap（改名互换）
    removed_left = list(removed)
    for k in added:
        pair = None
        for r in removed_left:
            if r[0] == k[0] and o[r][1:] == n[k][1:]:  # 同树·sha12/lines/bytes 全等
                pair = r
                break
        if pair is not None:
            removed_left.remove(pair)
            attributed.append({"class": "path_swap", "tree": k[0],
                               "old_path": pair[1], "new_path": k[1],
                               "sha12": n[k][1]})
        else:
            violations.append({"class": "added", "tree": k[0], "path": k[1]})
    for r in removed_left:
        violations.append({"class": "removed", "tree": r[0], "path": r[1]})
    # 同键变更
    counts = {"path_swap": 0, "kind_normalized": 0, "live_remeasured": 0,
              "content_changed": 0, "added": 0, "removed": 0}
    for a in attributed:
        counts[a["class"]] += 1
    for k in n:
        if k not in o:
            continue
        okind, osha, oln, oby = o[k]
        nkind, nsha, nln, nby = n[k]
        if (okind, osha, oln, oby) == (nkind, nsha, nln, nby):
            continue
        if osha == nsha and oln == nln and oby == nby:      # 仅 kind 字段规范化
            attributed.append({"class": "kind_normalized", "tree": k[0], "path": k[1],
                               "kind": "%s -> %s" % (okind, nkind), "sha12": nsha})
            counts["kind_normalized"] += 1
        elif nkind in LIVE_KINDS:                            # 活件行规例重测
            attributed.append({"class": "live_remeasured", "tree": k[0], "path": k[1],
                               "kind": nkind, "sha12": "%s -> %s" % (osha, nsha),
                               "lines": "%s -> %s" % (oln, nln)})
            counts["live_remeasured"] += 1
        else:                                                # frozen 类内容变更
            violations.append({"class": "content_changed", "tree": k[0], "path": k[1],
                               "kind": nkind, "sha12": "%s -> %s" % (osha, nsha)})
            counts["content_changed"] += 1
    for v in violations:
        counts[v["class"]] += 1
    return attributed, violations, counts, added, removed


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    old = json.load(open(sys.argv[1], encoding="utf-8"))
    new = json.load(open(sys.argv[2] if len(sys.argv) > 2 else NEW_DEFAULT, encoding="utf-8"))
    o, n = items(old), items(new)
    attributed, violations, counts, added, removed = classify(o, n)
    unchanged = sum(1 for k in n if k in o and o[k] == n[k])
    ok = (not violations) and set(o) == set(n)
    report = {
        "verdict_caliber": "v5",
        "old": {"version": old["version"], "head": old["head"], "items": len(o)},
        "new": {"version": new["version"], "head": new["head"], "items": len(n)},
        "item_sets_equal": set(o) == set(n),
        "counts": counts,
        "attributed": attributed,
        "violations": violations,
        "added": [{"tree": k[0], "path": k[1]} for k in added if
                  not any(a.get("new_path") == k[1] for a in attributed)],
        "removed": [{"tree": k[0], "path": k[1]} for k in removed if
                    not any(a.get("old_path") == k[1] for a in attributed)],
        "n_changed": counts["kind_normalized"] + counts["live_remeasured"] + counts["content_changed"],
        "n_unchanged": unchanged,
        "verdict": ("0 失配（v5 口径·逐项归因）" if ok else "失配·须处置"),
    }
    print(json.dumps(report, ensure_ascii=False, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
