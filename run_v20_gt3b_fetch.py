# -*- coding: utf-8 -*-
# GT-3b 跨厂商先验获取（docs/SPEC_GT3.md 修正案 A2，主代理执行）
#   评估者 E3=doubao-seed-evolving（火山引擎 Ark，第二厂商）
# key 仅从环境变量 ARK_API_KEY 读取，不打印不落盘；attempts 逐缓存落盘。
# 预算：6 域 × MAX_ATTEMPTS=2 ≤ 12 次（探测 2 次另计，修正案 A2）。
import hashlib
import json
import os

import requests

import llm_prior
from llm_prior import MAX_ATTEMPTS, build_prior_prompt
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
GT3_DIR = os.path.join(RESULTS, "gt3_prior_cache")
BASELINE_PRIOR_DIR = os.path.join(RESULTS, "familyL_prior_cache")

ARK_ENDPOINT = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
ARK_MODEL = "doubao-seed-evolving"
ARK_TIMEOUT = 240.0  # 修正案 A2：实测 60s 不足，推理模型响应慢


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    key = os.environ.get("ARK_API_KEY")
    if not key:
        raise SystemExit("ARK_API_KEY 未设置，GT-3b 挂起")
    os.makedirs(GT3_DIR, exist_ok=True)
    total_attempts = 0
    for domain in FAMILY_L_DOMAINS:
        g = json.load(open(os.path.join(CORPUS_DIR, f"L_{domain}.json"),
                           encoding="utf-8"))
        prompt = build_prior_prompt(g["labels"])
        s = sha(prompt)
        base = json.load(open(os.path.join(BASELINE_PRIOR_DIR,
                                           f"{domain}.json"), encoding="utf-8"))
        if base.get("prompt_sha256") != s:
            print(f"{domain}: prompt_mismatch, skipped")
            continue
        path = os.path.join(GT3_DIR, f"{ARK_MODEL}__{domain}.json")
        if os.path.exists(path):
            rec = json.load(open(path, encoding="utf-8"))
            if (rec.get("prompt_sha256") == s and rec.get("response_text")):
                print(f"{domain}: fresh cache, 0 attempts")
                continue
        content, last_err, attempts = None, None, 0
        for _ in range(MAX_ATTEMPTS):
            attempts += 1
            total_attempts += 1
            try:
                r = requests.post(
                    ARK_ENDPOINT,
                    headers={"Authorization": f"Bearer {key}",
                             "Content-Type": "application/json"},
                    json={"model": ARK_MODEL, "max_tokens": 8000,
                          "messages": [{"role": "user", "content": prompt}]},
                    timeout=ARK_TIMEOUT)
                if r.status_code != 200:
                    raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
                content = r.json()["choices"][0]["message"]["content"]
                if content:
                    break
            except Exception as e:
                last_err = f"{type(e).__name__}: {str(e)[:120]}"
        json.dump({"domain": domain, "kind": "gt3b_cross_vendor_prior",
                   "prompt_sha256": s, "model": ARK_MODEL,
                   "vendor": "volces_ark_bytedance",
                   "response_text": content, "attempts": attempts,
                   "last_error": last_err if not content else None,
                   "note": ("SPEC_GT3 修正案 A2；跨厂商评估者；"
                            "key 仅在运行时环境变量")},
                  open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{domain}: attempts={attempts} "
              f"{'cached ' + str(len(content)) + ' chars' if content else 'FAILED ' + str(last_err)}")
    print(f"total_http_attempts={total_attempts} (修正案预算 ≤12)")


if __name__ == "__main__":
    main()
