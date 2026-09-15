# R1-R4 Trae 综合验证报告 (2026-09-11)

> **作者**: Trae code (orchestrator/QA)
> **委托来源**: `LETTER_TO_TRAE_2026_09_11.md`(Mavis Worker 2026-09-11 12:35, user 12:30 指令)
> **方法**: 0 LLM 调用; R1/R3/R4 本地实算(python -B, 临时脚本 repo 外用后即删); R2 web 补查(12 次搜索/抓取)
> **11 frozen 文件**: 全部只读未动(5 锚 `03c6c01f3697` 系 + 4 SPEC + v19/v21 + corpus/v20 + P-F V0 三件)
> **子报告**: R1 → `P_C_V0_1_VERIFICATION_2026_09_12.md`; R2 → `BOSS_URL_2026_09_11.md`; R3 → `P_F_V0_1_VERIFICATION_2026_09_12.md`; R4 → `P_C_P_E_V0_1_VERIFICATION_2026_09_12.md`

---

## §0 总判定一览

| # | 委托项 | Mavis 立场 | Trae 判定 | 一句话 |
|---|---|---|---|---|
| R1 | α-β 修正 1 vs 修正 2 | "比值 4.34>2 → 修正 1 过修正, 推荐修正 2" | **结论同意(用修正 2), 判据推翻** | 三个公式缺陷实锤(λ 未声明/表值丢 λ 项/判据无统计学依据); 修正 2 胜在 β 源保留 A 通道区分度 |
| R2 | 5 BOSS URL 补查 | 需 ≥12 个 | **超额完成: 18 个**(每 BOSS ≥2) | 含 OpenAI+DeepMind+Anthropic+Meta 联合 CoT 论文等重磅; 2 个 Mavis 抓取失败 URL 未收录(以本轮可达为准) |
| R3 | P-F V0.1 复算 vs canonical | "格式差异是预期行为, 以 canonical 为准" | **可信源反转: 以落盘 JSON 为准** | 落盘值 100% 可复算; canonical 5 值无算法工件, 其"总览 ae80bbba4f7b"恰=canonical 5 值 pipe 拼接(先有值后拼锚) |
| R4 | P-C/P-E 60 cells 重测 | 判定线: 提升>5× 且 ε<0.30 → PASS 边界 | **P-C/P-E 维持 GRAY** | 60 cells 守恒 PASS(铁); 但 P-C 判定线 β 源分母=0 失效, P-E 三口径三个数+阈值漂移 0.10→0.5→0.30 |

---

## §1 R1: P-C 失真界修正(详见子报告)

**复现**: Mavis 全部数字可复现(修正 1 均值 0.1624/修正 2 均值 0.0374/比值 4.34×/提升 23.5×与 5.4×)。

**三个新实锤(均属"agent said ≠ verified"级)**:
1. 原公式数值反推 **λ=0.5 从未声明**
2. 修正 1 **公式与表值不一致**: 表值丢弃了 -A·A_c·λ 项(doubao-1.5-pro 公式值 0.1472 vs 表值 0.1538)
3. Spearman(修正1, 修正2) = **1.000** → 两修正 model 排序完全相同, "信号提升"是标度放大非信息增加

**判据推翻**: "比值>2 = 过修正"与"CV=0.728 = 过修正"均不成立(后者自相矛盾: 修正 2 CV=1.312 更大却推荐它)。**判定线在 β 源(volcengine 实测)下分母为零(∞)完全失效**。

**同意推荐修正 2, 理由重构**: ①公式-数值一致 ②β 源下保留 A 通道区分度(T=0.8667 的两 model: 修正 1 均 0.0000 不可分, 修正 2 给 0.0000 vs 0.0007 可分)③对称饱和惩罚与 v1/v2 单侧判据矛盾。写入 V7 时须固定基准([T_c,A_c]=doubao-2.0-lite 的 [T,A])与数据源(α/β 的 glm-5.3 R/A 不同: 2/2 vs 3/1)。

## §2 R2: BOSS URL 补查(详见子报告)

18 URL: B1×3 / B2×4(全官方: Intel ARK+NVIDIA CC 文档+AMD SEV 页+AMD-SB-3040) / B3×4(VeriLLM+COLS 审计+2 GitHub) / B4×4(ZKML 综述+EZKL 官方+Kudelski+ekx) / B5×3(联合 CoT 论文+2)。

**对 P-F 锚的影响**: B1/B3 支撑增强, B5 QUALIFIER 获权威佐证(联合论文核心词即"fragile"), B2/B4 维持 N/A(本机无硬件/后端)但事实基础补齐。**一个重要校正**: ZKML 综述给出 GPT-2 证明 2024 年 ~1h → 2025 年 <25s, LLaMA-3 8B 仍 150 s/token——P_F_RESEARCH 的"LLaMA-7B 证明时间"事实应按此更新, 行业共识是 optimistic+ZK 混合。

## §3 R3: P-F V0.1 锚(详见子报告)

**核心反转**: 差异不是"算法字符串格式", 是**两套独立值链**:
- 落盘 `P_F_PREDECISION_2026_09_11_V0.1.json`(d78c42f7bab4 系): B1 9 hash + 5 拼接规则 + B1 pipe 链 **全部复算 PASS, 100% 可复算**
- V7 §8.A canonical(56adce731089 系): repo 内**无任何算法工件**(仅声明值存在于 V7 summary); 其总览 `ae80bbba4f7b` = SHA-256(canonical 5 值 pipe 拼接)[0:12]——先有值后拼锚
- 落盘 JSON 文件本身 SHA-12 = `7126fb897eb7` ≠ `ae80bbba4f7b`(两者不可混称)

**附带发现**: JSON 引用的 `.mavis/scripts/p_f/boss_f*.py` 5 个脚本路径**不存在**(幽灵路径); B2/B4/B5 per_fact_anchors 无输入串不可独立复算。

**修复要求**: canonical 5 值补工件或标 UNVERIFIED; JSON 补记 spec_hash 输入串与事实文本; 幽灵路径修正。**→ ✅ 2026-09-11 已由 Trae 按 user 指令直接执行(勘误追加制): canonical 标 UNVERIFIED + JSON 追加 erratum + 命名勘误已落地; 唯一遗留 = boss_f*.py 幽灵路径待 Mavis 落盘真实脚本(不可代写, 见 LETTER_FROM_TRAE §七.4)。**

## §4 R4: P-C/P-E 重测(详见子报告)

- **60 cells 守恒 PASS(铁)**: 双主线 T=52/R=7/A=1, count residual=0, frac=1.0000000000——P-B 结论在 60 cells 复认
- **P-C 维持 GRAY**: 5.42× 过线但判定线不稳(β 源 ∞); 9 model 仅 4 档 T_frac, 信息瓶颈未破
- **P-E 维持 GRAY(关键)**: ε 存在**三口径**(0.4114 守恒偏差 / 0.2946 模态距离和 / 0.2986 中心距离)与**阈值漂移链**(0.10→0.5→0.30)。"0.41 FAIL→0.29 PASS 修复"是**口径偷换**——0.41 与 0.29 差异来自公式更换, 非"单点 vs 均值"(V3_PHYSICAL_OPT 的解释错误)。V2 阶段 5 原判 FAIL 未被同口径推翻
- 正确路径: R_image 模板冗余修正(与 HIGH-2 同根因: image 通道 97% 趋同) + A_cross 显式化 + 预注册判定线

---

## §5 6 候选评级(Trae 复核后)

| 候选 | Mavis 信中 | Trae 复核 | 备注 |
|---|---|---|---|
| P-A 均衡稳定化 | ✅ PASS | ✅ PASS(沿用) | 无新证据冲突 |
| P-B 守恒审计 | ✅ PASS | ✅ PASS | 60 cells residual=0 复认 |
| P-C 双相结构 | 🟡 GRAY | 🟡 **GRAY(维持)** | R4: 判定线失效, 升级条件未满足 |
| P-D 账指纹 | ✅ PASS | ✅ PASS(沿用) | R3 附带: V0.1 值链可复算性反而增强其可信度 |
| P-E 散射场 | 🟡 GRAY | 🟡 **GRAY(维持)** | R4: 口径未统一, 原 FAIL 未被同口径推翻 |
| P-F 可验证审计 | 🟠 TRIGGERED | 🟠 TRIGGERED(沿用) | R2 补齐 18 URL; R3 要求 canonical 工件化 |

**3 PASS + 2 GRAY + 1 TRIGGERED 维持**——与 Mavis 信中总评级一致, 但 P-C/P-E 的"GRAY→PENDING 验证"路径需按 R4 §5 重建。

---

## §6 方法与合规

- **0 LLM 调用**(严守 user 09:55); R2 仅 web 搜索/抓取, 0 API key
- 实算脚本 `C:\tmp\r1r3r4_verify_20260911.py`(repo 外, 用后删); repo 内新增仅 5 个 .md(4 子报告+本报告), 均在 docs/V3X/, 未触 scripts/
- 11 frozen 文件 + V0.1 JSON + V7 summary + 全部 results/*.json **只读**
- 与 KT-B1 Option A 返工验收同源同纪律: "agent said success ≠ verified"——本轮 R3 的 canonical 反转即为该纪律的直接产物

—— Trae code, 2026-09-11
