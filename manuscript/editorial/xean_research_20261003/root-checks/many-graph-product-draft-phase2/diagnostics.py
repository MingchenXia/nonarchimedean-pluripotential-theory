"""Small exact full-divisor diagnostics; no mathematical certification.

Every recursive coefficient is evaluated from primitive integral normal lifts
and the tangential term, on the product skeleton, rather than inserted masses.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations
from math import gcd, factorial, prod
import json

def vec(v): return tuple(F(x) for x in v)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(a,c): return tuple(c*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def egcd(a,b):
 if b==0: return (abs(a),1 if a>=0 else -1,0)
 g,x,y=egcd(b,a%b); return g,y,x-(a//b)*y

class Factor:
 def __init__(self,n): self.n=n;self.cells={};self.inc={}
 def value(self,cell,v):
  c=self.cells[cell]
  if c['dim']==0:
   assert all(x==0 for x in v); return F(0)
  if c['dim']==1:
   r=c['ray']; i=next(i for i,x in enumerate(r) if x)
   t=v[i]/r[i]; assert scale(r,t)==v
   return t*c['value']
  a,b=c['basis']; i=next(i for i,x in enumerate(a) if x);j=next(i for i,x in enumerate(b) if x)
  s=v[i]/a[i];t=v[j]/b[j];assert add(scale(a,s),scale(b,t))==v
  return dot(c['slope'],(s,t))

def graph(directions,weights,values):
 z=Factor(len(directions[0]));z.cells['o']={'dim':0,'weight':F(0)}
 for i,(r,w,h) in enumerate(zip(directions,weights,values)):
  assert gcd(*[abs(x) for x in r])==1
  key=f'r{i}';z.cells[key]={'dim':1,'weight':F(w),'ray':vec(r),'value':F(h)}
  z.inc[(key,'o')]=vec(r)
 return z

def pair_factor(inp):
 q=inp['first_directions'];r=inp['second_directions'];la=inp['first_relation'];mu=inp['second_relation']
 a=F(inp['a']);b=F(inp['b']);kappa=F(inp['kappa']);S=la;T=mu
 z=Factor(len(q[0])+len(r[0]));z.cells['o']={'dim':0,'weight':F(0)}
 rays={};axesA=[];axesB=[];c=[1,1,2]
 for i,u in enumerate(q):
  v=vec(u+[0]*len(r[0]));key=f'a{i}';axesA.append(v);rays[key]=v
  z.cells[key]={'dim':1,'weight':F(0),'ray':v,'value':kappa*c[i]/S[i]}
 for j,u in enumerate(r):
  v=vec([0]*len(q[0])+u);key=f'b{j}';axesB.append(v);rays[key]=v
  z.cells[key]={'dim':1,'weight':F(0),'ray':v,'value':kappa*c[j]/T[j]}
 for i,A in enumerate(axesA):
  for j,B in enumerate(axesB):
   qp=F(1,S[i]);rp=F(1,T[j]);omega=a*b*la[i]*mu[j]
   if i==j:
    D=qp.denominator*rp.denominator;Q=int(D*qp);U=int(D*rp);g=gcd(Q,U)
    co=(U//g,Q//g);v=add(scale(A,co[0]),scale(B,co[1]));key=f'k{i}{j}'
    assert gcd(*[abs(int(x)) for x in v])==1
    rays[key]=v;z.cells[key]={'dim':1,'weight':F(0),'ray':v,'value':F(0)}
    cones=[((f'a{i}',(1,0)),(key,co),(kappa*c[i]*qp,-kappa*c[i]*rp)),
           ((key,co),(f'b{j}',(0,1)),(-kappa*c[i]*qp,kappa*c[i]*rp))]
   else:
    cones=[((f'a{i}',(1,0)),(f'b{j}',(0,1)),(kappa*c[i]*qp,kappa*c[j]*rp))]
   for m,(rr,ss,slope) in enumerate(cones):
    ck=f'C{i}{j}{m}';z.cells[ck]={'dim':2,'weight':omega,'basis':(A,B),'slope':slope}
    for (rk,rc),(sk,sc) in [(rr,ss),(ss,rr)]:
     p,t=rc;gg,u,v=egcd(p,t);assert gg==1
     nc=(-v,u);sgn=1 if det(rc,sc)>0 else -1;nc=(sgn*nc[0],sgn*nc[1])
     assert abs(det(rc,nc))==1
     z.inc[(ck,rk)]=add(scale(A,nc[0]),scale(B,nc[1]))
 for key,v in rays.items():z.inc[(key,'o')]=v
 z.indices=[]
 for ck,cell in z.cells.items():
  if cell['dim']!=2:continue
  ends=[key for (co,key) in z.inc if co==ck];A,B=cell['basis'];i=next(i for i,x in enumerate(A) if x);j=next(i for i,x in enumerate(B) if x)
  co=[(rays[key][i]/A[i],rays[key][j]/B[j]) for key in ends]
  z.indices.append(abs(det(*co)))
 return z

def recursion(factors,slots=None):
 dims=[max(c['dim'] for c in z.cells.values()) for z in factors];d=sum(dims)
 allcells=list(product(*[list(z.cells) for z in factors]));cycles={}
 for cell in allcells:
  if all(z.cells[c]['dim']==m for z,c,m in zip(factors,cell,dims)):
   cycles[cell]=prod(z.cells[c]['weight'] for z,c in zip(factors,cell))
 stages=[]
 for step in range(d):
  k=d-step;result={};balancing_tests=0
  slot=None if slots is None else slots[step]
  for facet in allcells:
   if sum(z.cells[c]['dim'] for z,c in zip(factors,facet))!=k-1:continue
   sums=[vec([0]*z.n) for z in factors];first=F(0)
   for j,z in enumerate(factors):
    for (co,fa),n in z.inc.items():
     if fa!=facet[j]:continue
     cell=list(facet);cell[j]=co;cell=tuple(cell);w=cycles.get(cell,F(0))
     if not w:continue
     sums[j]=add(sums[j],scale(n,w))
     if slot is None or slot==j:first+=w*z.value(co,n)
   correction=F(0)
   for j,z in enumerate(factors):
    val=z.value(facet[j],sums[j]);balancing_tests+=1
    if slot is None or slot==j:correction+=val
   coeff=first-correction
   assert coeff>=0,(step,facet,coeff)
   if coeff:result[facet]=coeff
  stages.append({'dimension':k-1,'nonzero_cells':len(result),'tangent_balance_tests':balancing_tests,
                 'coefficient_sum':sum(result.values(),F(0))})
  cycles=result
 return cycles,stages

inp=json.loads(Path('diagnostic-input.json').read_text());records=[]
for case in inp['cases']:
 extra=[graph([x['direction'],[-t for t in x['direction']]],[x['weight']]*2,[x['slope']]*2) for x in case['extra']]
 if case['type']=='higher_relation':
  first=graph(case['directions'],case['weights'],case['slopes']);factors=[first]+extra
  m1=sum(F(w)*F(s) for w,s in zip(case['weights'],case['slopes']))
  expected=factorial(len(factors))*m1*prod(2*F(x['slope'])*F(x['weight']) for x in case['extra'])
  orders=list(permutations(range(len(factors))))
 else:
  first=pair_factor(case);factors=[first]+extra
  d=len(extra)+2;expected=F(factorial(d),2)*8*F(case['kappa'])**2*F(case['a'])*F(case['b'])*prod(2*F(x['slope'])*F(x['weight']) for x in case['extra'])
  orders=sorted(set(permutations([0,0]+list(range(1,len(factors))))))
 result,stages=recursion(factors);assert len(result)==1;mass=next(iter(result.values()));assert mass==expected
 wordmasses=[]
 for order in orders:
  cy,_=recursion(factors,order);assert len(cy)==1;wordmasses.append(next(iter(cy.values())))
 assert len(set(wordmasses))==1 and sum(wordmasses)==mass
 # A repeated line factor forces zero, evaluated by the same full divisor.
 repeat=[0]*sum(max(c['dim'] for c in z.cells.values()) for z in factors)
 if len(factors)>1:repeat=[1]*len(repeat)
 cy,_=recursion(factors,repeat);assert not cy
 records.append({'name':case['name'],'dimension':len(extra)+(1 if case['type']=='higher_relation' else 2),
                 'stages':stages,'full_mass':mass,'surviving_orders':len(orders),
                 'each_order_mass':wordmasses[0],'repeat_factor_zero':True,
                 'pair_actual_indices':getattr(first,'indices',None),
                 'negative_integral_if_the_global_tent_proof_applies':-mass})
out={'method':'Exact Fraction evaluation of the complete divisor formula including integral primitive lifts and tangential corrections at every product facet. Finite germs only, not proof certification.',
     'records':records,'all_assertions_passed':True}
Path('diagnostic-output.json').write_text(json.dumps(out,default=str,indent=2)+'\n')
print(json.dumps(out,default=str,indent=2))
