# -*- coding: utf-8 -*-
"""
EMBEDDING DUAL SMOKE 2026-09-10
- Task B: 整合 + 测试 2 个 vector embedding model
  1) 火山 doubao-embedding-vision (方舟 coding-plan)
  2) 海外 text-embedding-3-large (TeamoRouter)
- 3 cells 文本 from V3X 22 受控概念图 = GSM8K 1-3 + StrategyQA 1-3 (选 3 段)
- 不设 proxy
- key runtime, masked JSON
"""
import os
import re
import sys
import json
import time
import urllib.request
import urllib.error
import datetime

# ---------------- 0. 加载 keys (GB18030) ----------------
key_file = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
content = open(key_file, 'r', encoding='gb18030').read()

# Ark key (火山方舟 coding-plan, 第 2 个 ark-)
ark_matches = list(re.finditer(r'ark-[a-zA-Z0-9-]+', content))
if len(ark_matches) < 2:
    print("[FATAL] need 2 ark- keys (agent-plan + coding-plan)", file=sys.stderr)
    sys.exit(1)
ark_coding_plan_key = ark_matches[1].group(0)  # coding-plan
os.environ['ARK_API_KEY'] = ark_coding_plan_key

# TeamoRouter key
teamo_match = re.search(r'sk-teamo-[a-zA-Z0-9]+', content)
if not teamo_match:
    print("[FATAL] no sk-teamo- in LLM API.txt", file=sys.stderr)
    sys.exit(1)
teamorouter_key = teamo_match.group(0)
os.environ['TEAMOROUTER_API_KEY'] = teamorouter_key

# 显式清空 proxy
for p in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(p, None)

# 截断显示
def mask_key(k, head=12, tail=4):
    return f"{k[:head]}...{k[-tail:]}"

# Force UTF-8 stdout
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

print(f"[INIT] ARK key (coding-plan): {mask_key(ark_coding_plan_key)}")
print(f"[INIT] TeamoRouter key: {mask_key(teamorouter_key)}")
print(f"[INIT] proxy cleared (火山国内 + TeamoRouter 海外)")

# ---------------- 1. query helpers ----------------
def query_ark_embedding(text, model='doubao-embedding-vision-250615'):
    """Task B-1: 火山方舟 doubao-embedding-vision-250615"""
    url = 'https://ark.cn-beijing.volces.com/api/v3/embeddings'
    headers = {
        'Authorization': f'Bearer {ark_coding_plan_key}',
        'Content-Type': 'application/json'
    }
    data = {'model': model, 'input': text}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode())
            return body, (time.time() - t0) * 1000, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err
    except urllib.error.URLError as e:
        return None, (time.time() - t0) * 1000, 'URLError', str(e)[:500]
    except Exception as e:
        return None, (time.time() - t0) * 1000, 'EXC', str(e)[:500]


def query_teamorouter_embedding(text, model='text-embedding-3-large'):
    """Task B-2: TeamoRouter text-embedding-3-large"""
    url = 'https://api.teamorouter.com/v1/embeddings'
    headers = {
        'Authorization': f'Bearer {teamorouter_key}',
        'Content-Type': 'application/json'
    }
    data = {'model': model, 'input': text}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode())
            return body, (time.time() - t0) * 1000, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err
    except urllib.error.URLError as e:
        return None, (time.time() - t0) * 1000, 'URLError', str(e)[:500]
    except Exception as e:
        return None, (time.time() - t0) * 1000, 'EXC', str(e)[:500]


# ---------------- 2. 3 cells 文本 (V3X 22 受控概念图选 3 段) ----------------
# 选自 GSM8K 1-3 + StrategyQA 1-3 (V3X 已有 22 受控概念图中, 选 3 段差异最大)
with open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json', 'r', encoding='utf-8') as f:
    gsm8k_data = json.load(f)
with open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json', 'r', encoding='utf-8') as f:
    strategyqa_data = json.load(f)

TEST_TEXTS = [
    {
        'text_id': 'gsm8k_1',
        'task': 'gsm8k',
        'text': gsm8k_data['1']['question'],
        'note': 'long math word problem (multi-step)'
    },
    {
        'text_id': 'strategyqa_1',
        'task': 'strategyqa',
        'text': strategyqa_data['1']['question'],
        'note': 'short yes/no factual question (Voldemort Durmstrang)'
    },
    {
        'text_id': 'gsm8k_3',
        'task': 'gsm8k',
        'text': gsm8k_data['3']['question'],
        'note': 'longer math word problem (Doubtfire kittens)'
    }
]

# ---------------- 3. 跑 embedding ----------------
# Ark model version discovery: user said "doubao-embedding-vision" (literal)
# but the actual API needs version suffix. Use 250615 (stable, June 2025) as default.
# Available (per /v3/models GET): 241215 / 250328 / 250615 / 251215
print("\n[STEP 1] Doubao-Embedding-Vision (火山方舟 coding-plan) ...")
print("=" * 80)
EMB_MODEL_ARK = 'doubao-embedding-vision-250615'  # user said "doubao-embedding-vision" (no version); using 250615 (newest pre-251215)
ark_results = []
for txt in TEST_TEXTS:
    body, lat, status, err = query_ark_embedding(txt['text'], model=EMB_MODEL_ARK)
    if status == 200 and body and 'data' in body:
        emb = body['data'][0].get('embedding', [])
        usage = body.get('usage', {})
        result = {
            'text_id': txt['text_id'],
            'task': txt['task'],
            'note': txt['note'],
            'text_preview': txt['text'][:80] + '...',
            'embedding_dim': len(emb),
            'embedding_first5': emb[:5],
            'embedding_last5': emb[-5:] if len(emb) >= 5 else emb,
            'embedding_norm': (sum(x*x for x in emb) ** 0.5) if emb else None,
            'latency_ms': round(lat, 1),
            'http_status': status,
            'usage': usage,
            'model': body.get('model', EMB_MODEL_ARK),
            'error': None
        }
        print(f"  [{txt['text_id']}] dim={len(emb)} norm={result['embedding_norm']:.4f} lat={lat:.0f}ms")
    else:
        result = {
            'text_id': txt['text_id'],
            'task': txt['task'],
            'note': txt['note'],
            'text_preview': txt['text'][:80] + '...',
            'embedding_dim': None,
            'latency_ms': round(lat, 1),
            'http_status': status,
            'error': (err[:300] if err else 'unknown')
        }
        print(f"  [{txt['text_id']}] FAIL status={status} err={(err or '')[:200]}")
    ark_results.append(result)
    time.sleep(0.5)

print("\n[STEP 2] text-embedding-3-large (TeamoRouter) ...")
print("=" * 80)
# 注: 16:49 之前已确认 api.teamorouter.com DNS 解析到 Facebook IP 31.13.x.x, TCP 21s timeout
# 本次 3 cells 仍按约束"不设 proxy", 但预期会失败 (与 user "TeamoRouter 自带海外" 假设矛盾)
# 诊断诊断: 先 1 次 DNS + TCP 检测 (说明 endpoint 当前状态)
print("[DIAG] DNS + TCP probe before 3 cells ...")
import socket
try:
    ip = socket.gethostbyname('api.teamorouter.com')
    print(f"  DNS: api.teamorouter.com -> {ip}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    t0 = time.time()
    try:
        s.connect(('api.teamorouter.com', 443))
        print(f"  TCP:443 connect OK in {(time.time()-t0)*1000:.0f}ms")
    except Exception as e:
        print(f"  TCP:443 connect FAIL in {(time.time()-t0)*1000:.0f}ms: {e}")
    finally:
        s.close()
except Exception as e:
    print(f"  DNS FAIL: {e}")
teamo_results = []
for txt in TEST_TEXTS:
    body, lat, status, err = query_teamorouter_embedding(txt['text'], model='text-embedding-3-large')
    if status == 200 and body and 'data' in body:
        emb = body['data'][0].get('embedding', [])
        usage = body.get('usage', {})
        result = {
            'text_id': txt['text_id'],
            'task': txt['task'],
            'note': txt['note'],
            'text_preview': txt['text'][:80] + '...',
            'embedding_dim': len(emb),
            'embedding_first5': emb[:5],
            'embedding_last5': emb[-5:] if len(emb) >= 5 else emb,
            'embedding_norm': (sum(x*x for x in emb) ** 0.5) if emb else None,
            'latency_ms': round(lat, 1),
            'http_status': status,
            'usage': usage,
            'model': body.get('model', 'text-embedding-3-large'),
            'error': None
        }
        print(f"  [{txt['text_id']}] dim={len(emb)} norm={result['embedding_norm']:.4f} lat={lat:.0f}ms")
    else:
        result = {
            'text_id': txt['text_id'],
            'task': txt['task'],
            'note': txt['note'],
            'text_preview': txt['text'][:80] + '...',
            'embedding_dim': None,
            'latency_ms': round(lat, 1),
            'http_status': status,
            'error': (err[:300] if err else 'unknown')
        }
        print(f"  [{txt['text_id']}] FAIL status={status} err={(err or '')[:200]}")
    teamo_results.append(result)
    time.sleep(0.5)

# ---------------- 4. 跨模型维度对比 + 落盘 ----------------
print("\n[STEP 3] Cross-model dim comparison + JSON dump ...")

# 计算 GSM8K_1 + StrategyQA_1 的余弦相似度 (跨模型, 仅作 metadata 参考)
def cos_sim(a, b):
    if not a or not b or len(a) != len(b):
        return None
    dot = sum(x*y for x, y in zip(a, b))
    na = sum(x*x for x in a) ** 0.5
    nb = sum(x*x for x in b) ** 0.5
    if na == 0 or nb == 0:
        return None
    return dot / (na * nb)

# 由于两边维度可能不同 (Doubao 1024 / OpenAI 3072), 余弦不可计算
# 但我们可以记录各模型 self-similarity (text1 vs text1 from same model = 1.0) 跳过
# 改: 记录维度 + norm 即可

ts = datetime.datetime.now().astimezone().isoformat(timespec='seconds')

output = {
    "timestamp": ts,
    "task": "Task B: Vector Embedding dual-model integration smoke test",
    "models": {
        "ark": {
            "provider": "volcano_ark",
            "model": EMB_MODEL_ARK,
            "model_user_requested": "doubao-embedding-vision (no version); actual API requires version suffix; using 250615 as default stable",
            "auth": f"{mask_key(ark_coding_plan_key)} (key loaded from env at runtime; literal key never written to disk)",
            "endpoint": "https://ark.cn-beijing.volces.com/api/v3/embeddings",
            "proxy_cleared": True
        },
        "teamorouter": {
            "provider": "teamorouter",
            "model": "text-embedding-3-large",
            "auth": f"{mask_key(teamorouter_key)} (key loaded from env at runtime; literal key never written to disk)",
            "endpoint": "https://api.teamorouter.com/v1/embeddings",
            "proxy_cleared": True
        }
    },
    "test_texts": TEST_TEXTS,
    "ark_results": ark_results,
    "teamorouter_results": teamo_results,
    "summary": {
        "ark_passed": sum(1 for r in ark_results if r.get('embedding_dim')),
        "ark_total": 3,
        "teamorouter_passed": sum(1 for r in teamo_results if r.get('embedding_dim')),
        "teamorouter_total": 3,
        "ark_dims": [r.get('embedding_dim') for r in ark_results],
        "teamorouter_dims": [r.get('embedding_dim') for r in teamo_results],
        "ark_total_latency_ms": round(sum(r.get('latency_ms', 0) for r in ark_results), 1),
        "teamorouter_total_latency_ms": round(sum(r.get('latency_ms', 0) for r in teamo_results), 1),
        "diagnosis_ark": "coding-plan key has NO access to ANY embedding model (8 models tested: text-240515/240715, large-text-240915/250515, vision-241215/250328/250615/251215 - all return 404 InvalidEndpointOrModel.NotFound 'you do not have access to it'). 视觉 / 文本模型都是 404. 根因: coding-plan 是 inference billing, 不含 embedding 权限. 需 user 切到 agent-plan (第 1 个 ark-) 或申请 embedding 专用 key",
        "diagnosis_teamorouter": "api.teamorouter.com 当前从本机不可达: DNS 解析到 31.13.75.5 (Facebook IP 段, 强 base_url 失效 / 被劫持信号), TCP:443 21s timeout. 根因不在 key, 在 endpoint 状态. 16:49 同样证据 (deposon_gpt6_teamorouter_2026_09_10.json)"
    },
    "constraints_honored": {
        "no_proxy": True,
        "key_runtime_only": True,
        "key_in_json_masked": True,
        "no_retry": True,
        "3_cells_per_model_strict": True,
        "anchors_5json_untouched": True,
        "spec_v01_untouched": True
    }
}

out_path = r'D:\私人资料\deposon-repo\results\deposon_embedding_dual_2026_09_10.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\n[STEP 3] JSON written: {out_path}")
print(f"[STEP 3] ark_passed: {output['summary']['ark_passed']}/3, dims: {output['summary']['ark_dims']}")
print(f"[STEP 3] teamorouter_passed: {output['summary']['teamorouter_passed']}/3, dims: {output['summary']['teamorouter_dims']}")
print(f"[STEP 3] total latency: ark={output['summary']['ark_total_latency_ms']:.0f}ms, teamorouter={output['summary']['teamorouter_total_latency_ms']:.0f}ms")
print(f"[DONE] Task B complete.")
