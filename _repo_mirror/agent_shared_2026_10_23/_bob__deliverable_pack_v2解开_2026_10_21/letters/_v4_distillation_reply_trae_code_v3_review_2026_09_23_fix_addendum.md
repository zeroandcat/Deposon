# 修正补记信：E-15 锚链复位（PI 授权执行）· Trae code → deposon PI

> **补记方**：Trae code
> **主函**：`letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md`（SHA-12 `9BB22099DB3B`，2026-09-23）——本件为其修正补记，不重复主函内容
> **授权**：PI 于 2026-09-23 主函交付后明示「**你直接修正**」，授权对象 = 主函 §3.4/§4 列为「须 PI 先解决」的 **E-15（5 锚根件锚链断裂）**
> **性质**：资产层修复（恢复冻结契约所声明的字节状态）；**不涉任何实验结论与判定本体**

---

## §1 修了什么

| 项 | 内容 |
|---|---|
| 缺陷 | E-15：冻结主路径 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 被 11,318 B 顶替件（`6E9CD8CD8E07`）占据，冻结期望件（`03C6C01F3697`，6,680 B）仅存于未声明的 `_non_upload_local_archive`；冻结 fallback 路径无件 → `_verify_15frozen.py` 15/16 PASS，唯一 FAIL |
| 动作 | ① 顶替件备份（新名 `.bak_2026_09_23`，零覆盖）；② 冻结期望件从 `_non_upload_local_archive` 复位至主路径；③ 终验 |
| 执行件 | `deposon_team/plugins/_v3_review_r7_fix_e15_2026_09_23.py`（幂等保护 + 源件校验 + 备份名占用三重 assert；实跑 exit 0） |

## §2 修前核查（防误伤，机器扫描）

- 仓内 **13 个脚本**期望主路径 = `03c6c01f3697`：`boss_pa_1/2/3_*.py`、`skill_a/b/c/d_*.py`、`_pg_v01_compute.py`、`_verify_pg_v0.py`、`_verify_batch5_2026_09_18.py` + 6 个归档 V4 自检脚本；归档 `_v4_reader_verify_2026_09_20.py` 记录该件尺寸 **6,680 B**，与复位源逐字节一致。
- **0 个脚本**引用顶替件独有的 `boss_baselines` 键 → 顶替件无任何在跑依赖 → **复位零误伤**。

## §3 前后 SHA-12 对照

| 件 | 修前 | 修后 |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `6E9CD8CD8E07`（11,318 B） | **`03C6C01F3697`（6,680 B）** |
| `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | — | `6E9CD8CD8E07`（11,318 B，新增备份） |

**回滚**：备份件字节复制回主路径即回到修前状态。

## §4 修后终验（机器复算）

```
python -B deposon_team/plugins/_verify_15frozen.py
→ verifier/handoff/KT_ABC1_anchors_sha256_12.json   03c6c01f3697  03c6c01f3697  True  repo
→ TOTAL: 16 frozen files | OK: 16 | FAIL: 0
→ 0-touch declaration: PASS
```

修前 15/16（唯一 FAIL = E-15）→ 修后 **16/16 PASS**。V3/V4 各报告所引「5 锚 SHA-12 `03c6c01f3697` 未动」**自此在冻结主路径上重新可验证**。

## §5 没修什么（仍属 frozen / 结论层，维持只登记）

- **E-1…E-14、E-16**：全部位于已冻结报告正文或仓外件——按委托信 §5 仍以勘误清单登记（`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` §5），PI 另行处置。
- **E-17（`behated` 错字）**：位于 V4 邀请函 L218；**PI 已于 2026-09-22 裁定「不再修邀请函」**（`results/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md` L679）——已登记结案，非悬挂项。
- **E-18（4 个 `skill_*` 缺 SELF-CHECK 尾块）**：frozen-18 内，不动（仅登记）。
- **E-19（verifier 家族 4 件 BOM）**：verifier 内置，不动（仅登记）。
- **BOSS-P-A2 vs KT-B1 的 PG 口径冲突（3/22 vs 22/22）**：**结论层分歧，非资产缺陷**——修正它 = 改判定本体，超出「资产层修复」授权语义，**不在本次修正范围**。需 PI 以预注册口径裁决后另行处置。
- **3 件真缺件**（`deposon_v17_fusion_fix.json` / `deposon_v18_api_supplements.json` / `deposon_v20_baselines.json`）：repo/archive/sub 三处皆无——**无法「修正」不存在之物**，只能补件或废版标注，决定权在 PI。
- **勘误件更新**：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 已增 §7 处置记录 + §8 精扫复核记录 + E-17/E-18/E-19（初版 `48EFD3828D54` → 终版 SHA-12 见落盘报值）。

## §6 0 触动声明（修正后口径）

本轮修正的**唯一一处既有文件写入** = E-15 复位（§3 表）。其余一切既有文件（19 REPORT、16 frozen 其余 15 项、repo 内既有 `*.py`、`results/`、`corpus/v20/`、`deposon-sub/`、`_v4_*` 全链）**仍 0 字节改动**，由 `_verify_15frozen.py` 16/16 PASS（除复位件外 15 项 SHA 逐一相符）机器自证。0 LLM / 0 外部 URL / 0 明文密钥。

## §7 续轮：r8 精扫——可修面残余缺陷 = 0（机器自证）

「直接修正」续轮对委托信 §3 全部修复项做 tokenize 级精扫复核（`deposon_team/plugins/_v3_review_r8_precise_scan_2026_09_23.py`，实跑 exit 0）：

| 检验面 | 可修面结果 | 依据 |
|---|---|---|
| 无效转义 | **0 处真实** | r8 逐 STRING token（raw 前缀跳过）扫全 plugins 树 34 件；r4 先前报的 ODD_ESCAPE **全部为 raw-string 假阳性**——沿项目「测量仪器自身即误差源」惯例**修仪器不修文本**（r4 原件按历史证据保全） |
| BOM | **0**（报告层） | `docs/V3X` 全 md/json 0 BOM；plugins 4 件 BOM 全在 verifier 家族 → E-19 登记（不动） |
| 缺 SELF-CHECK 尾块 | **0** | 9 个 `boss_*.py` 已于 09-16 全部补齐（`TRAE_SELFCHECK_2026_09_16` 标记逐件在盘实核）；仅 4 个 frozen `skill_*` 悬挂 → E-18 登记 |
| 缺 `__main__` guard | **0**（可修面） | verifier 家族不动；`_v3_review_r*` 系一次性取证件，字节稳定即证据价值，不加 guard 以免 SHA 漂移 |
| repo 外绝对路径 | **0** | verifier fallback 系设计路径；取证脚本指向 `deposon-sub` 系取证必需 |

**终态**：E-15 已修 + 上述五面全零 → **委托信 §3 修复项在可修面上残余缺陷合计 = 0**；其余全部位于不动层并已按勘误 E-1…E-19 完整登记。「直接修正」的可修面至此清零，剩余事项全部属 PI 裁决域（结论层冲突 / 真缺件补废 / frozen 正文处置）。

---

*出证：Trae code · 2026-09-23 · 本件 SHA-12 见落盘报值*
