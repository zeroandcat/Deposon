# -*- coding: utf-8 -*-
"""
operationalization_v2 设计 + 重测 + 双读抽验
- v2 = 宽口径同义关键词扩充(同 6 类 + UNKNOWN 兜底)
- 首现位置扫描 + 纯函数确定性 + seed=42 沿字面
- 判定阈值/kill-line 一字不动
"""
import json, hashlib, re
from pathlib import Path
from collections import Counter

RESULTS = Path("D:/私人资料/deposon-repo/results")

# ============================================================================
# operationalization_v1 (字面沿用 _v4_pi_cot_v2_ruleset_executor.py)
# ============================================================================
KW_V1 = {
    "KILL_LINE": ("判死线", "判死", "判对死因", "通过", "不通过", "PASS", "FAIL",
                  "阈值", "边界", "达标", "不达标", "kill", "Kill", "KILL"),
    "COST": ("成本", "贵", "便宜", "廉价", "量化", "投入", "开销",
             "费用", "价格", "付费", "花费", "算力", "消耗"),
    "CRITERIA": ("准则", "原则", "口径", "规范", "约束", "标准",
                 "大材小用", "落到实处", "与死同行", "虚实回路", "FTFB",
                 "诚实", "不误导", "价值观", "世界观", "道德", "伦理",
                 "顶层", "根", "接口", "协议"),
    "RISK": ("风险", "误报", "假fail", "假pass", "假 FAIL", "假 PASS",
             "危害", "危机", "过敏", "不稳定", "陷阱",
             "可疑", "漏洞", "危险", "隐患", "瑕疵", "假"),
    "TIMING": ("时机", "暂缓", "立即", "后续", "步骤", "中途", "分批",
               "抽样", "全量", "两步", "三步", "现在", "未来", "当下", "过去",
               "今天", "昨天", "明天", "近", "远", "近期", "远期"),
    "DELEGATE": ("委托", "分派", "派单", "受托", "起草", "转交",
                 "GLM", "coze", "kimi", "agent", "主轴", "共同体",
                 "受托方", "派出", "我派", "代为", "代理", "派工"),
}

# ============================================================================
# operationalization_v2 (本次复核件定稿)
#   - 同 6 类 + UNKNOWN 兜底(沿 prereg §1 字面)
#   - 宽口径同义关键词扩充(基于 80 件 reasoning_full 已现 PI 表达)
#   - 严禁单字"派"/"通"等过广词
#   - 第一位位置扫描 + 纯函数确定性 + seed=42 沿字面
# ============================================================================
KW_V2 = {
    "KILL_LINE": KW_V1["KILL_LINE"] + (
        # v2 扩: PI 风格"完成性"/"证伪性"判据词
        "立案", "完工", "跑完", "跑通", "判据", "判据序列",
        "真证伪", "假证伪", "实证", "证伪", "死兆", "否决",
        "PASS判定", "FAIL判定", "FALSIFY", "PASS 立案",
        "立案", "完工标准", "通过门槛",
    ),
    "COST": KW_V1["COST"] + (
        # v2 扩: PI 风格"资源"/"资金"语境
        "资源", "资金", "经费", "算账", "无尽资源", "资金有限",
        "财力", "花钱", "收费", "资源留给", "没资源", "资源不够",
        "价格", "贵", "便宜", "省钱",
    ),
    "CRITERIA": KW_V1["CRITERIA"] + (
        # v2 扩: deposon 凝子/大一统/硬核/庖丁解牛/虚实闭合/伦理 等 PI 哲学口径
        "deposon", "凝子", "大一统", "大一统定义", "硬核",
        "客观", "区别于", "区别", "区分",
        "庖丁解牛", "数学等价", "物理唯一", "哲学命题", "虚实闭合",
        "时代铁律", "PI铁律", "PI 铁律",
        "唯物主义", "唯物史观", "朴素哲学", "马哲",
        "一视同仁", "一杆进洞", "落地", "实操",
        "优雅", "优雅回归", "外审",
        "反哺", "判据结构", "判据优先序",
        "顶层设计", "准则应用", "诚实边界",
        "判死先于", "可判", "可证伪", "判死线先于",
        "判对死因", "F-C3", "T/D/R", "接口协议",
        "万物理论", "大一统理论", "大一统命题",
        "伦理", "道德", "严谨", "求是",
        "数学恒等", "软化", "不软化",
        "派工单", "规则集", "判据类型", "结构相似度",
    ),
    "RISK": KW_V1["RISK"] + (
        # v2 扩: PI 风格"过敏"/"误导"/"不一致"语境
        "过敏反应", "过敏", "误导", "误导性",
        "不一致", "冲突", "不一", "错定", "错位",
        "假fail", "假pass", "假fail", "假pass", "假证",
        "过敏感", "BUG", "bug", "假证伪",
        "不可靠", "不可信", "不安全", "不稳",
        "不可", "误报", "假",
    ),
    "TIMING": KW_V1["TIMING"] + (
        # v2 扩: PI 风格"先斩后奏"/"补测"/"重判"/"续采"
        "先斩后奏", "补测", "续采", "重判", "重做", "续做",
        "实时", "等待", "轮询",
        "初稿先行", "回收站", "补一晚",
        "几天后", "三读", "跨日", "续",
        "判后再判", "分批上线", "不宣称",
        "按计划", "逐步", "迭代", "接续", "续", "待",
        "先…再", "分阶段", "阶段",
    ),
    "DELEGATE": KW_V1["DELEGATE"] + (
        # v2 扩: PI 风格"Mavis"/"sub-agent"/"VS code"/"外援"/"第三方"/"共同体"
        "Mavis", "mavis", "sub-agent", "subagent",
        "VS code", "VSCode", "vs code",
        "外援", "第三方", "第三方汇总", "verifier",
        "组织行为学", "集群",
        "转派", "派给", "派去",
        "协助", "求助",
        "派兼职", "受托方", "起草类",
        "委派", "托付", "交代",
        "worker", "verifier", "doc-writer",
        "GLM", "kimi", "coze",
        "派工", "派出",
        "委托", "派单",
        "agent 集群", "Mavis 永不", "Mavis自撰",
    ),
}

# ============================================================================
# 编码逻辑(同 v1 + v2,字面执行)
# ============================================================================
def encode(reasoning, kw_map):
    if not reasoning or not reasoning.strip():
        return []
    earliest = []
    for jt, kws in kw_map.items():
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

# ============================================================================
# 加载 80 件 (72 实际可得 + 8 D1 reasoning补填 缺位)
# ============================================================================
v1_events = json.loads((RESULTS / "_v4_pi_cot_v2_dataset.json").read_text(encoding="utf-8"))["events"]
for e in v1_events:
    e["wave"] = "D1_main"

d1_add = json.loads((RESULTS / "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json").read_text(encoding="utf-8"))
d1_supp = []
for s in d1_add["supplements"]:
    eid = s["event_id"]
    base = next((e for e in v1_events if e["event_id"] == eid), None)
    if base:
        d1_supp.append({
            "event_id": eid, "wave": "D1_supp",
            "reasoning_full": s["critical_reflection_supplement"],
            "d1_reasoning_orig": base["reasoning_full"],
        })

def load_batch(p, wname):
    j = json.loads((RESULTS / p).read_text(encoding="utf-8"))
    out = []
    for s in j.get("supplements", []):
        out.append({
            "pair_id": s.get("pair_id", ""), "wave": wname,
            "reasoning_full": s.get("reasoning_full", "") or "",
            "other_text": s.get("other_text", "") or "",
            "disposition_text": s.get("disposition_text", "") or "",
            "reasoning_missing": s.get("reasoning_missing", False),
            "ambiguous_mapping": s.get("ambiguous_mapping", False),
            "composite_option": s.get("composite_option", False),
            "scene_tag": s.get("scene_tag", ""),
        })
    return out

d2_w1 = load_batch("_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json", "D2_w1")
d2_w2 = load_batch("_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json", "D2_w2")
d2_w3 = load_batch("_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json", "D2_w3")
d2_w4 = load_batch("_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json", "D2_w4")
d2_w5 = load_batch("_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json", "D2_w5")
d3_w1 = load_batch("_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json", "D3_w1")
d3_w2 = load_batch("_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json", "D3_w2")
d3_w3 = load_batch("_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json", "D3_w3")

records = []
for e in v1_events:
    records.append({"id": e["event_id"], "wave": "D1_main", "rf": e["reasoning_full"]})
for s in d1_supp:
    records.append({"id": s["event_id"], "wave": "D1_supp", "rf": s["reasoning_full"]})
for batch_name, batch in [("D2_w1", d2_w1), ("D2_w2", d2_w2), ("D2_w3", d2_w3),
                          ("D2_w4", d2_w4), ("D2_w5", d2_w5),
                          ("D3_w1", d3_w1), ("D3_w2", d3_w2), ("D3_w3", d3_w3)]:
    for s in batch:
        rf = s.get("rf", "") or s.get("reasoning_full", "")
        ot = s.get("other_text", "")
        dt = s.get("disposition_text", "")
        full = rf
        if ot and ot not in full:
            full = full + " " + ot if full else ot
        if dt and dt not in full:
            full = full + " " + dt if full else dt
        records.append({"id": s.get("pair_id", "?"), "wave": batch_name, "rf": full,
                        "reasoning_missing": s.get("reasoning_missing", False),
                        "scene_tag": s.get("scene_tag", "")})

# ============================================================================
# v1 vs v2 重测
# ============================================================================
for r in records:
    rf = r["rf"]
    r["v1_seq"] = encode(rf, KW_V1)
    r["v1_primary"] = primary(r["v1_seq"])
    r["v2_seq"] = encode(rf, KW_V2)
    r["v2_primary"] = primary(r["v2_seq"])

# 全局统计
v1_unknown = sum(1 for r in records if r["v1_primary"] == "UNKNOWN")
v2_unknown = sum(1 for r in records if r["v2_primary"] == "UNKNOWN")
v1_dist = Counter(r["v1_primary"] for r in records)
v2_dist = Counter(r["v2_primary"] for r in records)

print(f"总记录数: {len(records)}")
print(f"v1 UNKNOWN: {v1_unknown}/{len(records)} = {v1_unknown/len(records):.3f}")
print(f"v2 UNKNOWN: {v2_unknown}/{len(records)} = {v2_unknown/len(records):.3f}")
print(f"改善: -{(v1_unknown - v2_unknown)} 件 ({(v1_unknown - v2_unknown)/len(records)*100:.1f} 个百分点)")
print()
print(f"v1 label_dist: {dict(v1_dist)}")
print(f"v2 label_dist: {dict(v2_dist)}")
print()

# 逐波
print("--- 逐波 v1 vs v2 ---")
wave_stats = {}
for r in records:
    w = r["wave"]
    if w not in wave_stats:
        wave_stats[w] = {"total": 0, "v1_unk": 0, "v2_unk": 0,
                         "v1_dist": Counter(), "v2_dist": Counter()}
    s = wave_stats[w]
    s["total"] += 1
    s["v1_dist"][r["v1_primary"]] += 1
    s["v2_dist"][r["v2_primary"]] += 1
    if r["v1_primary"] == "UNKNOWN": s["v1_unk"] += 1
    if r["v2_primary"] == "UNKNOWN": s["v2_unk"] += 1

for w in ["D1_main", "D1_supp", "D2_w1", "D2_w2", "D2_w3", "D2_w4", "D2_w5",
          "D3_w1", "D3_w2", "D3_w3"]:
    s = wave_stats[w]
    print(f"{w:9} | n={s['total']} | v1_UNK={s['v1_unk']}/{s['total']}={s['v1_unk']/s['total']:.2f} | "
          f"v2_UNK={s['v2_unk']}/{s['total']}={s['v2_unk']/s['total']:.2f} | "
          f"v2_dist={dict(s['v2_dist'])}")

print()
print("--- v1→v2 标签变化 (非UNKNOWN 即改判) ---")
changes = []
for r in records:
    if r["v1_primary"] != r["v2_primary"]:
        changes.append(r)
print(f"v1→v2 改判总数: {len(changes)}")
for c in changes[:30]:
    print(f"  {c['wave']:9} id={c['id']:12} | v1={c['v1_primary']:10} → v2={c['v2_primary']:10} | "
          f"seq v1={c['v1_seq']} → v2={c['v2_seq']} | rf='{c['rf'][:60]}...'")

# 输出 抽样 25 件的 v1 vs v2 双编码结果(用于复核件)
print()
print("--- 双读抽验: 25 件 D1_main + D2/D3 抽样 (覆盖各波) ---")
sample_targets = [
    # D1_main 全 37 (按 verdict.md 关注的 3 件: idx=16/20/26 + idx=3 + idx=22)
    3, 5, 7, 8, 10, 14, 16, 18, 20, 22, 24, 26, 28,
    # D2/D3 各 3 件
    "R1b", "Q40", "Q48",  # D2
    "Q1_third_read", "Q4_third_read", "Q16_third_read",  # D3
]
sampled = []
for tid in sample_targets:
    found = None
    for r in records:
        if r["id"] == tid:
            found = r
            break
    if found:
        sampled.append(found)
        print(f"  {found['wave']:9} id={found['id']:18} | v1_primary={found['v1_primary']:10} v2_primary={found['v2_primary']:10}")
    else:
        print(f"  id={tid} not found")

# 把结果写出来供后续使用
out = {
    "schema": "v1_v2_redesign_compare/1",
    "n_records": len(records),
    "v1_unknown_count": v1_unknown, "v1_unknown_rate": v1_unknown/len(records),
    "v2_unknown_count": v2_unknown, "v2_unknown_rate": v2_unknown/len(records),
    "improvement": v1_unknown - v2_unknown,
    "v1_label_dist": dict(v1_dist),
    "v2_label_dist": dict(v2_dist),
    "per_wave": {w: {
        "total": wave_stats[w]["total"],
        "v1_unknown": wave_stats[w]["v1_unk"],
        "v2_unknown": wave_stats[w]["v2_unk"],
        "v1_label_dist": dict(wave_stats[w]["v1_dist"]),
        "v2_label_dist": dict(wave_stats[w]["v2_dist"]),
    } for w in wave_stats},
    "n_changed_primary_v1_to_v2": len(changes),
}

(RESULTS / "_tmp_v2_compare.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("\n输出 -> results/_tmp_v2_compare.json")