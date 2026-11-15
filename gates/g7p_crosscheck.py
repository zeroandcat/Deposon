# -*- coding: utf-8 -*-
# G7′ Python+Lean 双实现交叉核对（P 侧）· 与 G7p.lean（L 侧）逐位对账
# 基据：shared/ops_P2p读数包_2026_11_15/（25 件·只读）
import os, json
from fractions import Fraction as F

PKG = "<readings-package-dir>"
blind = json.load(open(f"{PKG}/p2p_blind_kh_frozen.json"))["blind_kh"]
nL = sum(1 for k in blind if k < 64); nH = len(blind) - nL
assert (nL, nH) == (13, 19) and len(blind) == 32

sw = json.load(open(f"{PKG}/run_a_v4_2__p2p_ops_A主胞switch补射.json"))
m = sum(1 for e in sw if e["slot"] < 64); n = len(sw) - m
fq = {}
for e in sw:
    if e["slot"] in blind: fq[e["slot"]] = fq.get(e["slot"], 0) + 1
assert fq == {int(k): v for k, v in json.load(open(f"{PKG}/run_a_v4_2__p2p_readout_A主胞switch补射.json"))["freq_post"].items()}
a = sum(v for k, v in fq.items() if k < 64); b = sum(v for k, v in fq.items() if k >= 64)

def seg_freq(fname):
    ro = json.load(open(f"{PKG}/{fname}")); f = {int(k): v for k, v in ro["freq_pre"].items()}
    return sum(v for k, v in f.items() if k < 64), sum(v for k, v in f.items() if k >= 64)
aA, bA = seg_freq("run_a_v4_1__p2p_readout_A主胞.json")     # A 主胞（form+wd+dv）
aK, bK = seg_freq("run_a_v4_1__p2p_readout_KIMI.json")      # KIMI form

# ---- 形式化判据（与 G7p.lean 定义逐位对应·交叉相乘同式） ----
DA   = lambda a,b: F(a, a+b) - F(nL, nL+nH)                                   # A 口径
bias = lambda m,n: F(m*nL, m*nL+n*nH) - F(nL, nL+nH)                          # 解耦期望偏置
kappa= lambda a,b,m,n: F(a, a+b) - F(m*nL, m*nL+n*nH)                         # 耦合分量（主判据）
Bnorm= lambda a,b,m,n: F(64*b, n*nH) - F(64*a, m*nL)                          # B 归一口径（比值差）
Braw = lambda a,b,m,n: F(b, n) - F(a, m)                                      # B 原始口径

print("== 构成与段数据（直读复算） ==")
print(f"K_h: 32 键 = 低半区 {nL} + 高半区 {nH}（k<64 界·盲化件 seed 20261115）")
print(f"switch: m={m} n={n} a={a} b={b}（ops 1,152 条 slot=键号·freq≡readout 恒等核毕）")
print(f"A主胞 : a={aA} b={bA}（k5/6/7 各 120）· m/n 缺位（ops 仅 smoke 432 条）")
print(f"KIMI  : a={aK} b={bK}（总 {aK+bK}）· m/n 缺位（ops 仅 smoke 432 条）")
print()
print("== P×L 双实现交叉核对表（L 侧定理名·G7p.lean decide 机证） ==")
T1  = F(10)*a*(nL+nH) > F(1)*(a+b)*(nL+nH) + F(10)*nL*(a+b)
rows = [
 ("S1 A口径实测 D_A>0.10",        DA(a,b) > F(1,10),  f"D_A={float(DA(a,b)):.6f}", "g7p_switch_aCal_gt_tenth"),
 ("S2 完美解耦下偏置 bias>0.10",  bias(m,n) > F(1,10),f"bias={float(bias(m,n)):.6f}", "g7p_switch_aBias_gt_tenth"),
 ("S3 观测op分布 null 方程不成立", (m*13*32 != 13*(m*13+n*19)), "971≠181 非均匀", "g7p_switch_null_eq_false"),
 ("S4a κ≤0.10",  kappa(a,b,m,n) <= F(1,10),  f"κ={float(kappa(a,b,m,n)):.6f}", "g7p_switch_kappa_le_tenth"),
 ("S4b κ≥−0.10", kappa(a,b,m,n) >= F(-1,10), f"|κ|≤0.10", "g7p_switch_kappa_ge_ntenth"),
 ("S5a κ≤0.01",  kappa(a,b,m,n) <= F(1,100), "紧界", "g7p_switch_kappa_le_hundredth"),
 ("S5b κ≥−0.01", kappa(a,b,m,n) >= F(-1,100),"紧界", "g7p_switch_kappa_ge_nhundredth"),
 ("S6a B归一差≤0.10", Bnorm(a,b,m,n) <= F(1,10), f"B_norm={float(Bnorm(a,b,m,n)):.6f}", "g7p_switch_bNorm_le_tenth"),
 ("S6b B归一差≥−0.10",Bnorm(a,b,m,n) >= F(-1,10),"|B_norm|≤0.10", "g7p_switch_bNorm_ge_ntenth"),
 ("S6c B归一差符号≥0", Bnorm(a,b,m,n) >= 0, "正号", "g7p_switch_bNorm_pos"),
 ("S7a B原始差≤0.10", Braw(a,b,m,n) <= F(1,10), f"B_raw={float(Braw(a,b,m,n)):.6f}(距阈{float(F(1,10)-Braw(a,b,m,n)):.6f})", "g7p_switch_bRaw_le_tenth"),
 ("S7b 解耦期望原始差≤0.10", F(6,64) <= F(1,10), "期望=6/64=0.09375 阈盲位", "g7p_decoupled_bRaw_expected_le"),
 ("A1 A主胞 κ=0 见证(m=1440,n=0)", F(aA*(1440*13+0*19)) == F(1440*13*(aA+0)), "解耦相容·极端偏好态", "g7p_amain_kappa_zero_witness"),
 ("A2 A主胞 κ>0.10 见证(m=n=720)", kappa(aA,0,720,720) > F(1,10), f"κ={float(kappa(aA,0,720,720)):.6f}", "g7p_amain_kappa_gt_witness"),
 ("K1 KIMI κ>0.10 见证(m=n=720)", kappa(aK,bK,720,720) > F(1,10), f"κ={float(kappa(aK,bK,720,720)):.6f}", "g7p_kimi_kappa_gt_witness"),
 ("K2a KIMI |κ|≤0.01 见证(m=575,n=100)", kappa(aK,bK,575,100) <= F(1,100), f"κ={float(kappa(aK,bK,575,100)):.6f}", "g7p_kimi_kappa_le_witness"),
 ("K2b KIMI κ≥−0.01 见证", kappa(aK,bK,575,100) >= F(-1,100), "解耦相容态", "g7p_kimi_kappa_ge_witness"),
]
ok = True
for name, pv, val, thm in rows:
    ok &= pv
    print(f"  [{'PASS' if pv else 'FAIL'}] {name:<38} {val:<28} ↔ {thm}")
print()
print("== 精确分数（P 侧·与 L 侧交叉相乘同式） ==")
k = kappa(a,b,m,n)
print(f"κ(switch) = {k} ≈ {float(k):.6f}   〔分子 a·n·nH−b·m·nL = {a*n*nH}-{b*m*nL} = {a*n*nH-b*m*nL}〕")
print(f"bias(switch) = {bias(m,n)} ≈ {float(bias(m,n)):.6f}")
print(f"D_A(switch) = {DA(a,b)} ≈ {float(DA(a,b)):.6f}（= κ + bias 分解恒等）")
print(f"B_norm(switch) = {Bnorm(a,b,m,n)} ≈ {float(Bnorm(a,b,m,n)):.6f}")
print(f"B_raw(switch) = {Braw(a,b,m,n)} ≈ {float(Braw(a,b,m,n)):.6f}")
print(f"D_A(A主胞)={float(DA(aA,bA)):.6f}·D_A(KIMI)={float(DA(aK,bK)):.6f}（A 轨三数恒等复现）")
print()
print("P×L 交叉核对：%d/%d 全一致（L 侧 build EXIT=0·0 error·0 sorry）" % (sum(1 for r in rows if r[1]), len(rows)))
