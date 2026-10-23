# External Derivation Commission — R-J5 One-Dimensional Transverse-Field Ising Model, Exact Critical Equation, "Definition Factor" Breakpoint (v0.1, 2026-09-28)

> **Commissioning party (委托方)**: deposon project PI (drafted by the Mavis team doc-writer, 2026-09-28)
> **Addressee (拟致, intended)**: external derivation party / external literature-retrieval party — this letter is forwarded by the PI; the addressee is registered in the "intended / addressee" form and **does not certify, under its own name, any pre-existing conclusion of this project**
> **Authorization source**: the PI's verbatim wording in the contingency plan (questionnaire `ask_577b95bf8620614e98567bca` q4, **as carried in the work order**): 「失败则写委托外部推导，看看是谁的提案，查不出来我依次去各agent处尝试，无论如何VS code总能解决」 — *"If it fails, commission an external derivation, find out whose proposal it is; if it cannot be traced, I will try each agent in turn; either way VS Code will solve it."* The English rendering is our translation; the Chinese original governs.
> **Triggering fact**: the three-state attribution of the R-J5 re-derivation rod resolved to **(c) derivation failed**, with a single breakpoint (the Trotter–Suzuki generating factor) — main document `results/_v4_rj5_rederive_2026_09_28.md` (`34ec49511ee3`), §3.3 and §6.
> **Method declaration**: this letter was drafted with **0 LLM calls / 0 external URLs / 0 keys / 0 network access**; **0 modification of any existing document** (a purely new file); **0 unauthorized threshold changes**; **0 new external literature identifiers**; **0 presupposition of the value of `r`**.
> **Discipline basis**: the four deposon core principles — 大材小用，落到实处，与死同行，虚实回路（FTFB） (*"use great materials on small things; bring it down to earth; walk alongside death; fiction that feeds back"*) — together with the honesty discipline 「诚实的根因是不误导」 (*"the root of honesty is not to mislead"*).
> **Status**: pending PI review and forwarding; this letter does not take effect automatically, changes no existing verdict, and **0 substitution of adjudication**.
> **Counterpart version**: this English letter and the Chinese original `letters/_v5_rj5_external_rederive_request_2026_09_28.md` (`cfd58ae66463`) are mutual counterpart versions. See §9.11.

---

## §0 Commissioning reason (what is being asked for, in one paragraph)

While checking the "**definition factor**" of the **exact critical equation of the one-dimensional transverse-field Ising model (1D TFIM)**, our derivation **stalls at one step that cannot be settled self-consistently**: when the critical manifold of the two-dimensional classical anisotropic Ising model is transported to the one-dimensional quantum model, the **transverse-field term → interlayer coupling** step of the quantum↔classical correspondence introduces a **normalization factor** (whether an extra factor of 2 appears, and how the layer spacing `Δτ` enters). This is precisely the branching point at which the same critical equation is written, in different sources, as taking "**one half** of the coupling coefficient" for `K`, `Γ`, or taking "the coupling coefficient **itself**."

We have independently proved both ends (the classical end and the quantum end); **only this middle step could not be derived.** We now commission an external party to **re-derive this step**, or to **give the original source of that generating factor / of that equation** (verbatim, with equation numbers).

**This commission carries a second question (the PI explicitly asked "find out whose proposal it is")**: a declaration in our repository (Hamiltonian coefficients written as `J/4`, `h/4`, with `K`, `Γ` defined as `βJ/4`, `βh/4`) — please trace its **original proposer / source**: which paper, which community's convention, or which school of writing it corresponds to.

**This letter gives 0 hint as to the answer direction**: the two candidate values of `r` are **both left unpresupposed and stated side by side** (see §2.3); we lean toward neither branch.

---

## §1 Commissioned scope and out-of-scope

**In scope** (please answer):

1. Independently derive the **generating factor** for "transverse field → interlayer coupling" in the Trotter–Suzuki-type quantum↔classical correspondence, giving the complete algebra and the normalization conventions on which it depends;
2. Give the **original source** of the 1D TFIM exact critical equation (of the form `sinh(2K)·sinh(2Γ)=1`, or an equivalent `h_c(T)` form): bibliography + page number + equation number + verbatim text;
3. Answer the provenance question Q3 of §4.

**Out of scope** (this commission neither requests nor hints at):

- No request to revise, overturn, or re-grade any of our existing documents (including the `#12` executor, the γ-R1 preregistration / execution documents, and the R-J5 main document / appendix) — adjudication belongs to our verdict-keeper;
- No request to recompute any of our numerical values;
- No request to modify any threshold (`TH-*` / `K-*` are carried at their existing literal wording, **0 unauthorized change**).

---

## §2 Source ledger (**given in full**; structure and level of detail are for the addressee to decide)

### §2.1 Our proved formula I: the critical line of the two-dimensional anisotropic classical Ising model ✅ (0 breakpoints)

**Basis**: the Kramers–Wannier duality (exact, not approximate). The dual map `K₁* = -½ ln(tanh K₂)`, substituted back, yields the equivalent condition:

```
sinh(2K₁) · sinh(2K₂) = 1
```

Our local numerical verification (not from literature; script `.scratch_rj5/derive_local.py`):

```
K* (sinh(2K*)=1)   = 0.4406867935
½ ln(1+√2) check    = 0.4406867935          ← identity, K* = ½ asinh(1) = ½ ln(1+√2)
sinh(2K*)          = 1.0000000000001301
sinh(2K*)²         = 1.0000000000002602
```

Over the whole range `K₂ ∈ [0.05, 1.2]`, the measured `sinh(2K₁)·sinh(2K₂) = 1.000000000000` (12 digits).

> **Status**: complete, 0 breakpoints. This is the **only one of the "similar equations" that we have proved in full** — it belongs to the **two-dimensional classical** Ising model and is **not** the critical line of the 1D TFIM itself.

### §2.2 Our proved formula II: the zero-temperature quantum critical line of the 1D TFIM ✅ (0 breakpoints)

**Basis**: the Hamiltonian `H = -J Σ_i σ^z_i σ^z_{i+1} - h Σ_i σ^x_i` (**standard Pauli matrices**); the zero-temperature critical point = many-body gap closing.

**Criterion (three iterations, two actively retired; honestly registered)**:

| Version | Criterion | Result | Ruling |
|---|---|---|---|
| v1 | `prod(σ^z)` parity sector | `b_c/a = 1.5` | ❌ **Retired**: `prod(σ^z)=(-1)^{N↓}` **anti-commutes** with `σ^x` ⇒ **not a conserved quantity**; for even L, all-up / all-down lie in the same sector |
| v2 | full spectral gap `E₁-E₀` | `h_c/J ≈ 0.5` | ❌ **Retired**: the ferromagnetic ground state is **doubly degenerate** (global spin flip), so `E₁-E₀` measures that degeneracy, not the excitation gap |
| **v3** | **pin spin 0 (basis restriction `bit0=0`) + open boundaries ⇒ degeneracy removed ⇒ gap = true excitation gap; then fix the scale via the finite-size scaling ratio `r(h)=gap(2N,h)/gap(N,h)`** (**at criticality `gap ~ 1/L` ⇒ the ratio = ½**) | see below | ✅ **Adopted** |

Measured (`derive_b_v3.py` / `derive_b_v4.py`):

```
pin check: gap(L=8, h=0) = 2.000000   gap(L=10, h=0) = 2.000000   ← ferromagnetic gap correctly non-zero
scaling ratio r(h) = gap(10,h)/gap(5,h):
   h=0.90  r=0.5266      h=0.95  r=0.5112      h=1.00  r=0.5062  ← minimum
   h=1.05  r=0.5108      h=1.10  r=0.5230
```

**Conclusion**: the critical point `r_min = 0.5062 ≈ ½` falls at **`h = 1.00`**.

> **1D TFIM zero-temperature exact critical line (derived by us)**:
> ### `c_trans = c_ferro`; for `H = -J Σσ^zσ^z - h Σσ^x` (Pauli) this means **`h_c = J`**

**Cross-corroboration** (consistent with sources we have already checked; not new evidence): S3 of γ-R1 records `t ≡ h/|J|`, `t_c = 1`; S2 records `λ_c = 1`; S4 records `g_c = 1` — all three sources give a zero-temperature critical ratio of **1**.

> **Status**: complete, 0 breakpoints.

### §2.3 Statement of the breakpoint (**the only breakpoint**, copied verbatim from our document)

> ### §3.3 Third step: the generating factor of the Trotter–Suzuki correspondence — [breakpoint] ❌
>
> **This step determines `r`, and it is the only breakpoint of this rod.**
>
> To transport the **two-dimensional classical** critical line of §3.1 onto the **one-dimensional quantum** model of §3.2, one needs the **quantum↔classical correspondence** to give the relation between the classical couplings and the coefficients of the quantum Hamiltonian. The transverse-field term `σ^x` generates the **interlayer** coupling through Jordan–Wigner-type string operators, and its generating factor (whether an extra 2 or π is included, and how the layer spacing Δτ enters) **is exactly the branching point among the three claims `K ≡ βJ/4` / `βJ/2` / `βJ`**.
>
> **[breakpoint] This rod could not determine that factor.** The reasons, honestly graded:
> - **Mathematical layer**: the complete algebra of the Trotter expansion plus the string operators requires reconstructing the whole set of normalization conventions — "classical lattice geometry + the normalization of a slice of thickness Δτ". Without introducing an external authoritative convention, this rod **0 derived** and **0 guessed**.
> - **Tooling layer**: retrieval returned **0 hits** on any source stating that generating factor — the arXiv API searches only metadata, so equation-level statements in the body text are in principle unreachable.
>
> ⟹ **The common value of `r_K`, `r_Γ` (`1/2` or `1`) could not be determined by this rod.**

**Candidate values (two values side by side; this letter presupposes nothing, hints nothing, and weights nothing)**:

| Candidate | Content |
|---|---|
| **甲 (A)** | `r_K ≡ r_Γ ≡ 1/2` — "`K`, `Γ` take **one half** of that paper's Hamiltonian coupling coefficient / transverse-field coefficient" |
| **乙 (B)** | `r_K ≡ r_Γ ≡ 1` — "`K`, `Γ` take the coupling coefficient / transverse-field coefficient **itself**" |

**Definition-factor reading formula (carried at the literal wording of the γ-R1 preregistration, 0 modification)**:

```
r_K ≡ K_lit/(β·c_ferro)；r_Γ ≡ Γ_lit/(β·c_trans)
H_lit = -c_ferro·Σ_i S^z_i·S^z_{i+1} - c_trans·Σ_i S^x_i
K_lit ≡ the dimensionless longitudinal coupling used in that paper's critical equation
Γ_lit ≡ the dimensionless transverse field used in that paper's critical equation
c_ferro ≡ the ferromagnetic coupling coefficient in that paper's Hamiltonian (according to that paper's own writing, including its 1/2, 1/4, etc. normalization)
c_trans ≡ the transverse-field coefficient in that paper's Hamiltonian (according to that paper's own writing)
β ≡ 1/(k_B·T)
```

### §2.4 Our structural narrowing (**a derivation product, for your reference; not a conclusion**)

| # | Narrowing | Content |
|---|---|---|
| **R** | self-duality forces `r_K ≡ r_Γ` | the 1D TFIM has the exact `J ↔ h` self-duality; any correct correspondence must be exchanged by it ⇒ the two generating factors must be equal ⇒ the sub-case "`r_K ≠ r_Γ`" is **excluded by symmetry alone** for TFIM-family sources (re-verified, 0 breakpoints) |
| **S** | the declaration does not exist on the deposon side, and the symbol denotes something else | the claim `K ≡ βJ/4` **does not exist at all** among deposon's three definition anchor points; deposon's `Γ` (`Gamma_aether`, the ether-induced linewidth) is added inside a Feshbach denominator **dimensionally commensurate with** `E - E_0`, i.e. it is a **dimensional energy**, and is therefore **not the same object** as the **dimensionless** `Γ` of the TFIM (re-verified, dimensional layer) |
| **T** | the in-repository declaration triple cannot reproduce the model's own zero-temperature critical point | under that triple, `h_c/J` tends to zero exponentially as `T→0`, which is incompatible with `h_c/J = 1` of §2.2 (derivation; numerical detail in §3.4) |

> **Scope of narrowing R (honestly flagged)**: it applies only to TFIM-family sources carrying the `J ↔ h` self-duality. It does **not** apply to Feshbach-type or scattering-type `Γ` conventions — a scattering linewidth has no such symmetry and **cannot** be extrapolated. Narrowing R **narrows only to "the two values must be equal"; it does not narrow to a specific value**.

### §2.5 The four γ-R1 sources, excerpted verbatim (**given in full**, including the fact of "undefined")

> The following four documents, **in full**, **none** gives a dimensionless definition of `K`, `Γ`, and **none** gives an equation number for `sinh(2K)·sinh(2Γ)=1`. We have **not** back-filled any factor from the "form of the equation", the "zero-temperature critical ratio", or "conventions used elsewhere".

**S1** — Hui Yu, Sudip Chakravarty (2022), *Quantum critical points, lines and surfaces*, arXiv:2207.09547v1 [cond-mat.str-el]. URL `https://arxiv.org/pdf/2207.09547` (retrieval SHA-12 `eca05c215a3c`). **Equation (1), PDF page 2**, verbatim:

> The Hamiltonian, H, is H =− ∑ i (hiσx i +λ2σx iσz i−1σz i+1 +λ1σz iσz i−1) (1) written in terms of standard Pauli matrices. In this section we discuss its phase diagram. We shall set hi =h =cst.

**PDF page 3**, verbatim:

> For the Ising model in a transverse ﬁeld without three spin interaction, the gaps collapse at the Bril- louin zone boundaries, k = ±π at the self-dual point λ1 = 1 and λ2 = 0.

> Extraction note: `ﬁ` / `Bril- louin` are ligatures and hyphenation breaks produced by PDF text extraction, **left unchanged** (verbatim principle). That paper **does not define** `K`, `Γ` (0 occurrences of `sinh`/`asinh`/`cosh`/`K =`/`K ≡`/`κ` in the full text).

**S2** — Jian Ma, Lei Xu, Xiaoguang Wang (2008), *Reduced fidelity susceptibility in the one-dimensional transverse field Ising model*, arXiv:0808.1816v1 [quant-ph]. URL `https://arxiv.org/pdf/0808.1816` (retrieval SHA-12 `e377d6ef2afe`). **Equation (5), PDF page 2**, verbatim:

> The Hamiltonian of the 1D TFIM reads HI = − M∑ j=−M [ λσx j σx j+1 + σz j ] , (5) where σα j (α = x, y, z) is a Pauli matrix at site j, λ is the Ising coupling constant in units of the transverse ﬁeld, and periodic boundary conditions ( σ−M = σM ) are as- sumed.

> …As is well known, there is a critical point exactly at λc = 1 in the thermodynamic limit.

> That paper writes the model with a **single dimensionless parameter** `λ` (the transverse field in units of the coupling); but it gives **only** the zero-temperature critical ratio `λ_c = 1`, does **not** give a finite-temperature `h_c(T)` form, and does **not define** `K`, `Γ`.

**S3** — Gang Xiong, X. R. Wang (2006), *A direct calculation of critical exponents of two-dimensional anisotropic Ising model*, arXiv:cond-mat/0512369v2 [cond-mat.stat-mech]. URL `https://arxiv.org/pdf/cond-mat/0512369` (retrieval SHA-12 `a35361b1dccc`). **Equations (10)–(12), PDF page 2**, verbatim:

> eG(k) = −2 ( h + J cos k + √ h2 + 2J hcos k + J 2 ) . (10) Denote t = h |J| , (11) the excitation gap of ˆH is ∆ E = 2|J||t − 1|. (12) Thus the critical point of the ground-state CPT of the 1D TFIM is at t = tc = 1 where ∆ E vanishes.

> That paper treats the 1D TFIM with **Pauli matrices plus `J` (longitudinal) and `h` (transverse field)**, with a **zero-temperature** criterion `t ≡ h/|J| = 1`; the strings `sinh`/`asinh`/`cosh` do **not** appear anywhere in the full text.
> **Extraction quality, honestly declared**: equation (2) on the same page (the limiting relation from the 1D TFIM to the 2D classical anisotropic Ising model) had its **subscripts and exponents swallowed** in extraction, yielding unreliable fragments; we therefore **quote 0 instances of that equation** and **0 inferences from the fragmentary extraction**.

**S4** — Long Zhang, Chengxiang Ding (2023), *Finite-Size Scaling Theory at a Self-Dual Quantum Critical Point*, arXiv:1910.12538v2 [cond-mat.str-el]. URL `https://arxiv.org/pdf/1910.12538` (retrieval SHA-12 `b622cd5c853c`). **Equation (10), PDF page 3**, verbatim:

> The 1DTFIM can be exactly solved with the Jordan- Wigner transformation [11, 12],σz i =∏ l<i (2c† lcl−1)(ci−c† i) and σx i = 2c† ici− 1, in which ci and c† i are fermion operators. The Hamiltonian is mapped to free fermions, H(g) =− ∑ i (ci−c† i)(c† i+1+ci+1)−g ∑ i (2c† ici− 1). (10)

**PDF page 2**, verbatim:

> The Hamiltonian H(g) is mapped into gH(1/g), thus the QCP at gc = 1 is self-dual.

> **Guard against misattaching a homonymous `Γ` (trace kept)**: the `Γ` appearing in equation (1) on page 1 of that paper reads verbatim `Γ(T,g ) = ∂Tvg(T,g ) ∂Tϵ(T,g ) . (1)`; it is the **generalized Grüneisen ratio** (a thermodynamic quantity), **not** a dimensionless transverse field; `Γ` occurs 35 times in that paper, and **every occurrence has that meaning**. The homonymous symbol **must not** be misattached as `Γ_lit`.

> **Reading result for the four sources**: `r_K` = not readable (null), `r_Γ` = not readable (null). **Grade-A qualifying sources = 0.**

### §2.6 The in-repository declaration triple, verbatim (**for your comparison**)

**Location of the declaration**: `results/_v3_recheck_12_executor_2026_09_27.py:124-125`, constant name `TFIM_CONVENTION`, **verbatim**:

```python
TFIM_CONVENTION = ("H = -(J/4) Σ_i σ^z_i σ^z_{i+1} - (h/4) Σ_i σ^x_i；"
                   "K ≡ βJ/4，Γ ≡ βh/4；无量纲温度 t_rel ≡ k_BT/J = 1/(4K)")
```

**The critical condition and closed form accompanying that declaration** (same file `:128-130` / `:133-148`, verbatim):

```python
residual(κ, γ) = sinh(2κ) · sinh(2γ) − 1
h_c/J = 2 · t_rel · asinh( 1 / sinh( 1/(2 · t_rel) ) )
```

**Its still-earlier upstream literal** (`deposon_team/plugins/boss_pc_2_transverse_field_ising.py:30`, verbatim):

```python
PFEUTY_H_C_OVER_J = 1.0  # 1D chain Pfeuty 严格解 h_c/J = 1
```

### §2.7 The symbol conventions at deposon's three definition anchor points (**carries narrowing S**)

Our verbatim measurement (2026-09-28, local machine):

```
docs/Deposon_Requirements_v1.md            : Ising=0  sinh=0  β=0  → no Ising-theory claim about K/Γ/J/h
Deposon_凝子_统一场论研究报告_v1.pdf        : Ising=0  sinh=0  cosh=0  beta=0  transverse=0
                                             Gamma=5 (all of them Gamma_aether / gamma_aether)
README.md:5                                : no Ising / no K / no Γ
```

`Gamma_aether` verbatim context (the unified field theory report):

```
S_eff(E) = S_bg(E) - [S_bg(E) |W><W| S_bg(E)] / [E - E_0 + i*Gamma_aether/2]
- Gamma_aether: Ether-induced linewidth
Gamma_aether = gamma_ECM * psi(t)
```

> **Narrowing S (our measurement-based conclusion, for you to check; we do 0 reconciliation on your behalf)**: (i) the claim `K ≡ βJ/4`, `Γ ≡ βh/4` **does not exist in any deposon definition anchor point**; its origin is the in-repository `#12` executor (an internal construct of the V3 supplementary review), and it is **not a deposon definition**. (ii) `Gamma_aether` is added inside the same denominator as `E - E_0` ⇒ it is a **dimensional energy**; the TFIM `Γ` is **dimensionless** ⇒ the two fail a dimensional self-consistency test, and the identification of the two as the same symbol is **judged dead** (cause of death: mathematical layer · dimensionality). (iii) the Requirements document records `|t|² + |r|² + |a|² = 1.0` (tolerance 1e-6) and `resonance_factor = 1/(1 + detuning²)`, and contains **no** Ising-type or scattering critical condition of any kind.
>
> ⚠️ **Honest declaration about the anchor entity**: a recursive search of this repository (`deposon-repo`) and of `deposon-sub` and `_non_upload_local_archive` **did not locate the entity** `Deposon_凝子_统一场论研究报告_v1.pdf` (only `Deposon_凝子_统一场论报告_一致性核对_20260907.md` was hit). The character counts and verbatim excerpts for that PDF in the table above were **transcribed from our R-J5 documents**; **this letter did not independently re-extract them**. If you need to check that anchor point, please request the original from the PI; **do not assume it is on disk**.

### §2.8 A one-line falsification test (once you have the body text, this closes the question; we have already registered it)

> In the body text of any candidate paper, locate the page / equation carrying the critical condition for the 1D chain, and check whether that paper defines `K`, `Γ` as "**one half of** the coupling coefficient" or as "**the coupling coefficient itself**":
> - if "one half" ⇒ candidate **甲 (A)**;
> - if "itself" ⇒ candidate **乙 (B)**.
>
> We **0 substitute a prediction on behalf of the PI** (without the body text in hand we are not entitled to predict).

---

## §3 The negative readings we have already landed (**to save you from repeating the labour**; values verbatim)

### §3.1 The retrieval surface (**the surfaces we have already walked**; not exhaustive)

| Surface | Our measurement | Note |
|---|---|---|
| the literal phrase "similar equation" | **the arXiv API indexes metadata only** (title/abstract), **not body text** | equations such as `sinh(2K)·sinh(2Γ)=1` that appear only in body text are **in principle unreachable** through this channel — a **tooling-layer** limitation, **not exhaustive** |
| web / full-text search | **not enabled** (existing documents have already measured SSL failures / 403 / region-skewed irrelevance for DDG / Bing / Mojeek on this egress; **we reuse their already-verified surfaces and do not repeat the expenditure**) | — |
| SciPost direct fetch | **SSL UNEXPECTED_EOF** | same failure class as in existing documents |

Our R-J5 retrieval ledger of 14 attempts (cap 15), the 14-row machine record, and the mechanical counts of `sinh` / `Γ` over the four full-text PDFs (every `sinh` hit was checked individually and is the author surname "Sinha", not an equation) are all available in the evidence-document index (§5).

### §3.2 Full-text retrieval results for the preceding candidates (**all 4 independent channels closed**)

| Candidate | Bibliography | DOI | Measured availability on our side |
|---|---|---|---|
| **C1** | **Pfeuty, P. (1970). The one-dimensional Ising model with a transverse field. Ann. Phys. 57(1), 79–90.** | `10.1016/0003-4916(70)90270-8` | OpenAlex `oa_status:"closed"`, `any_repository_has_fulltext:false`, `best_oa_location=null`, `locations` length **1** with no pdf; Semantic Scholar `isOpenAccess:false` / `openAccessPdf.status=CLOSED`. **Not one page of body text or equation number obtained** |
| **C2** | **Chakrabarti, B. K.; Dutta, A.; Sen, P. (1996). Quantum Ising Phases and Transitions in Transverse Ising Models. LNP Monographs. Springer.** (Chapter 2 *Transverse Ising Chain (Pure System)*, pp. 17–49) | `10.1007/978-3-540-49865-0` | OpenAlex `closed`, `best_oa_location=null`; the Springer landing page carries `<meta name="access" content="No">`. **Body text: 0 obtained; only a site-side chapter abstract truncated at "Before…" was obtained** |

The chapter abstract of C2, verbatim (**the only "body-side" text we obtained**; 0 extrapolation):

> "Following the duality of the two dimensional Ising model on square lattice [2.1], one can show [2.2] the self-duality, and thereby make exact estimate of the critical tunnelling (transverse) field of the one-dimensional spin-1/2 transverse Ising model. Before…"

> That abstract contains **0 equations, 0 equation numbers, 0 definitions of `K`/`Γ`** ⇒ we **do not assert here that the form of the equation is fabricated**, and **0 infer anything from the abstract**.

### §3.3 Current status of the provenance of the equation (**honest statement**)

| Basis | Layer | Status |
|---|---|---|
| (i) self-implementation + self-check inside our repository's `#12` | **self-proved within this repository** (residual ≤ `2.220446049250313e-16`; closed form vs bisection ≤ `4.440892098500626e-16`) | **recomputable** |
| (ii) "the standard textbook conclusion" | **no source** (self-declared in existing documents) | **still no source** |
| (iii) C1 Pfeuty 1970 | literature candidate | **body text 0 obtained, page / equation number = `null`** |
| (iv) C2 Chakrabarti–Dutta–Sen 1996 | literature candidate | **body text 0 obtained, page / equation number = `null`** |

⟹ **To this day the equation remains "self-proved in this repository plus a sourceless textbook layer."** If you have a channel to full text (institutional subscription, interlibrary loan, the authors themselves, etc.), **that is exactly what this commission seeks.**

### §3.4 Internal-consistency test of the in-repository declaration triple (**a refutation**; our derivation, 0 re-adjudication of `#12`)

Test 1 (algebraic simplification): `sinh(βJ/2)·sinh(βh/2) = 1`.
Test 2 (`T→0` limit): as `β→∞` both parameters diverge simultaneously ⇒ **no solution for any** `h_c > 0`; the only branch gives `Γ_c ≈ e^{-βJ/2} → 0`, i.e. `h_c → 0`.
**More generally**: taking **any** finite generating factor `K = c_K·β·J`, `Γ = c_Γ·β·h`, the same argument gives `h_c → 0`.

> ⟹ **No β-dimensional rescaling pair of `K`, `Γ` can make `sinh(2K)·sinh(2Γ)=1` a TFIM critical line compatible with §2.2.** The correct correspondence must additionally contain a **layer-spacing Δτ factor** — which is exactly where the breakpoint of §2.3 lies.

The closed form of `#12` itself, `h_c/J = 2·t_rel·asinh(1/sinh(1/(2·t_rel)))`, measured by us:

| `t_rel = k_BT/J` | 10 | 3 | 1 | 0.5 | 0.2 | 0.1 | 0.05 | **0.01** |
|---|---|---|---|---|---|---|---|---|
| `h_c/J` (`#12` closed form) | `7.378176e+01` | `1.492331e+01` | `2.813658e+00` | `7.719368e-01` | `6.581609e-02` | `2.695220e-03` | `9.079986e-06` | **`7.714999e-24`** |

Whereas §2.2, under `#12`'s **own convention** (`c_ferro = J/4`, `c_trans = h/4` ⇒ `h_c = c_ferro = J`), gives **`h_c/J = 1`**.

> ⟹ **That declaration triple cannot reproduce the model's own zero-temperature critical point; the deviation diverges as `T→0`.**

**Boundary declaration**: the above is a **consistency test at the derivation layer**; it is **not a re-adjudication of `#12`** (`#12`'s grading is 0-touched; adjudication belongs to our verdict-keeper).

---

## §4 The three questions for the addressee

> **Q1 (derivation)**: please independently derive the generating factor for "transverse-field term → interlayer coupling" in the Trotter–Suzuki-type quantum↔classical correspondence: write out the complete algebra, state the normalization conventions it depends on (how the Hamiltonian coefficients become classical couplings, how the layer spacing Δτ enters, whether the spin operators are Pauli or S=1/2), and from this give the definition factors of `K`, `Γ` relative to `c_ferro`, `c_trans`. **Every step of the derivation must be checkable.**
>
> **Q2 (source)**: please give the **original source** of the 1D TFIM exact critical equation (of the form `sinh(2K)·sinh(2Γ)=1`, or an equivalent `h_c(T)` form): bibliography + page number + equation number + **verbatim text** (including how that paper itself defines `K`, `Γ`, and how it normalizes the Hamiltonian coefficients).
>
> **Q3 (provenance tracing · the PI explicitly asked "find out whose proposal it is")**: please trace the **original proposer / source** of the triple declaration of §2.6 (`H = -(J/4)Σσ^zσ^z - (h/4)Σσ^x`; `K ≡ βJ/4`, `Γ ≡ βh/4`; `t_rel ≡ k_BT/J = 1/(4K)`) — which paper, which community's convention, or which school of writing. If it cannot be found, please write honestly "cannot be found", and list **which channels you searched**.

The three questions may be answered independently. **If any one of them is unobtainable under your conditions, it suffices to write "unobtainable + the list of channels already searched + what is still missing" — "I could not find it" is acceptable reply content; "let me guess" is not.**

---

## §5 Evidence-document index (fingerprints and paths only; consult the originals as needed)

| # | Document | SHA-12 (measured on our machine, 2026-09-28) | Bytes | How to open |
|---|---|---|---|---|
| 1 | `results/_v4_rj5_rederive_2026_09_28.md` | `34ec49511ee3` | 22,145 | **main breakpoint document**: §1 anchor verification / §2 the four retrieval documents / §3.1–§3.5 step-by-step derivation / §4 three-anchor-point measurement / §5 three-gate self-check / §7 narrowings R/S/T/N / §8 honest declaration |
| 2 | `results/_v4_rj5_rederive_appendix_2026_09_28.md` | `985673661209` | 9,226 | **numerical appendix**: A two-dimensional classical critical-line values / B the three criteria for the 1D TFIM and the full scaling-ratio table / C items excludable from the breakpoint / D the full `#12` closed-form table / E verbatim counts at the three anchor points / F the 14-attempt retrieval ledger and the mechanical `sinh` count |
| 3 | `results/_v3_recheck_12_executor_2026_09_27.py` | `4850b1cbb010` | 49,430 | **source of the §2.6 triple verbatim**: `:114-122` erratum within this document / `:124-125` `TFIM_CONVENTION` / `:128-130` residual / `:133-148` closed form |
| 4 | `results/_v3_recheck_12_rj5_provenance_2026_09_27.md` | `20f15c49feb5` | 23,822 | **preceding full-text retrieval and source verification**: §1 line-by-line networking list / §1.1 availability across four channels / §2.2 inventory of bases / §2.3 the conditional form of γ-R1 / §2.4 the one-line falsification test / §3 line-by-line comparison with `#12` / §4 R-1–R-6 |
| 5 | `results/_v3_recheck_12_jsv_check_2026_09_27.md` | `2b9e886e729d` | 14,525 | **traceability-failure register J-1**: JSV 1999 does not exist in the V3 source documents; the C1/C2/C3 bibliography and DOIs are on disk |
| 6 | `results/_v4_gamma_r1_prereg_2026_09_28.md` | `02c072833cca` | 32,186 | **the §2.3 reading formula and the three kill-lines** (the literal wording `K-GR1-1/-2/-3/-4/-5`, **0 modification**) |
| 7 | `results/_v4_gamma_r1_exec_2026_09_28.md` | `0d946e65ba3c` | 21,496 | γ-R1 execution document (the per-source reading process over the four documents) |
| 8 | `results/_v4_gamma_r1_sources_20260928_S1.md` | `3d6e997aa692` | 2,944 | per-source record for Yu & Chakravarty (**verbatim excerpts of the original**) |
| 9 | `results/_v4_gamma_r1_sources_20260928_S2.md` | `dcec110ca2e0` | 2,647 | per-source record for Ma, Xu & Wang (verbatim excerpts of the original) |
| 10 | `results/_v4_gamma_r1_sources_20260928_S3.md` | `6b9761d710ca` | 2,554 | per-source record for Xiong & Wang (verbatim excerpts of the original) |
| 11 | `results/_v4_gamma_r1_sources_20260928_S4.md` | `16af6baf8463` | 3,050 | per-source record for Zhang & Ding (verbatim excerpts of the original) |
| 12 | `deposon_team/plugins/boss_pc_2_transverse_field_ising.py` | `210105a7f29a` | 7,053 | **the upstream literal source of §2.6**: `:30` `PFEUTY_H_C_OVER_J = 1.0` |
| 13 | `docs/Deposon_Requirements_v1.md` | `ee33f3f22e1b` | 13,914 | deposon definition anchor point 1 (**no** `K ≡ βJ/4` declaration) |
| 14 | `README.md` | `18e095c85427` | 3,756 | deposon definition anchor point 3 (`:5` three-channel scattering + ether + unitarity statements) |

> The index gives **fingerprints and paths only**; for the full reasoning of each document, consult the originals directly using the guidance above. **This commission does not transcribe the full reasoning text** (the derivations and verbatim excerpts needed for you to form a judgement have all been given in §2).

---

## §6 Reporting requirements

1. **Every derivation step must be checkable**: each step of Q1 must state its basis and the conventions used; where a step is skipped, **write "step skipped" explicitly** — 0 completion into "obviously".
2. **Sources quoted verbatim**: every citation in Q2 / Q3 must give **bibliography + page / equation number + verbatim text** (including that paper's own notation). **If page / equation numbers cannot be obtained, write `null`; 0 fabrication.**
3. **0 reverse-inference from abstracts**: where only an abstract is available, it may be cited as a **lead surface**, but **0** inference of body-text equations or definition factors from an abstract.
4. **If you cannot find it, say you cannot find it**: write "unobtainable" honestly and attach a **list of channels already searched**; "I could not find it" is a qualified reply, "let me guess" is not.
5. **Guard against homonymous symbols**: if the `Γ` you encounter denotes a **dissipation rate / noise linewidth / generalized Grüneisen ratio / scattering linewidth**, or any other homonym with a different meaning, please **state that explicitly** and exclude it (see the trace kept in §2.5 S4).
6. **0 adjudication in any form**: the reply **does not take effect automatically**; whether and when it is adopted is decided by the PI.
7. **The structure and level of detail of the reply are for you to decide** — following the PI's ruling of 2026-09-24, "commissioning materials contain no outline; the addressee is left free to develop it", this commission **prescribes no reply sections and requires no particular layout**; structured and recomputable is enough.
8. **The reply shall carry its own SHA-12**, following the established reply convention (structured + recomputable); a suggested name is `letters/_v5_rj5_external_rederive_reply_<addressee>_<YYYY_MM_DD>.md` (to be fixed at forwarding time).
9. **Anti-downgrade clause — declare the model actually used (mandatory)**: if your reply was produced by a large language model — in particular if it was produced through a **gateway, proxy, router or reseller** (for example teamorouter or a similar intermediary), or is **otherwise not traceable to a specific model build**, then the reply **must state, in a clearly marked block, the model name and the full version identifier actually used to produce it** (for example the vendor prefix and the dated or numeric build string exactly as the serving endpoint reports it), together with: the serving endpoint (host), the model string requested at the endpoint, and the date of the call. If the reply is **not** model-produced, write that explicitly instead. A reply that omits this declaration, or that we find on reception to have been served by a model other than the one declared, **will be registered as an unverifiable reply and will not be entered into our evidence chain**; we compare the declaration against the model metadata recorded in the forwarding request (`request.model`). This clause exists because a reply that silently downgrades to a weaker model would be misleading; declaring the model costs the addressee little, while an undeclared downgrade misleads.
   - Minimum acceptable declaration block (the addressee may add anything further):

     ```
     Model actually used:  <vendor/model-name + full version or build identifier>
     Serving endpoint:     <host[:port]>
     Model string requested at the endpoint: <exactly what was requested>
     Date of the call:     <YYYY-MM-DD HH:MM TZ>
     If not model-produced, write: "Not produced by a language model" + a one-line description of the method.
     ```

---

## §7 Boundaries (strictly observed)

- **0 modification of existing documents**: this letter is a purely new file; all 14 documents of §5 are **0 bytes changed**, and we ask the addressee likewise to read only.
- **0 unauthorized threshold changes**: the γ-R1 preregistration §3 kill-lines / §6 STOP conditions / §8 thresholds, and all preregistered constants of `#12` (`TOL_STRICT` / `TOL_LOOSE` / `PFEUTY_H_C_OVER_J`) are **carried at their existing literal wording, not one character altered**.
- **0 new external literature identifiers**: this letter **adds 0** literature identifiers / DOIs / volume-issue-page data not measured by us; the C1 / C2 bibliography and DOIs in §3.2 are **transcribed verbatim** from our existing documents.
- **0 merging of derived data**: this commission **adds 0 JSON and modifies 0 existing JSON**.
- **Keys**: this commission is unrelated to any API key; **no reply shall contain a plaintext key**.
- **Registration method**: the addressee's conclusions will be registered into the deposon evidence / erratum chain **in quoted form**, and **shall not be certified under the addressee's name** (honest attribution: the conclusion belongs to the addressee's judgement; registration and execution belong to the various Mavis team agents).
- **Attribution boundary**: the **drafter of this letter = the Mavis team doc-writer** (`agent-0032834a3e04`), the **commissioning party = the PI**; the reply is issued **under the addressee's own name**, and **0** impersonation of worker / verdict-keeper / evidence-auditor / protocol-keeper / Trae code or any other party's name.
- **Answer-hint check**: the two candidate values of §2.3 are **side by side, 0 weighted, 0 ranked, 0 tendency implied**; narrowings R/S/T of §2.4 are explicitly marked **"a derivation product, not a conclusion"**.
- **Counterpart-version rule**: this English letter and the Chinese original `letters/_v5_rj5_external_rederive_request_2026_09_28.md` (`cfd58ae66463`, 31,381 bytes) are mutual counterpart versions. The Chinese original was drafted first and this English version is a faithful full translation of it. **In the event of any discrepancy, the Chinese original together with the upstream documents as measured on disk governs**, and the discrepancy shall be registered in the erratum chain rather than silently reconciled.

---

## §8 Deadline

- We suggest a reply within **5 working days** (relaxed relative to previous commissions, because this one includes full-text-level source tracing); if you need longer, please say so in advance.
- This letter is **pending PI review and forwarding**; the moment of forwarding is the moment the commission takes effect.

---

## §9 Honest declaration for this letter (drafting side)

1. **Skill and fallback (honestly declared)**: for this English version this drafting session **actually loaded** the locally registered skill `scientific-writing` (K-Dense Inc., `〔本机用户目录〕/.minimax/skills/scientific-writing/SKILL.md`) and adopted the clauses relevant to this letter: **report measured values exactly, distinguish observation from inference, make tables self-sufficient with complete headers, acknowledge uncertainty, keep terminology consistent**. That skill's "a graphical abstract is mandatory / multiple figures must be generated" clauses target **journal papers**; this letter is a **commission letter**, so they were **not applied** (0 fabrication of figures for this letter). The work order **did not name** a specific skill plugin, so there is **no "Local skill not found" event to report**. **0 fabrication of skill instructions.**
2. **Layout and clause discipline anchor**: follows the layout of the existing letters (anchor documents `letters/_v3_recheck_indep_judgment_request_2026_09_27.md`, `2c486c1791d5`, 22,702 B, measured as present on disk; and `letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md`, `0e7600ac4478`, 7,510 B). **0 fabrication of layout.**
3. **0 fabrication**: every numerical value in §2.1 / §2.2, the verbatim breakpoint text of §2.3, the narrowings of §2.4, the four verbatim source excerpts of §2.5, the verbatim triple of §2.6, and all readings and bibliography in §3.1–§3.4 are **transcribed verbatim from documents on disk or read directly from the source lines**; all SHA-12 values and byte counts in §5 are **measured** on our machine with `Get-FileHash` on 2026-09-28 (14 documents checked one by one).
4. **Anchor entity not located (honestly registered, not falsely reported)**: the entity `Deposon_凝子_统一场论研究报告_v1.pdf` was **not located** by recursive search over `deposon-repo` / `deposon-sub` / `_non_upload_local_archive` (only `Deposon_凝子_统一场论报告_一致性核对_20260907.md` was hit, `125998731621`, 3,441 B). The character counts and verbatim excerpts for that PDF in §2.7 were **transcribed from the R-J5 documents** and **were not independently re-extracted by this letter** — this is flagged in §2.7, and **we do not assume it is on disk**.
5. **Surfaces not checked (honest declaration)**: this letter **did not check the full implementation of the `#12` executor line by line** (only the relevant region `:114-148` was read); **did not rerun any experiment**; **did not access the network** (the C1 / C2 availability and the 14-attempt ledger are transcribed from our existing documents, not measured by this letter).
6. **0 outline (the PI's explicit ruling of 2026-09-24)**: this commission **contains no reply outline** and **prescribes no reply sections and no particular layout** (§6 item 7); the source ledger is given in full and the structure is for the addressee to decide.
7. **0 presupposition of the answer**: the two candidate values of `r` are stated side by side, **0 hinted, 0 weighted, 0 ranked**; **0 substitution of a prediction on behalf of the PI** (following our existing literal wording "without the body text in hand, no prediction is permitted").
8. **Rendering convention (so that the style is not misread)**: this letter keeps the house convention of writing **"0"** before a noun to mean **"not a single" / "none"** (e.g. 0 breakpoints = no breakpoint at all, 0 fabrication = nothing fabricated). This is a literal carry-over from the Chinese original and is **not** the number zero in a mathematical expression. **All digits inside formulas, numerical tables, hashes and bibliographic entries are carried verbatim and are never part of this convention.**
9. **This English version is a translation, not a re-derivation**: no new physics was introduced by the translation; the terminology follows the standard usage of the field (Trotter–Suzuki decomposition / quantum↔classical correspondence; transverse-field Ising model (TFIM); transverse field; Jordan–Wigner transformation; Kramers–Wannier duality; self-dual point; Pauli matrices; asinh / sinh / cosh; Grüneisen ratio; Feshbach resonance). Where the source Chinese contains a term with no standard English equivalent, the original wording is retained in Chinese alongside the English. **No term was invented.**
10. **Translation risks honestly declared**: (i) the PI's verbatim authorization quote in the header is given in Chinese with our English rendering attached, and the Chinese governs; (ii) the Chinese full-width punctuation inside the `TFIM_CONVENTION` code block of §2.6 is **retained as-is**, since it is source code copied verbatim and altering it would break fidelity; (iii) §2.5, §2.6 and §3.4 contain verbatim quotations from published papers, from source code and from Chinese internal documents; where the source is English it is reproduced **exactly as extracted**, including ligatures and hyphenation breaks, so that the quoted text is **not** a cleaned-up version of the paper's wording.
11. **Counterpart version and consistency**: this English letter is the counterpart of `letters/_v5_rj5_external_rederive_request_2026_09_28.md` (`cfd58ae66463`, 31,381 bytes, verified on our machine 2026-09-28), whose SHA-12 was **re-measured before this translation began and confirmed unchanged**. All mathematical formulas, hashes, numerical values and bibliographic entries have been carried verbatim; the structural correspondence of each section is 1:1 with the Chinese original. See §7 "Counterpart-version rule".
12. **Mechanical byte-level consistency verification actually run (not asserted)**: before signing off, a byte-level comparison of this English file against the Chinese original was run on the drafting machine. Results: **23 twelve-hex fingerprint tokens in the Chinese original, all 23 present here**; **116 distinct decimal-number tokens in the Chinese original, all 116 present here** (the only extra numerals here are `31` and `381`, from the Chinese file's byte size `31,381`, and `18` / `40`, from the PI instruction timestamp `2026-09-28 18:40`); **all 10 arXiv identifiers, DOIs, URLs, page ranges and questionnaire ids present, verbatim**; **all four verbatim quotations from S1–S4 byte-identical**, including the ligature `ﬁ`, the hyphenation break `Bril- louin`, the truncated `…As is well known` and the truncated C2 abstract `Before…`; **all nine fenced code blocks of the Chinese original present here**, of which **5 are byte-identical** and **4 differ only in the Chinese annotation labels described in §10.1**. Scripts used: `.tmp/_en_verify_2026_09_28.py`, `.tmp/_en_verify2_2026_09_28.py`, `.tmp/_en_verify3_2026_09_28.py`, `.tmp/_en_verify4_2026_09_28.py`, and the final acceptance check `.tmp/_en_final_2026_09_28.py` (all five re-runnable; they read only and modify nothing).
13. **Format**: UTF-8 without BOM; LF line endings; the SHA-12 of this file upon landing is reported alongside (a file cannot contain its own hash).
14. **Version**: v0.1 of the English version (first version; there is no earlier English version to overwrite). Later revisions will be issued as v0.2 / v1.0 and **will not overwrite this file**; the Chinese original `cfd58ae66463` is likewise **0-touched**.
15. **0 verdict, 0 re-adjudication, 0 substitution of adjudication**: this letter **issues no verdict** and **0 modifies** the grading of `#12`, the three γ-R1 branches, or any wording of any preregistration.
16. **New clause added relative to the Chinese original**: §6 item 9 (the anti-downgrade clause requiring the reply to declare the model name and version actually used) was **added on the PI's instruction of 2026-09-28 18:40** and exists **only in this English version**; the Chinese original does not contain it. Since the English version is the one intended for forwarding to a model-mediated addressee, **if the two versions are ever forwarded together, this clause should be read as binding.** This difference is registered here rather than silently back-ported into the Chinese original (which is 0-touched by iron rule).

---

## §10 Consistency statement and zero-product declaration (closing section)

**Consistency statement.** This English file `letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md` is the English counterpart of the Chinese original `letters/_v5_rj5_external_rederive_request_2026_09_28.md` (SHA-12 `cfd58ae66463`, 31,381 bytes, measured on the drafting machine on 2026-09-28). Every mathematical formula, hash string, numerical value, bibliographic entry and verbatim quotation has been carried verbatim; §0–§9 of this file correspond 1:1 to §0–§9 of the Chinese original, with the sole exception registered in §9.16 (the anti-downgrade clause, which exists only in this English version by the PI's instruction). **In the event of any discrepancy, the Chinese original together with the upstream documents as measured on disk governs**, and the discrepancy shall be registered as an appended erratum line rather than silently reconciled. **The Chinese original is 0-touched (0 bytes changed).**

**§10.1 Translated-label category (disclosed, so that "verbatim" is not over-claimed).** The consistency statement above covers mathematical symbols, formulas, hashes, numbers, bibliographic entries and verbatim quotations. It does **not** extend to **Chinese annotation labels**, which had to be rendered into English for an English letter. Exactly **four** fenced code blocks of the Chinese original contain such labels, and in all four **every symbol, number, filename and column-alignment space is byte-identical** — only the Chinese wording of the label differs:

| Block | Chinese original (label) | This English version (label) | Everything else |
|---|---|---|---|
| §2.1 | `校验` / `恒等` | `check` / `identity` | byte-identical |
| §2.2 | `钉住校验：` / `标度比` / `极小` / `铁磁隙正确非零` | `pin check:` / `scaling ratio` / `minimum` / `ferromagnetic gap correctly non-zero` | byte-identical |
| §2.3 | the four Chinese glosses after `K_lit ≡`, `Γ_lit ≡`, `c_ferro ≡`, `c_trans ≡` | the same four definitions in English | byte-identical |
| §2.7 | `无 K/Γ/J/h 的伊辛学声明` / `全为` / `无 Ising / 无 K / 无 Γ` | `no Ising-theory claim about K/Γ/J/h` / `all of them` / `no Ising / no K / no Γ` | byte-identical |

The remaining **five** fenced code blocks of the Chinese original are byte-identical here, **including** the `TFIM_CONVENTION` Python block whose full-width Chinese punctuation is deliberately left unaltered (see §9.10 (ii)). **The term "anharmonic oscillator" does not occur in the source document and has deliberately not been introduced here; 0 addition.**

**SHA-12 of this English file.** SHA-12 is defined as `hashlib.sha256(data).hexdigest()[:12]` in lowercase. A file cannot contain its own hash, so the measured SHA-12 of this English file is reported **outside** the file, alongside its delivery (the Chinese original handles the same issue in the same way — see its §9 item 8, "the landing SHA-12 is reported alongside; a fingerprint at the moment of birth"). **Stated here rather than claimed: this file contains no self-hash placeholder that has been filled in after the fact, and no hash value in this letter has been written without measurement.**

**Zero-product declaration (drafting side).** This letter is a **pure translation and re-layout into English** of an existing Chinese commissioning document plus the single registered addition of §6 item 9. It produced **0 new experiments**, **0 new numerical readings**, **0 new literature identifiers**, **0 new JSON or other derived data**, **0 modification of any existing document** (the Chinese original and all 14 evidence documents of §5 are **0 bytes changed**), **0 change to any threshold**, and **0 verdict**. Nothing in this letter was inferred, estimated, reconstructed or completed on the addressee's behalf; where the source is unknown, this letter writes "unknown", and where an entity could not be located on disk, that is declared rather than glossed over. **No external call of any kind was made**: 0 LLM calls, 0 URLs fetched, 0 API keys read or written, 0 network access; the four verification scripts named in §9.12 read local files only.

---

**Status**: pending PI review and forwarding; it takes effect and locks at that moment.

Issued by | the Mavis team doc-writer (`agent-0032834a3e04`) | 2026-09-28 | English counterpart of `letters/_v5_rj5_external_rederive_request_2026_09_28.md` (`cfd58ae66463`)
