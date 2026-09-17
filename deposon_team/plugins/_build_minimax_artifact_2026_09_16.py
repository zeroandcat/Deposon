# -*- coding: utf-8 -*-
"""
_build_minimax_artifact_2026_09_16.py — P-K 跨主体指纹盲测 · minimax 制品构建(0 LLM)

委托: user 2026-09-16 "minimax 制品由你负责"(因 prior 改 minimax P-D 脚本)
沿 EXTERNAL_AGENT_PROMPTS_2026_09_16.md §1 配套提示词 A + P_D_FINGERPRINT_V0_SPEC.md

数据来源(只读): results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json
  30 cells(15 GSM8K + 15 StrategyQA)= minimax-m3 实际推理产出; 本脚本抽取为 ≥20 件制品(取全 30)

三件套 hash 预注册规约(计算前锁定; deposon-pf-observer README 未落盘, 由 Trae 预注册定义, 待 README 对齐):
  content_hash = sha256(json.dumps(artifact_core, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")))[0:12]   # 制品核心内容(不含 three_hashes)
  path_hash    = sha256("<repo_rel_path>#<artifact_id>")[0:12]
                # 制品文件为 deposon_team/products/minimax_artifact_v_<date>.json
  anchor_hash  = sha256(TRUST_ANCHOR_5_CONCAT + "|" + artifact_id + "|" + content_hash)[0:12]
  TRUST_ANCHOR_5_CONCAT = "d78c42f7bab4|0ff54f8d2f60|a8f81c98ea8a|bff8b1ce1f8c|d9a6a099b905"
                (沿 Trae fix_risk2 option_A 裁定的 5 锚 JSON 真值系, 拼接锚 79f8dfa2c296)

盲测协议约定(写入 meta): artifact element **不含 subject 字段**, 主体归属仅由文件名层体现;
  委外 agent 盲测时将三方制品混洗、剥离文件名、重编号后再做单件归属判别。

4 类不变性: 公式-数值-口径-参数四一致(三件套 hash 算法全 script 内可复算) + 三件套 hash +
  判定线预注册(SP_t≥0.7/抗洗白≥0.6 为下游盲测, 本脚本不判) + Spearman(本脚本无提升类声明)
0 LLM / 0 proxy / 0 网关 / key 不入 / 不动 frozen(本脚本只读 minimax 30cells JSON + 常量 5 锚真值)
"""
import json
import hashlib
import os

BASE = r'D:\私人资料\deposon-repo'
SRC = os.path.join(BASE, 'results', 'deposon_volcengine_minimax_m3_30cells_2026_09_10.json')
OUT_DIR = os.path.join(BASE, 'deposon_team', 'products')
OUT = os.path.join(OUT_DIR, 'minimax_artifact_v_2026_09_16.json')
REL_PATH = 'deposon_team/products/minimax_artifact_v_2026_09_16.json'

TRUST_ANCHOR_5_CONCAT = '|'.join([
    'd78c42f7bab4', '0ff54f8d2f60', 'a8f81c98ea8a', 'bff8b1ce1f8c', 'd9a6a099b905',
])


def sha12(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:12]


def canonical(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        src = json.load(f)
    cells = src['cells']
    assert len(cells) >= 20, f'cells 数量 {len(cells)} < 20, 不能建盲测集'
    model = src.get('cells_metadata', {}).get('model', 'minimax-m3')

    artifacts = []
    for i, c in enumerate(cells, 1):
        core = {
            'source_cell': c.get('cell_id'),
            'task': c.get('task'),
            'question': c.get('question'),
            'llm_output': c.get('llm_raw_response'),
            'extracted_answer': c.get('llm_extracted'),
            'is_correct': c.get('is_correct'),
            'latency_ms': c.get('latency_ms'),
            'usage': c.get('usage', {}),
        }
        content_hash = sha12(canonical(core))
        artifact_id = 'artifact_%03d' % i
        path_hash = sha12(REL_PATH + '#' + artifact_id)
        anchor_hash = sha12(TRUST_ANCHOR_5_CONCAT + '|' + artifact_id + '|' + content_hash)
        artifacts.append({
            'artifact_id': artifact_id,
            **core,
            'three_hashes': {
                'content': content_hash,
                'path': path_hash,
                'anchor': anchor_hash,
            },
        })

    # 文件级三件套 hash(不含顶层 meta 的 content_hash = 对 artifacts 数组规范序列化)
    artifacts_canonical = canonical(artifacts)
    file_content_hash = sha12(artifacts_canonical)
    file_path_hash = sha12(REL_PATH)
    file_anchor_hash = sha12(TRUST_ANCHOR_5_CONCAT + '|' + REL_PATH + '|' + file_content_hash)

    out = {
        'meta': {
            'date': '2026-09-16',
            'subject': model,
            'subject_label_location': '仅本 meta 层(盲测时由委外 agent 剥离文件名与本字段)',
            'artifact_count': len(artifacts),
            'source_data': 'results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json (read-only, 0 LLM 抽取)',
            'three_hashes_convention': 'Trae 预注册(README 未落盘): content=sha256(canonical_json(sort_keys,ensure_ascii=False,separators=(",",":")))[0:12]; path=sha256(rel_path#artifact_id)[0:12]; anchor=sha256(trust_anchor_5_concat|artifact_id|content)[0:12]',
            'trust_anchor_5_concat': TRUST_ANCHOR_5_CONCAT,
            'trust_anchor_concat_hash': sha12(TRUST_ANCHOR_5_CONCAT),
            'iron_rules': {
                'no_llm': True, 'no_proxy': True, 'no_gateway': True,
                'no_key': True, 'no_frozen_touch': True,
            },
        },
        'three_hashes': {
            'content': file_content_hash,
            'path': file_path_hash,
            'anchor': file_anchor_hash,
        },
        'artifacts': artifacts,
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out, src, model, len(artifacts)


# ---------- SELF-CHECK (import/执行均 0 LLM, 预注册 + 可复算 + frozen 快核) ----------
out, src, model, n = main()

# 1) 数量 ≥20
assert n >= 20 and n == len(src['cells']), f'制品数 {n}'
print(f'[SC] 制品数 {n} >= 20 PASS (subject={model})')

# 2) 每件制品三件套 hash 可复算(重新独立算一遍, 不信首算)
with open(OUT, 'r', encoding='utf-8') as f:
    written = json.load(f)
for i, a in enumerate(written['artifacts'], 1):
    core = {k: a[k] for k in ('source_cell', 'task', 'question', 'llm_output',
                               'extracted_answer', 'is_correct', 'latency_ms', 'usage')}
    ch = sha12(canonical(core))
    ph = sha12(REL_PATH + '#' + 'artifact_%03d' % i)
    ah = sha12(TRUST_ANCHOR_5_CONCAT + '|' + 'artifact_%03d' % i + '|' + ch)
    assert a['three_hashes'] == {'content': ch, 'path': ph, 'anchor': ah}, f'制品 {i} 三件套 hash 复算不一致'
print('[SC] 30/30 制品三件套 hash 独立复算 PASS')

# 3) 主体标签只在 meta 层(盲测协议: element 无 subject 字段)
for a in written['artifacts']:
    assert 'subject' not in a and 'minimax' not in str(a), 'element 泄露主体标签'
print('[SC] element 层零主体标签(盲测协议) PASS')

# 4) trust_anchor 拼接锚已知值核对(79f8dfa2c296)
assert sha12(TRUST_ANCHOR_5_CONCAT) == '79f8dfa2c296', 'trust_anchor 拼接锚漂移'
print('[SC] trust_anchor 拼接锚 == 79f8dfa2c296 PASS')

# 5) 5 锚 JSON 0 触动快核 + 源数据只读
with open(os.path.join(BASE, 'verifier', 'handoff', 'KT_ABC1_anchors_sha256_12.json'), 'rb') as f:
    assert hashlib.sha256(f.read()).hexdigest()[:12] == '03c6c01f3697', '5 锚 JSON 被触动'
with open(SRC, 'rb') as f:
    src_sha = hashlib.sha256(f.read()).hexdigest()[:12]
print(f'[SC] 5 锚 JSON 03c6c01f3697 0 触动 PASS; 源数据 read-only (sha12={src_sha})')

print('_build_minimax_artifact SELF-CHECK ALL PASS')
print('OUT ->', OUT, f'({os.path.getsize(OUT)} B)')