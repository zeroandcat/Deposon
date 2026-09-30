import json
import pathlib

d = json.loads(pathlib.Path("D:/私人资料/deposon-repo/.tmp/_cpatomic_pycache_pre_2026_09_28.json")
               .read_text(encoding="utf-8"))
out = []
for x in d["pyc_dirs"]:
    out.append(f"DIR {x['rel']}/  files={x['n_files']}  bytes={x['total_bytes']}  "
               f"gated={x['gated_frozen_adjacent']}")
    for f in x["files"]:
        out.append(f"    {f['name']:56s} {f['bytes']:>9d}  {f['sha12']}")
print("\n".join(out))
