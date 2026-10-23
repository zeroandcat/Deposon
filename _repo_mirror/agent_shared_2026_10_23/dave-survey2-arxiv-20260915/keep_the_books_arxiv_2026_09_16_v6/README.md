# Keep the Books — arXiv Source Package (v6 Post-Fix Candidate, 2026-09-16)

**Work**: second work, single-author survey in English (open-signature arXiv submission)
**Date**: 2026-09-16
**arXiv classes**: cs.CL (primary) / cs.AI / cs.LG
**Author**: Qihao Yuan (single author) — arXiv-style open signature; license statement CC BY 4.0; conflicts: none declared.

## Contents

- `keep_the_books_survey.tex` — the complete English manuscript (article class, inline `thebibliography` of 61 entries; no external .bib, figures, or data files).
- `README.md` — this file. No build products are shipped in the archive; the compiled verification PDF (30 pages) is delivered alongside the group message, not inside the tarball.

## Content baseline

- **Source of record (content chain head)**: `查理_第二作综述收口修复版_2026-09-16.md` (13,204 words by `wc -w`, 487 lines, 61 references, 10 tables; sha256 prefix `74bba2fc8bb6`). This md is the post-dual-review fix head: it folds the 21 P1 replacements and the 16 stage-2 replacements (reference-field corrections for [39][43][44][48][49][51][54], GLM-named AI-use disclosure, Table 2 legend-row removal, the four [48–50] cluster splits, and the §7.2/§7.3 rewrites) into the v5 rewrite-level source. All declared invariants carry over: 61 references each first-cited in strict 1→61 order of first appearance; FN1/FN2 in place; §9.3 frozen anchors byte-identical (five SHA-256 pre-registration anchors); three-tier evidence wording self-consistent; [4] anchored to arXiv:2609.09001.
- **Relation to v4/v5**: parallel candidate, not a replacement. The v4 (12,903-word, 29 pages) and v5 (13,070-word, 30 pages) packaging baselines are unchanged and remain released. This v6 package is the post-dual-review candidate for the KIMI re-review.

## Typographic baseline

- Same pipeline as v5 (`md2tex_v3` → `md2tex_v5` conventions, source = the 2026-09-16 fix-head md, full re-typeset; footnote machinery, typography rules, and table anti-overflow patches unchanged).
- **Compilation**: tectonic (XeTeX, DejaVu Serif) → 30 pages; four-zero metrics green: 0 errors, 0 Overfull boxes, 0 missing characters, 0 undefined citations (Underfull boxes are spacing hints, 15 in the final pass, same convention as v4/v5).
- **Page-level glyph check**: `τ∗` (U+2217 asterisk operator) renders visibly at all three §9.3 occurrences in the PDF text layer (per-state self-chosen τ∗ / median per-state τ∗ is 0 / choose τ∗=0); the v5 `τ\textit{...}` italic-eating bug is gone. Under `natbib` sort&compress, every cluster citation `\cite{key48,key49,key50}` renders as the compressed range `[48–50]` (six occurrences in the PDF: §7.2, Table 3 rows ①/⑤/L4, §9.2c, OP3) with `[51]` standing separately (twice: §7.2 and §7.3 "out of scope [51]"), never merged into the range.

## Counting calibers (README-side fix, per the dual-review verdict)

The v5 README's "75 table rows / 138 §9.3 numeric tokens" figures used an unspecified caliber and were not reproducible by the reviewers. This README fixes the caliber instead of touching the manuscript:

- **Table rows**: 65 rows including header rows (55 data rows) across the 10 tables, counted as rows terminated by `\\` inside each `tabularx` environment (header rows counted once per table).
- **§9.3 numeric tokens**: 134, counted as `re.findall(r'\d[\d,\.]*', §9.3 source text)` in the content-chain-head md (numeric substrings including SHA-16 anchor digits, ranges, and decimal points; scientific-notation merges would give 136). Counts of this kind are caliber-dependent; the caliber is stated here so the number is reproducible.

## Self-overlap disclosure (refreshed after re-typeset)

A 10-gram word-level overlap check against the first work (arXiv:2609.09001) measures **4.62% within §9.3** (60 matched words / 1,298 §9.3 words — the same 60-word numerator as v4/v5; the denominator moved by +1 word through the §9.3 wording fixes, which shifts the rounded percentage from 4.63% to 4.62%) and **0.21% across the remainder**; 8-gram whole-document coverage 0.91%. Matched fragments are the declared anchored material plus two shared reference titles. The manuscript's Availability sentence carries the refreshed 4.62%/0.21% figures (single one-token difference from the md chain head, declared in the re-typeset note).

## Conventions in force

- The AI-use disclosure names the drafting model (GLM); no GitHub repository citation (default: none; the Availability section carries no URL sentence); [4] is anchored to arXiv:2609.09001.

**Verification artifacts** (pipeline and re-verification scripts, internal): `agents/6a962cc259312f271f3f1e75/v6_retypeset/` (md2tex_v6.py, overlap_check_v6.py, compile logs, v5_v6.diff).
