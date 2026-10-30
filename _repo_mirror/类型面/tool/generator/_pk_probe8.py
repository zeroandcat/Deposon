import json

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

c = json.load(open(r_dep_path("results/_v3_recheck_08c_preexp_data/result_2026_09_27.json"), encoding="utf-8"))
b = json.load(open(r_dep_path("results/_v3_recheck_08b_executor/result_2026_09_27.json"), encoding="utf-8"))
def fp(f):
    if not f: return None
    sst, ssr = f.get("ss_tot"), f.get("ss_res")
    if sst is None or ssr is None or sst == 0: return None
    return ssr/sst
def fmt(v): return ("%.4e"%v) if v is not None else "None"
print("=== 08c: 45 runs ===")
print(f"{'scheme':7} {'fixture':24} {'seed':4} {'delta':>12} {'rf_ratio':>10} {'rc_ratio':>10} {'legs_id':>7} {'r2_full':>8} {'r2_clip':>8} {'sst_f':>8} {'sst_c':>8}")
for r in c["runs"]:
    f_, fc = r["r2_full"], r["r2_clipped"]
    legs = bool(f_ and fc and f_.get("n_points")==fc.get("n_points") and f_.get("beta")==fc.get("beta")
            and f_.get("log10_A")==fc.get("log10_A") and f_.get("ss_res")==fc.get("ss_res")
            and f_.get("ss_tot")==fc.get("ss_tot"))
    print(f"{r['scheme_id']:7} {r['fixture_id']:24} {str(r['trial_seed']):4} {r['delta']!s:>12} {fmt(fp(f_)):>10} {fmt(fp(fc)):>10} {str(legs):>7} "
          f"{str(f_.get('r2')):>8} {str(fc.get('r2') if fc else None):>8} {f_.get('ss_tot')!s:>8.8} {str(fc.get('ss_tot') if fc else None):>8.8}")
print()
print("=== 08b CTRL2 (no-op) ===")
for r in b["controls"]["CTRL2_NOOP_emulation_of_v3_defect"]["rows"]:
    f_ = r["r2_full"]; d = r["delta"]
    print(f"  seed={r['trial_seed']:4} delta={d['r2_delta_full_minus_clipped']} status={d['delta_status']:8} ratio={fp(f_):.6e} r2={f_['r2']} n_pts={f_['n_points']} ss_tot={f_['ss_tot']}")
