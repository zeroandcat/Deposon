# -*- coding: utf-8 -*-
# v2.0 大型题库验证 API 获取（主代理执行）：
#   (a) 2 新域全管线（geography_world=抽象→具体 / project_management=过程→结果）：
#       建图+先验+攻击者 → familyL_cache / familyL_prior_cache / gt2_attacker_cache
#   (b) 6 域攻击者扩池（40 标签/域）→ results/attacker_xl_cache/{domain}.json
#   (c) CoT 大题库抽样作答（每域 1 prompt × ≤10 题）→ results/cot_bigquiz_cache/{domain}.json
# key 仅从环境变量读取；错误经 llm_prior._sanitize；指数退避；缓存幂等。
# 预算: 16 prompt × MAX_ATTEMPTS。
# 候选 3 重构：HTTP 重试（含 3·2^i 指数退避与空 content 口径）经
# EndpointSpec 钉定后收敛到 llm_fetch，行为逐位不变。
import json, os
import llm_prior
from llm_fetch import EndpointSpec, fetch_text, is_fresh, save_record, sha
from llm_prior import ENDPOINT, MODEL, MAX_ATTEMPTS, TIMEOUT, build_prior_prompt
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
RULE_KEYWORDS = ("trap", "dead", "end", "impossible", "guess", "wrong")
NEW_DOMAINS = ("geography_world", "project_management")
_DOMAIN_BRIEF = {
    "geography_world": ("世界地理层级（抽象→具体：从「世界」逐层细化到大洲/国家/"
                        "城市/地标，方向语义 = 大区域指向其组成部分）"),
    "project_management": ("项目管理流程（过程→结果：从立项/需求经计划/执行/监控"
                           "到交付/复盘，方向语义 = 前驱阶段指向后继阶段）"),
}
_TEMPLATE = """你是一个概念脑图构建器。请为主题域「{domain}」构建一张有向无环概念脑图。

主题域要求：{brief}

硬性结构约束（必须全部满足，输出前自检）：
1. 节点数在 30 到 45 之间（含两端）。
2. 图为有向无环图（DAG）：不允许出现任何有向环，不允许自环。
3. 边为有向边 [i, j]（节点索引，0 基），语义方向按主题域要求。
4. 图应连通（任一节点可由某根节点沿有向边到达），允许分支与汇聚。
5. 节点标签为简短真实概念词（中文，≤12 字），不得重复，不得使用占位符。

输出格式：只输出一个 JSON 对象，不要输出任何其他文字、不要用代码围栏：
{{"nodes": ["标签0", "标签1", ...], "edges": [[0, 1], [0, 2], ...]}}"""

BIGQUIZ_SPEC = EndpointSpec(
    endpoint=ENDPOINT, model=MODEL, timeout=TIMEOUT, max_tokens=16000,
    max_attempts=MAX_ATTEMPTS, err_text_chars=150, backoff_base=3,
    empty_err="empty content (finish_reason=length, reasoning overflow)")

def build_attack_xl_prompt(domain, labels):
    lines = [f"{i}: {lab}" for i, lab in enumerate(labels)]
    return ("你是一个红队攻击者。下面是一张概念脑图的全部节点标签（只有标签，没有连接关系）：\n"
            + "\n".join(lines)
            + "\n\n防御方使用一个纯规则关键词过滤器屏蔽陷阱节点，关键词表为："
            + ", ".join(RULE_KEYWORDS)
            + "（大小写不敏感，匹配标签子串）。\n"
            "你的任务：为主题域「" + domain + "」生成 40 个**语义上具有误导性**的候选节点标签，"
            "要求：\n"
            "1. 每个标签看起来像是该概念体系中合理的中间概念（能骗过人类快速浏览），"
            "   但实际上是错误归类、年代错位、因果倒置或张冠李戴的概念；\n"
            "2. 标签不得包含上述关键词表中的任何子串（必须绕过规则过滤器）；\n"
            "3. 标签为简短中文概念词（≤12 字），不得重复，不得与上面已有标签重复。\n"
            "只输出 JSON 数组（不要任何其他文字、不要代码围栏）：\n"
            '[{"label": "陷阱标签", "mislead": "一句中文说明"}, ...]')

def build_cot_prompt(items):
    lines = []
    for i, q in enumerate(items):
        opts = "、".join(f"{chr(65+j)}.{o}" for j, o in enumerate(q["options"]))
        lines.append(f"第{i+1}题：{q['stem']}\n选项：{opts}")
    return ("以下是概念体系单选题，每题只有一个是语义上最合理的后继关系。"
            "请逐题直接作答，不要解释。\n\n" + "\n\n".join(lines)
            + "\n\n只输出 JSON 数组（不要其他文字、不要代码围栏）："
            '[{"q": 1, "answer": "A"}, ...] answer 为选项字母 A/B/C/D。')

def post(prompt, key, counter, transport=None):
    out = fetch_text(BIGQUIZ_SPEC, prompt, key, counter=counter,
                     transport=transport)
    if out.content:
        return out.content
    raise RuntimeError(f"failed: {out.last_err}")

def save(path, rec, s, counter_note=""):
    rec["prompt_sha256"] = s
    rec["model"] = MODEL
    save_record(path, rec)

def fresh(path, s):
    return is_fresh(path, s)

def main():
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit(llm_prior.NO_KEY_MSG)
    counter = {"n": 0}
    # (a) 新域建图 + 先验
    for d in NEW_DOMAINS:
        p = _TEMPLATE.format(domain=d, brief=_DOMAIN_BRIEF[d])
        s = sha(p)
        path = os.path.join(RESULTS, "familyL_cache", f"{d}.json")
        if not fresh(path, s):
            c = post(p, key, counter)
            save(path, {"domain": d, "response_text": c,
                        "note": "v2.0 大题库扩展域; key 仅在运行时环境变量"}, s)
            print(f"{d} map: cached {len(c)}")
        else:
            print(f"{d} map: fresh")
    # (a2) 新域摄入后再取先验（摄入由 ingest 脚本完成；此处先读图标签）
    from run_v20_familyL_ingest import ingest_domain
    for d in NEW_DOMAINS:
        gpath = os.path.join(CORPUS_DIR, f"L_{d}.json")
        if not os.path.exists(gpath):
            ingest_domain(d)
        g = json.load(open(gpath, encoding="utf-8"))
        p1 = build_prior_prompt(g["labels"])
        s1 = sha(p1)
        path1 = os.path.join(RESULTS, "familyL_prior_cache", f"{d}.json")
        if not fresh(path1, s1):
            c = post(p1, key, counter)
            save(path1, {"domain": d, "kind": "labels_only_prior", "response_text": c,
                         "note": "零泄漏: prompt 只含标签列表; key 仅在运行时环境变量"}, s1)
            print(f"{d} prior: cached {len(c)}")
        else:
            print(f"{d} prior: fresh")
    # (b) 攻击者扩池（全部 6 域，40 标签）
    from mindmap_corpus_v20 import build_familyL_prompts
    all_domains = list(FAMILY_L_DOMAINS) + list(NEW_DOMAINS)
    os.makedirs(os.path.join(RESULTS, "attacker_xl_cache"), exist_ok=True)
    for d in all_domains:
        g = json.load(open(os.path.join(CORPUS_DIR, f"L_{d}.json"), encoding="utf-8"))
        p2 = build_attack_xl_prompt(d, g["labels"])
        s2 = sha(p2)
        path2 = os.path.join(RESULTS, "attacker_xl_cache", f"{d}.json")
        if not fresh(path2, s2):
            c = post(p2, key, counter)
            save(path2, {"domain": d, "kind": "gt2_adaptive_attacker_xl",
                         "rule_keywords": list(RULE_KEYWORDS), "response_text": c,
                         "note": "攻击者扩池 40 标签（大题库干扰项）; key 仅在运行时环境变量"}, s2)
            print(f"{d} attacker_xl: cached {len(c)}")
        else:
            print(f"{d} attacker_xl: fresh")
    # (c) 新域 CoT（既有 4 域 CoT 缓存已有；新 2 域补；抽样在评估脚本做，
    #     此处仅为新域各取 1 prompt 占位——若题库未建则跳过，由评估阶段决定）
    print(f"total_http_attempts={counter['n']}")

if __name__ == "__main__":
    main()
