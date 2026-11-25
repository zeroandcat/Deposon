$ErrorActionPreference = 'Stop'
$repoRoot = (Get-Location).Path
$d2c = Join-Path $repoRoot 'results\_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json'
$ds = Join-Path $repoRoot 'results\_v4_pi_cot_v2_dataset.json'
$w1 = Join-Path $repoRoot 'results\_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json'
$w2 = Join-Path $repoRoot 'results\_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json'

function Get-SHA12($path) {
    $bytes = [System.IO.File]::ReadAllBytes($path)
    $h = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
    $full = ([BitConverter]::ToString($h) -replace '-', '')
    return @{ sha12 = $full.Substring(0,12); sha256 = $full; bytes = $bytes.Length }
}

$d2cInfo = Get-SHA12 $d2c
$dsInfo  = Get-SHA12 $ds
$w1Info  = Get-SHA12 $w1
$w2Info  = Get-SHA12 $w2

# Parse JSON to verify syntax
try {
    $json = Get-Content -Raw -Path $d2c -Encoding UTF8 | ConvertFrom-Json
    Write-Output ('JSON_PARSE: OK schema=' + $json.schema)
    Write-Output ('supplements_count: ' + $json.supplements.Count)
    Write-Output ('fingerprint_self_hash: ' + $json.fingerprint_self_hash_after_birth)
    Write-Output ('pre_post_dataset: ' + $json.addendum_for.dataset_sha12_pre + ' -> ' + $json.addendum_for.dataset_sha12_post)
    Write-Output ('pre_post_wave1:    ' + $json.addendum_for.d2_wave1_anchor_sha12_pre + ' -> ' + $json.addendum_for.d2_wave1_anchor_sha12_post)
    Write-Output ('pre_post_wave2:    ' + $json.addendum_for.d2_wave2_anchor_sha12_pre + ' -> ' + $json.addendum_for.d2_wave2_anchor_sha12_post)
    foreach ($s in $json.supplements) {
        Write-Output ('  - ' + $s.pair_id + ' | ' + $s.q_id + ' | option=' + $s.option_chosen + ' | reasoning_full=[' + $s.reasoning_full + ']')
    }
} catch {
    Write-Output ('JSON_PARSE_FAIL: ' + $_.Exception.Message)
}

Write-Output ('---FINAL_SHA---')
Write-Output ('FINAL_D2C_SHA12: ' + $d2cInfo.sha12)
Write-Output ('FINAL_D2C_BYTES: ' + $d2cInfo.bytes)
Write-Output ('FINAL_D2C_FULL256: ' + $d2cInfo.sha256)
Write-Output ('---ANCHOR_REVERIFY---')
Write-Output ('dataset_v11_SHA12: ' + $dsInfo.sha12 + ' (expect 7B01CD835A41)')
Write-Output ('d2_wave1_SHA12:    ' + $w1Info.sha12 + ' (expect 439721007AAF)')
Write-Output ('d2_wave2_SHA12:    ' + $w2Info.sha12 + ' (expect 41D6C28CA87C)')
Write-Output ('---DONE---')





Write-Output 'DONE'
