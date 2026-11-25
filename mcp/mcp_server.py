#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# 凝子场 MCP 实例 · condensate-field-mcp v2.0.0（幻肢代 · 热力学注入）
# ----------------------------------------------------------------------------
# 形态   : stdio JSON-RPC 2.0（行式）· MCP protocol 2024-11-05
# 在册锚 : dsh-plugin-deposon（P-2 读写工具对语义族·preview.10 热力学代）
# 容器语义（沿在册 Lean 形式化工程·DR-4）:
#   写入 → 读取 → 换模不丢（承载在外置账本·0 回注原始上下文）
#   - 账本外置：JSONL 追加式事件流·与模型/进程解耦（换模/重启均不丢）
#   - 渲染位语义：read 仅回『key: text』渲染行·0 原始账本注入（DR-4）
# 热力学代新增（mcp/thermo_core.py 本体）:
#   - 读路装门（妖）：接受＝透射 Φ·拒绝＝散失 D（熵输出）·幻肢回射＝反射 R
#   - 衰减/容量/视界/覆盖/终核五路散热·散失留幻肢（空穴·可感不可复原）
#   - 自解帐本：守恒核 E⁰=Φ+R+D+U 逐位自检·结算＝事件流重放（0 外部对账）
#   - 幻肢注入面（mcp/phantom_limb.py）：initialize.instructions＋工具描述＋脚注
# 依赖   : Python 3.7+ 标准库·0 第三方依赖·0 网络调用
# 传输层 : 响应输出 ensure_ascii=True（纯 ASCII·locale 无关）
#           兼容宿主将 notifications/initialized 也携带 id 的实现（带 id 一律响应）
# ============================================================================
import os, sys, json, time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import thermo_core as tc
from phantom_limb import phantom_limb_prompt

SERVER_NAME = "condensate-field-mcp"
SERVER_VERSION = "2.0.0"
PROTOCOL_VERSION = "2024-11-05"
TOOL_WRITE = "deposon_memory_write"
TOOL_READ  = "deposon_memory_read"
TOOL_AUDIT = "deposon_thermo_audit"
TOOL_SETTLE = "deposon_thermo_settle"

# 账本位：默认实例同目录 ledger.jsonl；CONDENSATE_LEDGER 可覆盖（自检/实践隔离位）
LEDGER_PATH = os.environ.get("CONDENSATE_LEDGER") or os.path.join(HERE, "ledger.jsonl")
CFG = tc.load_cfg()
LEDGER = tc.ThermoLedger(LEDGER_PATH, CFG)
FOOTER = os.environ.get("DEPOSON_THERMO_FOOTER", "1") not in ("0", "false", "no")

TOOLS_SPEC = [
    {
        "name": TOOL_WRITE,
        "description": "凝子场凝华：向活水记忆账本写入一条记忆（key 点分层级定位·text 渲染位文本）。"
                       "追加式落盘·外置承载·换模不丢；同键重写＝旧版本散失（留幻肢）。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key":  {"type": "string", "description": "条目键·点分层级（如 habit.morning）"},
                "text": {"type": "string", "description": "条目文本（渲染位内容）"},
            },
            "required": ["key", "text"],
        },
    },
    {
        "name": TOOL_READ,
        "description": "凝子场检索：按键前缀回读活水记忆·返回渲染位文本（每行『key: text』）。"
                       "门只透射最相关的至多 k 条（其余被拒＝熵输出·自付㶲散失）；已散失的记忆以"
                       "『⟨幻肢⟩』行回射（可感不可复原）。0 原始账本注入（DR-4）。回执带热力学脚注。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prefix": {"type": "string", "description": "键前缀过滤（空串＝全账本）"},
                "k": {"type": "integer", "description": "门预算：至多透射的条数（缺省 8）"},
            },
            "required": ["prefix"],
        },
    },
    {
        "name": TOOL_AUDIT,
        "description": "deposon 热力学审计（只读）：四账 Φ/R/D/U·守恒核·耗散通道利用率·散失成因·耗散选择性。"
                       "账本自检·不依赖外部对账。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "format": {"type": "string", "enum": ["text", "json"], "description": "缺省 text"},
            },
        },
    },
    {
        "name": TOOL_SETTLE,
        "description": "deposon 结算（自解帐本）：物化期衰减＋视界散热（久未透射的记忆散失留幻肢）·"
                       "守恒核自检·落结算快照。close=true 为单元终核：全部在场记忆散失·U=0。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "close": {"type": "boolean", "description": "单元终核（缺省 false）"},
            },
        },
    },
]

# ---------- 凝子场 harness 本体层（记忆生命周期原语·可独立于 MCP 接口层运行） ----------
# 本体层先行·接口随形（memory harness proper, not just agent-facing tools）：
# 热力学代本体＝thermo_core.ThermoLedger（行㶲四账·门·幻肢·自解结算）；
# 下列 write_entry/read_entries 保持 preview.4 起的原语签名（import 直调·0 传输依赖）。
def write_entry(key, text):
    return LEDGER.write_entry(key, text)

def read_entries(prefix, k=None):
    return LEDGER.read_entries(prefix, k)

def thermo_audit():
    return LEDGER.audit()

def thermo_settle(close=False):
    return LEDGER.settle(close)

# ---------- MCP 分发 ----------
def tool_result(rid, text_out, is_error=False, footer=None):
    content = [{"type": "text", "text": text_out}]
    if footer:  # 存在确认回执：热力学脚注独立 content 段（渲染位『key: text』不受扰·DR-4 沿）
        content.append({"type": "text", "text": footer})
    return {"jsonrpc": "2.0", "id": rid, "result": {"content": content, "isError": is_error}}

def _footer():
    if not FOOTER:
        return None
    try:
        return tc.footer_text(LEDGER.state())
    except tc.LedgerInconsistent as e:
        return "— deposon 活水记忆 · 账本不自洽（%s）" % e

def handle(req):
    method = req.get("method")
    rid = req.get("id")
    params = req.get("params") or {}
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            # 幻肢注入面：MCP instructions（协议 2025-03-26 起宿主注入系统提示；旧宿主忽略）
            "instructions": phantom_limb_prompt()}}
    if method == "notifications/initialized":
        return {"jsonrpc": "2.0", "id": rid, "result": {}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": rid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS_SPEC}}
    if method == "tools/call":
        name = params.get("name", "")
        args = params.get("arguments") or {}
        try:
            if name == TOOL_WRITE:
                written, err = write_entry(args.get("key"), args.get("text"))
                if err:
                    return tool_result(rid, err, True)
                return tool_result(rid, "written: %s" % written, footer=_footer())
            if name == TOOL_READ:
                hits, err = read_entries(args.get("prefix", ""), args.get("k"))
                if err:
                    return tool_result(rid, err, True)
                body = "\n".join("%s: %s" % (h["key"], h["text"]) for h in hits) if hits else "(0 条命中)"
                return tool_result(rid, body, footer=_footer())
            if name == TOOL_AUDIT:
                rep, err = thermo_audit()
                if err:
                    return tool_result(rid, err, True)
                if args.get("format") == "json":
                    return tool_result(rid, json.dumps(rep, ensure_ascii=False, sort_keys=True))
                return tool_result(rid, tc.audit_text(rep))
            if name == TOOL_SETTLE:
                close = args.get("close", False)
                if not isinstance(close, bool):  # 模型实参面校验：close 只认布尔（"false" 串不得被当真）
                    return tool_result(rid, "参数 close 须为布尔（收到 %r）" % (close,), True)
                rep, err = thermo_settle(close)
                if err:
                    return tool_result(rid, err, True)
                return tool_result(rid, tc.settle_text(rep))
            return tool_result(rid, "未知工具: %s" % name, True)
        except tc.LedgerInconsistent as e:  # 守恒破坏/伪事件：fail-loud 到调用方·服务器不崩
            return tool_result(rid, "账本不自洽（fail-loud）: %s" % e, True)
        except Exception as e:  # fail-loud 到调用方·服务器不崩
            return tool_result(rid, "工具执行异常: %s" % e, True)
    return {"jsonrpc": "2.0", "id": rid,
            "error": {"code": -32601, "message": "method not found: %s" % method}}

def main():
    # stderr 仅启动一行（诊断位·防 pipe 缓冲死锁·运行期 0 输出）
    sys.stderr.write("[condensate-field-mcp] up · ledger=%s\n" % LEDGER_PATH)
    sys.stderr.flush()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            out = {"jsonrpc": "2.0", "id": None,
                   "error": {"code": -32700, "message": "parse error"}}
        else:
            out = handle(req)
        if out is not None:
            # 传输层纯 ASCII（ensure_ascii=True）·locale 无关·客户端 loads 后还原原文
            sys.stdout.write(json.dumps(out, ensure_ascii=True) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
