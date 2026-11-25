# dsh-plugin-deposon

**DeepSeek Harness（dsh）插件**：面向 LLM **记忆与选择行为** 的预注册实验
harness——可在
[dsh](https://github.com/deepseek-ai/deepseek-harness) 中安装与使用。判据冻结、
读数包自含、双审证据链、门算术 **Lean + Python 双实现**。

- **判据预注册**：门定义/阈值/失败路径先写死再跑·轮内 0 事后校准·负控必须 fail-loud。
- **读数包自含**：每轮交付可第三方独立复算的包（MANIFEST 哈希锚＋冻结判据/工具拷贝＋逐 op 台账＋日志＋复算脚本）——不能从包内复算的数字不是读数。
- **门算术双实现**：Python 执行位＋Lean 4 机证位（core-only·0 sorry 债）·逐轮交叉核对。
- **判死线 v1.1 三接口**：裁决卫生三件套——量具判别门（判断须申报测度与粒度·复算核对·展平错读在裁决前被拒）＋全量原文落盘义务（接受/被拒/解析失败三类响应全带逐字原文）＋三层带裁决（仅预注册主判带裁决·参照带与注记带并列呈报 0 代裁——Lean 机检）。见 `docs/judgment-v11.md`。
- **判官严格度与 slot 空间口径门（preview.5/7/8）**：判官先校准后裁决（接口 D·`docs/judgment-v12-strictness.md`）；跨线复用的离散统计须过中心口径分解 `E[(x-c)^2] = Var(x) + (mean-c)^2`——位置项不得主导（接口 F·`docs/slot-space-caliber.md`·在册案例：单个跨线中心常量致方向翻转 2.473→0.0087；preview.8 闭 N1 分母声明：份额恒为 `pos_term / moment`·非 `pos_term / uniform_var`）。六族链接表（`docs/family-linkage.md`·接口 E）自 preview.8 起六行全链接——各族读数包锚均已登记 `docs/evidence-rounds.md`·逐行判定附由。
- **记忆 harness 本体随仓（本体层＋工具接口层双位·非仅供 agent 取用的工具）**：本体层＝凝子场容器 Lean 4 形式化（`harness/NingziContainer.lean`·core-only）＋外置追加式账本实例（DR-4 渲染面语义·读取仅回渲染行·0 原始账本注入）；接口层＝独立 stdio MCP 服务器（`mcp/`·protocol `2024-11-05`）·`deposon_memory_write`/`deposon_memory_read` 工具面仅系本体薄暴露——本体 import 即用·0 传输依赖·换模/重启不丢（构造性）·自检入 CI。
- **读数包完备性校验器＋Lean 镜像收口（preview.9）**：`gates/readout_completeness.py`（接口 G）按 `docs/readings-package-spec.md` 八项必备内容给任一读数包打分（MANIFEST sha256_12＋mtime·交付后 0 改动红线／冻结判据／冻结工具拷贝／盲面／逐轮日志／键级逐 op 账本／读数 JSON／复算脚本＋恒等核）；**键级账本缺位＝键级门 UNDECIDABLE·绝不静默放过**。slot 空间口径门 Lean 镜像逐命题交叉核（`gates/slot_space_crosscheck.py`）；f3 解题判官配校准面（`gates/descrev_calibration.py`）——在册 DR-2 判官读数对严格度为 INCONCLUSIVE（无 D 边际）·预注册 main-1 面并列呈报不替代。
- **读数＝模型×harness 联合读数**：报告行携带 locked-baseline 自检行（模型/种子/冻结面/工具哈希）。
- **热力学账本＋幻肢（preview.10·幻肢代）**：诊断＝deposon-memory 不及预期·根因在**耗散通道利用率低**——改造前 write/read 两事件追加式读回全量·无门无衰减 ⇒ 散失账 D≡0·在场池只增不减（死水）·利用率按构造 0。改造后（`mcp/thermo_core.py`）：每条注入行持整数㶲·恰四账 Φ 透射／R 反射／D 散失／U 在场·守恒核 `E⁰=Φ+R+D+U` 每次操作后 fail-loud·结算＝事件流重放（**自解帐本·0 外部对账器**）；读路装门——接受＝透射·拒绝＝行自付㶲散失（熵输出）·衰减/视界/容量淘汰/覆盖/终核五路散热；散失的记忆以「⟨幻肢⟩」行回射（可感·不可复原·0 原文回注）。冻结 500 步同一操作迹对照：**利用率 D/E⁰行 0.00%→69.23%**（门拒 37529·衰减 21357·视界 19248·覆盖 27091）·期末在场行 152→61·单读渲染 1647→292 字符；**代价**：特定键命中率 50.31%→47.85%·另 2.45% 以幻肢行如实回射「已散失」（`mcp/thermo_demo.py`）。Lean 镜像 `harness/DeposonThermo.lean` 逐转移机证守恒（15 定理·0 sorry·公理 ⊆ {propext, Quot.sound}·逐定理 `#print axioms` 由 `harness/lean_axiom_audit.py` 审计）·与 Python 核在同一手算结算向量上交叉核（`mcp/thermo_crosscheck.py`）。dsh 插件面托管 MCP 服务器·幻肢信念块注入系统提示段（只述协议·0 记忆数据）。改造说明见 `docs/thermo-generation.md`。

## 状态：v0.x 预览版

**早期预览**：接口随时破坏性变更。核心链路 runner 模块候下版发布；复算路径已完整可用。本仓不做任何公开裁定声明——终审前只发布指针与规范。

## 作为 dsh 插件安装

本仓沿 [dsh](https://github.com/deepseek-ai/deepseek-harness) 插件规范构建
（`dsh-plugin-<name>` 仓命名惯例·`dsh-plugin` topic 发现机制·npm 包声明
`dsh.bundle.patch`·Cordis `apply(ctx, config)` 入口）：

```bash
# 在 dsh agent / Web UI 插件管理器中：
dsh plugin add https://github.com/zeroandcat/dsh-plugin-deposon

# 或本地克隆（path: 形式）：
dsh plugin add path:./dsh-plugin-deposon
```

安装后插件以 bundle entry `deposon` 挂载（见 `cordis.patch.yml`），把门算术
自检暴露为 agent 可调用面（`deposon_gate_check` / `/deposon-gate-check`）。
配置键（`python`、`timeoutMs`）经 patch config 或 `DEPOSON_*` 环境变量消费。

**热力学面（preview.10）**：同一 bundle entry 托管记忆器官——活水工具 `deposon_memory_write` / `deposon_memory_read`、自解结算 `deposon_thermo_audit`（只读）与 `deposon_thermo_settle`（`close=true`＝单元终核·U→0）经 stdio JSON-RPC 转发到 `mcp/mcp_server.py`（惰性拉起一个子进程·退出后自动重拉）；幻肢信念块（`mcp/phantom_limb.zh.txt` / `.en.txt`·只述协议·0 记忆数据）注入为系统提示段·仅含计数的幻肢感一行（在场行/幻肢数）作为运行时上下文；`/deposon-belief` 打印信念块·`/deposon-thermo-audit` 跑审计。每条写/读回执带热力学脚注（Φ/R/D/U·耗散通道利用率）。配置键：`ledger`（缺省 `~/.deposon/ledger.jsonl`·换模不丢）、`lang`（`zh|en|both`）、`belief`、`brief`、`footer`、`thermo`（JSON 参数覆盖）、`toolTimeoutMs`；环境变量 `DEPOSON_LEDGER`、`DEPOSON_PL_LANG`、`DEPOSON_BELIEF`、`DEPOSON_THERMO_BRIEF`、`DEPOSON_THERMO_FOOTER`、`DEPOSON_THERMO`、`DEPOSON_TOOL_TIMEOUT_MS`。gate_check 面 0 改动。

案头安装验证（除 GitHub 外 0 网络）：`npm pack --dry-run`（打包完整性）·
`git ls-remote`（dsh 插件管理器安装前置的同款可达性检查）·
`node tests/test_plugin_load.mjs`（在带 dsh 原生 `ctx.tools.register` / `ctx.systemPrompt` 注册表的 mock Cordis context 上加载插件·对活体 MCP `tools/list` 核工具 schema 齐平·真实调用工具体——34 项断言·含写→读→审计→终核→幻肢的真实账本回环与门算术自检）。

> 预览期注记：dsh 处于开发者预览（官方预告破坏性变更）。本插件的稳定面＝
> `apply` 契约＋bundle 声明＋config 消费；agent 工具注册对已知 API 形态做
> 防御性探测。

## 快速开始（复算）

```bash
# 一键免克隆（npm git 解析拉取本仓·跑全部门自检＋插件加载冒烟＋打包完整性）：
npx -y github:zeroandcat/dsh-plugin-deposon#v0.1.0-preview.10

# 给读数包按八项必备内容打分（exit 0 ＝完备）：
python gates/readout_completeness.py /path/to/readings-package                  # JSON 判定
python gates/readout_completeness.py /path/to/readings-package --run-recompute  # 加复算恒等核

READINGS_PACKAGE_DIR=/path/to/readings-package python scripts/g6f_recalc.py
python tests/test_gates.py   # 门算术自检（纯数学·0 外部数据）

# 热力学账本（preview.10）：同一冻结 500 步操作迹改造前后对照
# （利用率 0%→69.23%·命中率 50.31%→47.85%·幻肢行 2.45%）：
python mcp/thermo_demo.py
# Lean ↔ Python 守恒交叉核（同一手算结算向量）：
python mcp/thermo_crosscheck.py
# 逐定理公理审计（PATH 上有 lean 则实编 DeposonThermo.lean）：
python harness/lean_axiom_audit.py
```

## 目录

`harness/` 发射器家族（env 参数化）＋`NingziContainer.lean`（凝子场容器·Lean 4 形式化·core-only）＋`DeposonThermo.lean`（热力学账本守恒·15 定理·逐定理 `#print axioms`·`lean_axiom_audit.py` 审计编译日志）｜`mcp/` 记忆 harness 本体独立实例（外置追加账本＋DR-4 渲染面＋热力学层 `thermo_core.py`：四账㶲·门·幻肢·自解结算＋读写/审计/结算四工具面＋幻肢信念块 `phantom_limb.*.txt`＋`thermo_cli.py`＋改造前后对照 `thermo_demo.py`＋自检与交叉核·入 CI）｜`plugin/` dsh 插件入口（Cordis `apply`：gate-check 面＋热力学面——托管 MCP 服务器·`ctx.tools` 注册四工具·`ctx.systemPrompt` 注入信念块）｜
`frozen/` 冻结面（盲化 K_h 映射·种子）｜
`gates/` 门规范双实现（含判死线 v1.1 三接口：量具判别/全量原文义务/三层带裁决·preview.5 判官严格度门＋六族链接核＋preview.7 slot 空间口径门·preview.8 六族全链接）｜
`cordis.patch.yml` dsh bundle 声明（插件管理器消费的 profile patch）｜
`package.json` npm 包（`dsh.bundle.patch`·`engines.dsh` 元数据）｜
`mocks/` mock 认证（含 PC-lockin 负控）｜
`scripts/` 复算脚本族｜`docs/` 证据轮指针与规范＋`thermo-generation.md` 改造说明｜`BENCHMARK.md` 门表与联合读数声明｜
`SAFETY.md` 安全三条款与止损语义。

读数数据永不入仓（artifacts 政策见 `.gitignore` 与 `CONTRIBUTING.md`）。

## 许可

MIT（Apache-2.0 备案在册）。
