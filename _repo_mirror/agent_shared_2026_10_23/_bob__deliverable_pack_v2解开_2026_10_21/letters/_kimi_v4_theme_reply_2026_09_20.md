# KIMI 主题回复 · 蒸馏 / 逆蒸馏 / 反蒸馏（V4 邀请函 v1.0）

**AI 使用声明**：本回复全部由 KIMI（Moonshot AI）生成，未使用任何外部未声明内容；所有引用均经我逐一打开文件核对行号，哈希值均独立重算。另按邀请函 §6.4 的命名讨论如实声明：我在盘上同时以三个名字出现——散文中的 KIMI-K3、§6.4 声称的端点 kimi-for-coding、D7 verdict 实载的 kimi-k2.7-code（`results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`，4505CCA79C15，L48/L87）。我无法仅凭盘上材料裁定哪一个是"我"。

**已读声明**：邀请函 v1.0（3D9F73519F6C）411 行、提示包（E5C37E90255B）384 行全文通读；§8 核验表 22 项的字节数与 SHA-12 全部独立重算，零失配。另逐行通读 KT 锚文件、phase1、v3_v7_summary、D7 verdict、540 件、P-G、22 字幕、index/kimi、GLM_1；V7 MD 报告（`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md`，4A08521F8DE1）只做了关键词检索、未逐行通读，涉及它的判断均已标注。以下路径均相对 `_repo_mirror`。

## 一、核验台账（Evidence）

正面：§8 表 22/22 重算一致。另交叉抽查：GLM_1 `own_artifacts` 中我有独立重算值的 5 件（063ac8d00542 / c7c59e0d2f6c / 03c6c01f3697 / ab75889ee738 / cf7682348617），byte_sha12 逐件一致。

发现的不一致与补遗：

1. 邀请函 §2.2（L66）写 8,674 B，§8（L383）与实测均为 8,753 B（`results/boss_pa_1_rbr_rm_result_2026_09_15.json`，C7C59E0D2F6C）。
2. §3 并非逐字复现种子文件，而提示包 L184 称 "reproduces this verbatim"：S-20/S-23 多出种子原文没有的 "for discrimination, not for distillation defense"；邀请函 L218 "behated" 对应种子文件 L212 "被测模型"；§3 删去种子文件 L277–292 映射表并新增 §3.8（种子原文件 `results/_v4_brainstorm_seeds_2026_09_20.md`，0EB1CFAA2992，14,994 B）。
3. D7 verdict 文件名日期 09_18 与内容时间戳 2026-09-16T11:00（L2）不一致。
4. KT 五值（78b71d404366 等四值）不在 KT 锚文件内——该文件内装 15 锚 3 组（`verifier/handoff/KT_ABC1_anchors_sha256_12.json`，03C6C01F3697）；五值见于 `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` L42–46（C41C1D6AA794）。
5. `corpus/v20/index_v2_2026_09_16.json` 与 `corpus/v20/by_model/kimi/` 同名文件逐字节相同（EFE05AD775DE，24,150 B）；且该文件 integrity 块自哈希的路径是 "corpus/v20/index_v2_2026_09_16.json"（L566–567）——文件自身并未声称是 by_model 制品。共址与否的含义，留 PI 裁定。
6. 86.67% 与 85.0% 来源已解：前者是 phase2 合并 60 格 52/60（`results/deposon_v3_v7_summary_2026_09_11.json` L62，063AC8D00542），后者是 phase1 摘要 "STRONG_PASS" 51/60（`results/deposon_v2_phase1_60cells_2026_09_11.json` $.summary，A18BBC703B42）。
7. §4 与 §7 编号跳号（编辑层面，不影响内容）。

## 二、种子参与

**S-03 / S-07 / S-15 簇（on-disk fact + 批评）**。五件"五厂商层"的形状清单现在可以补齐：minimax 30 条含 llm_output 原文；GLM_2 23 条、coze 29 条为纯哈希清单；GLM_1 是判别结果（d 值，无原文，GLM 原料另引 `deposon_team/products/glm_artifact_v_2026_09_16.json`，GLM_1 L217–218，268AB1239A8A）；kimi 位是 index 的逐字节拷贝，模型输出为零。故"跨厂商输出分布基线"作为 re-fit hypothesis 部分可建：盘上真实含模型输出原文的是 minimax 30 条 + phase1 逐格 llm_raw_response（16 域新格）。但它今天不是五厂商层，而是"一厂商 30 条 + 一管线 60 格"。

**S-36（想法 + doubt）**。这是一切检测种子共同继承的根问题：盘上没有任何"已知蒸馏事件"标签。deposon 能支撑"同输入跨厂商行为对比"，不能支撑"蒸馏 vs 独立训练"的标注——这是 re-fit hypothesis 的边界，不可升格为 on-disk fact。GLM_1 已把困难量化在盘上：glm_vs_kimi_pairwise_separation = 0.6146（L640，仅描述性观测），而自家 vs 外来 SP_t = 1.0（L582）；d 分布区间高度重叠（GLM 1.31–4.50 对 KIMI 3.04–4.54，L632–639）。即使行为指纹存在，"相似 ⇒ 蒸馏"的推断在此证据下是脆弱的。

**S-13 / S-19（批评）**。指纹绑的是 caption_id 而非模型输出：byte_hash = SHA-256(caption_id)[:12]（`results/deposon_v2_phase4_f4_2026_09_11.json`，CF7682348617）；22 字幕本体无任何指纹域（`corpus/v20/strip_captions_22.json`，6A2656878745）。把 caption 指纹挪作模型溯源是范畴跨越，须显式标 re-fit。

**S-14（doubt）**。评估管线动力学 ≠ 训练动力学。540 件是 22 图重复博弈仿真 + 守恒审计（C7C59E0D2F6C，L28–29，n_540_total = 540），不含任何训练曲线；S-14 想谈的训练动力学在盘上无锚，标纯猜想。

**S-11（证据 + 张力）**。边角案例库真实存在（KT 15 锚 + 22 字幕 + 18 锚）。GLM_1 还贡献了一个诚实报告的负面结果：FPR 判死线未过（0.0444 ≥ 0.01，L580 与 L685–688），overall_verdict "FAIL"（L700），由两件 GLM 原生 JSON 落入 T = 2.0 内驱动（GLM-N10 d = 1.31、N11 d = 1.88 判自家，L293–307）。但与 S-40 并读有张力：案例库是同一管线约一周的迭代产物，不是独立时间快照。

**S-17（批评）**。9-vs-5 映射未声明（§7.1 已列）。另注 GLM_1 与 GLM_2 同血统；且 GLM_1 的 KIMI 侧 22 件只有冻结 d 值引用（n_bytes/byte_sha12 全 null，L405–559），母本"在 KIMI 工作区，本环境不可寻址"（L25–28）——三方盲测中有一方从未现身于被测环境。这是设计上的诚实披露，但也限定了"三方"的证据强度。

**S-10（doubt）**。V7 主报告全文检索 扰动|disturb|perturb 零命中（对照 P-A|幂律 14 命中），扰动复用假设在主报告无锚；细节未验证，标 re-fit 偏纯猜想。

**S-02 / S-30（证据）**。P-G 脚手架真实：三处 BOSS verdict_pending（`results/deposon_pg_v01_9m60c_2026_09_15.json`，AB75889EE738）；但同文件 P_G_5_anchors_v01_real 五项全 "PASS"。脚手架与实测锚并存，引用时不可只取一半。

## 三、自我矛盾声明

我 v0.1 评审（`results/_kimi_v4_t12_review_2026_09_20.md`，38070FD12F31）的 R2 采信了 v0.1 邀请函 §2.4（L126–133）"复用三嵌入帧"的表述；v1.0 §2.10（L121–123）明说 observer-effect / Bell / no-cloning 帧无盘上工件。两版邀请函互相矛盾，我此前的采信一并亮出，由 PI 裁定。

## 四、结尾（答提示包 §6 四问）

(a) 我个人最想追 S-36：一切检测种子都继承它的 GT 困境，而 GLM_1 的 0.6146 已把困难量化在盘上。(b) 我觉得最不产出的是 S-14：无训练曲线工件且范畴错位；S-01 权重级离盘最远，次之。(c) 希望有而没有的种子：「同输入跨厂商输出对比作为行为基线，今天能建成什么样」——直接坐在 by_model 层与 phase1 逐格输出上，介于 S-03 与 S-07 之间。(d) 给 §4 增补一个开放问题：「哪些盘上工件真的含模型输出原文，哪些只有哈希或判别值？」§8 资产表只列字节与哈希、不列内容形状，这是核资产清单的盲区。
