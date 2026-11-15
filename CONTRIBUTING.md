# Contributing

## Ground rules

1. **Pre-registration discipline.** All experimental criteria, thresholds, and
   failure paths for evaluation rounds are pre-registered and frozen before a
   run. Issues proposing a change to a gate must state the pre-registration
   delta explicitly. No post-hoc threshold calibration inside a round.
2. **Readings are joint readings.** Every reading is a joint product of the
   model under test and the harness. Reports must describe the harness
   configuration alongside the model; raw scores without a harness pointer
   are not accepted as results.
3. **Self-contained readings packages.** A round is only complete when its
   readings package can be recomputed by a third party from the package alone:
   MANIFEST with content hashes, frozen criteria copy, frozen tool copy,
   per-round logs, and a recompute script that regenerates the headline
   numbers. If a number cannot be recomputed from the package, it is not a
   reading.
4. **Four exclusions.** Do not commit: (a) personal corpora or private data;
   (b) internal collaboration artifacts; (c) infrastructure or billing
   details; (d) credentials of any kind. Large data files belong in readings
   packages, never in this repository (see `.gitignore` artifacts policy).

## Gates

Gate definitions live in `BENCHMARK.md`; the executable specifications are
`gates/` (Lean + Python dual implementations). Changes to gate arithmetic are
changes to pre-registered criteria and require a pre-registration delta.

## Pull requests

- Keep the Lean and Python gate implementations in lockstep; a PR touching
  one must touch or explicitly exempt the other.
- CI must pass (`python -m compileall` on `harness/ gates/ mocks/ scripts/`
  plus the pure-math gate self-test; it never requires external data).
- New harness code must parameterize paths via environment variables; no
  absolute paths, no credentials in code or logs.
