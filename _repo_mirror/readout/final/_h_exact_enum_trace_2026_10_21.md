# H 精确枚举补实验 · 域①（在册 harness 面）· **留痕表** ｜`K-HEN-7` 逐条留痕 ｜2026-10-21 夜

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_h_exact_enum_trace_2026_10_21.md` |
| **件路径**（📌 惯例贴路径以便传递 · 复制即传） | `_repo_mirror/readout/final/_h_exact_enum_trace_2026_10_21.md` |
| **件性质** | 🔴 **实测留痕面之载体**（`K-HEN-7` 之「每格之决策条目须逐条留痕·0 抽样删减」）｜⛔ **0** 落五终判 · ⛔ **0** 闭 `KD` · ⛔ **0** 宣告段毕 · ⛔ **0** 宣告可开跑 · ⛔ **0** 代 PI 裁／释／择／给值 · ⛔ **0** 充「要件②已闭」 |
| **出件方** | `worker`（实验执行手）——棒 `H-EXACT-ENUM-D1-TRACE` |
| **令源** | ① `pi_rulings\_pi_card_answers_register_2026_10_21_v208.md`（Q1 ＝ 读甲·H 精确枚举之补实验之跑授权已给）② 同日 `..._v218.md`（Q1 Other 逐字「都说了，你侧没有跑禁」·Q2 ＝ 域③·Q3 ＝ 读甲 15 格·Q4 Other「不计」）③ 同日 `..._v219.md`（Q1 ＝ 拟案 `bfce04eb2745` 核准生效即锁·Q2 ＝ 域①先跑＋域②俟到位）④ `results\_h_exact_enum_killline_prereg_2026_10_21.md`（`K-HEN-1`…`K-HEN-16` ＋ `K-HEN-G1`…`G6`＝22 条·**生效·生效即锁**）——📌 四件之 SHA-12／bytes 皆**本棒直算**（`Get-FileHash`／SHA-256）·见 §5 |
| **观测时点** | **2026-10-21T23:04:35+08:00 UTC+8**（本棒实测·凡引现值必带此时点） |
| **状态** | 🔴 **实测留痕已落·判定面按 `K-HEN-9`／`K-HEN-10` 之处置语（见读出件 §6）**——本件 0 落五终判·0 宣告段毕·0 宣告可开跑 |
| **必遵 skill（⛔ 0「无需 skill」）** | ① `superpowers:verification-before-completion`（`...\skills\verification-before-completion\SKILL.md`＝`2befe7fc55bc`／3,646 B——**C: 盘与 D: 盘副本逐位相同**·两处各实测 1 命中）——**全文读毕**（「NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE」施于本件之落盘后独立回读＋字节级自扫）｜② `scientific-research-workflows:peer-review`（`...\skills\peer-review\SKILL.md`＝`fed0262d707a`／11,639 B·〔本地绝对路径·脱敏略:D〕: 逐位相同）——**全文读毕**（其「证据先于断言·claim–evidence 对齐·⛔ 0 虚构实验与结论·⛔ 0 代替人类裁决·阴性断言附通道／时点／射程」施于本件全部引面） |
| **本棒动作面（自证）** | **0** 次 LLM 调用 · **0** 次网络请求（socket 实例化即抛·封堵面见 §5）· **0** 读 key／`.env` · ⛔ **0** 触归档区 `〔归档件引用·未上传:〔归档区〕〕` · `〔本地他区引用·未上传:GLM〕` 与 `_repo_mirror` **0 触** · **0** 回改任何既有件一字 · **0** 移动／改名／删除 · **0** 新建目录 · **0** 新建或合并派生 JSON · ⛔ **0** 落五终判 · ⛔ **0** 闭 `KD` · ⛔ **0** 宣告段毕 · ⛔ **0** 宣告可开跑 ｜📌 **既有件触动数 ＝ 0 件**（写前／写后指纹对勘见读出件 §9） |

---

## §1 冻结面（`K-HEN-8` 逐项冻结·测量前登记）

| 项 | 冻结值 |
| :-- | :-- |
| **标的域** | **域①**（在册 harness 面）——⚠ 域之择 ＝ 域③（`v218-Q2`）·**域①先跑＋域②俟到位**（`v219-Q2`）·本件仅及域①·⛔ 0 以域①充域③ |
| **规模档** | **档甲**（在册 seed 42 面）——逐族 `n_decisions` ＝ `15／15／15／15／20`（照录在册供给面 ⑩） |
| **seed** | **42** |
| **`mask_key_fields`** | **False**（默认·遮蔽臂未开） |
| **排除口径** | **照录在册**：`excluded_cell_ids` ＝ `["T4_2x2#04"]`（v147-Q2）·每格 1 决策 ·排除前／后两套值**并报** |
| **计数口径** | **决策条目数**（prompt 级决策·⛔ 非 call 数·⛔ 非 token 数·⛔ 非「≈33」名义值） |
| **机制臂 RNG 播种规则** | `cell_seed ＝ SEED*10000 + tier_idx*100 + mech_idx*10 + fam_idx`（照录在册主实验之公式；域① 之 `tier_idx` ＝ 0 ＝ `ETAC-D1` 之默认 Deposon 参数 `eta=0.5／g_couple=1.0／g_aether=0.1`）——📌 本项为**留痕可复现所必需之构造登记**·非阈值·不改拟案之任何冻结面；📌 **计数与机制选择无关**（见 §4-3 之不变性检验） |
| **码载锚（自测）** | `tools\exp_harness.py` ＝ **`ce64b9b97489`**／45,590 B（执行前当场自测·`Get-FileHash`·⛔ 0 用内建 `hash()`）——📌 **⛔ 非 5 锚基准**（`K-GE01F-1` 之禁带自陈） |

## §2 留痕表（`K-HEN-7` 之逐条留痕·**0 抽样删减**·共 **237** 行 ＝ 3 机制 × 79 决策）

> 📌 字段（照录 `K-HEN-7` 之列举）：`cell_id`（**机制×族**）· `decision_idx` · `prompt` 文本哈希（**SHA-256 全文 hex**）· `options` · `chosen` · `correct` · `value` · `is_correct`；📌 另附 `face_cell_id`（族内面之 `族#序号`）与 `cell_seed`（可复现锚）。

| # | cell_id（机制×族） | decision_idx | face_cell_id | prompt_sha256（全文 hex） | options | chosen | correct | value | is_correct |
| --: | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-: |
| 1 | `M1_Deposon_TRA|T1_GSM8K` | 0 | `T1_GSM8K#00` | `0c76fc58fd20ceb38f9eec55e3bd33293ececbe9bb8f73e6425d04fc250597de` | 122; 115; 113; 118 | `115` | `115` | 122=0.0; 115=1.0; 113=0.0; 118=0.0 | ✔ |
| 2 | `M1_Deposon_TRA|T1_GSM8K` | 1 | `T1_GSM8K#01` | `b60bdd4fa94c257b2840e7cdd8074f781a1513b58f7fdfaf34c025f086c34520` | 259; 250; 260; 254 | `250` | `254` | 259=0.0; 250=0.0; 260=0.0; 254=1.0 | · |
| 3 | `M1_Deposon_TRA|T1_GSM8K` | 2 | `T1_GSM8K#02` | `9b0c702712a71394e1a22cfff22f7f64b40aaa8e494c2ffaae76ff35e10c11bf` | 111; 118; 113; 123 | `113` | `113` | 111=0.0; 118=0.0; 113=1.0; 123=0.0 | ✔ |
| 4 | `M1_Deposon_TRA|T1_GSM8K` | 3 | `T1_GSM8K#03` | `88512ff7cd8b65e42a3fb2966ce013fa3a8f24e19b4fce183f716e08da760923` | 132; 138; 130; 126 | `130` | `130` | 132=0.0; 138=0.0; 130=1.0; 126=0.0 | ✔ |
| 5 | `M1_Deposon_TRA|T1_GSM8K` | 4 | `T1_GSM8K#04` | `d8707f67f03690e588204201162c09251b2f889e1f8790f898be9c3b7d0327e8` | 99; 103; 107; 98 | `99` | `99` | 99=1.0; 103=0.0; 107=0.0; 98=0.0 | ✔ |
| 6 | `M1_Deposon_TRA|T1_GSM8K` | 5 | `T1_GSM8K#05` | `b2f7e3ed61140917d2f812362c71834f2283e87fd580f9f6f57c1c92170c08f2` | 627; 628; 633; 623 | `627` | `627` | 627=1.0; 628=0.0; 633=0.0; 623=0.0 | ✔ |
| 7 | `M1_Deposon_TRA|T1_GSM8K` | 6 | `T1_GSM8K#06` | `0315860bf255e8fe8e008f473f6adec4c20fc33d4577958d9ba9af3f3c5d28bd` | 152; 149; 159; 151 | `151` | `151` | 152=0.0; 149=0.0; 159=0.0; 151=1.0 | ✔ |
| 8 | `M1_Deposon_TRA|T1_GSM8K` | 7 | `T1_GSM8K#07` | `c5c1b113f335fb0a76dadbcec17f6bcb45cfa883365ae165e357700bea20ecd8` | 426; 421; 418; 416 | `421` | `418` | 426=0.0; 421=0.0; 418=1.0; 416=0.0 | · |
| 9 | `M1_Deposon_TRA|T1_GSM8K` | 8 | `T1_GSM8K#08` | `71e29171b1a126e77d5743908bf25a6241084c0f9285b97c786815929c65d2fb` | 291; 303; 293; 298 | `293` | `293` | 291=0.0; 303=0.0; 293=1.0; 298=0.0 | ✔ |
| 10 | `M1_Deposon_TRA|T1_GSM8K` | 9 | `T1_GSM8K#09` | `f57e2150496b023368f10df8ab4b41ec4d735c06aad4a3f9cfe2255c768c1833` | 451; 460; 454; 456 | `454` | `454` | 451=0.0; 460=0.0; 454=1.0; 456=0.0 | ✔ |
| 11 | `M1_Deposon_TRA|T1_GSM8K` | 10 | `T1_GSM8K#10` | `e4c1f39dba919c928ece38afecbbbd3fb9f49b4bb80855b00479bbc48891efcf` | 149; 157; 144; 151 | `149` | `149` | 149=1.0; 157=0.0; 144=0.0; 151=0.0 | ✔ |
| 12 | `M1_Deposon_TRA|T1_GSM8K` | 11 | `T1_GSM8K#11` | `6bf1c606078d62417413b35371cade9dba0be1a426b89d149c57c1a10589be4a` | 796; 803; 793; 798 | `796` | `796` | 796=1.0; 803=0.0; 793=0.0; 798=0.0 | ✔ |
| 13 | `M1_Deposon_TRA|T1_GSM8K` | 12 | `T1_GSM8K#12` | `fcb36ccf3223b1f5ef7e1533bd720ef5e72a7f2eadff87c0d1f4bc69dbd418cc` | 535; 530; 532; 539 | `532` | `532` | 535=0.0; 530=0.0; 532=1.0; 539=0.0 | ✔ |
| 14 | `M1_Deposon_TRA|T1_GSM8K` | 13 | `T1_GSM8K#13` | `2c8abd29b76a82a4448cb8ba13095702ce7a910a986e253a4892d5bf97f68983` | 111; 106; 115; 117 | `111` | `111` | 111=1.0; 106=0.0; 115=0.0; 117=0.0 | ✔ |
| 15 | `M1_Deposon_TRA|T1_GSM8K` | 14 | `T1_GSM8K#14` | `8cf47788f52a8784fc9b4aa21bbf7a19a1dfac625c97669df241e6dafbe7f44a` | 455; 456; 465; 454 | `455` | `455` | 455=1.0; 456=0.0; 465=0.0; 454=0.0 | ✔ |
| 16 | `M1_Deposon_TRA|T2_StrategyQA` | 0 | `T2_StrategyQA#00` | `eb001e923c9b465dc2981d1fd229dfae544d6e9dacde0b068d4b7d83242c3784` | Always; Maybe; No; Yes | `Yes` | `Yes` | Always=0.0; Maybe=0.0; No=0.0; Yes=1.0 | ✔ |
| 17 | `M1_Deposon_TRA|T2_StrategyQA` | 1 | `T2_StrategyQA#01` | `8a96a16fd45bb69ce23490fceeb6ac66c858843405099b8c4b272c15ba5c6862` | Maybe; Yes; Always; No | `No` | `No` | Maybe=0.0; Yes=0.0; Always=0.0; No=1.0 | ✔ |
| 18 | `M1_Deposon_TRA|T2_StrategyQA` | 2 | `T2_StrategyQA#02` | `2a530cced264d5942e466c58624700f01225065aaa4c314d26e5270768b4d698` | No; Yes; Always; Maybe | `No` | `No` | No=1.0; Yes=0.0; Always=0.0; Maybe=0.0 | ✔ |
| 19 | `M1_Deposon_TRA|T2_StrategyQA` | 3 | `T2_StrategyQA#03` | `1702b00458e43ce2d5620f5a9ebd5400ac49dc672c4d1ebb456765efd23e21af` | Always; No; Maybe; Yes | `Yes` | `Yes` | Always=0.0; No=0.0; Maybe=0.0; Yes=1.0 | ✔ |
| 20 | `M1_Deposon_TRA|T2_StrategyQA` | 4 | `T2_StrategyQA#04` | `2c3b008efd27b146f059e64a94874518cb23d16279f84d0e49330c5105e4dac5` | Maybe; Always; Yes; No | `Maybe` | `No` | Maybe=0.0; Always=0.0; Yes=0.0; No=1.0 | · |
| 21 | `M1_Deposon_TRA|T2_StrategyQA` | 5 | `T2_StrategyQA#05` | `c8aa41ddd15fe5b0ef03322782b7acda1d5df1ea6f09374e4e88cf2da09e9c5a` | Always; Yes; Maybe; No | `No` | `No` | Always=0.0; Yes=0.0; Maybe=0.0; No=1.0 | ✔ |
| 22 | `M1_Deposon_TRA|T2_StrategyQA` | 6 | `T2_StrategyQA#06` | `d60e0792d0b4b3cd489b3bd4b7a99298bdb4863230d62e336138e06f04cd36c9` | Always; Yes; No; Maybe | `Yes` | `No` | Always=0.0; Yes=0.0; No=1.0; Maybe=0.0 | · |
| 23 | `M1_Deposon_TRA|T2_StrategyQA` | 7 | `T2_StrategyQA#07` | `640a610246ed4de7ec45cd68a99ed1c7a3a6fde99271d6cf0673c3b5250c8b9a` | Always; Maybe; No; Yes | `No` | `No` | Always=0.0; Maybe=0.0; No=1.0; Yes=0.0 | ✔ |
| 24 | `M1_Deposon_TRA|T2_StrategyQA` | 8 | `T2_StrategyQA#08` | `4d17aa76336bc875ce3c0cdd130eeb740f3274b78aa4483dd3e098e507692efc` | Always; Maybe; Yes; No | `Yes` | `Yes` | Always=0.0; Maybe=0.0; Yes=1.0; No=0.0 | ✔ |
| 25 | `M1_Deposon_TRA|T2_StrategyQA` | 9 | `T2_StrategyQA#09` | `ab584ebe28a683fb20b899e6a5dc86aacf0790f36ea69c8a15835a9eabd6da57` | Maybe; No; Always; Yes | `No` | `Yes` | Maybe=0.0; No=0.0; Always=0.0; Yes=1.0 | · |
| 26 | `M1_Deposon_TRA|T2_StrategyQA` | 10 | `T2_StrategyQA#10` | `f05cd17d8a2ca54a9d1e6410081300a1358b4f4c59613cd10aa9ed31cad23c9c` | No; Always; Maybe; Yes | `No` | `No` | No=1.0; Always=0.0; Maybe=0.0; Yes=0.0 | ✔ |
| 27 | `M1_Deposon_TRA|T2_StrategyQA` | 11 | `T2_StrategyQA#11` | `87f9c55d642429f9bb2e8e3082f118d0c2e270fc1dd09c457a6ec338ad399931` | Yes; Always; Maybe; No | `Yes` | `No` | Yes=0.0; Always=0.0; Maybe=0.0; No=1.0 | · |
| 28 | `M1_Deposon_TRA|T2_StrategyQA` | 12 | `T2_StrategyQA#12` | `75b0e8adb1fd96f377e057b24533ffb895ef91ea39ac24c199625e2c72f711ae` | Yes; Maybe; Always; No | `Yes` | `Yes` | Yes=1.0; Maybe=0.0; Always=0.0; No=0.0 | ✔ |
| 29 | `M1_Deposon_TRA|T2_StrategyQA` | 13 | `T2_StrategyQA#13` | `04b07466b776339e1ba6b2a9365afbdcb23a6b4214fd471792fee7359c032963` | Always; Yes; Maybe; No | `Maybe` | `No` | Always=0.0; Yes=0.0; Maybe=0.0; No=1.0 | · |
| 30 | `M1_Deposon_TRA|T2_StrategyQA` | 14 | `T2_StrategyQA#14` | `20b8ccba8c31eaf2346b814ea999efff5545bf450a0dc02bf0faece329bb7515` | Yes; Always; No; Maybe | `No` | `No` | Yes=0.0; Always=0.0; No=1.0; Maybe=0.0 | ✔ |
| 31 | `M1_Deposon_TRA|T3_Trap` | 0 | `T3_Trap#00` | `71a7e415d2f1080b88a92a8602b8101ccf3f5d03645b56e1bd2268ff0dba725a` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 32 | `M1_Deposon_TRA|T3_Trap` | 1 | `T3_Trap#01` | `23df3b2a1a09b13e6f1a74a810d4fac8d6831ee1d943de2d38131dc1ab80b93c` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 33 | `M1_Deposon_TRA|T3_Trap` | 2 | `T3_Trap#02` | `75394574c9182065b9576a7d46674500dcad5c5150f2ac95f602b89a1930bae9` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 34 | `M1_Deposon_TRA|T3_Trap` | 3 | `T3_Trap#03` | `25b4fc9224972ffb7506c1616c5ed065ef991d7834d42ca83249b87fa32e9043` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 35 | `M1_Deposon_TRA|T3_Trap` | 4 | `T3_Trap#04` | `180aa741d4801c910668fa8f8ad89030d4a167c16e6d51107388920c91412619` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 36 | `M1_Deposon_TRA|T3_Trap` | 5 | `T3_Trap#05` | `c63e0071b3bfa2cc820c39d9cdf6ab80df16860f7f2f213c2bc22a299656fd05` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 37 | `M1_Deposon_TRA|T3_Trap` | 6 | `T3_Trap#06` | `6c3e7dff0ca757686b4fb2ad45f5bc5457b0449505a8e1caa0994cd51f7ed749` | Option B; Option A | `Option B` | `Option A` | Option B=0.5; Option A=1.0 | · |
| 38 | `M1_Deposon_TRA|T3_Trap` | 7 | `T3_Trap#07` | `a70cd5169fda85fb58e4a9695ac4a7990ebb29e82f646b5c958a50dc538b398c` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 39 | `M1_Deposon_TRA|T3_Trap` | 8 | `T3_Trap#08` | `ac9567c79516286dd0224348825f1d03fd79f305b9674794f8389023767528a3` | Option B; Option A | `Option A` | `Option B` | Option B=1.0; Option A=0.5 | · |
| 40 | `M1_Deposon_TRA|T3_Trap` | 9 | `T3_Trap#09` | `34c6901426da274bbc81d4080a38d5f26fcfa56364d6410c45fd8c5dddf2c4ad` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 41 | `M1_Deposon_TRA|T3_Trap` | 10 | `T3_Trap#10` | `45c1aa6e7528df01987b0c7f2fc0b534e7da06a72b308ab262f9f5a23ad6576d` | Option A; Option B | `Option B` | `Option B` | Option A=0.5; Option B=1.0 | ✔ |
| 42 | `M1_Deposon_TRA|T3_Trap` | 11 | `T3_Trap#11` | `9308ce7f312c555c41075eb4121b4165877d8de4a479dbd94c9fce73b3862c0e` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 43 | `M1_Deposon_TRA|T3_Trap` | 12 | `T3_Trap#12` | `2d138acb64a99749f18d34661d672e0d02139016db08bd417d92c99d8d065b0e` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 44 | `M1_Deposon_TRA|T3_Trap` | 13 | `T3_Trap#13` | `7fb518ba808120085320a7210ce330563822e6ff81ace99e3f6c13d8922ae99d` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 45 | `M1_Deposon_TRA|T3_Trap` | 14 | `T3_Trap#14` | `0d03da2c556fc0894f9bf7fabeeb17236938a91c01dbff16c6154f60d9d17a64` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 46 | `M1_Deposon_TRA|T4_2x2` | 0 | `T4_2x2#00` | `effb07b5143d0bfc1f42035ab28d74acb6535bba61352fab800da9f12bc23a62` | Cooperate; Defect | `Defect` | `Defect` | Cooperate=0.0; Defect=1.0 | ✔ |
| 47 | `M1_Deposon_TRA|T4_2x2` | 1 | `T4_2x2#01` | `313fef7364e9380df997b17ea46f8a448292a6537f36e3e2486a3ca5d8baf9b6` | Hawk; Dove | `Dove` | `Dove` | Hawk=0.0; Dove=1.0 | ✔ |
| 48 | `M1_Deposon_TRA|T4_2x2` | 2 | `T4_2x2#02` | `a3b772a8e1ad7187253d65ea83f49601251e4b35b9ec6d02b2eaeeaa90e85da6` | Push; Do not push | `Push` | `Push` | Push=2.0; Do not push=0.0 | ✔ |
| 49 | `M1_Deposon_TRA|T4_2x2` | 3 | `T4_2x2#03` | `4c4e32720591feedc959d5dd3ccaaa1cae7c39d6fbb0de9625f7502a544a398d` | Sport; Comedy | `Sport` | `Sport` | Sport=3.0; Comedy=0.0 | ✔ |
| 50 | `M1_Deposon_TRA|T4_2x2` | 4 | `T4_2x2#05` | `88febe1ec5a2f4762c7f1845ea2c3d19dcab64c9658b04a92256afe76e71d898` | Stag; Hunt | `Stag` | `Stag` | Stag=4.0; Hunt=3.0 | ✔ |
| 51 | `M1_Deposon_TRA|T4_2x2` | 5 | `T4_2x2#06` | `f5e246682ee0a253859862f906d50fa199c58f13c002abed9e4f89a076873905` | Cooperate; Defect | `Cooperate` | `Cooperate` | Cooperate=4.0; Defect=3.0 | ✔ |
| 52 | `M1_Deposon_TRA|T4_2x2` | 6 | `T4_2x2#07` | `8ec8d815ba3b3bd0bc2cb7668cd0fe4295eae4581659738e7a04afe26053ae8c` | Offload; Keep | `Keep` | `Keep` | Offload=1.0; Keep=3.0 | ✔ |
| 53 | `M1_Deposon_TRA|T4_2x2` | 7 | `T4_2x2#08` | `6d343baab95f2fb0ee5eb5528b2be40f2028d3e3230a2df661d5d79295ed46f2` | Home; Away | `Home` | `Away` | Home=0.0; Away=4.0 | · |
| 54 | `M1_Deposon_TRA|T4_2x2` | 8 | `T4_2x2#09` | `17b59e386a3fc4c7f55f1f2fcef2764faa3f4b76a4924bd527f5729688832ea5` | Buy; Hold | `Hold` | `Hold` | Buy=1.0; Hold=3.0 | ✔ |
| 55 | `M1_Deposon_TRA|T4_2x2` | 9 | `T4_2x2#10` | `96259d727be58500ce7189e9fc010ef9f6b1d4184df01696ab5d2febd130c028` | Set A; Set B; Mixed | `Mixed` | `Mixed` | Set A=0.0; Set B=0.0; Mixed=0.5 | ✔ |
| 56 | `M1_Deposon_TRA|T4_2x2` | 10 | `T4_2x2#11` | `499ba3107792f9fac3c86466634f80a3a0680d4c9929f0a005879c9716397f61` | Fund; Withdraw | `Withdraw` | `Withdraw` | Fund=1.0; Withdraw=2.0 | ✔ |
| 57 | `M1_Deposon_TRA|T4_2x2` | 11 | `T4_2x2#12` | `0a1be00fba49108ac2bd4bf8d0bf6ac84ce87c6e9d03c1a059ed241817f2c4ce` | Safe; Bold | `Safe` | `Safe` | Safe=3.0; Bold=2.0 | ✔ |
| 58 | `M1_Deposon_TRA|T4_2x2` | 12 | `T4_2x2#13` | `5e4db6251066fb9f2ca749378bd5304dfce810fe0db28a02ca715325cff03204` | Queue; Jump | `Jump` | `Jump` | Queue=0.0; Jump=3.0 | ✔ |
| 59 | `M1_Deposon_TRA|T4_2x2` | 13 | `T4_2x2#14` | `7233dd9eaa06fdec227899a2b884d9843891d989a60fd0ccf9601f9b6e99931f` | Volunteer; Free-ride | `Volunteer` | `Volunteer` | Volunteer=3.0; Free-ride=2.0 | ✔ |
| 60 | `M1_Deposon_TRA|T5_LowResource` | 0 | `T5_LowResource#00` | `5600ad7c61868d46127023b091ae70acf99832fe35b7e8aef579e468d820cffa` | Dig well; Truck; Ration; Cistern | `Truck` | `Dig well` | Dig well=8; Truck=6; Ration=2; Cistern=5 | · |
| 61 | `M1_Deposon_TRA|T5_LowResource` | 1 | `T5_LowResource#01` | `d866266f6543d4619bd1e59a7cc1e37e00832149cbbd7ddd5b13c8cd60e50aef` | Idle; Shed; Diesel; Rotate | `Diesel` | `Diesel` | Idle=1; Shed=4; Diesel=9; Rotate=6 | ✔ |
| 62 | `M1_Deposon_TRA|T5_LowResource` | 2 | `T5_LowResource#02` | `e7e0108f3de43c4c801184e4ec10eafbce32753075a6d8e77b32e98642bd03c5` | Triage; Bulk; Borrow; Wait | `Triage` | `Triage` | Triage=8; Bulk=5; Borrow=6; Wait=2 | ✔ |
| 63 | `M1_Deposon_TRA|T5_LowResource` | 3 | `T5_LowResource#03` | `c833524c37a84bd6563f1ad44c5130aa7ecfb07471b32c3aba475f767cf2b72f` | Batch; Rent; Cache; Idle | `Idle` | `Rent` | Batch=5; Rent=8; Cache=7; Idle=1 | · |
| 64 | `M1_Deposon_TRA|T5_LowResource` | 4 | `T5_LowResource#04` | `6804b551b5298b8e0526a89d7cb1c01c76b4beb904266f7adc7cad37f55dccf1` | Hold; Release; Waste; Swap | `Swap` | `Swap` | Hold=3; Release=6; Waste=1; Swap=7 | ✔ |
| 65 | `M1_Deposon_TRA|T5_LowResource` | 5 | `T5_LowResource#05` | `5588cb929e3f214d2bc6204c451a8bc1d854d87936831d95dbe4aed74c1d89f1` | Sow shallow; Hold seed; Sow deep; Sow late | `Sow deep` | `Sow deep` | Sow shallow=6; Hold seed=1; Sow deep=8; Sow late=4 | ✔ |
| 66 | `M1_Deposon_TRA|T5_LowResource` | 6 | `T5_LowResource#06` | `c3ee1c7e5ba3844d52c63763ece1273eb9f1ab223aee9a2a8e0d3742a30cddd7` | Recover old; Do nothing; Top up; Part charge | `Top up` | `Top up` | Recover old=4; Do nothing=1; Top up=9; Part charge=6 | ✔ |
| 67 | `M1_Deposon_TRA|T5_LowResource` | 7 | `T5_LowResource#07` | `986ba1e9e0df5046f17c6885e45ae5f1cc4e4beaf36c7bd3ab8ed93c8fc01437` | Transfer stock; Two vials; Wait for resupply; One vial | `Two vials` | `Two vials` | Transfer stock=5; Two vials=8; Wait for resupply=2; One vial=6 | ✔ |
| 68 | `M1_Deposon_TRA|T5_LowResource` | 8 | `T5_LowResource#08` | `052d609e8ae423f774a90fc3a57ac21be4ead29e5b2669ce1590b80c773d5a5c` | Idle; Discharge now; Hold for peak; Trickle charge | `Trickle charge` | `Discharge now` | Idle=1; Discharge now=8; Hold for peak=7; Trickle charge=5 | · |
| 69 | `M1_Deposon_TRA|T5_LowResource` | 9 | `T5_LowResource#09` | `d65ff38d8d09f932fec307ef2b007316776d74c38ab4e9c68b80508eed6e2703` | Substitute sizes; Stop work; Use reserves; Open new box | `Stop work` | `Open new box` | Substitute sizes=5; Stop work=2; Use reserves=6; Open new box=8 | · |
| 70 | `M1_Deposon_TRA|T5_LowResource` | 10 | `T5_LowResource#10` | `defb675e9121e6e87fccc6c8ca9570c785c3aba8a2189a0df5e4af348ffeca1f` | Half load; Delay sailing; Manifest only; Full load | `Manifest only` | `Full load` | Half load=6; Delay sailing=1; Manifest only=4; Full load=8 | · |
| 71 | `M1_Deposon_TRA|T5_LowResource` | 11 | `T5_LowResource#11` | `89dada61f6676a741557dee7622fc311e3c5153f965a02bf45f2f1c47bdc49a7` | Send raw; Split over night; Defer entirely; Compress first | `Send raw` | `Compress first` | Send raw=6; Split over night=5; Defer entirely=2; Compress first=8 | · |
| 72 | `M1_Deposon_TRA|T5_LowResource` | 12 | `T5_LowResource#12` | `21ca360c0e5452f2e80e20df3cd708eec7032db927d3c59a12bcc1d6c991c293` | Dose all now; Test first; Dose at symptoms; No dose | `Dose all now` | `Dose all now` | Dose all now=8; Test first=4; Dose at symptoms=6; No dose=1 | ✔ |
| 73 | `M1_Deposon_TRA|T5_LowResource` | 13 | `T5_LowResource#13` | `086c8b154b48fcb630de84da3fa8a026235f85246de6826653aef9f85e22a2f1` | Run intermittent; Run full load; Shut down; Run part load | `Run part load` | `Run full load` | Run intermittent=4; Run full load=8; Shut down=1; Run part load=7 | · |
| 74 | `M1_Deposon_TRA|T5_LowResource` | 14 | `T5_LowResource#14` | `526980f2cfb2150d80b5f88dde1ea7d7d43163a933bc6542c20eda228612897c` | Ship with ice; Ship with packs; Ship nothing; Ship half packed | `Ship half packed` | `Ship with packs` | Ship with ice=5; Ship with packs=8; Ship nothing=2; Ship half packed=6 | · |
| 75 | `M1_Deposon_TRA|T5_LowResource` | 15 | `T5_LowResource#15` | `dfa62cacc45ee14c3896fac3030161962d4797e2890030f0d684ceefc619b930` | Open full kit; Reuse tray; Open partial kit; Cancel list | `Open partial kit` | `Open full kit` | Open full kit=8; Reuse tray=3; Open partial kit=6; Cancel list=1 | · |
| 76 | `M1_Deposon_TRA|T5_LowResource` | 16 | `T5_LowResource#16` | `90a932d8b2b0b1b0f31f9c237ce1764aef56dad8553455f3580ee0eb25b1c0c9` | Send full trace; Send nothing; Send summary; Send sampled trace | `Send summary` | `Send full trace` | Send full trace=8; Send nothing=1; Send summary=7; Send sampled trace=5 | · |
| 77 | `M1_Deposon_TRA|T5_LowResource` | 17 | `T5_LowResource#17` | `53d7753d720acea3ad909d406bc54bb0b121c5d7e08c4f3e451e92da011ac252` | Truck; Ration; Dig well; Cistern | `Truck` | `Dig well` | Truck=6; Ration=2; Dig well=8; Cistern=5 | · |
| 78 | `M1_Deposon_TRA|T5_LowResource` | 18 | `T5_LowResource#18` | `7f207d2e22965751be7717a2f226397cde9bada1bf2911cbb85faed0ddf902f0` | Idle; Shed; Diesel; Rotate | `Diesel` | `Diesel` | Idle=1; Shed=4; Diesel=9; Rotate=6 | ✔ |
| 79 | `M1_Deposon_TRA|T5_LowResource` | 19 | `T5_LowResource#19` | `1f3d67400d856fd7d6643778409ba9ef3799ac3f5818aa385899fed0498c9baa` | Borrow; Wait; Triage; Bulk | `Borrow` | `Triage` | Borrow=6; Wait=2; Triage=8; Bulk=5 | · |
| 80 | `M2_Greedy|T1_GSM8K` | 0 | `T1_GSM8K#00` | `0c76fc58fd20ceb38f9eec55e3bd33293ececbe9bb8f73e6425d04fc250597de` | 122; 115; 113; 118 | `115` | `115` | 122=0.0; 115=1.0; 113=0.0; 118=0.0 | ✔ |
| 81 | `M2_Greedy|T1_GSM8K` | 1 | `T1_GSM8K#01` | `b60bdd4fa94c257b2840e7cdd8074f781a1513b58f7fdfaf34c025f086c34520` | 259; 250; 260; 254 | `254` | `254` | 259=0.0; 250=0.0; 260=0.0; 254=1.0 | ✔ |
| 82 | `M2_Greedy|T1_GSM8K` | 2 | `T1_GSM8K#02` | `9b0c702712a71394e1a22cfff22f7f64b40aaa8e494c2ffaae76ff35e10c11bf` | 111; 118; 113; 123 | `113` | `113` | 111=0.0; 118=0.0; 113=1.0; 123=0.0 | ✔ |
| 83 | `M2_Greedy|T1_GSM8K` | 3 | `T1_GSM8K#03` | `88512ff7cd8b65e42a3fb2966ce013fa3a8f24e19b4fce183f716e08da760923` | 132; 138; 130; 126 | `130` | `130` | 132=0.0; 138=0.0; 130=1.0; 126=0.0 | ✔ |
| 84 | `M2_Greedy|T1_GSM8K` | 4 | `T1_GSM8K#04` | `d8707f67f03690e588204201162c09251b2f889e1f8790f898be9c3b7d0327e8` | 99; 103; 107; 98 | `99` | `99` | 99=1.0; 103=0.0; 107=0.0; 98=0.0 | ✔ |
| 85 | `M2_Greedy|T1_GSM8K` | 5 | `T1_GSM8K#05` | `b2f7e3ed61140917d2f812362c71834f2283e87fd580f9f6f57c1c92170c08f2` | 627; 628; 633; 623 | `627` | `627` | 627=1.0; 628=0.0; 633=0.0; 623=0.0 | ✔ |
| 86 | `M2_Greedy|T1_GSM8K` | 6 | `T1_GSM8K#06` | `0315860bf255e8fe8e008f473f6adec4c20fc33d4577958d9ba9af3f3c5d28bd` | 152; 149; 159; 151 | `151` | `151` | 152=0.0; 149=0.0; 159=0.0; 151=1.0 | ✔ |
| 87 | `M2_Greedy|T1_GSM8K` | 7 | `T1_GSM8K#07` | `c5c1b113f335fb0a76dadbcec17f6bcb45cfa883365ae165e357700bea20ecd8` | 426; 421; 418; 416 | `418` | `418` | 426=0.0; 421=0.0; 418=1.0; 416=0.0 | ✔ |
| 88 | `M2_Greedy|T1_GSM8K` | 8 | `T1_GSM8K#08` | `71e29171b1a126e77d5743908bf25a6241084c0f9285b97c786815929c65d2fb` | 291; 303; 293; 298 | `293` | `293` | 291=0.0; 303=0.0; 293=1.0; 298=0.0 | ✔ |
| 89 | `M2_Greedy|T1_GSM8K` | 9 | `T1_GSM8K#09` | `f57e2150496b023368f10df8ab4b41ec4d735c06aad4a3f9cfe2255c768c1833` | 451; 460; 454; 456 | `454` | `454` | 451=0.0; 460=0.0; 454=1.0; 456=0.0 | ✔ |
| 90 | `M2_Greedy|T1_GSM8K` | 10 | `T1_GSM8K#10` | `e4c1f39dba919c928ece38afecbbbd3fb9f49b4bb80855b00479bbc48891efcf` | 149; 157; 144; 151 | `149` | `149` | 149=1.0; 157=0.0; 144=0.0; 151=0.0 | ✔ |
| 91 | `M2_Greedy|T1_GSM8K` | 11 | `T1_GSM8K#11` | `6bf1c606078d62417413b35371cade9dba0be1a426b89d149c57c1a10589be4a` | 796; 803; 793; 798 | `796` | `796` | 796=1.0; 803=0.0; 793=0.0; 798=0.0 | ✔ |
| 92 | `M2_Greedy|T1_GSM8K` | 12 | `T1_GSM8K#12` | `fcb36ccf3223b1f5ef7e1533bd720ef5e72a7f2eadff87c0d1f4bc69dbd418cc` | 535; 530; 532; 539 | `532` | `532` | 535=0.0; 530=0.0; 532=1.0; 539=0.0 | ✔ |
| 93 | `M2_Greedy|T1_GSM8K` | 13 | `T1_GSM8K#13` | `2c8abd29b76a82a4448cb8ba13095702ce7a910a986e253a4892d5bf97f68983` | 111; 106; 115; 117 | `111` | `111` | 111=1.0; 106=0.0; 115=0.0; 117=0.0 | ✔ |
| 94 | `M2_Greedy|T1_GSM8K` | 14 | `T1_GSM8K#14` | `8cf47788f52a8784fc9b4aa21bbf7a19a1dfac625c97669df241e6dafbe7f44a` | 455; 456; 465; 454 | `455` | `455` | 455=1.0; 456=0.0; 465=0.0; 454=0.0 | ✔ |
| 95 | `M2_Greedy|T2_StrategyQA` | 0 | `T2_StrategyQA#00` | `eb001e923c9b465dc2981d1fd229dfae544d6e9dacde0b068d4b7d83242c3784` | Always; Maybe; No; Yes | `Yes` | `Yes` | Always=0.0; Maybe=0.0; No=0.0; Yes=1.0 | ✔ |
| 96 | `M2_Greedy|T2_StrategyQA` | 1 | `T2_StrategyQA#01` | `8a96a16fd45bb69ce23490fceeb6ac66c858843405099b8c4b272c15ba5c6862` | Maybe; Yes; Always; No | `No` | `No` | Maybe=0.0; Yes=0.0; Always=0.0; No=1.0 | ✔ |
| 97 | `M2_Greedy|T2_StrategyQA` | 2 | `T2_StrategyQA#02` | `2a530cced264d5942e466c58624700f01225065aaa4c314d26e5270768b4d698` | No; Yes; Always; Maybe | `No` | `No` | No=1.0; Yes=0.0; Always=0.0; Maybe=0.0 | ✔ |
| 98 | `M2_Greedy|T2_StrategyQA` | 3 | `T2_StrategyQA#03` | `1702b00458e43ce2d5620f5a9ebd5400ac49dc672c4d1ebb456765efd23e21af` | Always; No; Maybe; Yes | `Yes` | `Yes` | Always=0.0; No=0.0; Maybe=0.0; Yes=1.0 | ✔ |
| 99 | `M2_Greedy|T2_StrategyQA` | 4 | `T2_StrategyQA#04` | `2c3b008efd27b146f059e64a94874518cb23d16279f84d0e49330c5105e4dac5` | Maybe; Always; Yes; No | `No` | `No` | Maybe=0.0; Always=0.0; Yes=0.0; No=1.0 | ✔ |
| 100 | `M2_Greedy|T2_StrategyQA` | 5 | `T2_StrategyQA#05` | `c8aa41ddd15fe5b0ef03322782b7acda1d5df1ea6f09374e4e88cf2da09e9c5a` | Always; Yes; Maybe; No | `No` | `No` | Always=0.0; Yes=0.0; Maybe=0.0; No=1.0 | ✔ |
| 101 | `M2_Greedy|T2_StrategyQA` | 6 | `T2_StrategyQA#06` | `d60e0792d0b4b3cd489b3bd4b7a99298bdb4863230d62e336138e06f04cd36c9` | Always; Yes; No; Maybe | `No` | `No` | Always=0.0; Yes=0.0; No=1.0; Maybe=0.0 | ✔ |
| 102 | `M2_Greedy|T2_StrategyQA` | 7 | `T2_StrategyQA#07` | `640a610246ed4de7ec45cd68a99ed1c7a3a6fde99271d6cf0673c3b5250c8b9a` | Always; Maybe; No; Yes | `No` | `No` | Always=0.0; Maybe=0.0; No=1.0; Yes=0.0 | ✔ |
| 103 | `M2_Greedy|T2_StrategyQA` | 8 | `T2_StrategyQA#08` | `4d17aa76336bc875ce3c0cdd130eeb740f3274b78aa4483dd3e098e507692efc` | Always; Maybe; Yes; No | `Yes` | `Yes` | Always=0.0; Maybe=0.0; Yes=1.0; No=0.0 | ✔ |
| 104 | `M2_Greedy|T2_StrategyQA` | 9 | `T2_StrategyQA#09` | `ab584ebe28a683fb20b899e6a5dc86aacf0790f36ea69c8a15835a9eabd6da57` | Maybe; No; Always; Yes | `Yes` | `Yes` | Maybe=0.0; No=0.0; Always=0.0; Yes=1.0 | ✔ |
| 105 | `M2_Greedy|T2_StrategyQA` | 10 | `T2_StrategyQA#10` | `f05cd17d8a2ca54a9d1e6410081300a1358b4f4c59613cd10aa9ed31cad23c9c` | No; Always; Maybe; Yes | `No` | `No` | No=1.0; Always=0.0; Maybe=0.0; Yes=0.0 | ✔ |
| 106 | `M2_Greedy|T2_StrategyQA` | 11 | `T2_StrategyQA#11` | `87f9c55d642429f9bb2e8e3082f118d0c2e270fc1dd09c457a6ec338ad399931` | Yes; Always; Maybe; No | `No` | `No` | Yes=0.0; Always=0.0; Maybe=0.0; No=1.0 | ✔ |
| 107 | `M2_Greedy|T2_StrategyQA` | 12 | `T2_StrategyQA#12` | `75b0e8adb1fd96f377e057b24533ffb895ef91ea39ac24c199625e2c72f711ae` | Yes; Maybe; Always; No | `Yes` | `Yes` | Yes=1.0; Maybe=0.0; Always=0.0; No=0.0 | ✔ |
| 108 | `M2_Greedy|T2_StrategyQA` | 13 | `T2_StrategyQA#13` | `04b07466b776339e1ba6b2a9365afbdcb23a6b4214fd471792fee7359c032963` | Always; Yes; Maybe; No | `No` | `No` | Always=0.0; Yes=0.0; Maybe=0.0; No=1.0 | ✔ |
| 109 | `M2_Greedy|T2_StrategyQA` | 14 | `T2_StrategyQA#14` | `20b8ccba8c31eaf2346b814ea999efff5545bf450a0dc02bf0faece329bb7515` | Yes; Always; No; Maybe | `No` | `No` | Yes=0.0; Always=0.0; No=1.0; Maybe=0.0 | ✔ |
| 110 | `M2_Greedy|T3_Trap` | 0 | `T3_Trap#00` | `71a7e415d2f1080b88a92a8602b8101ccf3f5d03645b56e1bd2268ff0dba725a` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 111 | `M2_Greedy|T3_Trap` | 1 | `T3_Trap#01` | `23df3b2a1a09b13e6f1a74a810d4fac8d6831ee1d943de2d38131dc1ab80b93c` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 112 | `M2_Greedy|T3_Trap` | 2 | `T3_Trap#02` | `75394574c9182065b9576a7d46674500dcad5c5150f2ac95f602b89a1930bae9` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 113 | `M2_Greedy|T3_Trap` | 3 | `T3_Trap#03` | `25b4fc9224972ffb7506c1616c5ed065ef991d7834d42ca83249b87fa32e9043` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 114 | `M2_Greedy|T3_Trap` | 4 | `T3_Trap#04` | `180aa741d4801c910668fa8f8ad89030d4a167c16e6d51107388920c91412619` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 115 | `M2_Greedy|T3_Trap` | 5 | `T3_Trap#05` | `c63e0071b3bfa2cc820c39d9cdf6ab80df16860f7f2f213c2bc22a299656fd05` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 116 | `M2_Greedy|T3_Trap` | 6 | `T3_Trap#06` | `6c3e7dff0ca757686b4fb2ad45f5bc5457b0449505a8e1caa0994cd51f7ed749` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 117 | `M2_Greedy|T3_Trap` | 7 | `T3_Trap#07` | `a70cd5169fda85fb58e4a9695ac4a7990ebb29e82f646b5c958a50dc538b398c` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 118 | `M2_Greedy|T3_Trap` | 8 | `T3_Trap#08` | `ac9567c79516286dd0224348825f1d03fd79f305b9674794f8389023767528a3` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 119 | `M2_Greedy|T3_Trap` | 9 | `T3_Trap#09` | `34c6901426da274bbc81d4080a38d5f26fcfa56364d6410c45fd8c5dddf2c4ad` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 120 | `M2_Greedy|T3_Trap` | 10 | `T3_Trap#10` | `45c1aa6e7528df01987b0c7f2fc0b534e7da06a72b308ab262f9f5a23ad6576d` | Option A; Option B | `Option B` | `Option B` | Option A=0.5; Option B=1.0 | ✔ |
| 121 | `M2_Greedy|T3_Trap` | 11 | `T3_Trap#11` | `9308ce7f312c555c41075eb4121b4165877d8de4a479dbd94c9fce73b3862c0e` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 122 | `M2_Greedy|T3_Trap` | 12 | `T3_Trap#12` | `2d138acb64a99749f18d34661d672e0d02139016db08bd417d92c99d8d065b0e` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 123 | `M2_Greedy|T3_Trap` | 13 | `T3_Trap#13` | `7fb518ba808120085320a7210ce330563822e6ff81ace99e3f6c13d8922ae99d` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 124 | `M2_Greedy|T3_Trap` | 14 | `T3_Trap#14` | `0d03da2c556fc0894f9bf7fabeeb17236938a91c01dbff16c6154f60d9d17a64` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 125 | `M2_Greedy|T4_2x2` | 0 | `T4_2x2#00` | `effb07b5143d0bfc1f42035ab28d74acb6535bba61352fab800da9f12bc23a62` | Cooperate; Defect | `Defect` | `Defect` | Cooperate=0.0; Defect=1.0 | ✔ |
| 126 | `M2_Greedy|T4_2x2` | 1 | `T4_2x2#01` | `313fef7364e9380df997b17ea46f8a448292a6537f36e3e2486a3ca5d8baf9b6` | Hawk; Dove | `Dove` | `Dove` | Hawk=0.0; Dove=1.0 | ✔ |
| 127 | `M2_Greedy|T4_2x2` | 2 | `T4_2x2#02` | `a3b772a8e1ad7187253d65ea83f49601251e4b35b9ec6d02b2eaeeaa90e85da6` | Push; Do not push | `Push` | `Push` | Push=2.0; Do not push=0.0 | ✔ |
| 128 | `M2_Greedy|T4_2x2` | 3 | `T4_2x2#03` | `4c4e32720591feedc959d5dd3ccaaa1cae7c39d6fbb0de9625f7502a544a398d` | Sport; Comedy | `Sport` | `Sport` | Sport=3.0; Comedy=0.0 | ✔ |
| 129 | `M2_Greedy|T4_2x2` | 4 | `T4_2x2#05` | `88febe1ec5a2f4762c7f1845ea2c3d19dcab64c9658b04a92256afe76e71d898` | Stag; Hunt | `Stag` | `Stag` | Stag=4.0; Hunt=3.0 | ✔ |
| 130 | `M2_Greedy|T4_2x2` | 5 | `T4_2x2#06` | `f5e246682ee0a253859862f906d50fa199c58f13c002abed9e4f89a076873905` | Cooperate; Defect | `Cooperate` | `Cooperate` | Cooperate=4.0; Defect=3.0 | ✔ |
| 131 | `M2_Greedy|T4_2x2` | 6 | `T4_2x2#07` | `8ec8d815ba3b3bd0bc2cb7668cd0fe4295eae4581659738e7a04afe26053ae8c` | Offload; Keep | `Keep` | `Keep` | Offload=1.0; Keep=3.0 | ✔ |
| 132 | `M2_Greedy|T4_2x2` | 7 | `T4_2x2#08` | `6d343baab95f2fb0ee5eb5528b2be40f2028d3e3230a2df661d5d79295ed46f2` | Home; Away | `Away` | `Away` | Home=0.0; Away=4.0 | ✔ |
| 133 | `M2_Greedy|T4_2x2` | 8 | `T4_2x2#09` | `17b59e386a3fc4c7f55f1f2fcef2764faa3f4b76a4924bd527f5729688832ea5` | Buy; Hold | `Hold` | `Hold` | Buy=1.0; Hold=3.0 | ✔ |
| 134 | `M2_Greedy|T4_2x2` | 9 | `T4_2x2#10` | `96259d727be58500ce7189e9fc010ef9f6b1d4184df01696ab5d2febd130c028` | Set A; Set B; Mixed | `Mixed` | `Mixed` | Set A=0.0; Set B=0.0; Mixed=0.5 | ✔ |
| 135 | `M2_Greedy|T4_2x2` | 10 | `T4_2x2#11` | `499ba3107792f9fac3c86466634f80a3a0680d4c9929f0a005879c9716397f61` | Fund; Withdraw | `Withdraw` | `Withdraw` | Fund=1.0; Withdraw=2.0 | ✔ |
| 136 | `M2_Greedy|T4_2x2` | 11 | `T4_2x2#12` | `0a1be00fba49108ac2bd4bf8d0bf6ac84ce87c6e9d03c1a059ed241817f2c4ce` | Safe; Bold | `Safe` | `Safe` | Safe=3.0; Bold=2.0 | ✔ |
| 137 | `M2_Greedy|T4_2x2` | 12 | `T4_2x2#13` | `5e4db6251066fb9f2ca749378bd5304dfce810fe0db28a02ca715325cff03204` | Queue; Jump | `Jump` | `Jump` | Queue=0.0; Jump=3.0 | ✔ |
| 138 | `M2_Greedy|T4_2x2` | 13 | `T4_2x2#14` | `7233dd9eaa06fdec227899a2b884d9843891d989a60fd0ccf9601f9b6e99931f` | Volunteer; Free-ride | `Volunteer` | `Volunteer` | Volunteer=3.0; Free-ride=2.0 | ✔ |
| 139 | `M2_Greedy|T5_LowResource` | 0 | `T5_LowResource#00` | `5600ad7c61868d46127023b091ae70acf99832fe35b7e8aef579e468d820cffa` | Dig well; Truck; Ration; Cistern | `Dig well` | `Dig well` | Dig well=8; Truck=6; Ration=2; Cistern=5 | ✔ |
| 140 | `M2_Greedy|T5_LowResource` | 1 | `T5_LowResource#01` | `d866266f6543d4619bd1e59a7cc1e37e00832149cbbd7ddd5b13c8cd60e50aef` | Idle; Shed; Diesel; Rotate | `Diesel` | `Diesel` | Idle=1; Shed=4; Diesel=9; Rotate=6 | ✔ |
| 141 | `M2_Greedy|T5_LowResource` | 2 | `T5_LowResource#02` | `e7e0108f3de43c4c801184e4ec10eafbce32753075a6d8e77b32e98642bd03c5` | Triage; Bulk; Borrow; Wait | `Triage` | `Triage` | Triage=8; Bulk=5; Borrow=6; Wait=2 | ✔ |
| 142 | `M2_Greedy|T5_LowResource` | 3 | `T5_LowResource#03` | `c833524c37a84bd6563f1ad44c5130aa7ecfb07471b32c3aba475f767cf2b72f` | Batch; Rent; Cache; Idle | `Rent` | `Rent` | Batch=5; Rent=8; Cache=7; Idle=1 | ✔ |
| 143 | `M2_Greedy|T5_LowResource` | 4 | `T5_LowResource#04` | `6804b551b5298b8e0526a89d7cb1c01c76b4beb904266f7adc7cad37f55dccf1` | Hold; Release; Waste; Swap | `Swap` | `Swap` | Hold=3; Release=6; Waste=1; Swap=7 | ✔ |
| 144 | `M2_Greedy|T5_LowResource` | 5 | `T5_LowResource#05` | `5588cb929e3f214d2bc6204c451a8bc1d854d87936831d95dbe4aed74c1d89f1` | Sow shallow; Hold seed; Sow deep; Sow late | `Sow deep` | `Sow deep` | Sow shallow=6; Hold seed=1; Sow deep=8; Sow late=4 | ✔ |
| 145 | `M2_Greedy|T5_LowResource` | 6 | `T5_LowResource#06` | `c3ee1c7e5ba3844d52c63763ece1273eb9f1ab223aee9a2a8e0d3742a30cddd7` | Recover old; Do nothing; Top up; Part charge | `Top up` | `Top up` | Recover old=4; Do nothing=1; Top up=9; Part charge=6 | ✔ |
| 146 | `M2_Greedy|T5_LowResource` | 7 | `T5_LowResource#07` | `986ba1e9e0df5046f17c6885e45ae5f1cc4e4beaf36c7bd3ab8ed93c8fc01437` | Transfer stock; Two vials; Wait for resupply; One vial | `Two vials` | `Two vials` | Transfer stock=5; Two vials=8; Wait for resupply=2; One vial=6 | ✔ |
| 147 | `M2_Greedy|T5_LowResource` | 8 | `T5_LowResource#08` | `052d609e8ae423f774a90fc3a57ac21be4ead29e5b2669ce1590b80c773d5a5c` | Idle; Discharge now; Hold for peak; Trickle charge | `Discharge now` | `Discharge now` | Idle=1; Discharge now=8; Hold for peak=7; Trickle charge=5 | ✔ |
| 148 | `M2_Greedy|T5_LowResource` | 9 | `T5_LowResource#09` | `d65ff38d8d09f932fec307ef2b007316776d74c38ab4e9c68b80508eed6e2703` | Substitute sizes; Stop work; Use reserves; Open new box | `Open new box` | `Open new box` | Substitute sizes=5; Stop work=2; Use reserves=6; Open new box=8 | ✔ |
| 149 | `M2_Greedy|T5_LowResource` | 10 | `T5_LowResource#10` | `defb675e9121e6e87fccc6c8ca9570c785c3aba8a2189a0df5e4af348ffeca1f` | Half load; Delay sailing; Manifest only; Full load | `Full load` | `Full load` | Half load=6; Delay sailing=1; Manifest only=4; Full load=8 | ✔ |
| 150 | `M2_Greedy|T5_LowResource` | 11 | `T5_LowResource#11` | `89dada61f6676a741557dee7622fc311e3c5153f965a02bf45f2f1c47bdc49a7` | Send raw; Split over night; Defer entirely; Compress first | `Compress first` | `Compress first` | Send raw=6; Split over night=5; Defer entirely=2; Compress first=8 | ✔ |
| 151 | `M2_Greedy|T5_LowResource` | 12 | `T5_LowResource#12` | `21ca360c0e5452f2e80e20df3cd708eec7032db927d3c59a12bcc1d6c991c293` | Dose all now; Test first; Dose at symptoms; No dose | `Dose all now` | `Dose all now` | Dose all now=8; Test first=4; Dose at symptoms=6; No dose=1 | ✔ |
| 152 | `M2_Greedy|T5_LowResource` | 13 | `T5_LowResource#13` | `086c8b154b48fcb630de84da3fa8a026235f85246de6826653aef9f85e22a2f1` | Run intermittent; Run full load; Shut down; Run part load | `Run full load` | `Run full load` | Run intermittent=4; Run full load=8; Shut down=1; Run part load=7 | ✔ |
| 153 | `M2_Greedy|T5_LowResource` | 14 | `T5_LowResource#14` | `526980f2cfb2150d80b5f88dde1ea7d7d43163a933bc6542c20eda228612897c` | Ship with ice; Ship with packs; Ship nothing; Ship half packed | `Ship with packs` | `Ship with packs` | Ship with ice=5; Ship with packs=8; Ship nothing=2; Ship half packed=6 | ✔ |
| 154 | `M2_Greedy|T5_LowResource` | 15 | `T5_LowResource#15` | `dfa62cacc45ee14c3896fac3030161962d4797e2890030f0d684ceefc619b930` | Open full kit; Reuse tray; Open partial kit; Cancel list | `Open full kit` | `Open full kit` | Open full kit=8; Reuse tray=3; Open partial kit=6; Cancel list=1 | ✔ |
| 155 | `M2_Greedy|T5_LowResource` | 16 | `T5_LowResource#16` | `90a932d8b2b0b1b0f31f9c237ce1764aef56dad8553455f3580ee0eb25b1c0c9` | Send full trace; Send nothing; Send summary; Send sampled trace | `Send full trace` | `Send full trace` | Send full trace=8; Send nothing=1; Send summary=7; Send sampled trace=5 | ✔ |
| 156 | `M2_Greedy|T5_LowResource` | 17 | `T5_LowResource#17` | `53d7753d720acea3ad909d406bc54bb0b121c5d7e08c4f3e451e92da011ac252` | Truck; Ration; Dig well; Cistern | `Dig well` | `Dig well` | Truck=6; Ration=2; Dig well=8; Cistern=5 | ✔ |
| 157 | `M2_Greedy|T5_LowResource` | 18 | `T5_LowResource#18` | `7f207d2e22965751be7717a2f226397cde9bada1bf2911cbb85faed0ddf902f0` | Idle; Shed; Diesel; Rotate | `Diesel` | `Diesel` | Idle=1; Shed=4; Diesel=9; Rotate=6 | ✔ |
| 158 | `M2_Greedy|T5_LowResource` | 19 | `T5_LowResource#19` | `1f3d67400d856fd7d6643778409ba9ef3799ac3f5818aa385899fed0498c9baa` | Borrow; Wait; Triage; Bulk | `Triage` | `Triage` | Borrow=6; Wait=2; Triage=8; Bulk=5 | ✔ |
| 159 | `M3_Random|T1_GSM8K` | 0 | `T1_GSM8K#00` | `0c76fc58fd20ceb38f9eec55e3bd33293ececbe9bb8f73e6425d04fc250597de` | 122; 115; 113; 118 | `122` | `115` | 122=0.0; 115=1.0; 113=0.0; 118=0.0 | · |
| 160 | `M3_Random|T1_GSM8K` | 1 | `T1_GSM8K#01` | `b60bdd4fa94c257b2840e7cdd8074f781a1513b58f7fdfaf34c025f086c34520` | 259; 250; 260; 254 | `250` | `254` | 259=0.0; 250=0.0; 260=0.0; 254=1.0 | · |
| 161 | `M3_Random|T1_GSM8K` | 2 | `T1_GSM8K#02` | `9b0c702712a71394e1a22cfff22f7f64b40aaa8e494c2ffaae76ff35e10c11bf` | 111; 118; 113; 123 | `123` | `113` | 111=0.0; 118=0.0; 113=1.0; 123=0.0 | · |
| 162 | `M3_Random|T1_GSM8K` | 3 | `T1_GSM8K#03` | `88512ff7cd8b65e42a3fb2966ce013fa3a8f24e19b4fce183f716e08da760923` | 132; 138; 130; 126 | `130` | `130` | 132=0.0; 138=0.0; 130=1.0; 126=0.0 | ✔ |
| 163 | `M3_Random|T1_GSM8K` | 4 | `T1_GSM8K#04` | `d8707f67f03690e588204201162c09251b2f889e1f8790f898be9c3b7d0327e8` | 99; 103; 107; 98 | `98` | `99` | 99=1.0; 103=0.0; 107=0.0; 98=0.0 | · |
| 164 | `M3_Random|T1_GSM8K` | 5 | `T1_GSM8K#05` | `b2f7e3ed61140917d2f812362c71834f2283e87fd580f9f6f57c1c92170c08f2` | 627; 628; 633; 623 | `627` | `627` | 627=1.0; 628=0.0; 633=0.0; 623=0.0 | ✔ |
| 165 | `M3_Random|T1_GSM8K` | 6 | `T1_GSM8K#06` | `0315860bf255e8fe8e008f473f6adec4c20fc33d4577958d9ba9af3f3c5d28bd` | 152; 149; 159; 151 | `152` | `151` | 152=0.0; 149=0.0; 159=0.0; 151=1.0 | · |
| 166 | `M3_Random|T1_GSM8K` | 7 | `T1_GSM8K#07` | `c5c1b113f335fb0a76dadbcec17f6bcb45cfa883365ae165e357700bea20ecd8` | 426; 421; 418; 416 | `416` | `418` | 426=0.0; 421=0.0; 418=1.0; 416=0.0 | · |
| 167 | `M3_Random|T1_GSM8K` | 8 | `T1_GSM8K#08` | `71e29171b1a126e77d5743908bf25a6241084c0f9285b97c786815929c65d2fb` | 291; 303; 293; 298 | `303` | `293` | 291=0.0; 303=0.0; 293=1.0; 298=0.0 | · |
| 168 | `M3_Random|T1_GSM8K` | 9 | `T1_GSM8K#09` | `f57e2150496b023368f10df8ab4b41ec4d735c06aad4a3f9cfe2255c768c1833` | 451; 460; 454; 456 | `454` | `454` | 451=0.0; 460=0.0; 454=1.0; 456=0.0 | ✔ |
| 169 | `M3_Random|T1_GSM8K` | 10 | `T1_GSM8K#10` | `e4c1f39dba919c928ece38afecbbbd3fb9f49b4bb80855b00479bbc48891efcf` | 149; 157; 144; 151 | `149` | `149` | 149=1.0; 157=0.0; 144=0.0; 151=0.0 | ✔ |
| 170 | `M3_Random|T1_GSM8K` | 11 | `T1_GSM8K#11` | `6bf1c606078d62417413b35371cade9dba0be1a426b89d149c57c1a10589be4a` | 796; 803; 793; 798 | `798` | `796` | 796=1.0; 803=0.0; 793=0.0; 798=0.0 | · |
| 171 | `M3_Random|T1_GSM8K` | 12 | `T1_GSM8K#12` | `fcb36ccf3223b1f5ef7e1533bd720ef5e72a7f2eadff87c0d1f4bc69dbd418cc` | 535; 530; 532; 539 | `530` | `532` | 535=0.0; 530=0.0; 532=1.0; 539=0.0 | · |
| 172 | `M3_Random|T1_GSM8K` | 13 | `T1_GSM8K#13` | `2c8abd29b76a82a4448cb8ba13095702ce7a910a986e253a4892d5bf97f68983` | 111; 106; 115; 117 | `115` | `111` | 111=1.0; 106=0.0; 115=0.0; 117=0.0 | · |
| 173 | `M3_Random|T1_GSM8K` | 14 | `T1_GSM8K#14` | `8cf47788f52a8784fc9b4aa21bbf7a19a1dfac625c97669df241e6dafbe7f44a` | 455; 456; 465; 454 | `454` | `455` | 455=1.0; 456=0.0; 465=0.0; 454=0.0 | · |
| 174 | `M3_Random|T2_StrategyQA` | 0 | `T2_StrategyQA#00` | `eb001e923c9b465dc2981d1fd229dfae544d6e9dacde0b068d4b7d83242c3784` | Always; Maybe; No; Yes | `Yes` | `Yes` | Always=0.0; Maybe=0.0; No=0.0; Yes=1.0 | ✔ |
| 175 | `M3_Random|T2_StrategyQA` | 1 | `T2_StrategyQA#01` | `8a96a16fd45bb69ce23490fceeb6ac66c858843405099b8c4b272c15ba5c6862` | Maybe; Yes; Always; No | `Always` | `No` | Maybe=0.0; Yes=0.0; Always=0.0; No=1.0 | · |
| 176 | `M3_Random|T2_StrategyQA` | 2 | `T2_StrategyQA#02` | `2a530cced264d5942e466c58624700f01225065aaa4c314d26e5270768b4d698` | No; Yes; Always; Maybe | `No` | `No` | No=1.0; Yes=0.0; Always=0.0; Maybe=0.0 | ✔ |
| 177 | `M3_Random|T2_StrategyQA` | 3 | `T2_StrategyQA#03` | `1702b00458e43ce2d5620f5a9ebd5400ac49dc672c4d1ebb456765efd23e21af` | Always; No; Maybe; Yes | `No` | `Yes` | Always=0.0; No=0.0; Maybe=0.0; Yes=1.0 | · |
| 178 | `M3_Random|T2_StrategyQA` | 4 | `T2_StrategyQA#04` | `2c3b008efd27b146f059e64a94874518cb23d16279f84d0e49330c5105e4dac5` | Maybe; Always; Yes; No | `Yes` | `No` | Maybe=0.0; Always=0.0; Yes=0.0; No=1.0 | · |
| 179 | `M3_Random|T2_StrategyQA` | 5 | `T2_StrategyQA#05` | `c8aa41ddd15fe5b0ef03322782b7acda1d5df1ea6f09374e4e88cf2da09e9c5a` | Always; Yes; Maybe; No | `Always` | `No` | Always=0.0; Yes=0.0; Maybe=0.0; No=1.0 | · |
| 180 | `M3_Random|T2_StrategyQA` | 6 | `T2_StrategyQA#06` | `d60e0792d0b4b3cd489b3bd4b7a99298bdb4863230d62e336138e06f04cd36c9` | Always; Yes; No; Maybe | `No` | `No` | Always=0.0; Yes=0.0; No=1.0; Maybe=0.0 | ✔ |
| 181 | `M3_Random|T2_StrategyQA` | 7 | `T2_StrategyQA#07` | `640a610246ed4de7ec45cd68a99ed1c7a3a6fde99271d6cf0673c3b5250c8b9a` | Always; Maybe; No; Yes | `Maybe` | `No` | Always=0.0; Maybe=0.0; No=1.0; Yes=0.0 | · |
| 182 | `M3_Random|T2_StrategyQA` | 8 | `T2_StrategyQA#08` | `4d17aa76336bc875ce3c0cdd130eeb740f3274b78aa4483dd3e098e507692efc` | Always; Maybe; Yes; No | `Maybe` | `Yes` | Always=0.0; Maybe=0.0; Yes=1.0; No=0.0 | · |
| 183 | `M3_Random|T2_StrategyQA` | 9 | `T2_StrategyQA#09` | `ab584ebe28a683fb20b899e6a5dc86aacf0790f36ea69c8a15835a9eabd6da57` | Maybe; No; Always; Yes | `Maybe` | `Yes` | Maybe=0.0; No=0.0; Always=0.0; Yes=1.0 | · |
| 184 | `M3_Random|T2_StrategyQA` | 10 | `T2_StrategyQA#10` | `f05cd17d8a2ca54a9d1e6410081300a1358b4f4c59613cd10aa9ed31cad23c9c` | No; Always; Maybe; Yes | `Maybe` | `No` | No=1.0; Always=0.0; Maybe=0.0; Yes=0.0 | · |
| 185 | `M3_Random|T2_StrategyQA` | 11 | `T2_StrategyQA#11` | `87f9c55d642429f9bb2e8e3082f118d0c2e270fc1dd09c457a6ec338ad399931` | Yes; Always; Maybe; No | `Maybe` | `No` | Yes=0.0; Always=0.0; Maybe=0.0; No=1.0 | · |
| 186 | `M3_Random|T2_StrategyQA` | 12 | `T2_StrategyQA#12` | `75b0e8adb1fd96f377e057b24533ffb895ef91ea39ac24c199625e2c72f711ae` | Yes; Maybe; Always; No | `Always` | `Yes` | Yes=1.0; Maybe=0.0; Always=0.0; No=0.0 | · |
| 187 | `M3_Random|T2_StrategyQA` | 13 | `T2_StrategyQA#13` | `04b07466b776339e1ba6b2a9365afbdcb23a6b4214fd471792fee7359c032963` | Always; Yes; Maybe; No | `Always` | `No` | Always=0.0; Yes=0.0; Maybe=0.0; No=1.0 | · |
| 188 | `M3_Random|T2_StrategyQA` | 14 | `T2_StrategyQA#14` | `20b8ccba8c31eaf2346b814ea999efff5545bf450a0dc02bf0faece329bb7515` | Yes; Always; No; Maybe | `Maybe` | `No` | Yes=0.0; Always=0.0; No=1.0; Maybe=0.0 | · |
| 189 | `M3_Random|T3_Trap` | 0 | `T3_Trap#00` | `71a7e415d2f1080b88a92a8602b8101ccf3f5d03645b56e1bd2268ff0dba725a` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 190 | `M3_Random|T3_Trap` | 1 | `T3_Trap#01` | `23df3b2a1a09b13e6f1a74a810d4fac8d6831ee1d943de2d38131dc1ab80b93c` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 191 | `M3_Random|T3_Trap` | 2 | `T3_Trap#02` | `75394574c9182065b9576a7d46674500dcad5c5150f2ac95f602b89a1930bae9` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 192 | `M3_Random|T3_Trap` | 3 | `T3_Trap#03` | `25b4fc9224972ffb7506c1616c5ed065ef991d7834d42ca83249b87fa32e9043` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 193 | `M3_Random|T3_Trap` | 4 | `T3_Trap#04` | `180aa741d4801c910668fa8f8ad89030d4a167c16e6d51107388920c91412619` | Option B; Option A | `Option B` | `Option A` | Option B=0.5; Option A=1.0 | · |
| 194 | `M3_Random|T3_Trap` | 5 | `T3_Trap#05` | `c63e0071b3bfa2cc820c39d9cdf6ab80df16860f7f2f213c2bc22a299656fd05` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 195 | `M3_Random|T3_Trap` | 6 | `T3_Trap#06` | `6c3e7dff0ca757686b4fb2ad45f5bc5457b0449505a8e1caa0994cd51f7ed749` | Option B; Option A | `Option B` | `Option A` | Option B=0.5; Option A=1.0 | · |
| 196 | `M3_Random|T3_Trap` | 7 | `T3_Trap#07` | `a70cd5169fda85fb58e4a9695ac4a7990ebb29e82f646b5c958a50dc538b398c` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 197 | `M3_Random|T3_Trap` | 8 | `T3_Trap#08` | `ac9567c79516286dd0224348825f1d03fd79f305b9674794f8389023767528a3` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 198 | `M3_Random|T3_Trap` | 9 | `T3_Trap#09` | `34c6901426da274bbc81d4080a38d5f26fcfa56364d6410c45fd8c5dddf2c4ad` | Option B; Option A | `Option A` | `Option A` | Option B=0.5; Option A=1.0 | ✔ |
| 199 | `M3_Random|T3_Trap` | 10 | `T3_Trap#10` | `45c1aa6e7528df01987b0c7f2fc0b534e7da06a72b308ab262f9f5a23ad6576d` | Option A; Option B | `Option B` | `Option B` | Option A=0.5; Option B=1.0 | ✔ |
| 200 | `M3_Random|T3_Trap` | 11 | `T3_Trap#11` | `9308ce7f312c555c41075eb4121b4165877d8de4a479dbd94c9fce73b3862c0e` | Option B; Option A | `Option A` | `Option B` | Option B=1.0; Option A=0.5 | · |
| 201 | `M3_Random|T3_Trap` | 12 | `T3_Trap#12` | `2d138acb64a99749f18d34661d672e0d02139016db08bd417d92c99d8d065b0e` | Option A; Option B | `Option A` | `Option A` | Option A=1.0; Option B=0.5 | ✔ |
| 202 | `M3_Random|T3_Trap` | 13 | `T3_Trap#13` | `7fb518ba808120085320a7210ce330563822e6ff81ace99e3f6c13d8922ae99d` | Option B; Option A | `Option B` | `Option B` | Option B=1.0; Option A=0.5 | ✔ |
| 203 | `M3_Random|T3_Trap` | 14 | `T3_Trap#14` | `0d03da2c556fc0894f9bf7fabeeb17236938a91c01dbff16c6154f60d9d17a64` | Option A; Option B | `Option B` | `Option A` | Option A=1.0; Option B=0.5 | · |
| 204 | `M3_Random|T4_2x2` | 0 | `T4_2x2#00` | `effb07b5143d0bfc1f42035ab28d74acb6535bba61352fab800da9f12bc23a62` | Cooperate; Defect | `Defect` | `Defect` | Cooperate=0.0; Defect=1.0 | ✔ |
| 205 | `M3_Random|T4_2x2` | 1 | `T4_2x2#01` | `313fef7364e9380df997b17ea46f8a448292a6537f36e3e2486a3ca5d8baf9b6` | Hawk; Dove | `Dove` | `Dove` | Hawk=0.0; Dove=1.0 | ✔ |
| 206 | `M3_Random|T4_2x2` | 2 | `T4_2x2#02` | `a3b772a8e1ad7187253d65ea83f49601251e4b35b9ec6d02b2eaeeaa90e85da6` | Push; Do not push | `Do not push` | `Push` | Push=2.0; Do not push=0.0 | · |
| 207 | `M3_Random|T4_2x2` | 3 | `T4_2x2#03` | `4c4e32720591feedc959d5dd3ccaaa1cae7c39d6fbb0de9625f7502a544a398d` | Sport; Comedy | `Sport` | `Sport` | Sport=3.0; Comedy=0.0 | ✔ |
| 208 | `M3_Random|T4_2x2` | 4 | `T4_2x2#05` | `88febe1ec5a2f4762c7f1845ea2c3d19dcab64c9658b04a92256afe76e71d898` | Stag; Hunt | `Stag` | `Stag` | Stag=4.0; Hunt=3.0 | ✔ |
| 209 | `M3_Random|T4_2x2` | 5 | `T4_2x2#06` | `f5e246682ee0a253859862f906d50fa199c58f13c002abed9e4f89a076873905` | Cooperate; Defect | `Cooperate` | `Cooperate` | Cooperate=4.0; Defect=3.0 | ✔ |
| 210 | `M3_Random|T4_2x2` | 6 | `T4_2x2#07` | `8ec8d815ba3b3bd0bc2cb7668cd0fe4295eae4581659738e7a04afe26053ae8c` | Offload; Keep | `Keep` | `Keep` | Offload=1.0; Keep=3.0 | ✔ |
| 211 | `M3_Random|T4_2x2` | 7 | `T4_2x2#08` | `6d343baab95f2fb0ee5eb5528b2be40f2028d3e3230a2df661d5d79295ed46f2` | Home; Away | `Away` | `Away` | Home=0.0; Away=4.0 | ✔ |
| 212 | `M3_Random|T4_2x2` | 8 | `T4_2x2#09` | `17b59e386a3fc4c7f55f1f2fcef2764faa3f4b76a4924bd527f5729688832ea5` | Buy; Hold | `Hold` | `Hold` | Buy=1.0; Hold=3.0 | ✔ |
| 213 | `M3_Random|T4_2x2` | 9 | `T4_2x2#10` | `96259d727be58500ce7189e9fc010ef9f6b1d4184df01696ab5d2febd130c028` | Set A; Set B; Mixed | `Set B` | `Mixed` | Set A=0.0; Set B=0.0; Mixed=0.5 | · |
| 214 | `M3_Random|T4_2x2` | 10 | `T4_2x2#11` | `499ba3107792f9fac3c86466634f80a3a0680d4c9929f0a005879c9716397f61` | Fund; Withdraw | `Withdraw` | `Withdraw` | Fund=1.0; Withdraw=2.0 | ✔ |
| 215 | `M3_Random|T4_2x2` | 11 | `T4_2x2#12` | `0a1be00fba49108ac2bd4bf8d0bf6ac84ce87c6e9d03c1a059ed241817f2c4ce` | Safe; Bold | `Bold` | `Safe` | Safe=3.0; Bold=2.0 | · |
| 216 | `M3_Random|T4_2x2` | 12 | `T4_2x2#13` | `5e4db6251066fb9f2ca749378bd5304dfce810fe0db28a02ca715325cff03204` | Queue; Jump | `Jump` | `Jump` | Queue=0.0; Jump=3.0 | ✔ |
| 217 | `M3_Random|T4_2x2` | 13 | `T4_2x2#14` | `7233dd9eaa06fdec227899a2b884d9843891d989a60fd0ccf9601f9b6e99931f` | Volunteer; Free-ride | `Volunteer` | `Volunteer` | Volunteer=3.0; Free-ride=2.0 | ✔ |
| 218 | `M3_Random|T5_LowResource` | 0 | `T5_LowResource#00` | `5600ad7c61868d46127023b091ae70acf99832fe35b7e8aef579e468d820cffa` | Dig well; Truck; Ration; Cistern | `Ration` | `Dig well` | Dig well=8; Truck=6; Ration=2; Cistern=5 | · |
| 219 | `M3_Random|T5_LowResource` | 1 | `T5_LowResource#01` | `d866266f6543d4619bd1e59a7cc1e37e00832149cbbd7ddd5b13c8cd60e50aef` | Idle; Shed; Diesel; Rotate | `Shed` | `Diesel` | Idle=1; Shed=4; Diesel=9; Rotate=6 | · |
| 220 | `M3_Random|T5_LowResource` | 2 | `T5_LowResource#02` | `e7e0108f3de43c4c801184e4ec10eafbce32753075a6d8e77b32e98642bd03c5` | Triage; Bulk; Borrow; Wait | `Borrow` | `Triage` | Triage=8; Bulk=5; Borrow=6; Wait=2 | · |
| 221 | `M3_Random|T5_LowResource` | 3 | `T5_LowResource#03` | `c833524c37a84bd6563f1ad44c5130aa7ecfb07471b32c3aba475f767cf2b72f` | Batch; Rent; Cache; Idle | `Rent` | `Rent` | Batch=5; Rent=8; Cache=7; Idle=1 | ✔ |
| 222 | `M3_Random|T5_LowResource` | 4 | `T5_LowResource#04` | `6804b551b5298b8e0526a89d7cb1c01c76b4beb904266f7adc7cad37f55dccf1` | Hold; Release; Waste; Swap | `Hold` | `Swap` | Hold=3; Release=6; Waste=1; Swap=7 | · |
| 223 | `M3_Random|T5_LowResource` | 5 | `T5_LowResource#05` | `5588cb929e3f214d2bc6204c451a8bc1d854d87936831d95dbe4aed74c1d89f1` | Sow shallow; Hold seed; Sow deep; Sow late | `Hold seed` | `Sow deep` | Sow shallow=6; Hold seed=1; Sow deep=8; Sow late=4 | · |
| 224 | `M3_Random|T5_LowResource` | 6 | `T5_LowResource#06` | `c3ee1c7e5ba3844d52c63763ece1273eb9f1ab223aee9a2a8e0d3742a30cddd7` | Recover old; Do nothing; Top up; Part charge | `Top up` | `Top up` | Recover old=4; Do nothing=1; Top up=9; Part charge=6 | ✔ |
| 225 | `M3_Random|T5_LowResource` | 7 | `T5_LowResource#07` | `986ba1e9e0df5046f17c6885e45ae5f1cc4e4beaf36c7bd3ab8ed93c8fc01437` | Transfer stock; Two vials; Wait for resupply; One vial | `Transfer stock` | `Two vials` | Transfer stock=5; Two vials=8; Wait for resupply=2; One vial=6 | · |
| 226 | `M3_Random|T5_LowResource` | 8 | `T5_LowResource#08` | `052d609e8ae423f774a90fc3a57ac21be4ead29e5b2669ce1590b80c773d5a5c` | Idle; Discharge now; Hold for peak; Trickle charge | `Trickle charge` | `Discharge now` | Idle=1; Discharge now=8; Hold for peak=7; Trickle charge=5 | · |
| 227 | `M3_Random|T5_LowResource` | 9 | `T5_LowResource#09` | `d65ff38d8d09f932fec307ef2b007316776d74c38ab4e9c68b80508eed6e2703` | Substitute sizes; Stop work; Use reserves; Open new box | `Open new box` | `Open new box` | Substitute sizes=5; Stop work=2; Use reserves=6; Open new box=8 | ✔ |
| 228 | `M3_Random|T5_LowResource` | 10 | `T5_LowResource#10` | `defb675e9121e6e87fccc6c8ca9570c785c3aba8a2189a0df5e4af348ffeca1f` | Half load; Delay sailing; Manifest only; Full load | `Half load` | `Full load` | Half load=6; Delay sailing=1; Manifest only=4; Full load=8 | · |
| 229 | `M3_Random|T5_LowResource` | 11 | `T5_LowResource#11` | `89dada61f6676a741557dee7622fc311e3c5153f965a02bf45f2f1c47bdc49a7` | Send raw; Split over night; Defer entirely; Compress first | `Split over night` | `Compress first` | Send raw=6; Split over night=5; Defer entirely=2; Compress first=8 | · |
| 230 | `M3_Random|T5_LowResource` | 12 | `T5_LowResource#12` | `21ca360c0e5452f2e80e20df3cd708eec7032db927d3c59a12bcc1d6c991c293` | Dose all now; Test first; Dose at symptoms; No dose | `Dose at symptoms` | `Dose all now` | Dose all now=8; Test first=4; Dose at symptoms=6; No dose=1 | · |
| 231 | `M3_Random|T5_LowResource` | 13 | `T5_LowResource#13` | `086c8b154b48fcb630de84da3fa8a026235f85246de6826653aef9f85e22a2f1` | Run intermittent; Run full load; Shut down; Run part load | `Run part load` | `Run full load` | Run intermittent=4; Run full load=8; Shut down=1; Run part load=7 | · |
| 232 | `M3_Random|T5_LowResource` | 14 | `T5_LowResource#14` | `526980f2cfb2150d80b5f88dde1ea7d7d43163a933bc6542c20eda228612897c` | Ship with ice; Ship with packs; Ship nothing; Ship half packed | `Ship half packed` | `Ship with packs` | Ship with ice=5; Ship with packs=8; Ship nothing=2; Ship half packed=6 | · |
| 233 | `M3_Random|T5_LowResource` | 15 | `T5_LowResource#15` | `dfa62cacc45ee14c3896fac3030161962d4797e2890030f0d684ceefc619b930` | Open full kit; Reuse tray; Open partial kit; Cancel list | `Open full kit` | `Open full kit` | Open full kit=8; Reuse tray=3; Open partial kit=6; Cancel list=1 | ✔ |
| 234 | `M3_Random|T5_LowResource` | 16 | `T5_LowResource#16` | `90a932d8b2b0b1b0f31f9c237ce1764aef56dad8553455f3580ee0eb25b1c0c9` | Send full trace; Send nothing; Send summary; Send sampled trace | `Send summary` | `Send full trace` | Send full trace=8; Send nothing=1; Send summary=7; Send sampled trace=5 | · |
| 235 | `M3_Random|T5_LowResource` | 17 | `T5_LowResource#17` | `53d7753d720acea3ad909d406bc54bb0b121c5d7e08c4f3e451e92da011ac252` | Truck; Ration; Dig well; Cistern | `Truck` | `Dig well` | Truck=6; Ration=2; Dig well=8; Cistern=5 | · |
| 236 | `M3_Random|T5_LowResource` | 18 | `T5_LowResource#18` | `7f207d2e22965751be7717a2f226397cde9bada1bf2911cbb85faed0ddf902f0` | Idle; Shed; Diesel; Rotate | `Shed` | `Diesel` | Idle=1; Shed=4; Diesel=9; Rotate=6 | · |
| 237 | `M3_Random|T5_LowResource` | 19 | `T5_LowResource#19` | `1f3d67400d856fd7d6643778409ba9ef3799ac3f5818aa385899fed0498c9baa` | Borrow; Wait; Triage; Bulk | `Bulk` | `Triage` | Borrow=6; Wait=2; Triage=8; Bulk=5 | · |

## §3 排除面（`T4_2x2#04`·**每格 1 决策**·共 **3** 行 ＝ 3 机制格 × 1）

> 📌 排除依据（照录在册）：v147-Q2（`T4_2x2#04`：best ＝ 0 ⇒ v(o)/best 未定义）｜📌 面之共享性：族内素材面为**逐族生成一次·3 机制共享**（照录在册主实验之 `build_face`）⇒ 同一排除决策在 3 个机制格各出现一次（3 行）｜📌 排除**前**逐格值 ＝ 排除后 ＋ 1（T4 族）｜📌 在册载「rows_excluded ＝ 12（4 档 × 3 机制格）」——本组域① 之档为**单档**⇒ 本组之排除行数 ＝ **3**（在册之 12 含在册主实验之 4 档并跑面）·两者之差**在册可核**（见读出件 §4-3）。

| cell_id（机制×族） | face_cell_id | prompt_sha256（全文 hex） | options | correct | value | 排除依据 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `M1_Deposon_TRA|T4_2x2` | `T4_2x2#04` | `84b894dddfaa2a98f1354cc45a9bfc0c0802bb82869f93fb0b185b5b48af55fd` | Heads; Tails; Mixed | `Mixed` | Heads=-1.0; Tails=-1.0; Mixed=0.0 | v147-Q2（T4_2x2#04：best ＝ 0 ⇒ v(o)/best 未定义） |
| `M2_Greedy|T4_2x2` | `T4_2x2#04` | `84b894dddfaa2a98f1354cc45a9bfc0c0802bb82869f93fb0b185b5b48af55fd` | Heads; Tails; Mixed | `Mixed` | Heads=-1.0; Tails=-1.0; Mixed=0.0 | v147-Q2（T4_2x2#04：best ＝ 0 ⇒ v(o)/best 未定义） |
| `M3_Random|T4_2x2` | `T4_2x2#04` | `84b894dddfaa2a98f1354cc45a9bfc0c0802bb82869f93fb0b185b5b48af55fd` | Heads; Tails; Mixed | `Mixed` | Heads=-1.0; Tails=-1.0; Mixed=0.0 | v147-Q2（T4_2x2#04：best ＝ 0 ⇒ v(o)/best 未定义） |

## §4 逐格留痕行数（`K-HEN-7` 之「逐格值 ＝ 留痕条目数」之核对面）

| cell_id（机制×族） | 留痕行数（本件实点） | 逐格 `H_exact`（排除后） | 差 |
| :-- | --: | --: | :-: |
| `M1_Deposon_TRA|T1_GSM8K` | 15 | 15 | 0 |
| `M1_Deposon_TRA|T2_StrategyQA` | 15 | 15 | 0 |
| `M1_Deposon_TRA|T3_Trap` | 15 | 15 | 0 |
| `M1_Deposon_TRA|T4_2x2` | 14 | 14 | 0 |
| `M1_Deposon_TRA|T5_LowResource` | 20 | 20 | 0 |
| `M2_Greedy|T1_GSM8K` | 15 | 15 | 0 |
| `M2_Greedy|T2_StrategyQA` | 15 | 15 | 0 |
| `M2_Greedy|T3_Trap` | 15 | 15 | 0 |
| `M2_Greedy|T4_2x2` | 14 | 14 | 0 |
| `M2_Greedy|T5_LowResource` | 20 | 20 | 0 |
| `M3_Random|T1_GSM8K` | 15 | 15 | 0 |
| `M3_Random|T2_StrategyQA` | 15 | 15 | 0 |
| `M3_Random|T3_Trap` | 15 | 15 | 0 |
| `M3_Random|T4_2x2` | 14 | 14 | 0 |
| `M3_Random|T5_LowResource` | 20 | 20 | 0 |

> 📌 合计：留痕行数 **237** ＝ 3 机制 × （15＋15＋15＋**14**＋20 ＝ 79）；排除前行数 ＝ **240**（3 × 80）｜📌 **逐格差 ＝ 0**（15/15 格）｜📌 排除面另计 **3** 行（不计入留痕行数·因其不属该格之决策）。

## §5 指纹自报（落盘后由本棒**独立回读**实测 · 自引用不可行 ⇒ 载于落账方之报回面）

| 项 | 值 |
| :-- | :-- |
| **本件之落盘后实测** | SHA-12／bytes／**BOM＝0**／**CR＝0**／**VT＝0**／**U+FFFD＝0** —— **载于落账方（worker）之报回面**（照录拟案 §11-2 之体例：自引用不可行）｜📌 本件之**读出件**路径 ＝ `results\_h_exact_enum_run_reading_2026_10_21.md`（其 SHA-12 同样载于报回面·两件互引之闭合以报回面为准） |
| **封堵面（0 联网·0 LLM）** | 本棒执行进程内：`socket.socket` ＝ 抛错替身（实例化即抛）·已载网络模块 ＝ **[]**（空）·已载 LLM 模块 ＝ **[]**（空·⛔ 0 `import llm_client`）·`run()` 全程 0 调 LLM（`self.llm_client` 存而不用于 `run()` 之全文核实见在册拟案 §5-1） |

---

**件终** ｜ 落账方 ＝ **worker**（棒 `H-EXACT-ENUM-D1-TRACE` · agent worker）｜ **2026-10-21 夜**｜ **令源** ＝ v208-Q1（授权）＋ v218-Q1/Q2/Q3/Q4（跑禁解·域③·15 格·不计）＋ v219-Q1（拟案核准生效即锁）＋ v219-Q2（域①先跑）｜ **状态** ＝ 留痕已落·**判定面按 `K-HEN-9`／`K-HEN-10` 处置语（见读出件 §6）** ｜ ⛔ 0 落五终判 · 0 闭 KD · 0 宣告段毕 · 0 宣告可开跑 · 0 回改既有件一字 · 0 移动／改名／删除 · 0 新建目录 · 0 LLM 调用 · 0 联网 · 0 读 key · 0 触归档区 · 0 新建或合并派生 JSON。
