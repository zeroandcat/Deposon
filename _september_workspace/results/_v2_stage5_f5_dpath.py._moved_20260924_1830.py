# -*- coding: utf-8 -*-
"""
deposon V2 阶段 5 (F-5 D 路径三模态守恒复算)
- 读 D 路径 JSON deposon_dpath_cross_modal_2026_09_10.json
- 验证 text_text(off=0.6563) + image_image(off=0.965) + text_image(off=0.2799) 是否守恒
- 试 T_text + R_image + A_cross = 1 或其他归一化约束
- 0 新 API 调用
"""
import os, sys, json, time, hashlib
import numpy as np

DPATH_REF = r'D:\私人资料\deposon-repo\results\deposon_dpath_cross_modal_2026_09_10.json'
OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_v2_phase5_f5_2026_09_11.json'

LOG_LINES = []
def log(msg):
    line = f'[{time.strftime("%H:%M:%S")}] {msg}'
    print(line, flush=True)
    LOG_LINES.append(line)


def main():
    # 锚校验
    anchor_path = r'D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json'
    anchor_sha = hashlib.sha256(open(anchor_path, 'rb').read()).hexdigest()[:12]
    assert anchor_sha == '03c6c01f3697', f'5 锚 SHA 变: {anchor_sha}'
    log(f'ANCHOR_OK SHA-12={anchor_sha}')

    # 读 D 路径
    d = json.load(open(DPATH_REF, 'r', encoding='utf-8'))
    sm = d['sim_matrix']
    
    tt_off = sm['text_text_offdiag_mean']
    ii_off = sm['image_image_offdiag_mean']
    ti_off = sm['text_image_offdiag_mean']
    tt_diag = sm['text_text_diag_mean']
    ii_diag = sm['image_image_diag_mean']
    
    log(f'text_text_offdiag={tt_off}  image_image_offdiag={ii_off}  text_image_offdiag={ti_off}')
    log(f'text_text_diag={tt_diag}  image_image_diag={ii_diag}')

    # F-5 三模态守恒检验
    # 假设:T_text + R_image + A_cross = 1 (或其它归一化约束)
    # T_text = 1 - tt_off (transmission = 信号穿越 text 通道保留的部分)
    # R_image = ii_off (reflection = 在 image 通道被反射回来的部分)
    # A_cross = ti_off (absorption/cross = 跨模态吸收的部分)
    
    T_text_1 = 1.0 - tt_off
    T_text_2 = tt_diag - tt_off  # diag - offdiag, 信号差
    R_image = ii_off
    A_cross = ti_off
    sum_1 = T_text_1 + R_image + A_cross
    sum_2 = T_text_2 + R_image + A_cross
    
    log(f'Sum1: (1-tt_off={T_text_1:.4f}) + ii_off({R_image:.4f}) + ti_off({A_cross:.4f}) = {sum_1:.4f}')
    log(f'Sum2: (tt_diag-tt_off={T_text_2:.4f}) + ii_off({R_image:.4f}) + ti_off({A_cross:.4f}) = {sum_2:.4f}')
    
    # Try several normalization hypotheses
    hypotheses = []
    # 1. T + R + A = 1 (deposon 守恒律, 类 Fresnel 方程)
    h1 = {'name': 'Fresnel-like T+R+A=1', 
          'formula': '(1-tt_off) + ii_off + ti_off',
          'value': round(sum_1, 4), 'target': 1.0, 'deviation': round(abs(sum_1 - 1.0), 4)}
    hypotheses.append(h1)
    
    # 2. T + R + A = 2 (类量子守恒 透射+反射+吸收 各 1/2 baseline)
    h2 = {'name': 'Quantum-like T+R+A=2', 
          'formula': '(1-tt_off) + ii_off + ti_off',
          'value': round(sum_1, 4), 'target': 2.0, 'deviation': round(abs(sum_1 - 2.0), 4)}
    hypotheses.append(h2)
    
    # 3. 归一化信号流: tt_off / (ii_off + ti_off) 比例恒定
    h3 = {'name': 'Ratio tt_off/(ii_off+ti_off)', 
          'formula': 'tt_off / (ii_off + ti_off)',
          'value': round(tt_off / (ii_off + ti_off), 4),
          'target': None, 'deviation': None}
    hypotheses.append(h3)
    
    # 4. 散射截面类: σ_text + σ_image = σ_cross (2D 散射)
    h4 = {'name': 'Scattering σ_text + σ_image = σ_cross', 
          'formula': 'tt_off + ii_off vs ti_off',
          'value': round(tt_off + ii_off, 4),
          'target': ti_off, 'deviation': round(abs(tt_off + ii_off - ti_off), 4)}
    hypotheses.append(h4)
    
    # 5. 信息流: text 通道 透射 = 1 - text 内耗
    h5 = {'name': 'Info-flow tt_off = 1 - R_text', 
          'formula': 'tt_off (transmission via text channel)',
          'value': round(tt_off, 4),
          'target': None, 'deviation': None}
    hypotheses.append(h5)
    
    # 6. deposon 守恒律: 1 - tt_off - ii_off = ti_off (双通道总耗损 = 跨模态)
    h6 = {'name': 'Conservation 1 - tt_off - ii_off = ti_off', 
          'formula': '1 - tt_off - ii_off',
          'value': round(1 - tt_off - ii_off, 4),
          'target': ti_off, 'deviation': round(abs(1 - tt_off - ii_off - ti_off), 4)}
    hypotheses.append(h6)
    
    for h in hypotheses:
        log(f'  H[{h["name"]}]: value={h["value"]} target={h["target"]} dev={h["deviation"]}')

    # 寻找最接近守恒的假设
    valid = [h for h in hypotheses if h['deviation'] is not None]
    best = min(valid, key=lambda x: x['deviation'])
    log(f'BEST_CONSERVATION: {best["name"]} deviation={best["deviation"]}')

    # 沿 5 候选 P-A/B/C/D 的 "P-B 守恒审计" 视角
    # P-B 要求守恒律在语义空间有 ε 容忍度
    # 这里 ε = best.deviation
    epsilon = best['deviation']
    if epsilon < 0.01:
        pb_verdict = 'STRONG_PASS (P-B 守恒在 D 路径三模态 0.01 内守恒)'
    elif epsilon < 0.05:
        pb_verdict = 'PASS (P-B 守恒在 0.05 内守恒)'
    elif epsilon < 0.10:
        pb_verdict = 'GRAY (P-B 守恒边界,需更紧分析)'
    else:
        pb_verdict = 'FAIL (P-B 守恒不成立)'
    log(f'P-B VERDICT: {pb_verdict} (epsilon={epsilon})')

    # 写输出
    results = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
        'phase': 'V2 阶段 5 (F-5 D 路径三模态守恒复算)',
        'dpath_source': os.path.basename(DPATH_REF),
        'sim_matrix_input': sm,
        'hypotheses': hypotheses,
        'best_conservation': best,
        'pb_verdict': pb_verdict,
        'epsilon': epsilon,
        'interpretation': {
            'tt_off=0.6563': 'text-text offdiag: caption 之间文本相似度 0.66(同一域)',
            'ii_off=0.965': 'image-image offdiag: PNG 渲染图之间 0.97(高冗余,视觉模板趋同)',
            'ti_off=0.2799': 'text-image offdiag: 文本与图像 0.28(显著低于同模态,说明跨模态守恒空间大)',
        },
        'constraints_honored': {
            'no_proxy': True, 'no_new_api_call': True, 'no_corpus_v20_modify': True,
            'dpath_unchanged': True,
        },
    }

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    log(f'OUTPUT_SAVED {OUTPUT_JSON}')

    # 也写日志
    log_path = OUTPUT_JSON.replace('.json', '.log')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(LOG_LINES))
    log('DONE')
    return 0


if __name__ == '__main__':
    sys.exit(main())
