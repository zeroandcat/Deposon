# -*- coding: utf-8 -*-
"""
复算 operationalization_v1 在 80 件全量上的覆盖率
- 不写入盘,不读任何既有件,纯本地复算,产出报告(JSON)
- 0 LLM 0 proxy 0 gateway
"""
import json, hashlib, re
from pathlib import Path

# Operationalization v1 编码表 (字面沿用 _v4_pi_cot_v2_ruleset_executor.py)
KEYWORDS_KILL_LINE = ("判死线", "判死", "判对死因", "通过", "不通过", "PASS", "FAIL",
                      "阈值", "边界", "达标", "不达标", "kill", "Kill", "KILL")
KEYWORDS_COST = ("成本", "贵", "便宜", "廉价", "量化", "投入", "开销",
                 "费用", "价格", "付费", "花费", "算力", "消耗")
KEYWORDS_CRITERIA = ("准则", "原则", "口径", "规范", "约束", "标准",
                     "大材小用", "落到实处", "与死同行", "虚实回路", "FTFB",
                     "诚实", "不误导", "价值观", "世界观", "道德", "伦理",
                     "顶层", "根", "接口", "协议")
KEYWORDS_RISK = ("风险", "误报", "假fail", "假pass", "假 FAIL", "假 PASS",
                 "危害", "危机", "过敏", "不稳定", "陷阱",
                 "可疑", "漏洞", "危险", "隐患", "瑕疵", "假")
KEYWORDS_TIMING = ("时机", "暂缓", "立即", "后续", "步骤", "中途", "分批",
                   "抽样", "全量", "两步", "三步", "现在", "未来", "当下", "过去",
                   "今天", "昨天", "明天", "近", "远", "近期", "远期")
KEYWORDS_DELEGATE = ("委托", "分派", "派单", "受托", "起草", "转交",
                     "GLM", "coze", "kimi", "agent", "主轴", "共同体",
                     "受托方", "派出", "我派", "代为", "代理", "派工")

KEYWORDS_BY_TYPE = {
    "KILL_LINE": KEYWORDS_KILL_LINE,
    "COST": KEYWORDS_COST,
    "CRITERIA": KEYWORDS_CRITERIA,
    "RISK": KEYWORDS_RISK,
    "TIMING": KEYWORDS_TIMING,
    "DELEGATE": KEYWORDS_DELEGATE,
}

CRITICAL_REFLECTION_MARKERS = (
    "不", "却", "反而", "然而", "但是", "但", "其实", "区别",
    "修正", "纠", "错", "未必", "不可", "不应", "误", "批判",
    "反思", "避免", "慎重", "慎", "重新", "未必", "未必是",
    "可疑", "重新考虑", "区别于", "不一定",
)

def extract_judgment_sequence(reasoning):
    if not reasoning or not reasoning.strip():
        return []
    earliest = []
    for jt, kws in KEYWORDS_BY_TYPE.items():
        pos = -1
        for kw in kws:
            idx = reasoning.find(kw)
            if idx >= 0 and (pos < 0 or idx < pos):
                pos = idx
        if pos >= 0:
            earliest.append((pos, jt))
    earliest.sort(key=lambda x: x[0])
    seen = set()
    seq = []
    for _, jt in earliest:
        if jt not in seen:
            seen.add(jt)
            seq.append(jt)
    return seq

def primary(seq):
    return seq[0] if seq else "UNKNOWN"

def has_critical(reasoning):
    if not reasoning:
        return False
    return any(m in reasoning for m in CRITICAL_REFLECTION_MARKERS)

# 加载所有事件
RESULTS = Path("D:/私人资料/deposon-repo/results")

# v1.1 dataset
v1_events = json.loads((RESULTS / "_v4_pi_cot_v2_dataset.json").read_text(encoding="utf-8"))["events"]
# 标 wave = D1
for e in v1_events:
    e["wave"] = "D1_main"

# D1 addendum 09-24 (3 supplements, 既有 event_id 17/21/27 推理补填)
d1_add = json.loads((RESULTS / "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json").read_text(encoding="utf-8"))
d1_supp = []
for s in d1_add["supplements"]:
    # 找到原 event 的 reasoning
    eid = s["event_id"]
    base = next((e for e in v1_events if e["event_id"] == eid), None)
    if base:
        # 用 supplement 的 reasoning 替换 (因为是补填)
        d1_supp.append({
            "event_id": eid,
            "wave": "D1_supp",
            "reasoning_full": s["critical_reflection_supplement"],
            "option_chosen": base.get("option_chosen", ""),
            "scene_tag": s["scene_tag"],
            "is_correction": base.get("is_correction", False),
            "d1_reasoning_orig": base["reasoning_full"],
        })

# D2 wave1
def load_d2(p, wname):
    j = json.loads((RESULTS / p).read_text(encoding="utf-8"))
    supp = []
    for s in j.get("supplements", []):
        supp.append({
            "wave": wname,
            "pair_id": s.get("pair_id"),
            "option_chosen": s.get("option_chosen", ""),
            "other_text": s.get("other_text", ""),
            "reasoning_full": s.get("reasoning_full", ""),
            "reasoning_missing": s.get("reasoning_missing", False),
            "scene_tag": s.get("scene_tag", ""),
            "composite_option": s.get("composite_option", False),
            "ambiguous_mapping": s.get("ambiguous_mapping", False),
            "disposition": s.get("disposition", ""),
            "disposition_text": s.get("disposition_text", ""),
        })
    return supp

d2_w1 = load_d2("_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json", "D2_w1")
d2_w2 = load_d2("_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json", "D2_w2")
d2_w3 = load_d2("_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json", "D2_w3")
d2_w4 = load_d2("_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json", "D2_w4")
d2_w5 = load_d2("_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json", "D2_w5")
d3_w1 = load_d2("_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json", "D3_w1")
d3_w2 = load_d2("_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json", "D3_w2")
d3_w3 = load_d2("_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json", "D3_w3")

# 分析 - 用 supplement 后的 reasoning (D1 events + D1 supp)
all_records = []
# D1 main events
for e in v1_events:
    rf = e["reasoning_full"]
    seq = extract_judgment_sequence(rf)
    all_records.append({
        "event_id": e["event_id"],
        "wave": "D1_main",
        "q_id": e.get("q_id", ""),
        "reasoning_full": rf,
        "v1_seq": seq,
        "v1_primary": primary(seq),
        "v1_n_types": len(seq),
        "v1_has_critical": has_critical(rf),
    })

# D1 supplement 替换 reasoning
for s in d1_supp:
    rf = s["reasoning_full"]
    seq = extract_judgment_sequence(rf)
    all_records.append({
        "event_id": s["event_id"],
        "wave": "D1_supp",
        "q_id": "",
        "reasoning_full": rf,
        "v1_seq": seq,
        "v1_primary": primary(seq),
        "v1_n_types": len(seq),
        "v1_has_critical": has_critical(rf),
        "d1_reasoning_orig": s["d1_reasoning_orig"],
    })

# D2 + D3 (合并 reasoning_full + other_text 作为完整文本)
for batch_name, batch in [("D2_w1", d2_w1), ("D2_w2", d2_w2), ("D2_w3", d2_w3),
                           ("D2_w4", d2_w4), ("D2_w5", d2_w5),
                           ("D3_w1", d3_w1), ("D3_w2", d3_w2), ("D3_w3", d3_w3)]:
    for s in batch:
        rf = s.get("reasoning_full", "") or ""
        ot = s.get("other_text", "") or ""
        dt = s.get("disposition_text", "") or ""
        # 完整文本 = reasoning_full + other_text (如果 other 不空) + disposition_text
        full = rf
        if ot and ot not in rf:
            full = full + " " + ot if full else ot
        if dt and dt not in full:
            full = full + " " + dt if full else dt
        seq = extract_judgment_sequence(full)
        all_records.append({
            "pair_id": s.get("pair_id", ""),
            "wave": batch_name,
            "reasoning_full": full,
            "v1_seq": seq,
            "v1_primary": primary(seq),
            "v1_n_types": len(seq),
            "v1_has_critical": has_critical(full),
            "reasoning_missing": s.get("reasoning_missing", False),
            "ambiguous_mapping": s.get("ambiguous_mapping", False),
            "composite_option": s.get("composite_option", False),
            "disposition": s.get("disposition", ""),
        })

# 逐波统计
from collections import Counter
wave_stats = {}
for r in all_records:
    w = r["wave"]
    if w not in wave_stats:
        wave_stats[w] = {"total": 0, "unknown": 0, "primaries": Counter(),
                         "critical_true": 0, "missing_reasoning": 0,
                         "non_empty_seq": 0, "non_empty_seq_with_crit": 0}
    s = wave_stats[w]
    s["total"] += 1
    if r["v1_primary"] == "UNKNOWN":
        s["unknown"] += 1
    s["primaries"][r["v1_primary"]] += 1
    if r["v1_has_critical"]:
        s["critical_true"] += 1
    if r.get("reasoning_missing"):
        s["missing_reasoning"] += 1
    if r["v1_seq"]:
        s["non_empty_seq"] += 1
        if r["v1_has_critical"]:
            s["non_empty_seq_with_crit"] += 1

# 全局统计
total_n = len(all_records)
total_unknown = sum(1 for r in all_records if r["v1_primary"] == "UNKNOWN")
total_primaries = Counter(r["v1_primary"] for r in all_records)
total_critical = sum(1 for r in all_records if r["v1_has_critical"])

# 输出 JSON
output = {
    "schema": "v1_coverage_recompute/1",
    "n_total_records": total_n,
    "v1_unknown_rate": f"{total_unknown}/{total_n} = {total_unknown/total_n:.3f}",
    "v1_label_distribution_total": dict(total_primaries),
    "v1_total_has_critical": total_critical,
    "per_wave": wave_stats,
    "n_distinct_primary_types": len(total_primaries) - (1 if "UNKNOWN" in total_primaries else 0),
    "degeneracy_check": {
        "n_distinct_primary_types_total": len(total_primaries),
        "rule": "n_distinct ≤3 即退化警报",
        "verdict": "PASS" if len(total_primaries) > 3 else "FAIL",
    },
}

print(json.dumps(output, ensure_ascii=False, indent=2, default=str))

# 也输出每条记录的简短表 (按 wave)
print("\n--- per-record summary ---")
for r in all_records:
    print(f"{r['wave']:8} | id={r.get('event_id', r.get('pair_id', '?'))!s:10} | v1_primary={r['v1_primary']:10} | crit={r['v1_has_critical']!s:5} | seq={r['v1_seq']}")