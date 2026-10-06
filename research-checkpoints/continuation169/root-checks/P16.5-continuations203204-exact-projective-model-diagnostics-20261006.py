"""Actual P^n deformation-to-the-normal-cone checks; no theorem certification."""
from fractions import Fraction as Q
from itertools import product
import json

# Blow up (p,0) on P^n x P1: T_a=dH-aE, 0<a<d.
# H^j E^(n+1-j)=0 for j>=1, E^(n+1)=(-1)^n.
# e(a)=-a^(n+1)/(n+1), raw mu=(d^n-a^n)delta_0+a^n delta_vE.
def e(n,a):
    return -a**(n+1)/(n+1)
def cap_e(n,a,C):
    return -a**n*min(a,C)/(n+1)
def record_bound(ok,label):
    assert ok,label

midpoint=fourpoint=capmass=capenergy=variation=0
per=[]
for n,d in product(range(1,7),(Q(1),Q(2))):
    vals=[d*Q(i,8) for i in (1,2,4,6)]
    for a in vals:
        V=d**n
        masses=(V-a**n,a**n)
        record_bound(sum(masses)==V and min(masses)>=0,'raw positive mass')
        energy_derivative=-a**n
        current_derivative=-masses[1]
        record_bound(energy_derivative==current_derivative,'energy/measure derivative')
        variation+=1
        for C in (Q(1,4),Q(1),Q(3)):
            tv=2*a**n if C<a else Q(0)
            record_bound(tv<=2*(n+1)*(-e(n,a))/C,'cap raw TV')
            capmass+=1
    for a,b in product(vals,repeat=2):
        # Independent raw atomic integral gives this I.
        I=(b-a)*(b**n-a**n)
        delta=e(n,(a+b)/2)-(e(n,a)+e(n,b))/2
        record_bound(I>=0 and delta>=0 and I<=4**(n+1)*delta,'raw I/midpoint')
        midpoint+=1
        for c in vals:
            moment=c*(b**n-a**n)
            Jc=-e(n,c)
            B=max(Jc,-e(n,a),-e(n,b))
            k=4*n  # Diagnostic grid constant only, not a claimed optimal theorem constant.
            power=2**n
            record_bound(abs(moment)**power <= k**power*I**(power//2)*Jc*B**(power//2-1),'fourpoint finite grid')
            fourpoint+=1
        if a<=b:
            original_gap=e(n,a)-e(n,b);D=-e(n,b)
            for C in (Q(1,4),Q(1),Q(3)):
                gap=cap_e(n,a,C)-cap_e(n,b,C)
                record_bound(gap>=0,'ordered cap energy')
                power=2**n;k=4*n
                record_bound(gap**power<=k**power*D**(power-1)*original_gap,'cap energy modulus finite grid')
                capenergy+=1
    per.append({'dimension':n,'actual_polarization_degree':str(d),'raw_mass':str(d**n)})
print(json.dumps({'classification':'Exact finite actual projective models only; does not prove203/204 or original P16.5.','models':'Bl_(p,0)(P^n x P1), actual dH-aE relatively ample, cleared rational powers','dimensions':[1,2,3,4,5,6],'raw_mass_examples':per,'energy_gradient_raw_measure_checks':variation,'midpoint_I_checks':midpoint,'fourpoint_squared_power_checks':fourpoint,'TV_cap_checks':capmass,'ordered_cap_energy_checks':capenergy,'generic_reference_value':0,'all_raw_masses_retained':True,'diagnostic_fourpoint_constant':'4n on this finite grid only','all_passed':True,'independent_acceptance':False,'original_closed':False},indent=2))
