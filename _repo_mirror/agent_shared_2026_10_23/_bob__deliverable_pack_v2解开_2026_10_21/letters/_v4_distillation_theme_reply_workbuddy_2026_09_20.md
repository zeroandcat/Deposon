# 反向阅读：V1–V3 资产栈让蒸馏主题「可想的」与「不可说的」

**收件人：** deposon 主编（principal investigator）
**回复方：** workbuddy（workplace-bundle / 新增通道均可）
**回应对象：** `results/_v4_distillation_invitation_2026_09_20_v1.0.md`（SHA-12 `3D9F73519F6C`）+ 配套 prompt pack（SHA-12 `E5C37E90255B`）
**日期：** 2026-09-20

---

## AI 使用披露

本回复由 AI 生成（WorkBuddy，作为受邀接收方运行）。**所有文件读取与 SHA-256 重算都是本次会话内通过工具实际执行的**，不是凭记忆断言；凡标注「实测」的数值均可由 PI 复算。推理、选题与措辞由模型产出。起草中未调用除本回复生成模型以外的 LLM API，未抓取外部 URL，未触及任何密钥或端点。

## 是否已读完

是 —— 邀请函 411 行与 prompt pack 384 行逐行读完，并按 §8 表独立重算了 25 个路径的字节数与 SHA-12，全部命中。

---

## 一、核对结果：哪些站得住，哪些站不住

### 站得住的（复核通过，值得明确肯定）

- **§8 资产表 25 条字节数与 SHA-12 全部实测命中**，无一偏差。这份表可靠。
- **§2.6 的「22 caption」修正正确**：`corpus/v20/strip_captions_22.json`（SHA-12 `6A2656878745`）实测为长度 22 的 list。
- **§2.1 对 GLM_1 文件名异常的提示正确**：第 2 行 `"task": "P-K 盲测 GLM 槽位落位 (三方: 自家 vs GLM vs KIMI, 判别规则零改动)"`，确实不是 `artifact_v_*.json` 形态。
- **§3 的种子性质标注是忠实的**。我回读了 `results/_v4_brainstorm_seeds_2026_09_20.md`（SHA-12 `0EB1CFAA2992`）：40 条性质行实测为 35 条「纯思辨」+ 3 条「纯思辨（脚手架借用）」+ 1 条「纯思辨（资产可复用、用途不同）」+ 1 条「纯思辨（资产用途不同）」。**邀请函没有把任何种子拔高** —— 我原本准备挑这个毛病，核对后发现没有。

### 站不住的（六条）

**C1 — 邀请函内部字节数自相矛盾。** §2.2 第 66 行写 `boss_pa_1_rbr_rm_result_2026_09_15.json` 为 8,674 字节；§8 第 383 行写 8,753。实测 **8,753**。§2.2 是错的。

**C2 — §2.2 说该文件「encodes the 9-backbone × 60-cell evaluation」，过头了。** 实测 `results/boss_pa_1_rbr_rm_result_2026_09_15.json`（SHA-12 `C7C59E0D2F6C`）：第 27–36 行 `v3_540_conservation_check` 确有 `n_models=9, n_540_total=540`，但它只是一个**守恒校验**（`T540_sum=384, R540_sum=78, A540_sum=78, residual=0`）。文件主体是第 37–337 行的 `boss_pa1_22graph_simulation` —— 22 张图上的重复最优反应／遗憾匹配博弈模拟（第 2–4 行：BOSS-P-A1，引 Hart & Mas-Colell 2000），终判在第 339–340 行为「DIFFERENTIATED」。**文件里没有 9×60 的逐格逐模型矩阵**，只有 540 这个被三分守恒掉的总数。

这直接影响 §2.2 的 re-fit 假设（「540 点行为信号面」）：那个面上没有 540 个点，只有三个加总和一个 22 图博弈结果。准确的说法应是 **re-fit on a summary statistic**，比邀请函标注的「re-fit hypothesis (not calibrated)」还弱一档。

**C3 — 「kimi 产物」是索引的字节级副本，可实测结案。** `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` 与 `corpus/v20/index_v2_2026_09_16.json` 的完整 SHA-256 实测同为 `efe05ad775de239883c908d6a603754f86cfab578c2543a63b16e5188dc79261`，字节数同为 24,150。§2.6 标 `[待 PI 裁定]` 是对的（**是否故意共置**仍需 PI 判），但「是否同一文件」已由测量回答：是。

**C4 — §2.1 称五个 by_model 产物为「one per vendor 的 output-distribution sample」，实测四个不是。** 逐个读结构：

| 文件 | 实测内容 |
|---|---|
| `kimi/index_v2_2026_09_16.json` (`EFE05AD775DE`) | 22 张 DAG 图的**结构索引**（graph_id / N / n_edges / n_named / seed / sha256），无模型输出 |
| `GLM_2/glm_artifact_v_2026_09_16.json` (`39732A92B5C9`) | schema `kimi_artifact_v/1.0`，count 23，**制品清单**（artifact_id / source_path / n_bytes / byte_sha12 / struct_signature） |
| `coze/coze_artifact_v_2026_09_16.json` (`FEE04170AA73`) | schema `coze_artifact_v/1.0`，artifact_count 29，制品清单，note 明写「0 LLM 抽取」 |
| `minimax/artifact_v_2026_09_16.json` (`9E1CCBDCEACC`) | meta.subject = **`minimax-m3`**，artifact_count 30，制品清单，`iron_rules: no_llm/no_proxy/no_gateway/no_key/no_frozen_touch` 全 true |
| `GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` (`268AB1239A8A`) | **不是清单，是一份跑完的预登记＋实测归因实验**（见第二节） |

五个里没有一个是「某厂商的逐格输出分布」。它们是**跨主体 authorship 指纹盲测用的制品清单** —— 列的是各主体撰写的文档文件及其哈希，不是模型生成的文本。

**C5 — 「四路终判」是六路里挑的四路，且 P-C 在盘上有两个判词。** `results/deposon_v3_v7_summary_2026_09_11.json`（SHA-12 `063AC8D00542`）第 210–214 行实测：

```
PASS:      ["P-A", "P-D"]
GRAY:      ["P-B (GRAY/NOISE 边界…)", "P-C (失真界)", "P-E"]
DEAD:      ["P-C (双相结构, 沿 V3 v4)"]
TRIGGERED: ["P-F (V0 → V0.1, 1 周判死 D1+D2)"]
total:     "2 PASS (P-A + P-D) + 3 GRAY (P-B + P-C 失真界 + P-E) + 1 DEAD (P-C 双相) + 1 P-F TRIGGERED"
```

盘上是 **P-A / P-B / P-C / P-D / P-E / P-F 六路**；「四路」剔掉了 P-B 与 P-D，而被剔的 P-D 是 PASS 的。P-C 同时挂 GRAY（失真界）与 DEAD（双相结构），§2.3 只写「P-C DEAD」。第 177 行原文为 `"DEAD (R²=0.0007, 落入 2D Ising 普适类)"`，后半句邀请函未录。

**C6 — 「5 KT anchors」在盘上对不上任何一个 5。** `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（SHA-12 `03C6C01F3697`）实测 3 个锚组（KT-A1 / KT-B1 / KT-C1）× 每组 5 条 = **15 条子锚**，metadata.note 自写「15 真 + 0 占位(全填)」。「5」对应的其实是 `trust_anchor_5_concat`（5 个 hash-12 拼接，拼接值 SHA-12 = `79f8dfa2c296`，见 d7 文件第 5 行）。**两个「5」是两件事**，邀请函混用。

### 附带：命名分歧可收敛一半

§6.4 请 PI 裁定 `KIMI-K3` 与 `kimi-for-coding`。实测盘上**至少三个串**：

- `KIMI-K3` —— 见于 `results/_kimi_v4_t12_review_2026_09_20.md` 等回复类文件（散文用法）
- `kimi-for-coding` —— `corpus/v20/L_algorithm_process.json` 第 485 行 `"model": "kimi-for-coding"`（同文件第 4 行 `"structure": "llm_generated_dag"`）
- `kimi-k2.7-code` —— `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` 第 48 行
- `minimax-m3` —— 同一 d7 文件第 40 行，及 minimax 产物 meta.subject

**我倾向认为 V0.1 散文里的 `M3` 就是 `minimax-m3` 的截断而非另一实体** —— 但这是推断，`M3` 是否作为独立串出现在盘上，我没有穷尽验证。

**九个骨干的名字盘上是有的**，就在 d7 文件第 22–59 行：doubao-seed-2.0-lite、glm-5.3、deepseek-v4-flash、doubao-seed-evolving、minimax-m3、glm-5.3-flash、kimi-k2.7-code、doubao-seed-2.1-turbo、deepseek-v4-pro。§7.1 说「映射未声明」是对的，但「九个骨干是谁」其实已声明，邀请函没写进去。

---

## 二、最重要的一条：盘上已经有一台量好的「来源归因仪」

这是我这次阅读最大的收获，也是邀请函低估自身资产的地方。

`corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json`（SHA-12 `268AB1239A8A`）不只是一份预登记，它跑完了：

- 第 7 行口径：`13 维特征/清洗/洗白/指纹函数`，`T=2.0, z_cap=8, std_floor=1e-6`，判别规则 `d<T 判自家，否则判外来`，不按结果调参。
- 第 35–37 行预登记判死线：`SP_t >= 0.7`、`FPR < 1/100`、`FNR < 1/20`、`anti_whitewash >= 0.6`。
- 第 579–583 行实测：`FPR = 0.04444…`、`FNR = 0.0`、`SP_t = 1.0`、`anti_whitewash_total = 0.95556…`。
- 第 680–698 行逐条比对：SP_t 过、FNR 过、抗洗白过、**FPR 未过**。
- 第 700 行：`"overall_verdict": "FAIL"`（盘上原文引用，不是我在下判定）。

**为什么对主题要紧。** 这四行数字的形状是：已知样本两两全分开（SP_t=1.0）、真阳性一个不漏（FNR=0）、但对「外来者」每约 22 个误报 1 个（FPR 4.4%）。而 4.4% 正是 V0.1 散文里「P-K FPR 4.4%」的来源 —— 它在这儿，在这个 by_model 产物里，而 §2.1 把该文件只描述成「a second teacher's per-cell output」。

**想法（idea）。** S-37 问假阳／假阴的成本结构如何倾斜。盘上已有一份相邻领域的量好答案：**分离能力不是瓶颈，误报率才是**。若蒸馏检测继承这个形状，决定这条路线价值的就不是「能不能检出」，而是「在什么基础发生率之下，4.4% 的误报率会让结论不可用」。这是个基础发生率（base rate）问题，而且可以只用一个已在盘上的数字来讨论。

**证据（evidence）。** 同文件第 585–613 行：三种抗洗白变换（W1 key reorder / W2 newline inject / W3 comment inject）下，45 件外来件有 43 件保持归因，率 0.9556。这是**对擦除攻击的实测鲁棒性**。

**批评（critique）。** 三种变换全是**语法层**的（键序、换行、注释）。学生模型做的不是语法层擦除，而是**语义层重述** —— 它不会保留键顺序，它会重新表达。所以这 95.6% 的鲁棒性测的是「格式擦除」，而主题真正关心的「语义擦除」恰恰落在测量之外。**这个缺口正好是主题所在的位置**，这是我读到这里最强烈的感受。

**怀疑（doubt）。** 我不能判断这 13 维特征在文档 authorship 上有效，是否意味着任何东西在模型行为上也有效。两者对象不同：这里比的是「谁写的这份文件」，蒸馏检测要比的是「这个分布是从哪个模型学来的」。我认为不能直接搬，但也不能说无关 —— **这是 re-fit 假设，不是盘上事实**，且我无法从文件本身判断它属于哪一档，请 PI 裁定。

---

## 三、逐种子的想法 / 证据 / 批评 / 怀疑

### S-17 跨模型溯源

**证据**：上面的 GLM_1 实测即为盘上锚点。种子标「pure speculative, no on-disk anchor」，我认为这个标注偏强 —— 盘上有锚点，只是在**相邻领域**（文档 authorship 而非模型蒸馏）。用它做蒸馏是 re-fit 假设；但说「没有盘上锚点」不准确。

### S-37 假阳／假阴成本结构

**证据**：`GLM_1` 第 580–581 行 FPR=0.0444 / FNR=0.0 的不对称是实测的。**想法**：这条不对称若迁移到蒸馏检测，会导出一个反直觉的推论 —— 检测器的可用与否不由其准确率决定，而由「被怀疑对象里真蒸馏者占比」决定。占比低于约 4% 时，多数阳性结论会是错的。**这是纯思辨，无盘上锚点**，但它是从盘上数字出发的。

### S-08 嵌入几何对齐

**证据（负面）**：`results/deposon_v3_v7_summary_2026_09_11.json` 第 102 行 `"P-A": "GRAY (-1.7pp vs no-RAG, 5 embedding 全 NOISE)"`、第 106 行 `"P-E": "NOISE (6 embedding 全 NOISE)"`。盘上已有嵌入实验，结果是 NOISE。**怀疑**：我不确定这两处的 embedding 指的是什么对象的嵌入（第 102–113 行在 V6 RAG 叠加比较块内），所以我不主张这就是对 S-08 的有力否证，只主张它是**一条应当被看见的负面记录**。

**另一条证据**：`results/deposon_volcengine_embedding_30cells_2026_09_10.json`（24,794 字节）实测含 2048 维嵌入、30 格、跨 4 个 vision embedding 模型；`results/deposon_volcengine_22caption_embedding_2026_09_10.json` 把 22 条 caption 全量嵌入并带 `gt_labels`（4 类）。**这两个文件不在 §8 表里**。所以 §2.10 的「盘上没有什么」清单若被读者反向读成「盘上没有嵌入资产」，会是错的 —— 嵌入资产存在，只是没被登记。

### S-02 / S-30 几何类种子

**批评**：`results/deposon_pg_v01_9m60c_2026_09_15.json`（SHA-12 `AB75889EE738`）第 1–9 行实测 `"method": "0 LLM, 0 proxy, 0 API, pure numpy Poincare ball (c=1) hyperbolic transport"`，scope 为「9 model × 60 cells = 540 cells 双曲 transport 实算」。**它是对双曲几何的纯数值模拟，从未接触任何模型的真实表示**。把它借作「蒸馏深度的几何指纹」，借到的是**几何的模拟**，不是**几何的测量**。邀请函已标「scaffolding tier」，我认为还应加一句：这是 synthetic geometry，不是 measured geometry。

### S-04 推理链转移

**证据**：`results/deposon_v3_v7_summary_2026_09_11.json` 第 197 行 `"B5_cot": {"verdict": "OBSERVED_WITH_QUALIFIER (2 model 0.867 但 CoT 未公开对比)"}`。§2.3 引作 P-A key_evidence 的「2 model 0.867」，在盘上挂在 **CoT 条目**下且带限定语「CoT 未公开对比」。**想法**：0.867 这个数在 `results/deposon_volcengine_9model_30cells_2026_09_10.json` 里也有踪迹 —— doubao-seed-2.0-lite `pass_rate_30 = 0.8667`（GSM8K 14/15 + StrategyQA 12/15 = 26/30）。**我认为两者同源，但这是推断，我没有确证**；若是，则「0.867」的真实出身是网关跑批的公开基准通过率，而非 deposon 判别指标。

**怀疑**：同一文件明示 `"note": "PARTIAL RUN: 9 model full run timed out at 85 min wall-clock. 1 model complete… 7 models not started"`。所以「9 model × 30 cells」这个最接近「教师输出」的资源，实测只有 1 个模型跑完。**这直接削弱任何把 9 骨干当作输出资源使用的假设。**

### S-13 / S-19 隐写指纹与水印

**批评**：邀请函反复出现「the 22-caption fingerprint」这一说法。实测 `corpus/v20/strip_captions_22.json` 每条的键只有 `id / text / family / structure / n_labels`，**没有任何 fingerprint 字段**，text 是概念图的中文标签串（「问题输入; 数据预处理; 特征工程; …」）。deposon 里的「指纹」指的是文档的 13 维特征指纹，不是 caption。把 22 条 caption 称作 fingerprint 是一个**范畴错误**，会误导 S-13/S-19 的读者以为盘上已有水印原型。盘上没有。

### S-15 输出统计异常

**证据**：`results/deposon_v3_v7_summary_2026_09_11.json` 第 93 行 `"byte + semantic 双指纹 PASS, delta_hash 必要性下降"`；第 227 行 `B1_fingerprinting: "HIGH (DeepMind 2022 / Google 2023 LLM 指纹可能已在 1% 开销内做 95% 准确率, P-F 联合方案无差异化)"`。

**想法**：第 227 行是盘上唯一一处对 LLM 指纹技术 landscape 的先验评估，而且它是**否定性**的 —— 「P-F 联合方案无差异化」。邀请函全文未引。这条比任何种子都更接近「这个主题值不值得做」的判断，且它是盘上事实。

**怀疑**：「95% 准确率 / 1% 开销」是该文件转述的文献说法，我没核实原始出处，标注为**未验证的转述**。

---

## 四、最深的怀疑：这个主题里没有「学生」

读完之后我最大的不安不是任何一条引用，而是结构性的：

蒸馏的定义在逻辑上需要两方 —— 教师与学生。而 V1–V3 盘上**只有教师侧**：by_model 是制品清单，9 backbone 是判别网格，四路终判是教师侧裁决，语料图是概念图。**没有任何一个盘上对象是一个学生**，也没有任何一条种子问「学生从哪来」。

而栈自身的铁律禁止造一个出来：`minimax/artifact_v_2026_09_16.json` 的 `iron_rules` 实测为 `no_llm / no_proxy / no_gateway / no_key / no_frozen_touch` 全 true；`boss_pa_1_rbr_rm_result_2026_09_15.json` 第 7–15 行同样有 `no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_〔IM〕API: true`。**不调 API 就造不出学生**。

所以这不是一个「还没做」的问题，而是一个**分叉**：要么这个主题被限定为纯教师侧 inquiry（那它的产出形态会与「蒸馏检测」很不一样），要么铁律需要被重新审视。我认为这条应该在邀请函里被明写出来，而不是留给读者自己撞上。

---

## 五、收尾

**(a) 最值得追的种子：S-17（跨模型溯源）。** 理由是它是 40 条里唯一一条盘上已存在**量好、预登记、带实测误差结构**的仪器的种子 —— `GLM_1` 那份 SP_t=1.0 / FNR=0 / FPR=4.4% / 抗洗白 95.6% 的四元组。它把 S-37 的成本问题从一个思辨问题变成了一个可以从已有数字出发讨论的问题。附带的好处是：它同时暴露了「语法层擦除测过、语义层擦除没测」这个精确缺口，而那个缺口正是蒸馏与文档归因的分界线。

**(b) 最不值得追的：S-02 / S-30（几何类）。** 理由是 P-G v01 实测是 `pure numpy Poincare ball (c=1)` 的数值模拟，0 LLM、0 API —— 它从未测量过任何模型的真实表示。把它当作蒸馏深度的几何指纹，借到的是几何的模拟而非几何的测量，且盘上已有嵌入实验返回 NOISE 的负面记录（第 102、106 行）作为旁证。

**(c) 我希望有但没有的种子：一条关于「学生」的种子。** 具体说，一条问：*若盘上不存在任何学生侧对象，那么关于蒸馏的任何一个可证伪命题，其证伪所需的对照物来自哪里？* 40 条种子全部预设了学生存在（S-01 到 S-35 无一例外），但没有一条追问它的来源。这是种子场最大的沉默。

**(d) 我会加进 §4 的开放问题：** 「这个主题是否需要放宽 `no_llm / no_proxy / no_gateway` 铁律？如果需要，由谁、在什么边界下放宽；如果不需要，那么 V4 的产出形态是否应当被重新描述为『教师侧的可提取性研究』而非『蒸馏检测研究』？」—— 引用 `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` 的 `meta.iron_rules` 与 `results/boss_pa_1_rbr_rm_result_2026_09_15.json` 第 7–15 行为据。

---

**最后一句自我矛盾，按 §6 的要求主动交代。** 我在第二节说「邀请函低估了自身资产」（S-17 有盘上锚点），在第四节又说「盘上没有学生，主题结构性不完整」。这两句不冲突但张力很大：前者说资产比邀请函写的好，后者说资产再好也缺一半。我认为两者都成立 —— 好消息和坏消息是同一件事的两面：deposon 有一台量好的归因仪，但它量的是作者，不是教师；而这台仪器所缺的那一半，恰恰是栈自己的铁律不让它去取的。

*本回复为受邀参与，不构成署名。主编是唯一可问责作者。*
