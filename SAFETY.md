# Safety

## Before you run

This harness issues prompts to external LLM endpoints. Read this file first.

- API credentials are injected via environment variables at launch time.
  They never appear in code, in committed files, or in logs. If you find a
  credential shape in any artifact, treat it as a security incident.
- The harness applies an anti-leak scan to every artifact before release
  (credential shapes, endpoints, internal paths, billing figures).

## Three protection clauses

- **PR-1 (fallback re-delivery content check).** If a response fails to
  parse, the fallback re-delivery must be content-verified before it can
  enter any metric; parse-failures are counted separately and never silently
  retried into the numerator.
- **PR-2 (ledger outside the model).** The authoritative state ledger lives
  outside the model's context. State is verified bit-exact against the
  harness-side ledger; a model-claimed state is never trusted by itself.
  (Construction aligned with the verifier-outside-the-loop pattern in
  arXiv:2611.02361, with its three reported limitations noted and a
  domain-limitation patch line applied.)
- **PR-3 (high-sensitivity fields marked).** Fields whose corruption would
  invalidate a round are marked high-sensitivity and cross-checked on every
  read; mismatches fail loud (FAIL_partial) rather than degrade silently.

## Stop-loss semantics (fail loud, never lose readings)

Budget and protocol stop conditions (ES-1..ES-9) halt the chain at round
boundaries; on any failure the harness dumps the partial readings package
with an explicit status (`DONE` / `FAIL_partial` + reason) so that a failed
run still yields auditable readings. `INVALID` events are tallied and
reported; they never silently disappear.
