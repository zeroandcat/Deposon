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
CEIL = 1e-24
def fp(f):
    if f is None: return None
    sst, ssr = f.get("ss_tot"), f.get("ss_res")
    if sst is None or ssr is None: return None
    return ssr/sst
print("=== 08c: 45 runs, 残差质量比 + 腿同一性 ===")
print(f"{'scheme':8} {'fixture':26} {'seed':5} {'d':6} {'ssres/sstot_full':18} {'ssres/sstot_clip':18} {'legs_identical':13} {'r2_full':10} {'r2_clip':10}")
for r in c["runs"]:
    f_, fc = r["r2_full"], r["r2_clipped"]
    legs = (f_ and fc and f_.get("n_points")==fc.get("n_points") and f_.get("beta")==fc.get("beta")
            and f_.get("log10_A")==fc.get("log10_A") and f_.get("ss_res")==fc.get("ss_res")
            and f_.get("ss_tot")==fc.get("ss_tot"))
    rf = f_.get("r2"); rc = fc.get("r2") if fc else None
    print(f"{r['scheme_id']:8} {r['fixture_id']:26} {str(r['trial_seed']):5} {str(r['delta']):6} "
          f"{('%.4e'%fp(f_)) if fp(f_) else 'None':18} {('%.4e'%fp(fc)) if fp(fc) else 'None':18} "
          f"{str(legs):13} {str(rf):10} {str(rc):10}")
print()
print("=== 08b CTRL2 (no-op) ===")
for r in b["controls"]["CTRL2_NOOP_emulation_of_v3_defect"]["rows"]:
    f_ = r["r2_full"]; d = r["delta"]
    print(f"  seed={r['trial_seed']:4} delta={d['r2_delta_full_minus_clipped']} status={d['delta_status']:8} "
          f"ssres/sstot={fp(f_):.6e}  r2={f_['r2']}  n_pts={f_['n_points']} ss_tot={f_['ss_tot']}")
