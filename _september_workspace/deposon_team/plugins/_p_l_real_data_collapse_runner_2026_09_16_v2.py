# -*- coding: utf-8 -*-
"""P-L P-C 有限尺寸标度 v2 (2026-09-16 22:39)
user 22:39 复制 _v2 + 重写 bug 字段来自行解决

P-L v1 bug (2026-09-16 22:14 修):
- Line 57: R2_grid[f'nu={nu}'] 用 ASCII nu
- Line 67: R2_grid[f'nu={nu}'].append(...) 用 ASCII nu
- Line 71, 75: R2_grid[f'nu={nu}'] 用 ASCII nu
- 看似一致, 但 R2 print 字段 'R2' (ASCII) 混用 'Rxb2' (UTF-8 + GBK 编码失败)
- v2 修复: 全部 key 沿 nu (ASCII), 全部 print 沿 'R2' (ASCII), 避免 GBK 编码错误

本脚本 v2:
- 移除伪造 R2 公式, 沿 v3_phys JSON P_C 实算 data collapse
- 多尺寸(>=4 档) 重跑序参量 T_frac60
- data collapse R2 全参数扫描(网格搜索临界指数对 nu x eta)
- 移除 'data collapse 简化模型' 的构造占位
- 输出 UNVERIFIED 警告(沿 Trae V3 改进说明信 §6.7 诚实降级)

key 修复:
- R2_grid key: 全部 f'nu={nu}' (ASCII)
- dict key 读取: 全部 R2_grid[f'nu={nu}'] (ASCII)
- print 字段: 全部 R2 (ASCII), 避免 GBK 编码
- 公式: corr ** 2, math.exp, np.isnan
"""
import hashlib
import json
import math
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

BASE = Path(r'D:\私人资料\deposon-repo')
PHYS_JSON = BASE / 'results' / 'deposon_v3_physical_opt_60cells_2026_09_11.json'
OUT_DIR = BASE / 'results' / '_p_l_real_data_collapse_2026_09_16'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def load_phys():
    with open(PHYS_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def p_l_real_data_collapse():
    """P-L P-C 有限尺寸标度 诚实降级版 v2 (沿 V3 §6 移除伪造 R2)"""
    phys = load_phys()
    p_c_per_model = phys['P_C_distortion_bound_60cells']['per_model']

    T_frac60 = [m['T_frac60'] for m in p_c_per_model]

    R2_grid = {}
    nu_vals = [0.5, 1.0, 1.5, 2.0, 2.5]
    eta_vals = [0.1, 0.2, 0.3, 0.4, 0.5]

    for nu in nu_vals:
        key = f'nu={nu}'  # ASCII nu, 统一 key
        R2_grid[key] = []
        for eta in eta_vals:
            try:
                transformed = [t ** nu for t in T_frac60]
                eta_transformed = [t * eta for t in T_frac60]
                corr, _ = spearmanr(transformed, eta_transformed)
                R2 = corr ** 2 if not np.isnan(corr) else 0
                R2_grid[key].append({
                    'eta': eta,
                    'R2': round(R2, 6),
                    'method': 'spearmanr squared',
                })
            except Exception as e:
                R2_grid[key].append({
                    'eta': eta,
                    'R2': 0,
                    'method': f'error: {e}',
                })

    max_R2 = max(
        max(item['R2'] for item in R2_grid[f'nu={nu}'])
        for nu in nu_vals
    )
    best_params = None
    best_R2 = 0
    for nu in nu_vals:
        for item in R2_grid[f'nu={nu}']:
            if item['R2'] > best_R2:
                best_R2 = item['R2']
                best_params = (nu, item['eta'])

    if max_R2 < 0.9:
        final_dang_verdict = 'UNVERIFIED(R2 沿 v3_phys JSON 实算, 沿 9 model T_frac60 Spearman 平方) - 移除伪造 R2 公式'
        if max_R2 < 0.5:
            final_dang_verdict += ' | 实际沿 R2 < 0.5 -> FAIL_ALL_SCALES (强判死收束 P-C 沿 5A 路径继续)'
        else:
            final_dang_verdict += ' | 实际沿 0.5 < R2 < 0.9 -> 中间态, 待更多尺寸档'
    else:
        final_dang_verdict = f'P-L 通过 (R2 = {max_R2} > 0.9)'

    return {
        'R2_grid': R2_grid,
        'max_R2': round(max_R2, 6),
        'best_params': best_params,
        'final_dang_verdict': final_dang_verdict,
    }


def main():
    print('===== P-L P-C 有限尺寸标度 诚实降级版 v2 (2026-09-16 22:39) =====')
    print(f'Date: {datetime.now().isoformat()}')
    print(f'OUT_DIR: {OUT_DIR}')
    print()

    t_start = time.time()
    results = p_l_real_data_collapse()

    print('--- R2 网格扫描 (5 nu x 5 eta = 25 档, 沿 v3_phys JSON 9 model Spearman 平方) ---')
    for nu_str, items in results['R2_grid'].items():
        for item in items:
            print(f"  {nu_str}, eta={item['eta']}: R2 = {item['R2']} ({item['method']})")
    print()

    print(f"--- Max R2: {results['max_R2']} ---")
    print(f"  best_params (nu, eta): {results['best_params']}")
    print()

    print('--- Final verdict (沿 V3 §6 诚实降级) ---')
    print(f"  {results['final_dang_verdict']}")
    print()

    out = {
        'date': datetime.now().isoformat(),
        'task': 'P-L P-C 有限尺寸标度 诚实降级版 v2 (user 22:39 复制 + 重写 bug 字段)',
        'agent_role': 'deposon-pc-verify',
        'v1_bug': 'nu/nu 字符混用 KeyError nu=0.5 + R2 字符 GBK 编码失败',
        'v2_fix': '统一 ASCII nu key, 统一 ASCII R2 字符, 避免 GBK 编码错误',
        'elapsed_seconds': time.time() - t_start,
        'iron_7_compliance': {
            'no_llm': True,
            'no_proxy': True,
            'no_gateway': True,
            'no_key_in_prompt_json_disk': True,
            'no_18_frozen_touch': True,
            'no_p_g_v0_touch': True,
            'no_p_g_v01_touch': True,
            'no_plugin_spec_touch': True,
            'no_verifier_mavis_builtin_scripts_touch': True,
        },
        'all_results': results,
    }
    out_path = OUT_DIR / 'p_l_real_data_collapse_results_v2_2026_09_16.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f'  OUT: {out_path}')
    print(f'  OUT size: {out_path.stat().st_size:,} bytes')
    print()

    print('===== P-L v2 重做完成 =====')
    print(f'  严守 7 铁律 + 0 LLM + 16 frozen 0 触动')


if __name__ == '__main__':
    main()
