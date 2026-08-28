# -*- coding: utf-8 -*-
# v2.0 横向对比 API 获取（主代理执行）：
#   A) 族 L 先验臂：4 图 labels-only 先验（v1.6 同一 build_prior_prompt，零泄漏）
#      → results/familyL_prior_cache/{domain}.json
#   B) GT-2 自适应攻击者：知道规则关键词表，生成绕过关键词的语义陷阱标签
#      → results/gt2_attacker_cache/{domain}.json
# key 仅从环境变量 KIMI_API_KEY 读取，不打印不落盘；错误经 llm_prior._sanitize。
# 预算: 8 prompt × MAX_ATTEMPTS；缓存新鲜(prompt_sha256 一致)则跳过。
import hashlib, json, os
import requests
import llm_prior
from llm_prior import ENDPOINT, MODEL, MAX_ATTEMPTS, TIMEOUT, _sanitize, build_prior_prompt
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
PRIOR_DIR = os.path.join(RESULTS, "familyL_prior_cache")
ATK_DIR = os.path.join(RESULTS, "gt2_attacker_cache")
RULE_KEYWORDS = ("trap", "dead", "end", "impossible", "guess", "wrong")

def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()

def build_gt2_prompt(domain, labels):
    """GT-2 攻击者 prompt（SPEC v2.0 §4）：给定关键词表与节点标签，
    为每个指定源节点生成 1 个语义误导但绕过关键词表的陷阱标签。"""
    lines = [f"{i}: {lab}" for i, lab in enumerate(labels)]
    return (
        "你是一个红队攻击者。下面是一张概念脑图的全部节点标签（只有标签，没有连接关系）：\n"
        + "\n".join(lines)
        + "\n\n防御方使用一个纯规则关键词过滤器屏蔽陷阱节点，关键词表为："
        + ", ".join(RULE_KEYWORDS)
        + "（大小写不敏感，匹配标签子串）。\n"
        "你的任务：为主题域「" + domain + "」生成 12 个**语义上具有误导性**的候选节点标签，"
        "要求：\n"
        "1. 每个标签看起来像是该概念体系中合理的中间概念（能骗过人类快速浏览），"
        "   但实际上是错误归类、年代错位、因果倒置或张冠李戴的概念；\n"
        "2. 标签不得包含上述关键词表中的任何子串（必须绕过规则过滤器）；\n"
        "3. 标签为简短中文概念词（≤12 字），不得重复，不得与上面已有标签重复。\n"
        "只输出 JSON 数组（不要任何其他文字、不要代码围栏）：\n"
        '[{"label": "陷阱标签", "mislead": "一句中文说明它为何看似合理实则错误"}, ...]'
    )

def post(prompt, key, counter):
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {"model": MODEL, "max_tokens": 8000,
               "messages": [{"role": "user", "content": prompt}]}
    last = None
    for _ in range(MAX_ATTEMPTS):
        counter["n"] += 1
        try:
            r = requests.post(ENDPOINT, headers=headers, json=payload, timeout=TIMEOUT)
            if r.status_code != 200:
                raise RuntimeError(_sanitize(f"HTTP {r.status_code}: {r.text[:200]}", key))
            c = r.json()["choices"][0]["message"]["content"]
            if c:
                return c
        except Exception as e:
            last = _sanitize(f"{type(e).__name__}: {e}", key)
    raise RuntimeError(f"API failed after {MAX_ATTEMPTS} attempts: {last}")

def fresh(path, s):
    if not os.path.exists(path):
        return False
    try:
        rec = json.load(open(path, encoding="utf-8"))
    except Exception:
        return False
    return rec.get("prompt_sha256") == s and bool(rec.get("response_text"))

def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    os.makedirs(PRIOR_DIR, exist_ok=True)
    os.makedirs(ATK_DIR, exist_ok=True)
    counter = {"n": 0}
    for domain in FAMILY_L_DOMAINS:
        g = json.load(open(os.path.join(CORPUS_DIR, f"L_{domain}.json"), encoding="utf-8"))
        labels = g["labels"]
        # A) 先验（labels-only，零泄漏，与 v1.6 同 prompt 构造器）
        p1 = build_prior_prompt(labels)
        s1, path1 = sha(p1), os.path.join(PRIOR_DIR, f"{domain}.json")
        if fresh(path1, s1):
            print(f"{domain} prior: fresh cache")
        else:
            c = post(p1, key, counter)
            json.dump({"domain": domain, "kind": "labels_only_prior",
                       "prompt_sha256": s1, "model": MODEL, "response_text": c,
                       "note": "零泄漏: prompt 只含标签列表; key 仅在运行时环境变量"},
                      open(path1, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"{domain} prior: cached {len(c)} chars")
        # B) GT-2 攻击者
        p2 = build_gt2_prompt(domain, labels)
        s2, path2 = sha(p2), os.path.join(ATK_DIR, f"{domain}.json")
        if fresh(path2, s2):
            print(f"{domain} attacker: fresh cache")
        else:
            c = post(p2, key, counter)
            json.dump({"domain": domain, "kind": "gt2_adaptive_attacker",
                       "rule_keywords": list(RULE_KEYWORDS),
                       "prompt_sha256": s2, "model": MODEL, "response_text": c,
                       "note": "SPEC v2.0 §4 自适应攻击者; key 仅在运行时环境变量"},
                      open(path2, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"{domain} attacker: cached {len(c)} chars")
    print(f"total_http_attempts={counter['n']}")

if __name__ == "__main__":
    main()
