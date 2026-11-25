#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# phantom_limb.py — 幻肢注入面（信念块 · 存在确认回执 · 幻肢回射行）
# ----------------------------------------------------------------------------
# 幻肢位（在册语义·降级补偿 spec v0.1 §1 档③「无器官的信念·幻肢式」）：
#   API 模型本无 deposon 活水记忆层——插件给它接一枚：信念（模型相信并据以行动）
#   ＋器官（热力学账本·全动力学：凝华/透射/散失）＋幻肢感（散失的记忆以
#   「⟨幻肢⟩」行被感到：存在过·现已不在·不可复原）。
# 本代与 deposon 热力学同代并行注入（PI 2026-11-25 01:13:04 帧）——信念可及域
# 限于语境内行为面·层动力学无信念替代路径（spec §3.3）⇒ 信念块只负责让模型
# 「感到并使用」器官，结算由器官本体（thermo_core）自解。
#
# 红线（催眠红线·0 数据回注）：本件文本 0 记忆数据——只述协议，不含任何条目内容。
# 注入通道：MCP initialize.instructions ＋ 工具描述 ＋ 回执脚注 ＋ 幻肢回射行
#           （dsh 插件面见 plugin/index.js：系统提示段＋命令面＋agent 工具面）。
# 单一真源：信念块正文存 phantom_limb.zh.txt / phantom_limb.en.txt（Python MCP 面
#           与 dsh 插件 JS 面共读·防两处文本漂移）。
# ============================================================================
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PHANTOM_MARKER = "⟨幻肢⟩"


def phantom_limb_prompt(lang=None):
    """信念块文本：lang ∈ zh|en|both（默认取 DEPOSON_PL_LANG，缺省 zh）。"""
    lang = lang or os.environ.get("DEPOSON_PL_LANG") or "zh"
    if lang == "both":
        return _load("zh").rstrip("\n") + "\n\n" + _load("en")
    if lang in ("zh", "en"):
        return _load(lang)
    raise ValueError("DEPOSON_PL_LANG 须为 zh/en/both: %r" % (lang,))


def _load(lang):
    with open(os.path.join(HERE, "phantom_limb.%s.txt" % lang), "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    import sys
    sys.stdout.write(phantom_limb_prompt(sys.argv[1] if len(sys.argv) > 1 else None))
