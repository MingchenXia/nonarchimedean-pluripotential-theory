#!/usr/bin/env python3
"""Supplementary local frame tests; no general or independent verification."""
from fractions import Fraction as Q
from pathlib import Path
import json

def clean(a,p):
    return {m:c%p for m,c in a.items() if c%p}

def mul(a,b,p):
    out={}
    for m,c in a.items():
        for n,d in b.items():
            key=tuple(x+y for x,y in zip(m,n));out[key]=out.get(key,0)+c*d
    return clean(out,p)

def prod(items,p):
    out={(0,0,0):1}
    for item in items:out=mul(out,item,p)
    return out

def minimum(items):
    good=[x for x in items if x is not None]
    return min(good) if good else None

def scaled(x,a):return None if x is None else x*a
def shifted(x,a):return None if x is None else x+a

polynomials=[];norm_units=[]
for p in [2,3,5,7]:
    # T,z,w are independent variables; w represents a base frame factor.
    actual=prod([{(1,0,0):1,(0,1,1):-1,(0,0,1):-c} for c in range(p)],p)
    expected=clean({(p,0,0):1,(1,0,p-1):-1,(0,p,p):-1,(0,1,p):1},p)
    assert actual==expected
    polynomials.append({'type':'Artin-Schreier','characteristic':p,'identity':'prod_c(T-w(z+c))=T^p-w^(p-1)T-w^p(z^p-z)'})
    for a in range(p):
        actual=prod([{(0,1,0):1,(0,0,0):c-a} for c in range(p)],p)
        assert actual==clean({(0,p,0):1,(0,1,0):-1},p)
        norm_units.append({'characteristic':p,'a':a,'unit':'z-a on the full preimage of D(x)','norm':'x=z^p-z','all_group_factors_are_units_after_inverting_x':True})
for p in [2,3,5]:
    for e in [1,2]:
        d=p**e;actual=prod([{(1,0,0):1,(0,1,1):-1}]*d,p)
        assert actual==clean({(d,0,0):1,(0,d,d):-1},p)
        polynomials.append({'type':'purely-inseparable','characteristic':p,'degree':d,'identity':'(T-wz)^d=T^d-w^d z^d'})

gammas=[Q(-5),Q(-3,2),Q(-1,7),Q(0),Q(1,11),Q(2),Q(13,3),None]
deltas=[Q(-3,2),Q(0),Q(2,7)]
weights=[Q(-2),Q(1,3),Q(7,11)]
cases=0;actual_reference_frame_cases=0
for p in [2,3,5,7]:
    for gamma in gammas:
        original=minimum([Q(0),scaled(gamma,Q(1,p))])
        for delta in deltas:
            transformed=minimum([delta,shifted(scaled(gamma,Q(1,p)),delta)])
            assert transformed==shifted(original,delta)
            for m in [1,2,3,5]:
                for weight in weights:
                    original_value=(weight-original)/m
                    transformed_value=(weight-transformed)/m
                    assert transformed_value==original_value-delta/m
                    # A base frame unit at the analytic center has valuation 0.
                    if delta==0:
                        assert original_value==transformed_value
                        actual_reference_frame_cases+=1
                    cases+=1

record={'status':'PASS_LOCAL_FRAME_COVARIANCE','scope':'Exact local polynomial/weight covariance and selected norm units; not global norm-line or numerical-class verification.','scaled_orbit_and_inseparable_polynomials':polynomials,'norm_unit_examples':norm_units,'weighted_valuation_cases':cases,'actual_reference_frame_unit_cases':actual_reference_frame_cases,'nonzero_frame_factor_valuation_cases_are_formal_covariance_only':True,'global_line_gluing_independently_verified':False,'general_descent_theorem_verified':False,'new_independent_model_receipt':False,'active_manuscript_integration':False}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'polynomial_covariance_identities':len(polynomials),'norm_unit_identities':len(norm_units),'weighted_valuation_cases':cases,'actual_reference_frame_unit_cases':actual_reference_frame_cases,'result_path':str(out)},indent=2))
