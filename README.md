# Deposon (凝子)

**An auditable, conservation-guaranteed, game-theoretically tested scattering layer over LLM reasoning paths.** · Paper: [arXiv:2609.09001](https://arxiv.org/abs/2609.09001) · License: [MIT](LICENSE)

Deposon is a research program on making multi-step LLM reasoning **machine-recheckable**. Its first two lines — **V1 (mind-map)** and **V2 (game-theory explanation)** — are **published** in the paper above; two further lines — **V3 (game-theory)** and **V4 (distillation)** — are **closed** in this repository: their kill-line protocols, adversarial & equilibrium analyses, probe verdicts and negative results are all kept on disk. **V5 (mind–matter formulation)** is in **SPEC-precursor planning** (draft #17, work-in-progress): a plan draft exists, but **no experiment has been run, no SPEC drafted, and no result claimed** — not an experiment line with results.

## Project lines

| Line | Theme | Status |
|---|---|---|
| **V1** | **脑图主线 / Mind-map** — an LLM-generated concept-decomposition graph as the substrate for reasoning | ✅ published |
| **V2** | **博弈论解释 / Game-theory explanation** — the scattering mechanism explained and tested game-theoretically (potential game, coordination ratio, falsified dynamical-equivalence propositions) | ✅ published |
| **V3** | **博弈论主线 / Game-theory line** — pre-registered kill protocols, adversarial & equilibrium analyses, independent verifier suites; closed on recorded verdicts | ✅ closed |
| **V4** | **蒸馏主线 / Distillation line** — distilling human judgment *methods* into datasets for **AI critical learning** (method transfer — explicitly **not** behavioral profiling) | ✅ closed |
| **V5** | **物心回路 / Mind–matter formulation** — SPEC-precursor planning only; no experimental program has been initiated | 📝 SPEC-precursor planning · draft #17 · not started |

**V1 + V2 are published as**: *Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths* — Qihao Yuan, [arXiv:2609.09001](https://arxiv.org/abs/2609.09001) (cs.AI, 2026-09; 23 pages, 5 figures). This repository is the program's code, verifier and record set.

> **Status wording.** `closed` means: the line's recorded work has reached a verdict and no further experiment is scheduled for it — it does **not** mean every hypothesis in the line was confirmed. A closed line may carry negative results, known defects, or a verdict that a construction failed rather than a claim. Read each line's own verdict files for what was actually decided. `draft only · not started` means that planning text exists but no SPEC or experimental program has been initiated; it implies no measurements, results, or verdicts. Since 2026-11-10 the V5 row reads `SPEC-precursor planning · draft #17 · not started`: the plan draft has reached #17 (重制版, remastered per PI 2026-11-10 16:32 order), which is still planning text only — the freeze register (no SPEC drafting, no seed-mapping table, no kill-experiment design) is unchanged. Preregistration-oriented real-model dry runs (0.6B / 4B pipeline shakedown on the new machine) may be in transit; when their receipts land, only registered readings are recorded in the backfill slot below — dry-run shakedown records of the planning phase do not by themselves turn V5 into an experiment line with results, and formal initiation remains pending the project owner's final verdict.

## The mechanism (V1 + V2 core)

- Each node of an LLM-generated concept-decomposition graph is bound to a two-parameter **Deposon state**; reasoning paths undergo **three-channel scattering** — transmission, reflection, irreversible dissipation — obeying `T + R + A = 1` for arbitrary parameters.
- The maximum per-path energy-audit deviation is **2.2e-16** (machine epsilon): discarded paths leave a **machine-recheckable record** instead of vanishing.

## Published findings (as reported in the paper)

- **Synthetic trap benchmarks** (pre-registered): the path-filtering gain **is closed** — unified reaches **100%** versus a decoy-capture baseline at **7% / 10%**.
- **Real benchmarks**: the layer is **indistinguishable from a trivial six-keyword rule filter** (GSM8K 0.87 vs 0.85, McNemar p = 0.5; StrategyQA 0.899 vs 0.899) — the claim is sharpened to: **the differential value lies solely in machine verifiability.**
- **Fusion yields a second negative result**: convex combinations with a semantic prior never improve; the apparent gain at λ = 2 is an anti-field artifact — any fusion gain must be **nonlinear**.
- **Game-theoretic analysis**: an auditable scalar's monotonicity and near-gradientness are evidenced and the empirical coordination ratio (ECR) quantified; the three dynamical-equivalence propositions (P1a / P1b / T-P1c) are **falsified under the pre-registered kill protocol**, and the potential-game claim is downgraded to *approximate* (cyclic-graph median residual 0.669).

> Negative results are reported as part of the evidence. The repository keeps the same posture: readings, preregistrations and audit records stay on disk, and nothing here is a claim stronger than the literal wording of the data.

## Closed lines (V3 / V4) — what the record contains

- **V3 · game-theory line** — the mechanism program ran under preregistration discipline: kill-line protocols, adversarial checks, equilibrium / coordination analyses and independent verification. Current specs live under [`docs/V3X/`](docs/V3X/); audit suites under [`verifier/`](verifier/); run records and verdicts under [`results/`](results/). The line's terminal verdicts (including a known-defect verdict on one hard-gap item) are recorded in `results/L1/V3/verdict/judgement/`.
- **V4 · distillation line** — human judgment *methods* (criteria, trade-offs, stopping rules) were collected and distilled into structured datasets for **AI critical learning**: the objective is *method transfer to AI*, explicitly **not** building a behavioral profile. Collection datasets and ledgers live under [`results/`](results/) (`pi_cot` series); the line's probe and adjudication verdicts in `results/L1/V4/verdict/judgement/`.

## V5 — SPEC-precursor planning, not started (draft #17)

- The V5 direction currently has a **SPEC-precursor plan draft**: it organizes the named direction, evidence and wording discipline, prerequisites, and decision points. Its claims are capped at **declaration level**.
- The draft's own freeze register records **no SPEC drafting, no seed-mapping table, no kill-experiment design, and no literature pre-scan**. Accordingly, there are **no V5 experimental measurements, results, or verdicts** to report.
- The `results/L1/V5/` folder is retained as a filing label and may contain mixed-line records. Its presence is not evidence that a V5 experimental program exists or that any V5 claim has been established.
- **Cold-start pack (定义行·B 轨升格位)**: a cold-start agent pack = ① V5 plan draft #17 (main text, mirrored in-repo) + ② this repo (github.com/zeroandcat/Deposon) + ③ the baseline commit as measured by `git ls-remote` at drafting time + ④ a declaration that the annotation book and other shared/ working files are **not part of the pack and not execution-required** (execution surface has zero dependency on them; the annotation book is now mirrored in-repo for auditability — see the planning register below) + ⑤ a superseding note that `handoff_machine_readable.json` follows the plan draft where they conflict.
- **Current planning register (2026-11-10)**: plan draft #15 `c70fa2e6fce0` (1,311 lines) → #16 `f105e4882a54` (1,490 lines, TRAE-corrected round version, mirrored at R32, 0 content edit since) → **#17 `00f2971ae043` (1,569 lines, remaster round version, mirrored at R33 — the current draft)**, mirrored in this repo under `_repo_mirror/V5计划/` (`查理_V5计划本体十六稿_2026_11_09.md` and `V5计划十七稿_2026_11_10.md`, the latter mirrored as-is from shared/); annotation book `d435dff68e47` (780 lines) + draft-#16 annotation sheet `b3603fca87b4` (120 lines, TRAE-corrected round version, mirrored at R32) — the draft-#17 companion annotation sheet `b1dac18fc68f` (57 lines, remaster-round companion, mirrored at R33 wave 2; carries the annotation-booklet supplement slot 注G per the 16th-draft annotation-face precedent — the booklet supplement is registered inside the sheet, the booklet itself stays 0-touch); persistent ledger `5f597ba81696` (1,064 lines, P114+ state, collection rounds ongoing; internal working file, not in this repo — always measure the shared/ current state directly).
- **Execution-results backfill slot (R33 wave 3 · in transit)**: real-model preregistration dry runs (0.6B / 4B pipeline shakedown on the new machine, per the plan draft's M0 window and the PI 2026-11-10 rerun order) are in transit tonight; this slot is a placeholder to be backfilled with their **registered readings** (anchored by the experiment seat's execution receipts) when they arrive — or honestly registered as *still in transit* at the 23:30 hard deadline (credential-expiry cut-off). Backfilled readings are dry-run / pre-experiment records of the planning phase, **not** V5-line results.
- **TRAE correct-name note (R31)**: **TRAE is the correct name** (trae = the ByteDance agent tool); the PI 2026-11-09 17:46 phrasing "TRAE是误拼于TREA" was **self-corrected by PI at 2026-11-10 00:56** ("请改回来"), and the R30 rename has been fully reverted at R31 — see the mirror governance notes below.

> **On the `results/L1/` family folders.** The experiment tree groups records by family (`V3`, `V4`, `S3S4`, `G-E01`, `T`, `K-杀线`, `ηETAC`, `39词`, `K-EXP8`, `委托面`, …). Folder names are **filing labels for where a file was archived, not a claim that every file inside belongs to that experiment line** — a directory may also hold cross-line bookkeeping and archival ledgers. Read each file's own header for what it is; the tree is an index of the record, not a taxonomy of conclusions.

## Selected audit records beyond the main lines

The wider record is not a single success/failure label. It preserves line-specific verdicts, recomputations, launch gates, and unresolved construction defects:

- **S3 / S4 — converged arithmetic, separate verdicts.** Independent implementations converged the outstanding S3 sequence value; the S4 record then reported two `FAIL` lines, one `PASS`, and a fourth whose five component hits did not satisfy the registered conjunction. Open items remain, so this is not presented as a whole-family closeout.
- **T / T1 — a bounded retirement, not a general no-effect claim.** Within the recorded construction and at the registered `>5pp` discernibility scale, the temperature axis was retired because temperature-associated changes were not separated from endpoint nondeterminism. The noise-floor observation remains a design constraint for later sampling experiments.
- **ηETAC — an independent measurement check.** A third-party recomputation found `sep = 3` across all four recorded tiers, with both orderings agreeing. This documents a constant-criterion / degeneration observation in the specified M1 construction domain; it is not a general verdict on η.

These examples illustrate the repository's rule: **a measurement, a criterion result, a construction failure, and a proposition-level verdict are different kinds of record.** The family index and its linked evidence files are the authority for their exact scope.

## Repository layout

| Path | Contents |
|---|---|
| `tools/` | Experiment harness (`exp_harness.py`), LLM client, distortion calculator, figure generation |
| `verifier/` | Audit suites and independent verification runs (`audit/`, `kill_lines/`, `runs/`, versioned checkers) |
| `docs/` | Specifications, requirements, verification reports, findings & lessons (`V3X/`, `reviews/`) |
| `results/` | Experimental records, audit registries and collection datasets (JSON) |
| `paper/` | Manuscript sources (CN / EN) and figures |
| `mindmap_corpus_v20.py`, `scripts/`, `run_*.py` | Mind-map corpus tooling and experiment runners |

## Getting started

```bash
git clone https://github.com/zeroandcat/Deposon.git
cd Deposon
pip install -r requirements.txt          # numpy, requests
```

- **API keys** (if you run LLM-backed experiments): provide them via **environment variables only** — never hard-code or commit keys. Several recorded experiments can be re-verified from cached data without any key.
- Each experiment script is self-describing (see its header); outputs are written to `results/`.

## Citation

```bibtex
@misc{yuan2026deposon,
  title         = {Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths},
  author        = {Yuan, Qihao},
  year          = {2026},
  eprint        = {2609.09001},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  doi           = {10.48550/arXiv.2609.09001}
}
```

## License

MIT — see [LICENSE](LICENSE).

---

## 中文简介（简版）

**Deposon（凝子）**：让多步 LLM 推理**可机器复核**的散射层研究计划。**第一、二条线——V1 脑图主线 与 V2 博弈论解释——已成文发表**（[arXiv:2609.09001](https://arxiv.org/abs/2609.09001)，2026-09，cs.AI；作者：Qihao Yuan），本仓库即该计划的代码、验证与记录集；**V3 博弈论主线 与 V4 蒸馏主线 已结束**（其判死协议、对抗与均衡分析、探针判定与负结果皆留档）；**V5 物心回路仍是未启动的 SPEC 前置草案**，无实验读数或终判。

- **机制（V1＋V2 核心）**：概念分解图节点绑定「凝子态」，路径经三通道散射（透射／反射／不可逆耗散），对任意参数满足 `T+R+A=1`（逐路径审计偏差 ≤ 2.2e-16，机器精度）。
- **已发表要点（如实）**：合成陷阱基准上路径筛选增益（预登记）**闭合**（unified 100% vs 抽取基线 7%／10%）；真实基准上与「6 关键词规则过滤」**无法区分**（GSM8K 0.87 vs 0.85；StrategyQA 0.899 vs 0.899）⇒ 主张收窄为「**差异化价值在于可机器验证性**」；融合为负结果；博弈论分析中三条动力学等价命题在预登记协议下**被证伪**、势博弈主张降级为**近似**。
- **已结束面**：**V3**＝机制程序（预登记判死协议、对抗与均衡分析、独立验证套件；`docs/V3X/`、`verifier/`、`results/`）；**V4**＝人类判断**方法**的蒸馏（服务于 AI 批判性学习，**方法迁移而非画像**；`results/` 之 `pi_cot` 系列）。**「已结束」只表该线已在判定件上收口，不表该线之假设皆被证实**——负结果、已知缺陷、乃至「构造失灵而非命题被证伪」之判定，皆在册可查。
- **V5 草案边界**：现有文本只整理具名方向、证据与措辞纪律、前置条件和决策点，主张封顶于声明级；草案冻结面明确 **0 SPEC、0 种子映射表、0 判死实验设计、0 文献预扫**。`results/L1/V5/` 仅作归档标签并含跨线混录，不能据目录名反推实验线已经启动。
- **其他在册审计例**：S3／S4 保存了算术收敛与逐线分判，未把整族宣称为收口；T1 温度轴只在既定构造域与 `>5pp` 可辨尺度上退役，并不推出「温度普遍无效」；ηETAC 的第三方复算记录了四档 `sep` 恒为 3 的判据退化观察，射程不外推。**测量、判据结果、构造失灵与命题级终判，始终分账。**
- **树册目录之读法**：`results/L1/` 下之族名目录是**归档归位之标签**，非「该目录内每一件皆属该实验线」之断言；跨线台账与清卷工作件亦在其中，须以各件自身之卷首为准。
- **密钥纪律**：一切 API key **只经环境变量**、0 硬编码、0 入库。｜**许可**：MIT（见 [LICENSE](LICENSE)）。
**V5 现态（2026-11-10）**：计划本体已至十七稿（SPEC 前置层计划·重制版〔Deposon 核心再锚定＋凝子绑定方向三候选＋走偏诚实披露＋当日全读数弧入稿〕·0 正式实验执行·0 SPEC 本体起草·立项候 PI 终判·全文已上仓 `_repo_mirror/V5计划/`〔R33〕）；README/handoff 已按 2026-11-10 夜 R33 全重制窗刷新（十七稿件位新增＋今夜 0.6B/4B 真机预实验执行果回填位〔在途·回填以执行回执锚定〕）；凌晨件族治理链沿 R30–R32 在册（R30 上传＋R31 TRAE 正名回改＋R32 十六稿更正轮）。

**V5 过渡立项登记（2026-11-10 · PI 裁示 20:58:59）**：PI 原文「均持撤回权下认可双审代裁，V5等待戈多Qwen4，可记过渡立项于可更新的仓根readme」。据此登记：① **V5 过渡立项**即日生效（登记于仓根 README·本行自含日期锚 2026-11-10·不候底账 P117 指纹〔同刻在途〕）；② **正式立项（qwen4-deposon）维持候 Qwen4**〔戈多式等待注记：不设到达期限·不作到达预测·Qwen4 到达即转入正式立项候选评审〕；③ **过渡推进形态＝候补底模序 Qwen3-4B**·服务器预实验在跑（0.6B/4B 真机预实验·执行果回填位在册〔R33 wave 3 在途·读数回填以执行回执锚定〕）；④ 与上段「立项候 PI 终判」之衔接：上段系本登记前之点态登记·0 回改（0 强改）·现态以本登记行为准——过渡立项已裁·正式立项候 Qwen4·SPEC 前置层冻结面（0 SPEC 起草·0 种子映射表·0 判死实验设计）不变。

---

## R27 本地交付账（2026-10-30）

- R26 正式决策总账：**4,710 = READY 4,069 + STOP 641**。本地 **3,913 = READY 3,404 + STOP 509**；既有远端孤本快照 **797 = READY 665 + STOP 132**。
- 本地范围账：**3,913 = mapped 3,565 + v11 347 + 原根 README 1**；mapped **3,565 = READY 3,404 + STOP 161**，故本地 STOP **509 = 161 + 347 + 1**。
- READY 原始字节 **190,921,854 B**，脱敏后上传件字节 **190,260,002 B**；STOP 原始字节 **113,342,402 B**。这些数字只描述门禁与字节账，不代表实验结论或上传授权。
- R27 本地 staging 预计 **4,071 = R26 READY 4,069 + 对外交付册 1 + 本特殊根 README 1**。内部线索册与全量索引不进入 staging。
- 对外交付册公开目标：`_repo_mirror/doc/_delivery_list_external_2026_10_30_r27.md`。R26 独立验证为 PASS；READY 原始／上传 SHA-256 与 v11 snapshot SHA-256 的两类交集均为 **0**。
- 本轮仅本地重建与核验：**upload_authorization=false；remote_write=NOT_PERFORMED**；R26 孤本来源未重采；R27 已另行完成当前远端全树精确字节拉回（HEAD 06045bceff07908aa38b8b5d3e626731b7326e7d，3,438 件），范围外非镜像文件 434 件已留档保护。
- 2026-11-10 注：本 README R30 刷新前远端 HEAD＝d471b2f（R29）·R31 回改前远端 HEAD＝3c1b5dd（R30）·R32 上仓前远端 HEAD＝329d3ac（R31）·R33 全重制前远端 HEAD＝50809f9（R32）——见下方「镜像治理注记」。

## 镜像治理注记（2026-11-10 · remote mirror governance notes）

- **Current HEAD**: `50809f9` (R32 — V5 draft #16 TRAE-corrected round + annotation-sheet update mirrored + README/handoff refresh) was the pre-update baseline of this **R33 full-remaster round** (V5 draft #17 mirrored + README/handoff pointer-face remaster + tonight's execution-results backfill slot, per PI order 2026-11-10 19:00:50, plan A; wave-split sync: structure wave → annotation wave → final wave). The R27 ledger above was written at HEAD `06045bc`; treat all as point-in-time registers, and always measure the current HEAD post-clone (`git ls-remote origin main`).
- **`_v5_` prefix count**: **218 files** as measured on origin/main at `d471b2f` (after the 2026-10-23 public-mirror narrowing of −166 files). The previously registered count of **235** is a **pre-narrowing historical snapshot**; executors should always measure post-clone (`git ls-tree -r origin/main --name-only | grep -c "_v5_"`).
- **Mirror-drift register (3 MISMATCH · all "true at registration, stale vs. remote current state" — not fabrications)**:
  1. **README registration (#8)**: draft-cited README version `a80b3db006a5` (7,279 B) was superseded by the R27 rebuild (`83485a30da0c`, 13,709 B), and again by this R30 refresh; old versions are recoverable via `git log -S` archaeology.
  2. **B3 blob (#11)**: blob `5c47126d361b` was removed at R27 — now reachable **only via history** (`git log --find-object=5c47126d361b`, last seen at `06045bc`).
  3. **TRAE chain file (#12)**: the locally registered v37 (`1b6ceaef0290`, 857,249 B) vs. the remote in-place copy (`62425707bfe3`, 857,116 B) differ by **133 B** — remote copy verified as the **redacted mirror variant** of the same v37; dual-anchor citation: registered anchor kept + remote measured anchor noted.
- **TREA→TRAE rename revert (executed at R31 · PI self-correction order 2026-11-10 00:56「请改回来」)**: the R30 round (per the then-current PI 17:46 reading) had renamed the uppercase `TRAE_`-prefixed family (8 files) to `TREA_`; per the PI self-correction (**TRAE is the correct name**; trae = the ByteDance agent tool), all 8 files are renamed back to their **original `TRAE_` names** at R31 (blob unchanged — e.g. the asset-chain file `_repo_mirror/类型面/work/_unclassified/repo/docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` keeps blob `62425707bfe3`; full TREA→TRAE mapping in the R31 commit message). Paths remain recoverable via `git log --follow` across both renames. Tree-wide `TREA_`-prefixed residue after R31: **0**. Historical references to the `TREA_` spellings inside existing mirror files are **point-in-time registers left untouched** (0 content edit beyond the registered positions); the current canonical names are the `TRAE_` originals. Lowercase `_trae` / infix usages were never renamed and remain as-is.
- **V5 plan upload register (2026-11-10 · PI order「皆上传」·R32 TRAE-corrected round update)**: `_repo_mirror/V5计划/查理_V5计划本体十六稿_2026_11_09.md` (`f105e4882a54`·1,490 lines — TRAE 正名更正轮版, replacing `817db4166817`·1,484 lines at R32), `_repo_mirror/V5计划/查理_V5计划本体注释册_2026_11_09.md` (`d435dff68e47`·780 lines — untouched at R32), `_repo_mirror/V5计划/查理_V5计划本体十六稿注释面_2026_11_09.md` (`b3603fca87b4`·120 lines — TRAE-corrected round version, replacing `afb5161a8308`·91 lines at R32) — mirrored for auditability per PI order; the cold-start execution surface still has **zero dependency** on the annotation book / annotation sheet.
- **V5 plan upload register (2026-11-10 night · PI order 19:00:50 plan-A full-remaster round · R33 wave 1)**: `_repo_mirror/V5计划/V5计划十七稿_2026_11_10.md` (`00f2971ae043`·1,569 lines — remaster round version, mirrored as-is from shared/, filename kept as the draft's registered shared name; the draft-#16 files registered above stay untouched, 0 content edit). The draft-#17 companion annotation sheet + booklet supplement landed and are registered in the wave-2 entry below; tonight's 0.6B/4B dry-run readings backfill (wave 3, anchored by execution receipts) remains a registered slot to follow in this same round window. The cold-start execution surface still has **zero dependency** on the annotation book / annotation sheet.
- **V5 plan upload register (2026-11-10 night · R33 wave 2 — annotation wave)**: `_repo_mirror/V5计划/V5计划十七稿注释面_2026_11_10.md` (`b1dac18fc68f`·57 lines — draft-#17 companion annotation sheet: base-chain fingerprint reconciliation + gate-D self-check maintenance note [12/12, 0-touch at rows 1096–1107] + mechanical-diff change ledger [title-row replace + §7.18 79-line block insert, 0 unregistered scatter] + pointer-refresh table + booklet-supplement slot 注G), mirrored as-is from shared/ per the writer seat's 19:18 delivery. The draft-#16 annotation sheet `b3603fca87b4` and annotation book `d435dff68e47` remain **0 content edit** as historical verification faces. Wave 3 (execution-results backfill) slot unchanged — in transit.
- **R34 (2026-11-10 night · transition-initiation registration round)**: root-README V5 transition-initiation slot added per PI order 2026-11-10 20:58:59 (transition initiation registered with self-contained date anchor; formal initiation qwen4-deposon awaits Qwen4 — Godot-style waiting note; transition advance = Qwen3-4B candidate base-model sequence, server pre-experiment in transit). Pre-update baseline measured at execution: remote HEAD `093d1c5` (R33 wave 2), README sha256-12 `383eed242c32` (141 lines) — no drift vs. in-register clues. Pure addition (existing content 0-touch beyond the new slot); `handoff_machine_readable.json` untouched this round (its `project.status` field still reads "formal initiation pending PI final verdict" — superseded-in-part by this registration; sync listed as an out-of-scope suggestion for the PI).
- **handoff_machine_readable.json**: updated to schema v2 alongside this README; where the handoff file and the V5 plan draft conflict, **the plan draft governs**.
