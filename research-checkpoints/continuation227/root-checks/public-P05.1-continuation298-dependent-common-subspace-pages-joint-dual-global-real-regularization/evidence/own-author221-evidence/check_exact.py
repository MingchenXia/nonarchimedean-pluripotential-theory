"""Bounded exact finite checks only. No solver, source executable, or network."""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm, factorial
from pathlib import Path
import json

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def solve(mat,rhs):
 n=len(rhs);a=[[F(x) for x in row]+[F(y)] for row,y in zip(mat,rhs)]
 for j in range(n):
  pivot=next((i for i in range(j,n) if a[i][j]),None)
  if pivot is None:return None
  a[j],a[pivot]=a[pivot],a[j];u=a[j][j];a[j]=[x/u for x in a[j]]
  for i in range(n):
   if i!=j:
    u=a[i][j];a[i]=[x-u*y for x,y in zip(a[i],a[j])]
 return tuple(a[i][-1] for i in range(n))
def det(mat):
 if not mat:return F(1)
 return sum(((-1)**j*mat[0][j]*det([r[:j]+r[j+1:] for r in mat[1:]]) for j in range(len(mat))),F(0))
def huber(x): return x*x/2 if abs(x)<=1 else abs(x)-F(1,2)
def egcd(a,b):
 if b==0:return (abs(a),1 if a>=0 else -1,0)
 g,x,y=egcd(b,a%b);return g,y,x-(a//b)*y

def raw_order(mat,order):
 """Successive saturated kernels; no appended factorial."""
 n=len(mat);basis=[[F(int(i==j)) for j in range(n)] for i in range(n)];value=F(1)
 for idx in order:
  rank=len(basis[0]) if basis else 0
  if rank==0:return F(0)
  row=[sum(mat[idx][i]*basis[i][j] for i in range(n)) for j in range(rank)]
  if not any(row):return F(0)
  denom=lcm(*(x.denominator for x in row));w=[int(x*denom) for x in row]
  v=[[int(i==j) for j in range(rank)] for i in range(rank)]
  for j in range(1,rank):
   a,b=w[0],w[j]
   if a==b==0:continue
   g,x,y=egcd(a,b);assert g>0
   old0=[v[i][0] for i in range(rank)];oldj=[v[i][j] for i in range(rank)]
   for i in range(rank):v[i][0]=x*old0[i]+y*oldj[i];v[i][j]=(-b//g)*old0[i]+(a//g)*oldj[i]
   w[0]=g;w[j]=0
  if w[0]<0:
   w[0]=-w[0]
   for i in range(rank):v[i][0]=-v[i][0]
  assert abs(det([[F(x) for x in r] for r in v]))==1
  assert all(dot(row,[F(v[i][j]) for i in range(rank)])==0 for j in range(1,rank))
  value*=2*F(w[0],denom)
  basis=[[sum(basis[i][k]*v[k][j] for k in range(rank)) for j in range(1,rank)] for i in range(n)]
 return value

z=json.loads(Path('exact-input.json').read_text());d=z['diagnostic293'];sample=[tuple(map(F,a)) for a in d['samples']];heights=list(map(F,d['sample_heights']));grad=tuple(map(F,d['support_gradient']))
assert heights==[huber(t)+huber(s) for t,s in sample]
assert all(dot(grad,a)==h for a,h in zip(sample,heights))
assert all(abs(x)<=1 for x in grad)
# Dual epigraph g_A: variables (pt,ps,c), seven rational inequalities >= rhs.
constraints=[((F(1),F(0),F(0)),F(-1)),((F(-1),F(0),F(0)),F(-1)),((F(0),F(1),F(0)),F(-1)),((F(0),F(-1),F(0)),F(-1))]
constraints += [((-t,-s,F(1)),-h) for (t,s),h in zip(sample,heights)]
verts=set()
for ids in combinations(range(7),3):
 sol=solve([constraints[i][0] for i in ids],[constraints[i][1] for i in ids])
 if sol is not None and all(dot(row,sol)>=rhs for row,rhs in constraints):verts.add(sol)
verts=sorted(verts)
def primal(t,s):return max(pt*t+ps*s-c for pt,ps,c in verts)
def trace(t):return -t if t<=0 else t/2 if t<=1 else t-F(1,2)
# Entire trace certificate: each dual vertex form <= trace on all three intervals,
# by endpoint values and outer slopes, and three exposed forms attain them.
for pt,ps,c in verts:assert -1<=pt<=1 and -c<=trace(F(0)) and pt-c<=trace(F(1))
for pt,c in [(-F(1),F(0)),(F(1,2),F(0)),(F(1),F(1,2))]:assert any(a==pt and h==c for a,b,h in verts)
for t in [F(j,8) for j in range(-16,25)]:assert primal(t,F(0))==trace(t)
center=tuple(map(F,d['center']));normals=[tuple(map(F,a)) for a in d['normal_directions']];delta=F(d['normal_displacement']);weights=list(map(F,d['pcc_weights']));ends=[tuple(x+delta*v for x,v in zip(center,normal)) for normal in normals]
assert tuple(sum(v[j] for v in normals) for j in range(3))==(0,0,0)
assert tuple(sum(a*x[j] for a,x in zip(weights,ends)) for j in range(3))==center
bary=list(map(F,d['triangle_barycentric']));endpoint_coord=tuple(sum(a*b[j] for a,b in zip(bary,sample)) for j in range(2));assert endpoint_coord==(F(1,2),F(1,8))
fend=primal(*endpoint_coord);fcenter=primal(F(1,2),F(0));cost=sum(a*fend for a in weights)-fcenter
assert (fend,fcenter,cost)==(F(13,64),F(16,64),-F(3,64))
tangent=d['common_tangent'];lattice=[]
for v in normals:
 minors=[int(tangent[i]*v[j]-tangent[j]*v[i]) for i,j in combinations(range(3),2)]
 assert gcd(*minors)==1
 lattice.append({'primitive_2_by_2_minors':minors,'gcd':1})
assert [primal(*a) for a in sample]==heights
# Explicit Huber joint model: D has |a|,|b|,|c|,|b+c|<=1.
N=z['dual_grid_denominator'];grid=[F(i,N) for i in range(-N,N+1)];fiber_count=0;joint_count=0;lower_count=0
for a in grid:
 k=a*a/2;low=max(abs(a)-F(1,2),F(0));assert k-F(1,8)<=low<=k
 vals=[a*a/2,a*a/2,a*a/2];assert max(vals)==k
 lower_count+=1
 for b,c in product(grid,repeat=2):
  if abs(b+c)>1:continue
  page=[k+b*b/2,k+c*c/2,k+(b+c)**2/2]
  assert all(v>=k for v in page)
  if max(page)==k:assert b==c==0 and page==[k]*3;joint_count+=1
  fiber_count+=1
mat_records=[];orders_checked=0
for raw in z['determinant_matrices']:
 mat=[list(map(F,row)) for row in raw];n=len(mat);mass=F(0);nonnull=0
 for order in product(range(n),repeat=n):
  val=raw_order(mat,order);mass+=val;orders_checked+=1
  if val:nonnull+=1;assert len(set(order))==n and val==2**n*abs(det(mat))
 assert mass==2**n*factorial(n)*abs(det(mat))
 mat_records.append({'matrix':mat,'determinant':det(mat),'raw_sum_of_orders':mass,'nonzero_orders':nonnull,'all_orders':n**n})
out={'status':'PASS: exact stated finite lists only','diagnostic293':{'sample_heights':heights,'dual_epigraph_vertices':verts,'endpoint_barycentric':bary,'ambient_endpoints':ends,'endpoint_value':fend,'center_value':fcenter,'legal_PCC_cost':cost,'lattice_checks':lattice,'entire_trace_certificate':'Endpoint plus recession comparisons for every listed affine dual vertex; three required trace forms attained.'},'joint_model':{'grid_denominator':N,'feasible_tuples_checked':fiber_count,'joint_minimizers_checked':joint_count,'trace_dual_lowering_points':lower_count,'boundary_q_values_included':['-1','1'],'dependent_H_zero_example':'a=0 slice: hexagonal joint normal domain with unique common quadratic minimizer (0,0)'},'saturated_determinant_checks':mat_records,'raw_orders_checked':orders_checked,'limitations':'Finite arithmetic does not verify continuum PC, sample selection, rational projected faces, universal regularization, all refinements, or acceptance. Those are proof claims in the paper.'}
Path('exact-output.json').write_text(json.dumps(out,indent=2,default=str)+'\n');print(json.dumps(out,indent=2,default=str))
