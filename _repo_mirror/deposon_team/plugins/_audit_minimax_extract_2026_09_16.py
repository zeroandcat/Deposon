# -*- coding: utf-8 -*-
"""
_audit_minimax_extract_2026_09_16.py — minimax-m3 30cells 提取器精度审计(0 LLM, 只读)

主职: 审校与改进 minimax 产出的代码。审计 minimax 生成脚本的 extract_number 缺陷对结果的影响面。
根因: 脚本 L113-130 extract_number 不处理千分位逗号, "$1,430" 被提取为 430 (取末个数字 "430"),
      导致 gsm8k_4 (gold=1430) 假阴性。本脚本用修正版提取(逗号/美元/bold)复算全部 gsm8k cell,
      找出 假阴性(原判错实为对) + 假阳性(原判对实为错), 给出修正后 T/R/A。

0 LLM / 0 proxy / 只读结果 JSON / 不写回任何历史文件
"""
import json
import re

SRC = r'D:\私人资料\deposon-repo\results\deposon_volcengine_minimax_m3_30cells_2026_09_10.json'


def extract_num_v2(s):
    """修正版提取: bold 优先, 千分位逗号/$ 容错, 取末个数"""
    if s is None:
        return None
    s = str(s)
    # 1) bold **N** 或 **N,N** (含千分位)
    m = re.findall(r'\*\*\s*(-?\d[\d,]*(?:\.\d+)?)\s*\*\*', s)
    if m:
        try:
            return float(m[-1].replace(',', ''))
        except Exception:
            pass
    # 2) 通用数字(含千分位逗号)
    m = re.findall(r'-?\d[\d,]*(?:\.\d+)?', s)
    if m:
        try:
            return float(m[-1].replace(',', ''))
        except Exception:
            return None
    return None


def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        d = json.load(f)
    cells = d['cells']
    gsm = [c for c in cells if c.get('task') == 'gsm8k']
    stq = [c for c in cells if c.get('task') == 'strategyqa']

    print('=== gsm8k 提取复算(修正版) ===')
    changed = []
    for c in gsm:
        gold = c.get('gold_answer')
        orig_pred = c.get('llm_extracted')
        orig_correct = c.get('is_correct')
        v2 = extract_num_v2(c.get('llm_raw_response'))
        v2_correct = (v2 is not None and gold is not None and abs(v2 - float(gold)) < 1e-3)
        if v2_correct != bool(orig_correct) or (v2 is not None and orig_pred is not None and abs(v2 - float(orig_pred)) > 1e-9):
            changed.append({
                'cell_id': c['cell_id'], 'raw': c.get('llm_raw_response'), 'gold': gold,
                'orig_extracted': orig_pred, 'v2_extracted': v2,
                'orig_correct': orig_correct, 'v2_correct': v2_correct,
            })
    for ch in changed:
        tag = 'FN(假阴性,原判错实对)' if (ch['v2_correct'] and not ch['orig_correct']) else \
              ('FP(假阳性,原判对实错)' if (ch['v2_correct'] is False and ch['orig_correct']) else '提取值变化')
        print(f'  [{tag}] {ch["cell_id"]}: raw={ch["raw"]!r} gold={ch["gold"]} orig={ch["orig_extracted"]}→v2={ch["v2_extracted"]} ({ch["orig_correct"]}→{ch["v2_correct"]})')

    # 修正后统计
    orig_pass = sum(1 for c in gsm if c.get('is_correct'))
    v2_pass = sum(1 for c in gsm if extract_num_v2(c.get('llm_raw_response')) is not None
                  and c.get('gold_answer') is not None
                  and abs(extract_num_v2(c.get('llm_raw_response')) - float(c['gold_answer'])) < 1e-3)
    print(f'gsm8k: 原 passed={orig_pass}/15, 修正版 passed={v2_pass}/15 (差异 {v2_pass - orig_pass:+d})')

    # stq 快扫: extract_yesno 是否可能误判
    print('=== strategyqa 快扫(原 extract_yesno) ===')
    stq_weird = []
    for c in stq:
        raw = c.get('llm_raw_response') or ''
        if raw.strip() and not re.search(r'\b(Yes|No)\b', raw, re.IGNORECASE):
            stq_weird.append((c['cell_id'], raw[:60], c.get('is_correct')))
    for w in stq_weird:
        print(f'  [无Yes/No字样] {w[0]}: raw={w[1]!r} correct={w[2]}')

    # 修正后 total
    stq_orig_pass = sum(1 for c in stq if c.get('is_correct'))
    print(f'strategyqa passed={stq_orig_pass}/15 (未改)')
    print(f'=== 修正后 TOTAL: {v2_pass + stq_orig_pass}/30 (原 {orig_pass + stq_orig_pass}/30) ===')

    return changed


changed = main()
# SELF-CHECK
assert changed, '预期至少 gsm8k_4 一处差异, 异常'
assert any(ch['cell_id'] == 'gsm8k_4' and ch['v2_extracted'] == 1430.0 for ch in changed), 'gsm8k_4 应为 1430'
assert any(ch['cell_id'] == 'gsm8k_4' and ch['orig_extracted'] == 430.0 for ch in changed), 'gsm8k_4 原提取应为 430'
print()
print('SELF-CHECK PASS: gsm8k_4 假阴性实锤, 修正后 1430.0')