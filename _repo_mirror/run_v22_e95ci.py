#!/usr/bin/env python3
"""R1/R5: mechanize the E9.5 difference CIs as an artifact.

Reads `results/deposon_v19_benchmark_fixes.json` -> `experiments.E9_5_rule_baseline`
mechanically (accuracy and b/c/n for both benchmarks), computes the *unpaired*
Newcombe hybrid (score) confidence interval for the difference of two
proportions via statsmodels `confint_proportions_2indep(method='newcomb')`,
and also computes the §2.3 unified-vs-CoT GSM8K interval (85/100 vs 97/100).

Why unpaired: the paired discordant pairs are only (b,c) = (0,2) and (0,0),
so paired intervals degenerate (strategyqa degenerates entirely at c=0).
We therefore report the unpaired conservative bound.

Output: results/deposon_v22_e95ci.json
"""
import json
from statsmodels.stats.proportion import confint_proportions_2indep

SRC = "results/deposon_v19_benchmark_fixes.json"
OUT = "results/deposon_v22_e95ci.json"

METHOD = "newcomb_unpaired_conservative"


def diff_ci(n2, x2, n1, x1):
    """CI for p2 - p1 (group2 = unified/scattering, group1 = rule filter / CoT)."""
    lo, hi = confint_proportions_2indep(x2, n2, x1, n1, method="newcomb", compare="diff")
    return {
        "n2": n2, "x2": x2, "p2": x2 / n2,
        "n1": n1, "x1": x1, "p1": x1 / n1,
        "diff": x2 / n2 - x1 / n1,
        "ci": [lo, hi],
        "ci_pp": [round(lo * 100, 1), round(hi * 100, 1)],
    }


def main():
    with open(SRC) as f:
        src = json.load(f)
    e95 = src["experiments"]["E9.5_rule_baseline"]["benchmarks"]

    out = {
        "spec_version": "v22-e95ci-1",
        "method": METHOD,
        "note": (
            "Unpaired Newcombe hybrid (score) intervals via statsmodels "
            "confint_proportions_2indep(method='newcomb', compare='diff'). "
            "Paired discordant pairs are only (b,c)=(0,2) for GSM8K and (0,0) "
            "for StrategyQA, so paired intervals degenerate; we report the "
            "unpaired conservative bound. Group2 = unified (scattering layer), "
            "group1 = rule filter (E9.5) or CoT (unified_vs_cot). "
            "ci_pp = 95% CI in percentage points, rounded to 0.1pp."
        ),
        "source": SRC,
    }

    for bm, d in e95.items():
        rb = d["rule_baseline"]
        un = d["unified_llm_prior"]
        mc = d["mcnemar_unified_vs_rule"]
        r = diff_ci(un["n_total"], un["n_correct"], rb["n_total"], rb["n_correct"])
        r["mcnemar_b"] = mc["b"]
        r["mcnemar_c"] = mc["c"]
        out[bm] = r

    # R5: §2.3 unified 85/100 vs CoT 97/100 (GSM8K, frozen v1.4 GSM8K benchmark)
    out["unified_vs_cot"] = diff_ci(100, 85, 100, 97)
    out["unified_vs_cot"]["source"] = "results/deposon_benchmark_v1_4_gsm8k.json"

    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    for k in ("gsm8k", "strategyqa", "unified_vs_cot"):
        r = out[k]
        print(f"{k}: diff={r['diff']*100:+.1f}pp  95% CI {r['ci_pp']} pp "
              f"(b={r.get('mcnemar_b','-')}, c={r.get('mcnemar_c','-')})")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
