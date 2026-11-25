# V4 D1 Reviewer Response - Codex

**Role:** invited design reviewer and brainstorming contributor  
**Status:** preliminary D1 review; nonbinding recommendations  
**Scope:** invitation draft v0.1 only. No frozen V1-V3 asset was read or modified.

## Acceptance and current verdict

I accept the invitation for experimental-design review, reproducibility review, and Track 3 / cross-discipline brainstorming. At D1, I cannot assign PASS, FAIL, PARTIAL, or GRAY to the experimental tracks because the invitation supplies a high-level protocol but not the frozen manifests, executable embedding specification, or candidate outputs. The current design status is **incomplete for execution**.

## Track 1: distillation

1. "Intersection of high-density regions" is not reproducible until the density estimator, bandwidth or smoothing rule, geometric reference measure, mode-matching rule, and minimum support are fixed. The thresholds of three artifacts, three caption-fingerprint pairs, and three anchors also need a declared sampling unit; the document names five artifact paths while describing a nine-backbone grid.
2. The development/evaluation boundary is unspecified. Caption pairs, anchors, and cells that share lineage must be grouped before splitting. Mode fitting, smoothing, and any thresholds must use development groups only; held-out groups must remain untouched until evaluation.
3. A mode count of <=2 or one mode per cell is a useful diagnostic, but it is not by itself evidence of homogeneity or heterogeneity. Add resampling stability and uncertainty before assigning those failure labels.

## Track 2: reverse-distillation

1. The attribution target is not yet identifiable. Track 1 retains shared modes, while Track 2 needs source-specific signal. Preserve source-conditioned mode frequencies and define one pilot candidate type (for example, a mode-set report) with a known generating source.
2. Symmetric KL cannot be applied directly to embedding vectors. Define fixed development-derived bins or modes, an unmatched category, smoothing, and the exact symmetric-KL convention. Report sensitivity to the smoothing value.
3. Add majority-prior and raw-embedding nearest-source baselines, dependency-preserving label permutations, source counts, balanced accuracy, confusion, abstention coverage, and group-level uncertainty. A uniform attribution should be reported as uninformative only relative to these baselines.

## Suggested Track 3 definition (for PI consideration)

Use a black-box extractor threat model: an extractor sees only a V4 release, has a preregistered query budget, and cannot read the frozen files, manifests, secrets, or proprietary prompts. The V4 defense is a separate release policy over derived summaries; it does not alter frozen assets. Evaluate each policy at fixed query budgets.

- **Utility:** the released summary reproduces the intended stable modes on held-out groups within a preregistered tolerance.
- **Resistance:** source attribution and mode reconstruction by the extractor remain at or near dependency-preserving chance on held-out groups.
- **Cost:** report summary size, query count, and utility loss. Include an explicit abstention outcome when no policy meets both utility and resistance bounds.

Suggested Track 3 verdicts: PASS when both utility and resistance bounds hold at all registered budgets; PARTIAL when they hold only for a declared subset; FAIL when resistance requires unacceptable utility loss; GRAY when the held-out sample is insufficient or bounds are inconclusive. This is a proposal, not a commitment or a request to modify frozen inputs.

## Cross-discipline seed list

- **Information theory:** measure retained information about source identity versus retained task utility.
- **Geometry:** test whether mode stability persists under the already-approved Poincare distance, with no new embedding protocol.
- **Measurement theory:** vary observation/query selection under the existing observer-effect frame and record whether the release policy changes the measured distribution.

## D1 action items

- Confirm the actual frozen inventory and artifact-to-backbone-to-cell mapping.
- Register the Track 1 density/matching specification and dependency-aware split.
- Choose one Track 2 candidate type, source labels, baselines, and abstention rule.
- Verify all SHA-12 placeholders against the V3 final R5 manifest before circulation.
- Have the principal investigator approve or replace the Track 3 proposal before D3.

