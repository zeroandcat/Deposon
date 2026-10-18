# v24 运行记录 — run1（2026-08-30）

- 触发：博弈论重构收口（GT-5/5b/6 + 评审闭环 + related_work 同步）
- 结果：FAILS=0；pytest 218 passed
- 过程：字段名适配三 JSON 实际结构（verdict.verdict / per_graph_summary）；
  M1 断言精化（旧宣称仅存于修订记录元描述行，合法）
- 判定锚点：GT-5 inconclusive（未回溯）、GT-5b 22/22 单调、GT-6 中位残余 1.6e-29、
  例外 3 图披露、M1–M5 闭合、related_work 同步
