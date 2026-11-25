#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F2 分支修复棒 · 两侧自测（scratch · .tmp/ · 非交付件）

目的：证明「修复前恒不触发 / 修复后可触发」两侧（PI 授权棒验收项）。
方法：importlib **只读加载**三件 executor（三件均 `if __name__ == "__main__"` 守卫 ⇒ 载入 0 跑正式读数），
      对 `judge_K_V3R_26` 逐格构造调用。

硬约束：
  - 0 调用 main()          ⇒ 0 正式新读数
  - 0 写任何件（含 OUT）    ⇒ 0 判定 / 0 派生 JSON
  - 0 网络 / 0 LLM
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "results"))

GAMMA_RB = "判据面恒定 ⇒ PASS 侧全域消失 ⇒ 判别力归零（读法乙结构性来源）"
NDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
STDS = [0.0, 1e-12, 0.5, 1.0, 2.5]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, REPO / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # 仅定义常量与函数；main() 受 __main__ 守卫
    return mod


def norm_orig(mod, nd, std):
    v, hit, br = mod.judge_K_V3R_26(nd, std)
    return {"verdict": v, "hit": bool(hit), "gamma": None, "branch": br}


def norm_new(mod, nd, std):
    d = mod.judge_K_V3R_26(nd, std)
    return {"verdict": d["new_verdict"], "hit": bool(d["kill_line_fail_hit"]),
            "gamma": d["gamma_root_cause"], "branch": d["branch_id"]}


def main() -> int:
    orig = load("x_orig", "results/_v3_recheck_26b_executor_2026_09_27.py")
    r2 = load("x_r2", "results/_v3_recheck_26b_executor_r2_2026_09_28.py")
    r3 = load("x_r3", "results/_v3_recheck_26b_executor_r3_2026_09_29.py")

    cells = [(nd, s) for nd in NDS for s in STDS]
    f2_cells = [(nd, s) for (nd, s) in cells if nd > 3 and s > 0.0]
    non_f2 = [(nd, s) for (nd, s) in cells if not (nd > 3 and s > 0.0)]
    print("网格 %d 格（nd∈%s × std∈%s）；F2 域 %d 格；非 F2 域 %d 格"
          % (len(cells), NDS, STDS, len(f2_cells), len(non_f2)))

    # ---------- 侧①：修复前（原件 5c906113a210）F2 域恒不触发 ----------
    o_pass = o_fail = 0
    o_hits = set()
    for nd, s in f2_cells:
        r = norm_orig(orig, nd, s)
        o_hits.add((r["verdict"], r["hit"]))
        o_pass += r["verdict"] == "PASS"
        o_fail += r["verdict"] == "FAIL"
    print("\n[侧① 修复前 · 原件 5c906113a210] F2 域 %d 格：PASS=%d FAIL=%d；输出集合=%s"
          % (len(f2_cells), o_pass, o_fail, sorted(o_hits)))
    before_ok = (o_fail == 0 and o_pass == len(f2_cells)
                 and o_hits == {("PASS", False)})
    print("[侧①] 判定：原件 F2 分支**恒不触发**读法乙应出的 FAIL（%s）"
          % ("✅ 成立" if before_ok else "❌ 不成立"))

    # ---------- 侧②：修复后（r3 6c83e7a7ca2e）F2 域可触发 ----------
    r_fail = r_pass = r_gamma_ok = 0
    r_branches = set()
    for nd, s in f2_cells:
        r = norm_new(r3, nd, s)
        r_branches.add(r["branch"])
        r_fail += r["verdict"] == "FAIL"
        r_pass += r["verdict"] == "PASS"
        r_gamma_ok += (r["gamma"] == GAMMA_RB and r["hit"] is True)
    after_ok = (r_fail == len(f2_cells) and r_pass == 0
                and r_gamma_ok == len(f2_cells)
                and r_branches == {"READING_B_V2_ROW3_ND_GT_3_AND_STD_GT_0"})
    print("\n[侧② 修复后 · r3 6c83e7a7ca2e] F2 域 %d 格：FAIL=%d PASS=%d；γ 合规=%d；branch=%s"
          % (len(f2_cells), r_fail, r_pass, r_gamma_ok, sorted(r_branches)))
    print("[侧②] 判定：F2 分支**可触发**（FAIL + K-V5RB-0-D 强制 γ）（%s）"
          % ("✅ 成立" if after_ok else "❌ 不成立"))

    # ---------- 侧③：全域 0 PASS（读法乙 v2：读数域内无任何 PASS 档） ----------
    g3_pass = sum(norm_new(r3, nd, s)["verdict"] == "PASS" for nd, s in cells)
    print("\n[侧③] r3 全域 %d 格 PASS 数 = %d（读法乙 v2 要求 0）%s"
          % (len(cells), g3_pass, "✅" if g3_pass == 0 else "❌"))

    # ---------- 侧④：非 F2 三域 r2 ≡ r3（0 被动摇） ----------
    diff = [c for c in non_f2 if norm_new(r2, *c) != norm_new(r3, *c)]
    print("[侧④] 非 F2 域 %d 格 r2≡r3：差异 %d %s"
          % (len(non_f2), len(diff), "✅" if not diff else "❌ %s" % diff[:3]))

    # ---------- 侧⑤：原件 F2 域 vs r3 域 = 唯一差异面（逐格对照） ----------
    same = [c for c in f2_cells
            if norm_orig(orig, *c)["verdict"] == norm_new(r3, *c)["verdict"]]
    print("[侧⑤] F2 域 %d 格中「原件与 r3 同档」格数 = %d（应 0；原件全 PASS、r3 全 FAIL）%s"
          % (len(f2_cells), len(same), "✅" if not same else "❌"))

    # ---------- 侧⑥：阈值/构造常量逐字未动（0 新设阈值） ----------
    names = ["SEED", "N_BUDGET", "JITTER", "N_CELLS", "CLASSES", "PRIORITY", "TOL",
             "O1_MAX_STEP", "O3_S", "O3_CAP", "O5_DT", "O5_CAP", "O5_C",
             "KV3R_26_PASS_N_DISTINCT_MIN", "KV3R_26_FAIL_N_DISTINCT_MAX",
             "DEGEN_N_DISTINCT_MIN", "DEGEN_STD_MIN_EXCL", "KILL_LINE_LITERAL", "TH_LITERAL"]
    const_bad = []
    for mod, tag in ((r2, "r2"), (r3, "r3")):
        for n in names:
            if hasattr(mod, n) and hasattr(orig, n) and getattr(mod, n) != getattr(orig, n):
                const_bad.append((tag, n, getattr(orig, n), getattr(mod, n)))
    print("[侧⑥] 常量比对 %d 项 ×（原件 vs r2/r3）：差异 %d %s"
          % (len(names), len(const_bad), "✅ 0 新设阈值" if not const_bad else "❌ %s" % const_bad))

    # ---------- 侧⑦：KD 显式拦截（std 非有限 ⇒ 不静默归入分支 B） ----------
    for tag, mod, fn in (("原件", orig, norm_orig), ("r3", r3, norm_new)):
        try:
            fn(mod, 9, float("nan"))
            print("[侧⑦] %s std=nan：返回 %s（原件按字面空档返回，r3 应拦截）" % (tag, "?"))
        except SystemExit as e:
            print("[侧⑦] r3 std=nan：SystemExit 显式拦截（KD 面）✅ str=%s" % str(e)[:40])
        except Exception as e:
            print("[侧⑦] %s std=nan：%s: %s" % (tag, type(e).__name__, e))

    # ---------- 侧⑧：盘上 19:08 真实读数（只读复核 F2 确在正式跑中触发） ----------
    j = json.loads((REPO / "results/_v3_recheck_26b_r3_result_2026_09_29.json")
                   .read_text(encoding="utf-8"))
    print("\n[侧⑧] 19:08 真实读数 c9d3c9f819f1（只读）：")
    for o, rec in j["per_ontology"].items():
        r = rec["criteria_evidence"]["rates"]
        print("      %-34s n=%d std=%.6g -> %s | branch=%s | legacy=%s | γ=%s"
              % (o, r["n_distinct"], r["std"], rec["new_verdict"],
                 rec["kill_line_branch_id"], rec["legacy_verdict"], rec["gamma_root_cause"]))
    print("      档位 = %s" % j["three_ontology_summary"]["hit_tier_all_same"])

    ok = before_ok and after_ok and g3_pass == 0 and not diff and not same and not const_bad
    print("\n[自测总判定] 两侧成立 = %s" % ("✅ 全部通过" if ok else "❌ 有失败项"))
    print("[边界声明] 本自测 0 调用 main()、0 落派生 JSON、0 出判定、0 网络 / 0 LLM。")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
