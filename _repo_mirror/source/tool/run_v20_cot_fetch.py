# -*- coding: utf-8 -*-
# v2.0 直接 CoT 大 BOSS 收编（BASELINE_REGISTRY C 族）：题库逐题直接问答
#   → results/cot_quiz_cache/{domain}.json（2 prompt/域 × 5 题打包，共 8 prompt）
# key 仅从环境变量读取；错误经 llm_prior._sanitize；缓存幂等。
# 候选 3 重构：HTTP 重试/缓存机制收敛到 llm_fetch；旧 post() 在"全部尝试
# 空 content 且无异常"路径上的 UnboundLocalError 随统一循环修复为
# RuntimeError("failed: None")（仅此崩溃路径的行为变化，见 REFACTOR_v2 §候选③）。
import json, os
import llm_prior
from llm_fetch import EndpointSpec, fetch_text, is_fresh, save_record, sha
from llm_prior import ENDPOINT, MODEL, MAX_ATTEMPTS, TIMEOUT

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
CACHE_DIR = os.path.join(RESULTS, "cot_quiz_cache")
BANK = os.path.join(RESULTS, "quizbank_v20.json")
BATCH = 5

COT_SPEC = EndpointSpec(endpoint=ENDPOINT, model=MODEL, timeout=TIMEOUT,
                        max_tokens=2000, max_attempts=MAX_ATTEMPTS,
                        err_text_chars=150)

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

def post(prompt, key, counter, transport=None):
    out = fetch_text(COT_SPEC, prompt, key, counter=counter,
                     transport=transport)
    if out.content:
        return out.content
    raise RuntimeError(f"failed: {out.last_err}")

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
            if is_fresh(path, s, strict=False):
                print(f"{d} b{bi//BATCH}: fresh")
                continue
            c = post(p, key, counter)
            save_record(path, {"domain": d, "batch": bi // BATCH,
                               "item_ids": [q["item_id"] for q in batch],
                               "prompt_sha256": s, "model": MODEL,
                               "response_text": c,
                               "note": "直接 CoT 大 BOSS 收编（BASELINE_REGISTRY C 族）; "
                                       "key 仅在运行时环境变量"})
            print(f"{d} b{bi//BATCH}: cached {len(c)} chars")
    print(f"total_http_attempts={counter['n']}")

if __name__ == "__main__":
    main()
