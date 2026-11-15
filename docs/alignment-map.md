# Alignment map (deepseek-harness conventions)

This repository aligns its public interface with the open-source
conventions of `deepseek-ai/deepseek-harness` (MIT, agent harness), with
three deliberate divergences.

| convention | here | note |
|---|---|---|
| governance file family at root (CONTRIBUTING / THIRD_PARTY_NOTICES / Citation) | yes | dsh-aligned |
| SAFETY.md at root | yes | **beyond dsh** (run-safety clauses + stop-loss semantics) |
| bilingual README trio + .i18n.yaml | yes | README.md + README.zh.md |
| BibTeX at README tail + CITATION.cff | yes | placeholder authorship until the paper line lands |
| topic-based plugin discovery | yes | repo topics + interface notes |
| license | MIT | Apache-2.0 kept as recorded fallback |
| AGENTS.md / CLAUDE.md | **not introduced** | deliberate |
| benchmarks data in-repo | **no - pointers only** | readings live in self-contained packages (privacy + audit chain) |
| status declaration | v0.x preview + breaking-change warning | honest-preview stance |
