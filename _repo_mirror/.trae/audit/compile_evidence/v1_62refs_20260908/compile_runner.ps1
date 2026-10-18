$ErrorActionPreference = 'Continue'
$pdflatex = '〔本机路径〕\miktex-portable\texmfs\install\miktex\bin\x64\pdflatex.exe'
$env:PATH = "〔本机路径〕\miktex-portable\texmfs\install\miktex\bin\x64;$env:PATH"
$env:MIKTEX_AUTOINSTALL = '1'
$env:MIKTEX_USERINSTALL = '1'
$env:MIKTEX_USERCONFIG = '〔本机路径〕\deposon_compile\miktex-config'
$env:MIKTEX_USERDATA = '〔本机路径〕\deposon_compile\miktex-data'

function Run-Pass($dir, $tex, $log) {
    Set-Location $dir
    & $pdflatex -interaction=batchmode -recorder -file-line-error $tex *>&1 |
        Out-File -FilePath $log -Append -Encoding utf8
    $code = $LASTEXITCODE
    Add-Content -Path $log -Value "EXITCODE=$code"
    return $code
}

Remove-Item 〔本机路径〕\deposon_compile\en_run.log,〔本机路径〕\deposon_compile\cn_run.log,〔本机路径〕\deposon_compile\DONE.flag -ErrorAction SilentlyContinue
$en1 = Run-Pass '〔本机路径〕\deposon_compile\deposon_arxiv_en' 'deposon_paper_en.tex' '〔本机路径〕\deposon_compile\en_run.log'
$en2 = Run-Pass '〔本机路径〕\deposon_compile\deposon_arxiv_en' 'deposon_paper_en.tex' '〔本机路径〕\deposon_compile\en_run.log'
$cn1 = Run-Pass '〔本机路径〕\deposon_compile\deposon_arxiv_cn' 'deposon_paper_cn.tex' '〔本机路径〕\deposon_compile\cn_run.log'
$cn2 = Run-Pass '〔本机路径〕\deposon_compile\deposon_arxiv_cn' 'deposon_paper_cn.tex' '〔本机路径〕\deposon_compile\cn_run.log'
Add-Content 〔本机路径〕\deposon_compile\en_run.log "SUMMARY en_p1=$en1 en_p2=$en2"
Add-Content 〔本机路径〕\deposon_compile\cn_run.log "SUMMARY cn_p1=$cn1 cn_p2=$cn2"
"EN_P1=$en1 EN_P2=$en2 CN_P1=$cn1 CN_P2=$cn2" | Out-File 〔本机路径〕\deposon_compile\DONE.flag -Encoding ascii
