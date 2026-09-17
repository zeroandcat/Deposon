# Transfer plan executor - 沿 user 14:54 + 15:40 + 15:46 "按推荐来"
# 严守 7 铁律 0 触动 18 frozen + P-G V0 spec

$ErrorActionPreference = 'Stop'
$srcBase = 'D:\私人资料\deposon-repo'
$dstBase = 'D:\私人资料\_mavis_external'

# 创建目标子目录
$subdirs = @('installers', 'backups', 'logs', 'proposals', 'scripts', 'reports', 'cache', 'tmp')
foreach ($sub in $subdirs) {
    $path = Join-Path $dstBase $sub
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
        Write-Host "CREATED: $path"
    } else {
        Write-Host "EXISTS: $path"
    }
}

# 转移计划
$transfers = @(
    @{ src = "$srcBase\.mavis\installers"; dst = "$dstBase\installers"; size = 0 },
    @{ src = "$srcBase\.mavis\backups"; dst = "$dstBase\backups"; size = 0 },
    @{ src = "$srcBase\.mavis\logs"; dst = "$dstBase\logs"; size = 0 },
    @{ src = "$srcBase\.mavis\proposals"; dst = "$dstBase\proposals"; size = 0 },
    @{ src = "$srcBase\.mavis\scripts"; dst = "$dstBase\scripts"; size = 0 },
    @{ src = "$srcBase\.mavis\reports"; dst = "$dstBase\reports"; size = 0 },
    @{ src = "$srcBase\.mavis\cache"; dst = "$dstBase\cache"; size = 0 },
    @{ src = "$srcBase\.tmp"; dst = "$dstBase\tmp\.tmp"; size = 0 },
    @{ src = "$srcBase\.tmp_volcengine_2026_09_10"; dst = "$dstBase\tmp\.tmp_volcengine_2026_09_10"; size = 0 },
    @{ src = "$srcBase\__pycache__"; dst = "$dstBase\tmp\__pycache__"; size = 0 },
    @{ src = "$srcBase\.pytest_cache"; dst = "$dstBase\tmp\.pytest_cache"; size = 0 }
)

foreach ($t in $transfers) {
    $src = $t.src
    $dst = $t.dst
    if (Test-Path $src) {
        # 算大小
        $size = (Get-ChildItem -Path $src -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum
        $files = (Get-ChildItem -Path $src -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
        Write-Host ""
        Write-Host "TRANSFER: $src"
        Write-Host "  size: $([math]::Round($size/1MB,2)) MB ($files files)"
        Write-Host "  -> $dst"
        try {
            Move-Item -Path $src -Destination $dst -Force
            Write-Host "  STATUS: OK"
        } catch {
            Write-Host "  STATUS: FAILED - $_"
            throw
        }
    } else {
        Write-Host ""
        Write-Host "SKIP (not exists): $src"
    }
}

Write-Host ""
Write-Host "===== Transfer complete ====="
Write-Host "Source: $srcBase"
Write-Host "Dest:   $dstBase"
