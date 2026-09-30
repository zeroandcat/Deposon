"""
_v5_qwen_retry_introspect_20260929.py
=====================================
V4 Track2 401 重试棒 - 前置件：key 文件结构勘察（**元数据/模式类，0 明文**）

【铁律】
- key 值 0 入 stdout / 0 入本文件 / 0 入 log / 0 入任何产物
- 本脚本只输出：行号、模式类别（前缀类 / URL 主机名）、字符长度
- URL 主机名非秘密，可登记；key 只登记「前缀类 + 长度 + 行号」

【输出】仅人读，不落盘（调用方直接捕获 stdout）
"""

import hashlib
import os
import re
import sys
from datetime import datetime, timezone

KEY_FILE = r"C:\Users\Administrator\Desktop\AI\LLM API.txt"

# key 特征模式：只用于**分类**，不用于取值
PATTERNS = [
    ("sk-",   re.compile(r"\bsk-[A-Za-z0-9_\-]{8,}")),
    ("ark-",  re.compile(r"\bark-[A-Za-z0-9_\-]{8,}")),
    ("sk-ant", re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{8,}")),
]
URL_RE = re.compile(r"https?://[^\s\"'<>）)，,；;]+")


def classify_secret(seg: str):
    """返回 (类别, 长度) —— 绝不返回明文。"""
    for name, rx in PATTERNS:
        m = rx.search(seg)
        if m:
            return name, len(m.group(0))
    # 兜底：长 token 样式（>=24 字符、无空格、混合大小写/数字）
    toks = [t for t in re.split(r"[\s,;：（）()\[\]]+", seg) if t]
    for t in toks:
        if len(t) >= 24 and re.fullmatch(r"[A-Za-z0-9_\-\.]{24,}", t) and not t.lower().startswith("http"):
            return "opaque-token", len(t)
    return None, 0


def main() -> int:
    if not os.path.isfile(KEY_FILE):
        print("STATE=ENV_BLOCK_NO_KEYFILE")
        return 2

    st = os.stat(KEY_FILE)
    with open(KEY_FILE, "rb") as f:
        raw = f.read()
    sha12 = hashlib.sha256(raw).hexdigest()[:12].upper()

    print("=" * 68)
    print("V4 Track2 401 重试棒 · key 文件结构勘察（0 明文）")
    print("=" * 68)
    print(f"path      = {KEY_FILE}")
    print(f"size      = {st.st_size} bytes")
    print(f"mtime_utc = {datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat()}")
    print(f"mtime_loc = {datetime.fromtimestamp(st.st_mtime).isoformat()}")
    print(f"sha256_12 = {sha12}")
    print(f"lines     = {len(raw.splitlines())}")
    print("-" * 68)

    lines = raw.decode("utf-8", errors="replace").splitlines()
    for i, ln in enumerate(lines, start=1):
        urls = URL_RE.findall(ln)
        cls, ln_len = classify_secret(ln)
        # 行的可公开描述
        desc = []
        for u in urls:
            m = re.match(r"https?://([^/\s]+)(/.*)?$", u)
            if m:
                desc.append(f"URL host={m.group(1)}")
        if cls:
            desc.append(f"SECRET[{cls}] len={ln_len}")
        if not desc:
            # 纯文本行：给长度与首 24 字符（若非 secret）
            s = ln.strip()
            if not s:
                continue
            desc.append(f"text len={len(s)}")
        print(f"  L{i:>3} | " + " ; ".join(desc))

    print("-" * 68)
    print("NOTE: 0 key 值出现在以上任何一行（仅类别 + 长度 + 行号）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
