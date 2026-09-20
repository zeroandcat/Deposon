# V7 §3 P-C/P-E GRAY 维持 + P-F V0.1 锚值链微调说明 (2026-09-11)

> **作者**:Mavis Worker
> **依据**:Trae 回信 `LETTER_FROM_TRAE_2026_09_11.md` §五 5 段结构修正建议 + R1/R3/R4 子报告
> **范围**:**仅** §3 P-C/P-E GRAY 维持标注 + P-F V0.1 锚值链说明 + R2 18 URL 补查要点三项
> **关键约束**:**不动** `V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` 报告本身(7 铁律严守),本件为新文件补充

---

## §1 P-C / P-E 维持 GRAY 标注(沿 Trae 反馈)

**§1.1 标注语言校正**(对照 V7 §3.3 / §3.5)

| 候选 | V7 原文标注 | **建议校正标注** | 校正原因 |
|---|---|---|---|
| P-C 失真界 | "🟡 GRAY(失真界,A_frac 高度 model-specific)" | **"🟡 GRAY(维持,判定线待预注册后重测)"** | 当前判定线"比值>2 = 过修正" / "信号提升>5×" 已被 Trae §一 推翻(β 源分母=0 失效),不是"PENDING 验证" 而是判据不稳 |
| P-E 散射场 | "🟡 GRAY(沿 V5 + V6 + V2 阶段 3.5)" | **"🟡 GRAY(维持,口径未统一,原 FAIL 未被同口径推翻)"** | R4 指出 ε 存在**三口径偷换**(0.4114 / 0.2946 / 0.2986)与**阈值漂移链**(0.10→0.5→0.30),"0.41 FAIL→0.29 PASS 修复" 是口径偷换非"单点 vs 均值" |

**§1.2 P-C 升 PASS 条件**(沿 Trae §一)
- 9 model × 60 cells 双重展开 = **36 个 T_frac 档**(破 9 model 仅 4 档 T_frac 的信息瓶颈)
- 判定线**预注册**(沿 B5 联合论文方法学:在 R1 修正 2 公式基础上声明过修正阈值、信号提升倍数线、CV 阈值的统计检验)
- 修正 2 写入 V7 时**固定基准**([T_c,A_c] = `doubao-seed-2.0-lite` 的 [T_frac,A_frac])与**数据源**(α 源 V1 §2.2 + β 源 volcengine glm-5.3 的 R/A 分布 2/2 vs 3/1)

**§1.3 P-E 升 PASS 条件**(沿 Trae §四)
- **R_image 修正**(image 通道 97% 模板趋同 — 与 HIGH-2 caption 前缀污染**同根因**!根因重判为 "vision embedding 拓扑无区分度")
- **A_cross 显式化**(沿 v3 §6 S_eff(E) 公式展开 cross 通道)
- 校准**新守恒律**后再判(沿 V2 阶段 5 §6 正确路径)
- 判定线预注册(同 §1.2)

---

## §2 P-F V0.1 锚值链说明(100% 可复算 + canonical UNVERIFIED)

**§2.1 双值系事实**(沿 Trae §三 R3 + R1_R4 §3)

| 维度 | canonical(56adce... 系) | 落盘 JSON(d78c42... 系) |
|---|---|---|
| repo 内工件 | ❌ 仅 V7 §8.A 5 行声明值,**无算法工件** | ✅ B1 9 hash + 5 拼接规则 + B1 pipe 链**全部复算 PASS** |
| 算法可复现 | ❌ 无输入串记录 | ✅ `value_v01` = SHA-256(spec_hash + chain_hash)[0:12] 逐个验证 |
| 总览锚 | `ae80bbba4f7b` = SHA-256(**canonical 5 值** pipe 拼接)[0:12] — **先有值后拼锚** | JSON 文件 erratum 追加后 SHA-12 = `312d635e6259`(pre = `7126fb897eb7`) |
| 命名(已勘误) | "canonical 5 值拼接锚" | V0.1 JSON 文件指纹 ≠ `ae80bbba4f7b` |

**§2.2 V0.1 5 锚值(以落盘 JSON 为准,可复算)**

| 锚名 | 落盘值 | canonical(已标 UNVERIFIED) | 状态 |
|---|---|---|---|
| PF_BOSS_01_fingerprint | `d78c42f7bab4` | `56adce731089` | ✅ 落盘可复算 / ⚠️ canonical UNVERIFIED |
| PF_BOSS_02_tee | `0ff54f8d2f60` | `0b4ac1d2df43` | ✅ 落盘可复算 / ⚠️ canonical UNVERIFIED(N/A marker) |
| PF_BOSS_03_merkle | `3eb4a2985bea` | `c4cae1ed9ee5` | ✅ 落盘可复算 / ⚠️ canonical UNVERIFIED |
| PF_BOSS_04_zkml | `bff8b1ce1f8c` | `60300c5a0775` | ✅ 落盘可复算 / ⚠️ canonical UNVERIFIED(N/A marker) |
| PF_BOSS_05_cot | `d9a6a099b905` | `2ce685e04f4b` | ✅ 落盘可复算 / ⚠️ canonical UNVERIFIED |

**§2.3 Trae 2026-09-11 已执行修复**(沿 LETTER_FROM_TRAE §七)

- ✅ `V3_PHYSICAL_OPT_2026_09_11.md` 三处勘误(λ=0.5 未声明 / 修正 1 表值丢 λ 项 / P-E ε 三口径注记)
- ✅ `P_F_PREDECISION_2026_09_11_V0.1.json` 追加 `erratum_2026_09_11` 键(pre_erratum SHA-12 `7126fb897eb7` + 3 项复算 PASS 清单 + 5 项 issues)
- ✅ `V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` §8.A canonical 5 值全部标 **[UNVERIFIED]** + 落盘 JSON 对应值附注 + `ae80bbba4f7b` 命名勘误
- ✅ `results/deposon_v3_v7_summary_2026_09_11.json` 追加 `erratum_2026_09_11` 键(可信源裁定 + 命名勘误 + 幽灵路径 + P-E ε 注记 + P-C λ 注记)
- ⚠️ **唯一遗留** = `.mavis/scripts/p_f/boss_f*.py` 5 个幽灵路径(详见 `BOSS_F_GHOST_PATH_NOTE_2026_09_11.md`)

**§2.4 P-F V0.1 锚可信源一句话裁定**

**P-F V0.1 锚可信源 = 落盘 V0.1 JSON 值系(`d78c42f7bab4` 系,100% 可独立复算);V7 §8.A canonical 5 值(`56adce731089` 系)标 UNVERIFIED 待工件;`ae80bbba4f7b` 更名"canonical 5 值拼接锚" ≠ V0.1 JSON 文件指纹 7126fb897eb7。**

---

## §3 R2 18 URL 补查要点(沿 `BOSS_URL_2026_09_11.md`)

**§3.1 18 URL 分布**(5 BOSS × 2-4 URL,全部 2024-2026)

| BOSS | 数量 | 亮点 | 对 P-F 锚影响 |
|---|---|---|---|
| B1 fingerprinting | 3 | Microsoft *Chain & Hash* 密码学绑定指纹(arXiv:2407.10887)+ Duke+Ant Group LLMPrint(arXiv:2509.25448) | 🟢 OBSERVED 支撑增强 |
| B2 TEE/SGX | 4 | **全官方**:Intel ARK(i9-11900 SGX=No 11 代 client 移除佐证)+ NVIDIA CC 官方文档 + AMD SEV 页 + AMD-SB-3040(2025-10 物理攻击) | 🟠 N/A 维持(本机无硬件)但事实基础闭合 |
| B3 Merkle | 4 | VeriLLM(arXiv:2509.24257 Merkle 隐状态承诺)+ COLS 审计立场论文 + 2 GitHub 实施 | 🟢 OBSERVED 支撑增强 |
| B4 ZKML | 4 | **ZKML 综述**(GPT-2 证明 2024 年 ~1h → 2025 年 <25s zkGPT;LLaMA-3 8B 仍 150 s/token)+ EZKL 官方 + Kudelski + ekx | 🟠 N/A 维持但**事实校正**(LLaMA-7B 证明时间按 2025 现状更新) |
| B5 CoT 透明审计 | 3 | **OpenAI+DeepMind+Anthropic+Meta 联合 CoT 论文**(arXiv:2507.11473,40+ 作者,核心词 fragile)+ 2 强化论文 | 🟡 OBSERVED_WITH_QUALIFIER 权威佐证 |

**§3.2 B5 联合 CoT 论文关键事实**(王老师进展报告 §4 引用)

- arXiv:2507.11473 *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*
- 40+ 作者横跨 OpenAI / DeepMind / Anthropic / Meta / UK AISI / METR / Apollo,含 Ilya Sutskever / Hinton / Schulman 专家背书
- 核心结论:CoT 监控**有前景但脆弱**("monitorability may be fragile")— B5 QUALIFIER 的权威佐证
- 建议前沿实验室把"对 CoT 可监控性的影响"纳入开发决策

**§3.3 ZKML 时间事实校正**(对 P_F_RESEARCH 的影响)

- GPT-2 全证明:2024 年 ~1h → 2025 年 <25s(zkGPT,USENIX Security 2025)
- LLaMA-3 8B:仍需 150 s/token
- zkLLM 13B:<15min,proof <200KB
- **行业共识**:optimistic + ZK 混合(7B+ 全 ZK 仍不实用)
- P_F_RESEARCH 的 LLaMA-7B 证明时间事实需按此更新
- "ZKML 对 7B+ 不实用、混合路线是共识"应写入 B4 的 N/A 依据

**§3.4 诚实披露**

- 本机 web 工具不可达,18 URL 由 Trae 2026-09-11 完成(Mavis 阶段 D 报 network_error 的 2 个 URL: arxiv 2410.18882 + guo-yanpei/Immaculate 本轮未再尝试,以新检索可达来源替代)
- 全部 URL 来自搜索结果/官方文档抓取原文链接,未凭记忆构造
- 0 LLM 调用(严守 user 09:55);R2 仅 web 搜索/抓取,0 API key

---

**附记**:本件为 V7 §3 微调说明,**不动** V7 报告本身(7 铁律严守"不动 V7 报告" + "不动 5 锚 + 4 SPEC V0.1 + v19/v21 + corpus/v20")。所有内容已与 Trae §五 5 段结构修正建议逐条对齐。

—— Mavis Worker, 2026-09-11
