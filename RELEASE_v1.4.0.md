# Release v1.4.0 发布说明

## Deposon v1.4.0 — 真实 LLM 后端 + 真实基准验证

### 本版本核心
1. **真实 LLM 后端落地**：`KimiLLMBackend`（kimi-for-coding API），严格 JSON 概念分解 + 指数退避重试 + 规则引擎自动降级；跨 prompt 版本持久化磁盘缓存，复跑零成本。
2. **效应量根因修复**：v1.2 四组 benchmark effect_size 恒为 0.0 的两大根因——(a) 答案计算与 Deposon 散射脱钩；(b) 陷阱节点 BFS 不可达——已在 v1.3 修复。
3. **三阶段实证**：
   - 合成简单集 100 题：baseline 7% → unified 100%（effect +0.93）
   - 合成陷阱集 100 题（六类陷阱）：baseline 10% → unified 100%（effect +0.90）
   - 真实 GSM8K 100 题（seed=42）：CoT 97.0% / unified 85.0%（McNemar p=4.9e-4，CoT 显著更优，如实报告）/ no_deposon 2.0%（p=4.4e-24，场过滤极显著）；敏感性口径（事后分析，修复 fold_chain 缺陷后）unified 94.0%（p=0.25）
4. **validate 主环路**：GSM8K 100 题全量真实 LLM 验证（与金标一致性 97%）；验证层对节点路径式推理链偏严格的误报问题已如实记录（v1.5 改"独立复算比对"范式）。

### 诚实边界
- GSM8K 真实子集上约束层呈现与合成陷阱集相反的权衡（信息损失代价主导）：主口径 unified 85.0% < CoT 97.0%；失败归因三分类（fold_chain 折叠器缺陷 10 / 分解器真错误 3 / 机制内陷阱损失 2）。防捕获增益与信息损失代价共同构成可审计约束层的完整画像。
- validate 层当前是保守风险标记器，非绝对判官。
- 无限维以太的"不可逆性"是工程强制 + 渐进论证的结合，非有限截断下的数学定理。

### 文件导览
- `deposon_agents_v1_3.py` / `deposon_agents_v1_4.py`：系统实现
- `run_benchmark_v1_3.py` / `run_benchmark_v1_4_gsm8k.py`：评测复现入口
- `results/`：全部 benchmark JSON（合成 + GSM8K）
- `docs/`：需求、技术报告、v1.3/v1.4 验证报告
- `paper/`：论文初稿（deposon_paper_v1.md + references.bib + fig1）

### 复现
```bash
pip install -r requirements.txt
export KIMI_API_KEY=你的key   # 仅环境变量, 勿写入代码
python3 run_benchmark_v1_3.py          # 合成集(缓存命中则零 API)
python3 run_benchmark_v1_4_gsm8k.py    # GSM8K 100 题
```

### v1.4.0 新增（相对 v1.4.0-draft）
- **GSM8K 终版回填**：双版论文（CN/EN）摘要与 §4.2 占位符全部替换为终版数据 + Table 10 + 失败归因三分类 + 事后敏感性分析。
- **G1-G3 算法扩展**：真实脑图摄入管线（附录 D，svg_mindmap_ingest.py + 人工转译诚实声明）；Born 规则路径积分集成对照（§4.5 Table 9，Born 100% vs 多数投票 19%/17%）；Arrhenius 势垒通道消融（§5.2 诚实负面结果：长度偏置与势垒-语义错配）。
- **三轮拒稿风险评审闭环**：R3 判决 PASS（6 大 17 小问题全部关闭）。
- **抗死循环修复**：5 道英文题 reasoning 死循环 → steps-fallback 路径 + 空 content 不重试的 token 保护。
- 论文终版产物：deposon_paper_v1.md / _en.md（R3-PASS），docx 与 PDF 转换产物见发布附件。
