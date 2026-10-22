import os, re, hashlib, datetime
ROOT = r"_repo_mirror"
TZ = datetime.timezone(datetime.timedelta(hours=8))
L=[]
def P(s=""): L.append(str(s))
p5=os.path.join(ROOT,"results","_fake_kd_p5_reversal_adjudication_2026_10_21.md")
b=open(p5,'rb').read(); t=b.decode('utf-8'); lines=t.split("\n")
P(f"=== P5 落定件：{os.path.basename(p5)} ===")
P(f"  SHA-12 = {hashlib.sha256(b).hexdigest()[:12]}  bytes={len(b)}  LF={b.count(bytes([10]))} CR={b.count(bytes([13]))} TAB={b.count(bytes([9]))} VT={b.count(bytes([11]))} BOM={1 if b[:3]==bytes([239,187,191]) else 0} U+FFFD={t.count(chr(0xFFFD))}")
P(f"  mtime = {datetime.datetime.fromtimestamp(os.path.getmtime(p5),TZ).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
P("  --- 头部 L1-L16 ---")
for i,l in enumerate(lines[:16],1): P(f"  {i:4d}| {l[:700]}")
P("  --- 标题骨架 ---")
for i,l in enumerate(lines,1):
    if re.match(r"^#{1,3}\s", l): P(f"  {i:4d}| {l[:200]}")
P()
P("=== P5 落定件 中 P5 翻转/勘误段/候 PI 采认 之命中 ===")
for i,l in enumerate(lines,1):
    if re.search(r"翻转|勘误|候 PI 复核|二段式|归因面未解|构成", l):
        P(f"  {i:4d}| {l[:420]}")
P()
bj=os.path.join(ROOT,"results","_pi_decision_backlog_consolidated_2026_10_21.md")
bb=open(bj,'rb').read(); bt=bb.decode('utf-8'); bl=bt.split("\n")
P(f"=== 并卷件 {os.path.basename(bj)} ===")
P(f"  SHA-12 = {hashlib.sha256(bb).hexdigest()[:12]}  bytes={len(bb)}  LF={bb.count(bytes([10]))} CR={bb.count(bytes([13]))} TAB={bb.count(bytes([9]))} VT={bb.count(bytes([11]))} BOM={1 if bb[:3]==bytes([239,187,191]) else 0} U+FFFD={bt.count(chr(0xFFFD))}")
P(f"  mtime = {datetime.datetime.fromtimestamp(os.path.getmtime(bj),TZ).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
P(f"  物理行数 = {len(bl)}")
for i,l in enumerate(bl[:12],1): P(f"  {i:4d}| {l[:500]}")
P("  --- 标题骨架（前 40 条）---")
n=0
for i,l in enumerate(bl,1):
    if re.match(r"^#{1,3}\s", l):
        P(f"  {i:4d}| {l[:200]}"); n+=1
        if n>=40: break
open(os.path.join(ROOT,"_tools_v176_panel4.txt"),"w",encoding="utf-8").write("\n".join(L))
print("ok")
