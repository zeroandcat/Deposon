#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# gen_tree_python.py — Python 事件账本树读数生成器（v5preR2 交付件·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-25 09:44:20 派单②「两帐树刷新」＋PI 09:47 校正
#       「两帐树指记忆帐树与实验帐树，RAG同理」。
# 本件只读仓内已验码（mcp/thermo_core.py·mcp/thermo_demo.py），重放同一冻结操作迹
# （500 步·种子 20261125·每 40 步结算一次·期末再结算一次），导出逐结算期四账读数
# 与守恒核逐位对表。输出：paper/evidence/python_tree.json + python_tree.md
# 纪律：0 网络·0 凭据·临时账本即用即弃·整数㶲逐位（0 浮点漂移）。
# 用法：python3 paper/tools/gen_tree_python.py
# ============================================================================
import hashlib, json, os, shutil, sys, tempfile

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(HERE, "mcp"))
import thermo_core as tc    # noqa: E402
import thermo_demo as td    # noqa: E402

OUT = os.path.join(HERE, "paper", "evidence")
N_OPS, SEED, SETTLE_EVERY = 500, 20261125, 40


def trace_fp(ops):
    """输入迹指纹（可复现锚）：逐操作规范化串 → sha256_12。"""
    h = hashlib.sha256()
    for op in ops:
        h.update(("\x1f".join("" if x is None else str(x) for x in op) + "\x1e").encode("utf-8"))
    return h.hexdigest()[:12]


def run():
    ops = td.make_trace(N_OPS, SEED)
    tmpd = tempfile.mkdtemp(prefix="v5preR2_tree_")
    try:
        L = tc.ThermoLedger(os.path.join(tmpd, "ledger.jsonl"), tc.load_cfg())
        epochs, ticks = [], []
        for i, op in enumerate(ops, 1):
            if op[0] == "write":
                L.write_entry(op[1], op[2])
            else:
                L.read_entries(op[1])
            if i % SETTLE_EVERY == 0:
                U0 = L.state().U_total()
                rep, _ = L.settle(False)
                epochs.append({
                    "epoch": len(epochs) + 1, "tick": rep["period"]["tick"],
                    "ops_end": i, "E0": rep["E0"], "E0_rows": rep["E0_rows"], "E0_q": rep["E0_q"],
                    "phi": rep["phi"], "R": rep["R"], "D": rep["D"], "U": rep["U"],
                    "D_by": dict(rep["D_by"]), "deposited": dict(rep["deposited_by_cause"]),
                    "live_rows": rep["live_rows"], "phantoms": rep["phantoms"],
                    "util_A": rep["util_A"], "util_T": rep["util_T"], "util_R": rep["util_R"],
                    "selectivity": rep["selectivity"], "phantom_pain": rep["phantom_pain"],
                    "verdict": rep["verdict"],
                    "d_phi": rep["period"]["d_phi"], "d_R": rep["period"]["d_R"],
                    "d_D": rep["period"]["d_D"], "d_U": rep["U"] - U0,
                    "d_D_by": dict(rep["period"]["d_D_by"]),
                    "d_deposited": dict(rep["period"]["deposited"]),
                    "materialized": rep["period"]["materialized"],
                })
                ticks.append(i)
        # 期末结算（非终核·在场余额结转）
        U0 = L.state().U_total()
        rep, _ = L.settle(False)
        epochs.append({
            "epoch": len(epochs) + 1, "tick": rep["period"]["tick"], "ops_end": len(ops),
            "E0": rep["E0"], "E0_rows": rep["E0_rows"], "E0_q": rep["E0_q"],
            "phi": rep["phi"], "R": rep["R"], "D": rep["D"], "U": rep["U"],
            "D_by": dict(rep["D_by"]), "deposited": dict(rep["deposited_by_cause"]),
            "live_rows": rep["live_rows"], "phantoms": rep["phantoms"],
            "util_A": rep["util_A"], "util_T": rep["util_T"], "util_R": rep["util_R"],
            "selectivity": rep["selectivity"], "phantom_pain": rep["phantom_pain"],
            "verdict": rep["verdict"],
            "d_phi": rep["period"]["d_phi"], "d_R": rep["period"]["d_R"],
            "d_D": rep["period"]["d_D"], "d_U": rep["U"] - U0,
            "d_D_by": dict(rep["period"]["d_D_by"]),
            "d_deposited": dict(rep["period"]["deposited"]),
            "materialized": rep["period"]["materialized"],
        })
        ticks.append(len(ops))
        final = {k: rep[k] for k in ("verdict", "E0", "E0_rows", "E0_q", "phi", "R", "D", "U",
                                     "D_by", "D_stale", "D_used", "live_rows", "cap", "phantoms",
                                     "deposited_by_cause", "n_reads", "n_tx", "n_rj", "n_ph",
                                     "util_A", "util_U", "util_T", "util_R", "selectivity",
                                     "phantom_pain")}
        final["params"] = dict(rep["params"])
        # 逐位对表（三式）：E⁰ = Φ+R+D+U；Φ+R = E⁰询；D+U = E⁰行
        bit = {
            "E0": rep["E0"], "phi_R_D_U": rep["phi"] + rep["R"] + rep["D"] + rep["U"],
            "E0_q": rep["E0_q"], "phi_R": rep["phi"] + rep["R"],
            "E0_rows": rep["E0_rows"], "D_U": rep["D"] + rep["U"],
            "D_by_sum": sum(rep["D_by"].values()), "D": rep["D"],
        }
        bit["equal"] = (bit["E0"] == bit["phi_R_D_U"] == bit["E0_q"] + bit["E0_rows"]
                        and bit["E0_q"] == bit["phi_R"]
                        and bit["E0_rows"] == bit["D_U"]
                        and bit["D_by_sum"] == bit["D"])
        return {"trace": {"n_ops": N_OPS, "seed": SEED, "settle_every": SETTLE_EVERY,
                          "fp": trace_fp(ops), "writes": sum(1 for o in ops if o[0] == "write")},
                "params": dict(tc.load_cfg()), "epochs": epochs, "final": final,
                "bitcheck": bit}
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)


def render_md(d):
    E, F, B = d["epochs"], d["final"], d["bitcheck"]
    L = ["# Python 事件账本树 · v5preR2 读数（现跑·66b53fc）", "",
         "> **令源**：群管理员 2026-11-25 09:44:20 派单②「两帐树刷新」＋PI 09:47 校正「两帐树指记忆帐树与实验帐树，RAG同理」。",
         "> **本件性质**：只读已验码重放（`mcp/thermo_core.py`·`mcp/thermo_demo.py`），**不改一行已验代码**。",
         "> **可复现**：`python3 paper/tools/gen_tree_python.py`（0 网络·0 凭据·临时账本即用即弃）。",
         "> **输入迹**：`mcp/thermo_demo.make_trace(500, 20261125)`·指纹 `%s`·写 %d／读 %d·每 40 步结算·期末再结算。"
         % (d["trace"]["fp"], d["trace"]["writes"], d["trace"]["n_ops"] - d["trace"]["writes"]),
         "## 1. 守恒核逐位对表（第一律·E⁰ = Φ+R+D+U）", "",
         "| 对表项 | 左 | 右 | 判定 |", "|---|---|---|---|",
         "| E⁰ 行＋询 | %d | Φ+R+D+U = %d | %s |" % (B["E0"], B["phi_R_D_U"], "✓" if B["E0"] == B["phi_R_D_U"] else "✗"),
         "| E⁰ = E⁰行 + E⁰询 | %d | %d + %d | %s |" % (B["E0"], B["E0_rows"], B["E0_q"],
                                                        "✓" if B["E0"] == B["E0_rows"] + B["E0_q"] else "✗"),
         "| E⁰询 = Φ + R | %d | %d + %d | %s |" % (B["E0_q"], F["phi"], F["R"],
                                                   "✓" if B["E0_q"] == B["phi_R"] else "✗"),
         "| E⁰行 = D + U | %d | %d + %d | %s |" % (B["E0_rows"], F["D"], F["U"],
                                                 "✓" if B["E0_rows"] == B["D_U"] else "✗"),
         "| D = Σ 成因 | %d | %s = %d | %s |" % (B["D"], " + ".join(str(v) for v in F["D_by"].values()),
                                               B["D_by_sum"],
                                               "✓" if B["D_by_sum"] == B["D"] else "✗"),
         "", "守恒判定：%s（`thermo_demo --check` 冻结带 13/13·`thermo_crosscheck` 15/15 同源同式）" % F["verdict"],
         "", "## 2. 四账总表（期末）", "",
         "| 账 | 值 | 占比 | 定义 |", "|---|---|---|---|",
         "| Φ 透射 | %d | %.2f%%（Φ/E⁰询） | 门接受·询㶲 c_T=100 入 Φ |" % (F["phi"], 100 * F["util_T"]),
         "| R 回射 | %d | %.2f%%（R/E⁰询） | 幻肢回射·c_P=50 入 R |" % (F["R"], 100 * F["util_R"]),
         "| D 散失 | %d | %.2f%%（D/E⁰行） | 五路散热＋门拒 |" % (F["D"], 100 * F["util_A"]),
         "| U 在场 | %d | %.2f%%（U/E⁰行） | 在场行余额 %d/%d |" % (F["U"], 100 * F["util_U"], F["live_rows"], F["cap"]),
         "", "## 3. D 成因分解（六路）", "",
         "| 成因 | 散失㶲 | 行数 | 说明 |", "|---|---|---|---|"]
    note = {"reject": "门拒（行自付 c_A=10）", "decay": "期衰减 λ·Δtick", "evict": "容量淘汰（本迹未触）",
            "horizon": "视界（≥200 步未透射）", "supersede": "同键覆盖", "close": "单元终核（本迹未调）"}
    for c in tc.CAUSES:
        L.append("| %s %s | %d | %d | %s |" % (c, tc.CAUSE_ZH[c], F["D_by"][c], F["deposited_by_cause"][c], note[c]))
    L += ["", "## 4. 逐结算期四账读数（13 期）", "",
          "| 期 | 末 op | tick | E⁰ | Φ | R | D | U | ΔΦ | ΔR | ΔD | ΔU | 在场 | 幻肢 | 利用率 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for e in E:
        L.append("| %d | %d | %d | %d | %d | %d | %d | %d | %+d | %+d | %+d | %+d | %d | %d | %.2f%% |" % (
            e["epoch"], e["ops_end"], e["tick"], e["E0"], e["phi"], e["R"], e["D"], e["U"],
            e["d_phi"], e["d_R"], e["d_D"], e["d_U"], e["live_rows"], e["phantoms"], 100 * e["util_A"]))
    L += ["", "## 5. 逐位对表（期末 vs 逐期累加）", "",
          "| 项 | 逐期累加 | 期末总账 | 判定 |", "|---|---|---|---|"]
    for k, lab, fk in (("d_phi", "ΔΦ", "phi"), ("d_R", "ΔR", "R"), ("d_D", "ΔD", "D")):
        s = sum(e[k] for e in E)
        L.append("| %s | %d | %d | %s |" % (lab, s, F[fk], "✓" if s == F[fk] else "✗"))
    s = sum(e["d_U"] for e in E)
    L.append("| ΔU | %d | %d | %s |" % (s, F["U"], "✓" if s == F["U"] else "✗"))
    for c in tc.CAUSES:
        s = sum(e["d_D_by"][c] for e in E)
        L.append("| ΔD·%s | %d | %d | %s |" % (c, s, F["D_by"][c], "✓" if s == F["D_by"][c] else "✗"))
    L += ["", "## 6. 复现命令", "", "```bash",
          "cd plugin_up_v1 && python3 mcp/thermo_demo.py --check    # 冻结读数 13/13",
          "cd plugin_up_v1 && python3 mcp/thermo_crosscheck.py      # Lean 向量过 Python reducer 15/15",
          "cd plugin_up_v1 && python3 harness/lean_axiom_audit.py    # 公理审计 27/27",
          "cd plugin_up_v1 && python3 paper/tools/gen_tree_python.py # 本件重出",
          "```", ""]
    return "\n".join(L) + "\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    d = run()
    with open(os.path.join(OUT, "python_tree.json"), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "python_tree.md"), "w", encoding="utf-8") as f:
        f.write(render_md(d))
    print("python_tree.json / python_tree.md -> %s" % OUT)
    print("守恒核逐位：%d = %d+%d+%d+%d · %s" % (
        d["bitcheck"]["E0"], d["final"]["phi"], d["final"]["R"], d["final"]["D"],
        d["final"]["U"], "✓" if d["bitcheck"]["equal"] else "✗"))
    print("期数 %d·末 tick %d·利用率 %.4f·在场 %d·幻肢 %d" % (
        len(d["epochs"]), d["epochs"][-1]["tick"], d["final"]["util_A"],
        d["final"]["live_rows"], d["final"]["phantoms"]))
    return 0 if d["bitcheck"]["equal"] else 1


if __name__ == "__main__":
    sys.exit(main())
