# v21 运行记录 — run2（2026-08-29）

- 触发：LESSONS_v20_deepprobe.md 登记后复验
- 结果：FAILS=0/22；pytest 200 passed
- 备注：run1 FAILS=1 为环境漂移（python3.12 的 pytest 模块在会话间被重置，重装后复绿）；
  该现象本身是 LESSONS #27（环境/断言漂移）的又一实例，已记录。
- 新资产：docs/LESSONS_v20_deepprobe.md（12 条新教训 #19–#30，密钥前缀扫描 0 命中）

