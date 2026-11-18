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

> **Status wording.** `closed` means: the line's recorded work has reached a verdict and no further experiment is scheduled for it — it does **not** mean every hypothesis in the line was confirmed. A closed line may carry negative results, known defects, or a verdict that a construction failed rather than a claim. Read each line's own verdict files for what was actually decided. `draft only · not started` means that planning text exists but no SPEC or experimental program has been initiated; it implies no measurements, results, or verdicts. Since 2026-11-10 the V5 row reads `SPEC-precursor planning · draft #17 · not started`: the plan draft has reached #17 (重制版 remaster round), which is still planning text only — the freeze register (no SPEC drafting, no seed-mapping table, no kill-experiment design) is unchanged. Preregistration-oriented real-model dry runs (0.6B / 4B pipeline shakedown on the new machine) have landed and are registered (closed chains in the execution repo's current-state register + the evidence-round pointer table below) — dry-run shakedown records of the planning phase do not by themselves turn V5 into an experiment line with results, and formal initiation remains pending the project owner's final verdict.

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
**V5 现态（2026-11-18）**：计划本体至十七稿（SPEC 前置层·重制版）；执行线自 2026-11-12 起推进——W-2→W-3 修复线、4B/0.6B 双 SP 轮、SIM 首档均已双审闭合；后续执行谱系与在途队列详见私有执行仓 `zeroandcat/Deposon-V5-exec` 根 README §8（现行态登记·覆盖式）与 HANDOFF。过渡立项登记（2026-11-10）在册：过渡推进形态＝候补底模序 Qwen3-4B；正式立项（qwen4-deposon）候 Qwen4；SPEC 前置层冻结面（0 SPEC 起草·0 种子映射表·0 判死实验设计）不变。

## 可观成果证据轮指针表（2026-11-12 起）

> 覆盖式登记：只保留轮号/资产/指纹的现行指针；各轮完整叙事与协作链＝git log 考古。

| 轮 | 日期 | 内容 | 远端指针 |
|---|---|---|---|
| R35 | 2026-11-12 | 隔夜终态读数呈报 `2cd005abe5c8` · W1 训练曲线 XLSX `fcf7c60d2479` · 中径 v11 日志 `d0b3acb51582` | `3bf0738` |
| R36 | 2026-11-12 | trial_fire_v2 读数长表 `ab33c298ddcb` · perm 终图 `d0b5f7c5aa7d` · v11 patch `3110309788ce` · SPEC 差异表 `26811ab5e679` | `d7b251d` |
| R37 | 2026-11-13 | W-3 修复轮闭合：三检点+reeval+JSON+scripts/logs+uvw2 17 卷（42 资产·34.3 GB）→ 私仓 `mirror-4B-w3-20261113` | — |
| R38 | 2026-11-13 | 0.6B W1 容器轮读数包（12 资产）→ 私仓 `mirror-0.6B-w1-20261113` | — |
| R39 | 2026-11-14 | 4B SP 轮 ALL-GREEN（20 资产·design `b405c2df3d88`）→ 私仓 `mirror-4B-sp-20261114` | — |
| R40 | 2026-11-14 | 0.6B SP 轮 ALL-GREEN（21 资产·母体 `40b281f62a88`·tag→commit `ab0ce0a5fb55`）→ 私仓 `mirror-0.6B-sp-20261114` | — |
| R41 | 2026-11-14 | SIM 轮 ALL-GREEN（读数包 6 件·工具 `ecadb06b51b1`/读数 `6c70894b6fa8`）→ 私仓 `results/sim_20261114/`（commit `2b3eb87fac2e`） | — |

后续执行线读数包（夜弧绑定深化/五臂链/seq3/fire6/w600 定性/VW 系判别与删凝子/镜像清理账）均入私仓 `results/`·主仓只保持指针面。

## 历史登记区指针（git log 考古）

- R27 本地交付账（2026-10-30）：R26 正式决策总账 4,710=READY 4,069+STOP 641；本地 3,913；READY 原始字节 190,921,854 B——完整数字面＝历史 README 版本（git log -S 考古）。
- 镜像治理注记（2026-11-10）：TRAE 正名链（R30 改名→R31 回改·8 件原名恢复·blob 不变）、`_v5_` 前缀 218 件、镜像漂移登记 3 项（README 版本迭代/B3 blob 历史可达/TRAE 链文件 133B 脱敏变体）——完整登记＝历史 README 版本。
- `handoff_machine_readable.json`：随本 README 同步刷新（schema v2）；与 V5 计划本体冲突处以计划本体为准。
