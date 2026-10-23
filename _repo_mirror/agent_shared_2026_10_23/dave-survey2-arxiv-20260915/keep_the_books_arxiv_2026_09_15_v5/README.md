# Keep the Books — arXiv Source Package (v5 Rewrite-Level Candidate, 2026-09-15)

**Work**: second work, single-author survey in English (open-signature arXiv submission)
**Date**: 2026-09-15
**arXiv classes**: cs.CL (primary) / cs.AI / cs.LG
**Author**: Qihao Yuan (single author) — arXiv-style open signature; license statement CC BY 4.0; conflicts: none declared.

## Contents

- `keep_the_books_survey.tex` — the complete English manuscript (article class, inline `thebibliography` of 61 entries; no external .bib, figures, or data files).
- `README.md` — this file. No build products are shipped in the package; the compiled verification PDF (30 pages) is delivered alongside the group message, not inside the archive.

## Content baseline

- **Source of record (content chain head)**: `查理_第二作综述英文重写版_2026-09-15.md` (13,070 words, 61 references, 10 tables; sha256 prefix `3da418383ca37dd2`), a full native-level English rewrite of the P1-revised manuscript, independently re-verified all-PASS (five checkpoints, zero revision items; 2026-09-15 18:33).
- **Relation to v4**: v5 is a parallel arXiv candidate, not a replacement. Invariants are byte-carried from the v4 tex: the 61-entry reference list, all ten tables (75 table rows), FN1/FN2 footnote definitions, and the §9.3 anchored paragraphs (self-stated limitations with the five SHA-256 preregistration anchors, Matrix row 6, the closing red-line paragraph) are byte-identical to the v4 baseline, except the one declared punctuation change in "Position and disclosure" (colon → period) and the two declared definition-syntax changes (the three-tier evidence definitions in the head conventions block; the rule-three sentence in §1.3). All remaining differences are confined to the free-prose regions of the rewrite (abstract, §1–§8 body, §9.1–9.2, §10, back matter).
- **Frozen number group**: the §9.3 numeric tokens (138 tokens) are identical as a multiset to the v4 baseline; the five preregistration anchors (aeefb8ef6972 / 9bbe43f41fa8 / 6e9673205dc0 / 68a5b08ef007 / 6b09de9911c0) and the anchor [4] → arXiv:2609.09001 are unchanged.
- Self-overlap vs. the author's first paper (arXiv:2609.09001), 10-gram word-level, recomputed under the v4 protocol: §9.3 4.63%, remainder of the survey 0.21% — within the disclosed envelope; matched fragments are the declared anchored material plus two shared reference titles.

## Status and conventions

- **Parallel candidate (user to choose)**: the v4 packaging baseline (12,903-word source, 29 pages) is unchanged and remains released; this v5 package (13,070-word rewrite-level source, 30 pages) is the alternative candidate for the KIMI strict double review. The user selects which version is submitted.
- **Compilation**: tectonic (XeTeX, DejaVu Serif) → 30 pages; four-zero metrics green: 0 errors, 0 Overfull boxes, 0 missing characters, 0 undefined citations (Underfull boxes are spacing hints, same convention as v4).
- **User-decided conventions in force**: the AI-use disclosure stays generic (no tool name; naming, if later decided, triggers a one-clause re-typeset and re-package); no GitHub repository citation (default: none; the Availability section carries no URL sentence); [4] is anchored to arXiv:2609.09001.

**Verification artifacts** (pipeline and re-verification scripts, internal): `agents/6a962cc259312f271f3f1e75/v5_retypeset/` (md2tex_v5.py, verify_v5_part1.py, verify_v5_part2.py).
