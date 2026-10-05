"""Small exact examples; these do not test or prove the infinite analytic claims."""
from pathlib import Path
import json
from fractions import Fraction as Q

# Multiplication by T0+T1*z in k[a,z]/(z^2-a), basis 1,z:
# [[T0, a*T1], [T1,T0]]. Independent expansion records its determinant.
def multiply(p,q):
    result={}
    for e,c in p.items():
        for f,d in q.items():
            g=tuple(x+y for x,y in zip(e,f))
            result[g]=result.get(g,0)+c*d
    return {e:c for e,c in result.items() if c}

# Exponent order is (a,T0,T1); expand the determinant from the four entries.
T0={(0,1,0):Q(1)}
T1={(0,0,1):Q(1)}
aT1={(1,0,1):Q(1)}
det=multiply(T0,T0)
for e,c in multiply(aT1,T1).items(): det[e]=det.get(e,0)-c
assert det=={(0,2,0):Q(1),(1,0,2):Q(-1)}
determinant_terms={"T0^2":int(det[(0,2,0)]),"a*T1^2":int(det[(1,0,2)])}
examples=[]
for alpha in [Q(-4),Q(-2),Q(0),Q(2),Q(4)]:
    # A split geometric fiber: log|z|=alpha/2; the total Artinian degree is 2.
    fiber_trace=2*max(alpha/2,Q(-1))
    determinant_gauss=max(Q(-2),alpha)
    assert fiber_trace==determinant_gauss
    examples.append({'log_abs_a':str(alpha),'trace':str(fiber_trace),'determinant_gauss':str(determinant_gauss)})
assert 2*Q(-1)==Q(-2) # dimension-two center at a=0 (log|a|=-infinity)
# Pole order example: f=z^2, h=z^-1, a=2,c=1; true pole bound, false ar<=c.
assert 2*1==1*2 and not (2*1<=1)
payload={'kind':'exact finite example calculations','determinant_terms':determinant_terms,'sample_rational_log_radii':examples,'nilpotent_center':{'artinian_dimension':2,'u_at_center':-1,'trace':-2},'pole_order_example':{'a':2,'c':1,'ord_f':2,'pole_order_h':1,'true_pole_bound':True,'printed_denominator_bound':False},'limits':'The five finite rational-radius cases and symbolic 2 by 2 determinant are exact. They do not establish the general determinant, curve, envelope or equation theorems.'}
Path('algebra-checks.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'exact_rational_examples':len(examples),'nilpotent_center_checked':True,'false_denominator_bound_checked':True}))
