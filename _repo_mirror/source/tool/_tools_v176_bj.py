import os, re, hashlib, datetime
ROOT = r"_repo_mirror"
TZ = datetime.timezone(datetime.timedelta(hours=8))
bj=os.path.join(ROOT,"results","_pi_decision_backlog_consolidated_2026_10_21.md")
bb=open(bj,'rb').read(); bt=bb.decode('utf-8'); bl=bt.split("\n")
print("=== 并卷件 metrics ===")
print(f"  SHA-12={hashlib.sha256(bb).hexdigest()[:12]}  bytes={len(bb)}  LF={bb.count(bytes([10]))} CR={bb.count(bytes([13]))} TAB={bb.count(bytes([9]))} VT={bb.count(bytes([11]))} BOM={1 if bb[:3]==bytes([239,187,191]) else 0} UFFFD={bt.count(chr(0xFFFD))}")
print(f"  mtime={datetime.datetime.fromtimestamp(os.path.getmtime(bj),TZ).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}  lines={len(bl)}")
print("  --- L1-L14 ---")
for i,l in enumerate(bl[:14],1): print(f"  {i:4d}| {l[:600]}")
print("  --- 标题骨架 (first 30) ---")
n=0
for i,l in enumerate(bl,1):
    if re.match(r"^#{1,3}\s", l):
        print(f"  {i:4d}| {l[:200]}"); n+=1
        if n>=30: break
print("  --- 面数相关关键词计数 ---")
for kw in ["147","面","候裁","94"]:
    print(f"   {kw!r}: {bt.count(kw)}")
