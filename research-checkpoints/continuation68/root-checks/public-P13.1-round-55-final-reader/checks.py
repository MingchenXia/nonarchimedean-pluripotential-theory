"""Small exact finite checks. These do not certify the general mathematical claims."""
from fractions import Fraction as F
from itertools import product
from math import comb, ceil
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def degree(xi, alpha):
    return sum(x*a for x,a in zip(xi,alpha,strict=True))

def fs(v, xi, alphas, lambdas):
    values=[]
    for alpha,lam in zip(alphas,lambdas,strict=True):
        if any(a and z is None for a,z in zip(alpha,v,strict=True)):
            continue
        val=sum(a*z for a,z in zip(alpha,v,strict=True) if a)
        values.append((lam-val)/degree(xi,alpha))
    return max(values) if values else None

def translate(v, t, xi):
    return tuple(None if x is None else x+t*d for x,d in zip(v,xi,strict=True))

count=[]
for n in range(1,6):
    for m in range(1,21):
        number=comb(m+n,n)
        weight=sum(d*comb(d+n-1,n-1) for d in range(m+1))
        assert weight == n*comb(m+n,n+1)
        assert F(weight,m*number) == F(n,n+1)
    count.append({'dimension':n,'cutoffs_checked':[1,20],
                  'exact_cumulative_average':str(F(n,n+1)),
                  'genuine_energy_for_reference_plus_one_by_argument':1})

xi=(F(1),F(1)); eta=(F(1),F(2)); zeta=(F(2),F(1))
alphas=[(1,0),(0,1),(2,0)]
carrier=[v for v in product([F(x) for x in range(6)],repeat=2) if min(v)==0]
carrier.extend([(None,F(0)),(F(0),None)])
root_checks=0
for lambdas in product([F(-3),F(-1),F(0),F(2)],repeat=3):
    for v in carrier:
        u=fs(v,xi,alphas,lambdas)
        root=fs(v,eta,alphas,lambdas)
        assert fs(translate(v,root,eta),xi,alphas,lambdas)==0
        # The zero-set construction recovers the source function and cocycle.
        assert fs(translate(v,u,xi),eta,alphas,lambdas)==0
        r3=fs(v,zeta,alphas,lambdas)
        assert fs(translate(v,r3,zeta),eta,alphas,lambdas)==0
        c=F(1); C=F(2)
        if u<=0:
            assert u/c<=root<=u/C
        else:
            assert u/C<=root<=u/c
        root_checks+=1

quotient=[]
for v in [(F(0),F(0)),(F(3),F(0))]:
    raw=fs(v,eta,[(1,0),(0,1)],[F(2),F(2)])
    ref=fs(v,eta,[(1,0),(0,1)],[F(0),F(0)])
    quotient.append({'valuation':[str(x) for x in v],'raw_shift_difference':str(raw-ref)})
assert quotient[0]['raw_shift_difference']=='2'
assert quotient[1]['raw_shift_difference']=='1'

primary_checks=0
# A genuinely primary presentation x^2,y^3, supplemented with x,y.
for theta in [xi,eta,zeta,(F(3,2),F(5,3))]:
    for v in carrier:
        u=fs(v,theta,[(2,0),(0,3)],[F(-1),F(-2)])
        augmented=fs(v,theta,[(2,0),(0,3),(1,0),(0,1)],
                     [F(-1),F(-2),F(-100),F(-100)])
        assert u==augmented
        primary_checks+=1

def eigenweight(i,j):
    # x,y,x^2 all have assigned weight -1; toric monomials are a basis.
    return -ceil(i/2)-j

def totals(theta, cutoff):
    maximum=int(cutoff/min(theta))
    points=[(i,j) for i in range(maximum+1) for j in range(maximum+1)
            if theta[0]*i+theta[1]*j<=cutoff]
    N=len(points)
    W=sum(eigenweight(i,j) for i,j in points)
    D=sum(theta[0]*i+theta[1]*j for i,j in points)
    # Shift by A=2 times this field's own degree. All three generators
    # and all actual monomial weights become nonnegative.
    shifted=[eigenweight(i,j)+2*(theta[0]*i+theta[1]*j) for i,j in points]
    assert min(shifted)>=0
    assert sum(shifted)==W+2*D
    return N,W,D

cutoff_observations=[]
for m in [10,40,100,160]:
    nx,wx,dx=totals(xi,F(m))
    ne,we,de=totals(eta,F(m))
    small=totals(xi,F(m,2))[1]
    assert wx<=we<=small
    cutoff_observations.append({'cutoff':m,'S_xi_exact_fraction':str(F(wx,m*nx)),
                               'S_eta_exact_fraction':str(F(we,m*ne)),
                               'signed_inclusion_verified':True,
                               'shift_identity_verified_both_fields':True})

# Redundant-generator norm saturation: x^2 assigned -10 but x assigned -1.
assigned_x2=F(-10)
actual_x2=max(assigned_x2,F(-2))
assert actual_x2>assigned_x2
assert -eigenweight(2,0)<-2*eigenweight(1,0)

output={
    'epistemic_status':'Exact arithmetic on finite examples only; not a general proof or correctness certificate.',
    'polynomial_degree_counts':count,
    'orbit_examples_checked':root_checks,
    'included_semivaluations_with_infinite_coordinate':True,
    'raw_quotient_counterexample':quotient,
    'primary_supplementation_examples_checked':primary_checks,
    'signed_cutoff_observations':cutoff_observations,
    'saturation_example':{'assigned_weight_x2':str(assigned_x2),'actual_weight_x2':str(actual_x2)},
    'negation_nonmultiplicative':{'chi_x':-1,'chi_x2':-1,'negated_chi_x2':1,'sum_negated_chi_x':2},
}
(ROOT/'checks-output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
