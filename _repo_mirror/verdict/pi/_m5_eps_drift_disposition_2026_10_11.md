# `M-5` ε-caliber drift — disposition · 2026-10-11

- **Nature**: new document (zero-edit, §4.3). Originated under commission `0ce066e5eb3f` §1.2.
- **Source attribution (§2.1)**: content originated by the addressee (this session) under §1.2.
- **Applicability (§2.4)**: governs the ε-caliber drift (`M-5`). Does **not** revive any `ε₀` value and does **not** change the `MD` definition.

## §1 The two calibers (both numerically 0.05)

| Caliber | Meaning | Source |
|---|---|---|
| **①** `ε₀` | 「比率型归一化之分母下限」 — the denominator floor in `RV_i ≡ nw/max(nled, ε₀)` | `11945e587b1d` §4-4; `5d8cd0d1676f` §7-2 |
| **②** `ε` | 「`ΔTV` 方向登记之容差」 | `7482699e8b07` §3-5; `5d8cd0d1676f` §7-2 |

Recorded as `eps_drift` = 丙·另议 (card 12) at `5d8cd0d1676f` §7-2 / `df1f5f75c7a0` §5.

## §2 Scope narrowing after `ε₀` declared inapplicable

`df1f5f75c7a0` §5: `ε₀` is declared **inapplicable** on the `MD` face — `MD ≡ LS × TV` has **no denominator** ⇒ `ε₀` has no object. ⚠「inapplicable」 ⇔ no object on that face; it is **not** 「voided」 (voiding is the PI's act).

## §3 Whether the drift dissolves, and what remains

- **Caliber ①** — **dissolves**. With `ε₀` inapplicable, caliber ① has no object on `MD`; nothing remains to dispose of *for caliber ①*. ⛔ No `ε₀` value is revived (§1.3 out-of-bounds), and `RV_i` is not revived.
- **Caliber ②** — **survives** as a live caliber. It is the direction-registration tolerance, and as such it is **consumed by `R-2`'s pointing** (`results/_r2_reference_pointer_disposition_2026_10_11.md`), where the registration basis is re-pointed `ΔTV` → `ΔMD`. Its value (`0.05`, adjacent-value half-spacing) is carried, not re-decided.

## §4 Disposition (originated)

The drift is resolved **by decomposition**: caliber ① **dissolves** (no object, no value revived), caliber ② is the single live caliber and is folded into `R-2`. This disposes of `M-5` without reviving an `ε₀` value and without touching `MD ≡ LS × TV`.

## §5 Separation of supplied and non-supplied parts (§2.5)

- Supplied: the decomposition (§3) and the disposition (§4).
- Not supplied: any `ε₀` value; any change to `MD` or to `ε₁` = 0.2; any `K-RJ-*` verdict.

## §6 Boundary (§1.3, §2.6)

No rule/threshold changed; ⛔ no revival of `ε₀` or `RV_i`; no terminal verdict.

---

*`M-5` ε-caliber drift · disposition · 2026-10-11 · originated under `0ce066e5eb3f` §1.2 · caliber ① dissolves (`MD` has no denominator ⇒ no object; `ε₀` not revived) · caliber ② = the live direction-registration tolerance, folded into `R-2` · `MD ≡ LS × TV` untouched.*
