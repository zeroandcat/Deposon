"""
Worker A: kimi-k2.7-code + minimax-m3 × 30 cells 补测
严格按 7 铁律执行:不写 key / 不 proxy / 不重试 / 2 model 严格
"""
import os
import re
import sys
import json
import time
import urllib.request
import urllib.error

# Force UTF-8 io
os.environ['PYTHONIOENCODING'] = 'utf-8'

# ============ 自带 log,直接写文件 (避免 stdout 重定向编码问题) ============
LOG_PATH = r'D:\私人资料\deposon-repo\verifier\_worker_a_run.log'
_log_fh = open(LOG_PATH, 'w', encoding='utf-8', buffering=1)  # line buffered

def log(msg):
    # 同时:文件(UTF-8)+ stdout
    safe = str(msg).encode('utf-8', errors='replace').decode('utf-8')
    _log_fh.write(safe + '\n')
    _log_fh.flush()
    try:
        print(safe, flush=True)
    except Exception:
        pass

# ============ 1. 读 key (GB18030 → env) ============
key_file = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
try:
    with open(key_file, 'r', encoding='gb18030') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(key_file, 'r', encoding='gbk') as f:
        content = f.read()

m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', content)
if not m:
    log("[FATAL] No ark-[REDACTED] key found in LLM API.txt")
    sys.exit(1)
api_key = m.group(0)
os.environ['ARK_CODING_PLAN_KEY'] = api_key

# ============ 2. 不设 proxy ============
for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(k, None)

base_url = 'https://ark.cn-beijing.volces.com/api/coding/v3'
KEY_PRE = api_key[:15]
KEY_END = api_key[-4:]
log(f"[OK] key loaded: {KEY_PRE}...{KEY_END} (len={len(api_key)})")
log(f"[OK] base_url: {base_url}")
log(f"[OK] proxy cleared")

# ============ 3. query_chat ============
def query_chat(prompt, model, max_tokens=1024, timeout=30):
    url = f'{base_url}/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body_bytes = resp.read()
            body = json.loads(body_bytes.decode('utf-8'))
            return {
                'ok': True,
                'status': resp.status,
                'ms': round((time.time() - t0) * 1000, 1),
                'body': body,
                'text': _extract_text(body)
            }
    except urllib.error.HTTPError as e:
        err_body = ''
        try:
            err_body = e.read().decode('utf-8', errors='replace')[:500]
        except Exception:
            pass
        return {
            'ok': False,
            'status': e.code,
            'ms': round((time.time() - t0) * 1000, 1),
            'error': err_body
        }
    except Exception as e:
        return {
            'ok': False,
            'status': -1,
            'ms': round((time.time() - t0) * 1000, 1),
            'error': str(e)[:500]
        }


def _extract_text(body):
    try:
        return body['choices'][0]['message']['content']
    except Exception:
        return ''


def extract_number(response_text):
    """提取数字: 优先 **N** 粗体, fallback 找最后数字"""
    if not response_text:
        return None
    # 1) **N** 粗体
    m = re.search(r'\*\*\s*([\d,.\-+]+)\s*\*\*', response_text)
    if m:
        try:
            return float(m.group(1).replace(',', '').replace('+', ''))
        except Exception:
            pass
    # 2) 最后数字 (允许负号/小数)
    nums = re.findall(r'-?\d+\.?\d*', response_text)
    if nums:
        try:
            return float(nums[-1])
        except Exception:
            pass
    return None


def normalize_answer(ans):
    """GSM8K: number, StrategyQA: yes/no/true/false"""
    if ans is None:
        return None
    s = str(ans).strip().lower()
    # yes/no
    if s in ('yes', 'true', '正确', '是'):
        return 'yes'
    if s in ('no', 'false', '错误', '否', '不正确'):
        return 'no'
    # number
    try:
        return float(s.replace(',', ''))
    except Exception:
        return s


# ============ 4. 加载 benchmark 题目 ============
GSM_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STR_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'

with open(GSM_FILE, 'r', encoding='utf-8') as f:
    gsm_all = json.load(f)
with open(STR_FILE, 'r', encoding='utf-8') as f:
    str_all = json.load(f)


def take_first_n(data, n=15):
    """data 可能是 dict(以 '1','2'...为 key) 或 list,统一返回 list"""
    if isinstance(data, list):
        return data[:n]
    if isinstance(data, dict):
        # 排序 key (按数字)
        keys = sorted(data.keys(), key=lambda x: int(re.sub(r'\D', '', x) or 0))
        return [data[k] for k in keys[:n]]
    return []


def extract_gsm(item):
    q = item.get('question') or item.get('query') or item.get('prompt') or item.get('input') or ''
    a = item.get('answer') or item.get('gold') or item.get('final_answer') or item.get('target') or item.get('ground_truth')
    return q, a

def extract_str(item):
    q = item.get('question') or item.get('query') or item.get('input') or item.get('prompt') or ''
    a = item.get('answer') or item.get('gold') or item.get('final_answer') or item.get('target') or item.get('ground_truth') or item.get('label')
    return q, a

gsm_items = take_first_n(gsm_all, 15)
str_items = take_first_n(str_all, 15)
log(f"[OK] GSM8K loaded: {len(gsm_items)}")
log(f"[OK] StrategyQA loaded: {len(str_items)}")


# ============ 5. sanity check (2 model 1 cell) ============
MODELS = ['kimi-k2.7-code', 'minimax-m3']

log("\n=== Sanity (2 model x 1 cell) ===")
sanity_results = {}
for model in MODELS:
    res = query_chat("What is 1+1? Reply with just the number.", model, max_tokens=1024, timeout=20)
    txt = res.get('text', '')
    sanity_results[model] = {
        'ok': res['ok'],
        'status': res['status'],
        'ms': res['ms'],
        'text': txt[:200],
        'has_2': '2' in txt
    }
    log(f"  [{model}] status={res['status']} ok={res['ok']} ms={res['ms']} has_2={'2' in txt} text={txt[:60]!r}")
    if not res['ok']:
        log(f"    ERROR: {res.get('error', '')[:200]}")


# ============ 6. 60 cells ============
def run_benchmark(model, items, kind):
    """跑一类题目,返回 [{'idx','q','a','gold','pred','passed','ms','status','text'}]"""
    out = []
    for idx, item in enumerate(items, 1):
        q, gold = (extract_gsm if kind == 'gsm' else extract_str)(item)
        # 构造 prompt (English, 简洁)
        if kind == 'gsm':
            prompt = f"Solve: {q}\nShow your reasoning. Final answer must be in **bold** like **42**."
        else:
            prompt = f"Answer yes or no. {q}\nReply with just yes or no."

        res = query_chat(prompt, model, max_tokens=1024, timeout=30)
        text = res.get('text', '')
        ms = res['ms']
        status = res['status']

        if not res['ok']:
            out.append({
                'idx': idx,
                'q': q[:120],
                'gold': gold,
                'pred': None,
                'passed': False,
                'ms': ms,
                'status': status,
                'text': text[:200],
                'error': res.get('error', '')[:200]
            })
            err_s = res.get('error', '')[:80].encode('ascii', errors='replace').decode('ascii')
            log(f"  [{model}|{kind}|{idx}] FAIL status={status} ms={ms} err={err_s}")
            continue

        # 提取答案
        if kind == 'gsm':
            pred = extract_number(text)
            gold_n = normalize_answer(gold)
            passed = (pred is not None and gold_n is not None and abs(pred - gold_n) < 1e-3)
        else:
            pred = normalize_answer(text)
            gold_n = normalize_answer(gold)
            passed = (pred is not None and gold_n is not None and str(pred).lower() == str(gold_n).lower())

        out.append({
            'idx': idx,
            'q': q[:120],
            'gold': gold,
            'pred': pred,
            'passed': passed,
            'ms': ms,
            'status': status,
            'text': text[:200]
        })
        mark = 'PASS' if passed else 'FAIL'
        gold_safe = str(gold).encode('ascii', errors='replace').decode('ascii')
        pred_safe = str(pred).encode('ascii', errors='replace').decode('ascii')
        log(f"  [{model}|{kind}|{idx}] {mark} ms={ms} pred={pred_safe} gold={gold_safe}")
    return out


log("\n=== 60 cells (2 model x 30) ===")
all_results = {}
for model in MODELS:
    log(f"\n--- {model} ---")
    gsm = run_benchmark(model, gsm_items, 'gsm')
    strat = run_benchmark(model, str_items, 'str')
    all_results[model] = {'gsm8k': gsm, 'strategyqa': strat}


# ============ 7. 汇总 + 写 JSON ============
def summarize(model_results):
    g = model_results['gsm8k']
    s = model_results['strategyqa']
    g_pass = sum(1 for x in g if x['passed'])
    s_pass = sum(1 for x in s if x['passed'])
    total_pass = g_pass + s_pass
    avg_ms = sum(x['ms'] for x in g + s) / max(1, len(g) + len(s))
    return {
        'gsm8k_passed': g_pass,
        'strategyqa_passed': s_pass,
        'total_passed': total_pass,
        'pass_rate': round(total_pass / 30, 4),
        'avg_ms': round(avg_ms, 1)
    }


summary_models = []
best_model = None
best_pass = -1
for model in MODELS:
    s = summarize(all_results[model])
    summary_models.append({'model': model, **s})
    if s['total_passed'] > best_pass:
        best_pass = s['total_passed']
        best_model = model

out_json = {
    'timestamp': '2026-09-10T21:13:00+08:00',
    'worker_id': 'A',
    'gateway': '火山方舟 Coding Plan',
    'base_url': base_url,
    'auth': f'{KEY_PRE}...{KEY_END} (key loaded from env at runtime; literal key never written to disk)',
    'max_tokens': 1024,
    'timeout_s': 30,
    'sanity_check': sanity_results,
    'models': summary_models,
    'summary': {
        'total_models_tested': len(MODELS),
        'total_cells_per_model': 30,
        'best_model': best_model
    },
    'detailed': all_results  # 全部 60 cell 详细
}

# 写 JSON
out_json_path = r'D:\私人资料\deposon-repo\results\deposon_volcengine_worker_a_2026_09_10.json'
os.makedirs(os.path.dirname(out_json_path), exist_ok=True)
with open(out_json_path, 'w', encoding='utf-8') as f:
    json.dump(out_json, f, ensure_ascii=False, indent=2)
log(f"\n[OK] JSON written: {out_json_path}")
log(f"[OK] size: {os.path.getsize(out_json_path)} bytes")


# ============ 8. 写报告 markdown ============
md_lines = []
md_lines.append(f"# Worker A 补测报告 — 火山方舟 Coding Plan 2 model x 30 cells")
md_lines.append(f"")
md_lines.append(f"**生成时间**: 2026-09-10 21:13 (Asia/Shanghai)  ")
md_lines.append(f"**Worker**: A  ")
md_lines.append(f"**测试目标**: kimi-k2.7-code + minimax-m3  ")
md_lines.append(f"**题目数**: GSM8K 15 + StrategyQA 15 = 30 cells/model x 2 model = 60 LLM calls  ")
md_lines.append(f"")
md_lines.append(f"## §1 测试环境")
md_lines.append(f"")
md_lines.append(f"| 字段 | 值 |")
md_lines.append(f"|---|---|")
md_lines.append(f"| Gateway | 火山方舟 Coding Plan |")
md_lines.append(f"| base_url | `{base_url}` |")
md_lines.append(f"| auth | `{KEY_PRE}...{KEY_END}` (key 永不入 prompt/JSON/磁盘) |")
md_lines.append(f"| max_tokens | 1024 |")
md_lines.append(f"| timeout/cell | 30 s |")
md_lines.append(f"| temperature | 0.0 |")
md_lines.append(f"| proxy | **无** (火山国内直连) |")
md_lines.append(f"")
md_lines.append(f"**Sanity check** (2 model x 1 cell 'What is 1+1?'):")
md_lines.append(f"")
for model in MODELS:
    s = sanity_results[model]
    md_lines.append(f"- `{model}`: status={s['status']} ok={s['ok']} ms={s['ms']} has_2={s['has_2']} text=`{s['text'][:40]}`")
md_lines.append(f"")
md_lines.append(f"## §2 2 model x 30 cells 结果")
md_lines.append(f"")
md_lines.append(f"| Model | GSM8K (15) | StrategyQA (15) | Total | Pass Rate | Avg ms |")
md_lines.append(f"|---|---|---|---|---|---|")
for s in summary_models:
    md_lines.append(f"| `{s['model']}` | {s['gsm8k_passed']}/15 | {s['strategyqa_passed']}/15 | {s['total_passed']}/30 | {s['pass_rate']*100:.1f}% | {s['avg_ms']} |")
md_lines.append(f"")
md_lines.append(f"### 各 model GSM8K 详情 (15 cells)")
md_lines.append(f"")
for model in MODELS:
    md_lines.append(f"**`{model}` - GSM8K**:")
    md_lines.append(f"")
    md_lines.append(f"| # | gold | pred | passed | ms |")
    md_lines.append(f"|---|---|---|---|---|")
    for x in all_results[model]['gsm8k']:
        md_lines.append(f"| {x['idx']} | {x['gold']} | {x['pred']} | {'PASS' if x['passed'] else 'FAIL'} | {x['ms']} |")
    md_lines.append(f"")
md_lines.append(f"### 各 model StrategyQA 详情 (15 cells)")
md_lines.append(f"")
for model in MODELS:
    md_lines.append(f"**`{model}` - StrategyQA**:")
    md_lines.append(f"")
    md_lines.append(f"| # | gold | pred | passed | ms |")
    md_lines.append(f"|---|---|---|---|---|")
    for x in all_results[model]['strategyqa']:
        md_lines.append(f"| {x['idx']} | {x['gold']} | {x['pred']} | {'PASS' if x['passed'] else 'FAIL'} | {x['ms']} |")
    md_lines.append(f"")
md_lines.append(f"## §3 与已有 baseline 对比")
md_lines.append(f"")
md_lines.append(f"| Model | Pass / 30 | 来源 |")
md_lines.append(f"|---|---|---|")
md_lines.append(f"| doubao-seed-2.0-lite | 26/30 (86.7%) | 已有 baseline |")
md_lines.append(f"| V4.1-Flash | 25/30 (83.3%) | 已有 baseline |")
for s in summary_models:
    md_lines.append(f"| `{s['model']}` | {s['total_passed']}/30 ({s['pass_rate']*100:.1f}%) | 本次 worker A 补测 |")
md_lines.append(f"")
md_lines.append(f"## §4 7 铁律自检")
md_lines.append(f"")
md_lines.append(f"- [x] 1. coding-plan key 从 `LLM API.txt` GB18030 读 -> `os.environ['ARK_CODING_PLAN_KEY']`")
md_lines.append(f"- [x] 2. 无 proxy (env 全清)")
md_lines.append(f"- [x] 3. 仅调 2 model (`kimi-k2.7-code` + `minimax-m3`),不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan")
md_lines.append(f"- [x] 4. key 永不入 prompt / JSON / 磁盘 (auth 字段只截断)")
md_lines.append(f"- [x] 5. 60 calls 严格,无重试,无切超 2 model")
md_lines.append(f"- [x] 6. 未触碰 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`)")
md_lines.append(f"- [x] 7. 未触碰 4 SPEC V0.1 冻结版 / v19 frozen JSON / v21 frozen JSON")
md_lines.append(f"")
md_lines.append(f"## §5 下一步")
md_lines.append(f"")
md_lines.append(f"- 等待 worker B / C / D 补测结果汇总")
md_lines.append(f"- 9 model 完整 pass rate 表生成")
md_lines.append(f"- 与 baseline 26/30 (doubao-seed-2.0-lite) / 25/30 (V4.1-Flash) 对比决定是否进入下一阶段")
md_lines.append(f"")
md_lines.append(f"---")
md_lines.append(f"")
md_lines.append(f"*报告生成: worker A, 2026-09-10 21:13 (Asia/Shanghai)*")

out_md_path = r'D:\私人资料\deposon-repo\docs\V3X\VOLCENGINE_9MODEL_30CELLS_WORKER_A_2026_09_10.md'
os.makedirs(os.path.dirname(out_md_path), exist_ok=True)
with open(out_md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
log(f"[OK] MD written: {out_md_path}")
log(f"[OK] size: {os.path.getsize(out_md_path)} bytes")

# 验证 hash
import hashlib
for p in [out_json_path, out_md_path]:
    with open(p, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    log(f"[HASH] {p} -> {h[:16]}...")

log("\n=== DONE ===")
_log_fh.close()
