#!/usr/bin/env python3
"""Author's bounded exact checks; never a continuum or source-proof verifier."""
from fractions import Fraction as Q
from math import comb, floor, ceil
import json
from pathlib import Path

def main():
    data=json.loads(Path('example-input.json').read_text())
    slopes=[Q(x) for x in data['slopes']]
    indices=[Q(x) for x in data['indices']]
    assertions=0; rows=[]
    for a in slopes:
        for c in indices:
            threshold=a*c
            exponent=floor(threshold)
            for k in range(8):
                integrable=2*k-2*threshold+1 > -1
                assert integrable == (k>=exponent)
                assertions+=1
            rows.append({'a':str(a),'c':str(c),'ideal_exponent':exponent,
                         'borderline':str(threshold-1),
                         'radial_rule':'k > a*c - 1'})
    binomial=[]
    for a in slopes:
        for m in data['degrees']:
            q=floor(a*m)
            assert 0<=q<=m
            for z in map(Q,data['real_points']):
                squared=sum(Q(comb(m-q,l))*z**(2*(q+l)) for l in range(m-q+1))
                expected=z**(2*q)*(1+z*z)**(m-q)
                assert squared==expected
                assertions+=1
            binomial.append({'a':str(a),'m':m,'q':q,'checked_points':data['real_points']})
        for j in range(1,9):
            m=2**j
            assert Q(floor(a*m),m)<=Q(floor(2*a*m),2*m)<=a
            assert 0<=a-Q(floor(a*m),m)<Q(1,m)
            assertions+=2
    # Direction test at lambda=1: the stalk on the left has exponent one;
    # every sampled smaller rational exponent has the unit ideal.
    smaller=[Q(x) for x in data['smaller_exponents']]
    assert floor(Q(1))==1 and all(0<x<1 and floor(x)==0 for x in smaller)
    assertions+=1
    # Finite checks of the threshold array's algebraic constraints.
    # Its continuum proof is the ceil inequality in the paper.
    for c in indices:
        for d in indices:
            n=lambda t:ceil(t)-1
            assert n(c+d)>=n(c)+n(d)
            if c<=d:assert n(c)<=n(d)
            assertions+=1+(c<=d)
    assert ceil(Q(1))-1==0
    assert all(ceil(Q(1)+x)-1>=1 for x in smaller)
    assertions+=2
    # Cantor lengths are not evaluated as underflowing floats.
    # The exact divergent lower-bound summands equal 3*2^(k-2).
    cantor=[]
    for k in range(1,13):
        term=Q(4**k-4**(k-1),2**k)
        assert term==3*Q(2)**(k-2)
        assertions+=1;cantor.append({'k':k,'layer_cake_lower_term':str(term)})
    result={'status':'PASS','exact_assertions':assertions,
            'integrability_rows':rows,'binomial_rows':binomial,
            'direction_counterexample':{'lambda':'1','left_ideal_exponent':1,
                                        'sampled_smaller_exponents':[str(x) for x in smaller],
                                        'sampled_right_ideal_exponent':0,
                                        'all_smaller_real_exponents_proved_in_paper':True},
            'cantor_terms':cantor,
            'scope':'Exhaustive for the finite supplied loops only. Does not prove regularization, envelopes, or the real continuum.'}
    Path('example-output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','exact_assertions','scope']}))

if __name__=='__main__':main()
