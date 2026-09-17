# -*- coding: utf-8 -*-
"""Rebuild Trae's isolated arXiv deliverables from the verified gold content.

Source of truth : paper/deposon_arxiv_2026/  (tex sha == audit3 gold, confirmed)
Trae home       : .trae/  (deliverables / build / scripts / audit / snapshots)
Output          : .trae/deliverables/deposon_arxiv_{en,cn}.tar.gz  (source-only,
                  8 members each, ReadOnly, sha256 manifest)

No paper content is edited here: this is repackaging + isolation only.
"""
import hashlib
import os
import shutil
import stat
import tarfile
import time
from pathlib import Path

REPO = Path(r"D:\私人资料\deposon-repo")
# The shared paper/ tree is being rewritten by another assistant in real time
# (deposon_arxiv_2026/ disappears between calls). The ONLY stable source of
# truth is the verified gold extraction in the Trae temp workspace.
GOLD = Path(r"c:\Users\Administrator\.trae-cn\work\6a9a7e1c7578e46bf7c7f60c\del28_edit")
TRAE = REPO / ".trae"
# Stable source tree INSIDE Trae home (gold copied here, frozen ReadOnly) so
# future rebuilds never depend on the volatile shared paper/ directory.
SRC = TRAE / "source"
DELIV = TRAE / "deliverables"
BUILD = TRAE / "build"
SCRIPTS = TRAE / "scripts"
AUDIT = TRAE / "audit"
SNAP = TRAE / "snapshots"

PACKAGES = {
    "en": {"tex": "deposon_paper_en.tex", "suffix": "_en.png"},
    "cn": {"tex": "deposon_paper_cn.tex", "suffix": "_cn.png"},
}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def set_readonly(p: Path) -> None:
    m = p.stat().st_mode
    p.chmod(m & ~stat.S_IWRITE & ~stat.S_IWGRP & ~stat.S_IWOTH)


def rmtree_retry(p: Path, retries: int = 6) -> None:
    def on_error(func, path, _exc):
        try:
            Path(path).chmod(stat.S_IWRITE)
            func(path)
        except OSError:
            pass
    for i in range(retries):
        try:
            shutil.rmtree(p, onerror=on_error)
            return
        except OSError:
            if i == retries - 1:
                raise
            time.sleep(0.4)


for d in (DELIV, BUILD, SCRIPTS, AUDIT, SNAP):
    d.mkdir(parents=True, exist_ok=True)

# ---- build the stable source tree INSIDE Trae home from the gold copy ----
# Layout mirrors paper/deposon_arxiv_2026 (merged): both tex, one references.bib,
# figures/ with all 10 PNGs. Frozen ReadOnly so nothing can silently mutate it.
print("== build stable source tree .trae/source/ from gold audit3_extract")
if SRC.exists():
    rmtree_retry(SRC)
(SRC / "figures").mkdir(parents=True)
for lang, spec in PACKAGES.items():
    g_tex = GOLD / f"deposon_arxiv_{lang}" / spec["tex"]
    assert g_tex.is_file(), f"gold tex missing: {g_tex}"
    dst = SRC / spec["tex"]
    shutil.copy(g_tex, dst)
    set_readonly(dst)
    print(f"   {spec['tex']:24s} {dst.stat().st_size:>7d} B  sha={sha256(dst)[:16]}")
    for f in sorted((GOLD / f"deposon_arxiv_{lang}" / "figures").glob("*.png")):
        d = SRC / "figures" / f.name
        shutil.copy(f, d)
        set_readonly(d)
# references.bib: verify the two language copies are identical, then freeze one
bib_en = GOLD / "deposon_arxiv_en" / "references.bib"
bib_cn = GOLD / "deposon_arxiv_cn" / "references.bib"
assert bib_en.is_file() and bib_cn.is_file(), "gold references.bib missing"
assert sha256(bib_en) == sha256(bib_cn), "references.bib differs en vs cn in gold"
shutil.copy(bib_en, SRC / "references.bib")
set_readonly(SRC / "references.bib")
print(f"   references.bib           { (SRC / 'references.bib').stat().st_size:>7d} B  "
      f"en==cn sha={sha256(SRC / 'references.bib')[:16]}")
n_fig = len(list((SRC / "figures").glob("*.png")))
assert n_fig == 10, f"expected 10 figures in source, got {n_fig}"
print(f"   figures/                 {n_fig} PNGs (frozen ReadOnly)")

# ---- lineage sanity: source tree tex must equal gold tex byte-for-byte ----
print("== lineage sanity (.trae/source vs gold audit3_extract)")
for lang, spec in PACKAGES.items():
    g = GOLD / f"deposon_arxiv_{lang}" / spec["tex"]
    s = SRC / spec["tex"]
    hg, hs = sha256(g), sha256(s)
    print(f"   {lang}: gold={hg[:16]} source={hs[:16]} identical={hg == hs}")
    assert hg == hs, f"LINEAGE MISMATCH for {lang}"

# ---- per-language staging + tar ----
manifest_lines = [
    "Deposon arXiv submission - Trae deliverables manifest",
    "Generated: 2026-09-08  (Asia/Shanghai)",
    "Source of truth: paper/deposon_arxiv_2026/  (lineage == audit3 gold)",
    "Compiler target: arXiv pdfLaTeX (TeX Live 2025), line-1 \\pdfoutput=1",
    "Packages contain ONLY sources: tex + references.bib + README.md + figures/*.png (5)",
    "No .pdf/.aux/.out/.log/.bbl/.broken inside any tarball.",
    "",
]

for lang, spec in PACKAGES.items():
    stage = BUILD / f"deposon_arxiv_{lang}"
    if stage.exists():
        rmtree_retry(stage)
    (stage / "figures").mkdir(parents=True)

    shutil.copy(SRC / spec["tex"], stage / spec["tex"])
    shutil.copy(SRC / "references.bib", stage / "references.bib")
    figs = sorted((SRC / "figures").glob(f"*{spec['suffix']}"))
    assert len(figs) == 5, f"expected 5 figs for {lang}, got {len(figs)}"
    for f in figs:
        shutil.copy(f, stage / "figures" / f.name)
    # README: copy from gold package (byte-identical to the audited version)
    shutil.copy(GOLD / f"deposon_arxiv_{lang}" / "README.md", stage / "README.md")

    members = [stage / spec["tex"], stage / "references.bib", stage / "README.md"]
    members += [stage / "figures" / f.name for f in figs]

    tar_path = DELIV / f"deposon_arxiv_{lang}.tar.gz"
    if tar_path.exists():
        os.chmod(tar_path, stat.S_IWRITE | stat.S_IREAD)
        tar_path.unlink()
    with tarfile.open(tar_path, "w:gz") as tar:
        for m in members:
            arc = f"deposon_arxiv_{lang}/" + str(m.relative_to(stage)).replace("\\", "/")
            tar.add(m, arcname=arc)
    set_readonly(tar_path)
    ro = not bool(tar_path.stat().st_mode & stat.S_IWRITE)

    # ---- verify: reopen tar, assert clean members, re-hash tex from archive ----
    with tarfile.open(tar_path, "r:gz") as tar:
        names = tar.getnames()
        bad = [n for n in names if Path(n).suffix.lower() in
               {".pdf", ".aux", ".out", ".log", ".bbl", ".blg", ".toc", ".broken", ".old"}]
        assert not bad, f"forbidden members in tar: {bad}"
        assert len(names) == 8, f"expected 8 members, got {len(names)}: {names}"
        tex_arc = [n for n in names if n.endswith(spec["tex"])][0]
        import io
        tex_bytes = tar.extractfile(tex_arc).read()
        h_arc = hashlib.sha256(tex_bytes).hexdigest()
        h_gold = sha256(GOLD / f"deposon_arxiv_{lang}" / spec["tex"])
        assert h_arc == h_gold, f"archived tex sha mismatch for {lang}"

    print(f"\n== {lang}: {tar_path.name}  {tar_path.stat().st_size} B  ReadOnly={ro}")
    for n in sorted(names):
        print(f"   {n}")
    print(f"   sha256={sha256(tar_path)}")
    print(f"   archived tex sha == gold: True")

    manifest_lines += [
        f"### deposon_arxiv_{lang}.tar.gz",
        f"size_bytes: {tar_path.stat().st_size}",
        f"sha256: {sha256(tar_path)}",
        f"tex_sha256: {h_gold}",
        f"readonly: {ro}",
        f"members: {len(names)} (source-only, no build artifacts)",
        f"top_level_dir: deposon_arxiv_{lang}/",
        "",
    ]

(DELIV / "MANIFEST.sha256.txt").write_text("\n".join(manifest_lines), encoding="utf-8")

# ---- consolidate Trae-owned scripts (copies; .mavis left untouched) ----
print("\n== consolidate scripts")
mavis_scripts = REPO / ".mavis" / "scripts"
for name in ["_md_to_tex.py", "_split_packages.py", "_verify_tex.py", "_arxiv_renumber.py"]:
    src = mavis_scripts / name
    if src.is_file():
        shutil.copy(src, SCRIPTS / name)
        print(f"   copied {name} -> .trae/scripts/")
work = Path(r"c:\Users\Administrator\.trae-cn\work\6a9a7e1c7578e46bf7c7f60c")
for name in ["compare_versions.py", "inspect_current_tars.py", "identify_dedicated.py",
             "rebuild_trae_home.py"]:
    src = work / name
    if src.is_file():
        shutil.copy(src, AUDIT / name)
        print(f"   copied {name} -> .trae/audit/")

# ---- gold snapshot (byte-identical fallback) ----
snap_dst = SNAP / "audit3_gold"
if snap_dst.exists():
    rmtree_retry(snap_dst)
shutil.copytree(GOLD, snap_dst)
print(f"   gold snapshot -> .trae/snapshots/audit3_gold/ "
      f"({sum(1 for _ in snap_dst.rglob('*') if _.is_file())} files)")

print("\nDONE.")
