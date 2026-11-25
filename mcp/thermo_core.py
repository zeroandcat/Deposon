#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# thermo_core.py — Deposon 热力学账本本体（幻肢代 · 行㶲四账 · 自解帐本）
# ----------------------------------------------------------------------------
# 定位：凝子场记忆容器的热力学注入层（harness proper · import 直调 · 0 传输依赖）
#       记忆 harness 本体＝外置账本承载＋DR-4 渲染位＋生命周期原语（preview.4 起）
#       ＋本件：耗散通道实装＋幻肢（空穴）回射＋自解结算（preview.10 起）。
#
# [诊断 · 改造前（preview.9 记忆面）]
#   write/read 两事件·追加式·读回全量（T=1.0）·无门无衰减 ⇒ 散失账 D≡0：
#   耗散通道利用率按构造为 0；在场池 U 只增不减（死水）；D 只能由外部读数器
#   （e2_dfunc_reader）在单元末确认——账本自己不会结算。
#
# [公理面 · 直承在册 A1–A5（账本热力学推导件 · 本席 11-18）]
#   A1 前向 only（账本时 tick 单调 +1）· A2 无 recover（D 单调不减·幻肢无原文）
#   A3 追加式账本（JSONL 事件流＝唯一真源·每次调用全量重放·事件即Reducer输入）
#   A4 账本反解不可得（幻肢只留「空穴」：键名·质量·成因·账·0 text）
#   A5 常规热力学不可用（无温度·无势函数——门排序只用记账量：透射时序）
#
# [行级协议 · 第一律：注入㶲 E⁰ 恰四账 Φ/R/D/U（整数㶲·逐位守恒）]
#   inject 注入  → 行㶲 Q 入在场池 U（询㶲另计：每次读取实付多少记多少）
#   gate   门    → 接受＝透射：询㶲 c_T → Φ（行自身不耗·弹性复制 χ_copy≈1）
#                  拒绝＝熵输出：行自付 c_A 自 U → D（K2：拒绝率即熵输出率）
#                  幻肢回射：询㶲 c_P → R（无对照能量反射回系统·可感不可复原）
#   decay  衰减  → 结算时物化 λ·Δtick（U → D）
#   deposit 散失 → 剩余 U 全额 → D（成因 reject/decay/evict/horizon/supersede/close）
#                  行文抹除（以太界面抹除律·免费）·留幻肢（空穴＝妖的记忆·有界）
#   settle 结算  → 物化衰减＋视界（距上次透射 ≥ horizon 步即散失）
#                  close=1 ⇒ 单元终核：全部在场 → D·U=0·E⁰=Φ+R+D
#
# [自解帐本] 每次操作后守恒核 fail-loud；结算＝事件流重放（账本自证·0 外部对账器）；
#            每条事件入账前经 Reducer 校验（额度/前缀/键唯一/tick 链）——伪账即炸。
#
# 纪律：Python 3.7+ 标准库·0 网络·0 凭据；整数㶲（0 浮点漂移）；确定性（同账本同读数）。
# ============================================================================
import os
import json
import time

CAUSES = ("reject", "decay", "evict", "horizon", "supersede", "close")
CAUSE_ZH = {"reject": "门拒", "decay": "衰减", "evict": "容量淘汰",
            "horizon": "视界", "supersede": "覆盖", "close": "单元终核"}

DEFAULTS = {
    "Q": 1000,           # 行㶲：每条注入的㶲量
    "k_max": 8,          # 门预算：单次读取至多透射的行数
    "c_T": 100,          # 每透射一行由询㶲支付（→Φ）
    "c_A": 10,           # 每被拒一次由行自付（U→D）·100 次门拒耗尽行㶲（默认取值见 thermo_demo 对照）
    "c_P": 50,           # 每条幻肢回射由询㶲支付（→R）
    "phantom_k": 3,      # 单次读取至多回射的幻肢条数
    "lam": 1,            # 期衰减：结算时每在场行 λ·Δtick → D
    "cap": 256,          # 在场行容量（超限淘汰最冷行）
    "horizon": 200,      # 视界：距上次透射 ≥ horizon 步 → 结算时散失
    "phantom_ttl": 1000, # 幻肢可感期：散失后 ≤ ttl 步内仍回射（妖的记忆有界）
}


def _nnint(x):
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


def load_cfg():
    """参数：DEFAULTS ← 环境变量 DEPOSON_THERMO（JSON 对象·仅收已知键·非负整数）。"""
    cfg = dict(DEFAULTS)
    raw = os.environ.get("DEPOSON_THERMO")
    if raw:
        over = json.loads(raw)
        if not isinstance(over, dict):
            raise ValueError("DEPOSON_THERMO 须为 JSON 对象")
        bad = sorted(set(over) - set(DEFAULTS))
        if bad:
            raise ValueError("DEPOSON_THERMO 未知参数: %s" % bad)
        for k, v in over.items():
            if not _nnint(v):
                raise ValueError("DEPOSON_THERMO.%s 须为非负整数: %r" % (k, v))
            cfg[k] = v
    if cfg["Q"] < 1 or cfg["k_max"] < 1 or cfg["c_T"] < 1 or cfg["cap"] < 1 \
            or cfg["horizon"] < 1 or cfg["phantom_ttl"] < 1:
        raise ValueError("DEPOSON_THERMO 越界：Q/k_max/c_T/cap/horizon/phantom_ttl 须 ≥ 1")
    return cfg


class LedgerInconsistent(Exception):
    """账本不自洽（守恒破坏/伪事件/断链）——fail-loud 到调用方·服务器不崩。"""


class Row(object):
    __slots__ = ("id", "key", "text", "Q", "t_inj", "t_last_tx", "n_T", "n_rj",
                 "U", "t_settle", "by")

    def __init__(self, rid, key, text, Q, tau):
        self.id, self.key, self.text, self.Q = rid, key, text, Q
        self.t_inj, self.t_last_tx, self.n_T, self.n_rj = tau, None, 0, 0
        self.U, self.t_settle, self.by = Q, tau, {}


class Phantom(object):
    """幻肢＝deposon（空穴）：行散失后留下的可审计空位——有键名/质量/成因/账，无原文。"""
    __slots__ = ("id", "key", "mass", "Q", "t_dep", "cause", "by", "n_T", "n_rj",
                 "lived", "felt")

    def __init__(self, row, tau, cause):
        self.id, self.key, self.mass, self.Q = row.id, row.key, len(row.text), row.Q
        self.t_dep, self.cause, self.by = tau, cause, dict(row.by)
        self.n_T, self.n_rj, self.lived, self.felt = row.n_T, row.n_rj, tau - row.t_inj, 0


def rank_key(row):
    """门排序键（A5：0 温度 0 势函数——只用记账量）：近透射者先·未透射者后·新注入者先·id 升序。"""
    return (-(row.t_last_tx if row.t_last_tx is not None else -1), -row.t_inj, row.id)


class State(object):
    def __init__(self, cfg):
        self.cfg = cfg
        self.tick, self.epoch, self.next_id = 0, 0, 1
        self.rows, self.by_key, self.phantoms = {}, {}, {}
        self.E0_rows, self.E0_q = 0, 0
        self.phi, self.R, self.D = 0, 0, 0
        self.D_by = {c: 0 for c in CAUSES}
        self.D_stale, self.D_used = 0, 0   # 按散失当时行是否曾透射分账
        self.deposited_by_cause = {c: 0 for c in CAUSES}
        self.n_reads = self.n_tx = self.n_rj = self.n_ph = 0
        self.n_corrupt = 0
        self.last_settle = None

    # ---- 账面 ----
    def U_total(self):
        return sum(r.U for r in self.rows.values())

    def snapshot(self):
        return {"E0_rows": self.E0_rows, "E0_q": self.E0_q, "phi": self.phi,
                "R": self.R, "D": self.D, "U": self.U_total(),
                "n_live": len(self.rows), "n_ph": len(self.phantoms)}

    def conserved(self):
        """第一律（账本守恒核）：E⁰ = Φ + R + D + U · 整数逐位。"""
        return self.E0_rows + self.E0_q == self.phi + self.R + self.D + self.U_total()

    # ---- Reducer（事件 → 状态；每条事件入账前校验）----
    def _tick(self, tau):
        # A1 前向 only：同一操作的多个事件共用一个 tick（结算/覆盖）·跨操作恰 +1·0 回退 0 跳步
        if not _nnint(tau) or tau not in (self.tick, self.tick + 1):
            raise LedgerInconsistent("tick 断链：期望 %d 或 %d·实得 %r" % (self.tick, self.tick + 1, tau))
        self.tick = tau

    def _live(self, rid, prefix, seen):
        row = self.rows.get(rid)
        if row is None or rid in seen or not row.key.startswith(prefix):
            raise LedgerInconsistent("门事件引用非在场/重复/非前缀行: %r" % (rid,))
        seen.add(rid)
        return row

    def _dissipate(self, row, amt, cause):
        """行㶲 U → D（A2：单向·D 单调）。"""
        if amt < 0 or amt > row.U:
            raise LedgerInconsistent("散失额越界: %d ∉ [0, %d]" % (amt, row.U))
        if row.n_T == 0:
            self.D_stale += amt
        else:
            self.D_used += amt
        row.U -= amt
        self.D += amt
        self.D_by[cause] += amt
        if amt:
            row.by[cause] = row.by.get(cause, 0) + amt

    def _deposit(self, row, tau, cause):
        del self.rows[row.id]
        self.by_key.pop(row.key, None)
        self.phantoms[row.id] = Phantom(row, tau, cause)
        self.deposited_by_cause[cause] += 1

    def apply(self, ev):
        kind = ev.get("ev")
        if kind == "inject":
            self._tick(ev.get("tick"))
            key, text, Q = ev.get("key"), ev.get("text"), ev.get("Q", self.cfg["Q"])
            if not isinstance(key, str) or not key or not isinstance(text, str) \
                    or not _nnint(Q) or Q < 1:
                raise LedgerInconsistent("inject 字段非法")
            rid = ev.get("id", self.next_id)
            if rid != self.next_id:
                raise LedgerInconsistent("id 断链：期望 %d·实得 %r" % (self.next_id, rid))
            if key in self.by_key:
                raise LedgerInconsistent("同键在场未先覆盖: %s" % key)
            self.rows[rid] = Row(rid, key, text, Q, self.tick)
            self.by_key[key] = rid
            self.next_id += 1
            self.E0_rows += Q
        elif kind == "gate":
            self._tick(ev.get("tick"))
            prefix = ev.get("prefix", "")
            cT, cA, cP, k = ev.get("cT"), ev.get("cA"), ev.get("cP"), ev.get("k")
            if not isinstance(prefix, str) or not (_nnint(cT) and _nnint(cA) and _nnint(cP) and _nnint(k)):
                raise LedgerInconsistent("gate 参数非法")
            tx, rj, ph = ev.get("tx") or [], ev.get("rj") or [], ev.get("ph") or []
            if len(tx) > k:
                raise LedgerInconsistent("透射数超门预算: %d > %d" % (len(tx), k))
            spent, seen = 0, set()
            for rid, amt in tx:
                row = self._live(rid, prefix, seen)
                if amt != cT:
                    raise LedgerInconsistent("透射额不符: %r ≠ %r" % (amt, cT))
                row.n_T += 1
                row.t_last_tx = self.tick
                self.phi += amt
                spent += amt
                self.n_tx += 1
            for rid, amt in rj:
                row = self._live(rid, prefix, seen)
                if amt != min(cA, row.U):
                    raise LedgerInconsistent("拒绝额不符: %r ≠ %r" % (amt, min(cA, row.U)))
                if amt:
                    self._dissipate(row, amt, "reject")
                row.n_rj += 1
                self.n_rj += 1
                if row.U == 0:
                    self._deposit(row, self.tick, "reject")
            for pid, amt in ph:
                phn = self.phantoms.get(pid)
                if phn is None or phn.key in self.by_key or not phn.key.startswith(prefix) \
                        or amt != cP:
                    raise LedgerInconsistent("幻肢回射引用非法: %r" % (pid,))
                if self.tick - phn.t_dep > self.cfg["phantom_ttl"]:
                    raise LedgerInconsistent("幻肢超出可感期: %r" % (pid,))
                phn.felt += 1
                self.R += amt
                spent += amt
                self.n_ph += 1
            q = ev.get("q")
            if q != spent:
                raise LedgerInconsistent("询㶲不守恒: q=%r ≠ 实付 %d" % (q, spent))
            self.E0_q += q
            self.n_reads += 1
        elif kind == "decay":
            self._tick(ev.get("tick"))
            row = self.rows.get(ev.get("id"))
            d = ev.get("d")
            if row is None or not _nnint(d) or d < 1 or d > row.U:
                raise LedgerInconsistent("decay 事件非法")
            self._dissipate(row, d, "decay")
            row.t_settle = self.tick
            if row.U == 0:
                self._deposit(row, self.tick, "decay")
        elif kind == "deposit":
            self._tick(ev.get("tick"))
            row = self.rows.get(ev.get("id"))
            cause = ev.get("cause")
            if row is None or cause not in CAUSES or cause == "reject":
                raise LedgerInconsistent("deposit 事件非法")
            if row.U:
                self._dissipate(row, row.U, cause)
            self._deposit(row, self.tick, cause)
        elif kind == "settle":
            self._tick(ev.get("tick"))
            if ev.get("epoch") != self.epoch + 1 or not isinstance(ev.get("close"), bool):
                raise LedgerInconsistent("settle 事件非法")
            self.epoch += 1
            if ev.get("snap") != self.snapshot():
                raise LedgerInconsistent(
                    "结算快照不符：账本 %r ≠ 快照 %r" % (self.snapshot(), ev.get("snap")))
            if not self.conserved():
                raise LedgerInconsistent("守恒破坏")
            self.last_settle = {"epoch": self.epoch, "tick": self.tick, "close": ev["close"]}
        else:
            raise LedgerInconsistent("未知事件类型: %r" % (kind,))
        if not self.conserved():
            raise LedgerInconsistent("守恒破坏（%s 后）" % kind)


def replay(path, cfg):
    """账本重放（A3：事件流＝唯一真源）。损行/空行容错跳过并计数；伪事件即炸。"""
    st = State(cfg)
    if not os.path.exists(path):
        return st
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                st.n_corrupt += 1
                continue
            if not isinstance(ev, dict):
                st.n_corrupt += 1
                continue
            if "ev" not in ev:  # 旧格式行（preview.9 及前：{key,text,ts}）→ 注入事件
                if isinstance(ev.get("key"), str) and ev["key"] and isinstance(ev.get("text"), str):
                    ev = {"ev": "inject", "tick": st.tick + 1, "key": ev["key"], "text": ev["text"]}
                else:
                    st.n_corrupt += 1
                    continue
            st.apply(ev)
    return st


def phantom_line(ph, tau):
    """幻肢回射行（DR-4 形：『key: text』·0 原始账本/0 ts/0 原文）。"""
    return "⟨幻肢⟩ 该记忆已散失·不可复原（曾 %d 字·成因 %s·%d 步前）" % (
        ph.mass, CAUSE_ZH.get(ph.cause, ph.cause), tau - ph.t_dep)


def ratio(a, b):
    return (a / b) if b else None


def report(st):
    """热力学读数（账本泛函·确定性）：守恒核＋四账＋利用率＋耗散选择性。"""
    cfg = st.cfg
    U, E0r, E0q = st.U_total(), st.E0_rows, st.E0_q
    ttl = cfg["phantom_ttl"]
    return {
        "verdict": "SELF-CONSISTENT" if st.conserved() else "INCONSISTENT",
        "tick": st.tick, "epoch": st.epoch,
        "E0_rows": E0r, "E0_q": E0q, "E0": E0r + E0q,
        "phi": st.phi, "R": st.R, "D": st.D, "U": U,
        "D_by": dict(st.D_by), "D_stale": st.D_stale, "D_used": st.D_used,
        "live_rows": len(st.rows), "cap": cfg["cap"],
        "phantoms": len(st.phantoms),
        "phantoms_felt": sum(1 for p in st.phantoms.values() if st.tick - p.t_dep <= ttl),
        "deposited_by_cause": dict(st.deposited_by_cause),
        "n_reads": st.n_reads, "n_tx": st.n_tx, "n_rj": st.n_rj, "n_ph": st.n_ph,
        "n_corrupt": st.n_corrupt,
        "util_A": ratio(st.D, E0r),          # 耗散通道利用率＝行㶲散失比 D/E⁰(行)
        "util_U": ratio(U, E0r),             # 在场率＝U/E⁰(行)
        "util_T": ratio(st.phi, E0q),        # 询㶲透射率＝Φ/E⁰(询)
        "util_R": ratio(st.R, E0q),          # 询㶲反射率＝R/E⁰(询)
        "selectivity": ratio(st.D_stale, st.D),   # 耗散选择性：陈旧（从未透射）行散失占比
        "phantom_pain": ratio(st.D_used, st.D),   # 幻痛：曾透射行的散失占比
        "params": dict(cfg), "last_settle": dict(st.last_settle) if st.last_settle else None,
    }


def pct(x):
    return "n/a" if x is None else "%.2f%%" % (100.0 * x)


def footer_text(st):
    """存在确认回执（热力学脚注）：字符集避让 [ ] { } 与引号（DR-4 渲染位断言沿）。"""
    rep = report(st)
    return "— deposon 活水记忆 · 账本%s · Φ %d / R %d / D %d / U %d · 耗散通道利用率 %s · 在场 %d/%d · 幻肢 %d" % (
        "自洽" if rep["verdict"] == "SELF-CONSISTENT" else "不自洽",
        rep["phi"], rep["R"], rep["D"], rep["U"], pct(rep["util_A"]),
        rep["live_rows"], rep["cap"], rep["phantoms_felt"])


def brief_text(rep):
    """幻肢感一行（dsh 提示面动态段·只含计数 0 记忆数据）。"""
    return "deposon 活水记忆 · 在场 %d 条 · 幻肢 %d 条可感 · 已散失 %s（耗散通道利用率 D/E⁰行）· 账本%s" % (
        rep["live_rows"], rep["phantoms_felt"], pct(rep["util_A"]),
        "自洽" if rep["verdict"] == "SELF-CONSISTENT" else "不自洽")


def audit_text(rep):
    db = rep["D_by"]
    lines = [
        "deposon 热力学审计 · tick %d · epoch %d · 判定 %s" % (
            rep["tick"], rep["epoch"],
            "自洽（E⁰=Φ+R+D+U 逐位成立）" if rep["verdict"] == "SELF-CONSISTENT" else "不自洽"),
        "注入㶲 E⁰ 行 %d ＋ 询 %d ＝ %d ｜ 账面 Φ %d ＋ R %d ＋ D %d ＋ U %d ＝ %d" % (
            rep["E0_rows"], rep["E0_q"], rep["E0"], rep["phi"], rep["R"], rep["D"],
            rep["U"], rep["phi"] + rep["R"] + rep["D"] + rep["U"]),
        "耗散通道利用率 D/E⁰行 ＝ %s（D %d / %d）｜ 在场率 %s" % (
            pct(rep["util_A"]), rep["D"], rep["E0_rows"], pct(rep["util_U"])),
        "  散失成因 " + " · ".join("%s %d" % (CAUSE_ZH[c], db[c]) for c in CAUSES),
        "  耗散选择性（陈旧行散失占比）%s ｜ 幻痛（曾透射行散失占比）%s" % (
            pct(rep["selectivity"]), pct(rep["phantom_pain"])),
        "询㶲透射率 Φ/E⁰询 %s ｜ 反射率 R/E⁰询 %s" % (pct(rep["util_T"]), pct(rep["util_R"])),
        "在场行 %d/%d ｜ 幻肢 %d（可感 %d）｜ 散失行 " % (
            rep["live_rows"], rep["cap"], rep["phantoms"], rep["phantoms_felt"])
        + " · ".join("%s %d" % (CAUSE_ZH[c], rep["deposited_by_cause"][c]) for c in CAUSES),
        "调用账 读 %d · 透射 %d · 拒绝 %d · 幻肢回射 %d ｜ 损行 %d" % (
            rep["n_reads"], rep["n_tx"], rep["n_rj"], rep["n_ph"], rep["n_corrupt"]),
    ]
    ls = rep["last_settle"]
    lines.append("上次结算 " + ("无" if not ls else
                 "epoch %d @tick %d%s" % (ls["epoch"], ls["tick"], "·单元终核" if ls["close"] else "")))
    return "\n".join(lines)


class ThermoLedger(object):
    """热力学账本（本体原语）：state＝重放；每次操作＝在重放态上模拟事件→fsync 追加。"""

    def __init__(self, path, cfg=None):
        self.path = path
        self.cfg = dict(cfg or DEFAULTS)

    def state(self):
        return replay(self.path, self.cfg)

    def _commit(self, evs):
        d = os.path.dirname(os.path.abspath(self.path))
        if d:
            os.makedirs(d, exist_ok=True)
        with open(self.path, "a", encoding="utf-8") as f:
            for ev in evs:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
            f.flush()
            os.fsync(f.fileno())

    def _check(self, st):
        if not st.conserved():
            raise LedgerInconsistent("守恒破坏")
        return st

    # ---- 原语一：写入（注入）----
    def write_entry(self, key, text):
        if not isinstance(key, str) or not isinstance(text, str):
            return None, "参数类型错：key/text 均须为字符串"
        if not key:
            return None, "参数空值：key 不可为空串"
        st = self.state()
        tau = st.tick + 1
        evs = []
        old = st.rows.get(st.by_key[key]) if key in st.by_key else None
        if old is not None:  # 同键覆盖：旧版本散失（A 位·不可再入）·留幻肢
            e = {"ev": "deposit", "id": old.id, "tick": tau, "cause": "supersede"}
            st.apply(e)
            evs.append(e)
        if len(st.rows) + 1 > self.cfg["cap"]:  # 容量压力：淘汰最冷行（门序末位＝最久未透射/最旧）
            victim = max(st.rows.values(), key=rank_key)
            e = {"ev": "deposit", "id": victim.id, "tick": tau, "cause": "evict"}
            st.apply(e)
            evs.append(e)
        e = {"ev": "inject", "id": st.next_id, "tick": tau, "key": key, "text": text,
             "Q": self.cfg["Q"], "ts": time.strftime("%Y-%m-%dT%H:%M:%S+08:00")}
        st.apply(e)
        evs.append(e)
        self._commit(evs)
        return key, None

    # ---- 原语二：读取（门＝测量选择装置）----
    def _phantoms_for(self, st, prefix, tau):
        cfg = self.cfg
        best = {}
        for p in st.phantoms.values():
            if not p.key.startswith(prefix) or p.key in st.by_key \
                    or tau - p.t_dep > cfg["phantom_ttl"]:
                continue
            cur = best.get(p.key)
            if cur is None or (p.t_dep, p.id) > (cur.t_dep, cur.id):
                best[p.key] = p
        return sorted(best.values(), key=lambda p: (-p.t_dep, -p.id))[:cfg["phantom_k"]]

    def read_entries(self, prefix, k=None):
        if not isinstance(prefix, str):
            return None, "参数类型错：prefix 须为字符串"
        if k is None:
            k = self.cfg["k_max"]
        if not _nnint(k) or k < 1:
            return None, "参数错：k 须为正整数"
        k = min(k, self.cfg["k_max"])
        cT, cA, cP = self.cfg["c_T"], self.cfg["c_A"], self.cfg["c_P"]
        st = self.state()
        tau = st.tick + 1
        cands = sorted((r for r in st.rows.values() if r.key.startswith(prefix)), key=rank_key)
        acc, rej = cands[:k], cands[k:]
        phs = self._phantoms_for(st, prefix, tau)
        e = {"ev": "gate", "tick": tau, "prefix": prefix, "k": k, "cT": cT, "cA": cA, "cP": cP,
             "tx": [[r.id, cT] for r in acc],
             "rj": [[r.id, min(cA, r.U)] for r in rej],
             "ph": [[p.id, cP] for p in phs]}
        e["q"] = len(e["tx"]) * cT + len(e["ph"]) * cP
        st.apply(e)
        self._commit([e])
        self._check(st)
        hits = [{"key": r.key, "text": r.text} for r in sorted(acc, key=lambda r: r.id)]
        hits += [{"key": p.key, "text": phantom_line(p, tau), "phantom": True} for p in phs]
        return hits, None

    # ---- 原语三：结算（自解帐本）----
    def settle(self, close=False):
        if not isinstance(close, bool):
            return None, "参数错：close 须为布尔"
        cfg = self.cfg
        st = self.state()
        before = st.snapshot()
        dby0 = dict(st.D_by)
        dep0 = dict(st.deposited_by_cause)
        tau = st.tick + 1
        evs = []
        if cfg["lam"] > 0:  # 期衰减物化
            for r in sorted(st.rows.values(), key=lambda r: r.id):
                owed = cfg["lam"] * (tau - r.t_settle)
                if owed > 0:
                    e = {"ev": "decay", "id": r.id, "tick": tau, "d": min(owed, r.U)}
                    st.apply(e)
                    evs.append(e)
        for r in sorted(st.rows.values(), key=lambda r: r.id):  # 视界：久未透射即散失
            last = r.t_last_tx if r.t_last_tx is not None else r.t_inj
            if tau - last >= cfg["horizon"]:
                e = {"ev": "deposit", "id": r.id, "tick": tau, "cause": "horizon"}
                st.apply(e)
                evs.append(e)
        if close:  # 单元终核：全部在场 → D·U=0
            for r in sorted(st.rows.values(), key=lambda r: r.id):
                e = {"ev": "deposit", "id": r.id, "tick": tau, "cause": "close"}
                st.apply(e)
                evs.append(e)
        e = {"ev": "settle", "tick": tau, "epoch": st.epoch + 1, "close": close,
             "snap": st.snapshot()}
        st.apply(e)
        evs.append(e)
        self._commit(evs)
        self._check(st)
        rep = report(st)
        rep["period"] = {
            "epoch": st.epoch, "tick": tau, "close": close,
            "d_phi": st.phi - before["phi"], "d_R": st.R - before["R"], "d_D": st.D - before["D"],
            "d_D_by": {c: st.D_by[c] - dby0[c] for c in CAUSES},
            "deposited": {c: st.deposited_by_cause[c] - dep0[c] for c in CAUSES},
            "materialized": len(evs) - 1,
        }
        return rep, None

    def audit(self):
        return report(self.state()), None


def settle_text(rep):
    p = rep.get("period") or {}
    lines = [
        "deposon 结算 · epoch %d @tick %d%s · 判定 %s" % (
            rep["epoch"], rep["tick"], "（单元终核）" if p.get("close") else "",
            "自洽" if rep["verdict"] == "SELF-CONSISTENT" else "不自洽"),
        "本期发生额 ΔΦ %d · ΔR %d · ΔD %d（%s）· 散失行 %d" % (
            p.get("d_phi", 0), p.get("d_R", 0), p.get("d_D", 0),
            " · ".join("%s %d" % (CAUSE_ZH[c], p.get("d_D_by", {}).get(c, 0)) for c in CAUSES),
            sum((p.get("deposited") or {}).values())),
        "期末余额 E⁰ %d ＝ Φ %d ＋ R %d ＋ D %d ＋ U %d · 守恒核 %s" % (
            rep["E0"], rep["phi"], rep["R"], rep["D"], rep["U"],
            "成立" if rep["verdict"] == "SELF-CONSISTENT" else "破坏"),
        "耗散通道利用率 D/E⁰行 %s ｜ 在场行 %d/%d ｜ 幻肢 %d" % (
            pct(rep["util_A"]), rep["live_rows"], rep["cap"], rep["phantoms"]),
    ]
    if p.get("close"):
        lines.append("单元终核：U=%d · E⁰=Φ+R+D %s（帐本自解·0 外部对账）" % (
            rep["U"], "成立" if rep["U"] == 0 and rep["verdict"] == "SELF-CONSISTENT" else "不成立"))
    return "\n".join(lines)
