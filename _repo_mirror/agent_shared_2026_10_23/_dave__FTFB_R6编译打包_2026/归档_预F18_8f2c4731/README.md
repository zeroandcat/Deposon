# Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews

arXiv submission package, R6 edition (2026-10-20). Single-author preprint.
Version lineage: R3 (2026-09-18) -> R4 (2026-09-27) -> R5 (2026-10-20,
submission suspended) -> R6 (2026-10-20, philosophical-register restructure).

## Contents (7 files, flat)

- `fiction_that_feeds_back.tex` — typeset source, R6 edition (pdflatex-
  compatible; no system-font or fontspec dependencies; standard packages
  only: fontenc, inputenc, lmodern, pifont, newunicodechar, amsmath/amssymb,
  graphicx, booktabs, tabularx, hyperref, url, enumitem, geometry).
  Self-contained: no \input/\include, no external figures, no .bib/.bbl —
  the reference pool is an in-text itemize list, [R01]–[R66] (unchanged
  from R5; R5 extended it from 56 to 66 by declared additions).
- `fiction_that_feeds_back.pdf` — pre-compiled PDF from this exact source
  (compile-chain baseline: pdfTeX 1.40.29 / TeX Live 2026, three passes,
  converged; 31 pages, A4). Included per the case-B package form, following
  the measured first-work upload precedent (a pre-compiled PDF alongside
  the same-named .tex, accepted by arXiv) and the R3 case-B precedent.
- `compile_verification_2026-10-20.txt` — compilation and verification
  record for this edition (fingerprint chain, four-zero metrics, arXiv
  compliance gates, hygiene scans, pool and anchor regression, discipline
  statement).
- `arxiv_metadata.txt` — submission metadata paste sheet for this edition
  (Title/Authors/Subjects/Comments/License/Conflicts/Date plus the abstract
  paste value, with field-by-field diff vs the R5 sheet). NOTE: the R6
  abstract measures 1,973 characters (whitespace-normalized), 53 over the
  standing 1,920 arXiv form limit — see the sheet's length warning and the
  steps sheet gate 4 before pasting.
- `word_count_report_2026-10-20.txt` — three-caliber word count (P/C/T:
  14,508 / 17,233 / 15,454; same v6 tool as R3/R4/R5).
- `SHA256_MANIFEST.txt` — sha256 manifest of all payload files (this file
  excluded), s6-format; verify with sha256sum -c after extraction.
- `README.md` — this file.

## Source hygiene

- Byte-identical to Charlie's R6 delivery (sha256 45887c4316d3...; 132,269
  B; 690 lines); the formatting chain re-verified the fingerprint before and
  after compilation (zero drift).
- The R6 restructure is Charlie's single-run 17-anchor application
  (script apply_r6_final.py, deterministic, R5 source read-only); the
  reference pool block, pool count (66), citation instances (190) and the
  citation-frozen commit token are regression-verified unchanged.

## Form-side fields (for the submitter)

- Fill in (per the delivery metadata sheet `arxiv_metadata.txt`, kept in
  sync with the title block): arXiv subjects cs.AI (primary) -
  physics.hist-ph - cs.CY; License CC BY 4.0; Conflicts of interest: none
  declared; Date 2026-10-20.
- Abstract: REWRITTEN with R6 (register-matched) — currently 1,973
  whitespace-normalized characters, 53 OVER the standing 1,920 form limit;
  trim decision pending (Charlie amendment round) — do not paste as-is.
- Comments-field draft for the R6 edition is provided in the metadata sheet
  (31 pages; R6 edition note; lineage R3 -> R4 -> R5 suspended -> R6; no
  AI-annotation clause, per the standing M-2 decision).
- This edition is a replace on the existing submission record of this
  preprint (not a new submission). Author list and license are unchanged,
  so the replace requires no moderation approval on those grounds.
- The suspended R5 package remains untransmitted by design (M-4); this R6
  package supersedes it.
