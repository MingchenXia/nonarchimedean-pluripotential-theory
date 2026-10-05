from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
functions=[(F(y,2),s) for y in (-1,-2,-4,-6,-8,-12,-16) for s in product((F(1),F(2)),repeat=3)]
def value(f,r):
 y,s=f;t=-r; total=y
 for speed in s:
  z=min(t,F(1)); total+=speed*z;t-=z
  if t<=0:return total
 return total+s[-1]*t
def root(f):
 y,s=f;need=-y;t=F(0)
 for speed in s:
  if need<=speed:return -(t+need/speed)
  need-=speed;t+=1
 return -(t+need/s[-1])
clip_cases=tail_cases=0; max_slack=F(0)
for f,g in product(functions,repeat=2):
 r1=root(f);r2=root(g)
 for M,N in product((F(1),F(3)),(1,3,6)):
  h=M/N;grid=[-M+j*h for j in range(N+1)]
  bound=max(abs(value(f,r)-value(g,r)) for r in grid)+4*h
  actual=abs(max(r1,-M)-max(r2,-M))
  assert actual<=bound,(f,g,M,N,actual,bound)
  clip_cases+=1;max_slack=max(max_slack,bound-actual)
for f in functions:
 a=min(f[1]);r=root(f); y=f[0]
 for M in (F(0),F(1,2),F(1),F(2),F(4),F(8)):
  assert max(-r-M,F(0))<=max(-y-a*M,F(0))/a
  tail_cases+=1
# Exact sup on the two torified normalized rays. Both functions have the
# same positive degree pair in each call, so their difference is constant
# beyond their final branch crossing.
def sup_difference(lam,nu,deg):
 ans=[]
 for moving in (0,1):
  fixed=1-moving
  c1=lam[moving]-deg[moving]*lam[fixed]/deg[fixed]
  c2=nu[moving]-deg[moving]*nu[fixed]/deg[fixed]
  points={F(0),max(c1,F(0)),max(c2,F(0)),max(c1,c2,F(0))+1}
  for t in points:
   vals=[F(0),F(0)];vals[moving]=t
   u=max((lam[j]-vals[j])/deg[j] for j in (0,1))
   v=max((nu[j]-vals[j])/deg[j] for j in (0,1))
   ans.append(u-v)
 return max(ans)
sign=lambda q:(q>0)-(q<0)
eta=(F(1),F(1));xi=(F(1),F(2));weights=list(product(map(F,(-2,-1,0,1,2)),repeat=2))
order_cases=0
for lam,nu,t in product(weights,weights,(F(-1),F(-1,2),F(0),F(1,2),F(1))):
 target=sup_difference(lam,nu,xi)-t
 back=tuple(nu[j]+t*xi[j] for j in (0,1))
 source=sup_difference(lam,back,eta)
 assert sign(target)==sign(source),(lam,nu,t,target,source)
 order_cases+=1
report={'status':'all finite cases passed','domains':{'clipped_roots':'56 negative-initial-value three-piece orbit functions, slopes 1 or 2, all ordered pairs, M=1,3 and N=1,3,6; common a=1,b=2','tails':'same 56 functions, M=0,1/2,1,2,4,8; actual minimum slope','order_thresholds':'25 two-generator weight lists in {-2,-1,0,1,2}^2, all pairs, eta=(1,1), xi=(1,2), five thresholds; exact analytic sup on both infinite normalized monomial rays'},'case_counts':{'clipped_root_grid':clip_cases,'root_tails':tail_cases,'strict_order_thresholds':order_cases},'total':clip_cases+tail_cases+order_cases,'limits':'Exhaustive finite rational diagnostics only. Not an analytic proof, geometric compactness check, or universal validation.'}
(ROOT/'finite-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
