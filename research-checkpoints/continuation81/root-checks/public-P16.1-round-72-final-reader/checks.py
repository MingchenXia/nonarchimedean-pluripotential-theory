from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial, comb
import json

def compositions(m,n):
    if n==1:
        yield (m,)
    else:
        for a in range(m+1):
            for tail in compositions(m-a,n-1):
                yield (a,)+tail

counts = dict(multinomial=0, real_support_monotonicity=0,
              split_integer_weights=0, dyadic_secants=0, actual_pole_example=0)
for n in range(1,4):
    for m in range(1,7):
        betas=list(compositions(m,n+1))
        assert len(betas)==comb(m+n,n)
        coefficients=[factorial(m)//__import__('functools').reduce(lambda a,b:a*b,(factorial(t) for t in beta),1) for beta in betas]
        for tail in product([F(0),F(1,2),F(1),F(2)],repeat=n):
            z=(F(1),)+tail
            terms=[F(c)*__import__('functools').reduce(lambda a,b:a*b,(x**p for x,p in zip(z,beta)),F(1)) for c,beta in zip(coefficients,betas)]
            total=sum(terms,F(0)); expected=sum(z,F(0))**m
            assert total==expected
            assert max(terms)<=total<=len(terms)*max(terms)
            counts['multinomial']+=1

# All interval/floor choices below are exact rational values. These finite
# examples exercise the monotonicity proof's upper-bound constraint F'<=D H.
for q0,q1,r1,r0 in [(F(0),F(1,4),F(3,4),F(1)),(F(1,2),F(5,8),F(7,8),F(1)),(F(1,4),F(1,4),F(3,4),F(1))]:
    for d,h in product(range(1,5),[F(1),F(3,2),F(4)]):
        eta0=d*(r0-q0);eta1=d*(r1-q1)
        assert eta0-eta1>=d*(q1-q0)
        for f1 in [F(-10),F(-1),F(0),F(1),d*h]:
            assert f1<=d*h
            for drop in [F(0),F(1,4),F(3)]:
                f0=f1+drop
                L0=q0*f0+(eta0+F(1,2))*h+F(1)
                L1=q1*f1+(eta1+F(1,4))*h
                assert L0>=L1
                counts['real_support_monotonicity']+=1

split_evidence=[]
for gamma in range(1,9):
    for multiplicity in range(1,gamma+1):
        delta=F(1)
        if gamma==1:
            assert multiplicity==1
            bound=-delta
        else:
            bound=-multiplicity*delta+(gamma-multiplicity)*delta/F(2*(gamma-1))
            assert bound<=-delta/2
        split_evidence.append(dict(gamma=gamma,own_weight=multiplicity,upper_bound=str(bound)))
        counts['split_integer_weights']+=1

def secant(x,M,level):
    if x>=0:return F(0)
    steps=2**level
    offset=(x+M)*steps/M
    index=min(steps-1,offset.numerator//offset.denominator)
    left=-M+M*F(index,steps);right=left+M/F(steps)
    return left**2+(right**2-left**2)*(x-left)/(right-left)

for M in [F(1),F(2),F(3)]:
    for level in range(6):
        for i in range(2**(level+3)+1):
            x=-M+M*F(i,2**(level+3))
            assert x**2<=secant(x,M,level+1)<=secant(x,M,level)
            counts['dyadic_secants']+=1

for i in range(-20,21):
    t=F(i,2)
    assert -2*t<=max(F(0),2*t,-2*t)
    counts['actual_pole_example']+=1
assert not (2*1<=1)
assert 2*1==1*2

report=dict(epistemic_status='Exhaustive finite rational checks on the listed grids only; not mathematical certification.',
            domains={'multinomial':'N=1..3, m=1..6, z0=1, zi in {0,1/2,1,2}',
                     'real_support':'3 nested intervals, D=1..4, 3 H values, 5 F-prime values, 3 nonnegative drops',
                     'split':'gamma=1..8 and every own integer weight 1..gamma, delta=1',
                     'secants':'M=1,2,3; levels 0..5; all mesh points with denominator 2^(level+3)',
                     'pole':'t=i/2, i=-20..20'},
            counts=counts,total=sum(counts.values()),split_evidence=split_evidence,
            whole_sum_floor_diagnostic='At z=0, max(p log|z|,-j)=-j independently of w; positive w-generator growth is impossible.',
            strict_interior_diagnostic='The interior of {|1|<=1} is the full space; {|1|<1} is empty.')
Path('finite-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'counts':counts,'total':report['total'],'all_passed':True}))
