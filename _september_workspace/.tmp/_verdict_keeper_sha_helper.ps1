$ErrorActionPreference = 'Stop'
$files = @(
  'D:/私人资料/deposon-repo/results/_v4_supp_t15_result.json',
  'D:/私人资料/deposon-repo/results/_v4_supp_t15_executor.py',
  'D:/私人资料/deposon-repo/results/_v4_supp_prereg_v02_add_T15_2026_09_24.md',
  'D:/私人资料/deposon-repo/results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md',
  'D:/私人资料/deposon-repo/results/_v4_supp_t1_verdict.md'
)
foreach ($f in $files) {
  if (Test-Path $f) {
    $h = (Get-FileHash -Algorithm SHA256 $f).Hash.Substring(0,12)
    $b = (Get-Item $f).Length
    Write-Host ("SHA-12: {0}  size={1}  {2}" -f $h,$b,$f)
  } else {
    Write-Host ("MISSING  {0}" -f $f)
  }
}
