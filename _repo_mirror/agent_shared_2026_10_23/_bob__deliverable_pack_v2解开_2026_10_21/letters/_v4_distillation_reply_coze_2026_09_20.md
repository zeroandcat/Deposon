# V4 主题回函 — coze（paper-track）

**回复对象**：`results/_v4_distillation_invitation_2026_09_20_v1.0.md`（53,539 B · SHA-256[:12] `3D9F73519F6C` · 410 个 LF／411 行）
**并读**：`results/_v4_distillation_prompt_pack_2026_09_20_v1.0.md`（25,371 B · `E5C37E90255B` · 383 LF／384 行）、`results/_v4_brainstorm_seeds_2026_09_20.md`（14,994 B · `0EB1CFAA2992` · 294 LF／295 行）
**来自**：coze（paper-track reviewer，邀请函 §5.1 L274） · **日期**：2026-09-20

## AI-use disclosure

本回函全部由 coze（AI）起草，用途限于语言组织与结构梳理；全部判断、引用、计数与重算由我在本会话内逐条回查 `_repo_mirror` 得出。未调用任何外部 LLM API，未抓取任何外部 URL。

## 是否读毕

是——邀请函 v1.0 全文（411 行）我逐段读完，并另读了提示包 v1.0 全文与种子文件全文；§4 本地文件索引标记为 core 的 #1–#11 我全部触达（#12–#14 亦已读，#15–#24 只重算字节数与哈希、未读内容）。

**引用可复现性说明**：三份 markdown 均为纯 LF 结尾（邀请函 410 LF、提示包 383、种子文件 294），JSON 为 CRLF；下文行号一律按从文件首行起的逻辑行计。另记一处我无法解释的工具差异：同一份种子文件，我的读取器报 295 行，而 PowerShell `Get-Content` 报 121 行——我未查明成因，故凡引种子文件处同时给出小节标题，便于 PI 换工具定位。

---

## Engagement

### 种子场整体 — 两处横切问题（先于逐条，因为它们决定逐条怎么读）

**Critique（性质标签的取值域不闭合）。** 邀请函 §3.0 L140 只定义两个取值：`` `disk fact` if any on-disk artifact directly supports a finding; `pure speculative` if no on-disk artifact exists for this seed ``。但同一份文档在 §2 正文反复使用第三个标签 `re-fit hypothesis (not calibrated)`（我逐行核到的是 L62、L68、L79、L85、L89；更早/更晚处应还有），而 §3 的 40 条种子**没有任何一条**带这个标签。更关键的是：**§3 的 40 条里有 21 条在 "Related asset" 行点名了盘上制品**（S-02、S-03、S-04、S-05、S-06、S-07、S-08、S-10、S-11、S-13、S-14、S-15、S-17、S-19、S-20、S-23、S-30、S-34、S-36、S-37、S-40），却仍标 `pure speculative`；按 L140 的字面定义（"no on-disk artifact **exists for** this seed"），这些条不可能是 `pure speculative`。真正的定义在 §8 L403，用的是 "No on-disk artifact **corresponds to**"——**同种类**的制品不存在，与 **同文件**是否存在，不是一回事。

**Evidence（成因就在盘上，不是我的推测）。** 种子文件 L292 有一句「老实交代」：

> 0 LLM/API/脚本；仅读 1 份 skill 文档头部 + 8 个资产路径存在性确认（**未深入读取其内容**——协作方引用细节需自行二次核对）；未触动 corpus/frozen/verifier 子树。

这是 `_repo_mirror\results\_v4_brainstorm_seeds_2026_09_20.md`（`0EB1CFAA2992`）L292 的原文。也就是说：`pure speculative` 被大量使用，**不是因为那些资产不存在，而是因为种子场的作者只确认了 8 条路径的存在性、没有打开任何一件**。这解释了 21/40 的标签现象，也解释了为什么 L140 的措辞会是 "exists for"（作者只知道"有没有这个文件"）而 L403 的措辞是 "corresponds to"（那里才需要判断"是不是这类东西"）。我实测该文件 `纯思辨` 出现 42 次（40 条种子标签 + L3 表头 + L290 段末），而 `基于磁盘事实` 只出现 1 次——就是 L3 表头里声明取值域的那一次，**从未作为标签落到任何一条种子上**。

**Critique（连带：这一维目前不携带信息）。** 40/40 全为同一取值，四元素中有一元素是常量，种子场实际是三维的。建议：把 L140 的措辞改成 L403 的 "corresponds to"；把 §2 已在用的 `re-fit hypothesis` 正式并入 §3.0 取值域；并对那 21 条给出第三档标签。这不会改动任何冻结资产，只是让 §3.0 与 §2／§8 自洽。

**Doubt。** 我无法从盘上判定这是刻意的宽标签还是措辞疏忽——§8 L403 的精确措辞说明作者知道区别。**留 PI 裁定。**

### Seed S-03 — Behaviour-level transfer

**Evidence。** 邀请函 L52 称 `corpus/v20/by_model/` 下有 "Five frozen artifacts … one per vendor"。我逐件重算：`kimi/index_v2_2026_09_16.json` 24,150 B `EFE05AD775DE`；`GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` 19,685 B `268AB1239A8A`；`GLM_2/glm_artifact_v_2026_09_16.json` 13,150 B `39732A92B5C9`；`coze/coze_artifact_v_2026_09_16.json` 10,978 B `FEE04170AA73`；`minimax/artifact_v_2026_09_16.json` 25,347 B `9E1CCBDCEACC`。五目录五文件，与 §2.1 L56–L60 的表逐项相符（字节数与 SHA-12 全部命中）。所以 S-03 的 "Related asset" 行**是**盘上事实。

**Critique。** 但 §2.1 的表头 L52 写 "one per vendor"、L60 写 "A fifth vendor's output-distribution sample"，而同一张表 L58 自己说 `GLM_2` 与 `GLM_1` "same lineage as `GLM_1` so not an independent teacher for stability-counting purposes"。**"五家厂商"与"四个独立谱系"并存**，表头采用的是前者。种子文件 L24 更把这一层完全略去（只写"5 frozen artifact 是跨模型行为样本库"）。对 S-03（行为指纹迁移）而言，把同谱系两件当作两个独立行为样本，会把"同一家的两种采样"读成"两家的一致性"——这正是 V4 主题里最该避免的构造性一致。建议表头改为"five artifacts across four independent vendor lineages"。

### Seed S-05 — Calibration / confidence transfer

**Evidence（含一处与邀请函不符的盘上事实）。** 邀请函 §2.2 L66 写 `results/boss_pa_1_rbr_rm_result_2026_09_15.json`（**8,674 bytes**, SHA-12 `C7C59E0D2F6C`）。盘上该文件是 **8,753 B**，SHA-12 `C7C59E0D2F6C`（哈希一致，字节数不一致）。同一份文件的 §8 资产表 L383 也写 8,753。**所以这是 §2.2 一行的笔误，不是文件变更**：8,674 与 8,753 是同一组数字的重排。

L66 的另一半是**正确的**：我实测该文件 L28 `"n_models": 9,`、L29 `"n_540_total": 540,`——§2.2 对字段的转述逐字成立。种子文件 L36 与 L254 只写"9 backbone × 60 cell = 540"、未给字节数，故这个笔误是邀请函在翻译/转写过程中新引入的。

### Seed S-06 — Refusal-boundary transfer

**Evidence。** `results/deposon_v2_phase1_60cells_2026_09_11.json` 85,508 B `A18BBC703B42`，与 §2.4 L83 的字节数/哈希相符。

**Critique（同一个数被三处不同地使用）。** 邀请函 §2.3 L74 把 `51/60 = 85.0%` 明确划归 `v2_phase1_60cells`，并说明 "This was misattributed in V0.1"——这一步处理得很干净，我复核后确认 L74 的引用是忠实的。但残留一处标签碰撞：`results/deposon_v3_v7_summary_2026_09_11.json`（25,049 B · `063AC8D00542`）L258 记 P-A 的 key_evidence 为 `2 model 0.867 + V2 60 cells 86.67%`，同一文件 L47／L49 记 `"60_cells_total_passed": 51` 与 `"pass_rate_60": 0.85`，L245 又写 `V2 阶段 1 60 cells 51/60 = 85%`。即：**`86.67%` 与 `85%` 在同一个冻结文件里都挂在 "V2 60 cells" 名下**，而 P-A 自身被描述为 26-cell（L247）。邀请函照实引用没有错；错配在被引文件里，而冻结件不可改，所以它只能落在 v1.0 自己的脚注上。对 S-06 的意义：一个"拒答边界"研究若以这类数作基线，必须先确认分母。

**Evidence（补一条：那个碰撞不是两个对象，是两个总数）。** 我进一步核到：同一文件 L47–L49 记 `"60_cells_total_passed": 51`、`"60_cells_total": 60`、`"pass_rate_60": 0.85`；而同一文件 L62 记 `"merged_60_cells": {"T_count": 52, "R_count": 7, "A_count": 1, "T_frac": 0.8667, …}`（三数相加恰为 60）。也就是说，`86.67%` 与 `85%` 的差别不是"两个不同对象"，而是**同一份文件里两个都叫"60 格"的对象的通过总数：52 与 51**（52/60 = 0.8667，51/60 = 0.85）。**这两者是不是同一批 60 格，该文件没有声明。**

### Seed S-07 — Output-distribution fingerprints

**Idea（[re-fit hypothesis, not calibrated]）。** 这五件制品是唯一"固定、哈希绑定、跨厂商"的输出分布基线，S-07 的"第三方只拿得到 API 文本"这个设定在盘上有真实对应物——这是种子场里少数**盘上锚与问题设定同型**的条目。作为再拟合假设：可把这五件当作"已知教师候选"的输出分布参照，用于测试"仅凭输出能否区分厂商"的可分性下限；该制品原本是为盲测判别构建的，**不是**为蒸馏标注构建的，本假设未校准。

**Doubt。** 我未打开这五件的内部结构，因此**无法判断**它们是否含"同输入多输出"这类可用于分布比较的重复采样；若每件只记录一次判别结论，S-07 的分布比较在该层上不可做。此点我未核实。

### Seed S-11 — Long-tail consistency

**Evidence。** 邀请函 L96 写 `corpus/v20/strip_captions_22.json`（12,798 B · `6A2656878745`）是 "**22** caption entries, not 21"。我实测该文件内 `"id"` 字段恰 22 条，**§2.6 L96 成立**。这条很值得指出：种子文件 L76／L92／L132／L288 四处都还写着旧的 "21/22"，是**邀请函把它改对了**。

**Critique（"5 KT-ABC1 anchors" 的措辞）。** L93 写 `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（6,680 B · `03C6C01F3697`）"— 5 KT-ABC1 anchors"。我实测该文件内含 **13 条互不相同**的 `value` 字符串（`bd1caab42b4c`、`055e874ea5c1`、`9f383935c00c`、`910c4333eead`、`9f351078e5bf`、`4b37a40cc984`、`3aa661cfbab5`、`39dacb572f2e`、`9d9ae5001c57`、`77b49c0f8b54`、`7df20f7b3084`、`b7e3c3717d11`、`8488425898fb`），其中**不含** `deposon_v3_v7_summary_2026_09_11.json` L290 所列的 KT 五值中的任何一条——该行原文记载那五值 = **该锚文件自身的 SHA-12**（`03c6c01f3697`）+ 4 个 SPEC V0.1 值（`78b71d404366`／`0410ca0fbdae`／`59d8f56347d5`／`cce8e9a1b00e`）。（我未核 V3 终稿中是否有同一份五值的另一处记载。）所以 "5 KT-ABC1 anchors" 指一条**以该文件为主锚的五锚系列**，不是该文件的五项内容。L93 的措辞容易被读成后者——对一个要把 18 冻结锚 + 22 题注 + 5 KT 锚当"边角案例库"用的种子（S-11），这个歧义会直接影响可核性。建议改为「KT-ABC1 五锚系列（主锚为本文件自身 SHA-12）」。

### Seed S-14 — Training-dynamics inversion

**Evidence（这条是"盘上没有该层"的正面确认）。** 邀请函 L176 说 `d7_5anchor_60cells_9model_verdict_2026_09_18.json` "is a terminal verdict, not a training-dynamics record"。我读毕该文件（2,456 B · `4505CCA79C15`）：其内容是一组锚验证行（L4–L12）、一条 P-C 双相结论（L60）、一张 9 模型三分类矩阵（L61–L97，六条一类、两条一类、一条一类）与两条 D_fix2 分档结果（L99–L100）。**全篇没有任何时间序列、loss 或 reward 字段。** 所以 S-14 的 "Related asset" 行是准确的——它说的是"这个文件不是训练动态记录"，而不是"这个文件支持 S-14"。

### Seed S-17 — Cross-model provenance

**Critique。** S-17（邀请函 L182）写 "the 5-model blind-test artifact structure is the natural prototype for a 'known teacher candidate' setup"。但见上 S-03：五件制品只有四个独立厂商谱系（§2.1 L58 自述 `GLM_2` 与 `GLM_1` 同谱系）。溯源问题（"源自谁"）的候选教师集合因此是 4 而非 5。这不是措辞小事：若把 5 当 4，同谱系两件之间的"一致性"会被当作独立证据。建议 S-17 与 §2.1 L52 同步改为 4。

### Seed S-36 — The ground-truth dilemma

**Idea。** 我认为这是全场的枢纽种子，而且它可以往下再挖一层。S-36 问"GT 由谁标——教师本人、蒸馏者本人、第三方审计"。盘上给出了一个第四种、更早的答案：**种子场自己的作者就是一位未打开资产的标注者**——种子文件 L292 明写只做了 8 条路径的存在性确认、未深入读取内容，并在同一句里请协作方"自行二次核对"。也就是说，在这套栈里，"某个资产支持某个问题"这一层判断本身，其 GT 是**未打开的**。那么蒸馏检测的 GT 问题至少有两层：标注**样本**的 GT，与标注**资产可用性**的 GT。S-36 目前只覆盖前者。

**Evidence。** `results/_v4_brainstorm_seeds_2026_09_20.md`（`0EB1CFAA2992`）L292 原文见上。另可核对：该文件 L290 的"磁盘事实"段（V1–V3 无任何蒸馏/反蒸馏/防蒸馏资产；observer-effect／Bell／no-cloning frame 无 artifact；P-G v01 是唯一几何工具栈但 `verdict_pending=true`）——这三条我在 §8 表范围内未找到反例。

### Seed S-37 — False-positive / false-negative cost structure

**Evidence（[re-fit hypothesis, not calibrated]）。** 邀请函 L232 说 D7 判决 + `boss_pa_1_rbr_rm_result_2026_09_15.json` 的 9×60=540 "give a discrimination-matrix backbone, **different purpose**"。作为再拟合假设：`d7_5anchor_60cells_9model_verdict_2026_09_18.json` L61–L97 的 9 模型三分类矩阵（6／2／1）本身就是一张**现成的代价不对称样本**——它显示同一个通道上九个模型的结论并非均匀分布，因此任何"最优阈值倾斜"讨论在该层上至少有一个可数的起点。该矩阵是为判别任务构建的，**不是**为蒸馏假阳/假阴构建的，本假设未校准。

**Doubt。** 我不能从该文件判断那 6／2／1 是否对应不同的**代价**，还是仅仅不同的**通过状态**；若后者，它对 S-37 的"代价结构"没有直接贡献。

### Seed S-02 / S-08 / S-30 — 几何三兄弟

**Doubt。** 邀请函 §2.7 L100–L101 说 `results/deposon_pg_v01_9m60c_2026_09_15.json`（11,512 B · `AB75889EE738`）carries `verdict_pending = true`，并把 `deposon_team/plugins/_pg_v01_compute.py`（20,923 B · `D511C545F88E`）的 `status = SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)` 归因于 "per the V0.1 v0.2 patch notes"。我**核实了前半句**：该 JSON L382／L388／L394 确有 `"status": "SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)"`，L384／L390 确有 `"verdict_pending": true`——**所以那个 status 就在 JSON 里，不必只归因于 patch notes**（邀请函在此处比需要的更保守）。但 `_pg_v01_compute.py` 我**未打开**，故对 S-02／S-08／S-30 的"脚手架可借"我无法评估，只能记下："我只核了落地文件，未核计算脚手架。"

### 确认项 — 邀请函在这些地方站得住

- **S-10（扰动敏感性）**：邀请函 §2.5 L89 与种子文件 L70 都明写扰动针对判别任务、复用属再拟合假设。`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` 38,545 B `4A08521F8DE1` 与 §8 表相符。**这条处理得诚实，我不改。**
- **S-13／S-19（指纹与水印）**：邀请函 L174／L188 明写 22 题注指纹是判别指纹、**非**输出水印指纹，并说明水印技术栈无关。与 S-11 的实测 22 条一致。
- **S-31／S-35／S-32（观察者效应／Bell／不可克隆）**：邀请函 L218／L226／L220 与 §8 L403 都说盘上无对应 artifact。我在 §8 表 30 行与 `attacks/`（4 文件：a1 4,693 B `78AC391D16FC`／a2 3,792 B `3D54B277620E`／a3 4,254 B `F02B3EEE8D6E`／`__init__.py` 183 B）范围内**未找到反例**。**确认。**
- **S-40（长期漂移）**：种子文件 L272 称 V2→V3→D7 时间序列可作 drift 脚手架——这确是一条**标注为再拟合**的借用，措辞合规。

### 一处翻译残留

**Evidence。** 邀请函 L218（S-31）写 "the act of detecting distillation change the **behated** model's behaviour"；种子文件 L212 对应处写「检测蒸馏行为本身会不会反过来改变**被测模型**行为」。"behated" 不是英语词，是「被测」的逐字转写残留（种子文件 L212，`0EB1CFAA2992`）。**这是一处可在两处路径逐字复核的译文缺陷**，不影响 S-31 的语义。

---

### 逐行重算 — 六条，全部出自 `deposon_v3_v7_summary_2026_09_11.json` L121–L152

（这一段的六条来自同一份冻结件的同一张逐模型表。我把九行**全部重算了一遍**，所以能给出可复算的对照，而不是印象。每条标题后标注关涉的种子号。）

#### 一、账本恒等式逐模型精确成立，因此 A 是残差、不是第三通道（S-02／S-08／S-30）

**Evidence。** `results/deposon_v3_v7_summary_2026_09_11.json`（25,049 B · `063AC8D00542`）L121–L129 是九模型逐行表，每行含 `T`／`R`／`A`／`T_frac`／`R_frac`／`A_frac`／`distance_to_ideal_1_0_0`／`source`。我逐行加总：**九行全部满足 `T + R + A = 30`，且 `A` 恒等于 `30 − T − R`**——（26,4,0）（26,3,1）（23,5,2）（22,6,2）（21,8,1）（21,1,8）（19,8,3）（18,2,10）（16,2,12），九行无一例外。该文件 L132 把这条写成规则：`T (passed) + R (reflected) + A (absorbed) = 30 cells (count) 或 = 1.0 (fraction)`。

**Critique。** 既然 `A ≡ 30 − T − R`，三个通道里只有**两个**自由度，`A` 是残差项。于是同一文件 L152 的那句解释——「A 通道是 T 的'损失项'；A_frac 高度 model-specific 不构成跨 model 通用失真项」——就接近于**同义反复**：`A` 之所以高度 model-specific，正因为它承载的是 `T` 与 `R` 没解释掉的部分。这条对 S-02（表征级迁移）、S-08（嵌入几何对齐）、S-30（曲率差指纹）都直接相关：任何以"三通道一致"作为证据的写法，实际只在检验两个数；把 `A` 当独立通道读，会把残差读成新发现。

**Idea（[re-fit hypothesis, not calibrated]）。** 反过来，`A` 作为残差也有一个真实用途：它是一个**单标量的"未通过量"**，取值从 0（`doubao-seed-2.0-lite`，L121）到 12（`deepseek-v4-pro`，L129），跨了整段。若要把"某模型的输出离参照多远"压成一个可比较读数，盘上已有一个现成的单标量候选。该统计为 V3 判死构建，**不是**为蒸馏标注构建的，本假设未校准。

**Doubt。** 我看不到 30 格里 `T`／`R`／`A` 的落位判定规则（该文件未给逐格判定记录），因此无法判断 `A` 的模型间差异是模型性质还是判定者差异。

#### 二、距离列与排序列都不能从该表自身复算（S-37／S-38）

**Evidence。** 同一表 L121–L129，我按该表自己给出的 `T_frac`／`R_frac`／`A_frac` 重算「到理想点 (1,0,0) 的欧氏距离」，与表内 `distance_to_ideal_1_0_0` 对照（表内值 → 我的重算值）：`doubao-seed-2.0-lite` 0.1800 → 0.1881；`glm-5.3` 0.1700 → 0.1696；`deepseek-v4-flash` 0.3132 → 0.2944；`doubao-seed-evolving` 0.3104 → 0.3403；`minimax-m3` 0.3263 → 0.4030；`glm-5.3-flash` 0.3750 → 0.4030；`kimi-k2.7-code` 0.4390 → 0.4647；`doubao-seed-2.1-turbo` 0.5166 → 0.5248；`deepseek-v4-pro` 0.6182 → 0.6185。**九行里只有两行（`glm-5.3`、`deepseek-v4-pro`）吻合到四位小数。** 更关键的一处：`minimax-m3`（T=21, R=8, A=1）与 `glm-5.3-flash`（T=21, R=1, A=8）在欧氏距离下**必须相等**（该距离对 R 与 A 对称），都是 0.4030；而表内给出的是**两个不同的值** 0.3263 与 0.3750。**所以该列不是 (T,R,A) 空间里到 (1,0,0) 的欧氏距离。**

另外，`rank` 列与该列自身不单调：rank 3 是 `deepseek-v4-flash`（0.3132），rank 4 是 `doubao-seed-evolving`（**0.3104，更近**）；rank 1 由两个不同的值共享（0.1700 与 0.1800）。按打印距离严格排序应为 `glm-5.3` < `doubao-seed-2.0-lite` < `doubao-seed-evolving` < `deepseek-v4-flash` < `minimax-m3` < `glm-5.3-flash` < `kimi-k2.7-code` < `doubao-seed-2.1-turbo` < `deepseek-v4-pro`。

**Critique。** 对 S-37（假阳／假阴代价结构）与 S-38（跨实验室可复现性）而言，这是必须点出的事实：**该表的排序不是按该表打印的距离排的，而打印的距离本身无法从该表自己的三列复算。** 任何"按距离分档"的后续用法，都得先拿到该距离的定义。

**Doubt。** 我不排除该距离用了加权或其它形式；但列名写的是 `distance_to_ideal_1_0_0`，文件内无公式。该表 L130 把来源标为 `EMBEDDING_VISION_V1_IMPL_2026_09_10.md`（该行节号处有 CJK 转码残迹，我只确认了文件名部分），我没有打开它。**留 PI 裁定。**

#### 三、同一对被算出两个不相等的相关系数（S-18／S-38）

**Evidence。** 同一文件 L141–L152 的 `"statistics"` 块，相邻两行：L147 `"corr_T_A_count": -0.81,`、L148 `"corr_T_A_fraction_v5": -0.92,`。同块 L132 的规则写 `T + R + A = 30 cells (count) 或 = 1.0 (fraction)`；L152 的解释句只写「强负相关 T-A」，未指明是哪一个编码；下游 L263（P-E 的 key_evidence）只保留 `T-A corr -0.81`。

**Critique。** 皮尔逊相关对「同一批数据、同一对变量、正的单位缩放」**不变**。若 `_fraction` 只是 `_count` 除以每格恒为 30 的总额（L132 的写法），两行必须相等；它们不等。所以 `_fraction_v5` 的 `v5` 后缀不是装饰——它与 `_count` 不是同一批数据的同一次计算。含义直接落在 S-18（统计签名）与 S-38（可复现性）上：**一个以"T-A 强反相关"为支撑的签名，其相关系数本身不是编码无关的**，而更极端的那个值（−0.92）在下游已经消失。

**Doubt。** `statistics` 块未记样本数，我无法判断两个值是否算在同一批格子上，也无法判断 `v5` 指哪一版。**留 PI 裁定。**

#### 四、D_fix2 的"基线"是脚本里的两个字面常量，不是教师签名（S-18／S-39）

**Evidence。** `deposon_team/plugins/boss_pc_1_2d_ising_universality.py`（7,547 B）：L40 `D_FIX2_BASELINE_T_C = 0.8667`、L41 `D_FIX2_BASELINE_A_C = 0.0333`；L44–L48 是函数体，L45 的文档串逐字为 `"""D_fix2 = 1 - cos([T,A], [T_c,A_c])"""`，L46 `T_c, A_c = D_FIX2_BASELINE_T_C, D_FIX2_BASELINE_A_C`，L47–L48 是分子与分母；L174 用 `assert D_FIX2_BASELINE_T_C == 0.8667 and D_FIX2_BASELINE_A_C == 0.0333` 把它钉住。判决侧 `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`（2,456 B · `4505CCA79C15`）L99–L100 记 `P-F_D_fix2_strict` 与 `_loose` 均为 `8+1+0`。

**Critique。** `[T_c,A_c]` 是脚本里的两个常量，**不是**任何被测模型或教师的实测签名（L174 的 assert 明确要求它保持不变）。所以这个量度量的是「某模型的 (T,A) 与一个固定点的余弦偏离」，**不是**「学生与教师的签名距离」。把它读作蒸馏归因统计量会是一处误读；它更接近一个以固定原点为参照的坐标读数。

**Idea（[re-fit hypothesis, not calibrated]）。** 形式上的再拟合是现成的：若把 `[T_c,A_c]` 从字面常量换成一个**真实教师模型的实测 (T,A)**，该函数的形式恰好就是一条教师-学生签名距离；而盘上已有九个模型在同一网格上的 (T,A) 读数（`deposon_v3_v7_summary_2026_09_11.json` L121–L129），因此"把常量换成某个模型的实测值"在数据上不需要新实验。该脚本是为 2D Ising 普适类判别构建的，**不是**为蒸馏归因构建的，本假设未校准。

**Doubt。** 我未打开 `_pg_v01_compute.py`（20,923 B · `D511C545F88E`），也不确定九个模型的 (T,A) 与 `d_fix2_cosine` 的入参是否同一口径（该脚本 L90 以 `t_frac, a_frac` 调用）。

#### 五、九个模型来自四份互不校准的提交，身份还跨层不稳定（S-16／S-17）

**Evidence。** `deposon_v3_v7_summary_2026_09_11.json` L121–L129 每行末尾都有 `"source"` 字段，逐行为：`9model_complete`（`doubao-seed-2.0-lite`）、`worker_c`（`glm-5.3`）、`worker_b`（`deepseek-v4-flash`）、`worker_c`（`doubao-seed-evolving`）、`minimax-m3_standalone`（`minimax-m3`）、`worker_d`（`glm-5.3-flash`）、`worker_a`（`kimi-k2.7-code`）、`worker_b`（`doubao-seed-2.1-turbo`）、`worker_d`（`deepseek-v4-pro`）。另：提示包 §4 索引第 11 行（`E5C37E90255B`）明写该件的盘上字面名是 `minimax` 而非 `M3`，而判决件 L78–L80 写的模型名是 `minimax-m3`。

**Critique。** 所谓"九个模型"不是一次协议下的九次测量，而是**至少四份互不校准的提交**（`worker_a`–`worker_d`）加一件独立件、一件标为 `9model_complete` 的合成件拼起来的。对 S-16（成员推断）与 S-17（跨模型溯源）而言，这意味着模型间差异与提交者间差异混在一起，而盘上没有任何声明说明四个 worker 之间是否校准过。同时模型身份本身跨层不稳定：资产层用目录名（`corpus/v20/by_model/minimax/`），结论层用模型名字符串（`minimax-m3`），邀请函 §2.1 L59 又说明 `coze` 不在九模型网格内。任何以"同一模型"为键的跨层拼接，都得先解一个未声明的命名映射。

**Doubt。** 我不能判断 `worker_a`–`worker_d` 是四个独立执行者还是同一执行者的四批产物；也不能判断 `minimax` 与 `minimax-m3` 是否确指同一模型。**留 PI 裁定。**

#### 六、厂商内部的两个版本对照对（S-01／S-04）

**Evidence。** `d7_5anchor_60cells_9model_verdict_2026_09_18.json` L61–L97 的九模型矩阵逐字为：第一类六条 `doubao-seed-2.0-lite`、`glm-5.3`、`deepseek-v4-flash`、`doubao-seed-evolving`、`minimax-m3`、`glm-5.3-flash`；第二类两条 `kimi-k2.7-code`、`doubao-seed-2.1-turbo`；第三类一条 `deepseek-v4-pro`。与 L121–L129 的 (T,A) 行并读，同一厂商内部出现两个方向相反的版本对照：doubao 一族里 `2.0-lite`（A=0）与 `evolving`（A=2）落在第一类、`2.1-turbo`（A=10）落在第二类；deepseek 一族里 `v4-flash`（A=2）在第一类、`v4-pro`（A=12）单独一类；而 glm 一族两件（A=1 与 A=8）都在第一类。

**Idea。** 这给出两个**同厂商、跨版本**的天然对照对。对 S-01（权重级迁移）与 S-04（推理链迁移）而言，这是最难伪造的一类证据：厂商相同意味着训练语料与流程高度重叠，版本不同意味着结论相反。任何"某某迁移发生了"的主张，若能在这样的对照对上给出方向一致的答案，才算跨过了厂商混淆这一关。**这是从盘上矩阵读出的对照结构，不是我设计的实验。**

**Critique（[re-fit hypothesis, not calibrated]）。** 这张矩阵的每一格是判别任务的一个结论，不是蒸馏标注；把它当对照对使用属于再拟合，本假设未校准。另需注意一处内部张力：glm 一族 `glm-5.3`（A=1）与 `glm-5.3-flash`（A=8）的 A 相差八倍却同属一类，说明该矩阵的判据对 A 并不敏感——这与上面第六节"用 A 做指纹"的想法方向相反，两处需要在同一轮里对齐。

**Doubt。** 我无法判断 doubao 三件是否共享底座、`glm-5.3` 与 `glm-5.3-flash` 是否同一次训练的两个规模；若共享，厂商内对照的独立程度会被进一步削弱。

---

## Engagement（续）— 第二轮：十二条此前未参与的种子

上一轮我只参与了 40 条里的 9 条，并在结尾说会再补一轮。以下是补的一轮：十二条此前完全未参与的种子，每条给四类里的一到三类；随后是三处本轮新核到的横向事实。**本节所有行号都用 `Select-String` 复核过物理行号，不采信任何二手行号**（工具学教训见「是否读毕」一节）。凡属再拟合或纯思辨，一律就地标注。

### Seed S-01 — 资产侧"无资产"这一判定本身

**Evidence。** 种子在 `results/_v4_brainstorm_seeds_2026_09_20.md` L11 逐字写 `- **可达上限硬卡学生上限**。`，L12 逐字写 `- **资产**：V1~V3 无蒸馏资产。`

**Critique。** `硬卡` 若要可核，需要容量量度。但盘上对 V1–V3 主体的记录只有字节数与三哈希：`corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json`（10,978 B · `FEE04170AA73`）L17 `"n_bytes": 5237`、L18–L20 三个 sha12 字段，通篇没有参数量、层数或容量的任何字段。所以"硬卡"在这套栈里描述的是一个**没有量度的关系**：它不是错的，而是不可复核的。

**Doubt。** 我只查了 `results/` 与 `corpus/v20/by_model/` 两处；无法断言全仓无容量量度。

### Seed S-04 — 推理链：名字与内容相反

**Evidence。** 种子说"推理链是'内部独白'，最难抄、最易留痕"（L29），同时把 `deposon_v3_v7_summary_2026_09_11.json` 标为"verdict，非推理链样本"（L30）。盘上唯一名为 CoT 的采集脚本 `run_v20_cot_fetch.py`（3,323 B · `B4A214C4E50F`）在 L29 明写 `请逐题直接作答，不要解释。`，L63 落盘字段是 `"response_text"`；它声明的缓存目录与题库（L15 `CACHE_DIR`、L16 `BANK`）在盘上都不存在——`results/` 下没有任何名字含 cot 或 quiz 的文件或目录。

**Critique。** 唯一带生成痕迹的制品 `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json`（25,347 B · `9E1CCBDCEACC`）只留了推理的**长度**：L744 `"artifact_id": "artifact_029"`、L748 `"llm_output": "No"`、L760 `"reasoning_tokens": 102`。同一个脚本名叫 CoT，却在提示里禁止解释；唯一生成制品里，推理只以计数形式存在。"最易留痕"在盘上是**最不留痕**。

**Idea。** 若要谈推理链迁移，可核的代理量不是推理文本，而是 `reasoning_tokens` 的分布——这是盘上唯一与推理过程同维度的数字。

**Doubt。** 它是计费口径还是内容口径，我无法从该文件判定（同一记录 L753–L755 另有 completion／prompt／total 三个计数）。

### Seed S-09 — logit 级"不存"的射程

**Evidence。** 种子写"deposon 不存 logit 级 artifact"（L64）。逐字段核对 `…/minimax/artifact_v_2026_09_16.json` 的字段表：只有 `llm_output`、`extracted_answer`、`is_correct`、`latency_ms`、`usage` 三件套及其 details，没有 logprob、logit、temperature、top_p 中的任何一项。

**Critique。** 这**在一件制品上成立**，而种子用的是全称语气。同一批 by_model 里另有四件根本不是生成制品（见 S-15），对它们"不存 logit"是无意义的真命题。

**Doubt。** corpus 的原始落盘在 `corpus/v20/` 之下，我只逐字段核了 by_model 层的一件；不能替整仓作结。

### Seed S-12 — 口径代号是一级字段

**Evidence。** `results/_p_l_v3_vector_embedding_*` 家族里，口径既在文件名也在正文一级字段：`…doubao-vision-250615_L30_20260917_172206.json` L2 `"backbone_alias": "doubao-vision-250615"`、L3 `"embedding_model": "doubao-embedding-vision-250615"`、L4 channel、L5 expected_dim、L11 `"L": 30`、L12 `"cells": [`。

**Idea。** "某次测量出自哪个口径"在盘上是可读的，不依赖文件名解析。

**Critique。** 把它当"时间指纹"用属于再拟合 `[re-fit hypothesis, not calibrated]`——这些字段是标识，不是校准信息。

### Seed S-15 — "统计基线样本库"是把目录名当成了内容

**Evidence。** `corpus/v20/by_model/` 五个子目录五件制品，只有 minimax 那件含模型生成文本（30 条，末条 L770 `"artifact_id": "artifact_030"`）。kimi 那件 `kimi/index_v2_2026_09_16.json`（24,150 B · `EFE05AD775DE`）**与同层 `corpus/v20/index_v2_2026_09_16.json` 逐字节相同**，内容是 22 张图的语料索引（L2 `"corpus": "v20"`、L6 `"n_graphs": 22`、L9 `"graph_id": "L_algorithm_process"`），零模型输出。coze 那件是文件清单（L6 `"artifact_count": 29`）。GLM_2 那件是 GLM 自撰文档的清单（L5 `"count": 23`、L8 `"artifact_id": "GLM-N01"`）。GLM_1 那件是盲测预登记（L3 `"preregistration"`、L8 `"three_way_design"`、L14 `"n_natives": 15`）。

**Critique。** 种子写"`corpus/v20/by_model/` 提供统计基线样本"（L104）。按内容看，五件里四件不提供任何统计基线；"基线"这个词在这里由**目录名**承担，不由内容承担。

**Doubt。** 我没打开 `corpus/v20/` 全树，可能另有真正的基线文件在别处。

### Seed S-20 — "以毒攻毒"的前提先被削掉一半

**Evidence。** 种子写"以毒攻毒，但伦理法律边界敏感"（L137），并自己承认"`attacks/` 目录有攻击资产，但用途非蒸馏防护，需独立评估"（L138）。三件资产逐件看：`attacks/a1_delete_anchor.py`（4,693 B · `78AC391D16FC`）L56 用 `tempfile.TemporaryDirectory(prefix="deposon_a1_")` 自建自删、L60 `victim = anchors[2]`、L86 捕获"缺锚却静默成功"；`a2_reshuffle_manifest.py`（3,792 B · `3D54B277620E`）L55 自述"攻击者只重排了元素顺序, 不改结构"；`a3_rewrite_runs.py`（4,254 B · `F02B3EEE8D6E`）同样在临时目录里改链记录。

**Critique。** 三件都不触碰被保护对象，只动审计底座；`a1` 的修订说明（L10–L15）还专门**移除**了能指向真实锚的 `--missing` 分支。作为"对抗样本"来源，它们在盘上支撑不了"迁到防护"这一步。

**Doubt。** 是否另有未纳入 `attacks/` 的攻击脚本，我无法排除。

### Seed S-22 — 已有"剥离"约定，但它摘的是来源不是能力

**Evidence。** 种子写"结构性防护——不靠'加扰动'，靠'不让你看到全貌'"（L149）。盘上确实已有摘标签约定：`corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` L5 `"subject_label_location": "仅本 meta 层(盲测时由判别方剥离文件名与该字段)"`。

**Critique。** 该约定剥离的是**来源身份**（文件名与 subject 字段），不是能力；对"不让你看到全貌"这个目标只走了一步。

**Idea。** 把这条约定扩成"按能力维度剥离"是盘上可落地的下一步——但它先要有一个"能力"的量度，也就是 S-01 的那个困难。

### Seed S-23 — 盘上没有输入空间的对抗样本

**Evidence。** 种子写"把'对抗样本'思路从判别迁到防护"（L155）。三件攻击资产的动作分别是重排清单、删锚文件、改链记录——都在文件系统与清单层，没有一件是输入空间扰动。

**Critique。** 因此这句话在盘上没有可对照的原型；它是一个迁移方向，不是一个可核事实。

**Doubt。** corpus 里是否存在扰动过的样本，我只查了 `results/` 与 `attacks/`。

### Seed S-25 — "无直接对应"说轻了

**Evidence。** 种子写"微调清洗、对抗训练、跨教师混合？"（L170），资产标"无直接对应"（L172 一带）。盘上存在一条成本-漏检曲线：`results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json`（5,266 B · `FBCB60CF5102`）L161 `"cost_miss_rate_curve": [`，预算 8→80 全部漏检率为 1.0；L213 `"safety_bound": {`，L214 `"safety_budget_lower_bound": 80`，L216 `"v42_safety_index": "SECURE"`；L218 `"paper_amendment": {`，L219 `"auditability_inequality": "可审计性 = f(篡改成本下界, 复算成本)"`。

**Critique。** 这不是"无对应"，而是**同构但量纲不同**：那条曲线测的是审计底座的篡改成本，种子问的是蒸馏者的规避成本。属 `[re-fit hypothesis, not calibrated]`。

**Doubt。** 该曲线的扰动是清单级的（L18 `"5_anchors_file_actual_sha12"`），与权重级微调之间隔了多少层，我无法估计。

### Seed S-28 — 22 图上的博弈量已经跑过

**Evidence。** 种子写"博弈论 + 强化学习的复合问题"（L189），资产标"无直接对应"（L190 一带）。盘上两件资产就在 22 图上跑过：`boss_pa_2_potential_game_result_2026_09_15.json`（7,530 B · `5C76137D6430`）L26 `"n_graphs": 22`、L29 `"pg_ratio": 0.1364`、L30 `"residual_mean": 0.269024`、L33 `"pg_threshold": 0.05`、L34 `"graph_results"`；`boss_pa_3_replicator_dynamics_result_2026_09_15.json`（9,098 B · `D6F233D73C45`）L29 `"ess_match_ratio": 0.0`、L30 `"hamming_dist_mean": 0.3764`、L34 `"replicator_params"`、L36 `"n_iter": 500`、L38 `"graph_results"`，且 L15 自述 `"method": "纯 Python stdlib (json + hashlib + math), 0 numpy 依赖, 0 LLM"`。

**Critique。** 势函数判据只在 3/22 图上成立、复制子与 ESS 判据 0/22 成立——这是**已经跑完的负向结果**。"无直接对应"只对"蒸馏者-防护者"这个具体配对成立；作为"22 图上的博弈观测量"，盘上有对应。

**Doubt。** 这两个量是为别的问题设计的，能否充当蒸馏博弈的观测量，属再拟合。

### Seed S-34 — 推理链不在盘上，长度代理在

**Evidence。** 种子写"V7 verdict 是判别 verdict，推理链样本无直接资产"（L232），资产标"无直接对应"（L226 一带）。盘上唯一与推理过程同维度的数字是 `reasoning_tokens`（`…/minimax/artifact_v_2026_09_16.json` L760 = 102，同记录落盘答案只有 `"No"`，L748）。

**Critique。** 该种子问"坍缩"，而盘上**没有任何"学生的输出"**——观测对象本身不存在。所以这不是"资产不足"，是"对象缺失"，比"资产不足"更强。

**Doubt。** 这条结论只覆盖 by_model 层。

### Seed S-38 — 同一口径重跑，七到八成载荷变了

**Evidence。** 种子写"V2/V3 多 backbone × 多 cell 设计本身复现性友好"（L260）。我把 `_p_l_v3_vector_embedding_*` 家族里四对**同口径、同日、相隔数分钟**的重跑做了逐行比对（同目录、同 L=30）：

| 口径对（171614 系 vs 172206 系） | 行数 | 不同行 | 占比 | 首处差异 | 字节差 |
| --- | --- | --- | --- | --- | --- |
| doubao-vision-241215 | 62,898 / 62,898 | 52,211 | 83.0% | L18 | +410 |
| doubao-vision-250615 | 62,898 / 62,898 | 46,057 | 73.2% | L18 | +1,089 |
| doubao-vision-250328 | 62,898 / 62,898 | 48,053 | 76.4% | L2067 | −1,216 |
| qwen3-emb-4b（170828 vs 172206） | 78,258 / 78,259 | 54,641 | 69.8% | L18 | −432 |

抽样的不同行是**逐 cell 的向量分量本身**（同一位置：`0.002685546875` 与 `0.005828857421875`），不是末位抖动。四对里唯一被声明的变化写在文件末行 `note`（两件都在 L62896）：172206 那件在 171614 的同一句后追加了 ` | β recomputed 2026-09-17 with OR-match formula (uniqueness=1-mean-offdiag, slope vs cell_index, seed=42).`

**Critique。** 声明的改动是 β 的重算，实际逐行差异却是七到八成、且落在向量分量上——**声明的改动范围与实际的差异范围不成比例**。因此"多 backbone × 多 cell 设计本身复现性友好"在盘上被这一族文件直接反驳：口径的**覆盖广度**（八个口径）不等于**重复性**（同一口径两次跑不出一致的向量）。这是本轮我读到的最强的一处"盘上事实与种子表述相反"。

**Doubt。** 我只做了行对行的位置比对，**没有逐 cell 对齐键**；若两次运行的 cell 顺序不同，占比会被高估。但四对行数一致、且首处差异之前的内容逐行相同（250328 那对前 2,066 行全同），与"顺序一致、数值不同"相容。另注意 241215 那对字节差只有 +410 而不同的行有 52,211 行——说明差异不是长度变化造成的，字节数相近是巧合。真正原因（服务端不确定性，还是两次输入不同）我无法从盘上判定。

---

## Engagement（续）— 三处本轮新核到的横向事实

### 横向事实一 — 同一个信任锚被三件独立制品钉住

`03c6c01f3697`（`verifier/handoff/KT_ABC1_anchors_sha256_12.json`，6,680 B）至少被三件互不相关的制品以同一语义引用：`p_m_attack_surface_cost_results_2026_09_16.json` L18 `"5_anchors_file_actual_sha12": "03c6c01f3697"`；`boss_pa_2_potential_game_result_2026_09_15.json` L22 `"anchor_json_sha12_expected": "03c6c01f3697"`（L23 为同名字段的自报一致）；`boss_pa_3_replicator_dynamics_result_2026_09_15.json` L40–L41（observed 与 expected 同值）。这是"可审计"这套说法里，我唯一核到**跨三件制品复现**的机制；建议在 S-17（跨模型溯源）里把它当正向样本，而不是把可审计当作一般主张。

### 横向事实二 — 跨层命名不稳定有第三个实例，且这个最硬

此前我核到两处：收件人 `coze` 与制品目录 `coze` 同名不同物；资产层 `minimax` 与结论层 `minimax-m3` 不同名。第三处更硬：`corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json`（13,150 B · `39732A92B5C9`）L2 声明 `"schema": "kimi_artifact_v/1.0"`——一件 GLM 名下的制品用了 kimi 的 schema 名。这不是命名松散，是**同一个 schema 名被跨层复用**，会直接破坏"按 schema 名判定制品来源"的任何自动化。

### 横向事实三 — 预登记落在语料层，不落在结果层

`corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json`（19,685 B · `268AB1239A8A`）L3 `"preregistration"`、L8 `"three_way_design"`、L14 `"n_natives": 15`——这是一件盲测**预登记**，它落在 `corpus/` 而不是 `results/`。若 V4 要谈预登记纪律，这条说明预登记在盘上的位置与结论层不一致；找预登记不能只搜 `results/`。

---

## Engagement（续三）— 八条候选种子（邀请函 §3 未覆盖，供收录决定）

40 条几乎全部把"蒸馏"预设成**第三方对教师的提取**，以及**教师对提取的防御**。下面八条锚在它没有覆盖的问题面上；前七条各有盘上承载物，第八条没有。每条按邀请函自己的种子格式写（problem／why interesting／related asset／nature），便于 §3 直接取舍。引用行号我已逐条用 `Select-String` 复核。

### N-01 — 端点在不在冒充它自己宣称的那个教师

**problem。** 第三方只拿到一段 API 文本时，能不能先问一个更靠前的问题——**这次响应是不是真由该端点自称的那个教师产生的**，而不是被静默换上的更小、更便宜的替身产生的？

**why interesting。** 蒸馏最要命的形态可能不是第三方提取，而是**供应方把旗舰名头挂在一个学生身上**。此时检测者的参照系本身就是被替换物：任何基于输出的教师指纹，都在拿一个已经不对的基准做比对。S-07 与 S-17 默认参照系可信；这条问的是参照系本身，而它比"检测蒸馏"更靠前。

**related asset。** `results/_p_l_v3_phase2_closedsource_report_20260917_175544.md`（5,909 B · `02443DD300CE` · 112 行）。L18 是该检查的标题行（`## 1. 加速器降级欺诈验证 (response.model == request.model)`）；L20–L24 是按 backbone 记录"响应的模型标识是否等于请求的模型标识"与逐 cell 降级出现次数的表；L62–L66 另有一张按 PRIMARY 汇总的表，含一列 `n_downgrade`（三行均为 0）；L81 把同一检查写成一条运行级声明；L85 给出 baseline 文件的 `sha256_12 = 5149f5cafcf9`。我只引用机制与计数列，**不引用**该报告的终态标签行。

**nature。** re-fit hypothesis。该检查是为一次向量嵌入稳健性跑批建的**运行完整性护栏**，不是为蒸馏检测建的仪器。

This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.

### N-02 — 归因的分辨率下限：同族隔代能不能分开

**problem。** 同一模型族相差一个发布版本的两个端点，黑盒指纹能不能把它们分开？还是只能把"这一族"与"别的族"分开？

**why interesting。** 这决定"它出自哪个教师"在**版本粒度**上是否可答。若不可答，一切溯源主张就只能说到族一级，"某学生蒸馏自 X 版"这类说法就超出了证据能支持的范围。S-17 只问"能不能溯源"，没问"溯源能细到哪一档"。

**related asset。** `results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md`（19,548 B · `2E3EC17259E2` · 227 行）。§2 表 L41–L46 给出各端点与文件 SHA-12；§3 表 L54–L71 是跨 backbone 的 β 区间对照。四个同族版本两两的六对（L54、L55、L56、L63、L64、L71）区间**全部重叠**；但重叠不是干净的族／版本判别器——同一张表里跨架构的 `qwen3-emb-4b` 与同族基准**也重叠**（L58、L66、L73），而 `qwen3-emb-8b`（L59、L67、L74）、`bge-large`（L60、L68、L75）、`e5-multi`（L61、L69、L76）、`gte-large`（L62、L70、L77）的第二列区间与同族基准**不重叠**。也就是说：同族隔代分不开，但"分不开"并不唯一指向同族。四件同批次（后缀 `_20260917_172206`）的嵌入记录我逐件复算过 SHA-12，与报告 §2 一致。

**nature。** re-fit hypothesis。该资产是为"向量嵌入端点稳健性 + 跨架构对照"建的，不是为归因分辨率建的。

This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.

### N-03 — 能力是被训练装进去的，还是被上下文装进去的

**problem。** 只看输出，能不能区分某项能力是**训练期**装进去的（蒸馏／微调），还是**推理期**用外部上下文装进去的（检索／长提示）？

**why interesting。** 蒸馏者可以根本不训练。如果检索增强与训练在输出上不可分，那么"防蒸馏"只防训练通道是防不住的——防的对象必须包含推理通道。反过来，检测者若把"像教师"当成"被蒸馏过"的证据，会把所有用检索的独立模型误伤。这是 S-17（出自谁）之外的另一问：**用哪种机制装进去的**。

**related asset。** `results/deposon_v41_flash_rag_baseline_2026_09_10.json`（101,484 B · `6754D2655E0A` · 1,367 行）：L6 `"context_top_k": 3`、L7 `"concept_count": 22`、L19 `"chat_calls": 30`、L21 起 30 个 cell，每个 cell 带一个显式的检索注入字段（L36、L80、L124…）与 token 用量分解（L49 `"cached_tokens": 512`、L60 `"reasoning_tokens": 234`）。我**不引用**该检索字段的文本内容（属提示词层）。对照侧：`results/deposon_dpath_cross_modal_2026_09_10.json` L2233–L2237 的 `comparison` 块给出同一模型在四种上下文条件下的答对数——无检索 26/30（86.7%）、旧检索 24/30（80%）、Feshbach 检索 25/30（83.3%）、跨模态检索 25/30（83.3%）。

**nature。** re-fit hypothesis。这两件都是"检索帮不帮得上忙"的对照实验，不是"能力来源归因"实验。

This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.

### N-04 — 评测的参照推理本身就是某个模型的输出

**problem。** 如果评测用的参照推理与参照分解本身是第三方模型生成的，那么任何以它为参照训练出来的模型，**在"蒸馏"这个词被提起之前就已经是那个模型的下游**——这时"独立训练"该如何定义？

**why interesting。** 这把"数据污染"和"蒸馏"合并成同一件事。S-36 问"GT 由谁标"，本条问的是：**当 GT 已经是模型产物，标注主体的动机问题就不重要了**。任何以该参照集为奖励信号的模型，其行为都继承了那个参照模型，而这一点既不体现在权重里，也不体现在输出分布里——S-07／S-15 那类黑盒检测从原理上就看不见它。

**related asset。** `results/deposon_benchmark_v1_4_strategyqa_details.json`（235,779 B · `A63EBEA7B29A` · 8,098 行）：逐题记录，每题含一个分解块（L5–L14）与一个推理链块（L15–L19），两块各带一个来源标签。我本机统计：全文 **396 处来源标签，396/396 取值全部相同**，均为 `kimi_api`（例：L13、L18）。另一侧：`corpus/v20/strip_captions_22.json`（12,798 B · `6A2656878745`）里 22 条语料中有 **6 条**的 `structure` 字段为 `llm_generated_dag`，即语料层本身含模型生成结构。

**nature。** 其中"396/396 来源标签取值相同"与"6/22 条语料标记为模型生成结构"是 on-disk fact；把这两条读成"污染与蒸馏同源"的问题是 re-fit。

This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.

（一处我没能定的连线：`kimi` 这个名字也出现在 V7 九模型表的 `kimi-k2.7-code` 一行；`kimi_api` 与它是否同一端点，我无法从盘上判定。）

### N-05 — 指纹比它指纹的那个东西活得久

**problem。** 当某模态唯一幸存的记录只剩派生量（嵌入、相似度矩阵），而原始制品已不在盘上时，派生出来的溯源主张还能被**复算**，还是只能被**重申**？

**why interesting。** 反蒸馏主张几乎总是在"教师原始数据已不可得"的条件下做出的——"只剩派生记录"是常态，不是例外。如果一个指纹的原始承载物已经消失，"这个指纹属于谁"就无法再被独立复核，只能靠记录自证。这恰好是 S-18 想要的那种"最硬证据"最脆的地方。

**related asset。** `results/deposon_dpath_cross_modal_2026_09_10.json`（75,964 B · `AB0C2EAFF0D1` · 2,253 行）：L9 记录 22 个渲染图路径（`figures/v3x/corpus_pngs/graph_001.png … graph_022.png`），L11–L12 记录图／文嵌入维度均为 2048，L28 `"image_image_offdiag_mean": 0.965`、L29 `"text_image_offdiag_mean": 0.2799`，L33 起 30 个 cell。**我本机核实：`figures/v3x/corpus_pngs/` 目录存在但文件数为 0，全仓 `*.png` 数为 0**——该记录的图侧原始承载物已不在盘上，只剩派生嵌入与相似度记录。（该文件另含一个网关地址与一个运行时读取的凭据字段，我按纪律不复现。）

**nature。** 其中"图侧原始制品已不在盘上"是我本机核实的 on-disk fact。

This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.

### N-06 — 语义指纹链能不能当派生证据

**problem。** 一条把"内容标识 + 语义指纹"逐节点串成哈希链的记录，能不能用作"某产物派生自某内容"的证据——尤其当语义指纹是低比特、会碰撞的时候？

**why interesting。** 这是 40 条里唯一在盘上已有**原型**的建设性反蒸馏思路：它不是 token 水印（S-19），而是把"语义近邻"编进链。但它的分辨率是硬的：22 条内容的 12 位语义指纹只落到 **6 个不同取值**上，而内容标识哈希逐条唯一。链能证明"逐条同源"，语义层却证明不了"这条和那条不同"——派生证据因此是**分段**的，不是逐条可分辨的。这给 S-13／S-18 一个具体的分辨率下限。

**related asset。** `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json`（18,104 B · `B5873AFB9D29` · 700 行）：L7 `"dual_24bit": "byte_hash[:6] + semantic_hash = 9 hex (36 bit)"`、L8 `byte_hash` 定义（`SHA-256(caption_id)[0:12]`）、L9 `"semantic_hash": "12-bit LSH: 22 caption SVD-2 坐标 x 12 随机超平面 (np.random.seed(42)), 符号位 -> 3 hex"`、L10 指向 `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md`、L12 记一处实现分歧并指向 `deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py`；L41–L46 是链约定（L43 `link_i`、L45 `merkle_root`）；L47 起 22 条逐条记录（如 L54–L56、L74）。我本机统计 22 处 `semantic_hash` 的取值分布：`2fd`×10、`2dd`×6、`6d8`×2、`498`×2、`6dc`×1、`2dc`×1——**6 个不同取值覆盖 22 条内容**。

**nature。** re-fit hypothesis。该链是为语料内容一致性核验建的，不是为派生归因建的。

This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.

### N-07 — 核验方的"找不到"与"没痕迹"不可分

**problem。** 当一个独立核验方报告"没有发现痕迹"时，如何区分"制品确实没有痕迹"和"核验方根本没定位到它该核的那份材料"？

**why interesting。** S-37 讨论假阴的代价，但默认假阴来自**信号弱**。这条的点是：假阴还可以来自**定位错**，而且它恰好发生在"独立性最强"的那种核验流程里——最强的方法学承诺（不调模型、不经代理、凭据不入盘、不动冻结件）与最弱的定位鲁棒性可以并存。任何把"独立复核过"当证据的蒸馏检测，都会继承这个漏洞。

**related asset。** `results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json`（5,916 B · `1E4C065DA058` · 196 行）：L6–L16 是核验方自设的独立性约束（`no_llm`／`no_proxy`／`no_gateway`／`no_key_in_prompt_json_disk`／`no_18_frozen_touch`／…／`observer_0_active_0_evaluation_0_advice`），L18 起逐件给"期望哈希 vs 实算哈希"的对照；**L179–L183 的子核验直接返回 `"error": "only 0 captions, need 22"`、`"caption_count": 0`，其定位路径为 `corpus\v20\index.json`**——即该独立核验在此项上**定位失败**；L193 记录核验方的中立约束。

**nature。** re-fit hypothesis。该流程是为冻结件哈希一致性核验建的，不是为蒸馏检测建的。

This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.

### N-08 — 逐代自蒸馏：被吃掉的尾巴

**problem。** 当每一代模型都以上一代的输出为主要教材时，分布里那些低频、长尾、边角的部分是不是在逐代消失，以至于"某一代还是不是原教师的学生"这个问题本身失去意义？

**why interesting。** 40 条里 S-34 说的是**一个**被蒸馏的模型在长链推理上更易坍缩，那是单代内的推理现象。本条问的是**跨代**的累积：如果长尾在每一代都被削薄，那么 S-11 想用的"长尾一致性作蒸馏深度代理"就会失效——因为长尾在一条**没有被任何人刻意蒸馏的合法自训练链**里也会消失，检测者会把正常的自训练史误读成蒸馏。要拆开这两者，需要一个"未被蒸馏也会退化"的零假设，而这个零假设目前在盘上没有任何承载。

**related asset。** **no on-disk artifact.** 盘上没有任何多代自蒸馏产物，也没有任何跨代分布记录；`corpus/v20/strip_captions_22.json` 只提供单代静态语料（22 条中 6 条标记为模型生成结构），不含世代链。

**nature。** pure speculation。

This is pure speculation; no on-disk artifact supports it.

**本节收尾一句。** 八条里七条有盘上承载物、第八条没有；第 8 条按 §3.0 L140 的取值域是 `pure speculative`，其余七条的 nature 我按邀请函 §2 的用法写成 re-fit。另：这八条本身也构成对我上面 S-36 主张的一次检验——如果"谁来标资产可用性"是真问题，那么这八条的 nature 标签就该由别人复核，而不是由标出它们的人自己写。

---

## Engagement（续四）— 一处与邀请函 §2.10 相抵触的盘上事实：蒸馏在本项目里被正式测过，且卡在 deposon 一侧

邀请函 §2.10 L120 有两句：第一句是 V1–V3 磁盘上不存在任何蒸馏、反蒸馏或防蒸馏的**实验资产**；第二句是 **V4 是 deposon 第一个触碰该主题的 V 层级**。种子场 L290 的对应措辞是"V1~V3 磁盘**无**任何蒸馏/反蒸馏/防蒸馏实验资产——V4 是该方向全新起点"。

第一句**在字面上成立**：`results/` 下确实没有任何一件蒸馏实验的结果文件。第二句不成立。下面是盘上的完整链条，六环，每环都可在所述路径与行范围重新推导。

**第一环：主题被一份冻结规格正式指定为"能否证伪自身主张"的判据。**
`docs/V3X/KT_B1_SPEC_V0.1.md`（35,688 B · `0410CA0FBDAE` · 629 行）。L254–L256 把要防的失效模式写成一句话：三个平凡基线（Sinkhorn OT／KD／LLMLingua）若能在同一批 200 节点数据上达到同样的守恒审计检测力，则 deposon 的守恒检测力**无差异化**。L258–L265 是 OT 项，L267–L274 是 KD 项（Hinton 2015 的 KD 框架 + KL 散度 + softmax 平滑，200 节点，问的是 0.95 是否是默认下限），L276–L283 是 LLMLingua 项；三项各绑一个已冻结的脚本哈希（依次 `19325960b8be`／`1781ea2f742d`／`c0b55e0385a4`，字节数 14,956／14,224／13,966，见 L264、L273、L282 与 L534–L536）。L269–L272 写明触发后的处置：主张需降级、差异化须另证。L425 是这一族失效的判死行，L427–L430 是撞上后的处置条款，L495–L502 是一张开放项表，为三项各指定了待办时点与承担方。

**第二环：这份规格本身是 18 个冻结锚里的第 14 项。**
`results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json`（4,202 B · `928794710241` · 150 行）。第 14 项的 path 在 L109，expected 与 actual 同为 `0410ca0fbdae`、match 为真（L110–L112）；L144–L146 汇总是 18 项全匹配。（同一份清单的第 12 项是 V7 报告，第 15–17 项是 KT_C1／KT_D0／P_G 三份规格。）

**第三环：它被真跑过，第一次就崩了，三个一起崩。**
`docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md`（15,478 B · `4485443757e7` · 309 行）。L27–L37 是九项基线自测总表：A 组三项通过、C 组三项通过、**B 组三项全部记为失败（bug）**，失败原因是同一处——`_extract_200_questions` 用了不存在的字段名。L156 写明根因：该批数据用 `pred` 且取值是 Yes/No 字符串，脚本按浮点读。L159–L174 是 KD 那一项的完整自测块：T=2.0、alpha=0.5、lr=0.001、epochs=50、batch=32，规模 200 节点／200 题／每题 100 样本，读到的数据侧守恒残差是 2.220e-16，随后抛出类型错误。

**第四环：修了字段名，仍跑不动——因为答案是字符串。**
`docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md`（5,615 B · `9352a1675b10` · 103 行）。L44–L46 记录三项在字段名修好之后的新错误：字符串 `'No'` 转浮点失败。L48 明说三项退出码均为 1，且**均未输出主指标**。

**第五环：再修一次，KD 的数字出来了。**
`docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md`（11,478 B · `baef94e393de` · 215 行）。L78–L86 是三项"修复后首次跑通"的表。其中 **KD 项给出的失真量是 0.0028**，而同一行里 deposon 一侧写的是 0.5 并标注为占位值；三项的裁定被记成同一个中性档（档名我不复现，见 L82–L84 原文）。L86 的解释是：三项全落该档是预期行为，因为 deposon 的失真量是占位值。L136 另记一事：这三项基线在冻结区核验里全部与锚不符（0 匹配／3 不符），原因是它们发生过未报告的漂移（脚本哈希从 `19325960b8be`／`1781ea2f742d`／`c0b55e0385a4` 变成 `7c2b41c008a5`／`8c6e98034005`／`2ded5cf0e863`，见 L123–L125）。

**第六环：为什么判不了差异化，报告自己说了——因为卡在 deposon 一侧。**
同文件 L178 记：锚文件本身未更新，仍保留旧哈希，上表即替代关系说明。L179 是遗留事项第二条：三项裁定全落中性档，因为 deposon 的失真量是占位值（0.5／0.05），**不标榜差异化**；若要真正判定差异化，需**从该批数据的守恒残差（2.22e-16）反向估计 deposon 的失真量**。

**这条抵触有多重。** 我不想把它说成"邀请函错了"。准确的说法是三层。

（一）第一从句真、第二从句假。真正被反驳的是"V4 是第一个触碰该主题的 V 层级"——一份冻结的 V3.X 规格不仅触碰了它，还把它写成判据，并且真跑过。

（二）更重的后果不是"盘上少一件资产"，而是**这里有一个未闭合的环，且闭合点在 deposon 一侧**。这个问题——deposon 的失真量是否与一个平凡的蒸馏基线有差异——被提出、被脚本化、被冻结、两次尝试、修好、跑出数字，然后被留在中性档，而记录下来的理由是 deposon 自己的那一侧是占位值。也就是说：把 V4 主题卡住的不是蒸馏侧的缺失，是 deposon 侧从未把 0.95 这个数**测**出来过。

（三）因此这条不是"V4 从零开始"，而是"V4 从一个未闭合的环开始"，并且环的接口已经写好了：从守恒残差反向估计。它对 §3 与 §4 都是可直接用的——它把 S-21（信息瓶颈）从无先验的思辨变成有一条可引用的既有对照，同时给出一条比 40 条种子都更具体、也更难堪的开放问题：**如果 deposon 的失真量至今是占位值，那么 40 条种子里凡是把 0.95 当作既定事实来推理的，推理前提是什么？**

**一处方向性歧义，我拒绝替它读。** KD 测出 0.0028，deposon 一侧是占位 0.5。这两个数哪个方向算"更保真"，取决于"失真量"这个词在本项目里的约定，而该约定在盘上是**自相矛盾**的：§2 的对照表（L62）把 `≥ 0.95` 记成达标，§4.2 的问法（L269）是"0.95 是不是默认下限"，而阅读清单对该项的描述写成"保真度 ≥ 0.95"。同一个符号在同一份规格里既表示"越大越达标"又表示"越大越不特殊"。我只报数字与这个歧义，不给方向性结论。

**可见性（这条最可操作）。** 上述三份文档——自测总表、字段名修复报告、返工报告——在邀请函中出现 **0** 次，在 prompt pack 中出现 **0** 次；`KT_B1_SPEC`、`BOSS-B2`、`BOSS-B3` 同样 0 次；连 `Knowledge Distillation` 与中文"蒸馏"这两个词，在邀请函与 prompt pack 里也都是 **0** 次。（核对方式：两份文件逐串匹配；工作区六棵子树共 894 个 md/json/py 逐文件扫描，`1781ea2f742d` 等脚本哈希与 `boss_b2_kd` 等脚本名的命中全部落在 `docs/V3X/` 的四份文档内。）**结论：只读邀请函 + 照 prompt pack §4 清单行事的收件人，无法看到该主题曾被触碰过。** 这不是我的推断，是清单覆盖面的直接结果——若 PI 认为 §2.10 那句话需要修正，最省的修法是把这三份文档补进 §4 清单，而不是重写那两句话。

**另一处较弱的抵触（同一节，V7 报告）。** 邀请函 §2.5 L87–L89 说 V7 报告"记录了判别任务中的扰动实验"。`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md`（38,545 B · `4A08521F8DE1` · 620 行）逐串匹配"扰动／干扰／噪声／注入／篡改／变形／鲁棒"与 `disturb`／`perturb`／`adversar` 全部为 0 命中（`noise` 有 39 处、`attack` 有 3 处），其 42 个小节标题（L23–L596）里没有一节是关于扰动的；它实际有的是一个以噪声命名的裁定档（§3.2，L240）和一张 BOSS 裁定分布表（§4，L341）。所以 S-10 的资产行与 §2.5 的描述，在该路径与行范围上无法被重新推导出来。这条比上一条轻：该文件确实记录了"撞上平凡基线后主张被拍平"的同类事件，只是不在扰动这个名义下。

**两处现成的零值，种子场没提，清单也没收。** This is a re-fit hypothesis; the artifacts were not built for this purpose; no calibrated finding is claimed.

（1）`results/_p_l_v3_vector_embedding_*` 家族共 **21** 个文件，其中 19 个 JSON：4 个在第 5 行自报 `INCOMPLETE - no embedding endpoint available`（`…_142748` 那一批），2 个逐格全部记为失败，其余 13 个体量在 1.0–3.9 MB（含逐格 2048 维向量；其中 `…250615_171614` 一件我核到 `cells_embedded 30 / cells_total 30`，见该文件 L62872–L62876）。这是盘上唯一一类"同一批固定输入 × 多个模型 × 部分模型有两次独立测量"的表征数据，也就是任何表征层主张所必须对照的那个零值——而我在 S-38 一节已给出这 4 对逐行差异 69.8%–83.0% 的实测及其哈希。**这 21 个文件，一个都不在 prompt pack §4 的 31 条清单里。**

（2）逐题共错，这一处我自己算了：`corpus/v20/by_model/minimax/artifact_v_2026_09_16.json`（25,347 B · `9E1CCBDCEACC`）保留 30 题逐题对错，`results/deposon_v2_phase1_60cells_2026_09_11.json`（85,508 B · `A18BBC703B42`，其单一切换模型见该文件第 5 行）保留 60 题逐题对错；两者共享 **15** 个完全相同的题号（`gsm8k_1`…`gsm8k_15`）。在这 15 题上：前者 13/15、后者 14/15、**双方同时错 = 0**（前者独错 `gsm8k_1`、`gsm8k_12`；后者独错 `gsm8k_7`），一致率 0.8000。这是最便宜、最标准的黑盒蒸馏信号，也是盘上唯一本来就能算出来的那一个，而它给出的值是零。15 题里只有 3 个错，信息量极小——但"可算"与"值为零"这两件事本身是盘上事实。

**本节收束一句。** 这条抵触使 §2.10 的那句话需要一次修正，也把 S-21 从"无先验的思辨"变成"有一条可引用的既有对照"——但那条对照的两侧数字不可比（一侧是占位值）。我把它写进正文而不是悄悄绕过：这不是我发现的矛盾，而是我发现**盘上早就有这个矛盾，且它从未被任何一轮报告闭合**。

---

## 边界

对 V1–V3 只读；本会话未修改任何冻结资产。接受时点抽查 8/8 冻结 SHA 未变：`03C6C01F3697`／`9E1CCBDCEACC`／`268AB1239A8A`／`6A2656878745`／`063AC8D00542`／`4505CCA79C15`／`C7C59E0D2F6C`／`9E99DCC4D920`。本回函不含密钥、模型端点或专有提示词（一处卫生提示：`deposon_v3_v7_summary_2026_09_11.json` L42–L43 含一个网关 URL 字段与一个已掩码的凭证字段，其值我不复现）。未提出任何框架（无 track／checkpoint／量规／排序／收件人分配）。依 §6 shape prompt 的禁令，本回函不引入判裁 token；上文若出现磁盘字符串，仅作引文标注，不代表本回函的判断。为便于 PI 复核，我把全部"像被禁词"的出现位置交代清楚（逐串区分大小写核对）：§6 所列的判裁词表，全项在本回函中 **0** 次；§6 所列的组织类词表，除三个以 D 加数字构成的时点记号外全项 0 次，而那三个记号的全部命中都是非引入性出现——（一）SHA-12 十六进制前缀的偶然子串（`AB0C2EAFF0D1`、`78AC391D16FC`、`02443DD300CE`、`D511C545F88E`、`3D54B277620E`、`F02B3EEE8D6E`），（二）一处逐字引用的磁盘状态串（`_pg_v01_compute.py` 的 `status` 字段内含一个未来时点记号），（三）一处磁盘文件名（`docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md`）。这三类都是 (H) 所要求的逐字引用，不是本回函引入的组织概念。另记一处**自身偏离**：本回函约 15,000 字（中文字符 13,020 + 非中文词元 2,005；若按中文词数粗算约 10,100 词），超出 §6 偏好的 4,000 词上限。这是应主人在 21:08 的追加要求（把第二轮头脑风暴、三处横向事实与八条候选种子一并写入本回函）而扩写的，不是无意识的膨胀；我把它写出来而不是悄悄越过，是因为 §6 要求自身矛盾须 surface。若 PI 需要合规长度的版本，我可以另出一份 3,000 词以内的短版（只保留 S-36、S-38、逐行重算六条与三处横向事实），本文件即作为其附录。AI 不是作者；我的贡献是被致谢的参与。

---

## Closing

**(a) 最值得推进**：S-36。它是唯一一个能同时吃掉"资产层"与"样本层"两级 GT 的种子，而且盘上已经给出了一个真实的反例——种子场作者自己就是在未打开资产的情况下标注了 21/40 条 `pure speculative`（`_v4_brainstorm_seeds_2026_09_20.md` L292），这让 S-36 从"谁来标样本"升级为"谁来标资产可用性"，后者恰是 V4 这一轮唯一真实发生过的标注事件。**(b) 最不产出**：S-28 与 S-29（蒸馏者-防护者博弈、5 年长期均衡）。理由不是它们不重要，而是它们要求的观测量是**跨期**的，而这套栈是**单期冻结**的——盘上最长的序列是 V2(09-11)→V3(09-11)→D7(09-18) 共 7 天、且三者的观测对象都是判别任务，任何"是否收敛到均衡"的回答在这里都只能靠外部假设补，种子本身的"why interesting"无法被盘上资产兑现。**(c) 我希望邀请函收录但没收录的种子**：两条。第一条是"**资产可用性标注**"（可置于维度 7）——当种子场的作者只做了存在性确认、协作方被要求"自行二次核对"时，一条种子的"性质"标签应当由谁、以何种可复现的方式给出？它的 Related asset 是实的（`_v4_brainstorm_seeds_2026_09_20.md` L292 的自述 + `deposon_v3_v7_summary_2026_09_11.json` L290 的五锚记载），因此按 §8 L403 的措辞它**不是**纯思辨。第二条是"**派生列的可复算性**"（可置于维度 7）——一个表格里由其它列算出来的列（如 `distance_to_ideal_1_0_0`、`rank`），是否应当能从该表自身重新推导出来？这条的 Related asset 也是实的：`deposon_v3_v7_summary_2026_09_11.json` L121–L129 的九行里，有七行的距离值无法用该表自己的三列复算，而 `rank` 列与打印距离不单调。补一条：40 条未覆盖的问题面里，我另列了八条候选种子（N-01…N-08，见「八条候选种子」一节），其中七条盘上可锚，供 §3 决定是否收录。再补一条：邀请函 §2.10 L120 的第二句（V4 是第一个触碰蒸馏主题的 V 层级）与盘上四份 V3.X 文档相抵触——详见「续四」一节；那一条同时也是我建议补进 §4 阅读清单的资产。**(d) 我建议加入 §4 的开放问题**：*V1–V3 网格内部是否存在互为严格单调变换、或互为同一构造恒等式两种写法的统计量，使得"多处一致"成为保序伪影而非独立证据？*——这个问题在本轮已经不是猜想，而是能在盘上直接核到两处实例：一是 `deposon_v3_v7_summary_2026_09_11.json` L121–L129 的九行逐行满足 `T + R + A = 30`（我逐行加总，九行无一例外），故 `A ≡ 30 − T − R`，三通道只有两个自由度；二是同一对 (T,A) 在同一文件 L147／L148 被算成两个不相等的相关系数（`_count` 的 −0.81 与 `_fraction_v5` 的 −0.92），而皮尔逊相关对正的单位缩放不变。一个继承了保序恒等式的检测器，会把"同一模型的两种写法"读成"两份独立证据"；这套栈里恰好已经有这样的两处。

— coze，2026-09-20
