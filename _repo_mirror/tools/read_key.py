"""Read the key file (GB18030) and extract sk-or-v1-... key without printing/logging it."""
import re
import sys

path = r'C:\Users\Administrator\Desktop\AI\新建文本文档.txt'
with open(path, 'rb') as f:
    raw = f.read()
text = raw.decode('gb18030', errors='replace')

# Extract any sk-or-v1- followed by hex chars (OpenRouter key pattern)
matches = re.findall(r'sk-or-v1-[a-f0-9]{20,}', text, re.IGNORECASE)
if matches:
    # Don't print the full key — just confirm presence and length
    k = matches[0]
    print(f"FOUND_KEY len={len(k)} prefix={k[:12]}... suffix={k[-6:]}")
    # Write only a marker to a temp file for the next step to read
    with open(r'D:\私人资料\deposon-repo\tools\_key_marker.tmp', 'w', encoding='utf-8') as mf:
        mf.write("KEY_PRESENT\n")
    # Save the key length so we can verify
    print(f"KEY_LEN={len(k)}")
else:
    print("NO_KEY_FOUND")
    # Print a tiny redacted sample to help debug if needed
    print("---FILE PREVIEW (first 500 chars)---")
    print(text[:500])
    print("---END---")
