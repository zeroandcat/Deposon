param([string]$Dir, [string]$List, [switch]$Execute)
$ErrorActionPreference = 'Continue'
if (-not (Test-Path -LiteralPath $Dir)) { Write-Host 'ABORT dir'; exit 2 }
if (-not (Test-Path -LiteralPath $List)) { Write-Host 'ABORT list'; exit 2 }
$names = Get-Content -LiteralPath $List -Encoding UTF8
Write-Host ('list: {0}' -f $names.Count)
$n = 0; $skip = 0; $fail = 0
foreach ($nm in $names) {
    if (-not $nm.Trim()) { continue }
    $p = Join-Path $Dir $nm.Trim()
    if (-not (Test-Path -LiteralPath $p)) { $skip++; continue }
    if (-not $Execute) { $n++; continue }
    try {
        rm -- "$p"
        if (Test-Path -LiteralPath $p) { $fail++ } else { $n++ }
    } catch { $fail++ }
}
if ($Execute) {
    Write-Host ('DONE deleted={0} skip={1} fail={2}' -f $n, $skip, $fail)
    Write-Host ('left: {0}' -f (Get-ChildItem -LiteralPath $Dir -File -Force).Count)
} else {
    Write-Host ('DRYRUN would={0} skip={1}' -f $n, $skip)
}
