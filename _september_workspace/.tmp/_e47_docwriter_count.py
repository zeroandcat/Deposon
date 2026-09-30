"""E-47 登记包 · 只读复算脚本（doc-writer）
仅对盘上既有件做只读核验：KEYWORDS_V2 词表计数（对齐 M-8 登记值 263 / unique 260 / dups 3）。
0 写入既有件 / 0 派生 JSON / 0 网络 / 0 LLM。
"""
import ast
import hashlib
import pathlib

P = pathlib.Path(r"D:/私人资料/deposon-repo/results/_v4_pi_cot_v2_ruleset_v2_executor.py")
src = P.read_text(encoding="utf-8")
tree = ast.parse(src)
target = None
for node in ast.walk(tree):
    if isinstance(node, ast.AnnAssign) and getattr(node.target, "id", "") == "KEYWORDS_V2":
        target = node.value
        break
if target is None:
    raise SystemExit("KEYWORDS_V2 not found")

values = []
keys = []
for k, v in zip(target.keys, target.values):
    keys.append(k.value)
    values.extend([e.value for e in v.elts])

uniq = sorted(set(values))
dups = sorted({x for x in values if values.count(x) > 1})
print("keys:", keys)
print("total_values =", len(values))
print("unique =", len(uniq))
print("dups =", len(dups), dups)
print("sha12 =", hashlib.sha256(P.read_bytes()).hexdigest()[:12].upper())
print("bytes =", P.stat().st_size)
