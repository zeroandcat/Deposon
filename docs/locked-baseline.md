# Locked-baseline self-check line

Every experimental report line must carry a locked-baseline self-check line
(eight elements, machine-readable):

```
locked_baseline: tool_sha=<sha12> frozen_sha=<sha12> criteria_sha=<sha12+section> seed=<int> models=<m1><-><m2>[;<m3>] per_tier=<tiers> fail_semantics=<INVALID|ES-x|FAIL_partial> dual_run=<plan/chain> input_sha=<MANIFEST sha12>
```

Semantics:

- `tool_sha` - frozen tool copy (byte-identical copy shipped in the readings
  package; hash anchored in its MANIFEST)
- `frozen_sha` - frozen face (blind K_h mapping; also `frozen/`)
- `criteria_sha` - pre-registered criteria text (with section pointer)
- `seed`, `models`, `per_tier` - run configuration
- `fail_semantics` - the declared failure taxonomy in force
- `dual_run` - plan/chain identifier
- `input_sha` - MANIFEST hash of the readings package the line was computed
  from

Worked example (P2' rerun round):

```
locked_baseline: tool_sha=088ed4f8dd9c frozen_sha=b3693a8c1804 criteria_sha=65a286367577#S6 seed=20261115 models=qwen3.7-flash<->qwen3.7-max;kimi-k3.1-pro per_tier=form,withdraw,devalue fail_semantics=INVALID|ES-1..9|FAIL_partial dual_run=a/p2p input_sha=7d7eca4527a0
```
