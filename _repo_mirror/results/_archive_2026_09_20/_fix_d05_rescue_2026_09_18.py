# -*- coding: utf-8 -*-
"""
Trae 2026-09-18 走读改进 #1: D05 数据抢救 (trash -> results 根副本)
背景: D05 bg 任务 (bg_21191cee) 被删后, deepseek_v4 主跑原始数据 (D05 唯一 PASS backbone)
      + qwen3_32b FAIL 证据被移入 `_d05_bg_21191cee_trash_2026_09_18/results/`。
      β JSON (_d05_backbone_robustness_beta_20260918_100853.json) 的 _meta 引用两者
      sha12 (deepseek=0a933d7c8d7a, qwen3=427b18da8114), trash 清空即 D05 溯源链断裂。
改进 2 (verify 脚本修复) 由 Write 直接重写, 本脚本只负责数据面。幂等。0 LLM。
"""
import hashlib, json, shutil
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS = ROOT / 'results'
TRASH = ROOT / '_d05_bg_21191cee_trash_2026_09_18' / 'results'

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

RESCUE = [
    ('_d05_main_run_results_20260918_100853.json', '0a933d7c8d7a',
     'deepseek_v4 主跑 (24/30, acc 0.8, Spearman 0.7917) — D05 唯一 PASS backbone 原始数据'),
    ('_d05_main_run_results_qwen3_failed_20260918_100853.json', '427b18da8114',
     'qwen3_32b FAIL 证据 (HTTP 400, 不擅自换 ID 纪律记录)'),
]

print('=== 改进 1: D05 数据抢救 (trash -> results 根) ===')
for name, expected_sha, desc in RESCUE:
    src, dst = TRASH / name, RESULTS / name
    src_sha = sha12(src)
    print(f'  src sha12={src_sha} expected={expected_sha} -> {"MATCH" if src_sha == expected_sha else "DRIFT!"}')
    assert src_sha == expected_sha, f'trash 内文件哈希与 β JSON _meta 声称不符: {name}'
    if dst.exists():
        print(f'  skip(idempotent): {name} 已在 results 根 (sha12={sha12(dst)})')
    else:
        shutil.copyfile(src, dst)
        got = sha12(dst)
        print(f'  rescued: {name} -> results/ (sha12={got} {"== src OK" if got == src_sha else "COPY-DRIFT!"})')
        assert got == src_sha

note = RESULTS / '_D05_DATA_RESCUE_NOTE_2026_09_18.md'
if not note.exists():
    note.write_text(
        '# D05 数据救援注记 (Trae code, 2026-09-18 走读改进 #1)\n\n'
        '## 事实链\n'
        '- D05 bg 任务 (bg_21191cee) 运行 main runner 后被删除, 其工作区含以下两份关键产物, 被移入\n'
        '  `_d05_bg_21191cee_trash_2026_09_18/results/` (trash 目录, 有被清理灭失风险):\n'
        '  1. `_d05_main_run_results_20260918_100853.json` (sha12=0a933d7c8d7a) — deepseek_v4 主跑原始数据,\n'
        '     D05 唯一 sanity PASS + 30 cells 完整跑成的 backbone (24/30, accuracy 0.8, Spearman vs baseline 0.7917)\n'
        '  2. `_d05_main_run_results_qwen3_failed_20260918_100853.json` (sha12=427b18da8114) — qwen3_32b HTTP 400\n'
        '     FAIL 证据 ("不擅自换 ID" 纪律记录)\n'
        '- `results/_d05_backbone_robustness_beta_20260918_100853.json` 的 `_meta` 字段引用上述两 sha12,\n'
        '  trash 清空即 D05 溯源链断裂。\n\n'
        '## 处置\n'
        '- 本注记随同将两文件**复制**(非移动)回 `results/` 根: 副本哈希与 trash 原件及 β _meta 声称值逐字节一致。\n'
        '- trash 目录原件保持不动 (bg 系统状态不干预)。\n'
        '- 下游引用 (combined report §1.1 source 列、verify_sha 脚本) 以 results 根副本为准。\n\n'
        '— Trae code (审校/走读), 2026-09-18\n', encoding='utf-8')
    print(f'  note written: {note.name}')
else:
    print('  skip(idempotent): 救援注记已存在')

print()
print('_fix_d05_rescue_2026_09_18 DONE')
