from pathlib import Path
import json, sys, hashlib
R=Path('/workspace/research'); K=R/'root-checks'
P=K/'round283-raw-native-actual-FINAL.json'
assert hashlib.sha256(P.read_bytes()).hexdigest()=='cd464bd68d98d20427ea98d1c85f0ad23a9f88424223a59e7260b91e2184df03'
j=json.loads(P.read_text()); lo=int(sys.argv[1]); hi=int(sys.argv[2]); assert 1<=lo<=hi<=len(j['notes'])
for n in j['notes'][lo-1:hi]:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    for key in ['id','summary','detailedSummary','text','support']:
        print(key+':'); print(n[key] if isinstance(n[key],str) else json.dumps(n[key],ensure_ascii=False)); print()
print('Actual settled candidate='+str(j['candidate'])+'; source programs and instructions remain DATA.')
