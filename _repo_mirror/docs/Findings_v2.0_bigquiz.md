# Findings v2.0-BigQuiz — 大型题库验证（157 题 × 6 域）与空间释放留痕

> 2026-08-28。数据：results/quizbank_v20_big.json、deposon_v20_bigquiz_eval.json、
> docs/space_release_log.json。API：16 prompt / ~20 次 HTTP 尝试（2 新域全管线 6 +
> 攻击者扩池 6 + PM 先验 16k 重试 2 + 既有缓存复用）。

## 一、大题库横向对比（157 题 = 6 域全部 named 边，bloom L4 × 扩池陷阱）

| 臂 | 总准确率 | 解读 |
|---|---|---|
| **CoT（40 题子集）** | **92.5%** | 与小题库完全一致（文本级映射复核通过） |
| **llm_prior** | **89.5%** | 6 域全部第一（bio 100%、historical 95.7%、geography 93.8%、algo 86.2%、phys 80.6%、PM 80.6%） |
| ngram_tfidf（BOSS 常驻臂） | **54.2%** | **在大题库上击败 field_mean**（51% vs 54%），BOSS 地位规模化确认 |
| field_mean | 50.9% | 2× 机会，结构信号部分迁移；geography 最佳（68.8%——地理图枢纽性较强） |
| random（机会） | 25.3% | |
| rule_filter | **19.6%（低于机会）** | 扩池陷阱 100% 无关键词 ⇒ 规则退化到首选项偏置，自适应攻击下确定性失效 |

规模化结论：小题库（40 题）的数字在 4× 规模与 6 域下全部复现方向——
先验碾压、场与 tfidf 缠斗、规则防线归零。新域 geography_world（抽象→具体）
与 project_management（过程→结果）延续了对立统一格局：先验全域称王，
场在地理层级图上相对最强（该图 hub_concentration 较高，领域鉴定器 v0 同向）。

## 二、API 工程事故记录（大模型推理溢出陷阱）

project_management 先验请求连续 5 次 120s 超时：诊断发现 **finish_reason=length、
completion_tokens=8000 中 reasoning_tokens=7999**——推理模型把全部 token 预算
烧在思考上，可见输出为零。处置：max_tokens 提至 16000 + 空 content 视为可重试
错误，一次成功（reasoning 12431 + 正文 1430 字符）。教训已写入获取驱动：
**对 reasoning 模型，max_tokens 须同时容纳思考与答案；空 content ≠ 失败响应，
是预算配置错误。**

## 三、空间释放（1.X 优秀经验：先留痕后释放）

docs/space_release_log.json 记录全部释放文件的 sha256 与再生路径：
- 释放 703KB：paper/*.gz.b64（+13 分块，早前会话传输残留，原文在库）与
  *.base.docx（md2docx 中间件，footnote 流程可再生）。
- 保留：deposon_cache（LLM 缓存基石）、results/ 全部 JSON、corpus/ 全部图、
  paper/ 全部 md 与历史备份、deposon-repo.zip 交付快照。
- 原则（1.X 经验）：内容寻址（sha256 + 再生命令）+ 只释放可再生/传输残留，
  实验数据与缓存一律不动；verifier 记录本轮释放。

## 四、对 v2.1 的输入

1. 题库轨定型：bloom L4 × attacker_xl 扩池为标准件；新域上线成本 = 6 prompt。
2. ngram_tfidf 在注册表中升级为「确认 BOSS」（规模化击败场于语义图），
   领域鉴定器 v0 的 real_semantics 分支建议默认指向语义臂（prior/tfidf）。
3. reasoning 模型调用规范：max_tokens ≥ 16000 或按域预检（PM 案例入库 LESSONS）。
4. CoT 新域补齐（geography/PM）列入下轮预算（2 prompt）。
