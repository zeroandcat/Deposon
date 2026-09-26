$ErrorActionPreference = 'Stop'
$dir = 'D:\私人资料\deposon-repo\results'
$names = @(
    '_v4_supp_t15r2_result.json',
    '_v4_supp_t15r2_executor.py',
    '_v4_supp_prereg_v02_add_T15r2_2026_09_26.md',
    '_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md',
    '_v4_supp_t15_verdict.md'
)
foreach ($n in $names) {
    $full = Join-Path $dir $n
    $bytes = [System.IO.File]::ReadAllBytes($full)
    $h = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
    $hex = -join ($h | ForEach-Object { $_.ToString('x2') })
    $sha12 = $hex.Substring(0, 12).ToUpper()
    $len = $bytes.Length
    Write-Output ("{0,-60} | sha12={1} | bytes={2}" -f $n, $sha12, $len)
}