# -*- coding: utf-8 -*-
"""
_v3_recheck_08c_sha12fix_r1_2026_10_12.py — 项 2 / C-8 修正实现（新名新件 · 0 原地改写）
成因登记：08c executor L526 用 `hasattr(ex08b, "sha12_file")` 前缀判空 ⇒ r2_function_sha12 落 null。
事实：ex08b 的哈希函数名为 `sha12`（def sha12(data: bytes)），非 `sha12_file`。
本件：以修正后取法（ex08b.sha12(08b件字节)）产出 r2_function_sha12，并断言 == b292410d9a69。
沿委托项 2③(c)：若仅登记未实现则写明；本件为「已实现」档，跑 exit 0 即自证。
"""
import hashlib, importlib.util, sys
from pathlib import Path

RES = Path(__file__).resolve().parents[2] / 'results'
EX08B = RES / '_v3_recheck_08b_executor' / 'executor_2026_09_27.py'

spec = importlib.util.spec_from_file_location('e08b_r1', str(EX08B))
ex08b = importlib.util.module_from_spec(spec)
sys.modules['e08b_r1'] = ex08b
spec.loader.exec_module(ex08b)

raw = EX08B.read_bytes()
print(f'hasattr(ex08b, "sha12_file") = {hasattr(ex08b, "sha12_file")}')
print(f'hasattr(ex08b, "sha12")      = {hasattr(ex08b, "sha12")}')
val = ex08b.sha12(raw)
print(f'r2_function_sha12 (修正取法) = {val}')
assert val == 'b292410d9a69', f'修正取法产出 {val} != b292410d9a69'
assert hashlib.sha256(raw).hexdigest()[:12] == 'b292410d9a69'
print('ASSERT PASS: r2_function_sha12 == "b292410d9a69"')
