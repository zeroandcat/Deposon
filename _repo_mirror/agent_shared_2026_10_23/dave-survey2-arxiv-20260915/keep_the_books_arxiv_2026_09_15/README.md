# Keep the Books — arXiv submission package (round 1, 2026-09-15)

Single-file `article`-class source for the survey *"Keep the Books: A Survey of
Auditability and Falsifiability in LLM Reasoning"* (Qihao Yuan). Layout follows the
conventions of the author's first work (arXiv:2609.09001, package
`deposon_arxiv_2026_en`).

## Contents

- `keep_the_books_survey.tex` — complete, self-contained source (no external
  figures, no `.bib` file: all 55 references are typeset inline via
  `thebibliography`, which preserves the "pending verification" annotations
  verbatim; a `.bib` export would lose those notes).

## Compile (arXiv-ready)

The file compiles standalone with **XeLaTeX** (tectonic 0.15.0 verified):

```
tectonic -X compile keep_the_books_survey.tex
```

Two passes are run automatically (citation/label resolution). Expected output:
28 pages, **0 errors, 0 Overfull boxes, 0 missing glyphs, 0 undefined
citations**. arXiv's build system runs the same XeLaTeX route.

## Fonts

Primary: DejaVu Serif (falls back to Latin Modern Roman if absent). Special
glyphs (①–⑥ circled digits, ★-class symbols) are mapped via `newunicodechar`
to DejaVu Sans. All 38 non-ASCII code points used in the text are covered; the
compile log shows zero missing-character warnings.

## Key layout decisions

1. **Tables (10 total in the source markdown: the §1.2 scope table, Tables 1–3
   with captions, five per-line matrix-row tables in §4.3–§8.3, and the §9.3
   case-study row).** All use `booktabs` + `tabularx` with `\raggedright`
   `p`-columns and `\footnotesize` (full matrix in §9.1 additionally drops to
   `\scriptsize` with 2.5 pt column separation). The full five-line ×
   six-attribute matrix fits portrait A4 with zero overfull boxes.
   Slash-joined compounds inside table cells (e.g. "rationalization/
   insensitivity") use `\slash` so they can break — visually identical.
2. **Citations.** `[n]`, `[n, m]`, and ranges like `[26–30]` are rendered via
   `natbib [numbers,sort&compress]`, so the printed text reproduces the
   compressed ranges of the content-final draft exactly. Reference numbering
   follows first-appearance order strictly (verified monotonic).
3. **Placeholders.** The 8 `[GAP-6]` markers (second-round novelty check) are
   preserved verbatim, per the round-1 instruction; they will be closed in the
   final compile round.
4. **Metadata.** PDF title/author set via `hyperref` (Title = survey title,
   Author = Qihao Yuan); in-document footer states cs.CL (primary) · cs.AI ·
   cs.LG, CC BY 4.0, no conflicts, date 2026-09-15. The author line carries no
   affiliation because the content-final draft supplies none — nothing was
   invented.
5. **Back matter.** "Availability and provenance" and "AI use disclosure" are
   standalone unnumbered sections before the references, matching the first
   work's final-round convention.

## Self-overlap audit (vs. arXiv:2609.09001)

Word-level 10-gram comparison of §9.3 against the first work's full text:
matching coverage 4.67%, decomposing into (a) frozen-result numerals quoted
from the first work's JSON artifacts, (b) the pre-registration anchor list
(file names + SHA-256 first-12-hex identifiers — byte-exact citation is a
verification requirement, not plagiarism), (c) one 13-word signature phrase of
the first work's central claim, restated with a rewritten continuation, and
(d) one 10-word technical phrase. No sentence- or paragraph-level copying. The
remainder of the survey overlaps the first work by 0.22%, entirely two
reference titles shared by both papers (Wei et al. 2022; Turpin et al. 2023).
Verdict: rewritten citation, arXiv-compliant.

## Round-1 status

This is the layout round, run in parallel with the pre-submission novelty
check. Remaining for the final round: close the 8 `[GAP-6]` placeholders, and
(optionally, author's call) name the drafting assistant in the AI-use
disclosure — the first work names its tool; this draft states "AI assistance
under direct instruction" without a tool name.
