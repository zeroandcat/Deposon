#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# 凝子场 MCP 实例 · 本地 stdio 自测（selftest_mcp.py）
# ----------------------------------------------------------------------------
# 段零 harness 本体直调（本体层先行·memory harness proper, not just tools）:
#   绕过 stdio/MCP 传输层·import 直调本体原语
#   —— 证明本体（外置账本承载+DR-4 渲染位+生命周期原语）可独立于接口层运行
# 三段（stdio 握手·工具枚举·工具调用）:
#   段一 initialize · 段二 tools/list · 段三 tools/call（write/read 回环）
# 强证明位（换模不丢·外置账本本质）:
#   写入 3 条 → 进程 terminate → 重启（同账本）→ 回读 3/3 恒等 → 续写 2 → 回读 5/5
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

class Host:  # 宿主侧最小 MCP 客户端（沿实践脚本 McpClient 体例）
    def __init__(self, ledger):
        env = dict(os.environ); env["CONDENSATE_LEDGER"] = ledger
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
    def call(self, tool, args):
        r = self.rpc("tools/call", {"name": tool, "arguments": args})
        res = r.get("result", {})
        if res.get("isError"):
            raise RuntimeError("tool error: %s" % res["content"][0]["text"])
        return res["content"][0]["text"]
    def kill(self):
        self.proc.terminate()
        try: self.proc.wait(timeout=5)
        except Exception: self.proc.kill()

def main():
    t0 = time.time()
    results = []
    def check(seg, ok, detail):
        results.append(ok)
        print("[%s] %s · %s" % (seg, "PASS" if ok else "FAIL", detail))

    tmpd = tempfile.mkdtemp(prefix="condensate_selftest_")
    ledger = os.path.join(tmpd, "ledger.jsonl")
    core_ledger = os.path.join(tmpd, "core_ledger.jsonl")  # 段零本体自证账本（独立位）
    try:
        # ---------- 段零 · harness 本体直调（绕过 stdio/MCP 传输层） ----------
        os.environ["CONDENSATE_LEDGER"] = core_ledger
        sys.path.insert(0, HERE)
        import mcp_server as core  # import 直调·0 子进程·0 传输层
        c_ok = True
        for m in SEED:
            w, err = core.write_entry(m["key"], m["text"])
            c_ok = c_ok and (err is None)
        hits, err = core.read_entries("habit.")
        c_ok = (c_ok and err is None and len(hits) == 3
                and all(any(h["key"] == m["key"] and h["text"] == m["text"] for h in hits) for m in SEED)
                and core.LEDGER_PATH == core_ledger)
        check("0-harness本体直调", c_ok,
              "import 直调原语 write×3→read 3/3 恒等·账本路径参数化生效（本体≠接口层·0 传输依赖）")

        # ---------- 段一 · initialize ----------
        h = Host(ledger)
        r = h.rpc("initialize", {"protocolVersion": "2024-11-05",
                                 "capabilities": {}, "clientInfo": {"name": "selftest-host", "version": "0.1"}})
        res = r.get("result", {})
        ok1 = (res.get("protocolVersion") == "2024-11-05"
               and res.get("serverInfo", {}).get("name") == "condensate-field-mcp"
               and "tools" in res.get("capabilities", {}))
        check("1-initialize", ok1,
              "protocol=%s server=%s caps.tools=%s" % (
                  res.get("protocolVersion"), res.get("serverInfo", {}).get("name"),
                  "tools" in res.get("capabilities", {})))
        # 宿主 quirk 位：notifications/initialized 携 id → 须有响应（不悬挂）
        r = h.rpc("notifications/initialized", {})
        check("1-initialized-quirk", "result" in r, "携 id 通知有响应（宿主 readline 不悬挂）")

        # ---------- 段二 · tools/list ----------
        r = h.rpc("tools/list", {})
        tools = {t["name"]: t for t in r.get("result", {}).get("tools", [])}
        w_ok = tools.get("deposon_memory_write", {}).get("inputSchema", {}).get("required") == ["key", "text"]
        r_ok = tools.get("deposon_memory_read", {}).get("inputSchema", {}).get("required") == ["prefix"]
        check("2-tools/list", w_ok and r_ok and len(tools) == 2,
              "2 工具·write{key,text}=%s·read{prefix}=%s" % (w_ok, r_ok))

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
        h2.kill()
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)  # 测试账本即用即弃·0 残留

    verdict = "SELFTEST-PASS" if all(results) else "SELFTEST-FAIL"
    print("\n段零本体直调＋三段自测（initialize/tools/call）＋换模不丢强证明：%s · %d/%d 断言 · %.1fs · 0 网络 0 计费"
          % (verdict, sum(results), len(results), time.time() - t0))
    return 0 if all(results) else 1

if __name__ == "__main__":
    sys.exit(main())
