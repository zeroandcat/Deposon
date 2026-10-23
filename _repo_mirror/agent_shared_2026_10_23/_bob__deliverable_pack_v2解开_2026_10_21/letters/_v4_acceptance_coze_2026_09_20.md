# V4 Invitation — Formal Acceptance (coze)

**To:** Principal Investigator, deposon V4 (via the deposon 〔IM〕 / paper-track channel)
**Re:** `results/_v4_experiment_invitation_2026_09_20.md` (draft v0.1)
**From:** coze (paper-track recipient; 〔IM〕 surface)
**Date:** 2026-09-20
**Boundary:** read-only. No frozen asset modified. No key, secret, or endpoint in this file.

---

## §1 Acceptance

coze **accepts** the V4 experiment-design invitation.

- **Assigned tracks (§7.2):** Track 1 (distillation / mode-set) + Track 2 (reverse-distillation / reverse-attribution).
- **Assigned lens (§7.2):** paper-track review of the **〔IM〕-deliverable form** of the mode-set table — surface-format feedback only.
- **Output form (§7.4):** Markdown, ~200–500 words per checkpoint, attached to the deposon 〔IM〕 / paper-track channel.

Acceptance is given in principle. It takes effect for the D1/D3/D5 cadence once the invitation reaches "circulation-ready" (§8.3), since the current draft is explicitly marked "not circulation-ready" (§12).

## §2 Scope acknowledged

**Asked of coze.** Surface-format review of the 〔IM〕-deliverable mode-set table — whether the table survives the 〔IM〕 surface (length, legibility, field order, copy-paste integrity, inline-vs-attachment split). **Not** the statistical content of the mode set, and not the substance of the reverse-attribution procedure.

**Not asked (§7.3) — understood and accepted.**

- Not asked to define the anti-distillation mechanism (§2.3) — that is the PI's call; I will comment on the placeholder only.
- Not asked to modify any frozen asset.
- Not asked to run new experiments on the frozen stack.
- Not asked to commit to authorship.

## §3 Boundary commitments

- **Frozen assets:** read-only. I will not modify any of the 18 frozen anchors, caption fingerprints, 5 V2 artifacts, 5 锚 JSON, plugin specs, verifier subtree, or Trae-IDE cache (§1.5, §5.7).
- **No-key:** no API key, secret, endpoint, or proprietary prompt will appear in any coze output (§1.5).
- **Cadence:** 〔IM〕-only; ~5–10 minutes per checkpoint; D1 / D3 / D5 (§2.6, §7.1). I will not push, fetch, or auto-message.
- **Authorship:** AI is not an author. My contributions are acknowledged, not authorship (§8.1). CRediT assignment is at the PI's discretion.

## §4 Surface-format findings (coze's lane)

Three items, all surface-level.

**S1 — the 〔IM〕-deliverable form of the mode-set table is not yet specified.** §2.1 and §2.6 fix the *content* of the mode-set table (Track 1 output) but not its *〔IM〕 rendering*. On a surface that truncates and strips formatting, an unspecified rendering means each recipient publishes a different-looking table and the surface comparison breaks. Proposed 〔IM〕 form, as a separate derived artifact with a frozen schema:

1. one line per mode, fixed field order: `mode_id | 血统覆盖 (vendor lineages) | anchor 命中 | verdict`;
2. raw SHA-12 kept **out** of the 〔IM〕 message body — attachment only;
3. hard cap on mode count (e.g. ≤20 lines) with an explicit `[truncated: n more]` marker if exceeded;
4. verdict tokens restricted to the four §3.1 tokens, no free-text verdicts.

**S2 — document-surface inconsistency (already raised by Trae code as B1; corroborated).** §1.1, §2.1, §5.2, and §2.7 write `{KIMI, GLM_1, GLM_2, coze, M3}`; the actual directories are `{kimi, GLM_1, GLM_2, coze, minimax}` — `M3` does not exist, and the fifth artifact is `minimax`. Flagging only to confirm the fix must be applied to **all four occurrences**, not one.

**S3 — broken internal cross-reference.** §12's draft banner asks the PI to verify "§7.5 (recipient channel IDs)", but §7 ends at §7.4 — there is no §7.5. Either add §7.5, or retarget the banner to §7.1 / §9 item 5.

**S4 — rubric/lane tension, flagged for the PI.** §2.6 (D5) asks *every* recipient to return PASS/FAIL/PARTIAL/GRAY on each track, while §7.2 limits coze to surface-format feedback only. Read together, coze cannot return a substantive track verdict. I will therefore return the verdict **as applied to the 〔IM〕 surface** (is the surface form fit for circulation?) and defer substantive Track 1/2 verdicts to the paper-track reviewers (KIMI-K3, GLM). If the PI intends otherwise, please say so at D1.

## §5 What coze will deliver

| Checkpoint | Deliverable |
|---|---|
| **D1** | Surface-format sign-off or objection on the 〔IM〕-deliverable mode-set table (length cap, field order, truncation rule, hash placement). |
| **D3** | Render the Track 2 reverse-attribution output in the proposed 〔IM〕 form; report any surface breakage (truncation, copy-paste loss, illegible columns). |
| **D5** | Return PASS / FAIL / PARTIAL / GRAY on the **〔IM〕 surface** for Track 1 and Track 2; comment on the Track 3 placeholder only, not define it. |

Also verified at acceptance time (read-only): §6's five KT SHA-12 values (`KT_ABC1 03c6c01f3697`, `KT_A1 78b71d404366`, `KT_B1 0410ca0fbdae`, `KT_C1 59d8f56347d5`, `KT_D0 cce8e9a1b00e`) all match the V3 终稿 R5 §3.2 asset-layer table — a second, independent confirmation beyond Trae code's file-level check. §9 item 3 is resolved for the five anchors.

## §6 Declaration

This acceptance modifies no frozen asset and transmits no key, secret, endpoint, or proprietary content. coze participates as an acknowledged contributor, not an author.

*coze — accepting the V4 invitation, 2026-09-20.*
