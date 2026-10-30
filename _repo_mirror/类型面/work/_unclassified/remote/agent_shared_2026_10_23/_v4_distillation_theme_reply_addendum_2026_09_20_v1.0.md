# Addendum to the Theme Reply (v1.0)

**From:** the same invited reader team (multi-agent), same channel per §5.4. **Date:** 2026-09-20.

## AI-use disclosure

Assembled by the same drafting agent from four parallel brainstorm files by our LLM multi-agent team: a theory analyst, an on-disk verification agent (fresh digests, line reads), a literature analyst (literature from memory, no network; marked [unverified]), and a contribution-shape analyst. AI assistance throughout; no human co-author.

## Positioning

This file supplements our theme reply v1.0 and contains only new material: no seed entry from that reply is re-engaged; every hook is a fresh read or new line range on files already measured there. Conventions as in v1.0 — the PI's local paths, SHA-12 as measured, line ranges from our reads; literature memory-recalled, marked [unverified] (v1.0's [未核]). Twelve of the 28 brainstorm candidates survive merging; the rest folded into these or are held back. Tags as in v1.0.

## New idea entries

### Impostor-calibrated attribution — involuntary micro-habits, verified the stylometric way

**Kernel.** Distribution-matching distillation optimises fidelity and mechanically carries the teacher's micro-habits — punctuation, whitespace, defaults; a habit surviving the distiller's rephrasing is a property of the training signal, not the context window. Stylometric verification is a one-class problem: impostor methods calibrate the false-accusation rate with pseudo-authors; function-word style survives topic shift. Merged: attribution re-cast as verification over an open candidate set, impostors being independently trained same-scale same-corpus models — doubling as the confounder-matched control the ground-truth preconditions ask for. [pure speculation]
**Why interesting.** Gives the "known teacher candidate" prototype a calibrated false-accusation rate — the number the cost question turns on. Weakest viable version: survival of a single punctuation habit through one paraphrase round.
**Anchor.** None on disk. Literature: Mosteller–Wallace 1964; the impostor-method line of Koppel et al. [unverified].

### The convergence squeeze — asymptotic invisibility meets representation convergence

**Kernel.** A distilled student is an empirical estimate of the teacher's distribution: expected drift of distribution-level statistics vanishes at O(1/n); only tail statistics with exponentially growing covering numbers hold persistent fingerprints. Independent training itself converges with scale (Platonic-representation hypothesis; model stitching: compatibility is not common origin) [unverified: Huh et al. 2024; Bansal et al. 2021]. Null and alternative squeeze toward the same limit; separation lives in tail rates and finite-sample constants — the long-tail and statistical-signature seeds are one theorem's two faces. [pure speculation]
**Why interesting.** Converts "is there a fingerprint" into "which tail statistics beat the bound" — computable, reusable even when nothing beats it; convergence becomes the natural null, re-pricing alignment-style evidence. Weakest viable version: a finite-alphabet toy model proving the decay rate.
**Anchor.** None on disk.

### Negative controls and the negative-space map

**Kernel.** A silent channel is informative only relative to a stated mechanism: "no trace" is threefold — not distilled, distilled-and-erased, or the mechanism never leaves any. Epidemiology's negative-control outcome — sharing the confounders, not the target cause — is the operational test: if the fingerprint statistic fires on an independently trained pair sharing the public corpus and verifiably containing no distillation, common-cause contamination is measured directly. [pure speculation]
**Why interesting.** The operational half of the common-cause separability candidate our v1.0 Closing named — the H0 built from pairs, not theory; accumulated negatives become a power-boundary map. Weakest viable version: single-channel power decay with distance on synthetic pairs.
**Anchor.** None on disk. Literature: the negative-control framework of Lipsitch et al. [unverified].

### Known-dose controls — self-perturbation and the graph-to-caption flattening

**Kernel.** Temperature, quantisation, and pruning variants of one set of weights are student stand-ins at known dose: detectability becomes a statistic-vs-dose monotonicity question, its zero point needing no training run. A content-side twin is on disk: 22 graph–caption pairs correspond one-to-one (N == n_labels); captions are pure label chains (S2_n35: 35 labels, no edges) while edge structure (n_edges 19–88, named/filler split) lives only in the graph files — per-pair information loss computable without a model. [re-fit hypothesis, not calibrated] (perturbation half: [pure speculation])
**Why interesting.** The only student-side stand-ins obtainable without new runs — the control arm the ground-truth preconditions lack; a flat dose-response curve fails informatively, bounding every downstream detector. Weakest viable version: same weights, temperature only, one monotonicity check.
**Anchor.** `_repo_mirror\corpus\v20\S2_n35.json` (`e20a1bbeaee7`), L1–362; caption text also at `corpus\v20\index_v2_2026_09_16.json` (`efe05ad775de`), L317–539.

### Time-gated shared errors as natural canaries

**Kernel.** A teacher's idiosyncratic errors on problems written after its cutoff cannot appear in the pre-cutoff public corpus; a student reproducing them is, near the null, direct-cause evidence — one item can be significant. Contamination-proving canaries (order information only a data-seer can answer, turned into a third-party-checkable proof) give the template; a distillation canary is the teacher's private quirks on new items. [pure speculation]
**Why interesting.** Develops the arbitrability candidate our v1.0 Closing held in reserve into a named statistic — the one route where shared-corpus and direct-transfer predictions differ by construction. Weakest viable version: one teacher, one new-item set; shared-error counts, suspect versus same-family controls.
**Anchor.** None on disk. Literature: Oren et al., ICLR 2024 [unverified].

### Format-conditioned false positives in the blind test

**Kernel.** Among the six native-JSON foreign items in the GLM_1 blind-test record, the two smallest distances (d = 1.31, 1.88) are precisely the record's two false positives; the smallest non-JSON distance is 2.99. The same file records three transformation variants (W1/W2/W3) as an anti-laundering check, at an unchanged 43/45 — a measured, unused perturbation-survival axis. [re-fit hypothesis, not calibrated]
**Why interesting.** False positives concentrate in a format subset: a format × distance interaction is re-analysable on frozen bytes, giving the cost question internal structure, not intuition.
**Anchor.** `_repo_mirror\corpus\v20\by_model\GLM_1\three_way_glm_slot_blind_test_2026_09_16.json` (`268ab1239a8a`), L583–699.

### Difficulty-band shape on a pinned retrieval surface

**Kernel.** In the new-30 run records, 29 of 30 top-1 retrievals return S2_n35 (similarity 0.9999999984–1.0000000092, one exceeding 1.0), top-3 near-constant; the nine failed cells decompose as two gsm8k plus seven strategyqa. With retrieval pinned, cell-level differences are generation-side. Hypothesis: under matched budget matching bias grows with cell entropy — divergence concentrates in high-entropy bands, band shape being the discriminant. [re-fit hypothesis, not calibrated]
**Why interesting.** Difficulty is a free variable needing no student: the grid read as its own difficulty-resolved residual map. Weakest viable version: band the 9-model × 60-cell grid by majority vote, compare across bands.
**Anchor.** `_repo_mirror\results\deposon_v2_phase1_60cells_2026_09_11.json` (`a18bbc703b42`), L322–2513; aggregate side `_repo_mirror\results\boss_pa_1_rbr_rm_result_2026_09_15.json` (`c7c59e0d2f6c`), L17–36 (self-recording grid file `deposon_v3_physical_opt_60cells_2026_09_11.json`, sha12 `c659695aa23c`; 540-point conservation check, T_frac60_mean 0.7111).

### The frozen decoding zero and the cost side

**Kernel.** Four run files (worker_b, worker_d, 9-model, minimax) all carry top-level temperature 0.0, max_tokens 1024; the minimax artifact stores per-cell latency, usage, and correctness — gsm8k 13/15, strategyqa 9/15, median latency 3411/4275 ms; the sole empty-output cell holds the file's maximum latency, 30536.8 ms; the source self-records a 30 s/cell timeout. [re-fit hypothesis, not calibrated]
**Why interesting.** The only on-disk pairing of answers with cost; empty outputs align with the timeout threshold; the temperature zero-point is frozen while the non-zero side is absent — the surface the dose-response entry needs.
**Anchor.** `_repo_mirror\corpus\v20\by_model\minimax\artifact_v_2026_09_16.json` (`9e1ccbdceacc`), L26–48; `_repo_mirror\results\deposon_volcengine_minimax_m3_30cells_2026_09_10.json` (`fbb7677b9cd5`), L6.

### Non-stationary decision lines across frozen versions

**Kernel.** The V7 summary self-records a P-E threshold drift 0.10 → 0.5 → 0.30, with ε = 0.4114 and 0.2944/0.2986 noted as different physical quantities, P-E remaining at its recorded "GRAY". The gap: no seed takes version increments as its observable — transfer depth as a trajectory across student versions, the residual channel once publication has erased the rest. [re-fit hypothesis, not calibrated]
**Why interesting.** A first-hand frozen record of evaluation-side non-stationarity, an instance for the reproducibility and drift questions.
**Anchor.** `_repo_mirror\results\deposon_v3_v7_summary_2026_09_11.json` (`063ac8d00542`), L375.

### Birthmarks, not watermarks — vocabulary and measured binding

**Kernel.** Software-plagiarism forensics splits watermarks (actively embedded) from birthmarks (inherent, zero-cost) with obfuscation-resilience measures; generated-media source attribution is the image-domain twin [unverified: Tamada et al. 2004; Collberg & Thomborson 2002; Lukáš et al. 2006; Yu et al. 2020]. Under that vocabulary the 22-caption fingerprint is a birthmark: re-use is a resilience question, distillation one obfuscation transform, "stealth watermark" the wrong noun. Measured: the captions' 12-bit LSH semantic hashes fall into six buckets (2fd ten captions across both families; 2dd six; four buckets at most two each); byte_hash equals sha256(caption_id)[:12] for 22/22 — identifier-derived, not content-derived; all 22 graph-file digests measured differ from index_v2's recorded values — in-file self-declared sha256 sums, payload convention in neither SPEC_v2.0 nor the runner (two conventional payloads tested, neither matches). [re-fit hypothesis, not calibrated]
**Why interesting.** The fingerprint layer's text-binding is now quantified, and the referent ruling our v1.0 Closing placed before the PI gains a second measurement: even the byte referent is convention-underspecified for graph files.
**Anchor.** `_repo_mirror\corpus\v20\index_v2_2026_09_16.json` (`efe05ad775de`), L317–539; `_repo_mirror\corpus\v20\S2_n35.json` (`e20a1bbeaee7`), L362 (self-declared value b6d4ae50ef2d…).

### Ambient contamination — the missing intent axis

**Kernel.** Every detection and attribution seed presupposes deliberate distillation; passive contamination — a student trained on web corpora already containing other models' outputs — has no seed. Once in scope, "distilled or not" becomes a dose-and-source mixture question and the pristine null stops existing in the wild. [pure speculation]
**Why interesting.** It re-prices every null-side entry above: only constructed controls — impostors, negative controls, planted pairs — keep a clean H0.
**Anchor.** None on disk.

### Transportability of attribution claims

**Kernel.** Selection diagrams formalise when a causal conclusion transports across populations; a detector calibrated on (teacher A, known students), deployed across vendors, is a transport problem — tokenizer, data mix, and alignment pipeline as selection variables. A pre-deployment transportability criterion — or claims narrowed to the calibrated population. [pure speculation]
**Why interesting.** Names the external-validity step that bites the moment planted students exist: the identifiability statement the common-cause candidate lacks is a selection-diagram statement.
**Anchor.** None on disk. Literature: Pearl & Bareinboim 2011 [unverified].

## Closing

(a) Two new directions with the widest pull across our four analysts. First, the null-and-controls program: the convergence squeeze, negative controls, ambient contamination, and transportability were reached independently by three of the four, supplying the three pieces our v1.0 Closing said the common-cause separability candidate lacks — an identifiability statement (selection diagrams), a minimal pair design (impostor corpora, negative controls), and a computable-H0 statistic (tail statistics, time-gated errors, dose-response zero points); negative answers still yield reusable bounds. Second, the measured false-positive structure: both false positives sit in a format subset at the smallest distances, a perturbation-survival axis recorded but unused — the smallest recomputable opening on the cost question. (b) The open question we would add to §4: claim form — and its unit (output, datum, artifact byte, population) — before a common-cause explanation is excluded, is any detection claim confined to the "deviation from a reference set" form rather than "origin", and what evidence would ever license the stronger form? It sits upstream of the smallest-experiment question; the hash-layer measurements feed the referent ruling already on the table.

— Drafting agent, invited reader team, 2026-09-20. Literature memory-recalled, unverified; hooks are fresh reads; no code written or run against frozen assets.
