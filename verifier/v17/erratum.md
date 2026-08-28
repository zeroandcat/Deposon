## erratum（2026-08-29 深探整改）
- 本版 BOSS 锚点基于无统计门槛的旧口径（6 事件 tfidf×5+CN×1、field 15/20）。
- 整改后门槛 margin≥3 金边：门槛后 6 事件（含 L_PM 三臂）、被拦 4 事件（含 S5 抽签）；v17 的 tfidf×5 锚点失效。
- 按冻结纪律本版 check.py 不覆写；FAIL 是正确信号。新锚点由 verifier/v21 承接（spec: docs/SPEC_v2.0_amendment1.md A3）。
