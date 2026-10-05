#!/usr/bin/env python3
"""Small exact illustrations, never a numerical test of analytic theorems."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

records = []
grid = [F(i, 4) for i in range(5)]
for chis in itertools.product(grid, repeat=4):
    if max(chis) != 1:
        continue
    partial = F(0)
    rhos = []
    for chi in chis:
        rho = min(chi, 1-partial)
        assert rho >= 0 and rho <= chi
        rhos.append(rho)
        partial += rho
    assert partial == 1
    records.append({'chi': list(map(str, chis)), 'rho': list(map(str, rhos))})
shifts = []
for r in range(2, 12):
    eps_previous, eps = F(1, 4**(r-1)), F(1, 4**r)
    tail_previous, tail = F(8, 3)*eps_previous, F(8, 3)*eps
    upper_increment = eps_previous + eps + tail-tail_previous
    assert upper_increment == eps-eps_previous < 0
    shifts.append({'r': r, 'worst_increment': str(upper_increment)})
tail_sup = []
for m in range(1, 6):
    for a in range(-3, 4):
        expected = F(max(a,0), m)
        terms = [F(a,j) for j in range(m,100)]
        assert all(term <= expected for term in terms)
        if a >= 0:
            assert terms[0] == expected
        else:
            assert terms[-1] > terms[0]
        tail_sup.append({'m': m, 'a': a, 'supremum': str(expected), 'attained': a>=0})
annuli=[]
for r in range(2, 10):
    c_previous=-r
    radius_previous=r+3
    assert 1-radius_previous<c_previous
    annuli.append({'r':r, 'old_floor':c_previous, 'old_radius':radius_previous, 'new_branch_upper_bound':1-radius_previous})
# B=A[z]/(z^2-a); multiplication by T0+T1*z has matrix
# [[T0, a*T1],[T1,T0]], determinant T0^2-a*T1^2.
determinant={'algebra':'k[a,z]/(z^2-a)', 'matrix':[['T0','a*T1'],['T1','T0']],
 'determinant':'T0^2-a*T1^2', 'u':'max(log|z|,-1)',
 'trace':'max(log|a|,-2)', 'center_artinian_dimension':2,
 'center_trace':-2, 'unweighted_center_value':-1}
result={'epistemic_status':'Exact finite arithmetic illustrations only; no analytic theorem or novelty checked.',
 'partition_grid_exhaustive_count':len(records), 'partition_grid_domain':'four coordinates in {0,1/4,1/2,3/4,1}, at least one equals 1',
 'partition_examples':records,'uniform_shift_checks':shifts,'tail_supremum_checks':tail_sup,
 'annular_checks':annuli, 'scalar_example':{'A':3,'dimension':4,'divided_product_multiplier':81,'undivided_product_extra_multiplier':1},
 'determinant_example':determinant}
Path('algebra-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'partition_cases':len(records),'shift_cases':len(shifts),'tail_cases':len(tail_sup),'annular_cases':len(annuli),'passed':True}))
