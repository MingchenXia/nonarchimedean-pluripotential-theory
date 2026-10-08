import json,sys,hashlib,pathlib,datetime
BASE=pathlib.Path("/workspace/research/campaigns/round-241/P05.2-original-carrier-tree-primitive-polynomial-independent-whole-proof-and-scope-review")
mode=sys.argv[1]
if mode=="math": p=pathlib.Path(json.loads((BASE/"mathematical-packet-bindings.json").read_text())[int(sys.argv[2])]["path"])
elif mode=="original": p=BASE/"original-task.json"
elif mode in ("BMPS","BBGS"): p=pathlib.Path(next(x["path"] for x in json.loads((BASE/"private-primary-packet-bindings.json").read_text()) if x["label"]==mode and x["format"]=="txt"))
else: raise ValueError(mode)
t=p.read_bytes().decode("utf-8")
if mode in ("BMPS","BBGS"):
 lines=t.split("\n"); a,b=map(int,sys.argv[2:4]); out="\n".join(f"{j+1}: {lines[j]}" for j in range(a-1,min(b,len(lines))))
else:
 a,b=map(int,sys.argv[3:5] if mode=="math" else sys.argv[2:4]); out=t[a:b]
print(f"READ {p.name} {a}:{b} chars={len(out)} sha256={hashlib.sha256(p.read_bytes()).hexdigest()}")
print(out)
with open("read-events.jsonl","a") as f: f.write(json.dumps({"path":str(p),"mode":mode,"start":a,"end":b,"output_chars":len(out),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"utc":datetime.datetime.now(datetime.timezone.utc).isoformat()})+"\n")
