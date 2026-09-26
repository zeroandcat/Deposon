$ErrorActionPreference = 'Stop'
$f = 'D:\私人资料\deposon-repo\docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md'
$h = Get-FileHash -Algorithm SHA256 $f
$len = (Get-Item $f).Length
Write-Host ("file_len=" + $len)
Write-Host ("file_sha256=" + $h.Hash)
$lines = Get-Content -Path $f -Encoding UTF8
Write-Host ("total_lines=" + $lines.Count)
Write-Host "---last 6 lines---"
for ($i = $lines.Count - 5; $i -le $lines.Count; $i++) {
  Write-Host ("L" + $i + ": [" + $lines[$i-1].Length + "] " + $lines[$i-1])
}
