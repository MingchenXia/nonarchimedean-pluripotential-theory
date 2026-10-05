#!/usr/bin/env python3
"""Small exact rational diagnostics. These are not proofs of the paper."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
NEG=None

def weighted(w,x):
    if any(a>0 and b is NEG for a,b in zip(w,x)): return NEG
    return sum((a*b for a,b in zip(w,x) if a),F(0))
def maximum(xs):
    ys=[x for x in xs if x is not NEG]
    return max(ys) if ys else NEG

def vertices(lam):
    n=len(lam);ws=[]
    for i,a in enumerate(lam):
        if a>=0:
            w=[F(0)]*n;w[i]=F(1);ws.append(w)
    for i,a in enumerate(lam):
        for j,b in enumerate(lam):
            if a>0>b:
                w=[F(0)]*n;w[i]=-b/(a-b);w[j]=a/(a-b);ws.append(w)
    return ws

def primal(lam,x):
    inds=[i for i,z in enumerate(x) if z is not NEG]
    if not inds:return NEG
    largest=max(lam[i] for i in inds)
    if largest<0:return NEG
    rs={F(0)}
    for i in inds:
        for j in inds:
            if lam[i]!=lam[j]:
                r=(x[j]-x[i])/(lam[i]-lam[j])
                if r>=0:rs.add(r)
    vals=[max(x[i]+r*lam[i] for i in inds) for r in rs]
    if largest==0:vals.append(max(x[i] for i in inds if lam[i]==0))
    return min(vals)

count=0
for n in [2,3]:
    for lam0 in product(range(-2,3),repeat=n):
        lam=tuple(map(F,lam0))
        if max(lam)<0:continue
        ws=vertices(lam)
        for x0 in product([NEG,F(-3),F(-1),F(0)],repeat=n):
            left=primal(lam,x0);right=maximum(weighted(w,x0) for w in ws)
            assert left==right,(lam,x0,left,right)
            count+=1
round_count=0
for z in [F(-7,3),F(-1,7),F(0),F(11,5)]:
    for d in [F(1,2),F(1,7),F(1,19)]:
        scale=1000
        upper=F(-(-z.numerator*scale//z.denominator),scale)
        assert z<=upper<=z+d
        round_count+=1
# A finite shadow preserves the incompatible-pole obstruction; not a test of nets.
N=7;terms=[]
for n in range(N):
    terms.append([NEG if j==n else F(-1) for j in range(N)])
compatible=0
for n,row in enumerate(terms):
    for m,later in enumerate(terms):
        if all(b is NEG or (a is not NEG and b<=a) for a,b in zip(row,later)):
            assert n==m
            compatible+=1
ray={str(b):[str(max(F(0),F(b)-t)-F(b)) for t in [F(0),F(1,2),F(1),F(2),F(3)]] for b in [1,2]}
assert ray['1']!=ray['2']
# Explicit numeric evidence that divided quotients need not decrease.
h1,t1,h2,t2=F(-4,5),F(7,10),F(-9,10),F(17,20)
r1,r2=h1+t1,h2+t2
assert h2<=h1 and t2>=t1 and r2>r1
out={'status':'pass','kind':'exhaustive finite rational diagnostics on explicitly bounded domains',
 'polytope_cases':count,'polytope_domain':'n=2,3; coefficients {-2,-1,0,1,2}, max>=0; logarithms {-infinity,-3,-1,0}',
 'rounding_cases':round_count,'incompatible_pole_families':N,'compatible_ordered_pairs':compatible,
 'zero_volume_ray_values':ray,'nonmonotone_quotient_example':{'h':[str(h1),str(h2)],'t':[str(t1),str(t2)],'sigma':'-1','quotients':[str(r1),str(r2)]},
 'limitation':'No mathematical correctness certificate. Does not establish geometric section existence, nets, local currents, energy, compactness or attainment.'}
Path('checks-output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
