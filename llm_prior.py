# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.6 LLM 语义先验模块 (SPEC v1.6 §1)
#
# 假说: v1.5 物理场在语义边上输随机是因为未做 LLM 集成; 纯仿物理不含语义信息。
# 本模块向 LLM (kimi-for-coding, 与 deposon_agents_v1_4 同 endpoint/model) 询问
# "仅凭节点标签, 哪些父→子语义边最可能存在", 作为实验 B 留一协议的语义先验臂。
#
# 红线:
# - 零泄漏: build_prior_prompt 只把节点标签给 LLM, 不含任何边/图结构信息。
# - API key 仅从环境变量 KIMI_API_KEY 读取, 绝不写入任何文件/日志/异常消息
#   (异常消息经 _sanitize 兜底剔除)。
# - 无 key 抛 RuntimeError, 严禁 mock 冒充真实调用结果。
# - LLM 调用总预算 <= 2 次 (全局先验 1 次 + 必要时重试 1 次, SPEC v1.6 §4)。
# - 响应 JSON 落盘缓存 (results/llm_prior_cache.json) 供复现。
# ============================================================
import hashlib
import json
import os
import re

import requests

ENDPOINT = "https://api.kimi.com/coding/v1/chat/completions"  # 与 deposon_agents_v1_4 一致
MODEL = "kimi-for-coding"
MAX_ATTEMPTS = 2          # SPEC v1.6 §4: 全局先验一次 + 必要时重试一次
TIMEOUT = 120.0
NO_KEY_MSG = "KIMI_API_KEY 未设置，LLM 臂挂起"


# ---------------------------------------------------------------- prompt
def build_prior_prompt(labels: list) -> str:
    """构造先验 prompt: 只给 LLM 节点标签 (带索引), 要求输出最可能的父→子语义边。

    零泄漏约定: 输入仅有 labels, 函数不接收也不构造任何边/图结构信息,
    prompt 中不存在任何索引对 (u, v) / u->v / u→v 形式的结构暗示
    (schema 中的 parent/child 为占位说明, 非具体索引对)。
    """
    lines = [f"{i}: {lab}" for i, lab in enumerate(labels)]
    return (
        "你是知识图谱语义分析器。下面是一张脑图的全部节点标签列表"
        "（只有标签，没有给你任何连接关系）。\n"
        + "\n".join(lines)
        + "\n\n请仅凭这些标签的语义，推断节点之间最可能存在的「父 → 子」语义关联，"
        "输出严格 JSON 数组（不要任何额外文字、不要 markdown 围栏），格式：\n"
        '[{"parent": 父节点索引, "child": 子节点索引, "confidence": 0到1的浮点数}, ...]\n'
        "规则：\n"
        "1. parent 与 child 必须是上面列表中出现的索引（整数）。\n"
        "2. confidence 表示你对该语义关联成立的把握，0 到 1 之间。\n"
        "3. 只输出你确有把握的关联，宁缺毋滥；索引不得自指。\n"
        "4. 只输出 JSON 数组本身。"
    )


# ---------------------------------------------------------------- 解析
def _extract_json_array(text: str) -> list:
    """从 LLM 响应中抽出 JSON 数组 (容忍 markdown 围栏与前后杂文本)。"""
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.MULTILINE).strip()
    i, j = t.find("["), t.rfind("]")
    if i < 0 or j <= i:
        raise ValueError("响应中未找到 JSON 数组")
    return json.loads(t[i:j + 1])


def _validate_prior(items: list, n_labels: int) -> dict:
    """校验并规整为 dict[(int,int), float]; confidence 截断到 [0,1]。"""
    if not isinstance(items, list):
        raise ValueError("先验必须是 JSON 数组")
    out = {}
    for it in items:
        u, v = int(it["parent"]), int(it["child"])
        if not (0 <= u < n_labels and 0 <= v < n_labels):
            raise ValueError(f"先验索引越界: ({u}, {v}) n_labels={n_labels}")
        if u == v:
            continue  # 自指忽略 (prompt 已禁止, 双保险)
        c = float(it["confidence"])
        out[(u, v)] = min(1.0, max(0.0, c))
    if not out:
        raise ValueError("先验数组为空")
    return out


def _sanitize(msg: str, secret: str) -> str:
    """兜底: 异常/HTTP 回显中若意外含有 secret, 一律剔除 (key 不写入日志/异常)。"""
    return msg.replace(secret, "***") if secret else msg


# ---------------------------------------------------------------- 调用
def call_llm_prior(cache_path: str, labels: list = None) -> dict:
    """调用 Kimi API 获取全局语义先验, 响应 JSON 落盘 cache_path 供复现。

    返回 dict[(int,int), float]。labels=None 时用实验 B 脑图的 45 个标签
    (SPEC 签名 call_llm_prior(cache_path); 标签来自 run_v15_experiment 的
    确定性重建, 非任何外部文件)。
    无 KIMI_API_KEY 时抛 RuntimeError —— 严禁 mock 冒充真实调用结果。
    预算: 最多 MAX_ATTEMPTS=2 次 HTTP 尝试 (SPEC v1.6 §4)。
    """
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise RuntimeError(NO_KEY_MSG)
    if labels is None:
        from run_v15_experiment import reconstruct_mindmap
        labels = reconstruct_mindmap()[3]
    prompt = build_prior_prompt(labels)
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {"model": MODEL, "max_tokens": 4000,
               "messages": [{"role": "user", "content": prompt}]}
    last_err = None
    for _attempt in range(MAX_ATTEMPTS):
        try:
            resp = requests.post(ENDPOINT, headers=headers, json=payload,
                                 timeout=TIMEOUT)
            if resp.status_code != 200:
                raise RuntimeError(
                    _sanitize(f"HTTP {resp.status_code}: {resp.text[:200]}", key))
            content = resp.json()["choices"][0]["message"]["content"]
            if not content:
                raise RuntimeError("空 content 响应")
            prior = _validate_prior(_extract_json_array(content), len(labels))
            record = {
                "spec_version": "v1.6",
                "model": MODEL,
                "endpoint": ENDPOINT,
                "n_labels": len(labels),
                "prompt_sha256": hashlib.sha256(
                    prompt.encode("utf-8")).hexdigest(),
                "n_prior_edges": len(prior),
                "prior": [{"parent": int(u), "child": int(v), "confidence": float(c)}
                          for (u, v), c in sorted(prior.items())],
                "note": "真实 Kimi API 响应落盘缓存, 供复现; API key 仅存在于运行时"
                        "环境变量, 不写入本文件。",
            }
            os.makedirs(os.path.dirname(os.path.abspath(cache_path)),
                        exist_ok=True)
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(record, f, ensure_ascii=False, indent=1)
            return prior
        except Exception as e:  # 含网络错误/解析错误; 重试一次后放弃 (预算上限)
            last_err = _sanitize(f"{type(e).__name__}: {e}", key)
    raise RuntimeError(
        f"LLM 先验调用失败 ({MAX_ATTEMPTS} 次尝试, SPEC 预算上限): {last_err}")


def load_prior(cache_path: str) -> dict:
    """解析缓存先验 → dict[(int,int), float] (confidence 截断到 [0,1])。"""
    with open(cache_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    for it in data["prior"]:
        u, v = int(it["parent"]), int(it["child"])
        if u == v:
            continue
        c = float(it["confidence"])
        out[(u, v)] = min(1.0, max(0.0, c))
    return out
