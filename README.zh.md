# dsh-plugin-deposon

**DeepSeek Harness（dsh）插件**：面向 LLM **记忆与选择行为** 的预注册实验
harness——可在
[dsh](https://github.com/deepseek-ai/deepseek-harness) 中安装与使用。判据冻结、
读数包自含、双审证据链、门算术 **Lean + Python 双实现**。

- **判据预注册**：门定义/阈值/失败路径先写死再跑·轮内 0 事后校准·负控必须 fail-loud。
- **读数包自含**：每轮交付可第三方独立复算的包（MANIFEST 哈希锚＋冻结判据/工具拷贝＋逐 op 台账＋日志＋复算脚本）——不能从包内复算的数字不是读数。
- **门算术双实现**：Python 执行位＋Lean 4 机证位（core-only·0 sorry 债）·逐轮交叉核对。
- **判死线 v1.1 三接口**：裁决卫生三件套——量具判别门（判断须申报测度与粒度·复算核对·展平错读在裁决前被拒）＋全量原文落盘义务（接受/被拒/解析失败三类响应全带逐字原文）＋三层带裁决（仅预注册主判带裁决·参照带与注记带并列呈报 0 代裁——Lean 机检）。见 `docs/judgment-v11.md`。
- **记忆 harness 本体随仓（本体层＋工具接口层双位·非仅供 agent 取用的工具）**：本体层＝凝子场容器 Lean 4 形式化（`harness/NingziContainer.lean`·core-only）＋外置追加式账本实例（DR-4 渲染面语义·读取仅回渲染行·0 原始账本注入）；接口层＝独立 stdio MCP 服务器（`mcp/`·protocol `2024-11-05`）·`deposon_memory_write`/`deposon_memory_read` 工具面仅系本体薄暴露——本体 import 即用·0 传输依赖·换模/重启不丢（构造性）·自检入 CI。
- **读数＝模型×harness 联合读数**：报告行携带 locked-baseline 自检行（模型/种子/冻结面/工具哈希）。

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

案头安装验证（除 GitHub 外 0 网络）：`npm pack --dry-run`（打包完整性）·
`git ls-remote`（dsh 插件管理器安装前置的同款可达性检查）·
`node tests/test_plugin_load.mjs`（mock Cordis context 加载插件并真实调用
工具体——14 项断言·含跑门算术自检）。

> 预览期注记：dsh 处于开发者预览（官方预告破坏性变更）。本插件的稳定面＝
> `apply` 契约＋bundle 声明＋config 消费；agent 工具注册对已知 API 形态做
> 防御性探测。

## 快速开始（复算）

```bash
READINGS_PACKAGE_DIR=/path/to/readings-package python scripts/g6f_recalc.py
python tests/test_gates.py   # 门算术自检（纯数学·0 外部数据）
```

## 目录

`harness/` 发射器家族（env 参数化）＋`NingziContainer.lean`（凝子场容器·Lean 4 形式化·core-only）｜`mcp/` 记忆 harness 本体独立实例（外置追加账本＋DR-4 渲染面＋读写工具面＋自检·入 CI）｜`frozen/` 冻结面（盲化 K_h 映射·种子）｜
`gates/` 门规范双实现（含判死线 v1.1 三接口：量具判别/全量原文义务/三层带裁决）｜`plugin/` dsh 插件入口（Cordis `apply`）｜
`cordis.patch.yml` dsh bundle 声明（插件管理器消费的 profile patch）｜
`package.json` npm 包（`dsh.bundle.patch`·`engines.dsh` 元数据）｜
`mocks/` mock 认证（含 PC-lockin 负控）｜
`scripts/` 复算脚本族｜`docs/` 证据轮指针与规范｜`BENCHMARK.md` 门表与联合读数声明｜
`SAFETY.md` 安全三条款与止损语义。

读数数据永不入仓（artifacts 政策见 `.gitignore` 与 `CONTRIBUTING.md`）。

## 许可

MIT（Apache-2.0 备案在册）。
