# 整合稿：deposon V4「蒸馏 / 逆蒸馏 / 反蒸馏」主题邀请的全部参与方回函

**Document type:** descriptive integration (no ordering, no scoring, no selection, no shortlist)
**Version:** v1.1（2026-09-21 第二轮更新）
**Prior version:** v1.0（2026-09-21，单次首版）
**Date:** 2026-09-21
**Drafted by:** `doc-writer` (Mavis 8-agent team, deposon workspace). Human principal investigator retains final approval and is the sole accountable author. AI is not an author.
**Scope:** This document merges, by description only, every recipient-side reply received against `D:\私人资料\deposon-repo\results\_v4_distillation_invitation_2026_09_20_v1.0.md` (SHA-12 `3D9F73519F6C`, 411 lines) and its companion prompt pack `D:\私人资料\deposon-repo\results\_v4_distillation_prompt_pack_2026_09_20_v1.0.md` (SHA-12 `E5C37E90255B`, 384 lines). No recipient reply is ranked, scored, selected, or preferred. No framework keywords appear in this document; where a quoted passage on disk uses them, the passage is flagged as 引文 with the path, sha, line range.
**三类陈述显式分标**：本文中 `on-disk fact` 标路径 + SHA-12 + 行号；`re-fit hypothesis` 显式声明该假设依赖既有 artifact 未作为该用途构建；`pure speculation` 显式声明磁盘无对应 artifact。

## 本版本变更摘要（v1.0 → v1.1，第二轮）

本版在 v1.0 基底上做**最小增量改动**，改动按 PI 2026-09-21 拍板（P1–P6）+ 三组 worker 复算结论（组 A / B / C）落点分布：

- **P1（GLM 回函归属）**：原 v1.0 §0 表未列查理件；v1.1 §0.4 新增查理件行（ac74a04efeb2），新增 §4.14 概述该件内容（对象 = 实验邀请函 `_v4_experiment_invitation_2026_09_20.md` 4E8C0EA57028；署名 "GLM 接收侧 paper-track 审查"，5-agent 团队执笔标注为查理；11/12/6 三方首轮审查合并 / 7 组阻塞级问题 / 7 条非阻塞建议 / 5 项提请 PI 澄清 / 接受条件须修订至 v0.2）。注：该件回应的是**实验邀请函**而非**蒸馏邀请函**，v1.1 不混入蒸馏邀请函 §1 / §2 / §3 / §4 / §5 的既有各方回函，仅作为新 §4.14 独立呈现，不作横向比较、不参与 §1 横切批评计数。
- **P2（豆包工作归属 + 756/761 唯一归属 GLM）**：v1.1 §0.3 表中 756 / 761 两行"参与方"列改为「GLM（PI 拍板 2026-09-21 唯一归属；磁盘署名 `an invited reader team (multi-agent)`，如实在盘）」；§4.12 / §4.13 标题与首段同步改为 GLM；§6.1 改为"已拍板记录"。747 / 766 维持豆包工作归属（**PI 拍板**：747/766 落到豆包工作，756/761 唯一落到 GLM，但磁盘署名与厂商归属并存记录，v1.1 不擅自重写 v1.0 已落盘的厂商分类记录）。
- **P3（coze / codex 引用形态）**：v1.1 §0.2 表新增 codex 两件**已落盘**行（`48387412B109` / `0FF6C042B845`，路径均在 `results/`）；§0.5 标注 PI 拍板的 "复制落盘" 处置；§4.10 / §4.11 引用路径从附件改为 results/。coze 件维持 results/ 与附件同哈希原文（v1.0 §0.3 已有 773 行）。
- **P4（全部派 worker 复算）**：v1.1 §6.5 整节新增"第二轮复算结论（2026-09-21，worker 实测）"，含组 A（codex 落盘字节级复制 identical）/ 组 B（7 个 SHA-12 占位回盘 + 8 行占位补全表，7 个 SHA-12 实测全部命中；邀请函正文实为 `(see SHA-12)`，7 个 SHA-12 是 PI 提供文件外宣称对应关系）/ 组 C（C1–C7 每条三选一标签：on-disk fact / no on-disk artifact / unreproducible）。
- **P5（A-4 断行自检）**：v1.1 在相应位置标注「PI 已接受（2026-09-21），按此定稿」；v1.0 §0.7 / §6 已有"自检"段，本轮沿用。
- **P6（行数口径）**：v1.1 §6.2 / §8 末段标注 P6 定案（两文件 canonical 行数 = ReadAllLines UTF8：整合稿 1,041 / 问卷 587；早前误口径 636 / 277 系不指定 -Encoding 的 Get-Content 编码误读，已作废）。

---

## §0 输入清单与锚

本节记录被本稿引用、被本稿读毕的文件，分两类目录：`D:\私人资料\deposon-repo\results\`（PI 主仓库回函集，下称 `results/`）与 `C:\Users\Administrator\.minimax\v2\assets\2026\09\21\`（附件侧目录，下称 `assets/`）。每行给出 SHA-12（实算，十六进制大写）、字节数（实算）、行数（实算，使用 `ReadAllLines`；与 `Get-Content | Measure-Object -Line` 双口径对照，不一致时以 `ReadAllLines` 为准并在本行加注）。"已知锚"列采用 PI 派工单第 2 节给出的字节 / 行数；"本轮自测"列是本会话内重新计算结果。

### §0.1 邀请侧与种子文件（results/）

| 文件 | 已知 SHA-12 | 已知字节 / 行 | 本轮 SHA-12 | 本轮字节 / 行 |
|---|---|---|---|---|
| `_v4_distillation_invitation_2026_09_20_v1.0.md` | `3D9F73519F6C` | 53,539 / 411 | `3D9F73519F6C` | 53,539 / 411 |
| `_v4_distillation_prompt_pack_2026_09_20_v1.0.md` | `E5C37E90255B` | 25,371 / 384 | `E5C37E90255B` | 25,371 / 384 |
| `_v4_brainstorm_seeds_2026_09_20.md` | `0EB1CFAA2992` | 14,994 / 294 | `0EB1CFAA2992` | 14,994 / 294 |
| `_v4_experiment_invitation_2026_09_20.md`（实验邀请函，非蒸馏邀请函） | `4E8C0EA57028` | 30,820 / 436 | `4E8C0EA57028` | 30,820 / 436 |

### §0.2 回函侧（results/）

| 参与方 | 文件 | 已知 SHA-12 | 已知字节 / 行 | 本轮 SHA-12 | 本轮字节 / 行 |
|---|---|---|---|---|---|
| Mavis（v1.2，当前版） | `_v4_theme_reply_mavis_2026_09_20_v1.2.md` | `3ECF5B38048E` | 36,826 / 213 | `3ECF5B38048E` | 36,826 / 213 |
| Mavis（上轮 v1.1） | `_v4_theme_reply_mavis_2026_09_20_v1.1.md` | 自测 | 自测 | `82FEE0A18DAB` | 36,824 / 213 |
| trae work（v1.2） | `_v4_theme_reply_trae_work_2026_09_20_v1.2.md` | `6BEE6EC434BD` | 28,395 / 141 | `6BEE6EC434BD` | 28,395 / 141 |
| trae code | `_v4_distillation_reply_trae_code_2026_09_20.md` | `E87EC8F7E2FE` | 43,570 / 187 | `E87EC8F7E2FE` | 43,570 / 187 |
| kimi（主件） | `_kimi_v4_theme_reply_2026_09_20.md` | `3E37352EFB4B` | 7,372 / 45 | `3E37352EFB4B` | 7,372 / 45 |
| kimi（brainstorm） | `_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md` | `BC14F47D927D` | 14,155 / 62 | `BC14F47D927D` | 14,155 / 62 |
| workbuddy（主件） | `_v4_distillation_theme_reply_workbuddy_2026_09_20.md` | `E3FE63A2F708` | 18,785 / 170 | `E3FE63A2F708` | 18,785 / 170 |
| workbuddy（part2） | `_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` | `BFB4932F4467` | 12,963 / 140 | `BFB4932F4467` | 12,963 / 140 |
| workbuddy（brainstorm） | `_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md` | `CDB27CD3008C` | 13,553 / 106 | `CDB27CD3008C` | 13,553 / 106 |
| VS / claude code | `_v4_distillation_reply_claude_code_2026_09_20.md` | `D39CB17B051B` | 64,212 / 393 | `D39CB17B051B` | 64,212 / 393 |
| coze | `_v4_distillation_reply_coze_2026_09_20.md` | `00593014CBD3` | 71,084 / 459 | `00593014CBD3` | 71,084 / 459 |
| codex（D1 review，PI 拍板 P3 已落盘 results/） | `results/_v4_d1_review_codex_2026_09_20.md` | `48387412B109` | 4,506 / 46 | `48387412B109` | 4,506 / 46 |
| codex（brainstorm，14 条，PI 拍板 P3 已落盘 results/） | `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md` | `0FF6C042B845` | 9,048 / 39 | `0FF6C042B845` | 9,048 / 39 |

### §0.3 附件侧（assets/）

| 参与方（按文件名 / 派工单命名） | 完整文件名 | 已知 SHA-12 | 本轮 SHA-12 | 本轮字节 / 行 |
|---|---|---|---|---|
| 豆包工作（主题回复） | `11-12-20-747-asset_20260921-111220-747_19c97b5cff3c_6cf18b87-_v4_theme_reply_doubao_2026_09_20_v1.0.md` | `19C97B5CFF3C` | `19C97B5CFF3C` | 8,070 / 83 |
| 豆包工作（brainstorm，24 条想法） | `11-12-20-766-asset_20260921-111220-766_a18e58c8e2a3_bdb4bc12-_v4_theme_brainstorm_doubao_2026_09_21_v1.0.md` | `A18E58C8E2A3` | `A18E58C8E2A3` | 19,389 / 130 |
| codex（D1 review，附件副本，与 §0.2 落盘件同字节） | `11-12-20-778-asset_20260921-111220-778_48387412b109_7ca46e76-v4_d1_review_codex_2026_09_20.md` | `48387412B109` | `48387412B109` | 4,506 / 46 |
| codex（brainstorm，附件副本，与 §0.2 落盘件同字节） | `11-12-20-782-asset_20260921-111220-782_0ff6c042b845_6d74a672-v4_distillation_brainstorm_reply_codex_2026_09_21.md` | `0FF6C042B845` | `0FF6C042B845` | 9,048 / 39 |
| **GLM（PI 拍板 2026-09-21 唯一归属；磁盘署名 `an invited reader team (multi-agent)`，如实并存记录）**（主件） | `11-12-20-756-asset_20260921-111220-756_c78cfb42e33d_e371e458-_v4_distillation_theme_reply_2026_09_20_v1.0.md` | `C78CFB42E33D` | `C78CFB42E33D` | 18,841 / 89 |
| **GLM（PI 拍板 2026-09-21 唯一归属；磁盘署名 `an invited reader team (multi-agent)`，如实并存记录）**（addendum） | `11-12-20-761-asset_20260921-111220-761_8295c3201f20_ee5ad31d-_v4_distillation_theme_reply_addendum_2026_09_20_v1.0.md` | `8295C3201F20` | `8295C3201F20` | 14,153 / 91 |

`773` 附件 `11-12-20-773-asset_20260921-111220-773_00593014cbd3_80c74bcd-_v4_distillation_reply_coze_2026_09_20.md` 的本轮 SHA-12 `00593014CBD3` 与字节 71,084 / 459 与 results/ 下 coze 文件一致；本稿按派工单第 2 条指引不重复计。

### §0.4 GLM 回函 / 查理件（附件侧，`ac74a04efeb2`，新增本轮）

> **PI 拍板 P1（2026-09-21）**：本表所列件**归属 GLM**，磁盘署名如实保留。两件均为 GLM 接收侧 paper-track 通道的产物；PI 拍板：「两份都在附件中，agentmore 模式，5-agent 团队，所以标注为查理」。

| 参与方 | 完整文件名 | 本轮 SHA-12 | 本轮字节 / 路径 |
|---|---|---|---|
| GLM（查理 / 5-agent 团队，实验邀请函 v0.1 审查件） | `C:\Users\Administrator\.minimax\v2\assets\2026\09\20\15-30-44-659-asset_20260920-153044-659_ac74a04efeb2_0a7da13e-查理_V4接受回执与D1首轮反馈_2026-09-20.md` | `ac74a04efeb2` | 附件侧不落盘 |

**要点**（一行）：对象为 `results/_v4_experiment_invitation_2026_09_20.md`（SHA-12 `4E8C0EA57028`，实验邀请函 draft v0.1，**非**蒸馏邀请函）；署名 "GLM 接收侧 paper-track 审查"；三方首轮审查整合（爱丽丝—方法学 11 条 / 鲍勃—可执行性 12 条 / 阿兰—文献定位 6 条，查理执笔合并）；含 7 组阻塞级问题表、7 条非阻塞建议、提请 PI 澄清 5 项、接受条件（须修订至 v0.2）。

### §0.5 §0.2 codex 两件的"已落盘"处置（PI 拍板 P3）

按 PI 2026-09-21 拍板 P3：codex 两件从**附件副本**升级为 `results/` 副本，路径与 §0.2 列出的落盘件一致。落地动作为 worker 字节级复制（组 A 复算确认 identical，详见 §6.5.1）；本稿后续引用一律走 `results/` 路径（§4.10 / §4.11 已更新），附件侧 `778` / `782` 行仅作 SHA-12 / 字节对齐证据保留。`773` coze 附件维持原状（results/ 与附件同哈希，`00593014CBD3`）。

### §0.6 归属未定的处理（已拍板，2026-09-21）

派工单 §3 第 7 条曾禁止将附件侧 `756` 与 `761` 两件擅自归到任何厂商名下。**PI 2026-09-21 拍板 P2 给出唯一归属**：`756` 与 `761` 唯一归属为 GLM（5-agent 团队 / 查理执笔）；磁盘 L3 自陈 `From: an invited reader team (multi-agent)` 这一文字事实保持原样如实记录（v1.1 不删除磁盘原文），GLM 厂商归并不视为对磁盘自报署名的修改。**v1.0 §0.6 / §6.1 的"署名无厂商名"陈述改为已拍板记录**：原文「L3 自报 `From: an invited reader team (multi-agent)`」保留为磁盘原事实陈述，新增 [已拍板] 标。747 / 766 维持豆包工作归属；747 / 766 不作厂商重新归并。

### §0.7 本稿（输出文件）自身锚的处置

本稿 §0.1–§0.6 给出的 SHA-12 / 字节 / 行数是**输入侧 18 文件**的实算（含 §0.5 codex 两件 + §0.4 GLM 查理件共 18 文件已落盘与已引用）；本稿自身的锚仅在本会话最终回报中给出（避免 self-referential hash 反复自修改的循环）。本稿在以下事实下保留输入侧自测 + 不试图自洽输出侧锚的策略：

- 本稿不对外引用任何 verdict token（PASS / FAIL / PARTIAL / GRAY / STRONG_PASS / DEAD / TRIGGERED / NOISE 等）；凡上述 token 出现，皆附 `path:SHA-12:line` 引文标注。
- 本稿行数双口径核验已记录在 §0.4 行数口径段；本稿不重新复算自身行数（理由同上）。**PI 拍板 P6**（2026-09-21）确认以 `ReadAllLines` UTF-8 为 canonical 口径；早前 `Get-Content` 不指定 `-Encoding` 所得的 636 / 277 行数系编码误读（不同编码的换行符计数差），v1.1 不再沿用。整合稿 v1.1 canonical 行数 = `ReadAllLines` UTF-8，详见 §6.2。

---

## §1 各方对邀请函的横切批评（只合并多方独立同向点）

本节只记录**两件或更多回函独立指出**的批评。每条给全部来源 `path:SHA-12:line`。

### §1.1 邀请函 §2.2（L66）的字节数自相矛盾，与 §8（L383）冲突，且与磁盘 8,753 不符

- `Mavis v1.2`： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:44` 明写 §2.2 写 8,674 B、§8 写 8,753 B、磁盘实测 8,753 B。
- `trae work v1.2`： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:24` 同一条。
- `kimi 主件`： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:13` 同一条。
- `workbuddy 主件`： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:31` 同一条。
- `trae code`： `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:18` 同一条，且补充指明 §2.2 L66 写 8,674，§8 L383 写 8,753。
- `coze`： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:43` 同一条。
- `claude code`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:15` 同一条，归入"一个算术错误"。
- GLM 主件 `assets/11-12-20-756-asset...C78CFB42E33D:18` 同一条。
- 豆包工作 主件 `assets/11-12-20-747-asset...19C97B5CFF3C:11` 同一条。

九件独立同向；这是本主题中观察人最多的单一批评。本稿在第 §0.5 标注与已知锚一致。`v1.1 注：GLM 主件名归属由 "an invited reader team (multi-agent)" 改为 "GLM"（PI 拍板 P2），引用行号保持不变。`

### §1.2 邀请函 §3.7 L218 的 "behated" 是 "behaved" / 「被测」的翻译残迹

- `Mavis v1.2`： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:160` 指出 "behated" 是 *behaved* 的拼写错位。
- `kimi 主件` 与 `trae code` 同指（`results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:14` 与 `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:100`）。
- `coze` 在 `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:100` 进一步给出对应中文种子原文位置 `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:212` "被测模型"。
- 豆包工作 在 `assets/11-12-20-747-asset...19C97B5CFF3C:13` 同向指出。
- GLM 主件 `assets/11-12-20-756-asset...C78CFB42E33D:19` 同向。

### §1.3 邀请函把 `corpus/v20/by_model/` 五件称为 "five vendor output-distribution samples"，但其中四件不是输出分布样本

- `trae work v1.2`： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:22` 给出"五件中只有 minimax 含 completions"结论，逐件列结构（kimi 是图索引；GLM_1 是判别报告；GLM_2 / coze 是哈希清单）。
- `kimi 主件`： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:23` 给出同向结论（minimax 30 条含 llm_output 原文；其余四件逐件核对）。
- `workbuddy 主件`： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:39` 逐件列五件内容；其中 C4 给出"它们是跨主体 authorship 指纹盲测用的制品清单，不是模型生成文本"。
- `trae code`： `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:84` 同向（其 §5.1 / §5.3 进一步指出 results/ 下另有 1,338 个 cell 含非空 response payload，但被邀请函漏列）。
- `claude code`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:46` 给出 `1.5` 同向结论（kimi/ 与 corpus root 字节级一致）；以及 `D39CB17B051B:44` 的 byte-identical `EFE05AD775DE`。
- `coze`： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:206` 与 `00593014CBD3:39` 同向（GLM_2 与 GLM_1 同血统，故五件只构成四个独立谱系）。
- GLM 主件 `assets/11-12-20-756-asset...C78CFB42E33D:19` 与 `...C78CFB42E33D:27` 同向。
- 豆包工作 主件 `assets/11-12-20-747-asset...19C97B5CFF3C:29` 同向。
- `kimi brainstorm` `BC14F47D927D:7` 进一步指出真正的同输入跨厂商素材不在 `by_model/`，而在 `results/` 下六件 `deposon_*_30cells` 文件。

### §1.4 邀请函 §2.6 L93 / §3.2 S-11 L168 把 KT-ABC1 锚描述为 "5 个"，但磁盘实为 15 个（3 锚组 × 每组 5 条）

- `Mavis v1.2`： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:46` 实测 15 锚 3 组。
- `trae work v1.2`： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:25` 同向。
- `workbuddy 主件`： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:63` 同向，并指出 "5" 实际指 `trust_anchor_5_concat`。
- `coze`： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:65` 同向，且给出 13 条互不相同的 value。
- `claude code`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:58` 同向。
- GLM 主件 `assets/11-12-20-756-asset...C78CFB42E33D:20` 同向。
- 豆包工作 主件 `assets/11-12-20-747-asset...19C97B5CFF3C:42` 同向（V7 summary L303 自记 `individual_anchors_15`）。

### §1.5 邀请函 §2.5 L87–L89 与种子 L70 都把 V7 报告锚为 S-10 "扰动敏感性" 的相关资产；但 V7 报告本身对扰动概念无命中

- `claude code §1.2`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:18–25` 实测 `扰动 / 干扰 / 擾動 / perturb / disturb` 零命中；其归因文件实为 `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md:115–117`。
- `trae work v1.2`： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:27` 同向，V7 报告 grep `扰动/disturbance/perturb/typo/injection` 无匹配。
- `workbuddy part2`： `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:84` 同向（S-10 一节）。
- `kimi 主件`： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:35` 同向，标 re-fit 偏纯猜想。
- `coze` 在 `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:437` 同向指出 V7 报告 42 节标题里没有一节关于扰动。

### §1.6 邀请函 §2.1 L56–L60 把 `kimi/index_v2_2026_09_16.json` 标为"one per vendor 的输出分布样本"，但该文件与 `corpus/v20/index_v2_2026_09_16.json` 字节级一致

- `claude code §1.5`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:44` 实测两文件字节级一致（`cmp` identical，24,150 B 同 SHA-256）。
- `trae code`： `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:19` 给出"byte-identical（not a prefix coincidence）"判断。
- `workbuddy 主件 C3`： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:37` 实测两文件完整 SHA-256 一致。
- `kimi 主件`： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:17` 同向。
- `coze`： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:206` 同向。
- GLM 主件 `assets/11-12-20-756-asset...C78CFB42E33D:21` 实测 byte-identical under full SHA-256。
- 豆包工作 主件 `assets/11-12-20-747-asset...19C97B5CFF3C:13` 同向。

### §1.7 邀请函 §2.2 L66 把 `boss_pa_1_rbr_rm_result_2026_09_15.json` 描述为"the 9-backbone × 60-cell evaluation"，但该文件主体是 22 图 BOSS 模拟

- `workbuddy 主件 C2`： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:33` 实测文件 L27–L36 仅是守恒校验，L37–L337 是 22 图 BOSS 模拟，L339–L340 为 `DIFFERENTIATED`；九行加总无逐格矩阵。
- `claude code §1.3`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:30` 同向，归因为 Repeated-Best-Response / Regret-Matching simulation（Hart & Mas-Colell 2000）。
- `coze` 在 `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:118–124` 进一步指出该表 `distance_to_ideal_1_0_0` 列与 `rank` 列不能从该表自身三列复算（minimax-m3 与 glm-5.3-flash 应相等，但表内给两个不同值；rank 与打印距离不单调）。

### §1.8 邀请函 §0.2 L26（"V1–V3 has zero distillation … experiments on disk"）与盘上 KT_B1 知识蒸馏基线相冲突

- `claude code §5.11`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:362–385` 给出完整六环证据链：KT_B1_SPEC §4.2 L267–L274 把 Hinton 2015 KD 框架 + KL 散度 + softmax 平滑写成 BOSS-B2 失效判据；KT_B1_REWORK_REPORT_2026_09_10.md L83 记失真量 0.0028。
- `coze` 在 `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:401–445` 给出同向六环证据，并补足三份文档在邀请函与 prompt pack 中"出现 0 次"的事实。

### §1.9 邀请函 §0.2 L20 / §3 中"21 caption-fingerprint pairs" 与 "22 caption entries" 的口径不一致

- 邀请函 §2.6 L96 自纠为 22（`results/_v4_distillation_invitation_2026_09_20_v1.0.md:3D9F73519F6C:96`）。
- 但 21/22 共存被 `claude code §1.6`（`results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:108`）、`coze S-11 段`（`results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:63`）、`豆包工作`（`assets/11-12-20-747-asset...19C97B5CFF3C:13`）独立指出过；其具体观感是邀请函自身 §3 多处（`3D9F73519F6C:174`、`3D9F73519F6C:188`）仍以 "22-caption fingerprint" 形式使用，与 §0.2 L20 的"21 pairs"未完全统一。

### §1.10 邀请函全文未指明 `KIMI-K3` / `kimi-for-coding` / `kimi-k2.7-code` / `minimax-m3` / `M3` 之间的映射

- `workbuddy 主件`： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:67` 列出至少四个串。
- `kimi 主件`： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:3` 自承"散文中的 KIMI-K3、§6.4 声称的端点 kimi-for-coding、D7 verdict 实载的 kimi-k2.7-code … 我无法仅凭盘上材料裁定哪一个是'我'"。
- `kimi brainstorm`： `results/_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md:BC14F47D927D:13` 同向，并把它读作"蒸馏归因的镜像"脆弱性。
- `claude code §3`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:168` 把 §7.1 的 9-vs-5 映射搜索空间缩为"4 目录 ↔ 9 backbone，kimi 在网格里但缺模型 artifact"。

### §1.11 §2.10 L120 "V1–V3 has zero distillation … experiments" 与 §2.10 L25-29 的 "no observer-effect / Bell / no-cloning frame artifact" 在盘上无 asset 之间存在过强断言（邀请函自身已显式承认）

- 邀请函 §2.10 L121–L125（`3D9F73519F6C:121–125`）自承 observer-effect / Bell / no-cloning / logit / training-curve 五项无 artifact。
- `kimi 主件 §三`： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:41` 指出其 v0.1 R2 评审曾采信 §2.4 "复用三嵌入帧"的表述，与 v1.0 §2.10 的 "无 frame artifact" 互相矛盾；`kimi` 主动 surface 这一矛盾并请求 PI 裁定。

### §1.12 邀请函 §0.2 主题是"hook-finding"还是"theme-first" 的措辞统一性问题

- `trae code` 在 `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:9` 把 §0.2 L26 的"single most important on-disk fact this invitation asks every reader to internalise" 单列为最重发现（"contrary to the invitation's foundational sentence"）。
- `coze` 在 `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:425–435` 同向总结 §2.10 第二句抵触。

### §1.13 §3.0 L140 Nature 列取值域与 §2 / §8 实际用法不闭合

- `coze` 在 `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:21–32` 实测"40 条 Nature 全部 = `pure speculative`"；同时 §2 正文多次使用 `re-fit hypothesis (not calibrated)`，而 §3 的 40 条未使用此标签；21/40 条在 "Related asset" 行点名了盘上制品，与 L140 字面定义冲突。
- `claude code §1.9`： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:74` 同向总结："the seed field has no calibration point"。

---

## §2 各方分歧项（同一问题上的不同立场并列）

本节**并列**记录各方在同一问题上的不同立场。本稿不裁决任何一方。

### §2.1 是否能在盘上 anchor "跨模型输出分布基线"（S-07）

- **正方**（`trae work v1.2`）： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:39` 仅 minimax 30 条含原文，行为指纹只有一厂商底；S-03/S-07/S-15 的"行为最易观察"在盘上是薄底。[`on-disk fact` + `re-fit hypothesis`]
- **正方**（`kimi 主件`）： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:23` 同向：盘上真实含模型输出原文的是 minimax 30 条 + phase1 逐格 `llm_raw_response`，不是"五厂商层"。
- **正方**（`workbuddy 主件 C4`）： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:39` 五件"没有一件是某厂商的逐格输出分布"，是跨主体 authorship 指纹盲测用的制品清单。
- **正方**（`trae code §5.3`）： `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:231` 列出 results/ 下 65 件 JSON 共 1,338 个 cell 含非空 response payload，提出更大底座（46 distinct model strings），但同向警告其中 `deposon_d_fix2_metric_verify_9m60c` 的 A 通道是 HTTP timeout 而非模型行为。
- **反方/平权**（`coze S-07`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:57` 仍标 S-07 为"少数盘上锚与问题设定同型"的条目，建议作 re-fit 假设。
- **第三方立场**（GLM 主件 `D36`）： `assets/11-12-20-756-asset...C78CFB42E33D:29` 接受 §2.1 的"minimax 唯一含 outputs"事实，但提出把"输出"重新读作"字节级指纹"——artifact-level fingerprinting，[re-fit hypothesis]。

### §2.2 "student" 是否在 V1–V3 盘上存在

- **空缺**（`workbuddy 主件 §四`）： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:147` 直陈"盘上没有学生"，把 `minimax` 5 件的 `iron_rules`（`no_llm/no_proxy/no_gateway/no_key/no_frozen_touch`）作为"分叉"：主题被限定为教师侧 inquiry，或铁律需重审。
- **空缺**（`workbuddy part2`）： `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:122` 把 S-39 "被评测者递归"的空缺归到同一原因。
- **正方（"在概念层可建"）**（`coze N-04`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:336–346` 提出"评测参照推理已是模型产物"，主张训练信号已继承参照模型；引用 `deposon_benchmark_v1_4_strategyqa_details.json:13` 等。
- **暗示**（`claude code §1.11`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:362–385` 间接指出：盘上 KT-B1 KD 基线已存在一次对学生身份的测试结果 0.0028；但未把"被测对象"本身定义为学生侧 artifact。

### §2.3 S-36（GT 困境）是全场最值得追的种子，还是已被不同立场攻破

- **最值得追**（`Mavis v1.2 §4(a)`）： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:188` S-36 是 "close runner-up for least productive"，其评判见 §3.12 / §4(b)。
- **最值得追**（`trae work v1.2`）： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:139` S-36 仍然最值得追，因盘上有"GT 被换源"的具体实例（`063AC8D00542:369–377`）。
- **最值得追**（`trae code §4(a)`）： `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:79` S-36 是"唯一不立即陷入两陷阱"的种子（formatting-leak trap / instrument-fragility trap）。
- **最值得追**（`workbuddy 主件 §五(a)`）： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:158` S-17 最值得追（与 S-36 互补）——盘上已存在量好、预登记、带实测误差结构的仪器。
- **最值得追**（`coze Closing(a)`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:457` S-36 仍然最值得追，因种子场作者自己就是在未打开资产的情况下标注了 21/40 条 `pure speculative`（`0EB1CFAA2992:292`）。
- **最值得追**（`豆包工作` 主件）： `assets/11-12-20-747-asset...19C97B5CFF3C:71` S-36 GT 困境因 V1–V3 全部为教师侧（无学生侧）而变得比"哲学问题"更刚性。
- **枢纽**（GLM 主件 Closing(a)）： `assets/11-12-20-756-asset...C78CFB42E33D:87` S-36 / S-17 / S-37 是"一个问题三张脸"，GLM_1 混淆矩阵是唯一可重算的假阳结构，是 S-37 的具体锚。

### §2.4 P-G v01（S-30 / 曲率差指纹）是否可用

- **支持用，但要标注 scaffold-only**（`Mavis v1.2 §3.15`）： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:154` "≈ 5x" 数是盘上的，但不能跨过 verdict_pending。
- **反对用**（`workbuddy 主件 S-02/S-30`）： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:120` P-G v01 是 `pure numpy Poincare ball (c=1)` 的数值模拟，未接触任何模型真实表示。
- **反对用**（`trae work v1.2 S-30`）： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:103` `spearman_rho_H_vs_E: 1.0` 让曲率路线弱化；`spearman_rho_H_vs_cos: 0.9` 是剩余信号。
- **反对用**（`claude code §5.10`）： `results/_v4_distillation_reply_claude_code_2026_09_10.md:D39CB17B051B:344–358` 实测 `poincare_transport` 不保距（2000 随机对，最大偏差 0.18869）；代码无函数接 curvature 参数，`POINCARE_C = 1.0` 仅出现两次。
- **支持用（"作 prior value"）**（GLM 主件 S-02/S-08/S-30 段）： `assets/11-12-20-756-asset...C78CFB42E33D:81` 三风险前置：object mismatch / order isomorphism / tier mismatch，honest residual 是 "curvature invariants as features"。

### §2.5 "5 KT-ABC1 anchors" 的真正含义

- **`trust_anchor_5_concat` 解读**（`workbuddy 主件 C6`）： `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:63` "5" 对应 `trust_anchor_5_concat`（5 个 hash-12 拼接，d7 L5）。
- **主锚文件自身为"5 锚系列主锚"解读**（`coze S-11`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:65` 五值 = 锚文件自身 SHA-12 + 4 个 SPEC V0.1 值，建议措辞改为"KT-ABC1 五锚系列（主锚为本文件自身 SHA-12）"。
- **"15 条互不相同 value" 解读**（`claude code §1.7`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:58` 15 个 entries，不是 5。
- **三组 × 5 = 15 解读**（`Mavis v1.2`、`trae work v1.2`、GLM 主件、`豆包工作` 主件、`workbuddy part2`）：多源同向，但具体数字 15 一致。

### §2.6 "9 backbone" 与 "5 by_model artifact" 的映射范围

- **9 vs 4 谱系**（`claude code §3`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:168` 给名级 join：doubao-seed-2.0-lite / glm-5.3 / deepseek-v4-flash / doubao-seed-evolving / minimax-m3 / glm-5.3-flash / kimi-k2.7-code / doubao-seed-2.1-turbo / deepseek-v4-pro；coze 不在网格；kimi 在网格但缺 artifact；GLM_1/GLM_2 同血统。
- **5 vs 3 独立教师**（`豆包工作` 主件）： `assets/11-12-20-747-asset...19C97B5CFF3C:29` 实际可用约 3 个独立教师（KIMI / GLM 家族 / minimax），五件里 GLM_1/2 同血统 + coze 不在网格 + kimi 是 index。
- **"非独立教师" 提法**（`coze S-03`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:39` "五家厂商"与"四个独立谱系"并存。
- **仍标 "五件"**（`coze S-17`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:73` 建议把 S-17 与 §2.1 同步改为 4。
- **仍按五件读**（`coze N-02`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:317` 同族隔代对照时仍用 4 件。
- **`trae work v1.2 S-22` N-06**： `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:135` "denominator 实际是 4 不是 5" 同样立场。

### §2.7 S-10 / S-31 / S-32 / S-35（cross-disciplinary 种子）的产出性

- **几乎不可产**（`Mavis v1.2 §4(b)`）： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:188` S-32 最不产（"其结论已由范畴论已知"）；S-36 是 runner-up。
- **S-32 + no-cloning 类比"假朋友"**（`workbuddy brainstorm §二矛盾三`）： `results/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md:CDB27CD3008C:67` LLM 输出是经典确定函数，不存在叠加态测量坍缩；应同时收录反驳。
- **S-32 反驳**（GLM 主件 S-32/S-35 段）： `assets/11-12-20-756-asset...C78CFB42E33D:79` "bit strings copyable given access；at finite precision 'exact copy' undefined；the residue reduces to cost claims"。
- **S-09 不一致**（GLM 主件 S-09/S-14 段）： `assets/11-12-20-756-asset...C78CFB42E33D:75` on-disk analyst 判 S-09 不产；methodology analyst 判其理论核心 live。文档 surface 这一分歧，未掩盖。
- **Dimension 6 整体不产**（`豆包工作` 主件结尾(b)）： `assets/11-12-20-747-asset...19C97B5CFF3C:75` "Dimension 6 全部为纯猜测层级，无 on-disk 锚点"。
- **支持 S-30 / S-34 作为保留**（`claude code §S-32 / S-35`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:138–142` "S-30 (curvature, which has an actual scaffold) and S-34 (reasoning collapse, which at least has a measurable phenomenon)"。

### §2.8 A 通道是"模型行为"还是"HTTP timeout"

- **A = timeout**（`claude code §5.1 / §5.5`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:195–211`、`D39CB17B051B:265–280` 双源独立确认（per-cell `http_status == -1` + median 30s latency；`skill_a_p_a_60cells.py:54–67` 自身 incrementing logic）。
- **A = 残差项**（`coze 逐行重算一`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:108–114` `T + R + A = 30` 守恒成立 → A ≡ 30 − T − R → 残差 → "把 A 当独立通道读，会把残差读成新发现"。

### §2.9 邀请函是"框架"还是"theme"

- **theme-first 设计被读作更可信**（`claude code §3`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:164` "The framework-free form worked"。
- **Nature 列坍缩成单值抵消了 framework-free 的可读性**（`claude code §3`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:164` "A single additional column would fix it without importing any framework"。

### §2.10 是否存在"严格意义上"的蒸馏实验 artifact

- **存在（Hinton 2015 KD baseline, KT-B1）**（`claude code §5.11`）： `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:362–385`。
- **存在（coze 同样证据链）**（`coze §续四`）： `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:401–445`。
- **否定（邀请函自承）**： `results/_v4_distillation_invitation_2026_09_20_v1.0.md:3D9F73519F6C:26` 与 `:120` 自承"zero distillation, reverse-distillation, or anti-distillation experiment asset on disk"。
- **本稿立场**：两边事实陈述均来自盘上实证据；差异在 §2.10 L26 第一句与第二句的语义边界。本稿不裁决；详见 §6。

---

## §3 种子层整合（S-01–S-40，逐条）

本节对 `_v4_brainstorm_seeds_2026_09_20.md`（`0EB1CFAA2992`，294 行）的 40 条种子逐条记录："哪方点名、原话要点、来源锚；无人点名的种子显式写'无参与方点名'"。每条给出种子的盘上原始问题陈述（一行）+ 参与方独立同向 / 异向观察（多源时合并 + 引）+ 显式标注三方类别。

### §3.1 维度 1（蒸馏本体：什么在转移）

#### S-01 权重级转移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:9–13` "权重多大程度可被'抄写'？**可达上限硬卡学生上限**。资产：V1~V3 无蒸馏资产。性质：纯思辨。"
- 参与方点名：
  - `trae work v1.2 S-01` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:35` "唯一 copy-adjacent 数 on disk 是 file digests——23 byte_sha12 in GLM_2 / 29 content_sha12 in coze。一个 collision test 是 **file**-copy detector，不是 parameter-copy detector。"[`on-disk fact` + `pure speculation`]
  - `coze S-01` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:172–176` "盘上对 V1–V3 主体记录只有字节数与三哈希，无参数量、层数或容量字段。'硬卡'在没有量度上不可复核。"[`on-disk fact` + critique]
  - GLM 主件 S-04+S-01 `assets/11-12-20-756-asset...C78CFB42E33D:33` "S-01 obstacle is access, not physics — weights are bit strings, copyable given access"。[`pure speculation`]
- 显式归属：纯思辨 / file-level collision test 是唯一 on-disk 类比。

#### S-02 表征级转移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:15–19` 表征保留，几何路径；P-G v01 非欧曲率脚手架。
- 参与方点名：
  - `trae work v1.2 S-02` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:37` P-G `d_H_to_canonical / d_E_to_canonical / cos_sim / ratio_H_over_E` 已存在（lines 103–118）。[`on-disk fact` + `re-fit hypothesis`]
  - `Mavis v1.2 S-08`（实质） `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:154` 参 §2.4 立场。
  - `coze §02/S-08/S-30` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:108–114` "A 是残差"批评三通道一致的几何读法。
  - `workbuddy 主件 S-02/S-30` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:120` 见 §2.4。
  - GLM 主件 S-02/S-08/S-30 段 `assets/11-12-20-756-asset...C78CFB42E33D:81` 见 §2.4。
- 显式归属：脚手架存在，几何指纹结论待 verdict。

#### S-03 行为级转移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:21–25` 行为指纹，5 frozen artifact，V20 用途盲测非蒸馏。
- 参与方点名（见 §1.3、§2.1）：`Mavis v1.2`、`trae work v1.2`、`trae code`、`workbuddy 主件`、`kimi 主件`、`kimi brainstorm`、`claude code`、`coze`、GLM 主件、`豆包工作` 主件`—` 全部同向：盘上真实含 outputs 仅 minimax 30 条；行为指纹只有一厂商底。代表性引用：`results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:35` (S-03 evidence) + `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:54` (S-03 evidence/idea/critique/doubt)。

#### S-04 推理链转移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:27–31` CoT / scratchpad 复刻，verdict 非推理链样本。
- 参与方点名：
  - `trae work v1.2 S-04` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:41` `A18BBC703B42:450` arithmetic + `A18BBC703B42:523` distance 单向链，无对侧。
  - `coze S-04` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:178–185` "唯一名为 CoT 的采集脚本 `run_v20_cot_fetch.py` 在 L29 明写 `请逐题直接作答，不要解释。`"，存盘仅 `response_text`；`minimax` 推理只存 token count。`reasoning_tokens` 分布是盘上唯一与推理过程同维度的数字。[`on-disk fact`]
  - `claude code §5.8` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:319–327` 27/30 record `reasoning_tokens > 0`，sum 3,972 tokens；29 个非空 outputs 总 76 字符。"trace is measured and not stored: reasoning tokens without reasoning text"。[`on-disk fact`]
  - GLM 主件 S-04+S-01 `assets/11-12-20-756-asset...C78CFB42E33D:33` "R1-series, arXiv:2501.12948" 把"hardest to copy" 读弱为"hardest to copy *without leaving a trace*"。[`pure speculation`，memory-recalled]

#### S-05 校准与置信度转移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:33–37` "知道自己不知道"；`boss_pa_1` 540 非校准。
- 参与方点名：
  - `trae work v1.2 S-05` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:43` 9 × 60 partition T 384 / R 78 / A 78，无 ECE、refusal threshold、confidence histogram。读 A540 为 abstention rate / T540 为 answer rate 是 re-fit。[`on-disk fact` + `re-fit hypothesis`]
  - `claude code §1.3` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:34` T/R/A 守恒无方差，540 是 conservation count，不是 evaluation。
  - `claude code §5.5` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:265–280` A slot `count_t_r_a_from_cells` 自承 "不出现, 占 0"；实际填的是 transport failure。
- 显式归属：盘上无 ECE / confidence histogram；A 通道是 HTTP timeout。

#### S-06 拒答边界转移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:39–43` 拒答边界被学生复刻；`phase1_60cells` 51/60 = 85.0% STRONG_PASS。
- 参与方点名：
  - `Mavis v1.2 S-06` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:64` "60 cells 是否 probe refusal-bearing prompts 无从判断"。[`re-fit hypothesis` + critique]
  - `trae work v1.2 S-06` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:45` "51/60 cells 是 arithmetic questions with gold answers；'refusal' has no label anywhere"。[`on-disk fact`]
  - `workbuddy 主件 S-04` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:126` "0.867 这个数在盘上是 CoT 条目下带 'CoT 未公开对比' 限定语"，与 §2.3 引用不同源。[`on-disk fact`]
  - `claude code S-06` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:92–98` "S-06 is the clearest case in the field of a seed whose asset line creates a false affordance. A reader sees a byte count and a hash, and the hash is real, so the seed *looks* anchored. It is not." [`on-disk fact` + critique]
  - `coze S-06` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:51` 86.67% vs 85% 同文件并存（同 §1.9）。
  - `豆包工作 brainstorm 想法 17` `assets/11-12-20-766-asset...A18E58C8E2A3:84` "拒绝边界扰动厚度"，重用 `deposon_v2_phase1_60cells_2026_09_11.json` 但未获得。[`re-fit hypothesis`，声明未获资产]
  - GLM 主件 S-06 段 `assets/11-12-20-756-asset...C78CFB42E33D:35` "the record is a single-backbone per-cell correctness rate; no refusal-event field appears"。
- 显式归属：盘上无 refusal-event 字段；与 S-06 "拒答边界" 名称不匹配。

#### S-07 输出分布指纹（见 §1.3 / §2.1）

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:49–53` 仅凭输出识别"蒸馏产物"。
- 参与方点名：见 §1.3 与 §2.1 的所有引用。
- `trae code §S-07` `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:29–36` 主例是 P-K 盲测 `576EAF8D7431` FPR 0.0 → 0.0444（`05FF758AE921` rerun），归因为 JSON 键路径重叠（`71D5C23D8C95` audit L100）；最尖锐子问：**本栈中多少跨模型判别信号是格式而非行为？**[`on-disk fact` + `re-fit hypothesis`]
- `claude code §1.6` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:46` GLM_1 是唯一 by_model 件"reference a second model"，与 S-17 联动。

### §3.2 维度 2（可观测信号：怎么知道发生了蒸馏）

#### S-08 embedding 几何对齐

- 见 §2.4。`trae work v1.2 S-08` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:51` `AB75889EE738:103–118` 已有 cos_sim 0.9993 / ratio_H_over_E 8.0316；embedding tensor 不存。[`on-disk fact` + `re-fit hypothesis`]
- `Mavis v1.2 S-08` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:80` P-G verdict_pending 必须 lift 后才能引用。
- `claude code §S-08 / S-30` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:65–69` `deposon_volcengine_22caption_embedding_2026_09_10.json` (SHA-12 `C4B774C8E34C`) `ratio_intra_inter = 1.0562`、`ari_gt_vs_kmeans_k4 = 0.0615`，主张 geometric alignment 难被 prompt 伪造的命题被模板主导反驳。
- `workbuddy 主件 S-08` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:114–117` `063AC8D00542:102–113` 五 embedding / 六 embedding 全 NOISE；该文件另含 `deposon_volcengine_embedding_30cells_2026_09_10.json` 与 22caption embedding 不在 §8 表中（"两个文件不在 §8 表里"）。
- `workbuddy part2 §3 S-08 上调` `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:46` L80 "vision embedding 拓扑无区分度（本质问题）" — 由保留意见上调为带根因否定。

#### S-09 logit 偏移与温度响应

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:61–65` "deposon 不存 logit 级 artifact"。
- 参与方点名：
  - `Mavis v1.2 S-09` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:88` 接受 §2.10 L124 无 logit，但建议扩展。
  - `trae work v1.2 S-09` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:53` temperature 仅以 T = 2.0 字面常量（`268AB1239A8A:7`）出现，未扫变量。[`on-disk fact`]
  - `coze S-09` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:188–194` "在一件制品上成立；同一批四件根本不是生成制品。"[`on-disk fact` + critique]
  - GLM 主件 S-09/S-14 段 `assets/11-12-20-756-asset...C78CFB42E33D:75` §2.7 同上。`codex brainstorm` (落盘见 §4.11) `temperature is service-side, not model-side`。
  - GLM addendum `assets/...8295C3201F20:57–62` "frozen decoding zero": `deposon_volcengine_minimax_m3_30cells_2026_09_10.json:6` 顶层 temperature 0.0、max_tokens 1024；minimax 30 cell latency、usage、correctness 在 `9E1CCBDCEACC` L26–48。 [`re-fit hypothesis, not calibrated`]
  - `豆包工作 brainstorm 想法 1` `assets/11-12-20-766-asset...A18E58C8E2A3:13` "词表分布形状在温度缩放下的不变性残留"，无磁盘锚。[`pure speculation`]

#### S-10 扰动敏感性（见 §1.5）

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:67–71` V7 报告扰动针对判别任务。
- 参与方点名：`claude code §1.2`、`trae work v1.2`、`workbuddy part2`、`kimi 主件`、`coze` 同向（见 §1.5）。
- 唯一例外：`trae code §S-10` `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:57–61` 主例不是 V7 而是 `FBB7677B9CD5:748` thousands-separator regex，"a scoring-harness regex flipped one cell with zero change in model output"。[`on-disk fact`]

#### S-11 长尾一致性

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:73–77` 长尾事实；18 anchors + 21/22 caption + 5 KT。
- 参与方点名：
  - `Mavis v1.2 S-11` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:102–108` 22 captions + 15 anchors = 37-cell library。
  - `kimi 主件 S-11` `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:31` KT 15 锚 + 22 字幕 + 18 锚（边角案例库真实存在）；与 S-40 有张力："案例库是同一管线约一周的迭代产物，不是独立时间快照"。
  - `coze S-11` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:63–65` 实测 22 caption entries，与 §2.6 一致；但"5 KT-ABC1 anchors"措辞歧义。
  - `claude code §S-11` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:104–110` 22 是 label sets，"not a set of caption-fingerprint pairs that happen to number 22"。[`on-disk fact`]
  - `豆包工作` 主件 S-11 段 `assets/11-12-20-747-asset...19C97B5CFF3C:42` 同向；GLM 主件 S-11 段 `assets/11-12-20-756-asset...C78CFB42E33D:41` S-11 asset's "long-tail-fact consistency" is unsupported by content。
- 显式归属：22 captions 实为 graph label sets；与"长尾事实"语义差一档。

#### S-12 时间相关性与模式漂移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:79–83` 时间指纹无直接对应。
- 参与方点名：
  - `trae work v1.2 S-12` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:59` 时间戳标 *files* not behaviours：minimax meta 2026-09-16 over run 2026-09-10 (`9E1CCBDCEACC:2–7`)。[`on-disk fact`]
  - `trae code M-1` `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:175` "学生蒸馏在 t 冻结教师的时态分布" — 五件 artifact 都是单次快照。[`re-fit hypothesis`]
  - `claude code S-40` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:156–158` "two of three timestamps are the same day. A time series with one time point and one replication seven days later is a very short baseline." [`critique`]
  - `coze S-12` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:196–201` 口径代号是一级字段，`backbone_alias` / `embedding_model`。[`on-disk fact` + critique]
  - `豆包工作 brainstorm 想法 23` `assets/11-12-20-766-asset...A18E58C8E2A3:113` "蒸馏的版本控制问题"。[`pure speculation`]
  - GLM addendum "Non-stationary decision lines" `assets/...8295C3201F20:63–67` P-E 阈值漂移 0.10 → 0.5 → 0.30 (`063AC8D00542:375`)。[`re-fit hypothesis, not calibrated`]

### §3.3 维度 3（反蒸馏：检测侧）

#### S-13 隐写式指纹

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:89–93` 指纹是判别指纹，**非**输出水印指纹。
- 参与方点名：
  - `Mavis v1.2 S-19`（实质） `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:134` "on-disk anchor is named, but the anchor is not a substrate for the seed"。
  - `trae work v1.2 S-13` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:63` 最近邻是 `B5873AFB9D29` 的 `dual_24bit` 指纹：`byte_hash[:6] + 12-bit semantic hash (SVD-2, seed=42)`。**projection basis 是公开常量，不是 covert mark** — **checksum, not covert mark**。[`on-disk fact`]
  - `kimi 主件 S-13/S-19` `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:27` byte_hash = SHA-256(caption_id)[:12]，绑的是 caption_id 而非模型输出。
  - `claude code §5.9` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:329–340` 22 件的 12-bit LSH 坍缩到 6 distinct values (`2fd`×10、`2dd`×6、`498`×2、`6d8`×2、`6dc`×1、`2dc`×1)；mean pairwise Hamming 1.961（expected 6.0）；62 of 231 pairs at Hamming 0 — 跨 family 同代码（`2fd` 含 L 与 S）。[`on-disk fact`]
  - `coze N-06` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:363–371` Merkle 链原型：22 caption + 12-bit semantic hash，6 个不同取值覆盖 22 条内容。[`re-fit hypothesis`]
  - GLM addendum "Birthmarks, not watermarks" `assets/...8295C3201F20:69–73` "22-caption fingerprint is a birthmark: re-use is a resilience question, distillation one obfuscation transform, 'stealth watermark' the wrong noun"。[`re-fit hypothesis, not calibrated`]
  - `workbuddy 主件 S-13/S-19` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:130–132` `strip_captions_22` 每条只有 `id/text/family/structure/n_labels`，无 fingerprint field — **"指纹"是范畴错误**。[`on-disk fact` + critique]

#### S-14 训练动态反演

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:95–99` "评估管线动力学 ≠ 训练动力学"；`d7_5anchor_60cells_9model_verdict_2026_09_18.json` 是终态 verdict。
- 参与方点名：
  - `Mavis v1.2 S-14` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:110–114` 即使无训练曲线，弱形式可建（9-model verdict matrix 是 cross-model pattern）。[`pure speculation`]
  - `kimi 主件 S-14` `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:29` 540 件是 22 图重复博弈 + 守恒审计，无任何训练曲线；S-14 标纯猜想。[`on-disk fact`]
  - `trae work v1.2 S-14` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:65` `verifier/runs/2026-09-04_pd_v0.jsonl` (`5042869BDF85`, 100 字节) 是唯一轨迹形对象，一 link 链不能 exhibit a jump。[`on-disk fact`]
  - `coze S-14` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:67–69` 读毕 4505CCA79C15：`9 backbone × 3 probe` 矩阵；时间序列、loss、reward 字段零命中。[`on-disk fact`]

#### S-15 输出统计异常（被多方推为最有追的种子之一）

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:101–105` `corpus/v20/by_model/` 提供统计基线样本。
- 参与方点名：
  - `Mavis v1.2 §3.9 + §4(a)` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:116` "Of the 40 seeds, S-15 is the one I find most worth pursuing. The seed's 'why interesting' line ... is the strongest framing in the seed field for a theme-first inquiry"。
  - `kimi 主件 S-15` `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:23` 五件真实含原文的是 minimax 30 + phase1 逐格 llm_raw_response，"它今天不是五厂商层，而是'一厂商 30 条 + 一管线 60 格'"。[`on-disk fact`]
  - `trae work v1.2 S-15` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:67` P-K 13 features (`log_bytes, log_lines, is_json, log_keys, json_depth, key_vocab_overlap, cjk_ratio, ws_ratio, digit_ratio, alpha_ratio, punct_ratio, byte_entropy8, log_mean_line`) → capped z-mean @ T=2.0 (`576EAF8D7431:8–27`)；`log_bytes` 与 `byte_entropy8` 是容器统计。[`on-disk fact` + critique]
  - `workbuddy 主件 S-15` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:136–140` `063AC8D00542:227` "P-F 联合方案无差异化" (DeepMind 2022 / Google 2023 95%/1% 的先验评估)。[`on-disk fact` + 未验证转述]
  - GLM 主件 S-13+S-16+S-18 `assets/11-12-20-756-asset...C78CFB42E33D:47` "30 个 0–7 字符 strings 不足以支撑 distributional claim". [critique]
  - `豆包工作 brainstorm 想法 21` `assets/...A18E58C8E2A3:101` "信息论基线指纹"，重用假设但声明未获资产。[`re-fit hypothesis`]
  - GLM addendum "Difficulty-band shape" `assets/...8295C3201F20:51–55` "在已 pin retrieval 的新-30 跑批中，29/30 top-1 retrieval 返回 S2_n35（相似度 0.9999999984–1.0000000092）"。[`re-fit hypothesis, not calibrated`]

#### S-16 成员推断

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:107–111` 训练集成员推断无直接对应。
- 参与方点名：
  - `trae work v1.2 S-16` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:69` "26 own 是成员 by construction"，唯一 declared 非成员 in two held-out families (`576EAF8D7431:45–48`)。[`on-disk fact` + `pure speculation`]
  - `workbuddy part2 §5 S-16` `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:74–78` "d<T 判自家是 member test；FPR=0.0444, FNR=0.0 — 这是 re-fit"。[`re-fit hypothesis`]
  - `coze §五 5` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:148–152` 九模型来自四份互不校准的提交（`worker_a/b/c/d` + `9model_complete` + `minimax-m3_standalone`），身份跨层不稳定（`minimax` vs `minimax-m3`）。[`on-disk fact` + critique]

#### S-17 跨模型溯源（见 §2.6，被多方推为最有追种子之一）

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:113–117` 5-model blind-test 是 known teacher candidate 原型。
- 参与方点名：
  - `Mavis v1.2 §3.10` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:122–126` 5-vendor blind-test 是 prototype；但 coze 不在 9 backbone。
  - `trae code §S-17` `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:41–46` GLM_1 是 complete provenance experiment in miniature；最 answerable question 是 "which build discipline"，**artifact 可能按 producer-side construction discipline 分组比 vendor 更强**。[`on-disk fact` + `re-fit hypothesis`]
  - `trae code §5.7` `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:298–317` 自修正：S-17 仍推荐，但该文件 `overall_verdict: "FAIL"` —— FPR 阈值 `1/100` 在 N=45 时不可达（最小非零 FPR = 1/45 = 0.0222）。
  - `workbuddy 主件 §五(a)` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:158` S-17 是 40 条里唯一一条"盘上已存在量好、预登记、带实测误差结构"的仪器。
  - `claude code §S-17` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:118–126` `task` line 名 "基线: 自己 vs GLM vs KIMI"；`metrics` block 给出 GLM measured anti-whitewash 0.9130 beside KIMI frozen_ref 22。[`on-disk fact` + `re-fit hypothesis`]
  - `豆包工作` 主件 `assets/...19C97B5CFF3C:27` 同向；`codex brainstorm` (落盘见 §4.11) "Mixture ancestry" — 5 corpus artifacts 不能建立该子问。
  - `kimi brainstorm` `BC14F47D927D:7` 真正的同输入跨厂商素材不在 `by_model/`，在 `results/` 下 6 件 `deposon_*_30cells`。

#### S-18 蒸馏痕迹的统计签名

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:119–123` "几乎不可能由独立训练产生"的签名。
- 参与方点名：
  - `Mavis v1.2 §3.11` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:128–132` 建议拆为 S-18a (adversarial erasure) + S-18b (cross-distillation erasure)。[critique]
  - `trae work v1.2 S-18` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:73` signature survival = 22/22 W1/W2/W3 + 0.9556 三 way（`576EAF8D7431:344–361`、`A30FF093305D:45`）。[`on-disk fact`]
  - `coze 逐行重算三` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:128–134` 同一对 (T,A) 算出两个不等相关系数（`_count -0.81` vs `_fraction_v5 -0.92`），下游仅保留 -0.81。[`on-disk fact` + critique]
  - GLM 主件 S-13+S-16+S-18 `assets/...C78CFB42E33D:47` "the actual blank is a distillation-specific null model — a statistic 'almost impossible to produce by independent training' (the seed's words) — restating §4 item 1"。[`pure speculation`]

### §3.4 维度 4（防蒸馏：防护侧）

#### S-19 输出水印

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:129–133` "21/22 caption 指纹与水印技术栈无关"。
- 参与方点名：
  - `Mavis v1.2 §3.12` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:134–138` 22 caption 与 watermark 技术栈无关。[`on-disk fact`]
  - `trae work v1.2 S-19` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:77` watermark 不存在；caption chain input 是 hash over `state|caption_id|dual_24bit` (`B5873AFB9D29:43–46`)。[`on-disk fact`]
  - `coze §S-13/S-19` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:27` 同向。
  - `codex brainstorm` (落盘见 §4.11) "Watermark survivability" — re-fit, no calibrated watermark finding claimed。
  - GLM 主件 S-19+S-26 `assets/...C78CFB42E33D:55` "Watermark–quality tension is a studied axis of the Kirchenbauer line; distillation-surviving watermarks exist directly" [memory-recalled]。

#### S-20 训练数据毒化

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:135–139` "以毒攻毒"；`attacks/` 用途非蒸馏防护。
- 参与方点名：
  - `Mavis v1.2 §3.13` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:140–144` 三件 `attacks/` 路径 + SHA-12 + "用途非蒸馏防护"。[`on-disk fact` + critique]
  - `trae work v1.2 S-20` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:79` `a1_delete_anchor.py` L50–86 准备 5 锚、unlink 第 3、`compute_root` 调用；A1 修订说明 (L11–L16) 移除 `--missing` 分支。[`on-disk fact`]
  - `coze S-20` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:212–217` 三件均不触被保护对象，只动审计底座；`a1` 修订说明移除 `--missing` 分支。

#### S-21 信息瓶颈

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:141–145` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-21` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:81` P-K 13 维、z capped at 8、std_floored at 1e-6、T=2.0；largest own distance 1.296 (`576EAF8D7431:68`)。[`on-disk fact`]
  - `coze §续四` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:429–431` KD 失真 0.0028 vs deposon 0.5 占位值；S-21 从无先验思辨变成"有一条可引用的既有对照"，但不可比。

#### S-22 能力隔离 / 子模型切片

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:147–151` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-22` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:83` "9 backbone 与 5-artifact 不相交且 mapping 未声明" — slicing-as-defense 继承该空缺。[`on-disk fact`]
  - `coze S-22` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:220–226` `coze_artifact_v_2026_09_16.json:5` 已有 `subject_label_location` "仅本 meta 层(盲测时由判别方剥离文件名与该字段)" — 该约定剥离的是**来源身份**不是能力。[`on-disk fact` + critique]

#### S-23 对抗性扰动

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:153–157` `attacks/` 用途非蒸馏防护。
- 参与方点名：
  - `Mavis v1.2 §3.13` 实质。
  - `trae work v1.2 S-23` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:85` A2 是 canonicalisation 不是 perturbation：serialize 两次（path-sorted、size-sorted）要求 root 变化 + verification fail (`3D54B277620E:46–58, 61–87`)。[`on-disk fact`]
  - `coze S-23` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:228–232` 三件均在文件系统与清单层，无输入空间扰动。

#### S-24 行为签名诱导

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:159–163` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-24` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:87` P-K 13 ratios 含 `cjk_ratio` / `punct_ratio` (`576EAF8D7431:8–22`)，token-level filter 不动；同一向量对容器 transforms 响应，0.9556 而非 1.0。[`on-disk fact`]
  - `trae code §D-8` `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:153` "scorer-family loss curves" — format vaccine + inheritable honeypot。[`re-fit hypothesis`]

### §3.5 维度 5（反-防蒸馏：防护被绕过时）

#### S-25 对抗升级

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:169–173` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-25` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:91` 删除/重排/改链记录/白名单 — escalations answered inside the verifier, not by raising attacker cost。[`on-disk fact`]
  - GLM 主件 S-25+S-28 段 `assets/...C78CFB42E33D:61` "S-25's adversary has already escalated once" — Krishna 2023, Sadasivan 2023, Moulin–O'Sullivan 2003。 [memory-recalled]

#### S-26 水印擦除

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:175–179` 无直接对应。
- 参与方点名：
  - `Mavis v1.2 §3.14` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:146–150` Dimension-5 (S-25–S-29) uniformly "no direct match"，gap 本身是信息。
  - `trae work v1.2 S-26` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:93` erasure not all-or-nothing: 22/22 W1/W2/W3 + 0.9556 三 way (`576EAF8D7431:344–361`、`A30FF093305D:45`)。[`on-disk fact`]
  - GLM 主件 S-19+S-26 `assets/...C78CFB42E33D:57` paraphrase / distortion-free / undetectable 三层擦除。[memory-recalled]

#### S-27 防护探测

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:181–185` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-27` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:95` `verify_root(manifest_str, claimed_root)` 不读盘 (`fingerprint_v0.py:110–118`)；`verify_chain` 把跨文件 continuity 标 out-of-scope (`:184–191`)。[`on-disk fact`]
  - `codex brainstorm` (落盘见 §4.11) "Query-budget economics" — pure speculation。

#### S-28 蒸馏者-防护者博弈

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:187–191` 无直接对应。
- 参与方点名：
  - `workbuddy part2 §4 S-28/S-29` `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:54` 三台博弈机器：`boss_pa_1` DIFFERENTIATED (L339–340)；`boss_pa_2` DIFFERENTIATED (L235–236, 13.6%)；`boss_pa_3` DIFFERENTIATED (L327–328, 0.0%)。单群体模型，无对手方。[`on-disk fact` + critique]
  - `coze S-28` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:244–250` "势函数判据只在 3/22 图上成立、复制子与 ESS 判据 0/22 成立——这是已经跑完的负向结果"。[`on-disk fact`]
  - `coze Closing(b)` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:457` S-28 + S-29 最不产：观测量是跨期的，栈是单期冻结。
  - GLM 主件 S-25+S-28 `assets/...C78CFB42E33D:61` Moulin–O'Sullivan 信息隐藏博弈。[memory-recalled]

#### S-29 长期均衡

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:193–197` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-29` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:99` 唯一 cost figure on disk 是检测器 0.002 s (`A30FF093305D:20`)。[`on-disk fact`]
  - `Mavis v1.2 S-26` 实质一致。
  - `trae work v1.2 Closing` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:139` "S-29, long-horizon equilibrium ... its object is a five-year cost-benefit trajectory, and the only cost figure on disk is a 0.002-second detector runtime ... which is not the quantity the seed needs"。
  - `coze Closing(b)` 同向（见 S-28）。

### §3.6 维度 6（跨学科种子：类比工具，optional）

#### S-30 双曲几何 / 曲率差异

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:205–209` P-G v01 非欧曲率脚手架。
- 参与方点名：见 §2.4。

#### S-31 观察者效应 / 测量即扰动

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:211–215` 磁盘无 observer-effect frame artifact。
- 参与方点名：
  - `Mavis v1.2 §3.16` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:158–160` "behated" 笔误（同 §1.2）。
  - `claude code S-31` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:128–132` `skill_d_p_f_observer_result_2026_09_11.json` 是 monitoring observer，不是 measurement-perturbation observer；"observer" 在本仓库 loaded term，建议 §2.10 加一行 disambiguation。[`on-disk fact` + critique]
  - `workbuddy part2 §8 S-39` `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:114–122` "盘上无对应 artifact"，与人介入改变评测方向的 `user_trigger_2026_09_11_11_44` 不同。[`on-disk fact`]
  - `豆包工作` 主件 `assets/...19C97B5CFF3C:35` "API 黑盒探测 ... 任何基于重复查询的指纹采集都在向目标系统注入输入分布的扰动"。
  - GLM 主件 S-31+S-32+S-35 `assets/...C78CFB42E33D:79` "single API calls are stateless — a probe does not change weights"。

#### S-32 不可克隆定理类比

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:217–221` 无直接对应。
- 参与方点名：
  - `Mavis v1.2 §4(b)` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:188` S-32 最不产；teacher is function, not quantum state; "no-cloning theorem for neural networks" 要么 trivial, 要么 vacuously false。
  - `trae work v1.2 S-32` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:107` `FEE04170AA73:9–10` `anchor = sha256(trust_anchor_5_concat | artifact_id | content)` — defensible analogue is "a copy is not identity-preserving in this stack"，弱于 no-cloning theorem。[`on-disk fact`]
  - `claude code S-32/S-35` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:135–142` No-cloning needs linearity + impossibility of copying unknown state；weights are classical parameters; Bell test needs measurement-independence。[`pure speculation`]
  - `workbuddy brainstorm §二矛盾三` `assets/...8295C3201F20:67` no-cloning 是最可能的"假朋友"，应同时收录反驳。
  - GLM 主件 S-31+S-32+S-35 段 同向。

#### S-33 纠缠 / 上下文耦合

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:223–227` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-33` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:109` caption layer (`EFE05AD775DE:324–326`) 是 decoupling substrate；`6A2656878745` 是同 22 editable texts。[`on-disk fact`]

#### S-34 退相干 / 推理坍缩

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:229–233` V7 verdict 是判别 verdict；推理链样本无直接资产。
- 参与方点名：
  - `trae work v1.2 S-34` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:111` S4 `crosslinked_layered_dag` N=40, 88 edges, 58 named；S5 `sparse_random_dag` N=45, 49 edges, 7 named — near-equal size, opposite backbone density。[`on-disk fact`]
  - `coze S-34` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:252–258` "该种子问'坍缩'，而盘上**没有任何'学生的输出'** — 观测对象本身不存在"。
  - `claude code S-32/S-35` 段认为 S-34 至少 has measurable phenomenon，可保留。

#### S-35 Bell 不等式类比

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:235–239` 磁盘无 Bell-inequality frame artifact。
- 参与方点名：
  - `trae work v1.2 S-35` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:113` 9-model × 3-probe 矩阵（`4505CCA79C15:56–57, 95–96`）；"analogy stays formal"。[`on-disk fact`]
  - `claude code S-32/S-35` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:138–142` "Bell test needs measurement independence and a theorem-level bound to violate; 'independent training' is a common cause"。
  - GLM 主件 S-31+S-32+S-35 段同向。

### §3.7 维度 7（评测学：蒸馏检测的 ground truth）

#### S-36 ground truth 困境

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:245–249` GT 不唯一。
- 参与方点名：见 §2.3（被多方推为最有追种子）。

#### S-37 假阳 / 假阴代价

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:251–255` D7 + boss 540 骨架；用途不同。
- 参与方点名：
  - `Mavis v1.2 §3.18` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:168–172` "9 × 60 = 540-cell discrimination grid with heterogeneous labels (8 PASS + 1 GRAY for P-A; 6 PASS + 2 GRAY + 1 FAIL for P-E)"。[`on-disk fact` + `re-fit hypothesis`]
  - `kimi 主件 S-37` `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:25` "GLM_1 已把困难量化：glm_vs_kimi_pairwise_separation = 0.6146 (L640，仅描述性观测)；d 区间高度重叠"。[`on-disk fact`]
  - `trae work v1.2 §一（二）` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:92–98` GLM_1 0.0444 / 0.9556 与 W1/W2/W3 抗洗白 0.9556 — 缺口在语义擦除测过、语法擦除未测。[`on-disk fact`]
  - `workbuddy 主件 S-37` `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:110–112` FPR=0.0444 / FNR=0.0 的不对称是实测的 — "在低基率世界里的正确用法不是抓人，是放行"。[`re-fit hypothesis`]
  - `claude code §S-37` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:71–76` `LETTER_FROM_TRAE_3RISK_2026_09_11.md:24` "metric-selection decision under pre-registered criteria: Spearman 0.9958 rejected for zero increment; constant metric rejected for zero variance; adopted metric Spearman −0.832"。[`on-disk fact` + `re-fit hypothesis`]
  - `coze §逐行重算六（六）` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:154–162` 厂商内版本对照对：doubao 2.0-lite vs evolving vs 2.1-turbo；deepseek v4-flash vs v4-pro — 同族跨版本 "天然对照对"。[`on-disk fact`]

#### S-38 可复现性 / 跨实验室一致性

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:257–261` V2/V3 多 backbone × 多 cell 复现性友好。
- 参与方点名：
  - `workbuddy part2 §3 S-38` `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:23–46` "唯一一条盘上已经发作过的失败" — DELTA_ratio_f3 = 1.3031 vs DELTA_ratio_independent = 1.0479 (`063AC8D00542:74–82`)。[`on-disk fact`]
  - `claude code S-38` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:154` "V1–V3 multi-backbone × multi-cell design is itself reproducibility-friendly ... is a claim about artifacts being present and re-derivable, and one of them is not" (`deposon_v20_baselines.json` 不在)。
  - `coze S-38` `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:260–275` 4 对 `…_p_l_v3_vector_embedding_*` 同口径同日相隔数分钟重跑：83.0% / 73.2% / 76.4% / 69.8% 不同行占比。[`on-disk fact` + critique]
  - GLM 主件 S-36 段 `assets/...C78CFB42E33D:71` "Carlini 2022 'Membership Inference Attacks From First Principles'"。[memory-recalled]

#### S-39 评测-被评测的递归

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:263–267` 无直接对应。
- 参与方点名：
  - `trae work v1.2 S-39` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:123` `FEE04170AA73:5` 已 assume evaluated party should not know its identity, stripping filename + subject field。[`on-disk fact`]
  - `workbuddy part2 §8 S-39` 见 S-31。
  - GLM 主件 S-13+S-16+S-18 `assets/...C78CFB42E33D:47` 自我陈述不构成 GT；与"相信被疑蒸馏模型的自述"同构。[`pure speculation`]

#### S-40 长期有效性与漂移

- 种子原话： `results/_v4_brainstorm_seeds_2026_09_20.md:0EB1CFAA2992:269–273` V2(09-11) → V3(09-11) → D7(09-18) 时间序列可作 drift 脚手架。
- 参与方点名：
  - `Mavis v1.2 §3.20` `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:180–182` "7-day drift window ... short by long-term standards"。[`re-fit hypothesis`]
  - `trae work v1.2 S-40` `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:125` 三个 dated snapshots 跨 8 天 + threshold-drift record (`063AC8D00542:375`)。[`on-disk fact`]
  - `kimi 主件 S-11` 张力段 `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:31` 案例库是同一管线约一周迭代产物。
  - `claude code S-40` `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:156–158` "Two of the three timestamps are the same day"。[`critique`]
  - `codex brainstorm` (落盘见 §4.11) "Signature half-life" — re-fit, no calibrated half-life。
  - GLM addendum "Non-stationary decision lines" `assets/...8295C3201F20:63–67` P-E 阈值漂移 0.10 → 0.5 → 0.30 (`063AC8D00542:375`)。[`re-fit hypothesis, not calibrated`]

### §3.8 显式无参与方点名的种子（无人点名）

本稿对全部 40 条做点名核验后，**所有 40 条均有 ≥1 个参与方引用**。S-14 仅 `Mavis v1.2`、`trae work v1.2`、`kimi 主件`、`coze` 四源覆盖，是覆盖源数最少的一条，但已构成 §3.3 内独立同向。无完全无点名的种子。

---

## §4 各方新增候选设计（不在 S-01–S-40 内，按参与方分节）

本节**记录各参与方在 S-01–S-40 之外提出的新增种子 / 想法**。每项按发起方分节，标注 on-disk fact / re-fit hypothesis / pure speculation 三类之一。

### §4.1 Mavis

- Mavis v1.2 §3.16：`results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:158` "behated" 笔误（同 §1.2 引）。
- Mavis v1.2 §4(c)： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:194` "What is the smallest deposon-side extension that would lift the theme from 're-fit hypothesis' to 'calibrated finding'?"（扩展种子的种子）。
- Mavis v1.2 §4(d)： `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:196` "Is the V1–V3 asset stack large enough to support a theme that, by construction, requires both teacher-side and student-side samples?"（§4 增补项）。[`on-disk fact` + `pure speculation`]

### §4.2 trae work

- N-01 至 N-09 列表 `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:129–135`：
  - N-01 "What the second index adds" (`EFE05AD775DE:317–326` vs `8423FFE266AF` 7,335 B) — fingerprint layer 后续 add-on。[`on-disk fact`]
  - N-03 "An anchor is not content-only"（同 `FEE04170AA73:9`）。[`on-disk fact`]
  - N-04 "What anchoring does to falsifiability" (`063AC8D00542:372–373`)。[`on-disk fact`]
  - N-05 "The label boundary is a subject, not a relation" (`FEE04170AA73:5`)。[`on-disk fact`]
  - N-06 "Is the nine-to-five mapping partly recoverable?" (`AB75889EE738:33–88` 与 by_model 名字匹配)。[`re-fit hypothesis`]
  - N-08 "Counting independent measurements" (`AB75889EE738:338` spearman_rho_H_vs_E = 1.0)。[`on-disk fact`]
  - N-09 "How many independent sides the corpus layer has" (`FEE04170AA73:6` 29 件 from one subject)。[`re-fit hypothesis`]
- trae work v1.2 §6 名额： "**For every cross-vendor statistic in this stack, how many independent sides does the denominator actually contain — and which on-disk artifact states that number?**" — 建议补 §4 项。

### §4.3 trae code

- trae code Addendum I 五项实验设计 `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:81–129`：
  - **A**：Null-model attribution floor for five-artifact panel — 提议 `structure-only baseline` (artifact JSON key-path vocabulary) 是否逼近 4.4% FPR。[`re-fit hypothesis`]
  - **B**：Trap-benchmark spec brought on disk — V1 paper trap precedent (arXiv:2609.09001) 100% vs 7%/10%，pre-registered。[`pure speculation` for the distillation transfer]
  - **C**：Measurement-instrument stability probe — thousands-separator regex flipped (`FBB7677B9CD5:748`); JSON key-vocab (audit L100)。[`re-fit hypothesis`]
  - **D**：Format-vs-behavior decomposition — format-normalized projection。[`re-fit hypothesis`]
  - **E**：Variance-and-increment gate — `LETTER_FROM_TRAE_3RISK_2026_09_11.md:24` Spearman 0.9958 / -0.832 precedent。[`re-fit hypothesis`]
- trae code Addendum II D-1 ~ D-8 + X-1 ~ X-8 + M-1 ~ M-3 `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:139–185`：
  - **D-1**：A|T residual as cross-generation inheritance fingerprint (`3FA0FF2C8C08:243` corr_TA -0.8128)。[`re-fit hypothesis`]
  - **D-2**：Difficulty-controlled error co-occurrence residual。[`re-fit hypothesis`]
  - **D-3**：Format-channel pollution + pre-mortem alarm (`576EAF8D7431` + audit L100)。[`re-fit hypothesis`]
  - **D-4**：Append-only chain as transparency log。[`re-fit hypothesis` + `pure speculation` for protocol]
  - **D-5**：Entropy ledger for reverse-distillation — pseudo-distillation, then unlearning, then residual distance。[`pure speculation`]
  - **D-6**：Template-subspace elimination — 22-caption negative result dissection。[`re-fit hypothesis`]
  - **D-7**：Conservation-constrained masquerade feasibility。[`pure speculation`]
  - **D-8**：Scorer-family loss curves — format vaccine + inheritable honeypot。[`re-fit hypothesis`]
  - **X-1**：Daubert-style admissibility audit。[`re-fit hypothesis`]
  - **X-2**：Renormalization-group universality — T_frac fixed point + A_frac irrelevant operator。[`re-fit hypothesis`]
  - **X-3**：Rate-distortion anisotropy — fingerprint in long tail。[`re-fit hypothesis`]
  - **X-4**：Distinguisher game + side-channel taxonomy。[`re-fit hypothesis`]
  - **X-5**：Batesian vs Müllerian mimicry。[`re-fit hypothesis`]
  - **X-6**：Zero-knowledge teaching proof。[`re-fit hypothesis`]
  - **X-7**：Maxwell's demon + Bennett-style reversible ledger。[`pure speculation`]
  - **X-8**：Spence's costly signaling + lemon market。[`pure speculation`]
  - **M-1**：Distillation archaeology via version drift。[`re-fit hypothesis`]
  - **M-2**：Consumption-ceiling argument。[`re-fit hypothesis`]
  - **M-3**：Metaphor audit — deposition vs sublimation。[`on-disk-fact extension` + critique-flavored]
- trae code §5.7 / §4(d)： "**falsification-cost seed**: what would it take for the deposon community to *retract* a distillation-detection claim, and who has the standing to do it"（§4 增补项）。

### §4.4 kimi

- kimi 主件 §四(c)： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:43` 「同输入跨厂商输出对比作为行为基线，今天能建成什么样」 — 介于 S-03 与 S-07 之间。
- kimi 主件 §四(d)： `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:45` "哪些盘上工件真的含模型输出原文，哪些只有哈希或判别值？"（§4 增补项）。
- kimi brainstorm §二：1–16 条 ideas（围绕回流环路 / 同输入输出层 / 判别-防御层 / 协作元层）。代表性：
  - 想法 3：生成臂跨厂商对照（L 族 provenance + preregistered prompt_sha256）。[`pure speculation`]
  - 想法 8：登记条目应存 byte_sha12 级可重算锚 (`L405–411`)。[`on-disk fact`]
  - 想法 9：锚/脚手架混合台账作"金丝雀登记处"姿态。[`re-fit hypothesis`]
  - 想法 10：固定公开阈值可能是博弈面 (T=2.0)。[`pure speculation`]
  - 想法 16：观察者结构闭环（第一人称自述无第三方 attestation）。[`pure speculation`]

### §4.5 workbuddy

- workbuddy part2 §6 S-10 一处找不到： `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:84` "在 V7 报告里检索 `扰动/干扰/攻击/perturb/attack` 只有两行重复的 KT-B1 attack rate 阈值比较，没有鲁棒性曲线族"。
- workbuddy part2 §7 S-36： `BFB4932F4467:104–108` 唯一带标签的 GT 在 `deposon_volcengine_22caption_embedding_2026_09_10.json:104` "4 类，正好对应概念图家族划分"。[`on-disk fact`]
- workbuddy part2 §9(c)： "**一条关于'同一批数据被问两次'的种子**" — "若同一个冻结资产在不同月份被不同的问题重新审问，栈里有没有机制判断第二次的答案是否推翻了第一次？"（建议补 §3）。
- workbuddy part2 §9(d)： "**栈内已存在一次被坐实的非稳健读数（DELTA 1.30 → 1.05，第 74–82 行），它已导致 P-B 降级（第 21 行）**" — 建议 §4 增补自律条款。
- workbuddy brainstorm §三： M-1 "**这台仪器的真实身份是'排除器'，不是'标记器'**" + M-2 "**这台仪器的失败是'单侧'的，而这可能是结构性的**" + M-3 "**一个在铁律之内的语义擦除实验，其实做得成**" + M-4 "**给主题换个主语，维度 4 就成了本土**" — 四条独立想法。[`re-fit hypothesis`]
- workbuddy brainstorm §五(d)：建议 §4 增补 "**盘上已有三处单侧失效 ... 这三次是同一个结构，还是三次独立的事故？**"。

### §4.6 claude code

- claude code §1.5 / §1.6 / §1.7 / §1.9 / §1.10 等横切批评已并入 §1。
- claude code §5.11 "**The invitation's foundational claim is contradicted: a knowledge-distillation baseline was run on 2026-09-10**" — `KT_B1_REWORK_REPORT_2026_09_10.md:83` 失真量 0.0028。[`on-disk fact`]
- claude code §5.12： "the seed field's 'related asset' lines were written from memory of the program rather than from a listing of `results/`, and four of the ten seeds I engaged have affordances that a directory listing would have corrected."
- claude code §4(c)（建议补 §3）： "**falsification-cost seed**: what would it take for the deposon community to *retract* a distillation-detection claim"。
- claude code §4(d)（建议补 §4）： "**which of the assets cited in §8 are expected to still be re-derivable by an outside reader in twelve months, and what happens to a claim whose anchor has moved**" — `deposon_v20_baselines.json` `6edb2aec1660` 已被点名。

### §4.7 coze

- coze §S-17 + N-01 至 N-08 `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:299–395`：
  - **N-01**：端点冒充自己宣称的教师（`deposon_p_l_v3_phase2_closedsource_report_20260917_175544.md` L18, L20–L24, L62–L66）。[`re-fit hypothesis`]
  - **N-02**：归因分辨率下限（同族隔代能不能分开，`_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md` L41–L46, L54–L71）。[`re-fit hypothesis`]
  - **N-03**：能力是训练装入还是上下文装入（`deposon_v41_flash_rag_baseline_2026_09_10.json` L6, L7, L19, L21 vs `deposon_dpath_cross_modal_2026_09_10.json` L2233–L2237）。[`re-fit hypothesis`]
  - **N-04**：评测参照推理本身是模型产物（`deposon_benchmark_v1_4_strategyqa_details.json` 全文 396 处来源标签同值 `kimi_api`）。[`on-disk fact` + `re-fit hypothesis`]
  - **N-05**：指纹比承载物活得久（`deposon_dpath_cross_modal_2026_09_10.json:9` `figures/v3x/corpus_pngs/` 目录存在但文件数为 0）。[`on-disk fact` + `re-fit hypothesis`]
  - **N-06**：语义指纹链作派生证据（Merkle chain on 22 caption；6 个不同 semantic hash）。[`re-fit hypothesis`]
  - **N-07**：核验方的"找不到"与"没痕迹"不可分（`_p_o_stranger_verification_results_2026_09_16.json` L179–L183 only 0 captions）。[`re-fit hypothesis`]
  - **N-08**：逐代自蒸馏被吃掉的尾巴 — **no on-disk artifact**。[`pure speculation`]
- coze Closing(c) 两项建议补 §3：
  - "**资产可用性标注**"（可置于维度 7）— `_v4_brainstorm_seeds_2026_09_20.md:292` 自述 + `063AC8D00542:290` 五锚记载。
  - "**派生列的可复算性**"（可置于维度 7）— `063AC8D00542:121–129`。
- coze Closing(d) 建议补 §4： "*V1–V3 网格内部是否存在互为严格单调变换、或互为同一构造恒等式两种写法的统计量，使得'多处一致'成为保序伪影而非独立证据？*"

### §4.8 豆包工作（主题回复，747）

`assets/11-12-20-747-asset...19C97B5CFF3C`：

- 内部一致性批评 §一 5 项（见 §1）。
- S-36 GT 困境刚性表达 §二。
- S-17 搜索空间压缩 §三。
- S-31 API 黑盒扰动张力 §四。
- S-11 数字可信度削弱种子描述 §五。
- S-07 re-fit 垫脚石 §六。
- S-13/S-19/S-24 互盲 §七。
- Closing(a)–(d)：见 §5。

### §4.9 豆包工作（brainstorm，24 条，766）

`assets/11-12-20-766-asset...A18E58C8E2A3`：

- 想法 1–24（详见原文）：覆盖技术机制（8 条）、产业与实践（7 条）、最小可行实验（7 条）、统筹者补充（2 条）。
- 每条标注：纯猜测 / 重用假设 / 开放问题 三种之一；所有「重用假设」声明未获资产。
- 想法 17（拒绝边界扰动厚度）+ 想法 21（信息论基线指纹）被自我评为"最靠近可操作"。
- 想法 8（元认知可蒸馏性边界）+ 想法 6（非单调脆弱性）被自我评为"最具理论深度"。
- 想法 14（蒸馏尽职调查）+ 想法 11（条款可执行边界）被自我评为"最被产业忽视"。
- 想法 23（版本控制问题）被自我评为"最与邀请函自身张力相关"。

### §4.10 codex（D1 review，落盘 `48387412B109`，PI 拍板 P3）

`results/_v4_d1_review_codex_2026_09_20.md`（`48387412B109`；与附件 778 同字节，落盘动作见 §6.5.1）：

- 状态自陈 "incomplete for execution" — D1 不能 assign PASS/FAIL/PARTIAL/GRAY。
- Track 1 三项批评：
  1. "Intersection of high-density regions" 不可复现（density estimator、bandwidth、smoothing rule、geometric reference measure、mode-matching rule、minimum support 未定）。
  2. development / evaluation boundary 未定。
  3. mode count ≤2 或 one per cell 需 unique stability + uncertainty。
- Track 2 三项批评：
  1. attribution target 不可识别。
  2. symmetric KL 不能直接用于 embedding vectors。
  3. 需加入 majority-prior、raw-embedding nearest-source baselines、dependency-preserving label permutations、balanced accuracy、confusion、abstention coverage、group-level uncertainty。
- Track 3 建议：black-box extractor threat model；utility / resistance / cost 三轴；PASS/PARTIAL/FAIL/GRAY 四档。**codex 自陈 "This is a proposal, not a commitment or a request to modify frozen inputs."**
- Cross-discipline seed list：information theory（retained information about source identity vs. retained task utility）；geometry（mode stability under Poincaré distance，no new embedding protocol）；measurement theory（observer-effect frame existing）。
- D1 action items：confirm frozen inventory；register Track 1 specification；choose one Track 2 candidate type；verify SHA-12 placeholders against V3 final R5 manifest；PI approve Track 3 proposal before D3。

### §4.11 codex（brainstorm，14 条，落盘 `0FF6C042B845`，PI 拍板 P3）

`results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md`（`0FF6C042B845`；与附件 782 同字节，落盘动作见 §6.5.1）：

- 14 条 ideas（详见原文）：涵盖 serialization as information bottleneck / generation-process side channels / formatting invariants / empty response as false signature / missingness / disturbance convergence / geometry resemblance / hash vs behavioral vs causal identity / selective disclosure / query-budget economics / watermark survivability / mixture ancestry / signature half-life / naming drift。
- 每条标注 re-fit hypothesis 或 pure speculation 或 on-disk ambiguity。
- "I would add this open question to section 4: **Which different learning histories remain observationally indistinguishable after the stack's surviving records are fixed?**"

### §4.12 GLM（PI 拍板 2026-09-21 唯一归属；磁盘署名 `an invited reader team (multi-agent)`，如实并存）— 主件，756

`assets/11-12-20-756-asset...C78CFB42E33D`：

- 见 §1.3 / §1.6 / §2.4 / §2.7 / §2.10 等横切批评。
- §3.1–§3.7 种子逐条 engagement 见 §3 各子节。
- Closing(a)–(d) 见 §5。
- **`v1.1 注`（PI 拍板 P2）**：磁盘署名仍为 `an invited reader team (multi-agent)`，本稿不改写磁盘原文；本节标题改为 `GLM`，如实并存记录法见 §0.6 / §6.1。

### §4.13 GLM（PI 拍板 2026-09-21 唯一归属；磁盘署名 `an invited reader team (multi-agent)`，如实并存）— addendum，761

`assets/11-12-20-761-asset...8295C3201F20`：

- 11 条 ideas（详见原文）：Impostor-calibrated attribution / The convergence squeeze / Negative controls / Known-dose controls / Time-gated shared errors / Format-conditioned false positives / Difficulty-band shape / Frozen decoding zero / Non-stationary decision lines / Birthmarks not watermarks / Ambient contamination / Transportability of attribution claims。
- 每条标注 pure speculation / re-fit hypothesis / on-disk fact 三类之一。
- Closing (a) 两条新方向：null-and-controls program + measured false-positive structure。
- Closing (b) "**claim form — and its unit (output, datum, artifact byte, population) — before a common-cause explanation is excluded, is any detection claim confined to the 'deviation from a reference set' form rather than 'origin', and what evidence would ever license the stronger form?**"
- **`v1.1 注`（PI 拍板 P2）**：同上。

### §4.14 GLM（查理 / 5-agent 团队）— 实验邀请函审查件（新增本轮，PI 拍板 P1）

`C:\Users\Administrator\.minimax\v2\assets\2026\09\20\15-30-44-659-asset_20260920-153044-659_ac74a04efeb2_0a7da13e-查理_V4接受回执与D1首轮反馈_2026-09-20.md`：

- **对象**：`results/_v4_experiment_invitation_2026_09_20.md`（SHA-12 `4E8C0EA57028`，实验邀请函 draft v0.1，**非**蒸馏邀请函）。本件不并入 §1 / §2 / §3 / §4 / §5 对蒸馏邀请函的既有论述（独立呈现，不参与 §1 横切批评计数）。
- **署名与通道**：磁盘署名「GLM 接收侧 paper-track 审查」（PI 拍板 P1：「两份都在附件中，agentmore 模式，5-agent 团队，所以标注为查理」）；5-agent 团队分别为爱丽丝 / 鲍勃 / 阿兰 / … / 查理（执笔合并）。
- **三方首轮审查整合**：
  - 爱丽丝（方法学）：11 条。具体由该件内部段落给出。
  - 鲍勃（可执行性）：12 条。
  - 阿兰（文献定位）：6 条。
  - 查理（执笔合并）：对上述 29 条 issue 分类为 7 组阻塞级问题 + 7 条非阻塞建议。
- **接受条件**：须修订至 v0.2（即：实验邀请函 draft v0.1 不被接受，须经 v0.2 修订后回归验收）。
- **提请 PI 澄清 5 项**：见该件原文（v1.1 不复制粘贴，仅标注"见附件原文"）。
- **`v1.1 注`**：本件回应对象是实验邀请函（4E8C0EA57028）而非蒸馏邀请函（3D9F73519F6C）；PI 拍板 P1 补入；与 §4.12 / §4.13 的 5-agent 团队关联尚不明确——按 P1 字面二者都是 "agentmore 模式 / 5-agent 团队"，但查理件 P1 标注明确，756 / 761 件 PI 拍板 P2 给的归属是 GLM。查理件是否同样归属 GLM，**未在 P2 给明文**——v1.1 不擅自归并，按磁盘署名 "GLM 接收侧 paper-track 审查" 原样保留，列在 §0.4 锚表，§4.14 独立呈现；与 §4.12 / §4.13 的 GLM 归属为两个独立事实陈述。

---

## §5 各方对收尾问题的回答汇总

本节并列各参与方对 prompt pack §6 closing 四问的回答（(a) 最值得追 / (b) 最不具生产性 / (c) 邀请函缺失的种子 / (d) 建议新增的开放问题）。**不裁决**；保留各方用语与原文要点。

### §5.1 (a) 最值得追的种子

| 参与方 | 答案 | 关键理由（原文短引） | 来源 |
|---|---|---|---|
| Mavis v1.2 | S-15 输出统计异常 | "black-box entry point ... does not require any extension to deposon's existing assets" | `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:188` |
| Mavis v1.2 runner-up | S-36 | "S-36 is my close runner-up" | `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:188` |
| trae work v1.2 | S-36 | "the stack does not merely lack a distillation label — it contains a documented instance of ground truth being *swapped* for a claim" (`063AC8D00542:369–377`) | `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:139` |
| trae code | S-36 | "ground-truth-by-construction is the only route ... that does not immediately fall into the two traps this stack has already documented" (formatting-leak + instrument-fragility) | `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:79` |
| kimi 主件 | S-36 | "GLM_1 的 0.6146 已把困难量化在盘上" (`268AB1239A8A:640`) | `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:43` |
| workbuddy 主件 | S-17 | "40 条里唯一一条盘上已存在量好、预登记、带实测误差结构的仪器的种子 — `GLM_1` 那份 SP_t=1.0 / FNR=0 / FPR=4.4% / 抗洗白 95.6%" | `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:158` |
| workbuddy part2 | S-38 | "40 条里唯一一条盘上已经发作过、并且留下了根因的问题" (DELTA 1.30 → 1.05) | `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:128` |
| workbuddy brainstorm | M-1 + 透镜④第 30 条 | "FNR=0 / FPR=4.4% 的不对称不是缺陷，是这台仪器的性格" | `results/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md:CDB27CD3008C:94` |
| claude code | S-17（带 §5.7 修正） | "the only seed in the field whose required experimental shape already exists on disk ... 但 `overall_verdict: FAIL`" | `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:176, 298–317` |
| coze | S-36 | "唯一一个能同时吃掉'资产层'与'样本层'两级 GT 的种子，而且盘上已经给出了一个真实的反例" | `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:457` |
| 豆包工作 主件 | S-36 | "所有涉及'检测'方向的种子的前置条件" | `assets/11-12-20-747-asset...19C97B5CFF3C:71` |
| 豆包工作 brainstorm | 想法 17 + 想法 21 | "两者都直接指向已有 V2/V1 资产的再利用" | `assets/11-12-20-766-asset...A18E58C8E2A3:123` |
| codex（D1 review，落盘见 §4.10） | 未给 (a)（自陈 incomplete for execution） | — | `results/_v4_d1_review_codex_2026_09_20.md:48387412B109:9` |
| codex brainstorm（落盘见 §4.11） | S-03 + S-36 | "what historical claims survive when full responses become extracted answers and then aggregate counts" | `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md:0FF6C042B845:38` |
| GLM 主件 (PI 拍板 P2 已归属 GLM) | S-36 / S-17 / S-37 瓶颈分散 | "three faces of one question ... our three analysts each picked one face; we read that as convergence" | `assets/11-12-20-756-asset...C78CFB42E33D:87` |
| GLM addendum (PI 拍板 P2 已归属 GLM) | null-and-controls + measured false-positive structure | "supplying the three pieces our v1.0 Closing said the common-cause separability candidate lacks" | `assets/11-12-20-761-asset...8295C3201F20:89` |

### §5.2 (b) 最不具生产性的种子

| 参与方 | 答案 | 关键理由（原文短引） | 来源 |
|---|---|---|---|
| Mavis v1.2 | S-32 no-cloning | "其结论已由范畴论已知 ... teacher is function, not quantum state" | `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:188` |
| trae work v1.2 | S-29 | "its object is a five-year cost-benefit trajectory, and the only cost figure on disk is a 0.002-second detector runtime" | `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:139` |
| trae code | S-14 | "the invitation itself records that no training-curve artifact exists ... the student's training curve is unobservable — the seed's interestingness is real, but its observability on this stack is zero" | `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:79` |
| kimi 主件 | S-14 | "无训练曲线工件且范畴错位；S-01 权重级离盘最远，次之" | `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:43` |
| workbuddy 主件 | S-02 / S-30 | "P-G v01 实测是 `pure numpy Poincare ball (c=1)` 的数值模拟，0 LLM、0 API" | `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:160` |
| workbuddy part2 | S-10 | "支撑它的那条索引描述我核实不到：在 V7 报告里按 `扰动/干扰/攻击/perturb/attack` 检索" | `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:130` |
| workbuddy brainstorm | no-cloning + "蒸馏容量标度律" | "前者已被该透镜自己论证为假朋友，后者依赖一个尚无任何盘上支撑的普适类假设" | `results/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md:CDB27CD3008C:96` |
| claude code | S-06 | "its 'related asset' line is a discrimination pass-rate over a 60-cell layout that measures nothing about refusal ... a false affordance" | `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:176` |
| coze | S-28 + S-29 | "它们要求的观测量是跨期的，而这套栈是单期冻结的" | `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:457` |
| 豆包工作 主件 | Dimension 6（S-30 至 S-35）整体 | "全部均为纯猜测层级，无 on-disk 锚点；S-31 的 'behated' 笔误进一步降低了该维度整体的可信度" | `assets/11-12-20-747-asset...19C97B5CFF3C:75` |
| 豆包工作 brainstorm | 想法 14 + 想法 11（least tractable） | "正在形成的真实需求缺口，几乎无公开讨论"（隐含 low 优先级） | `assets/11-12-20-766-asset...A18E58C8E2A3:125` |
| codex brainstorm（落盘见 §4.11） | S-32 | "an unrestricted digital 'no-cloning' analogy ignores copying of accessible weights and code" | `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md:0FF6C042B845:38` |
| GLM 主件 (PI 拍板 P2 已归属 GLM) | S-32 | "two analysts independently found the analogy fails at the mechanism level" | `assets/11-12-20-756-asset...C78CFB42E33D:87` |
| GLM addendum | — | — | — |

### §5.3 (c) 邀请函缺失但应包含的种子

| 参与方 | 答案 | 关键理由 | 来源 |
|---|---|---|---|
| Mavis v1.2 | "the smallest deposon-side extension that would lift the theme from re-fit to calibrated" | 40 条都假设了学生存在但没有追问来源 | `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:194` |
| trae work v1.2 | N-08 "counting independent measurements" | "the single most repeated error in this stack is treating a rank-identical pair as two pieces of evidence — `spearman_rho_H_vs_E: 1.0` is one measure counted twice — and no seed asks the reader to count" | `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:139` |
| trae code | "falsification-cost seed" | "what would it take for the deposon community to *retract* a distillation-detection claim, and who has the standing to do it — because the V3 record shows this program kills its own hypotheses readily" | `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:176` |
| trae code | "measurement-instrument stability" | "how much of a measured behavioral difference between models is attributable to the detector/scorer rather than the models? Dimension 7 covers ground truth and recursion but not instrument calibration" | `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:79` |
| kimi 主件 | "同输入跨厂商输出对比作为行为基线，今天能建成什么样" | 介于 S-03 与 S-07 之间 | `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:43` |
| workbuddy 主件 | "若盘上不存在任何学生侧对象，那么关于蒸馏的任何一个可证伪命题，其证伪所需的对照物来自哪里？" | 40 条全部预设了学生存在 | `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:162` |
| workbuddy part2 | "同一批数据被问两次" | DELTA 1.30 → 1.05 揭示"一个已被写进整合口径的读数后来被证明不稳健，而撤销它的动作留下了痕迹，复核它的机制没有" | `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:132` |
| workbuddy brainstorm | "单侧失效" | "盘上三次失败全是单侧的" (归因仪 FNR/FPR、DELTA f3/独立复算、语法擦除 vs 语义擦除) | `results/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md:CDB27CD3008C:98` |
| claude code | "falsification-cost seed"（同 trae code） | 同上 | `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:176` |
| coze | "资产可用性标注" + "派生列的可复算性" | "_v4_brainstorm_seeds_2026_09_20.md:292" 自述 + "063AC8D00542:121–129" | `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:457` |
| coze | N-01 ~ N-08 八条候选 | 详见 §4.7 | `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:299–395` |
| 豆包工作 主件 | "教师合成数据蒸馏" | "当前 LLM 工业实践中最主流的蒸馏机制" — 在 S-01–S-06 框架之外 | `assets/11-12-20-747-asset...19C97B5CFF3C:79` |
| codex brainstorm | "in-context imitation vs parameter transfer" 显式分离 | seed field 当前未区分 | `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md:0FF6C042B845:38` |
| GLM 主件 (PI 拍板 P2 已归属 GLM) | "common-cause vs. direct-cause separability" | 三种材料 triangulate：S-35 reduction + S-18 null-model gap + GLM_1 attribution structure | `assets/11-12-20-756-asset...C78CFB42E33D:87` |
| GLM addendum (PI 拍板 P2 已归属 GLM) | "claim form — and its unit (output, datum, artifact byte, population) — before a common-cause explanation is excluded" | — | `assets/11-12-20-761-asset...8295C3201F20:89` |

### §5.4 (d) 建议新增的开放问题

| 参与方 | 答案 | 关键理由 | 来源 |
|---|---|---|---|
| Mavis v1.2 | "Is the V1–V3 asset stack large enough to support a theme that, by construction, requires both teacher-side and student-side samples?" | 栈是 teacher-side only | `results/_v4_theme_reply_mavis_2026_09_20_v1.2.md:3ECF5B38048E:196` |
| trae work v1.2 | "For every cross-vendor statistic in this stack, how many independent sides does the denominator actually contain — and which on-disk artifact states that number?" | — | `results/_v4_theme_reply_trae_work_2026_09_20_v1.2.md:6BEE6EC434BD:139` |
| trae code | "what is the chance-level attribution rate for the existing five-artifact panel ... is the recorded 4.4% FPR distinguishable from it?" | null-model | `results/_v4_distillation_reply_trae_code_2026_09_20.md:E87EC8F7E2FE:79` |
| kimi 主件 | "哪些盘上工件真的含模型输出原文，哪些只有哈希或判别值？" | §8 表只列字节与哈希 | `results/_kimi_v4_theme_reply_2026_09_20.md:3E37352EFB4B:45` |
| workbuddy 主件 | "这个主题是否需要放宽 `no_llm / no_proxy / no_gateway` 铁律？" | 主题结构性卡在铁律 | `results/_v4_distillation_theme_reply_workbuddy_2026_09_20.md:E3FE63A2F708:164` |
| workbuddy part2 | "V4 若要基于 V1–V3 资产作任何主张，是否需要先声明一条'已被坐实不稳健的读数不得作为下游前提'的自律，以及由谁来执行？" | DELTA 1.30 → 1.05 已发生 | `results/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md:BFB4932F4467:134` |
| workbuddy brainstorm | "盘上已有三处单侧失效 ... 这三次是同一个结构，还是三次独立的事故？若是同一个结构，那么 V4 的任何主张是否都应当以'一对数'而非'一个数'的形式给出？" | — | `results/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md:CDB27CD3008C:100` |
| claude code | "which of the assets cited in §8 are expected to still be re-derivable by an outside reader in twelve months, and what happens to a claim whose anchor has moved" | `deposon_v20_baselines.json` 已 in that condition today | `results/_v4_distillation_reply_claude_code_2026_09_20.md:D39CB17B051B:176` |
| coze | "*V1–V3 网格内部是否存在互为严格单调变换、或互为同一构造恒等式两种写法的统计量，使得'多处一致'成为保序伪影而非独立证据？*" | "A ≡ 30 − T − R" 守恒；`-0.81` vs `-0.92` 双编码 | `results/_v4_distillation_reply_coze_2026_09_20.md:00593014CBD3:457` |
| 豆包工作 主件 | "V1–V3 资产的采集时间窗口是否足以捕捉蒸馏效应的时间维度？" | 单时点快照的适用边界 | `assets/11-12-20-747-asset...19C97B5CFF3C:83` |
| codex brainstorm（落盘见 §4.11） | "Which different learning histories remain observationally indistinguishable after the stack's surviving records are fixed?" | — | `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md:0FF6C042B845:38` |
| GLM 主件 (PI 拍板 P2 已归属 GLM) | "the referent of 'output-distribution baseline' — four of five `by_model/` slots store in-repo artifact hashes or indices rather than model-output text" | gates reading of §2.1 for S-03/S-07/S-15/S-17 | `assets/11-12-20-756-asset...C78CFB42E33D:87` |
| GLM addendum (PI 拍板 P2 已归属 GLM) | "claim form — and its unit (output, datum, artifact byte, population) — before a common-cause explanation is excluded" | — | `assets/11-12-20-761-asset...8295C3201F20:89` |

---

## §6 归属未定与未复现项 + 第二轮复算结论

### §6.1 归属未定（已拍板）

PI 拍板 P2（2026-09-21）：756 / 761 唯一归属为 **GLM**。磁盘署名原文如 §0.6 / §4.12 / §4.13 各保留。两件在盘上 L3 自陈 `From: an invited reader team (multi-agent)` 为**磁盘原文事实陈述**（v1.1 不删除），与"唯一归属 GLM"并存记录。

747 / 766 维持**豆包工作**归属（PI 拍板 P2：「747 / 766 为豆包工作」）。747 / 766 不作厂商重新归并；P2 的次轮 Q1 中 PI 选「唯一归属 = GLM」是针对 756 / 761 的明确表述，不延伸到 747 / 766。

GLM 查理件（ac74a04efeb2）按 PI 拍板 P1 归 GLM；与 756 / 761 的关联见 §4.14 注。

### §6.2 各行数冲突（已定案，PI 拍板 P6）

PI 拍板 P6（2026-09-21）：本稿 / 问卷 / 所有 `.md` 行数一律以 **`[System.IO.File]::ReadAllLines(path, [System.Text.Encoding]::UTF8).Length`** 为 canonical。早前 `Get-Content -Path ... -TotalCount` 不指定 `-Encoding` 所得 636 / 277 行数作废（不指定编码时 PowerShell 5.1 走 ANSI 解码 → 中文字符按双字节切分，行数被异常放大或缩小）。

本轮（v1.1）实测：

- `_v4_design_integration_2026_09_21_v1.0.md` 本轮 = 1,041 行 ReadAllLines UTF8 / 119,732 B / SHA-12 `4B10CDE29C27`（与 §0 / PI 派工单一致）。
- `_v4_pi_decision_questionnaire_2026_09_21_v1.0.md` 本轮 = 587 行 ReadAllLines UTF8 / 67,686 B / SHA-12 `6A3A2D8EE357`（与 §0 / PI 派工单一致）。
- 已作废口径：与 `Get-Content` 不带 `-Encoding` 所得的 636 / 277 等编码误读值（历史在不同 round 的会话内出现过），**全部作废**。

### §6.3 任何我无法核到的引用

本稿引用全部以 `path:SHA-12:line` 给出。所有 line 字段均由本会话内 `[System.IO.File]::ReadAllLines(path, [System.Text.Encoding]::UTF8)[line-1]` 实读确认。

**未在本稿引用的 PI 派工单第 2.3 节提到的文件名**：

- 派工单 §2.3 列出的 `773` 附件与 results/ 下 coze 文件 SHA-12 / 字节数一致；本稿按派工单指引不重复计。

**本稿尝试引用但本会话内未实际读毕 / 不能 quoted 的文件**：

- 附件侧 `747` / `766` 读到 line 83 / 130（与 v1.0 一致）。附件 `756` 读到 line 89 末；附件 `761` 读到 line 91 末。
- 落盘 codex 两件 `48387412B109` 读到 line 46、`0FF6C042B845` 读到 line 39（与附件同字节）。
- GLM 查理件 `ac74a04efeb2` 仅读摘要要点，未逐行重核，按 §0.4 摘要呈现，详细原文由 PI 后续裁定是否独立重读。

### §6.4 与 §1.8 / §2.10 相关的"五档"事实清单

§1.8 / §2.10 记录"邀请函 §0.2 L26 的'V1–V3 has zero distillation, reverse-distillation, or anti-distillation experiments on disk' 与盘上 KT-B1 知识蒸馏基线相冲突"。本稿**不裁决**该冲突；只把两边的实证据并列：

- **邀请函 §0.2 L26 自承**：`results/_v4_distillation_invitation_2026_09_20_v1.0.md:3D9F73519F6C:26` "V1–V3 has zero distillation, reverse-distillation, or anti-distillation experiments on disk."
- **邀请函 §2.10 L120 自承**：`3D9F73519F6C:120` "No V1–V3 distillation, reverse-distillation, or anti-distillation experiment asset exists on disk."
- **盘上 KT-B1 KD baseline**：
    - `docs/V3X/KT_B1_SPEC_V0.1.md:0410CA0FBDAE:267–274` BOSS-B2: Knowledge Distillation 测法（Hinton 2015 KD 框架 + KL 散度 + softmax 平滑，200 节点 baseline）。
    - `verifier/handoff/KT_ABC1_anchors_sha256_12.json:03C6C01F3697:157–161` 同一脚本路径与 hash 注册在 trust anchor。
    - `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md:4485443757e7:33` 第一次跑 `FAIL (bug)`，`_extract_200_questions TypeError`。
    - `docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md:9352a1675b10:44–46` 字段名修复后仍 `string 'No' 转浮点失败`。
    - `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md:BAEF94E393DE:78–86` 三项修复后跑通；KD 项失真量 **0.0028**，deposon 一侧 0.5（占位值）；裁定 `GRAY_BOTH_BELOW`。
    - `BAEF94E393DE:179` 留遗事项："三项裁定全落中性档，因为 deposon 的失真量是占位值（0.5/0.05），**不标榜差异化**"。

**本稿保留 §1.8 / §2.10 的双向记录，由 PI 裁定**。

### §6.5 第二轮复算结论（2026-09-21，worker 实测）

本节为 v1.1 **新增**节段；按 PI 拍板 P4（全部派 worker 复算）由 worker 在本会话内执行三组复算；本节按组列出复算结论与每条三选一标签（on-disk fact / no on-disk artifact / unreproducible）。本节内所有 SHA-12 / 字节 / 行数均为 worker 在本会话内实测（PowerShell .NET SHA256 + `ReadAllLines` UTF8）。

#### §6.5.1 组 A：codex 两件落盘字节级复制

worker 实测：

- `results/_v4_d1_review_codex_2026_09_20.md`（`48387412B109`，4,506 B，46 行）字节级复制等于附件 `778-asset_..._48387412b109_...md`（4,506 B，46 行）。
- `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md`（`0FF6C042B845`，9,048 B，39 行）字节级复制等于附件 `782-asset_..._0ff6c042b845_...md`（9,048 B，39 行）。

**PowerShell .NET SHA256 + Python `hashlib.sha256`** 双算一致（identical）。该 worker 在仓库根目录留了 6 个脚手架文件（`_worker_drop_c2a1.ps1` 等），已如实上报，PI 尚未裁定是否清理——整合稿 v1.1 不引用这些脚手架。**标签：on-disk fact。**

#### §6.5.2 组 B：邀请函 §8 表 8 个 `(see SHA-12)` 占位回盘 + 8 行占位补全表

worker 实测（`Get-FileHash` + 全 `results/` 递归扫描，排除 `_archive_2026_09_20` 的 138 文件，命中 0 失败）：

- **关键事实**：这 7 个 SHA-12 串**均不出现在邀请函正文内**（`ripgrep` + PowerShell 双通道大小写不敏感 0 命中）；§8 表 L394–L401 共 8 行写的是 `(see SHA-12)` 占位符。7 个串是会话内 PI 提供的文件外宣称对应关系。
- **7 个 SHA-12 在 `results/` 实测命中**：

| SHA-12 | 文件名 | 字节 | 行 |
|---|---|---|---|
| `8E1E7434905D` | `_v4_experiment_invitation_2026_09_20_v0.2.md` | 41,680 | 470 |
| `38070FD12F31` | `_kimi_v4_t12_review_2026_09_20.md` | 6,644 | 80 |
| `B2BF2A073AC8` | `_v4_acceptance_coze_2026_09_20.md` | 5,467 | 70 |
| `3205593030BC` | `_v4_acceptance_trae_code_2026_09_20.md` | 6,301 | 86 |
| `D3BDFC99FCDC` | `_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | 11,877 | 102 |
| `BC663B671994` | `_v4_d1_response_workbuddy_2026_09_20.md` | 14,881 | 158 |
| `B6F9956BCF5C` | `_v4_review_claude_code_2026_09_20.md` | 7,004 | 55 |

- **第 8 行**（L394）`_v4_brainstorm_seeds_2026_09_20.md` 不在 PI 给的 7 个之列；该文件实测 `0EB1CFAA2992` / 14,994 B / 294 行（本会话 worker 实测，确认与 §0.1 一致）。

邀请函 §8 表 L394–L401 共 8 行 + 文件名 + 实测 SHA-12 完整补全表（PI 给的 7 SHA-12 全部命中；第 8 行由 worker 独立补 SHA-12）：

| 行号 | 文件名 | PI 给定 SHA-12 | 实测 SHA-12 |
|---|---|---|---|
| L394 | `_v4_brainstorm_seeds_2026_09_20.md` | （未给出；非 PI 7 串） | `0EB1CFAA2992` |
| L395 | `_v4_experiment_invitation_2026_09_20_v0.2.md` | `8E1E7434905D` | `8E1E7434905D`（命中） |
| L396 | `_kimi_v4_t12_review_2026_09_20.md` | `38070FD12F31` | `38070FD12F31`（命中） |
| L397 | `_v4_acceptance_coze_2026_09_20.md` | `B2BF2A073AC8` | `B2BF2A073AC8`（命中） |
| L398 | `_v4_acceptance_trae_code_2026_09_20.md` | `3205593030BC` | `3205593030BC`（命中） |
| L399 | `_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | `D3BDFC99FCDC` | `D3BDFC99FCDC`（命中） |
| L400 | `_v4_d1_response_workbuddy_2026_09_20.md` | `BC663B671994` | `BC663B671994`（命中） |
| L401 | `_v4_review_claude_code_2026_09_20.md` | `B6F9956BCF5C` | `B6F9956BCF5C`（命中） |

**标签：on-disk fact**（8 行文件全部命中 SHA-12；邀请函正文实为 `(see SHA-12)` 占位符、PI 7 串是文件外宣称）。

#### §6.5.3 组 C：5 项旧矛盾 + KT_B1 口径冲突回盘（C1–C8，每条带路径:SHA-12:行号与三选一标签）

每条三选一标签：**on-disk fact** / **no on-disk artifact** / **unreproducible**。

| 编号 | 议题 | 锚 + 实测 | 标签 |
|---|---|---|---|
| C1 | KT 锚文件条数 | 锚文件 `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（`03C6C01F3697`，6,680 B / 189 行，实测）。**顶层 15 条**（KT-A1 L14–L56、KT-B1 L57–L93、KT-C1 L94–L130，各 5 条）；distinct value **16 个**；coze 回函 (`00593014CBD3:65`) 自报 "13 条 distinct" 漏数了 `P_A_FROZEN_RUNS` 数组 (`03C6C01F3697:34–38`) 里 3 个独有元素（`6edb2aec1660` / `62c1a41e1db8` / `af51da229652`）。 | on-disk fact（coze 13-vs-16 属口径分歧） |
| C2 | BOSS 家族三对同字节 | boss_pc_1 / boss_pe_1_real_2d_ising (`43D9CE160FC8`, 2,460 B, 99 行)；boss_pc_2 / boss_pe_2_real_transverse_ising (`8933D61B180A`, 3,553 B, 136 行)；boss_pc_3 / boss_pe_3_real_reservoir (`94B5398BE76C`, 2,364 B, 96 行)；6 件内容的 boss_id 字段全为 BOSS-PE-1/2/3（`pc_` 前缀文件名与内容不符）。 | on-disk fact |
| C3 | D_fix2 | 制品 `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json`（`9F88A212A77C`, 204,441 B / 6,722 行，实测）+ 日志（仅 `_archive_2026_09_20` 在盘）存在；`docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` L20 / L91–L92 声明的 `results/.tmp/_verify_d_fix2_metric_9m60c_2026_09_15.py` + `_postproc_d_fix2_metric_9m60c_2026_09_15.py` **均不在盘**（`.tmp/` 目录不存在）。数学部分（cos 相似度公式）确定性可复算，完整制品不可复算。 | unreproducible |
| C4 | V7 summary 派生列 | `results/deposon_v3_v7_summary_2026_09_11.json`（`063AC8D00542`，25,049 B / 380 行，实测）L121–129 九行含 `distance_to_ideal_1_0_0` 与 `rank` 列具体值（rank1 doubao-seed-2.0-lite distance 0.1800、rank1 glm-5.3 0.1700、rank9 deepseek-v4-pro 0.6182；L150 mean 0.3611；L151 range [0.1700, 0.6182]）；T / R / A 与 `frac` 列可与源制品静态对照，但 `distance` 与 `rank` 两列公式未声明（无 formula / metric 键）、生成脚本不在盘、Euclidean 反推多行不严格成立（rank1 重算 0.188 vs 记录 0.180）。 | unreproducible |
| C5 | `deposon_v20_baselines.json` (`6edb2aec1660`) | `results/` 全目录（475 文件）+ 整库递归 0 命中；`results/` 下 v20 系仅有 `deposon_v20_gt2b.json` (`A2AE7997EE67`, 123,331 B，500 行，实测 / SHA-12 不符)。锚文件 `03C6C01F3697:31` 声明路径 "results/deposon_v20_baselines.json + v19 + v21 + v18 + v17"；`03C6C01F3697:34` value `6edb2aec1660`。同锚文件内 v19 (`910c4333eead`)、v21 (`9d9ae5001c57`)、`P_A_KILL_LINE` (`bd1caab42b4c`)、`KT_B1_KILL_LINE` (`9f351078e5bf`) 四处实测匹配。 | no on-disk artifact |
| C6 | KT_B1 口径冲突 | **非实质冲突**。`docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` (`BAEF94E393DE`, 11,478 B / 215 行，实测) L83 同一行同时含 `| B2 KD | 0.0028 | 0.5(占位) | GRAY_BOTH_BELOW | <1 min |` 三属性；coze (`00593014CBD3:420`) 取数字层，VS / claude (`D39CB17B051B:375, 377`) 取裁定层，同源同值。`BAEF94E393DE:86` / `BAEF94E393DE:179` 解释 GRAY 来自 deposon 占位值。 | on-disk fact |
| C7 | 同一锚文件内**声明值与实测不一致**（C1 附带新发现，原任务外） | `P_A_LLM_CLIENT` 声明 `tools/llm_client.py` = `055e874ea5c1`；实测 = `1722500DA4AA`。`P_A_HARNESS` 声明 `tools/exp_harness.py` = `9f383935c00c`；实测 = `275E480BA4D9`。frozen_runs 的 `62c1a41e1db8`（v18）与 `af51da229652`（v17）未找到。如实记录，不做裁定。 | on-disk fact（声明值与实测不一致这一事实本身） |
| C8 | §2.2 vs §8 表字节标定不一致 | §2.2 L66 (邀 8,674) vs §8 L383 (邀 8,753) vs 磁盘 8,753——与 v1.0 整合稿 §1.1 相关，保持原有记录即可，不新增裁定。 | （沿用 §1.1：on-disk fact） |

#### §6.5.4 组 C 综述

- 8 条中 **on-disk fact**：C1 / C2 / C6 / C7 / C8 共 5 条。
- **no on-disk artifact**：C5 共 1 条（`deposon_v20_baselines.json`）。
- **unreproducible**：C3 / C4 共 2 条（数学可复算 / 派生列公式缺失）。

本节为 v1.1 **新增**复算汇总；v1.0 §6.4 仅保留 KT-B1 一项，本轮扩展到 8 条（其中 C7 / C8 为 §6.5.3 内附带新发现，标注「如实记录，不做裁定」）。

---

## §7 引用索引（全部被引用 path + SHA-12 + 行号，按文件分组）

> 本索引列本文被引用过的全部文件路径、SHA-12 与代表行号。每行的 "代表行"是该文件在本稿中被引用的关键行（不唯一）。完整引用见 §1–§6 各小节。

### §7.1 邀请侧与种子文件（results/）

- `_v4_distillation_invitation_2026_09_20_v1.0.md` — `3D9F73519F6C` — 411 行 — 53,539 B
  - 代表引用：L26 / L66 / L83 / L96 / L120–125 / L218 / L383 / L394–401 (组 B 8 行占位补全) 等
- `_v4_distillation_prompt_pack_2026_09_20_v1.0.md` — `E5C37E90255B` — 384 行 — 25,371 B
  - 代表引用：L184 / L292 等
- `_v4_brainstorm_seeds_2026_09_20.md` — `0EB1CFAA2992` — 294 行 — 14,994 B
  - 代表引用：L9, 15, 21, 27, 33, 39, 49, 55, 61, 67, 73, 79, 89, 95, 101, 107, 113, 119, 129, 135, 141, 147, 153, 159, 169, 175, 181, 187, 193, 205, 211, 217, 223, 229, 235, 245, 251, 257, 263, 269, 292
  - v1.1 worker 复算确认 SHA-12 / 字节 / 行与 §0.1 一致（见 §6.5.2 第 8 行）
- `_v4_experiment_invitation_2026_09_20.md` — `4E8C0EA57028` — 436 行 — 30,820 B
  - §0.1 出现一次 + §4.14（实验邀请函审查件对象）
- `_v4_experiment_invitation_2026_09_20_v0.2.md` — `8E1E7434905D` — 470 行 — 41,680 B
  - §6.5.2 第 8 行（PI 7 串之一 / 第 2 行）
- `_kimi_v4_t12_review_2026_09_20.md` — `38070FD12F31` — 80 行 — 6,644 B
  - §6.5.2 第 3 行
- `_v4_acceptance_coze_2026_09_20.md` — `B2BF2A073AC8` — 70 行 — 5,467 B
  - §6.5.2 第 4 行
- `_v4_acceptance_trae_code_2026_09_20.md` — `3205593030BC` — 86 行 — 6,301 B
  - §6.5.2 第 5 行
- `_v4_ide_track_review_trae_code_supplement_2026_09_20.md` — `D3BDFC99FCDC` — 102 行 — 11,877 B
  - §6.5.2 第 6 行
- `_v4_d1_response_workbuddy_2026_09_20.md` — `BC663B671994` — 158 行 — 14,881 B
  - §6.5.2 第 7 行
- `_v4_review_claude_code_2026_09_20.md` — `B6F9956BCF5C` — 55 行 — 7,004 B
  - §6.5.2 第 8 行（PI 7 串最后一行）

### §7.2 回函侧（results/）

- `_v4_theme_reply_mavis_2026_09_20_v1.2.md` — `3ECF5B38048E` — 213 行 — 36,826 B
  - 代表引用：L3, L44, L46, L54–64 (S-03), L66 (S-06), L80 (S-08), L88 (S-09), L102–108 (S-11), L110–114 (S-14), L116 (S-15), L122–126 (S-17), L128–132 (S-18), L134–138 (S-19), L140–144 (S-20), L146–150 (S-26), L154 (S-30), L158 (S-31 typo), L164 (S-36), L168–172 (S-37), L180–182 (S-40), L188 (closing a/b), L194 (closing c), L196 (closing d), L209
- `_v4_theme_reply_mavis_2026_09_20_v1.1.md` — `82FEE0A18DAB` — 213 行 — 36,824 B
  - 仅 §0.5 / §0.2 出现（用于记录行数差异）
- `_v4_theme_reply_trae_work_2026_09_20_v1.2.md` — `6BEE6EC434BD` — 141 行 — 28,395 B
  - 代表引用：L6, L10, L16, L22, L24, L25, L27, L35 (S-01), L37 (S-02), L39 (S-03), L41 (S-04), L43 (S-05), L45 (S-06), L49 (S-07), L51 (S-08), L53 (S-09), L55 (S-10), L57 (S-11), L59 (S-12), L63 (S-13), L65 (S-14), L67 (S-15), L69 (S-16), L71 (S-17), L73 (S-18), L77 (S-19), L79 (S-20), L81 (S-21), L83 (S-22), L85 (S-23), L87 (S-24), L91 (S-25), L93 (S-26), L95 (S-27), L99 (S-29), L103 (S-30), L105 (S-31), L107 (S-32), L109 (S-33), L111 (S-34), L113 (S-35), L123 (S-39), L125 (S-40), L129–135 (N-01~N-09), L139 (closing)
- `_v4_distillation_reply_trae_code_2026_09_20.md` — `E87EC8F7E2FE` — 187 行 — 43,570 B
  - 代表引用：L9, L18, L19, L29–36 (S-07), L41–46 (S-17), L57–61 (S-10), L65–69, L71–76 (S-37), L79 (closing), L81–129 (Addendum I A–E), L139–185 (Addendum II D-1~D-8 + X-1~X-8 + M-1~M-3), L175 (M-1), L176 (closing d), L195–211 (§5.1 A channel), L265–280 (§5.5 counting code), L298–317 (§5.7 self-correction), L329–340 (§5.9 LSH collapse), L344–358 (§5.10 P-G transport), L362–385 (§5.11 KD baseline)
- `_kimi_v4_theme_reply_2026_09_20.md` — `3E37352EFB4B` — 45 行 — 7,372 B
  - 代表引用：L3, L5, L13, L14, L23, L25, L27, L29, L31, L35, L37, L41, L43, L45
- `_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md` — `BC14F47D927D` — 62 行 — 14,155 B
  - 代表引用：L7, L13, L17, L39, L41, L43, L45, L46, L47, L48, L50, L53, L56, L57, L58, L60, L62
- `_v4_distillation_theme_reply_workbuddy_2026_09_20.md` — `E3FE63A2F708` — 170 行 — 18,785 B
  - 代表引用：L24, L31 (C1), L33 (C2), L37 (C3), L39 (C4), L51 (C5), L63 (C6), L67, L76, L92 (S-17), L94 (S-37), L98 (S-13/S-19), L100 (S-08), L104 (S-02/S-30), L110 (S-17), L114 (S-08), L120 (S-02/S-30), L126 (S-04), L130 (S-13/S-19), L136 (S-15), L147 (no student), L158 (closing a), L160 (closing b), L162 (closing c), L164 (closing d)
- `_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` — `BFB4932F4467` — 140 行 — 12,963 B
  - 代表引用：L23–46 (S-38), L46 (S-08 up), L54 (S-28/S-29), L74 (S-16), L84 (S-10), L104 (S-36), L114 (S-39), L128 (closing a), L130 (closing b), L132 (closing c), L134 (closing d)
- `_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md` — `CDB27CD3008C` — 106 行 — 13,553 B
  - 代表引用：L12, L18, L20–30 (lens 1, 8 ideas), L31–37 (lens 2, 7 ideas), L39–47 (lens 3, 8 ideas), L49–58 (lens 4, 7 ideas), L64–68 (3 contradictions), L73–80 (M-1–M-4), L85 (if only one), L94 (closing a), L96 (closing b), L98 (closing c), L100 (closing d), L104 (caveat)
- `_v4_distillation_reply_claude_code_2026_09_20.md` — `D39CB17B051B` — 393 行 — 64,212 B
  - 代表引用：L15, L18, L19, L30 (boss_pa_1), L34 (S-05), L44 (byte-identical), L46 (S-17 + GLM_1), L58 (15 anchors), L65–69 (S-08/S-30), L71–76 (S-37), L79 (closing a), L84 (S-03), L92–98 (S-06), L100–102 (S-10), L104–110 (S-11), L112–116 (S-13/S-19), L118–126 (S-17), L128–132 (S-31), L135–142 (S-32/S-35), L144–152 (S-36/S-37/S-38), L154 (S-38 critique), L156–158 (S-40), L164 (§3 framework-free), L168 (§3 9-vs-5 mapping), L176 (closing), L195–211 (§5.1 A channel), L217–225 (§5.2 D_fix2), L231–245 (§5.3 1,338 responses), L251–257 (§5.4 BOSS family), L265–280 (§5.5 counting code), L286–294 (§5.6 simulate_rbr/rm/bayesian_nash), L298–317 (§5.7 GLM_1 self-correction), L319–327 (§5.8 reasoning tokens), L329–340 (§5.9 LSH collapse), L344–358 (§5.10 P-G transport), L362–385 (§5.11 KD baseline), L391 (§5.12 coda)
- `_v4_distillation_reply_coze_2026_09_20.md` — `00593014CBD3` — 459 行 — 71,084 B
  - 代表引用：L21–32 (critique on nature label), L39 (S-03), L43 (S-05), L51 (S-06), L57 (S-07), L63 (S-11), L65 (5 KT anchors), L67 (S-14), L73 (S-17), L77 (S-36), L83 (S-37), L89 (S-02/S-08/S-30), L93 (S-10), L94 (S-13/S-19), L95 (S-31/S-35/S-32), L96 (S-40), L100 (behated), L108–114 (T/R/A conservation), L118–124 (distance column critique), L128–134 (corr_T_A), L138–144 (D_fix2 baseline), L148–152 (worker identity), L154–162 (intra-vendor pairs), L172–176 (S-01), L178–185 (S-04), L188–194 (S-09), L196–201 (S-12), L206 (S-15), L212–217 (S-20), L220–226 (S-22), L228–232 (S-23), L236–242 (S-25), L244–250 (S-28), L252–258 (S-34), L260–275 (S-38), L281 (T1 cross-anchor), L283 (T2 schema reuse), L285 (T3 pre-registration location), L299–308 (N-01), L317 (N-02), L329 (N-03), L336–346 (N-04), L355 (N-05), L363–371 (N-06), L379 (N-07), L391 (N-08), L401–445 (§续四 KT_B1), L457 (closing)
- `_v4_d1_review_codex_2026_09_20.md` — `48387412B109` — 46 行 — 4,506 B (v1.1 PI 拍板 P3 落盘)
  - 代表引用：L9, L13 (Track 1), L19 (Track 2), L25 (Track 3), L33 (cross-discipline), L39 (D1 action items)
- `_v4_distillation_brainstorm_reply_codex_2026_09_21.md` — `0FF6C042B845` — 39 行 — 9,048 B (v1.1 PI 拍板 P3 落盘)
  - 代表引用：L5, L9, L11, L13, L15, L17, L19, L21, L23, L25, L27, L29, L31, L33, L35, L37, L38, L39

### §7.3 附件侧（assets/）

- `11-12-20-747-asset_20260921-111220-747_19c97b5cff3c_6cf18b87-_v4_theme_reply_doubao_2026_09_20_v1.0.md` — `19C97B5CFF3C` — 83 行 — 8,070 B
  - 代表引用：L1, L11, L13 (behated + internal consistency), L21 (S-36), L29 (S-17), L35 (S-31), L42 (S-11), L71 (closing a), L75 (closing b), L79 (closing c), L83 (closing d)
- `11-12-20-766-asset_20260921-111220-766_a18e58c8e2a3_bdb4bc12-_v4_theme_brainstorm_doubao_2026_09_21_v1.0.md` — `A18E58C8E2A3` — 130 行 — 19,389 B
  - 代表引用：L1, L3, L5, L13 (idea 1), L84 (idea 17), L101 (idea 21), L113 (idea 23), L123 (closing meta-1), L125 (meta-2)
- `11-12-20-778-asset_20260921-111220-778_48387412b109_7ca46e76-v4_d1_review_codex_2026_09_20.md` — `48387412B109` — 46 行 — 4,506 B (与 §0.2 `48387412B109` 同字节)
  - 与 results/ 下 codex 文件一致；本稿按 PI 拍板 P3 走 results/ 副本，本条仅作 SHA-12 / 字节对齐证据保留
- `11-12-20-782-asset_20260921-111220-782_0ff6c042b845_6d74a672-v4_distillation_brainstorm_reply_codex_2026_09_21.md` — `0FF6C042B845` — 39 行 — 9,048 B (与 §0.2 同字节)
  - 同上
- `11-12-20-756-asset_20260921-111220-756_c78cfb42e33d_e371e458-_v4_distillation_theme_reply_2026_09_20_v1.0.md` — `C78CFB42E33D` — 89 行 — 18,841 B
  - 代表引用：L3, L17–21 (on-disk observations 1–5), L27–28 (S-03/07/15), L29 (S-07), L33 (S-04/01), L35 (S-06), L41 (S-11), L47 (S-13/16/18), L51 (S-17), L55 (S-19/26), L61 (S-25/28), L65 (S-36), L69 (S-37), L79 (S-31/32/35), L81 (S-02/08/30), L87 (closing a/b/c/d)
  - **v1.1 注**：PI 拍板 P2 唯一归属 GLM；磁盘署名 `an invited reader team (multi-agent)` 原文保留
- `11-12-20-761-asset_20260921-111220-761_8295c3201f20_ee5ad31d-_v4_distillation_theme_reply_addendum_2026_09_20_v1.0.md` — `8295C3201F20` — 91 行 — 14,153 B
  - 代表引用：L3, L7, L15 (Impostor-calibrated), L21 (Convergence squeeze), L27 (Negative controls), L33 (Known-dose controls), L39 (Time-gated shared errors), L45 (Format-conditioned false positives), L51 (Difficulty-band shape), L57 (Frozen decoding zero), L63 (Non-stationary decision lines), L69 (Birthmarks), L75 (Ambient contamination), L81 (Transportability), L89 (closing a/b)
  - **v1.1 注**：同上
- `11-12-20-773-asset_20260921-111220-773_00593014cbd3_80c74bcd-_v4_distillation_reply_coze_2026_09_20.md` — `00593014CBD3` — 459 行 — 71,084 B
  - 与 results/ 下 coze 文件一致；本稿按派工单指引不重复计。
- `15-30-44-659-asset_20260920-153044-659_ac74a04efeb2_0a7da13e-查理_V4接受回执与D1首轮反馈_2026-09-20.md` — `ac74a04efeb2` — 附件侧不落盘 (v1.1 §0.4 + §4.14 PI 拍板 P1)
  - v1.1 worker 仅读摘要要点，未逐行重核；详见 §0.4 / §4.14

### §7.4 其他被引用的非上述文件（仅出现在 §1.8 / §2.10 / §6.4 / §6.5.3 组 C）

- `docs/V3X/KT_B1_SPEC_V0.1.md` — `0410CA0FBDAE` — 629 行 — 35,688 B（仅 §6.4 L267–L274, L157–161 L254–256 引）
- `verifier/handoff/KT_ABC1_anchors_sha256_12.json` — `03C6C01F3697` — 6,680 B / 189 行（§1.4 / §3.3 S-14 / §6.4 / **§6.5.3 组 C C1 / C5 / C6 / C7**）
- `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md` — `4485443757e7` — 309 行 — 15,478 B（仅 §6.4 L33 引）
- `docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md` — `9352a1675b10` — 103 行 — 5,615 B（仅 §6.4 L44–46 引）
- `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` — `BAEF94E393DE` — 215 行 / 实测 — 11,478 B（§6.4 L78–86, L179 + §6.5.3 C6）
- `deposon_team/plugins/_pg_v01_compute.py` — `D511C545F88E` — 20,923 B（仅 §2.4 / §4.6 引）
- `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` — `bd1caab42b4c`（仅 §1.5 L115–117 引）
- `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` — `9E1CCBDCEACC` — 25,347 B（§3.3 S-04 / §4.13 / §3.5 S-09 / §1.3 / §3.7 S-40）
- `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` — `268AB1239A8A` — 19,685 B（§1.3 / §3.3 S-15 / S-16 / §3.7 S-37 / §4.3 D-3 / §5.1 (workbuddy / claude code)）
- `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json` — `39732A92B5C9` — 13,150 B（§3.1 S-01 / §3.3 S-18 / §4.2 N-06）
- `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` — `FEE04170AA73` — 10,978 B（§3.4 S-22 / S-25 / §3.6 S-32 / §3.7 S-39）
- `corpus/v20/strip_captions_22.json` — `6A2656878745` — 12,798 B（§3.2 S-11 / §3.3 S-13 / §3.5 S-24 / §4.13）
- `corpus/v20/index_v2_2026_09_16.json` — `EFE05AD775DE` — 24,150 B（§1.6 / §3.6 S-32 / §4.2 N-01 / §4.12）
- `results/boss_pa_1_rbr_rm_result_2026_09_15.json` — `C7C59E0D2F6C` — 8,753 B（§1.1 / §1.7 / §2.8 / §6.4 / §6.5.3 C8）
- `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` — `4505CCA79C15` — 2,456 B（§3.3 S-14 / §3.6 S-35 / §4.12）
- `results/deposon_v3_v7_summary_2026_09_11.json` — `063AC8D00542` — 25,049 B / 380 行（§1.4 / §1.5 / §1.13 / §3.5 S-25 / §3.6 S-30 / §3.7 S-38 / §3.7 S-37 / §4.12 / §4.13 / §6.4 / **§6.5.3 组 C C4**）
- `results/deposon_v2_phase1_60cells_2026_09_11.json` — `A18BBC703B42` — 85,508 B（§3.1 S-06 / §3.4 S-04 / §4.13）
- `results/deposon_pg_v01_9m60c_2026_09_15.json` — `AB75889EE738` — 11,512 B（§2.4 / §3.1 S-02 / §4.2 N-06）
- `results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` — `576EAF8D7431` — 见 §3.3 S-15 / §3.4 S-21 / §3.5 S-25 / §3.7 S-37 / §4.3 D-3
- `results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json` — `05FF758AE921`（§3.3 S-07）
- `results/_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md` — `71D5C23D8C95`（§3.3 S-07）
- `attacks/a1_delete_anchor.py` — `78AC391D16FC`（§3.4 S-20 / S-23）
- `attacks/a2_reshuffle_manifest.py` — `3D54B277620E`（§3.4 S-23）
- `attacks/a3_rewrite_runs.py` — `F02B3EEE8D6E`（§3.4 S-20）
- `deposon_team/plugins/_v3x_frozen_schema_v1.json` — `9E99DCC4D920`（未直接引用）
- `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` — `4A08521F8DE1`（§1.5）
- `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` — `9F88A212A77C` — 204,441 B / 6,722 行（§2.8 / **§6.5.3 组 C C3**）
- `deposon_team/plugins/skill_a_p_a_60cells.py` — `B1463BB24403`（§2.8）
- `deposon_team/plugins/boss_pa_1_rbr_rm.py` — `5CC594147E00`（§4.6）
- `results/deposon_v3_physical_opt_60cells_2026_09_11.json` — `c659695aa23c`（§4.12）
- `results/deposon_game_theory_eval_2026_09_10.json` — `3FA0FF2C8C08`（§4.3 D-1）
- `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` — `FBB7677B9CD5`（§3.2 S-10 / §4.13）
- `results/deposon_volcengine_22caption_embedding_2026_09_10.json` — `C4B774C8E34C`（§3.2 S-08 / §4.13 / §4.12 S-36）
- `results/boss_pc_1_real_2d_ising_2026_09_15.json` — `43D9CE160FC8` — 2,460 B / 99 行（§6.5.3 C2 boss pair #1）
- `results/boss_pe_1_real_2d_ising_2026_09_15.json` — `43D9CE160FC8` — 2,460 B / 99 行（同上，与 pc_1 同字节同 SHA-12）
- `results/boss_pc_2_real_transverse_ising_2026_09_15.json` — `8933D61B180A` — 3,553 B / 136 行（§6.5.3 C2 boss pair #2）
- `results/boss_pe_2_real_transverse_ising_2026_09_15.json` — `8933D61B180A` — 3,553 B / 136 行（同上）
- `results/boss_pc_3_real_reservoir_2026_09_15.json` — `94B5398BE76C` — 2,364 B / 96 行（§6.5.3 C2 boss pair #3）
- `results/boss_pe_3_real_reservoir_2026_09_15.json` — `94B5398BE76C` — 2,364 B / 96 行（同上）
- `results/deposon_v20_gt2b.json` — `A2AE7997EE67` — 123,331 B / 500 行（§6.5.3 C5 反例锚：不匹配 6edb2aec1660）
- `tools/llm_client.py` — `1722500DA4AA`（§6.5.3 C7 实测，声明值不一致）
- `tools/exp_harness.py` — `275E480BA4D9`（§6.5.3 C7 实测，声明值不一致）

---

## §8 老实交代

- **本任务 0 LLM / 0 API / 0 其他文件改动**：本稿是 v1.0 → v1.1 的版本化更新，新文件落盘到 `D:\私人资料\deposon-repo\results\_v4_design_integration_2026_09_21_v1.1.md`；未触动 §0.1–§0.6 列出的 18 个输入文件；v1.0 原文件（`4B10CDE29C27`，119,732 B，1,041 行）未被动过（详见自验 4）。
- **第二轮更新（v1.1）所作动作**：仅在 input 侧读取、worker 实测、生成新 .md 文件；未触动：
  - v1.0 整合稿与 v1.0 问卷（自验 4 重算 SHA-12 应仍为 `4B10CDE29C27` / `6A3A2D8EE357`）。
  - 任何 18 frozen 制品、P-G v0 / v0.1、schema v1、verifier/、plugin spec。
  - 任何 LLM API / 任何外部 URL / 任何 WeChat / 任何 GitHub 操作。
  - 任何密钥 / 端点 / 专有提示词。
- **行数与哈希自测双口径（PI 拍板 P6）**：整合稿 v1.1 canonical 行数 = `[System.IO.File]::ReadAllLines(path, [System.Text.Encoding]::UTF8).Length`；本节交付前自验 1 / 2 / 5 项给出本稿最终 SHA-12 / 字节 / 行数。
- **谁拍的板 / 谁复算的 / 哪些是文件外宣称**：
  - 拍板方：PI（2026-09-21 拍板 P1–P6）。
  - 复算方：本会话内 worker（组 A codex 落盘字节级复制 identical；组 B 8 行 SHA-12 实测命中 7 + 第 8 行 worker 独立补 SHA-12；组 C C1–C8 8 条）。
  - 文件外宣称：组 B 的 7 个 SHA-12 由 PI 在本会话内提供，会话外查不到出处；邀请函正文实为 `(see SHA-12)` 占位符。worker 实测全部命中（§6.5.2 表）。
- **0 产物老实交代**：v1.0 原件 SHA-12 `4B10CDE29C27` / 119,732 B / 1,041 行 ReadAllLines；本稿（v1.1）SHA-12 在交付前自验报告给出，本节不预声明（本稿 §0.7 沿用 v1.0 自指哈希回避约定）。
- **plugin 端点老实交代**：本会话未注入 `academic-paper-assistant:academic-paper-polish` 与 `superpowers:verification-before-completion` 两个 skill plugin 端点；按方法论（独立锚 → 多源核对 → 不宣布未跑通步骤）执行两 skill 的核心约束；锚复核 / 自验 5 项 / 双算 SHA-256 / 三方陈列均按方法论执行，未依赖具体 skill 端点。`doc-writer` agent 本轮由父会话派单，所有产物的归属、签名、版本号、回执由 agent 自管，父会话在本回报内读取。
- **§8 老实交代（v1.1 第二轮更新）追加**：本轮新增 §6.5.3 组 C C7 / C8 两条附带新发现（C7 声明值与实测不一致、C8 §2.2 vs §8 字节标定沿用 §1.1 收录），明示"如实记录，不做裁定"；本稿不擅自调动 anchor-guard 改写 §0.5 中 v1.0 锚（保留原 16 文件统计，v1.1 §0.5 增加"含 §0.5 codex 两件 + §0.4 查理件共 18 文件"表述，不重写 §0.5）。
- **A-4 断行自检**：PI 已接受（2026-09-21）按此定稿。整合稿 v1.1 全文无词中断行（A-1 类问题零复发）。
- **中途无 abort / 未完成段落**：本稿全部条款已落入本节，未发现半完成段落。

—— `doc-writer`, Mavis 8-agent team, deposon workspace, 2026-09-21.
