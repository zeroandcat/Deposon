$files = @(
    'D:/私人资料/deposon-repo/results/_v4_supp_t15r2_result.json',
    'D:/私人资料/deposon-repo/results/_v4_supp_t15r2_executor.py',
    'D:/私人资料/deposon-repo/results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md',
    'D:/私人资料/deposon-repo/results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md',
    'D:/私人资料/deposon-repo/results/_v4_supp_t15_verdict.md'
)
foreach ($f in $files) {
    $b = [System.IO.File]::ReadAllBytes($f)
    $h = (Get-FileHash -Algorithm SHA256 -InputStream ([System.IO.MemoryStream]::new($b))).Hash.Substring(0,12)
    $len = $b.Length
    $name = Split-Path $f -Leaf
    Write-Output ('{0}|{1}|{2}' -f $name, $h, $len)
}