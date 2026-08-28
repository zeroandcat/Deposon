# MANIFEST — 大体量结果文件（不入库，sha256 留痕 + 再生命令）

> 以下文件体积过大，按「无论文留痕」同原则不推送到 GitHub；
> 每行记录 sha256 与再生命令，任何人可本地复算校验。

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
