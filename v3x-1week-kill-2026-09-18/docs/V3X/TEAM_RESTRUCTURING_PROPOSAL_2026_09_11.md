# 团队重组 + 插件 + 技能分配建议文档 (2026-09-11)

> **任务来源**: user 2026-09-11 16:51 委托(基于 D7 V7 报告 §"六、下一步"4 路径)
> **出具方**: Mavis Worker (subagent, mvs_1296e236e36b42f6bc17cb614fb1bd82) | **执行时点**: 2026-09-11 16:53
> **性质**: 建议文档,不擅自执行
> **冻结区**: 5 锚 `03c6c01f3697` 复算通过、4 SPEC V0.1、v19/v21、corpus/v20、P-F V0 占位、200+ 已落盘、3 个 agent 目录(`.builtin` 3 / `mavis` 3 / `verifier` 2 文件) — **全部 0 触动**

---

## §0 一句话总结

当前 3 个 agent 目录沿 V2 阶段 1-3.5 跑通 0 LLM 工具链, 但 4 路径所需差异化 skill 尚未注册。本建议沿 V7 §"六、下一步"4 路径, 提出 "**`.builtin` 嵌入 4 个 0 LLM skill spec + mavis 派 4 个 explorer subagent + 严守 verifier 0 触动**" 重组方案 — 不创建临时文件 / 不动 scripts/ / 不动 3 个 agent 目录任何现有文件。

---

## §1 背景

**4 路径**(沿 V7 §"六、下一步" + D7 1-page v5): ① 深耕 P-A 9 model × 60 cells 守恒 540/540 + Feshbach S_eff(V7 §"六.1" 路径 1, 5 锚 baseline `03c6c01f3697`); ② 补 P-C 36 档 α-β 模板冗余判定线预注册 + P-E 三模态 ε 检测(V7 §3.6); ③ 沿 v3 §6 Feshbach + Lindblad + S_eff(E) 失真界物理公式深化(V7 §6.1, BCD 收尾); ④ 等 P-F 1 周判死 2026-09-11 → 2026-09-18 observer SKILL(沿 v3 §7 B5 CoT 论文 arXiv:2507.11473, V7 §3.6 TRIGGERED)。

**agent 现状**(`Get-ChildItem -Recurse` 验证, 16:53): 8 个 `deposon-*` agent 已删(回收站, 16:34)— `deposon-successor/data/v3x/reviewer-a/reviewer-b/paper-cn/paper-en/figure`; 3 个配置目录 0 触动 — `.builtin/` 3 文件(`explore/agent.md` 1880 B + `verifier/agent.md` 2083 B + `worker/agent.md` 1705 B), `mavis/` 3 文件(`config.yaml` 61 B + `memory/MEMORY.md` 20730 B + `memory/daily/2026-09-01.md` 125 B), `verifier/` 2 文件(`config.yaml` 61 B + `memory/daily/2026-09-01.md` 125 B); Mavis 历来只派 `task_type=worker`(user 14:25+16:34 严守"不要动 verifier/mavis/.builtin", **从未单独派过 explorer/verifier/mavis/.builtin**)。

**V2 阶段 1-3.5 已跑通的 0 LLM 工具链**(路径 ① 直接沿用): 9 model × 60 cells 守恒 T=52/R=7/A=1 双主线, count residual=0, frac=1.0000000000, 严格 1.11e-16 round-off; P-D 12bit delta_hash 3 链 PASS + Lindblad 8/8 守恒 + 5 BOSS 评估(B1/B3/B5 OBSERVED + F2/F4 N/A); 5 锚 SHA-12 `03c6c01f3697` 锁定(本次复算 03C6C01F3697151B32B86C9016434A17C43E2C1F6DB89BE7641FEE778B74E98A, 前 12 字符一致,文件未动)。

---

## §2 团队重组建议(沿 4 路径分配 plugins + skills)

### 2.1 重组总表(每 agent × 4 路径)

| Agent | 路径 ① P-A | 路径 ② P-C/P-E | 路径 ③ 物理公式 | 路径 ④ P-F 1 周 |
|---|---|---|---|---|
| **`.builtin` (3 文件)** | 0 LLM baseline + `skill_a_p_a_60cells.py` | 0 LLM + `skill_b_p_c_alpha_beta.py` + `skill_c_p_e_3modality.py` | 0 LLM + `skill_d_p_f_observer.py` | 0 LLM observer + 复用 `skill_d_p_f_observer.py` |
| **`mavis` (3 文件)** | 派 worker × `skill_p_a_explorer.py` | 派 worker × `skill_p_c_explorer.py` + `skill_p_e_explorer.py` | 派 worker × `skill_p_e_3modality_explorer.py` | 派 worker × `skill_p_f_observer_explorer.py`(1 周窗口) |
| **`verifier` (2 文件)** | **0 触动** | **0 触动** | **0 触动** | **0 触动** |
| **`deposon-*` (8 删)** | N/A(不复活) | N/A | N/A | N/A |

### 2.2 关键边界

- `.builtin/` 现有 3 文件 0 触动: skill spec **不写** `explore/verifier/worker/agent.md`, 走 plugin 层嵌入但**不修改**现有 3 agent.md
- `mavis/` 现有 3 文件 0 触动: 派单走 Mavis 内部派单引擎, **不修改** `mavis/config.yaml` / `mavis/memory/MEMORY.md` / `mavis/memory/daily/2026-09-01.md`
- `verifier/` 现有 2 文件 0 触动: **不派单、不读、不引用**
- 不复活 `deposon-*` 8 agent: user 16:34 "回收站" 是终态

---

## §3 插件 + 技能分配建议(每 agent 详细)

### 3.1 `.builtin` — 嵌入 4 个 0 LLM skill spec(plugin 层, 不写 agent.md)

| Skill spec | 触发 | 功能 |
|---|---|---|
| `skill_a_p_a_60cells.py` | 路径 ① | 9 model × 60 cells 守恒 540/540 验证(沿 `V2_PHASE2_3_INTEGRATION_2026_09_11.md`) |
| `skill_b_p_c_alpha_beta.py` | 路径 ② | α-β 模板冗余 + 5 锚判定线预注册(36 档 T_frac × 60 cells, 沿 `P_C_V0_1_VERIFICATION_2026_09_12.md` + Trae R1 修正 2) |
| `skill_c_p_e_3modality.py` | 路径 ② | 三模态守恒 ε 检测(0.4114/0.2946/0.2986 三口径同阈值复测, 沿 `V3_PHYSICAL_OPT_2026_09_11.md` §5.3 + Trae R4) |
| `skill_d_p_f_observer.py` | 路径 ③+④ | P-F 1 周判死 observer(沿 v3 §7 B5 CoT 论文 arXiv:2507.11473, 沿 `P_F_V0_1_VERIFICATION_2026_09_12.md` + `BOSS_URL_2026_09_11.md`) |

**严守**: 4 个 skill 都是 **0 LLM**(只读 9 model T/R/A + 5 锚 `03c6c01f3697` 锁定); 不创建临时文件; 不写 agent.md。

### 3.2 `mavis` — 沿用现有根 + explorer subagent 派单(Mavis 派单引擎管理, **不修改** mavis 3 文件)

| 路径 | task_type | skill spec | 模式 |
|---|---|---|---|
| ① | `worker` | `skill_p_a_explorer.py` | 单 worker 9 model × 60 cells 深耕 |
| ② | `worker` | `skill_p_c_explorer.py` + `skill_p_e_explorer.py` | 单 worker 串行 2 方向补判定线 |
| ③ | `worker` | `skill_p_e_3modality_explorer.py` | 单 worker 沿 v3 §6 深化 |
| ④ | `worker` | `skill_p_f_observer_explorer.py` | 单 worker 1 周窗口 observer |

**严守**: task_type 仍是 `worker`; 4 个 explorer **不写入** mavis/config.yaml; 派单前需 user 决定(见 §7)。

### 3.3 `verifier` — 严守 0 触动

**不派单 / 不读不引用 / 不改不补**; 即使需要 verifier 能力, 走 `.builtin/verifier/agent.md` 系统内置, **不动** `C:\Users\Administrator\.minimax\agents\verifier\` 任何文件。

---

## §4 4 路径实施顺序

| 路径 | 沿用基线 | 建议新增 | 派单 | 预期 |
|---|---|---|---|---|
| ① 深耕 P-A 均衡稳定化 | V2 阶段 1-3.5 9 model × 60 cells 守恒 540/540 + Feshbach S_eff 已稳 | `.builtin` 嵌入 `skill_a_p_a_60cells.py`(0 LLM, V2 阶段 2 双主线 T=52/R=7/A=1) | 单 `task_type=worker` × `skill_p_a_explorer.py` | P-A STRONG_PASS 锁链沿用, 5 锚 `03c6c01f3697` 0 触动 |
| ② 补 P-C/P-E 判定标准 | V7 §3.6 P-C 36 档判定线预注册(原 4 档 → 36 档, **预注册**不事后构造, 沿 Trae R1 教训 E8); P-E 三模态 ε 复认(0.4114/0.2946/0.2986 三口径**同阈值 0.30**) | `.builtin` 嵌入 `skill_b_p_c_alpha_beta.py` + `skill_c_p_e_3modality.py`(0 LLM, 沿 Trae R1+R4) | 单 `task_type=worker` × `skill_p_c_explorer.py` + `skill_p_e_explorer.py`(串行) | P-C/P-E 升 PASS 候选 |
| ③ 沿物理公式深化 | V3 §6 物理公式层: Feshbach 共振 `S_eff(E) = T·E_in - R·E_back + A·E_ground` + Lindblad 主方程 8/8 守恒 PASS | `.builtin` 嵌入 `skill_d_p_f_observer.py`(0 LLM, 沿 v3 §6 Feshbach + Lindblad + S_eff 失真界) | 单 `task_type=worker` × `skill_p_e_3modality_explorer.py` | V3 物理公式 V2 升级(BCD 收尾) |
| ④ 等 P-F 1 周判死 | V7 §3.6 P-F TRIGGERED(1 周窗口 2026-09-11 → 2026-09-18, D1 调研 + D2 实现) | `.builtin` 复用 `skill_d_p_f_observer.py`(同路径 ③ 脚本, 1 周 observer 模式) | 单 `task_type=worker` × `skill_p_f_observer_explorer.py`(1 周长跑) | 2026-09-18 出 P-F 1 周判死结论, 沿 B5 CoT 论文 arXiv:2507.11473 评估 |

**实施依赖**: ```
路径 ① (P-A 最稳) ──┐
                     ├──> 路径 ② ──> 路径 ③
路径 ④ (P-F 1 周, 独立) ──┘
``` ① 最稳可先做; ② 依赖 ①; ③ 依赖 ①+②; ④ 完全独立平行跑。

---

## §5 严守约束(7 铁律 0 违反)

1. **0 LLM** + 0 网络 + 0 key 落盘 + 0 proxy(严守 user 09:55 + 14:25)
2. **0 触动 11 frozen**: 5 锚 `03c6c01f3697` 复算通过 + 4 SPEC V0.1 + v19/v21 + corpus/v20(`8423ffe266af`) + P-F V0 占位(`b41c98bf90cc`) + 200+ 已落盘
3. **0 触动 3 个 agent 配置目录**: `.builtin/` 3 / `mavis/` 3 / `verifier/` 2 文件
4. **0 创建临时文件 / 0 写 scripts/**: 沿 V2 阶段 1-3.5 经验(repo 外 + `python -B` + 用后即删)
5. **0 新增 LLM API**: 4 路径 plugins / skills 都是 0 LLM 验证脚本
6. **0 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API**
7. **task_type 必为 `worker`**: Mavis 从未单独派过 explorer/verifier/.builtin(14:25+16:34 严守)

---

## §6 不动 verifier / mavis / .builtin 的具体边界

### 6.1 严守 0 触动的 8 个文件

| 目录 | 文件 | 字节 |
|---|---|---|
| `.builtin/` | `explore/agent.md` | 1880 B |
| `.builtin/` | `verifier/agent.md` | 2083 B |
| `.builtin/` | `worker/agent.md` | 1705 B |
| `mavis/` | `config.yaml` | 61 B |
| `mavis/` | `memory/MEMORY.md` | 20730 B |
| `mavis/` | `memory/daily/2026-09-01.md` | 125 B |
| `verifier/` | `config.yaml` | 61 B |
| `verifier/` | `memory/daily/2026-09-01.md` | 125 B |

(全部 0 触动; 状态列省略因每行同状态)

### 6.2 边界规则

- `verifier/` 严守 0 触动: 即使路径实施需 verifier 能力, 走 `.builtin/verifier/agent.md` 系统内置, **不引用** `C:\Users\Administrator\.minimax\agents\verifier\` 任何文件
- `mavis/` 严守 0 触动: 4 路径 explorer subagent 类型**不写** mavis/config.yaml(Mavis 内部派单引擎管理)
- `.builtin/` 严守 0 触动: 4 路径 plugins / skills **不写** agent.md, 走 plugin 层嵌入但**不修改**现有 3 agent.md
- 4 路径 plugins / skills 不落地(本建议文档只是"建议"): 等 user 决定后, 由 user 派 worker 子代理实施; 实施时 worker 仍然**不动** 3 个 agent 配置目录的任何现有文件

---

## §7 实施待 user 决定

### 7.1 本建议文档**不擅自执行**

4 路径 plugins / skills 是建议, **不擅自落盘**任何 plugin / skill / 派单。等 user 决定后, 由 user 派 worker 子代理实施。

### 7.2 6 个选项等 user 决定

- **选项 A**: user 派 1 worker 实施路径 ① — `.builtin` 嵌入 `skill_a_p_a_60cells.py`
- **选项 B**: user 派 1 worker 实施路径 ② — `.builtin` 嵌入 `skill_b_p_c_alpha_beta.py` + `skill_c_p_e_3modality.py`
- **选项 C**: user 派 1 worker 实施路径 ③ — `.builtin` 嵌入 `skill_d_p_f_observer.py` 沿 v3 §6 物理公式深化
- **选项 D**: user 派 1 worker 实施路径 ④ — `.builtin` 嵌入 `skill_d_p_f_observer.py` P-F 1 周判死(2026-09-11 → 2026-09-18)
- **选项 E**: user 决定 4 路径并行 + 7 铁律严守(4 worker 同时实施)
- **选项 F**: user 进一步指令(4 路径串行 / 部分并行 / 仅 P-A 沿用 / 等 P-F 1 周后再决定)

### 7.3 派单模式参考(无论 A-F)

1. `task_type` 必为 `worker`(user 14:25+16:34 严守)
2. worker 沿用 V2 阶段 1-3.5 0 LLM 工具链(9 model × 60 cells + 5 锚 + 5 BOSS)
3. worker 不动 3 个 agent 配置目录(verifier 2 / mavis 3 / .builtin 3)
4. worker 不动 11 frozen(5 锚 + 4 SPEC V0.1 + v19/v21 + corpus/v20 + P-F V0 占位 + 200+)
5. worker 不创建临时文件 / scripts/
6. worker 不调任何 LLM API

### 7.4 1 周窗口观察点(沿 V7 §3.6 P-F TRIGGERED)

- **D1 调研**: 2026-09-12 / 09-13 — 5 BOSS URL 补查(沿 Trae R2 已完成 18 URL)
- **D2 实现**: 2026-09-15 / 09-16 — boss_f1~f5 测试脚本(沿 v3 §7 B5 CoT 论文 arXiv:2507.11473)
- **D3 收口**: 2026-09-18 — P-F 1 周判死结论(PASS/FAIL/TRIGGERED 升级或降级)

---

## §8 总结

- **建议文档, 不擅自执行** — 7 铁律严守, 等 user 决定(A-F 选项)
- **4 路径 plugins / skills 是建议** — user 派 worker 子代理实施时才落盘
- **3 个 agent 配置目录 0 触动** — verifier 2 / mavis 3 / .builtin 3 文件全部只读
- **5 锚 SHA-12 `03c6c01f3697` 复算通过** — 03C6C01F3697... 前 12 字符一致, 文件未动
- **V1 + V2 团队纪律沿用**: 沿 `AGENT_TEAM_OPT_V2_2026_09_11.md` 8 条不变原则
- **合规**: 0 LLM / 0 网络 / 0 proxy / 0 触动 11 frozen / 0 触动 3 个 agent 配置目录 / 0 创建临时文件 / 0 写 scripts/

—— Mavis Worker, 2026-09-11 16:53
