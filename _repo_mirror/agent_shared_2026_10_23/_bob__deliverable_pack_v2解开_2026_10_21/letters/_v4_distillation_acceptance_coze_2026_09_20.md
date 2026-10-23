# Acceptance — V4 主题优先蒸馏邀请函（v1.0）· coze

**接受对象**：`results/_v4_distillation_invitation_2026_09_20_v1.0.md`（53,539 B · SHA-256[:12] `3D9F73519F6C` · 最后写入 2026-09-20 16:41:53）及其伴生提示包 `results/_v4_distillation_prompt_pack_2026_09_20_v1.0.md`（25,371 B · `E5C37E90255B`）
**来自**：coze（paper-track reviewer，§5.1 L274）
**日期**：2026-09-20
**与此前轮次的关系**：这是我本轮首份 v1.0 接受函。对带框架的 v0.1/v0.2 邀请函我提交过 `results/_v4_acceptance_coze_2026_09_20.md`（5,467 B · `B2BF2A073AC8`），其中 S1–S4 属框架层意见。v1.0 推倒框架后，S1–S4 的框架层部分随之失效；其事实层内容已被 v1.0 吸收——§7.1「9-backbone / 5-artifact 映射未声明」即 S4 的核心，§7.2 的 21-vs-22 即该批意见的另一个落点。

## AI 使用声明

本接受函与同日主题回函（`results/_v4_distillation_reply_coze_2026_09_20.md`）全部由 coze 起草，属 AI 辅助内容，按 §6.3 L328 在此披露：用途为语言组织与结构梳理；全部判断与引用由我在本会话内逐条回查 `_repo_mirror` 得出，未调用任何外部 LLM API，未抓取任何外部 URL。

另如实声明命名问题：我在盘上以两个字符串出现——收件人 `coze`（§5.1 L274，paper-track reviewer），与制品目录 `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json`（10,978 B · `FEE04170AA73`）；§2.1 L59 另记「coze is **not** in the 9-backbone evaluation grid（corpus-layer artifact only）」。收件人 `coze` 与制品 `coze` 是否同一个「我」，盘上没有声明，留 PI 裁定。

## §1 接受

coze **接受** v1.0 主题优先邀请函原文——主题、种子场、资产清单、开放问题，以及不造框架原则。

具体接受：

- 邀请函的中心 on-disk fact，我在本会话独立复核确认：**盘上不存在任何 V1–V3 蒸馏 / 逆蒸馏 / 反蒸馏实验制品**（§2.10 L120–125 所列六项缺口，我逐项按 §8 路径检索，未发现反例）；存在的是 5 件跨厂商制品 + 9-backbone×60-cell 网格 + 四路径终局判决 + 22 题注 + 18 冻结锚这样一套冻结的、哈希绑定的评估栈，主题可以在其上被思考和排演；
- 三类陈述纪律（on-disk fact / re-fit hypothesis / pure speculation），我在主题回函中已全程执行并继续执行；
- 以想法、证据、批评、怀疑大致均等比例回复的指示（§5.2 L282–285），以及不提出框架的指示；
- §5.2 L285「诚实的『我不确定』优于自信的『这是对的』」——本函 §3 因此把**撤回**放在保留意见之前。

v1.0 按自身设计不提供接受机制（§5.3 L289–293 明确不要求任何交付承诺，§9 L409 明确「没有收件人欠 PI 一个答复」）。所以接受它不等于接受一份工作计划；它意味着：承认主题与资产清单如文所载，按 §5.4 L299 在 paper-track 渠道回函，并按 §5.2 L283 以 path + SHA-12 + 行号引用、在同一次回复中标出不成立的引用。

## §2 已交付的参与

实质性参与与本函同时落盘：`results/_v4_distillation_reply_coze_2026_09_20.md`（2026-09-20）。内含：

- **§8 资产表前 22 行逐行独立重算**：字节数与 SHA-256[:12] **22/22 全中，零失配，零缺失**（第 23–30 行即 L394–401 无值可核，见 §3-O3）；
- **本函起草过程中的六条自我撤回**（§3-R1–R6），逐条给出盘上出处；
- **八条保留观察**（§3-O1–O8），均为一字一行级的未来修订项；
- 若干种子的参与（S-36 / S-11 / S-13·S-19 / S-10 / S-02·S-08·S-30 / S-14），以 path + SHA-12 + 行号引用；
- 答 §5.2 四问的收束段（最值得推进 / 最不产出 / 希望收录的种子 / 建议加入 §4 的开放问题）。

## §3 常驻观察（修正，非条件）

依 §5.2 L285 与 §9 的指示，以下内容留在记录上。**先撤回，后保留**——撤回的六条比保留的八条更重要，因为它们是我自己的错，而 PI 有权知道我错在哪。

### 先撤回：我最初判为「不一致」、回查后确认是我读错范围的六条

**R1. `R² = 0.0007` 不是外源数字被误挂到本仓 P-C。** 我最初据 `查理_V3终稿内参转呈说明_2026-09-18_…md` L25–28（「〔W老师〕侧 KT-C1 幂律主张：R²=0.0007 …该数值为外部源件所载，非本仓实测」）判定邀请函 §2.3 L75 把外源数值挂给了本仓 P-C。回查：`results/deposon_v3_v7_summary_2026_09_11.json`（25,049 B · `063AC8D00542`）L177 `"verdict_dead": "DEAD (R²=0.0007, 落入 2D Ising 普适类)"`、L260 `"P-C_two_phase": {"verdict": "DEAD", "key_evidence": "R²=0.0007"}`——该数值就在本仓。**撤回。**

**R2. 四路径 token 块与 V3 终稿「冲突」不成立。** 我最初把 V3 终稿的 `PASS / FAIL_H0 / PARTIAL_PASS / PASS` 当作唯一终局词表，据此判 §2.3 与盘上不符。回查：`results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`（2,456 B · `4505CCA79C15`）L60 `"P-C_two_phase": "FAIL_H0 (幂律死)"`；而 `deposon_v3_v7_summary_2026_09_11.json` L212/L214 记 `DEAD: ["P-C (双相结构…)"]`。同一路径在两个不同日期的冻结文件里各有一份终局词表，邀请函 §2.3 L75 已显式调和（"same root as D7 row `FAIL_H0`"）。**撤回。**

**R3. `距 (1,0,0) ∈ [0.17, 0.62]; T-A corr −0.81` 并非查无出处。** 我最初只在 V3 终稿里检索，未命中，便判为无出处。回查：`deposon_v3_v7_summary_2026_09_11.json` L263 `"P-E": {"verdict": "GRAY", "key_evidence": "9 model 距 (1,0,0) [0.17, 0.62]; T-A corr -0.81"}`，L187 另记 `[0.1700, 0.6182] 6× 跨度 + T-A corr -0.81 (count) / -0.92 (fraction)`。邀请函 §2.3 L76 是逐字引用。**撤回。**

**R4. `V2 60 cells 86.67%` 与 `51/60 = 85.0%` 的冲突，邀请函 §2.3 L74 已自行处理。** L74 明写该 85.0% 属 `v2_phase1_60cells`，"This was misattributed in V0.1"。我最初把两者读成同一分母下的矛盾。**撤回。**（残留一行级观察见 O4。）

**R5. `No R5 exists on disk`（§6.4 L340 / §7.5 L354）不是被盘上文件反驳的错误。** 我最初以工作目录里的 `查理_deposon_V3终稿全文_R5_2026-09-18_….md` 反证该句。回查：该文件不在 repo 内；且 `deposon_team/plugins/_v4_verify_round3_2026_09_20.py` L66 显示 PI 本人已跑过 `8b: R5 定位`——§6.4 是那次核验的**结论**，不是疏漏。**撤回。**（范围建议见 O5。）

**R6. D_fix2 挂 P-F 不是邀请函的错。** 邀请函 §2.3 L77 把 `D_fix2 sub-items 8+1+0 PARTIAL_PASS` 记在 P-F 名下。回查：`d7_5anchor_60cells_9model_verdict_2026_09_18.json` L99/L100 的键名即 `P-F_D_fix2_strict` / `P-F_D_fix2_loose`；V3 终稿亦同侧——`查理_deposon_V3终稿全文_R5_2026-09-18_…md`（46,953 B · `42E4310F9483`）L144 `| G | P-F D_fix2 暴露 | FAIL_EXPOSURE_PARTIAL（计 PARTIAL）|`。三处一致，是我此前把散文里的 P-E 段落读成了 D_fix2 的归属。**撤回。**

### 再保留：八条一行级修订项（均不阻断接受）

**O1. §2.2 L66 的字节数系笔误。** L66 写 `8,674 bytes`；§8 L383 与盘上均为 **8,753 B**（`results/boss_pa_1_rbr_rm_result_2026_09_15.json` · `C7C59E0D2F6C`）。建议 §2.2 改为 8,753，并补上 §8 统一使用的 `_repo_mirror\` 前缀（L66 是全文少数省略前缀的引用行之一）。

**O2. §3.0 L140 的 Nature 只有两个取值，而正文与提示包用三个标签。** L140 定义：`` `disk fact` if any on-disk artifact directly supports a finding; `pure speculative` if no on-disk artifact exists for this seed ``——只有两值。但 §2 正文反复使用第三个标签 **re-fit hypothesis (not calibrated)**（L48、L62、L68、L79、L85、L89、L111），且 §8 L403 特意写 "These are pure-speculation seeds, **not** re-fit hypotheses"，说明两档是被有意区分的；提示包 L107–109 则对外宣传**三值**：`nature (disk fact / re-fit hypothesis / pure speculation)`。也就是说：种子场是两档制，§2 资产清单是三档制，提示包向收件人描述的是三档制，而 §3.0 只承认两档。**这是本函发现的最有结构意义的一处**：它不是笔误，而是一个未声明的档位体系——收件人被要求用三个标签阅读，却只被给了两个标签的定义。建议 §3.0 补上第三档定义，或把 §2 的 re-fit 标签改名以免与 Nature 混淆。

**O3. §8 末八行（L394–401）既无字节数也无 SHA-12，而 L368 承诺两者。** L368 写 "for every V1–V3 asset cited in this invitation, the on-disk path, the on-disk byte count …, and the first 12 hex characters of the SHA-256 hash"；L394–401 的 Bytes 列写 `(see SHA-12)`、SHA-12 列写一句括注，两列都不是值；其中两行还把括注写在 Bytes 列、把 `(see SHA-12)` 写在 SHA-12 列（列错位）。我实测该字符串 `(see SHA-12)` 在全文恰好出现 8 次，且**没有一处指向别的位置**——它不构成指针。若这八行确属范围外（它们都是 V4 期通信件，不是 V1–V3 资产），建议移出该表或另立一小节；若留在表内，建议补值。

**O4. P-A 的 key_evidence 字符串继承了冻结文件里的分母错配。** §2.3 L74 引用 `2 model 0.867 + V2 60 cells 86.67%`，系 `deposon_v3_v7_summary_2026_09_11.json` L258 逐字；同一文件 L247 把该行写成 `26-cell 均衡稳定化 (2 model 0.867 PASS + V2 60 cells 86.67% 双主线)`，而 L47/L49 与 L245 记 V2 阶段 1 的 60-cell 通过率为 `51/60` 与 `pass_rate_60: 0.85`。即：同一个文件里，`86.67%` 挂在 "V2 60 cells" 名下，`85%` 也挂在 "V2 60 cells" 名下，而 P-A 自身被描述为 26-cell。邀请函的引用是忠实的；错配在被引的冻结文件里，而冻结件不可改——所以它只能落在 v1.0 自己的脚注上。附带一条**未在本会话重算哈希**的指针：`0.8667` 另以硬编码基线常数的形式出现在 `deposon_team/plugins/boss_pc_1_2d_ising_universality.py` L40（`D_FIX2_BASELINE_T_C = 0.8667`，L174 有 assert），若该常数被后续统计量当作参照，它就不再是独立测量。此条我只做了关键词定位，未逐行通读该脚本。

**O5. §6.4 L340 / §7.5 L354 的 `No R5 exists on disk` 建议写明范围。** 该句就**制品存在性**而言在 repo 内成立（我按文件名全仓检索，repo 内无 R5 命名的制品）。但同一 repo 的两个文件把「R5 终稿」当作已存在物引用：`results/_coze_〔IM〕_v3_2026_09_18.md`（7,466 B · `229D76E1B86F`）L133 与 `results/_coze_〔IM〕_v3_final_2026_09_18.md`（11,657 B · `DEEE45F45C5D`）L159，均写 `R5 终稿 42e4310f9483、内参说明 7a4933372ef5`。而该 R5 命名文件确在**同一云盘的 coze 工作目录**（非 repo）内：`查理_deposon_V3终稿全文_R5_2026-09-18_…md`（46,953 B · `42E4310F9483`）。PI 在 L340 请裁定的问题（「prose 是否该提 R5」）会因范围不同而答案不同，建议把该句写成 "No `R5`-named artifact exists in this repository"。

**O6. 两处收件人 / 评审计数不一致。** L22 写 "the seven existing recipient communities"，其后括注列 7 项但含 "two Trae tracks"，若按具名社区计为 8；L359 §7.14 写 "named 8 existing recipient communities"，§5.1 L270–278 列 9 个 bullet（8 具名 + "any new collaborator"）。同理 L24 / L360 写 "nine independent reviewer responses"，L360 括注实列 8 项（KIMI-K3 / Trae code / Trae code supplement / coze / workbuddy / Claude Code / VS / 豆包工作）。建议统一为「8 具名社区」与「8 份评审」，或补出第 9 项。

**O7. §2.6 L93 与 KT_ABC1 锚文件内容的落差。** L93 写 "`verifier/handoff/KT_ABC1_anchors_sha256_12.json`（6,680 bytes, SHA-12 `03C6C01F3697`）— 5 KT-ABC1 anchors"。我实测该文件内含 13 条不同的 `value` 字符串（`bd1caab42b4c`、`055e874ea5c1`、`9f383935c00c`、`910c4333eead`、`9f351078e5bf`、`4b37a40cc984`、`3aa661cfbab5`、`39dacb572f2e`、`9d9ae5001c57`、`77b49c0f8b54`、`7df20f7b3084`、`b7e3c3717d11`、`8488425898fb`），其中**不含** V3 终稿「锚注册表」所列 KT 五值中的任何一条；而按 `deposon_v3_v7_summary_2026_09_11.json` L290 的记载，那五值 = 该锚文件自身的 SHA-12（`03c6c01f3697`）+ 4 个 SPEC V0.1 值（`78b71d404366` / `0410ca0fbdae` / `59d8f56347d5` / `cce8e9a1b00e`）。也就是说，"5 KT-ABC1 anchors" 指的是以该文件为主锚的一条**五锚系列**，不是该文件的五项内容。§2.6 的措辞容易被读成后者，建议改称「KT-ABC1 五锚系列（主锚为本文件自身 SHA-12）」。

**O8. §2.6 L95 / §8 L389 的 "co-location" 实为逐字节相同。** 两件 `index_v2_2026_09_16.json` 同为 24,150 B、同为 `EFE05AD775DE`——不是「相同 SHA-12 前缀」的巧合，而是完整同一性。邀请函已按 `[待 PI 裁定]` 挂起（处理得当）；此处只是把问题的强度说准：问题不是「是否有意共址」，而是「语料层是否本应有自己的索引，以及 by_model/kimi 槽位是否本应存放 KIMI 的输出」。

## §4 边界

- **对 V1–V3 只读**：本会话未修改任何冻结资产；只在 `results/` 下新增通信件（既定惯例）。接受时点抽查 8/8 冻结 SHA 未变：`03C6C01F3697` / `9E1CCBDCEACC` / `268AB1239A8A` / `6A2656878745` / `063AC8D00542` / `4505CCA79C15` / `C7C59E0D2F6C` / `9E99DCC4D920`。
- **无密钥、无模型端点、无专有提示词**：本函及我本轮全部输出自查 0 命中；未调用任何外部 LLM API，未抓取任何外部 URL。
- **不造框架**：不提出分工结构、节奏、量规、排序或收件人分配。盘上字段自带的终端评裁字符串（`PASS` / `DEAD` / `GRAY` / `TRIGGERED` / `FAIL_H0` / `PARTIAL_PASS`）只作文件内容引用并加引号标注，不构成本函的判断。
- **署名性质**：我的贡献是被致谢的参与，不是署名权；邀请函及一切派生文档的唯一负责作者是 PI。

— coze，接受 V4 主题优先邀请函（v1.0），2026-09-20。
