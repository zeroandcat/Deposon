# P-D 可审计账指纹算法 V0 规范

## 1. 目标与范围

V0 把现有「单工件 SHA-256 12 位锚」工程惯例升级为**第三方可独立验证的密码学协议最小集**。锚定对象固定为 5 个冻结工件：

| 路径 | SHA-256[0:12] |
|---|---|
| `docs/GT_FORMALIZATION_v1.md` | `aeefb8ef6972` |
| `run_v21_gtformal.py` | `9bbe43f41fa8` |
| `run_v22_p1c.py` | `6e9673205dc0` |
| `docs/SPEC_GT2B.md` | `68a5b08ef007` |
| `docs/SPEC_GT8C.md` | `6b09de9911c0` |

### V0 包含

- 内容寻址 R1
- 规范 manifest R2
- 根指纹 R3
- 追加式运行链 R4
- 验证器最小安全边界 R5

### V0 不包含

- 二叉 Merkle 聚合（采用扁平行表）
- 成本线判死（12 个月第三方复现场景）
- 任何高层协议对接（接口在 §7 仅留位）

## 2. 五项需求

### R1 内容寻址

- **输入**：单个工件文件绝对路径
- **输出**：`hex(sha256(file_bytes))[0:12]`（12 位小写 hex）
- **不变量**：相同字节 → 相同 12 位；任意单字节改动 → 完全不同 12 位
- **V0.1 安全防御**：路径为**软链** (`Path.is_symlink() == True`) 时抛 `OSError("E_SYMLINK: ...")`，**不**静默跟随。理由：攻击者用软链替换锚指向恶意文件，`open()` 默认跟随会导致哈希映射到攻击者控制的字节。V0.1 显式拒绝。

### R2 Manifest（规范清单）

- **输入**：5 个锚文件路径集合
- **输出**：JSON 数组 `[{path: str, hash: str}, ...]`
- **排序规则**：按 `path` 字段 ASCII 升序
- **编码**：`utf-8`、`separators=(",",":")`、无 BOM
- **不变量**：
  - 元素个数恒为 5
  - 顺序唯一（任意重排导致序列化字节流不同）

### R3 根指纹

- **输入**：R2 输出的 manifest 字符串
- **输出**：`hex(sha256(manifest_bytes_utf8))[0:12]`
- **不变量**：
  - 5 锚全部命中时，root 必为 12 位 hex 字符串
  - 任一锚的 hash 改变、manifest 排序改变、UTF-8 编码空白改变 → root 改变

### R4 追加式 `runs/` 链

- **记录结构**（JSON Lines，每行一条）：

```
{"ts": "<ISO8601 UTC>", "prev_hash": "<12hex>", "current_root": "<12hex>"}
```

- **链头**：`prev_hash` = `"0"*12`
- **追加规则**：仅 `append`，禁止 `update/delete/truncate`
- **链文件命名**：`verifier/runs/YYYY-MM-DD_pd_v0.jsonl`
- **不变量**：
  - 任何历史记录的 `current_root` 改变 → 后续所有记录的 `prev_hash` 失配

### R5 验证器安全边界

- **暴露**：`compute_root`、`verify_root`、`append_run`、`read_runs_count`
- **不暴露**：
  - 工件文件字节
  - 任意锚点路径下的文件读取 API
  - 任何 `os.listdir`/`open(锚文件)` 类侧信道
- **不变量**：验证器调用者仅能获得 12 位 hex 字符串与布尔值，无法借此推断工件内容

## 3. 数据结构伪代码

```python
# R1
def content_addr(path: str) -> str:
    data = open(path, "rb").read()       # 仅内部读取
    return sha256(data).hexdigest()[:12]

# R2
def manifest(anchor_paths: list[str]) -> str:
    rows = [{"path": p, "hash": content_addr(p)} for p in anchor_paths]
    rows.sort(key=lambda r: r["path"])   # ASCII 升序
    return json.dumps(rows, ensure_ascii=False,
                      separators=(",", ":"))

# R3
def root(manifest_str: str) -> str:
    return sha256(manifest_str.encode("utf-8")).hexdigest()[:12]

# R4
def append_run(prev_hash: str, current_root: str) -> dict:
    return {"ts": "<iso8601>", "prev_hash": prev_hash,
            "current_root": current_root}

# R5：验证器只导出此面
verifier_interface = {
    "compute_root": ["list[str] -> str"],
    "verify_root":  ["str, str -> bool"],
    "append_run":   ["str, str -> dict"],
    "read_runs_count": ["-> int"],
    "verify_chain": ["-> dict"],
}
```

> **V0.1 修正**：R4 `append_run` 伪代码移除 `ts` 参数（与 §5 接口对齐），`ts` 内部自动生成；新增 `verify_chain` 用于 §4 A3 校验。

## 4. 三类攻击 → 检测信号映射

| 攻击 | 输入 | 触发 | 预期输出 |
|---|---|---|---|
| **A1 工件删除** | 5 锚 manifest 引用某路径；从磁盘删除该文件 | `compute_root([5 paths, 含被删])` | `OSError` 家族：`FileNotFoundError` (Linux/macOS) / `PermissionError` (Windows race，OS 还没释放 handle 时) / 任意 `OSError`。错误信息含缺失路径名 = **检出**。等效于 `E_FILE_MISSING` 错误码 |
| **A2 集合重排** | manifest 序列化改为按文件大小排序（或任意非字典序） | 用新序列化字节流重算 `root` | 新 `root` ≠ 公布 `root`；`verify_root(tampered, claimed)` 返回 `False`。diff 信息含"sort_key" 隐式（攻击动作描述） |
| **A3 追加日志回溯** | 改写 `runs/` 链中第 k 条的 `current_root` | 调 `verify_chain()` 重扫链 | `verify_chain` 返回 `valid=False`、`breaks` 非空；首个 break `error_code = "E_CHAIN_BREAK_AT_<file>:<k>"`（比原 spec 的 `E_CHAIN_BREAK_AT_k` 更精细——带文件名） |

> **V0.1 修正**：A1 错误码措辞统一到 OSError 家族（跨平台）；A3 错误码带文件名（定位更准）。

## 5. 实现接口签名（供 deposon-data 实现）

```python
def compute_root(artifact_paths: list[str]) -> str
def verify_root(manifest_str: str, claimed_root: str) -> bool
def append_run(prev_hash: str, current_root: str) -> dict  # ts 内部生成
def read_runs_count() -> int
def verify_chain() -> dict  # V0.1 新增: 校验链, 返回结构化报告
```

- 错误码（V0.1 完整列表）：

- 错误码（V0.1 完整列表）：
  - `E_FILE_MISSING`（A1，跨平台等效于 `OSError` 家族：FileNotFoundError / PermissionError / OSError）
  - `E_SYMLINK`（V0.1 新增，R1 软链拒绝）
  - `E_ROOT_MISMATCH`（A2）
  - `E_CHAIN_BREAK_AT_<file>:<k>`（A3，V0.1 比原 spec 更精细——带文件名）
  - `E_GENESIS_PREV_HASH`（V0.1 新增，链首条 prev_hash ≠ "0"*12）
  - `E_JSON_DECODE_AT_<file>:<n>`（V0.1 新增，链记录 JSON 解析失败）

## 6. 判死线（机械命令模板）

V0 判死线 = **表达力线**（成本线不在 V0 范围）。

**输入**：被攻击的工件集 + V0 公布根指纹 + V0 当前 `runs/` 链。

**3 个攻击脚本**（deposon-data 实现，deposon-reviewer-b 执行）：

1. `python attacks/a1_delete_anchor.py`
2. `python attacks/a2_reshuffle_manifest.py [--root <claimed_root>]`
3. `python attacks/a3_rewrite_runs.py [--chain verifier/runs/<date>_pd_v0.jsonl] [--at <k>]`

> **V0.1.2 修订**：三个攻击脚本统一为**无参直跑**；`--root` / `--chain` / `--at` 等参数仅作占位、脚本内忽略。A1 不再接受 `--missing <path>`（该分支已移除，详见本节末 V0.1.2 注记），从仓库根直接 `python attacks/a1_delete_anchor.py` 即可。

> **V0.1 修正**：原 spec 用 `python -m attacks.X` 命令模板，在 embeddable Python (isolated mode) 下不可用。**改用** `python attacks/X.py` 直跑（从仓库根执行）。Windows 标准 Python 可用 `python -m`；embeddable 不行——为跨环境兼容，统一用直跑。

**每脚本输出**（stdout JSON）：

```json
{"attack": "A1|A2|A3", "verdict": "PASS|FAIL",
 "diff": "<字段或记录定位>"}
```

- `verdict=PASS` = 攻击被检出
- `verdict=FAIL` = 攻击未被检出（指纹方案漏检）

**判死规则**：

- 3/3 脚本 verdict=PASS → V0 表达力存活
- 任一 verdict=FAIL → V0 死，**直接归档**为「hash 锚已够用」的否定结论，不回溯

**执行前置**（reviewer-b 必跑）：

```powershell
# Windows PowerShell (Win32 long path 兼容)
$ts = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$dst = Join-Path $env:TEMP "deposon-audit-$ts"
Copy-Item -Path "D:/私人资料/deposon-repo" -Destination $dst -Recurse -Force
Push-Location $dst
python attacks/a1_delete_anchor.py
python attacks/a2_reshuffle_manifest.py --root <claimed>
python attacks/a3_rewrite_runs.py --chain verifier/runs/2026-09-01_pd_v0.jsonl --at 1
Pop-Location
```

> **V0.1.2 注记（A1 无参化）**：A1 已改为**无参**运行，在 `tempfile.TemporaryDirectory` 内自建 5 锚、删除第 3 个、再用原始 5 路径调 `compute_root`，临时目录随上下文退出自动清理。原 `--missing <path>` 真实攻击分支已**移除**：它调用 `fp.compute_root([missing_path])` 却从不删除该路径——若指向的文件仍存在，`compute_root` 正常返回不抛异常，落入假性 `FAIL`；且该分支诱导操作者在真实仓库对冻结锚 `docs/SPEC_GT8C.md` 执行删除，危害严重。三个攻击脚本（A1/A2/A3）均在临时副本内自建工件、自建自删，**绝不触碰真实仓库五锚**（`docs/GT_FORMALIZATION_v1.md`、`run_v21_gtformal.py`、`run_v22_p1c.py`、`docs/SPEC_GT2B.md`、`docs/SPEC_GT8C.md`）。

## 7. 接口预留位（V0 不实接）

V0 仅保留以下占位常量与错误码，不引入任何外部对接：

```python
# 占位常量，V0 不消费
P_B_INTERFACE_RESERVED = None  # 高层对接位
```

任何试图在 V0 范围外调用此占位的实现，判为越界，与 V0 表达力判定正交。

---

锚点 SHA-256[0:12] 见 §1。判死线以 §6 表达力线为唯一依据。R1-R5 各自独立可测。
