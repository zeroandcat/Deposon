# -*- coding: utf-8 -*-
"""
_v4_wt_s3_b2probe — B2 定因探测：v1 件 §0.2/§0.1 记值与盘上实测对照 + 哈希口径假设检验（只读）
"""
import hashlib, os, zlib
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')

def H(b): return hashlib.sha256(b).hexdigest()[:12]

# v1 §0.2 表 16 行（记值 大写 12 hex）
ROWS = [
 ('1',     'results/boss_pa_1_rbr_rm_result_2026_09_15.json',                          'D9E14ED29FB9', 8753),
 ('1-r',   'deposon_team/plugins/boss_pa_1_rbr_rm.py',                                 '1935F164D5F3', 17743),
 ('1-rep', 'docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md',                                  'A3FA45E7D121', 19751),
 ('4',     'results/boss_pa_3_replicator_dynamics_result_2026_09_15.json',             '18C9C370A6AE', 9098),
 ('4-r',   'deposon_team/plugins/boss_pa_3_replicator_dynamics.py',                    '268F708B96AE', 12900),
 ('5-anc', 'results/_v3x_conservation_anchor_2026_09_17.txt',                          '425507BB555B', 940),
 ('5-rep', 'docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md',                                'BA8F3894969D', 15985),
 ('8',     'results/boss_pc_3_a3_clipping_2026_09_15.json',                            '717C26DF5A00', 1265),
 ('10',    'results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json','05B4649985B5', 17053),
 ('12',    'results/boss_pe_2_real_transverse_ising_2026_09_15.json',                  '04CEDB126B98', 3553),
 ('12-rep','docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md',                                  '664DD320F549', 13109),
 ('26',    'results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json','19F0A2CB8CEF', 1669),
 ('27',    'results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json','00DF93A112F7', 9076),
 ('28',    'results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json','1F11ED31273D', 5266),
 ('—',     'docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md',                             'AFD2161E6544', 8526),
]
ROWS01 = [
 ('0-A', 'letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md', '24EAFC05A217', 28207),
 ('0-B', 'results/_v3_supplement_verdict_2026_09_23.md',                     '9421E78B7E3C', 15247),
 ('0-C', 'results/_v4_pi_cot_v3_prereg.md',                                  '1A90FD8F385A', 27223),
]

print('=' * 118)
print('§0.2 表（16 行 / 15 个不同文件）: 记值 vs 实测')
print('=' * 118)
print(f'{"#":<6}{"记 SHA-12":<15}{"实测 SHA-12":<15}{"匹配":<6}{"记字节":>8}{"实字节":>8}  件')
n_diff = n_same = 0
for tag, rel, rec, rb in ROWS:
    p = REPO / rel
    if not p.exists():
        print(f'{tag:<6}{rec:<15}{"MISSING":<15}{"-":<6}{rb:>8}{"-":>8}  {rel}')
        continue
    b = p.read_bytes(); a = hashlib.sha256(b).hexdigest()[:12].upper()
    ok = (a == rec)
    n_same += ok; n_diff += (not ok)
    print(f'{tag:<6}{rec:<15}{a:<15}{"OK" if ok else "DIFF":<6}{rb:>8}{len(b):>8}  {rel}')
print(f'  ⇒ 不符 {n_diff} / 相符 {n_same}（共 {len(ROWS)} 行）')

print()
print('=' * 118)
print('§0.1 表（3 行）: 记值 vs 实测')
print('=' * 118)
for tag, rel, rec, rb in ROWS01:
    p = REPO / rel
    if not p.exists():
        print(f'{tag}: MISSING {rel}'); continue
    b = p.read_bytes(); a = hashlib.sha256(b).hexdigest()[:12].upper()
    print(f'  {tag}  记 {rec}  实测 {a}  {"OK" if a==rec else "DIFF"}  字节 记{rb}/实{len(b)}  {rel}')

print()
print('=' * 118)
print('定因探测：对 #1 / 4 / 8 三件，检验多种哈希口径 / 编码变换能否产出记值')
print('=' * 118)
TARGETS = [
 ('#1',  'results/boss_pa_1_rbr_rm_result_2026_09_15.json', 'D9E14ED29FB9'),
 ('#4',  'results/boss_pa_3_replicator_dynamics_result_2026_09_15.json', '18C9C370A6AE'),
 ('#8',  'results/boss_pc_3_a3_clipping_2026_09_15.json', '717C26DF5A00'),
]
def variants(b):
    out = {}
    out['sha256(bytes)'] = hashlib.sha256(b).hexdigest()[:12]
    out['sha1'] = hashlib.sha1(b).hexdigest()[:12]
    out['md5'] = hashlib.md5(b).hexdigest()[:12]
    out['sha512'] = hashlib.sha512(b).hexdigest()[:12]
    out['blake2b'] = hashlib.blake2b(b).hexdigest()[:12]
    out['sha224'] = hashlib.sha224(b).hexdigest()[:12]
    out['sha384'] = hashlib.sha384(b).hexdigest()[:12]
    out['sha3_256'] = hashlib.sha3_256(b).hexdigest()[:12]
    out['crc32'] = format(zlib.crc32(b) & 0xffffffff, '08x')
    # 文本变换
    try:
        t = b.decode('utf-8')
        out['utf8_lf'] = hashlib.sha256(t.replace('\r\n', '\n').encode('utf-8')).hexdigest()[:12]
        out['utf8_crlf'] = hashlib.sha256(t.replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8')).hexdigest()[:12]
        out['strip_all_ws'] = hashlib.sha256(''.join(t.split()).encode('utf-8')).hexdigest()[:12]
        import json as _j
        try:
            out['json_canon_compact'] = hashlib.sha256(_j.dumps(_j.loads(t), ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()[:12]
            out['json_canon_indent2'] = hashlib.sha256(_j.dumps(_j.loads(t), ensure_ascii=False, sort_keys=True, indent=2).encode('utf-8')).hexdigest()[:12]
            out['json_ascii_compact'] = hashlib.sha256(_j.dumps(_j.loads(t), sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()[:12]
        except Exception:
            pass
        # 去掉首行 / 末行
        lines = t.splitlines()
        out['minus_first_line'] = hashlib.sha256('\n'.join(lines[1:]).encode('utf-8')).hexdigest()[:12]
        out['minus_last_line'] = hashlib.sha256('\n'.join(lines[:-1]).encode('utf-8')).hexdigest()[:12]
    except Exception:
        pass
    if b[:3] == b'\xef\xbb\xbf':
        out['bom_stripped'] = hashlib.sha256(b[3:]).hexdigest()[:12]
    return out

for tag, rel, rec in TARGETS:
    p = REPO / rel
    b = p.read_bytes()
    print(f'  {tag} 记值 {rec}  ({rel})')
    for name, v in variants(b).items():
        mark = '  <<< 命中' if v.upper() == rec else ''
        print(f'      {name:<22} {v}{mark}')

print()
print('_wt_s3_b2probe DONE')
