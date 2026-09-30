# -*- coding: utf-8 -*-
"""R1 修复件响亮告警行为验证 (只读既有件; 只新建 .tmp scratch 件)."""
import importlib.util
import io
import contextlib
import pathlib

spec = importlib.util.spec_from_file_location(
    "t15r2r1", "results/_v4_supp_t15r2_executor_r1_2026_09_28.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
print("import OK (no side effects); cells =", m.CELLS)

sc = pathlib.Path(".tmp/_r1_scratch_corrupt_a.json")
sc.write_text('[{"cell_idx":0,', encoding="utf-8")           # 截断 / 半写
sb = pathlib.Path(".tmp/_r1_scratch_bom.json")
sb.write_bytes(b'\xef\xbb\xbf[{"ok": true}]')               # UTF-8 BOM (R-4 同族)

warn_log = pathlib.Path(".tmp/_t15r2_checkpoint_warn.jsonl")
if warn_log.exists():
    warn_log.unlink()

err = io.StringIO()
with contextlib.redirect_stderr(err):
    m.T15_RECORDS_PATH = sc
    m.T15R2_CHECKPOINT_PATH = sb
    ra = m.load_t15_records()
    rb = m.load_t15r2_records()
e = err.getvalue()

print("--- return values (contract: must be []) ---")
print("load_t15_records ->", ra, "| load_t15r2_records ->", rb)
print("--- alarms fired:", e.count("!" * 72) // 2)
print("--- says 'unreadable not unrun':", "已跑数据不可读" in e)
print("--- warns N_min=10 basis lost:", "K-N11-N1_T1relax" in e)
print("--- warns T1.5 anchor lost:", "T1.5 状态锚" in e)
print("--- stderr first alarm (verbatim) ---")
print(e[: e.find("!!", 2)])
print("--- warn log lines:",
      len(warn_log.read_text(encoding="utf-8").strip().splitlines())
      if warn_log.exists() else "MISSING")
print("--- warn log does not raise even on unwritable path ---")
m.CHECKPOINT_WARN_LOG_PATH = pathlib.Path("Z:/definitely/not/writable/warn.jsonl")
with contextlib.redirect_stderr(io.StringIO()):
    out = m._checkpoint_alarm("selftest", "unwritable-log-path", sc)
print("returned:", out, "(None = never raised) ✓")

# 正常件仍须零告警 (负向对照: 不得引入新失败面)
good = pathlib.Path(".tmp/_r1_scratch_good.json")
good.write_text('[{"ok": true}]', encoding="utf-8")
err2 = io.StringIO()
with contextlib.redirect_stderr(err2):
    m.T15_RECORDS_PATH = good
    ok = m.load_t15_records()
print("--- negative control: good file ->", ok, "| stderr bytes:", len(err2.getvalue()), "(0 = 无假告警 ✓)")
