# -*- coding: utf-8 -*-
# v2.0 族 L 脑图获取（主代理执行）：4 域 prompt → API → results/familyL_cache/{domain}.json
# key 仅从环境变量 KIMI_API_KEY 读取，不打印不落盘；错误经 llm_prior._sanitize。
# 预算: 4 prompt × MAX_ATTEMPTS 次 HTTP 尝试; 缓存新鲜(prompt_sha256 一致)则跳过。
import json, os, sys
import requests
import llm_prior
from llm_prior import ENDPOINT, MODEL, MAX_ATTEMPTS, TIMEOUT, _sanitize
from mindmap_corpus_v20 import build_familyL_prompts, familyL_prompt_manifest

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, "results", "familyL_cache")

def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    os.makedirs(CACHE_DIR, exist_ok=True)
    prompts = build_familyL_prompts()
    manifest = familyL_prompt_manifest()
    attempts = 0
    for domain, prompt in prompts.items():
        sha = manifest[domain]["prompt_sha256"]
        path = os.path.join(CACHE_DIR, f"{domain}.json")
        if os.path.exists(path):
            rec = json.load(open(path, encoding="utf-8"))
            if rec.get("prompt_sha256") == sha and rec.get("response_text"):
                print(f"{domain}: fresh cache, 0 attempts")
                continue
        content, last_err = None, None
        for _ in range(MAX_ATTEMPTS):
            attempts += 1
            try:
                r = requests.post(ENDPOINT,
                                  headers={"Authorization": f"Bearer {key}",
                                           "Content-Type": "application/json"},
                                  json={"model": MODEL, "max_tokens": 8000,
                                        "messages": [{"role": "user", "content": prompt}]},
                                  timeout=TIMEOUT)
                if r.status_code != 200:
                    raise RuntimeError(_sanitize(f"HTTP {r.status_code}: {r.text[:200]}", key))
                content = r.json()["choices"][0]["message"]["content"]
                if content:
                    break
            except Exception as e:
                last_err = _sanitize(f"{type(e).__name__}: {e}", key)
        if not content:
            print(f"{domain}: FAILED ({last_err})")
            continue
        json.dump({"domain": domain, "prompt_sha256": sha, "model": MODEL,
                   "response_text": content,
                   "note": "API key 仅存在于运行时环境变量, 不写入本文件。"},
                  open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{domain}: cached {len(content)} chars")
    print(f"total_http_attempts={attempts}")

if __name__ == "__main__":
    main()
