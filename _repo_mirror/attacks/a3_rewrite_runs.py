# -*- coding: utf-8 -*-
# ============================================================
# A3 追加日志回溯攻击 (V0 spec §4, §6; V0.1 改用 impl.verify_chain)
#
# 动作: 1 条初始 runs (genesis prev_hash, root1) ->
#       append 第 2 条 (prev=root1, root2) ->
#       篡改第 1 条 current_root=root1 -> root1_tampered ->
#       重新读链 -> 调 fingerprint_v0.verify_chain() 校验
# 预期: impl.verify_chain() 返回 valid=False + 1 break + E_CHAIN_BREAK_AT_ -> PASS
# 隔离: monkeypatch fp._today_chain_path / _runs_dir 指向 tempfile.mkdtemp() 子目录
# ============================================================
from __future__ import annotations

import argparse
import json
import sys
import tempfile
import traceback
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import fingerprint_v0 as fp  # noqa: E402


def _emit(verdict: str, diff: str):
    print(json.dumps({"attack": "A3", "verdict": verdict, "diff": diff},
                     ensure_ascii=False, separators=(",", ":")))


def run_internal():
    with tempfile.TemporaryDirectory(prefix="deposon_a3_") as td:
        tdp = Path(td)
        # 临时链: monkeypatch _today_chain_path 到 fake_runs/
        fake_runs = tdp / "runs"
        fake_runs.mkdir(parents=True, exist_ok=True)
        chain_path = fake_runs / "2099-01-01_pd_v0.jsonl"
        original_today_chain = fp._today_chain_path
        fp._today_chain_path = lambda: chain_path
        try:
            # 初始: 第 1 条 (链头)
            rec1 = fp.append_run(fp.GENESIS_PREV_HASH, "a" * 12)
            # 第 2 条: prev_hash = 第 1 条 current_root
            rec2 = fp.append_run(rec1["current_root"], "b" * 12)
        finally:
            fp._today_chain_path = original_today_chain

        # 篡改: 把第 1 条 current_root 改成不同的 12hex
        tampered_root_1 = "0" * 11 + "9"  # 与 "a" * 12 不同
        raw = chain_path.read_text(encoding="utf-8")
        lines = raw.splitlines()
        rec0_tampered = lines[0].replace(
            '"current_root":"aaaaaaaaaaaa"',
            f'"current_root":"{tampered_root_1}"',
        )
        chain_path.write_text(
            rec0_tampered + "\n" + "\n".join(lines[1:]),
            encoding="utf-8",
        )

        # V0.1: 用 impl.verify_chain() 校验, 不再自写
        # 需 monkeypatch _runs_dir 到 fake_runs
        original_runs_dir = fp._runs_dir
        fp._runs_dir = lambda: fake_runs
        try:
            report = fp.verify_chain()
        finally:
            fp._runs_dir = original_runs_dir

        if report["valid"]:
            return "FAIL", (
                f"rewrite of record 0 current_root -> {tampered_root_1!r} "
                f"was NOT detected by impl.verify_chain(); "
                f"report={report}"
            )

        # 期望: 1 break (record 1 prev_hash='aaa...' != record 0 重写 current_root='999...')
        breaks = report["breaks"]
        if not breaks:
            return "FAIL", (
                f"impl.verify_chain() returned valid=False but breaks=[]; "
                f"genesis_violations={report['genesis_violations']}"
            )
        brk = breaks[0]
        return "PASS", (
            f"chain break detected at {brk['file']}:{brk['record_index']} "
            f"by impl.verify_chain(): "
            f"prev_hash={brk['got_prev_hash']!r} != "
            f"prev current_root={brk['expected_prev_hash']!r}; "
            f"error_code={brk['error_code']!r}; "
            f"attacker rewrote record 0 current_root to {tampered_root_1!r}"
        )


def main():
    parser = argparse.ArgumentParser(description="A3 追加日志回溯攻击")
    parser.add_argument("--chain", help="(可选) 真实链 jsonl 路径, 演练模式忽略")
    parser.add_argument("--at", type=int, help="(可选) 篡改第 k 条, 演练模式忽略")
    args = parser.parse_args()

    try:
        verdict, diff = run_internal()
    except Exception:
        verdict, diff = "FAIL", f"unexpected crash: {traceback.format_exc()}"
    _emit(verdict, diff)
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
