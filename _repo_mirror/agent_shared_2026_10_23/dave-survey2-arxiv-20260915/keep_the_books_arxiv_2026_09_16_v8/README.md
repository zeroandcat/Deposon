# Keep the Books — arXiv Source Package (v8 pdflatex-Fixed, 2026-09-16)

**Work**: second work, single-author survey in English (open-signature arXiv submission)
**Date**: 2026-09-16
**arXiv classes**: cs.AI (primary) / cs.LG / cs.CL
**Author**: Qihao Yuan (single author) — arXiv-style open signature; license statement CC BY 4.0; conflicts: none declared.

## Purpose of this package (v8)

v8 repairs the failed arXiv submission of v7 (submission 8086112): the v7 source required XeTeX/LuaTeX via `fontspec` + system fonts (DejaVu Serif/Sans), which is fatal under arXiv's automatic `pdflatex`. v8 is a **pure pdflatex package**: the engine-compatibility layer (T1 `fontenc` + `utf8` `inputenc` + `lmodern` + `pifont` Zapf Dingbats circled digits + `newunicodechar` mappings for the remaining non-ASCII glyphs) replaces the fontspec layer. **The manuscript body is byte-identical to v7** except for one line: the arXiv subjects line now reads cs.AI (primary) · cs.LG · cs.CL, reflecting the corrected classification (cs.AI primary; no cs.CL endorsement for this author). No wording, reference, number, or frozen-anchor change of any kind.

## Contents

- `keep_the_books_survey.tex` — the complete English manuscript (article class, inline `thebibliography` of 61 entries; no external .bib, figures, data files, or font files).
- `README.md` — this file. No build products inside the tarball; the compiled verification PDF (26 pages) is delivered alongside the group message.

## Content baseline (unchanged from v7)

- **Source of record (content chain head)**: `查理_第二作综述措辞对齐版_2026-09-16.md` (13,206 words by `wc -w`, 486 lines, 61 references, 10 tables; sha256 prefix `e8933ebce0c0`). All v7 declared invariants carry over unchanged: 262 citation tokens in order and multiset; References block, FN1/FN2, GLM AI-use disclosure, and §9.3 frozen anchors byte-identical; 61 references first-cited in strict 1→61 order; [4] anchored to arXiv:2609.09001. The self-overlap disclosure numbers are unchanged (content untouched): 4.62% within §9.3 (60/1,298), 0.21% across the remainder, 8-gram 0.91% (127 words).

## Typographic baseline (v8)

- **Engine layer**: `pdflatex`-only, no `fontspec`, no system-font or file dependencies; Latin Modern throughout, circled digits ①–⑥ (163 source occurrences) via `pifont` `\ding{172}`–`\ding{177}` (URW Dingbats, embedded).
- **Compilation (verification)**: local `pdflatex` (TeX Live 2026; a TeX Live 2025 local install could not be completed this round for network reasons, disclosed in the fix note) → 26 pages; four-zero metrics green: 0 errors, 0 Overfull boxes, 0 missing characters, 0 undefined citations (Underfull boxes are spacing hints, 4 on the final pass).
- **Page count**: 26 pages vs. v7's 30 — Latin Modern is metrically more compact than v7's DejaVu Serif; this is an expected engine-layer effect, not a content change.
- **Fonts**: all embedded (subset) — Latin Modern family + URW Dingbats (`pdffonts`: every row emb=yes).
- **Glyph check**: `τ∗`, `κ`, `Φ`, `Δ`, `≠`, `≤`, `→`, superscript exponents (`10⁻⁴` etc. via text superscripts) all render in the PDF text layer; the ①–⑥ digits extract via ToUnicode.

## Counting calibers (carried over from v7, content untouched)

- **Table rows**: 65 rows including header rows (55 data rows) across the 10 tables.
- **§9.3 numeric tokens**: 134 (`re.findall(r'\d[\d,\.]*', §9.3 source)`).

## Conventions in force

- The AI-use disclosure names the drafting model (GLM); no GitHub repository citation; the Availability section carries no URL sentence; [4] is anchored to arXiv:2609.09001.

**Verification artifacts** (internal): `agents/6a962cc259312f271f3f1e75/v8_pdflatex/r2_build/` (make_v8.py, compile logs pass1–3, extraction/diff scripts).
