# -*- coding: utf-8 -*-
# GT-3a 跨评估者先验获取（docs/SPEC_GT3.md，主代理执行）
#   族 L 6 域 × 2 新评估者（moonshot-v1-8k / kimi-k2-thinking）
#   prompt 与既有先验臂逐字节相同（build_prior_prompt），prompt_sha256
#   必须匹配既有 familyL_prior_cache，否则该域记 prompt_mismatch 并跳过。
# key 仅从环境变量 KIMI_API_KEY 读取，不打印不落盘；attempts 逐缓存落盘。
# 预算（SPEC §2）：6 域 × 2 评估者 × MAX_ATTEMPTS=2 ≤ 24 次（探测 3 次另计）。
import hashlib
import json
import os

import requests

import llm_prior
from llm_prior import (ENDPOINT, MAX_ATTEMPTS, TIMEOUT, _sanitize,
                       build_prior_prompt)
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
GT3_DIR = os.path.join(RESULTS, "gt3_prior_cache")
BASELINE_PRIOR_DIR = os.path.join(RESULTS, "familyL_prior_cache")

EVALUATORS = ("moonshot-v1-8k", "kimi-k2-thinking")  # E0=kimi-for-coding 用既有缓存


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    os.makedirs(GT3_DIR, exist_ok=True)
    total_attempts = 0
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
            if os.path.exists(path):
                rec = json.load(open(path, encoding="utf-8"))
                if (rec.get("prompt_sha256") == s and rec.get("model") == model
                        and rec.get("response_text")):
                    print(f"{model}__{domain}: fresh cache, 0 attempts")
                    continue
            if not prompt_match:
                json.dump({"domain": domain, "kind": "gt3_cross_evaluator_prior",
                           "model": model, "prompt_sha256": s,
                           "prompt_mismatch": True, "response_text": None,
                           "attempts": 0},
                          open(path, "w", encoding="utf-8"),
                          ensure_ascii=False, indent=1)
                print(f"{model}__{domain}: prompt_mismatch, skipped")
                continue
            content, last_err, attempts = None, None, 0
            for _ in range(MAX_ATTEMPTS):
                attempts += 1
                total_attempts += 1
                try:
                    r = requests.post(
                        ENDPOINT,
                        headers={"Authorization": f"Bearer {key}",
                                 "Content-Type": "application/json"},
                        json={"model": model, "max_tokens": 8000,
                              "messages": [{"role": "user",
                                            "content": prompt}]},
                        timeout=TIMEOUT)
                    if r.status_code != 200:
                        raise RuntimeError(_sanitize(
                            f"HTTP {r.status_code}: {r.text[:200]}", key))
                    content = r.json()["choices"][0]["message"]["content"]
                    if content:
                        break
                except Exception as e:
                    last_err = _sanitize(f"{type(e).__name__}: {e}", key)
            json.dump({"domain": domain, "kind": "gt3_cross_evaluator_prior",
                       "prompt_sha256": s, "model": model,
                       "prompt_mismatch": False,
                       "response_text": content, "attempts": attempts,
                       "last_error": last_err if not content else None,
                       "note": ("SPEC_GT3；key 仅在运行时环境变量；"
                                "prompt 与 familyL_prior_cache 逐字节相同")},
                      open(path, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            print(f"{model}__{domain}: attempts={attempts} "
                  f"{'cached ' + str(len(content)) + ' chars' if content else 'FAILED ' + str(last_err)}")
    print(f"total_http_attempts={total_attempts} (SPEC 预算 ≤24)")


if __name__ == "__main__":
    main()
