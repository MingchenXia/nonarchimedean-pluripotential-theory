"""Exact finite P1 checks, not a proof or acceptance of either manuscript."""
from fractions import Fraction as Q
from itertools import product
import json

# Actual P1 O(1) FS model: xi(t)=g-min(a*t,b), 0<a<=1.
# Raw measure (1-a)delta_0+a delta_(b/a), E=g-a*b/2.
# Rational denominators can be cleared in actual section systems.
def value(p,t):
    a,b,g=p
    return g-min(a*t,b)
def measure(p):
    a,b,g=p
    return {Q(0):1-a,b/a:a}
def integral(p,mu):
    return sum(value(p,t)*mass for t,mass in mu.items())
def energy(p):
    a,b,g=p
    return g-a*b/2
def J(p):
    return p[2]-energy(p)
def signed_difference(mu,nu):
    return {t:mu.get(t,Q(0))-nu.get(t,Q(0)) for t in set(mu)|set(nu)}
def ordered(x,y):
    a,b,g=x;c,d,h=y
    return all(value(x,t)>=value(y,t) for t in (Q(0),b/a,d/c,max(b/a,d/c)+1))
def midpoint_energy(x,y):
    a,b,g=x;c,d,h=y
    nodes=sorted({Q(0),b/a,d/c})
    norm=Q(0)
    for left,right in zip(nodes,nodes[1:]):
        t=(left+right)/2
        slope=((a if t<b/a else 0)+(c if t<d/c else 0))/2
        norm+=(right-left)*slope*slope
    return (g+h)/2-norm/2
def cap(p,C):
    a,b,g=p
    if g<=-C:return (-C,{Q(0):Q(1)})
    height=min(b,C+g)
    return (g-a*height/2,{Q(0):1-a,height/a:a})

potentials=list(product((Q(1,4),Q(1,2),Q(1)),(Q(1,3),Q(1),Q(3)),(Q(-1,2),Q(0))))
fourpoint=midpoints=caps=capgaps=0
for x,y in product(potentials,repeat=2):
    mx,my=measure(x),measure(y)
    I=integral(x,my)-integral(y,my)-integral(x,mx)+integral(y,mx)
    assert I>=0
    delta=midpoint_energy(x,y)-(energy(x)+energy(y))/2
    assert delta==I/8
    midpoints+=1
    diff=signed_difference(mx,my)
    for z in potentials:
        moment=integral(z,diff)
        assert moment*moment<=2*I*J(z)
        fourpoint+=1
    for C in (Q(1,4),Q(1),Q(4)):
        ex,mcx=cap(x,C);ey,mcy=cap(y,C)
        if x==y:
            tv=sum(abs(mass) for mass in signed_difference(mx,mcx).values())
            assert tv<=4*(-energy(x))/C
            caps+=1
        if ordered(x,y):
            original_gap=energy(x)-energy(y)
            cap_gap=ex-ey
            assert original_gap>=0 and cap_gap>=0
            generic_error=abs(x[2]-y[2])
            remainder=max(cap_gap-generic_error,Q(0))
            D=max(-energy(x),-energy(y))
            assert remainder*remainder<=8*D*original_gap
            capgaps+=1
print(json.dumps({'classification':'Exact finite P1 diagnostics only; no all-dimensional proof or original closure.','actual_bundle':'P1 O(1), rational FS weights with cleared denominators','potentials':len(potentials),'raw_fourpoint_squared_checks':fourpoint,'exact_midpoint_I_over_8_checks':midpoints,'raw_TV_truncation_checks':caps,'ordered_cap_gap_checks':capgaps,'generic_constants_retained':True,'coefficient_formula':'(int z d(mu_x-mu_y))^2 <= 2 I(x,y) J(z)','n1_cap_formula':'TV(mu_x,mu_cap)<=4 B(x)/C; ordered cap energy gap minus generic error squared<=8 D original energy gap','all_passed':True,'independent_acceptance':False,'original_closed':False},indent=2))
