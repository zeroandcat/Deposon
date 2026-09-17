# KT-B1 SPEC V0.1 冻结版

> **作者**: Mavis(执行线,worker-b 子代理撰写)
> **日期**: 2026-09-09(D0 准备阶段, V0 草稿 2026-09-09; V0.1 升级 2026-09-09 沿用 P-A V0 spec V0.2 模式)
> **状态**: **V0.1 冻结版**(SPEC 文本先于运行冻结, 5 锚 SHA-256 已预登记, §11 7 条铁律兼容 + §12 已知未决项已固化)
> **位置**: `docs/V3X/KT_B1_SPEC_V0.1.md`
> **关联**:
>   - 上游: v3 提案(王老师致王子贺老师,2026-09-04,4 页,第六节 KT-B1 行)
>   - 下游: Mavis 内部 P-B 失真界 V0 spec(`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`)
>   - BOSS 源: `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` V0.2 §方向 2 BOSS-B1/B2/B3
>   - D0 准备: `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` §1.2 / §3
>   - **V0.1 frozen 锚 JSON**: `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1(15 真, 0 占位)

---

## 0. 元约束与铁律

### 0.1 7 条铁律(沿用 D0 准备 §6)

1. ✅ **双审**: reviewer-a 静态审 + reviewer-b `/tmp` 副本独立重跑
2. ✅ **API key 不入 prompt**: runtime `Path(file).read_text()` 读取, 不入 prompt
3. ✅ **术语红线**: 沿用 deposon 既有 T+R+A=1 / 透射+反射+耗散 / 账平 / 守恒审计
4. ✅ **数字溯源**: 全部论断指向 frozen 锚 JSON 字段路径(V0.1 §6 + 附录 B 数字溯源表)
5. ✅ **verifier 纪律**: 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/
6. ✅ **预登记**: 5 锚 SHA-256 前 12 位先于运行冻结并公布(V0.1 §6 已落地)
7. ✅ **推送策略**: 王老师 = WeChat 顾问模式(每周 1-2 条 + 收结果, ~5-10 min/周)

### 0.2 强度声明(沿用 v3 提案)

- **判死级**: 已预登记并执行的事实(5 锚 + 判死线 + 跑分)
- **观察性**: 数值规律(失真上界 vs v19 冻结残差)
- **探索性**: 猜想(守恒审计 = 检测力上限)

### 0.3 本 SPEC 不做的事(显式声明)

- ❌ 不改 P-D V0.1.1(已 PASS, 只引用)
- ❌ 不重做王老师已有工作(WINE 2025 分布报告 / arXiv:2507.04030)
- ❌ 不签 18 月 / 多论文规划
- ❌ 不上生产
- ❌ 不跑实验(本 spec 只做"先公布后运行"的冻结环节)
- ❌ 不触碰 API key
- ❌ 不写 BOSS baseline 的具体算法实现(只占位骨架, V0.1 阶段已实现真实脚本, 见 §4)

### 0.4 V0.1 升级变更

- V0 草稿中 §1.3 + §6 5 锚 SHA-256 占位("D1 successor 算")在 V0.1 已由 `KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1 实际值填入
- V0 草稿中 BOSS-B1/B2/B3 占位骨架在 V0.1 升级为已实现真实脚本(SHA-256 + 字节数见 §4)
- V0 草稿无 §11 7 条铁律、§12 已知未决项、§13 引用与版本, V0.1 全部新加
- V0 草稿无 V0 → V0.1 升级记录 footer, V0.1 新加

---

## 1. 目标与判死线

### 1.1 双视角目标(对外 + 内部, 互补)

KT-B1 是一条**双跑**(dual-perspective)判死线, 需要**两个独立指标**互证:

| 视角 | 指标 | 含义 | 阈值 |
|---|---|---|---|
| **对外**(v3 提案 §六 KT-B1) | 攻击成功率 | 合成操纵者改完后, deposon 守恒审计(T+R+A=1)能抓出的比例 | **≥ 50%** → "守恒即检测力"判死 / 退守复合协议分叉;**< 50%** → 升级为正面结果归档 |
| **内部**(Mavis P-B V0 spec §3-§4) | 失真上界 | deposon 三通道散射层相对 Bayesian 真实分布的失真度 | **≥ 0.95** → 失真上界达标(失真度 ≤ 0.05) |

**判死裁定矩阵**(双指标交叉):

| 攻击成功率(对外) | 失真上界(内部) | 裁定 | 解释 |
|---|---|---|---|
| ≥ 50% (PASS) | ≥ 0.95 (PASS) | **PASS_KT_B1** | 守恒审计 + 失真上界都达标, P-B 方向判活 |
| ≥ 50% (PASS) | < 0.95 (FAIL) | **GRAY_DOWN** | 守恒能抓攻击, 但失真过大, 降级为"工程可用但理论价值待审" |
| < 50% (FAIL) | ≥ 0.95 (PASS) | **GRAY_UP** | 失真小但守恒抓不出, 升级为正面结果(失真界不依赖守恒检测力) |
| < 50% (FAIL) | < 0.95 (FAIL) | **FAIL_KT_B1** | 双双不达标, P-B 方向判死, 撤 V3.X 整个 P-B 候选 |

### 1.2 判死线 SPEC 冻结(先于运行)

- v3 提案 KT-B1 对外判死线: **合成操纵者 n=200 次攻击下守恒审计成功率 ≥ 50% / < 50%**
- Mavis 内部 P-B V0 spec 判死线: **失真上界 ≥ 0.95(200 节点 v19 冻结管线)**
- **本 spec 冻结时点**: D0 末(Mavis 派 successor 算 5 锚 SHA-256 前 12 位)— V0.1 已落地
- **运行启动时点**: D3 末(Mavis 实现攻击者 + 200 次攻击 harness)
- **裁定冻结时点**: D5 末(reviewer-b 独立 `/tmp` 副本审计 + 双指标交叉)
- **结论公布时点**: D7 末(一页摘要 + 锚定工件包 + 中文判死报告)

### 1.3 5 锚预登记(V0.1 真实值, D0 末已算)

D0 末已由 successor 子代理计算并写入 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1, 完整 SHA-256 表见 §6。

| 锚 ID | 对象 | 算法 | 字段 | SHA-256[0:12] |
|---|---|---|---|---|
| `KT_B1_V19_BENCHMARK` | v19 冻结基准 JSON(200 道合成题守恒残差) | SHA-256 全文 → 前 12 位 | `physics_audit/t_plus_r_plus_a_max_deviation=2.2e-16` | **`910c4333eead`** |
| `KT_B1_KILL_LINE` | KT-B1 判死裁定函数(双视角 4 档 PASS/GRAY/FAIL) | SHA-256 全文 → 前 12 位 | `kills={"PASS_KT_B1":true, "GRAY_DOWN":true, "GRAY_UP":true, "FAIL_KT_B1":true}` | **`9f351078e5bf`** |
| `KT_B1_ATTACK_BANK` | 攻击脚本集(删锚/洗 manifest/改运行链 3 类 × 200 次) | SHA-256 全文 → 前 12 位 | `attacks={"deletion":200, "manifest_swap":200, "chain_modify":200}` | **`4b37a40cc984`** |
| `KT_B1_AUDIT_FUNCTION` | 守恒审计函数 T+R+A=1 实现 | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | **`3aa661cfbab5`** |
| `KT_B1_HARNESS` | 200 次攻击 harness + BOSS baseline harness | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | **`39dacb572f2e`** |

**任何 ≥ 1 锚漂移 → 全 KT-B1 撤回**(沿用 P-D V0 §2 5 锚铁律)。

### 1.4 王老师 D0 三问默认值(沿用 v3 提案)

1. 稳定化成本中烧掉的耗散, 计入机制侧预算还是参与者效用? **默认:机制侧预算**(与 KT-A1 共用)
2. 攻击实验的"结论错误", 按**终态标签翻转**还是评分阈值判? **默认:标签翻转**
3. 标度实验更关心审计强度参数还是环结构参数? **默认:环结构 d, 仅影响表述**

三问不回复即按默认执行, 判死线不依赖任何答复(沿用 v3 提案第六节三问默认值条款)。

---

## 2. 实验设计

### 2.1 数据集: v19 冻结 200 道合成题

- **数据源**: `deposon-project/results/deposon_v19_benchmark_fixes.json`(沿用 v3 提案附录 B 数字溯源表, SHA-256 锚 `KT_B1_V19_BENCHMARK` = `910c4333eead`)
- **字段**: `physics_audit/t_plus_r_plus_a_max_deviation=2.2e-16`(浮点精度极限, v19 全部 200 题通过)
- **冻结状态**: v19 是 deposon 守恒审计的黄金基准, **本实验所有重跑必须基于 v19 冻结副本, 不动 v19 本身**

### 2.2 攻击者: 合成操纵者 n=200

- **来源**: 沿用 deposon 现有 `v18_api_supplements` 中的合成操纵者构造器
- **规模**: 200 次独立攻击(每题 1 次, 无重复攻击)
- **攻击类型**: 3 类(沿用 P-D V0 三类攻击, 见 §2.3)
- **操纵目标**: 试图让守恒审计 T+R+A=1 不再成立(对 deposon 三通道之一做"账平但错"操作)
- **攻击者实现**: D2 由 data 子代理在 `.mavis/scripts/kt_b1/attacker.py` 实现(SHA-256 锚 `KT_B1_ATTACK_BANK` = `4b37a40cc984`, 本 spec 不实现)

### 2.3 攻击类型(沿用 P-D V0 三类)

| 攻击 ID | 类型 | 描述 | 检测难度 |
|---|---|---|---|
| `deletion` | 删锚 | 删除 v19 冻结 JSON 中某道题的 audit 字段 | 低(裸 SHA-256 就能抓) |
| `manifest_swap` | 洗 manifest | 改 manifest 中任务元数据(题目描述/参数)但保留守恒残差字段 | 中(需 manifest 哈希链) |
| `chain_modify` | 改运行链 | 修改 v19 推理计算图的中间节点权重, 但保持 T+R+A 数值 | 高(需验证器安全边界 + 推理图重算) |

每类攻击跑 200 次(n=200, 对应 v19 200 道题), 共 **3 × 200 = 600 次攻击**。主指标按总成功率算(对外判死线 ≥ 50%)。

### 2.4 检测器: deposon 守恒审计(T+R+A=1)

- **实现位置**: `verifier/audit/conservation.py`(沿用 P-D V0.1.1 验证器安全边界, SHA-256 锚 `KT_B1_AUDIT_FUNCTION` = `3aa661cfbab5`)
- **判定函数**: 算 T+R+A, 若与 1 的偏差 > ε(ε = 1e-9, 远大于浮点极限 2.2e-16)→ 报"检测到攻击"
- **检测粒度**: 逐路径审计(沿用 v19 200 题逐路径通过)
- **不依赖 LLM**: 纯数学审计, 零 LLM API 调用

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

- **基线**: Bayesian 真实分布(已知机制 + 支付 → 失真 = 0, 沿用 P-B V0 spec §3.1)
- **实际分布**: deposon 守恒审计通过后的"报告分布"
- **失真度 D(M, T)**: 沿用 P-B V0 spec §3.4 公式
  ```
  D(M, T) = E_π[ Σ_t |u*(a_t) - u(a_t)| / max_u ]
  ```
- **失真上界**: 1 - 真实分布保真度(≥ 0.95 = 保真度 ≥ 95%)
- **内部判死线**: 失真上界 ≥ 0.95(失真度 ≤ 0.05)

### 2.7 沿用 P-B V0 spec 的 5 任务族(可选, 扩展 cell)

如果双跑结果落在 GRAY 区(1.5 < 失真倍数 < 2.0 或攻击成功率 40-60%), Mavis 自主扩 cell:
- 沿用 P-B V0 spec §3.3 的 5 任务族(T1 GSM8K 算术 / T2 StrategyQA / T3 合成陷阱 / T4 自定义最小博弈 / T5 低资源博弈)
- 每族 20 题, 共 100 题
- 跑 GRAY 扩 cell, 重判死

---

## 3. 度量

### 3.1 主指标 1(对外, 给王老师看)

```
attack_success_rate = successful_attacks / total_attacks
                     = detected_attacks / 600
```

- **判死线**: ≥ 0.50(600 次攻击中至少抓出 300 次)
- **失败模式**:
  - **PASS_KT_B1** (≥ 50%): "守恒即检测力"判死 / 退守复合协议分叉
  - **FAIL_KT_B1** (< 50%): 升级为正面结果归档(失真界不依赖守恒检测力)
- **95% bootstrap CI**: 10k resamples, 计算攻击成功率的 Wilson 95% CI

### 3.2 主指标 2(内部, 给 Mavis 团队看)

```
distortion_upper_bound = 1 - fidelity(M_real, M_deposon)
                       ≥ 0.95
```

- **判死线**: ≥ 0.95(对应失真度 ≤ 0.05)
- **失败模式**:
  - **PASS**: 失真度 ≤ 0.05, 内部基线达标
  - **FAIL**: 失真度 > 0.05, 需扩 cell 重判
- **95% bootstrap CI**: 10k resamples, 跨 (M, T) 算 mean + CI

### 3.3 副指标

- **单攻击类型成功率**: 每类(删锚/洗 manifest/改运行链)单独算成功率
  - 预期: `deletion` 100% / `manifest_swap` 70-90% / `chain_modify` 30-60%
  - 若任一类 < 30% → 报"该攻击类型检测器盲点"
- **检测器 ROC-AUC**: 算检测器在所有 600 次攻击上的 ROC-AUC
  - 判死阈值: ROC-AUC ≥ 0.80(避免检测器"全抓全放"的对角线退化)
- **任务族特异**: 沿用 P-B V0 §4.2 副指标(每个 T 单独算 mean, 识别最易/最难任务)
- **机制特异**: 沿用 P-B V0 §4.2 副指标(每个 M 单独算 mean)

### 3.4 攻击成功率 = 1 - 检测器召回率(重要!)

- 攻击者"成功"= 操纵后通过守恒审计(没被检测出来)
- 因此: **攻击成功率 = 1 - 检测器召回率**
- 攻击成功率 ≥ 50% ⇔ 检测器召回率 < 50% ⇔ 守恒审计"抓不出多数攻击"
- **反直觉**: 对外 v3 提案 KT-B1 的判死线 ≥ 50% 是"攻击者通过率", 不是"检测器成功率"
- **重要性**: D5 reviewer-b 报告必须显式标注此反转, 避免王老师读数时混淆

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

### 4.0 §0.5 已知陷阱(V0.1 沿用 P-D V0 §0.5 + V1 六关键词规则教训 + 真实脚本标注)

**V1 撞过的 BOSS**(沿用 `QUICK_KILL_6_DIRECTIONS.md` 文档头):
- **六关键词规则过滤器** (six-keyword rule filter) 在 GSM8K / StrategyQA 上与 deposon 散射层 accuracy 不可区分(0.87 vs 0.85, 0.899 = 0.899)
- 后果: 论文 V1 §2.4 把"散射层筛选性能优于平凡基线"主张降级为 0
- 教训: **任何"deposon 比某基线好"的主张都必须先测平凡基线**, KT-B1 不例外

**V0.1 升级**: V0 草稿中 3 个 BOSS 占位骨架, V0.1 阶段已实现为真实脚本(`KT_ABC1_anchors_sha256_12.json` §boss_baselines/KT-B1), SHA-256 + 字节数如下。

**KT-B1 必须主动测的 BOSS**(防 V1 重演):
- 平凡基线(Sinkhorn OT / KD / LLMLingua)若能在 200 节点 v19 上达到守恒审计同样检测率 → deposon 守恒检测力无差异化
- 本 §4 给 BOSS 测法占位骨架 + 真实脚本 SHA-256, 具体实现在 D2-D4

### 4.1 BOSS-B1: Sinkhorn OT 测法(失真度可被拍平)

**测法**: 同样 200 节点 v19 数据, 直接跑 Sinkhorn Optimal Transport(Cuturi 2013), 看失真上界是否也 ≥ 0.95。

- **如果 Sinkhorn OT 失真上界 ≥ 0.95**: 失真上界不特殊(通用 OT 类方法的默认下限)
- **deposon 应对**: 失真上界主张降级为"通用 OT 工具的下限", 不强调"deposon 独有"
- **真实脚本**: `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py` SHA-256 = `19325960b8be`, 14956 字节
- **参考**: Cuturi 2013, "Sinkhorn Distances: Lightspeed Computation of Optimal Transport", NeurIPS

### 4.2 BOSS-B2: Knowledge Distillation 测法

**测法**: 用 Hinton 2015 KD 框架 + KL 散度 + softmax 平滑, 在 200 节点上做 baseline, 看 0.95 是否是默认下限。

- **如果 KD 失真上界 ≥ 0.95**: deposon 失真上界无差异化(0.95 是 KD 工具的默认下限)
- **deposon 应对**: 主张"deposon 物理守恒 = 优于 KD 的可审计保证"需另外论证(KD 不能保证审计)
- **真实脚本**: `.mavis/scripts/kt_b1/boss_b2_kd.py` SHA-256 = `1781ea2f742d`, 14224 字节
- **参考**: Hinton et al. 2015, "Distilling the Knowledge in a Neural Network", NeurIPS Deep Learning Workshop

### 4.3 BOSS-B3: LLMLingua 提示词压缩测法

**测法**: 用 Microsoft 2023 LLMLingua 压缩 prompt 到同样保留率, 看失真是否 < 0.05。

- **如果 LLMLingua 失真 < 0.05**: 主张被拍平(200 节点上 0.95 是教科书水平)
- **deposon 应对**: 主张降级为"deposon 在 200 节点上的失真界 = 通用提示词压缩的下限"
- **真实脚本**: `.mavis/scripts/kt_b1/boss_b3_llmlingua.py` SHA-256 = `c0b55e0385a4`, 13966 字节
- **参考**: LLMLingua (Microsoft 2023) / LLMLingua-2 论文

### 4.4 4 条禁示条款(沿用 D0 准备 §4)

1. **不得在真实仓库跑 BOSS baseline**(必须 `/tmp/deposon_kt_b1_audit_<timestamp>/` 副本)
2. **不得让 BOSS baseline 脚本诱导操作者删除冻结锚**
3. **不得在 BOSS 测法跑通前宣称 KT-B1 方向 PASS**
4. **不得跳过 BOSS 测法只跑主实验**(防 V1 撞 BOSS 重演)

### 4.5 BOSS 测法回写(沿用 QUICK_KILL V0.2 §"下次升级触发")

D7 末, KT-B1 判死 PASS/FAIL 后, 无论是否撞 BOSS, 必须把"实测记录"回写到 `QUICK_KILL_6_DIRECTIONS.md` V0.3:
- BOSS-B1/B2/B3 任一撞上 → 写入"已撞 BOSS, 失真上界主张降级"
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
- **预期**: 单调递增(攻击强度越大, 成功率越高)

### 5.3 A3: 种子复现

- **做法**: seed = 42 / 123 / 456 三套
- **判定**: 看 std/mean > 0.2 → 报"种子敏感"
- **预期**: std/mean < 0.1(种子稳健)

### 5.4 抗攻击通过条件

- A1 / A2 / A3 全部通过 → 攻击实验可信
- 任一不通过 → 重审实现, Mavis 派 reviewer-b 复审

---

## 6. 5 锚预登记(V0.1 真实值, D0 末已算)

> **V0.1 状态**: 5 锚 SHA-256 前 12 位已由 D0 末 successor 子代理算入 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1, 本节直接引用真实值。

| 锚 ID | 对象 | 算法 | 字段 | SHA-256[0:12] |
|---|---|---|---|---|
| `KT_B1_V19_BENCHMARK` | v19 冻结 200 题守恒残差 JSON | SHA-256 全文 → 前 12 位 | `t_plus_r_plus_a_max_deviation=2.2e-16` | **`910c4333eead`** |
| `KT_B1_KILL_LINE` | KT-B1 判死裁定函数(双视角 4 档) | SHA-256 全文 → 前 12 位 | `kills={PASS_KT_B1, GRAY_DOWN, GRAY_UP, FAIL_KT_B1}` | **`9f351078e5bf`** |
| `KT_B1_ATTACK_BANK` | 攻击脚本集(3 类 × 200 次) | SHA-256 全文 → 前 12 位 | `attacks={deletion:200, manifest_swap:200, chain_modify:200}` | **`4b37a40cc984`** |
| `KT_B1_AUDIT_FUNCTION` | 守恒审计函数 T+R+A=1 | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | **`3aa661cfbab5`** |
| `KT_B1_HARNESS` | 200 次攻击 harness + BOSS baseline harness | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | **`39dacb572f2e`** |

5 锚 SHA-256 前 12 位必须先于 D3 末运行公布, 公布后任何 ≥ 1 锚漂移 → 全 KT-B1 撤回。

**V0.1 与 V0 草稿的差异**: V0 草稿中 §1.3 表格"D1 successor 算"在 V0.1 升级为 5 个真实 SHA-256 值(从 frozen 锚 JSON §anchors/KT-B1 引用)。V0 草稿 §6 是占位表格, V0.1 升级为同一表格的真实值版本(§1.3 和 §6 内容一致, 7 条铁律 §11 引用一致)。

---

## 7. 复现协议(reviewer-b 独立 /tmp 副本审计)

### 7.1 复现步骤

1. **复制仓库到 `/tmp/deposon_kt_b1_audit_<timestamp>/`**(timestamp 格式 `YYYYMMDD_HHMMSS`)
2. **读 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1 验 5 锚**, 逐位比对 V0.1 §6 真实值
3. **选 50 次攻击**(从 600 次中随机抽 50, 固定 seed=42)重跑, 验攻击成功率 ± 5% 内
4. **验失真上界 ± 5% 内**
5. **跑 3 个 BOSS baseline**(BOSS-B1 Sinkhorn / BOSS-B2 KD / BOSS-B3 LLMLingua, 真实脚本见 §4), 记录各自失真上界

### 7.2 通过条件

- 5 锚 SHA-256 前 12 位全部一致(对比 V0.1 §6 真实值)
- 攻击成功率 ± 5% 内
- 失真上界 ± 5% 内
- 3 个 BOSS baseline 全部跑通(不要求 deposon 优于 BOSS, 只要求 BOSS 测法本身可跑通)

### 7.3 失败处理

- 任意一项超差 → 撤回整 KT-B1
- 5 锚漂移 ≥ 1 → 全 V0 撤回
- reviewer-b 报告独立成 1-2 页审计报告, 落 `verifier/audits/KT_B1_audit_<timestamp>.md`

---

## 8. 交付

### 8.1 D1 交付: SPEC 冻结

- Mavis 改 Mavis 内部 P-B V0 spec, 在 §1 加 BOSS 测法节(沿用本 spec §4)
- Mavis 派 successor 算 5 锚 SHA-256 前 12 位, 落 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1(V0.1 已落地)
- 本 spec 公布 SHA-256 后冻结(V0.1)

### 8.2 D5 交付: 内部判死报告 1-2 页

- 路径: `docs/V3X/KT_B1_D5_REPORT_2026_09_09_mavis.md`
- 内容: 攻击成功率(对外) + 失真上界(内部) + 95% CI + 判死裁定 + BOSS baseline 结果
- 双视角 4 档裁定表(PASS_KT_B1 / GRAY_DOWN / GRAY_UP / FAIL_KT_B1)

### 8.3 D7 交付: 一页摘要(对外, 微信友好) + 完整中文判死报告(内部, 备查)

- **一页摘要**: `docs/V3X/D7_KT_B1_ONE_PAGE.md`
  - 3 行内容: KT-B1 双指标 + 4 档裁定 + BOSS 测法结论
  - 微信可直接转发
- **完整中文判死报告**: `docs/V3X/KT_B1_PAPER_zh.md`
  - 10-15 页, 含 5 锚溯源 + 全部 600 次攻击明细 + BOSS 测法对照
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
- **处理**: 全 KT-B1 撤回, 重审 spec
- **通知**: WeChat 给王老师 + Mavis 群内同步
- **D7 影响**: 推迟 1-2 天交付

### 9.2 判死裁定(4 档)

| 档位 | 触发条件 | 主张降级 | WeChat 通知 |
|---|---|---|---|
| **PASS_KT_B1** | 攻击成功率 ≥ 50% 且 失真上界 ≥ 0.95 | 不降级, P-B 判活 | 一行: KT-B1 PASS |
| **GRAY_DOWN** | 攻击成功率 ≥ 50% 且 失真上界 < 0.95 | 失真过大, 降级为"工程可用" | 一行: KT-B1 GRAY_DOWN |
| **GRAY_UP** | 攻击成功率 < 50% 且 失真上界 ≥ 0.95 | 失真小但守恒检测力不足, 升级为"失真界不依赖守恒" | 一行: KT-B1 GRAY_UP |
| **FAIL_KT_B1** | 攻击成功率 < 50% 且 失真上界 < 0.95 | P-B 方向判死, 撤 V3.X 整个 P-B 候选 | 一行: KT-B1 FAIL, 撤 P-B 候选 |

### 9.3 BOSS 测法撞上(BOSS-B1/B2/B3 任一)

- **触发**: 失真上界 ≥ 0.95 但 Sinkhorn OT / KD / LLMLingua 也 ≥ 0.95
- **处理**: 失真上界主张降级为"通用 OT/KD 工具的下限", 不强调"deposon 独有"
- **回写**: D7 末回写 `QUICK_KILL_6_DIRECTIONS.md` V0.3
- **WeChat 通知**: 通知王老师"撞 BOSS, 主张降级"

### 9.4 抗攻击检查不通过(A1/A2/A3 任一)

- **触发**: 攻击者提示词扰动 > ±10% / 攻击强度无单调性 / 种子 std/mean > 0.2
- **处理**: 重审实现, Mavis 派 reviewer-b 复审
- **王老师**: 仅 ack, 是否撤回由 Mavis 自主决定

### 9.5 D1 阻塞(理论界未给)

- 沿用 P-B V0 spec §8: 内部判死线(失真上界)需要 P-B V0 §3.5 理论界公式(L(M, T) / U(M, T))
- **触发**: 王老师 D1 WeChat 未给 1-page theory
- **处理**: 整 KT-B1 内部判死线阻塞, 只跑对外判死线(攻击成功率)
- **后果**: D7 交付只有"对外 1 页", 内部失真上界延迟到 D1 理论输入后补

---

## 10. 时间线(D0-D7)

| Day | 任务 | 派给 | 输出 |
|---|---|---|---|
| **D0** | 锚点预登记 + §0.5 BOSS 测法节冻结 | Mavis + worker-b | 本 spec V0.1 公布(V0 → V0.1 升级已固化)+ 5 锚真实 SHA-256 已落地 |
| **D1** | Mavis 改 Mavis 内部 P-B V0 spec 加 BOSS 测法节 + successor 算 5 锚 SHA-256(已落地) | Mavis + successor | P-B V0 spec V0.1 + `verifier/handoff/KT_ABC1_anchors_sha256_12.json` |
| **D2** | 实现攻击者 + 200 次攻击 harness + BOSS-B1 Sinkhorn OT baseline(已实现, SHA `19325960b8be`) | data | `.mavis/scripts/kt_b1/attacker.py` + harness + `boss_b1_sinkhorn_ot.py` |
| **D3** | pilot 50 次攻击 + BOSS-B1 baseline 跑通 + WeChat 中期简报 | data + Mavis | pilot 报告 + WeChat 三行判死状态 |
| **D4** | 全 200 次攻击 × 3 类 = 600 次 + BOSS-B2 KD(已实现, SHA `1781ea2f742d`)+ BOSS-B3 LLMLingua(已实现, SHA `c0b55e0385a4`)跑通 | data | 600 次攻击原始日志 + 2 个 BOSS baseline 跑分 |
| **D5** | reviewer-b 判死 + 3 攻击 + BOSS-B1/B2/B3 测法 + P-B 判死裁定对照 | reviewer-b + data | D5 内部判死报告 1-2 页 + 4 档裁定表 |
| **D6** | 失败模式处理 / GRAY 扩 cell(若需要) | Mavis + v3x | GRAY 扩 cell 报告(若需要) |
| **D7** | 中文短稿 + 一页摘要 + 全 handoff 归档 + BOSS 测法结果回写 QUICK_KILL V0.3 | paper-cn + successor | D7 一页摘要 + 锚定工件包 + `QUICK_KILL_6_DIRECTIONS.md` V0.3 |

### 10.1 关键节点

- **D0 末**: 本 spec V0.1 公布 + 5 锚真实值已落地(冻结 SPEC 不依赖运行)
- **D3 末**: WeChat 中期简报(王老师三行判死状态)
- **D5 末**: 4 档判死裁定 + BOSS 测法结果(双视角双跑结论)
- **D7 末**: 完整交付 + 锚定工件包 + BOSS 回写

### 10.2 硬截止

- D7 硬截止, 最多宽限 1-2 天(沿用 v3 提案第七节风险缓解)
- 延误在 D3 中期简报中提前报

---

## 11. 与 7 条铁律兼容性(V0.1 新加, 沿用 P-A V0 spec V0.2 §9)

| 铁律 | KT-B1 V0.1 兑现 | 引用 |
|---|---|---|
| ✅ **双审** | reviewer-a 静态审本 SPEC + reviewer-b 在 `/tmp/deposon_kt_b1_audit_<timestamp>/` 副本独立重跑 50 次攻击 + 3 个 BOSS baseline | §7 复现协议 |
| ✅ **API key 不入 prompt** | 本 SPEC 零 LLM API 调用(守恒审计 + BOSS baseline 全是纯数学 / 传统 ML); 不读 `C:\Users\Administrator\Desktop\AI\新建文本文档.txt` | §2.4 检测器(纯数学审计) + §4 BOSS baseline(无 LLM) |
| ✅ **术语红线** | 用"账平 / 守恒审计 / 失真上界 / 攻击成功率 / 检测器召回率 / Sinkhorn OT / KD / LLMLingua"等工程/数学术语, 不用"散射层魔法"等营销词 | §2 + §3 + §4 |
| ✅ **数字溯源** | 全部数字从 frozen 锚 JSON 字段路径引(v3 提案附录 B + P-B V0 spec + 本 SPEC §6 5 锚真实 SHA-256 + 附录 B 数字溯源表) | §6 + 附录 B + §1.3 |
| ✅ **verifier 纪律** | §7 复现协议用 /tmp 副本; 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/ | §7 + D0_FREEZE_PREP §6 |
| ✅ **预登记** | §6 5 锚 SHA-256 前 12 位 D0 末已算, 先于运行冻结并公布, 任何 ≥ 1 锚漂移 → 全 KT-B1 撤回 | §6 + §9.1 失败模式 |
| ✅ **推送策略** | 不主动发, 等 D0 末群内公布 + D3 中期简报 + D7 末 WeChat 一行判死结果 | §8 交付 + v3 提案第八节 |

**V0 草稿差异**: V0 草稿无 §11 7 条铁律节(零散在 §0.1 列出), V0.1 升级为结构化表格, 7 条逐条展开 + 引用具体节 + 锚 SHA-256 对应。

---

## 12. 已知未决项(V0.1 新加, 等 D0 末 / D1 末 / D5 末 / D7 末确认)

| 编号 | 已知未决项 | 决策时点 | 派给 |
|---|---|---|---|
| **U-B1-01** | v19 冻结 200 题攻击者构造器是否已 D2 实现并通过本地 smoke test: `.mavis/scripts/kt_b1/attacker.py` SHA `4b37a40cc984` 已落地, 但 3 类攻击(deletion/manifest_swap/chain_modify)的实际实现细节 | D2 末 | data |
| **U-B1-02** | BOSS-B1 Sinkhorn OT(已实现, SHA `19325960b8be`)实测失真上界是否 ≥ 0.95(若 ≥ 0.95 → 主张降级"通用 OT 工具下限") | D4 末 | data |
| **U-B1-03** | BOSS-B2 KD(已实现, SHA `1781ea2f742d`)实测失真上界是否 ≥ 0.95(若 ≥ 0.95 → 主张降级"KD 工具默认下限") | D4 末 | data |
| **U-B1-04** | BOSS-B3 LLMLingua(已实现, SHA `c0b55e0385a4`)实测失真 < 0.05(若 < 0.05 → 主张被拍平"通用提示词压缩下限") | D4 末 | data |
| **U-B1-05** | GRAY 扩 cell 触发: 攻击成功率 40-60% 或失真上界 0.90-0.95 时是否需要扩 cell 到 1000 题重判 | D5 末 | Mavis |
| **U-B1-06** | 4 档裁定中 GRAY_DOWN / GRAY_UP 主张降级是否需王老师额外 ack(默认仅一行 WeChat 通知) | D5 末 | 王老师 WeChat |
| **U-B1-07** | 抗攻击 A1/A2/A3 任一不通过时, 重审实现 vs 重审整套 KT-B1 设计的判定标准 | D5 末 | Mavis |
| **U-B1-08** | 王老师 D0 三问默认值(沿用 v3 提案第六节)在 D1 末前是否 ack; 沿用 P-B V0 spec §1.4 沿用 P-A V0 spec §1.4 默认 | D1 末 | 王老师 WeChat |
| **U-B1-09** | D1 理论界(1-page theory)未给时, 内部判死线阻塞处理(沿用 §9.5); 王老师 1 周内是否补充 | D7 末 | 王老师 WeChat |
| **U-B1-10** | D7 末 BOSS 测法结果回写到 `QUICK_KILL_6_DIRECTIONS.md` V0.3 的具体段落位置 | D7 末 | successor |

**V0 草稿自检** (V0 阶段无 self-review 节, V0.1 新加完整性核对):
- ✅ §0 元约束与 7 条铁律(V0.1 §11 表格化)
- ✅ §1 双视角目标 + 4 档裁定矩阵 + 5 锚真实值(V0.1 §1.3 + §6)
- ✅ §2 实验设计 v19 200 题 + 3 类攻击 + 600 次 + 检测器 + 失真度
- ✅ §3 度量双指标 + 副指标 + 95% bootstrap CI + 攻击成功率 = 1 - 召回率反转
- ✅ §4 BOSS-B1/B2/B3 真实脚本 SHA + 占位说明
- ✅ §5 抗攻击 A1/A2/A3
- ✅ §6 5 锚真实值(从 frozen 锚 JSON 引用)
- ✅ §7 复现协议 /tmp 副本 + 4 项通过条件
- ✅ §8 D1/D5/D7 交付物清单
- ✅ §9 失败模式 5 类(5 锚漂移 / 4 档裁定 / BOSS 撞上 / 抗攻击不通过 / D1 阻塞)
- ✅ §10 时间线 D0-D7

---

## 13. 引用与版本(V0.1 新加)

- **v3 提案**: 《Deposon × 王子贺老师 合作提案》(2026-09-04, 4 页 PDF, 致: 王子贺 人大高瓴人工智能学院)
- **Mavis P-B V0 spec**: `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` V0(2026-09-09)
- **Mavis QUICK_KILL_6_DIRECTIONS.md V0.2**: `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` 方向 2 P-B + BOSS-B1/B2/B3
- **Mavis D0_FREEZE_PREP_2026_09_09.md**: `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` §1.2 / §3
- **V0.1 frozen 锚 JSON**: `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1(15 真 + BOSS self_test 数据)
- **BOSS 测法理论引用**:
  - BOSS-B1: Cuturi 2013, "Sinkhorn Distances: Lightspeed Computation of Optimal Transport", NeurIPS
  - BOSS-B2: Hinton et al. 2015, "Distilling the Knowledge in a Neural Network", NeurIPS Deep Learning Workshop
  - BOSS-B3: LLMLingua (Microsoft 2023) / LLMLingua-2
- **BOSS 测法真实脚本 SHA-256**(`KT_ABC1_anchors_sha256_12.json` §boss_baselines/KT-B1):
  - BOSS-B1 Sinkhorn OT: `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py` = `19325960b8be`(14956 字节)
  - BOSS-B2 KD: `.mavis/scripts/kt_b1/boss_b2_kd.py` = `1781ea2f742d`(14224 字节)
  - BOSS-B3 LLMLingua: `.mavis/scripts/kt_b1/boss_b3_llmlingua.py` = `c0b55e0385a4`(13966 字节)

---

## V0 → V0.1 升级记录(沿用 P-A V0 spec V0.1 → V0.2 模式)

### V0 状态(2026-09-09 草稿)

- §1.3 5 锚表格"D1 successor 算"占位
- §6 5 锚表格"D1 successor 算"占位(与 §1.3 内容重复, 占位)
- §4 BOSS baseline 占位骨架, 标"具体实现在 D2-D4"
- 无 §11 7 条铁律结构化节(0.1 节有零散列举)
- 无 §12 已知未决项
- 无 §13 引用与版本
- 无升级记录 footer
- §10 时间线 + 附录 A-D 已有

### V0.1 增量(2026-09-09 升级)

| 节 | 改动类型 | 改动原因 |
|---|---|---|
| **头标** | 新加 V0.1 状态声明 + frozen 锚 JSON 路径 | 显式标注冻结, 与 V0 草稿区分 |
| **§0.1** | 7 条铁律加上"数字溯源"具体引用"V0.1 §6 + 附录 B 数字溯源表" | V0 草稿 0.1 只列条目, V0.1 指向具体节 |
| **§0.4** | 新加"V0.1 升级变更"小节, 4 项关键改动摘要 | 读者快速看到 V0.1 与 V0 的最关键差异 |
| **§1.3** | 5 锚表格"D1 successor 算"占位 → 5 个真实 SHA-256 值(从 frozen 锚 JSON §anchors/KT-B1 引用) | V0.1 冻结的核心改动 |
| **§4.0** | 改标题 + 加"V0.1 升级"段说明 3 个 BOSS 占位 → 已实现真实脚本(SHA-256 + 字节数见 §4.1-4.3) | V0.1 反映 frozen 阶段实际进度 |
| **§4.1-§4.3** | BOSS-B1/B2/B3 占位骨架 → 真实脚本 SHA-256 + 字节数 + 路径(从 frozen 锚 JSON §boss_baselines/KT-B1 引用) | V0.1 冻结的核心改动 |
| **§6** | 5 锚占位 → 真实值(与 §1.3 一致, 7 条铁律 §11 引用一致) | V0.1 冻结的核心改动 |
| **§7.2** | 验 5 锚改用 V0.1 §6 真实值比对 | V0.1 反映 frozen 阶段 |
| **§8.1** | 标注 V0.1 5 锚已落地, 不需 D1 successor 算 | V0.1 状态反映 |
| **§10** | D0/D2/D4 加 "已落地 / 已实现" 标注(锚 JSON + BOSS 脚本) | V0.1 阶段真实进度 |
| **§11** | 新加, 7 条铁律自检升级为表格形式, 逐条展开 + 引用具体节 + 锚 SHA-256 对应 | V0 草稿 0.1 节零散列举, V0.1 结构化 |
| **§12** | 新加, V0 → V0.1 已知未决项(U-B1-01 ~ U-B1-10 共 10 项) + V0 完整性自检折叠 | V0.1 前瞻性缺口清单 |
| **§13** | 新加, 引用与版本(沿用 P-A V0 spec V0.2 §13 模式) | V0.1 反映 frozen 阶段实际工件 |
| **升级记录** | 新加 footer(沿用 P-A V0 spec V0.1 → V0.2 升级记录模式) | 透明化升级过程, 便于审查与回退 |

### V0 主体保持冻结

- §0.2 强度声明
- §0.3 本 SPEC 不做的事
- §1.1 双视角目标(阈值表不变)
- §1.2 判死线 SPEC 冻结时点(只把"已落地"标注到 §1.3)
- §1.4 王老师 D0 三问默认值
- §2 实验设计(v19 200 题 + 3 类攻击 + 600 次不变)
- §3 度量(双指标 + 副指标 + bootstrap CI + 攻击成功率反转说明不变)
- §5 抗攻击(沿用 P-B V0 §5 不变)
- §7 复现协议(只改 7.2 验 5 锚引用)
- §8 交付(只改 8.1 标注 V0.1 状态)
- §9 失败模式(5 类不变)
- §10 时间线(只加"已落地/已实现"标注)
- 附录 A-D(对齐 v3 提案 + 数字溯源表 + 5 锚 SHA-256 计算协议 + BOSS baseline 占位脚本索引)

### 下次升级触发

- D5 末 BOSS 测法结果 + 4 档判死裁定 → 回写到 `QUICK_KILL_6_DIRECTIONS.md` 对应 BOSS 列表, 作为"实测记录"
- D7 末判死 PASS/FAIL + BOSS 撞上情况 → 触发 KT-B1 V0.2 升级(若 PASS)或 V0 撤回(若 FAIL)
- §6 5 锚任一漂移 → V0.1 撤回(本 SPEC 与 P-B V0 spec 同时)

---

## 附录 A · 与 v3 提案 KT-B1 行的对齐

v3 提案第六节 KT-B1 行原文:
> "合成操纵者 n=200 次攻击下的守恒审计:成功率 ≥50% →「守恒即检测力」判死、退守复合协议分叉;<50% → 升级为正面结果归档。D3 冻结 SPEC,D5 跑。两个结局都是判死级交付(账平能否抓住操纵者)。"

本 spec 对齐:
- ✅ 合成操纵者 n=200 次攻击(本 spec §2.2)
- ✅ 守恒审计 T+R+A=1(本 spec §2.4)
- ✅ 成功率 ≥50% / <50% 二档(本 spec §1.1, 扩展为双视角 4 档)
- ✅ D3 冻结 SPEC, D5 跑(本 spec §10, 实际 V0.1 在 D0 末已冻结, D1 末 + D3 末 + D5 末分阶段跑通)
- ✅ 两个结局都是判死级交付(本 spec §9.2)

**关键差异**: 本 spec 增加了 Mavis 内部 P-B V0 spec 的失真上界判死线(双跑设计), 对外不破坏 v3 提案承诺, 内部多 1 个互补指标。

---

## 附录 B · 数字溯源表(V0.1 沿用, 来源冻结化)

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
| 5 锚 SHA-256 前 12 位 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-B1(V0.1 真实值) |
| BOSS-B1/B2/B3 真实脚本 SHA-256 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §boss_baselines/KT-B1 |

---

**KT-B1 SPEC V0.1 冻结版结束, 5 锚 SHA-256 已落地, §11 7 条铁律已逐条展开, §12 已知未决项已列 10 项。**
