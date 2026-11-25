# Independent External Analysis Reply — deposon Project / G-E01 Theory-Input Face (T1–T4)

> **In reply to**: `〔幽灵引用·原件已缺席·未上传:LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md〕` (SHA-12: `70fe266e87d6`, 8,361 bytes, 75 lines).
> **Scope & Compliance**: Analysis-only reply per §7 item 5. **0** project code files modified, **0** experiments executed on your behalf, **0** uploads performed. All standing constraints in §2 (frozen kill-lines before measurement, reproducibility with explicit derivations, model disclosure, dimension discipline, and anti-degeneracy registration) are strictly respected.

---

## §0 Model & Tool-Call Disclosure (§2 Item 3 & §7 Item 2)

```text
Addressee on commission header: Gemini 4
Assistant identity & model disclosure: I am an AI assistant using Copilot SDK in VS Code.
Exact serving model/version string: Unavailable to this assistant runtime from inside the session; verify against host/forwarding metadata.
Date of reply: 2026-10-15 (Asia/Shanghai, UTC+08:00)
```

**Tool calls made during preparation of this reply**:
1. Read-only file inspection (`view` / `grep`) of the commission letter `〔幽灵引用·原件已缺席·未上传:LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md〕` and referenced local context (`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` [`423c84de20d5`], `tools/distortion_calculator.py`, `tools/exp_harness.py`, `results/_m41_verdict_kd_effect_register_2026_10_15.md`, `results/_external_commission_gemini4_ge01_theory_inputs_2026_10_15_draft.md`, and prior C4 replies in `〔本地绝对路径·脱敏略:codex-workspace〕\`).
2. One local read-only Python SHA-256 check (`powershell` running `hashlib.sha256`) to record the exact fingerprint of `LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` (`70fe266e87d6`, 8,361 B, 75 lines).
3. File creation (`create`) of this reply markdown file only. No existing file in `_repo_mirror` was modified.

---

## §1 Task T1 — $\varepsilon^*$ for the Kill-Line Track (BL-2)

### 1.1 Algebraic Structure & Why $\varepsilon^*$ Governs the Verdict
In the P-B specification (`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`, §3.4 & §4.1) and the exact rational implementation (`tools/distortion_calculator.py`, L3), per-cell distortion is the expected rejected-decision count over a horizon of $H$ decisions per cell (with per-decision payoff cap $c = \max_u = 1$ and binary payoff domain $\{0,1\}$):
$$D(M, T) = \mathbb{E}_{\pi}\!\left[\sum_{t=1}^{H} \mathbf{1}\{A_t \notin K_t\}\right] \in [0, H], \qquad R(M, T) := \frac{D(M, T)}{H} \in [0, 1].$$

The distortion multiplier is defined as:
$$\text{mult}(M, T) = \frac{D_{\text{LLM}}(M, T)}{\max\!\left(D_{\text{Bayesian}}(M, T),\, c \cdot \varepsilon^*\right)}.$$

Because the Bayesian baseline player is defined as a zero-distortion oracle ($D_{\text{Bayesian}}(M, T) \equiv 0$, Spec §1 L12 & §3.1), the denominator is **identically trapped on the guard branch** $\max(0, \varepsilon^*) = \varepsilon^*$ (for $c=1$). Consequently:
$$\text{mult}(M, T) = \frac{D_{\text{LLM}}(M, T)}{\varepsilon^*} = \frac{H \cdot R_{\text{LLM}}(M, T)}{\varepsilon^*}, \qquad \overline{\text{mult}} = \frac{H \cdot \overline{R}_{\text{LLM}}}{\varepsilon^*}.$$

Against the frozen kill-decision thresholds in `kill_decision` (Spec §4.3 L103–110):
- **$\text{FAIL\_H0}$ (kill)**: $\overline{\text{mult}} \ge 2.0$ (or `theory_U_hit_rate >= 0.3`)
- **$\text{PASS\_H1}$ (close)**: $\overline{\text{mult}} \le 1.5$ and $\text{ci\_hi} \le 1.8$ (and `theory_U_hit_rate <= 0.1`)
- **$\text{GRAY}$**: $1.5 < \overline{\text{mult}} < 2.0$ (or CI crosses boundary)

### 1.2 Dimension Analysis & Why $\varepsilon^*$ Must Differ from the Self-Check $\varepsilon = 0.1$
Under the standing dimension discipline (§2 Item 4):
1. **If $D$ is an extensive count over $H$ decisions** ($D \in [0, H]$, as enforced in `distortion_calculator.py` B10: *"D 之量纲 = 计数 (可取值区间 [0, H])"*), then $\varepsilon^*$ in $\max(D_{\text{Bayesian}}, \varepsilon^*)$ **must have the dimension of a decision count per cell** (i.e., scale linearly with $H$: $\varepsilon^*(H) = H \cdot \varepsilon_{\text{rate}}^*$).
2. **Why the self-check $\varepsilon = 0.1$ fails on the count scale**:
   - In the calculator self-check track, $\varepsilon = 1/10$ is an **unscaled scalar** designed to verify the guard-branch algebra (`G_L = 2, G_B = 0, eps = 0.1 => 20` for $c=1$ and `10` for $c=2$).
   - If an unscaled $\varepsilon^* = 0.1$ is plugged into a count-scale numerator $D_{\text{LLM}} = H \cdot R_{\text{LLM}}$, then for $H = 15$ (M-41) and the observed error rate $\overline{R}_{\text{LLM}} = 1/10$, we get $D_{\text{LLM}} = 1.5$ and:
     $$\overline{\text{mult}} = \frac{1.5}{0.1} = 15.0 \gg 2.0 \implies \text{automatic FAIL\_H0}.$$
   - Even a near-perfect model making **one single error across $H=25$ decisions** ($R = 0.04$, $D = 1$) yields $\text{mult} = 1 / 0.1 = 10.0 \ge 2.0$ ($\text{FAIL\_H0}$). Any non-zero error count $D \ge 1$ automatically triggers $\text{FAIL\_H0}$ whenever $\varepsilon^* \le 0.5$ on the count scale!
3. **Conversely, if $D$ is reported as a normalized rate $R \in [0, 1]$** (as in Task T3's Context note: *"reports only the raw error rate D (rejected-decision rate)"*), then $\varepsilon_{\text{rate}}^* = 0.1$ means a baseline reference error rate of $10\%$:
   - $\text{PASS\_H1}$ ($\overline{\text{mult}} \le 1.5$) $\iff \overline{R}_{\text{LLM}} \le 1.5 \varepsilon_{\text{rate}}^* = 0.15$ ($15\%$ error rate, with 95% CI upper bound $\le 18\%$).
   - $\text{FAIL\_H0}$ ($\overline{\text{mult}} \ge 2.0$) $\iff \overline{R}_{\text{LLM}} \ge 2.0 \varepsilon_{\text{rate}}^* = 0.20$ ($20\%$ error rate).

### 1.3 Principled Selection Rule & Recommendation for $\varepsilon^*$
Because $D_{\text{Bayesian}} \equiv 0$, $\varepsilon^*$ is **not** a small numerical-stability regularizer; it is the **reference baseline distortion budget** defining $1.0\times$ nominal distortion. A single number cannot be derived from pure logic without specifying the tolerated baseline error rate $r_0 \in (0, 1)$, so we give the exact **dimensionally consistent selection rule** and recommended preregistered anchor:

$$\boxed{\varepsilon^*(H) = r_0 \cdot H \quad \text{(on the count scale } D \in [0, H]\text{)}, \qquad \text{or} \qquad \varepsilon_{\text{rate}}^* = r_0 \quad \text{(on the rate scale } R \in [0, 1]\text{)}}$$

where $r_0$ is the preregistered nominal baseline error rate:
- **Recommended default rule**: Set **$r_0 = \frac{1}{10} = 0.10$**, which translates to:
  - **On the count scale (`distortion_calculator.py` input)**: **$\varepsilon^*(H) = \frac{H}{10}$** (e.g., $\varepsilon^* = \frac{3}{2} = 1.5$ for $H=15$; $\varepsilon^* = \frac{5}{2} = 2.5$ for $H=25$; $\varepsilon^* = \frac{33}{10} = 3.3$ for $H=33$).
  - **On the rate scale ($R = D/H$)**: **$\varepsilon_{\text{rate}}^* = \frac{1}{10} = 0.10$**.
- **Justification**:
  1. **Preserves the exact numeric meaning of the self-check constant $0.1$** as a $10\%$ per-decision error rate while fixing the missing factor of $H$ required by dimension discipline (§2 Item 4).
  2. **Granularity floor**: On a finite horizon $H$, the minimum non-zero error count in a single cell is $1$ decision ($R = 1/H$). For $\text{PASS\_H1}$ ($\text{mult} \le 1.5$) to admit at least $1$ error per cell without automatic failure, $\varepsilon^*(H)$ must satisfy $\varepsilon^*(H) \ge \frac{2}{3}$. Setting $\varepsilon^*(H) = H/10$ satisfies $\varepsilon^*(H) \ge 1.5 > 2/3$ for all $H \ge 15$.
  3. **Non-degeneracy against random guessing ($M_3$)**: For 4-choice tasks where random guessing has rejection rate $R(M_3) = 3/4 = 0.75$, $r_0 = 0.10$ places random guessing at $\text{mult}(M_3) = 0.75 / 0.10 = 7.5\times \gg 2.0\times$ ($\text{FAIL\_H0}$), while a strong LLM at $R \le 0.15$ achieves $\text{PASS\_H1}$.

### 1.4 Verdict Sensitivity & Failure Modes
For any observed mean rejection rate $\overline{R}_{\text{LLM}}$ (and upper 95% CI $\text{CI}_{\text{hi}}(R)$), the kill-line verdict is a step function of $r_0 = \varepsilon^*(H)/H$:

| Regime of $r_0 = \varepsilon^*(H)/H$ | Condition relative to $\overline{R}_{\text{LLM}}$ | Resulting Verdict | At M-41 global $\overline{R}_{\text{LLM}} = 1/10$ ($D = 1.5$ at $H=15$) |
| :--- | :--- | :--- | :--- |
| **Small $\varepsilon^*$** | $r_0 \le \frac{1}{2}\,\overline{R}_{\text{LLM}}$ | **$\text{FAIL\_H0}$** ($\overline{\text{mult}} \ge 2.0$) | $r_0 \le 0.05$ ($\varepsilon^*(15) \le 0.75$) $\implies \text{FAIL\_H0}$ |
| **Intermediate $\varepsilon^*$** | $\frac{1}{2}\,\overline{R}_{\text{LLM}} < r_0 < \frac{2}{3}\,\overline{R}_{\text{LLM}}$ | **$\text{GRAY}$** ($1.5 < \overline{\text{mult}} < 2.0$) | $0.05 < r_0 < 0.0667$ ($0.75 < \varepsilon^*(15) < 1.0$) $\implies \text{GRAY}$ |
| **CI-boundary $\varepsilon^*$** | $r_0 \ge \frac{2}{3}\,\overline{R}_{\text{LLM}}$ but $r_0 < \frac{5}{9}\,\text{CI}_{\text{hi}}(R)$ | **$\text{GRAY}$** ($\overline{\text{mult}} \le 1.5$, $\text{ci\_hi} > 1.8$) | Depends on bootstrap $\text{CI}_{\text{hi}}$ |
| **Large $\varepsilon^*$** | $r_0 \ge \max\!\left(\frac{2}{3}\,\overline{R}_{\text{LLM}},\, \frac{5}{9}\,\text{CI}_{\text{hi}}(R)\right)$ | **$\text{PASS\_H1}$** | $r_0 = 0.10$ ($\varepsilon^*(15) = 1.5$) gives $\overline{\text{mult}} = 1.0 \implies \text{PASS\_H1}$ (if $\text{CI}_{\text{hi}}(R) \le 0.18$) |

- **Failure mode if $\varepsilon^*$ is chosen too small** (e.g., unscaled $\varepsilon^* = 0.1$ on the count scale, or $r_0 \ll 1/H$): **Hyper-sensitive / vacuous kill ($\text{FAIL\_H0}$ saturation)**. Even a single discrete mistake ($D=1$) across the cell horizon produces $\text{mult} = 1/\varepsilon^* > 2.0$, making $\text{PASS\_H1}$ mathematically unreachable unless $D_{\text{LLM}} \equiv 0$ (perfect oracle performance).
- **Failure mode if $\varepsilon^*$ is chosen too large** (e.g., $r_0 > 0.375$, i.e., $\varepsilon^*(H) > 3H/8$): **Vacuous pass ($\text{PASS\_H1}$ dilution / anti-degeneracy violation)**. Even the uniform random baseline $M_3$ ($D = 3H/4$ on 4-choice tasks, or $H/2$ on 2-choice tasks) drops below the $2.0\times$ kill threshold (and for $r_0 \ge 0.50$, random guessing passes $\text{PASS\_H1}$), destroying all discriminative power of the harness.

**T1 Verdict**: **derivable (with value/rule: $\varepsilon^*(H) = H/10$ on the decision-count scale $D \in [0, H]$, equivalently $\varepsilon_{\text{rate}}^* = 1/10$ on the per-decision error-rate scale $R = D/H \in [0, 1]$, corresponding to a preregistered $10\%$ nominal baseline error rate; an unscaled $\varepsilon^* = 0.1$ on the count scale violates dimension discipline and causes vacuous FAIL\_H0 for any $D \ge 1$)**

---

## §2 Task T2 — `null-L` / `null-U` (Theory Inputs `T-2` / `T-3`)

### 2.1 Assessment of `T-2` (`null-L`: Minimal Distortion under Information Restriction)

#### (a) Derivability under Stated Constraints (Simultaneous L-1 through L-5)
Under the exact on-disk state and simultaneously enforced five-level criteria (L-1 through L-5), **`T-2` (`L(M, T)`) is underivable as a non-degenerate empirical bound** for the following three independent obstructions:
1. **Obstruction 1 — Missing empirical observation law (blocks L-1 & L-4)**: There are `0` LLM intermediate observation records $z$ on disk. Therefore, the finite conditional observation table $Q(z \mid x)$ cannot be estimated or verified from historical data; it can only be stipulated *by design*.
2. **Obstruction 2 — Full-information exposure in $M_1$ and $M_2$ (blocks L-5 on 10/15 cells)**: In `tools/exp_harness.py`, both `DeposonMechanism.choose` (L75) and `GreedyMechanism.choose` (L97) receive the full task dictionary `p` as `context` and directly read `context.get('value', {})`, which encodes the ground-truth key $K_t$. Thus, for $M_1$ and $M_2$, the observation channel is the noiseless identity channel $Q_{\text{id}}(z \mid x) = \mathbf{1}\{z = x\}$. Over any strategy class containing the greedy argmax rule, the exact minimum distortion is **structurally zero**:
   $$L(M_1, T_k) = 0, \qquad L(M_2, T_k) = 0 \qquad (\forall k \in \{1,\dots,5\}).$$
   By L-5 (and §2 Item 5, anti-degeneracy), these **10/15 cells must be registered as `structural zero`**, not presented as non-trivial lower-bound solutions.
3. **Obstruction 3 — Strategy-class mismatch on $M_3$ vs. LLM rules (blocks L-2, L-3, L-5 on remaining 5/15 cells)**:
   - In `exp_harness.py` (L108), `RandomMechanism.choose` ignores `context` completely (erasure channel $Q_{\text{null}}(z_0 \mid x) = 1$) and forces uniform random sampling over `options`. For a 4-choice task with $|K_t|=1$, its exact expected distortion is $D(M_3, T) = \frac{3}{4}H$ (and for 2-choice `T3_Trap` / `T4_2x2` in `exp_harness.py`, $\frac{1}{2}H$). However, §4 explicitly constrains that the reference point **`3H/4` may serve only as a sanity check, never as $L$ or $U$**.
   - Conversely, if $Q(z \mid x)$ is taken to be the rendered natural-language prompt string $z = \text{prompt}(x)$, then for deterministic well-posed tasks ($T_1, T_2, T_4$), $z$ uniquely determines the correct answer $K_t$ ($H(K_t \mid Z) = 0$). Over the unrestricted policy class $\Pi_{\text{full}}$, Fano / Bayes risk gives $\inf_{\pi \in \Pi_{\text{full}}} D(\pi) = 0$ (**structural zero** again, unreachable by bounded-rational LLM rule families). Over a restricted LLM strategy class $\Pi_{\text{LLM}}$, no finite rule table with verified assumption annotations exists on disk (blocking L-2 and L-3).

#### (b) Explicit Construction & Level Satisfaction Check
For completeness, the conditional finite-table Bayes-risk construction (from the prior unblock derivation) proceeds as follows:
- Given finite state space $\mathcal{X}$ with prior $p(x)$, finite observation alphabet $\mathcal{Z}$ with channel $Q(z \mid x)$ ($\sum_z Q(z \mid x) = 1$, $Q(z \mid x) \ge 0$), key map $x \mapsto K(x) \subset \mathcal{A}$ ($\emptyset \neq K(x) \subset \{1,2,3,4\}$), and admissible deterministic decision rules $\Pi_{\text{adm}} \subseteq \mathcal{A}^{\mathcal{Z}}$, the exact single-decision minimum rejection probability is:
  $$r^*(Q, \Pi_{\text{adm}}) = \min_{\pi \in \Pi_{\text{adm}}} \sum_{x \in \mathcal{X}} p(x) \sum_{z \in \mathcal{Z}} Q(z \mid x)\,\mathbf{1}\{\pi(z) \notin K(x)\}.$$
- When $\Pi_{\text{adm}} = \Pi_{\text{all}} = \mathcal{A}^{\mathcal{Z}}$, this reduces by pointwise minimization over $z \in \mathcal{Z}$ (with $0/0 := 0$ on zero-probability observations) to:
  $$r^*(Q, \Pi_{\text{all}}) = 1 - \sum_{z \in \mathcal{Z}} \max_{a \in \mathcal{A}} \sum_{x \in \mathcal{X}:\, a \in K(x)} p(x)\,Q(z \mid x), \qquad L(M, T) = H \cdot r^*(Q, \Pi_{\text{all}}).$$
- **Which levels this satisfies under current constraints**:
  - Satisfies **L-3** (exact mathematical consistency with $\Pi_{\text{all}}$ across $H$ independent decisions) and **L-5** (properly flags $L=0$ under $Q_{\text{id}}$ as `structural zero` and matches the count dimension of $3H/4$).
  - **Fails L-1, L-2, and L-4** on disk unless a specific non-degenerate design channel $Q_{\text{design}}(z \mid x)$ and finite strategy class $\Pi_{\text{adm}}$ are prospectively locked into preregistration.

#### (c) Minimal Constraint Relaxation to Make `T-2` Derivable
To make `T-2` derivable at all 5 levels without violating anti-degeneracy:
1. **Relaxation R-L1 (Prospective Design-Channel Parameterization)**: Explicitly stipulate a non-degenerate $M_1$ scattering observation law $Q_{M_1}(z \mid x; \eta, g_{\text{couple}}, g_{\text{aether}})$ in preregistration (where the player observes a single scattered action sample $z \in \mathcal{A}$ drawn from the $M_1$ T+R+A distribution rather than raw `context['value']`), and define $\Pi_{\text{adm}}$ as the finite set of $4^4 = 256$ observation-to-action maps $\pi: \mathcal{A} \to \mathcal{A}$.
2. **Resulting exact non-degenerate closed form under R-L1**: For a symmetric 4-choice task where $v(a^*) = 1$ and $v(a) = 0$ ($a \neq a^*$), $M_1$ assigns weight $w^* = (1-\eta) + \eta g_{\text{couple}} + g_{\text{aether}}$ to $a^*$ and $w_0 = g_{\text{aether}}$ to each of the 3 incorrect options (for default $\eta=0.5, g_{\text{couple}}=1.0, g_{\text{aether}}=0.1$, $w^* = 1.1$, $w_0 = 0.1$, total $W = 1.4$). The optimal rule in $\Pi_{\text{adm}}$ is $\pi^*(z) = z$, yielding the exact non-degenerate lower bound:
   $$L(M_1, T) = H \cdot \left(1 - \frac{w^*}{w^* + 3 w_0}\right) = H \cdot \frac{3 g_{\text{aether}}}{(1-\eta) + \eta g_{\text{couple}} + 4 g_{\text{aether}}} = \frac{3}{14}H \approx 0.2143 H \in \left(0, \frac{3}{4}H\right).$$
   Meanwhile, $M_2$ ($g_{\text{aether}}=0, \eta=0$) remains registered as `structural zero` ($L(M_2, T) = 0$), and $M_3$ remains registered as the uninformative boundary ($3H/4$ sanity check).

---

### 2.2 Assessment of `T-3` (`null-U`: Mechanism-Specific Convergence Tolerance)

#### (a) Derivability under Stated Constraints (Simultaneous U-1 through U-5)
Under the stated P-B constraints, **`T-3` (`U(M, T)`) is strictly underivable (0/5 levels achievable)**.
- **Fundamental Obstruction**: Criteria U-1 and U-2 require an explicit state transition law $S_{t+1} = F(S_t, A_t, \xi_t)$ with a non-empty state space $\mathcal{S}$ and a convergence certificate toward a target equilibrium/attractor. Criterion U-3 requires a proven mapping from cumulative decision regret $D \in [0, H]$ to the certificate's tolerated perturbation. Criterion §2 Item 4 (dimension discipline) forbids equating a bounded mistake count $D$ with convergence of a state process.
- In `tools/exp_harness.py`, all three mechanisms (`DeposonMechanism`, `GreedyMechanism`, `RandomMechanism`) and all task prompts are **strictly memoryless across $t = 1, \dots, H$**: there is no state variable $S_t$ carried from decision $t$ to decision $t+1$.

#### (b) Explicit Engagement with Routes 甲, 乙, and 丙
1. **Route-甲 (Current memoryless P-B harness)**:
   - **Verdict**: **Concur with internal verdict — structurally unsolvable (0/5 levels: fails U-1, U-2, U-3, U-4, U-5).**
   - **Obstruction**: Because $\mathcal{S} = \emptyset$ (or a trivial singleton), no state transition map $F$ exists (failing U-1), no convergence target or certificate can be defined (failing U-2), and any attempt to declare a static error-count threshold $D \le U$ as a "convergence tolerance" violates dimension discipline (§2 Item 4, failing U-3).
2. **Route-乙 (Redefine "mechanism" via deposon field dynamics $S_{t+1} = F_M(S_t, A_t)$)**:
   - **Verdict**: **Derivable-with-relaxation (requires a definition-level protocol revision to `exp_harness.py` and preregistration; satisfies U-1 through U-5 *only* for coupled field mechanisms $M_1$, while $M_2/M_3$ must be registered as degenerate/uncoupled).**
   - **Construction under Route-乙**:
     - **U-1 (State & Transition Law)**: Equip the harness with a persistent per-cell scalar/vector field state $S_t \in [0, 1]$ (e.g., deposon reservoir/field potential initialized at $S_0$) evolving across decisions $t=0,\dots,H-1$ via the dissipative contraction law:
       $$S_{t+1} = (1 - \gamma)\,S_t + \gamma\,\mathbf{1}\{A_t \notin K_t\}, \qquad \gamma \in (0, 1).$$
     - **U-2 (Convergence Target & Certificate)**: The undisturbed oracle fixed point is $S^* = 0$. The finitely checkable certificate at horizon $H$ is terminal/average field stability: $\overline{S}_H := \frac{1}{H}\sum_{t=1}^{H} S_t \le \tau_{\text{cert}}$ (or Lyapunov contraction $\mathbb{E}[S_H] \le \tau_{\text{cert}}$) for a preregistered stability margin $\tau_{\text{cert}} \in (0, 3/4)$.
     - **U-3 (Proven Mapping from $D$ to Perturbation Tolerance, with Direction & Tightness)**: Taking expectations and summing the linear recursion over $t=0,\dots,H-1$ with $S_0 = 0$:
       $$\mathbb{E}[S_t] = \gamma \sum_{k=0}^{t-1} (1-\gamma)^{t-1-k} \mathbb{P}(A_k \notin K_k) \implies \sum_{t=1}^{H} \mathbb{E}[S_t] = \sum_{k=0}^{H-1} \left(1 - (1-\gamma)^{H-k}\right) \mathbb{P}(A_k \notin K_k) \le \sum_{k=0}^{H-1} \mathbb{P}(A_k \notin K_k) = D(M, T).$$
       With exact tightness: by worst-case adversarial placement of mistakes at the end of the horizon ($k = H-1$) for terminal state $\mathbb{E}[S_H]$, or at the beginning ($k=0$) for average state $\overline{S}_H$, we obtain the tight two-sided bounds:
       $$\gamma(1-\gamma)^{H-1} D(M, T) \le \mathbb{E}[S_H] \le \gamma D(M, T), \qquad \text{and} \qquad \frac{\gamma}{H} D(M, T) \le \mathbb{E}[\overline{S}_H] \le \frac{1 - (1-\gamma)^H}{H} D(M, T).$$
       Hence, guaranteeing the average-field certificate $\mathbb{E}[\overline{S}_H] \le \tau_{\text{cert}}$ for **all** temporal distributions of mistakes (worst-case tight sufficient condition) holds if and only if:
       $$D(M, T) \le U(M, T) := \frac{H \cdot \tau_{\text{cert}}}{1 - (1-\gamma)^H}.$$
     - **Why Route-乙 cannot be applied without relaxation**: It modifies the frozen memoryless execution semantics of `exp_harness.py` (standing constraint §2 Item 1).
3. **Route-丙 (Three mechanisms as perturbation source + borrowing an existing certificate from the 22-graph game protocol)**:
   - **Verdict**: **Underivable / Invalid under U-3 and U-5 (cross-protocol dimensional & domain mismatch).**
   - **Obstruction**: The 22-concept-graph game (`v20_gt` / `v21_gtformal`) operates on a 22-node graph diffusion state space with graph-Laplacian/scattering transitions, whereas P-B tasks ($T_1$ arithmetic, $T_2$ StrategyQA, $T_3$ trap, $T_4$ $2\times 2$ matrix) have no graph topology and no Jacobian/homomorphism mapping a discrete choice error $\mathbf{1}\{A_t \notin K_t\}$ in GSM8K or StrategyQA onto a 22-node graph edge perturbation. Borrowing a numeric threshold from the 22-graph protocol violates U-3 (no proven mapping from P-B regret $D$ to the 22-graph perturbation domain) and §2 Item 4 (dimension/domain discipline).

**T2 Verdict**: **underivable as stated (`T-2` is obstructed by 0 on-disk LLM observation records and full-information `value` leakage making 10/15 $M_1/M_2$ cells `structural zero`; `T-3` is obstructed by memoryless mechanisms having no state process $\mathcal{S}$) / derivable-with-relaxation (for `T-2`: preregister the $M_1$ T+R+A sampling distribution as a noisy design observation channel $Q_{M_1}(z\mid x)$, yielding $L(M_1,T) = \frac{3 g_{\text{aether}}}{(1-\eta)+\eta g_{\text{couple}}+4 g_{\text{aether}}}H = \frac{3}{14}H$ while registering $M_2$ as `structural zero`; for `T-3`: adopt Route-乙 by adding an explicit dissipative field recursion $S_{t+1}=(1-\gamma)S_t+\gamma\mathbf{1}\{A_t\notin K_t\}$ with certificate $\mathbb{E}[\overline{S}_H]\le\tau_{\text{cert}}$, yielding tight tolerance $U = \frac{H\tau_{\text{cert}}}{1-(1-\gamma)^H}$, whereas Route-甲 is structurally unsolvable and Route-丙 fails U-3 cross-protocol domain mapping)**

---

## §3 Task T3 — Independent Review of Dual-Readout Experiment (M-41)

### 3.1 Verification of the Readouts & Concurrence with Diagnoses (a), (b), (c)
First, we cross-check the exact arithmetic from the 60-cell experiment ($4 \text{ families} \times 15 \text{ decisions} = 60\text{ cells}$, $5$ rejected decisions at `T2#03, T2#07, T2#11, T3#01, T4#00`, and $10$ no-action cells all inside `T3_Trap` $\subset C_2 \subset C_1$):
- **No-strip global**: $60$ total $- 10$ no-action $= 50$ valid cells; $5$ errors $\implies R_{\text{LLM}} = 5/50 = 1/10 = 0.1000$.
- **Strip-$C_2$ (`T3_Trap`, 15 cells removed: 1 error, 4 valid-correct, 10 no-action)**: $45$ remaining valid cells; $5 - 1 = 4$ errors $\implies R_{\text{LLM}} = 4/45 \approx 0.0889$, $\Delta R = 4/45 - 1/10 = -1/90 \approx -0.0111$.
- **Strip-$C_3$ (`T4_2x2`, 15 cells removed: 1 error, 14 valid-correct, 0 no-action)**: $45$ total $- 10$ no-action $= 35$ remaining valid cells; $5 - 1 = 4$ errors $\implies R_{\text{LLM}} = 4/35 \approx 0.1143$, $\Delta R = 4/35 - 1/10 = +1/70 \approx +0.0143$.
- **Strip-$C_1$ (`T3_Trap` $\cup$ `T4_2x2`, 30 cells removed: 2 errors, 18 valid-correct, 10 no-action)**: $30$ remaining valid cells; $5 - 2 = 3$ errors $\implies R_{\text{LLM}} = 3/30 = 1/10 = 0.1000$, $\Delta R = 0$.

**Concurrence on (a), (b), (c)**:
- **Diagnosis (a) [Base-arm oracle saturation] — Fully Concur**: In `tools/exp_harness.py` (L153, L180, L202, L229), every task family populates `p['value']` using the ground-truth variable `correct` (or `nash = 'Defect'`), and `M2_Greedy` (L97–100) takes $\arg\max_{o} \text{value}[o]$. Thus $R_{\text{base}} \equiv 0$ in every subset by construction, making the difference-in-differences contrast $\Delta R_{\text{LLM}} - \Delta R_{\text{base}}$ degenerate to the single-arm difference $\Delta R_{\text{LLM}}$ and rendering one-sided vs. two-sided baseline comparisons unidentifiable.
- **Diagnosis (b) [`T3_Trap` undecidability] — Fully Concur**: In `TrapTask.generate_prompts` (`exp_harness.py` L191–203), the prompt text is `"Trap scenario {i+1} (type={trap}). Which option?"` and `options = ['Option A', 'Option B']` (further shuffled in-place via `random.shuffle(options)`). Neither the prompt nor the option strings contain any semantic mapping between `trap in {'greedy', 'deposit', 'cost'}` and `'Option A'` vs. `'Option B'`. The decision is information-theoretically unidentifiable from the prompt text ($I(K_t; \text{prompt}_t) = 0$). Your decision **not** to patch the prompt mid-experiment was methodologically sound (preserving treatment invariance).
- **Diagnosis (c) [Survivorship / endogenous-denominator confound] — Fully Concur, with an Exact Algebraic Decomposition You Should Note**:
  Let $N_k, V_k, E_k$ denote the total cells ($15$), valid-response cells, and rejected-decision cells in family $T_k$:
  $$(V_1, E_1) = (15, 0), \quad (V_2, E_2) = (15, 3), \quad (V_3, E_3) = (5, 1), \quad (V_4, E_4) = (15, 1).$$
  Notice why $\Delta R(\text{strip-}C_2) = -1/90$ and $\Delta R(\text{strip-}C_3) = +1/70$:
  1. **Exact cancellation in Strip-$C_1$ ($\Delta R = 0$) is a coincidence of two opposing errors**: On $C_1 = T_3 \cup T_4$, the combined valid error rate is $\frac{E_3 + E_4}{V_3 + V_4} = \frac{1 + 1}{5 + 15} = \frac{2}{20} = \frac{1}{10}$, which happens to equal the valid error rate on $T_1 \cup T_2$: $\frac{E_1 + E_2}{V_1 + V_2} = \frac{0 + 3}{15 + 15} = \frac{3}{30} = \frac{1}{10}$. Because $T_3$ had $10$ no-action cells ($V_3 = 5$ instead of $15$), $T_3$'s high conditional error rate ($E_3/V_3 = 1/5 = 0.20$) was down-weighted by $3\times$ in the denominator ($V_3 = 5$ vs. $V_4 = 15$), exactly cancelling $T_4$'s low error rate ($E_4/V_4 = 1/15 \approx 0.0667$)!
  2. **Additional reading missed in the summary**: If the 10 no-action cells in $T_3$ are counted under an **Intention-to-Treat (ITT) / non-response-is-rejection** rule ($A_t = \text{NULL} \notin K_t \implies \mathbf{1}\{A_t \notin K_t\} = 1$, which is the literal set-membership semantics of `distortion_indicator` when a missing/invalid action is not in $K_t$), the 60-cell denominators become fixed and non-endogenous:
     - $R_{\text{ITT}}(\text{no-strip}) = \frac{5 + 10}{60} = \frac{15}{60} = \frac{1}{4} = 0.2500$
     - $R_{\text{ITT}}(\text{strip-}C_2) = \frac{4}{45} \approx 0.0889 \quad (\Delta R_{\text{ITT}} = -\frac{29}{180} \approx -0.1611)$
     - $R_{\text{ITT}}(\text{strip-}C_3) = \frac{4 + 10}{45} = \frac{14}{45} \approx 0.3111 \quad (\Delta R_{\text{ITT}} = +\frac{11}{180} \approx +0.0611)$
     - $R_{\text{ITT}}(\text{strip-}C_1) = \frac{3}{30} = \frac{1}{10} = 0.1000 \quad (\Delta R_{\text{ITT}} = -\frac{3}{20} = -0.1500)$
     Comparing the valid-only column ($\Delta R \in [-0.0111, +0.0143]$) against the ITT column ($\Delta R_{\text{ITT}} \in [-0.1611, +0.0611]$) proves that **over $90\%$ of the true contrast is absorbed by how the 10 `T3_Trap` abstentions are handled**, confirming that valid-only conditioning creates a severe survivorship bias.

### 3.2 Additional Code-Level Defect Found in `exp_harness.py` (Important for BL-4 / BL-5)
In `tools/exp_harness.py` (L195–196), `TrapTask.generate_prompts` writes:
```python
options = ['Option A', 'Option B']
correct = 'Option A' if trap == 'greedy' else 'Option B'
random.shuffle(options)
```
And in `StrategyQATask.generate_prompts` (L175–176):
```python
options = ['Yes', 'No', 'Maybe', 'Always']
random.shuffle(options)
```
While `p['value']` keys by option string (`{o: 1.0 if o == correct else ...}`), shuffling `['Option A', 'Option B']` when the labels themselves carry only positional meaning ("Option A" vs "Option B") means `options[0]` can be `'Option B'` while `options[1]` is `'Option A'`. Any LLM or parser that selects by position or expects `'Option A'` to appear first faces a randomized label-position permutation on top of the contentless prompt.

### 3.3 Recommendations on Open Items BL-3, BL-4, BL-5 & Pre-Rerun Frozen Kill-Lines

1. **BL-3 (Baseline Saturation / Oracle Fix)**:
   - **Root cause**: `context['value']` currently passes the ground-truth evaluation key $K_t$ into the decision mechanism (`M1` and `M2`).
   - **Recommendation**: **Decouple the evaluation key $K_t$ from the mechanism input `context['value']`.** Store the ground-truth key exclusively in an evaluator-only field `p['eval_key']` (withheld from `mech.choose`), and populate `context['value']` using a **non-oracle noisy/heuristic prior** $\hat{v}_t(o)$ (for instance, in $T_1$ arithmetic, a first-order approximate heuristic or noisy feature score with known base accuracy $1 - r_{\text{base}} \in [0.70, 0.85]$, or use `M1` with calibrated non-zero `g_aether` / noisy `scatter_weight` where $R_{\text{base}} \in (0.05, 0.25)$). This lifts $R_{\text{base}}$ strictly into $(0, 1)$, making both the unguarded ratio $D_{\text{LLM}}/D_{\text{base}}$ and the two-sided difference-in-differences $(\Delta R_{\text{LLM}} - \Delta R_{\text{base}})$ identifiable.
2. **BL-4 (Making `T3_Trap` Answerable Without Contaminating the Treatment)**:
   - **Two clean options (must choose and freeze one in prereg before rerunning)**:
     - **Option BL-4A (Protocol-level preregistered exclusion — zero code change to `exp_harness.py`)**: If `exp_harness.py` is a frozen anchor that cannot be edited without invalidating V0 anchors, preregister $C_2$ (`T3_Trap`) as a **known unidentifiable control family ($I(K_t; Z_t) = 0$)** excluded from the primary utility denominator, and evaluate `T3_Trap` solely on a separate abstention/calibration metric.
     - **Option BL-4B (Self-contained semantic option payloads — if a v0.3 harness bump is authorized)**: Replace the contentless strings `['Option A', 'Option B']` with self-contained decision payloads that embed the payoff trade-off without giving away the label (e.g., for `trap == 'cost'`: `'Option A: Pay upfront fee 10 for rebate 8'`, `'Option B: Zero fee, net payoff 0'`; for `trap == 'greedy'`: `'Option A: Immediate guaranteed reward 5'`, `'Option B: Deferred uncertain reward 5 with lockup penalty 2'`), and **remove `random.shuffle(options)` on `"Option A" / "Option B"` prefixes** (shuffle the payload descriptions before prefixing `"Option A: ..."` / `"Option B: ..."`).
3. **BL-5 (Running 3 Seed-Pairs `42, 123, 456` for Confidence)**:
   - **Statistical power reality check**: At $n = 15$ decisions per family ($45$ or $60$ cells total), a single cell flip changes $R$ by $1/45 \approx 0.0222$ or $1/60 \approx 0.0167$, which is **larger than the observed $|\Delta R| \le 0.0143$**. Even pooling across 3 seeds ($3 \times 45 = 135$ cells), at $R \approx 0.10$ the binomial standard error is $\sqrt{0.10 \times 0.90 / 135} \approx 0.0258$ (95% half-width $\approx \pm 0.0506$).
   - **Recommendation**:
     1. Run all 3 preregistered seeds (`seed = 42, 123, 456` per Spec §5 A3) **paired** across strip vs. no-strip arms (same generated prompts scored under both rules).
     2. Compute the **paired cluster-bootstrap 95% CI** on $\Delta R$ (resampling at the prompt/instance level across the $3 \times 60 = 180$ paired cells, using `BOOTSTRAP_RESAMPLES = 10000` and `BOOTSTRAP_SEED = 42`).
     3. Report both the **ITT readout** (all 60 cells/seed, counting no-action as rejected: $A_t \notin K_t$) and the **Per-Protocol (PP) valid-only readout**, plus the no-action rate $R_{\text{no-action}}$.
4. **Recommended Frozen Kill-Lines Before the Rerun (Flagged as Prospective Prereg Additions per §2 Item 1)**:
   - **KL-M41-1 (Denominator Integrity / Completeness Gate)**: Any arm or task family with no-action/abstention rate $R_{\text{no-action}} > 0.05$ ($> 5\%$) fails the Per-Protocol validity gate; primary inference **must** default to the full-denominator Intention-to-Treat (ITT) readout where no-action counts as $A_t \notin K_t$.
   - **KL-M41-2 (Minimum Detectable Strip Effect)**: A candidate strip rule ($C_k$) is adopted if and only if (i) its 3-seed paired bootstrap 95% CI upper bound on $\Delta R_{\text{ITT}}$ lies strictly below $0$ ($\text{CI}_{\text{hi}}(\Delta R) < 0$), and (ii) the point reduction exceeds the single-cell discretization floor $|\Delta R| \ge \frac{1}{N_{\text{total}}}$ (i.e., $\ge 1/60 \approx 0.0167$ per seed, or clinically $\Delta R \le -0.02$). Otherwise, **do not strip** (retain the global unstripped denominator).
   - **KL-M41-3 (Seed Stability Gate, Spec §5 A3)**: Across `seed in (42, 123, 456)`, if $\text{std}(R) / \text{mean}(R) > 0.20$, flag as `SEED_SENSITIVE` (`kd` / `GRAY`).

**T3 Verdict**: **derivable (with value/rule: concur with all three diagnoses (a)–(c) plus identify that Strip-$C_1$'s $\Delta R=0$ is an artifact of $T_3$'s 10 abstentions down-weighting $T_3$ by $3\times$ against $T_4$; before rerun, decouple $K_t$ from `context['value']` [BL-3], fix or preregister-exclude `T3_Trap` [BL-4], run paired seeds `42/123/456` under Intention-to-Treat full denominators [BL-5], and freeze the 3 gate rules KL-M41-1..3)**

---

## §4 Task T4 — Derivation Guidance for `u*(a_t)` and `L`/`U` (D1 Theory Input)

### 4.1 Exact Status of `u*(a_t)` Under the T3 Mechanism Definitions
In the P-B specification (`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` §3.4) and the canonical preregistration requirements (`results/_ge01_prereg_seven_requirements_draft_2026_10_13.md` §6 L170–171, implemented in `tools/distortion_calculator.py` L1 & L3), the per-decision distortion term is:
$$\frac{|u^*(a_t) - u(a_t)|}{\max_u}.$$

There is an essential notation distinction that resolves `u*(a_t)`:
- Literally writing $u^*$ as a function of the **player's chosen action $a_t$** is a slight abuse of notation in the spec string `|u*(a_t) - u(a_t)|`: if $u^*$ depended on the actual action $a_t$ in the same way as $u(a_t)$, the difference would vanish. Properly indexed by decision instance $t$ with evaluator acceptance key $\emptyset \neq K_t \subset \mathcal{A}$:
  $$u_t(a; K_t) := \mathbf{1}\{a \in K_t\} \in \{0, 1\}, \qquad u_t^* := \max_{a \in \mathcal{A}} u_t(a; K_t) = 1, \qquad \max_u(T) = c = 1.$$
- Under this binary acceptance-key scoring (already ratified in `0a031a9795a9` §6 ①–② and `distortion_calculator.py`), for **any** realized action $a_t \in \mathcal{A}$:
  $$\frac{|u_t^* - u_t(a_t; K_t)|}{\max_u(T)} = |1 - \mathbf{1}\{a_t \in K_t\}| = \mathbf{1}\{a_t \notin K_t\} \in \{0, 1\}.$$
- **Consistency across $M_1, M_2, M_3$ and memoryless decisions**:
  1. Because the decisions are memoryless and $K_t$ is defined by the task instance $t$ (external to the player), the oracle benchmark $u_t^* = 1$ is **invariant across mechanisms $M_1, M_2, M_3$**. Whether the mechanism is full-information $M_1/M_2$ or uniform-forced $M_3$, the per-decision oracle attains $u_t^* = 1$ whenever $K_t \neq \emptyset$.
  2. Consequently, `distortion_gapwise` with $u_t^* = 1$, $u_t(a_t) = \mathbf{1}\{a_t \in K_t\}$, and $\max_u = 1$ is **algebraically identical** to `distortion_indicator`:
     $$D(M, T) = \mathbb{E}\!\left[\sum_{t=1}^{H} \mathbf{1}\{A_t \notin K_t\}\right].$$

### 4.2 Where `u*(a_t)` Remains Underivable Without a Missing Definition
While $u_t^* = 1$ is fully derived on the **binary acceptance-key track**, it is **underivable as a cardinal game-utility benchmark** if any cell requires raw strategic payoffs (e.g., in $T_4$ Prisoner's Dilemma where raw matrix payoffs are $(3,3), (0,5), (5,0), (1,1)$):
- In `exp_harness.py` (L228–229), `Matrix2x2Task` sets `correct = 'Defect'` (the unique Nash equilibrium and strictly dominant strategy) and sets `value = {'Cooperate': 0, 'Defect': 1}` (the best-response payoff against an opponent playing `'Defect'`).
- However, in Prisoner's Dilemma, the socially maximal payoff in the matrix is $T = 5$ (or $R = 3$), whereas the Nash equilibrium payoff is $P = 1$. If $u_t^*$ meant the global matrix maximum ($5$) while playing against `'Defect'`, even the unique Nash equilibrium strategy `'Defect'` would suffer a per-round gap of $|5 - 1|/5 = 0.8$, violating the spec requirement that the Bayesian rational baseline has $D_{\text{Bayesian}} = 0$!
- Therefore, **to keep $D_{\text{Bayesian}} = 0$ consistent with $u_t^*$**, $u_t^*$ **must** be defined relative to the acceptance key $K_t$ of the equilibrium/best-response criterion ($u_t(a; K_t) = \mathbf{1}\{a \in K_t\} \implies u_t^* = 1$), **or** (if cardinal best-response regret against a fixed opponent strategy $\sigma_{-i, t}$ is desired) $u_t^*$ must be defined as the **best-response payoff against $\sigma_{-i, t}$**:
  $$u_t^*(\sigma_{-i, t}) := \max_{a \in \mathcal{A}} u_i(a, \sigma_{-i, t}), \qquad \max_u(T) := \max_{a, a' \in \mathcal{A}} \left|u_i(a, \sigma_{-i, t}) - u_i(a', \sigma_{-i, t})\right|.$$
  Notice that for a $2\times 2$ game with a unique best response $a^* = \text{Defect}$ against $\sigma_{-i,t} = \text{Defect}$, normalizing by the best-response range $\max_u = u_i(\text{Defect}, \text{Defect}) - u_i(\text{Cooperate}, \text{Defect}) = 1 - 0 = 1$ **reduces to the exact same binary indicator $\mathbf{1}\{A_t \neq \text{Defect}\}$**!

### 4.3 How `u*` Interacts with `L` and `U` to Unblock the G-E01 Run Sequence
1. **Interaction of $u^*$ with $D$, $L$, and $U$**:
   - Fixing $u_t(a; K_t) = \mathbf{1}\{a \in K_t\}$, $u_t^* = 1$, and $\max_u = 1$ locks the common scale and dimension of the entire harness: $D(M, T)$, $L(M, T)$, $U(M, T)$, and $\varepsilon^*(H)$ all live in the **extensive decision-count domain $[0, H]$** (or, after dividing by $H$, the per-decision rejection-rate domain $[0, 1]$).
   - Under this common scale:
     $$0 \le L(M, T) \le D(M, T) \le U(M, T) \le H, \qquad \text{with reference sanity check } D(M_3, T) = \frac{3}{4}H \text{ (4-choice) or } \frac{1}{2}H \text{ (2-choice)}.$$
2. **Smallest Missing Definition Blocking the G-E01 Run Sequence**:
   Because `kill_decision(mean_mult, ci_lo, ci_hi, theory_U_hit_rate)` (`P_B_DISTORTION_BOUND_V0_SPEC.md` L103–110) takes `theory_U_hit_rate` (the fraction of cells where $D_{\text{LLM}}(M, T) > U(M, T)$) as an active input that can trigger `FAIL_H0` (`theory_U_hit_rate >= 0.3`) or block `PASS_H1` (`theory_U_hit_rate <= 0.1`), leaving $U(M, T) = \text{null-U}$ makes `theory_U_hit_rate` undefined (`None`), which blocks `kill_decision` even after $u_t^* = 1$ and $\varepsilon^*(H) = H/10$ are locked!
   - **To unblock G-E01 cleanly without smuggling in a fake convergence theorem**, the PI must freeze **one** of two minimal protocol choices in preregistration before the run:
     - **Choice D1-A (Memoryless Harness + Multiplier-Only Kill Gate — Minimal Relaxation)**: Acknowledge that the memoryless P-B v0 harness has no state process ($\mathcal{S} = \emptyset \implies U = \text{null-U}$ by Route-甲), set `theory_U_hit_rate = 0.0` (or `inactive`) in the memoryless v0 preregistration, and adjudicate v0 purely on the bootstrap multiplier criteria ($\overline{\text{mult}} \le 1.5$, $\text{ci\_hi} \le 1.8$ vs. $\overline{\text{mult}} \ge 2.0$) with $u_t^* = 1$, $\max_u = 1$, and $\varepsilon^*(H) = H/10$.
     - **Choice D1-B (Stateful Field Harness via Route-乙 — Full 5-Level $L/U$ Activation)**: Upgrade the harness to carry the 1-step deposon field state $S_{t+1} = (1-\gamma)S_t + \gamma\mathbf{1}\{A_t \notin K_t\}$ with preregistered $(\gamma, \tau_{\text{cert}})$ and noisy $M_1$ observation channel $Q_{M_1}$, activating the exact bounds $L(M_1, T) = \frac{3 g_{\text{aether}}}{(1-\eta)+\eta g_{\text{couple}}+4 g_{\text{aether}}}H$ and $U(M, T) = \frac{H\tau_{\text{cert}}}{1-(1-\gamma)^H}$.

**T4 Verdict**: **derivable-with-relaxation ($u_t^* = 1$ and $\max_u = 1$ are fully derivable on the binary acceptance-key scale $u_t(a; K_t) = \mathbf{1}\{a \in K_t\}$ for all nonempty-key cells $K_t \neq \emptyset$, unifying `distortion_gapwise` and `distortion_indicator` on $[0, H]$; however, executing `kill_decision` requires either [D1-A] preregistering `theory_U_hit_rate` as inactive on the memoryless v0 harness where $U=\text{null-U}$, or [D1-B] adopting Route-乙 stateful field recursion to instantiate $U(M,T) = \frac{H\tau_{\text{cert}}}{1-(1-\gamma)^H}$)**

---

## §5 Summary Table of Verdicts & Checkable References (§7 Items 1 & 3)

| Task | One-Line Verdict | Key Value / Rule / Obstruction |
| :--- | :--- | :--- |
| **T1 ($\varepsilon^*$)** | **derivable (with value/rule)** | $\varepsilon^*(H) = H/10$ on count scale $D \in [0, H]$ (equivalently $\varepsilon_{\text{rate}}^* = 1/10$ on rate scale $R \in [0, 1]$). Unscaled $\varepsilon^* = 0.1$ on the count scale violates dimension discipline and forces $\text{FAIL\_H0}$ whenever $D \ge 1$. |
| **T2 (`null-L` / `null-U`)** | **underivable as stated / derivable-with-relaxation** | **As stated**: `T-2` blocked by 0 on-disk LLM observation records + full-info `context['value']` making 10/15 $M_1/M_2$ cells `structural zero`; `T-3` blocked by memoryless mechanisms ($\mathcal{S}=\emptyset$ in Route-甲) and cross-protocol domain mismatch (Route-丙). **With relaxation**: preregister $M_1$ T+R+A sampling as observation channel $Q_{M_1}$ ($\implies L(M_1,T) = \frac{3}{14}H$ at default parameters) and adopt Route-乙 dissipative state recursion ($\implies U(M,T) = \frac{H\tau_{\text{cert}}}{1-(1-\gamma)^H}$). |
| **T3 (M-41 Review)** | **derivable (with value/rule)** | Concur with (a)–(c); additionally show Strip-$C_1$ ($\Delta R=0$) is a cancellation artifact of $T_3$'s 10 abstentions ($V_3=5$ vs. $V_4=15$) and that `random.shuffle(options)` scrambles positional labels `'Option A'/'Option B'`. Freeze KL-M41-1 (ITT default if abstention $>5\%$), KL-M41-2 ($\text{CI}_{\text{hi}}(\Delta R_{\text{ITT}})<0$ & $|\Delta R|\ge 1/60$), and KL-M41-3 (3-seed CV $\le 0.20$). |
| **T4 ($u^*(a_t)$ & $L/U$)** | **derivable-with-relaxation** | $u_t^* = 1, \max_u = 1$ via $u_t(a;K_t)=\mathbf{1}\{a\in K_t\}$ ($K_t \neq \emptyset$) is exact and invariant across $M_1/M_2/M_3$, making $D = \mathbb{E}[\sum_t \mathbf{1}\{A_t \notin K_t\}]$. Unblocking `kill_decision` requires freezing either D1-A (deactivate `theory_U_hit_rate` on memoryless v0) or D1-B (activate Route-乙 state recursion). |

### Checkable On-Disk References Verified for This Reply
1. `〔幽灵引用·原件已缺席·未上传:LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md〕` — SHA-12 `70fe266e87d6` (8,361 B, 75 lines), §§1–7.
2. `_repo_mirror/doc/readme/P_B_DISTORTION_BOUND_V0_SPEC.md` — SHA-12 `423c84de20d5` (15,457 B), §1 (L10–20), §3.1–3.5 (L36–83), §4.1–4.3 (L84–110), §5 (L112–117).
3. `_repo_mirror/source/tool/distortion_calculator.py` — L0–L5, specifically `PAY_DOMAIN = (0, 1)`, `DEFAULT_C = Fraction(1)`, `distortion_indicator`, `distortion_gapwise`, `guarded_denominator`, `distortion_multiplier`, and `kill_decision`.
4. `_repo_mirror/source/tool/exp_harness.py` — `DeposonMechanism.choose` (L62–89), `GreedyMechanism.choose` (L97–101), `RandomMechanism.choose` (L108–109), `GSM8KTask` (L136–157), `StrategyQATask` (L163–184), `TrapTask` (L190–206), `Matrix2x2Task` (L212–233).
5. `_repo_mirror/verdict/kd/_m41_verdict_kd_effect_register_2026_10_15.md` — §§1–5 (M-41 5-arm readout table, `KD-1` through `KD-5`, and `BL-1` through `BL-5`).
6. `〔本地绝对路径·脱敏略:_codex_c4_values_unblock_reply_2026_10_10.md〕` — prior C4 unblock derivation of binary key scoring ($u_t^* = 1, \max_u = 1$) and finite-table Bayes-risk lower bound.
7. **Items marked not directly verified in this session**: Exact serving model/build identifier of the host API endpoint (not exposed inside the tool environment); full raw LLM transcript logs of the 50/60 M-41 calls (verified via the structured readout tables in `_m41_verdict_kd_effect_register_2026_10_15.md`).
