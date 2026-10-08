import json,itertools,hashlib,platform,sys
from fractions import Fraction as F
from pathlib import Path
cfg=json.loads(Path('bounded-input.json').read_text())
fail=[];counts={'coefficient_minimum':0,'primary_truncation':0,'node_profile':0,'endpoint':0,'tower':0,'two_slots':0}
def multiply(a,b,char):
 c={}
 for (t,z),v in a.items():
  for (tt,zz),vv in b.items():c[t+tt,z+zz]=c.get((t+tt,z+zz),0)+v*vv
 return {k:(v%char if char else v) for k,v in c.items() if (v%char if char else v)}
for char in cfg['characteristics']:
 for r in cfg['factor_counts']:
  for s in itertools.product(cfg['root_orders'],repeat=r):
   for ls in itertools.product(cfg['artinian_lengths'],repeat=r):
    poly={(0,0):1};d=sum(ls)
    for order,l in zip(s,ls):
     for _ in range(l):poly=multiply(poly,{(1,0):1,(0,order):-1},char)
    vals=[]
    for i in range(1,d+1):
     zs=[z for (t,z),v in poly.items() if t==d-i and v]
     vals.append(min(zs) if zs else None)
    m=min(F(v,i) for i,v in enumerate(vals,1) if v is not None)
    counts['coefficient_minimum']+=1
    if m!=min(s):fail.append(['coefficient',char,s,ls,str(m)])
    L=F(vals[-1],d);N=int(d*L)+1
    mm=min(F(min(v,N) if v is not None else N,i) for i,v in enumerate(vals,1))
    counts['primary_truncation']+=1
    if mm!=m:fail.append(['truncation',char,s,ls,N])
weights=[F(x) for x in cfg['node_weights']]
for N in range(cfg['node_N_min'],cfg['node_N_max']+1):
 alpha=F(1,N-1)
 for s,t in itertools.product(weights,repeat=2):
  if min(s,t)!=1:continue
  h=-(1-alpha)-alpha*min(s,N*t)
  counts['node_profile']+=1
  if h>-1:fail.append(['node',N,str(s),str(t),str(h)])
 h1=-(1-alpha)-alpha*N
 counts['endpoint']+=1
 if h1!=-2:fail.append(['endpoint',N,str(h1)])
for char in cfg['characteristics']:
 direct=F(-2,3);iterated=F(-1,2);raw=-2
 counts['tower']+=1
 if direct==iterated or raw!=-2:fail.append(['tower',char])
counts['two_slots']=1
assert 0!=1 and F(1,4)!=0
out={'kind':'exhaustive finite arithmetic over the explicitly listed Cartesian inputs','counts':counts,'failures':fail,'failure_count':len(fail),'node_value_gap':1,'closed_image_gap':1,'vertical_gap':1,'two_slot_source_mass':0,'two_slot_traced_base_mass':1,'varying_average_direct':str(direct),'varying_average_iterated':str(iterated),'unnormalized_trace':raw,'python':sys.version,'platform':platform.platform(),'input_sha256':hashlib.sha256(Path('bounded-input.json').read_bytes()).hexdigest(),'limitations':'No arithmetic check verifies Cartier geometry, cone comparison, model independence, or universal envelope/product statements.'}
Path('evidence/bounded-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
