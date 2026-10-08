#!/usr/bin/env python3
"""Fresh exact bounded diagnostics; NOT a proof of general multiplicity claims."""
import json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent

def minimal(points):
    result=[]
    # Sorting makes it enough to test divisibility by previously retained points.
    for a,b in sorted(set(points)):
        if not any(c<=a and d<=b for c,d in result):
            result.append((a,b))
    return tuple(result)

def product(first,second):
    return minimal((a+c,b+d) for a,b in first for c,d in second)

def power(ideal,t):
    result=((0,0),)
    for _ in range(t):
        result=product(result,ideal)
    return result

def colength(ideal):
    pure_x=min(a for a,b in ideal if b==0)
    return sum(min(d for c,d in ideal if c<=a) for a in range(pure_x))

def sampled_multiplicity(ideal):
    # In a two-dimensional regular local monomial example, the stable second
    # finite difference is the coefficient convention. We report only this window.
    lengths=[colength(power(ideal,t)) for t in range(3,7)]
    second=[lengths[i+2]-2*lengths[i+1]+lengths[i] for i in range(2)]
    assert len(set(second))==1, {'ideal':ideal,'lengths':lengths}
    return second[0],lengths

ideals=[((a,0),(0,b)) for a in range(1,4) for b in range(1,4)]
cache={}
def em(ideal):
    ideal=minimal(ideal)
    if ideal not in cache:
        cache[ideal]=sampled_multiplicity(ideal)
    return cache[ideal][0]

def mixed(first,second):
    value=Fraction(em(product(first,second))-em(first)-em(second),2)
    assert value.denominator==1
    return int(value)

monotone=0
for small in ideals:
    for large in ideals:
        if all(any(c<=a and d<=b for c,d in large) for a,b in small):
            for test in ideals:
                assert mixed(small,test)>=mixed(large,test)
                monotone+=1
power_checks=0
for ideal in ideals:
    for test in ideals:
        for l in (1,2,3):
            assert mixed(power(ideal,l),test)==l*mixed(ideal,test)
            power_checks+=1
product_checks=0
for first in ideals:
    for second in ideals:
        for test in ideals:
            assert mixed(product(first,second),test)==mixed(first,test)+mixed(second,test)
            product_checks+=1

# A finite coefficient-sign witness is diagnostic of the rejected inference.
polynomial_values=[{'s':s,'t':t,'value':(s-t)**2} for s in range(1,8) for t in range(1,8)]
assert all(x['value']>=0 for x in polynomial_values)

# Explicit curve reference data: three abstract DVR branches and residue degrees.
branches=[{'a_order':2,'b_order':3,'j_order':5,'residue_degree':1},
          {'a_order':3,'b_order':1,'j_order':4,'residue_degree':2},
          {'a_order':1,'b_order':4,'j_order':2,'residue_degree':3}]
gauge=[]
for row in branches:
    mass_a=row['residue_degree']*row['a_order']
    d=Fraction(row['b_order'],row['a_order'])
    mass_b=row['residue_degree']*row['b_order']
    assert mass_a*d==mass_b
    assert Fraction(row['j_order'],row['b_order'])*mass_b==row['residue_degree']*row['j_order']
    gauge.append({'mass_a':mass_a,'d':str(d),'mass_b':mass_b})

output={'status':'PASS finite diagnostics only',
        'domain':{'ring_examples':'monomial primary ideals in k[[x,y]]','initial_ideals':'(x^a,y^b), 1<=a,b<=3','length_exponents':[3,4,5,6],'power_l':[1,2,3],'all_arithmetic':'exact integers/Fraction','characteristic_used_by_monomial_counts':'none','e_sampled_convention':'common second finite difference only in the stated observed window; no claim this establishes eventual polynomial stabilization'},
        'counts':{'inclusion_monotonicity':monotone,'power_law':power_checks,'product_law':product_checks,'computed_distinct_ideals':len(cache),'sign_witness_grid':len(polynomial_values),'curve_gauge_cases':len(gauge)},
        'sign_witness':{'polynomial':'(s-t)^2','st_coefficient':-2,'grid':polynomial_values},
        'curve_input':branches,'curve_output':gauge,
        'nilpotent_reference_witness':{'s_domain':[1,2,3,4,5,6],'reduced_lengths':[1,2,3,4,5,6],'square_zero_extension_lengths':[2,4,6,8,10,12]},
        'sample_length_sequences': [{'ideal':list(map(list,key)),'e_sampled':value[0],'lengths':value[1]} for key,value in list(cache.items())[:12]],
        'limitations':'No general rings, all-support functions, actual nets, geometric intersections, locality or source theorems are verified by these finite checks.'}
(HERE/'evidence/finite-diagnostics.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':output['status'],'counts':output['counts']}))
