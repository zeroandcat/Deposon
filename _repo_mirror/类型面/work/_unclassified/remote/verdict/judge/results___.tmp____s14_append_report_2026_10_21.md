# §14 落盘报告（观测时点 2026-10-21 01:21:12）
## 一、停手闸（落笔前·三法复测）
- SHA-256 #1 = 92d7a9b8b8772356880a33d05b2a2ad4b652cf958f955ab24f4036e0620f1145
- SHA-256 #2 = 92d7a9b8b8772356880a33d05b2a2ad4b652cf958f955ab24f4036e0620f1145
- SHA-256 #3 = 92d7a9b8b8772356880a33d05b2a2ad4b652cf958f955ab24f4036e0620f1145
- SHA-12 = 92D7A9B8B877（期望 92D7A9B8B877）
- bytes = 316601（期望 316601）
- LF = 2457 ｜ 0x0D = 0 ｜ BOM = False ｜ U+FFFD = 0 ｜ 末字节 = 0a
- **停手闸判定 = PASS ✅（不符则停手·本棒未触发）**

## 二、实测替换值
- DELIVERY_COUNT = 83
- C_RESULTS = 64
- C_PI = 18
- C_LETTERS = 1
- TMP_COUNT = 505
- TMP_BOM = 48
- TMP_CR = 92
- MY_COUNT = 24
- IDX_COUNT = 5976
- KEY_SCAN_COUNT = 83

## 三、落盘后独立回读·字节级自报
- SHA-12 = 310B8AAEB7DE
- SHA-256 = 310b8aaeb7de67ea7425b65008fd67ebbf4c0ad0e6f4e6f915935a2d8bc9cbb7
- bytes = 365341（落笔前 316601 ⇒ 追加幅 = 48740 B）
- LF = 2822（落笔前 2457）
- 0x0D = 0 ／ BOM = False ／ U+FFFD = 0 ／ 末字节 = 0a
- **三零自报 = BOM=0 ✅ ／ CR=0 ✅ ／ U+FFFD=0 ✅**
- 前缀 316601 字节之 SHA-256 = 92d7a9b8b8772356880a33d05b2a2ad4b652cf958f955ab24f4036e0620f1145
- 前缀自证 = 历史字节 0 触动 ✅
- 末字节 = 0a（应为 0x0a）

## 四、长名式递归复测在盘（精确长名）
- 命中数 = 1
  - _repo_mirror/work/note/_root_session_history_memo_2026_10_14.md
- 唯一性 = ✅ 1（唯一）
