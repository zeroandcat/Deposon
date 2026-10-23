# Keep the Books — arXiv Source Package (v7 Final Delivery, 2026-09-16)

**Work**: second work, single-author survey in English (open-signature arXiv submission)
**Date**: 2026-09-16
**arXiv classes**: cs.CL (primary) / cs.AI / cs.LG
**Author**: Qihao Yuan (single author) — arXiv-style open signature; license statement CC BY 4.0; conflicts: none declared.

## Contents

- `keep_the_books_survey.tex` — the complete English manuscript (article class, inline `thebibliography` of 61 entries; no external .bib, figures, or data files).
- `README.md` — this file. No build products are shipped in the archive; the compiled verification PDF (30 pages) is delivered alongside the group message, not inside the tarball.

## Content baseline

- **Source of record (content chain head)**: `查理_第二作综述措辞对齐版_2026-09-16.md` (13,206 words by `wc -w`, 486 lines, 61 references, 10 tables; sha256 prefix `e8933ebce0c0`). This md is the wording-alignment head over the v6 fix head: exactly five wording-level replacements (§1.1 "lives in"→"sits in"; §5.2 "and that is a feature"→"and the negative content carries equal weight"; §7.2 "candidly,"→"stated as-is"; §9.2(d) "audit-grade response"→"honest response"; §10.1 "this is the binding ③ of the next decade"→"the projected binding ③ of the coming decade"), aligning free-running prose to the first work's register anchors. All declared invariants carry over unchanged: the 262 `[n]/[n–m]` citation tokens match token-by-token in order and multiset; the References block, FN1/FN2, the GLM AI-use disclosure, and the §9.3 frozen anchors (five SHA-256 pre-registration anchors and the frozen numbers) are byte-identical; 61 references each first-cited in strict 1→61 order of first appearance; [4] anchored to arXiv:2609.09001.
- **Relation to v4/v5/v6**: parallel final candidate, not a replacement; the v4/v5/v6 packaging baselines are unchanged and remain released. This v7 package is the final delivery per the standing instruction (no further review round).

## Typographic baseline

- Same pipeline as v6 (`md2tex` conventions, source = the 2026-09-16 wording-alignment md, full re-typeset; footnote machinery, typography rules, and table anti-overflow patches unchanged).
- **Compilation**: tectonic (XeTeX, DejaVu Serif) → 30 pages; four-zero metrics green: 0 errors, 0 Overfull boxes, 0 missing characters, 0 undefined citations (this final pass also logged 0 Underfull boxes; Underfull boxes are spacing hints under the v4/v5/v6 convention in any case).
- **Page-level glyph check**: `τ∗` (U+2217 asterisk operator) renders visibly at all three §9.3 occurrences in the PDF text layer. Under `natbib` sort&compress, the `\cite{key48,key49,key50}` cluster renders as the compressed range `[48–50]` at all six occurrences (§7.2, Table 3 rows ①/⑤/L4, §9.2c, OP3) with `[51]` standing separately, never merged into the range. Table 2 carries no legend row (the tier-letter legend lives in §3.2 body text).

## Counting calibers (carried over, refreshed against the v7 chain head)

- **Table rows**: 65 rows including header rows (55 data rows) across the 10 tables, counted as rows terminated by `\\` inside each `tabularx` environment (header rows counted once per table) — re-counted on the v7 tex, unchanged from v6 (no table content touched).
- **§9.3 numeric tokens**: 134, counted as `re.findall(r'\d[\d,\.]*', §9.3 source text)` in the content-chain-head md — re-counted on the v7 chain head, unchanged (§9.3 untouched by the wording pass). Counts of this kind are caliber-dependent; the caliber is stated here so the number is reproducible.

## Self-overlap disclosure (refreshed after re-typeset)

A 10-gram word-level overlap check against the first work (arXiv:2609.09001) measures **4.62% within §9.3** (60 matched words / 1,298 §9.3 words; same numerator and denominator as v6 — none of the five wording replacements falls in §9.3) and **0.21% across the remainder**; 8-gram whole-document coverage **0.91%** (127 matched words, match set identical to v6's). Matched fragments are the declared anchored material plus two shared reference titles. The manuscript's Availability sentence carries the 4.62%/0.21% figures (single one-token difference from the md chain head's 4.63%, declared in the re-typeset note).

## Conventions in force

- The AI-use disclosure names the drafting model (GLM); no GitHub repository citation (default: none; the Availability section carries no URL sentence); [4] is anchored to arXiv:2609.09001.

**Verification artifacts** (pipeline and re-verification scripts, internal): `agents/6a962cc259312f271f3f1e75/v7_retypeset/` (md2tex_v7.py, overlap_check_v7.py, token_check.py, compile logs, v6_v7 diffs).
