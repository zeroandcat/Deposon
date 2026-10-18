"""P-6 切换落地：把 r1 哨兵修复面逐块应用回原件（新名件，落 .tmp，可复跑）。

方法：不重写整文件，只把 4 个变更块（difflib opcode 定位）按「原件行 -> r1 行」
逐块替换，其余行逐字节沿用原件内容。写回用 LF、utf-8、无 BOM。
"""
import ast
import difflib
import hashlib
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORIG = os.path.join(ROOT, "mindmap_corpus_v20.py")
R1 = os.path.join(ROOT, "mindmap_corpus_v20_r1.py")

# ── 2026-09-29 追加（protocol-keeper · PI 确认批 5 ⑱③ 授权修正）─────────────────
# 事实：本脚本的**唯一任务已完成**——r1 的 4 个变更块已应用回原件（原件由
#       `7d8d6a30dd8c` / 23,893 B → `e77e7f3455e0` / 25,791 B，修后与 r1 逐字节相同）。
# 随后 r1 本体已由 parent 按**可恢复删除通道**清除（回执 `mavis-trash: moved to trash`）。
# 本脚本硬编该路径为**补丁来源** ⇒ 重跑已无意义。
# **0 静默改指原件**：改指会把「读 r1 源」变成「读原件并与自身比对」＝ 伪造 `patched == r1`。
# 改为**显式失效 ＋ 出处可追**。
# 落册：results/_v5_confirm_b5_decisions_register_2026_09_29.md（⑱③）
# ──────────────────────────────────────────────────────────────────────────────
if not os.path.exists(R1):
    raise SystemExit(
        "[HISTORICAL / 0-RUNNABLE] 本脚本以已删除的修订件为补丁来源：%s\n"
        "  该件已于 2026-09-29 经可恢复删除通道清除（0 永久删除，可自回收站复原）。\n"
        "  且本脚本任务**早已完成**：其 4 个变更块已应用回原件（原件修后 = `e77e7f3455e0` / 25,791 B）。\n"
        "  本脚本**0 改指原件**：那会把「读 r1 源」变成「原件与自身比对」＝ 伪造 `patched == r1`。\n"
        "  落册出处：results/_v5_confirm_b5_decisions_register_2026_09_29.md（⑱③）" % R1
    )


def sha12_bytes(b):
    return hashlib.sha256(b).hexdigest()[:12]


def main():
    orig_b = open(ORIG, "rb").read()
    orig = orig_b.decode("utf-8")
    r1 = open(R1, encoding="utf-8").read()
    assert orig_b.count(b"\r\n") == 0, "原件含 CRLF，停止"

    a = orig.splitlines()
    b = r1.splitlines()
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
    print("change_blocks=%d" % len(ops))
    assert len(ops) == 4, "变更块数与登记件不符，停止"

    out = list(a)
    # 从后往前替换，行号不位移
    for tag, i1, i2, j1, j2 in reversed(ops):
        print("  apply %s orig L%d-%d -> r1 L%d-%d" % (tag, i1 + 1, i2, j1 + 1, j2))
        out[i1:i2] = b[j1:j2]

    new = "\n".join(out) + "\n"
    ast.parse(new)  # 写盘前语法闸
    new_b = new.encode("utf-8")

    # 哨兵面之外必须逐块一致：修后原件 vs r1
    ident = (new == r1)
    print("patched == r1 : %s" % ident)
    print("pre  sha12 %s (%d B)" % (sha12_bytes(orig_b), len(orig_b)))
    print("post sha12 %s (%d B)" % (sha12_bytes(new_b), len(new_b)))

    with open(ORIG, "wb") as f:
        f.write(new_b)
    print("written -> %s" % ORIG)


if __name__ == "__main__":
    main()
