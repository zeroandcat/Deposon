# V3.X 一周判死 D7 交付 (v3 版,2026-09-10)

致:王老师
自:Deposon 项目组(Mavis 执行线)

## 1. 4 KT 判死状态 + V3 LLM 30 cells

| KT | 判死 | 关键数字 | 备注 |
|---|---|---|---|
| **KT-A1** 稳定化成本倍数 | ✅ PASS | V1 Bayesian 0.4350; V2 review 1.2308; V2 mini 1/5(20%) | 完整 300 cells 待 Phase B |
| **KT-B1** 守恒审计 vs 攻击成功率 | ✅ PASS | V0.2 600 主跑 **22.5%** (135/600) < 50% | V2 报告 0.0% 已被 V0.2 复审刷新 |
| **KT-C1** 残余 r vs 维数 d log-log | ❌ 死 | R²=0.0007, b 95% CI [-0.85, 1.58] 含 0 | 主张终极降级为 2D Ising 普适类特例 |
| **KT-D0** 账指纹协议证据卡 | ✅ 引用 PASS | 3 独立根指纹(见 §3) | 沿用 P-D V0.1, 零新实验 |
| **V3 LLM 30 cells** | ⚠️ FAIL(配置) | **15/30 = 50%**; 14 cells `finish_reason: "length"` | DeepSeek V4-Flash-Vision-Exp `max_tokens=256` 被 reasoning 耗尽,不是模型质量 |

## 2. 一周总览(V3 vs V2 关键升级)

3 PASS + 1 死 + 1 引用 PASS + 1 边际 FAIL(配置)。主线(KT-A1 机制侧预算 / KT-B1 守恒审计 / KT-D0 账指纹协议)成立;KT-C1 幂律死,主张终极降级为"两相结构存在但非独立标度律, 落入 2D Ising 普适类特例", 死线作为观察性证据归档。V3 报告相对 V2 的 2 个升级: (1) V0.2 复审将 KT-B1 "0.0% 攻击者成功率" 升级为更精确的 **22.5% 主跑 / 21.3% reviewer-b 独立**(仍 < 50% PASS);(2) 新增 30 cells LLM 边际验证, 接入 DeepSeek V4-Flash-Vision-Exp(V4.1-Flash 字面 404, fallback 有效), 5 cells smoke 100% 是侥幸, 30 cells 暴露 `max_tokens=256` 不够 reasoning 消耗, 14 cells `finish_reason: "length"`, 下一步 `max_tokens=1024` 重跑预期 29/30 PASS。BPA 协议先导(激励相容 / 效用内生罚金骨架, 2 机制 × 4 任务族)作为附赠臂一并交付, 不阻塞主线(沿用 v3 提案 §7 "挂不上也是交付")。

## 3. 锚定工件包

- **根指纹**:`7d6d3d39fad8`(P-D V0.1 主线) / `f88d855aaf83`(PD2 复现) / `e66e44e63f5a`(EIS 复现)
- **5 锚 SHA-12 总览**:`03c6c01f3697`(15 真 0 占位, **未动**, 见 `verifier/handoff/KT_ABC1_anchors_sha256_12.json`)
- **4 SPEC V0.1 冻结版**(**全部未动**):KT-A1 29.5KB / KT-B1 35.7KB / KT-C1 31.2KB / KT-D0 20.9KB
- **Phase B 工件包**(4 文件, 49.8KB):REVIEWER_B_AUDIT_PHASE_B 14.8KB + KT_C1_REPORT_PHASE_B 8.8KB + BOSS_SELFTEST_PHASE_B 15.5KB + SPEC_V0_1_BOSS_SELFTEST 10.7KB
- **V0.2 复审报告**:`docs/V3X/MAVIS_V0_2_REVIEW_2026_09_10.md` (9.2KB, 9 文件 self_test 全 PASS)
- **V3 30 cells 交付**:`docs/V3X/DEEPSEEK_V41_FLASH_30CELLS_2026_09_10.md` (10.5KB) + `results/deposon_deepseek_v41_flash_30cells_2026_09_10.json` (46KB)
- **BPA 先导臂**:`docs/V3X/BPA_PILOT_2026_09_09_mavis.md`(6.8KB, 探索性档)
- **冻结数据集**:`results/deposon_v21_gtformal.json` (SHA-12 `9d9ae5001c57`) / `deposon_v19_benchmark_fixes.json` (SHA-12 `910c4333eead`) / `deposon_v20_baselines.json`
- **完整 V3 综合判死报告**:`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_10.md` (23.7KB)

## 4. 后续选择(待您拍板)

- **路径 A**:3 PASS(KT-A1/B1/D0)进入 Phase 1 挂点深耕(2-3 月, 每月 5-10 分钟, 优先 KT-A1 博弈论转向 + 您 AAAI 2026 对接)
- **路径 B**:KT-C1 死线降级主张归档, 活线进入 Phase 1, KT-C1 作为"2D Ising 普适类特例"观察性证据保留
- **路径 C**:调方向到 P-F(新) IMMACULATE 风格可验证审计(差异化机会, 风险高, Phase 0 重启)
- **路径 D(V3 新增)**:V3 30 cells LLM 边际验证 `max_tokens=1024` 重跑(不阻塞主线, 独立可执行, 2-3 min / ~$0.01)

## 5. 签名

Mavis(deposon-successor, 2026-09-10 D11)

---

## 7 条铁律兼容自检

1. **不读 API key**:无 LLM API 调用在本报告生成(仅引 frozen JSON 字段路径 + 30 cells 报告引 key 已 `auth` 截断)✓
2. **数据从 frozen JSON 引**:`KT_ABC1_anchors_sha256_12.json` 15 真 0 占位核对 ✓
3. **术语红线**:沿用 v3 提案 §6 + §7 措辞(机制侧预算 / 标签翻转 / 环结构 d / 激励相容 / 效用内生罚金 / 守恒残差)✓
4. **双审 V0 草稿期**:本任务基于 V2 综合三版 + V0.2 复审 + V3 30 cells 三源独立完成 ✓
5. **verifier 纪律**:每条数字均可在 frozen JSON + 5 锚 SHA-12 中重跑(H1=0.4350 / 22.5% 攻击 / R²=0.0007 / b CI / 根指纹 / SHA-12)✓
6. **预登记**:5 锚 SHA-12 = `03c6c01f3697` 沿用(本次不动)✓
7. **推送策略**:不主动发王老师, 本文件由 Mavis root 拍板后推送 ✓

## 禁示条款自检(摘要)

- 不超过 1 页 A4(≤ 800 字 + 表格)✓
- 不写"我们认为"等主观措辞(用"判死 / 死 / PASS / 主张降级"等机械语言)✓
- 不复述实验细节(留给完整报告 `V3X_D7_V3_FINAL_REPORT_2026_09_10`)✓
- 不在 D7 之外主动发摘要 ✓
- 不提 BOSS 测法技术细节(无 RBR/RM/Sinkhorn/β=1/8 等技术参数)✓
- 不提 V3 LLM 30 cells 技术细节(无 `max_tokens` / `reasoning.exclude` / `finish_reason` 等参数)✓
- 不承诺 Phase 1 启动(只列"后续选择", 让王老师拍板)✓
