# R-J5 段 A' · 1D TFIM 量子迁移矩阵 与 2D 经典各向异性 Ising 行迁移矩阵 的**精确配分函数比对**
# 目的：不靠记忆，数值确定 1D TFIM -> 2D 经典 Ising 映射中 K1/K2 的因子（空间/时间）。
# 判据：Tr T_q^M 是否逐 M 等于 Tr V(K1,K2)^M。
# 4x4 实对称矩阵；指数用 scaling-and-squaring + Taylor；stdlib only。
# =====================================================================================
# ⚠ FAILED / INCONCLUSIVE — 本脚本 **0 用作任何证据**，仅留失败痕迹（诚实交代用）
# -------------------------------------------------------------------------------------
# 缺陷（自查）：本脚本构造量子迁移矩阵时用了 X4 = σx⊗I，**漏掉 I⊗σx 项**
#   （L=2 周期链的横向场应为 bh·(σx⊗I + I⊗σx)）。故本脚本算出的 T_q 不是 L=2 TFIM 的
#   真实迁移矩阵，段 A2 的「逐 M 配分函数比对」结论全部作废。
# 实测：Tr(本脚本 T_q) = 4.3856421，而 L=2 真值应为 4·cosh(bJ)·cosh(2·bh) = 4.7307…
# 另：有限尺寸下 Z_quantum(L) 与 Z_classical(L×M) 本就只在 Trotter 连续极限相等，
#   「逐 M 精确相等」本就不是正确判据 —— 双重不成立。
# 结论：本件 **0 从本脚本得出任何映射因子结论**；R-J5 的因子问题仍为未解决缺口。
# =====================================================================================
import math

N = 4


def zeros(n=N):
    return [[0.0] * n for _ in range(n)]


def eye(n=N):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def kron(A, B):
    na, nb = len(A), len(B)
    return [[A[i // nb][j // nb] * B[i % nb][j % nb] for j in range(na * nb)]
            for i in range(na * nb)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(N)] for i in range(N)]


def scale(A, s):
    return [[A[i][j] * s for j in range(N)] for i in range(N)]


def matmul(A, B):
    C = zeros()
    for i in range(N):
        Ai = A[i]
        for k in range(N):
            a = Ai[k]
            if a == 0.0:
                continue
            Bk, Ck = B[k], C[i]
            for j in range(N):
                Ck[j] += a * Bk[j]
    return C


def matpow(A, m):
    R = eye()
    B = [row[:] for row in A]
    while m:
        if m & 1:
            R = matmul(R, B)
        B = matmul(B, B)
        m >>= 1
    return R


def expm(A):
    """scaling-and-squaring + Taylor（|A| 范数可控的 4x4 情形）"""
    nrm = max(sum(abs(v) for v in row) for row in A)
    s = 0
    if nrm > 0.5:
        s = math.ceil(math.log2(nrm / 0.5))
    A2 = scale(A, 2.0 ** (-s)) if s else [row[:] for row in A]
    R = eye()
    term = eye()
    for k in range(1, 40):
        term = matmul(term, A2)
        term = scale(term, 1.0 / k)
        R = add(R, term)
    for _ in range(s):
        R = matmul(R, R)
    return R


def trace(A):
    return sum(A[i][i] for i in range(N))


def sigma_z():
    return ((1.0, 0.0), (0.0, -1.0))


def sigma_x():
    return ((0.0, 1.0), (1.0, 0.0))


def tfim_transfer(bJ, bh):
    """T_q = exp(bJ * (σz⊗σz) + bh * (σx⊗I))，基底 (↑↑, ↑↓, ↓↑, ↓↓)"""
    Z4 = kron(sigma_z(), sigma_z())
    X4 = kron(sigma_x(), eye(2))
    return expm(add(scale(Z4, bJ), scale(X4, bh)))


def classical_row_transfer(k1, k2, L=2):
    """2D 经典各向异性 Ising（L=2，空间周期）：行间转移矩阵
       V[s,s'] = exp(K1 * Σ_n s_n s_{n+1} + K2 * Σ_n s_n s'_n)"""
    states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    V = zeros()
    for a, s in enumerate(states):
        for b, sp in enumerate(states):
            inrow = sum(s[i] * s[(i + 1) % L] for i in range(L))
            inter = sum(s[i] * sp[i] for i in range(L))
            V[a][b] = math.exp(k1 * inrow + k2 * inter)
    return V


def main():
    print("== 段 A0 · 指数器自检：expm(diag) 对已知值 ==")
    D = zeros()
    for i in range(N):
        D[i][i] = [0.3, -0.7, 1.1, -2.0][i]
    E = expm(D)
    print("  max|expm(D)-diag(e^d)| =",
          max(abs(E[i][j] - (math.exp(D[i][i]) if i == j else 0.0))
              for i in range(N) for j in range(N)))

    bJ, bh = 0.37, 0.23
    Tq = tfim_transfer(bJ, bh)
    print("\n== 段 A1 · 量子迁移矩阵 T_q = exp(bJ σz⊗σz + bh σx⊗I) ==")
    for r in Tq:
        print("  [" + ", ".join("%9.6f" % v for v in r) + "]")
    print("  Tr T_q     =", trace(Tq))

    cands = [("bJ/2, bh/2", bJ / 2, bh / 2), ("bJ/4, bh/4", bJ / 4, bh / 4),
             ("bJ, bh", bJ, bh), ("bJ/2, bh/4", bJ / 2, bh / 4),
             ("bJ/4, bh/2", bJ / 4, bh / 2), ("bJ, bh/2", bJ, bh / 2),
             ("bJ/2, bh", bJ / 2, bh)]
    print("\n== 段 A2 · 逐 M 比对 Tr V(K1,K2)^M  vs  Tr T_q^M ==")
    for label, k1, k2 in cands:
        V = classical_row_transfer(k1, k2)
        errs = []
        for m in (1, 2, 3, 4, 6, 8):
            errs.append(abs(trace(matpow(V, m)) - trace(matpow(Tq, m))))
        print("  K1=%-10s K2=%-10s  maxM<=8 abs diff = %.3e   Tr V^8=%.9f  Tr Tq^8=%.9f"
              % (label, "", max(errs), trace(matpow(V, 8)), trace(matpow(Tq, 8))))

    print("\n== 段 A3 · 谱：T_q 与最佳候选 V 的特征值对比（幂法近似不可靠 => 用解析式核对） ==")
    # 2D 经典 L=2 周期链：解析谱（Kramers-Wannier 的 2x2 分解）
    def v_eigs(k1, k2):
        # 空间方向 2 站点周期：先用横向 2x2 块分解求 V 的特征值（数值：对角化 4x4 用幂迭代）
        vals = []
        V = classical_row_transfer(k1, k2)
        for vec in ([1.0, 0, 0, 0], [0, 1.0, 0, 0]):
            w = [sum(V[i][j] * vec[j] for j in range(N)) for i in range(N)]
            nw = math.sqrt(sum(x * x for x in w)) or 1.0
            lam = sum(vec[i] * w[i] for i in range(N)) / (sum(x * x for x in vec) or 1.0)
            vals.append(lam)
        return vals
    print("  (仅记录，无判定用途)")


if __name__ == "__main__":
    main()
