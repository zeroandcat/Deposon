# COZE 项目进展报告需求文档(Deposon V3X)

- **文档 ID**:`COZE_PROJECT_PROGRESS_REQUIREMENTS_2026_09_11`
- **生成时间**:2026-09-11 14:00(CST)
- **目标读者**:coze 委托人(由 user 委托撰写综合报告)
- **撰写方**:Mavis worker 子代理(0 LLM,纯文本编辑,沿 7 铁律)
- **沿用源文件 SHA-12**:`03C6C01F3697`(5 锚 JSON)

---

## §1 报告目标

### 1.1 目标受众
1. **coze 委托人**(user 委托 coze 撰写综合报告)
2. **Deposon 项目组内部**(沿 v3 提案格式标准)

### 1.2 报告类型
Deposon V3X 1 周判死承诺后**项目综合进展报告**(中文 PDF)。

### 1.3 报告目的
诚实记录 Deposon V3X 项目**真实 2 周工作量**:
- 4 资产(锚定 JSON + 冻结 SHA + 9 model × 30 cells 实算 + 4 候选 V0.1 SPEC)
- 9 model × 30 cells 守恒(沿 v3 §6 物理公式)
- 9 model × 60 cells 物理公式 540/540 PASS
- 6 候选 P-A/B/C/D/E/F 综合评级(3 PASS + 2 GRAY + 1 TRIGGERED)
- 7 铁律严守(0 LLM / 不动 11 frozen / 不设 proxy / key 不入盘)

### 1.4 报告禁区(硬约束)
- **不写任何外部合作人**(user 2026-09-11 13:59 明确要求,聚焦项目进展)
- **不写王老师** / **不写 WeChat 顾问** / **不写 6 月合作**
- 仅呈现项目内部资产、实算数据、判死结论、剩余风险

---

## §2 报告要求

### 2.1 内容范围
- **真实 2 周工作量**(2026-09-04 → 2026-09-11):
  - Phase A:4 候选 V0.1 SPEC(P-A / P-B / P-C / P-D)起草
  - Phase B:4 候选 P0.1 验证(2 PASS + 2 GRAY)
  - Phase C:9 model × 30 cells 火山方舟实测(Worker A/B/C/D)
  - Phase D:60 cells 沿 v3 §6 物理公式守恒 540/540
  - Phase E:P-E 加入 GRAY 边界 / P-F 1 周判死承诺
  - Phase F:RAG 三次证伪 / B5 联合 CoT 论文
  - Phase G:5 锚冻结 SHA-12 = `03C6C01F3697` / V7 综合报告 / R1-R4 修
- **6 候选 P-A/B/C/D/E/F 综合评级**:
  - P-A:PASS(沿 v3 §6 物理公式)
  - P-B:PASS(60 cells 沿 v3 §6)
  - P-C:GRAY(V7 §3 P_C P_E GRAY NOTE 2026-09-11 解释)
  - P-D:PASS(Distortion Bound)
  - P-E:GRAY(同上)
  - P-F:TRIGGERED(1 周判死,user 主动 trigger 撤销 1/5 FAIL)

### 2.2 格式要求
- **中文 PDF**(中文系统生成,中易雅黑 msyh.ttc)
- **1 页 A4**(微信友好版,3-5 KB) + **5-10 页综合报告**(详细版,5-10 KB)
- **强度声明前置**:判死级 / 观察性 / 探索性 3 档纪律(沿 v3 提案 §1)

### 2.3 风格要求
- **沿 v3 提案格式**(V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md + V3_PHYSICAL_OPT_2026_09_11.md)
- **数字溯源**:全部数字附 JSON 字段路径,无手写数字
- **沿用 5 锚 JSON**:`03C6C01F3697`,SHA-12 验证 0 触动
- **诚实风险**:4 个剩余风险老实承认,不留口头兜底

---

## §3 数据来源(16 个只读文件 + 4 张实算表)

### 3.1 11 个 frozen 文件(严守不动,SHA-12 实算已验证)

| # | 文件 | 路径 | SHA-12(已验) | 字节 |
|---|------|------|--------------|------|
| 1 | 5 锚 JSON | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03C6C01F3697` ✓ | 6680 |
| 2 | P_F_PREDECISION V0 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `B41C98BF90CC` | 3680 |
| 3 | P_F_PREDECISION V0.1 | `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` | `312D635E6259` | 12498 |
| 4 | KT_A1_SPEC_V0.1 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `78B71D404366` | 29570 |
| 5 | KT_B1_SPEC_V0.1 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410CA0FBDAE` | 35688 |
| 6 | KT_C1_SPEC_V0.1 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `59D8F56347D5` | 31241 |
| 7 | KT_D0_SPEC_V0.1 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `CCE8E9A1B00E` | 20927 |
| 8 | V2 Phase 2+3 合并(v19) | `docs/V3X/V2_PHASE2_3_INTEGRATION_2026_09_11.md` | `8178E61E7C97` | 11678 |
| 9 | v20 run1 | `verifier/runs/v20_run1.md` | `41D3D7F4A148` | 295 |
| 10 | v21 run1 | `verifier/runs/v21_run1.md` | `36B69E195F06` | 247 |
| 11 | v21 run2 | `verifier/runs/v21_run2.md` | `3246C7D46480` | 448 |

> **5 锚 JSON 沿用 `03C6C01F3697`**,与 P-F PREDECISION V0.1 (312D635E6259) 并存。coze 不可触动 11 frozen 文件。

### 3.2 5 份新报告(只读参考)

| # | 文件 | SHA-12(已验) | 字节 | 作用 |
|---|------|--------------|------|------|
| 1 | `PROGRESS_REPORT_WANG_2026_09_11.pdf` | `60C32843D84B` | 147916 | 中文字体 + 1 页 A4 版式参考 |
| 2 | `WANG_TEACHER_PROGRESS_REPORT_2026_09_11.md` | `7BBB557C99D3` | 6770 | 已有进度报告(不写入新报告) |
| 3 | `V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | `54FFD2F400D1` | 37929 | V7 综合报告(沿 v3 提案格式) |
| 4 | `R1_R4_TRAE_REPORT_2026_09_11.md` | `7B79AE4E947D` | 6776 | Trae 修 4 剩余风险(R1-R4) |
| 5 | `V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | `F80CC4E1FB7F` | 7344 | P-C/P-E GRAY 边界解释 |

> coze 撰写新报告时**只读不写**这 5 份文件。综合进展报告应**整合** 5 份内容,但**不复制粘贴**。

### 3.3 4 worker JSON + 1 总 JSON(9 model × 30 cells 实算)

| # | 文件 | SHA-12(已验) | 字节 | 作用 |
|---|------|--------------|------|------|
| 1 | Worker A 报告 | `C073741329EE` | 4869 | doubao-seed-2.0-lite 完整 + kimi 部分 |
| 2 | Worker B 报告 | `726E7A3F4EA0` | 8078 | deepseek / glm 实测 |
| 3 | Worker C 报告 | `68267B7849EE` | 9545 | doubao-seed-2.1-turbo 实测 |
| 4 | Worker D 报告 | `E3EFD17C1ED1` | 6239 | minimax-m3 / evolving 实测 |
| 5 | 总 JSON | `3871EADAA3A0` | 4893 | 9 model 数据汇总(best = doubao-seed-2.0-lite 26/30 = 86.7%) |

### 3.4 4 张实算表(coze 需自行用已有数据重算,0 LLM)

1. **9 model × 30 cells T/R/A 表**(沿 v3 §6 物理公式,Tolerance + Retention + Accuracy 三档)
2. **9 model × 60 cells 守恒表**(Feshbach 共振 + Lindblad ρ(t) + T+R+A 守恒,540/540 PASS)
3. **36 T_frac 档判定线表**(P-A/P-B 沿 v3 §6 的判定线,P-C/P-E GRAY 解释)
4. **5 锚 SHA-12 验证表**(沿用 `03C6C01F3697`,11 frozen 文件 0 触动)

---

## §4 报告章节结构(8 节正文 + 5 附录)

### 4.1 §1 标题 + 强度声明 + 署名
- 标题:Deposon V3X 1 周判死承诺后项目综合进展报告
- 强度声明前置:
  - 判死级(P-A / P-B / P-D PASS + 9 model × 60 cells 守恒 540/540)
  - 观察性(P-C / P-E GRAY 边界)
  - 探索性(P-F 1 周判死,user 主动 trigger 撤销 1/5 FAIL)
- 署名:Deposon 项目组(2026-09-11),不写外部合作人

### 4.2 §2 4 资产 + 1 周判死承诺 + 9 model × 60 cells 守恒
- **4 资产清单**:
  1. 锚定 JSON:5 锚 SHA-12 = `03C6C01F3697`
  2. 冻结 SHA:11 frozen 文件 SHA-12 表
  3. 9 model × 30 cells 实算数据(Worker A/B/C/D + 总 JSON)
  4. 4 候选 V0.1 SPEC(KT_A1/B1/C1/D0_SPEC_V0.1)
- **1 周判死承诺**:D7 → D14 窗口,user 主动 trigger
- **9 model × 60 cells 守恒 540/540**:沿 v3 §6 物理公式

### 4.3 §3 6 候选 P-A/B/C/D/E/F 综合评级

| 候选 | 评级 | 关键证据 |
|------|------|----------|
| P-A | **PASS**(判死级) | 60 cells 沿 v3 §6 物理公式 |
| P-B | **PASS**(判死级) | 60 cells 沿 v3 §6 |
| P-C | **GRAY**(观察性) | V7 §3 P_C P_E GRAY NOTE:α-β 模板冗余过修正 |
| P-D | **PASS**(判死级) | Distortion Bound 9 model × 30 cells |
| P-E | **GRAY**(观察性) | ε 三口径偷换(Douban embedding 跨域) |
| P-F | **TRIGGERED**(探索性) | 1 周判死,user 主动 trigger 撤销 1/5 FAIL |

### 4.4 §4 RAG 三次证伪 + B5 联合 CoT 论文
- **RAG 三次证伪**:
  - 跨域检索 + 模板前缀主导 NOISE(V1 解释)
  - 9 model × 30 cells RAG 变体对比(no-RAG 86.7% 最佳)
- **B5 联合 CoT 论文**:OpenAI + DeepMind + Anthropic + Meta 四机构联合 CoT 论文佐证
- **final claim**:no-RAG 86.7% 是 9 model 30 cells 实算 final,但未沿 v3 §6 物理公式解释(剩余风险)

### 4.5 §5 D7 交付工件包
- 5 锚 JSON(SHA-12 = `03C6C01F3697`)
- 11 frozen 文件 SHA-12 表
- 9 model × 30 cells 总 JSON
- 4 候选 V0.1 SPEC
- P-F PREDECISION V0.1 JSON

### 4.6 §6 Trae 修 4 剩余风险(R1-R4)
- **R1**:canonical 5 值工件缺失(V7 §8.A 与落盘 JSON 两套值链)
- **R2**:BOSS URL 12 个待补查(本机 web 不可达,Trae 18 URL 已超额)
- **R3**:α-β 判定线不稳(P-C GRAY)
- **R4**:ε 三口径偷换(P-E GRAY)
- **11 frozen 文件 0 触动**:Trae 修不可动 11 frozen

### 4.7 §7 后续 3 路径选择
- **路径 1**:继续 P-A(已 PASS,扩展数据集)
- **路径 2**:V7 §3 微调(P-C/P-E 修 α-β / ε 判定线)
- **路径 3**:沿 v3 §6 物理优化(60 cells 守恒 540/540 已稳定)
- **路径 4**:P-F 1 周判死(user 主动 trigger 撤销 1/5 FAIL)
- **建议**:沿用 v3 提案 3 路径,coze 在 §7 列表呈现 4 选项,user 决定

### 4.8 §8 项目组署名(2026-09-11)
- 仅 Deposon 项目组
- 不写外部合作人(硬约束)

### 4.9 5 附录(沿 v3 提案格式)
- **附录 A**:数字溯源表(5 锚 + 9 model × 60 cells 数据)
- **附录 B**:6 候选评级表(沿 §3)
- **附录 C**:RAG 三次证伪 + 6 候选最终 verdict
- **附录 D**:11 frozen 文件 SHA-12 验证
- **附录 E**:4 个诚实风险(R1-R4 详解)

---

## §5 当前质量缺陷(用户对前报告不满意,16 缺陷)

> coze 撰写时**必须避免**这 16 个缺陷。

### A. 结构与逻辑(4)
1. **依赖口头交付**:前报告均以 worker 内部"老实承认"/"诚实披露"段落兜底,缺乏系统化交付链路。→ **改进**:沿 v3 提案 8 节 + 5 附录结构。
2. **RAG 收口未与 v3 §6 物理公式对齐**:no-RAG 86.7% 是 final claim,但未沿 Feshbach S_eff / Lindblad ρ(t) 解释机制。→ **改进**:§4 必须沿 v3 §6 物理公式解释。
3. **P-C/P-E GRAY 判定线不稳**:α-β 模板冗余过修正 / ε 三口径偷换。→ **改进**:V7 §3 P_C P_E GRAY NOTE 整合到 §3 / 附录 C。
4. **P-F 启动条件依赖 user 主动 trigger**:撤销硬性规则,缺乏自动启动机制。→ **改进**:§3 标注 "TRIGGERED" + §7 列路径 4。

### B. 数据与证据(4)
5. **5 锚 JSON SHA-12 验证重复多次**:每个 worker 都验证一次,缺乏 single source of truth。→ **改进**:附录 D 只列 11 frozen 文件 SHA-12(本需求文档已实算 11 SHA-12,coze 直接引用)。
6. **canonical 5 值工件缺失**:V7 §8.A 与落盘 JSON 两套值链,无算法工件。→ **改进**:§5 / 附录 E 老实承认,列为 R1 风险。
7. **BOSS URL 12 个待补查**:本机 web 不可达,Trae 18 URL 已超额。→ **改进**:§6 / 附录 E 老实承认 R2 风险,需 user 派外网子代理。
8. **RAG 三次证伪边界**:"跨域检索 + 模板前缀主导 NOISE"是 V1 解释,不是 v3 §6 物理机制。→ **改进**:§4 标注 V1 解释,final claim 沿 v3 §6 重述。

### C. 工作流与协作(4)
9. **deposon 5 worker 并发 60 cells 沿 V2 阶段 2**:无独立 9 model × 30 cells 重算。→ **改进**:§2 列 4 worker JSON(Worker A/B/C/D) + 总 JSON。
10. **LLM 调用边界不严**:0 LLM 是 worker 老实声明,不是规则化。→ **改进**:§7 严守约束明文:"0 LLM,coze 沿用已有数据实算"。
11. **BOSS 测法 verifier 边界不严**:Trae 5 BOSS 测评 18 URL 是"观测",不是"定理"。→ **改进**:§6 / 附录 E 老实承认 R2 风险。
12. **R1-R4 4 个剩余风险**无系统性修复路径。→ **改进**:§6 列 4 风险,§7 后续路径对应风险。

### D. 报告呈现(4)
13. **文件大小溢出**:多次报告超 user 设定目标 1.3-3×。→ **改进**:§6 严守"1 页 A4(3-5 KB)+ 综合(5-10 KB)"。
14. **3 PASS + 2 GRAY + 1 TRIGGERED 评级** 沿用,但 P-C/P-E 仍是 GRAY 边界。→ **改进**:§3 评级表,附录 C verdict 表。
15. **诚实承认段落过多**:worker 报告"风险"和"Blockers"占大半,正面结论不够显眼。→ **改进**:§2 / §3 / §4 正面结论前置,§6 / 附录 E 风险后置。
16. **项目进展时间线不清**:D0-D7 时间表散落各报告。→ **改进**:整合到 §2 / 附录 A(沿 v3 提案附录 C 时间表)。

---

## §6 报告质量要求(17 条)

| # | 要求 | 验证方式 |
|---|------|----------|
| 1 | 总长度:1 页 A4(3-5 KB)+ 综合 5-10 KB | 字节计数 |
| 2 | 结构:8 节正文 + 5 附录(沿 v3 提案) | 章节 grep |
| 3 | 判死级 / 观察性 / 探索性 3 档纪律前置 | §1 强度声明 |
| 4 | 数字溯源:全部数字附 JSON 字段路径 | 附录 A 数字溯源表 |
| 5 | 5 锚 JSON 沿用 `03C6C01F3697` | 附录 D SHA-12 |
| 6 | 6 候选评级:3 PASS + 2 GRAY + 1 TRIGGERED | §3 + 附录 B |
| 7 | RAG 三次证伪 + B5 联合 CoT 论文 | §4 + 附录 C |
| 8 | v3 §6 物理公式沿用:Feshbach / Lindblad / T+R+A | §2 + §4 |
| 9 | 9 model × 60 cells 守恒 540/540 | §2 + 附录 A |
| 10 | P-F 1 周判死 + 撤销 1/5 FAIL | §3 + §7 路径 4 |
| 11 | 诚实 4 个风险(R1-R4) | §6 + 附录 E |
| 12 | 3 张深蓝表头表(数字溯源 / 6 候选 / RAG 证伪) | 沿 v3 提案 |
| 13 | 沿 v3 提案分档强度声明 | §1 前置 |
| 14 | **不写王老师**(user 明确要求) | §1 报告禁区 |
| 15 | 0 LLM 严守,数字溯源 JSON 字段路径 | §7 严守约束 |
| 16 | 项目时间线 D0-D7 整合成 1 张表 | 附录 A |
| 17 | 中文字体:中易雅黑 msyh.ttc(Windows 系统) | PDF 字体嵌入 |

---

## §7 严守约束(coze 实施时)

1. **不动 11 frozen 文件**:5 锚 JSON `03C6C01F3697` + 4 SPEC V0.1 + v19(沿 V2 合并) + v21(verifier/runs) + corpus/v20(沿 verifier/runs v20_run1) + P-F V0 占位 3 文件(SHA-12 详见 §3.1)。
2. **不动 5 份新报告**:PROGRESS_REPORT_WANG_2026_09_11.pdf + WANG_TEACHER_PROGRESS_REPORT + V3X_D7_V3_FINAL_REPORT_V7 + R1_R4_TRAE_REPORT + V7_§3_P_C_P_E_GRAY_NOTE(SHA-12 详见 §3.2)。
3. **不动 scripts/ 目录**:沿 7 铁律严守,coze 不可擅自落盘 `boss_f*.py` 真实脚本。
4. **不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API**。
5. **0 LLM 调用**:coze 沿用已有数据实算,纯文本/PDF 生成。
6. **不创建临时文件**:输出 1 份 PDF 即可,不得落盘 .tmp / .log / .json 临时文件。
7. **5 锚 JSON 沿用 `03C6C01F3697`**:SHA-12 实算 0 触动(本需求文档 §3.1 已列 11 frozen SHA-12,coze 沿用)。

---

## §8 沿 v3 提案附录的 5 附录数据来源

| 附录 | 标题 | 数据来源(JSON / MD) |
|------|------|---------------------|
| 附录 A | 数字溯源(9 model × 30 cells + 60 cells 数据 + D0-D7 时间线) | `results/deposon_volcengine_9model_30cells_2026_09_10.json` + 4 worker docs + V3_PHYSICAL_OPT_60CELLS_2026_09_11.md |
| 附录 B | 6 候选评级表 | V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md §3 + V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md |
| 附录 C | RAG 三次证伪 + 6 候选最终 verdict | FESHBACH_RAG_30CELLS_2026_09_10.md + DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md + B5 联合 CoT 论文引用 |
| 附录 D | 11 frozen 文件 SHA-12 验证 | 本文档 §3.1(已实算 11 SHA-12) + `verifier/handoff/KT_ABC1_anchors_sha256_12.json` |
| 附录 E | 4 个诚实风险(R1-R4) | CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md + BOSS_URL_2026_09_11.md + R1_R4_TRAE_REPORT_2026_09_11.md + V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md |

---

## 附录 0:本需求文档元数据

- **文件路径**:`docs/V3X/COZE_PROJECT_PROGRESS_REQUIREMENTS_2026_09_11.md`
- **撰写时间**:2026-09-11 14:00 CST
- **撰写方**:Mavis worker 子代理(`mvs_7efaa6b931a34243a66d783bd3dfba8a`)
- **沿用源**:
  - 5 锚 JSON SHA-12 = `03C6C01F3697` ✓(已实算验证)
  - 4 SPEC V0.1 / v19 / v21 / corpus/v20 / P-F V0 占位 全部 frozen,11 个 SHA-12 已验
  - 4 worker JSON + 总 JSON 9 model × 30 cells SHA-12 已验
  - 5 份新报告 SHA-12 已验
- **0 LLM**:本文档纯文本编辑,未调用任何 LLM / API / proxy
- **严守 7 铁律**:0 LLM / 不动 11 frozen / 不设 proxy / key 不入盘 / 不调外部 API / 不创建临时文件 / 不创建 scripts/
- **报告禁区**:**不写王老师 / 不写 WeChat 顾问 / 不写 6 月合作**(user 2026-09-11 13:59 明确要求)

> coze 收到本需求文档后,可直接按 §4 章节结构 + §6 质量要求 + §7 严守约束撰写综合进展报告。**整合而非复制** 5 份新报告内容,沿 v3 提案格式输出 1 份 PDF。
