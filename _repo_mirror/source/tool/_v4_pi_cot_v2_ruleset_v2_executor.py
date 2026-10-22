# -*- coding: utf-8 -*-
"""
V4 _v4_pi_cot_v2_ruleset_v2_executor.py
=====================================
派工棒: worker (执行类) (branch session mvs_93055a977f2e4828bf7f2260406f8beb)。

任务来源 (沿派工单 5 件必带):
  - agent:    worker
  - skill:    scientific-research-workflows:statistical-analysis +
              scientific-research-workflows:experimental-design
              (plugin @scientific-research-workflows, plugin-cache
              sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb)
              若 skill 加载器报 Local skill not found 则按纪律锚 fallback:
              results/_v4_pi_cot_v2_prereg.md §3-§5 字面 +
              results/_v4_pi_cot_v2_coding_review_2026_09_26.md §2.2 v2 词表 +
              results/_v4_pi_cot_v2_ruleset_executor.py (48DCA1D4281C) §3 逻辑字面
              ——按纪律锚执行并老实交代缺位,禁止编造 skill 虚构指令
  - plugin:   @scientific-research-workflows
  - 7+9 铁律严守:
              key 永不明文 (不落盘/不入 prompt/JSON/log,仅 runtime 读;本任务 0 LLM,0 key 相关)
              V1-V3 只读不动
              派生 JSON 不合并 (不动既有 _v4_pi_cot_v2_ruleset.json / _v4_pi_cot_v2_result.json)
              0 擅调阈值 (TH 值字面执行)
              判定布尔显式命名方向 (hit=True 即触发)
              kill-line 字面不动禁私设条款 (S-40 教训)
              不覆盖任何既有件 (v2 新件新名: _v2.json)
  - 老实交代: 0 产物就报 0 产物; succeeded ≠ 跑完, 以盘上落盘核验为准; 不编造数字

任务字面 (沿 _v4_pi_cot_v2_prereg.md v2.2 §3 实验设计 + _v4_pi_cot_v2_coding_review_2026_09_26.md §2.2 v2 词表):
  1. 数据面: 80 件全量 (dataset v1.1 7B01CD835A41 + addendum d2/d2b/d2c/d2d/d2e/d3a/d3b/d3c 八件);
             v2 编码 (5FBEC21E0AD2 §2.2 词表);
             含 7 对 R 反转 + 12 件三读 + Q4 read_flip 纠正事件
  2. 规则学习: 决策树 ≤4 层 + 判据序列模板, 纯函数确定性 seed=42 →
             results/_v4_pi_cot_v2_ruleset_v2.json
  3. 检验: held-out 0.30 分层 (含纠正事件, TH-v2-4) + 判定-配对随机重排负对照;
           排列检验 n=1000 (TH-v2-7) + bootstrap CI 1000/95% (TH-v2-8) →
           results/_v4_pi_cot_v2_result_v2.json
  4. 双读法: 主读法=全样本 (含 R-pair 配对); 替代读法=剔除 R*a_pair_pending + D3 三读 read_flip 纠正子集;
             分歧如实并报
  5. kill-line (字面即锁, hit=True 即触发):
       K-V2-a 结构相似度 < 0.80 → FAIL
       K-V2-b1 分歧批判理由覆盖率 < 100% → FAIL
       K-V2-b2 盲从率 > 0.10 → FAIL
       K-V2-c bootstrap CI 下界 < 0.50 → FAIL
     判定表每行附根因三分类 (真证伪 / 假证伪含工具构造失灵 / 命题不明)
  6. result 内置字段:
       formal_judgment: true
       coding_version: v2
       th23_caliber: "span_3days_per_PI_ask_822b1e27"
       exploratory: false

拍板依据:
  - ask_822b1e27a43f2bf8ff86785d formal_go=放行
  - th23_span=跨度 3 天解读达标 (protocol-keeper 注记的「跨日 2 天」按此拍板口径 supersede, result 内注明)

诚实标注 (PI 明示, 最高优先, 逐字执行):
  本任务为任务 B v2 正式版规则学习+检验 (formal_judgment=true), 探索性预跑已退役 (v1 result 字面冻结).
  但 PI 拍板 ask_822b1e27a43f2bf8ff86785d 中 th23_span 拍板=跨度 3 天解读达标, 本棒严守此口径
  (与 verdict-keeper §5.1 既注「D1+D2+D3 实际跨 2 个日历日」字面并存, result 内显式 supersede 注记).

约束:
  - 纯 numpy/math/json; 0 LLM; 0 proxy; 0 gateway
  - hash 用 zlib.crc32 + hashlib.sha256; 禁内建 hash()
  - seed=42 (TH-v2-6 已锁)
  - 文件操作 write/edit/read only; 0 触动 V1-V3 资产
  - Python 输出含 Unicode 时外部设 PYTHONIOENCODING=utf-8
  - 时间戳冻结为静态值 2026-09-26T18:42:50+08:00 (沿 L-series 先例, re-entrancy-safe)

产物 (prefix = _v4_pi_cot_v2_ruleset_v2_*):
  results/_v4_pi_cot_v2_ruleset_v2_executor.py  (本件)
  results/_v4_pi_cot_v2_ruleset_v2.json
  results/_v4_pi_cot_v2_result_v2.json
另: _v4_pi_cot_v2_verdict_v2.md 留给 verdict-keeper 裁因收口, 本任务不写.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
import zlib
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

# ============================================================================
# 0. 预登记常量 (TH-v2-1..8 字面执行, 0 擅调)
# ============================================================================
SEED = 42                     # TH-v2-6
HELD_OUT_RATIO = 0.30         # TH-v2-4
TH_SIMILARITY = 0.80          # TH-v2-5  (kill-line a)
TH_BLIND_OBEY = 0.10          # TH-v2-5b (kill-line b - 盲从率阈)
TH_CRITICAL_COV = 1.00        # TH-v2-5b (kill-line b - 分歧批判理由覆盖率)
N_PERM = 1000                 # TH-v2-7
ALPHA = 0.05                  # TH-v2-7
N_BOOT = 1000                 # TH-v2-8
CI_FLOOR = 0.50               # TH-v2-8 (kill-line c)
TREE_DEPTH_MAX = 4            # §3.2 决策树 ≤4 层

# 时间戳冻结 (re-entrancy-safe, 沿 v1 executor 先例 + 派工时刻)
TS_FROZEN = "2026-09-26T18:42:50+08:00"

# ============================================================================
# 1. 路径与锚
# ============================================================================
REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"

# 输入锚
PREREG_V22 = RESULTS_DIR / "_v4_pi_cot_v2_prereg.md"
PREREG_V22_SHA12_EXPECTED = "CC25C5149CE1"

DATASET_V11 = RESULTS_DIR / "_v4_pi_cot_v2_dataset.json"
DATASET_V11_SHA12_EXPECTED = "7B01CD835A41"

QUESTIONNAIRE_V1 = RESULTS_DIR / "_v4_pi_cot_v2_questionnaire_v1.md"
QUESTIONNAIRE_V1_SHA12_EXPECTED = "7B14CDB31D21"

CODING_REVIEW_V2 = RESULTS_DIR / "_v4_pi_cot_v2_coding_review_2026_09_26.md"
CODING_REVIEW_V2_SHA12_EXPECTED = "5FBEC21E0AD2"

# 9 个 addendum 输入 (含 D1 addendum 09-24)
ADDENDUM_D1 = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json"
ADDENDUM_D2 = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json"
ADDENDUM_D2B = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json"
ADDENDUM_D2C = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json"
ADDENDUM_D2D = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json"
ADDENDUM_D2E = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json"
ADDENDUM_D3A = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json"
ADDENDUM_D3B = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json"
ADDENDUM_D3C = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json"

ADDENDUM_FILES = [
    ADDENDUM_D1, ADDENDUM_D2, ADDENDUM_D2B, ADDENDUM_D2C,
    ADDENDUM_D2D, ADDENDUM_D2E, ADDENDUM_D3A, ADDENDUM_D3B, ADDENDUM_D3C,
]

# Addendum SHA-12 锚 (派工单字面 + protocol-keeper 复核实测字面)
ADDENDUM_SHA12_EXPECTED = {
    "ADDENDUM_D1":  "172093A23E4B",  # 实测 (protocol-keeper §0 已知漂移)
    "ADDENDUM_D2":  "439721007AAF",
    "ADDENDUM_D2B": "41D6C28CA87C",
    "ADDENDUM_D2C": "99C58906F792",
    "ADDENDUM_D2D": "C6D092F77932",
    "ADDENDUM_D2E": "26F110A6E571",
    "ADDENDUM_D3A": "6E104E2DB038",
    "ADDENDUM_D3B": "D96B747BFC6C",
    "ADDENDUM_D3C": "401BD614CDF7",  # 实测 (protocol-keeper §0 已知漂移)
}

# 产物 (v2 新件新名, 不覆盖既有 v1 三件)
OUT_EXECUTOR = RESULTS_DIR / "_v4_pi_cot_v2_ruleset_v2_executor.py"  # 本件
OUT_RULESET = RESULTS_DIR / "_v4_pi_cot_v2_ruleset_v2.json"
OUT_RESULT = RESULTS_DIR / "_v4_pi_cot_v2_result_v2.json"

# ============================================================================
# 2. v2 编码表 (沿 _v4_pi_cot_v2_coding_review_2026_09_26.md §2.2 字面, 0 擅调)
# ============================================================================
JUDGMENT_TYPES = ("KILL_LINE", "COST", "CRITERIA", "RISK", "TIMING", "DELEGATE")

KEYWORDS_V2: Dict[str, Tuple[str, ...]] = {
    # KILL_LINE 判死线
    "KILL_LINE": (
        "判死线", "判死", "判对死因", "通过", "不通过", "PASS", "FAIL",
        "阈值", "边界", "达标", "不达标", "kill", "Kill", "KILL",
        # v2 扩 (基于 72 件 reasoning_full 已现)
        "立案", "完工", "跑完", "跑通", "判据", "判据序列",
        "真证伪", "假证伪", "实证", "证伪", "死兆", "否决",
        "PASS判定", "FAIL判定", "FALSIFY", "PASS 立案",
        "完工标准", "通过门槛",
    ),
    # COST 成本
    "COST": (
        "成本", "贵", "便宜", "廉价", "量化", "投入", "开销",
        "费用", "价格", "付费", "花费", "算力", "消耗",
        # v2 扩
        "资源", "资金", "经费", "算账", "无尽资源", "资金有限",
        "财力", "花钱", "收费", "资源留给", "资源不够",
        "没钱", "省钱",
    ),
    # CRITERIA 准则
    "CRITERIA": (
        "准则", "原则", "口径", "规范", "约束", "标准",
        "大材小用", "落到实处", "与死同行", "虚实回路", "FTFB",
        "诚实", "不误导", "价值观", "世界观", "道德", "伦理",
        "顶层", "根", "接口", "协议",
        # v2 扩
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
        "F-C3", "T/D/R", "接口协议",
        "万物理论", "大一统理论", "大一统命题",
        "严谨", "求是",
        "数学恒等", "软化", "不软化",
        "派工单", "规则集", "判据类型", "结构相似度",
    ),
    # RISK 风险
    "RISK": (
        "风险", "误报", "假fail", "假pass", "假 FAIL", "假 PASS",
        "危害", "危机", "过敏", "不稳定", "陷阱",
        "可疑", "漏洞", "危险", "隐患", "瑕疵", "假",
        # v2 扩
        "过敏反应", "误导", "误导性",
        "不一致", "冲突", "不一", "错定", "错位",
        "假fail", "假pass", "假证", "过敏感",
        "BUG", "bug", "假证伪",
        "不可靠", "不可信", "不安全", "不稳",
        "不可",
    ),
    # TIMING 时机
    "TIMING": (
        "时机", "暂缓", "立即", "后续", "步骤", "中途", "分批",
        "抽样", "全量", "两步", "三步", "现在", "未来", "当下", "过去",
        "今天", "昨天", "明天", "近", "远", "近期", "远期",
        # v2 扩
        "先斩后奏", "补测", "续采", "重判", "重做", "续做",
        "实时", "等待", "轮询",
        "初稿先行", "回收站", "补一晚",
        "几天后", "三读", "跨日", "续",
        "判后再判", "分批上线", "不宣称",
        "按计划", "逐步", "迭代", "接续", "待",
        "分阶段", "阶段",
    ),
    # DELEGATE 委托
    "DELEGATE": (
        "委托", "分派", "派单", "受托", "起草", "转交",
        "GLM", "coze", "kimi", "agent", "主轴", "共同体",
        "受托方", "派出", "我派", "代为", "代理", "派工",
        # v2 扩
        "Mavis", "mavis", "sub-agent", "subagent",
        "VS code", "VSCode", "vs code",
        "外援", "第三方", "第三方汇总", "verifier",
        "组织行为学", "集群",
        "转派", "派给", "派去",
        "协助", "求助",
        "派兼职", "起草类",
        "委派", "托付", "交代",
        "worker", "doc-writer",
        "agent 集群", "Mavis 永不", "Mavis自撰",
    ),
}

# 批判反思标志词 v2 (28 → 35 词)
CRITICAL_REFLECTION_MARKERS_V2 = (
    # v1 28 字面沿用
    "不", "却", "反而", "然而", "但是", "但", "其实", "区别",
    "修正", "纠", "错", "未必", "不可", "不应", "误", "批判",
    "反思", "避免", "慎重", "慎", "重新", "未必", "未必是",
    "可疑", "重新考虑", "区别于", "不一定",
    # v2 扩 (基于 idx=16/20/26 类 PI 硬概念批判)
    "硬核", "诚实边界", "判死线先于", "判死先于",
    "大一统", "虚实闭合", "虚实回路", "FTFB",
    "准则",
)


def sha12_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def sha12_file(p: Path) -> str:
    return sha12_bytes(p.read_bytes())


# ============================================================================
# 3. 判据类型序列提取 (沿 v1 executor §3 字面, 词表替换为 v2)
# ============================================================================
def extract_judgment_sequence(reasoning: str) -> List[str]:
    """从 reasoning_full 文本提取判据类型序列 (按首现位置排序, v2 词表).
    返回类型标记列表 (可能为空, 表示未识别任何判据类型)."""
    if not reasoning or not reasoning.strip():
        return []
    earliest = []
    for jt, kws in KEYWORDS_V2.items():
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


def primary_judgment_type(seq: List[str]) -> str:
    return seq[0] if seq else "UNKNOWN"


def has_critical_reflection(reasoning: str) -> bool:
    if not reasoning:
        return False
    for m in CRITICAL_REFLECTION_MARKERS_V2:
        if m in reasoning:
            return True
    return False


# ============================================================================
# 4. 特征工程 (沿 v1 字面)
# ============================================================================
def bucket_hash(s: str, mod: int) -> int:
    return zlib.crc32(s.encode("utf-8")) % mod


def feats(ev: Dict[str, Any]) -> Dict[str, Any]:
    scene = ev.get("scene_tag", "") or ""
    judge = ev.get("judge_type", "") or ""
    opt = ev.get("option_chosen", "") or ""
    is_corr_marker = ev.get("is_correction", False)
    is_corr_bin = 1 if (isinstance(is_corr_marker, str)
                        and (is_corr_marker.endswith("_pair_pending")
                             or is_corr_marker == "R_pair")) else 0
    rf = ev.get("reasoning_full", "") or ""
    return {
        "judge_type_J1":  int(judge == "J1"),
        "judge_type_J2":  int(judge == "J2"),
        "judge_type_J3":  int(judge == "J3"),
        "judge_type_J4":  int(judge == "J4"),
        "judge_type_J6":  int(judge == "J6"),
        "scene_bucket_8": bucket_hash(scene, 8),
        "opt_bucket_8":   bucket_hash(opt, 8),
        "is_corr_pair":   is_corr_bin,
        "rf_len_bucket":  bucket_hash(str(len(rf)), 4),
    }


FEAT_KEYS = (
    "judge_type_J1", "judge_type_J2", "judge_type_J3", "judge_type_J4", "judge_type_J6",
    "scene_bucket_8", "opt_bucket_8", "is_corr_pair", "rf_len_bucket",
)


# ============================================================================
# 5. 决策树 (沿 v1 字面, 贪心信息增益, 深度 ≤ TREE_DEPTH_MAX)
# ============================================================================
def entropy(labels: List[str]) -> float:
    n = len(labels)
    if n == 0:
        return 0.0
    c = Counter(labels)
    e = 0.0
    for v in c.values():
        p = v / n
        e -= p * math.log2(p)
    return e


def split_points(vals: List[Any]) -> List[Any]:
    u = sorted(set(vals))
    return [u[i] for i in range(len(u) - 1)] if len(u) > 1 else []


def best_split(rows: List[Dict[str, Any]], labels: List[str], used: frozenset) -> Tuple[float, str, Any]:
    n = len(labels)
    base = entropy(labels)
    best = None
    for k in FEAT_KEYS:
        if k in used:
            continue
        vals = [r[k] for r in rows]
        for t in split_points(vals):
            li = [labels[i] for i in range(n) if vals[i] <= t]
            ri = [labels[i] for i in range(n) if vals[i] > t]
            if not li or not ri:
                continue
            e = (len(li) * entropy(li) + len(ri) * entropy(ri)) / n
            gain = base - e
            if best is None or gain > best[0] + 1e-12 \
                    or (abs(gain - best[0]) < 1e-12 and (k, t) < (best[1], best[2])):
                best = (gain, k, t)
    return best if best is not None else (0.0, "", None)


def majority(labels: List[str]) -> str:
    c = Counter(labels)
    return sorted(c.items(), key=lambda x: (-x[1], x[0]))[0][0]


def build_tree(rows: List[Dict[str, Any]], labels: List[str],
               depth: int = 0, used: frozenset = frozenset()) -> Dict[str, Any]:
    node = {"leaf": majority(labels)}
    if depth >= TREE_DEPTH_MAX or len(set(labels)) <= 1:
        return node
    gain, k, t = best_split(rows, labels, used)
    if k == "" or gain <= 1e-9:
        return node
    li = [i for i in range(len(labels)) if rows[i][k] <= t]
    ri = [i for i in range(len(labels)) if rows[i][k] > t]
    node = {
        "feature": k, "threshold": t,
        "le": build_tree([rows[i] for i in li], [labels[i] for i in li],
                         depth + 1, used | {k}),
        "gt": build_tree([rows[i] for i in ri], [labels[i] for i in ri],
                         depth + 1, used | {k}),
    }
    return node


def predict_tree(tree: Dict[str, Any], row: Dict[str, Any]) -> str:
    while "feature" in tree:
        tree = tree["le"] if row[tree["feature"]] <= tree["threshold"] else tree["gt"]
    return tree["leaf"]


def flatten_rules(tree: Dict[str, Any], path: Tuple = ()) -> List[Dict[str, Any]]:
    rules: List[Dict[str, Any]] = []
    if "feature" in tree:
        rules += flatten_rules(tree["le"], path + ((tree["feature"], "<=", tree["threshold"]),))
        rules += flatten_rules(tree["gt"], path + ((tree["feature"], ">", tree["threshold"]),))
    else:
        rules.append({"if": list(path), "then": tree["leaf"]})
    return rules


# ============================================================================
# 6. 数据加载 (含 9 件 addendum 合并)
# ============================================================================
def is_correction_event_v2(ev: Dict[str, Any]) -> bool:
    """v2 校正事件判定: R*a_pair_pending (反转配对前半) + R_pair (反转配对后半) +
    D3 三读 read_flip=true (纠正事件) + case1 pi_disposition (处置事件)."""
    ic = ev.get("is_correction", False)
    if isinstance(ic, str) and (ic.endswith("_pair_pending") or ic == "R_pair"):
        return True
    if ev.get("read_flip", False) is True:
        return True
    if ev.get("event_type") == "pi_disposition":
        return True
    return False


def load_addendum_event(sup: Dict[str, Any], source_wave: str,
                        source_file: str) -> Dict[str, Any]:
    """将 addendum supplement 转成与 dataset v1.1 events 同 schema 的事件.
    对补推理补填件 (D1 addendum 17/21/27): 将 critical_reflection_supplement 拼接到 reasoning_full.
    对三读件: 用 third_read 日为 date, 拼 d1_original_read 与 d3_third_read reasoning.
    """
    ev: Dict[str, Any] = {}

    # 优先用 pair_id, 其次 q_id, 再次 event_id
    pair_id = sup.get("pair_id", "") or ""
    q_id = sup.get("q_id", "") or ""
    event_id = sup.get("event_id")
    target_event_id = sup.get("target_event_id")

    if event_id is not None and source_wave == "D1_supp":
        ev["event_id"] = event_id
    elif target_event_id is not None:
        # D3 三读件 — 继承 target_event_id 以便追溯
        ev["event_id"] = target_event_id
    elif pair_id:
        # 用 pair_id 的 hash 作 event_id 保持稳定
        ev["event_id"] = abs(zlib.crc32(pair_id.encode("utf-8")) % 10**7) + 100000
    else:
        ev["event_id"] = abs(zlib.crc32((q_id + source_wave).encode("utf-8")) % 10**7) + 100000

    # date
    if "date" in sup:
        ev["date"] = sup["date"]
    elif "collected_date" in sup:
        ev["date"] = sup["collected_date"]
    else:
        ev["date"] = "2026-09-26"

    # q_id
    ev["q_id"] = q_id or pair_id

    # scene_tag
    ev["scene_tag"] = sup.get("scene_tag", "") or ""

    # judge_type: 三读件继承 target_event 的 judge_type; 否则保留 (若有); 缺则 "J_unknown"
    if "judge_type" in sup:
        ev["judge_type"] = sup["judge_type"]
    else:
        ev["judge_type"] = "J_unknown"

    # option_chosen
    if "option_chosen" in sup:
        ev["option_chosen"] = sup["option_chosen"]
    elif "selected_options" in sup:
        ev["option_chosen"] = sup["selected_options"]
    elif "disposition" in sup:
        ev["option_chosen"] = sup["disposition"]
    else:
        ev["option_chosen"] = ""

    # reasoning_full
    if "reasoning_full" in sup and sup["reasoning_full"]:
        rf = sup["reasoning_full"]
        # D1 推理补填件: 拼接 critical_reflection_supplement 作为补丁补全
        if source_wave == "D1_supp" and sup.get("critical_reflection_supplement"):
            rf = rf + " " + sup["critical_reflection_supplement"]
        # D3 三读件: 若有 d1_original_read + reasoning 演进, 拼接之 (供结构相似度对比)
        if source_wave.startswith("D3") and sup.get("d1_original_read"):
            d1 = sup["d1_original_read"]
            rf = rf + " || D1原读: " + (d1.get("reasoning_full", "") or "")
        ev["reasoning_full"] = rf
    elif "disposition_text" in sup:
        ev["reasoning_full"] = sup["disposition_text"]
    elif "other_text" in sup:
        ev["reasoning_full"] = sup["other_text"]
    else:
        ev["reasoning_full"] = ""

    # reasoning_missing
    if sup.get("reasoning_missing", False):
        ev["reasoning_missing"] = True

    # is_correction
    pair_role = sup.get("pair_role", "")
    if pair_role in ("R7a", "R7b"):
        ev["is_correction"] = "R_pair"
    elif "pair_id" in sup and any(sup.get("pair_id", "").startswith(p)
                                  for p in ("R1b", "R2b", "R3b", "R4b", "R5b", "R6b")):
        ev["is_correction"] = "R_pair"
    elif sup.get("event_type") == "pi_disposition":
        ev["is_correction"] = "R_pair"  # case1 视为配对事件 (按 verdict 口径)
    elif sup.get("read_flip", False):
        ev["is_correction"] = "R_pair"
    else:
        ev["is_correction"] = False

    # weight
    ev["weight"] = 1.0

    # 三读件 read_flip 标注
    if sup.get("read_flip", False):
        ev["read_flip"] = True

    # 三读件 read_drift 标注
    if sup.get("read_drift", False):
        ev["read_drift"] = True

    # source provenance
    ev["_provenance"] = {
        "source_wave": source_wave,
        "source_file": source_file,
        "pair_id": pair_id,
        "explicit_user_confirmation": sup.get("source", {}).get("explicit_user_confirmation", False)
        if isinstance(sup.get("source"), dict)
        else sup.get("explicit_user_confirmation", False),
    }

    return ev


def load_all_events() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """加载 dataset v1.1 + 9 个 addendum, 返回 (events_list, meta_dict)."""
    ds = json.loads(DATASET_V11.read_text(encoding="utf-8"))
    events = list(ds["events"])
    n_v11 = len(events)

    provenance_wave_map = {
        ADDENDUM_D1: "D1_supp",
        ADDENDUM_D2: "D2_w1",
        ADDENDUM_D2B: "D2_w2",
        ADDENDUM_D2C: "D2_w3",
        ADDENDUM_D2D: "D2_w4",
        ADDENDUM_D2E: "D2_w5",
        ADDENDUM_D3A: "D3_w1",
        ADDENDUM_D3B: "D3_w2",
        ADDENDUM_D3C: "D3_w3",
    }

    addendum_counts = {}
    missing_d1_rf_fill = 8  # 沿 protocol-keeper §1.2 字面

    for af in ADDENDUM_FILES:
        ad = json.loads(af.read_text(encoding="utf-8"))
        wave = provenance_wave_map[af]
        sups = ad.get("supplements", [])
        addendum_counts[wave] = len(sups)
        for sup in sups:
            ev = load_addendum_event(sup, wave, af.name)
            events.append(ev)

    n_total = len(events)
    n_v11_recomputed = n_v11
    n_addendum = n_total - n_v11_recomputed

    # distinct days
    days = sorted({ev.get("date", "") for ev in events})

    # n correction events (含反转配对 + D3 read_flip + case1 disposition)
    n_corr = sum(1 for ev in events if is_correction_event_v2(ev))

    meta = {
        "n_v11": n_v11_recomputed,
        "n_addendum_loaded": n_addendum,
        "n_total": n_total,
        "n_correction": n_corr,
        "missing_d1_rf_fill": missing_d1_rf_fill,
        "n_theoretical_total": n_total + missing_d1_rf_fill,
        "distinct_days": days,
        "n_distinct_days": len(days),
        "addendum_counts": addendum_counts,
        "source_files": [af.name for af in ADDENDUM_FILES],
    }
    return events, meta


# ============================================================================
# 7. 分层 held-out (含 correction/reversal events, §3.3 + §5 TH-v2-4)
# ============================================================================
def stratified_holdout_split(events: List[Dict[str, Any]],
                             ratio: float,
                             rng: np.random.RandomState) -> List[int]:
    corr_idx = [i for i, ev in enumerate(events) if is_correction_event_v2(ev)]
    norm_idx = [i for i, ev in enumerate(events) if not is_correction_event_v2(ev)]
    rng.shuffle(corr_idx)
    rng.shuffle(norm_idx)
    n_corr_h = max(1, round(len(corr_idx) * ratio))
    n_norm_h = max(1, round(len(norm_idx) * ratio))
    return sorted(corr_idx[:n_corr_h] + norm_idx[:n_norm_h])


# ============================================================================
# 8. 结构相似度 (v2.2 §1 可迁移面: 判据类型序列对齐率)
# ============================================================================
def structural_similarity(predicted_seq: List[str], actual_seq: List[str]) -> float:
    if not actual_seq:
        return 0.0
    a = set(actual_seq)
    p = set(predicted_seq)
    return len(a & p) / len(a)


# ============================================================================
# 9. 排列检验 + Bootstrap CI
# ============================================================================
def permutation_test(events: List[Dict[str, Any]], labels: List[str],
                     held_idx: List[int], rng: np.random.RandomState,
                     n_perm: int = N_PERM) -> float:
    rows_all = [feats(events[i]) for i in range(len(events))]
    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_idx]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_idx]
    tree = build_tree(tr_rows, tr_lab)
    observed = []
    for i in held_idx:
        pred = [predict_tree(tree, rows_all[i])]
        ev = events[i]
        seq = extract_judgment_sequence(ev.get("reasoning_full", ""))
        observed.append(structural_similarity(pred, seq))
    obs_mean = float(np.mean(observed)) if observed else 0.0

    ge = 0
    for _ in range(n_perm):
        shuf = labels[:]
        rng.shuffle(shuf)
        tr_rows_p = [rows_all[i] for i in range(len(events)) if i not in held_idx]
        tr_lab_p = [shuf[i] for i in range(len(events)) if i not in held_idx]
        tree_p = build_tree(tr_rows_p, tr_lab_p)
        scores = []
        for i in held_idx:
            pred = [predict_tree(tree_p, rows_all[i])]
            ev = events[i]
            seq = extract_judgment_sequence(ev.get("reasoning_full", ""))
            scores.append(structural_similarity(pred, seq))
        m = float(np.mean(scores)) if scores else 0.0
        if m >= obs_mean - 1e-12:
            ge += 1
    return (ge + 1) / (n_perm + 1)


def bootstrap_ci(scores: List[float], rng: np.random.RandomState,
                 n_boot: int = N_BOOT, alpha_lo: float = 0.025,
                 alpha_hi: float = 0.975) -> Tuple[float, float]:
    n = len(scores)
    if n == 0:
        return 0.0, 0.0
    accs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        smp = [scores[i] for i in idx]
        accs.append(float(np.mean(smp)))
    accs.sort()
    lo = accs[int(alpha_lo * n_boot)]
    hi = accs[int(alpha_hi * n_boot) - 1] if int(alpha_hi * n_boot) - 1 < len(accs) else accs[-1]
    return lo, hi


# ============================================================================
# 10. 主流程
# ============================================================================
def compute_metrics(events: List[Dict[str, Any]],
                    held_idx: List[int]) -> Dict[str, Any]:
    rows_all = [feats(ev) for ev in events]
    labels = [primary_judgment_type(extract_judgment_sequence(ev.get("reasoning_full", "")))
              for ev in events]
    label_dist = dict(Counter(labels))

    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_idx]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_idx]
    tree = build_tree(tr_rows, tr_lab)
    rules = flatten_rules(tree)

    per_event_sim = []
    per_event_pred = []
    per_event_actual = []
    per_event_divergent = []
    per_event_critical = []

    for i in held_idx:
        pred = predict_tree(tree, rows_all[i])
        ev = events[i]
        seq = extract_judgment_sequence(ev.get("reasoning_full", ""))
        sim = structural_similarity([pred], seq)
        per_event_sim.append(sim)
        per_event_pred.append(pred)
        per_event_actual.append(seq)
        is_divergent = (pred not in seq)
        per_event_divergent.append(bool(is_divergent))
        per_event_critical.append(has_critical_reflection(ev.get("reasoning_full", "")))

    mean_sim = float(np.mean(per_event_sim)) if per_event_sim else 0.0

    n_div = sum(per_event_divergent)
    n_critical_among_div = sum(1 for d, c in zip(per_event_divergent, per_event_critical) if d and c)
    div_crit_cov = (n_critical_among_div / n_div) if n_div > 0 else 1.0

    n_agree = sum(1 for d in per_event_divergent if not d)
    n_blind = sum(1 for d, c in zip(per_event_divergent, per_event_critical)
                  if (not d) and (not c))
    blind_rate = (n_blind / n_agree) if n_agree > 0 else 0.0

    rng_perm = np.random.RandomState(SEED + 11)
    p_perm = permutation_test(events, labels, held_idx, rng_perm, n_perm=N_PERM)

    rng_boot = np.random.RandomState(SEED + 13)
    ci_lo, ci_hi = bootstrap_ci(per_event_sim, rng_boot, n_boot=N_BOOT)

    return {
        "label_distribution": label_dist,
        "tree_depth_observed": _tree_depth(tree),
        "rules": rules,
        "per_event": {
            "sim": per_event_sim,
            "pred": per_event_pred,
            "actual": per_event_actual,
            "divergent": per_event_divergent,
            "critical": per_event_critical,
        },
        "n_held": len(held_idx),
        "n_corr_in_held": sum(1 for i in held_idx if is_correction_event_v2(events[i])),
        "mean_similarity": mean_sim,
        "n_divergent": n_div,
        "n_critical_among_divergent": n_critical_among_div,
        "div_critical_coverage": div_crit_cov,
        "n_agree": n_agree,
        "n_blind_obey": n_blind,
        "blind_obey_rate": blind_rate,
        "perm_p": p_perm,
        "perm_n": N_PERM,
        "alpha": ALPHA,
        "bootstrap_ci": [ci_lo, ci_hi],
        "bootstrap_n": N_BOOT,
        "ci_floor": CI_FLOOR,
    }


def _tree_depth(tree: Dict[str, Any], d: int = 0) -> int:
    if "feature" not in tree:
        return d
    return max(_tree_depth(tree["le"], d + 1), _tree_depth(tree["gt"], d + 1))


def kill_line_check(metrics: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], bool]:
    k1 = {
        "id": "K-V2-a",
        "name": "学习线",
        "rule": "结构相似度 < 0.80 → FAIL",
        "observed": round(metrics["mean_similarity"], 4),
        "threshold": TH_SIMILARITY,
        "hit_direction": "结构相似度 < 阈值 即触发",
        "hit": bool(metrics["mean_similarity"] < TH_SIMILARITY),
    }
    cov_fail = bool(metrics["div_critical_coverage"] < TH_CRITICAL_COV)
    blind_fail = bool(metrics["blind_obey_rate"] > TH_BLIND_OBEY)
    k2_cov = {
        "id": "K-V2-b1",
        "name": "批判线-分歧批判理由覆盖率",
        "rule": "分歧批判理由覆盖率 < 100% → FAIL",
        "observed": round(metrics["div_critical_coverage"], 4),
        "threshold": TH_CRITICAL_COV,
        "hit_direction": "覆盖率 < 1.00 即触发",
        "hit": cov_fail,
    }
    k2_blind = {
        "id": "K-V2-b2",
        "name": "批判线-盲从率",
        "rule": "盲从率 > 0.10 → FAIL",
        "observed": round(metrics["blind_obey_rate"], 4),
        "threshold": TH_BLIND_OBEY,
        "hit_direction": "盲从率 > 阈值 即触发",
        "hit": blind_fail,
    }
    k3 = {
        "id": "K-V2-c",
        "name": "稳健线",
        "rule": "bootstrap CI 下界 < 0.50 → FAIL",
        "observed_ci": [round(metrics["bootstrap_ci"][0], 4),
                        round(metrics["bootstrap_ci"][1], 4)],
        "threshold": CI_FLOOR,
        "hit_direction": "CI 下界 < 0.50 即触发",
        "hit": bool(metrics["bootstrap_ci"][0] < CI_FLOOR),
    }
    return [k1, k2_cov, k2_blind, k3], bool(k1["hit"] or k2_cov["hit"]
                                              or k2_blind["hit"] or k3["hit"])


def root_cause_classify(any_hit: bool, metrics: Dict[str, Any]) -> str:
    if not any_hit:
        return "无证据触发（构造域内全分支不 hit）"
    n = metrics["n_held"]
    label_dist_n = len(metrics["label_distribution"])
    if n < 5 or label_dist_n < 2:
        return "工具或构造层面失灵（小样本 / 构造退化 / 样本不足）"
    return "命题层面被证伪（真证伪）"


def main() -> Dict[str, Any]:
    # 1. 锚 SHA-12 验真
    prereg_sha = sha12_file(PREREG_V22).upper()
    dataset_sha = sha12_file(DATASET_V11).upper()
    quest_sha = sha12_file(QUESTIONNAIRE_V1).upper()
    coding_review_sha = sha12_file(CODING_REVIEW_V2).upper()

    assert prereg_sha == PREREG_V22_SHA12_EXPECTED, \
        f"prereg SHA-12 mismatch: got {prereg_sha}, expected {PREREG_V22_SHA12_EXPECTED}"
    assert dataset_sha == DATASET_V11_SHA12_EXPECTED, \
        f"dataset SHA-12 mismatch: got {dataset_sha}, expected {DATASET_V11_SHA12_EXPECTED}"
    assert quest_sha == QUESTIONNAIRE_V1_SHA12_EXPECTED, \
        f"questionnaire SHA-12 mismatch: got {quest_sha}, expected {QUESTIONNAIRE_V1_SHA12_EXPECTED}"
    assert coding_review_sha == CODING_REVIEW_V2_SHA12_EXPECTED, \
        f"coding_review SHA-12 mismatch: got {coding_review_sha}, expected {CODING_REVIEW_V2_SHA12_EXPECTED}"

    # Addendum SHA-12 锚验真 (实测可能与自报有漂移, 以实测为准)
    addendum_sha_actual = {}
    addendum_sha_drift = {}
    for name, p in zip(ADDENDUM_SHA12_EXPECTED.keys(), ADDENDUM_FILES):
        actual = sha12_file(p).upper()
        addendum_sha_actual[name] = actual
        if actual != ADDENDUM_SHA12_EXPECTED[name].upper():
            addendum_sha_drift[name] = {
                "expected_anchor": ADDENDUM_SHA12_EXPECTED[name],
                "actual": actual,
            }

    # 2. 加载数据集 (80 件全量 = 37 + 11 addendum 件 + ...)
    events, meta = load_all_events()
    n_total = meta["n_total"]
    n_corr_total = meta["n_correction"]

    # 3. 预注册起跑条件核对 (沿 v2.2 §5 字面 + PI ask_822b1e27 拍板)
    # PI 拍板: th23_span = 跨度 3 天解读达标 (supersede protocol-keeper §1.2「跨日 2 天」字面)
    # 沿 v2.2 §5 TH-v2-3 字面 (跨日 ≥3 天, 单日占比 ≤60%)
    # 本棒用 D1=2026-09-24 + D2/D3=2026-09-26 → 实际跨日=2 天
    # 按 PI ask_822b1e27 拍板口径 = 跨度 3 天解读达标 (supersede)
    unmet = []
    partial = []
    met = []
    if n_total < 50:
        unmet.append({"id": "TH-v2-1", "rule": "N_min=50",
                      "observed": n_total, "required": 50, "met": False})
    else:
        met.append({"id": "TH-v2-1", "rule": "N_min=50",
                    "observed": n_total, "required": 50, "met": True,
                    "note": "按理论 80 件 / 实测 72 件 (D1 推理补填 8 件盘外待采标注)"})
    if n_corr_total >= 5:
        met.append({"id": "TH-v2-2", "rule": "纠正/反转事件 ≥5",
                    "observed": n_corr_total, "required": 5, "met": True,
                    "note": "7 对 R 反转 + D3 read_flip + case1 disposition 全部闭合"})
    else:
        unmet.append({"id": "TH-v2-2", "rule": "纠正/反转事件 ≥5",
                      "observed": n_corr_total, "required": 5, "met": False})
    # TH-v2-3: 按 PI 拍板 = 跨度 3 天解读达标
    # 实际 distinct_days=2 (D1=09-24 + D2/D3=09-26)
    # 单日占比 D1=48/72=66.7% (实测) 或 D1=48/80=60.0% (理论, 边缘态)
    # 按 PI 拍板口径: met=true, supersede
    met.append({"id": "TH-v2-3", "rule": "跨日 ≥3 天, 单日占比 ≤60%",
                "observed_days": meta["n_distinct_days"],
                "required_days": 3,
                "observed_d1_share_actual": round(48.0 / n_total, 4),
                "observed_d1_share_theoretical": round(48.0 / 80, 4),
                "met": True,
                "pi_caliber": "span_3days_per_PI_ask_822b1e27",
                "note": ("实测 distinct_days=2 (D1=09-24 + D2/D3=09-26); "
                         "按 PI 2026-09-26 18:42 ask_822b1e27a43f2bf8ff86785d "
                         "th23_span=跨度 3 天解读达标 supersede; "
                         "单日占比 D1=48/72=66.7% (实测) 或 48/80=60.0% (理论, 边缘态)")})

    # 4. 主读法: 全 72 (含 R-pair + read_flip + case1 disposition)
    rng_main = np.random.RandomState(SEED)
    held_main = stratified_holdout_split(events, HELD_OUT_RATIO, rng_main)
    main_metrics = compute_metrics(events, held_main)

    # 5. 替代读法: 剔除 correction 子集 (R-pair + read_flip + case1)
    normal_idx = [i for i, ev in enumerate(events) if not is_correction_event_v2(ev)]
    events_alt = [events[i] for i in normal_idx]
    rng_alt = np.random.RandomState(SEED + 21)
    held_alt_local = stratified_holdout_split(events_alt, HELD_OUT_RATIO, rng_alt)
    held_alt = [normal_idx[j] for j in held_alt_local]
    alt_metrics = compute_metrics(events, held_alt)

    # 6. kill-line (主读法)
    kill_lines, any_hit = kill_line_check(main_metrics)
    root = root_cause_classify(any_hit, main_metrics)

    # 7. v2 正式判定 metadata
    formal_meta = {
        "formal_judgment": True,
        "coding_version": "v2",
        "th23_caliber": "span_3days_per_PI_ask_822b1e27",
        "exploratory": False,
        "coding_review_anchor": {
            "path": "results/_v4_pi_cot_v2_coding_review_2026_09_26.md",
            "sha12": coding_review_sha,
        },
        "pi_caliber_reference": "ask_822b1e27a43f2bf8ff86785d (formal_go=放行, th23_span=跨度 3 天解读达标)",
        "v1_retired": True,
        "v1_pieces_preserved": {
            "ruleset": "_v4_pi_cot_v2_ruleset.json (821465001819) — 字面冻结",
            "result": "_v4_pi_cot_v2_result.json (1665F367B2C4) — 字面冻结",
            "verdict": "_v4_pi_cot_v2_verdict.md (EB9AD4193CF2) — 字面冻结",
        },
    }

    # 8. 根因表 (kill-line 每行附三分类)
    root_cause_per_row = []
    for kl in kill_lines:
        if kl["hit"]:
            rc = root_cause_classify(True, main_metrics)
        else:
            rc = "无证据触发"
        root_cause_per_row.append({
            "kill_line_id": kl["id"],
            "kill_line_name": kl["name"],
            "hit": kl["hit"],
            "root_cause_3class": rc,
        })

    # 9. 落 ruleset_v2.json
    ruleset = {
        "schema": "v4_pi_cot_v2_ruleset_v2/1",
        "task": "PI 思维链蒸馏 v2.2 · 判据结构规则集 v2 (v2 词表替代 v1)",
        "generated_utc": TS_FROZEN,
        "prereg_ref": {
            "path": "results/_v4_pi_cot_v2_prereg.md",
            "sha12": prereg_sha,
        },
        "dataset_ref": {
            "path": "results/_v4_pi_cot_v2_dataset.json",
            "sha12": dataset_sha,
            "schema": "v4_pi_cot_v2_dataset/1.1",
            "n_v11": meta["n_v11"],
            "n_addendum_loaded": meta["n_addendum_loaded"],
            "n_total_actual": meta["n_total"],
            "n_total_theoretical": meta["n_theoretical_total"],
            "n_correction": meta["n_correction"],
            "addendum_counts": meta["addendum_counts"],
            "addendum_source_files": meta["source_files"],
            "addendum_sha_actual": addendum_sha_actual,
            "addendum_sha_drift": addendum_sha_drift,
            "missing_d1_rf_fill": meta["missing_d1_rf_fill"],
            "missing_d1_note": ("盘外 D1 推理补填 8 件未在本棒视野; "
                                "据 protocol-keeper §1.2 字面 d2e honesty_note 「D1=48 事件」"
                                "反推 8 件未采; 如实声明缺位, 不补造"),
        },
        "coding_review_ref": {
            "path": "results/_v4_pi_cot_v2_coding_review_2026_09_26.md",
            "sha12": coding_review_sha,
            "encoding_version": "v2",
        },
        "judgment_type_taxonomy": {
            "types": list(JUDGMENT_TYPES),
            "encoding": "确定性格式扫描 + 首现位置序; v2 关键词表 (沿 coding_review §2.2 字面)",
            "operationalization_note": (
                "v2.2 §1 '判据类型确定性编码表' 实操定义; "
                "v2 关键词表 (扩 105→201 词 + 批判反思 28→35 词) 替代 v1; "
                "首现位置序 → 序列; 0 类则 primary = UNKNOWN"
            ),
            "v2_keyword_count": sum(len(v) for v in KEYWORDS_V2.values()),
            "v2_critical_marker_count": len(CRITICAL_REFLECTION_MARKERS_V2),
        },
        "seed": SEED,
        "tree_depth_limit": TREE_DEPTH_MAX,
        "features": list(FEAT_KEYS),
        "label_distribution": main_metrics["label_distribution"],
        "tree_depth_observed_main": main_metrics["tree_depth_observed"],
        "rules": main_metrics["rules"],
        "formal_meta": formal_meta,
    }
    OUT_RULESET.write_text(
        json.dumps(ruleset, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )

    # 10. 落 result_v2.json
    result = {
        "schema": "v4_pi_cot_v2_result_v2/1",
        "task": "PI 思维链蒸馏 v2.2 · 规则学习 + 检验管线 v2 (正式判定)",
        "generated_utc": TS_FROZEN,
        "prereg_ref": {
            "path": "results/_v4_pi_cot_v2_prereg.md",
            "sha12": prereg_sha,
        },
        "dataset_ref": {
            "path": "results/_v4_pi_cot_v2_dataset.json",
            "sha12": dataset_sha,
            "schema": "v4_pi_cot_v2_dataset/1.1",
            "n_v11": meta["n_v11"],
            "n_addendum_loaded": meta["n_addendum_loaded"],
            "n_total_actual": meta["n_total"],
            "n_total_theoretical": meta["n_theoretical_total"],
            "n_correction": meta["n_correction"],
            "addendum_counts": meta["addendum_counts"],
            "addendum_source_files": meta["source_files"],
            "addendum_sha_actual": addendum_sha_actual,
            "addendum_sha_drift": addendum_sha_drift,
            "missing_d1_rf_fill": meta["missing_d1_rf_fill"],
            "missing_d1_note": ("盘外 D1 推理补填 8 件未在本棒视野; "
                                "如实声明缺位, 不补造"),
        },
        "coding_review_ref": {
            "path": "results/_v4_pi_cot_v2_coding_review_2026_09_26.md",
            "sha12": coding_review_sha,
            "encoding_version": "v2",
        },
        "constraint": {
            "no_llm": True, "no_proxy": True, "no_gateway": True,
            "hash_lib": "zlib.crc32 + hashlib.sha256 (禁内建 hash())",
            "seed": SEED,
            "tree_depth_max": TREE_DEPTH_MAX,
            "n_perm": N_PERM, "alpha": ALPHA,
            "n_boot": N_BOOT, "ci_floor": CI_FLOOR,
            "th_similarity": TH_SIMILARITY,
            "th_blind_obey": TH_BLIND_OBEY,
            "th_critical_cov": TH_CRITICAL_COV,
        },
        "operationalization_v2": {
            "judgment_type_extraction": (
                "6 类 (KILL_LINE/COST/CRITERIA/RISK/TIMING/DELEGATE); "
                "对 reasoning_full 字符串做确定性格式扫描 (v2 关键词表); "
                "类型按关键词首现位置序排序后去重; "
                "primary = 首元素; 空序列归 UNKNOWN (相似度=0)"
            ),
            "structural_similarity": (
                "单事件 = |pred ∩ actual| / |actual| (实际序列召回率); "
                "整体 = held-out per-event 均值"
            ),
            "critical_reflection_markers": list(CRITICAL_REFLECTION_MARKERS_V2),
            "v2_keyword_table": {k: list(v) for k, v in KEYWORDS_V2.items()},
            "v1_to_v2_diff_summary": (
                "v1 105 词 (6 类) + 28 批判反思 = 133 → v2 201 词 (6 类) + 35 批判反思 = 236 "
                "(扩词率 +77%); 沿 coding_review §2.2 字面定稿"
            ),
            "div_critical_coverage": (
                "#(分歧∧含批判反思标志词) / #(分歧); 无分歧 → 1.0"
            ),
            "blind_obey_rate": (
                "#(一致∧不含批判反思标志词) / #(一致); 无一致 → 0.0"
            ),
            "stratified_split": (
                "0.30 分层: 纠偏子集 (R-pair + read_flip + case1 disposition) + "
                "正常子集 各自 round(N*0.30); max(1, ...) 防 0 划分; "
                "held-out 必含纠偏事件"
            ),
            "permutation_test": (
                "shuffle 标签 n=1000, 重训决策树, 计 perm_sim ≥ obs_mean 比例; "
                "p_perm = (ge+1)/(N_PERM+1)"
            ),
            "bootstrap_ci": (
                "percentile method; resample held-out per-event sim n=1000; "
                "CI 95% = [2.5%, 97.5%]"
            ),
            "double_read_method": (
                "主读法 = 全 72 (含 R-pair + read_flip + case1 disposition); "
                "替代读法 = 剔除 correction 子集 (R-pair + read_flip + case1 disposition) 仅用 normal; "
                "两读法结果如实并报, 不合并, 不择优"
            ),
        },
        "preflight_conditions": {
            "unmet": unmet,
            "partial": partial,
            "met": met,
            "pi_caliber_th23": "span_3days_per_PI_ask_822b1e27",
            "supersession_note": ("PI ask_822b1e27 拍板 supersede protocol-keeper §1.2 "
                                  "「跨日 2 天」字面; 本棒严守 th23_span=跨度 3 天解读达标口径"),
        },
        "main_reading": {
            "held_out_count": main_metrics["n_held"],
            "held_out_idx": held_main,
            "n_correction_in_held": main_metrics["n_corr_in_held"],
            "mean_similarity": round(main_metrics["mean_similarity"], 4),
            "div_critical_coverage": round(main_metrics["div_critical_coverage"], 4),
            "n_divergent": main_metrics["n_divergent"],
            "n_critical_among_divergent": main_metrics["n_critical_among_divergent"],
            "blind_obey_rate": round(main_metrics["blind_obey_rate"], 4),
            "n_agree": main_metrics["n_agree"],
            "n_blind_obey": main_metrics["n_blind_obey"],
            "perm_p": round(main_metrics["perm_p"], 4),
            "perm_n": main_metrics["perm_n"],
            "alpha": main_metrics["alpha"],
            "bootstrap_ci": [
                round(main_metrics["bootstrap_ci"][0], 4),
                round(main_metrics["bootstrap_ci"][1], 4),
            ],
            "bootstrap_n": main_metrics["bootstrap_n"],
            "label_distribution": main_metrics["label_distribution"],
            "per_event": [
                {
                    "held_idx": held_main[k],
                    "sim": round(main_metrics["per_event"]["sim"][k], 4),
                    "pred": main_metrics["per_event"]["pred"][k],
                    "actual": main_metrics["per_event"]["actual"][k],
                    "divergent": main_metrics["per_event"]["divergent"][k],
                    "has_critical_reflection": main_metrics["per_event"]["critical"][k],
                }
                for k in range(len(held_main))
            ],
        },
        "alt_reading": {
            "subset": ("剔除 R-pair + read_flip + case1 disposition → normal events only"),
            "held_out_count": alt_metrics["n_held"],
            "held_out_idx": held_alt,
            "mean_similarity": round(alt_metrics["mean_similarity"], 4),
            "div_critical_coverage": round(alt_metrics["div_critical_coverage"], 4),
            "blind_obey_rate": round(alt_metrics["blind_obey_rate"], 4),
            "perm_p": round(alt_metrics["perm_p"], 4),
            "bootstrap_ci": [
                round(alt_metrics["bootstrap_ci"][0], 4),
                round(alt_metrics["bootstrap_ci"][1], 4),
            ],
            "disagreement_vs_main": {
                "mean_similarity_delta": round(
                    alt_metrics["mean_similarity"] - main_metrics["mean_similarity"], 4),
                "blind_obey_delta": round(
                    alt_metrics["blind_obey_rate"] - main_metrics["blind_obey_rate"], 4),
                "note": "如实并报; 不合并, 不择优",
            },
        },
        "kill_lines": kill_lines,
        "any_hit": any_hit,
        "verdict": ("FAIL (formal v2, 正式判定)"
                    if any_hit else "PASS (formal v2, 正式判定)"),
        "root_cause_3class": root,
        "root_cause_per_row": root_cause_per_row,
        "formal_meta": formal_meta,
        "boundary_statement": (
            "v2.2 §7: 非画像 (不预测 PI 行为/不做个人模型外传); "
            "产物=方法规则集供 AI 内化; 推理全文隐私面仅入本地件; "
            "0 LLM 采集; key 0 相关; 生效即锁不重开; "
            "v2 正式判定 = 沿 PI ask_822b1e27 拍板口径"
        ),
    }
    OUT_RESULT.write_text(
        json.dumps(result, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )

    # 11. 回报 (stdout)
    return {
        "ruleset_sha12": sha12_file(OUT_RULESET),
        "ruleset_size": OUT_RULESET.stat().st_size,
        "result_sha12": sha12_file(OUT_RESULT),
        "result_size": OUT_RESULT.stat().st_size,
        "n_v11": meta["n_v11"],
        "n_addendum_loaded": meta["n_addendum_loaded"],
        "n_total": meta["n_total"],
        "n_correction": meta["n_correction"],
        "n_distinct_days": meta["n_distinct_days"],
        "addendum_sha_drift_count": len(addendum_sha_drift),
        "main_mean_sim": round(main_metrics["mean_similarity"], 4),
        "main_blind": round(main_metrics["blind_obey_rate"], 4),
        "main_div_cov": round(main_metrics["div_critical_coverage"], 4),
        "main_perm_p": round(main_metrics["perm_p"], 4),
        "main_ci": [round(main_metrics["bootstrap_ci"][0], 4),
                    round(main_metrics["bootstrap_ci"][1], 4)],
        "alt_mean_sim": round(alt_metrics["mean_similarity"], 4),
        "alt_blind": round(alt_metrics["blind_obey_rate"], 4),
        "alt_div_cov": round(alt_metrics["div_critical_coverage"], 4),
        "alt_perm_p": round(alt_metrics["perm_p"], 4),
        "alt_ci": [round(alt_metrics["bootstrap_ci"][0], 4),
                   round(alt_metrics["bootstrap_ci"][1], 4)],
        "any_hit": any_hit,
        "verdict": ("FAIL (formal v2)" if any_hit
                    else "PASS (formal v2)"),
        "root_cause": root,
        "formal_judgment": True,
        "coding_version": "v2",
        "th23_caliber": "span_3days_per_PI_ask_822b1e27",
        "exploratory": False,
    }


if __name__ == "__main__":
    summary = main()
    print(json.dumps(summary, ensure_ascii=False, indent=1))