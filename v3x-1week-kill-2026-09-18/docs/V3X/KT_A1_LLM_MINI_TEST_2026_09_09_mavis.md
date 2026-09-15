# KT-A1 LLM Mini Test (2026-09-09)

> **作者**: Mavis(root session, V1 折中补阶段)
> **位置**: `docs/V3X/KT_A1_LLM_MINI_TEST_2026_09_09_mavis.md`

## 1. 一句话结果

- 1/5 correct (accuracy = 20.0%)
- 跑 5 cells (1 机制 × 1 任务族 × 5 决策)
- 完整 300 cells 待 V1 折中补 D3-D4

## 2. 关键数字

| 数字 | 值 |
|---|---|
| 机制 | M1_Deposon_TRA |
| 任务族 | T1_GSM8K |
| N | 5 |
| 正确数 | 1 |
| 准确率 | 0.2000 |

## 3. 详细结果

```json
[
  {
    "mechanism": "M1_Deposon_TRA",
    "task_family": "T1_GSM8K",
    "decision_idx": 0,
    "decision": "329",
    "correct": "325",
    "is_correct": false
  },
  {
    "mechanism": "M1_Deposon_TRA",
    "task_family": "T1_GSM8K",
    "decision_idx": 1,
    "decision": "578",
    "correct": "573",
    "is_correct": false
  },
  {
    "mechanism": "M1_Deposon_TRA",
    "task_family": "T1_GSM8K",
    "decision_idx": 2,
    "decision": "93",
    "correct": "94",
    "is_correct": false
  },
  {
    "mechanism": "M1_Deposon_TRA",
    "task_family": "T1_GSM8K",
    "decision_idx": 3,
    "decision": "634",
    "correct": "634",
    "is_correct": true
  },
  {
    "mechanism": "M1_Deposon_TRA",
    "task_family": "T1_GSM8K",
    "decision_idx": 4,
    "decision": "375",
    "correct": "366",
    "is_correct": false
  }
]
```

## 4. 已知边界

- mini test 仅 5 cells(快速验证 LLM client 接入), 完整 300 cells 沿用 V2 计划 D3-D4
- 7 条铁律: API key runtime 读, 不入 prompt
- Mavis(root session, deposon-successor 角色)
