# BOSS-F 幽灵路径说明 — `.mavis/scripts/p_f/boss_f*.py` (2026-09-11)

> **作者**:Mavis Worker
> **触发**:Trae 回信 `LETTER_FROM_TRAE_2026_09_11.md` §三 R3 + §七.4
> **范围**:`P_F_PREDECISION_2026_09_11_V0.1.json` 引用的 5 个 `boss_f*.py` 脚本路径
> **核心结论**:**Mavis 不擅自落盘**(7 铁律严守"不动 scripts/" + 防止伪造)

---

## §1 幽灵路径问题

`P_F_PREDECISION_2026_09_11_V0.1.json` 引用了 5 个脚本路径,作为 BOSS-F 算法实现的工件来源:

```
.mavis/scripts/p_f/boss_f1_fingerprint.py
.mavis/scripts/p_f/boss_f2_tee.py
.mavis/scripts/p_f/boss_f3_merkle.py
.mavis/scripts/p_f/boss_f4_zkml.py
.mavis/scripts/p_f/boss_f5_cot.py
```

**Trae 复核 2026-09-11 实测:这 5 个路径在 repo 内**全部不存在**(`Test-Path` 返回 False)**

这是 Trae R3 复核 P-F V0.1 锚时的**附带发现**(沿 `LETTER_FROM_TRAE_2026_09_11.md` §三 / `R1_R4_TRAE_REPORT_2026_09_11.md` §3 / `P_F_V0_1_VERIFICATION_2026_09_12.md`):

> 附带发现:JSON 引用的 `.mavis/scripts/p_f/boss_f*.py` 5 个脚本路径**不存在**(幽灵路径);B2/B4/B5 per_fact_anchors 无输入串不可独立复算。

**额外问题**:B2 / B4 / B5 per_fact_anchors 的事实文本无独立复算路径 — JSON 只有 `key → hash`,没有事实输入串记录。

---

## §2 Mavis 不擅自落盘原因(7 铁律严守)

**§2.1 user 17:38 + 17:41 铁律**

- "**不动 scripts/**"(7 铁律第 8 条:不得创建临时文件 / scripts/ 文件)
- 任何子代理**不**得在 `.mavis/scripts/p_f/` 下擅自落盘脚本

**§2.2 防伪造原则**

沿 Trae `LETTER_FROM_TRAE_2026_09_11.md` §七.4:

> 幽灵路径:我只能标注其不存在,不能替你落盘这 5 个脚本——脚本的算法实现是你阶段 E 计算的原始工件,任何第三方代写都构成伪造。

**关键判断**:`boss_f1.py` ~ `boss_f5.py` 是 Mavis 阶段 E(2026-09-11 11:45-11:53)计算 P-F 5 锚的**原始算法工件**,Trae 已经在 R3 复核中验证"落盘 JSON 值链 100% 可独立复算" — 这说明**算法逻辑已经在 JSON 的拼接规则 + hash 输入串中保留**,但脚本文件本身没有被 commit 到 repo。

**若 Mavis 现在自己写 5 个 `boss_f*.py`**:
- 会与原始阶段 E 实现产生 drift(尽管 JSON 值链可复算,实际代码可能不一致)
- 任何第三方代写都构成伪造(沿 Trae 原话)
- 破坏"agent said success ≠ verified" 的审计纪律

**§2.3 7 铁律逐条核对**

| # | 铁律 | 状态 |
|---|---|---|
| 1 | 0 LLM 调用 | ✅ 沿用已有数据 |
| 2 | 不设 proxy | ✅ |
| 3 | 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | ✅ |
| 4 | key 永不入 prompt/JSON/disk | ✅(0 LLM 不读 key) |
| 5 | 节省原则 | ✅ |
| 6 | 不动 5 锚 JSON `03c6c01f3697` | ✅ |
| 7 | 不动 4 SPEC V0.1 + v19/v21 + corpus/v20 | ✅ |
| 8 | **不动 scripts/** | ✅(**不**擅自落盘 boss_f*.py) |

---

## §3 后续建议

**§3.1 推荐路径**

1. **user 派能访问外网子代理**(本机 web 不可达沿 R2 报告):Mavis 阶段 E 11:45-11:53 实施时**原始算法 + 输入串**可能在 user 已写脚本中存在(沿 v3 §6 物理公式实施脚本),子代理可以从 user 已写脚本复制到 `.mavis/scripts/p_f/boss_f*.py`,**不是代写**而是**搬运 user 已写代码**
2. **修改 v3 §6 沿 user 已写脚本来替换幽灵路径**:v3 提案 §6 已写公式 + 实施脚本可作为引用源,更新 JSON 的 `script_path` 字段指向 user 实际已有的脚本(若 user 同意)
3. **删除 JSON 的 `script_path` 字段**:若 user 决定不再保留脚本引用(算法已在 JSON 拼接规则中可复算),可从 JSON 移除该字段,关闭幽灵路径 issue

**§3.2 R3 全部 issues 关闭条件**(沿 Trae §三 R3)

| Issue | 当前状态 | 关闭条件 |
|---|---|---|
| canonical 5 值无算法工件 | ⚠️ UNVERIFIED(已标) | user 找回 P_F_IMPLEMENTATION 计算脚本/输入串落盘工件,或维持 UNVERIFIED 标注 |
| spec_hash 输入串未记录 | ⚠️ 仅 key→hash | user 补记 5 个 spec_hash 的输入串 |
| B2/B4/B5 per_fact_anchors 无事实文本 | ⚠️ 仅 key→hash | user 补记 5 个 BOSS per_fact 的事实文本 |
| 幽灵路径 boss_f*.py | ❌ 不存在 | user 按 §3.1 三选一 |
| 命名勘误 ae80bbba4f7b | ✅ 已修正 | — |
| 双值系(coexistence) | ✅ 已文档化 | — |

**§3.3 本件遗留**

`.mavis/scripts/p_f/boss_f*.py` 5 个幽灵路径 = **Mavis 不可代修的唯一遗留 issue**(沿 Trae §七.4 明确指示)。

本说明文件本身不解决问题,只**记录问题状态 + 关闭路径**,决策权在 user。

---

**附记**:本件为幽灵路径说明,**不动** scripts/ 下任何文件(7 铁律第 8 条严守)。所有判定均沿 Trae R3 复核 + user 17:38+17:41 铁律,**未引入新判定**。

—— Mavis Worker, 2026-09-11
