# Keep the Books — arXiv Source Package (v4 Final, 2026-09-15)

**Work**: second work, single-author survey in English (open-signature arXiv submission)
**Date**: 2026-09-15
**arXiv classes**: cs.CL (primary) / cs.AI / cs.LG
**Author**: Qihao Yuan (single author) — arXiv-style open signature; license statement CC BY 4.0; conflicts: none declared.

## Contents

- `keep_the_books_survey.tex` — the complete English manuscript (article class, inline `thebibliography` of 61 entries; no external .bib, figures, or data files).
- `README.md` — this file. No build products are shipped in the package; the compiled verification PDF (29 pages) is delivered alongside the group message, not inside the archive.

## Content baseline

- **Source of record (content chain head)**: `查理_第二作综述P1修复版_2026-09-15.md` (12,903 words, 61 references, 10 tables; sha256 prefix `bca87448991193f7`). The Chinese-language process documents in the working directory are internal review artifacts only and are not part of the submission.
- **v4 = v3 tex + one-clause sync**: in §9.3 "Limitations, self-stated (compressed from [4])", the third sub-clause was replaced (P1 fix, back-filled from the first paper's self-stated limitation) — old "the claims are at the structural-isomorphism level, not magnitude claims" → new "apart from the closed verdicts and the kills, the game-theoretic positive evidence is consistency evidence, not formal proof". **Every other byte of the tex is unchanged** (line-level check: 1 changed line out of 557; the only in-line changed span is that sub-clause).
- **Typesetting baseline**: third-round re-typesetting pipeline (md2tex_v3, table overflow-avoidance patches inlined, FN1/FN2 realized as \footnote). v4 did not re-run the pipeline; the single clause was synced by hand.

## Build

Engine of record: tectonic 0.15.0 (XeTeX, DejaVu Serif primary font):

```bash
tectonic -X compile keep_the_books_survey.tex   # produces the 29-page PDF
```

## Verification (2026-09-15, fourth-round re-verification)

- Compile: **0 errors / 0 Overfull boxes / 0 missing glyphs / 0 undefined citations**; 29 pages (page count identical to v3).
- Citation integrity: 61 entries, all cited in the body; first-appearance sequence strictly monotonic 1→61 under the main-text-flow convention (footnote-body mention tokens are disclosed entry references).
- Footnotes FN1/FN2 in place; the P1 replacement clause present in both tex and rendered PDF; the retired clause "structural-isomorphism" has zero occurrences in tex and PDF.
- Self-overlap vs. the author's first paper (arXiv:2609.09001), 10-gram word-level: §9.3 4.63%, remainder of the survey 0.21% — within the disclosed envelope.

## Status and conventions

- **Final submission package (packaging released)**: independent double review concluded all-PASS (2026-09-15 17:20); this tar.gz was packaged the same day from the v4 tex plus this README. The obsolete 13:33 55-reference package has been quarantined under `_obsolete/`.
- **User-decided conventions in force**: the AI-use disclosure stays generic (no tool name; naming, if later decided, triggers a one-clause re-typeset and re-package); no GitHub repository citation (default: none; the Availability section carries no URL sentence); [4] is anchored to arXiv:2609.09001.

**Verification artifacts** (pipeline and re-verification scripts, internal): `agents/6a962cc259312f271f3f1e75/` (md2tex_v3.py, verify scripts, v4_recompile/).
