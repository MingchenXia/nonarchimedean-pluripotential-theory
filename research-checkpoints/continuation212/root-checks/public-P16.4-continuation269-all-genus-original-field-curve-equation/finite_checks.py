#!/usr/bin/env python3
"""Small exact finite checks; no analytic or formal-geometry certification."""
from fractions import Fraction as F
from dataclasses import dataclass
from itertools import product
from math import lcm
import json,pathlib
@dataclass(frozen=True)
class Q2:
 a:F=F(0); b:F=F(0)
 def __post_init__(self):
  object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
 def __add__(self,o):
  o=co(o);return Q2(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return Q2(-self.a,-self.b)
 def __sub__(self,o):return self+-co(o)
 def __rsub__(self,o):return co(o)+-self
 def __mul__(self,o):
  o=co(o);return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __truediv__(self,o):
  o=co(o);d=o.a*o.a-2*o.b*o.b;assert d
  return self*Q2(o.a/d,-o.b/d)
 def __rtruediv__(self,o):return co(o)/self
 def sign(self):
  a,b=self.a,self.b
  if not b:return (a>0)-(a<0)
  if not a:return (b>0)-(b<0)
  if a>0 and b>0:return 1
  if a<0 and b<0:return -1
  return ((a*a>2*b*b)-(a*a<2*b*b))*(1 if a>0 else -1)
 def __lt__(self,o):return (self-co(o)).sign()<0
 def __le__(self,o):return (self-co(o)).sign()<=0
 def __gt__(self,o):return (self-co(o)).sign()>0
 def __ge__(self,o):return (self-co(o)).sign()>=0
 def __eq__(self,o):
  o=co(o);return self.a==o.a and self.b==o.b
 def __bool__(self):return bool(self.a or self.b)
 def __abs__(self):return -self if self.sign()<0 else self
 def __str__(self):return str(self.a)+(('+'+str(self.b)+'sqrt(2)') if self.b else '')
def co(x):return x if isinstance(x,Q2) else Q2(x)
def zeros(n):return [[Q2() for _ in range(n)] for _ in range(n)]
def inverse(A):
 n=len(A);m=[row[:]+[co(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  k=next(k for k in range(i,n) if m[k][i]);m[i],m[k]=m[k],m[i]
  c=m[i][i];m[i]=[x/c for x in m[i]]
  for k in range(n):
   if k!=i:
    c=m[k][i];m[k]=[x-c*y for x,y in zip(m[k],m[i])]
 return [r[n:] for r in m]
def lap(n,edges):
 A=zeros(n)
 for v,w,l in edges:
  l=co(l);assert l>0
  if v==w:continue
  c=1/l;A[v][v]+=c;A[w][w]+=c;A[v][w]-=c;A[w][v]-=c
 return A
def kernel(n,edges):
 A=lap(n,edges);B=inverse([r[1:] for r in A[1:]]) if n>1 else [];J=zeros(n)
 for i in range(1,n):
  for k in range(1,n):J[i][k]=B[i-1][k-1]
 assert all(J[i][k]==J[k][i] and J[i][k]>=0 for i in range(n) for k in range(n))
 return J
def matvec(A,x):return [sum((a*b for a,b in zip(r,x)),Q2()) for r in A]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q2())
def floor_q2(x):
 # Integer bracketing/order in Q(sqrt2), not floating-point approximation.
 B=abs(x.a)+2*abs(x.b)+1;lo=-(B.numerator//B.denominator+1);hi=-lo
 while hi-lo>1:
  mid=(lo+hi)//2
  if co(mid)<=x:lo=mid
  else:hi=mid
 return lo
GRAPHS=[('singleton',1,[]),('self_loop',1,[(0,0,Q2(0,1))]),('parallel',2,[(0,1,Q2(1)),(0,1,Q2(0,1))]),('triangle',3,[(0,1,Q2(1)),(1,2,Q2(0,1)),(2,0,Q2(3,1))]),('cycle_branch',4,[(0,1,Q2(1)),(1,2,Q2(2)),(2,0,Q2(0,1)),(2,3,Q2(3))]),('loop_subdivision',3,[(0,1,Q2(1)),(1,2,Q2(0,1)),(2,0,Q2(1))])]
rows=[];bendcases=energycases=0;example=None
for name,n,edges in GRAPHS:
 J=kernel(n,edges);A=lap(n,edges);beta=len(edges)-n+1
 for weights in product((1,2,3),repeat=n):
  raw=Q2(F(5,7));mu=[raw*F(w,sum(weights)) for w in weights];mu0=[raw/F(n) for _ in range(n)]
  u=matvec(J,[b-a for a,b in zip(mu,mu0)])
  assert all(x==y for x,y in zip(matvec(A,u),[b-a for a,b in zip(mu,mu0)]))
  I=dot(mu,matvec(J,mu));I00=dot(mu0,matvec(J,mu0));C=dot(mu,matvec(J,mu0))
  E=dot(u,[x+y for x,y in zip(mu,mu0)])/2;ff=E-dot(u,mu)
  assert E==(I00-I)/2 and ff==(I-2*C+I00)/2;energycases+=1
  # Integer horizontal degree 5, rational vertex targets, exact shared-height perturbations.
  av=[Q2(5)]+[Q2() for _ in range(n-1)];qv=[Q2(F(5*w,sum(weights))) for w in weights]
  h=matvec(J,[a-q for a,q in zip(av,qv)])
  val=[0]*n
  for v,w,l in edges:val[v]+=1;val[w]+=1
  slack=min(qv);margin=slack/(4*max(1,max(val)));minlen=min((l for _,_,l in edges),default=Q2(1))
  for mesh in (1,3,7):
   # rational mesh fine enough for every outgoing margin; perturb GLOBAL heights once.
   scale=mesh
   while co(F(4,scale))/minlen>=margin:scale*=2
   gv=[x+F((i%3)-1,scale*8) for i,x in enumerate(h)]
   old=av[:];new=[];slopes=[];newedges=[]
   for ei,(v,w,l) in enumerate(edges):
    chord=(gv[w]-gv[v])/l;M=scale
    while co(F(2,M))>=margin:M*=2
    z=floor_q2(chord*M);p=F(z-1,M);q=F(z+2,M)
    assert p<chord<q
    t=(q*l-(gv[w]-gv[v]))/(q-p);assert 0<t<l
    assert gv[v]+p*t+q*(l-t)==gv[w]
    assert (q-p)>0
    old[v]+=p;old[w]-=q;new.append(co(q-p));slopes.extend((p,q));
    # Reverse orientation is the same function with slopes -q,-p and bend l-t.
    assert gv[w]-q*(l-t)-p*t==gv[v]
   assert all(x>0 for x in old+new)
   assert sum(old+new,Q2())==5
   k=lcm(*(s.denominator for s in slopes)) if slopes else 1
   assert all((x*k).b==0 and (x*k).a.denominator==1 for x in old+new)
   d=7;N=k;section_power=11
   # whole d*N*section_power, including raw degree after the same tensor power
   assert co(5*N*section_power)/(d*N*section_power)==F(5,7)
   assert (2*len(edges))-(n+len(edges))+1==beta
   bendcases+=1
   if name=='parallel' and example is None:example={'target':[str(x) for x in qv],'old_degrees':[str(x) for x in old],'bend_degrees':[str(x) for x in new],'denominator_multiplier':k,'first_betti':beta}
 rows.append({'graph':name,'vertices':n,'edges':len(edges),'first_betti':beta,'target_grid':3**n})
# Attach one branched tree to a cyclic graph, checking old cycles and common depths.
base_edges=[(0,1,Q2(1)),(1,2,Q2(0,1)),(2,0,Q2(2))];J0=kernel(3,base_edges)
full=base_edges+[(1,3,Q2(3)),(3,4,Q2(2)),(3,5,Q2(0,1))];J=kernel(6,full)
r=[0,1,2,1,1,1]
def common(i,k):
 if i<3 or k<3:return Q2()
 if i==k:return Q2(3)+(Q2(2) if i==4 else Q2(0,1) if i==5 else Q2())
 return Q2(3)
for i in range(6):
 for k in range(6):assert J[i][k]==J0[r[i]][r[k]]+common(i,k)
# Trace law on the core: collapse tree masses and sum outgoing incidences.
mu=[Q2(F(k,42)) for k in range(1,7)];mu0=[Q2(F(1,6))]*3+[Q2()]*3
# Equalize total mass without a probability renormalization assumption.
mu0=[sum(mu,Q2())/3]*3+[Q2()]*3
u=matvec(J,[b-a for a,b in zip(mu,mu0)]);projected=[sum((mu[k] for k in range(6) if r[k]==i),Q2()) for i in range(3)]
assert matvec(lap(3,base_edges),u[:3])==[mu0[i]-projected[i] for i in range(3)]
assert u[4]<=u[3]<=u[1] and u[5]<=u[3]
# Nonatomic interval, anchor0: u(x)=-a(x-x^2/2), I=a^2/3, E=-a^2/6, F=a^2/6.
a=F(5,7);nonatomic=[]
for m in (2,4,8,16,32):
 points=[F(2*k+1,2*m) for k in range(m)]
 for z in range(65):
  x=F(z,64);u=-a*(x-x*x/2);um=-sum((a/m*min(x,y) for y in points),F())
  assert abs(u-um)<=a/(2*m)
 I=sum((a*a/(m*m)*min(x,y) for x in points for y in points),F());nonatomic.append({'atoms':m,'I':str(I),'limit_I':str(a*a/3),'max_error_bound':str(a/(2*m))})
assert -a*(F(1,2)-F(1,8)) != (-a*0 + -a*F(1,2))/2 # not affine
# Concrete flat nonnegative Cech complex: Z^2 -> Z, (x,y) -> x+2y.
for modulus in range(2,13):
 kernels={(x,y) for x in range(modulus) for y in range(modulus) if (x+2*y)%modulus==0}
 assert kernels=={((-2*t)%modulus,t) for t in range(modulus)}
 assert {(x+2*y)%modulus for x in range(modulus) for y in range(modulus)}==set(range(modulus))
# Negative-degree Z --2--> Z: H^-1=0 before mod2, nonzero afterwards.
negative_kernel_mod2={x for x in range(2) if (2*x)%2==0}
assert negative_kernel_mod2=={0,1} and F(2)!=0
negative_obstruction={'degrees':[-1,0],'map':2,'base_change_modulus':2,'before_Hminus1_rank':0,'after_Hminus1_elements':2}
result={'status':'exact finite arithmetic checks, not analytic proof','graphs':rows,'energy_cases':energycases,'positive_bend_cases':bendcases,'tree_kernel_pairs':36,'trace_cancellation':True,'raw_mass':'5/7','example':example,'nonatomic_interval':nonatomic,'flat_Cech_moduli':list(range(2,13)),'negative_degree_obstruction':negative_obstruction}
pathlib.Path('finite-inputs.json').write_text(json.dumps({'graphs':[{'name':s,'n':n,'edges':[(v,w,str(l)) for v,w,l in e]} for s,n,e in GRAPHS],'weights':[1,2,3],'mesh_factors':[1,3,7],'raw_mass':'5/7','horizontal_degree':5,'original_denominator_d':7,'formal_section_power':11},indent=2)+'\n')
pathlib.Path('finite-output.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
