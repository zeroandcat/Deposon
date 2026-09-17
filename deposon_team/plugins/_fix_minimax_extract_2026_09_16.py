# -*- coding: utf-8 -*-
"""
_fix_minimax_extract_2026_09_16.py — 修 minimax 生成脚本 extract_number 千分位缺陷 + 修正结果 JSON

主职: 审校与改进 minimax 产出的代码。
根因: extract_number 不处理千分位逗号 → gsm8k_4 的 "$1,430" 被提取为 430(实际应 1430) → 假阴性。
影响: minimax-m3 实为 22/30(原 21/30), gsm8k 12/15→13/15; 污染下游(制品/game theory/V7)。

动作(勘误式, 不篡改实测痕迹):
  1. 修生成脚本 extract_number(千分位逗号容错) —— 改进代码
  2. 修正结果 JSON gsm8k_4(extracted 430→1430, is_correct false→true) + 顶层统计 + 追加 fix_note 字段
  3. SELF-CHECK(修正后复读校验)

0 LLM / 0 proxy / 非 frozen 文件 / 5 锚 0 触动
"""
import json
import re

SRC_PY = r'D:\私人资料\deposon-repo\results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py'
SRC_JSON = r'D:\私人资料\deposon-repo\results\deposon_volcengine_minimax_m3_30cells_2026_09_10.json'


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


# ---- 1) 修生成脚本 extract_number ----
py = rd(SRC_PY)
old_bold = r"    m = re.findall(r'\*\*\s*(-?\d+(?:\.\d+)?)\s*\*\*', s)"
new_bold = r"    m = re.findall(r'\*\*\s*(-?\d[\d,]*(?:\.\d+)?)\s*\*\*', s)"
old_gen = r"    m = re.findall(r'-?\d+(?:\.\d+)?', s)"
new_gen = r"    m = re.findall(r'-?\d[\d,]*(?:\.\d+)?', s)"
old_ret1 = "            return float(m[-1])"
new_ret1 = "            return float(m[-1].replace(',', ''))"
old_ret2 = "            return float(m[-1])"
assert py.count(old_bold) == 1 and py.count(old_gen) == 1, 'extract_number 锚点异常'
# 两处 return float(m[-1]) 都要加 replace; 但第一处(bold)与第二处(gen)文本相同, 需精确区分
# 用更大上下文区分: bold 分支后的 return 与 gen 分支后的 return
bold_block_old = "    if m:\n        try:\n            return float(m[-1])\n        except Exception:\n            pass\n    m = re.findall(r'-?\\d+(?:\\.\\d+)?', s)"
bold_block_new = "    if m:\n        try:\n            return float(m[-1].replace(',', ''))\n        except Exception:\n            pass\n    m = re.findall(r'-?\\d[\\d,]*(?:\\.\\d+)?', s)"
assert py.count(bold_block_old) == 1, 'bold 块锚点异常'
py = py.replace(bold_block_old, bold_block_new, 1)
gen_block_old = "    m = re.findall(r'-?\\d[\\d,]*(?:\\.\\d+)?', s)\n    if m:\n        try:\n            return float(m[-1])\n        except Exception:\n            return None\n    return None"
gen_block_new = "    m = re.findall(r'-?\\d[\\d,]*(?:\\.\\d+)?', s)\n    if m:\n        try:\n            return float(m[-1].replace(',', ''))\n        except Exception:\n            return None\n    return None"
assert py.count(gen_block_old) == 1, 'gen 块锚点异常'
py = py.replace(gen_block_old, gen_block_new, 1)
wr(SRC_PY, py)
print('[1] extract_number 已加千分位逗号容错(bold + 通用两分支)')

# ---- 2) 修正结果 JSON ----
d = json.loads(rd(SRC_JSON))
fixed = 0
for c in d['cells']:
    if c['cell_id'] == 'gsm8k_4':
        assert c['gold_answer'] == 1430 and c['llm_extracted'] == 430.0 and c['is_correct'] is False
        c['llm_extracted'] = 1430.0
        c['is_correct'] = True
        fixed += 1
assert fixed == 1, 'gsm8k_4 修正目标异常'
# 顶层统计重算(显式重算, 不信原值)
gsm_pass = sum(1 for c in d['cells'] if c['task'] == 'gsm8k' and c['is_correct'])
stq_pass = sum(1 for c in d['cells'] if c['task'] == 'strategyqa' and c['is_correct'])
d['gsm8k_passed'] = gsm_pass
d['strategyqa_passed'] = stq_pass
d['total_passed'] = gsm_pass + stq_pass
d['pass_rate_30'] = round((gsm_pass + stq_pass) / 30, 4)
# 勘误式 fix_note(保留历史, 不删原字段)
d['fix_note_extract_2026_09_16'] = (
    'extract_number 千分位缺陷勘误: gsm8k_4 raw="$1,430" 原误提取 430 判错, 修正为 1430 判对; '
    'minimax-m3 total_passed 21→22 (gsm8k 12/15→13/15)。原始实测痕迹不删, 本字段为修正记录。'
)
wr(SRC_JSON, json.dumps(d, ensure_ascii=False, indent=2))
print('[2] 结果 JSON gsm8k_4 修正 430→1430 + 顶层统计 21→22 + fix_note 追加')

# ---- 3) SELF-CHECK ----
d2 = json.loads(rd(SRC_JSON))
g4 = [c for c in d2['cells'] if c['cell_id'] == 'gsm8k_4'][0]
assert g4['llm_extracted'] == 1430.0 and g4['is_correct'] is True
assert d2['gsm8k_passed'] == 13 and d2['strategyqa_passed'] == 9 and d2['total_passed'] == 22
assert d2['pass_rate_30'] == round(22 / 30, 4)
# 修正版提取器复读验证(独立重算)
def v2(s):
    if s is None:
        return None
    m = re.findall(r'\*\*\s*(-?\d[\d,]*(?:\.\d+)?)\s*\*\*', str(s))
    if m:
        return float(m[-1].replace(',', ''))
    m = re.findall(r'-?\d[\d,]*(?:\.\d+)?', str(s))
    return float(m[-1].replace(',', '')) if m else None
assert v2(g4['llm_raw_response']) == 1430.0
# 生成脚本改动已生效(compile)
compile(rd(SRC_PY), SRC_PY, 'exec')
print('[3] SELF-CHECK: gsm8k_4=1430 True; 13/9/22; 脚本 compile PASS')

print('_fix_minimax_extract SELF-CHECK ALL PASS')