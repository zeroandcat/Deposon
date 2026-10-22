#!/bin/bash
# v43: 内嵌交付物（自解包sh + MD内嵌版）还原一致性
O=/mnt/agents/output; fail=0
WANT=6c8979f8571bdc296d668702a518e984
# 1 sh 自解包实测（/tmp 隔离）
T=$(mktemp -d); bash $O/deposon_bundle_selfextract.sh "$T" >/dev/null 2>&1 && [ "$(md5sum $T/deposon_core_bundle_final.zip | cut -d' ' -f1)" = "$WANT" ] || { echo "FAIL sh-restore"; fail=1; }
[ -f $T/HANDOFF_MACHINE_READABLE.json ] && [ -d $T/deposon-repo ] || { echo "FAIL sh-content"; fail=1; }
rm -rf $T
# 2 md 负载解码校验
python3 -c "
import base64,hashlib,re,sys
t=open('$O/deposon_bundle_embedded.md').read()
p=re.search(r'\`\`\`base64\n(.*?)\`\`\`',t,re.S).group(1)
sys.exit(0 if hashlib.md5(base64.b64decode(p)).hexdigest()=='$WANT' else 1)" || { echo "FAIL md-payload"; fail=1; }
# 3 还原指令与红线在场
grep -q "HANDOFF_MACHINE_READABLE.json" $O/deposon_bundle_embedded.md && grep -q "术语红线" $O/deposon_bundle_embedded.md || { echo "FAIL md-instructions"; fail=1; }
# 4 密钥零落盘
! grep -qE "sk-kimi-[0-9A-Za-z]{20,}|ark-[0-9a-f-]{20,}" $O/deposon_bundle_selfextract.sh $O/deposon_bundle_embedded.md || { echo "FAIL keys"; fail=1; }
[ $fail -eq 0 ] && echo "PASS v43" || echo "FAIL v43"
exit $fail
