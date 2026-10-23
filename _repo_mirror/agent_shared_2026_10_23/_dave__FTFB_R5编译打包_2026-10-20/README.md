# Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews

arXiv submission package, R5 revision edition (2026-10-20). Single-author preprint.

## Contents

- `fiction_that_feeds_back.tex` — typeset source, R5 revision edition (pdflatex-compatible;
  no system-font or fontspec dependencies; standard packages only: fontenc, inputenc,
  lmodern, pifont, newunicodechar, amsmath/amssymb, graphicx, booktabs, tabularx,
  hyperref, url, enumitem, geometry). Self-contained: no \input/\include, no external
  figures, no .bib/.bbl — the reference pool is an in-text itemize list, [R01]–[R66]
  (R4 edition: [R01]–[R56]; the ten additions [R57]–[R66] enter by declaration).
- `compile_verification_2026-10-20.txt` — compilation and verification record for this
  edition (fingerprint chain, four-zero metrics, arXiv compliance gates, hygiene scans,
  pool and anchor regression, disclosures).
- `README.md` — this file.

## SHA-256 fingerprint chain (this edition)

- `fiction_that_feeds_back.tex`:
  ba2f157196f575366700fe2209097f4499417412550759039dd814fe3cc51482 (123,129 bytes)
- compiled PDF (delivery-chain baseline; not shipped inside this package):
  f5b985006b592f50ab8ab0c776c7e51d7a5ce17af25ae79526800c12ddf49786
  (29 pages, 431,627 bytes, A4, all fonts embedded)
- The package itself carries no prebuilt PDF: the arXiv build compiles the source;
  the PDF fingerprint above is the delivery-chain baseline compiled with the same
  engine (pdfTeX 3.141592653-2.6-1.40.29, TeX Live 2026) in three passes.

## Notes for the submitter

- Three pdflatex passes converge: 0 errors, 0 Overfull boxes, 0 missing characters,
  0 undefined references, 0 LaTeX Warnings. Two Underfull boxes (badness 5548/1990)
  are carried over from the previous edition at the same content (the [R37] entry)
  and are disclosed in the verification record.
- Page count of this edition: 29 (previous revision edition: 25).
- Submission info line (page 1, under the title block): arXiv subjects
  cs.AI (primary) - physics.hist-ph - cs.CY; License CC BY 4.0; Conflicts of
  interest: none declared; Date 2026-10-20.
- Abstract: paste verbatim from the paper's Abstract section (synced in the
  delivery metadata sheet, arxiv_metadata.txt); 1,822 characters
  whitespace-normalized (limit 1,920). The abstract is unchanged from the
  previous revision edition (byte-identical).
- Comments-field draft for the R5 edition is provided in the delivery metadata
  sheet (arxiv_metadata.txt), with a field-by-field diff against the previous
  revision edition: Title, Authors, Subjects, License, Conflicts of interest
  unchanged; Date and Comments updated.
- This edition is a replace on the existing submission record of this preprint
  (not a new submission). Author list and license are unchanged, so the replace
  requires no moderation approval on those grounds.
