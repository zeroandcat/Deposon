import json
with open(r'D:\私人资料\deposon-repo\results\deposon_volcengine_worker_c_2026_09_10.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
print('=== Worker C Final Summary ===')
print('worker_id:', d['worker_id'])
print('timestamp:', d['timestamp'])
print('overall_elapsed_s:', d['overall_elapsed_s'])
print('auth:', d['auth'])
print('proxy_cleared:', d['proxy_cleared'])
print()
for m in d['models']:
    name = m['model']
    print('  ' + name + ':')
    print('    sanity: status=' + str(m['sanity']['status']) + ' ms=' + str(m['sanity']['ms']) + ' pass=' + str(m['sanity_pass']))
    print('    GSM8K: ' + str(m['gsm8k_passed']) + '/' + str(m['gsm8k_attempted']))
    print('    STQ:   ' + str(m['strategyqa_passed']) + '/' + str(m['strategyqa_attempted']))
    print('    total: ' + str(m['total_passed']) + '/' + str(m['cells_done']) + ' pass_rate=' + str(m['pass_rate_30']) + ' avg_ms=' + str(m['avg_ms']))
    print('    status=' + m['status'] + ' elapsed_s=' + str(m['elapsed_s']))
    print()
print('Total cells:', sum(m['cells_done'] for m in d['models']))
print('Total passed:', sum(m['total_passed'] for m in d['models']))
