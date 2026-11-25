#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family-aware max_u adapter for tools/distortion_calculator.py.

Append-only implementation of the 2026-10-29 U-C3 family-level decision. The
anchored calculator is imported read-only and is not modified. Callers must
supply a family explicitly; there is deliberately no silent scalar default.
All arithmetic remains in fractions.Fraction.
"""
import importlib.util
from fractions import Fraction
from pathlib import Path

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


_SPEC = importlib.util.spec_from_file_location(
    "distortion_calculator_anchor",
    Path(r_dep_path("tools/distortion_calculator.py")),
)
_anchor = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_anchor)

FAMILY_MAX_U = {
    "T1": Fraction(1),
    "T2": Fraction(1),
    "T3": Fraction(1),
    "T4": Fraction(4),
    "T5": Fraction(9),
}
ALIASES = {
    "T1_GSM8K": "T1",
    "T2_STRATEGYQA": "T2",
    "T3_TRAP": "T3",
    "T4_2X2": "T4",
    "T5_LOWRESOURCE": "T5",
}


def family_c(task_family) -> Fraction:
    key = str(task_family).strip()
    key = ALIASES.get(key.upper(), key.upper())
    if key not in FAMILY_MAX_U:
        raise ValueError("Unknown task_family; explicit family is required: %r" % task_family)
    return FAMILY_MAX_U[key]


def guarded_denominator_for_family(d_bayesian, eps, task_family) -> Fraction:
    return _anchor.guarded_denominator(d_bayesian, eps, family_c(task_family))


def distortion_multiplier_for_family(d_llm, d_bayesian, eps, task_family) -> Fraction:
    return _anchor.distortion_multiplier(d_llm, d_bayesian, eps, family_c(task_family))


def distortion_gapwise_for_family(choices, optimal_payoffs, actual_payoffs, task_family, weights=None) -> Fraction:
    return _anchor.distortion_gapwise(
        choices,
        optimal_payoffs,
        actual_payoffs,
        max_u=family_c(task_family),
        weights=weights,
    )


def cell_table_row_for_family(choice_readings, eps, task_family) -> dict:
    row = _anchor.cell_table_row(choice_readings, eps, family_c(task_family))
    row["task_family"] = task_family
    row["max_u_exact"] = family_c(task_family)
    row["max_u_exact_str"] = str(family_c(task_family))
    return row
