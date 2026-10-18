# -*- coding: utf-8 -*-
# GT-8c「领域鉴定器 v0」real_semantics 轴扩样（Ark 后端）API 获取
# （docs/SPEC_GT8C.md §4，主代理执行）：2 新真实语义域
#   A) 图生成 prompt（逐字沿用 mindmap_corpus_v20._PROMPT_TEMPLATE，只换域）
#      → results/gt8c_cache/{domain}.json
#   B) 先验臂 prompt（llm_prior.build_prior_prompt，labels-only 零泄漏）
#      → results/gt8c_cache/prior_{domain}.json
# 后端：火山引擎 Ark（EndpointSpec；vendor=volces_ark_bytedance，
#   model=doubao-seed-evolving，max_tokens=32000，timeout=300s——吸收
#   SPEC_GT8B 修正案 B2/B3 教训：推理模型 reasoning 耗尽默认 max_tokens）。
# key 仅从环境变量 ARK_API_KEY 读取，不打印不落盘；错误经 llm_fetch
# sanitize_secret（llm_prior._sanitize 同式）兜底剔除。
# 预算（SPEC_GT8C §4 预登记）: 4 prompt × MAX_ATTEMPTS=2 → 总 HTTP ≤ 8；
# 预算计数落盘 results/gt8c_cache/budget.json；缓存新鲜(prompt_sha256 一致)
# 则跳过；超时/失败如实记 fetch_failed，绝不伪造响应。
# B 阶段依赖 A 阶段缓存中的标签：A 缓存缺失/失效 → 该域先验挂起并清晰报告，
# 绝不伪造标签（与 run_v20_gt8b_fetch.py 同一纪律）。
import json
import os

import llm_prior
from llm_fetch import EndpointSpec, fetch_text, is_fresh, save_record, sha
from llm_prior import MAX_ATTEMPTS, build_prior_prompt
from mindmap_corpus_v20 import (_PROMPT_TEMPLATE, CacheMissingError,
                                parse_familyL_response)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
CACHE_DIR = os.path.join(RESULTS, "gt8c_cache")

# ------------------------------------------------- SPEC_GT8C §2 冻结常量
GT8C_DOMAINS = ("biological_taxonomy", "programming_concepts")
GT8C_DOMAIN_BRIEF = {
    "biological_taxonomy": (
        "生物分类（抽象→具体：从「生物分类」逐层细化到界/门/纲/目/科/属/种"
        "与代表物种，方向语义 = 类别指向其成员）"),
    "programming_concepts": (
        "编程概念（抽象→具体：从编程范式细化到语言特性再到具体语言/构造，"
        "方向语义 = 概念指向其实例）"),
}

# ------------------------------------------------- SPEC_GT8C §4 Ark 后端（冻结）
ARK_ENDPOINT = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
ARK_MODEL = "doubao-seed-evolving"
ARK_VENDOR = "volces_ark_bytedance"
ARK_TIMEOUT = 300.0    # SPEC_GT8C §4 预登记（吸收 GT-8b 修正案 B2/B3 教训）
ARK_MAX_TOKENS = 32000  # 推理模型 reasoning 耗尽默认 max_tokens 的教训

GT8C_SPEC = EndpointSpec(endpoint=ARK_ENDPOINT, model=ARK_MODEL,
                         timeout=ARK_TIMEOUT, max_tokens=ARK_MAX_TOKENS,
                         max_attempts=MAX_ATTEMPTS)

BUDGET_PATH = os.path.join(CACHE_DIR, "budget.json")
HTTP_BUDGET = 4 * MAX_ATTEMPTS  # SPEC_GT8C §4：4 prompt × 2 → ≤ 8


def build_gt8c_prompts() -> dict:
    """按 SPEC_GT8C §2 生成 2 个新域的建图 prompt（不执行 API）。
    模板逐字沿用 mindmap_corpus_v20._PROMPT_TEMPLATE（与族 L 同款，只换域）。"""
    return {d: _PROMPT_TEMPLATE.format(domain=d, brief=GT8C_DOMAIN_BRIEF[d])
            for d in GT8C_DOMAINS}


def gt8c_prompt_manifest() -> dict:
    """{domain: {"prompt_sha256": ...}}；prompt_sha256 落盘纪律。"""
    return {d: {"prompt_sha256": sha(p)}
            for d, p in build_gt8c_prompts().items()}


def fresh(path, s):
    return is_fresh(path, s)


def post(prompt, key, counter, transport=None):
    """单 prompt 调用，≤ MAX_ATTEMPTS 次尝试；失败抛 RuntimeError（已 sanitize）。"""
    out = fetch_text(GT8C_SPEC, prompt, key, counter=counter,
                     transport=transport)
    if out.content:
        return out.content
    raise RuntimeError(f"API failed after {MAX_ATTEMPTS} attempts: {out.last_err}")


def load_labels_from_graph_cache(domain):
    """A 阶段缓存 → 校验后的标签列表；缓存缺失/失效 → CacheMissingError。"""
    path = os.path.join(CACHE_DIR, f"{domain}.json")
    manifest = gt8c_prompt_manifest()
    if not fresh(path, manifest[domain]["prompt_sha256"]):
        raise CacheMissingError(
            f"GT-8c graph cache missing/stale: {path} — 先验臂 prompt 需要"
            "已摄入图的标签；请先完成 A 阶段图生成 fetch。绝不伪造标签。")
    rec = json.load(open(path, encoding="utf-8"))
    return parse_familyL_response(rec["response_text"])["nodes"]


def main():
    key = os.environ.get("ARK_API_KEY")
    if not key:
        raise SystemExit("ARK_API_KEY 未设置，GT-8c 挂起（no LLM API calls "
                         "issued；key 仅从环境变量读取，不打印不落盘）")
    os.makedirs(CACHE_DIR, exist_ok=True)
    counter = {"n": 0}
    manifest = gt8c_prompt_manifest()
    fetch_failed = {}
    # ---- A) 图生成（每域 1 prompt）
    for domain, prompt in build_gt8c_prompts().items():
        path = os.path.join(CACHE_DIR, f"{domain}.json")
        if fresh(path, manifest[domain]["prompt_sha256"]):
            print(f"{domain} graph: fresh cache")
            continue
        try:
            c = post(prompt, key, counter)
        except RuntimeError as e:
            fetch_failed[f"{domain}.graph"] = str(e)
            print(f"{domain} graph: FETCH_FAILED ({e})")
            continue
        save_record(path, {"domain": domain, "kind": "gt8c_graph_gen",
                           "prompt_sha256": manifest[domain]["prompt_sha256"],
                           "model": ARK_MODEL, "vendor": ARK_VENDOR,
                           "response_text": c,
                           "note": "SPEC_GT8C §2 冻结域; key 仅在运行时环境变量"})
        print(f"{domain} graph: cached {len(c)} chars")
    # ---- B) 先验臂（每域 1 prompt，labels-only 零泄漏）
    for domain in GT8C_DOMAINS:
        path = os.path.join(CACHE_DIR, f"prior_{domain}.json")
        try:
            labels = load_labels_from_graph_cache(domain)
        except CacheMissingError as e:
            fetch_failed[f"{domain}.prior"] = str(e)
            print(f"{domain} prior: DEFERRED ({e})")
            continue
        p = build_prior_prompt(labels)
        s = sha(p)
        if fresh(path, s):
            print(f"{domain} prior: fresh cache")
            continue
        try:
            c = post(p, key, counter)
        except RuntimeError as e:
            fetch_failed[f"{domain}.prior"] = str(e)
            print(f"{domain} prior: FETCH_FAILED ({e})")
            continue
        save_record(path, {"domain": domain, "kind": "labels_only_prior",
                           "prompt_sha256": s, "model": ARK_MODEL,
                           "vendor": ARK_VENDOR, "response_text": c,
                           "note": "零泄漏: prompt 只含标签列表; key 仅在运行时环境变量"})
        print(f"{domain} prior: cached {len(c)} chars")
    # ---- 预算计数落盘（SPEC_GT8C §4）
    save_record(BUDGET_PATH, {"experiment": "deposon_v20_gt8c_fetch",
                              "total_http_attempts": counter["n"],
                              "http_budget": HTTP_BUDGET,
                              "within_budget": bool(counter["n"] <= HTTP_BUDGET),
                              "max_attempts_per_prompt": MAX_ATTEMPTS,
                              "endpoint": ARK_ENDPOINT, "model": ARK_MODEL,
                              "vendor": ARK_VENDOR,
                              "timeout": ARK_TIMEOUT,
                              "max_tokens": ARK_MAX_TOKENS,
                              "fetch_failed": fetch_failed,
                              "note": "SPEC_GT8C §4 预登记预算; key 不落盘"})
    print(f"total_http_attempts={counter['n']} "
          f"(budget <= {HTTP_BUDGET}, SPEC_GT8C §4)")
    if fetch_failed:
        print("fetch_failed: " + json.dumps(fetch_failed, ensure_ascii=False))


if __name__ == "__main__":
    main()
