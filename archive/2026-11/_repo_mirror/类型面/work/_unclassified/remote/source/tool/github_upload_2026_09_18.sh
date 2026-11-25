#!/bin/bash
# V3X 1 Week Kill Report (2026-09-18) — github 上传脚本
# 严守: 7 铁律 + 18 frozen 0 触动
# 配套: LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md

set -e

# ============================================================
# 配置(沿 user 拍板仓库命名空间)
# ============================================================
GITHUB_USER="<your-github-username>"        # TODO: user 拍板
GITHUB_REPO="deposon-v3x-1week-kill"          # TODO: user 拍板仓库名
GITHUB_BRANCH="main"                          # 主分支
COMMIT_MSG_FILE="deposon_team/plugins/git_commit_msg_2026_09_18.txt"
RELEASE_TAG="v3.0.0-1week-kill-2026-09-18"   # release 标签

# ============================================================
# 0. 严守 7 铁律 + 18 frozen 验证(必须先 verify 再 push)
# ============================================================
echo "[Step 0] 验证 16 frozen + P-G V0 + P-G V0.1 spec 0 触动"
python deposon_team/plugins/_verify_15frozen.py 2>&1 | tail -20

if ! python deposon_team/plugins/_verify_15frozen.py 2>&1 | grep -q "0-touch declaration: PASS"; then
    echo "[ERROR] 16 frozen verify FAIL, 不允许上传"
    exit 1
fi

# ============================================================
# 1. 检查 git 配置
# ============================================================
echo "[Step 1] 检查 git 配置"
git --version
git config --global user.name 2>/dev/null || echo "WARNING: git user.name not set"
git config --global user.email 2>/dev/null || echo "WARNING: git user.email not set"

# ============================================================
# 2. 检查 git remote
# ============================================================
echo "[Step 2] 检查 git remote"
if [ -z "$(git remote -v 2>/dev/null | grep origin)" ]; then
    echo "[INFO] 未配置 origin remote, 需要:"
    echo "  git remote add origin git@github.com:${GITHUB_USER}/${GITHUB_REPO}.git"
    echo "  (或 git remote add origin https://github.com/${GITHUB_USER}/${GITHUB_REPO}.git)"
    echo ""
    echo "  TODO: user 在 github 创建空仓库 ${GITHUB_REPO} 后, 配置 origin"
    exit 1
fi

# ============================================================
# 3. 检查 git status(必须先 0 触动 frozen)
# ============================================================
echo "[Step 3] 检查 git status"
git status --short

# [2026-09-16 Trae 主动审查修正] 原检查只 grep 4 个文件名, 16 frozen 中 12+ 不在检查内(假阴性敞口);
# 现为全 16 frozen 路径模式。注: skill_d 若出现在 git status 属 user 12:01 拍板 1A 合法改动
# (期望值已沿 FROZEN POLICY reconcile 至 3e369a1f6171), 需在 commit 前确认其为该拍板改动本身。
FROZEN_PAT='verifier/handoff/KT_ABC1_anchors_sha256_12.json|docs/V3X/KT_A1_SPEC_V0.1.md|docs/V3X/KT_B1_SPEC_V0.1.md|docs/V3X/KT_C1_SPEC_V0.1.md|docs/V3X/KT_D0_SPEC_V0.1.md|docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md|results/deposon_v19_benchmark_fixes.json|results/deposon_v21_gtformal.json|corpus/v20/index.json|verifier/handoff/P_F_PREDECISION_2026_09_09.json|docs/V3X/P_F_SPEC_V0.md|docs/V3X/P_F_RESEARCH_2026_09_09.md|plugins/skill_a_p_a_60cells.py|plugins/skill_b_p_c_alpha_beta.py|plugins/skill_c_p_e_3modality.py|plugins/skill_d_p_f_observer.py'
if git status --short | grep -E "${FROZEN_PAT}"; then
    echo "[ERROR] 检测到 frozen 文件改动, 不允许上传"
    echo "       严守 7 铁律: 不动 18 frozen"
    exit 1
fi

# ============================================================
# [2026-09-16 Trae 主动审查新增] Step 3.5: .gitignore 防护
# git add . 在无 .gitignore 时会全仓提交(.mavis/logs/backups 等私人目录有公开泄露风险)
# ============================================================
if [ ! -f .gitignore ]; then
    echo "[ERROR] repo 根缺 .gitignore: 'git add .' 会把 .mavis/(logs/backups/pdfbuild) 等全部提交"
    echo "        请先按 github_dir_structure_2026_09_18.md §1 建立 .gitignore(排除 .mavis/ .tmp/ 等)后重跑"
    exit 1
fi

# ============================================================
# 4. git add + commit
# ============================================================
echo "[Step 4] git add + commit"
git add .
git commit -F "${COMMIT_MSG_FILE}"

# ============================================================
# 5. git push(沿 user 拍板推送方式)
# ============================================================
echo "[Step 5] git push(等 user 拍板推送)"
echo "  选项 A: git push origin ${GITHUB_BRANCH}    (HTTPS + token)"
echo "  选项 B: git push origin ${GITHUB_BRANCH}    (SSH)"
echo "  选项 C: git push -u origin ${GITHUB_BRANCH}  (首次推送)"
echo ""
echo "  TODO: user 在 D7 (2026-09-18) 终极判死后手动执行 git push"

# ============================================================
# 6. github release tag(可选, 沿 user 拍板)
# ============================================================
echo "[Step 6] github release tag(可选)"
echo "  选项 A: gh release create ${RELEASE_TAG} --title 'V3X 1 Week Kill Report (2026-09-18)' --notes-file docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md"
echo "  选项 B: 不打 tag, 只 push main 分支"
echo ""
echo "  TODO: user 在 D7 (2026-09-18) 终极判死后手动执行"

# ============================================================
# 7. 后置验证(推送后)
# ============================================================
echo "[Step 7] 后置验证(推送后)"
echo "  沿 github web UI 验证:"
echo "  - README.md 首页可见"
echo "  - V3X_1WEEK_KILL_REPORT_2026_09_18.md 1 页摘要可见"
echo "  - 5 锚 JSON 文件 SHA-12 = 03c6c01f3697"
echo "  - 4 plugin spec 文件 SHA-12 = b1463bb24403 / e5a299f69a22 / e19e76c5da7e / 3e369a1f6171"

echo ""
echo "===== 上传脚本执行完成 ====="
echo "严守 7 铁律 + 18 frozen 0 触动"
echo "D7 (2026-09-18) 终极判死后 user 手动执行 git push + github release tag"