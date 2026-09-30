import json
p = r"D:/私人资料/deposon-repo/results/_v3_recheck_08c_preexp_data/result_2026_09_27.json"
d = json.load(open(p, encoding="utf-8"))
def walk(o, path=""):
    if isinstance(o, dict):
        for k,v in o.items():
            walk(v, path+"/"+str(k))
    elif isinstance(o, list):
        for i,v in enumerate(o):
            walk(v, path+"/%d"%i)
print("TOP KEYS:", list(d.keys()))
