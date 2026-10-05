#!/usr/bin/env python3
"""Bounded exact diagnostics, not a proof checker for analytic assertions."""
from fractions import Fraction as Q
from itertools import product
import json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent

def main():
    counts={}; examples={}
    # P=(T0+xT1+yT2)^2-x(xT3+yT4)^2.
    # Every tuple below is a complete finite enumeration; valuation of 2 is 0.
    n=0
    for rx,ry in product(map(Q,[-2,-1,0,1,2]),repeat=2):
        for w in product(map(Q,[-1,0,1]),repeat=5):
            u=max(w[0],rx+w[1],ry+w[2],Q(3,2)*rx+w[3],ry+rx/2+w[4])
            norm=max(2*w[0],rx+w[0]+w[1],ry+w[0]+w[2],
                     2*rx+2*w[1],rx+ry+w[1]+w[2],2*ry+2*w[2],
                     3*rx+2*w[3],2*rx+ry+w[3]+w[4],rx+2*ry+2*w[4])
            assert norm==2*u
            n+=1
    counts['quadratic_norm_weighted_Gauss_cases']=n
    n=0
    for x,y,a,b,p,q,r,t in product([-1,0,1],repeat=8):
        u=x*p+y*q; v=x*r+y*t
        norm=lambda aa,uu: aa*aa-x*uu*uu
        aa=a*b+x*u*v; uu=a*v+b*u
        assert norm(aa,uu)==norm(a,u)*norm(b,v)
        n+=1
    counts['nonflat_norm_multiplicativity_cases']=n
    examples['nonflat_fiber']={'generic_degree':2,'origin_fiber_vector_space_dimension':3,
       'origin_canonical_weight':2,'origin_determinant':'T0^2',
       'proof_not_computational':'B=A plus (x,y)z, z^2=x; I/mI has basis x,y, and its product at the origin is zero.'}
    n=0
    weights=[]
    for d in range(1,7):
        for r in range(1,min(3,d)+1):
            for m in product(range(1,d+1),repeat=r):
                if sum(m)!=d: continue
                weights.append(m)
                for a in product(map(Q,[-1,0,2]),repeat=r):
                    for b in product(map(Q,[-1,0,2]),repeat=r):
                        assert abs(sum(mi*(ai-bi) for mi,ai,bi in zip(m,a,b)))<=d*max(abs(ai-bi) for ai,bi in zip(a,b))
                        n+=1
    counts['positive_integer_degree_Lipschitz_cases']=n
    n=0
    for m in range(1,7):
        for top in map(Q,[-2,-1,0,1,2]):
            for bounds in product(map(Q,[-2,-1,0,1,2]),repeat=m):
                # In a monic equation, a leading term cannot strictly dominate every other term.
                root_bound=max(bounds[i]/(m-i) for i in range(m))
                if top>root_bound:
                    assert m*top>max(bounds[i]+i*top for i in range(m))
                n+=1
    counts['monic_generator_bound_cases']=n
    n=0
    for j in range(1,13):
        eps=Q(1,4**j); eps2=eps/4
        B=Q(8,3)*eps; B2=B/4
        for err1,err2 in product([-1,0,1],repeat=2):
            assert err1*eps+B-(err2*eps2+B2)>0
            n+=1
    counts['decreasing_uniform_shift_cases']=n
    report={'status':'all finite diagnostics passed','arithmetic':'Python standard-library Fraction/integer',
            'counts':counts,'total_cases':sum(counts.values()),'examples':examples,
            'limits':'Finite grids and symbolic algebra examples only; no mathematical validation of infinite analytic arguments, EP, or the equation.'}
    (ROOT/'finite-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'counts':counts,'total_cases':report['total_cases']}))

if __name__=='__main__': main()
