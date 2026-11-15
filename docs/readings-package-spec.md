# Readings package specification

A round is only complete when its readings package can be recomputed by a
third party **from the package alone**.

Required contents:

1. `MANIFEST` - per-file sha256_12 and mtime; the manifest hash is the
   package anchor (`input_sha` of the locked-baseline line). Delivery
   red line: zero post-delivery modifications (mtime-checked).
2. Frozen criteria copy (the pre-registered gate text in force).
3. Frozen tool copy (byte-identical launcher copy; `tool_sha`).
4. Blind face / frozen faces (`frozen_sha`).
5. Per-round logs (launch log, progress ledger, per-call ledger).
6. Per-op ledger (key-level operations) - required for key-level gates
   (G6'/G7' adjudication); missing key-level ledgers make key-level gates
   explicitly **undecidable** (never silently passed).
7. Readout JSON (headline aggregates; per-segment statistics).
8. Recompute script that regenerates headline numbers from raw ledgers;
   aggregates must equal the direct ledger recomputation (identity check).

Principles:

- If a number cannot be recomputed from the package, it is not a reading.
- Readings are joint readings of model x harness; the package pins both.
- Failed rounds still ship packages (fail-loud partials with status and
  reason), because auditable failures are readings too.
