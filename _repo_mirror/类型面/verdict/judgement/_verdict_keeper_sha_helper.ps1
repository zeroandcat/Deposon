$ErrorActionPreference = 'Stop'
$files = @(
  (_dep_path "results/_v4_supp_t15_result.json"),
  (_dep_path "results/_v4_supp_t15_executor.py"),
  (_dep_path "results/_v4_supp_prereg_v02_add_T15_2026_09_24.md"),
  (_dep_path "results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md"),
  (_dep_path "results/_v4_supp_t1_verdict.md")
)
foreach ($f in $files) {
  if (Test-Path $f) {
    $h = (Get-FileHash -Algorithm SHA256 $f).Hash.Substring(0,12)
    $b = (Get-Item $f).Length

function _dep_path([string]$rel) {
    $roots = @()
    $p = $PSScriptRoot
    for ($i = 0; $i -lt 7 -and $p; $i++) { $roots += $p; $p = Split-Path $p -Parent }
    foreach ($r in $roots) { $t = Join-Path $r $rel; if (Test-Path -LiteralPath $t) { return $t } }
    $name = Split-Path $rel -Leaf
    if ($name) {
        foreach ($r in $roots) {
            $f = Get-ChildItem -LiteralPath $r -Recurse -Filter $name -File -ErrorAction SilentlyContinue | Select-Object -First 1
            if ($f) { return $f.FullName }
        }
    }
    return $rel
}

    Write-Host ("SHA-12: {0}  size={1}  {2}" -f $h,$b,$f)
  } else {
    Write-Host ("MISSING  {0}" -f $f)
  }
}
