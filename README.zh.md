# deposon-harness

面向 LLM **记忆与选择行为** 的预注册实验 harness：判据冻结、读数包自含、
双审证据链、门算术 **Lean + Python 双实现**。

- **判据预注册**：门定义/阈值/失败路径先写死再跑·轮内 0 事后校准·负控必须 fail-loud。
- **读数包自含**：每轮交付可第三方独立复算的包（MANIFEST 哈希锚＋冻结判据/工具拷贝＋逐 op 台账＋日志＋复算脚本）——不能从包内复算的数字不是读数。
- **门算术双实现**：Python 执行位＋Lean 4 机证位（core-only·0 sorry 债）·逐轮交叉核对。
- **读数＝模型×harness 联合读数**：报告行携带 locked-baseline 自检行（模型/种子/冻结面/工具哈希）。

## 状态：v0.x 预览版

**早期预览**：接口随时破坏性变更。核心链路 runner 模块候下版发布；复算路径已完整可用。本仓不做任何公开裁定声明——终审前只发布指针与规范。

## 快速开始（复算）

```bash
READINGS_PACKAGE_DIR=/path/to/readings-package python scripts/g6f_recalc.py
python tests/test_gates.py   # 门算术自检（纯数学·0 外部数据）
```

## 目录

`harness/` 发射器家族（env 参数化）｜`frozen/` 冻结面（盲化 K_h 映射·种子）｜
`gates/` 门规范双实现｜`mocks/` mock 认证（含 PC-lockin 负控）｜
`scripts/` 复算脚本族｜`docs/` 证据轮指针与规范｜`BENCHMARK.md` 门表与联合读数声明｜
`SAFETY.md` 安全三条款与止损语义。

读数数据永不入仓（artifacts 政策见 `.gitignore` 与 `CONTRIBUTING.md`）。

## 许可

MIT（Apache-2.0 备案在册）。
