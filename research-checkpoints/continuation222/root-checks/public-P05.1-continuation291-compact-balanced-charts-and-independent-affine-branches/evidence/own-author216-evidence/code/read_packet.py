import json, pathlib, sys
i=int(sys.argv[1]); start=int(sys.argv[2]); end=int(sys.argv[3])
b=json.loads(pathlib.Path("inputs/mathematical-packet-bindings.json").read_text())
p=pathlib.Path(b[i]["path"]);s=p.read_text();end=min(end,len(s))
print(f"BODY {i} {p.name} characters [{start},{end}) of {len(s)}")
print(s[start:end])
with pathlib.Path("logs/read-spans.jsonl").open("a") as f:f.write(json.dumps({"index":i,"start":start,"end":end,"length":len(s)})+"\n")
