#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
日志保留策略 v1.0 执行脚本（deposon · 2026-10-13）
策略登记件：results/_log_retention_policy_register_2026_10_13.md

面 A  〔本机用户目录〕\AppData\Roaming\MiniMax\logs  （真实实体路径，非 junction）
      软阈 6 GB -> 清理至 4 GB；硬阈 10 GB -> 立即清理至 4 GB
      滚动窗口：保留最近 2 个日历日（含今日）
面 B  〔本机用户目录〕\.minimax\v2\observability\logs
      保留最近 24 小时；上限 1 GB

用法
    python _log_retention_purge_2026_10_13.py             # dry-run（默认，不删任何件）
    python _log_retention_purge_2026_10_13.py --apply     # 执行
    python _log_retention_purge_2026_10_13.py --selftest  # 阈值算例自检（10-10 峰值态回代）

铁律（与策略登记件一致）
    0 截断 / 0 SetLength(0) / 0 Remove-Item / 0 裸 rm
    0 清空回收站
    删除一律经子进程调用 mavis-trash.cmd（字面前斜杠绝对路径）=> 可恢复
    失败即停并如实报，0 回退永久删除
    归档区 〔本地归档区〕  0 读 0 写 0 列目录
"""
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta

GB = 1024 ** 3
MB = 1024 ** 2

# ---- 策略参数（与登记件逐字一致） ----------------------------------------
FACE_A_DIR = r"〔本机用户目录〕\AppData\Roaming\MiniMax\logs"
FACE_B_DIR = r"〔本机用户目录〕\.minimax\v2\observability\logs"
TRASH_LAUNCHER = r"〔本机用户目录〕\.minimax\bin\mavis-trash.cmd"

A_SOFT_GB = 6.0
A_TARGET_GB = 4.0
A_HARD_GB = 10.0
A_KEEP_DAYS = 2

B_KEEP_HOURS = 24
B_CAP_GB = 1.0

LIVE_GRACE_MIN = 5

PROTECTED_PREFIX = ("truncate",)
NEVER_TOUCH = r"_non_upload_local_archive"

DATE_PATTERNS = [
    re.compile(r"-(\d{2})-(\d{2})\.log$"),
    re.compile(r"-(\d{4})-(\d{2})-(\d{2})\.log$"),
]


def file_day(path):
    """返回该日志件所属日期 YYYY-MM-DD；无法解析返回 None。"""
    name = os.path.basename(path)
    for pat in DATE_PATTERNS:
        m = pat.search(name)
        if not m:
            continue
        g = m.groups()
        if len(g) == 2:
            mm, dd = g
            return "%04d-%02d-%02d" % (datetime.now().year, int(mm), int(dd))
        return "%s-%s-%s" % g
    return None


def is_protected(name):
    low = name.lower()
    return any(low.startswith(p) for p in PROTECTED_PREFIX)


def dir_size(files):
    total = 0
    for f in files:
        try:
            total += os.path.getsize(f)
        except OSError:
            pass
    return total


def listdir(path):
    try:
        return [os.path.join(path, n) for n in os.listdir(path)
                if os.path.isfile(os.path.join(path, n))]
    except OSError:
        return []


def mtime(path):
    try:
        return datetime.fromtimestamp(os.path.getmtime(path))
    except OSError:
        return datetime.now()


def trash(paths):
    """经 mavis-trash.cmd 可恢复删除。返回 (成功 list, 失败 list)。

    mavis-trash 拒绝经重定向点（junction）路径回收，故此处先以
    os.path.realpath 解析出真实实体路径（例：〔本机用户目录〕\\.minimax
    -> 〔本机用户目录〕\\.minimax），再以前斜杠字面路径下发。
    """
    ok, bad = [], []
    if not paths:
        return ok, bad
    if not os.path.isfile(TRASH_LAUNCHER):
        return [], [(p, "launcher not found: %s" % TRASH_LAUNCHER) for p in paths]
    for p in paths:
        real = os.path.realpath(p)
        lit = real.replace("\\", "/")
        try:
            r = subprocess.run([TRASH_LAUNCHER, "--", lit],
                               capture_output=True, text=True, timeout=300)
            if r.returncode == 0:
                ok.append(p)
            else:
                bad.append((p, (r.stderr or r.stdout or "").strip()[:200]))
        except Exception as exc:  # noqa: BLE001
            bad.append((p, "EXC:%s" % exc))
    return ok, bad


def plan_face_a(now):
    files = listdir(FACE_A_DIR)
    total = dir_size(files)
    today = now.strftime("%Y-%m-%d")

    dated, undated = [], []
    for f in files:
        name = os.path.basename(f)
        if is_protected(name) or NEVER_TOUCH.lower() in f.lower():
            continue
        d = file_day(f)
        if d is None:
            undated.append(f)
            continue
        if d == today:
            continue
        if (now - mtime(f)) < timedelta(minutes=LIVE_GRACE_MIN):
            continue
        dated.append((d, f))
    dated.sort(key=lambda x: x[0])

    keep_from = (now - timedelta(days=A_KEEP_DAYS - 1)).strftime("%Y-%m-%d")
    beyond = [f for d, f in dated if d < keep_from]
    in_win = [(d, f) for d, f in dated if d >= keep_from]

    trigger = None
    if total >= A_HARD_GB * GB:
        trigger = "HARD"
    elif total >= A_SOFT_GB * GB:
        trigger = "SOFT"

    to_del = list(beyond)
    remaining = total - dir_size(to_del)
    if trigger and remaining > A_TARGET_GB * GB:
        for _d, f in in_win:
            if remaining <= A_TARGET_GB * GB:
                break
            to_del.append(f)
            remaining -= os.path.getsize(f)

    to_del = [f for f in to_del if not is_protected(os.path.basename(f))]
    to_del = [f for f in to_del if file_day(f) not in (None, today)]
    return {"total": total, "trigger": trigger, "keep_from": keep_from,
            "dated": dated, "undated": undated, "to_del": to_del}


def plan_face_b(now):
    files = listdir(FACE_B_DIR)
    total = dir_size(files)
    cutoff = now - timedelta(hours=B_KEEP_HOURS)
    to_del = [f for f in files if mtime(f) < cutoff]
    if total > B_CAP_GB * GB:
        rest = sorted([f for f in files if f not in to_del], key=mtime)
        remain = total - dir_size(to_del)
        for f in rest:
            if remain <= B_CAP_GB * GB:
                break
            to_del.append(f)
            remain -= os.path.getsize(f)
    return {"total": total, "to_del": to_del}


def selftest():
    print("[selftest] face-A threshold scenario, replaying the 10-10 peak state")
    scenario = [("2026-10-08", 999.8), ("2026-10-09", 4941.0), ("2026-10-10", 7067.0),
                ("2026-10-11", 3433.7), ("2026-10-12", 2707.4), ("2026-10-13", 832.0)]
    total = sum(v for _d, v in scenario) * MB
    now = datetime(2026, 10, 13, 9, 30)
    keep_from = (now - timedelta(days=A_KEEP_DAYS - 1)).strftime("%Y-%m-%d")
    trig = "HARD" if total >= A_HARD_GB * GB else (
        "SOFT" if total >= A_SOFT_GB * GB else "NONE")
    print("  total=%.2f GB  trigger=%s  keep_from=%s" % (total / GB, trig, keep_from))
    del_list, remain = [], total
    for d, v in scenario:
        if d < keep_from:
            del_list.append((d, v))
            remain -= v * MB
    for d, v in scenario:
        if d >= keep_from and remain > A_TARGET_GB * GB:
            del_list.append((d, v))
            remain -= v * MB
    print("  delete: %s" % ", ".join("%s(%.0fMB)" % x for x in del_list))
    print("  converged=%.2f GB (target %.1f GB) => %s"
          % (remain / GB, A_TARGET_GB, "PASS" if remain <= A_TARGET_GB * GB else "FAIL"))


def main():
    args = sys.argv[1:]
    do_apply = "--apply" in args
    if "--selftest" in args:
        selftest()
        return 0

    now = datetime.now()
    print("=== log retention policy v1.0 : %s ===" % ("APPLY" if do_apply else "DRY-RUN"))
    print("time: %s" % now.strftime("%Y-%m-%d %H:%M:%S"))

    a = plan_face_a(now)
    print("")
    print("[faceA] %s" % FACE_A_DIR)
    print("  total=%.2f GB  trigger=%s  keep_from=%s"
          % (a["total"] / GB, a["trigger"] or "NONE", a["keep_from"]))
    print("  undated (protected): %d" % len(a["undated"]))
    print("  to_delete=%d files (%.2f GB)" % (len(a["to_del"]), dir_size(a["to_del"]) / GB))
    for f in a["to_del"]:
        print("    - %s (%.1f MB)" % (os.path.basename(f), os.path.getsize(f) / MB))

    b = plan_face_b(now)
    print("")
    print("[faceB] %s" % FACE_B_DIR)
    print("  total=%.2f GB  window=%dh  cap=%.1f GB  to_delete=%d files (%.2f GB)"
          % (b["total"] / GB, B_KEEP_HOURS, B_CAP_GB,
             len(b["to_del"]), dir_size(b["to_del"]) / GB))
    for f in b["to_del"][:10]:
        print("    - %s (%.1f MB)" % (os.path.basename(f), os.path.getsize(f) / MB))
    if len(b["to_del"]) > 10:
        print("    ... and %d more" % (len(b["to_del"]) - 10))

    if not do_apply:
        print("")
        print("[dry-run] nothing deleted. use --apply to execute.")
        return 0

    if not a["to_del"] and not b["to_del"]:
        print("")
        print("[apply] nothing to purge (under thresholds).")
        return 0

    print("")
    print("[apply] running (via mavis-trash, recoverable)...")
    for label, pl in (("faceA", a), ("faceB", b)):
        if not pl["to_del"]:
            continue
        ok, bad = trash(pl["to_del"])
        print("  %s: ok %d / fail %d" % (label, len(ok), len(bad)))
        for p, err in bad[:10]:
            print("    !! FAIL %s :: %s" % (os.path.basename(p), err))
        if bad:
            print("  [STOP] %s had failures => halt (no permanent-delete fallback)" % label)
            return 2

    a2 = plan_face_a(now)
    b2 = plan_face_b(now)
    print("")
    print("[verify] faceA=%.2f GB | faceB=%.2f GB" % (a2["total"] / GB, b2["total"] / GB))
    return 0


if __name__ == "__main__":
    sys.exit(main())