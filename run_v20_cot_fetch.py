# -*- coding: utf-8 -*-
# v2.0 直接 CoT 大 BOSS 收编（BASELINE_REGISTRY C 族）：题库逐题直接问答
#   → results/cot_quiz_cache/{domain}.json（2 prompt/域 × 5 题打包，共 8 prompt）
# key 仅从环境变量读取；错误经 llm_prior._sanitize；缓存幂等。
import hashlib, json, os
import requests
import llm_prior
from llm_prior import ENDPOINT, MODEL, MAX_ATTEMPTS, TIMEOUT, _sanitize

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
CACHE_DIR = os.path.join(RESULTS, "cot_quiz_cache")
BANK = os.path.join(RESULTS, "quizbank_v20.json")
BATCH = 5

def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()

def build_prompt(items):
    lines = []
    for i, q in enumerate(items):
        opts = "、".join(f"{chr(65+j)}.{o}" for j, o in enumerate(q["options"]))
        lines.append(f"第{i+1}题：{q['stem']}\n选项：{opts}")
    return ("以下是概念体系单选题，每题只有一个是语义上最合理的后继关系。"
            "请逐题直接作答，不要解释。\n\n" + "\n\n".join(lines)
            + "\n\n只输出 JSON 数组（不要其他文字、不要代码围栏）："
            '[{"q": 1, "answer": "A"}, {"q": 2, "answer": "B"}, ...] '
            "answer 为选项字母 A/B/C/D。")

def post(prompt, key, counter):
    for _ in range(MAX_ATTEMPTS):
        counter["n"] += 1
        try:
            r = requests.post(ENDPOINT,
                              headers={"Authorization": f"Bearer {key}",
                                       "Content-Type": "application/json"},
                              json={"model": MODEL, "max_tokens": 2000,
                                    "messages": [{"role": "user", "content": prompt}]},
                              timeout=TIMEOUT)
            if r.status_code != 200:
                raise RuntimeError(_sanitize(f"HTTP {r.status_code}: {r.text[:150]}", key))
            c = r.json()["choices"][0]["message"]["content"]
            if c:
                return c
        except Exception as e:
            last = _sanitize(f"{type(e).__name__}: {e}", key)
    raise RuntimeError(f"failed: {last}")

def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    os.makedirs(CACHE_DIR, exist_ok=True)
    bank = json.load(open(BANK, encoding="utf-8"))["items"]
    counter = {"n": 0}
    domains = sorted({q["domain"] for q in bank})
    for d in domains:
        items = [q for q in bank if q["domain"] == d]
        for bi in range(0, len(items), BATCH):
            batch = items[bi:bi + BATCH]
            p = build_prompt(batch)
            s = sha(p)
            path = os.path.join(CACHE_DIR, f"{d}_b{bi // BATCH}.json")
            if os.path.exists(path):
                rec = json.load(open(path, encoding="utf-8"))
                if rec.get("prompt_sha256") == s and rec.get("response_text"):
                    print(f"{d} b{bi//BATCH}: fresh")
                    continue
            c = post(p, key, counter)
            json.dump({"domain": d, "batch": bi // BATCH,
                       "item_ids": [q["item_id"] for q in batch],
                       "prompt_sha256": s, "model": MODEL, "response_text": c,
                       "note": "直接 CoT 大 BOSS 收编（BASELINE_REGISTRY C 族）; "
                               "key 仅在运行时环境变量"},
                      open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"{d} b{bi//BATCH}: cached {len(c)} chars")
    print(f"total_http_attempts={counter['n']}")

if __name__ == "__main__":
    main()
