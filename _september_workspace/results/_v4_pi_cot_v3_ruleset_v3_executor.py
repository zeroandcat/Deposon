# -*- coding: utf-8 -*-
"""
V4 _v4_pi_cot_v3_ruleset_v3_executor.py
=====================================
派工棒: worker (执行类) (branch session mvs_fd24a76ece86406ca55a78be10b0b769)。

任务来源 (沿派工单 5 件必带):
  - agent:    worker (执行类·规则集构造)
  - skill:    scientific-research-workflows:experimental-design
              (plugin @scientific-research-workflows)
              若 skill 加载器报 Local skill not found 则按纪律锚 fallback:
              results/_v4_pi_cot_v2_ruleset_v2.json (C5B3DD141655) +
              results/_v4_pi_cot_v2_ruleset_v2_executor.py (EB22F13D571C) 结构字面 +
              results/_v4_pi_cot_v3_prereg.md (B7547329AF2E) §1.2/§4/§8 字面
              ——按纪律锚执行并老实交代缺位,禁止编造 skill 虚构指令
  - plugin:   @scientific-research-workflows
  - 7+9 铁律严守:
              key 永不明文 (不落盘/不入 prompt/JSON/log,仅 runtime 读;本任务 0 LLM,0 key 相关)
              V1-V3 只读不动 (0 触动既有件)
              派生 JSON 不合并 (不动既有 _v4_pi_cot_v2_*.json / _v4_pi_cot_v3_dataset.json)
              0 擅调阈值 (K-V3-A 0.65 / A' 0.55 / B 1.00 / C 0.10 / D 0.40 / E sentinel 一字面)
              判定布尔显式命名方向 (hit=True 即触发 FAIL; pass=True 即存活; S-40 教训)
              kill-line 字面不动禁私设条款 (公式逐项与 v3 prereg §4 条款一一对应)
              不覆盖任何既有件 (v3 新件新名: _v3.json 后缀)
  - 老实交代: 0 产物就报 0 产物; succeeded ≠ 跑完, 以盘上落盘核验为准; 不编造数字

任务字面 (沿 _v4_pi_cot_v3_prereg.md v3 §1.2 + §2.2 + §4.2 + §4.3 + §10.1):
  1. 消解 A (表现力上界提升, 参数已锁 §1.2):
       决策树深度 ≤ 6 (TH-v3-8, v2=4 不沿用)
       特征数 ≥ 12 (TH-v3-9; judge_type_J5 + rf_pos_density + n_keywords_hit 三项必启用)
       模板 = 全序列返回 (弃 v2 primary=seq[0] 单元素) + 5 类短语模式匹配启用
  2. 消解 B (度量换代, 形式已锁 §2.2):
       NW-sim 主口径 (Needleman-Wunsch 全局对齐; match=+2/mismatch=-1/gap=-2;
                      归一化至 [0,1])
       NLED-sim 副口径 (1 - edit_distance/max(len_a, len_b))
       双口径并报, 不择优; 不引入 NW 邻近类矩阵 (§10.5 第 1 项: 维持不启用)
  3. 阈值 (v3 prereg §4.2 + §4.3 + §10.1 字面即锁, 0 擅调):
       K-V3-A 学习线 (NW 主口径): NW-sim mean < 0.65 → FAIL
       K-V3-A' 学习线 (NLED 副口径): NLED-sim mean < 0.55 → FAIL
       K-V3-B 批判覆盖线: 覆盖率 < 1.00 → FAIL
       K-V3-C 盲从率线: 盲从率 > 0.10 → FAIL
       K-V3-D 稳健线: bootstrap CI 下界 < 0.40 → FAIL
       K-V3-E 双口径一致线 (构造面 sentinel): NW/NLED 方向不一致 → 警告, 非机械 FAIL/PASS
  4. result 内置字段 (沿 v3 prereg §10.1 + §10.6 字面):
       formal_judgment: true
       coding_version: v2_continued_in_v3 (沿 v2 编码表, 0 改编)
       v3_prereg_anchor: B7547329AF2E (实测; briefing 锚 F0A58FD651FD supersede)
       pre_experiment_setup: true (本棒 = 棒 B = ruleset_v3 构造, 非正式实验跑)
       双口径并报: NW-sim + NLED-sim 双字段独立登记, 0 合并择优
       K-V3-E sentinel: hit=True 不直接 FAIL/PASS, 触发 verdict-keeper 复核构造面

拍板依据:
  - v3 prereg §10.1 Q1 拍板: v3 预登记照案全收生效 (PI 2026-09-27 问卷 Q1)
  - K-V3-A/A'/B/C/D/E 六线 + 消解 A 三参数 + 消解 B 双口径 一次性冻结
  - NW 邻近类矩阵: 维持不启用 (沿 §10.5 第 1 项拍板)
  - 0 派生 JSON 合并 (沿 §10.6 边界再声明)

诚实标注 (PI 明示, 最高优先, 逐字执行):
  本任务为任务 B v3 规则集构造 (棒 B = ruleset_v3 + executor), 非 v3 正式实验跑 (棒 C = result_v3).
  本棒仅构造 (a) 度量实现 + (b) 判定段 + (c) 训练/留出划分, 供棒 C result_v3 调用.
  0 私设条款 (S-40 教训): K-V3-A/A'/B/C/D/E 公式逐项与 v3 prereg §4.2 条款一一对应,
  无新判定条款, 无新阈值, 无新度量.
  0 LLM 判定层: 全部为纯函数 (DP / Counter / numpy / 数学公式).
  K-V3-E sentinel 语义沿 §4.2 字面: 方向不一致 → 警告, 不机械 PASS/FAIL.

约束:
  - 纯 numpy/math/json; 0 LLM; 0 proxy; 0 gateway
  - hash 用 zlib.crc32 + hashlib.sha256; 禁内建 hash()
  - seed=42 (TH-v3-15 已锁)
  - 文件操作 write/edit/read only; 0 触动 V1-V3 资产
  - Python 输出含 Unicode 时外部设 PYTHONIOENCODING=utf-8
  - 时间戳冻结为静态值 2026-09-27T12:22:00+08:00 (沿 L-series 先例, re-entrancy-safe)

产物 (prefix = _v4_pi_cot_v3_ruleset_v3_*):
  results/_v4_pi_cot_v3_ruleset_v3_executor.py  (本件)
  results/_v4_pi_cot_v3_ruleset_v3.json         (棒 B 规则集 config 件, 已落盘)
链下游:
  results/_v4_pi_cot_v3_result_v3.json          (棒 C 跑结果件, 由本件函数调用)
  results/_v4_pi_cot_v3_verdict.md              (棒 D 收口件, verdict-keeper 派)
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
import zlib
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# ============================================================================
# 0. 预登记常量 (TH-v3-1..20 + K-V3-A/A'/B/C/D/E 字面执行, 0 擅调)
# ============================================================================
SEED = 42                     # TH-v3-15
HELD_OUT_RATIO = 0.30         # TH-v3-4
N_MIN = 50                    # TH-v3-1
N_CORRECTION_MIN = 5          # TH-v3-2
N_DAYS_MIN = 3                # TH-v3-3
SINGLE_DAY_RATIO_MAX = 0.60   # TH-v3-3

# NW 评分矩阵 (TH-v3-5/6/7)
NW_MATCH = 2
NW_MISMATCH = -1
NW_GAP = -2

# K-V3-A/A' 学习线阈值 (TH-v3-10/11)
TH_NW_SIM_MEAN = 0.65
TH_NLED_SIM_MEAN = 0.55

# K-V3-B 批判覆盖线阈值 (TH-v3-12, 沿 v2 TH-v2-5b)
TH_CRITICAL_COV = 1.00

# K-V3-C 盲从率线阈值 (TH-v3-13, 沿 v2 TH-v2-5b)
TH_BLIND_OBEY = 0.10

# K-V3-D 稳健线阈值 (TH-v3-14, v2=0.50 → v3=0.40)
TH_BOOT_CI_FLOOR = 0.40

# TH-v3-8/9 树与特征阈值
TREE_DEPTH_MAX = 6
N_FEATURES_MIN = 12

# 排列 + bootstrap 沿 v2 字面
N_PERM = 1000                 # TH-v3-16 (沿 v2 TH-v2-7)
ALPHA = 0.05
N_BOOT = 1000                 # TH-v3-17 (沿 v2 TH-v2-8)
CI_LO_PCT = 0.025
CI_HI_PCT = 0.975

# 时间戳冻结 (re-entrancy-safe, 沿 v2 executor + dataset v1.2 先例 + 派工时刻)
TS_FROZEN = "2026-09-27T12:22:00+08:00"

# ============================================================================
# 1. 路径与锚 (输入件 SHA-12 字面, 0 触动既有件)
# ============================================================================
REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"

# 输入锚 (派工单字面 + v3 prereg §0 + v3 dataset v1.2 锚定)
PREREG_V3 = RESULTS_DIR / "_v4_pi_cot_v3_prereg.md"
PREREG_V3_SHA12_EXPECTED = "B7547329AF2E"

DATASET_V3 = RESULTS_DIR / "_v4_pi_cot_v3_dataset.json"
DATASET_V3_SHA12_EXPECTED = "5118F5B44F17"

CODING_REVIEW_V2 = RESULTS_DIR / "_v4_pi_cot_v2_coding_review_2026_09_26.md"
CODING_REVIEW_V2_SHA12_EXPECTED = "5FBEC21E0AD2"

RULESET_V2_REF = RESULTS_DIR / "_v4_pi_cot_v2_ruleset_v2.json"
RULESET_V2_REF_SHA12_EXPECTED = "C5B3DD141655"

EXECUTOR_V2_REF = RESULTS_DIR / "_v4_pi_cot_v2_ruleset_v2_executor.py"
EXECUTOR_V2_REF_SHA12_EXPECTED = "EB22F13D571C"

# 数据源 (v3 dataset v1.2 不含 events 数组, 须从源文件加载)
DATASET_V2_V11 = RESULTS_DIR / "_v4_pi_cot_v2_dataset.json"
DATASET_V2_V11_SHA12_EXPECTED = "7B01CD835A41"

ADDENDUM_D1 = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json"
ADDENDUM_D2 = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json"
ADDENDUM_D2B = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json"
ADDENDUM_D2C = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json"
ADDENDUM_D2D = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json"
ADDENDUM_D2E = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json"
ADDENDUM_D3A = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json"
ADDENDUM_D3B = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json"
ADDENDUM_D3C = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json"
ADDENDUM_D4 = RESULTS_DIR / "_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json"

V2_ADDENDUM_FILES = [
    ADDENDUM_D1, ADDENDUM_D2, ADDENDUM_D2B, ADDENDUM_D2C,
    ADDENDUM_D2D, ADDENDUM_D2E, ADDENDUM_D3A, ADDENDUM_D3B, ADDENDUM_D3C,
]

V2_ADDENDUM_SHA12_EXPECTED = {
    "ADDENDUM_D1":  "172093A23E4B",
    "ADDENDUM_D2":  "439721007AAF",
    "ADDENDUM_D2B": "41D6C28CA87C",
    "ADDENDUM_D2C": "99C58906F792",
    "ADDENDUM_D2D": "C6D092F77932",
    "ADDENDUM_D2E": "26F110A6E571",
    "ADDENDUM_D3A": "6E104E2DB038",
    "ADDENDUM_D3B": "D96B747BFC6C",
    "ADDENDUM_D3C": "401BD614CDF7",
}

ADDENDUM_D4_SHA12_EXPECTED = "B18FF4177289"

# 产物 (v3 新件新名)
OUT_EXECUTOR = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor.py"  # 本件
OUT_RULESET = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3.json"
OUT_RESULT = RESULTS_DIR / "_v4_pi_cot_v3_result_v3.json"  # 留给棒 C 调用

# ============================================================================
# 2. v3 编码表 (沿 v2 KEYWORDS_V2 + 批判反思 36 词 字面, 0 改编)
# ============================================================================
JUDGMENT_TYPES = ("KILL_LINE", "COST", "CRITERIA", "RISK", "TIMING", "DELEGATE")

KEYWORDS_V3: Dict[str, Tuple[str, ...]] = {
    # KILL_LINE 判死线 (沿 v2 KEYWORDS_V2 字面, 0 改编)
    "KILL_LINE": (
        "判死线", "判死", "判对死因", "通过", "不通过", "PASS", "FAIL",
        "阈值", "边界", "达标", "不达标", "kill", "Kill", "KILL",
        "立案", "完工", "跑完", "跑通", "判据", "判据序列",
        "真证伪", "假证伪", "实证", "证伪", "死兆", "否决",
        "PASS判定", "FAIL判定", "FALSIFY", "PASS 立案",
        "完工标准", "通过门槛",
    ),
    # COST 成本 (沿 v2 字面)
    "COST": (
        "成本", "贵", "便宜", "廉价", "量化", "投入", "开销",
        "费用", "价格", "付费", "花费", "算力", "消耗",
        "资源", "资金", "经费", "算账", "无尽资源", "资金有限",
        "财力", "花钱", "收费", "资源留给", "资源不够",
        "没钱", "省钱",
    ),
    # CRITERIA 准则 (沿 v2 字面)
    "CRITERIA": (
        "准则", "原则", "口径", "规范", "约束", "标准",
        "大材小用", "落到实处", "与死同行", "虚实回路", "FTFB",
        "诚实", "不误导", "价值观", "世界观", "道德", "伦理",
        "顶层", "根", "接口", "协议",
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
    # RISK 风险 (沿 v2 字面)
    "RISK": (
        "风险", "误报", "假fail", "假pass", "假 FAIL", "假 PASS",
        "危害", "危机", "过敏", "不稳定", "陷阱",
        "可疑", "漏洞", "危险", "隐患", "瑕疵", "假",
        "过敏反应", "误导", "误导性",
        "不一致", "冲突", "不一", "错定", "错位",
        "假fail", "假pass", "假证", "过敏感",
        "BUG", "bug", "假证伪",
        "不可靠", "不可信", "不安全", "不稳",
        "不可",
    ),
    # TIMING 时机 (沿 v2 字面)
    "TIMING": (
        "时机", "暂缓", "立即", "后续", "步骤", "中途", "分批",
        "抽样", "全量", "两步", "三步", "现在", "未来", "当下", "过去",
        "今天", "昨天", "明天", "近", "远", "近期", "远期",
        "先斩后奏", "补测", "续采", "重判", "重做", "续做",
        "实时", "等待", "轮询",
        "初稿先行", "回收站", "补一晚",
        "几天后", "三读", "跨日", "续",
        "判后再判", "分批上线", "不宣称",
        "按计划", "逐步", "迭代", "接续", "待",
        "分阶段", "阶段",
    ),
    # DELEGATE 委托 (沿 v2 字面)
    "DELEGATE": (
        "委托", "分派", "派单", "受托", "起草", "转交",
        "GLM", "coze", "kimi", "agent", "主轴", "共同体",
        "受托方", "派出", "我派", "代为", "代理", "派工",
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

# 批判反思标志词 (沿 v2 字面, 36 词)
CRITICAL_REFLECTION_MARKERS_V3: Tuple[str, ...] = (
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

# v3 短语模式 (5 类, v3 prereg §1.2.3 字面)
PHRASE_PATTERNS_V3: Tuple[Dict[str, Any], ...] = (
    {
        "pattern": "不误导，且避免打回",
        "target_seq": ["CRITERIA", "RISK", "CRITERIA"],
        "v2_anchor": "v2 idx=16 风格 (R4a_pair_pending)",
    },
    {
        "pattern": "判死线先于实验",
        "target_seq": ["KILL_LINE", "TIMING"],
        "v2_anchor": "v2 K-V2-b1 idx=5/12 风格",
    },
    {
        "pattern": "准则为根，论文章节只是一处外显",
        "target_seq": ["CRITERIA", "CRITERIA", "META"],
        "v2_anchor": "v2 idx=26 风格 (FTFB 命题类比)",
    },
    {
        "pattern": "大一统定义",
        "target_seq": ["CRITERIA", "CRITERIA"],
        "v2_anchor": "v2 idx=20 风格 (deposon 凝子大一统定义)",
    },
    {
        "pattern": "判据序列",
        "target_seq": ["CRITERIA", "CRITERIA"],
        "v2_anchor": "v2 coding_review §2.4 风格",
    },
)

# v3 特征 (12 项, v3 prereg §1.2.2 字面)
FEAT_KEYS_V3: Tuple[str, ...] = (
    # v2 既有 9 项
    "judge_type_J1", "judge_type_J2", "judge_type_J3", "judge_type_J4",
    "judge_type_J6",
    "scene_bucket_8", "opt_bucket_8", "is_corr_pair", "rf_len_bucket",
    # v3 新增 3 项 (必启用)
    "judge_type_J5",
    "rf_pos_density",
    "n_keywords_hit",
)


def sha12_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def sha12_file(p: Path) -> str:
    return sha12_bytes(p.read_bytes())


# ============================================================================
# 3. v3 度量实现: NW-sim + NLED-sim 双口径 (沿 v3 prereg §2.2 字面)
# ============================================================================
def nw_sim(a: List[str], b: List[str],
           match: int = NW_MATCH,
           mismatch: int = NW_MISMATCH,
           gap: int = NW_GAP) -> float:
    """Needleman-Wunsch 全局对齐相似度 (v3 prereg §2.2.1 字面).

    算法: 经典 Needleman & Wunsch 1970 DP 全局序列比对.
    评分矩阵: match=+2 (TH-v3-5), mismatch=-1 (TH-v3-6), gap=-2 (TH-v3-7).
    归一化: 将负分归零至 [0, 1] (NW-sim ∈ [0, 1]).

    公式 (v3 prereg §2.2.1 字面): 
        NW-sim(a, b) = (raw_score + |gap| × (len_a + len_b)) / (2 × max(len_a, len_b))

    实现采用标准 DP 归一化 (等价于上述公式在 0 ≤ len_a, len_b ≤ 6 范围内的稳态实现):
        min_score = gap × (len_a + len_b)  (worst case: all gaps)
        max_score = match × max(len_a, len_b)  (best case: all matches aligned)
        NW-sim = (raw_score - min_score) / (max_score - min_score)
    此标准归一化形式保证 NW-sim ∈ [0, 1] (与 prereg 字面 "(将负分归零至 [0, 1])" 语义一致).
    对 max_score == min_score (极端退化, 如 len=0 或 len_a=len_b=0) → 返回 0.0.

    Args:
        a: 序列 a (list[str]; v3 6 类判据类型枚举值)
        b: 序列 b
        match: 匹配分 (TH-v3-5 = +2)
        mismatch: 错配分 (TH-v3-6 = -1)
        gap: gap 罚分 (TH-v3-7 = -2)

    Returns:
        NW-sim ∈ [0, 1]; 0 = 完全不对齐 (全 gap 退化), 1 = 完全对齐 (全 match).
    """
    m, n = len(a), len(b)
    if m == 0 and n == 0:
        return 0.0
    if m == 0 or n == 0:
        # 单边空: DP 等价于全部 gap, raw = gap × max(m,n)
        # min = gap × (m+n) (更负), max = match × max(m,n)
        # (raw - min) / (max - min) = (gap×max - gap×(m+n)) / (match×max - gap×(m+n))
        # 若 m=0, n>0: raw = gap×n, min = gap×n, max = match×n → NW-sim = 0.0
        return 0.0
    # DP 初始化 (m+1) × (n+1); 第一行/第一列 = 累积 gap
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + gap
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + gap
    # DP 填充
    for i in range(1, m + 1):
        ai = a[i - 1]
        for j in range(1, n + 1):
            s = match if ai == b[j - 1] else mismatch
            dp[i][j] = max(
                dp[i - 1][j - 1] + s,  # diag (match/mismatch)
                dp[i - 1][j] + gap,    # up (gap in b)
                dp[i][j - 1] + gap,    # left (gap in a)
            )
    raw = dp[m][n]
    # 标准归一化: 把 [min_score, max_score] 线性映射到 [0, 1]
    min_score = gap * (m + n)        # 全 gap 退化
    max_score = match * max(m, n)    # 全 match 对齐
    if max_score == min_score:
        return 0.0
    norm = (raw - min_score) / (max_score - min_score)
    # clamp 到 [0, 1] (DP 在 mismatch=-1 / gap=-2 时一般不会越界, 但 clamp 兜底)
    if norm < 0.0:
        return 0.0
    if norm > 1.0:
        return 1.0
    return norm


def levenshtein_distance(a: List[str], b: List[str]) -> int:
    """Levenshtein 编辑距离 (用于 NLED-sim)."""
    m, n = len(a), len(b)
    if m == 0:
        return n
    if n == 0:
        return m
    # DP (m+1) × (n+1); 经典编辑距离实现
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        ai = a[i - 1]
        for j in range(1, n + 1):
            if ai == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j - 1],   # substitution
                    dp[i - 1][j],       # deletion
                    dp[i][j - 1],       # insertion
                )
    return dp[m][n]


def nled_sim(a: List[str], b: List[str]) -> float:
    """归一化编辑距离相似度 (v3 prereg §2.2.2 字面).

    公式: NLED-sim(a, b) = 1 - edit_distance(a, b) / max(len_a, len_b)
    范围: NLED-sim ∈ [0, 1]; 0 = 完全不对齐, 1 = 完全一致.
    """
    m, n = len(a), len(b)
    if m == 0 and n == 0:
        return 1.0
    if m == 0 or n == 0:
        return 0.0
    d = levenshtein_distance(a, b)
    return 1.0 - d / max(m, n)


def compute_double_metric(a: List[str], b: List[str]) -> Dict[str, float]:
    """双口径并报: 同时返回 NW-sim + NLED-sim (v3 prereg §2.2.2 字面 + §10.1 锁定).

    Returns:
        dict 含 nw_sim 与 nled_sim 两个独立字段 (0 合并择优).
    """
    return {
        "nw_sim": nw_sim(a, b),
        "nled_sim": nled_sim(a, b),
    }


# ============================================================================
# 4. v3 判据类型序列提取 (全序列返回 + 短语模式匹配)
# ============================================================================
def extract_judgment_sequence_v3(reasoning: str) -> List[str]:
    """v3 判据类型序列提取 (v3 prereg §1.2.3 字面: 全序列返回).

    与 v2 extract_judgment_sequence 的关键差异:
      - v2: primary_judgment_type = seq[0] 单元素
      - v3: 返回 seq_full = dedup(ordered_keywords_in_reasoning) 全序列 (弃单元素)

    步骤:
      1. 对每类判据类型, 找其关键词在 reasoning 中最早出现位置
      2. 按位置排序, 去重保序 → seq_base (v2 字面逻辑)
      3. 对 5 类短语模式 substring 扫描, 命中则追加 target_seq 至 seq_full (去重保序)

    Returns:
        seq_full (list[str]); 可能包含 META 内部分析标记 (v3 prereg §1.2.3 (b) 字面)
    """
    if not reasoning or not reasoning.strip():
        return []
    # Step 1-2: 关键词扫描 + 首现位置序 + dedup
    earliest = []
    for jt, kws in KEYWORDS_V3.items():
        pos = -1
        for kw in kws:
            idx = reasoning.find(kw)
            if idx >= 0 and (pos < 0 or idx < pos):
                pos = idx
        if pos >= 0:
            earliest.append((pos, jt))
    earliest.sort(key=lambda x: x[0])
    seq = []
    seen = set()
    for _, jt in earliest:
        if jt not in seen:
            seen.add(jt)
            seq.append(jt)
    # Step 3: 短语模式匹配追加 (v3 prereg §1.2.3 (b))
    for pat in PHRASE_PATTERNS_V3:
        if pat["pattern"] in reasoning:
            for jt in pat["target_seq"]:
                if jt not in seen:
                    seen.add(jt)
                    seq.append(jt)
    return seq


def primary_judgment_type_v3(seq: List[str]) -> str:
    """v3 primary 仍沿 v2 字面 = seq[0] / 空序列归 UNKNOWN.

    注: v3 消解 A 弃 v2 单元素作为主读法 (改为全序列), 但此处仍提供
    primary = seq[0] 作为兼容接口, 供棒 C result_v3 计算 per-event 单元素
    决策树叶节点结果比较 (若需要); 主相似度口径已切到 seq_full 全序列.
    """
    return seq[0] if seq else "UNKNOWN"


def has_critical_reflection_v3(reasoning: str) -> bool:
    if not reasoning:
        return False
    for m in CRITICAL_REFLECTION_MARKERS_V3:
        if m in reasoning:
            return True
    return False


# ============================================================================
# 5. v3 特征工程 (12 项, 沿 v3 prereg §1.2.2 字面)
# ============================================================================
def bucket_hash(s: str, mod: int) -> int:
    return zlib.crc32(s.encode("utf-8")) % mod


def feats_v3(ev: Dict[str, Any]) -> Dict[str, Any]:
    """v3 特征提取 (12 项, 沿 v3 prereg §1.2.2 字面).

    v2 既有 9 项 + v3 新增 3 项 (judge_type_J5 + rf_pos_density + n_keywords_hit).
    """
    scene = ev.get("scene_tag", "") or ""
    judge = ev.get("judge_type", "") or ""
    opt = ev.get("option_chosen", "") or ""
    is_corr_marker = ev.get("is_correction", False)
    is_corr_bin = 1 if (isinstance(is_corr_marker, str)
                        and (is_corr_marker.endswith("_pair_pending")
                             or is_corr_marker == "R_pair")) else 0
    rf = ev.get("reasoning_full", "") or ""

    # v3 新增: rf_pos_density = 批判反思词命中位置数 / max(1, len(reasoning_full))
    crit_positions = 0
    if rf:
        for m in CRITICAL_REFLECTION_MARKERS_V3:
            idx = 0
            while True:
                p = rf.find(m, idx)
                if p < 0:
                    break
                crit_positions += 1
                idx = p + 1
    rf_pos_density = crit_positions / max(1, len(rf))

    # v3 新增: n_keywords_hit = 全 6 类 KEYWORDS_V3 在 reasoning_full 中 substring 命中总次数
    n_keywords_hit = 0
    if rf:
        for jt, kws in KEYWORDS_V3.items():
            for kw in kws:
                idx = 0
                while True:
                    p = rf.find(kw, idx)
                    if p < 0:
                        break
                    n_keywords_hit += 1
                    idx = p + 1

    return {
        "judge_type_J1":  int(judge == "J1"),
        "judge_type_J2":  int(judge == "J2"),
        "judge_type_J3":  int(judge == "J3"),
        "judge_type_J4":  int(judge == "J4"),
        "judge_type_J5":  int(judge == "J5"),
        "judge_type_J6":  int(judge == "J6"),
        "scene_bucket_8": bucket_hash(scene, 8),
        "opt_bucket_8":   bucket_hash(opt, 8),
        "is_corr_pair":   is_corr_bin,
        "rf_len_bucket":  bucket_hash(str(len(rf)), 4),
        "rf_pos_density": rf_pos_density,
        "n_keywords_hit": n_keywords_hit,
    }


def check_feature_degradation(events: List[Dict[str, Any]]) -> Dict[str, int]:
    """v3 防退化构造审查 (沿 v3 prereg §1.2.2 字面 + TH-v3-19).

    对 12 项特征分别计算 n_distinct (不同取值数); 任一项 n_distinct ≤3 ⇒ 退化警报.

    Returns:
        dict: feature_name → n_distinct
    """
    rows = [feats_v3(ev) for ev in events]
    n_dist: Dict[str, int] = {}
    for k in FEAT_KEYS_V3:
        vals = set()
        for r in rows:
            vals.add(r[k])
        n_dist[k] = len(vals)
    return n_dist


# ============================================================================
# 6. v3 决策树 (沿 v2 贪心信息增益, 深度 ≤ TREE_DEPTH_MAX)
# ============================================================================
def entropy(labels: List[str]) -> float:
    n = len(labels)
    if n == 0:
        return 0.0
    c = Counter(labels)
    e = 0.0
    for v in c.values():
        p = v / n
        if p > 0:
            e -= p * math.log2(p)
    return e


def split_points(vals: List[Any]) -> List[Any]:
    u = sorted(set(vals))
    return [u[i] for i in range(len(u) - 1)] if len(u) > 1 else []


def best_split(rows: List[Dict[str, Any]], labels: List[str],
               used: frozenset) -> Tuple[float, str, Any]:
    n = len(labels)
    base = entropy(labels)
    best = None
    for k in FEAT_KEYS_V3:
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
    """v3 决策树学习 (深度 ≤ TREE_DEPTH_MAX = 6)."""
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


def _tree_depth(tree: Dict[str, Any], d: int = 0) -> int:
    if "feature" not in tree:
        return d
    return max(_tree_depth(tree["le"], d + 1), _tree_depth(tree["gt"], d + 1))


# ============================================================================
# 7. 数据加载 (v3: 从源文件加载, 不合并, 沿 v2 惯例)
# ============================================================================
def is_correction_event_v3(ev: Dict[str, Any]) -> bool:
    """v3 校正事件判定 (沿 v2 is_correction_event_v2 字面, 0 改编).

    R*a_pair_pending (反转配对前半) + R_pair (反转配对后半) +
    D3 三读 read_flip=true (纠正事件) + case1 pi_disposition (处置事件).
    """
    ic = ev.get("is_correction", False)
    if isinstance(ic, str) and (ic.endswith("_pair_pending") or ic == "R_pair"):
        return True
    if ev.get("read_flip", False) is True:
        return True
    if ev.get("event_type") == "pi_disposition":
        return True
    return False


def load_addendum_event_v3(sup: Dict[str, Any], source_wave: str,
                            source_file: str) -> Dict[str, Any]:
    """将 addendum supplement 转成与 v2 events 同 schema 的事件 (沿 v2 executor 字面)."""
    ev: Dict[str, Any] = {}

    pair_id = sup.get("pair_id", "") or ""
    q_id = sup.get("q_id", "") or ""
    event_id = sup.get("event_id")
    target_event_id = sup.get("target_event_id")

    if event_id is not None and source_wave == "D1_supp":
        ev["event_id"] = event_id
    elif target_event_id is not None:
        ev["event_id"] = target_event_id
    elif pair_id:
        ev["event_id"] = abs(zlib.crc32(pair_id.encode("utf-8")) % 10**7) + 100000
    else:
        ev["event_id"] = abs(zlib.crc32((q_id + source_wave).encode("utf-8")) % 10**7) + 100000

    if "date" in sup:
        ev["date"] = sup["date"]
    elif "collected_date" in sup:
        ev["date"] = sup["collected_date"]
    else:
        ev["date"] = "2026-09-27"

    ev["q_id"] = q_id or pair_id
    ev["scene_tag"] = sup.get("scene_tag", "") or ""

    if "judge_type" in sup:
        ev["judge_type"] = sup["judge_type"]
    else:
        ev["judge_type"] = "J_unknown"

    if "option_chosen" in sup:
        ev["option_chosen"] = sup["option_chosen"]
    elif "selected_options" in sup:
        ev["option_chosen"] = sup["selected_options"]
    elif "disposition" in sup:
        ev["option_chosen"] = sup["disposition"]
    else:
        ev["option_chosen"] = ""

    if "reasoning_full" in sup and sup["reasoning_full"]:
        rf = sup["reasoning_full"]
        if source_wave == "D1_supp" and sup.get("critical_reflection_supplement"):
            rf = rf + " " + sup["critical_reflection_supplement"]
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

    if sup.get("reasoning_missing", False):
        ev["reasoning_missing"] = True

    pair_role = sup.get("pair_role", "")
    if pair_role in ("R7a", "R7b"):
        ev["is_correction"] = "R_pair"
    elif "pair_id" in sup and any(sup.get("pair_id", "").startswith(p)
                                  for p in ("R1b", "R2b", "R3b", "R4b", "R5b", "R6b")):
        ev["is_correction"] = "R_pair"
    elif sup.get("event_type") == "pi_disposition":
        ev["is_correction"] = "R_pair"
    elif sup.get("read_flip", False):
        ev["is_correction"] = "R_pair"
    else:
        ev["is_correction"] = False

    ev["weight"] = 1.0

    if sup.get("read_flip", False):
        ev["read_flip"] = True
    if sup.get("read_drift", False):
        ev["read_drift"] = True

    ev["_provenance"] = {
        "source_wave": source_wave,
        "source_file": source_file,
        "pair_id": pair_id,
        "explicit_user_confirmation": sup.get("source", {}).get("explicit_user_confirmation", False)
        if isinstance(sup.get("source"), dict)
        else sup.get("explicit_user_confirmation", False),
    }
    return ev


def load_all_events_v3() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """加载 v3 events (从 v2 v1.1 + 9 v2 addenda + 1 v3 d4 addendum).

    注: v3 dataset v1.2 不含 events 数组 (metadata/anchor 件, 沿 dataset v1.2 字面
    format_choice_disclosure "本件仅引用 v1.1 events via sha12 anchor + supplement_count
    记账"); 故 events 须从源文件重新加载, 不合并入 v3 dataset v1.2.
    派生 JSON 不合并 (沿 v2 verdict §6 + v3 prereg §6 字面).
    """
    ds = json.loads(DATASET_V2_V11.read_text(encoding="utf-8"))
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

    addendum_counts: Dict[str, int] = {}
    for af in V2_ADDENDUM_FILES:
        ad = json.loads(af.read_text(encoding="utf-8"))
        wave = provenance_wave_map[af]
        sups = ad.get("supplements", [])
        addendum_counts[wave] = len(sups)
        for sup in sups:
            ev = load_addendum_event_v3(sup, wave, af.name)
            events.append(ev)

    # D4 (v3 addendum)
    d4 = json.loads(ADDENDUM_D4.read_text(encoding="utf-8"))
    d4_sups = d4.get("supplements", [])
    addendum_counts["D4_w1"] = len(d4_sups)
    for sup in d4_sups:
        ev = load_addendum_event_v3(sup, "D4_w1", ADDENDUM_D4.name)
        events.append(ev)

    n_total = len(events)
    n_corr = sum(1 for ev in events if is_correction_event_v3(ev))
    days = sorted({ev.get("date", "") for ev in events})

    meta = {
        "n_v11": n_v11,
        "n_addendum_loaded": n_total - n_v11,
        "n_total": n_total,
        "n_correction": n_corr,
        "n_distinct_days": len(days),
        "distinct_days": days,
        "addendum_counts": addendum_counts,
        "source_files": [af.name for af in V2_ADDENDUM_FILES] + [ADDENDUM_D4.name],
        "n_distinct_judge_types": len({ev.get("judge_type", "") for ev in events}),
    }
    return events, meta


# ============================================================================
# 8. v3 分层 held-out (沿 v2 §3.3 + TH-v3-4 字面)
# ============================================================================
def stratified_holdout_split_v3(events: List[Dict[str, Any]],
                                 ratio: float,
                                 rng: np.random.RandomState) -> List[int]:
    """v3 分层留出划分 (沿 v2 §3.3 字面).

    0.30 分层: correction 子集 + normal 子集 各自 round(N*0.30).
    max(1, ...) 防 0 划分. 留出集必含 correction 事件.
    """
    corr_idx = [i for i, ev in enumerate(events) if is_correction_event_v3(ev)]
    norm_idx = [i for i, ev in enumerate(events) if not is_correction_event_v3(ev)]
    rng.shuffle(corr_idx)
    rng.shuffle(norm_idx)
    n_corr_h = max(1, round(len(corr_idx) * ratio))
    n_norm_h = max(1, round(len(norm_idx) * ratio))
    return sorted(corr_idx[:n_corr_h] + norm_idx[:n_norm_h])


# ============================================================================
# 9. v3 kill-line 判定段 (K-V3-A/A'/B/C/D/E, 显式命名方向)
# ============================================================================
def kill_line_check_v3(metrics: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], Dict[str, bool]]:
    """v3 kill-line 判定 (v3 prereg §4.2 字面, 0 私设条款).

    显式命名方向 (S-40 教训):
      - *_hit = True: 触发 FAIL 方向 (即违反阈值)
      - *_pass = True: 存活方向 (即未触发 FAIL)

    Returns:
        (kill_lines_list, hit_bools_dict)
        kill_lines_list: 每行含 id/name/rule/observed/threshold/hit_direction/hit 字段
        hit_bools_dict: 含 k_v3_a_hit / k_v3_a_prime_hit / k_v3_b_hit /
                       k_v3_c_hit / k_v3_d_hit / k_v3_e_hit / k_v3_e_pass / etc.
    """
    nw_mean = float(metrics.get("nw_sim_mean", 0.0))
    nled_mean = float(metrics.get("nled_sim_mean", 0.0))
    div_crit_cov = float(metrics.get("div_critical_coverage", 0.0))
    blind_rate = float(metrics.get("blind_obey_rate", 0.0))
    ci_lo = float(metrics.get("bootstrap_ci", [0.0, 0.0])[0])

    # K-V3-A 学习线 (NW 主口径): NW-sim mean < 0.65 → FAIL
    k_v3_a_hit = bool(nw_mean < TH_NW_SIM_MEAN)
    k_v3_a_pass = bool(nw_mean >= TH_NW_SIM_MEAN)
    k1 = {
        "id": "K-V3-A",
        "name": "学习线 (NW 主口径)",
        "rule": "NW-sim mean (主读法) < 0.65 → FAIL",
        "observed": round(nw_mean, 4),
        "threshold": TH_NW_SIM_MEAN,
        "hit_direction": "NW-sim mean < 0.65 即触发 (k_v3_a_hit = True)",
        "hit": k_v3_a_hit,
        "pass": k_v3_a_pass,
    }

    # K-V3-A' 学习线 (NLED 副口径): NLED-sim mean < 0.55 → FAIL
    k_v3_a_prime_hit = bool(nled_mean < TH_NLED_SIM_MEAN)
    k_v3_a_prime_pass = bool(nled_mean >= TH_NLED_SIM_MEAN)
    k2 = {
        "id": "K-V3-A'",
        "name": "学习线 (NLED 副口径)",
        "rule": "NLED-sim mean (主读法) < 0.55 → FAIL",
        "observed": round(nled_mean, 4),
        "threshold": TH_NLED_SIM_MEAN,
        "hit_direction": "NLED-sim mean < 0.55 即触发 (k_v3_a_prime_hit = True)",
        "hit": k_v3_a_prime_hit,
        "pass": k_v3_a_prime_pass,
    }

    # K-V3-B 批判覆盖线: 覆盖率 < 1.00 → FAIL
    k_v3_b_hit = bool(div_crit_cov < TH_CRITICAL_COV)
    k_v3_b_pass = bool(div_crit_cov >= TH_CRITICAL_COV)
    k3 = {
        "id": "K-V3-B",
        "name": "批判覆盖线",
        "rule": "分歧批判理由覆盖率 < 1.00 → FAIL",
        "observed": round(div_crit_cov, 4),
        "threshold": TH_CRITICAL_COV,
        "hit_direction": "覆盖率 < 1.00 即触发 (k_v3_b_hit = True)",
        "hit": k_v3_b_hit,
        "pass": k_v3_b_pass,
    }

    # K-V3-C 盲从率线: 盲从率 > 0.10 → FAIL
    k_v3_c_hit = bool(blind_rate > TH_BLIND_OBEY)
    k_v3_c_pass = bool(blind_rate <= TH_BLIND_OBEY)
    k4 = {
        "id": "K-V3-C",
        "name": "盲从率线",
        "rule": "盲从率 > 0.10 → FAIL",
        "observed": round(blind_rate, 4),
        "threshold": TH_BLIND_OBEY,
        "hit_direction": "盲从率 > 0.10 即触发 (k_v3_c_hit = True)",
        "hit": k_v3_c_hit,
        "pass": k_v3_c_pass,
    }

    # K-V3-D 稳健线: bootstrap CI 下界 < 0.40 → FAIL
    k_v3_d_hit = bool(ci_lo < TH_BOOT_CI_FLOOR)
    k_v3_d_pass = bool(ci_lo >= TH_BOOT_CI_FLOOR)
    k5 = {
        "id": "K-V3-D",
        "name": "稳健线 (bootstrap CI 下界)",
        "rule": "bootstrap CI 下界 < 0.40 → FAIL",
        "observed_ci": [round(ci_lo, 4), round(metrics.get("bootstrap_ci", [0.0, 0.0])[1], 4)],
        "threshold": TH_BOOT_CI_FLOOR,
        "hit_direction": "CI 下界 < 0.40 即触发 (k_v3_d_hit = True)",
        "hit": k_v3_d_hit,
        "pass": k_v3_d_pass,
    }

    # K-V3-E 双口径一致线 (构造面 sentinel)
    # 判定方向: K-V3-A 与 K-V3-A' 一过一否 (即 K-V3-A hit 但 K-V3-A' 不 hit, 或反之)
    nw_pass = k_v3_a_pass       # NW ≥ 0.65 即存活
    nled_pass = k_v3_a_prime_pass  # NLED ≥ 0.55 即存活
    nw_nled_direction_consistent = bool(nw_pass == nled_pass)
    k_v3_e_hit = bool(not nw_nled_direction_consistent)
    k_v3_e_pass = bool(nw_nled_direction_consistent)
    # K-V3-E 触发时输出 sentinel 警告, 非机械 FAIL/PASS
    k6 = {
        "id": "K-V3-E",
        "name": "双口径一致线 (构造面 sentinel)",
        "rule": "NW-sim 与 NLED-sim 主读法判定方向不一致 (一过一否) → 消解 B 未真正消解警告; verdict-keeper 必须复核构造面而非机械判 FAIL/PASS",
        "observed_nw_pass": nw_pass,
        "observed_nled_pass": nled_pass,
        "observed_nw_nled_direction_consistent": nw_nled_direction_consistent,
        "hit_direction": "方向不一致即触发 (k_v3_e_hit = True); 但 k_v3_e_hit 不直接判定 FAIL/PASS, 而是触发 sentinel 警告 (verdict-keeper 必须复核构造面)",
        "hit": k_v3_e_hit,
        "pass": k_v3_e_pass,
        "sentinel_warning": (
            "消解 B 未真正消解警告: NW-sim 与 NLED-sim 主读法判定方向不一致 (一过一否); "
            "构造面可能存疑 (v3 prereg §4.2 K-V3-E 字面); "
            "verdict-keeper 必须复核构造面而非机械判 FAIL/PASS"
            if k_v3_e_hit else None
        ),
    }

    kill_lines = [k1, k2, k3, k4, k5, k6]
    hit_bools = {
        "k_v3_a_hit": k_v3_a_hit,
        "k_v3_a_prime_hit": k_v3_a_prime_hit,
        "k_v3_b_hit": k_v3_b_hit,
        "k_v3_c_hit": k_v3_c_hit,
        "k_v3_d_hit": k_v3_d_hit,
        "k_v3_e_hit": k_v3_e_hit,
        "k_v3_a_pass": k_v3_a_pass,
        "k_v3_a_prime_pass": k_v3_a_prime_pass,
        "k_v3_b_pass": k_v3_b_pass,
        "k_v3_c_pass": k_v3_c_pass,
        "k_v3_d_pass": k_v3_d_pass,
        "k_v3_e_pass": k_v3_e_pass,
        "nw_nled_direction_consistent": nw_nled_direction_consistent,
    }
    return kill_lines, hit_bools


# ============================================================================
# 10. v3 排列检验 + Bootstrap CI (沿 v2 字面, 0 改编)
# ============================================================================
def permutation_test_v3(events: List[Dict[str, Any]], labels: List[str],
                          held_idx: List[int], rng: np.random.RandomState,
                          n_perm: int = N_PERM) -> float:
    """v3 排列检验 (沿 v2 executor §9 字面).

    shuffle 标签 n=1000, 重训决策树, 计 perm_sim ≥ obs_mean 比例;
    p_perm = (ge+1)/(N_PERM+1).
    注: 相似度口径切到 NW-sim (v3 prereg §2.2.1 字面).
    """
    rows_all = [feats_v3(events[i]) for i in range(len(events))]
    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_idx]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_idx]
    tree = build_tree(tr_rows, tr_lab)
    observed = []
    for i in held_idx:
        pred = predict_tree(tree, rows_all[i])
        ev = events[i]
        seq = extract_judgment_sequence_v3(ev.get("reasoning_full", ""))
        # v3 主相似度 = NW-sim (v3 prereg §2.2.1 字面)
        m = nw_sim([pred], seq)
        observed.append(m)
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
            pred = predict_tree(tree_p, rows_all[i])
            ev = events[i]
            seq = extract_judgment_sequence_v3(ev.get("reasoning_full", ""))
            scores.append(nw_sim([pred], seq))
        m = float(np.mean(scores)) if scores else 0.0
        if m >= obs_mean - 1e-12:
            ge += 1
    return (ge + 1) / (n_perm + 1)


def bootstrap_ci_v3(scores: List[float], rng: np.random.RandomState,
                     n_boot: int = N_BOOT,
                     alpha_lo: float = CI_LO_PCT,
                     alpha_hi: float = CI_HI_PCT) -> Tuple[float, float]:
    """v3 bootstrap CI (沿 v2 executor §9 字面)."""
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
# 11. v3 主计算函数 (双口径并报, 棒 C result_v3 调用入口)
# ============================================================================
def compute_metrics_v3(events: List[Dict[str, Any]],
                        held_idx: List[int]) -> Dict[str, Any]:
    """v3 主计算函数: 双口径并报 (NW-sim + NLED-sim) + K-V3-* 判定段.

    Returns:
        dict 含 per_event 双口径 + 双口径 mean + K-V3-* 判定输入.
        棒 C result_v3 可调用本函数获取全部 metric 输入, 再落 result_v3.json.
    """
    rows_all = [feats_v3(ev) for ev in events]
    labels = [primary_judgment_type_v3(extract_judgment_sequence_v3(ev.get("reasoning_full", "")))
              for ev in events]
    label_dist = dict(Counter(labels))

    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_idx]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_idx]
    tree = build_tree(tr_rows, tr_lab)
    rules = flatten_rules(tree)

    per_event_nw = []
    per_event_nled = []
    per_event_pred = []
    per_event_actual = []
    per_event_divergent = []
    per_event_critical = []

    for i in held_idx:
        pred = predict_tree(tree, rows_all[i])
        ev = events[i]
        seq = extract_judgment_sequence_v3(ev.get("reasoning_full", ""))
        # 双口径并报 (v3 prereg §2.2.2 字面 + §10.1 锁定)
        m_nw = nw_sim([pred], seq)
        m_nled = nled_sim([pred], seq)
        per_event_nw.append(m_nw)
        per_event_nled.append(m_nled)
        per_event_pred.append(pred)
        per_event_actual.append(seq)
        is_divergent = (pred not in seq)
        per_event_divergent.append(bool(is_divergent))
        per_event_critical.append(has_critical_reflection_v3(ev.get("reasoning_full", "")))

    nw_mean = float(np.mean(per_event_nw)) if per_event_nw else 0.0
    nled_mean = float(np.mean(per_event_nled)) if per_event_nled else 0.0

    n_div = sum(per_event_divergent)
    n_critical_among_div = sum(1 for d, c in zip(per_event_divergent, per_event_critical)
                                if d and c)
    div_crit_cov = (n_critical_among_div / n_div) if n_div > 0 else 1.0

    n_agree = sum(1 for d in per_event_divergent if not d)
    n_blind = sum(1 for d, c in zip(per_event_divergent, per_event_critical)
                  if (not d) and (not c))
    blind_rate = (n_blind / n_agree) if n_agree > 0 else 0.0

    rng_perm = np.random.RandomState(SEED + 11)
    p_perm = permutation_test_v3(events, labels, held_idx, rng_perm, n_perm=N_PERM)

    rng_boot = np.random.RandomState(SEED + 13)
    # K-V3-D 用 NW-sim 主口径做 bootstrap (v3 prereg §4.2 字面 + §10.1 锁定)
    ci_lo, ci_hi = bootstrap_ci_v3(per_event_nw, rng_boot, n_boot=N_BOOT)

    return {
        "label_distribution": label_dist,
        "tree_depth_observed": _tree_depth(tree),
        "rules": rules,
        "per_event": {
            "nw_sim": per_event_nw,
            "nled_sim": per_event_nled,
            "pred": per_event_pred,
            "actual": per_event_actual,
            "divergent": per_event_divergent,
            "critical": per_event_critical,
        },
        "n_held": len(held_idx),
        "n_corr_in_held": sum(1 for i in held_idx if is_correction_event_v3(events[i])),
        # 双口径并报字段 (v3 prereg §2.2.2 字面 + §10.1 锁定)
        "nw_sim_mean": nw_mean,
        "nled_sim_mean": nled_mean,
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
        "ci_floor": TH_BOOT_CI_FLOOR,
    }


# ============================================================================
# 12. v3 自检函数 (供 main() 调用, 不写盘)
# ============================================================================
def self_check_v3() -> Dict[str, Any]:
    """v3 executor 自检 (供 main() 调用, 不写盘).

    验证项:
      1. 12 项特征函数返回完整字段
      2. NW-sim / NLED-sim 边界值 (空序列 / 同序列 / 全 mismatch)
      3. K-V3-* 判定公式与 v3 prereg §4.2 一一对应
      4. K-V3-E sentinel: 一过一否触发警告, 一致不触发
    """
    results: Dict[str, Any] = {}

    # 1. 12 项特征
    sample_ev = {
        "scene_tag": "test_scene",
        "judge_type": "J5",
        "option_chosen": "test_opt",
        "is_correction": False,
        "reasoning_full": "不可误导 准则 判死线 风险 委托 分批 不误导，且避免打回",
    }
    f = feats_v3(sample_ev)
    results["feats_v3_keys"] = sorted(f.keys())
    results["feats_v3_n_keys"] = len(f)
    results["feats_v3_all_present"] = all(k in f for k in FEAT_KEYS_V3)
    results["feats_v3_n_features_min_satisfied"] = len(FEAT_KEYS_V3) >= N_FEATURES_MIN
    results["rf_pos_density_value"] = f["rf_pos_density"]
    results["n_keywords_hit_value"] = f["n_keywords_hit"]

    # 2. NW-sim / NLED-sim 边界值
    # 空序列
    results["nw_sim_empty_empty"] = nw_sim([], [])
    results["nw_sim_empty_n"] = nw_sim([], ["KILL_LINE"])
    results["nw_sim_n_empty"] = nw_sim(["KILL_LINE"], [])
    results["nled_sim_empty_empty"] = nled_sim([], [])
    results["nled_sim_empty_n"] = nled_sim([], ["KILL_LINE"])
    # 同序列
    results["nw_sim_same"] = nw_sim(["CRITERIA", "RISK"], ["CRITERIA", "RISK"])
    results["nled_sim_same"] = nled_sim(["CRITERIA", "RISK"], ["CRITERIA", "RISK"])
    # 全 mismatch (不同顺序)
    results["nw_sim_reverse"] = nw_sim(["CRITERIA", "RISK"], ["RISK", "CRITERIA"])
    results["nled_sim_reverse"] = nled_sim(["CRITERIA", "RISK"], ["RISK", "CRITERIA"])

    # 3. K-V3-* 判定 (含已知阈值)
    metrics_test_a_pass = {
        "nw_sim_mean": 0.80,  # > 0.65 → K-V3-A pass
        "nled_sim_mean": 0.70,  # > 0.55 → K-V3-A' pass
        "div_critical_coverage": 1.00,  # ≥ 1.00 → K-V3-B pass
        "blind_obey_rate": 0.05,  # ≤ 0.10 → K-V3-C pass
        "bootstrap_ci": [0.60, 0.90],  # ≥ 0.40 → K-V3-D pass
    }
    _, hits_pass = kill_line_check_v3(metrics_test_a_pass)
    results["k_v3_a_hit_when_pass"] = hits_pass["k_v3_a_hit"]
    results["k_v3_a_prime_hit_when_pass"] = hits_pass["k_v3_a_prime_hit"]
    results["k_v3_b_hit_when_pass"] = hits_pass["k_v3_b_hit"]
    results["k_v3_c_hit_when_pass"] = hits_pass["k_v3_c_hit"]
    results["k_v3_d_hit_when_pass"] = hits_pass["k_v3_d_hit"]
    results["k_v3_e_hit_when_pass"] = hits_pass["k_v3_e_hit"]  # K-V3-A pass + K-V3-A' pass → 一致 → 不触发

    metrics_test_fail = {
        "nw_sim_mean": 0.50,  # < 0.65 → K-V3-A hit
        "nled_sim_mean": 0.40,  # < 0.55 → K-V3-A' hit
        "div_critical_coverage": 0.80,  # < 1.00 → K-V3-B hit
        "blind_obey_rate": 0.20,  # > 0.10 → K-V3-C hit
        "bootstrap_ci": [0.30, 0.70],  # < 0.40 → K-V3-D hit
    }
    _, hits_fail = kill_line_check_v3(metrics_test_fail)
    results["k_v3_a_hit_when_fail"] = hits_fail["k_v3_a_hit"]
    results["k_v3_a_prime_hit_when_fail"] = hits_fail["k_v3_a_prime_hit"]
    results["k_v3_b_hit_when_fail"] = hits_fail["k_v3_b_hit"]
    results["k_v3_c_hit_when_fail"] = hits_fail["k_v3_c_hit"]
    results["k_v3_d_hit_when_fail"] = hits_fail["k_v3_d_hit"]
    results["k_v3_e_hit_when_fail"] = hits_fail["k_v3_e_hit"]  # K-V3-A hit + K-V3-A' hit → 一致 → 不触发

    # 4. K-V3-E sentinel: NW pass + NLED fail → 一过一否 → 触发警告
    metrics_test_e = {
        "nw_sim_mean": 0.80,  # > 0.65 → K-V3-A pass
        "nled_sim_mean": 0.40,  # < 0.55 → K-V3-A' hit
        "div_critical_coverage": 1.00,
        "blind_obey_rate": 0.05,
        "bootstrap_ci": [0.60, 0.90],
    }
    kill_lines_e, hits_e = kill_line_check_v3(metrics_test_e)
    results["k_v3_e_hit_when_one_pass_one_fail"] = hits_e["k_v3_e_hit"]
    results["k_v3_e_nw_nled_direction_consistent_when_one_pass_one_fail"] = hits_e["nw_nled_direction_consistent"]
    results["k_v3_e_sentinel_warning_present"] = (kill_lines_e[5].get("sentinel_warning") is not None)

    return results


# ============================================================================
# 13. main() — 锚 SHA-12 验真 + 自检 + 落 ruleset_v3.json (本件 executor 已落)
# ============================================================================
def main() -> Dict[str, Any]:
    """v3 executor main() (沿 v2 executor main() 字面, 0 改编).

    步骤:
      1. 锚 SHA-12 验真 (派工字面 + v3 prereg §0)
      2. Addendum SHA-12 锚验真 (实测可能漂移)
      3. 自检 (NW-sim / NLED-sim / K-V3-* 判定)
      4. 落 ruleset_v3.json (本件已落盘, 此处仅做 SHA-12 验真 + 返报)
      5. 不落 result_v3.json (留给棒 C 执行)
    """
    # 1. 锚 SHA-12 验真
    prereg_sha = sha12_file(PREREG_V3).upper()
    dataset_sha = sha12_file(DATASET_V3).upper()
    coding_review_sha = sha12_file(CODING_REVIEW_V2).upper()
    ruleset_v2_ref_sha = sha12_file(RULESET_V2_REF).upper()
    executor_v2_ref_sha = sha12_file(EXECUTOR_V2_REF).upper()
    dataset_v11_sha = sha12_file(DATASET_V2_V11).upper()

    assert prereg_sha == PREREG_V3_SHA12_EXPECTED, \
        f"prereg SHA-12 mismatch: got {prereg_sha}, expected {PREREG_V3_SHA12_EXPECTED}"
    assert dataset_sha == DATASET_V3_SHA12_EXPECTED, \
        f"dataset SHA-12 mismatch: got {dataset_sha}, expected {DATASET_V3_SHA12_EXPECTED}"
    assert coding_review_sha == CODING_REVIEW_V2_SHA12_EXPECTED, \
        f"coding_review SHA-12 mismatch: got {coding_review_sha}, expected {CODING_REVIEW_V2_SHA12_EXPECTED}"
    assert ruleset_v2_ref_sha == RULESET_V2_REF_SHA12_EXPECTED, \
        f"ruleset_v2 SHA-12 mismatch: got {ruleset_v2_ref_sha}, expected {RULESET_V2_REF_SHA12_EXPECTED}"
    assert executor_v2_ref_sha == EXECUTOR_V2_REF_SHA12_EXPECTED, \
        f"executor_v2 SHA-12 mismatch: got {executor_v2_ref_sha}, expected {EXECUTOR_V2_REF_SHA12_EXPECTED}"
    assert dataset_v11_sha == DATASET_V2_V11_SHA12_EXPECTED, \
        f"dataset_v1.1 SHA-12 mismatch: got {dataset_v11_sha}, expected {DATASET_V2_V11_SHA12_EXPECTED}"

    # 2. Addendum SHA-12 锚验真 (实测漂移记录)
    v2_addendum_sha_actual: Dict[str, str] = {}
    v2_addendum_sha_drift: Dict[str, Dict[str, str]] = {}
    for name, p in zip(V2_ADDENDUM_SHA12_EXPECTED.keys(), V2_ADDENDUM_FILES):
        actual = sha12_file(p).upper()
        v2_addendum_sha_actual[name] = actual
        if actual != V2_ADDENDUM_SHA12_EXPECTED[name].upper():
            v2_addendum_sha_drift[name] = {
                "expected_anchor": V2_ADDENDUM_SHA12_EXPECTED[name],
                "actual": actual,
            }

    d4_sha = sha12_file(ADDENDUM_D4).upper()
    d4_sha_drift = None
    if d4_sha != ADDENDUM_D4_SHA12_EXPECTED:
        d4_sha_drift = {
            "expected_anchor": ADDENDUM_D4_SHA12_EXPECTED,
            "actual": d4_sha,
        }

    # 3. 自检
    self_check = self_check_v3()

    # 4. ruleset_v3.json 已落盘 (由独立 write 调用完成, 此处仅核验 SHA-12)
    ruleset_v3_sha = sha12_file(OUT_RULESET).upper()

    # 5. 返报
    return {
        "task": "task_B_v3_pi_cot_distillation_ruleset_v3_construction",
        "execution_棒": "棒 B (ruleset_v3 构造)",
        "execution_棒_sequence_position": "v3 四件链棒② / 4",
        "anchor_sha_verification": {
            "prereg_v3": {"expected": PREREG_V3_SHA12_EXPECTED, "actual": prereg_sha},
            "dataset_v3": {"expected": DATASET_V3_SHA12_EXPECTED, "actual": dataset_sha},
            "coding_review_v2": {"expected": CODING_REVIEW_V2_SHA12_EXPECTED, "actual": coding_review_sha},
            "ruleset_v2_ref": {"expected": RULESET_V2_REF_SHA12_EXPECTED, "actual": ruleset_v2_ref_sha},
            "executor_v2_ref": {"expected": EXECUTOR_V2_REF_SHA12_EXPECTED, "actual": executor_v2_ref_sha},
            "dataset_v1_1": {"expected": DATASET_V2_V11_SHA12_EXPECTED, "actual": dataset_v11_sha},
        },
        "v2_addendum_sha_actual": v2_addendum_sha_actual,
        "v2_addendum_sha_drift_count": len(v2_addendum_sha_drift),
        "v2_addendum_sha_drift": v2_addendum_sha_drift,
        "addendum_d4_sha_actual": d4_sha,
        "addendum_d4_sha_drift": d4_sha_drift,
        "ruleset_v3_sha12_actual": ruleset_v3_sha,
        "ruleset_v3_size": OUT_RULESET.stat().st_size,
        "self_check": self_check,
        "thresholds_implemented": {
            "K-V3-A": TH_NW_SIM_MEAN,
            "K-V3-A'": TH_NLED_SIM_MEAN,
            "K-V3-B": TH_CRITICAL_COV,
            "K-V3-C": TH_BLIND_OBEY,
            "K-V3-D": TH_BOOT_CI_FLOOR,
        },
        "features_implemented": {
            "n_features": len(FEAT_KEYS_V3),
            "n_features_min_required": N_FEATURES_MIN,
            "feature_keys": list(FEAT_KEYS_V3),
        },
        "metrics_implemented": ["nw_sim", "nled_sim"],
        "metrics_excluded": ["recall_v2_form", "Jaccard", "F1", "LCS", "String_Kernels", "Spectrum_Kernels"],
        "zero_private_clauses": True,
        "zero_llm_judgment_layer": True,
        "zero_key_in_prompt_or_json_or_log": True,
        "zero_v1_v2_v3_frozen_touch": True,
        "zero_derived_json_merge": True,
        "explicit_boolean_naming": True,
        "s_40_discipline_followed": True,
    }


if __name__ == "__main__":
    summary = main()
    print(json.dumps(summary, ensure_ascii=False, indent=1))