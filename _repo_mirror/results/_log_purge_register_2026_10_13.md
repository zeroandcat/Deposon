# 日志清理登记件（2026-10-13）

- 件号：`_log_purge_register_2026_10_13`
- 执行棒：日志清理执行棒（Worker）
- 落盘时间：2026-10-13
- 目标目录：`〔本机用户目录〕\AppData\Roaming\MiniMax\logs`
- 结论：**已删 0 件／失败 35 件**。可恢复通道拒删，未回退永久删除，故日志仓规模**未变**。

---

## 一、PI 裁（逐字）

> 逐件删（每类仅留最近 1 日）

来源：卡 `ask_bb48b73d2cbc4cd3f0010725` 之 `log_purge` 项。

## 二、删前规模（实测，非估算）

| 项 | 值 |
|---|---|
| 文件件数（非递归） | 43 |
| 总 bytes | 20,511,375,786 |
| 总 MB | 19,561.2 MB |
| 构成 | 7 个日卷类 × 6 日（10-08…10-13）＝ 42 件，加 `truncate-main-0929.ps1` 1 件 |

## 三、逐类保留口径

「每类仅留最近 1 日」→ **保留该类 mtime 最新之 `*-10-13.log` 今日卷**；同类 `10-08…10-12` 为待删历史卷。

| 日卷类 | 保留件 | 保留 bytes | 待删件数 | 待删 bytes |
|---|---|---|---|---|
| `main-*` | `main-10-13.log` | 282,541,976 | 5 | 20,078,956,398 |
| `chat-session-trace-*` | `chat-session-trace-10-13.log` | 3,365,771 | 5 | 102,611,185 |
| `api-*` | `api-10-13.log` | 1,414,389 | 5 | 36,280,152 |
| `remoteControl-*` | `remoteControl-2026-10-13.log` | 59,551 | 5 | 13,226,708 |
| `remoteControl-rc-case-*` | `remoteControl-rc-case-2026-10-13.log` | 139,537 | 5 | 4,762,173 |
| `remoteControl-sidebar-pinned-order-*` | `remoteControl-sidebar-pinned-order-2026-10-13.log` | 8,965 | 5 | 93,961 |
| `update-*` | `update-10-13.log` | 9,126 | 5 | 156,908 |
| 非日卷类 | `truncate-main-0929.ps1`（保留） | 433 | 0 | 0 |
| **合计** | 8 件保留 | **287,541,748** | **35** | **20,236,087,485** |

## 四、删除清单（35 件；bytes／mtime 逐件实测）

| # | 类 | 件名 | bytes | mtime |
|---|---|---|---|---|
| 1 | api | `api-10-08.log` | 2,533,588 | 2026-10-08 18:44 |
| 2 | api | `api-10-09.log` | 8,042,530 | 2026-10-09 23:59 |
| 3 | api | `api-10-10.log` | 9,244,293 | 2026-10-10 23:59 |
| 4 | api | `api-10-11.log` | 8,678,637 | 2026-10-11 23:59 |
| 5 | api | `api-10-12.log` | 7,781,104 | 2026-10-12 23:59 |
| 6 | chat-session-trace | `chat-session-trace-10-08.log` | 9,745,017 | 2026-10-08 18:46 |
| 7 | chat-session-trace | `chat-session-trace-10-09.log` | 27,333,957 | 2026-10-09 23:59 |
| 8 | chat-session-trace | `chat-session-trace-10-10.log` | 27,895,062 | 2026-10-10 23:59 |
| 9 | chat-session-trace | `chat-session-trace-10-11.log` | 18,379,759 | 2026-10-11 23:59 |
| 10 | chat-session-trace | `chat-session-trace-10-12.log` | 19,257,390 | 2026-10-12 23:59 |
| 11 | main | `main-10-08.log` | 1,048,325,179 | 2026-10-08 18:46 |
| 12 | main | `main-10-09.log` | 5,181,025,842 | 2026-10-09 23:59 |
| 13 | main | `main-10-10.log` | 7,410,242,463 | 2026-10-10 23:59 |
| 14 | main | `main-10-11.log` | 3,600,460,816 | 2026-10-11 23:59 |
| 15 | main | `main-10-12.log` | 2,838,902,098 | 2026-10-12 23:59 |
| 16 | remoteControl | `remoteControl-2026-10-08.log` | 492,278 | 2026-10-08 18:44 |
| 17 | remoteControl | `remoteControl-2026-10-09.log` | 3,295,738 | 2026-10-09 23:59 |
| 18 | remoteControl | `remoteControl-2026-10-10.log` | 8,027,137 | 2026-10-10 23:59 |
| 19 | remoteControl | `remoteControl-2026-10-11.log` | 242,668 | 2026-10-11 23:58 |
| 20 | remoteControl | `remoteControl-2026-10-12.log` | 1,168,887 | 2026-10-12 23:59 |
| 21 | remoteControl-rc-case | `remoteControl-rc-case-2026-10-08.log` | 482,830 | 2026-10-08 18:38 |
| 22 | remoteControl-rc-case | `remoteControl-rc-case-2026-10-09.log` | 1,334,259 | 2026-10-09 23:52 |
| 23 | remoteControl-rc-case | `remoteControl-rc-case-2026-10-10.log` | 1,403,847 | 2026-10-10 23:54 |
| 24 | remoteControl-rc-case | `remoteControl-rc-case-2026-10-11.log` | 820,540 | 2026-10-11 23:59 |
| 25 | remoteControl-rc-case | `remoteControl-rc-case-2026-10-12.log` | 720,697 | 2026-10-12 23:59 |
| 26 | remoteControl-sidebar-pinned-order | `remoteControl-sidebar-pinned-order-2026-10-08.log` | 5,167 | 2026-10-08 18:14 |
| 27 | remoteControl-sidebar-pinned-order | `remoteControl-sidebar-pinned-order-2026-10-09.log` | 24,863 | 2026-10-09 23:59 |
| 28 | remoteControl-sidebar-pinned-order | `remoteControl-sidebar-pinned-order-2026-10-10.log` | 36,303 | 2026-10-10 23:37 |
| 29 | remoteControl-sidebar-pinned-order | `remoteControl-sidebar-pinned-order-2026-10-11.log` | 19,522 | 2026-10-11 21:56 |
| 30 | remoteControl-sidebar-pinned-order | `remoteControl-sidebar-pinned-order-2026-10-12.log` | 8,106 | 2026-10-12 16:41 |
| 31 | update | `update-10-08.log` | 55,556 | 2026-10-08 17:52 |
| 32 | update | `update-10-09.log` | 19,848 | 2026-10-09 23:41 |
| 33 | update | `update-10-10.log` | 27,913 | 2026-10-10 23:26 |
| 34 | update | `update-10-11.log` | 27,443 | 2026-10-11 23:22 |
| 35 | update | `update-10-12.log` | 26,148 | 2026-10-12 23:09 |

## 五、执行方式（`rm --` 字面）

按硬约束以**一次顶层 `rm --`** 携带全部 35 个目标之**前斜杠字面绝对路径**（形如 `rm -- "〔本机用户目录〕/main-10-08.log" …`）。⛔ 未用裸 `Remove-Item`｜⛔ 未传 PowerShell 变量｜⛔ 未用 `-Force`。

命令实际落地为运行时受信任启动器 `mavis-trash`（可恢复回收站通道）。

## 六、执行结果：失败 35／已删 0

`mavis-trash` 对 **35 件全部拒删**，理由一致（逐字节选）：

```
mavis-trash: refused to trash redirecting reparse point
'〔本机用户目录〕/AppData/Roaming/MiniMax/logs/api-10-08.log'
(resolved '〔本机用户目录〕\AppData\Roaming\MiniMax\logs\api-10-08.log')
(reparse path '〔本机用户目录〕\AppData\Roaming\MiniMax')
(link target '〔本机用户目录〕\AppData\Roaming\MiniMax')
-> '〔本机用户目录〕\AppData\Roaming\MiniMax\logs\api-10-08.log';
run mavis-trash '〔本机用户目录〕\api-10-08.log' explicitly if you intend to
delete the redirect target
```

**根因（实测）**：`〔本机用户目录〕\AppData\Roaming\MiniMax` 系 reparse point（junction），属性实测 `Directory, ReparsePoint`，链接目标 `〔本机用户目录〕\AppData\Roaming\MiniMax`。故日志目录实际实体在 **D 盘**，`mavis-trash` 拒绝经由重定向点路径回收文件（防误删跨越 junction 的实体）。

**处置**：依派工令「若 `mavis-trash` 报错或部分失败 ⇒ 即刻停止」，已即刻停止。
⛔ **未回退永久删除**｜⛔ **未改用他法**｜⛔ **未按报错提示改走 D 盘目标路径**（该路径不在派工授权字面内，属改用他法，须先候裁）。

## 七、删后规模（实测）

| 项 | 删前 | 删后 |
|---|---|---|
| 件数 | 43 | **43（0 变化）** |
| 历史卷 10-08…10-12 仍在 | 35 | **35（0 件移出）** |
| 总 MB | 19,561.2 | **19,583.2** |

删后总 MB 略增，纯因**今日卷 `*-10-13.log` 为活动写入**（比对 `main-10-13.log` 由 270,336,545 → 282,541,976 字节）；与删除动作无关。

## 八、回收站可恢复性枚举结果

**无可枚举实体**。因 0 件进入回收站，D 盘回收站 `$R` 实体数 **0**，本棒无新增可恢复对象。此结果与「0 永久删」互为佐证：文件仍在原位，不依赖回收站亦可恢复。

> 注：派工预期「枚举 D: 回收站 `$R` 实体」以证可恢复；因拒删未发生转移，该枚举项**空集**，非遗漏。

## 九、0 永久删之自证

1. ⛔ 全程 **0 次** `Remove-Item`、`0 次` `rm` 不经启动器、⛔ `0 次` `cmd /c del`、`0 次` `.NET File.Delete`、⛔ `0 次` `Clear-Content`／截断。
2. `truncate-main-0929.ps1`（⚠ 截断＝永久）**未执行、未改动**：实测仍在，bytes ＝ **433**，与删前一致。
3. 全部 35 件待删卷**字节级未损**：逐件复核 bytes 与删前实测值**逐件相等**（例：`main-10-10.log` ＝ 7,410,242,463，两次实测一致）。
4. 任何 `*-10-13.log` **未纳入命令**，零风险。
5. 未写入归档区 `〔本地归档区〕`（0 读 0 写 0 列目录）。
6. 本棒 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT。

## 十、未决项（候裁）

1. **处置路径待裁**：是否授权改以**真实实体路径** `〔本机用户目录〕\AppData\Roaming\MiniMax\logs\...`（前斜杠字面，一次顶层 `rm --`，同 35 件）重试。此为派工明令禁止之「改用他法」，故本棒**未擅自执行**。
2. **需 PI 明确一句**：`log_purge` 授权是否覆盖 D 盘重定向目标路径。字面授权为 `〔本机路径〕\...\MiniMax\logs\…`，实删须为 `〔本机用户目录〕\MiniMax\logs\…`。
3. **爆仓未解**：日志仓仍 19,583.2 MB，主因 `main-10-10.log` 单卷 7,410,242,463 bytes（≈6.9 GB）仍在。仓容压力持续。
4. **递归校验缺口**：派工令限定「非递归」列目录，本棒遵办；若该日志目录存在子目录，未纳入本次盘点（未列）。