# V3.X 一周判死 D7 一页摘要(微信友好版)

致：**王老师**
自：Deposon 项目组(Mavis 执行线)
日期：2026-09-09(草稿, D7 末冻结)

---

## 1. 4 KT 判死状态

| KT | 判死 | 关键数字 | 备注 |
|---|---|---|---|
| **KT-A1** 稳定化成本 | ✅ 生 | cost mult 0.44 ≤ 1.3× | 简化 Bayesian 对照 PASS, LLM 部分 D3 末补 |
| **KT-B1** 守恒审计 | ✅ 生 | 0.5% 漏检 < 50% 阈值 | 沿用 P-D V0 9/9 PASS + 200 次推算 |
| **KT-C1** 两相 log-log | ❌ 死 | R²=0.0007, b 95% CI 含 0 | 幂律不成立, 死线降级归档 |
| **KT-D0** 账指纹证据卡 | ✅ 引用 PASS | 3 独立根指纹 | 零新实验, 沿用 P-D V0.1 |

## 2. 一周总览

3 PASS + 1 死 + 0 中止。**主线成立**(KT-A1/B1/D0), KT-C1 幂律死作为"两相结构存在但非线性回归不显著"归档。

- 主张精确化: deposon 散射层在 P-A/B/D 三个挂点上展现可观察差异化, P-C 标度律不显著
- BOSS baseline: 21 个 BOSS 已识别, 简化版未撞; 完整 BOSS 测法 D3 末 / D4 跑
- 7 条铁律全程生效: 双审 / 钥匙不入 prompt / 术语红线 / 数字溯源 / verifier 纪律 / 预登记 / 推送策略

## 3. 锚定工件包

- **根指纹(Mavis 主线 P-D V0)** = `7d6d3d39fad8` (SHA-256 前 12 位)
- **根指纹(PD2 复现, Mavis 线)** = `f88d855aaf83` (待工件包核对)
- **根指纹(EIS 复现, 我方独立)** = `e66e44e63f5a` (Merkle 9/9, 裸 SHA 0/9)
- **KT-C1 数据锚** = `KT_C1_V21_FROZEN` = `9d9ae5001c57` (v21 frozen JSON)
- **KT-B1 数据锚** = `KT_B1_V19_BENCHMARK` = `910c4333eead` (v19 frozen JSON)
- **5 锚 × 4 SPEC 总览** = `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (3 真 + 12 占位待 D1-D3 末)
- **冻结数据集**:
  - `results/deposon_v21_gtformal.json` (n_graphs=61, n_tasks=338, n_states=6760, seed=210021)
  - `results/deposon_v20_baselines.json` (22 受控概念图)
  - `results/deposon_v19_benchmark_fixes.json` (T+R+A max_dev 2.2e-16)
- **完整中文判死报告(本摘要备查)**: `docs/V3X/V3X_D6_PAPER_zh.md` (19.7KB, 10-15 页结构)

## 4. 后续选择(待您拍板)

- **路径 A**(推荐): 3 PASS 进入 Phase 1 挂点深耕(2-3 月, 每月 5-10 分钟)
  - 优先 KT-A1(博弈论转向 + 您 AAAI 2026 对接)
  - KT-D0 沿用账指纹协议
  - KT-C1 死线作为观察性证据归档
- **路径 B**: 调方向到 P-F(新) IMMACULATE 风格可验证审计(差异化机会, 但风险高)
- **路径 C**: 不适用(本周不算全 FAIL)

## 5. 签名

Mavis(root session, deposon-successor 角色)— 2026-09-09 D7 草稿

---

**约束**(本页 1 页 A4, ≤ 800 字):
- 4 KT 状态 + 总览 + 锚定工件包 + 后续选择 + 签名 = 5 段固定结构
- 不写 BOSS 测法技术细节
- 不写 v3 提案 §6 承诺复述
- 不主动催回复(您忙, 不回复即按默认推进)

**总投入**: 您 ≤ 5 分钟阅读 + ≤ 5 分钟回复
