import json, os
os.chdir('D:/私人资料/deposon-repo')
data = json.load(open('results/deposon_volcengine_9model_30cells_2026_09_10.json', 'r', encoding='utf-8'))
print('Total elapsed:', data.get('total_elapsed_s'), 's')
print('Best:', data.get('best_model'), data.get('best_pass_rate'))
print()
print('=== Model rankings (by pass count) ===')
ranked = sorted(data['models'], key=lambda m: (-m['total_passed'], m['avg_ms']))
for i, m in enumerate(ranked, 1):
    model_name = m['model']
    gsm = m['gsm8k_passed']
    stq = m['strategyqa_passed']
    tot = m['total_passed']
    pr = m['pass_rate'] * 100
    avg = m['avg_ms']
    elap = m['elapsed_s']
    print('  #' + str(i) + ' ' + model_name.ljust(30) + ' GSM=' + str(gsm) + '/15 STQ=' + str(stq) + '/15 Tot=' + str(tot) + '/30 (' + ('%.1f' % pr) + '%) avg=' + str(avg) + 'ms elapsed=' + str(elap) + 's')
print()
print('=== Summary ===')
for k, v in data['summary'].items():
    print('  ' + k + ': ' + str(v))
print()
print('=== Sanity check results ===')
for m in data['models']:
    sn = m.get('sanity', {})
    print('  ' + m['model'].ljust(30) + ' sanity_pass=' + str(sn.get('sanity_pass')) + ' http=' + str(sn.get('http_status')) + ' ms=' + str(sn.get('latency_ms')))
