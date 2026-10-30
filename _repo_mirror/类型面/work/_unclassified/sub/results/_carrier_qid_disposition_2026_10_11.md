# Carrier-`q_id` face — disposition (choice 甲: backfill document) · 2026-10-11

- **Nature**: new document (zero-edit, §4.3). Originated under commission `0ce066e5eb3f` §1.2.
- **Source attribution (§2.1)**: content originated by the addressee (this session) under §1.2.
- **Applicability (§2.4)**: governs the **carrier-`q_id` face** (the *second* `R-6` referent, §4.6). Does **not** govern the `F-3` requirement `R-6` (that is `results/_r6_disposition_2026_10_11.md`). The verification is `6509ae68f778`.

## §1 The fact

The carrier `5777a07c608a`'s `heldout_items[]` has `q_id` = `null` at `order_in_r1_key` 6/7/8; the readings file `839fb5452578` carries values at the same keys (`6509ae68f778` §1; `9a62fb2a6956` §5 `R-6`).

## §2 The verification's finding (read back)

`6509ae68f778` §3: the fingerprint is `sha256("file#idx")` with **no** `q_id` (counter-test ①: including `q_id` gives `b2788149ab28` ≠ `c34835ad59cf`; counter-test ②: filling the three values leaves `c34835ad59cf` unchanged). Therefore the defect **does not affect `K-RJ-8′`**. §4.1 classifies it a 「无实质影响之记录瑕疵」; §4.3 offers dispositions 甲/乙/丙/丁.

## §3 Disposition (originated)

**Choose 甲 — a separate backfill document** (annotating the value's provenance as the executor's `pair_id` fallback). Reasoning: 甲 is the only path that makes the carrier's own three rows readable/retrievable while honoring the zero-edit rule; 乙 leaves the carrier itself unreadable; 丙 wrongly merges unrelated semantics; 丁 would break byte-reproducibility of historical carriers (§4.3).

## §4 The values (bit-for-bit from the readings file, §3(6) request)

| `order_in_r1_key` | `file#idx` (R1 key) | `q_id` (from `839fb5452578` `per_item`) | provenance |
|:--:|---|---|---|
| 6 | `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json#1` | `Q2_third_read` | executor `8a81d90c69ba` L758 `ev["q_id"] = q_id or pair_id` |
| 7 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json#0` | `Q6_third_read` | same |
| 8 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json#3` | `Q10_third_read` | same |

These three values are read from `839fb5452578` `per_item[].q_id` and cross-checked against `9a62fb2a6956` §4 rows 6/7/8 (both read back; identical). Provenance: the source supplement for these three items carries no `q_id` key (it identifies by `pair_id`), so the readings value is the executor's `pair_id` fallback (`6509ae68f778` §2).

## §5 Constraints honored (§3(6))

- ⛔ The carrier `5777a07c608a` is **not** edited; ⛔ the extractor `068e1a7a1d04` is **not** edited; ⛔ no JSON is merged.
- The backfilled values **match the readings file bit-for-bit** (§4).

## §6 Separation of supplied and non-supplied parts (§2.5)

- Supplied: the disposition (甲); the three values with provenance.
- Not supplied: any in-place edit of the carrier or extractor; any change to `K-RJ-8′` or its verdict.

## §7 Boundary

⛔ No edit of carrier/extractor; ⛔ no JSON merge; values bit-for-bit from `839fb5452578`; no `K-RJ-*` verdict.

---

*carrier-`q_id` disposition · 2026-10-11 · originated under `0ce066e5eb3f` §1.2 · choice 甲 (separate backfill doc) · three values `Q2_third_read`/`Q6_third_read`/`Q10_third_read` bit-for-bit from `839fb5452578`, provenance = executor `pair_id` fallback · carrier & extractor untouched · does not affect `K-RJ-8′`.*
