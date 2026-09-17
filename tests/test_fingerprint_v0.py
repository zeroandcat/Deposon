# -*- coding: utf-8 -*-
# -*- mode: python; py-indent-offset: 4 -*-
# ============================================================
# V0 指纹算法测试 (5 个测试, 对应 R1-R5)
#
# 隔离策略: 所有测试用 pytest tmp_path fixture 写临时文件,
# 不在原 repo 落任何文件, 不动 verifier/runs/ (除 test_r4 显式
# monkeypatch 模块内部 _runs_dir 指向 tmp, 这是 spec §5 兼容
# /tmp 副本的关键路径)。
# ============================================================
import importlib
import json
import os
import sys
from pathlib import Path

import pytest

# 把仓库根加入 path, 支持 `import fingerprint_v0`
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import fingerprint_v0 as fp  # noqa: E402


# ----------------------------------------------------------------
# 工具: 在 tmp_path 下造 5 个假锚
# ----------------------------------------------------------------
def _make_anchors(tmp_path: Path, n: int = 5):
    paths = []
    for i in range(n):
        p = tmp_path / f"anchor_{i:02d}.bin"
        p.write_bytes(f"PAYLOAD-{i:02d}-V0".encode("utf-8"))
        paths.append(str(p))
    return paths


# ----------------------------------------------------------------
# R1: 内容寻址
# ----------------------------------------------------------------
def test_r1_content_addr(tmp_path):
    """同字节 -> 同 12hex; 1 字节变 -> 完全不同 12hex。"""
    a = tmp_path / "a.bin"
    b = tmp_path / "b.bin"
    a.write_bytes(b"hello world")
    b.write_bytes(b"hello world")  # 完全相同
    assert fp.compute_root([str(a), str(b)]) is not None  # sanity: 不抛

    # 直接通过模块私有 _content_addr 验证 R1 单文件性质
    h1 = fp._content_addr(str(a))
    h1_b = fp._content_addr(str(b))
    assert h1 == h1_b
    assert len(h1) == 12
    assert all(c in "0123456789abcdef" for c in h1)

    # 改 1 字节
    b.write_bytes(b"hello worlD")  # D 变 d
    h1b = fp._content_addr(str(b))
    assert h1 != h1b, "1 字节变化必须导致 12hex 全变"


# ----------------------------------------------------------------
# R2: manifest 排序不变量
# ----------------------------------------------------------------
def test_r2_manifest_sort(tmp_path):
    """5 锚任意乱序输入 -> manifest 字节流完全相同 (ASCII 升序)。"""
    anchors = _make_anchors(tmp_path, 5)

    # 用模块私有 _manifest 直测序列化字节
    m_ordered = fp._manifest(anchors)  # 已经是按 path 升序
    m_reversed = fp._manifest(list(reversed(anchors)))
    m_shuffled1 = fp._manifest([anchors[2], anchors[4], anchors[0], anchors[3], anchors[1]])
    m_shuffled2 = fp._manifest([anchors[4], anchors[1], anchors[3], anchors[0], anchors[2]])

    assert m_ordered == m_reversed == m_shuffled1 == m_shuffled2, (
        "5 锚任意乱序必须产出同一规范 manifest 字节流"
    )

    # 解析校验: 5 元素, 按 path 升序
    parsed = json.loads(m_ordered)
    assert len(parsed) == 5
    paths_in_manifest = [r["path"] for r in parsed]
    assert paths_in_manifest == sorted(anchors), "manifest 内 path 字段必须 ASCII 升序"
    assert all(len(r["hash"]) == 12 for r in parsed)


# ----------------------------------------------------------------
# R3: 根指纹
# ----------------------------------------------------------------
def test_r3_root(tmp_path):
    """root 输出 12 位小写 hex; 改 manifest 任意 1 字符 -> root 变。"""
    anchors = _make_anchors(tmp_path, 5)
    m = fp._manifest(anchors)
    root = fp._root(m)

    assert len(root) == 12
    assert all(c in "0123456789abcdef" for c in root)
    assert root == fp._root(m), "同 manifest 必产同 root"

    # 改 manifest 任意 1 字符 (改一个 hash 的末位)
    parsed = json.loads(m)
    h = parsed[0]["hash"]
    parsed[0]["hash"] = h[:-1] + ("0" if h[-1] != "0" else "1")
    m_tampered = json.dumps(parsed, ensure_ascii=False, separators=(",", ":"))
    assert fp._root(m_tampered) != root, "manifest 任意 1 字符变化必须改 root"

    # 验证 compute_root 与 _root 一致 (R1+R2+R3 合并)
    assert fp.compute_root(anchors) == root


# ----------------------------------------------------------------
# R4: 追加式 runs/ 链
# ----------------------------------------------------------------
def test_r4_chain_append_only(tmp_path, monkeypatch):
    """append_run 输出符合结构; 连续 3 次 append, read_runs_count 增 3。

    隔离: monkeypatch fp._runs_dir 指向 tmp_path/runs,
    不污染真实 verifier/runs。
    """
    fake_runs = tmp_path / "runs"
    fake_runs.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(fp, "_runs_dir", lambda: fake_runs)
    # 关键: 同时改 today_chain 内部依赖 -> 直接 setattr 模块里的函数
    # 因为 _today_chain_path 用了 _runs_dir, setattr 后会自动跟随
    # 但要重 import 模块使 _today_chain_path 走新 _runs_dir。
    # 简单做法: 直接替换 _today_chain_path
    import datetime as _dt
    monkeypatch.setattr(
        fp,
        "_today_chain_path",
        lambda: fake_runs / f"{_dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%d')}_pd_v0.jsonl",
    )

    before = fp.read_runs_count()
    rec1 = fp.append_run(fp.GENESIS_PREV_HASH, "a" * 12)
    rec2 = fp.append_run(rec1["current_root"], "b" * 12)
    rec3 = fp.append_run(rec2["current_root"], "c" * 12)
    after = fp.read_runs_count()

    # 结构校验
    for rec in (rec1, rec2, rec3):
        assert set(rec.keys()) == {"ts", "prev_hash", "current_root"}
        assert len(rec["prev_hash"]) == 12
        assert len(rec["current_root"]) == 12
        # ts 是 ISO8601 字符串, 至少包含 "T" 分隔符
        assert "T" in rec["ts"]

    # 链增长
    assert after - before == 3, f"连续 3 次 append 应增 3, 实际 {after - before}"

    # 链头校验
    assert rec1["prev_hash"] == "0" * 12
    # 链式校验
    assert rec2["prev_hash"] == rec1["current_root"]
    assert rec3["prev_hash"] == rec2["current_root"]


# ----------------------------------------------------------------
# R5: 验证器最小安全边界
# ----------------------------------------------------------------
def test_r5_verifier_interface():
    """模块 dir() 不暴露:
       - 自定义 read_file / listdir / read_bytes 等侧信道 API
       - 锚点路径字符串 (5 个冻结工件的相对路径)
    """
    exposed = dir(fp)
    exposed_str = "\n".join(exposed)

    # 模块自定义 API 中不应出现 read_file / read_bytes / listdir 等
    # (注: Python 内建 open / read 是 builtins, 不算模块导出)
    forbidden_custom = ["read_file", "read_anchor", "read_bytes",
                        "list_anchors", "read_artifact", "open_anchor"]
    leaked = [name for name in forbidden_custom if name in exposed]
    assert not leaked, f"R5 违例: 模块导出了 {leaked}"

    # 锚点路径字符串不应在 dir() / __all__ 中 (避免侧信道)
    # 取模块 __dict__ 的所有字符串值, 找是否泄漏 spec §1 路径片段
    forbidden_path_fragments = [
        "GT_FORMALIZATION_v1.md",
        "run_v21_gtformal.py",
        "run_v22_p1c.py",
        "SPEC_GT2B.md",
        "SPEC_GT8C.md",
    ]
    leaked_fragments = []
    for name in exposed:
        val = getattr(fp, name, None)
        if isinstance(val, str):
            for frag in forbidden_path_fragments:
                if frag in val:
                    leaked_fragments.append((name, frag))
    assert not leaked_fragments, f"R5 违例: 锚点路径片段泄漏: {leaked_fragments}"

    # 公开 API 必须是 5 个 (spec §5 + V0.1 verify_chain)
    assert set(fp.__all__) == {
        "compute_root",
        "verify_root",
        "append_run",
        "read_runs_count",
        "verify_chain",
        "P_B_INTERFACE_RESERVED",
    }

    # 调用方可正常调用
    assert callable(fp.compute_root)
    assert callable(fp.verify_root)
    assert callable(fp.append_run)
    assert callable(fp.read_runs_count)


# ----------------------------------------------------------------
# 附加: compute_root 缺失文件行为 (A1 输入侧, 不计入 R1-R5, 但与 spec §4 对齐)
# ----------------------------------------------------------------
def test_compute_root_missing_file_raises(tmp_path):
    """compute_root 收到不存在路径应抛 FileNotFoundError (spec §4 A1)。"""
    anchors = _make_anchors(tmp_path, 5)
    anchors[2] = str(tmp_path / "does_not_exist_999.bin")
    with pytest.raises(FileNotFoundError):
        fp.compute_root(anchors)


# ----------------------------------------------------------------
# V0.1: verify_chain  校验链完整性 (补 spec §4 A3 缺口)
# ----------------------------------------------------------------
def test_verify_chain_clean(tmp_path, monkeypatch):
    """正常 3 步链: verify_chain 应 valid=True, 0 breaks, 0 genesis violations."""
    fake_runs = tmp_path / "runs"
    fake_runs.mkdir(parents=True, exist_ok=True)
    chain_path = fake_runs / "2099-01-01_pd_v0.jsonl"
    import datetime as _dt
    # 关键: 同时 patch _today_chain_path (append 写哪) 与 _runs_dir (verify_chain 扫哪)
    monkeypatch.setattr(fp, "_today_chain_path", lambda: chain_path)
    monkeypatch.setattr(fp, "_runs_dir", lambda: fake_runs)

    fp.append_run(fp.GENESIS_PREV_HASH, "a" * 12)
    fp.append_run("a" * 12, "b" * 12)
    fp.append_run("b" * 12, "c" * 12)

    report = fp.verify_chain()
    assert report["valid"] is True
    assert report["total_records"] == 3
    assert report["breaks"] == []
    assert report["genesis_violations"] == []


def test_verify_chain_detects_tamper(tmp_path, monkeypatch):
    """篡改 record 0 的 current_root 后, verify_chain 应检出 break."""
    fake_runs = tmp_path / "runs"
    fake_runs.mkdir(parents=True, exist_ok=True)
    chain_path = fake_runs / "2099-01-01_pd_v0.jsonl"
    monkeypatch.setattr(fp, "_today_chain_path", lambda: chain_path)
    monkeypatch.setattr(fp, "_runs_dir", lambda: fake_runs)

    fp.append_run(fp.GENESIS_PREV_HASH, "a" * 12)
    fp.append_run("a" * 12, "b" * 12)

    # 攻击: 改 record 0 current_root
    raw = chain_path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    rec0 = lines[0]
    # 改 "current_root":"aaaa..." -> "current_root":"9999..."
    rec0_tampered = rec0.replace('"current_root":"aaaaaaaaaaaa"',
                                '"current_root":"999999999999"')
    chain_path.write_text(rec0_tampered + "\n" + "\n".join(lines[1:]),
                          encoding="utf-8")

    report = fp.verify_chain()
    assert report["valid"] is False
    # 期望: record 1 的 prev_hash ("aaa...") 与 record 0 重写的 current_root ("999...") 不匹配
    assert len(report["breaks"]) == 1
    brk = report["breaks"][0]
    assert brk["record_index"] == 1
    assert brk["expected_prev_hash"] == "999999999999"  # 篡改后的 record 0 current_root
    assert brk["got_prev_hash"] == "aaaaaaaaaaaa"      # record 1 的 prev_hash
    assert brk["error_code"].startswith("E_CHAIN_BREAK_AT_")


def test_verify_chain_detects_genesis_violation(tmp_path, monkeypatch):
    """非 genesis 的 prev_hash 在 record 0 上: 应被 genesis_violations 捕获."""
    fake_runs = tmp_path / "runs"
    fake_runs.mkdir(parents=True, exist_ok=True)
    chain_path = fake_runs / "2099-01-01_pd_v0.jsonl"
    monkeypatch.setattr(fp, "_today_chain_path", lambda: chain_path)
    monkeypatch.setattr(fp, "_runs_dir", lambda: fake_runs)

    # 故意用非 genesis prev_hash 写第 1 条
    fp.append_run("abcabcabcabc", "a" * 12)

    report = fp.verify_chain()
    assert report["valid"] is False
    assert len(report["genesis_violations"]) == 1
    assert "prev_hash='abcabcabcabc'" in report["genesis_violations"][0]


# ----------------------------------------------------------------
# V0.1.1 (TDD): 边角 + 安全
# ----------------------------------------------------------------
def test_compute_root_empty_list(tmp_path):
    """空路径列表: compute_root 应返回可重现的 12hex (sha256('[]')[:12]).

    文档化: 不抛错, 适用于"无锚"快照场景.
    """
    import hashlib
    expected = hashlib.sha256(b"[]").hexdigest()[:12]
    assert fp.compute_root([]) == expected


def test_compute_root_duplicate_paths(tmp_path):
    """重复路径: 文档化行为 — manifest 含 2 条, hash 不同于单条.

    注意: 重复 = 输入层冗余, 不会去重 (V0 spec 未要求).
    """
    paths = _make_anchors(tmp_path, 1)  # 只有 1 锚
    single = fp.compute_root(paths)
    duplicate = fp.compute_root(paths + paths)  # 同一路径出现 2 次
    assert single != duplicate
    # 重复时, manifest 应有 2 条
    m = fp._manifest(paths + paths)
    import json as _json
    rows = _json.loads(m)
    assert len(rows) == 2
    assert rows[0]["path"] == rows[1]["path"]


def test_content_addr_refuses_symlink(tmp_path):
    """安全: 软链不应被静默跟随 (防攻击者替换锚为指向恶意文件的软链).

    行为: 遇到软链应抛 OSError (含 E_SYMLINK 错误码字样, 类似 E_FILE_MISSING 风格).
    """
    if not hasattr(tmp_path, "symlink_to"):  # Windows 某些 fs 不支持
        import pytest
        pytest.skip("filesystem does not support symlinks")

    real = tmp_path / "real.bin"
    real.write_bytes(b"real content")
    link = tmp_path / "link.bin"
    try:
        link.symlink_to(real)
    except (OSError, NotImplementedError) as e:
        import pytest
        pytest.skip(f"cannot create symlink: {e!s}")

    with pytest.raises(OSError) as exc_info:
        fp._content_addr(str(link))
    assert "E_SYMLINK" in str(exc_info.value) or "symlink" in str(exc_info.value).lower()
