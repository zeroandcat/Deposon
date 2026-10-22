# Deposon (凝子)

**An auditable, conservation-guaranteed, game-theoretically tested scattering layer over LLM reasoning paths.** · Paper: [arXiv:2609.09001](https://arxiv.org/abs/2609.09001) · License: [MIT](LICENSE)

Deposon is an ongoing research program on making multi-step LLM reasoning **machine-recheckable**. Its first two lines — **V1 (mind-map)** and **V2 (game-theory explanation)** — are **published** in the paper above; two further lines — **V3 (game-theory)** and **V4 (distillation)** — are active in this repository.

## Project lines

| Line | Theme | Status |
|---|---|---|
| **V1** | **脑图主线 / Mind-map** — an LLM-generated concept-decomposition graph as the substrate for reasoning | ✅ published |
| **V2** | **博弈论解释 / Game-theory explanation** — the scattering mechanism explained and tested game-theoretically (potential game, coordination ratio, falsified dynamical-equivalence propositions) | ✅ published |
| **V3** | **博弈论主线 / Game-theory line** — the mechanism program continues: pre-registered kill protocols, adversarial & equilibrium analyses, independent verifier suites | 🔬 active |
| **V4** | **蒸馏主线 / Distillation line** — distilling human judgment *methods* into datasets for **AI critical learning** (method transfer — explicitly **not** behavioral profiling) | 🔬 active |

**V1 + V2 are published as**: *Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths* — Qihao Yuan, [arXiv:2609.09001](https://arxiv.org/abs/2609.09001) (cs.AI, 2026-09; 23 pages, 5 figures). This repository is the program's code, verifier and record set.

## The mechanism (V1 + V2 core)

- Each node of an LLM-generated concept-decomposition graph is bound to a two-parameter **Deposon state**; reasoning paths undergo **three-channel scattering** — transmission, reflection, irreversible dissipation — obeying `T + R + A = 1` for arbitrary parameters.
- The maximum per-path energy-audit deviation is **2.2e-16** (machine epsilon): discarded paths leave a **machine-recheckable record** instead of vanishing.

## Published findings (as reported in the paper)

- **Synthetic trap benchmarks** (pre-registered): the path-filtering gain **is closed** — unified reaches **100%** versus a decoy-capture baseline at **7% / 10%**.
- **Real benchmarks**: the layer is **indistinguishable from a trivial six-keyword rule filter** (GSM8K 0.87 vs 0.85, McNemar p = 0.5; StrategyQA 0.899 vs 0.899) — the claim is sharpened to: **the differential value lies solely in machine verifiability.**
- **Fusion yields a second negative result**: convex combinations with a semantic prior never improve; the apparent gain at λ = 2 is an anti-field artifact — any fusion gain must be **nonlinear**.
- **Game-theoretic analysis**: an auditable scalar's monotonicity and near-gradientness are evidenced and the empirical coordination ratio (ECR) quantified; the three dynamical-equivalence propositions (P1a / P1b / T-P1c) are **falsified under the pre-registered kill protocol**, and the potential-game claim is downgraded to *approximate* (cyclic-graph median residual 0.669).

> Negative results are reported as part of the evidence. The repository keeps the same posture: readings, preregistrations and audit records stay on disk, and nothing here is a claim stronger than the literal wording of the data.

## Ongoing lines (V3 / V4)

- **V3 · game-theory line** — the mechanism program continues under the same preregistration discipline: kill-line protocols, adversarial checks, equilibrium / coordination analyses and independent verification. Current specs live under [`docs/V3X/`](docs/V3X/); audit suites under [`verifier/`](verifier/); run records under [`results/`](results/).
- **V4 · distillation line** — collecting and distilling human judgment *methods* (criteria, trade-offs, stopping rules) into structured datasets for **AI critical learning**: the objective is *method transfer to AI*, explicitly **not** building a behavioral profile. Collection datasets and ledgers live under [`results/`](results/) (`pi_cot` series).

## Repository layout

| Path | Contents |
|---|---|
| `tools/` | Experiment harness (`exp_harness.py`), LLM client (`llm_client.py`), figure generation |
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

**Deposon（凝子）**：让多步 LLM 推理**可机器复核**的散射层研究计划。**第一、二条线——V1 脑图主线 与 V2 博弈论解释——已成文发表**（[arXiv:2609.09001](https://arxiv.org/abs/2609.09001)，2026-09，cs.AI；作者：Qihao Yuan），本仓库即该计划的代码、验证与记录集；**V3 博弈论主线 与 V4 蒸馏主线 为进行中**。

- **机制（V1＋V2 核心）**：概念分解图节点绑定「凝子态」，路径经三通道散射（透射／反射／不可逆耗散），对任意参数满足 `T+R+A=1`（逐路径审计偏差 ≤ 2.2e-16，机器精度）。
- **已发表要点（如实）**：合成陷阱基准上路径筛选增益（预登记）**闭合**（unified 100% vs 抽取基线 7%／10%）；真实基准上与「6 关键词规则过滤」**无法区分**（GSM8K 0.87 vs 0.85；StrategyQA 0.899 vs 0.899）⇒ 主张收窄为「**差异化价值在于可机器验证性**」；融合为负结果；博弈论分析中三条动力学等价命题在预登记协议下**被证伪**、势博弈主张降级为**近似**。
- **进行面**：**V3**＝机制程序延续（预登记判死协议、对抗与均衡分析、独立验证套件；`docs/V3X/`、`verifier/`、`results/`）；**V4**＝人类判断**方法**的蒸馏（服务于 AI 批判性学习，**方法迁移而非画像**；`results/` 之 `pi_cot` 系列）。
- **密钥纪律**：一切 API key **只经环境变量**、0 硬编码、0 入库。｜**许可**：MIT（见 [LICENSE](LICENSE)）。
