"""Small exact finite diagnostics. They do not verify the analytic proof."""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json
counts={};observations={}
# The cumulative/degree-wise factor is already forced by translations.
cnt=0
for n in range(1,7):
 for m in range(1,25):
  N=comb(m+n,n);W=sum(q*comb(q+n-1,n-1) for q in range(m+1))
  assert W==n*comb(m+n,n+1)
  assert F(W,m*N)==F(n,n+1);cnt+=1
counts['translation_and_binomial_identities']=cnt
# Signed extended-semigroup count on the full section ring of P^1.
cnt=0
for m in range(1,51):
 weights=[-m-j for j in range(m+1)]
 gamma={(m,j,a) for j,w in enumerate(weights) for a in range(-4*m,w+1)}
 assert len(gamma)==sum(weights)+(4*m+1)*(m+1)
 assert len(gamma)==(m+1)*(5*m+2)//2
 assert F(sum(weights),m*(m+1))==F(-3,2);cnt+=1
counts['signed_extended_semigroup_slices']=cnt
observations['P1_signed_example']={'assignments':{'x':-1,'y':-2},'C':4,'slice_volume':'5/2','a0':'1','signed_degree_mean':'-3/2','count_m50':len(gamma),'interpretation':'The count and mean are exact finite arithmetic; identifying the mean with genuine energy uses the paper argument.'}
# A genuinely nonnormal finite semigroup with the full group lattice.
def S(m):
 return {2*j+l for l in range(m//2+1) for j in range(m-2*l+1)}
cnt=0
for m in range(0,61):
 vals=S(m)
 if m:assert len(vals)==2*m and 2*m-1 not in vals
 # c=(2,1): translate every boundary and interior cone lattice point.
 assert {1+a for a in range(2*m+1)}<=S(m+2);cnt+=1
counts['nonnormal_full_lattice_conductor_slices']=cnt
observations['conductor_example']={'generators':[[1,0],[1,2],[2,1]],'full_lattice_determinant':1,'conductor':[2,1],'slice_volume':2,'missing_point_at_degree_m':'(m,2m-1)','scope':'All cone lattice points up to degree 60 were enumerated; the universal conductor proof is in the paper.'}
# A rank-six Veronese module with explicit fixed denominator and signed shifts.
e=[(0,0),(2,1),(1,0),(0,1),(2,0),(1,1)];cnt=0
for a in range(21):
 for b in range(21):
  residue=(2*a+3*b)%6;u,v=e[residue]
  assert (2*u+3*v)%6==residue
  qa,qb=a+3-u,b+2-v
  assert qa>=0 and qb>=0 and (2*qa+3*qb)%6==0
  norm=lambda x,y:-x-2*y
  assert norm(u,v)+norm(qa,qb)==norm(a,b)-7
  cnt+=1
counts['rank_six_residue_and_signed_shift_cases']=cnt
observations['rank_six_module']={'degrees':[2,3],'Veronese':6,'residue_basis_exponents':e,'denominator_exponents':[3,2],'denominator_degree':12,'denominator_index':-7}
# Sign-sensitive roots, including +infinity coordinates.
cnt=0
for ax in [F(1),F(2),F(3)]:
 for ay in [F(1),F(2),F(4)]:
  c=min(ax,ay);C=max(ax,ay)
  for lx,ly in [(F(0),F(-1)),(F(-3),F(0)),(F(-2),F(0))]:
   for vx,vy in [(F(0),F(q)) for q in range(7)]+[(F(q),F(0)) for q in range(7)]+[(F(0),None),(None,F(0))]:
    branches=[(lx-vx,ax)] if vx is not None else []
    if vy is not None:branches.append((ly-vy,ay))
    u=max(x for x,d in branches);root=max(x/d for x,d in branches)
    assert u/c<=root<=u/C<=0;cnt+=1
counts['normalized_root_cases_with_infinite_values']=cnt
# The explicit both-sign quadratic binomial bound.
cnt=0
for p in range(1,6):
 for A in [F(1,3),F(1),F(3)]:
  for tau in [F(1,4),F(1),F(2)]:
   for j in range(1,13):
    t=tau*F(j,12)
    lhs=2*t*((1+A*t)**p-1);rhs=2*p*A*(1+A*tau)**(p-1)*t*t
    assert lhs<=rhs;cnt+=1
counts['quadratic_binomial_bounds']=cnt
# Actual cone/projective/finite-map scalar cancellations.
cnt=0
for n in range(1,6):
 for d in range(1,7):
  for s in [F(1,2),F(1),F(3,2)]:
   volume=s**(-n)*F(d)**(1-n)*7
   current_factor=F(d)/(s*d)**n
   assert volume==current_factor*7
   energy_factor=(F(d)/(s*d)**(n+1)*7)/volume
   assert energy_factor==1/(s*d);cnt+=1
counts['finite_map_mass_and_energy_scalars']=cnt
N=W=0
for a in range(61):
 for b in range(41):
  if 2*a+3*b<=120:N+=1;W+=-a-2*b
observations['weighted_cutoff_120']={'dimension':N,'weight_sum':W,'signed_cutoff_mean':str(F(W,120*N)),'paper_predicted_asymptotic_mean':'-7/18','paper_predicted_energy':'-7/12','status':'Finite observation plus separately labeled mathematical predictions.'}
report={'checks_passed':True,'counts':counts,'observations':observations,'epistemic_status':'Exhaustive finite results only for the enumerated domains; not mathematical verification of the cone theorem.'}
Path('checks-output.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
