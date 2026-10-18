# -*- coding: utf-8 -*-
# GT-3a 跨评估者先验获取（docs/SPEC_GT3.md，主代理执行）
#   族 L 6 域 × 2 新评估者（moonshot-v1-8k / kimi-k2-thinking）
#   prompt 与既有先验臂逐字节相同（build_prior_prompt），prompt_sha256
#   必须匹配既有 familyL_prior_cache，否则该域记 prompt_mismatch 并跳过。
# key 仅从环境变量 KIMI_API_KEY 读取，不打印不落盘；attempts 逐缓存落盘。
# 预算（SPEC §2）：6 域 × 2 评估者 × MAX_ATTEMPTS=2 ≤ 24 次（探测 3 次另计）。
# 候选 3 重构：HTTP 重试/缓存机制收敛到 llm_fetch（本文件仅余配置+流程，
# 缓存文件名/prompt_sha256 落盘格式/预算计数语义逐位不变）。
import json
import os

import llm_prior
from llm_fetch import EndpointSpec, fetch_text, is_fresh, save_record, sha
from llm_prior import build_prior_prompt
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
GT3_DIR = os.path.join(RESULTS, "gt3_prior_cache")
BASELINE_PRIOR_DIR = os.path.join(RESULTS, "familyL_prior_cache")

EVALUATORS = ("moonshot-v1-8k", "kimi-k2-thinking")  # E0=kimi-for-coding 用既有缓存

# 端点/超时/预算钉定（同 llm_prior 口径；模型逐评估者派生）
GT3_SPEC = EndpointSpec(endpoint=llm_prior.ENDPOINT, model="",
                        timeout=llm_prior.TIMEOUT, max_tokens=8000,
                        max_attempts=llm_prior.MAX_ATTEMPTS)


def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    os.makedirs(GT3_DIR, exist_ok=True)
    counter = {"n": 0}
    for domain in FAMILY_L_DOMAINS:
        g = json.load(open(os.path.join(CORPUS_DIR, f"L_{domain}.json"),
                           encoding="utf-8"))
        prompt = build_prior_prompt(g["labels"])
        s = sha(prompt)
        base = json.load(open(os.path.join(BASELINE_PRIOR_DIR,
                                           f"{domain}.json"), encoding="utf-8"))
        prompt_match = bool(base.get("prompt_sha256") == s)
        for model in EVALUATORS:
            path = os.path.join(GT3_DIR, f"{model}__{domain}.json")
            if is_fresh(path, s, model=model, strict=False):
                print(f"{model}__{domain}: fresh cache, 0 attempts")
                continue
            if not prompt_match:
                save_record(path, {"domain": domain,
                                   "kind": "gt3_cross_evaluator_prior",
                                   "model": model, "prompt_sha256": s,
                                   "prompt_mismatch": True,
                                   "response_text": None, "attempts": 0})
                print(f"{model}__{domain}: prompt_mismatch, skipped")
                continue
            out = fetch_text(GT3_SPEC.for_model(model), prompt, key,
                             counter=counter)
            content, last_err, attempts = out
            save_record(path, {"domain": domain,
                               "kind": "gt3_cross_evaluator_prior",
                               "prompt_sha256": s, "model": model,
                               "prompt_mismatch": False,
                               "response_text": content, "attempts": attempts,
                               "last_error": last_err if not content else None,
                               "note": ("SPEC_GT3；key 仅在运行时环境变量；"
                                        "prompt 与 familyL_prior_cache 逐字节相同")})
            print(f"{model}__{domain}: attempts={attempts} "
                  f"{'cached ' + str(len(content)) + ' chars' if content else 'FAILED ' + str(last_err)}")
    print(f"total_http_attempts={counter['n']} (SPEC 预算 ≤24)")


if __name__ == "__main__":
    main()
