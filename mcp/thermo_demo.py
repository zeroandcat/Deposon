#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# thermo_demo.py — 改造前后对照：preview.9 记忆面 vs 幻肢代热力学账本
# ----------------------------------------------------------------------------
# 问：耗散通道利用率低到什么程度？改造后到什么程度？代价是什么？
# 法：同一操作迹（定种子·0 随机漂移）分别驱动
#     (甲) 改造前——preview.9 原码（git 历史取出·stdio MCP 实跑；无 git 时用
#         语义等价模拟器，且两者读回行数逐读交叉核对）
#     (乙) 改造后——thermo_core 本体（幻肢代·每 40 步结算一次·期末再结算一次）
# 读数：在场行·单读渲染行数/字符数（上下文代价）·特定键命中率·幻肢感知率·
#       耗散通道利用率 D/E⁰行 及成因分解·耗散选择性
# 纪律：0 网络 · 0 计费 · 临时账本即用即弃 · 0 触实例正式账本
# 用法：python3 mcp/thermo_demo.py [--ops 500] [--json] [--check]
#   --check ＝ 冻结读数回归门（同种子同迹逐位对表·漂移即 exit 1·CI 用·须 git 历史在场）
# ============================================================================
import os, sys, json, math, random, shutil, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import thermo_core as tc  # noqa: E402

BASELINE_REV = "4ee12b6"  # preview.9（热力学注入前最后一版记忆面）


# ---------------------------------------------------------------- 操作迹 ----
def make_trace(n_ops, seed):
    """定种子操作迹：30% 写（六成新笔记·四成改写热键）·35% 特定键读·20% 宽读·15% 全量读。"""
    rng = random.Random(seed)
    hot = ["user.k%02d" % i for i in range(40)]
    w = [1.0 / ((i + 1) ** 0.8) for i in range(40)]  # Zipf s=0.8 热度权
    note = [0]

    def pick_hot():
        return rng.choices(hot, weights=w)[0]

    def text(tag):
        return "%s：晨间先查账后开工·读数先落盘后发群·分歧走双审不代裁（%s）" % (tag, tag)

    ops = []
    for _ in range(n_ops):
        r = rng.random()
        if r < 0.30:
            if rng.random() < 0.60:
                note[0] += 1
                ops.append(("write", "note.%04d" % note[0], text("n%04d" % note[0]), None))
            else:
                k = pick_hot()
                ops.append(("write", k, text("%s-%d" % (k, rng.randrange(10 ** 6))), None))
        elif r < 0.65:
            k = pick_hot()
            ops.append(("read", k, None, k))
        elif r < 0.85:
            ops.append(("read", "user.", None, None))
        else:
            ops.append(("read", "", None, None))
    return ops


# ------------------------------------------------------- 改造前（甲）----
class LegacySim(object):
    """preview.9 语义等价模拟器：追加式·同前缀全量读回·注入序·无门无衰减（D≡0）。"""

    def __init__(self):
        self.rows = []

    def write(self, key, text):
        self.rows.append((key, text))

    def read(self, prefix):
        return [(k, t) for (k, t) in self.rows if k.startswith(prefix)]


class LegacyMcp(object):
    """preview.9 原码实跑（git 历史取出·stdio JSON-RPC 行式）。"""

    def __init__(self, tmpd):
        src = subprocess.run(["git", "-C", ROOT, "show", "%s:mcp/mcp_server.py" % BASELINE_REV],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if src.returncode != 0:
            raise RuntimeError("git show 失败")
        path = os.path.join(tmpd, "legacy_mcp_server.py")
        with open(path, "wb") as f:
            f.write(src.stdout)
        env = dict(os.environ)
        env["CONDENSATE_LEDGER"] = os.path.join(tmpd, "legacy_ledger.jsonl")
        self.proc = subprocess.Popen([sys.executable, path], stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                     text=True, encoding="utf-8", env=env)
        self._id = 0
        self.rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                "clientInfo": {"name": "thermo_demo", "version": "1"}})
        self.rpc("notifications/initialized", {})

    def rpc(self, method, params):
        self._id += 1
        self.proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": self._id,
                                          "method": method, "params": params}) + "\n")
        self.proc.stdin.flush()
        return json.loads(self.proc.stdout.readline())

    def call(self, name, args):
        res = self.rpc("tools/call", {"name": name, "arguments": args}).get("result", {})
        if res.get("isError"):
            raise RuntimeError("legacy tool error: %s" % res["content"][0]["text"])
        return res["content"][0]["text"]

    def close(self):
        self.proc.terminate()
        try:
            self.proc.wait(timeout=5)
        except Exception:
            self.proc.kill()


def run_legacy(ops, use_git):
    sim = LegacySim()
    mcp = None
    tmpd = tempfile.mkdtemp(prefix="thermo_demo_legacy_") if use_git else None
    stats = {"reads": 0, "rows": 0, "chars": 0, "by": {}, "found": 0, "specific": 0}
    try:
        if use_git:
            mcp = LegacyMcp(tmpd)
        for op in ops:
            if op[0] == "write":
                sim.write(op[1], op[2])
                if mcp:
                    assert mcp.call("deposon_memory_write", {"key": op[1], "text": op[2]}) == "written: %s" % op[1]
            else:
                hits = sim.read(op[1])
                kind = "specific" if op[3] else ("broad" if op[1] else "global")
                if mcp:  # 原码与模拟器逐读交叉核对（渲染行数恒等）
                    t = mcp.call("deposon_memory_read", {"prefix": op[1]})
                    n = 0 if t == "(0 条命中)" else len(t.split("\n"))
                    assert n == len(hits), (n, len(hits), op[1])
                stats["reads"] += 1
                stats["rows"] += len(hits)
                stats["chars"] += sum(len(k) + len(t) + 2 for (k, t) in hits)
                b = stats["by"].setdefault(kind, [0, 0])
                b[0] += 1
                b[1] += len(hits)
                if op[3]:
                    stats["specific"] += 1
                    stats["found"] += 1 if any(k == op[3] for (k, t) in hits) else 0
        return {"injected_rows": len(sim.rows), "live_rows": len(sim.rows),
                "crosschecked_vs_preview9_code": bool(mcp), **stats}
    finally:
        if mcp:
            mcp.close()
        if tmpd:
            shutil.rmtree(tmpd, ignore_errors=True)


# ------------------------------------------------------- 改造后（乙）----
def run_thermo(ops, settle_every=40):
    tmpd = tempfile.mkdtemp(prefix="thermo_demo_new_")
    try:
        L = tc.ThermoLedger(os.path.join(tmpd, "ledger.jsonl"), tc.load_cfg())
        stats = {"reads": 0, "rows": 0, "chars": 0, "by": {}, "found": 0, "specific": 0,
                 "phantom_felt": 0, "phantom_lines": 0}
        for i, op in enumerate(ops, 1):
            if op[0] == "write":
                L.write_entry(op[1], op[2])
            else:
                hits, _ = L.read_entries(op[1])
                live = [h for h in hits if not h.get("phantom")]
                ph = [h for h in hits if h.get("phantom")]
                kind = "specific" if op[3] else ("broad" if op[1] else "global")
                stats["reads"] += 1
                stats["rows"] += len(live)
                stats["chars"] += sum(len(h["key"]) + len(h["text"]) + 2 for h in live)
                stats["phantom_lines"] += len(ph)
                b = stats["by"].setdefault(kind, [0, 0, 0])
                b[0] += 1
                b[1] += len(live)
                b[2] += len(ph)
                if op[3]:
                    stats["specific"] += 1
                    stats["found"] += 1 if any(h["key"] == op[3] for h in live) else 0
                    stats["phantom_felt"] += 1 if any(h["key"] == op[3] for h in ph) else 0
            if i % settle_every == 0:
                L.settle(False)
        L.settle(False)  # 期末结算（非终核·在场余额结转）
        rep, _ = L.audit()
        return {"injected_rows": rep["live_rows"] + rep["phantoms"], **stats, "thermo": rep}
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)


def _avg(a, b):
    return (a / b) if b else 0.0


def main():
    n_ops, seed, as_json = 500, 20261125, "--json" in sys.argv
    if "--ops" in sys.argv:
        n_ops = int(sys.argv[sys.argv.index("--ops") + 1])
    ops = make_trace(n_ops, seed)
    has_git = subprocess.run(["git", "-C", ROOT, "rev-parse", BASELINE_REV],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    A = run_legacy(ops, has_git)
    B = run_thermo(ops)
    T = B["thermo"]
    assert A["reads"] == B["reads"] and A["specific"] == B["specific"]

    def row(name, a, b):
        return "| %s | %s | %s |" % (name, a, b)

    lines = [
        "改造前后对照（同一操作迹 %d 步·种子 %d·30%% 写/35%% 特定读/20%% 宽读/15%% 全量读）" % (n_ops, seed),
        "",
        row("读数", "改造前 preview.9", "改造后 幻肢代（热力学注入）"),
        "|---|---|---|",
        row("注入行数", A["injected_rows"], B["injected_rows"]),
        row("期末在场行", A["live_rows"], T["live_rows"]),
        row("单读渲染行数（均）", "%.2f" % _avg(A["rows"], A["reads"]),
            "%.2f" % _avg(B["rows"], B["reads"])),
        row("单读渲染字符（均·上下文代价）", "%.0f" % _avg(A["chars"], A["reads"]),
            "%.0f" % _avg(B["chars"], B["reads"])),
        row("　特定键读：命中率", "%.2f%%" % (100 * _avg(A["found"], A["specific"])),
            "%.2f%%（另 %.2f%% 以幻肢行如实回射）" % (
                100 * _avg(B["found"], B["specific"]), 100 * _avg(B["phantom_felt"], B["specific"]))),
        row("　宽读/全量读：均渲染行", "%s" % " / ".join("%.1f" % _avg(A["by"][k][1], A["by"][k][0]) for k in ("broad", "global")),
            "%s" % " / ".join("%.1f" % _avg(B["by"][k][1], B["by"][k][0]) for k in ("broad", "global"))),
        row("散失账 D", "0（按构造·无散失事件）", "%d" % T["D"]),
        row("**耗散通道利用率 D/E⁰行**", "**0.00%（按构造）**", "**%.2f%%**（%d/%d）" % (100 * T["util_A"], T["D"], T["E0_rows"])),
        row("散失成因分解", "—", " · ".join("%s %d" % (tc.CAUSE_ZH[c], T["D_by"][c]) for c in tc.CAUSES if T["D_by"][c])),
        row("耗散选择性（陈旧行散失占比）", "—", tc.pct(T["selectivity"])),
        row("守恒核 E⁰=Φ+R+D+U", "n/a（无账）", "%s（%d=%d+%d+%d+%d）" % (
            "成立" if T["verdict"] == "SELF-CONSISTENT" else "破坏", T["E0"], T["phi"], T["R"], T["D"], T["U"])),
    ]
    if not has_git:
        lines.append("")
        lines.append("注：无 git 历史·改造前读数出自 preview.9 语义等价模拟器（未与原码交叉核对）。")
    else:
        lines.append("")
        lines.append("注：改造前读数出自 preview.9 原码实跑（git %s 取出·stdio MCP）·与模拟器逐读行数交叉核对全等。" % BASELINE_REV)
    print("\n".join(lines))
    if as_json:
        print("\nJSON " + json.dumps({"legacy": A, "thermo": {k: v for k, v in B.items() if k != "thermo"},
                                       "thermo_report": T}, ensure_ascii=False))
    if "--check" in sys.argv:
        # 冻结读数带（同种子同迹 ⇒ 确定性·逐位）：CI 回归门——漂移即 fail-loud
        hit_a, hit_b = _avg(A["found"], A["specific"]), _avg(B["found"], B["specific"])
        ph_b = _avg(B["phantom_felt"], B["specific"])
        expect = [
            ("改造前期末在场行", A["live_rows"], 152),
            ("改造后期末在场行", T["live_rows"], 61),
            ("改造前特定键命中率", round(hit_a, 4), 0.5031),
            ("改造后特定键命中率", round(hit_b, 4), 0.4785),
            ("幻肢行回射率", round(ph_b, 4), 0.0245),
            ("耗散通道利用率", round(T["util_A"], 4), 0.6923),
            ("散失·门拒", T["D_by"]["reject"], 37529),
            ("散失·衰减", T["D_by"]["decay"], 21357),
            ("散失·视界", T["D_by"]["horizon"], 19248),
            ("散失·覆盖", T["D_by"]["supersede"], 27091),
            ("守恒核", T["verdict"], "SELF-CONSISTENT"),
            ("守恒核逐位 E⁰=Φ+R+D+U", T["E0"], T["phi"] + T["R"] + T["D"] + T["U"]),
            ("改造前交叉核对（有 git 历史时 preview.9 原码实跑 vs 模拟器逐读行数全等）", A["crosschecked_vs_preview9_code"], has_git),
        ]
        bad = [(n, g, e) for (n, g, e) in expect if g != e]
        for n, g, e in expect:
            print("%s %s：实得 %r · 冻结 %r" % ("PASS" if g == e else "FAIL", n, g, e))
        print("thermo_demo --check: %s (%d/%d)" % ("FROZEN READINGS MATCH" if not bad else "DRIFT",
                                                   len(expect) - len(bad), len(expect)))
        return 0 if not bad else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
