$ErrorActionPreference = 'Stop'
$f = (_dep_path "docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md")
$h = Get-FileHash -Algorithm SHA256 $f
$len = (Get-Item $f).Length
Write-Host ("file_len=" + $len)
Write-Host ("file_sha256=" + $h.Hash)
$lines = Get-Content -Path $f -Encoding UTF8

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

Write-Host ("total_lines=" + $lines.Count)
Write-Host "---last 6 lines---"
for ($i = $lines.Count - 5; $i -le $lines.Count; $i++) {
  Write-Host ("L" + $i + ": [" + $lines[$i-1].Length + "] " + $lines[$i-1])
}
