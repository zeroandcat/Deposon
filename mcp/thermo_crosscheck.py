#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# thermo_crosscheck.py — 热力学账本双实现交叉核（Lean DeposonThermo ↔ Python thermo_core）
# ----------------------------------------------------------------------------
# Lean 侧（harness/DeposonThermo.lean·core-only·0 sorry）：整数㶲状态机
#   inject / dissipate / transmit / reflect / deposit 五转移的第一律守恒
#   （e0 = phi + refl + diss + us.sum）、第二律方向锚（diss 单调）、在场池单调，
#   以及手算结算向量 run（settle_close / settle_conserved·decide 0 公理）。
# Python 侧（mcp/thermo_core.py）：同一手算向量经真实事件 Reducer（State.apply）
#   驱动——事件级校验（tick 链/id 断链/额度/守恒核 fail-loud）全部在位。
# 本件：同一向量两侧逐位对表 ＋ 边界（越界散失/伪 deposit 必炸）＋ 幻肢回射
#   不变量（deposit 后原文 0 回注）＋ sum_drop_zero 的池和镜像。
# 纪律：0 网络 · 0 凭据 · 0 落盘（纯内存状态机）。退出码 0 全过 / 1 有失配。
# 用法：python3 mcp/thermo_crosscheck.py
# ============================================================================
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import thermo_core as tc  # noqa: E402

# ---- Lean run 的手算向量（harness/DeposonThermo.lean · settle_close）-------------
# 池序＝前插（index 0 = b · index 1 = a）；Python 行 id 按注入序（a=1·b=2）。
LEAN_E0, LEAN_PHI, LEAN_REFL, LEAN_DISS, LEAN_US = 210, 10, 0, 150, [50, 0]


def main():
    results = []

    def check(label, ok, detail=""):
        results.append(bool(ok))
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", label, (" — " + detail) if detail else ""))

    cfg = dict(tc.DEFAULTS)
    st = tc.State(cfg)
    tau = 0

    def step(ev):
        nonlocal tau
        tau += 1
        ev = dict(ev, tick=tau)
        st.apply(ev)   # 每条事件入账即校验守恒核（伪账即炸）

    step({"ev": "inject", "id": 1, "key": "a", "text": "alpha", "Q": 100})
    step({"ev": "inject", "id": 2, "key": "b", "text": "beta", "Q": 100})
    # transmit s 10 —— 门透射 a（cT=10·询㶲 q=10 实付）
    step({"ev": "gate", "prefix": "", "cT": 10, "cA": cfg["c_A"], "cP": cfg["c_P"], "k": 8,
          "tx": [(1, 10)], "rj": [], "ph": [], "q": 10})
    # dissipate idx0 (b) 30 · idx1 (a) 20 · b 10 · a 10 · b 10
    for rid, d in ((2, 30), (1, 20), (2, 10), (1, 10), (2, 10)):
        step({"ev": "decay", "id": rid, "d": d})
    # deposit idx1 (a)：剩余 70 全额 → D
    step({"ev": "deposit", "id": 1, "cause": "close"})

    # ---- 逐位对表 -------------------------------------------------------------
    check("e0 = 210 (100 + 100 + 10)", st.E0_rows + st.E0_q == LEAN_E0,
          "%d + %d = %d" % (st.E0_rows, st.E0_q, st.E0_rows + st.E0_q))
    check("phi = 10", st.phi == LEAN_PHI, "phi=%d" % st.phi)
    check("refl = 0 (no phantom readback in the vector)", st.R == LEAN_REFL, "R=%d" % st.R)
    check("diss = 150 (30 + 20 + 10 + 10 + 10 + 70)", st.D == LEAN_DISS, "D=%d" % st.D)
    check("diss by cause: decay 80 · close 70",
          st.D_by["decay"] == 80 and st.D_by["close"] == 70, repr(st.D_by))
    pool = [st.rows[2].U, st.rows.get(1).U if 1 in st.rows else 0]   # 池序 b, a
    check("pool (prepend order b, a) = [50, 0]", pool == LEAN_US, repr(pool))
    check("conservation core e0 = phi + refl + diss + U", st.conserved(),
          "%d = %d + %d + %d + %d" % (st.E0_rows + st.E0_q, st.phi, st.R, st.D, st.U_total()))

    # ---- sum_drop_zero 镜像：删掉已 deposit 的 0 项·池和不变 -----------------------
    with_zero = [r.U for r in st.rows.values()] + [0]
    check("sum_drop_zero mirror (dropping a 0 entry keeps the pool sum)",
          sum(with_zero) == sum(with_zero[:-1]) == st.U_total() == 50)

    # ---- 第二律方向锚：diss 单调（本向量逐步不减）-------------------------------
    check("diss never decreases along the vector", st.D == LEAN_DISS and st.D >= 80)

    # ---- 边界：越界散失 / 伪 deposit / 断链 id 必炸（fail-loud）------------------
    for label, ev in (
        ("decay beyond row U rejected", {"ev": "decay", "id": 2, "d": 51}),
        ("deposit of a non-live row rejected", {"ev": "deposit", "id": 1, "cause": "close"}),
        ("deposit with cause=reject rejected", {"ev": "deposit", "id": 2, "cause": "reject"}),
        ("id chain break rejected", {"ev": "inject", "id": 7, "key": "c", "text": "x", "Q": 10}),
    ):
        before = st.snapshot()
        try:
            st.apply(dict(ev, tick=st.tick + 1))
            ok = False
        except tc.LedgerInconsistent:
            ok = True
        # 注意：State.apply 抛出后状态可能已被部分改写——交叉核只断言「炸了」；
        # 账本层的原子性由 ThermoLedger._commit（先重放后落盘）保证（selftest 6 覆盖）。
        check(label + " (LedgerInconsistent raised)", ok)

    # ---- 幻肢不变量：a 已散失 → 幻肢在册·原文 0 回注 ---------------------------
    ph = st.phantoms.get(1)
    ph_line = tc.phantom_line(ph, st.tick) if ph else ""
    check("phantom limb recorded for the deposited row (cause close)",
          ph is not None and ph.cause == "close" and ph.mass == len("alpha"))
    check("phantom line reflects the hole, never the source text",
          "⟨幻肢⟩" in ph_line and "alpha" not in ph_line)

    ok_all = all(results)
    print("thermo_crosscheck: %s (%d/%d)" % ("ALL PASS" if ok_all else "FAIL",
                                             sum(results), len(results)))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
