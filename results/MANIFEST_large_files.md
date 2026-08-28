# MANIFEST — 大体量结果文件（不入库，sha256 留痕 + 再生命令）

> 以下文件体积过大，按「无论文留痕」同原则不推送到 GitHub；
> 每行记录 sha256 与再生命令，任何人可本地复算校验。
> 更正（2026-08-28）：quizbank_v20_big 与 bigquiz_eval 两条曾因传输笔误写入占位哈希，
> 已更正为真实值（本文件为准）。

- `results/deposon_v15_diffusion.json`  
  sha256: `c16d1768d1cad8651a9e852dc7f0e2d3fb42cea17ebdb8c58c0bd43c6e62e56a`  
  再生: `python3 run_v15_experiment.py`
- `results/deposon_v15_diffusion_maxpath_negativeresult.json`  
  sha256: `00ee97c82dccd8a9eba4d82b4d36ecf59bce0a570e67ff0987616cdcceb6efb5`  
  再生: `python3 run_v15_experiment.py --maxpath`
- `results/deposon_v19_benchmark_fixes.json`  
  sha256: `910c4333eead7940f41545b06e5a0daa764456e808d374f36ce6bbdd5b87932c`  
  再生: `python3 run_v19_benchmark_fixes.py`
- `results/deposon_benchmark_v1_4_gsm8k_details.json`  
  sha256: `39f79fce7cdb404ce1cca2730cb97cb07de4f7a260600bc08866e0e3740c5dfd`  
  再生: `python3 run_benchmark_v1_4_gsm8k.py`
- `results/deposon_benchmark_v1_4_strategyqa_details.json`  
  sha256: `85d6cc1cd7b358bf3ab8fb54466e86877379d2770ff5d5e6dc0b73a5b0b1860a`  
  再生: `python3 run_benchmark_v1_4_strategyqa.py`
- `results/deposon_benchmark_v1_3_details.json`  
  sha256: `9fcb6b243e0d78c443b3f62e1e6545c6f7f2999b76d6c8663d4e963dc2a2f234`  
  再生: `python3 run_benchmark_v1_3.py`
- `results/deposon_v17_fusion_fix_tieartifact_negativeresult.json`  
  sha256: `556086d9e3bc1c7f85bf76d5dbee0e2126aa0b879f0258023c666900be3d28d8`  
  再生: `python3 run_v17_fusion_fix.py`
- `results/deposon_v20_corpus_eval.json`  
  sha256: `c4b04014491669fbf22e97188cb5ed24fb236a21b0c62c4a92a5bcb0427785f3`  
  再生: `python3 run_v20_corpus_eval.py --families=S,L`
- `results/deposon_v17_fixed_sampler.json`  
  sha256: `701ad291a714f75c79967f569059c463057a238119668416d156194b4b95f765`  
  再生: `python3 run_v17_fusion_fix.py  # fixed_sampler 由 v1.7.1 管线产生`
- `results/deposon_v17_fusion_fix.json`  
  sha256: `af51da229652b84ad908a100d71a9b442fd27214e456b33646d3c48e862bef14`  
  再生: `python3 run_v17_fusion_fix.py`
- `audits_outliers.json`  
  sha256: `3b1c881c4594327ff5878453cfd40b88ee83fcab1ce44ba62debbcdc51ae8954`  
  再生: `python3 /app/.agents/skills/outlier-scan/scripts/anomaly_detector.py results/v19_edges_audit_input.csv`
- `results/quizbank_v20.json`  
  sha256: `f6035466ff3d478144b0791e7aa5b3a69ce9493ed2bb9410cbf4719fc83c204d`  
  再生: `python3 run_v20_quizbank.py  # 由 BANK_SEED + gt2_attacker_cache 确定性再生`
- `results/v20_regression_field.json`  
  sha256: `534c121765b132044ea29a05e2ca67723767e0089055193b3747b1a78e4f0ee7`  
  再生: `python3 /app/.agents/skills/regression-insight/scripts/regression_analyzer.py results/v20_graph_features.csv --target field_named --features "N,n_edges,density,hub_concentration,real_semantics"  # v1 全特征版（VIF 问题），v2 精简版已入库`
- `results/quizbank_v20_big.json`  
  sha256: `da6fecdcbbf6f94036f2a0968ce27b0ccdccd699e24e6b868ce75bdbe510aed4`  
  再生: `python3 run_v20_bigquiz_eval.py  # 由 BANK_SEED + attacker_xl_cache 确定性再生`
- `results/deposon_v20_bigquiz_eval.json`  
  sha256: `283dbc8c5b638769b6c6ecdb6afb6621c82b7704fb2c9242794a6ca81b724923`  
  再生: `python3 run_v20_bigquiz_eval.py  # 5.5s 再生；accuracy 汇总见 docs/Findings_v2.0_bigquiz.md`
