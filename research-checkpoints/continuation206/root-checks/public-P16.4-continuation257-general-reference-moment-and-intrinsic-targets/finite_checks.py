"""Exact finite evidence; these checks do not certify geometric source applications."""
from fractions import Fraction as F
from math import comb,factorial,isqrt
from itertools import product
from pathlib import Path
import json

def bernstein_integral(n,k,t):
 return sum((F(comb(n,k)*comb(n-k,j)*(-1)**j,k+j+1)*t**(k+j+1) for j in range(n-k+1)),F(0))
r={'status':'PASS','kind':'exhaustive finite rational arithmetic and symbolic coefficient checks','mathematical_correctness_certified':False}
c=0
for n in range(1,13):
 D=F(n*(n+1),2)
 for t in [F(j,40) for j in range(41)]:
  z=[bernstein_integral(n,k,t) for k in range(n+1)]
  assert sum(z)==t
  assert 0<=z[0]<=t
  for k in range(1,n+1):
   assert 0<=z[k]<=D*t*t/F(n+1)
  c+=1
r['bernstein_time_pairs']=c;r['bernstein_domain']={'n':[1,12],'t':'j/40, j=0,...,40'}
# Exact identity at t=1: each integrated Bernstein basis coefficient is 1/(n+1).
assert all(bernstein_integral(n,k,F(1))==F(1,n+1) for n in range(1,25) for k in range(n+1))
r['bernstein_endpoint_coefficients']=sum(n+1 for n in range(1,25))
# Counterexample with ell=m^2 and raw mass V; genuine formulas follow O/Q/N, not this program.
ce=[]
for V in [F(1),F(2),F(3,2)]:
 for m in range(2,22):
  ell=F(m*m);B=V*ell/2;A=V*ell;obj=-B+A
  t=F(1,m); unitB=V*t*t*ell/2;unitA=V*t*ell
  assert obj==B and unitA==V*m
  ce.append({'V':str(V),'m':m,'B':str(B),'objective':str(obj),'scaled_B':str(unitB),'scaled_A':str(unitA)})
r['counterexample_rows']=len(ce);r['counterexample_first_last']=[ce[0],ce[19]]
# Scaling bound with c >= sqrt(2 D B), keeping every calculation rational.
count=0
for n,M,B in product(range(1,13),[F(0),F(1,3),F(2),F(10)],[F(0),F(1,8),F(1),F(9),F(100)]):
 D=F(n*(n+1),2); q=2*D*B; c=F(isqrt(q.numerator//q.denominator)+1);assert c*c>=q
 t=1/(1+2*M+c);bound=t*M+D*t*t*B
 assert bound<=1 and t>0
 count+=1
r['scaling_pairs']=count
# Actual polynomial map-degree model: residue index of tau -> tau^q, basis residues modulo |q|.
count=0
for q in list(range(-12,0))+list(range(1,13)):
 for power in range(-60,61):
  j=power%abs(q);k=(power-j)//q
  assert power==q*k+j and 0<=j<abs(q)
  count+=1
r['laurent_residue_decompositions']=count
# Full Gauss incidence rank on the affine coordinate model: exact determinant cases.
rank2=sing2=0
for a,b,c,d in product(range(-2,3),repeat=4):
 if a*d-b*c:rank2+=1
 else:sing2+=1
r['two_row_rank_grid']={'total':rank2+sing2,'full_rank':rank2,'singular':sing2,'entries':'-2,...,2'}
# Koszul E1 coordinates for total degree 0 and incoming degree -1.
ks=[]
for n in range(2,25):
 for k in range(1,n):
  for q in [k,k-1]:
   assert q==0 or 1<=q<=n-1
   ks.append((n,-k,q,q-k))
r['koszul_diagonal_terms']=len(ks)
# Fixed-cycle metric / finite max Lipschitz check; real weights modeled by all listed rational weights.
lengths=[F(1),F(3,2),F(2)];max_slope=F(3)
# Functions continuous around one cycle: slopes (a,b,c) satisfying sum slope*length=0.
families=[]
for a,b in product([F(j,2) for j in range(-4,5)],repeat=2):
 c=-(a*lengths[0]+b*lengths[1])/lengths[2]
 if abs(c)<=max_slope:families.append((a,b,c))
paths=[F(0),F(1),F(5,2),F(9,2)]
def val(slopes,x):
 v=F(0);offset=F(0)
 for q,l in zip(slopes,lengths):
  v+=q*max(F(0),min(l,x-offset));offset+=l
 return v
cnt=0
for slopes in families:
 assert val(slopes,paths[-1])==0
 for x,y in product(paths,repeat=2):
  dist=min(abs(x-y),paths[-1]-abs(x-y))
  assert abs(val(slopes,x)-val(slopes,y))<=max_slope*dist
  cnt+=1
r['cycle_path_tests']=cnt
weighted=0
for f,g in product(families[:9],repeat=2):
 for b,c in product([F(-5,2),F(0),F(7,3)],repeat=2):
  for x,y in product(paths,repeat=2):
   dist=min(abs(x-y),paths[-1]-abs(x-y));denom=F(7)
   wx=max(val(f,x)+b,val(g,x)+c)/denom
   wy=max(val(f,y)+b,val(g,y)+c)/denom
   assert abs(wx-wy)<=max_slope*dist/denom
   weighted+=1
r['weighted_maximum_path_tests']=weighted
r['weighted_maximum_domain']='first9 cycle functions, both weights in{-5/2,0,7/3}, denominator7, four endpoint positions'
r['limitations']='Only the explicitly listed finite domains are exhaustive. No analytic model, all-field point, target attainment, or universal slope theorem is machine-certified.'
Path('finite-checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
