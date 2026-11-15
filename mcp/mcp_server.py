#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# 凝子场 MCP 实例 · condensate-field-mcp v1.0.0
# ----------------------------------------------------------------------------
# 形态   : stdio JSON-RPC 2.0（行式）· MCP protocol 2024-11-05
# 在册锚 : dsh-plugin-deposon（85db3dc 在册·P-2 读写工具对语义族）
# 容器语义（沿在册 Lean 形式化工程·DR-4）:
#   写入 → 读取 → 换模不丢（承载在外置账本·0 回注原始上下文）
#   - 账本外置：JSONL 追加式落盘·与模型/进程解耦（换模/重启均不丢）
#   - 渲染位语义：read 仅回『key: text』渲染行·0 原始账本注入（DR-4）
# 依赖   : Python 3.7+ 标准库·0 第三方依赖·0 网络调用
# 传输层 : 响应输出 ensure_ascii=True（纯 ASCII·locale 无关）
#           兼容宿主将 notifications/initialized 也携带 id 的实现（带 id 一律响应）
# ============================================================================
import os, sys, json, time

SERVER_NAME = "condensate-field-mcp"
SERVER_VERSION = "1.0.0"
PROTOCOL_VERSION = "2024-11-05"
TOOL_WRITE = "deposon_memory_write"
TOOL_READ  = "deposon_memory_read"

# 账本位：默认实例同目录 ledger.jsonl；CONDENSATE_LEDGER 可覆盖（自检/实践隔离位）
LEDGER_PATH = os.environ.get("CONDENSATE_LEDGER") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "ledger.jsonl")

TOOLS_SPEC = [
    {
        "name": TOOL_WRITE,
        "description": "凝子场写入：向账本追加一条记忆（key 点分层级定位·text 渲染位文本）。"
                       "追加式落盘·外置承载·换模不丢。",
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
        "description": "凝子场读取：按键前缀回读账本·返回渲染位文本（每行『key: text』）。"
                       "0 原始账本注入（DR-4·ts 等元数据不出渲染位）。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prefix": {"type": "string", "description": "键前缀过滤（空串＝全量）"},
            },
            "required": ["prefix"],
        },
    },
]

# ---------- 凝子场 harness 本体层（记忆生命周期原语·可独立于 MCP 接口层运行） ----------
# 定位注记（本体层先行·接口随形·memory harness proper, not just agent-facing tools）:
# 本层即凝子场容器本体——外置账本承载（追加式落盘）＋DR-4 渲染位语义（read 仅回
# 渲染行·0 原始账本注入）＋生命周期原语（write_entry/read_entries 纯函数位·
# import 即用·0 依赖 stdio/MCP/传输层）。MCP 工具面（deposon_memory_write/read）
# 仅系本体的接口暴露位——本体先行·接口随形。
def write_entry(key, text):
    if not isinstance(key, str) or not isinstance(text, str):
        return None, "参数类型错：key/text 均须为字符串"
    if not key:
        return None, "参数空值：key 不可为空串"
    rec = {"key": key, "text": text, "ts": time.strftime("%Y-%m-%dT%H:%M:%S+08:00")}
    d = os.path.dirname(os.path.abspath(LEDGER_PATH))
    if d:
        os.makedirs(d, exist_ok=True)
    with open(LEDGER_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())
    return key, None

def read_entries(prefix):
    if not isinstance(prefix, str):
        return None, "参数类型错：prefix 须为字符串"
    hits = []
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue  # 损坏行容错跳过（账本健壮性·不中断读路）
                if isinstance(rec.get("key"), str) and rec["key"].startswith(prefix):
                    hits.append(rec)
    return hits, None

# ---------- MCP 分发 ----------
def tool_result(rid, text_out, is_error=False):
    return {"jsonrpc": "2.0", "id": rid, "result": {
        "content": [{"type": "text", "text": text_out}], "isError": is_error}}

def handle(req):
    if not isinstance(req, dict):
        return {"jsonrpc": "2.0", "id": None,
                "error": {"code": -32600, "message": "invalid request"}}
    method = req.get("method", "")
    rid = req.get("id")
    if rid is None:
        return None  # 真·通知（无 id）·按规范不响应
    params = req.get("params") or {}
    # 宿主兼容位：凡带 id 一律响应（含宿主将 notifications/initialized 携 id 的实现）
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION}}}
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
                return tool_result(rid, "written: %s" % written)
            if name == TOOL_READ:
                hits, err = read_entries(args.get("prefix", ""))
                if err:
                    return tool_result(rid, err, True)
                if not hits:
                    return tool_result(rid, "(0 条命中)")
                return tool_result(rid, "\n".join("%s: %s" % (h["key"], h["text"]) for h in hits))
            return tool_result(rid, "未知工具: %s" % name, True)
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
