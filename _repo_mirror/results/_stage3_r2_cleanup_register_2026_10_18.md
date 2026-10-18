# ③段-R2「夜间整理文件夹」之**清理/转移登记件**（2026-10-18）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_stage3_r2_cleanup_register_2026_10_18.md` |
| **件性质** | 执行登记件（判据冻结件指纹 ＋ 两区前后账 ＋ 四型清单 ＋ 转移映射 ＋ 保留面 ＋ 停手候裁 ＋ 账目校正 ＋ 字节级自报）· **非判定件** ⇒ ⛔ 0 落五终判 · ⛔ 0 宣告段毕/①毕 · ⛔ 0 代 PI 裁 |
| **权源** | `results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md` §1/§2（`7439157b7be4`）＋ `results/_stage_sequence_ruling_effect_2026_10_17.md` §3-2（`b582bde59d6d`，与派工给定指纹一致） |
| **区域** | 仅 `deposon-repo` ＋ `deposon-sub`｜⛔ 0 触 `D:\私人资料\_non_upload_local_archive`｜⛔ 0 触 `D:\私人资料\GLM` |
| **落前占位实测** | `Test-Path` ＝ `False`；`results\*stage3_r2*` glob ＝ **0** |

---

## §0 一句话结论

清走 **96 件**（判据四型 **89** ＋ 本棒自清 **7**）**全部走可恢复通道**（回收站 `$I`/`$R` 成对验道 **96/96**）、跨区转移 **166 件**中 **141 件**净转移（逐件 SHA-256 移动前后 **MATCH**）、**25 件因检出活代码功能引用而当场回退原位**（棒自捕之仪器缺陷所致，见 §7-1）、**残余功能断链 0**；两区比 **3.720:1 → 3.354:1**，🔴 **≤1.50:1 目标未达**（不可达性之根因见 §6）。

---

## §1 判据冻结件之指纹

| 件 | SHA-12 | bytes |
| :-- | :-- | --: |
| `.tmp/_stage3_r2_criteria_freeze_2026_10_18.md` | `885ec7fb04dd` | 9971 |
| `.tmp/_r2_tool_03_refindex.json` | `aa05d398bb1d` | 9700261 |
| `.tmp/_r2_tool_14_plan4.json` | `b7942c0a75f1` | 51836 |
| `.tmp/_r2_tool_19_trashverify.json` | `5ff0887b086c` | 66439 |
| `.tmp/_r2_tool_20_xfer.json` | `2c06c1d70839` | 66273 |
| `.tmp/_r2_tool_25_restore.json` | `e8cabb5339c2` | 392957 |

📌 冻结件落盘时点**先于**任何移动/删除动作（本棒首动为 §4 之清走）；判据**事后未调**。

---

## §2 两区前后账（实测）

| 区 | 整理前件数 | 整理前字节 | 整理后件数 | 整理后字节 | 件数差 |
| :-- | --: | --: | --: | --: | --: |
| `deposon-repo` | **4423** | 192,857,021 | **4280** | 189,574,034 | -143 |
| `deposon-sub` | **1189** | 58,756,451 | **1276** | 60,166,418 | +87 |
| **合计** | **5612** | 251,613,472 | **5556** | 249,740,452 | -56 |

| 指标 | 整理前 | 整理后 |
| :-- | --: | --: |
| **件数比 repo:sub** | **3.720 : 1** | **3.354 : 1** |
| 目标（沿先例） | — | ≤1.50:1 ⇒ 🔴 **未达** |

📌 **件账完全对平（实测）**：repo 4423 − 消失 **202** ＋ 新增 **29**（本棒工件）＝ **4280**；sub 1189 − 清走 **54** ＋ 转入 **166** − 回退 **25** ＝ **1276**；全仓预期移除 **262** 件（清走 89 ＋ 转移源 166 ＋ 自清 7）**逐件在案**，**0 件非预期移除**、**0 件预期移除而仍留存**。

📌 **时点口径**：上表为**动作完成时点**（末次清走 ＋ 末次回退之后）之实测；其后本棒另生成本登记件与其生成脚本 **2 件** ⇒ **本件落盘后终态**为 repo **4,282** / sub **1,276** / 比 **3.356:1**（`os.walk` 遍历错误 **0**）。

---

## §3 四型清走清单（判据 89 件 · 逐件路径 ＋ SHA-256 ＋ 验道证据）

| 型 | 件数 | 字节 | 说明 |
| :-: | --: | --: | :-- |
| **A** 同哈希冗余副本 | 89 | 1,585,165 | 须有存活孪生（脚本内 `assert` 硬校验 · **孤儿 0**）·存活孪生取向 ＝ 冗余副本归只读副本面(sub) |
| **B** 0 字节件 | 2 | 0 | `size == 0` |
| **C** 畸形名件 | 0 | 0 | 含 `< > : " \ | ? *`、控制字符、首尾点/空格、长度 > 200 |
| **E** `.tmp` 中间件 | 19 | 148,185 | 0 活代码引用 ＋ 0 在册 md 可解析路径引用 ＋ 非任何保护面（与 A/B 有交叠，去重后清走 89 件） |
| **清走合计（去重）** | **89** | **1,585,165** | 其中 repo 35 件／sub 54 件 |
| **本棒自清（E 同判据 · 本棒工件）** | **7** | **78,617,417** | 可复算之巨型中间索引，保留全部脚本与冻结/登记所需件 |

### §3-1 逐件明细（# · 型 · 路径 · SHA-256 · 字节 · 验道证据）

| # | 型 | 路径（相对两区根） | SHA-256 | bytes | 验道 `$I`／`$R` |
| --: | :-: | :-- | :-- | --: | :-- |
| 1 | A | `.tmp/_m5_k5_net.err` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | `$IPQDZ3G.err`／`$RPQDZ3G.err` |
| 2 | A | `.tmp/_m5_k5_scan.err` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | `$IQWNI1P.err`／`$RQWNI1P.err` |
| 3 | A | `.tmp/_recheck_r1_runA.log` | `68c85cf076d111da22c646f5af7b33348a36295b8ce4bc8439043c019c9390df` | 2,634 | `$IRKO8BA.log`／`$RRKO8BA.log` |
| 4 | A | `.tmp/_recheck_r1_runB.log` | `68c85cf076d111da22c646f5af7b33348a36295b8ce4bc8439043c019c9390df` | 2,634 | `$ILGBG7Q.log`／`$RLGBG7Q.log` |
| 5 | A | `.tmp/_recheck_r1_runC.log` | `b15384cff9f0f75ed825cda787789857b8e54892ec2e00ead4920cd440802332` | 2,568 | `$I9LXJ46.log`／`$R9LXJ46.log` |
| 6 | A | `.tmp/_recheck_r1_runD.log` | `b15384cff9f0f75ed825cda787789857b8e54892ec2e00ead4920cd440802332` | 2,568 | `$I4TK644.log`／`$R4TK644.log` |
| 7 | A | `.tmp/_rj5_convention_check_2026_09_27.out.json` | `c88e4ba1a4ce1caab9d598acfb9926300924aea4030e9898ba05c5470df3d037` | 8,983 | `$IOCHKBU.json`／`$ROCHKBU.json` |
| 8 | A | `.tmp/_t1_gap_implA_2026_10_01.py` | `c5d1dc7badcdd0660cd417152f8e4b7f4fa0fe677c2ba162f0396d43f79a6469` | 4,468 | `$ICB52L7.py`／`$RCB52L7.py` |
| 9 | A | `.tmp/_t1_gap_implB_2026_10_01.ps1` | `19aebfd44310a0f41a381c764a92473caf4a634443d1c717011e1abca077485d` | 5,735 | `$IBPDKYI.ps1`／`$RBPDKYI.ps1` |
| 10 | A | `.tmp/_v5_item21_patched_b1_semA_none_default.py` | `ceb33de660fd5a43d3c22bd051ad9c6b281c92d8727bc435bca9fad5b4bd2770` | 16,768 | `$IM0FM1L.py`／`$RM0FM1L.py` |
| 11 | A | `.tmp/_v5_item21_patched_b1_semB_none_skip.py` | `be0208abaffac626b33d0e7d4dcaf8539a128d059bb505d6c7260048bc27cae7` | 16,829 | `$IOB0NT5.py`／`$ROB0NT5.py` |
| 12 | A | `.tmp/_v5_item21_patched_b2_semA_none_default.py` | `801ee31e8bdc24ab5a37cd65ee25660caabf4fd6f29f991c29c0ce4f34f1f443` | 16,036 | `$IROW79R.py`／`$RROW79R.py` |
| 13 | A | `.tmp/_v5_item21_patched_b2_semB_none_skip.py` | `8293535673dc2e5aceec70fc9f0d1610e8026f8d4900730cb94c218f031496f9` | 16,097 | `$IMROFSK.py`／`$RMROFSK.py` |
| 14 | A | `.tmp/_v5_item21_patched_b3_semA_none_default.py` | `9d8a4a875b6278bfd6f4cb985ee86b9350772c0acd30c9d5d0bdc5903c90fd54` | 15,778 | `$IAPABK0.py`／`$RAPABK0.py` |
| 15 | A | `.tmp/_v5_item21_patched_b3_semB_none_skip.py` | `8df8e94724fff8d893276960764c2cb1422d162d41b173f586f8750ac0984174` | 15,839 | `$IHGFSBW.py`／`$RHGFSBW.py` |
| 16 | A | `.tmp/ref_exp_harness_OLD_2026_10_15.py` | `7957bac14455fd45b546c51a22a85cc0460c07edd1c828bfbf2a759614b43d51` | 13,342 | `$IEDQ0W7.py`／`$REDQ0W7.py` |
| 17 | A | `.tmp/t3_harness_diff_2026_10_15.diff` | `0f8532aefdffaa3cc88a69c68fe321da7cfe390ea3aff0c9c5353abb9e443974` | 3,463 | `$ISYCUH6.diff`／`$RSYCUH6.diff` |
| 18 | A | `.tmp/t5_harness_diff_2026_10_15.diff` | `6f1e9689201b9c4e65e6f9064e01f214a7169154593089526162146fa6d9f66d` | 4,043 | `$IYYV3HM.diff`／`$RYYV3HM.diff` |
| 19 | A | `.tmp/t5_prefix_T1T4_digest_2026_10_15.json` | `9eb43782b73cd606440a285a5a6993d4a616283cdb9b2f6e2030e61eb4bfe6c8` | 400 | `$I4ZFOC3.json`／`$R4ZFOC3.json` |
| 20 | A | `corpus/v20_caption_surface/_adendum_I_po_captions_closure_20260917_132049.json` | `18165008bef6d9f4510f40a3e3a91130ec1e5f4e5c428bcfb7cf9c431e372f52` | 4,429 | `$I0T1QKG.json`／`$R0T1QKG.json` |
| 21 | A | `letters/LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | `70fe266e87d624591af3efa00abd83f6edf0e3c41b311e638c719865ed995f5d` | 8,361 | `$IK0442E.md`／`$RK0442E.md` |
| 22 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `5777a07c608ab93d6f06432ee5ea4d53c33615927f7522b948631749120b960c` | 43,130 | `$IN2ZZND.json`／`$RN2ZZND.json` |
| 23 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `784f042bf93d2ff16c295a6b8fe5cd32e14ed8ac0951c18c5fb91ba1354e59aa` | 22,646 | `$IS0UO7R.md`／`$RS0UO7R.md` |
| 24 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json` | `839fb545257895575828dd5f4ecba71db3024df31d9e4982ad1ce54449e94125` | 16,099 | `$IKTU385.json`／`$RKTU385.json` |
| 25 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json` | `079108c62a822c7678e2c81a537143a4cf6e1d6744556bfd9c7254a169573c50` | 21,049 | `$I33ZYQ3.json`／`$R33ZYQ3.json` |
| 26 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_v3_recheck_05_result_2026_09_28.json` | `81460acbb4f974220fa8032b20e0bd8a01f33ef2e23c1b8a228831faa4092fed` | 450,751 | `$IBIGDTI.json`／`$RBIGDTI.json` |
| 27 | A | `results/_family_e_q_type_refresh_exec_2026_10_14.md` | `71f5a0769dab936f0cb33d631d17977bfa2ed6f84a2d63ad30ea7ebd0f4b56d5` | 28,259 | `$ILRE2X3.md`／`$RLRE2X3.md` |
| 28 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_criterion_application_scope_prereg_2026_10_01.md` | `c4e3338619c6e036015714df170a9793912ff0d93e6961642e147c1ed6bae000` | 50,322 | `$IZVG467.md`／`$RZVG467.md` |
| 29 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_day_close_register_2026_10_01.md` | `6dbac1d1bcd6d57498b1a567814939b598b08c99a6860374e694aba9961dbc4e` | 33,115 | `$IVHVTRM.md`／`$RVHVTRM.md` |
| 30 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_n7_mutual_exclusion_determination_2026_10_01.md` | `b6bdf807cb272eed5b46ead4a379774ea91585e597ef30e0dcea62d6361a9572` | 40,169 | `$II67WIT.md`／`$RI67WIT.md` |
| 31 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_proxy_signoff_execution_register_2026_10_01.md` | `b6e5e15b70e50d399a6ebf4b741c7fcdcdf37394a3a31829ca63fad417f842e0` | 20,766 | `$IC9W5FO.md`／`$RC9W5FO.md` |
| 32 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_closeout_convergence_2026_10_01.md` | `bb62b5c174dad21d63bb6f1dfd7961133d7fd6e3a9a6d7cfaeac2242c3401021` | 42,443 | `$I7RIW4W.md`／`$R7RIW4W.md` |
| 33 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_kv3s_3_verdict_2026_10_01.md` | `e394bb6b5ddf55016860617253f3ce47beba6186744a4f9e55bc033a37db4422` | 35,037 | `$IZQY6IK.md`／`$RZQY6IK.md` |
| 34 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_missing_field_backfill_rule_effective_2026_10_01.md` | `1450057b081903039643c4972b065ec063baad204094a63e6046b95e0771b52f` | 52,469 | `$I3S54CS.md`／`$R3S54CS.md` |
| 35 | A | `results/_p4_pulled_back_conservation.py_2026_10_12` | `4bdec2683f061669ae4098fd08d73efa9ecda06a21e81722bdadc202191b2454` | 22,105 | `$II28MDL.py_2026_10_12`／`$RI28MDL.py_2026_10_12` |
| 36 | A | `sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/COMPILE_SUMMARY.txt` | `1bad41b3929f30bbdb25d2b3d399851b50dcc79121f493fc357657c01f84a2ba` | 1,693 | `$I4Y9ZEW.txt`／`$R4Y9ZEW.txt` |
| 37 | A | `sub/results/Deposon_评估汇总_v1_3_0.json` | `2f02f50c164b15fedb2101e62e6b664760435a380d292c6c9cb9fc9935bf68fe` | 2,811 | `$IFT5SFH.json`／`$RFT5SFH.json` |
| 38 | A | `sub/results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | `c0d629df69d84834c12f811f7e3875e259d320f6c0f21c6723c3d5afc75ea558` | 7,855 | `$IVZ8E16.md`／`$RVZ8E16.md` |
| 39 | A | `sub/results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | `ace3c6b390cbeaf3cdd31614810de437b7ac1dd3bb4c1dab8522ac4ffc13e99c` | 9,343 | `$IHE2P8A.md`／`$RHE2P8A.md` |
| 40 | A | `sub/results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | `0011b7924dfba711d81f6c11f848958d9123977f6d17ed28d65224994a76e93e` | 11,575 | `$I1B26JS.md`／`$R1B26JS.md` |
| 41 | A | `sub/results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | `2e6a31af5e4bc0b21bd8733b7cec8a0ee4125d4dd661b920777aaec2ee1dfae4` | 4,784 | `$IPJ8TOK.md`／`$RPJ8TOK.md` |
| 42 | A | `sub/results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` | `f01a374e9c81e3db89b3a42940c4d6a5447684986a1296e42bf13f196eed6295` | 5 | `$I5HVSHI.note`／`$R5HVSHI.note` |
| 43 | A | `sub/results/_archive_2026_09_20/_tmp_probe_archive` | `a6689025804c7f9ffe9d283b20f47c60514b25a331366ff3c4933f4dcec6e019` | 1,270 | `$I7OBBX4`／`$R7OBBX4` |
| 44 | A | `sub/results/_archive_2026_09_20/fiction_that_feeds_back.tex` | `d060f75dbe9ff19061acb91ee0eeac2cbf4dd9a8bbedcf9e7483cb18cc6f7afe` | 93,324 | `$IQVZE4D.tex`／`$RQVZE4D.tex` |
| 45 | A | `sub/results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | `5198a7059c06cd0c620f9022a5aab4e8fa274c1150e8d2ae0ea5f33164c76fec` | 20,082 | `$IGQIBOJ.md`／`$RGQIBOJ.md` |
| 46 | A | `sub/results/_archive_2026_09_20/review_tech_B1_grok46.md` | `09784ff172b3afff0e8b5685ea1215a4a49f0706f73252ea86efc4464af68d92` | 18,923 | `$IDIOTZX.md`／`$RDIOTZX.md` |
| 47 | A | `sub/results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | `8d00c6d4a242b44f64851fafaffbe8cd9c7d5916e613b168c5e08a8b4e687d78` | 8,098 | `$IVG5BOA.md`／`$RVG5BOA.md` |
| 48 | A | `sub/results/_archive_2026_09_21/Deposon_评估汇总_v1_3_0.json` | `2f02f50c164b15fedb2101e62e6b664760435a380d292c6c9cb9fc9935bf68fe` | 2,811 | `$IA0Q6GO.json`／`$RA0Q6GO.json` |
| 49 | A | `sub/results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | `e934819ee9ed5ca9bb6d35fa21411bf89bf158a8176e70810fe53bf82fed35f3` | 1,043 | `$ISO0BYC.json`／`$RSO0BYC.json` |
| 50 | A | `sub/results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | `664e7cc05aecb2f3bdf08f73c2ceb4eab540d1b68f6170a1d15f3da53d3b044a` | 9,076 | `$IWW5HRF.json`／`$RWW5HRF.json` |
| 51 | A | `sub/results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | `afe975606d4083db475e728321aadaa273f35a2e0a2f53edb67dc0d58a9378d4` | 3,761 | `$I37UIV3.json`／`$R37UIV3.json` |
| 52 | A | `sub/results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | `fbcb60cf5102b73e1e6d4859a5842b356635bf73c730acb2123fb59ae25b69a7` | 5,266 | `$IF559IV.json`／`$RF559IV.json` |
| 53 | A | `sub/results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | `a4b12d1cfedcef5892fd173e09372d3ccf8bc7544337c463c166c8eeb6a56aeb` | 2,042 | `$IIJK4UV.json`／`$RIJK4UV.json` |
| 54 | A | `sub/results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json` | `088f28524a1d9efe419a1319d4d617ce37d2318df242b934c2cbffd110a81dd6` | 4,276 | `$IBF7AKH.json`／`$RBF7AKH.json` |
| 55 | A | `sub/results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json` | `1e4c065da058cf490e905482b90fffc0862951717cacea9319770551b6df99f7` | 5,916 | `$IDKNDDZ.json`／`$RDKNDDZ.json` |
| 56 | A | `sub/results/_tra_v0_2026_09_10.py` | `d80a8f75a1224cda9280945644b7ffef8c4355be9b447b781f76953b0998c85b` | 12,125 | `$IY5XQ7K.py`／`$RY5XQ7K.py` |
| 57 | A | `sub/results/_v2_setup.py._moved_20260924_1830.py` | `73f2b8712a9064b6d9ad9011cfec78618067e68a1e61358a0be20094f48be034` | 3,483 | `$ICFGUGI.py`／`$RCFGUGI.py` |
| 58 | A | `sub/results/_v2_show_summary.py._moved_20260924_1830.py` | `0012b38ce4389cf223360cbb74992b801b616b82d105e914b026691ae7190aef` | 1,200 | `$I8222P6.py`／`$R8222P6.py` |
| 59 | A | `sub/results/_v2_smoketest.py._moved_20260924_1830.py` | `0b6c22c8f37965633e4ee4c5e2c6fc59a0661304ccb68056e404aee95f4e8b12` | 2,040 | `$I4SSFTK.py`／`$R4SSFTK.py` |
| 60 | A | `sub/results/_v2_stage1_60cells.py._moved_20260924_1830.py` | `8c7bd12c3a8c189d6ddfcf91b0ccb2d4f096d4e01956aa6852207d60f10fdac7` | 31,556 | `$I2OP7RE.py`／`$R2OP7RE.py` |
| 61 | A | `sub/results/_v2_stage2_f2_drift.py._moved_20260924_1830.py` | `7e9b2fc57d8064f0f643f47eb1c5ad4b41d66c7055c1f076626e69c6f5f867ec` | 10,798 | `$ICWZSIW.py`／`$RCWZSIW.py` |
| 62 | A | `sub/results/_v2_stage3_f3_strip.py._moved_20260924_1830.py` | `ce4362e325cad5c80e356ec8a6e71df9103144ac9754e458779ea91a5b901553` | 11,803 | `$I2BBVL5.py`／`$R2BBVL5.py` |
| 63 | A | `sub/results/_v2_stage4_f4_pdv2.py._moved_20260924_1830.py` | `b84f5aab6fafe3a862cb5d1a620afaffbaf5d39661daddbdaf19b02f73dce817` | 10,355 | `$IYZPHVA.py`／`$RYZPHVA.py` |
| 64 | A | `sub/results/_v2_stage5_f5_dpath.py._moved_20260924_1830.py` | `e8871b829d899dadf412ff8c55bf2e40ee63ae44ec2e74eea6c911ce88471d41` | 6,480 | `$ILTO051.py`／`$RLTO051.py` |
| 65 | A | `sub/results/_v2_verify_outputs.py._moved_20260924_1830.py` | `eb0107dd79b5461c2b506cb10baea9c469887b23208f9f1e6064c87cc7e179b1` | 2,656 | `$I8CXCCV.py`／`$R8CXCCV.py` |
| 66 | A | `sub/results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json` | `9287947102412254992acddc59ba233c97afc80fb75a46693cf6451a10dffb29` | 4,202 | `$IK364CJ.json`／`$RK364CJ.json` |
| 67 | A | `sub/results/_v3x_conservation_anchor_2026_09_17.txt` | `f331a9c2bd22bb9c9b4e167e087b7d03ca142523f50598db8efbbb4a09205f87` | 940 | `$I7R0JK9.txt`／`$R7R0JK9.txt` |
| 68 | A | `sub/results/_v3x_d0_5_aggregation_2026_09_17.md` | `ddf0d1aa96d2920a0311b89dba414f3d63e86cfbf653b166f3a1144f5456c5ca` | 12,010 | `$ICN0E6G.md`／`$RCN0E6G.md` |
| 69 | A | `sub/results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | `d8f2b99aa5270a7e91eec05e8e6d68b5a9c0290c9a2bbc6b6a2436da5f8f90e2` | 7,617 | `$IRKHDND.md`／`$RRKHDND.md` |
| 70 | A | `sub/results/_v3x_d0_5_proposal_coze_2026_09_17.md` | `759c25b21ed416fb0e87f2630f4361370a774171f88f7da4ad41c495d81d8b85` | 13,200 | `$IPNKLFA.md`／`$RPNKLFA.md` |
| 71 | A | `sub/results/_v3x_d0_5_proposal_trae_2026_09_17.md` | `b1c227d54a821716564086fe39e1b6dc55b97b23b43b0455918401b2182cbc71` | 13,254 | `$I6IIOVB.md`／`$R6IIOVB.md` |
| 72 | A | `sub/results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | `f39412103366302e6983afd71d9e5013bc08b5fbd51b4f306b6216e01ed4f882` | 17,053 | `$ITMC4W0.json`／`$RTMC4W0.json` |
| 73 | A | `sub/results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | `59c2113b7c716fd8c63352f36d9d73d361b46ae5188c65aaf69dcd489488a67a` | 2,059 | `$I14B1N8.json`／`$R14B1N8.json` |
| 74 | A | `sub/results/_v3x_p_l_v3_external_spec_2026_09_17.md` | `6a5b6eb635f0443dbc74a26ef967ec2902763f61fd1f8e21d97c8b5d8988acf1` | 5,769 | `$INSDP2G.md`／`$RNSDP2G.md` |
| 75 | A | `sub/results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | `523b5941c30c10b14bf454337330ad13b66b11ba5642507712562311cd0e1bd9` | 16,835 | `$ISVMW0O.json`／`$RSVMW0O.json` |
| 76 | A | `sub/results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `183205baa9ac946b0ef6cdc997a70923887792ad24c4484880ddfca40479eaf6` | 9,570 | `$IORILVK.md`／`$RORILVK.md` |
| 77 | A | `sub/results/boss_pc_2_a2_fitting_2026_09_15.json` | `5a880678c386af2094eebb86c06f568373b316e67e0b6b4468a9a822810970c8` | 1,024 | `$IMTYH6T.json`／`$RMTYH6T.json` |
| 78 | A | `sub/results/boss_pc_3_a3_clipping_2026_09_15.json` | `d74d6b39d1b038f63095761aedb3d89c088d435537e5822eeac3e611142bab13` | 1,265 | `$I6WIHZ6.json`／`$R6WIHZ6.json` |
| 79 | A | `sub/results/boss_pe_1_real_2d_ising_2026_09_15.json` | `43d9ce160fc80ea50b767aff7e651da2c07bcf8e0f1492f1d267e610f8b20fdb` | 2,460 | `$I63BQMO.json`／`$R63BQMO.json` |
| 80 | A | `sub/results/boss_pe_2_real_transverse_ising_2026_09_15.json` | `8933d61b180add8aa953a4b01bd913300c50e835662189bd902bc0558e674507` | 3,553 | `$IWNPIXK.json`／`$RWNPIXK.json` |
| 81 | A | `sub/results/boss_pe_3_real_reservoir_2026_09_15.json` | `94b5398be76c7b7a8de04aef3ac0dd5b425edd01203ba4c9dd1ec06488ef0574` | 2,364 | `$IADR2ON.json`／`$RADR2ON.json` |
| 82 | A | `sub/results/deposon_dpath_cross_modal_runner_2026_09_10.py` | `fb20a6ba5ec60c430987f296adf8707bc347971baac2b4466565a82f6c51e459` | 27,930 | `$IR5FEE3.py`／`$RR5FEE3.py` |
| 83 | A | `sub/results/deposon_feshbach_rag_30cells_2026_09_10.py` | `a072e4184e834da2e72f3cc19269996711d79b036a68579c9a4b8af0bd2e3115` | 14,343 | `$I1I7055.py`／`$R1I7055.py` |
| 84 | A | `sub/results/deposon_v1_implementation_calculator_2026_09_10.py` | `121f104012f4bb090be695d7b2e98403bb142aa5cddee78f2c13f343770f549c` | 10,751 | `$I83NI2E.py`／`$R83NI2E.py` |
| 85 | A | `sub/results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | `a3ca05aec6fbcb6271a4c5539722cf64e153b44f67e2830b11c08f77d4ca982c` | 8,112 | `$I80ARAO.py`／`$R80ARAO.py` |
| 86 | A | `sub/results/deposon_volcengine_worker_b_2026_09_10.py` | `401dfd3c27f35b46e8ffa09a11f991f02dcb4c6512f187567b3be7d22971ba35` | 13,232 | `$I7Z07WW.py`／`$R7Z07WW.py` |
| 87 | A | `sub/results/deposon_volcengine_worker_c_2026_09_10.py` | `b5eeef1e9bd74c8012ec050f4b5efd82439316d651165147ef65e13037434d50` | 11,692 | `$I65OLN6.py`／`$R65OLN6.py` |
| 88 | A | `sub/tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak` | `7d8d6a30dd8ca4eb1d98a5cda8e6a065928723e6254674e739f6e21aa80515b9` | 23,893 | `$IGR4HV0.bak`／`$RGR4HV0.bak` |
| 89 | A | `sub/tmp_movedout_2026_10_01/process_scripts/volcengine_补测_worker_A_2026_09_10.py` | `20b8a2f54ad936ff93e1f7b537ac082422c7f2ffba82661de087cdc9cdfb0d6d` | 16,252 | `$INJ48KZ.py`／`$RNJ48KZ.py` |

### §3-2 本棒自清 7 件（可复算之中间索引）

| 路径 | bytes | 验道 |
| :-- | --: | :-- |
| `_r2_tool_01_inventory.json` | （已离原位） | `$ITOYPEE.json`／`$RTOYPEE.json` |
| `_r2_tool_04_classes.json` | （已离原位） | `$IRST67Y.json`／`$RRST67Y.json` |
| `_r2_tool_04b_channels.json` | （已离原位） | `$IZCJHQ4.json`／`$RZCJHQ4.json` |
| `_r2_tool_07_xferpool.json` | （已离原位） | `$IMEKIUC.json`／`$RMEKIUC.json` |
| `_r2_tool_10_plan2.json` | （已离原位） | `$IF2BKK1.json`／`$RF2BKK1.json` |
| `_r2_tool_11_channels.json` | （已离原位） | `$IE8B36W.json`／`$RE8B36W.json` |
| `_r2_tool_12_plan3.json` | （已离原位） | `$IDDHKVR.json`／`$RDDHKVR.json` |

### §3-3 验道标准与结果（**exit 0 ≠ 成功**）

| 项 | 值 |
| :-- | :-- |
| 通道 | Windows 受信 launcher 之 `rm -- <字面目标>`（本会话内 `Remove-Item` ＝ 永久删 ⇒ ⛔ 0 用）|
| 小样本验道 | 1 件（`.tmp/_m5_k5_net.err`）先验：离原位 ✔ ＋ `$I`/`$R` 成对 ✔ ＋ `$I` 原路径解码（偏移 **28**，UTF-16LE）✔ ⇒ 方批量 |
| 批量验道 | 清走 88 件 → **88/88** 命中；自清 7 件 → **7/7** 命中；样本 1 件 → **1/1** 命中；**合计 96/96** |
| 回收站位置 | **`D:\$Recycle.Bin\<SID>\`**（非 `C:` —— 本棒样本在 **D:** 卷，首轮查 `C:` 曾误判「验道未过」，已改查正确卷并复验通过）|
| `$I` 条目总数 | 104（含本棒 96 ＋ 他棒既有 8）· 缺 `$R` 者 **0** |
| ⛔ | 0 永久删 · 0 覆盖 · 0 重命名既有件 · 单件最大 450,751 B ≪ 站容 |

---

## §4 转移映射表（跨区 repo→sub · 逐件 SHA-256 复算）

| 项 | 值 |
| :-- | :-- |
| 方向 | **repo→sub 141 件**（净）｜**sub→repo 0 件**（两方向之射程沿 §3-2 定本；sub 侧 190 件 `.py` 全为 9 月实验执行体且 0 误置 ⇒ 见 §5-3）|
| 断链 | 🟢 **残余功能断链 0**（活代码 .py 403 件＋在册 md 895 件 之大小写无关全量复核）｜⚠ **文本引用 164 件**已登记映射（§4-2）|
| SHA-256 复算 | **MATCH 141 / FAIL 0**（移动前后逐件复算）|
| 同身份已占用 | **SAME_IDENTITY 0**｜**CONFLICT 0**（转移前实测：目标空位 166 / 已占用 0）|
| 目标路径 | 保持相对结构 `deposon-sub/<原相对路径>` |
| ⚠ 回退 | **25 件**检出活代码功能引用（`verifier/vNN/check.py` 之 `read_text()` 等）⇒ 当场回退原位，**RESTORED_MATCH 25/25**（§7-1）|

### §4-1 净转移 141 件之映射（旧路径 → 新路径 · SHA-256）

| # | 旧路径（repo 相对） | 新路径（sub 相对） | SHA-256（移动前 ＝ 移动后） | bytes | 复算 |
| --: | :-- | :-- | :-- | --: | :-: |
| 1 | `docs/ADVISOR_BRIEFING_2026-08-30.md` | `sub/docs/ADVISOR_BRIEFING_2026-08-30.md` | `40278bc425e66a1681bea1c5ed264a0e1ca27b584e8852bb07d88c1ca10715c6` | 5,890 | MATCH |
| 2 | `docs/ARCH_AUDIT_v2.md` | `sub/docs/ARCH_AUDIT_v2.md` | `5bee4c6cf47cd37ab22a6dbf09f952b143dc89552e33f6c1ce07ac8dbda6213b` | 14,698 | MATCH |
| 3 | `docs/DATASET_HEALTH_v2.md` | `sub/docs/DATASET_HEALTH_v2.md` | `c87a0c1f5af6076d1145375d9e1220627679d6788a360caca4cce2e266ebb3a3` | 4,892 | MATCH |
| 4 | `docs/Deposon_Requirements_v1.md` | `sub/docs/Deposon_Requirements_v1.md` | `ee33f3f22e1bb8a761b0baacee1c019ea08f22cab6daf53cfae7ff8d8eff0758` | 13,914 | MATCH |
| 5 | `docs/Deposon_v1_3_验证报告.md` | `sub/docs/Deposon_v1_3_验证报告.md` | `dc5be727f92043c3b4ff5dd9aef919f363a70b12c7447a13ddff1ee651dd1bd0` | 8,003 | MATCH |
| 6 | `docs/Deposon_v1_4_验证报告.md` | `sub/docs/Deposon_v1_4_验证报告.md` | `3bcccf03f7cab3b576c9bb68bfec5208b514708b2db1c213ee09416482abdd63` | 4,254 | MATCH |
| 7 | `docs/FIGURES_v2.md` | `sub/docs/FIGURES_v2.md` | `1cd4a4cb0a76b0d0ca092ffb01bf55062b9099e361a4193ca56c2b0c1a90cfd7` | 5,851 | MATCH |
| 8 | `docs/LESSONS_INDEX.md` | `sub/docs/LESSONS_INDEX.md` | `7e3674a80cb7d0d6f99b92eb3406843c14b6f71d19357ba996ab26176e507129` | 4,682 | MATCH |
| 9 | `docs/LESSONS_v19.md` | `sub/docs/LESSONS_v19.md` | `dbbcf8e5e89d3f637d8261739f41293f09d0c3ad5b6fb4073e54e00a3bfbe874` | 5,290 | MATCH |
| 10 | `docs/LESSONS_v20_deepprobe.md` | `sub/docs/LESSONS_v20_deepprobe.md` | `5c898d4407ee709c7bbdcd434e52a9d515dce21527b45257d46e14f651097579` | 8,409 | MATCH |
| 11 | `docs/MODEL_ARGUMENTATION_v2.md` | `sub/docs/MODEL_ARGUMENTATION_v2.md` | `2c83c42804e4ffea8f8470a79f58cfd8aa7c3b634f206096acbfa25a15bd00e0` | 30,142 | MATCH |
| 12 | `docs/PROGRESS_REPORT_LAYMAN.md` | `sub/docs/PROGRESS_REPORT_LAYMAN.md` | `25546ffdc56b8668a0a77a7921452392e32a85471aa86aec667d859127d74f6e` | 8,472 | MATCH |
| 13 | `docs/Roadmap_v2X.md` | `sub/docs/Roadmap_v2X.md` | `a6aaf320061116a59195f9345ba57b77630c628849be2f9229ef3506236a20c7` | 6,467 | MATCH |
| 14 | `docs/SALVAGE_v2.md` | `sub/docs/SALVAGE_v2.md` | `f28a81d6302dae8b734afed333f70771c46487a405d1f5bccc570e1a5482b1f8` | 7,312 | MATCH |
| 15 | `docs/SECURITY_AUDIT_v2.md` | `sub/docs/SECURITY_AUDIT_v2.md` | `317fb508940a9425caad92ee28218c6878fee0ec12229c34ecb0c9dbefd7c0ff` | 4,707 | MATCH |
| 16 | `docs/SPEC_GT2C.md` | `sub/docs/SPEC_GT2C.md` | `29af533486b289f7d85ec9ce399f7a2b2498244c51ddbd2a35d0069d59c6509a` | 3,172 | MATCH |
| 17 | `docs/SPEC_GT5C.md` | `sub/docs/SPEC_GT5C.md` | `1e41b43347354d93006b3bc1e0fd06270257ae89471c41055c996f257b8b5634` | 3,046 | MATCH |
| 18 | `docs/SPEC_v1.5.md` | `sub/docs/SPEC_v1.5.md` | `c165a86cf55101472fd614fc4dda980310c4b5d59857ede8fe3553493c251ab6` | 6,204 | MATCH |
| 19 | `docs/THINKING_V3_GT_CONTRIB_2026.md` | `sub/docs/THINKING_V3_GT_CONTRIB_2026.md` | `8c1d733f9182dac4f84508f7e981924681849a6580facddaa7ca615d452c8bd8` | 19,508 | MATCH |
| 20 | `docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | `sub/docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | `bbd074b7652670be9c068aa2db86940995a669f3c63d4a24addb3716d20841b1` | 11,835 | MATCH |
| 21 | `docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md` | `sub/docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md` | `9352a1675b100266c4bc14259a532df055ae4a2b67856d0ea47bddf6bbe867fa` | 5,615 | MATCH |
| 22 | `docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md` | `sub/docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md` | `354a1360234f965ca3a63436778a6b3a7d85860fd2871a625a6fe6599f6c2ccf` | 4,840 | MATCH |
| 23 | `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `sub/docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `c28f7f0b530fa1248fc33107d424c56d2e42561d3553020a2acebd93a3548162` | 11,079 | MATCH |
| 24 | `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md` | `sub/docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md` | `4485443757e751d494085564106070521ba9d47e775cad604cf95437982d5870` | 15,478 | MATCH |
| 25 | `docs/V3X/BOSS_URL_2026_09_11.md` | `sub/docs/V3X/BOSS_URL_2026_09_11.md` | `1ba7419178a14e8bf0c5710884cc1f83853304e36305d9cb3417862a5990d2ee` | 7,135 | MATCH |
| 26 | `docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | `sub/docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | `0fb588bb0c2ec27f4f530f0004036a9df0117199dd231efb1459a96f8341d541` | 10,970 | MATCH |
| 27 | `docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | `sub/docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | `d74e1534493e9ac87dad82faff39a22f5bcca651e746865262a257a9c74fc84c` | 6,864 | MATCH |
| 28 | `docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md` | `sub/docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md` | `b049140e130ce79415c690e0d28548824af004196fa7551fccc3a39303805c82` | 6,804 | MATCH |
| 29 | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | `sub/docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | `de772cd9e7ba143168b168596526474ff1b6b570ab326f0b3aafae4225795cb3` | 6,825 | MATCH |
| 30 | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | `sub/docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | `0d1e88c258aa1ea746adbf6372367b0d0720a81b25f2a7cfea2e0f9003c264be` | 9,844 | MATCH |
| 31 | `docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` | `sub/docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` | `574d5a79e363d353af1f1985cec5a03c3641f9c49825b27d25583a25f87e455f` | 4,361 | MATCH |
| 32 | `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `sub/docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `8ff1a7c5413f0787ec9317edf2e135f6d0cf608b7363bd7f1ad32d9092028851` | 21,756 | MATCH |
| 33 | `docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | `sub/docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | `2c4bb6078ee78bdd307e0856eea8742e8f274e8303a918013d811ab7f0a28701` | 5,930 | MATCH |
| 34 | `docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | `sub/docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | `67063f9cb2381fed2aac98f31149aa845280453c4fce2196c9601c29bdb426a9` | 6,459 | MATCH |
| 35 | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | `sub/docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | `87563a63b8544db6f23cf618d80f1c4794550c80c8c728ca8c39a886888481d7` | 5,830 | MATCH |
| 36 | `docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json` | `sub/docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json` | `0b8a1a357aaee4139a07cd3dc89b2698ade82fc253caba3a4db0a711c065029a` | 20,271 | MATCH |
| 37 | `docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json` | `sub/docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json` | `40955bf2abc5c1118205f47b28f5e64b0529bdf87c620b1496fd16b2332021fa` | 1,248 | MATCH |
| 38 | `docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | `sub/docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | `51869e3184f4e39eabcb377404cab86303269ca22d93f0788f22258a2c6205e8` | 10,692 | MATCH |
| 39 | `docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | `sub/docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | `935cb6ee356652430bdd3841c1e5bd6a496b14b499e0b44af78f1cae4b8973f6` | 8,037 | MATCH |
| 40 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | `sub/docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | `ac8997b077317641b8be60dc3de510d636c8722eafcbb3a196e6bffe8b0cdf03` | 22,442 | MATCH |
| 41 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | `sub/docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | `240a7ae4bdfbb3d18680abcd69bfc10b01919177703c06ad1116491ec537f1cf` | 17,803 | MATCH |
| 42 | `docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` | `sub/docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` | `e4ee3999f7cea1addd1489b2e832b738bdedb6efa55af23acc4270624d0b3def` | 26,460 | MATCH |
| 43 | `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `sub/docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `0a63824f0805a0184a287d779db4c084e32962f61ce03499d58c9bec7a6b4295` | 7,352 | MATCH |
| 44 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `sub/docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d4043663ff3592361958ee8b76baaaf0582c1bdccaaf54376eb1109e3a0` | 29,570 | MATCH |
| 45 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `sub/docs/V3X/KT_B1_SPEC_V0.1.md` | `0397b757362fa0badabc8d2ffde6baac965a028015cb093e3a06d5e6a972f98e` | 39,206 | MATCH |
| 46 | `docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md` | `sub/docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md` | `825337b10a2d04c6c0ee57bc8a8d10dc35d942769347444c7cc08b1a8b164d97` | 8,753 | MATCH |
| 47 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `sub/docs/V3X/KT_C1_SPEC_V0.1.md` | `59d8f56347d50df285b779cac54ee0230849f4d5a62eb425ebf5b8a37e979810` | 31,241 | MATCH |
| 48 | `docs/V3X/KT_D0_EVIDENCE_CARD.md` | `sub/docs/V3X/KT_D0_EVIDENCE_CARD.md` | `75b2f3b38c2a1fd35c464429ba848e40e934f7ff34566a2d5fe2b24c1ab61fbe` | 6,354 | MATCH |
| 49 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `sub/docs/V3X/KT_D0_SPEC_V0.1.md` | `cce8e9a1b00e31a02c54a35c853f226e94ee44c9da40947e4532044d40a16bb4` | 20,927 | MATCH |
| 50 | `docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | `sub/docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | `ba53d73e39375004f327fc4a001e122434c732bd7a5881a4b99831c0c13245e5` | 9,701 | MATCH |
| 51 | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `sub/docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `bd1caab42b4c3f8a80c7de37f7289fe34c68321df0d5ba65dd2aa266640ab4fb` | 10,351 | MATCH |
| 52 | `docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | `sub/docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | `ee043a13f801f152bdff283565f8c3128c19f70c307c51779eacc91f38a7fea6` | 3,899 | MATCH |
| 53 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `sub/docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `d427b2f57c3362962348169292fc9dbc8317f84b345b808fa8e74aa114e51453` | 6,301 | MATCH |
| 54 | `docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md` | `sub/docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md` | `00c7b7ceccdc0a5ffd07083ad65cc03c75c6512b7bbe43ca9db70ac1faee7adf` | 4,885 | MATCH |
| 55 | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | `sub/docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | `7f1492fbe6574852ebc9bf72d98139f78d6b1d95631519bd4724da008d5d8cd3` | 10,979 | MATCH |
| 56 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | `sub/docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | `fc73cab85d8f3a326ae426297453eeb3d514d22405e601007bba19810a3ded9f` | 15,021 | MATCH |
| 57 | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | `sub/docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | `c13449101ab325b45c3096cd3f6309b539cc79567babca0f26bd9f33528567b1` | 34,367 | MATCH |
| 58 | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | `sub/docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | `3b67461b05fe35682e228113b3f46b9ea7894597440d74a3f403b2af2f9b5630` | 9,192 | MATCH |
| 59 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `sub/docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `900da300d11e859a8caf29f924b79c3205bc9b6bb962fc06305bd8fc26edc2dd` | 13,109 | MATCH |
| 60 | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | `sub/docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | `817efdc2f0ad032bd9f1cafb442c8f5df563d98fe072a3c778eacb116a2e7f78` | 15,985 | MATCH |
| 61 | `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | `sub/docs/V3X/P_F_D1_REPORT_2026_09_15.md` | `e47d0348922ec8f49cc16c3a43d3b03fec4c48db59ad1df905f123881eefa714` | 12,608 | MATCH |
| 62 | `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | `sub/docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | `edd048eaa7214d7c94eb3973595e0987f1637eebc65a610746ec4d06ed1eb8cd` | 22,973 | MATCH |
| 63 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `sub/docs/V3X/P_F_RESEARCH_2026_09_09.md` | `98085df7811afd8dc96075249a6fd4f6458ac141a837b3457226cbeb1322b0b4` | 17,603 | MATCH |
| 64 | `docs/V3X/P_F_SPEC_V0.md` | `sub/docs/V3X/P_F_SPEC_V0.md` | `de90faf362c53502444808d5c1a74d0e431e7a160b2b15024d86f2d99e39b6a2` | 19,804 | MATCH |
| 65 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `sub/docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `b10fae0da66defa154db7083f4acaae2a1e5d8df786ac72c86eb42d15e6f4d82` | 6,375 | MATCH |
| 66 | `docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md` | `sub/docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md` | `4d970e9c0aec6b382de860e0296d7dedb964e55d3ca650553520286c31f008bf` | 4,188 | MATCH |
| 67 | `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | `sub/docs/V3X/P_G_V01_REPORT_2026_09_15.md` | `9a6b08d03e0cafd2cfd01d5eed1116b48d28e70aed9b1dd9af0c4537eac53b82` | 15,479 | MATCH |
| 68 | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | `sub/docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | `a476f241edb2e8260b2ae972c7cf38ae9c0fede6170e8d83f656b42daf7a6691` | 15,085 | MATCH |
| 69 | `docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | `sub/docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | `575572872e9a5e2b87e50458204201c7c46830952ebed8f93ea718529c38661f` | 34,647 | MATCH |
| 70 | `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | `sub/docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | `195373c094d636c2ff241efda2bb314611264356d06b96a5f3671bd2a3d89d28` | 20,698 | MATCH |
| 71 | `docs/V3X/REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md` | `sub/docs/V3X/REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md` | `33ee7266cf5b3f399bea9eda5eb66b2c46b74663a15b5a40573151a2a823c606` | 17,151 | MATCH |
| 72 | `docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | `sub/docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | `5e99e79f2e11dad8b5aac6fe9b263734c130e3070c3fbe9164c5a47ea2b72f8d` | 14,835 | MATCH |
| 73 | `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` | `sub/docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` | `f5ac9820310ab3e52c8a35a112e17b2c0403443e172b27d28463cd27a99c0ce0` | 16,278 | MATCH |
| 74 | `docs/V3X/REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md` | `sub/docs/V3X/REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md` | `31c27c0117a626b880ded79549a9cf803dbf9f6b804c9b6a176f3ee1d1fd2485` | 16,926 | MATCH |
| 75 | `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | `sub/docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | `c00d1c22e7ed5f9bde38f16e6771cfb27fd855817722925da1c978034c90e840` | 13,271 | MATCH |
| 76 | `docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md` | `sub/docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md` | `00e543564e3fa8113c8a4d838d11c662ff1304e9bc06a163eaf31c37ba807f33` | 10,708 | MATCH |
| 77 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | `sub/docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | `7478959cfc7de0027a52b42bc9dcfc2d906271c061088cddf4ac6181e997435d` | 9,267 | MATCH |
| 78 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | `sub/docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | `4020b18097807ea1edc5b731774030df996e8d912caef9e6218e402501d28233` | 8,849 | MATCH |
| 79 | `docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | `sub/docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | `813b34dcac708521ac2ef2addb4368ad0f49036fa4725fe5cf320ccfbf2a5b8d` | 6,493 | MATCH |
| 80 | `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | `sub/docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | `226f740aa120edacf1d83995cc1e92fe31e1532b28c8647a926ed7845da4221a` | 4,840 | MATCH |
| 81 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `sub/docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `4ffb21bb6bfafc1d9b9a340c0302f50ca4a44165dcfb833ce988786b61cd0680` | 8,526 | MATCH |
| 82 | `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | `sub/docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | `4d06d34cb6fadd3875737128ef742097807eb48fb117cee16dc22d776f92b04c` | 24,778 | MATCH |
| 83 | `docs/V3X/V3X_D6_PAPER_zh.md` | `sub/docs/V3X/V3X_D6_PAPER_zh.md` | `feae8af2fefe8fcbb619558a27fef8f2602e104991bcee7efd1fb9b8d84b2dc8` | 19,716 | MATCH |
| 84 | `docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | `sub/docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | `37e97e1e7b7f16ec4cd50a4764ec9904c306a02186f287178238d2f81afb20c7` | 15,327 | MATCH |
| 85 | `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `sub/docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `3d847f9f3151e6c7ebf75330c4dc8c8199aa78e2c94c7e4794e4455ea0853b4a` | 22,427 | MATCH |
| 86 | `docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | `sub/docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | `4de2cbf57a49ee2c7c0057d0410b853d523f3f07d3603374e1bf53216fbcc288` | 12,908 | MATCH |
| 87 | `docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md` | `sub/docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md` | `e451a5a3d07917ec431348992fea75d1285089ec3df1dcf64601d11c200b34bb` | 4,775 | MATCH |
| 88 | `docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | `sub/docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | `914053fc3e173bba1fe8eae4593f10f98bbb4b15b5fe64b689a8a3cf1645f53f` | 11,080 | MATCH |
| 89 | `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | `sub/docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | `f80cc4e1fb7f531ad6cc1d161592ec7f61db8586c569aff612ddf1420179ff89` | 7,344 | MATCH |
| 90 | `docs/V3X_COLLAB_DIRECTIONS.md` | `sub/docs/V3X_COLLAB_DIRECTIONS.md` | `5a27c2350036038d38b26683b8ccfef72035c6b477ab6eb489713d39a19f6db8` | 16,363 | MATCH |
| 91 | `docs/reviews/review_gtformal_integration_v2X.md` | `sub/docs/reviews/review_gtformal_integration_v2X.md` | `325c9d87787b3b08490b59da4bc940959cf298ef4d4b642e244b4e4de3078c6c` | 8,582 | MATCH |
| 92 | `docs/reviews/review_salvage_integration_v2X.md` | `sub/docs/reviews/review_salvage_integration_v2X.md` | `96ae50306f365c23190b73b8f652112d49b14b184909bd2a561b37f5a6c5ec03` | 6,212 | MATCH |
| 93 | `docs/reviews/review_sprint_v2X.md` | `sub/docs/reviews/review_sprint_v2X.md` | `4356cd02562e92435f99ee4c56868a791de206b6639ca36bffc564196fc42fa3` | 7,776 | MATCH |
| 94 | `results/_batch12_deliberation_judgment_2026_10_14.md` | `sub/results/_batch12_deliberation_judgment_2026_10_14.md` | `8218a8777192cc2ac0d7ca85bfe9a2577fa9fa89d9a603fd5c726c2afa1bc765` | 39,448 | MATCH |
| 95 | `results/_family_e_q_type_conflict_resolution_2026_10_14.md` | `sub/results/_family_e_q_type_conflict_resolution_2026_10_14.md` | `dd5547b8e8c72bb3e2e80d79a650e6f1b828925ab3f4451e73020055a5ba5f3b` | 19,640 | MATCH |
| 96 | `results/_ge01_H_enumeration_and_lock_2026_10_13.md` | `sub/results/_ge01_H_enumeration_and_lock_2026_10_13.md` | `4c5860342d7fa3c0ca9994372cf4a80f4ee12fdcb95a83b6db2ef8d23eddad56` | 28,522 | MATCH |
| 97 | `results/_ge01_H_enumeration_round2_2026_10_13.md` | `sub/results/_ge01_H_enumeration_round2_2026_10_13.md` | `ff2afb7a634bb3754a697ce08a1ac2370dff962c674cd58cb79a72c54f48d3bf` | 37,191 | MATCH |
| 98 | `results/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md` | `sub/results/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md` | `deea2ccb264383a638baf4aa721135d9f4f853f8e99bf8fa02f71de3c84feef7` | 17,885 | MATCH |
| 99 | `results/_itemH_fingerprint_provenance_2026_10_12.md` | `sub/results/_itemH_fingerprint_provenance_2026_10_12.md` | `bacbee9a158f912697e4a768075cbdd9fbedbcf6e9c0b24458f09c40de705144` | 22,752 | MATCH |
| 100 | `results/_itemH_nonclade_and_hangings_register_2026_10_12.md` | `sub/results/_itemH_nonclade_and_hangings_register_2026_10_12.md` | `37ea7f65a8d68ef9cc0c82ab8269ad5a77a62985d6caf1e5b530e35a03afe3eb` | 13,223 | MATCH |
| 101 | `results/_l3_deferred_items_immediate_disposition_register_2026_10_13.md` | `sub/results/_l3_deferred_items_immediate_disposition_register_2026_10_13.md` | `92e410f452568ebee34153d966b6c162ba28a955e69f54630caffcb9cf01963d` | 33,958 | MATCH |
| 102 | `results/_m3_glm29_adoption_register_2026_10_13.md` | `sub/results/_m3_glm29_adoption_register_2026_10_13.md` | `6aff3c459ca09bad3bf2593ae729701d1631085cbb0d28b24db0d9f61229ceb9` | 23,309 | MATCH |
| 103 | `results/_m5_rejudgment_and_dual_value_register_2026_10_14.md` | `sub/results/_m5_rejudgment_and_dual_value_register_2026_10_14.md` | `4b72fbe08ce224b6bfe8ec58194c0cc5fea5ecd325bd631f92393954286367d6` | 16,093 | MATCH |
| 104 | `results/_mq_rollout_v7_effect_register_2026_10_14.md` | `sub/results/_mq_rollout_v7_effect_register_2026_10_14.md` | `a709ff7b48de359010d36c64f9bd51555136c4829b591da1097633fedc12ded0` | 15,538 | MATCH |
| 105 | `results/_mq_rollout_v8_effect_register_2026_10_14.md` | `sub/results/_mq_rollout_v8_effect_register_2026_10_14.md` | `5f32931507bb6be38776f4829d954e6be3f1e8377ab4f976561acb3fc37af222` | 14,621 | MATCH |
| 106 | `results/_numbering_face_signature_effect_2026_10_13.md` | `sub/results/_numbering_face_signature_effect_2026_10_13.md` | `6a7f0a1890a43b0f39e14d19d82d95fb0fb2eb54387d6f5580be5ad85a7b0258` | 11,273 | MATCH |
| 107 | `results/_numbering_family_count_corrigendum_2026_10_14.md` | `sub/results/_numbering_family_count_corrigendum_2026_10_14.md` | `9baf2ea2e9cb3c2c3a894d62a2b7a7a4b0f6c02118aa604fae86b94caf9418a0` | 19,812 | MATCH |
| 108 | `results/_numbering_raw_residual_461_variants_corrigendum_2026_10_14.md` | `sub/results/_numbering_raw_residual_461_variants_corrigendum_2026_10_14.md` | `33feb734ca80b77e31c9bb7fcc3a97d134917d95f06252a9c2b97db1a73276aa` | 5,239 | MATCH |
| 109 | `results/_p3_candidate3_supplement_register_2026_10_13.md` | `sub/results/_p3_candidate3_supplement_register_2026_10_13.md` | `b7f725de2d95c31e44047b4ed6baf6138b4266a5e1a008b11e7562ff36c1383d` | 22,448 | MATCH |
| 110 | `results/_pi_give_a_class_pilot_design_2026_10_14.md` | `sub/results/_pi_give_a_class_pilot_design_2026_10_14.md` | `5ec0638e94986312590b4248329a9d10ac3bc9b31ee0aaec83414029f5259b99` | 103,140 | MATCH |
| 111 | `results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | `sub/results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | `bb7ca983815032f6bb7324d7465766307fd8faaacb4fadc948c26ca5831e29b5` | 7,126 | MATCH |
| 112 | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | `sub/results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | `5ca1aa500fd839310a921e2d81fccf44f26327c4b506486a48008ae94bbfbb90` | 1,037 | MATCH |
| 113 | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `sub/results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `843e42ef4d2acb187d19286a776fc77dce81379e464e51e01bdb1296f39725b8` | 21,309 | MATCH |
| 114 | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `sub/results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `443efb39804ab3efe053db72e0df3eb04848fac8b6f348f20079d012759c5cf5` | 20,751 | MATCH |
| 115 | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `sub/results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936b6300154a0dd8e18b6b88e82939868620ea3d83486da2c099457a79a31e` | 14,234 | MATCH |
| 116 | `results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json` | `sub/results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json` | `24b0d5eda48ab799ad5432ecfade1eb6a15b491213b7d995396cf7e41934dfde` | 28,638 | MATCH |
| 117 | `results/_w1_stage2_premise_stale_register_2026_10_14.md` | `sub/results/_w1_stage2_premise_stale_register_2026_10_14.md` | `a7e14145e1c88993e3275df52ba545c597f80ee7d36aa3cfdd43d80a352fa401` | 8,326 | MATCH |
| 118 | `results/_xiang14_third_reissue_registration_2026_10_13.md` | `sub/results/_xiang14_third_reissue_registration_2026_10_13.md` | `25141de92c507975ab7a9d41bfec58de85b1d88db781e1a1c3b672d86f956d60` | 7,188 | MATCH |
| 119 | `reviews/deep_probe_R1.md` | `sub/reviews/deep_probe_R1.md` | `190dd5df9af29947ed9a4ec67b5c36c38256abb551446788e600d0dac6ae8749` | 14,895 | MATCH |
| 120 | `reviews/deep_probe_R2.md` | `sub/reviews/deep_probe_R2.md` | `a4f8a55b70ba5b5ec448541ff5d2d8faa74a839640a7ff386d3ac844d27fc4cf` | 23,391 | MATCH |
| 121 | `reviews/literature_scan_v2X_A.md` | `sub/reviews/literature_scan_v2X_A.md` | `d0bba9379b4b4d914d5348012a31f86676c22367cfb8326f472abf5efe38a341` | 18,876 | MATCH |
| 122 | `reviews/literature_scan_v2X_B.md` | `sub/reviews/literature_scan_v2X_B.md` | `313b30815a39893313be59136800fc296d8b6e2bdedc9aea22dee20474cb5c47` | 30,468 | MATCH |
| 123 | `reviews/peer_review_v19_A.md` | `sub/reviews/peer_review_v19_A.md` | `28878116d87becee2edca11b43735b379c44c241840b4c978ff345a08b5b475e` | 24,409 | MATCH |
| 124 | `reviews/peer_review_v19_B.md` | `sub/reviews/peer_review_v19_B.md` | `da98f9e310d40e9600ae9bed209b7d7acd907a88a66e8fedc8d6db2af597548e` | 42,672 | MATCH |
| 125 | `reviews/review_coach_v2X_draft.md` | `sub/reviews/review_coach_v2X_draft.md` | `0bafe659c00ddf32af6415007af260c2a6641c5581830f3668d63855a5d6a210` | 23,468 | MATCH |
| 126 | `reviews/review_format_v2X.md` | `sub/reviews/review_format_v2X.md` | `2dc4b45424ab3bb85f77ad2c6052916b34c407e1b4fed3b4bdc685cb5a5e41b1` | 6,656 | MATCH |
| 127 | `verifier/README.md` | `sub/verifier/README.md` | `d76f2dc473be455c77a442f6b53702f80b142d8143d425ccbb7d53db99774f80` | 14,360 | MATCH |
| 128 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `sub/verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `da517c115f3c4b73b0a9cb7990676bfc82d4524f8b097f439002972811f04a75` | 5,049 | MATCH |
| 129 | `verifier/handoff/P_A_V0_anchors_sha256_12.json` | `sub/verifier/handoff/P_A_V0_anchors_sha256_12.json` | `c4f029f780d8ebf31e899c9fb2ef3c8f84031cd46d8c6646a2bb73dd9d9ae9a5` | 7,796 | MATCH |
| 130 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `sub/verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `b41c98bf90ccd1ae740e5f8aa9b34485df56ac2c427d9261aa845870b94364d1` | 3,680 | MATCH |
| 131 | `verifier/kill_lines/GT_kill_line_carrier_v0.md` | `sub/verifier/kill_lines/GT_kill_line_carrier_v0.md` | `0f65a42e7a34518aa20d87e7fb260fc2cdf624d5e382d49202a9fead2a033dcd` | 16,486 | MATCH |
| 132 | `verifier/kill_lines/GT_kill_line_carrier_v1.md` | `sub/verifier/kill_lines/GT_kill_line_carrier_v1.md` | `9e09214cf0884d31961c1575c1300eda195bb462f3a811d1118b23e8ddaef34c` | 18,905 | MATCH |
| 133 | `verifier/runs/20260823T022721Z.log` | `sub/verifier/runs/20260823T022721Z.log` | `cf205dbb8cea84897b488abcc281bf96698d5e94b1096b16657b4caba9082a22` | 7 | MATCH |
| 134 | `verifier/runs/20260823T130229Z.log` | `sub/verifier/runs/20260823T130229Z.log` | `1af06784d975dab7ce0c5805f0ac7f57290384f5d32c7f2fecfa36513aaae0fa` | 839 | MATCH |
| 135 | `verifier/runs/20260823T130254Z.log` | `sub/verifier/runs/20260823T130254Z.log` | `8316e03518f2021c4b1e1c1e87470d49f69a695df0f0f4f45174277df87f74cd` | 839 | MATCH |
| 136 | `verifier/runs/20260823T130326Z.log` | `sub/verifier/runs/20260823T130326Z.log` | `e8698e422d69b87e65fa6a72582a3582b0364a2c51059bd03305450109a290c8` | 819 | MATCH |
| 137 | `verifier/runs/20260823T130405Z.log` | `sub/verifier/runs/20260823T130405Z.log` | `d6071ff9493e719a70591a0688a84eacd1da49cdb4e60bae9253bf40caaf75c7` | 576 | MATCH |
| 138 | `verifier/runs/20260823T131053Z.log` | `sub/verifier/runs/20260823T131053Z.log` | `94e57864959934e40aea58d773f0ec8a3ced3f19e5e5f4324278c4e783ebcd45` | 911 | MATCH |
| 139 | `verifier/runs/20260823T134128Z.log` | `sub/verifier/runs/20260823T134128Z.log` | `6cf95aade825f41c17756c644765e24d0b648ee035db02c495d1cd1ff260c217` | 910 | MATCH |
| 140 | `verifier/runs/20260823T134305Z.log` | `sub/verifier/runs/20260823T134305Z.log` | `c9ae2079fc1f90e24e88a414fa0c395b41ddd75af5a527d9b03306967253356b` | 972 | MATCH |
| 141 | `verifier/runs/20260823T154658Z.log` | `sub/verifier/runs/20260823T154658Z.log` | `1fca4529088384b4f1a636620524d4e9d9c5b6c40b8bebfa0c144f3e8fe51d4c` | 1,536 | MATCH |

### §4-2 回退 25 件之映射（新路径 → 旧路径 · 已复原）

| # | 回退件（repo 相对，已复原） | 原转出至 | 功能引用方（示例） | 复算 |
| --: | :-- | :-- | :-- | :-: |
| 1 | `docs/BASELINE_REGISTRY.md` | `sub/docs/BASELINE_REGISTRY.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 2 | `docs/CLOSURE_v19_and_v2X_gametheory.md` | `sub/docs/CLOSURE_v19_and_v2X_gametheory.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 3 | `docs/Findings_GT2B.md` | `sub/docs/Findings_GT2B.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 4 | `docs/Findings_GT3.md` | `sub/docs/Findings_GT3.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 5 | `docs/Findings_GT8.md` | `sub/docs/Findings_GT8.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 6 | `docs/Findings_GT8B.md` | `sub/docs/Findings_GT8B.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 7 | `docs/Findings_v2.0.md` | `sub/docs/Findings_v2.0.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 8 | `docs/Findings_v2.0_bigquiz.md` | `sub/docs/Findings_v2.0_bigquiz.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 9 | `docs/Findings_v2.0_boss.md` | `sub/docs/Findings_v2.0_boss.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 10 | `docs/Findings_v2.0_corrections.md` | `sub/docs/Findings_v2.0_corrections.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 11 | `docs/Findings_v2.0_crossval.md` | `sub/docs/Findings_v2.0_crossval.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 12 | `docs/Findings_v2.0_hardening.md` | `sub/docs/Findings_v2.0_hardening.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 13 | `docs/Findings_v2.0_photonics.md` | `sub/docs/Findings_v2.0_photonics.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 14 | `docs/Findings_v2.0_skills.md` | `sub/docs/Findings_v2.0_skills.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 15 | `docs/SPEC_GT3.md` | `sub/docs/SPEC_GT3.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 16 | `docs/SPEC_GT8B.md` | `sub/docs/SPEC_GT8B.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 17 | `docs/SPEC_v1.8.md` | `sub/docs/SPEC_v1.8.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 18 | `docs/SPEC_v2.0.md` | `sub/docs/SPEC_v2.0.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 19 | `docs/SPEC_v2.0_amendment1.md` | `sub/docs/SPEC_v2.0_amendment1.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 20 | `docs/SYNTHESIS_mind_game.md` | `sub/docs/SYNTHESIS_mind_game.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 21 | `reviews/post_draft_verification_v2X.md` | `sub/reviews/post_draft_verification_v2X.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 22 | `reviews/review_coach_v2X_draft_r2.md` | `sub/reviews/review_coach_v2X_draft_r2.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 23 | `reviews/review_coach_v2X_outline.md` | `sub/reviews/review_coach_v2X_outline.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 24 | `reviews/review_realign_v2X.md` | `sub/reviews/review_realign_v2X.md` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |
| 25 | `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | `sub/verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | `verifier/*/check.py`（`read_text()`）| RESTORED_MATCH |

### §4-3 文本引用面（**非 I/O** · 文档漂移 · 已登记映射）

净转移 141 件中，**164 件**被活代码注释/docstring 或在册 md 以**文件名/路径文本**提及（共 3288 处）。此类提及**不构成运行期断链**（代码不以其作 I/O 目标），但文档文本已过时 ⇒ **以上 §4-1 映射表即为「旧路径→新路径」之权威改写依据**（沿「移动交付件前须核引用」纪律）。

---

## §5 保留面与不动作面清单

### §5-1 保护闸门（任一命中即原地保留 · 冻结件 §3）

| 闸门 | 判据 | repo 命中件数 |
| :-- | :-- | --: |
| `SELF` | 本棒工件（`_r2_tool_`／`_stage3_r2_`） | 5（基线时点） |
| `PULLBACK` | `_remote_pullback_2026_10_17\`（219 件拉回成果 · 派工明列 ⛔ 0 动） | **219** |
| `DIR_RECENT` | 祖先目录名日期 ≥ `2026_10_16`（在途/近期棒产物面） | **713** |
| `RECENT` | `mtime ≥ 2026-10-16` | **1,367** |
| `CODE_REF` | 被活代码（repo 非 `.tmp` 之 `.py`）按路径或名引用 | **656** |
| `FUNC_REF_MD` | 被 `results`/`pi_rulings`/`letters` 之 md 以**可解析路径**引用 | **1,198** |
| `REPO_FRONTDOOR` | repo 根层件（`README*`／`RELEASE*` 等） | 17 |

### §5-2 `whitelist_backup_2026_10_17\` 之专项整棵保护（**棒自捕**）

该目录 **699** 件（38,301,580 B）多为 `results` 之逐位副本（A 型本可清 **470** 件），然：**①** 成员 mtime 保留旧值（2026-09-24…10-17）而绕过 `RECENT` 闸门；**②** **56** 件在册文本按目录名提及（`cleanup511_manifest_2026_10_17.json`／`card_reloc_m1_refscan_2026_10_17.json`／`d8x_*` 等）；**③** 由 **10-17 在途棒脚本**操作 ⇒ 依派工「在途/近期棒之产物面 ⛔ 0 动」**整棵保护**，候裁（§6-1）。

### §5-3 「功能归属存疑而 ⛔ 0 动」之面

| 面 | 件数 | 不动作之理由 |
| :-- | --: | :-- |
| `corpus\` | 24 | 代码依赖之数据面，移之即断链 |
| `letters\` | 18 | PI 委托/上传面（含「`letters/` 0 上传标注」纪律）|
| `paper\` | 3 | 论文源件（活面）|
| `deposon_team`／`tools`／`scripts`／`tests`／`attacks` | 5+ | 活代码/插件面 |
| sub 侧 `.py` 190 件 | 190 | 全为 9 月实验执行体；**0 件**属「误置 sub 之活面件」（其引用方皆为在册 md，且其孪生件已在 repo 活面）⇒ **sub→repo 方向 0 动作**，非「漏做」而是「无可归属者」 |

---

## §6 拉平面结论：🔴 ≤1.50:1 **不可达**（根因如实登记）

| 项 | 值 |
| :-- | --: |
| 整理前比 | 3.720 : 1 |
| 整理后比 | **3.354 : 1** |
| 达 ≤1.50 所需最少转移件数（清走后） | **915** |
| 本棒可用之合规转移池 | **141**（功能归属明确 ＋ 0 引用 ＋ 回退 25 后之净数）|
| **缺口** | **774 件** |
| 根因 | repo 增量之 **93%**（4,154/4,423）落于**受保护面**：近 3 日产物面 1,367 ＋ 目录级近期面 713 ＋ 拉回成果面 219 ＋ 在册 md 路径引用 1,198 ＋ 活代码引用 656 —— 其中 `results` 内既有之**绝对路径钉住**（先例载 600 件）移动即断链 |
| 口径观察（**仅供参考，非本棒之计量** · **终态实测**） | 若剔 repo 之 `.tmp` 与 sub 之 `.trae`／`tmp_movedout_*` 暂存面，则**文档面**为 **repo 2,014 件 / 67,496,331 B** ＋ **sub 1,211 件 / 56,107,786 B**，比 **1.663 : 1** —— 仍高于 1.50 ⇒ 即便改用文档面口径亦未达 |

📌 **⛔ 本棒 0 为动作而动作**：未以「移动受保护件」之方式凑比；未扩张判据。

---

## §7 停手候裁面（**0 自行扩张判据**）

| # | 面 | 件数 | 候裁之问 |
| :-: | :-- | --: | :-- |
| 1 | `.tmp\whitelist_backup_2026_10_17\` 整棵（其中 470 件为 `results` 逐位副本） | 699 | 是否于白昼授权清此备份面 |
| 2 | 近 3 日产物面 ＋ 目录级近期面 | 2,080 | 近期棒产物何时脱离「在途」身份 |
| 3 | 在册 md 路径引用面 ＋ 活代码引用面（含 600 件绝对路径钉住） | 1,854 | 是否允许「移动 ＋ 出映射」以解锁拉平 |
| 4 | **口径选择**（枚举 ≠ 功能引用；沿先例「取功能性引用而非清单行数」） | — | 若 PI 裁定裸名枚举/独立指纹亦构成保护 ⇒ 清走 **89→10** 件、转移 **141→0** 件 |
| 5 | 拉平口径本身（是否剔暂存面计量） | — | 见 §6 口径观察 |
| 6 | `KDS-4`（PI 未给执行面参数） | — | 本棒参数取先例，候 PI 裁 |
| 7 | `corpus`(24)／`letters`(18)／`paper`(3) 之归属 | 45 | 是否转至 sub（本棒 ⛔ 0 转）|
| 8 | 25 件「文本引用」之文档漂移（§4-3） | 141（涉 164 件引用面）| 是否另派棒批量改写注释/docstring 之路径文本 |

---

## §8 棒自捕之缺陷与限制（如实 · ⛔ 0 软化）

### §8-1 仪器缺陷（**已致实际动作** · 已当场补救）

**缺陷**：引用归因时对相对路径先 `.lower()` 再拼键，与磁盘实际大小写不符 ⇒ 凡文件名含大写字母者（如 `docs/SPEC_v2.0.md`）之引用**漏配** ⇒ 闸门 `CODE_REF` 对其失效。

- **潜在后果**：25 件被 `verifier/v9…v33/check.py` 以 `(ROOT / "docs/…").read_text()` **运行期读取**之件已被转移 ⇒ 断链 |
- **捕获点**：转移后专项复核（步骤23/25）—— 检出于盘 |
- **补救**：**25 件当场回退原位**，`RESTORED_MATCH 25/25`，复验**残余功能断链 0** |
- **教训**（沿先例 §2-4 之同族）：**分词/归因之任何键构造必须保真大小写**（Windows 文件系统大小写不敏感而字符串比较敏感 ⇒ 归因层须显式 `normcase` 双向一致） |

### §8-2 限制

1. **清点基线非静态**：`os.walk` 遍历错误 **0**；但本棒执行期间两区仍有他棒并发写入之可能 ⇒ 终态清点与件账对平之核对已逐件在案（§2 末），**未发现**非预期移除（0 件） |
2. **文本解码**：引用扫描 5,524 件文本中 **102 件**以 `errors=replace` 解码（含 GBK 之 `.ps1` 等）⇒ 该 102 件之引用归因**可能漏字**；本棒据此采取**保守面**（裸名提及全归） |
3. **功能引用之判定为行级启发**（`read_text/open(/Path(/os.path.join/json.load` 等 I/O 意图正则）⇒ 跨多行拼接之路径常量**可能漏判**；本棒对 141 净转移件已作**大小写无关全量复核**，仍建议 PI 于白昼以「改相对路径棒」正本（先例已载该棒之必要）|
4. **C 型判据 0 命中**：先例所载 `$null` 畸形名件**本棒实测 0 件**（两区全量 5,612 件扫描）⇒ 非漏做，为确无 |
5. **`KDS-4` 参数非 PI 逐字所给**：四型判据、保护面、拉平目标均**沿先例**径行（§1）|

---

## §9 字节级自报

| 项 | 值 |
| :-- | :-- |
| 落盘方式 | `io.open(encoding='utf-8', newline='\n')` 直写 |
| BOM | **0** |
| CRLF / CR | **0** |
| U+FFFD | **0** |
| 行数 | **474**（纯 LF） |
| 本件之 SHA-12／bytes | **自指不可内含** ⇒ 由落盘后**独立亲测回读**报回父会话（先例同此法：`_stage3_1_bulk_reorg_completion_register_2026_10_12.md` §2-5 亦列他件指纹、自件指纹报回） |
| 落前占位 | `Test-Path` ＝ `False`；glob `*stage3_r2*` ＝ **0** |

---

## §10 纪律自证

⛔ 0 落五终判 · ⛔ 0 宣告段毕/①毕 · ⛔ 0 代 PI 裁 · ⛔ 0 回改任何既有件一字 · ⛔ 0 永久删 · ⛔ 0 覆盖 · ⛔ 0 重命名既有件 · ⛔ 0 触 `D:\私人资料\_non_upload_local_archive` · ⛔ 0 触 `D:\私人资料\GLM` · ⛔ 0 联网 · ⛔ 0 读 key · ⛔ 0 联网文献调用 · 本棒既有件触动面 ＝ **清走 89（可恢复）＋ 转移 166（0 覆盖 · 0 断链 · 25 回退）＋ 自清 7** ｜ 新增件 ＝ 冻结件 1 ＋ 本登记件 1 ＋ 本棒脚本/日志（`.tmp/_r2_tool_*`） |

*件止。③段-R2 夜间整理棒 · 2026-10-18 · **清理/转移登记** —— 清走 **96**（判据 89 ＋ 自清 7 · 可恢复通道 · 验道 96/96）｜转移 166 → **净 141**（MATCH 141/FAIL 0 · 回退 25 · 残余功能断链 0）｜两区 **4,423/1,189 → 4,280/1,276**（比 **3.720 → 3.354**）｜🔴 ≤1.50 **不可达**（缺口 774 · 根因＝受保护面占 repo 增量 93%）｜⛔ 0 落五终判 · 0 宣告段毕/①毕 · 0 代 PI 裁 · 0 联网 · 0 触归档区*
