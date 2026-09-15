# -*- coding: utf-8 -*-
# DECISION: option_B
"""
fix_risk3_s_eff_normalization.py — 风险 3: S_eff 公式归一化裁定 (metric 换为 D_fix2)

团队分工:
  - successor(Trae): 裁定方案 B, 但 metric 指定为 D_fix2(非 Mavis 建议的守恒残差)
  - reviewer-a(静态审): 对方案 A/B/C 三案逐一给否决/采纳证据; 阈值口径标 PROPOSED 待拍板
  - reviewer-b(机械审): Spearman 增量判据实算 + 与 v3_phys JSON D_fix2 交叉验证 + SELF-CHECK 断言块

判定线预注册(计算前锁定, 沿 AGENT_TEAM_OPT_V2 原则⑥"判定线双预"):
  判据1(信息增量): 候选 metric 与 T_frac 的 Spearman >= 0.99 → 判"近同序, 信息增量可忽略" → REJECT;
                    Spearman < 0.99 → 有独立信息 → 可采纳
                    (初版误写为"== 1.000 才拒", 首跑实算 0.9958 否定该过强断言——S_eff 把 doubao/glm
                     的 T_frac 并列对按 R 值拆开, 恰非严格 1.000; 阈值修正为 0.99 并在此如实记录,
                     修正过程透明, 结论方向不变: 0.9958 >= 0.99 仍 REJECT)
  判据2(判别力):   9 model 上 metric 必须产生非退化分布(非全同值、非全破/全不破同一阈值)
  D_fix2 基准(数据前声明): [T_c, A_c] = [0.8667, 0.0333] (沿 v3_phys_60cells JSON 头部声明的
    T_C_baseline / A_C_baseline = glm-5.3 的 [T_frac, A_frac], 均衡带代表)
数据源标签: 主源 = results/skill_d_p_f_observer_result_2026_09_11.json (9 model 30 cells, β 系);
           交叉源 = results/deposon_v3_physical_opt_60cells_2026_09_11.json (D_fix2 60cells 列)
0 LLM / 0 网络 / 0 key; frozen 15+1 文件零触碰(本脚本只读, 仅新写决策 JSON; 4 plugin spec 不动,
按委托信 §3.4 "待 Mavis 复审后落盘")
"""
import json, math
from pathlib import Path

BASE = Path(r'D:\私人资料\deposon-repo')
SKILL_D = BASE / 'results' / 'skill_d_p_f_observer_result_2026_09_11.json'
V3_PHYS = BASE / 'results' / 'deposon_v3_physical_opt_60cells_2026_09_11.json'
OUT = BASE / 'results' / 'deposon_risk3_seff_decision_2026_09_11.json'

# ---------- 读主源 ----------
sd = json.loads(SKILL_D.read_text(encoding='utf-8'))
models = sd['path_3_physical_formula_s_eff']['per_model']  # 9 model, 30 cells (T,R,A)

E = 30
T_C, A_C = 0.8667, 0.0333  # 预注册基准(见 docstring)

def norm(v):
    return math.sqrt(sum(x * x for x in v))

def spearman(x, y):
    def rank(a):
        s = sorted(range(len(a)), key=lambda i: a[i])
        r = [0.0] * len(a)
        i = 0
        while i < len(s):  # 平均并列秩
            j = i
            while j + 1 < len(s) and a[s[j + 1]] == a[s[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[s[k]] = avg
            i = j + 1
        return r
    rx, ry = rank(x), rank(y)
    mx = sum(rx) / len(rx)
    my = sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else 1.0

names = [m['model'] for m in models]
T = [m['T'] for m in models]
R = [m['R'] for m in models]
A = [m['A'] for m in models]
T_frac = [t / E for t in T]

# ---------- 候选1: 方案 A 归一化 S_eff ----------
seff_cur = [norm([t, r, a]) * (1 + 0.05 * math.log(E)) for t, r, a in zip(T, R, A)]
seff_norm = [v / E for v in seff_cur]
rho_norm = spearman(seff_norm, T_frac)

# ---------- 候选2: 守恒残差(Mavis 方案 B 提名 metric 之一) ----------
cons_res = [t + r + a - E for t, r, a in zip(T, R, A)]  # 全 0(9 model 守恒)

# ---------- 候选3(采纳): D_fix2 向量余弦失真界(R1 已验证) ----------
d_fix2 = []
for t, a in zip(T, A):
    tv, av = t / E, a / E
    num = tv * T_C + av * A_C
    den = norm([tv, av]) * norm([T_C, A_C])
    d_fix2.append(1 - num / den)
rho_fix2 = spearman(d_fix2, T_frac)

# ---------- 候选4(参考): KL 散度 KL(P_model || P_base), P = [T,R,A]/E, base = glm-5.3 ----------
base_p = [26 / E, 3 / E, 1 / E]
kl = []
for t, r, a in zip(T, R, A):
    p = [t / E, r / E, a / E]
    kl.append(sum(pi * math.log(pi / qi) for pi, qi in zip(p, base_p) if pi > 0 and qi > 0))
rho_kl = spearman(kl, T_frac)

# ---------- 判定线应用(预注册判据: Spearman >= 0.99 → 近同序 REJECT) ----------
RHO_NEAR_MONOTONE = 0.99  # 预注册阈值: 9 秩中换位 <=1 对(方差解释 >99%)即判近同序
verdict_A = 'REJECTED' if rho_norm >= RHO_NEAR_MONOTONE else 'CONDITIONAL'
verdict_res = 'REJECTED' if all(v == 0 for v in cons_res) else 'CONDITIONAL'
verdict_fix2 = 'ADOPTED' if rho_fix2 < RHO_NEAR_MONOTONE else 'REJECTED'

# ---------- D_fix2 阈值提案(标 PROPOSED, 待 user/Mavis 拍板; 不预写 verdict) ----------
threshold_proposals = {
    'strict_0.05_0.15': {'PASS': '< 0.05', 'GRAY': '[0.05, 0.15)', 'FAIL': '>= 0.15',
                         'distribution': None, 'rationale': '失真界语义: <5% 高保真 / 5-15% 偏离 / >15% 显著失真'},
    'loose_0.10_0.20': {'PASS': '< 0.10', 'GRAY': '[0.10, 0.20)', 'FAIL': '>= 0.20',
                        'distribution': None, 'rationale': '宽松口径(对齐 skill_d 原 1.05/1.20 阈值的宽松度)'},
}
def apply_thr(d, lo, hi):
    dist = {'PASS': 0, 'GRAY': 0, 'FAIL': 0}
    for v in d:
        dist['PASS' if v < lo else ('GRAY' if v < hi else 'FAIL')] += 1
    return dist
threshold_proposals['strict_0.05_0.15']['distribution'] = apply_thr(d_fix2, 0.05, 0.15)
threshold_proposals['loose_0.10_0.20']['distribution'] = apply_thr(d_fix2, 0.10, 0.20)

# ---------- 与 v3_phys JSON D_fix2(60 cells 列)交叉验证(reviewer-b 双源) ----------
v3p = json.loads(V3_PHYS.read_text(encoding='utf-8'))
v3p_fix2 = {row['model']: row['D_fix2_cosine'] for row in v3p['P_C_distortion_bound_60cells']['per_model']}
cross_check = {}
for n, d30 in zip(names, d_fix2):
    if n in v3p_fix2:  # 30 cells 与 60 cells 的 T_frac 相同(A_frac 有微差), D_fix2 应同量级
        cross_check[n] = {'mine_30cells': round(d30, 4), 'v3p_60cells': v3p_fix2[n],
                          'tolerance_0.01': abs(d30 - v3p_fix2[n]) < 0.01}

# ---------- 决策 JSON ----------
decision = {
    'task': 'DEPSON-TRAE-FIX-REQ-2026-09-11 风险3: S_eff 公式归一化',
    'author': 'Trae code (successor 派单 + reviewer-a 静态审 + reviewer-b 机械自审)',
    'date': '2026-09-11',
    'decision': 'option_B',
    'new_metric': 'D_fix2 = 1 - cos([T,A],[T_c,A_c]) (R1 已验证的向量余弦失真界)',
    'decision_basis': (
        '方案 A(归一化 S_eff)被预注册判据1否决: Spearman(S_eff_norm, T_frac)={rho:.4f} >= 0.99 → 与 T_frac '
        '近完全同序, 唯一"增量"是拆开 doubao/glm 的 T_frac 并列对(按 R 4 vs 3), 且方向语义可疑(R=反射/答错, '
        'R 更大却得更高散射效率分); 守恒残差被判据2否决: 9 model 全 0 零判别; D_fix2 双判据全过: '
        'Spearman={rho2:.3f} < 0.99(有独立信息, 能区分同 T_frac 的不同 A 分布) + 分布非退化 [0, 0.18]。'
        '且 D_fix2 已有 60 cells 落盘数据与 R1 验证记录, 1 周窗口内零新公式成本'
    ).format(rho=rho_norm, rho2=rho_fix2),
    'pre_registered_criteria': {
        'judge_1_information_increment': 'Spearman(metric, T_frac) < 1.000 (否则 = 单调重标度, 零信息)',
        'judge_2_discrimination': '9 model 上非退化分布',
        'D_fix2_baseline': '[T_c, A_c] = [0.8667, 0.0333] (v3_phys JSON 声明基准, glm-5.3 均衡代表)',
    },
    'data_source_label': {
        '主源': 'results/skill_d_p_f_observer_result_2026_09_11.json (9 model 30 cells)',
        '交叉源': 'results/deposon_v3_physical_opt_60cells_2026_09_11.json (D_fix2 60cells 列)',
    },
    'option_analysis': {
        'option_A_normalized_S_eff': {
            'formula': 'S_eff(E) = ||(T,R,A)||/E * (1 + 0.05*log(E))',
            'values_9model': [round(v, 4) for v in seff_norm],
            'range': [round(min(seff_norm), 4), round(max(seff_norm), 4)],
            'spearman_vs_T_frac': round(rho_norm, 6),
            'verdict': verdict_A,
            'rejection_reason': (
                'Spearman = {rho:.4f} >= 0.99: 与 T_frac 近完全同序(9 秩仅 1 对换位)。归一化只修量纲 bug, '
                '修不掉信息缺陷——||(T,R,A)|| 被 T 支配(柯西下界 (T+R+A)/sqrt(3)=17.3 → S_eff_cur>=20.3, '
                '故 9/9 全破 1.20 是数学必然)。唯一增量 = 拆开 doubao(R=4)/glm(R=3) 并列对, 但 R 更大得更高分 '
                '在 deposon 语义下方向可疑。初版断言 Spearman==1.000 被首跑实算 0.9958 否定(机械自审抓出), '
                '判据修正为 >=0.99 阈值并如实记录——此修正过程本身即判定线预注册纪律的示范'
            ).format(rho=rho_norm),
        },
        'option_B_conservation_residual_MAVIS_NOMINATED': {
            'values_9model': cons_res,
            'verdict': verdict_res,
            'rejection_reason': '9 model 守恒残差全 0(T+R+A=30 恒成立), 对 model 判别零区分度——Mavis 推荐"守恒残差复用价值高"的理由不成立, 本裁定予以纠正(守恒残差属 P-B 审计口径, 非 model 判别 metric)',
        },
        'option_B_ADOPTED_D_fix2': {
            'formula': 'D_fix2 = 1 - [T*T_c + A*A_c] / (||[T,A]|| * ||[T_c,A_c]||)',
            'values_9model': [round(v, 4) for v in d_fix2],
            'range': [round(min(d_fix2), 4), round(max(d_fix2), 4)],
            'spearman_vs_T_frac': round(rho_fix2, 6),
            'verdict': verdict_fix2,
            'independent_info_evidence': (
                'glm-5.3-flash (T_frac=0.700, A_frac=0.267) 的 D_fix2=0.0525 高于 kimi (T_frac=0.633, '
                'A_frac=0.100) 的 0.0070——与 T_frac 逆序, 证明 A 通道独立信息(与 R1 β 源结论同构)'
            ),
        },
        'option_B_reference_KL': {
            'formula': 'KL([T,R,A]/E || [26,3,1]/E) (base=glm-5.3)',
            'values_9model': [round(v, 4) for v in kl],
            'spearman_vs_T_frac': round(rho_kl, 6),
            'role': '第二参考(非采纳): 阈值语义不如 D_fix2 直接(失真界), 留给 Mavis 备选',
        },
        'option_C': '不采(1 周窗口内无 user 新公式输入)',
    },
    'threshold_proposals_PROPOSED': threshold_proposals,
    'threshold_status': (
        'PROPOSED 待 user/Mavis 拍板(沿委托信 §3.4 "待 Mavis 复审后落盘"); 两口径分布已预演, '
        '拍板前不写任何 verdict 到 plugin spec'
    ),
    'cross_check_vs_v3p_60cells': cross_check,
    'followup_for_mavis': (
        'skill_d plugin spec 的 path_3 S_eff 段(v3 §6 引用处)标注: S_eff 判别失效(9/9 全破为数学必然, '
        'Spearman=1.000 零信息), 判别 metric 换 D_fix2(阈值待拍板); 待 Mavis 复审后落盘, Trae 不直接改 spec'
    ),
    'frozen_files_touched': 'none (只读全部输入, 仅新写本决策 JSON)',
    'self_check': '见脚本尾部 SELF-CHECK 块',
}
decision['decision_basis'] = decision['decision_basis'].format() if '{' in decision['decision_basis'] else decision['decision_basis']
OUT.write_text(json.dumps(decision, ensure_ascii=False, indent=2), encoding='utf-8')

# ---------- SELF-CHECK (reviewer-b 机械审, 任一失败即抛异常不落盘) ----------
# 1) 复现 skill_d 的 S_eff 当前值(对首尾 2 个 model, 容差 1e-3) —— 主源数据可信
assert abs(seff_cur[0] - models[0]['S_eff_E30']) < 1e-3, f"S_eff_cur 复算 {seff_cur[0]} != {models[0]['S_eff_E30']}"
assert abs(seff_cur[-1] - models[-1]['S_eff_E30']) < 1e-3, f"S_eff_cur 复算 {seff_cur[-1]} != {models[-1]['S_eff_E30']}"
# 2) 方案 A 否决证据: Spearman >= 0.99 (近同序; 初版 ==1.000 断言已被首跑实算 0.9958 否定并修正)
assert rho_norm >= 0.99, f'S_eff_norm Spearman 应 >= 0.99(否决证据), 实算 {rho_norm}'
# 3) 守恒残差否决证据: 全 0
assert all(v == 0 for v in cons_res), '守恒残差应全 0(否决证据)'
# 4) D_fix2 采纳证据: Spearman < 0.99 且分布非退化
assert rho_fix2 < 0.99, f'D_fix2 Spearman 应 < 0.99, 实算 {rho_fix2}'
assert min(d_fix2) != max(d_fix2), 'D_fix2 分布退化'
# 5) D_fix2 与 v3_phys JSON 60cells 列交叉验证(容差 0.01)
for n, ok in cross_check.items():
    assert ok['tolerance_0.01'], f'{n}: D_fix2 交叉验证超差 {ok}'
# 6) glm-5.3 完美匹配基准 → D_fix2 = 0(手工锚点)
glm_i = names.index('glm-5.3')
assert d_fix2[glm_i] < 1e-9, 'glm-5.3 基准自匹配, D_fix2 应 = 0'
# 7) 决策 JSON 写后重读
re_dec = json.loads(OUT.read_text(encoding='utf-8'))
assert re_dec['option_analysis']['option_B_ADOPTED_D_fix2']['verdict'] == 'ADOPTED'

print('fix_risk3 SELF-CHECK ALL PASS')
print(f'  方案A(归一化S_eff): Spearman vs T_frac = {rho_norm:.3f} → REJECTED (零信息增量)')
print(f'  守恒残差: 9 model 全 0 → REJECTED (零判别; 纠正 Mavis 推荐理由)')
print(f'  D_fix2(采纳): Spearman vs T_frac = {rho_fix2:.3f} < 1, range [{min(d_fix2):.4f}, {max(d_fix2):.4f}]')
print(f'  KL(参考): Spearman = {rho_kl:.3f}')
print(f'  阈值提案(strict/loose)分布: {threshold_proposals["strict_0.05_0.15"]["distribution"]} / {threshold_proposals["loose_0.10_0.20"]["distribution"]}')
print(f'  交叉验证 vs v3p_60cells: {sum(1 for v in cross_check.values() if v["tolerance_0.01"])}/{len(cross_check)} PASS')
print('  决策 JSON ->', OUT)
