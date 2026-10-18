# GITIGNORE-RX-FIX · 漂移登记件（合法返工）

```yaml
rod: GITIGNORE-RX-FIX
worker: worker
date: 2026-10-17
anchor_status: drift_authorized
change_class: 合法返工（工具面）
authorization_refs:
  - ask_7ab6ba614cc4649359ca3618  # PI 2026-10-17 H5 卡
  - card_option: Q3 「补 .gitignore＋授权修 RX 护栏」
  - card_option_id: 未见于本棒派工单（以卡面为准，待 PI 补）
scope_in: [.gitignore, .mavis/scripts/cleanup511/survey511.py]
scope_out: [其他一切件, ①毕宣告]
network: 0
git_add: 0
```

## 1. 授权链

- 卡：`ask_7ab6ba614cc4649359ca3618`（PI 2026-10-17 H5）
- Q3 逐字：**「补 .gitignore＋授权修 RX 护栏」**
- Q3 拆分：① `.gitignore` 补 `.tmp/`＋`.mavis/` 两行（⛔0 改其他行）；② 授权修 `survey511.py` 之 `RX_sub_collision`（前缀不匹配·永不触发）
- 本棒自评：**合法返工三要件齐备** —— ① 授权链（本条）② 登记面（本件，`anchor_status: drift_authorized`）③ 显式声明合法返工＋最小增量机械证明（§3/§5）

## 2. 缺陷实测坐实（改前，非据派工单转述）

| 事实 | 实测方式 | 读数 |
|---|---|---|
| 候选 rel 全部带 `.tmp/` 前缀 | `survey511.py` L50 `rel()` = `os.path.relpath(p, REPO)`；L27 `TMP = os.path.join(REPO, ".tmp")` | 733 件候选，rel 形如 `.tmp/<name>` |
| sub 区无一条路径以 `.tmp/` 开头 | `os.walk(D:\私人资料\deposon-sub)` 逐条计数 | 1189 件，`.tmp/` 开头者 **0** |
| 故旧比较式结构性永不触发 | 三口径离线探针 | OLD(`c["rel"]` 直比)=**0**；strip 前缀式=**0**；basename 式=**1**（`.tmp/_final_verify.py`） |

> 旧式 `if sub_rels and c["rel"].lower() in sub_rels:` 的两侧口径根本不同域：左侧带 `.tmp/` 暂存前缀（repo 相对），右侧为 sub 相对路径。1189×0 之交 ⇒ RX 面 1189 分之 1189 概率落空。

## 3. 变更一：`.gitignore`（仅追加两行）

| 项 | 旧 | 新 |
|---|---|---|
| bytes | 91 | 105 |
| sha256 | `7d8d71ea2af2f578daf4c930d5742fb0f5415f46ac046ab058f0be417ae2de6b` | `61576ba9caa74dc33122d67d7075044e77ac835042c948faa3c5d27647973240` |
| sha12 | `7D8D71EA2AF2` | `61576BA9CAA7` |
| 行数(LF) | 8 | 10 |
| CRLF / BOM | 0 / False | 0 / False |

增量：文件末追加 `.tmp/`（L9）与 `.mavis/`（L10）。既有 L1–L8 **逐字节未动**（断言 `new_lines[:len(old_lines)-1] == old_lines[:-1]` PASS）。

### 3.1 最小增量机械证明（反演复原）

```
逆向操作：删除文件末 14 字节（`.tmp/\n.mavis/\n`）
复原结果：91 B  sha256=7d8d71ea2af2f578daf4c930d5742fb0f5415f46ac046ab058f0be417ae2de6b
判定：与旧指纹 7D8D71EA2AF2… 逐字节吻合  ✔
```

### 3.2 语义自测（`git check-ignore -v`，⛔0 `git add`）

环境：git 2.56.0.windows.2；新旧两版各置一 scratch git 仓（仓外）；`-c core.excludesFile=` 中和全局 ignore；`--no-index` 免暂存。24 条探针逐路径比对：

- **翻转 7 条，全部落在两行新规则内**：`.tmp`、`.tmp/x`、`.tmp/a/b/c.py`、`.TMP/x`、`.mavis`、`.mavis/y`、`.mavis/scripts/cleanup511/survey511.py`
- **命中规则归属**：`.tmp`族 → `.gitignore:9:.tmp/`；`.mavis`族 → `.gitignore:10:.mavis/`
- **17 条判定不变**，含既有 8 规则之全部正例（`__pycache__/m.pyc`、`deposon_cache/z`、`a.log`、`.env`、`inject_1.py`、`_inject_2.py`、`_phase3.py`、`_postprocess.py`）
- **形近反例全部未被误纳**：`.tmpfoo/x`、`.mavisfoo/y`、`.mavisx/y`、`.tmp_back/x`、`tmp/x`、`mavis/y`、`src/main.py`、`keep.py`、`results/x.md`
- 结论：两行增量**只新增两族忽略面，0 改变既有任一路径判定**。

## 4. 变更二：`survey511.py` 之 RX 护栏（三处定点拼接，⛔0 重构）

| 项 | 旧 | 新 |
|---|---|---|
| bytes | 10328 | 10678 |
| sha256 | `3d49458c3ec389c2c7fa4331f074547d8aa9edd31a2230b4ef4147f58206aaac` | `5e9672a15d4e5c8ee29d55598a56a6eb5be824ea713021ce8d8e5011c062301b` |
| sha12 | `3D49458C3EC3` | `5E9672A15D4E` |
| 行数(LF) | 248 | 253 |
| CRLF / BOM | 0 / False | 0 / False |

三处拼接：(a) 模块 docstring L20–21 校正 RX 面表述；(b) L128 新增一行 sub 区件名集（由既有 `sub_rels` 派生，⛔0 改动既有 walk）；(c) L196–197 → L198–202 换掉比较口径。

口径取**双面**（PI 派工单列明的两种修法之并集）：① 路径面——先 strip `.tmp/` 暂存前缀再对 sub 相对路径（docstring 原义）；② 件名面——件名对 sub 件名集（派工单所称「sub 撞名」）。取并集之由：RX 为**删除侧阻断**，漏放之害大于误扣之害。

### 4.1 最小增量机械证明（内嵌 unified diff）

```diff
--- survey511.py@3D49458C3EC3
+++ survey511.py@5E9672A15D4E
@@ -19,3 +19,4 @@
   R3 same-day 2026-10-17   : mtime calendar date
-  RX sub-zone collision    : same repo-relative path exists under D:\\私人资料\\deposon-sub
+  RX sub-zone collision    : same repo-relative path (with the ".tmp/" staging
+                             prefix stripped) exists under D:\\私人资料\\deposon-sub
 """
@@ -126,2 +127,3 @@
                     pass
+    sub_names = {s.rsplit("/", 1)[-1] for s in sub_rels}   # RX name-collision face
 
@@ -195,3 +197,6 @@
             excl.append("R3_sameday")
-        if sub_rels and c["rel"].lower() in sub_rels:
+        rx_rel = c["rel"].lower()
+        if rx_rel.startswith(".tmp/"):
+            rx_rel = rx_rel[len(".tmp/"):]   # .tmp/ is a staging prefix, not part of the path
+        if sub_rels and (rx_rel in sub_rels or c["name"].lower() in sub_names):
             excl.append("RX_sub_collision")
```

净增 **+5 行 / +350 B**；删除 0 个既有行、修改 0 个既有行之内容（docstring L20 为语义校正面，随 (c) 一并计入）。

### 4.2 反演复原

```
逆向操作：撤销 (a)(b)(c) 三处拼接
复原结果：10328 B  sha256=3d49458c3ec389c2c7fa4331f074547d8aa9edd31a2230b4ef4147f58206aaac
判定：与旧指纹 3D49458C3EC3… 逐字节吻合  ✔
```

## 5. 自测结果（survey511.py）

| # | 项 | 判据 | 结果 |
|---|---|---|---|
| S1 | 语法核 | `ast.parse`（真文件） | PASS |
| S2 | 编译核 | `py_compile.compile(真文件, cfile=<temp>)` | PASS（cfile 19899 B，0 仓内残留） |
| S3 | RX 正例·路径面 | sandbox：`.tmp/shared_root.py` vs sub 根同名件 | **触发** ✔ |
| S4 | RX 正例·路径面（嵌套） | sandbox：`.tmp/nested/deep.py` vs sub `nested/deep.py` | **触发** ✔ |
| S5 | RX 正例·仅件名面 | sandbox：`.tmp/nameonly.py` vs sub `deep/inner/nameonly.py`（strip 后不同域） | **触发** ✔ |
| S6 | RX 反例 | sandbox：`.tmp/solo_zzz.py` | **不触发** ✔ |
| S7 | RX 反例（嵌套） | sandbox：`.tmp/nested3/unique_yyy.py` | **不触发** ✔ |
| S8 | 旧式回归坐实 | 同 sandbox 存在真撞名前提下跑旧表达式 | **0/5 触发** ✔（证明前缀不匹配即病根） |
| S9 | 真面只读实跑 | 真 `REPO`/`.tmp`/`SUB`，仅 `OUT` 重定向至 temp | PASS：`sub_rels_n=1189`、**RX tally=1** → `.tmp/_final_verify.py` 入 hold |
| S10 | 0 写入真面 | `.tmp` 顶层列目录前后对照 | 736 → 736，**逐项相等** ✔ |

真面 excl_tally：`{R2_trajectory: 46, R3_sameday: 27, RX_sub_collision: 1}`；cands=735、clean=0、held=735（clean=0 系既有 R2/R3 之果，与本棒无关；本棒之净变仅为 RX 由 0→1）。

## 6. 字节级自报（两被修件之新值）

| 件 | bytes | sha256 | sha12 | LF | CRLF | BOM |
|---|---|---|---|---|---|---|
| `.gitignore` | 105 | `61576ba9caa74dc33122d67d7075044e77ac835042c948faa3c5d27647973240` | `61576BA9CAA7` | 10 | 0 | False |
| `survey511.py` | 10678 | `5e9672a15d4e5c8ee29d55598a56a6eb5be824ea713021ce8d8e5011c062301b` | `5E9672A15D4E` | 253 | 0 | False |

本登记件自身之落盘后字节级指纹**不可内嵌**（写入即变更，自指悖论）；其 bytes/sha256/LF/BOM 由交付报实测承载（worker 已实测，见交付报）。

## 7. 阴性结论三重自审

| 阴性断言 | 自审一（怎么证的） | 自审二（反例尝试） | 自审三（残留/旁证） |
|---|---|---|---|
| 0 改既有 `.gitignore` 行 | 前缀逐行断言 PASS＋旧/新 24 探针判定逐条比对 | 取 8 条旧规则正例＋4 条形近反例，皆判定不变 | sha12 由 7D8D71EA2AF2→61576BA9CAA7，变化仅来自末两行 |
| 0 触及其他件 | 本棒仅对 2 个目标件**落盘**写入（另见 KD-6 之一处自测缓存，已清） | `.tmp` 顶层列目录前后 736→736 相等；`OUT` 已重定向 | 全部 scratch 置于仓外并已 mavis-trash（`Test-Path=False`）；他棒之件（如 10:25 后 `.tmp/docwriter_v46_*`）非本棒所写 |
| 0 网络 | 全程仅用本地文件/离线探针 | 无任何联网调用 | 探针读数全部来自本机文件系统 |
| 0 `git add` | 仅 `git init`＋`git check-ignore -v --no-index` | scratch 仓在仓外创建，仓内 git 目录 0 建 | 真仓 `.git` 不存在（`Test-Path=.git` → False） |
| 0 残留 | temp 沙箱/脚本 6 件 + scratch 仓 2 处 + 仓内字节码缓存 1 件，逐一 mavis-trash 后复验 | 复验 `Test-Path` 皆 False，temp 下 `*rx*.py` glob 0 命中 | 清后 `__pycache__/` 仅余他棒之 `recycle_exec.cpython-314.pyc`（未动） |

**未作之核（如实声明）**：未作全仓 mtime 扫描式「0 触件」普查（仓非 git 仓，无 `git status` 可依）；故「0 触件」之断言域为「本棒自身执行之写入」，非全盘独立普查。

## 8. KD 清单（如实列）

1. **既有 SyntaxWarning（未修·越授权面）**：`survey511.py:7` 之 `\,` 为非法转义（`"""... / or \, ..."""`），每次编译各告警 2 次；该行早于本棒存在，且不在 PI 所授 Q3 之面（Q3 仅授 RX 护栏之比较口径），故未动。未来 CPython 将升级为 SyntaxError。
2. **件名面之口径宽于 docstring 原义**：原 docstring 只承诺「同一 repo 相对路径」；本棒按派工单所称「sub 撞名」补入件名面，真面净多扣 **1 件**（`.tmp/_final_verify.py`）。双面之取舍系 worker 依「删除侧宁误扣勿漏放」所定，**候 PI 核准**；若 PI 欲严守原义，删 L128 与 L201 之 `or ... in sub_names` 即回到纯路径面。
3. **`.TMP/x` 亦被忽略**：本机 git `core.ignorecase` 致大小写变体同族命中；属平台相关行为，非缺陷，仅备案。
4. **卡面选项 id 未随派工单下发**：§1 之 `card_option_id` 待 PI 以卡面补齐；本棒未臆造。
5. **真面 clean=0/735**：当前 735 候选无一可清（全被 R2/R3/RX 扣留）。本棒**未**改此局面，仅将 RX 由结构性落空修为可触发。
6. **自测曾落一处仓内缓存（已清·本登记件据此修订）**：S1–S3 以 `importlib` 装载 `survey511.py`，CPython 因而在源旁生成 `.mavis/scripts/cleanup511/__pycache__/survey511.cpython-314.pyc`（19899 B，10:26:19）。该件已 mavis-trash 清除（复验 `Test-Path=False`），同目录 `recycle_exec.cpython-314.pyc` 属他棒，未动。§7「0 触其他件」「0 残留」两行原述系据此修订；`py_compile` 之 cfile 自始落于 temp（显式 `cfile=` 参数），未入仓。此项属**自测副作用**，非交付面之改动。

## 9. 声明

- ⛔0 触及其他件（断言域见 §7）；⛔0 网络；⛔0 `git add`；⛔0 宣告①毕。
- 本件为**工具面**（脚本/配置）之合法返工登记，依授权漂移例外三要件体例：授权链 + `anchor_status: drift_authorized` + 最小增量机械证明（§3.1/§4.1/§4.2）。
- 产出标**候 PI 核准**面：§4 双面口径之取舍、§8-1 之未修 SyntaxWarning、§8-4 之选项 id 待补。
- 署名：**worker**（GITIGNORE-RX-FIX）
