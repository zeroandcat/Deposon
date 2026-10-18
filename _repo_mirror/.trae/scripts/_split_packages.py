# -*- coding: utf-8 -*-
"""FMT-007 (revised): split the merged intermediate package into two
single-language arXiv submission packages and build one tar.gz per language.

Inputs : paper/deposon_arxiv_2026/  (produced by _md_to_tex.py)
           - deposon_paper_en.tex, deposon_paper_cn.tex
           - references.bib
           - figures/fig{1..5}_*.png (10 files, both languages)
Outputs: paper/deposon_arxiv_en_pkg/  + paper/deposon_arxiv_en.tar.gz
         paper/deposon_arxiv_cn_pkg/  + paper/deposon_arxiv_cn.tar.gz

Each tar.gz contains ONLY: <lang>.tex, references.bib, figures/*.png (5,
language-matched), README.md — never .aux/.log/.pdf or other build artifacts.
A language-specific README.md is generated here (the merged package does not
ship one).
"""
import os
import shutil
import stat
import tarfile
import time
from pathlib import Path


def _set_readonly(path: Path) -> None:
    """Make a file read-only for everyone (Windows clears the write bit; on
    POSIX this is 0o444). The submission tarballs are frozen artifacts."""
    mode = path.stat().st_mode
    path.chmod(mode & ~stat.S_IWRITE & ~stat.S_IWGRP & ~stat.S_IWOTH)


def _rmtree_retry(path: Path, retries: int = 4) -> None:
    """rmtree with retries; Windows sometimes raises 'directory not empty'
    due to transient antivirus/indexer handles."""
    def _on_error(func, p, _exc):
        try:
            Path(p).chmod(stat.S_IWRITE)
            func(p)
        except OSError:
            pass
    for i in range(retries):
        try:
            shutil.rmtree(path, onerror=_on_error)
            return
        except OSError:
            if i == retries - 1:
                raise
            time.sleep(0.5)

REPO = Path(r"D:\私人资料\deposon-repo")
SRC = REPO / "paper" / "deposon_arxiv_2026"
OUT_BASE = REPO / "paper"

# --- explicit per-language specification (no and/or lambda precedence bugs) ---
PACKAGES = {
    "en": {
        "tex": "deposon_paper_en.tex",
        "fig_suffix": "_en.png",
    },
    "cn": {
        "tex": "deposon_paper_cn.tex",
        "fig_suffix": "_cn.png",
    },
}

README_EN = """# Deposon — arXiv submission package (English)

This package contains the English version of the paper:

**Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested
Scattering Layer over LLM Reasoning Paths**

## Contents

- `deposon_paper_en.tex` — LaTeX source (pdfLaTeX, `article` class)
- `references.bib` — BibTeX references (62 entries). The `.tex` file also
  embeds a `thebibliography` environment, so **no BibTeX run is required** to
  compile.
- `figures/` — 5 figures with English labels (PNG)
- `README.md` — this file

## Compilation

```
pdflatex deposon_paper_en.tex
pdflatex deposon_paper_en.tex
```

Run pdfLaTeX **twice** to resolve cross-references. Standard packages are used
(`graphicx`, `booktabs`, `longtable`, `amsmath`, `hyperref`, `geometry`).

## AI-use disclosure

Project version: deposon v0.1.1 (2026-09-08). The Deposon framework definition
and project guidance were provided by the corresponding author. The core
algorithm, the experimental pipeline, and the first draft of the manuscript
were produced with the assistance of KIMI (Moonshot AI); the author reviewed
and edited the manuscript and takes full responsibility for all content under
arXiv's authorship and AI-use policy.

## License

CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

## Reference numbering

References [1]–[34] are cited in the main text; references [35]–[62] are
retained in the bibliography for completeness.
"""

README_CN = """# Deposon（凝子）— arXiv 投稿包（中文版）

本包包含论文的中文版：

**Deposon：可审计、守恒保证、经博弈论检验的 LLM 推理路径散射层**

## 内容

- `deposon_paper_cn.tex` — LaTeX 源文件（pdfLaTeX，`article` 文档类）
- `references.bib` — BibTeX 参考文献（62 条）。`.tex` 文件内已内嵌
  `thebibliography` 环境，**编译无需运行 BibTeX**。
- `figures/` — 5 张中文标注图片（PNG）
- `README.md` — 本文件

## 编译方法

```
pdflatex deposon_paper_cn.tex
pdflatex deposon_paper_cn.tex
```

需运行 **两遍** pdfLaTeX 以解析交叉引用。中文版使用 `CJKutf8` 宏包与
`gbsn`（简体中文宋体）字体；使用 MiKTeX 时首次编译会自动下载安装所需
字体宏包（需联网），TeX Live 用户请确认已安装 CJK 相关宏包。

## AI 使用披露

项目版本：deposon v0.1.1（2026-09-08）。Deposon 框架定义与项目指导由通讯
作者提供；核心算法、实验管线与论文初稿由 KIMI（月之暗面 Moonshot AI）
协助完成，作者已审阅、修订全文，并依 arXiv 著作权与 AI 使用政策对全部
内容承担完全责任。

## 许可

CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

## 引用编号说明

参考文献 [1]–[34] 在正文中被引用；[35]–[62] 为完整保留的参考文献。
"""


def build_package(lang: str) -> None:
    spec = PACKAGES[lang]
    out_dir = OUT_BASE / f"deposon_arxiv_{lang}_pkg"
    if out_dir.exists():
        _rmtree_retry(out_dir)
    for _ in range(4):
        try:
            (out_dir / "figures").mkdir(parents=True, exist_ok=True)
            break
        except OSError:
            time.sleep(0.5)
    assert (out_dir / "figures").is_dir(), f"cannot create {out_dir / 'figures'}"

    # 1. tex (explicit filename)
    src_tex = SRC / spec["tex"]
    assert src_tex.is_file(), f"missing {src_tex}"
    shutil.copy(src_tex, out_dir / spec["tex"])

    # 2. references.bib
    src_bib = SRC / "references.bib"
    assert src_bib.is_file(), f"missing {src_bib}"
    shutil.copy(src_bib, out_dir / "references.bib")

    # 3. figures: exactly the 5 language-matched PNGs
    src_fig_dir = SRC / "figures"
    figs = sorted(p for p in src_fig_dir.glob("*.png")
                  if p.name.endswith(spec["fig_suffix"]))
    assert len(figs) == 5, f"expected 5 figures for {lang}, found {len(figs)}"
    for f in figs:
        shutil.copy(f, out_dir / "figures" / f.name)

    # 4. language-specific README (generated here)
    readme = README_EN if lang == "en" else README_CN
    (out_dir / "README.md").write_text(readme, encoding="utf-8")

    # 5. tar.gz — explicit member list, top-level dir deposon_arxiv_<lang>
    tar_path = OUT_BASE / f"deposon_arxiv_{lang}.tar.gz"
    if tar_path.exists():
        # an older build may have marked the tar read-only; clear the write bit
        # before unlinking so the rebuild never fails on a frozen artifact
        os.chmod(tar_path, stat.S_IWRITE | stat.S_IREAD)
        tar_path.unlink()
    members = [out_dir / spec["tex"], out_dir / "references.bib",
               out_dir / "README.md"] + [out_dir / "figures" / f.name for f in figs]
    with tarfile.open(tar_path, "w:gz") as tar:
        for m in members:
            arc = f"deposon_arxiv_{lang}/" + str(m.relative_to(out_dir)).replace("\\", "/")
            tar.add(m, arcname=arc)

    # freeze the tarball: read-only submission artifact (must not be rewritten
    # by accident after the build)
    _set_readonly(tar_path)
    ro = not bool(tar_path.stat().st_mode & stat.S_IWRITE)

    print(f"== package {lang}: {out_dir}")
    for m in members:
        print(f"   {m.relative_to(out_dir)}  {m.stat().st_size} bytes")
    print(f"   tar: {tar_path}  {tar_path.stat().st_size} bytes  ReadOnly={ro}")
    with tarfile.open(tar_path, "r:gz") as tar:
        print(f"   tar members ({len(tar.getmembers())}):")
        for t in tar.getmembers():
            print(f"      {t.name}  {t.size} bytes")
    print()


if __name__ == "__main__":
    for _lang in ("en", "cn"):
        build_package(_lang)
    print("Done.")
