# KT-B1 SPEC V0 草稿

> **元信息**
> - **作者**: Mavis 执行线(worker-b 子代理派单)
> - **日期**: 2026-09-09
> - **状态**: V0 草稿(D0 准备阶段,等待 successor 算 5 锚 SHA-256 前 12 位)
> - **位置**: `docs/V3X/KT_B1_SPEC_V0.md`
> - **关联**:
>   - 上游: v3 提案(王老师致王子贺老师,2026-09-04,4 页,第六节 KT-B1 行)
>   - 下游: Mavis 内部 P-B 失真界 V0 spec(`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`)
>   - BOSS 源: `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` V0.2 §方向 2 BOSS-B1/B2/B3
>   - D0 准备: `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` §1.2 / §3

---

## 0. 元约束与铁律

### 0.1 7 条铁律(沿用 D0 准备 §6)

1. ✅ **双审**: reviewer-a 静态审 + reviewer-b `/tmp` 副本独立重跑
2. ✅ **API key 不入 prompt**: runtime `Path(file).read_text()` 读取,不入 prompt
3. ✅ **术语红线**: 沿用 deposon 既有 T+R+A=1 / 透射+反射+耗散
4. ✅ **数字溯源**: 全部论断指向冻结 JSON 字段路径
5. ✅ **verifier 纪律**: 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/
6. ✅ **预登记**: 5 锚 SHA-256 前 12 位先于运行冻结并公布
7. ✅ **推送策略**: 王老师 = WeChat 顾问模式(每周 1-2 条 + 收结果,~5-10 min/周)

### 0.2 强度声明(沿用 v3 提案)

- **判死级**: 已预登记并执行的事实(5 锚 + 判死线 + 跑分)
- **观察性**: 数值规律(失真上界 vs v19 冻结残差)
- **探索性**: 猜想(守恒审计 = 检测力上限)

### 0.3 本 SPEC 不做的事(显式声明)

- ❌ 不改 P-D V0.1.1(已 PASS,只引用)
- ❌ 不重做王老师已有工作(WINE 2025 分布报告 / arXiv:2507.04030)
- ❌ 不签 18 月 / 多论文规划
- ❌ 不上生产
- ❌ 不跑实验(本 spec 只做"先公布后运行"的冻结环节)
- ❌ 不触碰 API key
- ❌ 不写 BOSS baseline 的具体算法实现(只占位骨架)

---

## 1. 目标与判死线

### 1.1 双视角目标(对外 + 内部,互补)

KT-B1 是一条**双跑**(dual-perspective)判死线,需要**两个独立指标**互证:

| 视角 | 指标 | 含义 | 阈值 |
|---|---|---|---|
| **对外**(v3 提案 §六 KT-B1) | 攻击成功率 | 合成操纵者改完后,deposon 守恒审计(T+R+A=1)能抓出的比例 | **≥ 50%** → "守恒即检测力"判死 / 退守复合协议分叉 ;**< 50%** → 升级为正面结果归档 |
| **内部**(Mavis P-B V0 spec §3-§4) | 失真上界 | deposon 三通道散射层相对 Bayesian 真实分布的失真度 | **≥ 0.95** → 失真上界达标(失真度 ≤ 0.05) |

**判死裁定矩阵**(双指标交叉):

| 攻击成功率(对外) | 失真上界(内部) | 裁定 | 解释 |
|---|---|---|---|
| ≥ 50% (PASS) | ≥ 0.95 (PASS) | **PASS_KT_B1** | 守恒审计 + 失真上界都达标,P-B 方向判活 |
| ≥ 50% (PASS) | < 0.95 (FAIL) | **GRAY_DOWN** | 守恒能抓攻击,但失真过大,降级为"工程可用但理论价值待审" |
| < 50% (FAIL) | ≥ 0.95 (PASS) | **GRAY_UP** | 失真小但守恒抓不出,升级为正面结果(失真界不依赖守恒检测力) |
| < 50% (FAIL) | < 0.95 (FAIL) | **FAIL_KT_B1** | 双双不达标,P-B 方向判死,撤 V3.X 整个 P-B 候选 |

### 1.2 判死线 SPEC 冻结(先于运行)

- v3 提案 KT-B1 对外判死线:**合成操纵者 n=200 次攻击下守恒审计成功率 ≥ 50% / < 50%**
- Mavis 内部 P-B V0 spec 判死线:**失真上界 ≥ 0.95(200 节点 v19 冻结管线)**
- **本 spec 冻结时点**: D0 末(Mavis 派 successor 算 5 锚 SHA-256 前 12 位)
- **运行启动时点**: D3 末(Mavis 实现攻击者 + 200 次攻击 harness)
- **裁定冻结时点**: D5 末(reviewer-b 独立 `/tmp` 副本审计 + 双指标交叉)
- **结论公布时点**: D7 末(一页摘要 + 锚定工件包 + 中文判死报告)

### 1.3 5 锚预登记占位(D1 由 successor 子代理算 SHA-256)

D1 由 successor 子代理计算,落到 `verifier/handoff/KT_B1_anchors_sha256_12.json`:

| 锚 ID | 对象 | 算法 | 字段 |
|---|---|---|---|
| `KT_B1_V19_BENCHMARK` | v19 冻结基准 JSON(200 道合成题守恒残差) | SHA-256 全文 → 前 12 位 | `physics_audit/t_plus_r_plus_a_max_deviation=2.2e-16` |
| `KT_B1_KILL_LINE` | KT-B1 判死裁定函数(双视角 4 档 PASS/GRAY/FAIL) | SHA-256 全文 → 前 12 位 | `kills={"PASS_KT_B1":true, "GRAY_DOWN":true, "GRAY_UP":true, "FAIL_KT_B1":true}` |
| `KT_B1_ATTACK_BANK` | 攻击脚本集(删锚/洗 manifest/改运行链 3 类 × 200 次) | SHA-256 全文 → 前 12 位 | `attacks={"deletion":200, "manifest_swap":200, "chain_modify":200}` |
| `KT_B1_AUDIT_FUNCTION` | 守恒审计函数 T+R+A=1 实现 | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |
| `KT_B1_HARNESS` | 200 次攻击 harness + BOSS baseline harness | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |

**任何 ≥ 1 锚漂移 → 全 KT-B1 撤回**(沿用 P-D V0 §2 5 锚铁律)。

### 1.4 王老师 D0 三问默认值(沿用 v3 提案)

1. 稳定化成本中烧掉的耗散,计入机制侧预算还是参与者效用? **默认:机制侧预算**(与 KT-A1 共用)
2. 攻击实验的"结论错误",按**终态标签翻转**还是评分阈值判? **默认:标签翻转**
3. 标度实验更关心审计强度参数还是环结构参数? **默认:环结构 d,仅影响表述**

三问不回复即按默认执行,判死线不依赖任何答复(沿用 v3 提案第六节三问默认值条款)。

---

## 2. 实验设计

### 2.1 数据集: v19 冻结 200 道合成题

- **数据源**: `deposon-project/results/deposon_v19_benchmark_fixes.json`(沿用 v3 提案附录 B 数字溯源表)
- **字段**: `physics_audit/t_plus_r_plus_a_max_deviation=2.2e-16`(浮点精度极限,v19 全部 200 题通过)
- **冻结状态**: v19 是 deposon 守恒审计的黄金基准,**本实验所有重跑必须基于 v19 冻结副本,不动 v19 本身**

### 2.2 攻击者: 合成操纵者 n=200

- **来源**: 沿用 deposon 现有 `v18_api_supplements` 中的合成操纵者构造器
- **规模**: 200 次独立攻击(每题 1 次,无重复攻击)
- **攻击类型**: 3 类(沿用 P-D V0 三类攻击,见 §2.3)
- **操纵目标**: 试图让守恒审计 T+R+A=1 不再成立(对 deposon 三通道之一做"账平但错"操作)
- **攻击者实现**: D2 由 data 子代理在 `.mavis/scripts/kt_b1/attacker.py` 实现(本 spec 不实现)

### 2.3 攻击类型(沿用 P-D V0 三类)

| 攻击 ID | 类型 | 描述 | 检测难度 |
|---|---|---|---|
| `deletion` | 删锚 | 删除 v19 冻结 JSON 中某道题的 audit 字段 | 低(裸 SHA-256 就能抓) |
| `manifest_swap` | 洗 manifest | 改 manifest 中任务元数据(题目描述/参数)但保留守恒残差字段 | 中(需 manifest 哈希链) |
| `chain_modify` | 改运行链 | 修改 v19 推理计算图的中间节点权重,但保持 T+R+A 数值 | 高(需验证器安全边界 + 推理图重算) |

每类攻击跑 200 次(n=200,对应 v19 200 道题),共 **3 × 200 = 600 次攻击**。主指标按总成功率算(对外判死线 ≥ 50%)。

### 2.4 检测器: deposon 守恒审计(T+R+A=1)

- **实现位置**: `verifier/audit/conservation.py`(沿用 P-D V0.1.1 验证器安全边界)
- **判定函数**: 算 T+R+A,若与 1 的偏差 > ε(ε = 1e-9,远大于浮点极限 2.2e-16)→ 报"检测到攻击"
- **检测粒度**: 逐路径审计(沿用 v19 200 题逐路径通过)
- **不依赖 LLM**: 纯数学审计,零 LLM API 调用

### 2.5 总 cell 与 harness 设计

| 模块 | 数量 | 备注 |
|---|---|---|
| 数据集 | 1(v19 冻结 200 题) | 不可变 |
| 攻击者 | 1(合成操纵者) | 沿用 v18_api_supplements 构造器 |
| 攻击类型 | 3(删锚/洗 manifest/改运行链) | 沿用 P-D V0 |
| 每类攻击次数 | 200 | 与数据集题数 1:1 对应 |
| 检测器 | 1(conservation audit) | 沿用 v19 |
| **总攻击次数** | **600**(3 × 200) | |
| **成功次数阈值** | **≥ 300 / 600 = 50%** | 对外判死线 |
| **失真上界** | **≥ 0.95** | 内部判死线 |

### 2.6 失真度计算(内部判死线)

- **基线**: Bayesian 真实分布(已知机制 + 支付 → 失真 = 0,沿用 P-B V0 spec §3.1)
- **实际分布**: deposon 守恒审计通过后的"报告分布"
- **失真度 D(M, T)**: 沿用 P-B V0 spec §3.4 公式
  ```
  D(M, T) = E_π[ Σ_t |u*(a_t) - u(a_t)| / max_u ]
  ```
- **失真上界**: 1 - 真实分布保真度(≥ 0.95 = 保真度 ≥ 95%)
- **内部判死线**: 失真上界 ≥ 0.95(失真度 ≤ 0.05)

### 2.7 沿用 P-B V0 spec 的 5 任务族(可选,扩展 cell)

如果双跑结果落在 GRAY 区(1.5 < 失真倍数 < 2.0 或攻击成功率 40-60%),Mavis 自主扩 cell:
- 沿用 P-B V0 spec §3.3 的 5 任务族(T1 GSM8K 算术 / T2 StrategyQA / T3 合成陷阱 / T4 自定义最小博弈 / T5 低资源博弈)
- 每族 20 题,共 100 题
- 跑 GRAY 扩 cell,重判死

---

## 3. 度量

### 3.1 主指标 1(对外,给王老师看)

```
attack_success_rate = successful_attacks / total_attacks
                     = detected_attacks / 600
```

- **判死线**: ≥ 0.50(600 次攻击中至少抓出 300 次)
- **失败模式**:
  - **PASS_KT_B1** (≥ 50%): "守恒即检测力"判死 / 退守复合协议分叉
  - **FAIL_KT_B1** (< 50%): 升级为正面结果归档(失真界不依赖守恒检测力)
- **95% bootstrap CI**: 10k resamples,计算攻击成功率的 Wilson 95% CI

### 3.2 主指标 2(内部,给 Mavis 团队看)

```
distortion_upper_bound = 1 - fidelity(M_real, M_deposon)
                       ≥ 0.95
```

- **判死线**: ≥ 0.95(对应失真度 ≤ 0.05)
- **失败模式**:
  - **PASS**: 失真度 ≤ 0.05,内部基线达标
  - **FAIL**: 失真度 > 0.05,需扩 cell 重判
- **95% bootstrap CI**: 10k resamples,跨 (M, T) 算 mean + CI

### 3.3 副指标

- **单攻击类型成功率**: 每类(删锚/洗 manifest/改运行链)单独算成功率
  - 预期: `deletion` 100% / `manifest_swap` 70-90% / `chain_modify` 30-60%
  - 若任一类 < 30% → 报"该攻击类型检测器盲点"
- **检测器 ROC-AUC**: 算检测器在所有 600 次攻击上的 ROC-AUC
  - 判死阈值: ROC-AUC ≥ 0.80(避免检测器"全抓全放"的对角线退化)
- **任务族特异**: 沿用 P-B V0 §4.2 副指标(每个 T 单独算 mean,识别最易/最难任务)
- **机制特异**: 沿用 P-B V0 §4.2 副指标(每个 M 单独算 mean)

### 3.4 攻击成功率 = 1 - 检测器召回率(重要!)

- 攻击者"成功"= 操纵后通过守恒审计(没被检测出来)
- 因此:**攻击成功率 = 1 - 检测器召回率**
- 攻击成功率 ≥ 50% ⇔ 检测器召回率 < 50% ⇔ 守恒审计"抓不出多数攻击"
- **反直觉**: 对外 v3 提案 KT-B1 的判死线 ≥ 50% 是"攻击者通过率",不是"检测器成功率"
- **重要性**: D5 reviewer-b 报告必须显式标注此反转,避免王老师读数时混淆

### 3.5 95% bootstrap CI 协议

```python
def bootstrap_ci(samples, n_resamples=10000, ci=0.95):
    """
    Standard 10k resamples Wilson bootstrap CI.
    Returns (mean, ci_lo, ci_hi).
    """
    n = len(samples)
    means = []
    rng = np.random.default_rng(seed=42)
    for _ in range(n_resamples):
        boot = rng.choice(samples, size=n, replace=True)
        means.append(np.mean(boot))
    means.sort()
    lo = means[int(0.025 * n_resamples)]
    hi = means[int(0.975 * n_resamples)]
    return (np.mean(samples), lo, hi)
```

- 沿用 P-B V0 spec §4.1 的 10k resamples 协议
- seed=42 锁定(可复现)

---

## 4. BOSS 测法(防 V1 撞六关键词规则重演)

### 4.0 §0.5 已知陷阱(沿用 P-D V0 §0.5 + V1 六关键词规则教训)

**V1 撞过的 BOSS**(沿用 `QUICK_KILL_6_DIRECTIONS.md` 文档头):
- **六关键词规则过滤器** (six-keyword rule filter) 在 GSM8K / StrategyQA 上与 deposon 散射层 accuracy 不可区分(0.87 vs 0.85, 0.899 = 0.899)
- 后果: 论文 V1 §2.4 把"散射层筛选性能优于平凡基线"主张降级为 0
- 教训: **任何"deposon 比某基线好"的主张都必须先测平凡基线**,KT-B1 不例外

**KT-B1 必须主动测的 BOSS**(防 V1 重演):
- 平凡基线(Sinkhorn OT / KD / LLMLingua)若能在 200 节点 v19 上达到守恒审计同样检测率 → deposon 守恒检测力无差异化
- 本 §4 给 BOSS 测法的占位骨架,具体实现在 D2-D4

### 4.1 BOSS-B1: Sinkhorn OT 测法(失真度可被拍平)

**测法**: 同样 200 节点 v19 数据,直接跑 Sinkhorn Optimal Transport(Cuturi 2013),看失真上界是否也 ≥ 0.95。

- **如果 Sinkhorn OT 失真上界 ≥ 0.95**: 失真上界不特殊(通用 OT 类方法的默认下限)
- **deposon 应对**: 失真上界主张降级为"通用 OT 工具的下限",不强调"deposon 独有"
- **占位脚本**: `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py`
- **参考**: Cuturi 2013, "Sinkhorn Distances: Lightspeed Computation of Optimal Transport", NeurIPS

### 4.2 BOSS-B2: Knowledge Distillation 测法

**测法**: 用 Hinton 2015 KD 框架 + KL 散度 + softmax 平滑,在 200 节点上做 baseline,看 0.95 是否是默认下限。

- **如果 KD 失真上界 ≥ 0.95**: deposon 失真上界无差异化(0.95 是 KD 工具的默认下限)
- **deposon 应对**: 主张"deposon 物理守恒 = 优于 KD 的可审计保证"需另外论证(KD 不能保证审计)
- **占位脚本**: `.mavis/scripts/kt_b1/boss_b2_kd.py`
- **参考**: Hinton et al. 2015, "Distilling the Knowledge in a Neural Network", NeurIPS Deep Learning Workshop

### 4.3 BOSS-B3: LLMLingua 提示词压缩测法

**测法**: 用 Microsoft 2023 LLMLingua 压缩 prompt 到同样保留率,看失真是否 < 0.05。

- **如果 LLMLingua 失真 < 0.05**: 主张被拍平(200 节点上 0.95 是教科书水平)
- **deposon 应对**: 主张降级为"deposon 在 200 节点上的失真界 = 通用提示词压缩的下限"
- **占位脚本**: `.mavis/scripts/kt_b1/boss_b3_llmlingua.py`
- **参考**: LLMLingua (Microsoft 2023) / LLMLingua-2 论文

### 4.4 4 条禁示条款(沿用 D0 准备 §4)

1. **不得在真实仓库跑 BOSS baseline**(必须 `/tmp/deposon_kt_b1_audit_<timestamp>/` 副本)
2. **不得让 BOSS baseline 脚本诱导操作者删除冻结锚**
3. **不得在 BOSS 测法跑通前宣称 KT-B1 方向 PASS**
4. **不得跳过 BOSS 测法只跑主实验**(防 V1 撞 BOSS 重演)

### 4.5 BOSS 测法回写(沿用 QUICK_KILL V0.2 §"下次升级触发")

D7 末,KT-B1 判死 PASS/FAIL 后,无论是否撞 BOSS,必须把"实测记录"回写到 `QUICK_KILL_6_DIRECTIONS.md` V0.3:
- BOSS-B1/B2/B3 任一撞上 → 写入"已撞 BOSS,失真上界主张降级"
- 全部未撞 → 写入"deposon 失真上界在通用 OT/KD/LLMLingua 工具下仍差异化"

---

## 5. 抗攻击检查(沿用 P-B V0 spec §5)

### 5.1 A1: 攻击者提示词扰动

- **做法**: 攻击者提示词扰动 3 次(改 1-2 关键词 + 改顺序 + 加噪声)
- **判定**: 看攻击成功率 > 50% 是否变化超过 ± 10% → 报"不稳定"
- **预期**: 攻击成功率 ± 5% 内波动(稳健)

### 5.2 A2: 攻击强度扫描

- **做法**: 攻击强度分 3 档(0.1 / 0.5 / 1.0)
  - 0.1: 轻度扰动(只改 1 个字段)
  - 0.5: 中度扰动(改 3-5 个字段)
  - 1.0: 全强度(改 ≥ 10 个字段)
- **判定**: 看攻击成功率是否单调(0.1 < 0.5 < 1.0)→ 单调性破坏报"强度无差异"
- **预期**: 单调递增(攻击强度越大,成功率越高)

### 5.3 A3: 种子复现

- **做法**: seed = 42 / 123 / 456 三套
- **判定**: 看 std/mean > 0.2 → 报"种子敏感"
- **预期**: std/mean < 0.1(种子稳健)

### 5.4 抗攻击通过条件

- A1 / A2 / A3 全部通过 → 攻击实验可信
- 任一不通过 → 重审实现,Mavis 派 reviewer-b 复审

---

## 6. 5 锚预登记(沿用 §1.3 表格,D1 由 successor 算 SHA-256)

| 锚 ID | 对象 | 算法 | 字段 | SHA-256 前 12 位 |
|---|---|---|---|---|
| `KT_B1_V19_BENCHMARK` | v19 冻结 200 题守恒残差 JSON | SHA-256 全文 | `t_plus_r_plus_a_max_deviation=2.2e-16` | D1 successor 算 |
| `KT_B1_KILL_LINE` | KT-B1 判死裁定函数(双视角 4 档) | SHA-256 全文 | `kills={PASS_KT_B1, GRAY_DOWN, GRAY_UP, FAIL_KT_B1}` | D1 successor 算 |
| `KT_B1_ATTACK_BANK` | 攻击脚本集(3 类 × 200 次) | SHA-256 全文 | `attacks={deletion:200, manifest_swap:200, chain_modify:200}` | D1 successor 算 |
| `KT_B1_AUDIT_FUNCTION` | 守恒审计函数 T+R+A=1 | SHA-256 全文 | `version=2026-09-11` | D1 successor 算 |
| `KT_B1_HARNESS` | 200 次攻击 harness + BOSS baseline harness | SHA-256 全文 | `version=2026-09-11` | D1 successor 算 |

5 锚 SHA-256 前 12 位必须先于 D3 末运行公布,公布后任何 ≥ 1 锚漂移 → 全 KT-B1 撤回。

---

## 7. 复现协议(reviewer-b 独立 /tmp 副本审计)

### 7.1 复现步骤

1. **复制仓库到 `/tmp/deposon_kt_b1_audit_<timestamp>/`**(timestamp 格式 `YYYYMMDD_HHMMSS`)
2. **读 `verifier/handoff/KT_B1_anchors_sha256_12.json` 验 5 锚**
3. **选 50 次攻击**(从 600 次中随机抽 50,固定 seed=42)重跑,验攻击成功率 ± 5% 内
4. **验失真上界 ± 5% 内**
5. **跑 3 个 BOSS baseline**(BOSS-B1 Sinkhorn / BOSS-B2 KD / BOSS-B3 LLMLingua),记录各自失真上界

### 7.2 通过条件

- 5 锚 SHA-256 前 12 位全部一致
- 攻击成功率 ± 5% 内
- 失真上界 ± 5% 内
- 3 个 BOSS baseline 全部跑通(不要求 deposon 优于 BOSS,只要求 BOSS 测法本身可跑通)

### 7.3 失败处理

- 任意一项超差 → 撤回整 KT-B1
- 5 锚漂移 ≥ 1 → 全 V0 撤回
- reviewer-b 报告独立成 1-2 页审计报告,落 `verifier/audits/KT_B1_audit_<timestamp>.md`

---

## 8. 交付

### 8.1 D1 交付: SPEC 冻结

- Mavis 改 Mavis 内部 P-B V0 spec,在 §1 加 BOSS 测法节(沿用本 spec §4)
- Mavis 派 successor 算 5 锚 SHA-256 前 12 位,落 `verifier/handoff/KT_B1_anchors_sha256_12.json`
- 本 spec 公布 SHA-256 后冻结

### 8.2 D5 交付: 内部判死报告 1-2 页

- 路径: `docs/V3X/KT_B1_D5_REPORT_2026_09_09_mavis.md`
- 内容: 攻击成功率(对外) + 失真上界(内部) + 95% CI + 判死裁定 + BOSS baseline 结果
- 双视角 4 档裁定表(PASS_KT_B1 / GRAY_DOWN / GRAY_UP / FAIL_KT_B1)

### 8.3 D7 交付: 一页摘要(对外,微信友好) + 完整中文判死报告(内部,备查)

- **一页摘要**: `docs/V3X/D7_KT_B1_ONE_PAGE.md`
  - 3 行内容: KT-B1 双指标 + 4 档裁定 + BOSS 测法结论
  - 微信可直接转发
- **完整中文判死报告**: `docs/V3X/KT_B1_PAPER_zh.md`
  - 10-15 页,含 5 锚溯源 + 全部 600 次攻击明细 + BOSS 测法对照
- **锚定工件包**: `results/v3x_kt_b1/`
  - v19 冻结副本(只读)
  - 5 锚 SHA-256 JSON
  - 600 次攻击原始日志
  - 3 个 BOSS baseline 跑分 JSON
  - reviewer-b 审计报告

### 8.4 全程归档(沿用 P-B V0 spec §7)

- 所有脚本落 `.mavis/scripts/kt_b1/`
- 所有 handoff 锚点落 `verifier/handoff/`
- 所有复跑日志落 `results/v3x_kt_b1/`

---

## 9. 失败模式(与王老师 WeChat 同步)

### 9.1 5 锚漂移

- **触发**: 任意 ≥ 1 锚 SHA-256 前 12 位与 D1 公布值不一致
- **处理**: 全 KT-B1 撤回,重审 spec
- **通知**: WeChat 给王老师 + Mavis 群内同步
- **D7 影响**: 推迟 1-2 天交付

### 9.2 判死裁定(4 档)

| 档位 | 触发条件 | 主张降级 | WeChat 通知 |
|---|---|---|---|
| **PASS_KT_B1** | 攻击成功率 ≥ 50% 且 失真上界 ≥ 0.95 | 不降级,P-B 判活 | 一行: KT-B1 PASS |
| **GRAY_DOWN** | 攻击成功率 ≥ 50% 且 失真上界 < 0.95 | 失真过大,降级为"工程可用" | 一行: KT-B1 GRAY_DOWN |
| **GRAY_UP** | 攻击成功率 < 50% 且 失真上界 ≥ 0.95 | 失真小但守恒检测力不足,升级为"失真界不依赖守恒" | 一行: KT-B1 GRAY_UP |
| **FAIL_KT_B1** | 攻击成功率 < 50% 且 失真上界 < 0.95 | P-B 方向判死,撤 V3.X 整个 P-B 候选 | 一行: KT-B1 FAIL,撤 P-B 候选 |

### 9.3 BOSS 测法撞上(BOSS-B1/B2/B3 任一)

- **触发**: 失真上界 ≥ 0.95 但 Sinkhorn OT / KD / LLMLingua 也 ≥ 0.95
- **处理**: 失真上界主张降级为"通用 OT/KD 工具的下限",不强调"deposon 独有"
- **回写**: D7 末回写 `QUICK_KILL_6_DIRECTIONS.md` V0.3
- **WeChat 通知**: 通知王老师"撞 BOSS,主张降级"

### 9.4 抗攻击检查不通过(A1/A2/A3 任一)

- **触发**: 攻击者提示词扰动 > ±10% / 攻击强度无单调性 / 种子 std/mean > 0.2
- **处理**: 重审实现,Mavis 派 reviewer-b 复审
- **王老师**: 仅 ack,是否撤回由 Mavis 自主决定

### 9.5 D1 阻塞(理论界未给)

- 沿用 P-B V0 spec §8: 内部判死线(失真上界)需要 P-B V0 §3.5 理论界公式(L(M, T) / U(M, T))
- **触发**: 王老师 D1 WeChat 未给 1-page theory
- **处理**: 整 KT-B1 内部判死线阻塞,只跑对外判死线(攻击成功率)
- **后果**: D7 交付只有"对外 1 页",内部失真上界延迟到 D1 理论输入后补

---

## 10. 时间线(D0-D7)

| Day | 任务 | 派给 | 输出 |
|---|---|---|---|
| **D0** | 锚点预登记 + §0.5 BOSS 测法节冻结 | Mavis + worker-b | 本 spec 公布 + 5 锚占位(等 successor 算 SHA-256) |
| **D1** | Mavis 改 Mavis 内部 P-B V0 spec 加 BOSS 测法节 + successor 算 5 锚 SHA-256 | Mavis + successor | P-B V0 spec V0.1 + `verifier/handoff/KT_B1_anchors_sha256_12.json` |
| **D2** | 实现攻击者 + 200 次攻击 harness + BOSS-B1 Sinkhorn OT baseline 占位 | data | `.mavis/scripts/kt_b1/attacker.py` + harness + `boss_b1_sinkhorn_ot.py` |
| **D3** | pilot 50 次攻击 + BOSS-B1 baseline 跑通 + WeChat 中期简报 | data + Mavis | pilot 报告 + WeChat 三行判死状态 |
| **D4** | 全 200 次攻击 × 3 类 = 600 次 + BOSS-B2 KD + BOSS-B3 LLMLingua 跑通 | data | 600 次攻击原始日志 + 2 个 BOSS baseline 跑分 |
| **D5** | reviewer-b 判死 + 3 攻击 + BOSS-B1/B2/B3 测法 + P-B 判死裁定对照 | reviewer-b + data | D5 内部判死报告 1-2 页 + 4 档裁定表 |
| **D6** | 失败模式处理 / GRAY 扩 cell(若需要) | Mavis + v3x | GRAY 扩 cell 报告(若需要) |
| **D7** | 中文短稿 + 一页摘要 + 全 handoff 归档 + BOSS 测法结果回写 QUICK_KILL V0.3 | paper-cn + successor | D7 一页摘要 + 锚定工件包 + `QUICK_KILL_6_DIRECTIONS.md` V0.3 |

### 10.1 关键节点

- **D0 末**: 本 spec 公布 + 5 锚占位(冻结 SPEC 不依赖运行)
- **D3 末**: WeChat 中期简报(王老师三行判死状态)
- **D5 末**: 4 档判死裁定 + BOSS 测法结果(双视角双跑结论)
- **D7 末**: 完整交付 + 锚定工件包 + BOSS 回写

### 10.2 硬截止

- D7 硬截止,最多宽限 1-2 天(沿用 v3 提案第七节风险缓解)
- 延误在 D3 中期简报中提前报

---

## 附录 A · 与 v3 提案 KT-B1 行的对齐

v3 提案第六节 KT-B1 行原文:
> "合成操纵者 n=200 次攻击下的守恒审计:成功率 ≥50% →「守恒即检测力」判死、退守复合协议分叉;<50% → 升级为正面结果归档。D3 冻结 SPEC,D5 跑。两个结局都是判死级交付(账平能否抓住操纵者)。"

本 spec 对齐:
- ✅ 合成操纵者 n=200 次攻击(本 spec §2.2)
- ✅ 守恒审计 T+R+A=1(本 spec §2.4)
- ✅ 成功率 ≥50% / <50% 二档(本 spec §1.1,扩展为双视角 4 档)
- ✅ D3 冻结 SPEC,D5 跑(本 spec §10)
- ✅ 两个结局都是判死级交付(本 spec §9.2)

**关键差异**: 本 spec 增加了 Mavis 内部 P-B V0 spec 的失真上界判死线(双跑设计),对外不破坏 v3 提案承诺,内部多 1 个互补指标。

---

## 附录 B · 数字溯源表

| 数字 | 字段路径 |
|---|---|
| 200 道合成题 | `results/deposon_v19_benchmark_fixes.json` : n_questions |
| 守恒审计最大残差 2.2e-16 | 同上 : `physics_audit/t_plus_r_plus_a_max_deviation` |
| v18_api_supplements 攻击者构造器 | `deposon-project/v18_api_supplements/`(复用) |
| 3 类攻击(删锚/洗 manifest/改运行链) | 沿用 P-D V0 §3.2 攻击类型 |
| 95% bootstrap CI 10k resamples | 沿用 P-B V0 §4.1 |
| seed=42 / 123 / 456 | 沿用 P-B V0 §5 A3 |
| 攻击成功率 ≥ 50% | v3 提案第六节 KT-B1 行 |
| 失真上界 ≥ 0.95 | P-B V0 spec §3.3 失真度量 + Mavis 内部判死线 |

---

## 附录 C · 5 锚 SHA-256 计算协议(D1 successor 执行)

```python
import hashlib
import json
from pathlib import Path

ANCHORS = {
    "KT_B1_V19_BENCHMARK": "results/deposon_v19_benchmark_fixes.json",
    "KT_B1_KILL_LINE": "verifier/kill_lines/kt_b1_kill_decision.py",
    "KT_B1_ATTACK_BANK": ".mavis/scripts/kt_b1/attacker.py",
    "KT_B1_AUDIT_FUNCTION": "verifier/audit/conservation.py",
    "KT_B1_HARNESS": ".mavis/scripts/kt_b1/harness.py",
}

out = {}
for anchor_id, path in ANCHORS.items():
    content = Path(path).read_bytes()
    sha = hashlib.sha256(content).hexdigest()[:12]
    out[anchor_id] = {"path": path, "sha256_12": sha}

Path("verifier/handoff/KT_B1_anchors_sha256_12.json").write_text(
    json.dumps(out, indent=2, ensure_ascii=False)
)
```

- 5 锚 SHA-256 前 12 位在 D1 末计算并公布
- 公布后任何 ≥ 1 锚漂移 → 全 KT-B1 撤回

---

## 附录 D · BOSS baseline 占位脚本索引(3 个,本仓库)

- `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py`(Sinkhorn OT baseline 占位)
- `.mavis/scripts/kt_b1/boss_b2_kd.py`(Knowledge Distillation baseline 占位)
- `.mavis/scripts/kt_b1/boss_b3_llmlingua.py`(LLMLingua baseline 占位)

**注意**: 本 spec 不实现 BOSS baseline 具体算法,只占位骨架(防 V1 六关键词规则重演)。D2-D4 由 data 子代理实现。

---

**KT-B1 SPEC V0 草稿结束,等待 D1 successor 算 5 锚 SHA-256 前 12 位冻结。**
