import os, re, hashlib, datetime, json
ROOT = r"_repo_mirror"
TZ = datetime.timezone(datetime.timedelta(hours=8))
L=[]
def P(s=""): L.append(str(s))
now = datetime.datetime.now(TZ).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
P(f"OBS_TS = {now}")
P()
P("=== 1. 停手闸第2次（落笔前即刻）· Python os.walk 长名式 ===")
target = os.path.join(ROOT,"results","_v176_v179_adoption_effect_2026_10_21.md")
P(f"  Test-Path(target) = {os.path.exists(target)}")
allf=[]; md=0; res_top=0; res_dirs=0
for dp,dn,fn in os.walk(ROOT):
    for f in fn:
        allf.append(os.path.join(dp,f))
        if f.lower().endswith(".md"): md+=1
    if dp == os.path.join(ROOT,"results"):
        res_top = len(os.listdir(dp))
        res_dirs = len([d for d in os.listdir(dp) if os.path.isdir(os.path.join(dp,d))])
P(f"  全仓递归件数 = {len(allf)}")
P(f"  全仓 .md 件数 = {md}")
P(f"  results\\ 顶层条目 = {res_top}  顶层目录 = {res_dirs}")
for pat in ["*v176*","*v177*","*v178*","*v179*","*v176_v179*","*adoption_effect*"]:
    hits=[os.path.relpath(p,ROOT) for p in allf if pat.strip("*").lower() in os.path.basename(p).lower()]
    P(f"  {pat} = {len(hits)} 命中")
    for h in sorted(hits)[:12]: P(f"       {h}")
    if len(hits)>12: P(f"       ... 其余 {len(hits)-12} 件")
P()
P("=== 2. K-W0-* 唯一标识符仪器计数（波 0 口径件） ===")
w0=os.path.join(ROOT,"results","_kd_false9_wave0_calibers_2026_10_20.md")
t=open(w0,encoding="utf-8").read()
ids=sorted(set(re.findall(r"K-W0-\d+-\d+", t)))
P(f"  波0口径件 K-W0-* 唯一标识符 = {len(ids)}")
P(f"  物理行数 = {len(t.split(chr(10)))}")
from collections import Counter
c=Counter(i.split("-")[2] for i in ids)
P(f"  域前缀分布 = {dict(sorted(c.items()))}")
P()
P("=== 3. 假 kd 判定件 §3 判定表 9 行（机器解析 · 非目测） ===")
ad=os.path.join(ROOT,"results","_fake_kd_itemwise_adjudication_2026_10_21.md")
lines=open(ad,encoding="utf-8").read().split("\n")
start=None;end=None
for i,l in enumerate(lines):
    if l.startswith("## §3 判定表"): start=i
    if start is not None and l.startswith("### §3-1"): end=i; break
rows=[]
for l in lines[start:end]:
    if l.startswith("|") and re.match(r"^\|\s*\*{0,2}P\d", l):
        c2=[x.strip() for x in l.strip("|").split("|")]
        rows.append(c2)
P(f"  判定表行数（机器解析）= {len(rows)}")
for r in rows: P("   | " + " | ".join(x[:60] for x in r[:5]))
P()
P("=== 4. 登记件九枚总账 vs 判定件判定分布（对照） ===")
P("  判定件一句话面（照录 L14 之旨）：kd 成立(坐实) 1 枚(P1) · kd 不成立(翻转) 2 枚(P2/P7) · 不明(挂账) 6 枚(P3/P4/P5/P6/P8/P9)")
P("  v178 §3 总账：P1 成立｜P2 翻转采认｜P3/P4/P5/P6/P8 不明｜P7 翻转采认｜P9 不明(挂账·风险位)")
P("  v179 §3 总账（更新）：P1 成立(v168-Q2)｜P2 翻转采认(v178-Q1)｜P3 不明(v178-Q4)｜P4 不明(v179-Q4)｜P5 翻转(v179-Q3)｜P6 不明(v178-Q4)｜P7 翻转采认(v178-Q2)｜P8 不明(v178-Q4)｜P9 不明(挂账·守门·释-甲已采)")
P()
P("=== 5. 交付件目标路径在盘复测（落盘后） ===")
P(f"  (本节为落盘前快照 · 落盘后另行复测)")
open(os.path.join(ROOT,"_tools_v176_panel2.txt"),"w",encoding="utf-8").write("\n".join(L))
print("ok")
