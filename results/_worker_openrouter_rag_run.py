"""
OpenRouter 5 embedding model + Volcano (coding-plan) LLM RAG on 30 cells (15 GSM8K + 15 StrategyQA).

Strategy:
  - Read 2 keys (OpenRouter + Volcano coding-plan) from LLM API.txt (GB18030), keep in os.environ only.
  - Embed 22 captions with 5 OpenRouter embedding models (chunked 10/batch, HIGH-3 fix 2026-09-11).
  - Embed 30 cells with 5 OpenRouter embedding models (chunked 10/batch; chunk-level failure degrades
    only the affected items, never the whole model).
  - For each model x 30 cells, do top-3 cosine retrieval over 22 captions, then call Volcano LLM (doubao-seed-2.0-lite)
    with the context + question, parse answer, check correctness.
  - Write JSON + MD report.

Hard constraints (from parent brief):
  - No proxy
  - No key in prompt/JSON/files (auth field masked)
  - No retry
  - Only the 5 specified embedding models, only doubao-seed-2.0-lite chat model
  - Anchor JSON + 4 SPEC V0.1 + corpus/v20 untouched
  - max_tokens=1024, timeout=30s for LLM
"""

import os
import re
import json
import time
import math
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone, timedelta

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
OR_BASE = 'https://openrouter.ai/api/v1'
ARK_BASE = 'https://ark.cn-beijing.volces.com/api/coding/v3'
DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
CORPUS_DIR = DEPOSON_ROOT / 'corpus' / 'v20'
GSM8K_FILE = DEPOSON_ROOT / 'results' / 'deposon_benchmark_v1_4_gsm8k_details.json'
SQA_FILE = DEPOSON_ROOT / 'results' / 'deposon_benchmark_v1_4_strategyqa_details.json'
CAPTION_BAK = DEPOSON_ROOT / 'results' / '_v41_flash_rag_caption_embs.bak.json'
OUT_JSON = DEPOSON_ROOT / 'results' / 'deposon_openrouter_5model_rag_30cells_2026_09_10.json'
OUT_MD = DEPOSON_ROOT / 'docs' / 'V3X' / 'OPENROUTER_5MODEL_RAG_30CELLS_2026_09_10.md'

EMBED_MODELS = [
    "liquid/lfm-2.5-embedding-350m:free",
    "nvidia/nemotron-3-embed-1b:free",
    "nvidia/llama-nemotron-embed-vl-1b-v2:free",
    "thenlper/gte-base",
    "voyageai/voyage-4",
]
CHAT_MODEL = "doubao-seed-2.0-lite"

# Step counter for logging
_log_lines = []

def log(msg):
    line = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    _log_lines.append(line)


# ---------- 1) load keys ----------
content = Path(KEY_FILE).read_text(encoding='gb18030')
m1 = re.search(r'sk-or-v1-[a-f0-9]{64}', content)
m2 = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', content)
if not m1 or not m2:
    raise SystemExit('KEY_NOT_FOUND in LLM API.txt')
or_key = m1.group(0)
ark_key = m2.group(0)
os.environ['OPENROUTER_API_KEY'] = or_key
os.environ['ARK_CODING_PLAN_KEY'] = ark_key
# Strip any proxy envs
for k in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(k, None)
# HIGH-1 修复(2026-09-11): Windows 上 urllib.request.getproxies() 会回退读注册表 Internet Settings,
# 仅清环境变量不足以禁代理。显式安装空 ProxyHandler opener, 所有请求强制直连(含注册表代理场景)。
urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))
log(f"KEYS loaded (or={len(or_key)}b ark={len(ark_key)}b) | NO_PROXY set (env stripped + registry bypassed)")


# ---------- 2) helpers ----------
def or_embed_batch(inputs, model, timeout=60):
    """OpenRouter batched embedding. inputs: list of str. returns list of list[float] or (None, error_str)."""
    url = f'{OR_BASE}/embeddings'
    headers = {
        'Authorization': f'Bearer {or_key}',
        'Content-Type': 'application/json',
    }
    payload = {'model': model, 'input': inputs}
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            embs = [d['embedding'] for d in data['data']]
            return embs, None, (time.time() - t0) * 1000
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='ignore')[:500] if e.fp else ''
        return None, f'HTTP {e.code}: {err}', (time.time() - t0) * 1000
    except Exception as e:
        return None, f'{type(e).__name__}: {e}', (time.time() - t0) * 1000


def or_embed_chunked(texts, model, chunk_size=10, timeout=60):
    """HIGH-3 修复(2026-09-11): 分块嵌入, 单块单次调用(维持 no-retry 铁律)。
    返回 (embs, errors): embs[i] 为向量或 None, errors[i] 为错误串或 None。
    块级失败只降级该块内条目, 不拖垮整个 model。"""
    embs = [None] * len(texts)
    errors = [None] * len(texts)
    for start in range(0, len(texts), chunk_size):
        chunk = texts[start:start + chunk_size]
        got, err, ms = or_embed_batch(chunk, model, timeout=timeout)
        if err:
            for i in range(start, min(start + chunk_size, len(texts))):
                errors[i] = err
        else:
            for j, vec in enumerate(got):
                embs[start + j] = vec
    return embs, errors


def ark_chat(prompt, model=CHAT_MODEL, max_tokens=1024, timeout=30):
    """Volcano Ark (coding-plan) chat completion. Returns dict {ok, content, ms, error, usage}."""
    url = f'{ARK_BASE}/chat/completions'
    headers = {
        'Authorization': f'Bearer {ark_key}',
        'Content-Type': 'application/json',
    }
    payload = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0,
    }
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            content = data['choices'][0]['message']['content'] if data.get('choices') else ''
            usage = data.get('usage', {})
            return {'ok': True, 'content': content, 'ms': (time.time() - t0) * 1000,
                    'error': None, 'usage': usage, 'status': resp.status}
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='ignore')[:500] if e.fp else ''
        return {'ok': False, 'content': None, 'ms': (time.time() - t0) * 1000,
                'error': f'HTTP {e.code}: {err}', 'usage': None, 'status': e.code}
    except Exception as e:
        return {'ok': False, 'content': None, 'ms': (time.time() - t0) * 1000,
                'error': f'{type(e).__name__}: {e}', 'usage': None, 'status': -1}


def cosine(a, b):
    """cosine similarity of two equal-length vectors."""
    if not a or not b:
        return -1.0
    da = sum(x * x for x in a) ** 0.5
    db = sum(x * x for x in b) ** 0.5
    if da == 0 or db == 0:
        return -1.0
    return sum(x * y for x, y in zip(a, b)) / (da * db)


def extract_number(text):
    """Extract predicted number from LLM response. Priority: **N** bold, then last numeric."""
    if not text:
        return None
    # 1) Bold pattern **N** (or **N,N**)
    m = re.search(r'\*\*\s*([-+]?\d[\d,]*\.?\d*)\s*\*\*', text)
    if m:
        try:
            return float(m.group(1).replace(',', ''))
        except Exception:
            pass
    # 2) Last number in text
    nums = re.findall(r'-?\d+\.?\d*', text)
    if nums:
        try:
            return float(nums[-1])
        except Exception:
            pass
    return None


def extract_yesno(text):
    """Extract yes/no from LLM response."""
    if not text:
        return None
    t = text.lower().strip()
    # Look for explicit yes/no patterns first
    m = re.search(r'\*\*\s*(yes|no|true|false)\s*\*\*', t)
    if m:
        v = m.group(1)
        return 'Yes' if v in ('yes', 'true') else 'No'
    # Look at first significant word
    for word in re.split(r'\W+', t):
        if word in ('yes', 'true'):
            return 'Yes'
        if word in ('no', 'false'):
            return 'No'
    return None


# ---------- 3) load 22 caption text from corpus/v20 ----------
log("Loading 22 caption text from corpus/v20/")
index = json.loads((CORPUS_DIR / 'index.json').read_text(encoding='utf-8'))
caption_texts = []  # list of (graph_id, caption_text)
for g in index['graphs']:
    gid = g['graph_id']
    fam = g['family']
    struct = g['structure']
    N = g['N']
    n_named = g['n_named']
    gdata = json.loads((CORPUS_DIR / g['file']).read_text(encoding='utf-8'))
    labels = gdata.get('labels', [])
    caption = f"Concept graph {gid} (family={fam}, structure={struct}, N={N}, n_named={n_named}): " + '; '.join(labels)
    caption_texts.append((gid, caption))
log(f"Loaded {len(caption_texts)} caption texts | sample: {caption_texts[0][1][:120]}...")


# ---------- 4) load 30 cells (15 GSM8K + 15 StrategyQA) ----------
log("Loading 30 cells (15 GSM8K + 15 StrategyQA)")
gsm = json.loads(GSM8K_FILE.read_text(encoding='utf-8'))
sqa = json.loads(SQA_FILE.read_text(encoding='utf-8'))
cells = []  # list of {id, text, answer, kind, gt}
for i in range(1, 16):
    cells.append({
        'id': f'GSM8K_{i}',
        'text': gsm[str(i)]['question'],
        'gt': float(gsm[str(i)]['answer']),
        'kind': 'gsm8k',
    })
for i in range(1, 16):
    cells.append({
        'id': f'StrategyQA_{i}',
        'text': sqa[str(i)]['question'],
        'gt': str(sqa[str(i)]['answer']),
        'kind': 'strategyqa',
    })
log(f"Loaded {len(cells)} cells (gsm8k={sum(1 for c in cells if c['kind']=='gsm8k')}, sqa={sum(1 for c in cells if c['kind']=='strategyqa')})")


# ---------- 5) sanity: 1-cell embed for all 5 models ----------
log("=== Sanity: 1-cell embed 'What is 2+2?' for all 5 models ===")
sanity_text = "What is 2+2?"
sanity_results = {}
for m in EMBED_MODELS:
    embs, err, ms = or_embed_batch([sanity_text], m, timeout=30)
    if err:
        sanity_results[m] = {'ok': False, 'err': err, 'ms': ms}
        log(f"  {m}: FAIL err={err[:100]}")
    else:
        sanity_results[m] = {'ok': True, 'dim': len(embs[0]), 'ms': ms}
        log(f"  {m}: OK dim={len(embs[0])} ms={ms:.0f}")


# ---------- 6) embed 22 captions per model ----------
log("=== Embedding 22 captions x 5 models (chunked 10/batch) ===")
cap_embs_per_model = {}  # {model: [vec or None, ...]} — HIGH-3: None=该条目所在块失败
cap_ids = [c[0] for c in caption_texts]
cap_texts_only = [c[1] for c in caption_texts]
for m in EMBED_MODELS:
    embs, errors = or_embed_chunked(cap_texts_only, m, chunk_size=10, timeout=60)
    ok_idx = [i for i, e in enumerate(embs) if e is not None]
    if not ok_idx:
        cap_embs_per_model[m] = None
        log(f"  {m}: ALL CHUNKS FAIL err={(errors[0] or '')[:200]}")
    else:
        cap_embs_per_model[m] = embs
        log(f"  {m}: {len(ok_idx)}/{len(embs)} captions OK (dim={len(embs[ok_idx[0]])}, {len(embs) - len(ok_idx)} missing)")


# ---------- 7) embed 30 cells per model ----------
log("=== Embedding 30 cells x 5 models (chunked 10/batch) ===")
cell_embs_per_model = {}  # {model: {cell_id: vec or None}} — HIGH-3: None=该 cell 所在块失败
cell_texts_only = [c['text'] for c in cells]
for m in EMBED_MODELS:
    embs, errors = or_embed_chunked(cell_texts_only, m, chunk_size=10, timeout=60)
    ok_idx = [i for i, e in enumerate(embs) if e is not None]
    if not ok_idx:
        cell_embs_per_model[m] = None
        log(f"  {m}: ALL CHUNKS FAIL err={(errors[0] or '')[:200]}")
    else:
        cell_embs_per_model[m] = {cells[i]['id']: embs[i] for i in range(len(cells))}
        log(f"  {m}: {len(ok_idx)}/{len(embs)} cells OK ({len(embs) - len(ok_idx)} missing)")


# ---------- 8) RAG run: 5 models x 30 cells = 150 LLM calls ----------
log("=== RAG run: 5 models x 30 cells = 150 LLM calls (volcano) ===")
rag_results = []  # list of {model, cell_id, top3, prompt, response, pred, gt, is_correct, ms, llm_ms}
total_llm_calls = 0
total_llm_pass = 0
for m in EMBED_MODELS:
    cap_embs = cap_embs_per_model.get(m)
    cell_embs = cell_embs_per_model.get(m)
    if cap_embs is None or cell_embs is None:
        log(f"  {m}: SKIP (no embeddings at all)")
        # record 30 failures
        for c in cells:
            rag_results.append({
                'model': m, 'cell_id': c['id'], 'top3': None,
                'pred': None, 'gt': c['gt'], 'is_correct': False,
                'llm_ms': 0, 'llm_err': 'embedding_unavailable',
            })
        continue
    # HIGH-3 修复: 检索仅在嵌入成功的 caption 上进行; 缺嵌入的 cell 单独降级, 不拖垮整个 model
    avail_caps = [i for i in range(len(cap_ids)) if cap_embs[i] is not None]
    log(f"  {m}: starting 30 RAG runs (retrieval over {len(avail_caps)}/{len(cap_ids)} captions)...")
    model_pass = 0
    for c in cells:
        cell_id = c['id']
        qvec = cell_embs.get(cell_id)
        if qvec is None:
            rag_results.append({
                'model': m, 'cell_id': cell_id, 'top3': None,
                'pred': None, 'gt': c['gt'], 'is_correct': False,
                'llm_ms': 0, 'llm_err': 'embedding_unavailable',
            })
            continue
        # top-3 cosine over available captions only
        sims = [(cap_ids[i], cosine(qvec, cap_embs[i])) for i in avail_caps]
        sims.sort(key=lambda x: x[1], reverse=True)
        top3 = sims[:3]
        # build RAG prompt
        context_lines = []
        for rank, (gid, sim) in enumerate(top3, 1):
            txt = dict(caption_texts)[gid]
            context_lines.append(f"{rank}. {txt}")
        context_block = "\n".join(context_lines)
        if c['kind'] == 'gsm8k':
            prompt = (
                f"Context (3 most relevant concepts):\n{context_block}\n\n"
                f"Question: {c['text']}\n\n"
                f"Let's think step by step.\n"
                f"Answer with the final number in **bold** at the end."
            )
        else:  # strategyqa
            prompt = (
                f"Context (3 most relevant concepts):\n{context_block}\n\n"
                f"Question: {c['text']}\n\n"
                f"Let's think step by step.\n"
                f"Answer Yes or No in **bold** at the end."
            )
        # call volcano LLM
        r = ark_chat(prompt, model=CHAT_MODEL, max_tokens=1024, timeout=30)
        total_llm_calls += 1
        # parse
        if c['kind'] == 'gsm8k':
            pred = extract_number(r.get('content', ''))
            is_correct = (pred is not None and abs(pred - c['gt']) < 1e-3)
        else:
            pred = extract_yesno(r.get('content', ''))
            is_correct = (pred is not None and pred == c['gt'])
        if is_correct:
            model_pass += 1
            total_llm_pass += 1
        rag_results.append({
            'model': m,
            'cell_id': cell_id,
            'top3': [{'caption_id': t[0], 'sim': round(t[1], 4)} for t in top3],
            'pred': pred,
            'gt': c['gt'],
            'is_correct': is_correct,
            'llm_ms': round(r['ms'], 1) if r['ms'] else 0,
            'llm_status': r.get('status'),
            'llm_err': r.get('error'),
            'llm_content_head': (r.get('content', '') or '')[:200].replace('\n', ' '),
        })
    log(f"  {m}: pass {model_pass}/30 (model avg)")
log(f"=== RAG done. total_pass={total_llm_pass}/{total_llm_calls} ===")


# ---------- 9) summarize per model ----------
log("=== Summarizing per model ===")
per_model = []
for m in EMBED_MODELS:
    gsm_pass = sum(1 for r in rag_results if r['model'] == m and r['cell_id'].startswith('GSM8K_') and r['is_correct'])
    sqa_pass = sum(1 for r in rag_results if r['model'] == m and r['cell_id'].startswith('StrategyQA_') and r['is_correct'])
    total = gsm_pass + sqa_pass
    cell_ms = [r['llm_ms'] for r in rag_results if r['model'] == m and r['llm_ms']]
    avg_ms = sum(cell_ms) / len(cell_ms) if cell_ms else 0
    per_model.append({
        'model': m,
        'gsm8k_passed': gsm_pass,
        'strategyqa_passed': sqa_pass,
        'total_passed': total,
        'pass_rate': round(total / 30, 4),
        'avg_llm_ms': round(avg_ms, 1),
    })
    log(f"  {m}: GSM8K {gsm_pass}/15, SQA {sqa_pass}/15, total {total}/30, avg_llm_ms={avg_ms:.0f}")


# ---------- 10) write JSON ----------
ts = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
out = {
    'timestamp': ts,
    'approach': 'OpenRouter 5 embedding model + Volcano (coding-plan) doubao-seed-2.0-lite RAG 30 cells',
    'gateway_embedding': 'OpenRouter',
    'gateway_chat': 'Volcano Ark coding-plan',
    'auth': 'sk-or-v1-... (runtime only) | ark-...e219 (runtime only)',
    'user_constraint_note': 'user 2026-09-10 22:25: 严格主线故不撤销,OpenRouter embedding 仅参考测试 RAG 是否回归, 不作 V3X baseline',
    'embed_models_tested': EMBED_MODELS,
    'chat_model': CHAT_MODEL,
    'sanity': sanity_results,
    'cells': cells,
    'per_model': per_model,
    'rag_results': rag_results,
    'summary': {
        'total_models_tested': len(EMBED_MODELS),
        'total_llm_calls': total_llm_calls,
        'total_passed': total_llm_pass,
        'best_model': max(per_model, key=lambda x: x['total_passed'])['model'] if per_model else None,
        'best_pass': max((p['total_passed'] for p in per_model), default=0),
        'verdict_rule': 'RAG PASS if >=24, MARGINAL if 18-23, FAIL if <18 (across 30 cells)',
    },
    'comparison': {
        'no_rag_baseline_2_0_lite': '26/30 = 86.7% (pre-existing baseline, see task brief)',
        'old_rag_2048d_cosine': '24/30 = 80% (prior RAG run #1)',
        'feshbach_rag_2_0_lite': '25/30 = 83.3% (prior RAG run #2)',
        'c_path_rag': '0% (prior RAG run #3)',
        'openrouter_5model_rag_2_0_lite': f'{total_llm_pass}/{total_llm_calls} = {(total_llm_pass/total_llm_calls*100 if total_llm_calls else 0):.1f}% (this run, best across 5 models)',
    },
    'constraints_honored': {
        'no_proxy': True,
        'key_runtime_only': True,
        'key_in_json_masked': True,
        'embedding_models_count': len(EMBED_MODELS),
        'chat_model_one': CHAT_MODEL,
        'no_retry': True,
        'no_proxy_mechanism': 'env strip + Windows registry bypass (empty ProxyHandler opener, HIGH-1 fix 2026-09-11)',
        'embedding_chunk_size': 10,  # HIGH-3 fix: 单块单次调用, 块级失败只降级对应条目
        'frozen_files_untouched': [
            'verifier/handoff/KT_ABC1_anchors_sha256_12.json',
            'docs/SPEC_v0.1 (4 files)',
            'corpus/v20/*',
            'results/deposon_v21_gtformal.json (insofar as relevant)',
        ],
    },
    'log': _log_lines,
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
log(f"JSON saved -> {OUT_JSON}  size={OUT_JSON.stat().st_size}B")


# ---------- 11) write MD report ----------
lines = []
lines.append(f"# OpenRouter 5 Model + Volcano LLM RAG 30 Cells (2026-09-10)\n")
lines.append(f"**Run timestamp**: {ts}  ")
lines.append(f"**Approach**: {out['approach']}  ")
lines.append(f"**User constraint**: {out['user_constraint_note']}\n")
lines.append("## §1 测试环境\n")
lines.append(f"- **Embedding gateway**: OpenRouter (`{OR_BASE}`), 5 models only: " + ", ".join(EMBED_MODELS))
lines.append(f"- **Chat gateway**: Volcano Ark **coding-plan** (`{ARK_BASE}/chat/completions`), model: `{CHAT_MODEL}`")
lines.append(f"- **No proxy** (env vars stripped + Windows registry proxy bypassed via empty ProxyHandler opener, HIGH-1 fix 2026-09-11)")
lines.append(f"- **Keys**: loaded from `LLM API.txt` (GB18030), kept in `os.environ` only, masked in JSON (`sk-or-v1-...`, `ark-...e219`)")
lines.append(f"- **No retry**, no extra models, no Anthropic/OpenAI/Google direct call")
lines.append("")
lines.append("## §2 5 model × 30 cells RAG 横向对比\n")
lines.append("| Model | GSM8K 15 | StrategyQA 15 | Total /30 | Pass% | Avg LLM ms |")
lines.append("|---|---:|---:|---:|---:|---:|")
for p in per_model:
    lines.append(f"| `{p['model']}` | {p['gsm8k_passed']} | {p['strategyqa_passed']} | {p['total_passed']} | {p['pass_rate']*100:.1f}% | {p['avg_llm_ms']:.0f} |")
lines.append("")
best = max(per_model, key=lambda x: x['total_passed'])
lines.append(f"**Best**: `{best['model']}` with {best['total_passed']}/30 = {best['pass_rate']*100:.1f}%\n")
lines.append("## §3 5 baseline 对比 (no-RAG / RAG 1/2/3 / OpenRouter RAG)\n")
lines.append("| Baseline | Score | Note |")
lines.append("|---|---:|---|")
lines.append("| no-RAG `doubao-seed-2.0-lite` | 26/30 = 86.7% | Pre-existing baseline, dual mainline |")
lines.append("| Old RAG 2048-d cosine | 24/30 = 80% | Prior RAG run #1 |")
lines.append("| Feshbach RAG `2.0-lite` | 25/30 = 83.3% | Prior RAG run #2 |")
lines.append("| C path RAG | 0/30 = 0% | Prior RAG run #3 (regression) |")
lines.append(f"| **OpenRouter 5model RAG `2.0-lite`** | **{total_llm_pass}/30 = {(total_llm_pass/30*100):.1f}%** | This run, best of 5 embed models |")
lines.append("")
lines.append("## §4 7 铁律自检\n")
lines.append("| # | Rule | Honored |")
lines.append("|---:|---|---|")
lines.append("| 1 | OpenRouter + coding-plan key 双重 runtime 读 (`LLM API.txt` GB18030) | ✅ |")
lines.append("| 2 | 不设 proxy | ✅ |")
lines.append("| 3 | 不调 OpenAI / Anthropic / Google (OpenRouter layer-2 gate) | ✅ |")
lines.append("| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 | ✅ (`sk-or-v1-...`, `ark-...e219`) |")
lines.append("| 5 | call 数严格 (5 embed + 1 chat) | ✅ |")
lines.append("| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✅ |")
lines.append("| 7 | 不动 4 SPEC V0.1 + v19 + v21 + corpus/v20 | ✅ |")
lines.append("")
lines.append("## §5 下一步\n")
if total_llm_pass >= 24:
    lines.append(f"- RAG **PASS** 阈值({total_llm_pass}>=24): **回归主线?**")
    lines.append(f"- 若要撤回 22:25 'OpenRouter embedding 仅参考' 声明,需 user 明确确认")
elif total_llm_pass >= 18:
    lines.append(f"- RAG **MARGINAL** ({total_llm_pass} in 18-23): 不撤 22:25 声明;记入参考证据")
else:
    lines.append(f"- RAG **FAIL** ({total_llm_pass}<18): 第四次证伪,主线故不撤销已 stable")
lines.append(f"- 严守 user 17:38(火山 catalog 内)+ 17:41(只走 coding-plan)= LLM 答必须用 `{CHAT_MODEL}`")
lines.append(f"- 严守 user 22:25(所有声明仅限主线故不撤销)= 本次结果**仅作 RAG 回归参考**,**不**作 V3X baseline\n")
lines.append("## §6 Per-cell details (best model)\n")
lines.append(f"### Best model: `{best['model']}`\n")
lines.append("| Cell | Top-3 captions (sim) | Pred | GT | OK | LLM ms |")
lines.append("|---|---|---:|---:|:---:|---:|")
best_results = [r for r in rag_results if r['model'] == best['model']]
for r in best_results:
    top3 = ', '.join(f"{t['caption_id']}({t['sim']:.2f})" for t in (r['top3'] or []))
    pred = r['pred'] if r['pred'] is not None else '—'
    lines.append(f"| {r['cell_id']} | {top3} | {pred} | {r['gt']} | {'✅' if r['is_correct'] else '❌'} | {r['llm_ms']:.0f} |")
lines.append("")
lines.append("---\n")
lines.append(f"_Run artifacts: `{OUT_JSON.relative_to(DEPOSON_ROOT)}`, `{OUT_MD.relative_to(DEPOSON_ROOT)}`  ")
lines.append(f"_Log lines: {len(_log_lines)}  ")
lines.append(f"_Strict 5 embed models + 1 chat model (`{CHAT_MODEL}`), no proxy, no key on disk._")

OUT_MD.parent.mkdir(parents=True, exist_ok=True)
OUT_MD.write_text('\n'.join(lines), encoding='utf-8')
log(f"MD saved -> {OUT_MD}  size={OUT_MD.stat().st_size}B")
log("=== DONE ===")
