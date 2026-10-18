# 碰撞 16 件（第三方改动件）逐件清单 · 入档件 ｜ 2026-10-18

- 依据：PI 卡 `ask_49c507b84a1831e89f233a0d` Q6 之裁（2026-10-18 10:31:41.880 生效）：**0 覆盖 ＋ 逐件清单入档**（沿 H5 停手登记之例——覆盖即毁第三方之工作）
- 窗口：10-12（R2 终态 `f44996fbfd9f`，3,063 blobs）→ 10-17（快照 `74c7d769`，3,076 blobs，+13）间第三方推送所涉
- 处置：远端版本维持不动 ⛔ 上传侧 0 以本地件覆盖；第三方改动之内容面不在本侧射程（⛔ 0 复核其内容、⛔ 0 主张其当否），处置实质归 PI
- 指纹口径：git blob sha1（40 位十六进制）；`local`＝本地两区实测，`remote`＝远端 `74c7d769` 树实测（序0 重核 `daf70334` 树 0 漂移）

| # | 仓内相对路径（rel） | 区 | local git sha1 | remote git sha1 | remote bytes |
|--:|---|:-:|---|---|--:|
| 1 | `results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | SUB | `18a9f0bc64099e6705506313266616bd19ded0ae` | `d15d568263ea4718a1efc9054ff71dcfb8dc4a23` | 29,664 |
| 2 | `results/_kd_heteronym_classification_disposition_2026_10_09.md` | SUB | `ac32249b79c98eff5e2b7f65c3fafc9fd1f27828` | `b599603f8215652e7f00b7cccf556a4b022968d4` | 29,761 |
| 3 | `results/_kd_resolvability_and_optional_experiments_2026_10_09.md` | SUB | `a69fcae9ce3d6ae34df8f946fe03eb38015fdf4d` | `23b1ac0af9e5e715212eb8ee7fd96424dad5338e` | 70,328 |
| 4 | `results/_kd_writing_convention_guidance_2026_10_09.md` | REPO | `f1c7d5d987c73967b6634116ab9f7bebf8f8c12c` | `31344dc9a77d5e6ed1dc089a6b94046c921cad25` | 20,179 |
| 5 | `results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | SUB | `826ea32705edb5aee1b2b8e3364edbf7aa3b5976` | `e59531f0622353d32f62cbfdc805b025777bbb9b` | 32,296 |
| 6 | `results/_mini_round_6_7_settlement_register_2026_10_01.md` | SUB | `518b209d97b452921aeb39182577515a86f63028` | `12c3be4c2a40bf12d0544ddbd9db57ae17859047` | 68,053 |
| 7 | `results/_s3_d1_rulings_supplement_register_2026_10_01.md` | SUB | `d60dadddb99cf7df58e392a613cd9551144d3c72` | `17ba92d24cd4cfd63bd089cb1b290ec5fc9c6f81` | 28,762 |
| 8 | `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | SUB | `dcd1fc53e83c6695043b2109ddf0560ea95c4d79` | `d03126028128994eb0fc2538422e9532bb4e371c` | 18,923 |
| 9 | `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | SUB | `ee0f43b1fe83d44c40751db9e959ded04c3e777a` | `1b1f027db26465eab45c95cf5f1fd7b8912ac959` | 52,655 |
| 10 | `results/_s4prime_readings_runner_2026_10_11.py` | SUB | `a951729c2167330fa9ed6b90e3bb3ab170d660f4` | `1ea33216570264351d13b62a9cfb15c82d3ea24f` | 23,766 |
| 11 | `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | SUB | `8b48768dd2b6b015a616caa82521d5e5fb9f521d` | `93d13cd8a5fa7f15aa7710c01c67d5624396aa50` | 31,138 |
| 12 | `results/_t1_substrate_gap_precondition_2026_10_01.md` | REPO | `8ec92ab97e47f07c7f0e84e01d1134a7fa405d4c` | `62d7d7c4bee94efc496694914f6731410d397200` | 22,196 |
| 13 | `results/_v3_recheck_05_executor_2026_09_28.py` | SUB | `3dbba73f89d22a8079001c9de9b49eec46dfd1e4` | `01b8e0ccd9900202a9f28c93b05577c98561527a` | 38,639 |
| 14 | `results/_v3_recheck_05_result_2026_09_28.json` | REPO | `eda36fcfe0df8c81cf76af9e048af4fb3d106317` | `948ae3ece2245f693b52c87e6f868547d9e5ba0b` | 450,701 |
| 15 | `results/_verdict_pack_d_prep_2026_10_01.md` | SUB | `2c441b0d9326af65cfb7c994f1ec6426d11f6089` | `de93624ff635244f759b7c0f82b2544613252bee` | 49,471 |
| 16 | `tools/exp_harness.py` | REPO | `41625e64df7c03e0999c5817838a01dd669d4e4b` | `b440f527eb54d1761d1b99f41c6f1c673da3d5c1` | 10,090 |

## 补充登记

- 本 16 件与 R2 脱敏覆盖件（447）及 `.gitignore`（止血点标的，序1 已同步为独立 commit）合计 464 件碰撞面；依 Q5/Q6 之裁 **464 件全 0 覆盖**。
- 序0（2026-10-18 执行时）重核：16 件远端 sha 相对备战读数 **0 漂移**。
- 本件 0 密钥明文、0 PAT 片段、0 推理文本引用。
