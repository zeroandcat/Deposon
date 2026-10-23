# Keep the Books — arXiv Source Package (v9 abstract-synced, 2026-09-16)

**Work**: second work, single-author survey in English (open-signature arXiv submission)
**Date**: 2026-09-16
**arXiv classes**: cs.AI (primary) / cs.LG / cs.CL
**Author**: Qihao Yuan (single author) — arXiv-style open signature; license statement CC BY 4.0; conflicts: none declared.

## Purpose of this package (v9)

v9 syncs the arXiv-compliant abstract into the manuscript (submission 8086112, Metadata step rejected the previous abstract: 2,677 characters over the 1,920 limit plus 5 illegal dash characters). The new abstract (1,844 characters / 243 words, pure ASCII, no macro or escaping needed) was delivered by the lead author as `查理_第二作综述摘要_arXiv合规版_2026-09-16.txt` and is used **identically** as the PDF abstract and the arXiv form abstract. **The manuscript is otherwise byte-identical to v8** except for this single abstract paragraph: the tex diff v8→v9 is exactly one line. No wording, reference, number, or frozen-anchor change of any kind.

## Contents

- `keep_the_books_survey.tex` — the complete English manuscript (article class, inline `thebibliography` of 61 entries; pure pdflatex, no external .bib, figures, data files, or font files).
- `README.md` — this file. No build products inside the tarball; the compiled verification PDF (25 pages) is delivered alongside the group message.

## Content baseline (unchanged from v7/v8)

- **Source of record (content chain head)**: `查理_第二作综述措辞对齐版_2026-09-16.md` (13,206 words by `wc -w`, 486 lines, 61 references, 10 tables; sha256 prefix `e8933ebce0c0`), as carried by v7/v8. All declared invariants carry over unchanged: citation tokens in order and multiset; References block, FN1/FN2, GLM AI-use disclosure, and §9.3 frozen anchors byte-identical (tex outside the abstract is byte-identical to v8); 61 references first-cited in strict 1→61 order; [4] anchored to arXiv:2609.09001. The self-overlap disclosure numbers are unchanged (content outside the abstract untouched): 4.62% within §9.3 (60/1,298), 0.21% across the remainder, 8-gram 0.91% (127 words).
- **New abstract compliance**: 1,844 characters incl. spaces (arXiv hard limit 1,920; 76 headroom), 243 words, pure ASCII (0 illegal characters), script-counted not eyeballed. Content preserves the keep-the-books axis claim, one sentence per research line, all six contributions (i)–(vi), and the closing self-citation / parity-discipline sentence.

## Typographic baseline (v9)

- **Engine layer**: unchanged from v8 — `pdflatex`-only, T1 `fontenc` + `utf8` `inputenc` + `lmodern` + `pifont` circled digits via `\ding{172}`–`\ding{177}` + `newunicodechar` mappings. The new abstract is plain ASCII and needs no macro layer.
- **Compilation (verification)**: local `pdflatex` (TeX Live 2026; TL2025 local install not feasible for network reasons, disclosed in the v8/v9 notes) → three passes, all exit 0; 25 pages; four-zero metrics green: 0 errors, 0 Overfull boxes, 0 missing characters, 0 undefined citations (Underfull boxes are spacing hints, 4 on the final pass, same as v8).
- **Page count**: 25 pages vs. v8's 26 — the shorter abstract pulls the text back by one page; an expected abstract-layer effect, not a content change.
- **Fonts**: all embedded (subset) — Latin Modern family + URW Dingbats (`pdffonts`: every row emb=yes).
- **Rendering check**: `pdftotext` confirms the new abstract head/tail and Keywords line on page 1 and zero residual fragments of the old abstract (all four probe strings absent).

## Counting calibers (carried over from v7/v8, body untouched)

- **Table rows**: 65 rows including header rows (55 data rows) across the 10 tables.
- **§9.3 numeric tokens**: 134 (`re.findall(r'\d[\d,\.]*', §9.3 source)`).

## Conventions in force

- The AI-use disclosure names the drafting model (GLM); no GitHub repository citation; the Availability section carries no URL sentence; [4] is anchored to arXiv:2609.09001.

**Verification artifacts** (internal): `agents/6a962cc259312f271f3f1e75/v9_retypeset/` (make_v9.py, compile logs pass1–3, v9_pdf.txt).
