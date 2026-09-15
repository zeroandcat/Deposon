# V3.X 一周判死 D7 交付 — 2026-09-09

致:王老师
自:Deposon 项目组(Mavis 执行线)

## 1. 4 KT 判死状态

| KT | 判死 | 关键数字 | 备注 |
|---|---|---|---|
| **KT-A1** 稳定化 g_a* vs λ_gap 单调 | ✅ 生 | H1=0.4350;V2 完整 1.23 双触发 | 机制侧预算闭合(标签翻转未触发) |
| **KT-B1** 守恒审计 vs 攻击成功率 | ✅ 生 | 600 攻击 0.0% 攻击者 | 100% 检出(守恒残差 ≤ 2.2e-16) |
| **KT-C1** 残余 r vs 维数 d log-log | ❌ 死 | R²=0.0007, b 95% CI [-0.85, 1.58] 含 0 | 主张终极降级为 2D Ising 普适类特例 |
| **KT-D0** 账指纹协议证据卡 | ✅ 引用 PASS | 3 独立根指纹(见 §3) | 沿用 P-D V0.1, 零新实验 |

## 2. 一周总览

3 PASS + 1 死 + 1 引用 PASS。主线(KT-A1 机制侧预算 / KT-B1 守恒审计 / KT-D0 账指纹协议)成立;KT-C1 幂律死, 主张终极降级为"两相结构存在但非独立标度律, 落入 2D Ising 普适类特例", 死线作为观察性证据归档。BPA 协议先导(激励相容 / 效用内生罚金骨架, 2 机制 × 4 任务族)作为 D5 附赠臂一并交付, 不阻塞主线(沿用 v3 提案 §7 "挂不上也是交付")。D3 末已发微信中期简报(5 行固定格式), 您未回复即按默认推进, 本摘要为 D7 终期交付。

## 3. 锚定工件包

- **根指纹**:`7d6d3d39fad8`(P-D V0.1 主线) / `f88d855aaf83`(PD2 复现) / `e66e44e63f5a`(EIS 复现)
- **5 锚 SHA-12 总览**:`03c6c01f3697`(15 真 0 占位, 见 `verifier/handoff/KT_ABC1_anchors_sha256_12.json`)
- **4 SPEC V0.1 冻结版**:KT-A1 29.5KB / KT-B1 35.7KB / KT-C1 31.2KB / KT-D0 20.9KB
- **Phase B 工件包**(4 文件, 49.8KB):REVIEWER_B_AUDIT_PHASE_B 14.8KB + KT_C1_REPORT_PHASE_B 8.8KB + BOSS_SELFTEST_PHASE_B 15.5KB + SPEC_V0_1_BOSS_SELFTEST 10.7KB
- **BPA 先导臂**:`docs/V3X/BPA_PILOT_2026_09_09_mavis.md`(2 机制 × 4 任务族骨架, 6.8KB, 探索性档)
- **冻结数据集**:`results/deposon_v21_gtformal.json` / `results/deposon_v19_benchmark_fixes.json` / `results/deposon_v20_baselines.json`
- **完整中文判死报告**(备查):`docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md`(V2 综合三版, 24.7KB)

## 4. 后续选择(待您拍板)

- **路径 A**:3 PASS(KT-A1/B1/D0)进入 Phase 1 挂点深耕(2-3 月, 每月 5-10 分钟, 优先 KT-A1 博弈论转向 + 您 AAAI 2026 对接)
- **路径 B**:KT-C1 死线降级主张归档, 活线进入 Phase 1, KT-C1 作为"2D Ising 普适类特例"观察性证据保留
- **路径 C**:调方向到 P-F(新) IMMACULATE 风格可验证审计(差异化机会, 风险高, Phase 0 重启)

## 5. 签名

Mavis(deposon-successor, 2026-09-09)

---

## 7 条铁律兼容自检

1. **不读 API key**:无 LLM API 调用, 仅引 frozen JSON 字段路径 ✓
2. **数据从 frozen JSON 引**:`KT_ABC1_anchors_sha256_12.json` 15 真 0 占位核对 ✓
3. **术语红线**:沿用 v3 提案 §6 + §7 措辞(机制侧预算 / 标签翻转 / 环结构 d / 激励相容 / 效用内生罚金 / 守恒残差)✓
4. **双审 V0 草稿期**:本任务基于 V2 综合三版 + frozen JSON 字段路径独立完成 ✓
5. **verifier 纪律**:每条数字均可在 frozen JSON + 5 锚 SHA-12 中重跑(H1=0.4350 / 0.0% 攻击 / R²=0.0007 / b CI / 根指纹 / SHA-12)✓
6. **预登记**:5 锚 SHA-12 = `03c6c01f3697` 沿用 ✓
7. **推送策略**:不主动发王老师, 本文件由 Mavis root 拍板后推送 ✓

## 禁示条款自检(摘要)

- 不超过 1 页 A4(≤ 800 字 + 表格)✓
- 不写"我们认为"等主观措辞(用"判死 / 死 / PASS / 主张降级"等机械语言)✓
- 不复述实验细节(留给完整报告 `V3X_D6_PAPER_V2`)✓
- 不在 D7 之外主动发摘要 ✓
- 不提 BOSS 测法技术细节(无 RBR/RM/Sinkhorn/β=1/8 等技术参数)✓
- 不承诺 Phase 1 启动(只列"后续选择", 让王老师拍板)✓
