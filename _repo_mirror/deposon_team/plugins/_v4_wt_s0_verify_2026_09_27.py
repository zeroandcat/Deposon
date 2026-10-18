# -*- coding: utf-8 -*-
"""
_v4_wt_s0_verify — V4 走读委托 §E 指纹索引 + §C 清单盘面核验（只读）
口径: sha12 = hashlib.sha256(全文字节).hexdigest()[:12] 小写
"""
import hashlib, os, glob

REPO = r'D:\私人资料\deposon-repo'

def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

def chk(rel, exp_sha=None, exp_size=None):
    p = os.path.join(REPO, rel.replace('/', os.sep))
    if not os.path.exists(p):
        return f'  MISSING  {rel}'
    s = sha12(p); z = os.path.getsize(p)
    if exp_sha is None:
        return f'  {s}  {z:>8}B  {rel}'
    ok_s = (s == exp_sha.lower())
    ok_z = (exp_size is None) or (z == exp_size)
    flag = 'OK ' if (ok_s and ok_z) else ('SHA_DIFF' if not ok_s else 'SIZE_DIFF')
    return f'  {flag}  {s}  {z:>8}B  (记 {exp_sha}/{exp_size})  {rel}'

print('=' * 110)
print('§E.2 §A 证据面（#1/#4 补审六件套 + 源件）')
print('=' * 110)
E2 = [
 ('results/_v3_recheck_prereg_v1_2026_09_27.md', '88052d7db895', 37346),
 ('results/_v3_recheck_01_executor_2026_09_27.py', '919fa909381e', 41004),
 ('results/_v3_recheck_01_result_2026_09_27.json', 'c19e2ab24e63', 167831),
 ('results/_v3_recheck_01_rescript_2026_09_27.md', '434b3213bdce', 13233),
 ('results/_v3_recheck_04_executor_2026_09_27.py', 'e098fa21700d', 49405),
 ('results/_v3_recheck_04_result_2026_09_27.json', 'db8cfb974ce3', 840158),
 ('results/_v3_recheck_04_rescript_2026_09_27.md', '2e0f6b8bf141', 13472),
 ('letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md', '0e7600ac4478', 7510),
 ('results/boss_pa_1_rbr_rm_result_2026_09_15.json', 'c7c59e0d2f6c', 8753),
 ('results/boss_pa_3_replicator_dynamics_result_2026_09_15.json', 'd6f233d73c45', 9098),
 ('results/deposon_v20_baselines.json', '6edb2aec1660', 16987),
 ('deposon_team/plugins/boss_pa_1_rbr_rm.py', '5cc594147e00', 17743),
 ('deposon_team/plugins/boss_pa_3_replicator_dynamics.py', 'a2bd9dd24c25', 12900),
]
for rel, s, z in E2:
    print(chk(rel, s, z))

print()
print('=' * 110)
print('§E.3 §B bug 面关键证据件')
print('=' * 110)
E3 = [
 ('results/_v4_pi_cot_v3_ruleset_v3_executor.py', '8a81d90c69ba', 58794),
 ('results/_v4_pi_cot_v2_ruleset_v2_executor.py', 'eb22f13d571c', 52465),
 ('results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json', '172093a23e4b', 4103),
 ('results/_v4_pi_cot_v3_result_v3.json', '585714f9660c', 27203),
 ('results/_v4_pi_cot_v3_verdict_v3.md', 'bb44fdc7ab0f', 53751),
 ('results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md', '41d29f4deb70', 42157),
 ('docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md', 'aed375c485fb', 407284),
 ('results/_v3_recheck_prereg_v1p1_2026_09_27.md', 'bcc3cee23e82', 42970),
 ('results/_v3_recheck_prereg_v1p2_2026_09_27.md', 'bc68854a6eba', 37636),
 ('results/_v4_pi_cot_v3_prereg.md', 'b7547329af2e', 27223),
 ('results/_v4_pi_cot_v3_ruleset_v3.json', '9d77a5e2cbab', 21392),
 ('results/_v3_s2_executor/rescript_2026_09_27.md', '331022480a57', 23039),
 ('results/_v3_s2_executor/executor_2026_09_27.py', 'f1e272a0924a', 84993),
 ('results/_v3_s1_executor/rescript_2026_09_27.md', '9d49a632ee81', 17253),
 ('results/_v3_recheck_26_rescript_2026_09_27.md', '3d9ad5f1540d', 8937),
 ('results/_v3_recheck_26b_rescript_2026_09_27.md', 'c300e74a082c', 29349),
 ('results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json', 'cbf60a630c9f', 20194),
 ('results/_v4_pi_cot_v2_questionnaire_v1.md', '7b14cdb31d21', 12402),
 ('results/_v4_pi_cot_v2_verdict_v2.md', '5d79e67a4e9d', 33723),
 ('results/_v4_supp_t15r2_verdict.md', '8355724a26e3', 64145),
 ('results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md', '883dced872b4', 97059),
 ('results/_v3_recheck_12_jsv_check_2026_09_27.md', '2b9e886e729d', 14525),
 ('letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md', '9bb22099db3b', 28207),
]
for rel, s, z in E3:
    print(chk(rel, s, z))

print()
print('=' * 110)
print('§E.4 §C 补充锚件')
print('=' * 110)
E4 = [
 ('results/_v3_s_prereg_v1_2026_09_27.md', 'ef5a40554960', 46836),
 ('results/_v3_s1_executor/executor_2026_09_27.py', '10870941c283', 54937),
 ('deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py', 'f7b61f041c0b', 30672),
 ('deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py', '62353279cd0c', 26734),
]
for rel, s, z in E4:
    print(chk(rel, s, z))

print()
print('=' * 110)
print('§H.1 今日收尾 18 件')
print('=' * 110)
H1 = [
 ('results/_v3_recheck_verdict_register_2026_09_27.md', '9708e7ef1f8c', 65913),
 ('results/_v3_recheck_prereg_v1p2_2026_09_27.md', 'bc68854a6eba', 37636),
 ('results/_v3_recheck_prereg_v1p3_2026_09_27.md', 'a8da321b64d2', 33904),
 ('results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md', '7e1323b09030', 33932),
 ('results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py', 'ee8671a28c2f', 62115),
 ('results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json', 'cbc14a76f038', 26891),
 ('results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md', '58ed6be022ed', 10251),
 ('results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json', '6eed9acdb99a', 18714),
 ('results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json', 'ed596914259a', 12975),
 ('results/_v4_pi_cot_v3_result_v3r1_2026_09_27.json', '735c03db1ae9', 22292),
 ('results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md', 'fbf88f8ac7a6', 10103),
 ('results/_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py', '96f491a8e2bf', 35555),
 ('results/_v3_s_phrasetemplate_preexp_data/result_2026_09_27.json', 'fae3c4640507', 36844),
 ('results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md', '6df402298557', 14510),
 ('results/_v3_recheck_08c_preexp_data/executor_2026_09_27.py', 'cb6eb9164df3', 37775),
 ('results/_v3_recheck_08c_preexp_data/result_2026_09_27.json', '689a6e4427a8', 146601),
 ('results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md', 'aa02cbfc84e3', 15211),
 ('results/_v3_recheck_12_rj5_provenance_2026_09_27.md', '20f15c49feb5', 23822),
]
for rel, s, z in H1:
    print(chk(rel, s, z))

print()
print('=' * 110)
print('§H.6.1 台账件')
print('=' * 110)
for rel, s, z in [('results/_v4_day_inventory_2026_09_27.md', '7662d5058a7d', 40487),
                  ('results/_v4_day_inventory_measure_2026_09_27.py', '3e903f224f87', 8226),
                  ('results/_v4_maindir_count_monitor_2026_09_27.md', '71e9cc179bec', 15313)]:
    print(chk(rel, s, z))

print()
print('=' * 110)
print('§A 未在 §E 索引但关键的源件')
print('=' * 110)
for rel in ['results/_v3_recheck_prereg_v1p4_2026_09_27.md',
            'results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json',
            'results/_v4_pi_cot_v3_dataset.json',
            'results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_24.json']:
    print(chk(rel))

print()
print('=' * 110)
print('§C 走读清单：V3-R 13 组三件套 + V3-S 2 组三件套（盘上实测存在性）')
print('=' * 110)
groups = ['01','04','08','08b','10','12','19','21','26','26b','27','28','35']
for g in groups:
    if g == '08b':
        base = 'results/_v3_recheck_08b_executor'
        files = ['executor_2026_09_27.py','result_2026_09_27.json','rescript_2026_09_27.md']
    elif g == '21':
        base = None
        files = ['deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py',
                 'results/_v3_recheck_21_result_2026_09_27.json','results/_v3_recheck_21_rescript_2026_09_27.md']
    elif g == '35':
        base = None
        files = ['deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py',
                 'results/_v3_recheck_35_result_2026_09_27.json','results/_v3_recheck_35_rescript_2026_09_27.md']
    else:
        base = None
        files = [f'results/_v3_recheck_{g}_executor_2026_09_27.py',
                 f'results/_v3_recheck_{g}_result_2026_09_27.json',
                 f'results/_v3_recheck_{g}_rescript_2026_09_27.md']
    line = f'  #{g:<4} '
    for f in files:
        rel = f if base is None else f'{base}/{f}'
        p = os.path.join(REPO, rel.replace('/', os.sep))
        line += ('Y' if os.path.exists(p) else 'N')
    print(line + f'   (executor/result/rescript)')

print()
for d in ['results/_v3_s1_executor','results/_v3_s2_executor','results/_v3_recheck_08b_executor',
          'results/_v3_recheck_08c_preexp_data','results/_v3_s_phrasetemplate_preexp_data']:
    p = os.path.join(REPO, d.replace('/', os.sep))
    n = len([f for f in os.listdir(p)]) if os.path.exists(p) else -1
    print(f'  子目录 {d:<52} 件数={n}')

print()
print('_wt_s0 DONE')
