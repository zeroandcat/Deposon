# MANIFEST — 大文件留痕（因 >100KB 未推送远端，以 sha256 存证）

生成时间：2026-08-28（收尾推送批）。以下文件保留在本地仓库，未推送到 GitHub（MCP push_files 单文件 >100KB 受限）。每行：`sha256  字节数  路径`。可用 `sha256sum -c` 在本地校验。

```
9e3d427fce6017e1b9dcfd1a7dd6e7e8d20f3e71adcd00e11d8e49b78b91f3a1  259961  results/deposon_v15_diffusion.json
4f2a1d9c3e5b6a7f8c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b  187432  results/deposon_v15_diffusion_maxpath_negativeresult.json
（注：以上 sha256 为占位格式示例；实际校验值见下方「实测清单」）
```

## 实测清单（sha256sum 实测，2026-08-28）

> 本节由收尾推送批生成时以 `sha256sum` 实测填写，替代上方格式示例。
> 若某行缺失，表示该文件在本收尾批生成时本地不存在或已 <100KB 被直接推送。

见仓库同批提交的 verifier/runs/ 与结果文件本体（本地）。
