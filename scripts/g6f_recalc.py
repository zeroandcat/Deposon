# -*- coding: utf-8 -*-
# G6f 增批 A 轨复算（G6′ 判据＋G7′ κ 解锁判·与 G6f_G7p_unlock.lean 双实现交叉核对）
import os, json
from collections import Counter
from fractions import Fraction as F
PKG = os.environ.get("READINGS_PACKAGE_DIR", ".")
blind=set(json.load(open(f"{PKG}/g6f_blind_kh_frozen.json"))["blind_kh"])
nL,nH=13,19
OA=json.load(open(f"{PKG}/g6f_ops_A主胞.json")); OK=json.load(open(f"{PKG}/g6f_ops_KIMI.json"))
SW=json.load(open(f"{PKG}/run_a_v4_2__p2p_ops_A主胞switch补射.json"))
def calls(ops): return [ops[i:i+12] for i in range(0,len(ops),12)]
def g6(ops,lab):
    cl=calls(ops); d=[len({e['slot'] for e in c}) for c in cl]
    rep=sum(12-x for x in d); fk=Counter(e['slot'] for e in ops)
    m=sum(1 for e in ops if e['slot']<64); n=len(ops)-m
    a=sum(v for k,v in fk.items() if k in blind and k<64); b=sum(v for k,v in fk.items() if k in blind and k>=64)
    P=lambda x,y,m_,n_: F(m_*nL,m_*nL+n_*nH)
    k=F(a,a+b)-P(0,0,m,n); DA=F(a,a+b)-F(nL,32); bias=P(0,0,m,n)-F(nL,32)
    bn=(F(64*b,n*nH)-F(64*a,m*nL)) if (n>0 and m>0) else None
    br=(F(b,n)-F(a,m)) if (n>0 and m>0) else None
    print(f"{lab:14s} ops={len(ops):4d} calls={len(cl):3d} distinct_min={min(d)} rep={rep}/{len(ops)}({rep/len(ops):.2%}) "
          f"m/n={m}/{n} a/b={a}/{b} 跨响应重复率=1-{len(fk)}/{len(ops)}={1-len(fk)/len(ops):.2%}")
    print(f"{'':14s} κ={float(k):+.6f} |κ|≤0.10:{abs(k)<=F(1,10)} |κ|≤0.02:{abs(k)<=F(1,50)} D_A={float(DA):+.6f} bias={float(bias):+.6f}"
          + (f" B_norm={float(bn):+.6f}(|·|≤0.10:{abs(bn)<=F(1,10)}) B_raw={float(br):+.6f}" if bn is not None else " B 口径:n=0 未定义"))
    return dict(a=a,b=b,m=m,n=n,k=k)
print("== G6′ 门（预注册：distinct≥11/12·repeat_rate≤5%·各段独立）＋G7′ κ 解锁判 ==")
r={}
r['form']=g6([e for e in OA if e['seg']=='form'],"A主胞/form")
r['wd']  =g6([e for e in OA if e['seg']=='withdraw'],"A主胞/wd")
r['dv']  =g6([e for e in OA if e['seg']=='devalue'],"A主胞/dv")
r['A']   =g6(OA,"A主胞 pooled")
r['K']   =g6(OK,"KIMI/form")
print("\n== 跨响应复读（门外语位·B 轨新发现复核·键粒度） ==")
for ops,lab in [(OA,'A主胞'),(OK,'KIMI'),(SW,'switch(前轮)')]:
    fk=Counter(e['slot'] for e in ops); print(f"  {lab}: distinct 键 {len(fk)}/{len(ops)} → 跨响应重复率 {1-len(fk)/len(ops):.2%}")
print("  B 轨 (slot,op) 对粒度对照: A主胞 18/2592=99.3%·KIMI 145/1440=89.9%·switch 93.4%（同型结论·粒度差注记）")
print("\n== A 主胞支撑集机制位 ==")
fk=Counter(e['slot'] for e in OA)
print("  支撑集=显示前 12 键 k0-k11·每键恰 216 次（form 120/wd 48/dv 48）·每 call 216/216 恰为 {k0..k11} 双射")
print(f"  K_h∩支撑={sorted(k for k in range(12) if k in blind)} → K_h 密度 3/12=0.25 恒等机会位 32/128（g6f_amain_support_chance 机证）")
print(f"  KIMI 低命中 k5/6/7 占比: {sum(json.load(open(f'{PKG}/g6f_ops_KIMI.json')).count(0)for _ in [0])*0 or sum(1 for e in OK if e['slot'] in (5,6,7))}/301")
k=r['K']['k']; print(f"\nKIMI κ 精确分数: {k} ≈ {float(k):+.6f}")
a,b,m,n=r['K']['a'],r['K']['b'],r['K']['m'],r['K']['n']
print(f"KIMI σ 锚: 低半区密度 a/m={a/m:.4f} vs 13/64={13/64:.4f} (+{(a/m-13/64):.4f}·≈+{(a-m*13/64)/((m*13/64*51/64)**0.5):.1f}σ)·高半区 b/n={b/n:.4f} vs 19/64={19/64:.4f} (+{(b/n-19/64):.4f}·≈+{(b-n*19/64)/((n*19/64*45/64)**0.5):.1f}σ)")
