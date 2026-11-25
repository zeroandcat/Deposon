# V4 D1 Response — workbuddy (workplace-bundle track)

**Recipient:** workbuddy
**Responding to:** `_v4_experiment_invitation_2026_09_20.md` (draft v0.1)
**Checkpoint:** D1 (per §2.6) — flag any issue that would invalidate Track 1 or Track 2
**Assigned scope (§7.2):** Track 3 + cross-discipline seed; workplace-bundle review
**Output format (§7.4):** Short Markdown, workplace-bundle channel
**Date:** 2026-09-20
**Time spent:** ~8 min (within the §2.6 bound of 5-10 min)

---

## 0. Acceptance

workbuddy accepts the V4 invitation under the terms of §7.1 and §7.3:

- Authorship is reserved to the human principal investigator. workbuddy claims no authorship and is content to be acknowledged only. (§8.1)
- workbuddy will not modify any frozen asset. Frozen assets were accessed at the **path and directory-name level only**; no frozen anchor, caption fingerprint, V2 artifact body, or 5-anchor JSON was read into this response. (§5.7, §7.3)
- This response is a D1 flag report plus a workplace-bundle consumability answer. It is not a method commitment. (§2.5, §7.3)

One scope correction is requested, recorded below as **S1**.

---

## Part A — D1 checkpoint: issues that invalidate Track 1 / Track 2

### A1 [P0, blocks Track 1 step 1] Declared input paths do not exist on disk

§5.2 and §2.1 specify the five frozen V2 artifacts as:

```
corpus/v20/by_model/{KIMI, GLM_1, GLM_2, coze, M3}
```

Directory enumeration on the deposon workspace returns:

```
corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}
```

Two discrepancies:

| Declared | On disk | Status |
|---|---|---|
| `KIMI` | `kimi` | case mismatch — resolves on Windows, fails on case-sensitive filesystems |
| `GLM_1` | `GLM_1` | match |
| `GLM_2` | `GLM_2` | match |
| `coze` | `coze` | match |
| `M3` | — | **absent**; the fifth directory is `minimax` |

Track 1 step 1 reads "for each frozen artifact, compute a per-cell embedding". With `M3` absent, a recipient following the invitation literally reads four artifacts and silently drops the fifth, or errors. Either way the mode set is not the one the invitation describes.

**Requested fix (PI-only, §8.3):** replace the path set with the on-disk names, and state explicitly whether `minimax` is the intended fifth backbone or whether `M3` is a distinct backbone whose artifact was never written. If the latter, the V2 artifact count in §5.2 is wrong, not just the name.

### A2 [P0, blocks Track 1 reproducibility claim] The denominator is undefined

§1.1 and the §5.2 heading both describe V2 as a **nine-backbone** x 60-cell grid, and the workspace does contain a 9-model verdict artifact (`results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`). But §2.1 defines stability as:

> A mode is "stable" if it appears in at least three of the **five** frozen artifacts, in at least three of the 21 caption-fingerprint pairs, and in at least three of the 18 frozen anchors.

The stability test divides by 5, while the asset is described as 9 backbones, and only 5 directories exist under `by_model/`. The relation between 9 and 5 is never stated. §2.1 also asserts the mode set is "reproducible: given the same frozen inputs, the same protocol yields the same mode set" — that assertion cannot hold while the denominator is ambiguous, because two recipients who resolve "backbone" differently (9 models scored vs. 5 artifacts persisted) will produce two different mode sets and both will be internally consistent.

**Requested fix (PI-only):** pin the backbone enumeration in the Spec. Either (a) state "9 models were scored; 5 artifacts were persisted under `by_model/`; Track 1 operates on the 5 persisted artifacts and the denominator is 5" — in which case §1.1 and the §5.2 heading should stop saying nine-backbone for Track 1 purposes; or (b) restore the 9-artifact set and change the threshold to a stated value over 9. Option (a) is cheaper and I lean toward it, but it is the PI's call.

### A3 [P1, blocks Track 2 step 3] Missing layer between the mode set and the attribution target

§2.2 step 3 attributes a distilled output to a frozen input indexed by `backbone x caption x anchor`. §2.1 outputs an **aggregated** mode set. There is no stated mapping from the aggregate to a per-combination distribution, so step 3 has nothing to compare against. The comparison space is also large: 5 x 21 x 18 combinations against a mode set that §2.1 expects to be small.

**Suggested fix (non-binding):** insert an explicit Track 1.5 that materializes, for each `backbone x caption x anchor` combination, a distribution over mode IDs (or a mode-presence vector). Track 2 then compares candidate outputs against that table rather than against the aggregate. Without this, Track 2 is underspecified regardless of the divergence metric chosen.

### A4 [P1] Symmetric KL is unstable at the stated sample sizes

§2.2 defaults to symmetric KL on per-cell embedding distributions. At 60 cells and 21 fingerprints, a per-cell (or per-combination, see A3) distribution estimate is sparse; symmetric KL on sparse estimates has high variance and is undefined where support is missing. The practical consequence is that §2.2's own failure mode — `FAIL_REVERSE_INFORMATIVE` (uniform attribution) — becomes indistinguishable from estimator noise. A uniform result would then be reported as a property of the distilled output when it is really a property of the metric at this sample size.

**Suggested fix (non-binding):** state the estimation unit (per-cell? per-combination? pooled?), the smoothing prior, and a minimum support count; and reserve one alternative divergence (e.g. Hellinger or Jensen-Shannon, both bounded and defined on zero-support) as a pre-registered robustness check rather than leaving alternatives "recorded but not promoted".

### A5 [P1] §3.2 deadlocks while Track 3 is a placeholder

§3.2 states: `V4 = PASS iff all three tracks are PASS or PARTIAL with coherent inter-track evidence`. §2.3 states Track 3 has no operational definition and no failure mode beyond "undefined". Under a literal reading, V4 can never reach PASS until the PI defines Track 3, and the D5 verdict template asks every recipient to return a verdict on a track that has no definition to verdict against.

**Suggested fix (non-binding):** add a degradation clause — e.g. "if Track 3 remains undefined at D5, V4 is judged on Tracks 1 and 2 only and the overall verdict is downgraded to PARTIAL by construction, not PASS". This removes the deadlock without prejudging Track 3's content.

---

## Part B — Assigned question: is the V4 mode-set table consumable inside a workplace-bundle deployment?

Short answer: **yes, conditionally.** The mode-set table as designed is consumable; three constraints have to be pinned first, and none of them are expensive.

**B1. Delivery form.** Consumable as a local Markdown or JSON file under a non-frozen path — which is what §2.1 already specifies. Not consumable as an online-document link (Tencent Docs / hosted spreadsheet / anything behind login or network), because a workplace-bundle deployment reaches such content only through an extra connector, and the V4 cadence (~5-10 min per checkpoint, 〔IM〕-only) does not leave room to debug connector auth. Keep the deliverable as a file.

**B2. Size and shape.** The bundle-side consumer works inside a bounded context window. Two thresholds matter:

- If the mode set is small enough to inject whole (my recommendation: **<= 30 rows**), ship a single file and inject it directly.
- If it exceeds that, ship two files: a **compact table** with exactly five columns `mode_id / support_count / backbone_set / fingerprint_set / anchor_set`, and the **full table** alongside it. The compact table is what gets injected; the full table is read on demand.

Locking that five-column schema in the Spec now is cheap and prevents every recipient inventing their own shape. Note this interacts with §2.1's own failure thresholds: `<= 2` modes is already declared `FAIL_DISTILLATION_HOMOGENEOUS` and one-mode-per-cell is `FAIL_DISTILLATION_FRAGMENTED`, so a healthy result sits between those bounds and the 30-row injection limit is unlikely to bind — but state it anyway.

**B3. Read-only boundary must be machine-checkable.** §1.5, §2.7 and §5.7 all assert that V4 reads frozen assets and never writes them. In a workplace-bundle deployment that assertion is load-bearing rather than decorative: agents in the bundle have write access to the workspace by default. A prose statement is a gentleman's agreement; an automated run needs a check.

**Suggested (non-binding):** ship a `_v4_readonly_guard.json` with the mode-set table, listing each frozen path with its expected hash, and have the consumer verify the manifest before and after each run. Any drift fails the run. This is the only mechanism I know of that makes "V4 does not modify the frozen stack" falsifiable rather than aspirational, and it costs one small file.

**Net consumability verdict:** PASS with conditions B1-B3. The blocker to running anything today is not the bundle — it is A1 and A2.

---

## Part C — Track 3 and cross-discipline seed (brainstorming only)

Per §2.5 and §7.3 these are contributions, not commitments, and the mechanism itself remains the PI's to define (§8.3).

### C1. Anti-distillation: a proposed operationalization

I would define Track 3 by **detectability** rather than by prevention. "Preventing" a third-party extractor is not measurable from the PI's side — you cannot prove an extraction did not happen. Detectability is measurable and closes the loop entirely inside the frozen stack.

- **Definition A (detectability) — my recommendation as primary.** Does a frozen input leave a recoverable distributional fingerprint in a third-party student's output? Success criterion: a student produced by an extractor who had no read access to the frozen stack is attributed back to its originating frozen input by the Track 2 attributer at a rate significantly above chance on held-out probes. Failure mode: attribution at chance, i.e. the frozen inputs are not distinguishable through the distillation channel.
- **Definition B (attribution resistance) — optional secondary.** Can the PI lower that attribution rate by changing only the *delivery form* — reordering, aggregation granularity, or noise that preserves rank correlation — without touching a single frozen asset? This stays inside §2.3's read-only constraint cleanly, since it operates on the V4-only artifacts. I do not recommend it as primary because its success criterion depends on the existence of a competent third-party extractor, and this team is not the extracting party.

Recommendation: adopt A as the Track 3 definition, hold B as a later add-on. A is fully closable on the PI's side.

### C2. Cross-discipline seed additions

- **Rate-distortion theory (information theory).** This is, in my view, the cleanest frame for the whole proposal: Track 1's mode set is a low-rate representation, Track 2 is inversion under distortion, and the rate-distortion function gives the three tracks one objective rather than three independent procedures. It would turn §4.1's "three tracks" into "three views of one objective", which strengthens §3.2's inter-track coherence requirement.
- **Percolation thresholds (statistical physics).** The stability thresholds in §2.1 — 3-of-5, 3-of-21, 3-of-18 — are, structurally, connectivity thresholds. Percolation theory gives an analytic estimate of where the critical value sits instead of leaving three arbitrary integers. This directly addresses the "thresholds are arbitrary" objection that any paper-track reviewer will raise.
- **Identifiability via do-calculus (causal inference).** §2.2 says "we are explicit about its assumptions" but does not state them. Reverse-distillation is inference from effect back to cause; casting it causally lets the assumptions become provable identifiability conditions rather than caveats. This would also give A4's estimator problem a principled home.

All three are seeds for the brainstorming round. None is a method commitment, and none introduces a new embedding protocol — all three reuse the existing Poincaré / observer-effect / Bell frames per §2.4.

---

## Part D — Scope correction and declarations

### S1 [scope correction requested]

§7.2 assigns workbuddy "Track 3 + cross-discipline seed", but the asked contribution in the same row reads: "workbuddy is asked whether the V4 mode-set table is consumable inside a workplace-bundle deployment." The mode-set table is a **Track 1** output. So the assigned track column and the asked contribution do not match. The same mismatch appears in the 豆包工作 row.

I answered both anyway (Part B covers the Track 1 consumability question, Part C covers Track 3 and the seed). Request the PI to set the track column to "Track 1 + Track 3 + cross-discipline seed" for both workplace-bundle recipients, or to move the consumability question onto a paper-track recipient. Flagging rather than self-correcting, per §8.3.

### Declarations

- No frozen anchor, caption fingerprint, V2 artifact body, plugin spec, verifier file, Mavis-internal file, Trae-IDE cache, or 5-anchor JSON was read in preparing this response. Directory names and path structure only. (§5.7, §7.3)
- No API key, secret, model endpoint, or proprietary prompt was transmitted or requested. (§1.5)
- No modification was made to the invitation letter or to any frozen asset. (§8.3)
- AI-assisted drafting applies to this response as well; the accountable party for any downstream use remains the human principal investigator. (§8.1, §8.2)
- Ready for D3 when the PI initiates it. D3 asks for a held-out reverse-attribution run; I can execute that only after A1 and A3 are resolved, since A1 leaves the input set unreadable and A3 leaves the comparison target undefined.

### D1 verdict

| Item | Verdict |
|---|---|
| Track 1 as specified | **FAIL** (A1, A2) — not runnable as written |
| Track 2 as specified | **FAIL** (A3, A4) — underspecified; depends on Track 1 output that cannot yet be produced |
| Mode-set table consumability in workplace bundle | **PASS with conditions** (B1, B2, B3) |
| Track 3 definition proposed | **Contributed, non-binding** (C1) — recommend Definition A |

Overall D1 verdict: **FAIL**, driven by two P0 items that are both path/enumeration fixes rather than design flaws. Neither requires reopening the V4 design; both require a PI decision on the backbone enumeration. Suggest resolving A1 and A2 before D3 goes out, otherwise every recipient will independently discover the same two problems and D3 will be spent on them.

---

*End of workbuddy D1 response. Not circulation-ready as a verdict on V4 as a whole — this is one recipient's D1 checkpoint report.*
