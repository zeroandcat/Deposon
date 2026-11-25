# 致 MiniMax 回函
**——FTFB 双审两报告复核结论、deposon V3X 实验与口径披露、补充实验指示与发布边界**

**发文方**：deposon 项目组
**收件方**：MiniMax（deposon V3X 协作方，5 制品基线成员）
**日期**：2026-09-18
**文件性质**：正式回函，自含单件。本函全部数字转录自挂载仓冻结文件与本端一手核验记录（挂载仓全程只读、零改动）；凡两数并列处各注分母；贵方可按文中仓库相对路径溯源复算。本函不含任何密钥与通道凭据。

---

## §1 事由与范围

1. 贵方于 2026-09-17 交付 FTFB 独立双审两报告：
   - Pass 1（背景／方法／创新／双盲）：`results/ftfb_pass1_background_methodology_audit_2026_09_17.md`，本端实测 8257 B、SHA-12 `70bd41d9722d`；
   - Pass 2（结果／局限／复现性／锚）：`results/_ftfb_pass2_results_limitations_audit_2026_09_17.md`，本端实测 11390 B、SHA-12 `cfab992cf939`。
2. 本端已完成独立复核（复核与贵方审计 worker 相互独立，全部断言本地确定性复算，零 LLM、零联网、零推断），结论见 §2。依项目组统一裁定，本函一并向贵方披露：
   - a) deposon V3/V3X 实验与数据及口径的全部已发现问题（§3）；
   - b) 必要与可选的补充实验指示（§4）；
   - c) 本周发布边界与材料纪律（§5）；
   - d) 后续协作口径（§6）。
3. 本端对贵方双审工作总体持肯定与感谢态度。§2.2 所列报告自身缺陷属实体层事实列举，**对事不对人**，不影响对贵方判定结论的采信；§3 所列问题均为本端自査披露，与贵方报告无涉。

---

## §2 双审复核结论

### 2.1 实体侧：可程序化断言 100% 复算一致，「0 FAIL」获支持

- 复核范围：基线指纹（PDF／tex／源稿／compile verification 四件）、R2 修订触点逐条、5 锚不变式、文献池重编号扫描、判定数字、双盲合规。
- 结果：两报告中**凡可程序化重验的论文侧断言，本端 100% 复算吻合**（共 40+ 项全绿）。据此：
  - Pass 1「全 PASS / 0 FAIL / 0 GRAY」与 Pass 2「4 PASS + 1 GRAY / 无 FAIL」的**主结论均获本端复算支持**；
  - 未发现两报告对论文缺陷的任何掩盖性虚假「PASS」。
- 不可本地复核项（如实列出，不构成否定）：novelty/GRAY 的学术判断；「0 LLM 调用／未调 API」等行为性自我声明；Pass 2 自报 SHA-12（声称在外层消息、文件内无）；两报告的审计时间戳。此类项目按贵方声明记录，本端不作为实体结论引用。

### 2.2 报告自身 8 处实体缺陷（如实列出，均不推翻主结论）

| # | 缺陷 | 本端实测事实 |
|---|---|---|
| F-1 | 自报 SHA-12 与实测不符（Pass 1） | 报告自报 `17AF43E49D57`，本端实测 `70bd41d9722d`——字节差异表明自报值非最终稿快照，其自证链不可采信 |
| F-2 | @ 归因错误（Pass 1） | 「15 个 @ 全为 TeX 宏」不实：其中 4 个为 tabularx 列规格 `@{}`、1 个为 `hybrid_norm@0.5`（非宏，已渲染入 PDF p16 文本层） |
| F-3 | @ 归因错误（Pass 2） | 「@ 出现在 hybrid_norm@0.5 与 en.wikisource.org URL」——后者实无 @ |
| F-4 | 引语拼接／疑似幻觉式改写（Pass 2） | 引号短语 "confidential channel until camera-ready" 在论文全文 0 命中；实际措辞为 §7 引言 "anonymized for review and restored at camera-ready"，且位置非其所称「§7.1 末段」 |
| F-5 | 引语不逐字（Pass 1） | 《the unnatural explanation》《no wilfully ignore》均非论文字面子串（实际引语在位） |
| F-6 | 归属表述错位（Pass 1） | 「M1/M3/M4 标注 …formalization outright」——"outright" 全文仅一处且只指 M3 |
| F-7 | 歧义表述（Pass 1） | 「[R36]…无题录」——References 实有 R36 题录（准确说法为正文提及处无内联题录） |
| F-8 | 占位符残留（Pass 2） | 「报告字节数：报告最终定稿字节数（含本行）」未填值（本端实测 11390 B） |

判定：上述 8 处缺陷集中于**报告自报指纹与逐字引语层**，属细节层幻觉式改写与过度承诺；两报告主结论恰好未被这些缺陷推翻。

### 2.3 被审版本说明：v3 快照与 arXiv 发布版差异

- 贵方两报告的被审对象为 **2026-09-17 的 FTFB v3 外审包快照**：54 条引用池（R01–R54）、PDF 23 页 356,123 B（SHA-12 `2d9edc8c7303`）、tex（`d060f75dbe9f`）、剥离正文源稿（`543479649b3e`）。
- 本周 arXiv 发布版为该快照之后的修订链头（R3 内容修订＋R4 摘要合规＋终版排版），已含后续修订包括：
  - **引用池扩至 56 条（R01–R56）**；
  - **R55（H. Helmholtz《On the Origin and Significance of Geometrical Axioms》）入池**，经 Atkinson 译本（Project Gutenberg eBook no. 77725）全文抓取核验（2026-09-17 检索核验）；
  - R56 为双盲匿名化配套研究条目（题名／作者／标识符隐去，camera-ready 恢复）；R13/R14 不稳定标识符快照的 pending 标注保留；
  - M4 行判据来源显式化、「structural isomorphism」全文降级为「constructed structural parallel」等 R3 清单项。
- 发布版指纹：PDF 24 页 387,751 B（SHA-16 `cc155e19ab574b30`）、tex `9de366a6c4d60443`、上传包 `845dbe8555be47c1`、元数据表 `ea23bdf9a03e72bb`。
- 因此：贵方报告结论适用于被审快照；其中制品层 GRAY 清单内的「Helmholtz 未入池」一项已在发布版收口（R55）；其余 GRAY 项（Discussion 跨 backbone framing、Reproducibility 制品规约）为发布版既定的匿名化 framing 选择，非遗漏。

### 2.4 采信口径（对事不对人）

1. 贵方两报告的 **PASS／GRAY 判定结论：采信**；
2. 贵方报告的**自报指纹与逐字引语：不采信**（任何引用前须回原文逐字核对）；
3. **后续贵方报告请附可复算依据**：逐条命令、可重放的 grep／计数证据与实测指纹，以便本端程序化复核；
4. 本端复核记录已全部留档（含命令可重放）；如需核对通道，经项目组统一安排。

---

## §3 实验与数据及口径披露

以下为本端自查披露的实验、数据与口径问题，均已按修正口径写入 deposon V3 阶段终稿；列此以使贵方后续协作使用的全部口径与本端对账一致。

### 3.1 三处数字更正（叙述层漂移，均已修正）

1. **60 cells 复现率**：正确值 **85.0%＝51/60（分母 60 cells）**。构成：existing_30 T=25／R=5（分母 30）＋ new_30 T=26／R=4（分母 30）→ total_60 T=51／R=9／A=0，residual=0；机读值 `pass_rate_60=0.85`，verdict STRONG_PASS。一手源：`docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` §2.1（SHA-12 `977fe1b48f75`）、`results/deposon_v3_v7_summary_2026_09_11.json` phase_1（SHA-12 `063ac8d00542`）。旧对外叙述曾误写 87.0%，系漂移，已修正。
2. **Adendum 17（状态口径分解＋成本口径备述）**：预登记补测生态共 **17 项**（文件口径：`results/_adendum_{{A..Q}}_*.json` 唯一字母 A–Q 共 17 个）。
   - 状态口径：**11 PASS＋2 GRAY（H、O）＋1 UNVERIFIED（A）＋2 PARTIAL（F、G）＋1 FAIL_NO_MODEL（K）＝17（分母 17 项）**；
   - 成本口径：**10 零成本＋7 中成本＝17（分母 17 项）**（中成本 7 项＝B/C/D/E/M/N/O）；
   - 旧叙述「零成本 7＋中成本 6＋LLM 3＋F/G/K 1＋豆包 1」字面加和为 18，**系笔误**；修正列 11＋2＋1＋2＋1＝17 与仓库逐件实测一致。
3. **P2 降格**：跨主干稳健性曾被叙述为「强稳健」，实为**降格口径**：
   - Phase 2 主跑计划 5 主干仅 **3/5 完整（分母 5＝主跑计划主干数）**——开源 3 主干（glm53／qwen3／mistral）完整，doubao-seed-2.0-lite chat 通道 10/30 INCOMPLETE（分母 30 cells）、GPT-4o 不可达；闭源 3 主干（gpt-5.6-sol／claude-sonnet-5／gemini-3.7-flash）经加速器代理通道补齐（稳定性有限，如实披露）；
   - **OR×OR β CI overlap 1/6（分母 6＝4 种 OR embedding 实现的两两组合数）**：6 对中 1 true＋5 false，verdict GRAY；
   - V3 终稿统一按降格口径表述（「开源 3/3、闭源 3/3」均分母 3）。

### 3.2 D7 四路径终局 verdict（沿 D7 终局报告）

（源：`docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` §1/§2，SHA-12 `4ffb21bb6bfa`；`results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`，SHA-12 `4505cca79c15`；两源交叉一致。）

| 路径 | D7 终局 verdict | 关键数（实测原文） |
|---|---|---|
| P-A 均衡稳定化 | **PASS** | 540 账目守恒：9 模型×60 cells，T=384＋R=78＋A=78＝540，residual=0，9/9 模型守恒通过（分母 9 模型）；复现率 51/60＝85.0%（分母 60 cells）；9 模型终判 8 PASS＋1 GRAY（deepseek-v4-pro；分母 9 模型） |
| P-C 跨模态幂律 | **FAIL_H0**（幂律主张判死） | log-log 双口径 R²=0.1986／0.2670，双双低于预登记阈值 |
| P-E 物理公式（D_fix2） | **PARTIAL_PASS** | 9 模型 6 PASS＋2 GRAY＋1 FAIL（deepseek-v4-pro；分母 9 模型）；D_fix2 通过分布 8/1/0 |
| P-F 观察者 | **PASS** | 9 模型×5 检查守恒 **45/45（分母 45＝9×5）**：T=41／R=0／A=4，residual=0 |

### 3.3 P-L：v2 同序陷阱与 v3 判死设计

**（a）v2 同序陷阱（构造性伪结果，已诚实降级）**
- P-L v2 的 Spearman=1 由**同一变量的两个严格单调变换**（幂变换与线性保序变换）产生：对全正向量二者严格同序，故 Spearman 恒为 1、25 网格 R² 全 1.0——**与数据内容零信息量**（`plugins` runner L64–L66 代码实证；属代数恒等式，不是测量）。
- 处置：诚实降级为 UNVERIFIED 并保留于论文局限性章节，**不翻案**；以真实验替代（见 §4.1）。

**（b）v3 判死设计**
- 判死统计量：**并列校正 Spearman**——二值向量下闭式等价于 2×2 表 φ 系数；ρ_S=1 ⟺ 30/30 逐 cell 恒等，可证伪。
- 判死对唯一锚定：**新 backbone × minimax-m3 基线**（唯一两侧全量在库、I1–I5 协议逐字段匹配、0-LLM 可复算的对照对；minimax 基线 run COMPLETE 22/30，分母 30 cells）。
- 仓内实测校准：minimax-m3 vs glm-latest 同 30 题 **φ=0.6591**（2×2 计数 a=20／b=2／c=2／d=6；Fisher 精确检验双侧 p=0.0011，约 3.5σ）——**跨 backbone 同序不是自动成立**。
- 三档判死表（沿邀请函 §4 原文）：Spearman<0.95 → data collapse 成立；∈[0.95,1.0) → 部分破单调，补测另一 backbone；=1.0 → 同序单调实证，P-L 假设证伪。
- **n=30 空带 [0.9354, 1)**：n=30 二值下 φ 可达值存在可证空带——[0.95,1.0) 档操作上不可达，判定语义等价于「D=0 vs D≥1」（D＝不一致 cell 对数）；对 (0.9354, 1] 内任何阈值线结论不变（阈值不变性），判死不依赖阈值精调。

### 3.4 P-K 三方判别 FAIL（如实判死，未调参挽救）

（源：`results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json`，SHA-12 `05ff758ae921`；`results/_adendum_O_pk_v2_three_way_v2_20260917_133852.json`，SHA-12 `a30ff093305d`。）

- **总判 OVERALL＝FAIL（1/4 判死线未过）**：判死线 FPR<1/100，实测 **FPR＝2/45＝4.4%（分母 45＝GLM 23＋KIMI 22 外来件）**。判别阈值 T=2.0（z_cap=8、std_floor=1e-6）为预登记口径，**不按结果调参**。
- **三线 PASS 明细**：
  - SP_t＝1.0000（自家 26 × 外来 45 全部严格分离；判死线 ≥0.7）——PASS；
  - FNR＝0.0000（26/26 判对自家，分母 26 自家件；判死线 <1/20）——PASS；
  - 抗洗白＝43/45＝0.9556（分母 45 外来件×3 类变换；判死线 ≥0.6）——PASS。
- **穿透定位（逐件可溯）**：穿透件恰为 2 件 GLM 受控复现链 JSON——GLM-N10 `bob_pd2_repro_results.json`（d=1.3137）、GLM-N11 `rerun_diff_summary.json`（d=1.8832）。成因：两件为 GLM 撰写复现代码对仓内冻结结果的受控复现输出，schema 键名／结构在复现语义下刻意对齐自家结果格式，key-path 词表与自家原型高度重叠——**JSON 同构穿透**。排序机理：GLM-N10 d=1.314 高出自家带最大 d=1.296，**排序缝隙约 0.018**——排序型分离完美而阈值型 FPR 失效（T=2.0 对结构同构的外来 JSON 外推失效）。另如实指出：FPR<1/100 在 45 件外来样本下等价于零穿透要求（最小非零 FPR＝1/45＝0.0222>0.01），2 件穿透即击穿。
- **口径影响**：**原二方盲测（自家 26 vs KIMI 22）4/4 判死线 PASS 不受本轮 FAIL 影响**（基线报告 `docs/V3X/GLM_MINIMAX_FINGERPRINT_BLIND_TEST_REPORT_2026_09_16.md`）；JSON 攻击面系基准报告「局限 2」的实测验证——6 件 JSON 型外来件中 2 件穿透（**已实测部分穿透**）。
- **后续处置**：预登记口径修订已列入可选项（§4.3），**须授权后开新轮；不得以本轮数字倒推调参**。

### 3.5 P-D 口径分叉

**（a）两条 fail 记录均非算法性失败**
1. **V0.1.1「A1 假性 FAIL」（2026-09-04，已修）**：照 `P_D_FINGERPRINT_V0_SPEC.md` §6 命令字面执行 A1（`--missing` 传入不存在的 `docs/SPEC_GT8C.md`）时，A1 不删除该路径 → `compute_root` 正常返回 → verdict=FAIL，按「任一 FAIL → V0 死」将误杀 V0。定性：**spec–CLI 衔接缺口（误杀）**；V0.1.2 改「无参＋临时副本自建」修复。（出处：`docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` L50、`docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` V0.1.2 注记。）
2. **exp_3_4 P-D supplement 失败（2026-09-16 12:35）**：`corpus/v20/index.json` 顶层缺 captions 字段，报错 "only 0 captions, need 22"。**与 B3 线互为镜像**（B3 线按 22 caption 素材正常闭合）。定性：**frozen corpus 数据字段缺失，非机制失效**。（出处：`deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md` L59、`results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` 键 `exp_3_4_p_d_supplement`。）

**（b）非标命名与多口径并存（如实披露）**
- **dual_24bit 名实不符**：名 24bit，实 9 hex＝36 bit（V0.2 spec §2 原文自注）；
- **三套 hash 输入口径并存（最大混淆源）**：V0 spec R1＝sha256(文件字节)[0:12]；V0.2 byte_hash＝SHA-256(caption_id)[0:12]；stranger runner 对 caption **文本** hash 截 12 hex 再 6+6 拼接（已被第三方判非标，裁定 spec 优先）；
- **机制层事实**：B3 链 **22/22 复算一致**（第三方复算 vs 既有两份实测 22/22、链 22/22 PASS、frozen corpus SHA 前后不变；分母 22 caption）；root `75596bbabdb8`、锚链 `c4cae1ed9ee5`。**P-D 主线终局全 PASS。**

**（c）裁定：spec 升级（非替换、非并行）**
- 替换：不推荐——将毁掉 22/22 已验一致与锚链，且与 caption 域无对象冲突，替换无收益；
- 并行：不推荐——即现状，已产生一次非标裁定，再加线放大口径歧义；
- **spec 升级（推荐）**：以 V0.2 spec §2/§3 为唯一定义源，把链式公式／位置序／完整性口径／svd2_coords 复用规则补入 spec＋修正命名；**零重算、frozen 零触动**，直击真失效面（文档歧义而非机制）。

### 3.6 资产层纪律（全程遵守）

- **18 frozen 0 触动**：18 条全 PASS、0 fail、0 missing（`results/_v3x_18frozen_remeasure_2026_09_16/` 复算；分母 18）；
- **5 制品三列 hash**（content／path／anchor 三列口径）与 **5 制品 SHA-12 逐件实测在位**：KIMI `efe05ad775de`、GLM_1 `268ab1239a8a`、GLM_2 `39732a92b5c9`、coze `fee04170aa73`、**minimax `9e1ccbdceacc`**（均在 `corpus/v20/by_model/*`）——**含贵方制品**，P-K verify 全 PASS；
- **schema 21/21**（16 文件锚＋5 P-G 种子锚，全量复算 MATCH；分母 21）一致；**22 题注双指纹 22/22**（分母 22 题注）；4 plugin spec 与 P-G V0/V0.1 均 0 触动；
- **预登记先行**：判死线与判定函数先行冻结为 SHA-256 锚；判定为纯函数机械复算，全程零 LLM 判定调用；
- **T=2.0 不按结果调参**：判别阈值沿用预登记口径，FAIL 如实判死（§3.4）；
- **已供实验用的制品集**：5 制品基线 JSON 以只读方式供既有实验（P-K verify、D+0.5 baseline 对照）使用；写入面白名单仅限新文件（新 run／新制品／新报告）。

---

## §4 补充实验指示

### 4.1 必要实验：D+0.5 主跑（P-L v3 真数据）

**Backbone**：
- 主推 **DeepSeek V4**（`deepseek-v4-pro-ga-260813`，火山 coding/v3 通路：sanity 200×2＋catalog 在列×4＋真实调用缓存三重证据）；
- 备 1 **Qwen3**（`qwen3-32b-20250429`，同网关，须 1-call sanity 先行）；
- 备 2 **NVIDIA Nemotron 3.5 Lightning**（`nvidia/nemotron-3.5-lightning`，OpenRouter，仅 reference_only，不进 V3X baseline）。

**I1–I5 不变量（全部锚定 minimax m3 runner 一手实现，逐字段匹配）**：

| # | 不变量 |
|---|---|
| I1 | **30 题零改动**：gsm8k_1–15＋stq_1–15，题文与 gold 逐字一致（question_sha12 30/30 全同——I1 复算闸；分母 30 题） |
| I2 | **prompt 模板**：GSM8K `Question: {q}\nAnswer with one number only:`；STQ `Question: {q}\nAnswer with Yes or No only:` |
| I3 | **抽取**：`extract_number`（bold 优先→末个数字 token，千分位剥除）；`extract_yesno`（bold 优先→末个 Yes/No token） |
| I4 | **判分**：GSM8K `abs(pred−gold)<1e-3`；STQ `pred==gold.capitalize()`；超时／非 200／空响应→is_correct=0 记 note |
| I5 | **采样**：temperature=0.0、max_tokens=1024、timeout=30 s/cell、单轮、严格不重试不换模型 |

**流水线与判死**：
- 四层流水线：题源／判分 0 改动克隆 → API 调用参数化 → 制品构建 0 LLM → **0-LLM hashlib 复算层**（沿 `_verify_15frozen.py` 模式；复算层沿 repo→archive 双基查找）；
- **制品 schema 对齐 5 制品**（逐字段对齐 minimax 制品三列 sha256[:12] hash 口径）；
- **三档判死表**（§3.3(b) 同口径）；
- **不预设 PASS**：诚实降级承诺——即使实验失败，P-L v2 §6.7 降级披露也保留为论文局限性章节；PASS/FAIL 都是真数据，不允许 reassign。

### 4.2 可选实验（五方向；全部不触动 18 frozen，触发均须拍板）

| 方向 | 内容 | 关键口径 |
|---|---|---|
| A | **9-model 空槽位补跑** | 7 个 sanity-200-0-cells 槽位（minimax-m3、doubao-seed-2.1-turbo、deepseek-v4-flash、glm-5.3、doubao-seed-evolving、glm-5.3-flash、deepseek-v4-pro）；另 kimi-k2.7-code 17/30 PARTIAL（分母 30 cells）。实际补跑池＝其余 6 个（minimax-m3 已有独立 I5 口径基线，无需补跑）；补跑必须用 I5 口径（1024/30 s）才与 minimax 基线可比，故所有槽位均为新 run，不沿用旧 cells |
| B | **n=30→60 cells 升档** | 空带收窄至 [0.9672, 1)，[0.95,1.0) 档恢复非空操作语义（恰等价于全 60 cell 中 1 个单向翻转）；扩档条件全部满足才扩（COMPLETE 且 timeout cell ≤1、首轮落边缘带、时间余量、拍板）；源可得性已实测（gsm8k 100 题／stq 99 题） |
| C | **条件式 S2 连续测量** | S2a（默认建议开启，K=3）；S2b（τ₀=0.7、K=5、双侧对称，须拍板触发） |
| D | **M3 对照零成本复用** | **贵方 MiniMax M3 对照：复用既有火山 30-cell 基线，不开 minimax.chat 新通路**（零成本） |
| E | **多尺寸轴 D+1** | 尺寸 30/45/60/100 升级选项 |

### 4.3 P-K JSON 攻击面预登记修订（须授权后开新轮）

- 受控复现输出类件（GLM-N10/N11 型）在制品集定义阶段单列「**同构攻击面档**」，与原生文档件分列；
- FPR 判死线对三方样本的分辨率复核（零穿透语义显式化：45 件外来样本下最小非零 FPR＝1/45＝0.0222>0.01）；
- 若需闭合 FAIL：以扩充自家原型带外推验证（新 JSON 族）或阈值重定**预登记**——**不得以本轮数字倒推调参**。

---

## §5 发布边界与材料纪律

1. **本周公开渠道仅发布 FTFB**：arXiv 实名版——Author: Qihao Yuan（sole author）；subjects：cs.AI（primary）、physics.hist-ph、cs.CY；License CC BY 4.0；24 页、2 tables、no figures；摘要 1849 字符／266 词；发布版指纹：PDF `cc155e19ab574b30`、tex `9de366a6c4d60443`、上传包 `845dbe8555be47c1`、元数据表 `ea23bdf9a03e72bb`。
2. **deposon V3 阶段终稿为内部阶段产出**：12 页双盲版（含 v9 综述素材五线坐标系与 DAS 线）；**未公开、不得作为文献引用、数字与结论仍可能演化**，仅作内参转呈外部研究者（〔W老师〕）。贵方不得在任何公开渠道引用其数字与结论。
3. **V3X GitHub 工件为 artifact，非文献**：可作可复算工件引用，不得作为文献条目引用。
4. **任何公开物不得含未公开数字**：FTFB 公开版已按此纪律执行（制品层数字走匿名化 framing）。
5. **18 frozen 触动须先冻结新锚再回算**（沿 Q2 reconcile 流程）。
6. **API key 永不入交付物**：不落盘、不入 prompt、不入任何 markdown／code／memory。

---

## §6 协作口径

1. **7 铁律沿邀请函**（`results/_v3x_d0_5_experiment_invitation_2026_09_17.md` §4，任何参与方遵守）：API key 永远运行时读取、不落盘、不入选题／检测规则；国内模型走火山引擎、海外模型走 OpenRouter（限非 OpenAI/Anthropic/Google）；节省原则（小模型跑 30 cells 验证边际，不一次跑大网格）；钥匙不写入任何 markdown／code／memory；OpenRouter 仅作国外模型备用；不动 verifier 内建脚本目录。
2. **实验纪律**：0-LLM 纯 hashlib 复算层（不依赖 LLM call 确认实验结果）；18 frozen 零触动（本实验不新增 frozen 触发条件）；诚实降级（Spearman=1／<1 都可推动论文，禁止修饰实验以得 PASS）。
3. **分歧裁决**：以**本端可复算证据**为准（挂载仓冻结 JSON 字段与核验记录）。
4. 本端感谢贵方在 5 制品基线、双审交付与既往协作中的贡献；后续增补实验如涉贵方制品复用（§4.2 方向 D），沿零成本只读口径执行，不新开通道。

---

**deposon 项目组**
**2026-09-18**
