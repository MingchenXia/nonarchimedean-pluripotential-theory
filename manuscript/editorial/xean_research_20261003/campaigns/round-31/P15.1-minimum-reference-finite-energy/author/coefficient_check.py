#!/usr/bin/env python3
"""Exact finite algebra diagnostics. These are not pluripotential proofs."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json

def c(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def solve(a,b):
    a = [list(map(F,row))+[F(value)] for row,value in zip(a,b)]
    n = len(b)
    for j in range(n):
        pivot = next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot] = a[pivot],a[j]
        scale = a[j][j]
        a[j] = [x/scale for x in a[j]]
        for i in range(n):
            if i != j:
                scale = a[i][j]
                a[i] = [x-scale*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]

def p(coeff,xy):
    m=len(coeff)-1
    x,y=xy
    return sum(a*x**(m-k)*y**k for k,a in enumerate(coeff))

def main():
    vandermonde = 0
    for n in range(25):
        for k in range(n+1):
            for a in range(k+1):
                assert sum(c(j,a)*c(n-j,k-a) for j in range(n+1))==c(n+1,k+1)
                assert F(c(n+1,k+1),n+1)==F(c(n,k),k+1)
                vandermonde += 1
    interpolation = 0
    polarization = 0
    errors = []
    for m in range(1,9):
        coeff = [F((-1)**k*(k+2),k+1) for k in range(m+1)]
        points = [(F(1),F(t)) for t in range(1,m+2)]
        matrix = [[x**(m-k)*y**k for k in range(m+1)] for x,y in points]
        assert solve(matrix,[p(coeff,xy) for xy in points])==coeff
        interpolation += 1
        for level in (1,2,10,100):
            approximation = [v+F(k+1,level) for k,v in enumerate(coeff)]
            recovered = solve(matrix,[p(approximation,xy) for xy in points])
            assert recovered == approximation
            errors.append({'m':m,'level':level,'coefficient_max_error':str(max(abs(x-y) for x,y in zip(recovered,coeff)))})
            interpolation += 1
        args = [(F(i+1),F(i+2)) for i in range(m)]
        polarized = F(0)
        for size in range(m+1):
            for subset in combinations(range(m),size):
                xy=(sum(args[i][0] for i in subset),sum(args[i][1] for i in subset))
                polarized += (-1)**(m-size)*p(coeff,xy)
        polarized /= factorial(m)
        direct = F(0)
        for k,alpha in enumerate(coeff):
            term = F(0)
            for subset in combinations(range(m),k):
                idx=set(subset)
                value=F(1)
                for i,(x,y) in enumerate(args):
                    value *= y if i in idx else x
                term += value
            direct += alpha*term/comb(m,k)
        assert polarized==direct
        polarization += 1
    deficits = 0
    for m in range(1,13):
        x,y,A=F(2),F(3),F(5)
        D=A*x-y
        assert D>0
        assert sum(F(comb(m,j))*y**j*D**(m-j) for j in range(m+1))==(A*x)**m
        deficits += 1
    report={'subset_coefficient_cases':vandermonde,'homogeneous_interpolation_cases':interpolation,
            'polarization_cases':polarization,'synthetic_positive_expansion_cases':deficits,
            'synthetic_coefficient_errors':errors,'all_passed':True,
            'scope':'Exhaustive finite checks of the stated arithmetic cases only; no analytic correctness certification.'}
    Path('coefficient-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f'Exact diagnostics passed: {vandermonde} coefficient cases, {interpolation} interpolation cases, '
          f'{polarization} polarization cases, {deficits} positive expansions.')

if __name__=='__main__':
    main()
