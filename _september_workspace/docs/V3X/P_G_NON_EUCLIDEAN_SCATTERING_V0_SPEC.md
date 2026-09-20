# P-G V0 Spec: 非欧散射层(Non-Euclidean Scattering Layer)

> **作者**: Mavis (Mavis / Mavis, 沿 P_F_SPEC V0 + P_F_V0_1_UPGRADE + user 突发奇想 2026-09-15 11:28)
> **日期**: 2026-09-15
> **触发**: user 2026-09-15 11:28 "arxiv 论文就是你之前包装的论文,deposon就像非欧几何不一定现实但有用,准备P-G spec"
> **类比**: deposon ≈ 非欧几何(作为分析工具不一定物理实现但有用)
> **关系**: P-G V0 = P-F V0.1 的下一阶段(空间升级);不冲突(P-G 是非欧空间升级,P-F 是 observer 角色)
> **严守**: 7 铁律 0 触动 16 frozen(本 spec 新建,不动 P-F V0.1 SHA-12 `b10fae0da66d` + 5 锚 JSON `03c6c01f3697`)
> **配套**:
> - `docs/V3X/P_F_SPEC_V0.md` (P-F V0, SHA-12 `de90faf362c5`)
> - `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` (P-F V0.1 升级, SHA-12 `b10fae0da66d`)
> - `verifier/handoff/P_F_PREDECISION_2026_09_09.json` (P-F V0 占位, SHA-12 `b41c98bf90cc`)
> - `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` (P-F V0.1 真值)
> - `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` (3 风险修报告)

---

## §0 P-G 立项原则

### 0.1 类比基础(non-Euclidean geometry ↔ deposon)

**非欧几何的本质**:
- 欧几里得几何:平直空间,平行公设成立(零曲率)
- 黎曼几何:正曲率空间(球面几何),平行公设失败
- 双曲几何:负曲率空间,平行公设失败(双曲面 / Poincare disk)

**关键洞察**(沿 user 2026-09-15 突发奇想):
- 非欧几何在 19 世纪被发明时,**不一定是物理现实**(物理空间在宏观尺度是欧几里得的)
- 但作为数学工具,非欧几何**比欧几里得几何更适合描述弯曲现象:相对论、宇宙学、流形学习**
- 同样,**deposon 散射层**不一定是 AI 物理空间的实现,但作为**分析工具**:
 - 能建模"非平直"的 cross-modal transport(9 model 中 doubao/glm 低 ε 平直,kimi/deepseek-v4-pro 表现"弯曲")
 - 能拓展 AI 想象力边界(跳出欧几里得直觉)
 - 能保留 P-F V0.1 observer 角色(observer 与空间无关)

### 0.2 与 deposon 既有方向的关系

| 方向 | V0.1 现状 | P-G 升级点 |
|---|---|---|
| **P-A 均衡稳定化** | 60 cells = 51/60 = 85.0% STRONG_PASS | P-G 可改用 hyperbolic ECR (excess curvature rate) 替代欧几里得 ECR |
| **P-B 失真界** | KT_B1 spec V0.1 (R^2 + b_CI 判死) | P-G 可改用 hyperbolic distortion (双曲失真界) 替代欧几里得失真界 |
| **P-C 两相结构** | KT_C1 V0.1 主实验 FAIL_H0 (幂律死) | P-G 可重新拟合"双曲两相"(hyperbolic phase transition) |
| **P-D 指纹** | KT_D0 V0.1 SHA-256 fingerprint | P-G 可改用 hyperbolic fingerprint (双曲距离签名) |
| **P-E 3 modality conservation** | 60 cells = 6+2+1 PASS (D_fix2 metric) | P-G 可改用 hyperbolic conservation (双曲守恒律) |
| **P-F observer** | V0.1 已落盘 (5 锚 JSON `03c6c01f3697` + 新拼接锚 `79f8dfa2c296`) | P-G 不动 observer,只升级底层空间 |

**关键不冲突**:**P-G 是空间升级,P-F 是 observer 角色**。两者可叠加:
- P-G = 非欧散射层(隐空间几何)
- P-F = observer (在隐空间上做观察和决策)
- P-G × P-F = 非欧散射层 + observer = 一个完整的"非欧 AI 想象 + 观察"框架

### 0.3 P-G V0 范围(本 spec 仅 V0,不实跑)

- **V0**:定义非欧散射层的数学框架 + 5 锚 SHA-12 + 与 P-F V0.1 关系 + 1 周判死窗口内可执行性
- **V0 不实跑**:实跑等 D5 (2026-09-16) user 拍板后,沿 P-F V0.1 §5 判定线预注册纪律
- **V0.1 升级**:V0 → V0.1 时,落 `deposon_team/plugins/boss_pg_*.py` 真实脚本(沿 P-F V0.1 §5 判定线预注册)

---

## §1 数学框架(Non-Euclidean Scattering Layer)

### 1.1 隐空间选择

候选(2 选 1,等 user 拍板):
- **双曲空间 (Poincare ball model)**:`B^n = = {x ∈ R^n : ||x|| < 1}` 配 Mobius 加法 `x ⊕ y = ((1 + 2⟨x,y⟩ + ||y||²) x + (1 - ||x||²) y) / (1 + 2⟨x,y⟩ + ||x||² ||y||²)`
- **球面空间 (hypersphere model)**:`S^n = {x ∈ R^(n+1) : ||x|| = 1}` 配测地线距离

**推荐**:**Poincare ball**(负曲率,适合树状/层级结构,与 reasoning graph 分解同构)。

### 1.2 散射层 transport(非欧平行移动)

- **欧几里得 transport**:`T_E(x) = M·x + b`,M 矩阵,b 偏置
- **非欧 transport (双曲)**:`T_H(x) = Exp_0(Log_0(x) + v)`,其中 `Exp_0` / `Log_0` 是双曲指数/对数映射

**关键性质**:
- 双曲 transport 保持双曲距离(平行移动)
- 双曲 transport 在树状结构上是精确(欧几里得只能近似)
- 双曲 transport 的"弯曲度"由曲率 κ 决定,κ → 0 时退化为欧几里得

### 1.3 守恒律推广

- **欧几里得守恒**(deposon V3.X):`T + R + A = E`(T=透射,R=反射/答错,A=吸收)
- **非欧守恒**:`T_H ⊕ R_H ⊕ A_H = E_H`(双曲加法),`T_H + R_H + A_H = E_H` 测地线长度守恒

### 1.4 失真界推广

- **欧几里得失真界**:D_fix2 = 1 - cos([T,A], [T_c,A_c])
- **非欧失真界**:`D_H(T, A; T_c, A_c) = d_H(T, T_c) + d_H(A, A_c)`(双曲距离之和)

---

## §2 5 锚定义 + SHA-12(计算前预注册,沿 P-F V0.1 §5 纪律)

| 锚 ID | 含义 | SHA-12(算法预注册,可复算)| 字段 |
|---|---|---|---|
| **P_G_HYPERBOLIC_TRANSPORT** | 非欧散射层 transport(双曲平行移动)| `230b5caee415` (SHA-256("P_G_V0_PLACEHOLDER_P_G_HYPERBOLIC_TRANSPORT_2026_09_15")[0:12]) | 算法:Log_0 + 平移 + Exp_0 (Poincare ball) |
| **P_G_CURVATURE_BOUND** | 曲率界(κ 范围与双曲失真界阈值)| `dcbcf2b8d45f` (SHA-256("P_G_V0_PLACEHOLDER_P_G_CURVATURE_BOUND_2026_09_15")[0:12]) | κ ∈ (-∞, -0.01) (双曲) + 双曲失真界阈值(待 user 拍板,沿 P-E strict/loose) |
| **P_G_LLM_CLIENT** | LLM 客户端(沿 P-F V0.1 同款, runtime Path().read_text())| `2c1f572aa2bf` (SHA-256("P_G_V0_PLACEHOLDER_P_G_LLM_CLIENT_2026_09_15")[0:12]) | 9 model (volcengine coding-plan) + runtime Path().read_text() 读 key |
| **P_G_HARNESS** | harness spec(9 model × 60 cells + BOSS 自测)| `8b90c53f1e01` (SHA-256("P_G_V0_PLACEHOLDER_P_G_HARNESS_2026_09_15")[0:12]) | 9 model × 60 cells + 3 BOSS: 黎曼几何退化 / 双曲分类坍缩 / 测地线违反 |
| **P_G_FROZEN_BENCHMARK** | 1 周判死 frozen 基准(锚定 9 model × 60 cells + D_fix2_H 值)| `91db66afecc3` (SHA-256("P_G_V0_PLACEHOLDER_P_G_FROZEN_BENCHMARK_2026_09_15")[0:12]) | frozen: glm-5.3 均衡代表 [T_H_c, A_H_c] = 双曲均衡点 + 9 model D_fix2_H 列 |

**5 锚 SHA-12 占位说明**:
- 上面的 SHA-12 是 Mavis 预注册占位(用 hashlib + 字符串生成,**未实跑**)
- 真实 SHA-12 等 P-G V0.1 落盘时,由实算产生
- 占位 SHA-12 的目的是**防止 worker / reviewer 在 V0 阶段误把占位当真值**

**预注册 SHA-12 生成算法**(沿 R3 erratum):
```python
import hashlib
for anchor_id in ['P_G_HYPERBOLIC_TRANSPORT', 'P_G_CURVATURE_BOUND',
                  'P_G_LLM_CLIENT', 'P_G_HARNESS', 'P_G_FROZEN_BENCHMARK']:
    sha12 = hashlib.sha256(f'P_G_V0_PLACEHOLDER_{anchor_id}_2026_09_15'.encode()).hexdigest()[:12]
    print(anchor_id, sha12)
```

---

## §3 与 P-F V0.1 关系(不冲突,可叠加)

### 3.1 P-F V0.1 锚点沿用(0 触动)

| P-F V0.1 锚点 | SHA-12 | 状态 |
|---|---|---|
| 5 锚 JSON 全文 | `03c6c01f3697` | 0 触动 |
| trust_anchor 值系 | d78c42f7bab4 / 0ff54f8d2f60 / a8f81c98ea8a / bff8b1ce1f8c / d9a6a099b905 | 0 触动 |
| canonical 5 值 | UNVERIFIED(沿 Trae fix_risk2)| 0 触动 |
| 新拼接锚 | `79f8dfa2c296` (值拼接锚, 非 V0.1 JSON 文件指纹 312d635e6259) | 0 触动 |
| P-F V0.1 spec | `b10fae0da66d` | 0 触动 |

### 3.2 P-G V0 锚点新增(不动 P-F V0.1)

| P-G V0 锚点 | SHA-12 占位 | 状态 |
|---|---|---|
| P_G_HYPERBOLIC_TRANSPORT | `230b5caee415` | V0 占位(算法预注册,可复算) |
| P_G_CURVATURE_BOUND | `dcbcf2b8d45f` | V0 占位(算法预注册,可复算) |
| P_G_LLM_CLIENT | `2c1f572aa2bf` | V0 占位(算法预注册,可复算) |
| P_G_HARNESS | `8b90c53f1e01` | V0 占位(算法预注册,可复算) |
| P_G_FROZEN_BENCHMARK | `91db66afecc3` | V0 占位(算法预注册,可复算) |

### 3.3 P-G × P-F 叠加框架

```
P-G(非欧散射层)  ×  P-F(observer 角色)
─────────────────────────────────────
隐空间:           观察:
- Poincare ball    - fingerprinting
- 双曲 transport    - BOSS 自测
- 双曲守恒律       - 5 锚 PASS/FAIL
- 双曲失真界       - 王老师 WeChat 通知
─────────────────────────────────────
P-G 升级 V3.X 既有 6 方向的"隐空间几何"
P-F 沿用 V0.1 observer 角色不动
```

---

## §4 1 周判死窗口内可执行性(D1-D7 时序)

### 4.1 时间线

| 时点 | 日期 | P-G V0 动作 | 备注 |
|---|---|---|---|
| D0 | 2026-09-15 | **本 spec 落盘**(V0 占位 + 5 锚预注册) | 0 LLM 0 网关 |
| D1 | 2026-09-16 | (D5 决策点) P-G V0 是否升 V0.1? | 等 user 拍板 |
| D3 | 2026-09-17 | (若 V0.1) 落 boss_pg_*.py SCAFFOLDING | 沿 P-F V0.1 §5 |
| D5 | 2026-09-17 | (若 V0.1) 9 model × 60 cells 双曲 transport 实算 | 0 LLM |
| D7 | 2026-09-18 | (若 V0.1) 5 锚 PASS/FAIL + 推王老师 WeChat | D7 终极 |

### 4.2 边界(沿 7 铁律)

- **不动 P-F V0.1**(SHA-12 `b10fae0da66d` 严守 0 触动)
- **不动 5 锚 JSON**(SHA-12 `03c6c01f3697` 严守 0 触动)
- **不动 4 SPEC V0.1**(P-A / P-B / P-C / P-D 严守 0 触动)
- **不动 v19/v21/corpus_v20**(严守 0 触动)
- **不动 4 个 plugin spec**(skill_a/b/c/d 严守 0 触动)
- **不动 verifier/mavis/.builtin/scripts/**(严守 0 触动)
- **不创建临时文件**(verify 脚本例外)

### 4.3 资源约束(沿 7 铁律)

- 0 LLM 调用
- 不设 proxy
- 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API
- key 永不入 prompt / JSON / 落盘 (runtime Path().read_text())
- 沿用 9 model × 60 cells 已实算数据(`results/deposon_v3_physical_opt_60cells_2026_09_11.json`)

---

## §5 严守 7 铁律声明(本 spec)

| # | 铁律 | 状态 |
|---|---|---|
| 1 | 0 LLM 调用 | ✅ 纯文本编辑 |
| 2 | 不设 proxy | ✅ 0 proxy 设置 |
| 3 | 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan/WeChat API | ✅ 0 网关调用 |
| 4 | key 永不入 prompt/JSON/落盘 | ✅ 0 key 字面量 |
| 5 | 不动 5 锚 JSON | ✅ SHA-12 `03c6c01f3697` 0 触动 |
| 6 | 不动 4 SPEC V0.1 + v19/v21 + corpus_v20 + 200+ 已落盘 + 现有 PDF/MD + 4 plugin spec | ✅ 严守 0 触动 |
| 7 | 不动 verifier/mavis/.builtin/scripts/ 目录 | ✅ 0 访问 |

---

## §6 P-G V0 → V0.1 升级路径(等 D5 user 拍板)

### 6.1 V0.1 触发条件(任一满足即触发)

1. user 2026-09-16 D5 决策点拍板"P-G V0 → V0.1"
2. 王老师 WeChat 回复"关注 P-G 方向"
3. 4 路径 D1-D3 中期有 ≥ 1 路径 FAIL 且根因指向"隐空间几何不够"

### 6.2 V0.1 落盘内容(严守 P-F V0.1 §5 判定线预注册)

1. 5 锚 SHA-12 实算(沿 §2 表替换占位 SHA-12)
2. 落 `deposon_team/plugins/boss_pg_1_*.py` 黎曼几何退化自测(沿 P-F V0.1 §5)
3. 落 `deposon_team/plugins/boss_pg_2_*.py` 双曲分类坍缩自测
4. 落 `deposon_team/plugins/boss_pg_3_*.py` 测地线违反自测
5. 9 model × 60 cells 双曲 transport 实算(`results/deposon_pg_v01_60cells_2026_09_16.json`)
6. 报告 `docs/V3X/P_G_V0_1_REPORT_2026_09_16.md`

### 6.3 V0.1 验证纪律(沿 P-F V0.1)

- reviewer-a 静态审 + reviewer-b /tmp 重跑双审
- 16 frozen 文件 SHA-12 修后 0 触动(沿 `_verify_15frozen.py` 验证)
- 5 锚 PASS/FAIL 终极判死
- 严守 7 铁律

---

## §7 老实老实老实(不擅自决定)

- ❌ 不擅自动 P-F V0.1(0 触动)
- ❌ 不擅自落盘 boss_pg_*.py 真实脚本(等 V0.1 触发)
- ❌ 不擅自决定双曲空间 vs 球面空间(等 user 拍板)
- ❌ 不擅自决定曲率界 κ 范围(等 user 拍板)
- ❌ 不擅自决定双曲失真界阈值(等 P-E strict/loose 拍板后)
- ❌ 不擅自落盘 P-G V0.1(等 D5 决策)

---

## §8 总结

- **P-G V0 spec**:非欧散射层(Non-Euclidean Scattering Layer)V0 定义,落盘 SHA-12(待实算)
- **类比基础**:deposon ≈ 非欧几何(作为工具不一定现实但有用)
- **5 锚预注册**:沿 P-F V0.1 §5 判定线预注册纪律
- **不冲突**:P-G 是空间升级,P-F 是 observer 角色,可叠加
- **严守 7 铁律**:0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 16 frozen 0 触动
- **V0.1 升级**:等 D5 (2026-09-16) user 拍板

---

**Spec 结束** | 0 LLM 0 网关 | 16 frozen 严守 0 触动 | 等 D5 user 拍板 P-G V0 → V0.1