# -*- coding: utf-8 -*-
"""Trae 2026-09-18 修复 #8: P0-6 skill inventory 使用须知注记 (幂等追加)"""
import hashlib
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
MARK = 'TRAE_FIXED_2026_09_18'
p = ROOT / 'results' / '_mavis_skill_inventory_2026_09_18.md'

def sha12(x):
    return hashlib.sha256(Path(x).read_bytes()).hexdigest()[:12]

if not p.exists():
    print('MISSING', p)
else:
    s = p.read_text(encoding='utf-8')
    if MARK in s:
        print('skip(idempotent)', sha12(p))
    else:
        before = sha12(p)
        note = """
---

## 【TRAE_FIXED_2026_09_18 使用须知】

**Trae code 走读发现（不改本清单原有条目，仅追加使用须知）**：

1. **路径不可解析**：本清单 423 条条目的路径均为**相对形态**（如 `skills\\abstract-writing\\SKILL.md`、
   `v2\\plugin-cache\\official\\sha256-tree-v1-...\\academic-paper-polish\\SKILL.md`），
   但**未声明 base path**。抽查 5 条（含 `.builtin-skills\\code-review\\SKILL.md`）在本仓及
   `D:\\私人资料` 下均不存在。按本项目"路径可对回"的自我标准，**423 条路径当前一条都无法核验**。

   → 使用前请补 base path 声明（推测为 Mavis 的 plugin-cache 根，形如
   `C:\\Users\\Administrator\\.minimax\\v2\\plugin-cache\\...`），或随清单附生成命令。

2. **中文描述编码乱码**：部分条目的中文描述存在 GBK/UTF-8 编码错位
   （如 openclaw-self-evolution-pack / b2b-lead-engine / codex-* 系列 / 末行"论文写作专家"条目），
   可用性受损。

3. **无生成方法说明**：头部仅一行 `TOTAL: 423 unique (441 raw - 14 duplicates)`，
   未说明提取工具、去重规则与失败条目的处理约定（提取失败条目留空或标 `/`，虽为如实处理但需明示）。

**结论**：清单的**条目数与生态细节真实可信**（423 条与头部统计吻合、描述具体、无 TODO/占位残留），
但**路径层零可核验 + 编码受损**，作为可引用资产前需修复上述 3 点。

— Trae code (走读/审校), 2026-09-18
"""
        p.write_text(s.rstrip() + '\n' + note, encoding='utf-8')
        print(f'annotated: {before} -> {sha12(p)}')
print('DONE')
