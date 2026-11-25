# V3X GitHub 上线×第二作备忘（清单 V4）

阿兰｜2026-09-16｜只读核阅：KIMI 委托信、项目梳理信、判死报告（verdict 占位）、D7_GITHUB_PUSH_RECEIVE V1/V2、Trae 09-16 修复信与主动审查报告。零推断，数字均出自信载文件。

## ① 实际影响：push 已完成（早于 09-18）

关键事实更正：push 并非预计 09-18——user 已于 09-15 17:13 通报完成：仓库 `zeroandcat/Deposon` main 分支，新目录 `v3x-1week-kill-2026-09-18/`，398 文件 13 MB，commit `9678ec4`（全量 398/398 核验＋17 锚全 PASS）。但该 commit 系 interim：判死报告 4 路径 verdict 仍占位待 D7；且约 70 个文件含明文 ark- key，user 17:26 拍板 C「不轮换 SAME key、D7 后清理源仓文档并 re-commit」（D7_POST_CLEANUP_PLAN_2026_09_18.json）。

对第二作定性不变（工件≠可检索文献）：不占先例、不入 to-our-knowledge 检索范围、不计 61 条基数；六处链头挂钩表述全部维持（沿 09-15 备忘②）。引用案沿 V2：仅 Availability 一句＋commit hash，不进参考文献表。

表述草案（arXiv 版可用，hash 待 D7 后填）：
"A same-source extension artifact—a pre-registered one-week kill trial with frozen JSON results and SHA-256 verification anchors—is publicly available at https://github.com/zeroandcat/Deposon (subdirectory v3x-1week-kill-2026-09-18/, commit ⟨hash⟩)."
双盲 venue 版：URL 须换匿名镜像或整句延至 camera-ready。

## ② 清单 V4（触发条件逐条重审）

1. 「09-18 前投稿勿引 URL」→**失效删除**：仓库 09-15 已在线，该分支不可能再触发。
2. 「D7 后引用案」→**触发时点变更**：URL 即刻可达，但可引 hash 须待 D7 脱敏 re-commit 完成——`9678ec4` 含暴露 key 且将被重写，引之无意义（且会把读者引向含明文 key 的版本）；核验项新增：仓库可见性＝public 确认、脱敏完成确认。另信载立即处理项：PAT `ghp_Ecfr…RAG` 须吊销。
3. 「知悉 D7 结果」→**维持**（09-18，仅校准视野）。
4. 「V4 上 arXiv 早于投稿日＝唯一真触发」→**不触发**（V4 无日期，user 13:39「不急定位 V4」）。
5. 「10-15 后投稿重跑 30 天查新」→**不触发**（查新基准 09-15，与 GitHub 无关）。
6. 「双盲匿名化」→**强化**：仓库挂 zeroandcat 个人命名空间，docs 内含用户决策记录，身份信息密度高；双盲版必须匿名化或延后。
7. Trae A1（commit msg 曾预写 D7 结论、已占位符化）对第二作无新增影响，verdict 以 D7 实测为准，勿在 D7 前引任何「终极判死」结论。

## ③ 打包与投稿时点建议

先后关系：用户本地双审（唯一硬前置）→ D7 09-18（verdict 回填＋脱敏 re-commit，hash 稳定）→ tar.gz 打包（Availability 取稳定 hash）→ 投稿/arXiv 上传，全程宜在 10-15 前完成（30 天查新保鲜期内）。建议窗口 **09-19～10-15**。若双审拖过 10-15：重跑查新后再投。若 Availability 不引 repo：双审通过即可打包，D7 仅作校准；arXiv 版与双盲版 Availability 句分叉维护。
