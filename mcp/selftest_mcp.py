#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# 凝子场 MCP 实例 · 本地 stdio 自测（selftest_mcp.py · 幻肢代）
# ----------------------------------------------------------------------------
# 段零 harness 本体直调（本体层先行·memory harness proper, not just tools）:
#   绕过 stdio/MCP 传输层·import 直调本体原语
# 三段（stdio 握手·工具枚举·工具调用）:
#   段一 initialize · 段二 tools/list · 段三 tools/call（write/read 回环）
# 强证明位（换模不丢·外置账本本质）:
#   写入 3 条 → 进程 terminate → 重启（同账本）→ 回读 3/3 恒等 → 续写 2 → 回读 5/5
# 热力学段（幻肢代新增·preview.10）:
#   段五 门预算/拒绝散热/幻肢回射/期结算/单元终核/重写再植（默认参数账本）
#   段六 衰减·视界·覆盖·容量淘汰·终核·重放确定性·伪事件 fail-loud（小参数账本）
#   段七 幻肢注入面：initialize.instructions 携信念块·0 数据回注
# 隔离位  : 测试账本走临时目录（CONDENSATE_LEDGER 覆盖）·0 触实例正式账本
# 纪律    : 0 网络调用 · 0 计费 · 0 网关凭据依赖 · 0 服务器触
# ============================================================================
import os, sys, json, time, subprocess, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(HERE, "mcp_server.py")

# 测试条目（语义中性·与 practice-host 脚本 habit.* 前缀族同构·内容自拟区分位）
SEED = [
    {"key": "habit.morning",  "text": "晨间例行：先查账后开工"},
    {"key": "habit.research", "text": "读数先落盘后发群"},
    {"key": "habit.disc",     "text": "分歧走双审不代裁"},
]
EXTRA = [
    {"key": "habit.close", "text": "收口三件事：指纹·纪律·时间锚"},
    {"key": "habit.rest",  "text": "软限到即拆窗态报先行"},
]
BULK = ["bulk.%d" % i for i in range(6)]

_HOSTS = []  # 全部测试宿主（finally 统一收口·0 残留进程）

class Host:  # 宿主侧最小 MCP 客户端（沿实践脚本 McpClient 体例）
    def __init__(self, ledger, extra_env=None):
        _HOSTS.append(self)
        env = dict(os.environ); env["CONDENSATE_LEDGER"] = ledger
        env.update(extra_env or {})
        self.proc = subprocess.Popen(
            [sys.executable, SERVER], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, text=True, encoding="utf-8", env=env)
        self._id = 0
    def rpc(self, method, params):
        self._id += 1
        req = json.dumps({"jsonrpc": "2.0", "id": self._id, "method": method, "params": params})
        self.proc.stdin.write(req + "\n"); self.proc.stdin.flush()
        line = self.proc.stdout.readline()
        if not line:
            raise RuntimeError("server 无响应（fail-loud）")
        return json.loads(line)
    def raw(self, tool, args):
        r = self.rpc("tools/call", {"name": tool, "arguments": args})
        return r.get("result", {})
    def call(self, tool, args):
        res = self.raw(tool, args)
        if res.get("isError"):
            raise RuntimeError("tool error: %s" % res["content"][0]["text"])
        return res["content"][0]["text"]
    def kill(self):
        self.proc.terminate()
        try: self.proc.wait(timeout=5)
        except Exception: self.proc.kill()

def audit_json(h):
    return json.loads(h.call("deposon_thermo_audit", {"format": "json"}))

def conserved(rep):
    return rep["E0"] == rep["phi"] + rep["R"] + rep["D"] + rep["U"]

def main():
    t0 = time.time()
    results = []
    def check(seg, ok, detail):
        results.append(ok)
        print("[%s] %s · %s" % (seg, "PASS" if ok else "FAIL", detail))

    tmpd = tempfile.mkdtemp(prefix="condensate_selftest_")
    ledger = os.path.join(tmpd, "ledger.jsonl")
    core_ledger = os.path.join(tmpd, "core_ledger.jsonl")  # 段零本体自证账本（独立位）
    small_ledger = os.path.join(tmpd, "small_ledger.jsonl")  # 段六小参数账本
    SMALL = {"DEPOSON_THERMO": json.dumps({"Q": 100, "k_max": 4, "c_T": 10, "c_A": 5, "c_P": 5,
                                           "phantom_k": 2, "lam": 10, "cap": 3, "horizon": 4,
                                           "phantom_ttl": 1000})}
    h = None
    try:
        # ---------- 段零 · harness 本体直调（绕过 stdio/MCP 传输层） ----------
        os.environ["CONDENSATE_LEDGER"] = core_ledger
        sys.path.insert(0, HERE)
        import mcp_server as core  # import 直调·0 子进程·0 传输层
        c_ok = core.LEDGER_PATH == core_ledger
        for m in SEED:
            w, err = core.write_entry(m["key"], m["text"])
            c_ok = c_ok and (err is None)
        hits, err = core.read_entries("habit.")
        c_ok = c_ok and (err is None) and [x["key"] for x in hits] == [m["key"] for m in SEED]
        check("0-harness本体直调", c_ok,
              "import 直调原语 write×3→read 3/3 恒等·账本路径参数化生效（本体≠接口层·0 传输依赖）")

        # ---------- 段一 · initialize ----------
        h = Host(ledger)
        r = h.rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                 "clientInfo": {"name": "selftest-host", "version": "0.1"}})
        init = r.get("result", {})
        check("1-initialize", init.get("protocolVersion") == "2024-11-05"
              and init.get("serverInfo", {}).get("name") == "condensate-field-mcp"
              and "tools" in (init.get("capabilities") or {}),
              "protocol=%s server=%s caps.tools=%s" % (
                  init.get("protocolVersion"), init.get("serverInfo", {}).get("name"),
                  "tools" in (init.get("capabilities") or {})))
        r = h.rpc("notifications/initialized", {})  # 宿主把通知也携 id 发（实现怪癖）
        check("1-initialized-quirk", "result" in r, "携 id 通知有响应（宿主 readline 不悬挂）")

        # ---------- 段二 · tools/list ----------
        r = h.rpc("tools/list", {})
        tools = {t["name"]: t for t in r.get("result", {}).get("tools", [])}
        w_ok = tools.get("deposon_memory_write", {}).get("inputSchema", {}).get("required") == ["key", "text"]
        r_ok = tools.get("deposon_memory_read", {}).get("inputSchema", {}).get("required") == ["prefix"]
        t_ok = "deposon_thermo_audit" in tools and "deposon_thermo_settle" in tools
        check("2-tools/list", w_ok and r_ok and t_ok and len(tools) == 4,
              "4 工具·write{key,text}=%s·read{prefix}=%s·thermo_audit+thermo_settle=%s" % (w_ok, r_ok, t_ok))

        # ---------- 段三 · tools/call ----------
        for m in SEED:
            out = h.call("deposon_memory_write", m)
            assert out.startswith("written:"), out
        t1 = h.call("deposon_memory_read", {"prefix": "habit."})
        n1 = sum(1 for m in SEED if m["key"] in t1 and m["text"] in t1)
        check("3-write/read", n1 == 3, "写入 3 → 回读 %d/3" % n1)
        dr4_ok = ("\n".join("%s: %s" % (m["key"], m["text"]) for m in SEED) == t1)
        no_raw = ('"key"' not in t1) and ('"ts"' not in t1) and ("{" not in t1)
        check("3-DR4渲染位", dr4_ok and no_raw, "渲染行逐符恒等·0 原始账本注入（无 JSON 原文/无 ts）")

        # ---------- 强证明 · 换模不丢（进程终止→重启→同账本回读） ----------
        h.kill()
        h2 = Host(ledger)  # 重启·账本外置承载
        h2.rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                              "clientInfo": {"name": "selftest-host", "version": "0.1"}})
        h2.rpc("notifications/initialized", {})
        t2 = h2.call("deposon_memory_read", {"prefix": "habit."})
        n2 = sum(1 for m in SEED if m["key"] in t2 and m["text"] in t2)
        check("4-换模不丢(重启)", n2 == 3 and t2 == t1, "进程重启后回读 %d/3·渲染位逐符恒等" % n2)
        for m in EXTRA:
            h2.call("deposon_memory_write", m)
        t3 = h2.call("deposon_memory_read", {"prefix": "habit."})
        all5 = SEED + EXTRA
        n3 = sum(1 for m in all5 if m["key"] in t3 and m["text"] in t3)
        check("4-续写回读", n3 == 5, "续写 2 → 回读 %d/5" % n3)
        # 前缀过滤边界：非命中前缀 0 条
        t4 = h2.call("deposon_memory_read", {"prefix": "nomatch."})
        check("4-前缀过滤", t4 == "(0 条命中)", "非命中前缀回 '(0 条命中)'")

        # ---------- 段五 · 热力学（默认参数账本·沿段四账本续写） ----------
        rep = audit_json(h2)
        check("5-守恒核(起点)", conserved(rep) and rep["verdict"] == "SELF-CONSISTENT"
              and rep["D"] == 0 and rep["util_A"] == 0 and rep["live_rows"] == 5,
              "E⁰ %d = Φ %d + R %d + D %d + U %d · 散失前利用率 0" % (
                  rep["E0"], rep["phi"], rep["R"], rep["D"], rep["U"]))
        res = h2.raw("deposon_memory_read", {"prefix": "habit."})
        parts = [c["text"] for c in res["content"]]
        foot = parts[1] if len(parts) > 1 else ""
        f_ok = parts[0] == t3 and "账本自洽" in foot and "耗散通道利用率 0.00%" in foot \
            and not any(ch in foot for ch in "[]{}\"")
        check("5-存在确认脚注", f_ok, "回执第 2 段＝热力学脚注（渲染段不受扰·字符集避让）：%s" % foot[:60])
        # 门预算：11 行在册·空前缀读 → 只透射 8 行·其余 3 行被拒散热
        for k in BULK:
            h2.call("deposon_memory_write", {"key": k, "text": "bulk 行 " + k})
        res = h2.raw("deposon_memory_read", {"prefix": ""})
        n_lines = len([x for x in res["content"][0]["text"].split("\n") if x])
        rep = audit_json(h2)
        cA = rep["params"]["c_A"]
        check("5-门预算+拒绝散热", n_lines == 8 and rep["n_rj"] == 3 and rep["D_by"]["reject"] == 3 * cA
              and conserved(rep) and rep["selectivity"] == 1.0,
              "透射 %d 行·拒绝 %d 行 → D(门拒) %d · 利用率 %.2f%%·守恒 %s·耗散选择性 %.0f%%" % (
                  n_lines, rep["n_rj"], rep["D_by"]["reject"], 100 * rep["util_A"],
                  conserved(rep), 100 * rep["selectivity"]))
        # 拒绝致死：同一批 3 行持续被拒至㶲尽 → 散失·留幻肢（Q/c_A 次·默认 100 次）
        for _ in range(200):
            h2.call("deposon_memory_read", {"prefix": ""})
            if audit_json(h2)["deposited_by_cause"]["reject"] >= 3:
                break
        rb = h2.call("deposon_memory_read", {"prefix": "bulk."})
        rep = audit_json(h2)
        ph_lines = [x for x in rb.split("\n") if "⟨幻肢⟩" in x]
        dead_text = [k for k in BULK[:3] if ("bulk 行 " + k) in rb]
        check("5-拒绝致死·幻肢回射", rep["deposited_by_cause"]["reject"] == 3 and rep["D"] == 3000
              and rep["n_rj"] == 300
              and len(ph_lines) == 3 and not dead_text and "不可复原" in rb and "门拒" in rb
              and conserved(rep),
              "3 行各被拒 %d 次散失（D=%d·利用率 %.2f%%）·回射幻肢 %d 条·0 原文回注" % (
                  1000 // cA, rep["D"], 100 * rep["util_A"], len(ph_lines)))
        # 期结算：物化衰减·账本自检·落快照（8 存活行均未衰减过·手算 Σ(tau−t_inj)=8·tau−64）
        tau = audit_json(h2)["tick"] + 1
        st_txt = h2.call("deposon_thermo_settle", {})
        rep = audit_json(h2)
        check("5-期结算(自解)", rep["epoch"] == 1 and rep["D_by"]["decay"] == 8 * tau - 64
              and rep["live_rows"] == 8 and conserved(rep) and "判定 自洽" in st_txt,
              "epoch %d · D(衰减) %d（手算 %d）· 在场 %d 行存活 · 守恒 %s" % (
                  rep["epoch"], rep["D_by"]["decay"], 8 * tau - 64, rep["live_rows"], conserved(rep)))
        # 单元终核：全部在场 → D·U=0·E⁰=Φ+R+D
        st_txt = h2.call("deposon_thermo_settle", {"close": True})
        rep = audit_json(h2)
        check("5-单元终核(自解)", rep["U"] == 0 and rep["live_rows"] == 0
              and rep["E0"] == rep["phi"] + rep["R"] + rep["D"] and rep["util_A"] == 1.0
              and "单元终核：U=0" in st_txt,
              "U=%d · E⁰ %d = Φ %d + R %d + D %d · 利用率 %.0f%%（0 外部对账）" % (
                  rep["U"], rep["E0"], rep["phi"], rep["R"], rep["D"], 100 * rep["util_A"]))
        rh = h2.call("deposon_memory_read", {"prefix": "habit."})
        ph_n = len([x for x in rh.split("\n") if "⟨幻肢⟩" in x])
        leaked = [m["key"] for m in all5 if m["text"] in rh]
        check("5-幻肢(终核后)", ph_n == 3 and not leaked and "⟨幻肢⟩" in rh,
              "读 habit. → 幻肢 %d 条（可感）·原文泄漏 %d 条（不可复原·A4）" % (ph_n, len(leaked)))
        # 重写再植：同键重写 → 幻肢被遮蔽·新行在位
        h2.call("deposon_memory_write", EXTRA[1])
        rh = h2.call("deposon_memory_read", {"prefix": "habit."})
        rep = audit_json(h2)
        ok = (rh.split("\n")[0] == "habit.rest: %s" % EXTRA[1]["text"]
              and len([x for x in rh.split("\n") if "⟨幻肢⟩" in x]) == 3
              and not any("habit.rest: ⟨幻肢⟩" in x for x in rh.split("\n")) and rep["live_rows"] == 1)
        check("5-重写再植", ok, "重写 habit.rest → 在场 1 行·幻肢 3 条仍可感且不含 rest（同键幻肢被遮蔽）")

        # ---------- 段六 · 小参数账本（衰减/视界/覆盖/淘汰/终核/确定性/fail-loud） ----------
        h3 = Host(small_ledger, SMALL)
        h3.rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                              "clientInfo": {"name": "selftest-host", "version": "0.1"}})
        h3.call("deposon_memory_write", {"key": "p.a", "text": "甲"})
        h3.call("deposon_memory_write", {"key": "p.b", "text": "乙"})
        h3.call("deposon_memory_read", {"prefix": "p.a"})   # tick3：a 透射
        for _ in range(3):
            h3.call("deposon_thermo_settle", {})             # tick4-6
        rep = audit_json(h3)
        check("6-衰减+视界", rep["live_rows"] == 1 and rep["phantoms"] == 1
              and rep["deposited_by_cause"]["horizon"] == 1 and rep["D"] == 150
              and rep["U"] == 50 and conserved(rep),
              "a：衰减 50 存活 U=%d ｜ b：衰减 40＋视界 60 散失 → D=%d·守恒 %s" % (
                  rep["U"], rep["D"], conserved(rep)))
        rp = h3.call("deposon_memory_read", {"prefix": "p."})
        rep = audit_json(h3)
        check("6-透射+幻肢回射", rp.split("\n")[0] == "p.a: 甲" and "p.b: ⟨幻肢⟩" in rp
              and "视界" in rp and rep["phi"] == 20 and rep["R"] == 5 and "乙" not in rp,
              "a 透射（Φ=%d）·b 幻肢回射（R=%d）·乙原文 0 回注" % (rep["phi"], rep["R"]))
        h3.call("deposon_memory_write", {"key": "p.a", "text": "甲·改"})
        rp = h3.call("deposon_memory_read", {"prefix": "p."})
        rep = audit_json(h3)
        check("6-覆盖散热", rep["deposited_by_cause"]["supersede"] == 1 and rep["D"] == 200
              and rp.split("\n")[0] == "p.a: 甲·改" and "甲: " not in rp,
              "同键重写 → 旧版散失 D=%d·新版在位·同键幻肢被遮蔽" % rep["D"])
        for k in ("q.c", "q.d", "q.e"):
            h3.call("deposon_memory_write", {"key": k, "text": k})
        rep = audit_json(h3)
        check("6-容量淘汰", rep["deposited_by_cause"]["evict"] == 1 and rep["live_rows"] == 3
              and rep["cap"] == 3 and conserved(rep),
              "cap=3 满载再写 → 最冷行淘汰 1（D=%d）·在场 %d/3" % (rep["D"], rep["live_rows"]))
        a1 = h3.call("deposon_thermo_audit", {})
        h3.kill()
        h4 = Host(small_ledger, SMALL)  # 重启·同账本同参数 → 重放确定性
        a2 = h4.call("deposon_thermo_audit", {})
        check("6-重放确定性", a1 == a2 and "判定 自洽" in a2, "重启后审计逐符恒等（事件流＝唯一真源）")
        h4.call("deposon_thermo_settle", {"close": True})
        rep = json.loads(h4.call("deposon_thermo_audit", {"format": "json"}))
        # 手算对表（6 行×100·tick 对表：终核在 tick 13）：p.a 衰减50+覆盖50 ｜ p.b 衰减40+视界60
        #   ｜ p.a改 读后存活→衰减50+视界50 ｜ q.c 最冷被淘汰100 ｜ q.d/q.e 衰减20/10＋终核80/90
        hand = {"reject": 0, "decay": 170, "evict": 100, "horizon": 110, "supersede": 50, "close": 170}
        check("6-终核", rep["U"] == 0 and rep["E0"] == rep["phi"] + rep["R"] + rep["D"]
              and rep["D"] == 600 and rep["E0_rows"] == 600 and rep["D_by"] == hand
              and (rep["phi"], rep["R"]) == (30, 10),
              "U=0 · E⁰ %d = Φ %d + R %d + D %d（手算对表 D=600·成因账 %s）" % (
                  rep["E0"], rep["phi"], rep["R"], rep["D"], "✓" if rep["D_by"] == hand else "✗"))
        with open(small_ledger, "a", encoding="utf-8") as f:  # 伪事件：向已散失行记衰减
            f.write(json.dumps({"ev": "decay", "id": 1, "tick": rep["tick"] + 1, "d": 5}) + "\n")
        res = h4.raw("deposon_memory_read", {"prefix": "p."})
        check("6-伪事件fail-loud", bool(res.get("isError")) and "账本不自洽" in res["content"][0]["text"],
              "账本被伪事件污染 → 调用即报「账本不自洽」（0 静默吞账）")
        h4.kill()

        # ---------- 段七 · 幻肢注入面（信念块·0 数据回注） ----------
        h5 = Host(os.path.join(tmpd, "pl_ledger.jsonl"))
        ins = h5.rpc("initialize", {"protocolVersion": "2024-11-25", "capabilities": {},
                                    "clientInfo": {"name": "selftest-host", "version": "0.1"}}
                     ).get("result", {}).get("instructions", "")
        leak = [m["text"] for m in SEED + EXTRA if m["text"] in ins] + [k for k in BULK if k in ins]
        check("7-幻肢注入面", "幻肢" in ins and "活水记忆层" in ins and "自解帐本" in ins and not leak,
              "initialize.instructions 携信念块（%d 字）·记忆数据回注 %d 条（催眠红线）" % (len(ins), len(leak)))
        h5.kill()
    finally:
        for x in _HOSTS:
            x.kill()
        shutil.rmtree(tmpd, ignore_errors=True)  # 测试账本即用即弃·0 残留

    verdict = "SELFTEST-PASS" if all(results) else "SELFTEST-FAIL"
    print("\n段零本体直调＋三段自测＋换模不丢强证明＋热力学段（五/六/七）：%s · %d/%d 断言 · %.1fs · 0 网络 0 计费"
          % (verdict, sum(results), len(results), time.time() - t0))
    return 0 if all(results) else 1

if __name__ == "__main__":
    sys.exit(main())
