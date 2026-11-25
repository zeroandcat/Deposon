#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# thermo_cli.py — 账本热力学命令面（dsh 插件工具位 / 人工位）
# ----------------------------------------------------------------------------
#   audit   审计（只读·0 事件落账）：全账＋耗散通道利用率＋守恒核判定
#   settle  结算（显式）：物化衰减·视界散热·快照自核；--close＝单元终核（U→0）
#   brief   幻肢感一行（提示面动态段·只含计数）
#   belief  打印幻肢信念块（zh|en|both）
# 退出码：0 自洽 · 3 不自洽/结算失败（fail-loud·0 静默吞账）
# 账本位：--ledger > CONDENSATE_LEDGER > mcp/ledger.jsonl；参数：DEPOSON_THERMO(JSON)
# ============================================================================
import os, sys, json, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import thermo_core as tc  # noqa: E402


def main():
    ap = argparse.ArgumentParser(prog="thermo_cli", description="deposon 账本热力学命令面")
    ap.add_argument("action", choices=["audit", "settle", "brief", "belief"])
    ap.add_argument("--close", action="store_true", help="settle：单元终核（在场全散失·U→0）")
    ap.add_argument("--json", action="store_true", help="audit/settle：输出 JSON")
    ap.add_argument("--ledger", default=None, help="账本路径（缺省沿 CONDENSATE_LEDGER）")
    a = ap.parse_args()
    path = a.ledger or os.environ.get("CONDENSATE_LEDGER") or os.path.join(HERE, "ledger.jsonl")
    try:
        if a.action == "belief":
            from phantom_limb import phantom_limb_prompt
            sys.stdout.write(phantom_limb_prompt("both" if a.json else None))
            return 0
        L = tc.ThermoLedger(path, tc.load_cfg())
        if a.action == "audit":
            rep, _ = L.audit()
            out = json.dumps(rep, ensure_ascii=False, indent=1) if a.json else tc.audit_text(rep)
        elif a.action == "settle":
            rep, _ = L.settle(a.close)
            out = json.dumps(rep, ensure_ascii=False, indent=1) if a.json else tc.settle_text(rep)
        else:
            out = tc.brief_text(tc.report(L.state()))
            rep = None
        sys.stdout.write(out.rstrip("\n") + "\n")
        return 0 if rep is None or rep["verdict"] == "SELF-CONSISTENT" else 3
    except tc.LedgerInconsistent as e:
        sys.stderr.write("账本不自洽（fail-loud）: %s\n" % e)
        return 3


if __name__ == "__main__":
    sys.exit(main())
