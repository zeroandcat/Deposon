/-
CondensateLedger.lean — machine-checked semantics of the condensate-field
ledger core (companion to `mcp/mcp_server.py` core primitives and
`harness/NingziContainer.lean` container formalization).

The persistence substrate of the condensate field is an append-only external
ledger (JSONL in the Python instantiation): lines are either parsed entries
or corrupt lines (tolerated, skipped — a corrupt line never aborts a read).
Reads are prefix-filtered and render-surface only (DR-4): a read returns
`key: text` lines; the raw record (JSON, timestamps, …) never enters the
render surface.

Machine-checked claims (core-only, no mathlib, no `sorry`):

  T1  readHits_write_visible   — an appended entry whose key carries the
                                 requested prefix is returned by the
                                 subsequent read (write visibility).
  T2  readHits_subset_append   — reads are monotone: appending never removes
                                 an earlier hit (append-only ⟹ memory only
                                 grows; durability is structural, not an
                                 implementation promise).
  T3  readHits_corrupt_append  — appending a corrupt line changes nothing:
                                 corrupt lines are invisible to reads.
  T4  dr4_render_eq            — the render surface is exactly
                                 `key ++ ": " ++ text`.
  T5  dr4_render_ts_irrelevant — rendering is independent of the metadata
                                 field `ts` (DR-4: no metadata in render).
  T6  mem_readHits_prefix      — prefix-filter soundness: every hit's key
                                 carries the requested prefix.

Verified with lean 4.15.0 (core only). Compile standalone:
    lean harness/CondensateLedger.lean
Dual-implementation note: `mcp/ledger_crosscheck.py` runs the same six
properties as concrete vectors against the Python core primitives.
-/

namespace CondensateLedger

/-- One ledger entry: a dotted key, render text, and metadata (DR-4 keeps
metadata out of the render surface). -/
structure Entry where
  key : String
  text : String
  ts : String

/-- One raw ledger line: either a parsed entry or a corrupt line
(unparseable JSON in the Python instantiation; tolerated and skipped). -/
inductive Line where
  | parsed : Entry → Line
  | corrupt : Line

/-- The ledger: a sequence of lines, append-only in every operation that
matters (see `readHits_subset_append`). -/
abbrev Ledger := List Line

/-- Prefix-filtered read of parsed entries (the `read_entries` core
primitive). Corrupt lines are skipped; hits come back in write order. -/
def readHits : String → Ledger → List Entry
  | _, [] => []
  | p, Line.parsed e :: rest =>
      if e.key.startsWith p then e :: readHits p rest else readHits p rest
  | p, Line.corrupt :: rest => readHits p rest

/-- DR-4 render surface: exactly `key: text`. -/
def render (e : Entry) : String := e.key ++ ": " ++ e.text

/-- Workhorse: reads distribute over append. -/
theorem readHits_append (p : String) (L L' : Ledger) :
    readHits p (L ++ L') = readHits p L ++ readHits p L' := by
  induction L with
  | nil => simp [readHits]
  | cons x xs ih =>
      cases x with
      | parsed e =>
          by_cases hc : e.key.startsWith p = true
          · simp [readHits, hc, ih]
          · simp [readHits, hc, ih]
      | corrupt =>
          simp only [List.cons_append, readHits]
          exact ih

/-- T1: write visibility — an appended entry with a matching prefix is
returned by the subsequent read. -/
theorem readHits_write_visible {p : String} {e : Entry} (L : Ledger)
    (h : e.key.startsWith p = true) :
    e ∈ readHits p (L ++ [Line.parsed e]) := by
  rw [readHits_append]
  have h1 : readHits p [Line.parsed e] = [e] := by
    simp only [readHits, if_pos h]
  rw [h1]
  exact List.mem_append_right _ (List.mem_singleton_self e)

/-- T2: read monotonicity — appending never removes an earlier hit. -/
theorem readHits_subset_append (p : String) (L L' : Ledger) :
    readHits p L ⊆ readHits p (L ++ L') := by
  rw [readHits_append]
  exact List.subset_append_left _ _

/-- T3: corrupt lines are invisible to reads. -/
theorem readHits_corrupt_append (p : String) (L : Ledger) :
    readHits p (L ++ [Line.corrupt]) = readHits p L := by
  rw [readHits_append]
  simp [readHits]

/-- T4: the render surface is exactly `key: text`. -/
theorem dr4_render_eq (k t ts : String) :
    render ⟨k, t, ts⟩ = k ++ ": " ++ t := rfl

/-- T5: DR-4 — rendering is independent of the metadata field `ts`. -/
theorem dr4_render_ts_irrelevant (k t ts₁ ts₂ : String) :
    render ⟨k, t, ts₁⟩ = render ⟨k, t, ts₂⟩ := rfl

/-- T6: prefix-filter soundness — every hit's key carries the prefix. -/
theorem mem_readHits_prefix {p : String} {e : Entry} : ∀ (L : Ledger),
    e ∈ readHits p L → e.key.startsWith p = true := by
  intro L
  induction L with
  | nil => intro h; exact ((List.not_mem_nil (a := e)) h).elim
  | cons x xs ih =>
      cases x with
      | parsed f =>
          intro h
          simp only [readHits] at h
          by_cases hc : f.key.startsWith p = true
          · rw [if_pos hc] at h
            rcases List.mem_cons.mp h with rfl | h'
            · exact hc
            · exact ih h'
          · rw [if_neg hc] at h
            exact ih h
      | corrupt =>
          intro h
          exact ih h

#print axioms readHits_append
#print axioms readHits_write_visible
#print axioms readHits_subset_append
#print axioms readHits_corrupt_append
#print axioms dr4_render_eq
#print axioms dr4_render_ts_irrelevant
#print axioms mem_readHits_prefix

end CondensateLedger
