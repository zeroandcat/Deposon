import sys, hashlib, io

# 1. 读全文并实测基础指标
p = r'_repo_mirror/work/note/_root_session_history_memo_2026_10_14.md'
data = open(p, 'rb').read()
print('===AFTER-STATE===')
print('total_bytes:', len(data))
print('SHA256:', hashlib.sha256(data).hexdigest())
print('SHA12 :', hashlib.sha256(data).hexdigest()[:12].upper())
print('CRLF  :', data.count(b'\r\n'))
print('LF_total:', data.count(b'\n'))
print('CR_count:', data.count(b'\r'))
print('BOM_in_head:', data[:3] == b'\xef\xbb\xbf')
print('tail_byte:', hex(data[-1]))
print('U+FFFD_count:', data.count(b'\xef\xbf\xbd'.decode('utf-8').encode('utf-8')))

# 2. 验证历史 0-187,404 字节（前 187,404 字节）与原基线 SHA-12 `648BD68A2DBC` 之对应
# 原基线 = 187,404 B；现在文件前 187,404 字节应当完全等于历史内容
# 实际不可能 byte-by-byte 比较（已植入新节）——但可以验证 §10-9 末节前的内容完整性
# 通过验证：本文件 187,404 字节位置处的字节应当是历史末字节 0x0A
# —— 但是我们的 §0-锚 + §0A 已经插入到文件头部，所以从字节 187,404 开始的就是「原文件末字节 0x0A 之后的部分」
# 验证方法：截取现在文件中与原 187,404 B 等长的字节区段，应当不含任何「§10-9 末节件止行」之前出现的内容（因为植入只发生在头部）

# 简化验证：读出现文件 1,755 行的全部 LF 边界
lines = data.split(b'\n')
print('===LINE_COUNT_AFTER:', len(lines), '===')
# 检查 §0-锚 / §0A / §11 是否出现
content = data.decode('utf-8')
print('§0-锚_count:', content.count('## §0-锚'))
print('§0A_count:', content.count('## §0A'))
print('§11_count:', content.count('## §11'))
# 检查历史节号仍然完整
for h in ['## §0 摘要（先给判）','## §1','## §2','## §3','## §4','## §5','## §6','## §7','## §8','## §9','## §10','### 10-9 勘误补记']:
    print(f'[{h}]:', h in content)
# 检查原末节件止行存在且未被改
orig_tail = '（件止 · worker 子棒版补录 · 2026-10-19 16:3x · §10 补 ＋ §10-9 勘误 · ⛔ 0 宣告①毕/段毕 · ⛔ 0 闭任何 KD · ⛔ 0 落五终判 · ⛔ 0 回改 §0–§9 一字 · ⛔ 0 强合主代理版 · 候 PI 核准）'
print('原末节件止行存在:', orig_tail in content)
# 检查新末节件止行
new_tail = '（件止 · worker 子棒版补录 §11 · 2026-10-19 19:1x'
print('新末节件止行存在:', new_tail in content)

# 3. 验证历史 §7-3-3 / §7-3-4 之 2833F89D623B / 66,561 B / 601 行 旧指纹值仍存在于原文（未改动）
print('§7-3-3 表旧值仍存在:', '2833F89D623B' in content and '66,561' in content and '601' in content)

sys.stdout.buffer.write(b'\n===DONE===\n')
