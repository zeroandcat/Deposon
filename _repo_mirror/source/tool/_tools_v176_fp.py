import hashlib, json, os
root = r"_repo_mirror"
targets = {
 "v176":"cc039d075311","v177":"f4a2ee253746","v178":"60e19ccaea69","v179":"26d24d3f0195",
 "Q0_koujing":"609943436a0d","K-SEPCAL-7_verdict":"c013aeb1235f","new_construct_draft":"356ef2e9db1c",
 "bo0_koujing":"97ac680345ac","false_kd_per_item":"b6221e7a2efe","shi_trig_draft":"c7ef49e7ced3",
 "D13_newname_cand":"9c75e1d4cd76","jiexian_draft":"0ef78a26f637","A6_verdict":"09aea8d27041",
 "shi_jia_note":"25f8841cdbd4","jiexian_luozhang":"b69092972467","DEN16_alias_rev":"4eee36e8d339",
 "ambiguity_paren_note":"a5953d67cfbc","P2P7_errata":"2f2006f9a4ff","v175_style":"26abab740b0c",
}
skip = ("\\.git\\","\\.mavis\\","\\.tmp\\","\\.vscode\\","\\.trae\\")
idx = {}
for dp,dn,fn in os.walk(root):
    if any(s in dp for s in skip): continue
    for f in fn:
        p = os.path.join(dp,f)
        try:
            b = open(p,'rb').read()
        except Exception:
            continue
        h = hashlib.sha256(b).hexdigest()[:12]
        idx.setdefault(h, []).append((os.path.relpath(p,root), len(b)))
out = {"scanned": sum(len(v) for v in idx.values()), "matches": {}}
for k,t in targets.items():
    out["matches"][k] = [{"sha12":t,"paths":idx.get(t,[])}]
json.dump(out, open(r"_repo_mirror/readout/final/_tools_v176_fp_out.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("scanned files:", out["scanned"])
for k,t in targets.items():
    m = idx.get(t,[])
    print(f"{k:24s} {t}  ->", "MISS" if not m else "; ".join(f"{p} [{n}B]" for p,n in m))
