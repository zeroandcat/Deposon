import hashlib, os, datetime
ROOT = r"_repo_mirror"
OUT  = os.path.join(ROOT, "_tools_v176_measure_out.txt")
L=[]
def P(s=""): L.append(str(s))
TZ = datetime.timezone(datetime.timedelta(hours=8))
def mmss(ms):
    return (datetime.datetime.fromtimestamp(ms//1000, TZ).strftime("%Y-%m-%d %H:%M:%S")
            + f".{ms%1000:03d}")
FILES = [
 ("v176 登记件", r"pi_rulings\_pi_card_answers_register_2026_10_21_v176.md", "cc039d075311", 5689),
 ("v177 登记件", r"pi_rulings\_pi_card_answers_register_2026_10_21_v177.md", "f4a2ee253746", 6747),
 ("v178 登记件", r"pi_rulings\_pi_card_answers_register_2026_10_21_v178.md", "60e19ccaea69", 6753),
 ("v179 登记件", r"pi_rulings\_pi_card_answers_register_2026_10_21_v179.md", "26d24d3f0195", 7112),
 ("体例锚 v175", r"results\_v175_adoption_effect_2026_10_21.md", "26abab740b0c", 145012),
 ("Q0 口径件", r"results\_kd_identified_defect_attribution_caliber_2026_10_20.md", "609943436a0d", 73752),
 ("K-SEPCAL-7 终判件", r"results\_kd_sepcal7_final_verdict_2026_10_20.md", "c013aeb1235f", 70518),
 ("新构造草案", r"results\_preexp_design_new_construct_mda8a24_2026_10_20.md", "356ef2e9db1c", 79800),
 ("波 0 口径件", r"results\_kd_false9_wave0_calibers_2026_10_20.md", "97ac680345ac", 76664),
 ("假 kd 逐枚判定件", r"results\_fake_kd_itemwise_adjudication_2026_10_21.md", "b6221e7a2efe", 83606),
 ("释触发态拟案件", r"results\_mda8a24_release_trigger_proposals_2026_10_20.md", "c7ef49e7ced3", 87614),
 ("D13 新名候选件", r"results\_d13_rename_candidates_2026_10_21.md", "9c75e1d4cd76", 54962),
 ("界线拟案件", r"results\_kd_two_gates_boundary_proposal_2026_10_21.md", "0ef78a26f637", 41462),
 ("A6 判定件", r"results\_kabla6_trigger_review_adjudication_2026_10_21.md", "09aea8d27041", 50919),
 ("释-甲注记件", r"results\_kreltrig_release_note_2026_10_21.md", "25f8841cdbd4", 44908),
 ("界线落账件", r"results\_kd_two_gates_boundary_adoption_2026_10_21.md", "b69092972467", 43097),
 ("DEN16 别名表修订件", r"results\_den16_alias_table_revision_2026_10_21.md", "4eee36e8d339", 46947),
 ("歧义括注注记件", r"results\_d13_current_caliber_parenthesis_note_2026_10_21.md", "a5953d67cfbc", 48277),
 ("P2/P7 勘误段件", r"results\_fake_kd_p2_p7_reversal_errata_2026_10_21.md", "2f2006f9a4ff", 47276),
]
P("=== A. 19 件源件盘面实测 ===")
P("| # | 件 | SHA-12(实测) | 派工给定 | 吻合 | bytes | 派工bytes | LF | CR | TAB | VT | BOM | U+FFFD | mtime |")
ok_all=True
for i,(nm,rel,exp_sha,exp_b) in enumerate(FILES,1):
    p=os.path.join(ROOT,rel); b=open(p,'rb').read()
    sha=hashlib.sha256(b).hexdigest()[:12]; t=b.decode('utf-8')
    mt=datetime.datetime.fromtimestamp(os.path.getmtime(p),TZ).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    ok = (sha==exp_sha and len(b)==exp_b)
    if not ok: ok_all=False
    P(f"| {i} | {nm} | {sha} | {exp_sha} | {'OK' if sha==exp_sha else 'MISMATCH'} | {len(b)} | {exp_b} | {b.count(chr(10).encode())} | {b.count(bytes([13]))} | {b.count(bytes([9]))} | {b.count(bytes([11]))} | {1 if b[:3]==bytes([239,187,191]) else 0} | {t.count(chr(0xFFFD))} | {mt} |")
    P(f"    path={rel}  sha256_full={hashlib.sha256(b).hexdigest()}")
P(f"ALL_19_MATCH = {ok_all}")
P()
P("=== B. 卡答锚三法复算 ===")
ANCH=[("v176",1792550836456,"2026-10-21 10:47:16.456"),
      ("v177",1792552142400,"2026-10-21 11:09:02.400"),
      ("v178",1792553323917,"2026-10-21 11:28:43.917"),
      ("v179",1792554548015,"2026-10-21 11:49:08.015")]
allthree=True
for nm,ms,exp in ANCH:
    m1=mmss(ms); q,r=divmod(ms,1000)
    m3=(datetime.datetime.fromtimestamp(q,TZ).strftime("%Y-%m-%d %H:%M:%S")+f".{r:03d}")
    eq=(m1==m3==exp); allthree = allthree and eq
    P(f"{nm}: ms={ms} | 法1={m1} | 法3(divmod)={m3} | 登记件载={exp} | 三法逐位一致={eq}")
P("--- 锚差加算法（逐对相接） ---")
for i in range(len(ANCH)-1):
    nm0,ms0,_=ANCH[i]; nm1,ms1,_=ANCH[i+1]
    d=ms1-ms0
    base=datetime.datetime.fromtimestamp(ms0//1000,TZ)+datetime.timedelta(milliseconds=ms0%1000)
    calc=(base+datetime.timedelta(milliseconds=d)).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    P(f"  {nm0}->{nm1}: diff={d} ms = {d/1000:.3f}s => {calc} | =={nm1}所载: {calc==ANCH[i+1][2]}")
P(f"ALL_THREE_STRING_EQ = {allthree}")
P(f"OBS_TS = {datetime.datetime.now(TZ).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
P()
P("=== C. skill 四路径存在性 + 哈希（两盘符内容同否） ===")
SK=[("verification-before-completion(C)", r"〔本地绝对路径·脱敏略:SKILL.md〕"),
    ("verification-before-completion(D)", r"〔本地绝对路径·脱敏略:SKILL.md〕"),
    ("peer-review(C)", r"〔本地绝对路径·脱敏略:SKILL.md〕"),
    ("peer-review(D)", r"〔本地绝对路径·脱敏略:SKILL.md〕")]
grp={}
for nm,p in SK:
    ex=os.path.exists(p)
    if ex:
        b=open(p,'rb').read(); hh=hashlib.sha256(b).hexdigest()
        base=nm.split("(")[0]; grp.setdefault(base,[]).append((nm,hh,len(b),p))
        P(f"  EXISTS {nm}: sha256={hh} bytes={len(b)}")
        P(f"         path={p}")
    else:
        P(f"  MISSING {nm}: {p}")
P("  --- 两盘符内容同否 ---")
for base,v in grp.items():
    if len(v)==2:
        P(f"  {base}: C==D ? {v[0][1]==v[1][1]}  C={v[0][1][:16]}  D={v[1][1][:16]}")
open(OUT,"w",encoding="utf-8").write("\n".join(L))
print("WROTE", OUT, len(L), "lines")
