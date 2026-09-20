#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse the log file to build a partial JSON with whatever models completed"""
import os, json, re
from datetime import datetime, timezone, timedelta

log_path = r'D:\私人资料\deposon-repo\verifier\_run.log'
# Read as utf-8 first, fallback to utf-16
try:
    with open(log_path, 'r', encoding='utf-8') as f:
        log = f.read()
except UnicodeDecodeError:
    with open(log_path, 'r', encoding='utf-16') as f:
        log = f.read()

print('Log length:', len(log))
print('First 200 chars:', repr(log[:200]))

# Parse each line
models_data = {}
current_model = None
model_data = None
for line in log.split('\n'):
    line = line.strip()
    if not line:
        continue
    # Model header: [1/9] doubao-seed-2.0-lite
    m = re.match(r'\[(\d+)/9\]\s+(\S+)', line)
    if m:
        idx, current_model = m.group(1), m.group(2)
        if current_model not in models_data:
            models_data[current_model] = {'gsm_pass': 0, 'stq_pass': 0, 'gsm_total': 0, 'stq_total': 0, 'latency_sum': 0, 'latency_n': 0, 'sanity': {}}
        model_data = models_data[current_model]
        continue
    # Sanity line: OK  <model> ... sanity=True
    m = re.match(r'OK\s+(\S+)\s+http=(\d+)\s+ms=\s*(\d+)\s+sanity=(True|False)', line)
    if m:
        mod, http, ms, ok = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4) == 'True'
        if mod not in models_data:
            models_data[mod] = {'gsm_pass': 0, 'stq_pass': 0, 'gsm_total': 0, 'stq_total': 0, 'latency_sum': 0, 'latency_n': 0, 'sanity': {}}
        models_data[mod]['sanity'] = {'http_status': http, 'latency_ms': ms, 'sanity_pass': ok}
        continue
    # GSM line: GSM#01 http=200 ms=9919 exp=18.0 pred=18.0 PASS
    m = re.match(r'GSM#(\d+)\s+http=(-?\d+)\s+ms=\s*(\d+)\s+exp=([\d.\-]+)\s+pred=([\S]+)\s+(PASS|FAIL)', line)
    if m:
        cell_id, http, ms, exp, pred, status = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4), m.group(5), m.group(6)
        if model_data is None: continue
        model_data['gsm_total'] += 1
        if status == 'PASS': model_data['gsm_pass'] += 1
        if http == 200:
            model_data['latency_sum'] += ms
            model_data['latency_n'] += 1
        continue
    # STQ line: STQ#01 http=200 ms=13988 exp=Yes pred=Yes PASS
    m = re.match(r'STQ#(\d+)\s+http=(-?\d+)\s+ms=\s*(\d+)\s+exp=(\S+)\s+pred=(\S+)\s+(PASS|FAIL)', line)
    if m:
        cell_id, http, ms, exp, pred, status = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4), m.group(5), m.group(6)
        if model_data is None: continue
        model_data['stq_total'] += 1
        if status == 'PASS': model_data['stq_pass'] += 1
        if http == 200:
            model_data['latency_sum'] += ms
            model_data['latency_n'] += 1
        continue
    # STQ error line
    m = re.match(r'STQ#(\d+)\s+http=(-?\d+)\s+ms=\s*(\d+)\s+ERROR', line)
    if m:
        cell_id, http, ms = m.group(1), int(m.group(2)), int(m.group(3))
        if model_data is None: continue
        model_data['stq_total'] += 1
        # count as fail, no latency
        continue
    # Done line: >>> <model> done in 397s | GSM=14/15 STQ=12/15 Total=26/30 avg_ms=13263
    m = re.match(r'>>>\s+(\S+)\s+done\s+in\s+(\d+)s\s+\|\s+GSM=(\d+)/15\s+STQ=(\d+)/15\s+Total=(\d+)/30\s+avg_ms=(\d+)', line)
    if m:
        mod, elap, gsm_p, stq_p, tot, avg = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6))
        if mod not in models_data:
            models_data[mod] = {'gsm_pass': 0, 'stq_pass': 0, 'gsm_total': 0, 'stq_total': 0, 'latency_sum': 0, 'latency_n': 0, 'sanity': {}}
        models_data[mod].update({
            'elapsed_s': elap, 'gsm_pass': gsm_p, 'stq_pass': stq_p, 'total_pass': tot, 'avg_ms': avg
        })
        continue

print('=== Parsed models ===')
for m, d in models_data.items():
    print(' ', m, d)

# Build final JSON
models_list = []
for m in [
    "doubao-seed-2.0-lite",
    "kimi-k2.7-code",
    "minimax-m3",
    "doubao-seed-2.1-turbo",
    "deepseek-v4-flash",
    "glm-5.3",
    "doubao-seed-evolving",
    "glm-5.3-flash",
    "deepseek-v4-pro"
]:
    if m not in models_data:
        continue
    d = models_data[m]
    gsm_pass = d.get('gsm_pass', 0)
    stq_pass = d.get('stq_pass', 0)
    gsm_total = d.get('gsm_total', 0)
    stq_total = d.get('stq_total', 0)
    total_done = gsm_total + stq_total
    total_pass = gsm_pass + stq_pass
    avg_ms = d.get('avg_ms', 0)
    if avg_ms == 0 and d.get('latency_n', 0) > 0:
        avg_ms = int(d['latency_sum'] / d['latency_n'])
    pr = round(total_pass / 30.0, 4) if total_done == 30 else round(total_pass / max(total_done, 1), 4)
    models_list.append({
        'model': m,
        'gsm8k_passed': gsm_pass,
        'gsm8k_attempted': gsm_total,
        'strategyqa_passed': stq_pass,
        'strategyqa_attempted': stq_total,
        'total_passed': total_pass,
        'cells_done': total_done,
        'pass_rate_30': pr,
        'avg_ms': avg_ms,
        'sanity': d.get('sanity', {}),
        'status': 'COMPLETE' if total_done == 30 else f'PARTIAL ({total_done}/30)',
        'elapsed_s': d.get('elapsed_s', 0)
    })

# Best among complete models
complete = [m for m in models_list if m['status'] == 'COMPLETE']
best = max(complete, key=lambda x: x['total_passed']) if complete else (max(models_list, key=lambda x: x['total_passed']) if models_list else None)

now_iso = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')

output = {
    'timestamp': now_iso,
    'gateway': '火山方舟 Coding Plan',
    'base_url': 'https://ark.cn-beijing.volces.com/api/coding/v3',
    'auth': 'ark-[REDACTED]... (key loaded from env at runtime; literal key never written to disk)',
    'max_tokens': 2048,
    'timeout_s': 60,
    'temperature': 0.0,
    'note': 'PARTIAL RUN: 9 model full run timed out at 85 min wall-clock. 1 model complete (doubao-seed-2.0-lite), 1 partial (kimi-k2.7-code GSM done, STQ#01 PASS, STQ#02 timeout, rest not reached). 7 models not started. Re-run with --limit flag or smaller cells to complete.',
    'models': models_list,
    'best_model': best['model'] if best else None,
    'best_pass_rate': (str(best['total_passed']) + '/30') if best else 'N/A',
    'summary': {
        'total_models_tested_full': len(complete),
        'total_models_tested_partial': len(models_list) - len(complete),
        'total_models_not_started': 9 - len(models_list),
        'best_model_complete': best['model'] if best and best['status'] == 'COMPLETE' else None,
        'best_pass_count': best['total_passed'] if best else 0
    }
}

out_json = r'D:\私人资料\deposon-repo\results\deposon_volcengine_9model_30cells_2026_09_10.json'
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print('=== JSON written ===')
print('Path:', out_json)
print('Size:', os.path.getsize(out_json), 'bytes')
print('Models:', len(models_list))
