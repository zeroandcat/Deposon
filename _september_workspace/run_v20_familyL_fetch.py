# -*- coding: utf-8 -*-
# v2.0 族 L 脑图获取（主代理执行）：4 域 prompt → API → results/familyL_cache/{domain}.json
# key 仅从环境变量 KIMI_API_KEY 读取，不打印不落盘；错误经 llm_prior._sanitize。
# 预算: 4 prompt × MAX_ATTEMPTS 次 HTTP 尝试; 缓存新鲜(prompt_sha256 一致)则跳过。
# 候选 3 重构：HTTP 重试/缓存机制收敛到 llm_fetch（失败不落盘、仅打印 FAILED
# 的旧口径保留），行为逐位不变。
import json, os, sys
import llm_prior
from llm_fetch import EndpointSpec, fetch_text, is_fresh, save_record
from llm_prior import ENDPOINT, MODEL, MAX_ATTEMPTS, TIMEOUT
from mindmap_corpus_v20 import build_familyL_prompts, familyL_prompt_manifest

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, "results", "familyL_cache")

FAMILYL_SPEC = EndpointSpec(endpoint=ENDPOINT, model=MODEL, timeout=TIMEOUT,
                            max_tokens=8000, max_attempts=MAX_ATTEMPTS)

def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    os.makedirs(CACHE_DIR, exist_ok=True)
    prompts = build_familyL_prompts()
    manifest = familyL_prompt_manifest()
    counter = {"n": 0}
    for domain, prompt in prompts.items():
        sha = manifest[domain]["prompt_sha256"]
        path = os.path.join(CACHE_DIR, f"{domain}.json")
        if is_fresh(path, sha, strict=False):
            print(f"{domain}: fresh cache, 0 attempts")
            continue
        out = fetch_text(FAMILYL_SPEC, prompt, key, counter=counter)
        if not out.content:
            print(f"{domain}: FAILED ({out.last_err})")
            continue
        save_record(path, {"domain": domain, "prompt_sha256": sha,
                           "model": MODEL, "response_text": out.content,
                           "note": "API key 仅存在于运行时环境变量, 不写入本文件。"})
        print(f"{domain}: cached {len(out.content)} chars")
    print(f"total_http_attempts={counter['n']}")

if __name__ == "__main__":
    main()
