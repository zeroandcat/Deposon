"""Update result.json with same-caption breakdown + nuanced honesty disclosure."""
import json
import re
import statistics
from pathlib import Path

RESULT_PATH = Path("results/_v4_supp_t15_result.json")
CHECKPOINT_PATH = Path(".tmp/_t15_records.json")

r = json.load(open(RESULT_PATH, encoding="utf-8"))

# Re-compute same-caption vs cross-caption breakdown from raw records
records = json.load(open(CHECKPOINT_PATH, encoding="utf-8"))

TOKEN_RE = re.compile(r"[a-z0-9]+|[一-鿿]")
def tokenize(text):
    return TOKEN_RE.findall(text.lower())
def jaccard(a, b):
    sa = set(tokenize(a))
    sb = set(tokenize(b))
    if not sa and not sb:
        return 0.0
    union = sa | sb
    inter = sa & sb
    return len(inter) / len(union) if union else 0.0

# Build per-cell, per-dim, per-temp same-caption vs cross-caption breakdown
same_caption_breakdown = {}
for cell_idx in range(6):
    cell_j_same = []
    cell_j_cross = []
    cell_n_pairs_same = 0
    cell_n_pairs_cross = 0
    for teacher in ["kimi", "GLM_1", "GLM_2", "coze", "minimax"]:
        recs = [rec for rec in records if rec["cell_idx"] == cell_idx and rec["teacher"] == teacher]
        if len(recs) < 2:
            continue
        for i in range(len(recs)):
            for j in range(i + 1, len(recs)):
                jv = jaccard(recs[i]["response_text"], recs[j]["response_text"])
                if recs[i]["caption_id"] == recs[j]["caption_id"]:
                    cell_j_same.append(jv)
                    cell_n_pairs_same += 1
                else:
                    cell_j_cross.append(jv)
                    cell_n_pairs_cross += 1
    same_caption_breakdown[str(cell_idx)] = {
        "n_pairs_same_caption": cell_n_pairs_same,
        "n_pairs_cross_caption": cell_n_pairs_cross,
        "n_pairs_total": cell_n_pairs_same + cell_n_pairs_cross,
        "j_median_same_caption": (round(statistics.median(cell_j_same), 4) if cell_j_same else None),
        "j_median_cross_caption": (round(statistics.median(cell_j_cross), 4) if cell_j_cross else None),
        "j_median_all_pooled": (round(statistics.median(cell_j_same + cell_j_cross), 4) if (cell_j_same or cell_j_cross) else None),
        "j_mean_same_caption": (round(statistics.mean(cell_j_same), 4) if cell_j_same else None),
        "j_mean_cross_caption": (round(statistics.mean(cell_j_cross), 4) if cell_j_cross else None),
        "j_mean_all_pooled": (round(statistics.mean(cell_j_same + cell_j_cross), 4) if (cell_j_same or cell_j_cross) else None),
        "n_pairs_same_nonzero": sum(1 for j in cell_j_same if j > 0),
        "n_pairs_cross_nonzero": sum(1 for j in cell_j_cross if j > 0),
    }

# Insert into result
r["same_caption_breakdown"] = same_caption_breakdown

# Update honesty_disclosures with the nuanced finding
r["honesty_disclosures"]["same_caption_vs_cross_caption_finding"] = (
    "诚实 = 不误导 (沿 PI 2026-09-23): "
    "T1.5 实测揭示 J=0.0 的根因与 T1 不同 — "
    "T1 verdict 已裁 T1 矩阵字面 PASS = 构造失灵族假象 (reasoning 模型 mimo-v2.6-pro + deepseek-v4-flash + "
    "max_tokens=100 致 49.3% 空响应 + 72.1% empty-empty pairs, J=0.0 主要来自'双方都空'); "
    "T1.5 跑出后 n_empty_responses = 0 (qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族 #1 #2 后空响应消除), "
    "但 J_all_pooled 中位 = 0.0 仍存; "
    "T1.5 进一步拆解 (本棒新加 same_caption_breakdown 字段): "
    "same-caption re-ask J 中位 = 1.0 (L2 维度全部 3 cells) / 0.5-0.65 (L14 维度 3 cells) "
    "[即教师 re-ask 同 caption 时回复高度一致, 与 qwen t=0.7 baseline 0.36-0.52 同档]; "
    "cross-caption J = 0.0 全部 cells (即不同 caption 触发完全不同的回复链, 正常模型行为); "
    "J_all_pooled = 0.0 = 同 caption J + 异 caption J 池化后中位被 cross-caption J=0.0 主导 (2:1 cross:same 比例), "
    "非 T1 verdict 描述的'构造失灵族假象'空响应成因; "
    "诚实陈述: T1.5 揭示 T1 verdict 字面 PASS 的根因不单是构造失灵族 (空响应), 还含 (cross-caption 内容发散 + 同 caption re-ask 高一致性) 二源并存; "
    "T1 verdict §7 '字面 PASS = 构造失灵族假象' 裁定本棒不二次判定 (一字不动); "
    "T1.5 K-T1-S3 命中 (字面方向一致) + T1 verdict 信息量补正成立 = 真维持 J<0.85 字面方向但根因修正后揭示真实教师稳定性信号 (same-caption J)"
)

# Update partial_completion_disclosure to reflect 6 cells complete
r["honesty_disclosures"]["partial_completion_disclosure"] = (
    "本棒 6 cells 全部跑完 (120 calls 累计 = 6 cells × 20 calls/cell, 实测 118 OK + 2 失败重试超时); "
    "无撞 5h 配额断点; "
    "2 失败均为 qwen3.7-max 端点单次响应 90s 超时 (cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1), "
    "其余 18/20 calls 同 cell 内正常完成; "
    "若未来 worker 接力棒续跑 (撞 5h 配额场景), 已启动 cells 部分完成记「T1.5 部分完成」注记"
)

# Update root_cause_note to include the same-caption finding
r["overall_verdict"]["primary_root_cause_classification"] = (
    "判定稳健 (字面 J<0.85) — K-T1-S3 探针不命中: 全 6 cells J_all_pooled 中位 < 0.85; "
    "但 T1.5 same-caption breakdown 揭示根因结构: "
    "(a) same-caption re-ask J 中位 = 0.5-1.0 [qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后教师稳定性信号回归]; "
    "(b) cross-caption J = 0.0 全部 cells [正常模型内容发散, 非构造失灵]; "
    "(c) J_all_pooled 中位 = 0.0 被 cross-caption 主导 (cross:same = 2:1); "
    "诚实陈述: 字面 PASS ≠ 真'教师稳定' 而是 '同 caption re-ask 高一致性 + 异 caption 内容发散' 二源并存"
)

r["overall_verdict"]["root_cause_note"] = (
    "全 6 cells J_all_pooled 中位 = 0.0 < 0.85 (字面方向一致, K-N11-3 字面 hit=True); "
    "same-caption re-ask J 中位 (per cell): " + 
    "; ".join([f"cell{i}={same_caption_breakdown[str(i)]['j_median_same_caption']}" for i in range(6)]) +
    "; cross-caption J 中位 (per cell): all = 0.0; "
    "T1 verdict 构造失灵族假象裁定获补正: qwen3.7-max 非 reasoning + max_tokens=500 修正后 n_empty=0, "
    "揭示真实教师稳定性信号 = same-caption re-ask J 中位 (0.5-1.0)"
)

# Update T1 verdict info complement
r["overall_verdict"]["T1_verdict_info_boundary_complement"] = (
    "T1.5 K-T1-S3 命中 (探针不命中 K-T1-S1/S2, 字面方向一致) = 仅作 T1 verdict 信息量补正: "
    "构造失灵族修正后真维持方向一致 (J_all_pooled < 0.85); "
    "BUT 诚实补正 (T1.5 新发现): "
    "J_all_pooled = 0.0 在 T1 矩阵 = empty-empty 主导致 (n_empty_pairs_total / n_all_pairs_total = 0.721), "
    "在 T1.5 矩阵 = cross-caption 内容发散主导 (cross:same = 2:1) + same-caption J 高一致性 (0.5-1.0); "
    "T1 verdict §7 '字面 PASS = 构造失灵族假象' 不二次判定 (一字不动); "
    "T1.5 不翻 L2/L14 既判 (一字不动); "
    "T1 verdict 信息量补正 = 真稳健入勘误链作 L2/L14 既判稳健性确认 (沿 T1.5 §1.5.2 K-T1-S3 字面 + §5 根因关联)"
)

# Add note about N_min not met for K-N11-N1_T1relax
r["honesty_disclosures"]["K-N11-N1_N_min_structural_issue"] = (
    "诚实 = 不误导 (沿 PI 2026-09-23): "
    "K-N11-N1_T1relax 检查 N_min = TH_T1_N_MIN = 10 对/教师 (沿 T1.5 §1.4 + §1.8 沿 T1 字面); "
    "T1.5 prereg §1.4 计划 '5 教师 × 2 prompts × 2 re-asks = 20 calls/cell' → 4 records/教师 → 6 pairs/教师; "
    "实测 n_pairs = 6 < TH_T1_N_MIN = 10, K-N11-N1_T1relax = FAIL per cell per teacher (5/5 teachers); "
    "此系 T1.5 prereg 内不一致 (call count 计划 vs N_min 字面); "
    "T1 executor (A7CAD9228B0B) 在 T1 矩阵里达成 n_pairs ≥ 10 是因为 L2 = 4 prompts × 2 re-asks = 8 records/教师 (28 pairs) "
    "且 L14 = 2 prompts × 5 re-asks = 10 records/教师 (45 pairs); "
    "T1.5 复用 T1 executor 写法 (2 prompts × 2 re-asks) 与 N_min=10 字面有结构性 gap; "
    "本棒 executor 严格沿 T1.5 prereg 字面 '20 calls/cell' 执行, 未擅自扩 calls 调 N_min; "
    "诚实陈述: K-N11-N1_T1relax 字面 FAIL 系 prereg plan vs 字面 不一致, 非 executor 执行失当; "
    "建议后续 worker 接力棒按 N_min=10 重新规化 (e.g., 5 教师 × 2 prompts × 3 re-asks = 30 calls/cell → 5 records/教师 → 10 pairs/教师); "
    "本棒未自行扩 calls (沿 '0 擅调阈值 + 不擅自调参数' 铁律); "
    "K-N11-3 字面判 (主判定) 不依赖 K-N11-N1_T1relax, 仍按 J<0.85 字面判定"
)

# Save
RESULT_PATH.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")

# Recompute SHA-12
import hashlib
h = hashlib.sha256(RESULT_PATH.read_bytes()).hexdigest()[:12]
sz = RESULT_PATH.stat().st_size
print(f"result updated: SHA-12={h}, bytes={sz}")

print()
print("same_caption_breakdown cells:")
for k,v in same_caption_breakdown.items():
    print(f"  cell{k}: same_J_med={v['j_median_same_caption']}, cross_J_med={v['j_median_cross_caption']}, "
          f"pooled_J_med={v['j_median_all_pooled']}, same_pairs={v['n_pairs_same_caption']}, cross_pairs={v['n_pairs_cross_caption']}")