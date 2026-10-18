# -*- coding: utf-8 -*-
"""EXP-06 · 10-09 版 runner 同式修正 ＋ 键名勘正 · 静态构建器（工具件 · 0 属证据面）。

⛔0 运行任何 runner（本件只做文本层静态变换 ＋ difflib 登记 ＋ AST 级校验）。
⛔0 回改任何既有件：原件 7c095c54fb99 只读；新件另立新名。
"""
import difflib
import hashlib
from pathlib import Path

BASE = Path(r"D:\私人资料\deposon-repo")
PLUG = BASE / "deposon_team" / "plugins"
SRC = PLUG / "_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py"

OUT_FIX = PLUG / "_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py"
OUT_REN = PLUG / "_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py"

KEY_OLD = "self_verified_only"
KEY_NEW = "verification_basis_self_rewalk_only"


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def stats(p: Path) -> dict:
    b = p.read_bytes()
    t = b.decode("utf-8")
    return {
        "sha12": sha12(p), "bytes": len(b), "lines": t.count("\n"),
        "bom": b[:3] == b"\xef\xbb\xbf", "crlf": t.count("\r\n"), "lf_only": t.count("\n") - t.count("\r\n"),
    }


def L(*xs: str) -> list:
    return [x for x in xs]


def header(mode: str, gen: str) -> list:
    if mode == "fix":
        return L(
            "# ============================================================================",
            "# 【EXP-06 · 10-09 版 runner self_verified_only 硬写修正版副本】· 新名件 · 原件 0 触动 · 2026-10-10",
            "# ----------------------------------------------------------------------------",
            "# 授权锚：PI 2026-10-10 11:06「轮 36」卡（ask_90373daee410768058a3e852 step runner_two）",
            "#         裁「两者都办（含键名改）」—— 之「① 10-09 版同式修正」一支",
            "# 前棒锚：PI 2026-10-10 10:39「轮 34」卡（ask_2901c721b5788ebbb00670a5 step exp06_finds）",
            "#         裁「授权 runner 修正」＋ 同步注记件 _exp06_selfverified_runner_fix_note_2026_10_10.md",
            "#         §7 残留登记第 1 项（10-09 版 L248 同形硬写 · 登记待裁）",
            "# 勘误源：results/_exp06_supplement_four_gaps_2026_10_10.md · SHA-12 9f86cc5be8e9",
            "#         §2.3.3（规格与实现之张力）＋ §3 勘误登记 E-EXP06-S3",
            "# 规格源：results/_criterion_application_scope_prereg_2026_10_01.md · SHA-12 c4e3338619c6",
            "#         §3.3②「全 true 字段须附独立验证件（可核、0 与被验证件同源）；⛔0 预置为 true」",
            "# 体例底本：_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py · SHA-12 041525fd05a2",
            "#           （09-29 版之同式修正副本）—— 本件沿其四件套形式逐项复刻",
            "# 原件  ：deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py",
            "#         SHA-12 7c095c54fb99 · 21,826 B · 474 行（本棒跑前＝跑后复测一致 ⇒ 0 回改）",
            "# 本件  ：原件之全量副本；**唯一语义改动 ＝ 原 L248 之 self_verified_only 硬写**",
            "# 同步件：results/_exp06_selfverified_renaming_note_2026_10_10.md（本棒出，见该件）",
            "# ----------------------------------------------------------------------------",
            "# 【缺陷实体】原件 L246-L248 之第二行: c[\"chain\"][\"self_verified_only\"] = True",
            "#            —— 无条件字面量, 0 依赖 rewalk_ok, 0 任何比较, 0 任何探测",
            "#            ⇒ 该位之 true 值非由任何验证面求出 ⇒ 与 §3.3② 之「0 预置为 true」相悖",
            "#            （读数不变: 22/22 仍为 true; 独立性在实现级未满足）",
            "#            与 09-29 版 L230-L232 逐字同构（两版该循环体完全一致）",
            "#",
            "# 【修正形式 · 沿 09-29 版修正副本之四件套, 单一改动面】:",
            "#   (1) 求值  : 值 ＝ bool(rewalk_ok) and not independent_verification_verified",
            "#               —— 由自证复走之真实结果 ＋ 独立验证面之真实探测共同决定, ⛔0 预置",
            "#   (2) 标注  : per_caption[].chain.self_verified_only_basis ＋ 顶层 independence_verification 节",
            "#               —— 载 §3.3① 三要素（置位者/置位时机/依据件）＋ 计算式 ＋ 取值（§3.3① 之落面要求）",
            "#   (3) 探测  : probe_independent_evidence() 于运行期实测独立验证面",
            "#               （在位/哈希相符/异源 ⇒ 方计 verified; 「0 与被验证件同源」之异源判据）",
            "#   (4) 警报  : independence_deficiency_alarm（burden 未满足即亮起, ⛔0 静默）",
            "#               —— 沿 §3.3④「0 记为通过、0 静默」之同族纪律",
            "#",
            "# 【键名 · 本件 0 改】PI 轮 36 卡同裁「含键名改」, 但该一支由同棒之键名勘正副本",
            "#   （_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py）承担。",
            "#   本件**保留规格件 c4e3338619c6 §5 逐字段分类表所锁之键名 self_verified_only**",
            "#   （该表「随本件生效即锁」, L173 明载 chain.self_verified_only 之配套位）,",
            "#   理由: 使本件与 09-29 版修正副本（041525fd05a2）schema 完全一致 ⇒ 读数面可比;",
            "#   且规格面之改名后果 ⛔0 由棒方自行承担（归 PI / protocol-keeper, 见同步件残留登记）。",
            "#",
            "# 【身份改写 · 与语义改动严格分离登记】详见同步件 §2",
            "#   DATE / GENERATOR / task_id / 两组输出路径常量(P_OUT_INDEX_V3,P_OUT_RESULTS,",
            "#   REL_INDEX_V3,REL_RESULTS) / docstring 件名与 out件名 —— 0 语义影响",
            "#   （必要性: 输出路径若不改写, 本副本一跑即覆写 10-09 版两产出 ⇒ 违反 0 回改）",
            "#   落位同目录（deposon_team/plugins/）之因: 原件 L40 BASE = Path(__file__).resolve().parents[2]",
            "#   同深度落位 ⇒ BASE 解析 0 改动",
            "#   本版较 09-29 版多出之 PROTOCOL_VERSION / PROTOCOL_VERSION_AXIS 两常量与",
            "#   index_v3 协议版本键面 —— **一字未动, 0 回退**（10-09 版既有能力全部保留）",
            "#",
            "# 【本棒纪律】⛔0 回改原件 1 byte ｜ ⛔0 重跑任何实验载荷（本件 0 运行, 未生成任何产出）",
            "#            ｜ ⛔0 网络 ｜ ⛔0 skill ｜ ⛔0 LLM ｜ 0 读 key ｜ ⛔0 改任何既有产出件",
            "#   验证止于 parse / AST 级 ＋ 静态 grep（0 硬写残留）＋ difflib 改动区登记",
            "# 标记 EXP06_SELFVERIFY_FIXCOPY_1009BASE_2026_10_10（与原件 0 并存标记）",
            "# ============================================================================",
        )
    return L(
        "# ============================================================================",
        "# 【EXP-06 · 10-09 版 runner 键名勘正副本（硬写修正 ＋ 键名改）】· 新名件 · 原件 0 触动 · 2026-10-10",
        "# ----------------------------------------------------------------------------",
        "# 授权锚：PI 2026-10-10 11:06「轮 36」卡（ask_90373daee410768058a3e852 step runner_two）",
        "#         裁「两者都办（含键名改）」—— 之「② 键名改」一支",
        "# 拟案件：results/_exp06_selfverified_renaming_note_2026_10_10.md（本棒出 · 拟案 ＋ 论证 ＋ 影响面 ＋ 迁移）",
        "# 规格源：results/_criterion_application_scope_prereg_2026_10_01.md · SHA-12 c4e3338619c6",
        "#         §3.3②「全 true 须附独立验证件」＋ §5 逐字段分类表 L173（**随本件生效即锁**）",
        "# 修侧基线：_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py",
        "#           （本棒同出之 ① 同式修正副本）—— 本件 ＝ ① ＋ 键名勘正 之另立副本",
        "# 原件  ：deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py",
        "#         SHA-12 7c095c54fb99 · 21,826 B · 474 行（跑前＝跑后复测一致 ⇒ 0 回改）",
        "# 本件  ：原件之全量副本；**语义改动 ＝ 原 L248 硬写之求值化 ＋ 键名 self_verified_only 勘正**",
        "# ----------------------------------------------------------------------------",
        "# 【键名改之实体与理由】",
        "#   旧键名 self_verified_only 之语义为「验证仅由自证支撑」; 而 §3.3② 要求",
        "#   「全 true 字段须附独立验证件」⇒ 若该位读 true, 按键名自身定义即**无独立验证件可附**",
        "#   ⇒ 定义层张力: 一个恒为 true 之位按定义即不可能满足其自身所受之配套校验。",
        "#   修正之路: 旧键名把**证据依据面（basis）**与**豁免宣称面（claim）**压在同一个键名里,",
        "#   使该键名既被读作「自证已通过」又须承担「全 true 须附独立件」之负担 ⇒ 0 稳定读法。",
        "#   本件所采新键名（拟案 · 候 PI 核准）:",
        f"#       {KEY_OLD}  ->  {KEY_NEW}",
        "#   语义改为纯**描述位**: 「本记录之验证依据仅为自证复走」, ⛔0 承担「已附独立验证件」之宣称",
        "#   —— 该负担由 independence_burden_satisfied / independence_deficiency_alarm 二位独立承载。",
        "#   **值表达式 0 变动**: bool(rewalk_ok) and not indep_verified（与 ① 逐字同式）。",
        "#   ⛔ **0 双写**: 本件 0 同时输出旧键（⛔0 双键并存致 schema 歧义 ＋ 0 单一事实源）;",
        "#      旧键之读法仅存于既有产出件, 由同步件之迁移注记承载（读旧件仍用旧键）。",
        "#",
        "# 【⛔ 归 PI 之未代裁项】c4e3338619c6 §5 逐字段分类表 L173 已**逐字锁**",
        "#   `chain.self_verified_only` 之名与配套位（「随本件生效即锁」）⇒ 任何改名均与该",
        "#   锁定表产生**形式偏离**。本棒 ⛔0 回改 c4e3338619c6、⛔0 代裁是否发规格附录/勘误件",
        "#   （该面归 PI / protocol-keeper）; 本件以 key_rename_migration 节**显式登记该偏离**,",
        "#   0 以沉默掩盖, 0 以「已改键名」冒充「规格已对齐」。",
        "#",
        "# 【本棒纪律】⛔0 回改原件 1 byte ｜ ⛔0 回改 ① 修正副本 ｜ ⛔0 重跑任何实验载荷",
        "#            （本件 0 运行, 未生成任何产出）｜ ⛔0 网络 ｜ ⛔0 skill ｜ ⛔0 LLM",
        "#            ｜ 0 读 key ｜ ⛔0 改任何既有产出件",
        "#   验证止于 parse / AST 级 ＋ 静态 grep ＋ difflib 改动区登记",
        "# 标记 EXP06_SELFVERIFY_RENAME_1009BASE_2026_10_10（与原件 0 并存标记）",
        "# ============================================================================",
    )


def probe_block() -> list:
    return L(
        "# ---- 独立验证面声明位 (c4e3338619c6 §3.3②「全 true 须附独立验证件」之落面入口) ----",
        "# 本副本 0 声明独立验证件: ⛔0 以本 runner 之自身产出充当「独立验证件」",
        "# (§3.3② 明定「0 与被验证件同源」⇒ 同源产出无效) ⇒ 0 声明 ⇒ status=\"not_declared\"。",
        "# 声明形如: {\"path\": \"results/<独立验证件>.json\", \"sha256\": \"<64 hex>\"}; 声明后须重跑本 runner 方见效果。",
        "INDEP_VERIFY_DECL = None",
        "",
        "",
        "def probe_independent_evidence(base: Path, self_generator: str) -> dict:",
        "    \"\"\"§3.3② 独立验证面之运行期实测 (纯只读文件系统探测; 0 网络 / 0 写 / 0 LLM / 0 读 key)。",
        "",
        "    status ∈ {not_declared, absent, unpinned_hash, sha256_mismatch, same_source, verified}",
        "    仅 \"verified\" (在位 + 哈希相符 + 异源) 之状态计入 independence_burden_satisfied。",
        "    \"\"\"",
        "    probe = {",
        "        \"declared\": INDEP_VERIFY_DECL,",
        "        \"path\": None,",
        "        \"sha256_expected\": None,",
        "        \"sha256_actual\": None,",
        "        \"sha256_match\": None,",
        "        \"artifact_generator\": None,",
        "        \"same_source\": None,",
        "        \"exists\": None,",
        "        \"status\": \"not_declared\",",
        "        \"probe_method\": \"Path.exists() + hashlib.sha256(file bytes) + artifact['generator'] 字段读取\",",
        "        \"same_source_criterion\": \"artifact['generator'] == 本 runner 之 GENERATOR ⇒ 同源 ⇒ 无效\",",
        "        \"spec_ref\": \"results/_criterion_application_scope_prereg_2026_10_01.md §3.3②\",",
        "    }",
        "    if not INDEP_VERIFY_DECL:",
        "        return probe",
        "    rel = INDEP_VERIFY_DECL.get(\"path\")",
        "    p = base / rel",
        "    probe[\"path\"] = rel",
        "    probe[\"sha256_expected\"] = INDEP_VERIFY_DECL.get(\"sha256\")",
        "    if not p.exists():",
        "        probe[\"status\"] = \"absent\"",
        "        return probe",
        "    probe[\"exists\"] = True",
        "    actual = sha256_file(p)",
        "    probe[\"sha256_actual\"] = actual",
        "    if probe[\"sha256_expected\"] is None:",
        "        probe[\"status\"] = \"unpinned_hash\"",
        "        return probe",
        "    probe[\"sha256_match\"] = actual == probe[\"sha256_expected\"]",
        "    if not probe[\"sha256_match\"]:",
        "        probe[\"status\"] = \"sha256_mismatch\"",
        "        return probe",
        "    try:",
        "        gen = load_json(p).get(\"generator\")",
        "    except (OSError, ValueError):",
        "        gen = None",
        "    probe[\"artifact_generator\"] = gen",
        "    probe[\"same_source\"] = gen == self_generator",
        "    probe[\"status\"] = \"same_source\" if probe[\"same_source\"] else \"verified\"",
        "    return probe",
        "",
        "",
    )


def loop_block(key: str, gen: str) -> list:
    vr = f"{key} = (rewalk_ok 为真) 且 (独立验证面未取得 verified 状态)"
    return L(
        "    # ---------- 5b. 独立验证面实测 (步 7 之后, 任何 chain 布尔位置位之前) ----------",
        "    # §3.3① 三要素之声明 (逐字段): 置位者 = 本 runner (本段) ｜ 置位时机 = 22 节点建毕",
        "    # 且自证复走毕之后 ｜ 依据件 = INDEP_VERIFY_DECL 所声明之独立验证件 + 本段探测记录。",
        "    indep = probe_independent_evidence(BASE, GENERATOR)",
        "    indep_verified = indep[\"status\"] == \"verified\"",
        "",
        "    for c in per_caption:",
        "        c[\"chain\"][\"link_verified\"] = rewalk_ok",
        "        # ⛔0 预置: 该位之值由本段实测结果求值, 非无条件字面量 (§3.3②)",
        f"        c[\"chain\"][\"{key}\"] = bool(rewalk_ok) and not indep_verified",
        "        # 取值语义之随件声明 (§3.3①): 值之来源与判定条件逐行可核",
        f"        c[\"chain\"][\"{key}_basis\"] = {{",
        f"            \"declared_by\": \"{gen} (本副本 5b 段)\",",
        "            \"declared_at\": \"22 节点建毕且自证复走毕之后, 任何 chain 布尔位置位之前\",",
        "            \"source_evidence\": \"INDEP_VERIFY_DECL 所声明之独立验证件 + 5b 段运行期探测记录\",",
        f"            \"value_rule\": \"{vr}\",",
        "            \"rewalk_ok\": bool(rewalk_ok),",
        "            \"independent_verification_status\": indep[\"status\"],",
        "            \"independent_verification_verified\": bool(indep_verified),",
        "            \"preset\": False,",
        "            \"prescription_ref\": \"c4e3338619c6 §3.3① 三要素 ＋ §3.3②「0 预置为 true」\",",
        "        }",
        "        # 独立验证件之可核指针 (§3.3② 之「附独立验证件」; 未获验证时显式记 none, 0 静默)",
        "        c[\"chain\"][\"independent_verification_ref\"] = (",
        "            indep[\"path\"] if indep_verified else None",
        "        )",
        "        c[\"chain\"][\"independent_verification_status\"] = indep[\"status\"]",
        "        # ⛔0 记为通过、0 静默: 独立验证面未获 verified 者, 警报位显式亮起 (§3.3④ 同族纪律)",
        "        c[\"chain\"][\"independence_deficiency_alarm\"] = not indep_verified",
    )


def indep_section(key: str) -> list:
    vr = f"{key} = (rewalk_ok 为真) 且 (独立验证面未取得 verified 状态)"
    return L(
        "        \"independence_verification\": {",
        "            \"note\": (",
        f"                \"{key} 之独立验证面全局面 (置位者/时机/依据件/探测记录 逐项可核); \"",
        "                \"0 判档, 0 翻转既往读数\"",
        "            ),",
        f"            \"field\": \"per_caption[].chain.{key}\",",
        "            \"declared_by\": GENERATOR,",
        "            \"declared_at\": \"22 节点建毕且自证复走毕之后, 任何 chain 布尔位置位之前\",",
        "            \"source_evidence\": \"INDEP_VERIFY_DECL 所声明之独立验证件 + 5b 段运行期探测记录\",",
        f"            \"value_rule\": \"{vr}\",",
        f"            \"{key}_value\": bool(rewalk_ok) and not indep_verified,",
        "            \"preset\": False,",
        "            \"independent_verification_declared\": indep[\"declared\"],",
        "            \"independent_verification_probe\": indep,",
        "            \"independence_burden_satisfied\": indep_verified,",
        "            \"independence_deficiency_alarm\": not indep_verified,",
        "            \"deficiency_note\": (",
        "                \"若 burden 未满足 (独立验证面未取得 verified), 则该位读 true 而独立验证件并未在位; \"",
        "                \"此时 ⛔0 静默 —— independence_deficiency_alarm 置 true 之同时 \"",
        "                \"independent_verification_status 记 none 态之实况\"",
        "            ),",
        "            \"prescription_ref\": \"c4e3338619c6 §3.3① 三要素 ＋ §3.3②「0 预置为 true」\",",
        "        },",
    )


def migration_section(gen: str) -> list:
    return L(
        "        \"key_rename_migration\": {",
        "            \"note\": (",
        "                \"键名勘正之迁移注记 (PI 轮 36 卡裁「含键名改」); 拟案 ＋ 影响面 ＋ 迁移路径 \"",
        "                \"见 results/_exp06_selfverified_renaming_note_2026_10_10.md\"",
        "            ),",
        f"            \"old_key\": \"{KEY_OLD}\",",
        f"            \"new_key\": \"{KEY_NEW}\",",
        "            \"old_key_semantics\": \"「验证仅由自证支撑」—— 依键名自身定义, 该位读 true 即无独立验证件可附\",",
        "            \"new_key_semantics\": \"「本记录之验证依据仅为自证复走」—— 纯描述位, 0 承担「已附独立验证件」之宣称\",",
        "            \"value_expression_unchanged\": True,",
        "            \"value_expression\": \"bool(rewalk_ok) and not indep_verified\",",
        "            \"dual_write\": False,",
        "            \"dual_write_policy\": \"⛔0 双写旧键: 双键并存致 schema 歧义 ＋ 0 单一事实源\",",
        "            \"reading_old_artifacts\": (",
        "                \"既有产出件 (09-29 版 33ad1c01f745 ＋ 10-09 版 95f3f0957be8) 之该位**仍为旧键名** ⛔0 回改; \"",
        "                \"读旧件须用 old_key, 读本副本新产出用 new_key\"",
        "            ),",
        "            \"spec_divergence\": {",
        "                \"locked_spec\": \"results/_criterion_application_scope_prereg_2026_10_01.md §5 逐字段分类表 L173\",",
        "                \"locked_field_name\": \"chain.self_verified_only\",",
        "                \"lock_clause\": \"「随本件生效即锁 · 事实源 ＝ 24418fa60ede §3.2/§3.3」\",",
        "                \"divergence\": \"本键名改与该锁定表逐字所载之字段名不一致 ⇒ 形式偏离\",",
        "                \"action_taken_here\": \"⛔0 回改该规格件; ⛔0 代裁是否发附录/勘误件 (归 PI / protocol-keeper); 本节显式登记该偏离\",",
        "            },",
        "            \"renamed_by\": GENERATOR,",
        "            \"authority\": \"PI 2026-10-10 11:06「轮 36」卡 (ask_90373daee410768058a3e852 step runner_two) 裁「两者都办（含键名改）」\",",
        "        },",
    )


def build(mode: str, dst: Path, extra_pins: list) -> dict:
    is_ren = (mode == "rename")
    key = KEY_NEW if is_ren else KEY_OLD
    gen = dst.relative_to(BASE).as_posix()
    out_idx = f"corpus/v20/index_v3_selfverify_{'rename' if is_ren else 'fix'}_1009base_2026_10_10.json"
    out_res = f"results/deposon_p_d_b3_merkle_22_caption_selfverify_{'rename' if is_ren else 'fix'}_1009base_2026_10_10.json"
    task_id = ("V3X-C5B-RUNNER-2026-10-10-A1-FIXCOPY-1009" if not is_ren
               else "V3X-C5B-RUNNER-2026-10-10-A1-RENAME-1009")
    copy_tag = "self_verified_only 去 hard-write; 0 touch on the original of 2026-10-09" if not is_ren else \
        "self_verified_only 去 hard-write + 键名勘正; 0 touch on the original of 2026-10-09"

    src_lines = SRC.read_bytes().decode("utf-8").split("\n")
    if src_lines and src_lines[-1] == "":
        src_lines.pop()

    # (kind, 1-based orig line, span, replacement lines)  —— 自下而上施加, 免索引失效
    ops = []
    if not is_ren:
        ops.append(("after", 409, 0, L(
            "        \"runner_fix_notice\": (",
            f"            \"本产出由 10-09 版修正版副本 {dst.name} 生成; \"",
            "            \"原件 _p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py 之 L248 self_verified_only 硬写 \"",
            "            \"已在本副本改为运行期实测求值 (c4e3338619c6 §3.3②「0 预置为 true」); \"",
            "            \"⛔0 回改原件 1 byte; 既往产出 95f3f0957be8 ＋ 33ad1c01f745 之读数 0 变动\"",
            "        ),",
        )))
    else:
        ops.append(("after", 409, 0, L(
            "        \"runner_fix_notice\": (",
            f"            \"本产出由 10-09 版键名勘正副本 {dst.name} 生成; \"",
            "            \"原件 _p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py 之 L248 self_verified_only 硬写 \"",
            "            \"已在本副本改为运行期实测求值 (c4e3338619c6 §3.3②「0 预置为 true」); \"",
            f"            \"链名另经勘正: {KEY_OLD} -> {KEY_NEW} (PI 轮 36 卡裁「含键名改」); \"",
            "            \"⛔0 回改原件 1 byte; 既往产出 95f3f0957be8 ＋ 33ad1c01f745 之读数与键名 0 变动\"",
            "        ),",
        )))
    ops.append(("after", 388, 0, migration_section(gen) + indep_section(key) if is_ren else indep_section(key)))
    ops.append(("replace", 302, 1, L(f"        \"task_id\": \"{task_id}\",")))
    ops.append(("replace", 246, 3, loop_block(key, gen)))
    ops.append(("after", 148, 0, probe_block()))
    ops.append(("replace", 94, 1, L(f"GENERATOR = \"{gen}\"")))
    ops.append(("replace", 78, 11, L(
        "PINNED = {",
        "    \"corpus/v20/index_v2_2026_09_16.json\": \"efe05ad775de\",",
        "    \"results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json\": \"b5873afb9d29\",",
        "    \"corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py\": \"d2cd7acb29a1\",",
        "    # V3-02 乙档追加 pin 面 (0 覆写既有产出件 3 件 + 本副本之旧本 2 件)",
        "    \"results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json\": \"33ad1c01f745\",",
        "    \"corpus/v20/index_v3_2026_09_29.json\": \"3ba2449cf986\",",
        "    \"results/c5_b_group_fix_readings_2026_10_01.json\": \"2a7749da7c4d\",",
        "    \"deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py\": \"de16bc002198\",",
        "    \".tmp/_v5_c5_b_fix_readings_2026_10_01.py\": \"191efa7fe0b6\",",
    ) + extra_pins + L("}")))
    ops.append(("replace", 72, 4, L(
        "# ---- outputs (NEW names; 身份改写: 0 覆写 10-09 版两产出) ----",
        f"P_OUT_INDEX_V3 = BASE / \"{out_idx}\"",
        f"P_OUT_RESULTS = BASE / \"{out_res}\"",
        f"REL_INDEX_V3 = \"{out_idx}\"",
        f"REL_RESULTS = \"{out_res}\"",
    )))
    ops.append(("replace", 49, 1, L("DATE = \"2026-10-10\"              # 身份改写: 修正版副本落盘日 (原件 2026-10-09)")))
    ops.append(("replace", 6, 3, L(
        "out件 (new names, 0 overwrite the 2026-09-16 / 2026-09-29 / 2026-10-09 assets):",
        f"  1. {out_idx}",
        f"  2. {out_res}",
    )))
    ops.append(("replace", 5, 1, L(task_id)))
    ops.append(("replace", 3, 1, L(
        "P-D B3 Merkle 22 caption dual chain re-walk runner -- V0.4 coordinate space (new name)",
        f"CORRECTED COPY ({copy_tag})",
    )))
    ops.append(("after", 1, 0, header(mode, gen)))

    out = list(src_lines)
    expect = {
        3: "P-D B3 Merkle 22 caption dual chain re-walk runner",
        5: "V3X-C5B-RUNNER-2026-09-29-A1",
        6: "out件 (new names, 0 overwrite the 2026-09-16 assets):",
        49: 'DATE = "2026-10-09"',
        72: "P_OUT_INDEX_V3",
        78: "PINNED = {",
        94: 'GENERATOR = "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py"',
        246: "for c in per_caption:",
        302: '"task_id": "V3X-C5B-RUNNER-2026-10-09-A1"',
    }
    for kind, no, span, repl in sorted(ops, key=lambda o: -o[1]):
        if kind == "replace":
            i = no - 1
            assert i + span <= len(src_lines), f"L{no} 跨 {span} 行越界"
            got = src_lines[i]
            if no in expect:
                assert expect[no] in got, f"锚定失败 L{no}: {got!r}"
            out[i:i + span] = repl
        else:
            out[no:no] = repl   # after L{no} ⇒ 0-based 插入点 = no

    text = "\n".join(out) + "\n"
    dst.write_bytes(text.encode("utf-8"))
    return dict(path=dst, stats=stats(dst))


def diff_regions(src_lines, dst_lines) -> list:
    sm = difflib.SequenceMatcher(None, src_lines, dst_lines, autojunk=False)
    rows = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        rows.append((tag, f"L{i1+1}" if i1 != i2 else f"L{i1+1}", i2 - i1,
                     f"L{j1+1}" if j1 != j2 else f"L{j1+1}", j2 - j1))
    return rows


if __name__ == "__main__":
    assert sha12(SRC) == "7c095c54fb99", sha12(SRC)
    for p in (OUT_FIX, OUT_REN):
        assert not p.exists(), f"落前 0 命中失败: {p}"

    src_lines = SRC.read_bytes().decode("utf-8").split("\n")
    if src_lines and src_lines[-1] == "":
        src_lines.pop()

    # ---- ① 10-09 版同式修正副本 ----
    r1 = build("fix", OUT_FIX, L(
        "    # 本棒追加 pin 面 (0 覆写 10-09 版两产出 ＋ 其原件; 该 3 件皆在盘、哈希跑前已核)",
        "    \"results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json\": \"95f3f0957be8\",",
        "    \"corpus/v20/index_v3_2026_10_09.json\": \"74b27393574f\",",
        "    \"deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py\": \"7c095c54fb99\",",
    ))
    d1 = diff_regions(src_lines, OUT_FIX.read_bytes().decode("utf-8").split("\n")[:-1])
    print("== ① 同式修正副本 ==")
    print(r1["stats"])
    print("改动区数:", len(d1))
    for t, a, an, b, bn in d1:
        print(f"  {t:8s} {a:>9s} ({an:>3d})  ->  {b:>9s} ({bn:>3d})")

    # ---- ② 键名勘正副本 ----
    r2 = build("rename", OUT_REN, L(
        "    # 本棒追加 pin 面 (0 覆写 10-09 版两产出 ＋ 其原件 ＋ ① 修正副本; 该 4 件皆在盘、哈希跑前已核)",
        "    \"results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json\": \"95f3f0957be8\",",
        "    \"corpus/v20/index_v3_2026_10_09.json\": \"74b27393574f\",",
        "    \"deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py\": \"7c095c54fb99\",",
        f"    \"{OUT_FIX.relative_to(BASE).as_posix()}\": \"{r1['stats']['sha12']}\",",
        "    # ⛔ ① 之两产出路径无法 pin (0 声明 · 本棒 0 运行 ⇒ 该 2 件不在盘);",
        "    #   本副本已将其输出路径另立新名 ⇒ 结构上 0 可能覆写之",
    ))
    d2 = diff_regions(src_lines, OUT_REN.read_bytes().decode("utf-8").split("\n")[:-1])
    print("== ② 键名勘正副本 ==")
    print(r2["stats"])
    print("改动区数:", len(d2))
    for t, a, an, b, bn in d2:
        print(f"  {t:8s} {a:>9s} ({an:>3d})  ->  {b:>9s} ({bn:>3d})")

    # ---- 跑后原件复测（0 回改） ----
    print("原件复测:", stats(SRC))
