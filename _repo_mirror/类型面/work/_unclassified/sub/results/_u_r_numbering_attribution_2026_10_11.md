# `U-*` / `R-*` numbering attribution — proposal · 2026-10-11

- **Nature**: **proposal in a new document**. Originated under commission `0ce066e5eb3f` §1.2. ⛔ No in-place renumbering (§3(5) request); ⛔ does **not** assert the two series are "equivalent" (the lead agent aligned them by referent only).
- **Source attribution (§2.1)**: content originated by the addressee (this session) under §1.2.
- **Applicability (§2.4)**: governs the attribution of the two defect/exit numbering series across the third-domain chain. Does not govern the objects themselves.

## §1 Provenance of each series

| Series | Origin face | Carries | On-disk evidence |
|---|---|---|---|
| **`R-*`** (`R-1`…`R-9`) | the third-domain **declaration face** `9a62fb2a6956` §5 「报回项与未闭出口」 | the declaration face's exit roster | `9a62fb2a6956` §5; occupancy: R-1×4, R-2×4, R-3×2, R-4×2, R-5×1, R-6×2, R-7×1, R-8×3, R-9×2 |
| **`U-*`** (`U-1`…`U-6`) | the **verdict-keeper** face `f2e8e32089b2` §3 (不符项 table) and `bba3b889d849` | a defect set on the third domain | `f2e8e32089b2` §3; `78fb8c47c944` §2-10 |
| **(collision)** `U-2`/`U-3` | `_u2u3_effectivity_register_2026_10_10.md` | `af` entity definition / `give-up` semantics — **unrelated** | `_u2u3_effectivity_register_2026_10_10.md` (full) |

⚠ **Two distinct collisions**: (i) the `U-*` defect set vs the `R-*` exit roster (same referents, different labels); (ii) the label `U-3` (and `U-2`) is **also** occupied by the `af`/`give-up` semantics register, so those labels are permanently ambiguous bare.

## §2 `U-1`…`U-6` objects (verbatim from `f2e8e32089b2` §3, read back)

| Label | Object |
|---|---|
| `U-1` | 🔴 `LIM-A″` 三条断言于第三域皆不成立 |
| `U-2` | 🔴 上游 `mixed_object` ＝ `false` 之字面不符 |
| `U-3` | ⚠ 载体字段不一致（`q_id` 缺 3 件） |
| `U-4` | ⚠ 第二域「C 在本留出集上退化」之描述于第三域不成立（第三域 C ＝ `1/5`） |
| `U-5` | ⚠ `K-RJ-4` 条文「A′ 逐位持平」措辞于第三域字面失配 |
| `U-6` | ⚠ 差因含 2 件负向项 |

## §3 `R-1`…`R-9` objects (verbatim from `9a62fb2a6956` §5, read back)

`R-1` 位移覆盖限制；`R-2` `LIM-A′` 原文三条实测断言于第三域三处皆失配（须 PI／protocol）；`R-3` `K-RJ-4` 「⛔ 0 以『A′ 逐位持平』沿用为触发量」措辞于第三域字面失配；`R-4` `mixed_object` ＝ `false` 与冻结字面 `true` 抵触；`R-5` `K-RJ-4` 取值候 PI 另给；`R-6` 载体 `q_id` 缺 3 件；`R-7` 本棒交付之事实；`R-8` 编号同形异指（`S5″`）；`R-9` 自算射程。

## §4 Attribution scheme (proposal)

**Recommend: domain-separated namespaces, unify on the `R-*` series for the defect/exit objects, retire the `U-*` labels to alias status.**

- The `R-*` series is the **authoritative on-disk roster** (it lives in the declaration face, quotable and fingerprint-anchored). Future references to these objects should use the `R-*` label **plus a referent note** naming the object, to defeat the `R-2`/`R-6` referent ambiguity noted at commission §4.6.
- The `U-*` labels are a **legacy alias set** originating in the verdict-keeper face. They are retained as history (⛔ not erased) but should not be used bare in new documents.
- ⛔ `U-2`/`U-3` in particular must **never** be used bare (the give-up-semantics register occupies them).
- This is a **proposal**: no document is renumbered in place; adoption is the PI's.

## §5 Legacy → new crosswalk (complete; unmapped cells marked)

| Legacy (`U-*`) | Object | `R-*` label by object | Note |
|---|---|---|---|
| `U-1` | `LIM-A″` 三断言失配 | **`R-2`** | matches `f4b129e3312f` §2-2 |
| `U-2` | `mixed_object` 字面不符 | **`R-4`** | matches `f4b129e3312f` §2-2 |
| `U-3` | 载体 `q_id` 缺 3 件 | **`R-6`** | matches `f4b129e3312f` §2-2; ⚠ bare-label collision with give-up register |
| `U-4` | 第二域「C 退化」描述第三域不成立 | **(no counterpart)** | not in `9a62fb2a6956` §5 roster; no `f4b129e3312f` §2-2 row |
| `U-5` | `K-RJ-4` 措辞失配 | **`R-3`** (by object) | ⚠ same object class (both `K-RJ-4` 措辞); `f4b129e3312f` §2-2 declines the mapping (0 命中) ⇒ **by object only, not ruled equivalent** |
| `U-6` | 差因负向项 | **(no counterpart)** | not in `9a62fb2a6956` §5 roster |
| — | 位移覆盖限制 | **`R-1`** | no `U` counterpart |
| — | `K-RJ-4` 取值候 PI | **`R-5`** | no `U` counterpart |
| — | 交付事实 / `S5″` 编号 / 自算射程 | **`R-7`／`R-8`／`R-9`** | no `U` counterpart |

## §6 Separation of supplied and non-supplied parts (§2.5)

- Supplied: the provenance, the scheme (§4), the crosswalk (§5).
- Not supplied: any renumbering (⛔ forbidden in place); any ruling on which series "wins"; any assertion of equivalence.

## §7 Boundary

⛔ Never by renumbering in place; ⛔ no assertion the two series are equivalent; adoption is the PI's / protocol's.

---

*`U-*`/`R-*` numbering attribution · proposal · 2026-10-11 · originated under `0ce066e5eb3f` §1.2 · recommended: domain-separated namespaces, `R-*` authoritative, `U-*` retired to alias · crosswalk complete with `R-1/5/7/8/9` and `U-4/6` marked unmapped · no in-place renumber, no equivalence asserted.*
