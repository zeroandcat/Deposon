"""
V2 启动设置:验证 key 加载 + 代理禁用 + 锚 SHA 校验 + 网络连通性
"""
import os, sys, re, json, hashlib, time
import urllib.request, urllib.error
import socket

print('=== V2 启动设置 ===')

# 1. 读 key
key_file = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
try:
    with open(key_file, 'r', encoding='gb18030') as f:
        content = f.read()
except Exception as e:
    print(f'FAIL 读 key 文件: {e}')
    sys.exit(1)

m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', content)
if not m:
    print('FAIL 未找到 ark-[REDACTED]* key')
    sys.exit(1)
api_key = m.group(0)
os.environ['ARK_CODING_PLAN_KEY'] = api_key
print(f'OK key 前缀: {api_key[:18]}... 长度={len(api_key)}')

# 2. 显式清代理 (Trae 修的 HIGH-1)
for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(k, None)
print('OK 代理已清空 (env + Windows 注册表泄漏防护)')

# 3. 显式空代理 opener
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
urllib.request.install_opener(opener)
print('OK urllib 空代理 opener 安装')

# 4. 校验 5 锚 SHA-12
anchor_path = r'D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json'
try:
    with open(anchor_path, 'rb') as f:
        anchor_sha = hashlib.sha256(f.read()).hexdigest()[:12]
    expected = '03c6c01f3697'
    if anchor_sha == expected:
        print(f'OK 5 锚 SHA-12 匹配: {anchor_sha}')
    else:
        print(f'FAIL 5 锚 SHA-12 不匹配: {anchor_sha} (期望 {expected})')
        sys.exit(1)
except Exception as e:
    print(f'FAIL 校验 5 锚 SHA: {e}')
    sys.exit(1)

# 5. DNS 检查 (避免网络层失败被误判为 API 失败)
try:
    ip = socket.gethostbyname('ark.cn-beijing.volces.com')
    print(f'OK DNS ark.cn-beijing.volces.com → {ip}')
except Exception as e:
    print(f'WARN DNS 解析: {e}')

# 6. base_url
base_url = 'https://ark.cn-beijing.volces.com/api/coding/v3'
print(f'OK base_url: {base_url}')

# 7. 不调用 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan
# 严守 user 17:38 + 17:41
print('OK 仅使用 coding-plan endpoint (user 17:38 + 17:41 硬性)')

# 8. sanity check call to chat
sanity_prompt = [{"role": "user", "content": "Respond with the single word OK."}]
body = json.dumps({
    "model": "doubao-seed-2.0-lite",
    "messages": sanity_prompt,
    "max_tokens": 8,
    "temperature": 0.0
}).encode('utf-8')

req = urllib.request.Request(
    f'{base_url}/chat/completions',
    data=body,
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    },
    method='POST',
)

t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = resp.read().decode('utf-8')
        j = json.loads(data)
        print(f'OK sanity: http={resp.status} latency={int((time.time()-t0)*1000)}ms')
        # Mask the key in any output
        safe = data.replace(api_key, 'ark-[REDACTED]***')
        print(f'   content: {j.get("choices",[{}])[0].get("message",{}).get("content","")[:50]}')
except urllib.error.HTTPError as e:
    body = e.read().decode('utf-8', errors='replace')
    safe = body.replace(api_key, 'ark-[REDACTED]***')
    print(f'FAIL sanity http={e.code}: {safe[:300]}')
except Exception as e:
    print(f'FAIL sanity: {e}')

print('=== 设置完成 ===')
