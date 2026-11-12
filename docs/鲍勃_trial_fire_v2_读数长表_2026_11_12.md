# 鲍勃 · trial_fire_v2 读数长表（已完段全读数）· 2026-11-12

> **承办**：鲍勃-实验分析师｜**件性质**：主序 trial_fire_v2（bcdebe8317741c7e）＋附带位已完段读数成表（派单第 2 点读数呈）
> **口径**：红绿如实·异常与修复逐条入账（§六）；SPEC 双账制沿既定（600 态 GRAY 读数回填后合并呈批）
> **数据源**：pull_w1/ 本地回传件＋远端 log 实测（指纹在册）＋aux_pull/ 附带位回传件

---

## 一、主序 9 段段态总表

| 段 | 态 | 完成时点 | 备注 |
|---|---|---|---|
| smoke | done | 11-12 00:24:24（301s） | P1 bit-exact✓ P2 boomloop✓ P3 probe✓（预注册三绿） |
| assets | done | 00:24:27 | 10 项全✓·nina dev/test md5 在案 |
| tp4 | done | 02:12:41（warn 容收） | R1 全链；R2 train 完·eval 未竟（盘满·§六.1） |
| r4 | done | 07:43（段收）·07:52（eval 读数补全） | 早停 350·两锚漏修复后 eval 全读数出（§六.3） |
| m0 | done | 07:46:05 | 8 行差异表 measured 6/8·pending 2/8（#1/#4/#7 时序未至） |
| d4 | done | 07:46:06 | d4_windowB 5 件全恒等（0 补传） |
| expan | R1✓07:50·R2 在途 | — | R1 四锚全绿（dg_match/bit-match/agree 962/962）；R2 GRAY 注记（w1c 缺位·§六.4） |
| mem | 待跑（自动） | — | S0 记忆基线产出位（iter-1 硬依赖） |
| perm | 待跑（自动） | — | PERMPROBE 尾槽 |

## 二、tp4 段读数（T-P4 补跑·双臂）

### R1（约束臂·自然荷）
- **train**（150→600·310.7s·early_stop off）：final_wm_loss 0.50272｜base_loss 12.57817｜**loss_drop 96.0%**｜viol_total **0**｜best_step 590｜grad_max 965.82｜nan_free true｜vram 13.36G
- **eval 600 态**（26.4s）：**BAcc500 0.7293**｜BAcc310 0.7176｜BAcc155 0.7500｜KL_lastpos 14.6217｜KL_posavg 16.6862｜task_CE 0.5392｜**ED_face 0.037983**｜ED_tern 0.206805｜violations_deploy 0｜deployed_charge_sha 80768d18ebb6…（dg 链在案）｜drift_rows 282866｜corr_flips 670697
- **T-P 判据**：T-P1✓（viol=0）｜T-P2✓（drop≥90%：96.0%）｜T-P3✗（红绿如实）｜T-P4✓（ckpts+ledger 齐）

### R2（约束臂·置换荷）
- **t0 绑定**（10s·11-11 23:04 绑定沿用）：n_tern_rows 344064｜perm_src 573de5a1b2fc｜ED_tern_t0 0.207097｜BAcc_t0 0.5398｜KL_t0 11.9282｜base_loss 12.53727
- **train**（230→600·02:03–02:07）：W1-CKPT viol=0 全链恒等（sha db385d28dd6c）｜wm 0.5123（终窗）
- **eval 600 态**：**缺位**（02:12 盘满·进程连 log 都建不出·§六.1）——600 态读数以 expan 面A复算补位（GRAY 级·双账制 GRAY 候选面）

## 三、r4 段读数（三角对照臂·无荷约束）

- **t0**（9.5s·④锚修复后自然荷路径）：viol 0｜corr 0/0｜**ED_tern 0.206882**｜BAcc_t0 0.4797｜KL_t0 12.3295｜base_loss 12.57817｜charge_sha 573de5a1b2fc（自然荷·与 R1 同源）
- **train**（0→**350 早停**·144.8s·since_best 60·设计内行为）：final_wm 0.67252｜**loss_drop 94.65%**｜viol_total 0｜drift_rows 4010｜grad_max 1044.19｜nan_free true｜best_step 290
- **eval**（⑤锚修复后）：**BAcc 0.6397**｜KL 13.1608｜KLp 13.5093｜ED_face 0.037998｜EDt 0.206885｜drop 94.65%｜**W1-R4-EVAL-DRIFT viol=23**（无约束臂 drift 画像·不阻断·读数入账）｜T-P1✓ T-P2✓ T-P3✗ T-P4✗（ckpt_600 缺位＝早停字面判·如实）

## 四、expan 段读数（600 态扩面·faceA+faceB）

| 臂 | ckpt 路径 | dg_match | faceA（eval500 复算） | faceA bit_match | faceB_orig | faceB_d4 | GRAY | agree | wall |
|---|---|---|---|---|---|---|---|---|---|
| R1 | ckpt_600.pt（state_bf16 部署态直载·§六.4） | **true** | 0.7293 | **true** | 0.6876 | 0.6966 | 38（3.8%） | **962/962** | 16.9s |
| R2 | ckpt_600.pt | 待出（GRAY：w1c 对拍源缺位·A_MATCH=None 注记） | 跑中 | — | — | — | — | — | — |

## 五、附带位读数

### 5.1 vLLM v2.2 验装（vllm_v22_verify·30s）
- G0 product sha 复算 5c63c0563d8b…**与在册恒等✓**｜bundle 6 件指纹在案
- phase1 **GREEN**｜phase2 **YELLOW**（引擎红→transformers 代偿面 GREEN·引擎安装候次窗）

### 5.2 中径 3 配置（c1_midpath_pre·wall≈60s each·脚本尾部 json.dump bug 落盘红·读数在 log 全量在案·§六.5）

| 配置 | embed_mode | ln_exempt | n_quant | ED_energy | S4_cos_layer0 | S4_KL_lastpos | S5_bacc | G1A_ED | G1A_cos | G1A_dir |
|---|---|---|---|---|---|---|---|---|---|---|
| M1_embedexempt | exempt | false | 309 | 0.7173 | 0.1645 | 11.726 | 0.4854 | ✗ | ✗ | ✗ |
| **M2_lnexempt** | **tern** | **true** | **197** | **0.2647** | **0.8473** | **2.475** | **0.5905** | ✗ | **✓** | **✓** |
| M3_int8embed | int8 | false | 310 | 0.6715 | 0.1660 | 11.791 | 0.4875 | ✗ | ✗ | ✓ |

**读法**：M2（tern embed＋LN 豁免）全面最优——ED 0.265（vs M1 0.717/M3 0.672）·cos_layer0 0.847·方向门✓·KL 2.47（vs 11.7/11.8）·n_quant 最少 197；G1A_ED 三配置均✗（ED 门未过·能量门收紧位候 PI 裁——ε 收紧建议与 m0 差异表同呈）。中径＝SPEC「中位径」参考面（SPEC 数值暂认可·初值冻结·双账制 M0 回填）。

## 六、异常与修复账（红绿如实）

1. **磁盘 100% 满**（50G/50G·余 20K·01:44–07:28 持续）：R2 ckpt_resume_600 写坏（2.4G/应 7.15G）＋tp4ev_R2 连 log 建不出＋man_save SFTP OSError——**修复**：07:28 腾挪 20.05G（本窗新产物：坏件+resume_600×2〔ckpt_600 代偿〕+中间 ckpt 9 件·11-10 既有件 0 触）；GPU 空转 5h（02:12–07:34·PI 07:29 点破属实）如实入账。
2. **mk_variants R4 锚漏④**（t0 荷表位）：R4 误入 R2 置换荷分支→W1-T0-RED 340262 假红——**修复**：④锚补（R4 全同 R1 走自然荷）·变体重生成 sha 9e0233d6997d5b3f。
3. **mk_variants R4 锚漏⑤**（eval 审计位）：R4 无约束臂训练后部署面 vs QDEV 必然漂移（设计内 drift 画像）·基件 assert 假红——**修复**：⑤锚（R4 放行+viol 记读不阻断）·变体 sha 809f3acdf986e7c6（④⑤合一版）。两修均候双审追认。
4. **expand 兼容修**：R1/R2 ckpt_resume_600 盘桥清理后双取 fallback 至 ckpt_600（审计点件·无 theta 键）→KeyError——**修复**：state_bf16 部署态直载路径（语义等价锚＝dg 重算对拍 w1c〔**R1 实测 dg_match=true+faceA bit-match true**〕）＋R2 w1c 缺位容错（GRAY 注记）。
5. **中径 json.dump bug**：`open()` 误带 indent 参数→TypeError 落盘崩——读数在 log 全量在案（§5.2 已提取）·修复件候次窗（2 分钟级重跑）。
6. **r4 段收口时序**：主程序 07:43 段收（W1-TRAIN-DONE 命中）先于 eval 重跑（07:50–07:52）——R4-PULL 读数回传为主程序自动位·本表读数以 07:52 后补拉为准（R4 w1c_results.json 在位）。

## 七、SPEC 双账制登记（600 态）

- **GREEN 面**（强锚读数）：R1 600 态全读数（§2.1·eval+expan faceA bit-match 双源一致）
- **GRAY 面**（候回填·合并呈批）：R2 600 态（train 链 viol=0 恒等✓·eval 缺位→expan 面A复算 GRAY 注记）；R4 350 早停态（drift 画像 viol=23 读数在账）
- 呈批位：expan R2 读数出＋mem/perm 收口后合并呈批（含 M0 差异表 ε 收紧建议·中径 M2 参考面）

---

**落款**：鲍勃-实验分析师·2026-11-12 08:02 窗中实测｜红绿如实·修复链全入账｜凭据 0 落盘 0 回显
