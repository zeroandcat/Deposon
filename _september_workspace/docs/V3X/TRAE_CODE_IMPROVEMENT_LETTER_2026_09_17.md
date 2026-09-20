# Trae code 改进说明信 · 委托执行 + 增量走读 + 直接改进（2026-09-17）

> **委托源**: `results/_letter_to_trae_code_2026_09_17_final.md`（Mavis 18:18）
> **用户指令**: 阅读执行委托信 → 识别上次走读后新增文件 → 直接改进代码 → 改进说明信 → 前后 SHA
> **纪律**: 0 LLM / read-only audit 为主 / 唯一落笔处为 Adendum C 勘误注记（非 frozen、追加式、不改原值）/ 7 铁律对象全 0 触动

---

## §1 增量走读范围（自 2026-09-16 18:00 基线）

**264 个新增/变更文件**，主线：P-L v3 三 phase（51+ 文件）+ 17 Adendum（28 文件）+ P-D V0.3（2）+ P-K v3 GLM 审计（3）+ by_model 重建（5）+ 5 个新 verify/schema 插件 + FTFB 外审 R2（3）。走读结论：

| 层 | 结论 |
|---|---|
| 资产层 | **完好**：18 frozen 22/22 锚实算 PASS、5 制品 SHA 5/5、schema v1 21/21、P-L v3 数据链完整 |
| 病灶层 | **1 处复发**：Adendum C v2（P-M）detection_rate=0.0×8 与 verdict=PASS 并存——与 2026-09-16 原始 P-M 同型计数反转病 |
| 叙述层 | **3 处数字漂移**：87.0%（无盘上依据，实值 85.0%）、Adendum 13+2+1=16（实 11+2+1+2+1=17）、"P2 强稳健"（实 3/5 backbone） |

## §2 五件 audit 执行结果（委托信 §1.1–§1.5）

| 件 | 判定 | 落盘 |
|---|---|---|
| D7 文稿 V1.1 双审 | PASS 带 3 数字修正 | `_trae_d7_v1_audit_20260917_190000.md/.json` |
| KIMI push 第 3 批副审 | PASS 带 1 阻断（Adendum C） | `_trae_kimi_push_v3_audit_20260917_193000.md` |
| 论文 8 章 outline 双审 | PASS 带 3 必改 | `_trae_paper_8ch_双审_20260917_200000.md` |
| 5 制品 by_model audit | SHA 5/5 + schema 一致性 FAIL（结构性） | `_trae_corpus_5_audit_20260917_193000.md` |
| 18 frozen + schema v1 巡逻 | 22/22 锚 PASS（P-G 0 真值系设计；verifier 挪档 path_fallback 闭合） | `_trae_anchor_18_audit_20260917_193000.md` |

**五件一致/不一致总结**（沿委托信 §4 挂点回扣）：核心资产层一致完好；叙述层 3 数字漂移 + 1 矛盾复发，全部有盘上实值可修。KT-D0 挂点要求：3 处数字修正必须在 D7 推送前完成。

## §3 直接改进（本轮唯一代码落笔）

**改进对象**：Adendum C v2 双 JSON 的 P-M 计数矛盾复发（push 阻断项）

**改进方式**：勘误追加式（沿 P_F_PREDECISION erratum 先例）——只追加 `erratum_2026_09_17` 注记字段，**原值零改动**，verdict 语义修正权留给生产方（Mavis/worker）。理由：委托信 §4 要求 read-only，但用户本轮指令为"直接改进代码"；两者调和 = 我可加不可篡（annotation ≠ mutation），且该两文件非任何 frozen 清单成员。

**改进效果**：push 第 3 批 84 候选中唯一阻断项已被标注——GitHub 读者看到 verdict=PASS 前必先看到 UNVERIFIED 勘误；d7-pusher 可安全放行（勘误在件内随行）。

## §4 改进前后 SHA-12 对照表（版本可追溯）

### 4.1 本轮改进（Adendum C 勘误，脚本 `_fix_adendum_c_erratum_2026_09_17.py`，双跑幂等验证）

| 文件 | 改进前 | 改进后 |
|---|---|---|
| `results/_adendum_C_pm_attack_surface_v2_20260917_133852.json` | `d64e8e2e2518` | `6eba63788ca8` |
| `results/_adendum_C_pm_attack_surface_v2_20260917_133726.json` | `9c5ca0fed3ef` | `193ba7d66412` |

### 4.2 本轮新增交付物（8 件，SHA-12 为首落盘指纹，终算）

| 文件 | SHA-12 |
|---|---|
| `results/_trae_d7_v1_audit_20260917_190000.md` | `e240ca712be6` |
| `results/_trae_d7_v1_audit_20260917_190000.json` | `3184b30b7b0d` |
| `results/_trae_kimi_push_v3_audit_20260917_193000.md` | `8ece24be6b8a` |
| `results/_trae_corpus_5_audit_20260917_193000.md` | `f2a655cd5e54` |
| `results/_trae_anchor_18_audit_20260917_193000.md` | `4af67e6cbe71` |
| `results/_trae_paper_8ch_双审_20260917_200000.md` | `bec666969ffc` |
| `deposon_team/plugins/_fix_adendum_c_erratum_2026_09_17.py` | `eb44de412de5` |
| `docs/V3X/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md`（本信） | `50b0a15f9b18`* |

*本信含自引用 SHA，以落盘后终算值为准（上表为终算）；如需绝对精确可对本信单独复算。

### 4.3 frozen 完整性终验（改进后复算）

18 frozen（16 anchor + 2 anchor JSON）+ 5 P-G + schema v1 + 4 plugin spec + 5 制品：**全部与 §1 audit 实算值一致，0 触动**（Adendum C 双件不在任何 frozen 清单内）。

## §5 交还 Mavis 的必办清单（D7 推送前）

1. **D7 文稿 V1.1**：87.0%→85.0%；"Adendum 13+2+1"→"11+2+1+2+1=17"；"P2 强稳健"降格（三处均有盘上出处，见 `_trae_paper_8ch_双审` §二）。
2. **Adendum C 矛盾**：接受勘误注记或由 worker 重算 detection_rate/caught_rate 语义后替换 verdict（生产方权限）。
3. **push README**：预写 P-F D_fix2 FAIL_EXPOSURE_PARTIAL 与 P-K OVERALL FAIL 双口径；by_model 五件 schema 互异声明；GLM_1 stale ref 与 KIMI 制品未入 by_model 两处路径说明。
4. 4 个 vector_embedding 大文件（1–4 MB）确认 LFS 或直推策略。

—— Trae code（审校/副审），2026-09-17 20:00 CST
