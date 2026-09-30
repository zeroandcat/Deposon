# -*- coding: utf-8 -*-
"""
_v5_wa_s3_fix — B 档授权修复（F3 类·标注失实 → 只追加勘误注记）
目标：results/_plan_v3_pending_verify_2026_09_30.md 附记-1「ffda214d1917 盘上 0 命中」
事实：该件在归档区（本棒独立复算坐实，SHA 逐字吻合）
授权：委托 §B.2 F3「只追加勘误注记，0 回改历史行」
幂等 + 前缀 SHA 自证 + compile 不适用（md 件）
"""
import hashlib
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
TARGET = REPO / 'results' / '_plan_v3_pending_verify_2026_09_30.md'
ARCH = Path(r'D:\私人资料\_non_upload_local_archive') / '_movedout_scratch_2026_09_29' / 'verif_doubt6_v_20260928' / '_v5_trae_doubt6_verify_2026_09_28.md'

def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]

# 事实侧独立复算
arch_sha = sha12b(ARCH.read_bytes())
arch_size = ARCH.stat().st_size
print(f'归档区件实测: {arch_sha} / {arch_size:,} B')
assert arch_sha == 'ffda214d1917', '归档区件 SHA 与委托记录不符，中止'

before = TARGET.read_bytes()
n_before = len(before)
sha_before = sha12b(before)
sha_full = hashlib.sha256(before).hexdigest()
print(f'目标件改前: {sha_before} / {n_before:,} B')

APPEND = """

---

## 附录 A · 勘误注记（受托方 Trae code 追加 · 2026-09-30 · 委托件 §B.2 F3 授权「标注失实——只追加勘误注记，0 回改历史行」）

> **性质**：纯追加。本件 §1–§八 及附记-1/附记-2 历史行**一字不动**（追加前 {NB:,} B / SHA-256 全文 `{SH}` 逐字保留）。
> **署名如实**：本附录为受托方 Trae code 独立复核结论，**以引述形式**入勘误链；**不自动生效**，是否采认由 PI 拍板。

### A.1 附记-1「`ffda214d1917`（Trae 混合体）盘上 0 命中」——**检索面缺陷（0 命中断言的检索范围不含归档区）**

本件附记-1 记「全仓递归 `*trae_doubt6*` 文件名枚举 ⇒ 仅 1 件 r3verifier；原路径不在盘；`ffda214d1917` **0 命中**」。

**受托方独立复算（2026-09-30）**：该件**在盘**，位于归档区——

| 项 | 实测 |
|---|---|
| 路径 | `D:\\私人资料\\_non_upload_local_archive\\_movedout_scratch_2026_09_29\\verif_doubt6_v_20260928\\_v5_trae_doubt6_verify_2026_09_28.md`（另有同内容副本 `_merged_canonical_snapshot_224910.md`） |
| SHA-12 | **`ffda214d1917`**（与本件附记-1 所记「混合体」值**逐字吻合**） |
| 字节 | **51,778 B** |
| mtime | 2026-09-28 22:46:33 |

⇒ 附记-1 的「0 命中」系**检索面缺陷**：其「全仓递归」实际覆盖面为 `deposon-repo`（仓内），**未含 `_non_upload_local_archive` 归档区**。附记-1「根因未坐实」一栏中的第三假设「本棒检索面外」**即为实情**——该件于 09-29 归档清理中被移入归档区（同目录 `_pre_b11_snapshot.json` 等 24 件同期移入可佐证）。

**对 v3 §B4（撞名归属 PI 拍板项）的影响**：归属比对面现有**两件**可依：
1. 仓内 `results/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md`（`58101ef93a6f` / 30,192 B / mtime 2026-09-30 17:02:47——属并发写入 7 件面，本附录 0 覆写）；
2. 归档区 `ffda214d1917` / 51,778 B（即 v3 §一 所记「混合体」本体）。

**本附录 0 判归属**（沿委托 §C.4：撞名「混合体」归属 = PI 拍板项）。

### A.2 复算方式（可复算）

`deposon_team/plugins/_v5_wa_s2_2026_09_30.py`（实跑 exit 0）：对归档区路径逐件 `hashlib.sha256(bytes)[:12]`，`ffda214d1917` 在归档区 `verif_doubt6_v_20260928/` 目录命中 2 处（`_v5_trae_doubt6_verify_2026_09_28.md` 与 `_merged_canonical_snapshot_224910.md`，二者**逐字节相同**）。

### A.3 边界

- 本附录**0 回改**附记-1 历史行（其「本棒 0 判定」的如实交代本身成立——该棒确实未扫归档区）；
- **0 触动**归档区任何件（含 `ffda214d1917` 本体：归档面属 PI 整理面执行中，沿委托 §B.3「归档转移面 0 搬动」）；
- **0 触动**并发写入 7 件面（`_plan_v3_pending_verify_2026_09_30.md` 本件 mtime = 17:03:36，**不在** 17:02:47 七件名单内，可安全追加）。

*追加：受托方 Trae code · 2026-09-30（§B.2 F3 授权档）*
""".replace('{NB:,}', f'{n_before:,}').replace('{SH}', sha_full)

after = before + APPEND.encode('utf-8')
TARGET.write_bytes(after)
prefix_ok = hashlib.sha256(TARGET.read_bytes()[:n_before]).hexdigest() == sha_full
print()
print(f'追加后: {sha12b(after)} / {len(after):,} B')
print(f'前缀 [{n_before:,} B] SHA-256 逐字未变: {prefix_ok}')
print(f'改前 SHA-12 = {sha_before} → 改后 SHA-12 = {sha12b(after)}')
print('_wa_s3 DONE' if prefix_ok else '_wa_s3 FAILED')
