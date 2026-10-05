"""Small exact diagnostics; these do not verify universal mathematical claims."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

count = 0
for n in range(2,11):
    p = n-1
    for l in range(1,p+1):
        assert sum(comb(j,l) for j in range(l,p+1)) == comb(n,l+1)
        for k in range(65):
            t=F(k,64)
            coefficient=t*sum(F(comb(j,l))*t**l*(1-t)**(j-l) for j in range(l,p+1))
            assert 0 <= coefficient <= 2**n*t*t
            count += 1

def secant(x, depth, upper=4):
    if x <= 0:
        return F(0)
    step=F(upper,2**depth)
    i=min(int(x/step),2**depth-1)
    a=i*step; b=(i+1)*step
    return a*a+(a+b)*(x-a)

secant_count=0
for k in range(257):
    x=F(k,64)
    for depth in range(7):
        coarse=secant(x,depth)
        fine=secant(x,depth+1)
        assert x*x <= fine <= coarse
        secant_count += 1

# Finite-map and radial algebra, with n=p+1. It is documentation, not an analytic test.
scalar_count=0
for n in range(1,7):
    for s in [F(1,3), F(1), F(5,2)]:
        for d in [1,2,3,7,11]:
            raw=s**(-n)*F(d)**(1-n)
            transverse=F(1,(s*d)**(n-1))
            assert transverse == s*raw
            assert F(d,(s*d)**n)==raw
            scalar_count += 1

report={'kind':'exhaustive finite diagnostics only',
        'scaling_coefficient_cases':count,
        'dyadic_secant_cases':secant_count,
        'radial_scalar_cases':scalar_count,
        'all_passed':True,
        'limitations':'No test establishes E1 completeness, envelope membership, universal realization or novelty.'}
Path('checks-output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
