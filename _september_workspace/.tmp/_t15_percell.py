import json
r = json.load(open('results/_v4_supp_t15_result.json', encoding='utf-8'))
scb = r['same_caption_breakdown']
for ci in range(6):
    d = scb[str(ci)]
    cs = r['per_cell_summary'][str(ci)]
    print(f'cell {ci} ({cs["dim"]}/t={cs["temperature"]}): '
          f'J_all_pooled_med={d["j_median_all_pooled"]} '
          f'J_same_cap_med={d["j_median_same_caption"]} '
          f'J_cross_cap_med={d["j_median_cross_caption"]} '
          f'pairs same/cross/total = {d["n_pairs_same_caption"]}/{d["n_pairs_cross_caption"]}/{d["n_pairs_total"]} '
          f'n_records={cs["n_records"]}')