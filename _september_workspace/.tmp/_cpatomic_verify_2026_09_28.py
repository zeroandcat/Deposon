# -*- coding: utf-8 -*-
"""CLEAN-A棒 · 修复验证：checkpoint 原子写（cpath_r1 同款）四项实测。

T1 落盘字节同构   : 原子写 vs 原非原子写 => 逐字节同 (0 改落盘字节, 0 改实验逻辑)
T2 双跑不互毁     : 2 进程并发写同一 checkpoint => 终态 = 某一方的完整 payload, 0 混合 0 截断
T3 崩半路数据不动 : 写入中途 SIGKILL => 既有 checkpoint 逐字节不动
T4 对照组(旧写法) : 同样中途 SIGKILL => 既有 checkpoint **被截断摧毁** (缺陷复现, 证修复非装饰)

被测件 = 新名 _r2_atomic 件; 对照 = 被引 R1 原件 (0 触动, 只 import 不写)。
0 LLM / key 永不明文 / 0 动真实 checkpoint (全部在 .tmp 沙箱内跑)。
"""
import hashlib
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True  # 0 产生 __pycache__

# 控制台 GBK 不可编码 ⇒ stdout 强制 UTF-8 + 替换, 0 因字符编码丢结果
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path("D:/私人资料/deposon-repo")
SCRATCH = ROOT / ".tmp/_cpatomic_scratch"
RESULTS = []


def sha12(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def load(mod_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(mod_name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def payload(tag: str, n: int):
    return [{"ok": True, "tag": tag, "i": i, "payload": f"{tag}-{i}" * 40}
            for i in range(n)]


def check(name, passed, detail=""):
    RESULTS.append({"test": name, "pass": bool(passed), "detail": detail})
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")
    return passed


# ---------------------------------------------------------------- T1
def t1_bytesequivalence():
    print("=== T1 落盘字节同构（原子写 vs 原非原子写）===")
    recs = payload("T1", 500)
    for tag, mod_path, fn, ck in [
        ("t15r2", RESULTS_DIR / "_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py",
         "save_t15r2_records", "T15R2_CHECKPOINT_PATH"),
        ("t15", RESULTS_DIR / "_v4_supp_t15_executor_r2_atomic_2026_09_28.py",
         "save_checkpoint", "CHECKPOINT_PATH"),
    ]:
        m = load(f"cpa_t1_{tag}", mod_path)
        p = SCRATCH / f"t1_{tag}.json"
        setattr(m, ck, p)
        getattr(m, fn)(recs)                      # 原子写
        atomic_bytes = p.read_bytes()
        # 原非原子写 = json.dumps 同参 + write_text utf-8
        legacy = json.dumps(recs, ensure_ascii=False).encode("utf-8")
        check(f"T1/{tag} 原子写落盘字节 == 原非原子写",
              atomic_bytes == legacy,
              f"atomic={sha12(atomic_bytes)}/{len(atomic_bytes)}B "
              f"legacy={sha12(legacy)}/{len(legacy)}B")
        # 0 临时件残留
        leftovers = list(SCRATCH.glob(f"t1_{tag}.json.tmp_*"))
        check(f"T1/{tag} 0 临时件残留", not leftovers, f"leftovers={[x.name for x in leftovers]}")


# ---------------------------------------------------------------- T2
WRITER = r'''
import importlib.util, json, os, sys
sys.dont_write_bytecode = True
mod_path, fn, ck, out, tag, n = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6])
spec = importlib.util.spec_from_file_location("w", mod_path)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
from pathlib import Path
p = Path(out); setattr(m, ck, p)
recs = [{"ok": True, "tag": tag, "i": i, "payload": f"{tag}-{i}" * 40} for i in range(n)]
getattr(m, fn)(recs)
print("done")
'''


def t2_double_run():
    print("=== T2 双跑不互毁（2 进程并发写同一 checkpoint）===")
    writer = SCRATCH / "_writer.py"
    writer.write_text(WRITER, encoding="utf-8")
    N = 4000
    pay = {}
    for tag in ("A", "B"):
        pay[tag] = json.dumps(payload(tag, N), ensure_ascii=False).encode("utf-8")

    for label, mod_path, fn, ck in [
        ("t15r2", RESULTS_DIR / "_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py",
         "save_t15r2_records", "T15R2_CHECKPOINT_PATH"),
        ("t15", RESULTS_DIR / "_v4_supp_t15_executor_r2_atomic_2026_09_28.py",
         "save_checkpoint", "CHECKPOINT_PATH"),
    ]:
        ck_path = SCRATCH / f"t2_{label}.json"
        procs = [subprocess.Popen(
            [sys.executable, "-B", str(writer), str(mod_path), fn, ck,
             str(ck_path), tag, str(N)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for tag in ("A", "B")]
        outs = [(p.wait(), p.communicate()) for p in procs]
        check(f"T2/{label} 双进程 exit=0",
              all(rc == 0 for rc, _ in outs),
              f"rc={[rc for rc, _ in outs]}")
        final = ck_path.read_bytes()
        match = [t for t in ("A", "B") if final == pay[t]]
        check(f"T2/{label} 终态 = 某一方完整 payload（0 混合 0 截断）",
              len(match) == 1,
              f"matched={match} bytes={len(final)}")
        try:
            json.loads(final)
            ok = True
        except Exception as e:
            ok = False
        check(f"T2/{label} 终态可 json.loads（0 截断）", ok)
        left = list(SCRATCH.glob(f"t2_{label}.json.tmp_*"))
        if left:
            info = [(x.name, x.stat().st_size) for x in left]
            # 再等 1s: 收尾窗口 (os.replace 已在进程内完成, 此处仅排除观察竞态)
            time.sleep(1.0)
            left2 = list(SCRATCH.glob(f"t2_{label}.json.tmp_*"))
            check(f"T2/{label} 0 临时件残留", not left2,
                  f"first_seen={info} after_1s={[(x.name, x.stat().st_size) for x in left2]}")
        else:
            check(f"T2/{label} 0 临时件残留", True, "[]")


# ---------------------------------------------------------------- T3 / T4
CRASHER = r'''
import importlib.util, json, os, signal, sys, time
sys.dont_write_bytecode = True
mode, mod_path, fn, ck, out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
spec = importlib.util.spec_from_file_location("c", mod_path)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
from pathlib import Path
p = Path(out); setattr(m, ck, p)
recs = [{"ok": True, "tag": "CRASH", "i": i, "payload": "CRASH-" * 400} for i in range(60000)]
if mode == "legacy":
    # 旧写法等价物: 直接覆盖写目标件
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False))
else:
    getattr(m, fn)(recs)
'''


def _seed(path: Path, tag: str, n: int):
    p = json.dumps(payload(tag, n), ensure_ascii=False).encode("utf-8")
    path.write_bytes(p)
    return p


def _kill_midwrite(ck_path: Path, glob_pat: str, min_bytes: int, timeout=90.0):
    """起进程 → 等临时件/目标件长到 min_bytes → 强杀。返回 (killed, rc, stderr)。"""
    p = subprocess.Popen([sys.executable, "-B", str(SCRATCH / "_crasher.py")] + CRASH_ARGS,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    t0 = time.time()
    killed = False
    while time.time() - t0 < timeout:
        cands = list(SCRATCH.glob(glob_pat))
        if cands and any(c.stat().st_size >= min_bytes for c in cands):
            time.sleep(0.05)
            # Windows 无 SIGKILL; p.kill() = TerminateProcess, 不可捕获, 等价语义
            try:
                p.kill()
            except ProcessLookupError:
                pass
            killed = True
            break
        if p.poll() is not None:
            break
        time.sleep(0.01)
    try:
        _, err = p.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        p.kill()
        _, err = p.communicate()
    return killed, p.returncode, (err or b"").decode("utf-8", "replace")[-300:]


CRASH_ARGS = []


def t3_t4_crash():
    global CRASH_ARGS
    print("=== T3 崩半路数据不动 / T4 对照组(旧写法崩溃摧毁数据) ===")
    crasher = SCRATCH / "_crasher.py"
    crasher.write_text(CRASHER, encoding="utf-8")

    for label, mod_path, fn, ck in [
        ("t15r2", RESULTS_DIR / "_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py",
         "save_t15r2_records", "T15R2_CHECKPOINT_PATH"),
        ("t15", RESULTS_DIR / "_v4_supp_t15_executor_r2_atomic_2026_09_28.py",
         "save_checkpoint", "CHECKPOINT_PATH"),
    ]:
        # ---- T3 原子写: 中途强杀, 既有数据须逐字节不动
        ck_path = SCRATCH / f"t3_{label}.json"
        seed = _seed(ck_path, "P0", 300)
        CRASH_ARGS = ["atomic", str(mod_path), fn, ck, str(ck_path)]
        killed, rc, err = _kill_midwrite(ck_path, f"t3_{label}.json.tmp_*", 8_000_000)
        after = ck_path.read_bytes()
        check(f"T3/{label} 中途强杀确实发生", killed and not err.strip(),
              f"rc={rc} err={err!r}")
        check(f"T3/{label} 既有 checkpoint 逐字节不动",
              after == seed,
              f"seed={sha12(seed)}/{len(seed)}B after={sha12(after)}/{len(after)}B")
        try:
            json.loads(after); ok = True
        except Exception:
            ok = False
        check(f"T3/{label} 既有 checkpoint 仍可解析", ok)
        # ---- T4 对照: 旧写法同样强杀 → 数据应被摧毁 (缺陷复现)
        CRASH_ARGS = ["legacy", str(mod_path), fn, ck, str(ck_path)]
        killed4, rc4, err4 = _kill_midwrite(ck_path, f"t3_{label}.json", 8_000_000)
        after4 = ck_path.read_bytes()
        check(f"T4/{label} 对照组中途强杀确实发生", killed4 and not err4.strip(),
              f"rc={rc4} err={err4!r}")
        try:
            json.loads(after4); ok4 = True
        except Exception as e4:
            ok4 = False
        check(f"T4/{label} 旧写法数据被摧毁（缺陷复现 => 修复非装饰）",
              after4 != seed,
              f"after={sha12(after4)}/{len(after4)}B (seed {len(seed)}B) "
              f"json_loads_ok={ok4}")
        # 复原沙箱
        ck_path.write_bytes(seed)
    CRASH_ARGS = []


def main():
    global RESULTS_DIR
    RESULTS_DIR = ROOT / "results"
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir(parents=True)
    print(f"sandbox = {SCRATCH}\n")
    t1_bytesequivalence()
    t2_double_run()
    t3_t4_crash()
    n_pass = sum(1 for r in RESULTS if r["pass"])
    print(f"\n=== 汇总: {n_pass}/{len(RESULTS)} PASS ===")
    out = ROOT / ".tmp/_cpatomic_verify_2026_09_28.json"
    out.write_text(json.dumps({"schema": "v4_cpatomic_verify/1", "date": "2026-09-28",
                               "n_tests": len(RESULTS), "n_pass": n_pass,
                               "results": RESULTS}, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print(f"OUT -> {out}")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
