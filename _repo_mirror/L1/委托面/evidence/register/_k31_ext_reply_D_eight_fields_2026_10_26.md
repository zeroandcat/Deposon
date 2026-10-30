# 外委回件 · D（第三批·事 3 八字段逐项定义 ／ 缺值惯例 ／ 三套近似定义）

> 📌 **来源**：外委会话 `mvs_cd51c4b0cb2a49379acb0e71e629feea`（模型 `k3.1-pro`）· 其自报任务号 `DEPOSON-EXT-20261026-03` 之第三事（`turn_6b76bd85` 所催之续交）
> 📌 **取得**：2026-10-26 23:0x 由主代理（mavis）经**跨会话消息**收到（该会话主动送达），本部原样照录，未删改一词；**仅前置本头**
> 📌 **性质**：外委回件——⛔0 视为五终判之词、⛔0 视为 PI 之采认；其末自书「以上仅作文献接地；不判断本项目任何位之词，不代为采认，最终权属仍归 PI」，本部**承此界**
> 📌 **本部尚未核**：其所述各节号／页码／零命中射程与正控，**本部未独立复核**；凡引须并书此限

---

## ① 八字段逐项定义

**结论：无统一（C；仅限下述检索射程）**。截至 2026-10-26 22:55:04（+08:00），所核测量、临床数据模型、SI 与溯源规范中，未见把委托所列八项规定为通用“最小可用八字段集”的权威定义。下表是将权威概念**映射**到这八个内部字段；**每行总级均为 C**，`C←A/B` 只表示支撑材料等级，不表示该八字段组合已成标准。

| 字段 | 可用定义（C 级映射） | 单位与精度 | 缺失时能否填名义量／如何留白 | 级别与出处锚 |
|---|---|---|---|---|
| `cell_id` | 可唯一回指记录对象的标识，供其余字段归属与联查。 | 无物理单位；完整字符串／URI。唯一性、非空是校验，不是测量精度。 | **不可代填**，也不得以行序冒充身份；缺失按②具名。 | C←A：FHIR R5 *Observation* §10.1.7，`identifier` 逐字为 "The unique id for a particular observation"。 |
| `budget_quantity_definition` | 描述所计之量及预期用途；必要时连同测量程序与条件。量纲不能代替此定义。 | 无物理单位；定义文本不适用小数位。测量精密度另按 VIM §2.15。 | **不可填名义量或名义属性**；定义缺则记 `unknown`。 | C←A：VIM §2.1 Note 3，PDF p.32／印刷 p.16："Measurement presupposes a description of the quantity commensurate with the intended use …"；§1.7 Note 4 另明言同量纲不必然是同类量。 |
| `budget_dimension` | 量对基本量的幂积依赖关系，省略数值因子，记作 `dim Q`。 | 无物理单位；保存符号式及指数，不作数值修约。 | **不得默认填 `1`／dimensionless**；只有量定义确属 VIM §1.8 时才可如此标记。 | C←A：VIM §1.7，PDF p.20／印刷 p.4："expression of the dependence of a quantity … omitting any numerical factor"；§1.8，PDF p.22／印刷 p.6。 |
| `budget_unit` | 与同类量比较、使其比值可表为数的约定标量；在数据记录中存机器可处理单位代码。 | 字段自身无单位；代码须逐字符准确。openEHR `units` 为 1..1，默认 UCUM 且区分大小写；数值精度另记。 | **不可猜单位**。在 openEHR `DV_QUANTITY` 中缺 `units` 就不是合格数量实例，须由外层记录缺值，而非伪造单位。 | C←A：VIM §1.9，PDF p.22／印刷 p.6："real scalar quantity, defined and adopted by convention …"；openEHR §6.2.8。 |
| `unit_evidence` | 记录单位代码所属体系、URI／版本与来源；显示名不能替代代码。 | 无物理单位；URI、版本、代码均逐字符保存。 | **仅有一个规范明示的缺省例外**：openEHR `units_system` 可不设，未设即假定 UCUM；非默认体系仍须 URI。此缺省不得外推成"缺证据可随便补"。 | C←A：openEHR §6.2.8："If not set, the UCUM standard (case-sensitive codes) is assumed …"；单位语法见 §6.3.1。 |
| `conversion_reference` | 记录换算两端、因子、出处版次／表式及精确或修约状态。 | 无物理单位；引用须到版次与表／式，因子有效数字照源，不二次修约。 | 未发生换算可记 `not-applicable`；已换算而缺出处应记 `unknown`／`error`（依实因），**不得填 1 或名义因子**。 | C←A+B：A＝NIST SP 330 §4 Table 8，PDF p.41／印刷 p.25；B＝SP 811 登记件 §4-1-2 L125–127（"A factor in boldface is exact. All other factors have been rounded …"）及 §4-3 L207–235。 |
| `B_t_role` | 标明该值在记录中的语义角色；可参照实测、标称量、测量区间之区分，但角色码表须声明为本地码表。 | 无物理单位；受控代码，不适用小数精度。 | **不得默认 `NOMINAL`，更不得拿标称量补实测缺**；角色缺则记 `unknown`。 | C←A：VIM §2.1；§4.6，PDF p.54／印刷 p.38："rounded or approximate value … of a measuring instrument or measuring system"；§4.7，PDF p.55／印刷 p.39。§4.6 的标称量定义有特定仪器／系统语境，不是通用补缺许可。 |
| `provenance` | 记录产生数据的实体、活动、代理人及派生／责任关系，使来源与加工可回溯。 | 无物理单位；标识、时间、关系与版本锚须准确，不属测量精度。 | 无通用默认来源；**不可伪造或拼补**。PROV 本身不给缺值码，须由外层记录显式记缺。 | C←A：W3C *PROV-DM* Abstract："Provenance is information about entities, activities, and people involved in producing a piece of data or thing …"。 |

出处全名与定位：**VIM**＝JCGM 200:2012（DOI `10.59161/JCGM200-2012`）｜**openEHR**＝*Data Types Information Model* RM 1.1.0 §6.2.8／§6.1.2.2／§6.3.1／App A.2.5｜**FHIR R5**＝*Observation* §10.1.4／§10.1.5.9／§10.1.7、*Quantity* §2.1.28.0.6、*DataAbsentReason*｜**NIST SP 330**＝2019 Edition（DOI `10.6028/NIST.SP.330-2019`）｜**PROV**＝W3C Rec *PROV-DM*｜**SP 811（仅 B 级转引）**＝在册取回登记件 `_nist_sp811_fulltext_retrieval_2026_10_25.md`（28,684／`5447ecd37faf`）节号＋行号如上；**该件为取回登记件，原件未落盘（内存抽取、零落盘）**——见其 §1-3 L39、§2-1 R5 L57；本次未重取 SP 811，故不得升为 A。

## ② 缺值惯例与三套近似定义

**缺值惯例：无跨模型统一记号，但有可援的明确规则。**

1. **FHIR（A）**：`obs-6` 逐字规定 "dataAbsentReason SHALL only be present if Observation.value[x] is not present" ⇒ 不是拿 `0`、空串或名义量补值，而是**值缺席＋原因在场**。15 码中 `unknown`＝应有值但未知，`temp-unknown`＝以后可能得知，`not-applicable`＝该元素无适当值，`not-performed`＝未实施观察程序，`error`＝系统／流程错误；`not-a-number` 只用于浮点处理导致未定义／不可表示。**15 码中无 `UNOBTAINED` 字面**，不得冒充标准码。
2. **openEHR（A）**：`magnitude` 与 `units` 皆 1..1；App A.2.5 对未完全知悉之数据采「不创建该类型实例＋在包含类创建 null marker」，而非伪造内部属性。⚠ `precision=0` 表整数、`precision=-1` 表不限小数位；`accuracy=0` 却表 100% 准确（未知准确度在 `DV_AMOUNT` 用 `accuracy=-1`）。**故 `0`／`-1` 皆非跨字段通用缺值码。**
3. **本表之建议（C·不冒充行业标准）**：字段值缺席／null，另记 `absent_reason`（可采用上述 FHIR 码）与必要之 `absent_detail`／来源；⛔0 空串、零填、均值／默认／名义量、静默弃格。缺值标记只说明「为何缺」，**不会使必填字段变成已满足**。

**最接近之三套定义（皆非通行八字段集）**

| 近似模型 | 文献实际给出之结构 | 与委托八项之关键差异 |
|---|---|---|
| **openEHR `DV_QUANTITY`** | `magnitude` 1..1／`precision` 0..1／`units` 1..1／`units_system` 0..1／`units_display_name` 0..1 | 最近「数值＋单位＋小数位＋单位体系」；无 `cell_id`／量定义／量纲／换算出处／角色／溯源；其 `precision` 是**小数位数**，非 VIM 之测量精密度 |
| **FHIR R5 Observation＋Quantity＋DataAbsentReason** | Observation 载 `identifier`／`code`／`value[x]`／`status`／`dataAbsentReason`；Quantity 含 `value`／`comparator`／`unit`／`system`／`code`，并规单位 `code` 在场则 `system` 亦须在场 | 最近「观测身份＋结果＋单位＋显式缺值原因＋流程状态」；非固定八项，无统一 `conversion_reference`／`B_t_role` |
| **VIM＋SP 330（SP 811 仅 B 级补证）** | VIM 给量描述／量纲／单位／测量精密度／标称量／测量区间；SP 330 给单位与换算 | 最近「量→同类量／量纲→单位→值之角色→换算」之语义链；不规定字段数、必填基数、缺值码或溯源结构 |

**零命中与反命中射程（结论仍为 C·不得外推为全文献不存在）**
- 时间窗：**2026-10-26 22:10:26–22:55:04（+08:00）**。全文范围：VIM 108 页、SP 330 138 页；openEHR RM 1.1.0 Data Types、FHIR R5 Observation、FHIR R5 DataAbsentReason、W3C PROV-DM 之官方完整 HTML。
- 六文本共同检索：`eight-field`／`eight fields`／`8 fields`／`minimum eight`／`minimal eight` **皆 0**；两 PDF 另检四字段名皆 0；四 HTML 另检六字段名皆 0。`provenance` 为通用词，**未**拿它作区别性零命中证据。
- 正控同文本可检：VIM `measurement unit` 48｜SP 330 `quantity` 114｜openEHR `magnitude` 79｜FHIR Observation `dataAbsentReason` 46｜ValueSet `not-applicable` 1｜W3C `Provenance` 170 ⇒ **非伪零命中**。
- 网页补检两式仍 0；**有反命中**：CSP 商业博客 *Minimal data model for traceability: 8 fields that really matter*（自述 "not because standards require it"／"The minimum data model is not what standards require."，字段亦不同）⇒ 只作「并非全网无八字段说法」之边界证据（B），**不用于支持通行定义**。
- 访问失败不计入已核全文：QUDT 404、UCUM 与 BIPM SI Brochure 直链超时、FHIR 一 CodeSystem 404（改以实际打开之 ValueSet 全文为据）。失败**不用于**证明文献不存在。

以上仅作文献接地；不判断本项目任何位之词，不代为采认，最终权属仍归 PI。
