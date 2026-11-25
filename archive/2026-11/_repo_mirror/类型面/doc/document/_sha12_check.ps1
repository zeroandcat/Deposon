$files = @(
    (_dep_path "results/_v4_supp_t15r2_result.json"),
    (_dep_path "results/_v4_supp_t15r2_executor.py"),
    (_dep_path "results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md"),
    (_dep_path "results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md"),
    (_dep_path "results/_v4_supp_t15_verdict.md")
)
foreach ($f in $files) {
    $b = [System.IO.File]::ReadAllBytes($f)
    $h = (Get-FileHash -Algorithm SHA256 -InputStream ([System.IO.MemoryStream]::new($b))).Hash.Substring(0,12)
    $len = $b.Length
    $name = Split-Path $f -Leaf

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

    Write-Output ('{0}|{1}|{2}' -f $name, $h, $len)
}