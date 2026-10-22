import os, re, datetime, hashlib
ROOT = r"_repo_mirror"
TZ = datetime.timezone(datetime.timedelta(hours=8))
L=[]
def P(s=""): L.append(str(s))
# A. v179 登记件 mtime 之后落盘之 results 件
cut = os.path.getmtime(os.path.join(ROOT,"pi_rulings","_pi_card_answers_register_2026_10_21_v179.md"))
P(f"=== A. results/ 中 mtime 晚于 v179 登记件({datetime.datetime.fromtimestamp(cut,TZ).strftime('%H:%M:%S.%f')[:-3]}) 之件 ===")
res=os.path.join(ROOT,"results")
for f in sorted(os.listdir(res)):
    p=os.path.join(res,f)
    if os.path.isfile(p) and os.path.getmtime(p)>cut:
        P(f"  {datetime.datetime.fromtimestamp(os.path.getmtime(p),TZ).strftime('%H:%M:%S.%f')[:-3]}  {f}  {os.path.getsize(p)}B")
P()
# B. 并卷件 87d3bac68420
P("=== B. 并卷件 87d3bac68420 之全仓定位 ===")
found=[]
for dp,dn,fn in os.walk(ROOT):
    for f in fn:
        p=os.path.join(dp,f)
        try: b=open(p,'rb').read()
        except: continue
        if hashlib.sha256(b).hexdigest()[:12]=="87d3bac68420":
            found.append((os.path.relpath(p,ROOT), len(b)))
P(f"  命中 = {found if found else '0 命中（盘上 0 存在）'}")
P()
# C. 歧义括注注记件 之计数面三口径
P("=== C. 歧义括注注记件 之计数口径（grep 定位） ===")
nt=os.path.join(ROOT,"results","_d13_current_caliber_parenthesis_note_2026_10_21.md")
lines=open(nt,encoding="utf-8").read().split("\n")
for i,l in enumerate(lines,1):
    if re.search(r"22\s*处|21\s*处|60\s*处|12\s*件|11\s*件|两读并出|三读并出|口径差", l):
        P(f"  {i:4d}| {l[:420]}")
P()
# D. 勘误段件 §5-2 总账之版本面
P("=== D. P2/P7 勘误段件 §5-2 总账（v178 版 or v179 版） ===")
et=os.path.join(ROOT,"results","_fake_kd_p2_p7_reversal_errata_2026_10_21.md")
el=open(et,encoding="utf-8").read().split("\n")
for i,l in enumerate(el,1):
    if 210<=i<=232: P(f"  {i:4d}| {l[:400]}")
P()
# E. 五枚之确切所指（v178 §2-4 逐字）
P("=== E. v178 §2-4 之五枚清单逐字 ===")
v=open(os.path.join(ROOT,"pi_rulings","_pi_card_answers_register_2026_10_21_v178.md"),encoding="utf-8").read().split("\n")
P("  "+v[38][:1200])
P()
# F. 勘误段件是否含 P5 翻转
P("=== F. 勘误段件 中 P5 字面之命中（grep 定位） ===")
for i,l in enumerate(el,1):
    if re.search(r"P5| KD-VKR-6", l): P(f"  {i:4d}| {l[:300]}")
open(os.path.join(ROOT,"_tools_v176_panel3.txt"),"w",encoding="utf-8").write("\n".join(L))
print("ok")
