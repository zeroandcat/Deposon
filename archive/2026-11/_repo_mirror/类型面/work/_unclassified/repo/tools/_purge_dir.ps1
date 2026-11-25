param([string]$Dir, [switch]$Execute)
$ErrorActionPreference = 'Stop'
if (-not $Dir -or -not (Test-Path -LiteralPath $Dir)) { Write-Host 'ABORT: dir not found'; exit 2 }
$files = Get-ChildItem -LiteralPath $Dir -File -Force | Sort-Object Name
Write-Host ('count: {0}' -f $files.Count)
$n = 0
$skip = 0
$fail = 0
foreach ($f in $files) {
    $p = $f.FullName
    if (-not $p.StartsWith($Dir, [System.StringComparison]::OrdinalIgnoreCase)) { Write-Host ('SKIP {0}' -f $p); $skip++; continue }
    if (-not (Test-Path -LiteralPath $p)) { $skip++; continue }
    if (-not $Execute) { $n++; continue }
    try {
        rm -- "$p"
        if (Test-Path -LiteralPath $p) { $fail++ } else { $n++ }
    } catch {
        $fail++
    }
}
if ($Execute) {
    Write-Host ('DONE deleted={0} skip={1} fail={2}' -f $n, $skip, $fail)
    Write-Host ('left: {0}' -f (Get-ChildItem -LiteralPath $Dir -File -Force).Count)
} else {
    Write-Host ('DRYRUN total={0}' -f $n)
}
