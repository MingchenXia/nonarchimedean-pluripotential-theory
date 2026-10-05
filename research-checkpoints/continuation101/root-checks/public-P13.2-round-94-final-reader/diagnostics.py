#!/usr/bin/env python3
"""Small exhaustive rational diagnostics; none certify the analytic proof."""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import comb
from pathlib import Path
import json

def main():
    # Maxima c-s*r. Every branch slope is in [1,3], and every c is <=0.
    branches = [(F(c),F(s)) for c in (-6,-3,0) for s in (1,2,3)]
    functions = list(combinations_with_replacement(branches,2))
    value = lambda g,r: max(c-s*r for c,s in g)
    root = lambda g: max(c/s for c,s in g)
    checks=0
    for g,f in product(functions,repeat=2):
        for M,N in [(F(1),2),(F(3),3),(F(6),6)]:
            h=M/N
            grid=[-M+j*h for j in range(N+1)]
            clipped_gap=abs(max(root(g),-M)-max(root(f),-M))
            discrepancy=max(abs(value(g,r)-value(f,r)) for r in grid)
            assert clipped_gap <= discrepancy+6*h
            # The stronger continuous discrepancy inverse bound is checked too:
            knots=set(grid)
            for q in (g,f):
                (c,s),(d,t)=q
                if s!=t:
                    knot=(c-d)/(s-t)
                    if -M<=knot<=0:
                        knots.add(knot)
            assert clipped_gap <= max(abs(value(g,r)-value(f,r)) for r in knots)
            assert max(-root(g)-M,0) <= max(-value(g,F(0))-M,0)
            checks+=1
    # Exact midpoint Green integral on each monomial basis for p=1,...,8.
    midpoint=[]
    def integral(poly,lo,hi):
        return sum(c*(hi**(i+1)-lo**(i+1))/F(i+1) for i,c in enumerate(poly))
    for p in range(1,9):
        bound=F(p,4**(p+1))
        for j in range(p):
            poly=[F(0)]*p
            for k in range(p-j):
                poly[j+k]=F(p*comb(p-1,j)*comb(p-1-j,k)*(-1)**k)
            left=[F(0)]+[c/2 for c in poly]
            right=[F(0)]*(p+1)
            for i,c in enumerate(poly):
                right[i]+=c/2
                right[i+1]-=c/2
            exact=integral(left,F(0),F(1,2))+integral(right,F(1,2),F(1))
            assert exact>=bound
            midpoint.append({'p':p,'j':j,'exact_green_integral':str(exact),'a_p':str(bound)})
    calibration_checks=0
    for p,s,d,Vproj in product(range(0,7),(F(1,2),F(1),F(3,2)),(1,2,6),(F(1),F(7))):
        n=p+1
        Vcone=s**(-n)*F(d)**(1-n)*Vproj
        omega_volume=Vproj/(s*d)**p
        assert omega_volume==s*Vcone
        calibration_checks+=1
    out={'kind':'exhaustive finite rational diagnostics, not an analytic proof',
       'piecewise_linear_domain':{'functions':len(functions),'branches_per_function':2,
          'intercepts':[-6,-3,0],'slopes':[1,2,3], 'grids':[[1,2],[3,3],[6,6]]},
       'grid_root_tail_checks':checks,'midpoint_basis_checks':len(midpoint),
       'midpoint_basis_results':midpoint,'calibration_checks':calibration_checks,
       'p1_deficit_factor':str(1/(2*F(1,16))),'all_passed':True,
       'mathematical_acceptance':False}
    Path('diagnostic-output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='midpoint_basis_results'},indent=2))

if __name__=='__main__':
    main()
