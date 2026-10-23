# Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews

arXiv submission package, R3 revision edition (2026-09-18). Single-author preprint.

## Contents

- `fiction_that_feeds_back.tex` -- typeset source, R3 revision edition (pdflatex-compatible;
  no system-font or fontspec dependencies; standard packages only: fontenc, inputenc, lmodern,
  pifont, newunicodechar, amsmath/amssymb, graphicx, booktabs, tabularx, hyperref, url,
  enumitem, geometry).
- `fiction_that_feeds_back.pdf` -- compiled output (pdflatex, 3 passes; 24 pages; zero
  errors, zero overfull boxes, zero missing characters, zero undefined references).
- `compile_verification.txt` -- full compilation and regression verification record
  for this edition (fingerprint chain, four-zero metrics, cleared-grep scan, anchor
  and pool regression).
- `word_count_report_2026-09-18.txt` -- word-count report (tools, raw counts, calibers,
  per-touchpoint attribution), regenerated for this edition.
- `arxiv_metadata.txt` -- submission metadata sheet (paste fields verbatim; abstract
  verbatim).
- `SHA256_MANIFEST.txt` -- SHA-256 fingerprints of all files above.

## Build

    pdflatex fiction_that_feeds_back.tex   (run 3 times)

Expected: A4; 24 pages; zero errors / overfull boxes / missing characters /
undefined references.

## Verification summary

- This edition is a content-level revision of the acceptance-revision edition
  (tex ec3e1a15...): exactly 5 source lines changed (L264 / L298 / L409 / L488 / L494);
  the abstract, the five printed anchor prefixes, all numbers, and the decision
  lines are untouched (regression-verified; see compile_verification.txt).
- Reference pool: a closed pool of 56 numbered entries ([R01]-[R56]); pool arithmetic
  closes at 55 verified + 1 anonymized = 56. [R13] and [R14] carry their full
  identifiers (NTRS document ID 19940022856; DOI 10.1007/s12369-022-00876-z);
  entry [R56] is the anonymized companion-study entry (anonymized in this edition;
  to be restored in a revised version).
- Body prose, caliber P of word_count_report_2026-09-18.txt (Introduction heading
  through the Appendix, tables and table notes excluded, whitespace tokens):
  base 12297 -> this edition 10435 words = 15.14% reduction (meets the >= 15%
  line with a 0.14 pp margin). Calibers C and T: 12414 and 11240.
- The abstract is unchanged from the previous edition (byte-identical): 1846
  characters whitespace-normalized (the arXiv paste caliber; limit 1920, margin 74);
  1851 characters raw within the abstract environment; 1867 characters counted
  from the \begin{abstract} marker (the content-line verification caliber).
  Paste it verbatim from the paper's Abstract section (synced in arxiv_metadata.txt).

## Notes for the submitter

- Submission info line (page 1, under the title block): arXiv subjects
  cs.AI (primary) - physics.hist-ph - cs.CY; License CC BY 4.0; Conflicts of
  interest: none declared; Date 2026-09-18.
