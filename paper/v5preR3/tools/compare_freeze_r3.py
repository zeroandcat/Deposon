#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# compare_freeze_r3.py — FREEZE_v5preR3 现态重算与逐位比对（沿 R2 compare_freeze 链·R3 口径）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-26 07:21:08「冻结生成／比对工具沿 R2 链」。
# R2 链保留：sha12/行/字节重算·逐位归因·verdict·退出码 0/1。
# R3 口径：frozen 件任一 content_changed / MISSING / 净增删 ⇒ 「失配·须处置」；
#   external 件变动 ⇒ 「外部输入变动·登记」（不判失配·因只记不冻·但必须报出）；
#   r2_voided 件变动 ⇒ 失配（R2 作废件 0 删是硬边界）。
# 用法：python3 compare_freeze_r3.py [freeze.json] [--quiet]
# ============================================================================
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R3DIR = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(R3DIR, "..", ".."))
DEFAULT = os.path.join(R3DIR, "evidence", "FREEZE_v5preR3.json")


def fp(path):
    h = hashlib.sha256(); n = 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk); n += chunk.count(b"\n")
    return {"sha12": h.hexdigest()[:12], "lines": n, "bytes": os.path.getsize(path)}


def resolve(path):
    return path if os.path.isabs(path) else os.path.join(REPO, path)


def classify(old, new):
    if new is None:
        return "MISSING"
    if old.get("sha12") == new["sha12"] and old.get("bytes") == new["bytes"]:
        return "identical"
    return "content_changed"


def main():
    quiet = "--quiet" in sys.argv
    jpath = None
    for a in sys.argv[1:]:
        if a.endswith(".json"):
            jpath = a
    jpath = jpath or DEFAULT
    doc = json.load(open(jpath, encoding="utf-8"))
    print(f"== compare against {os.path.basename(jpath)} v{doc.get('version')} ({doc.get('freeze')}) ==")
    verdict_ok = True
    ext_changed = []
    for section, strict in (("frozen", True), ("r2_voided", True), ("external_inputs", False)):
        for r in doc.get(section, []):
            p = resolve(r["path"])
            new = fp(p) if (os.path.exists(p) and os.path.isfile(p)) else None
            if r.get("kind") == "external" and os.path.isdir(p):
                # 目录件：按 MANIFEST.sha256（若原冻结按 MANIFEST 记）
                m = os.path.join(p, "MANIFEST.sha256")
                new = fp(m) if os.path.exists(m) else None
            st = classify(r, new)
            line = f"[{st:15s}] {section:14s} {r['label']}  {r.get('sha12','—')} -> {(new or {}).get('sha12','—')}"
            if st == "identical":
                if not quiet:
                    print(line)
            else:
                print(line)
                if strict:
                    verdict_ok = False
                else:
                    ext_changed.append(r["label"])
    # 净增删：现态目录内 frozen 件之外的新文件（仅提示）
    print()
    if verdict_ok and not ext_changed:
        print("verdict: 0 失配（frozen 与 r2_voided 全部 identical；external 全部 identical）")
        sys.exit(0)
    if verdict_ok:
        print("verdict: 0 失配（frozen 与 r2_voided 全部 identical）；外部输入变动·登记：" + "；".join(ext_changed))
        sys.exit(0)
    print("verdict: 失配·须处置（frozen 或 r2_voided 件有 content_changed / MISSING）" + ("；外部输入变动：" + "；".join(ext_changed) if ext_changed else ""))
    sys.exit(1)


if __name__ == "__main__":
    main()
