#!/usr/bin/env python3
"""Small exact checks for the direct lemmas. They are not mathematical verification."""
from fractions import Fraction as Q
from itertools import product
import json

xi = (Q(1), Q(1))
zeta = (Q(1), Q(2))
weights = [(1, 0), (0, 1), (2, 1), (1, 3)]
lam = [Q(-1), Q(0), Q(-2), Q(-3)]
def degree(a, eta):
    return sum(Q(x)*y for x, y in zip(a, eta))
def fs(v, eta, shift=None):
    terms = []
    for a, c in zip(weights, lam):
        if any(x is None and k for x, k in zip(v, a)):
            continue
        valuation = sum(Q(k)*x for k, x in zip(a, v) if k)
        if shift is not None:
            valuation += degree(a, zeta)*shift
        terms.append((-valuation+c)/degree(a, eta))
    return max(terms)

l = min(degree(a,zeta)/degree(a,xi) for a in [(1,0),(0,1)])
u = max(degree(a,zeta)/degree(a,xi) for a in [(1,0),(0,1)])
points = [(Q(a),Q(b)) for a,b in product(range(-3,4),repeat=2)]
points += [(None,Q(b)) for b in range(-3,4)] + [(Q(a),None) for a in range(-3,4)]
root_checks = slope_checks = sandwich_checks = 0
for v in points:
    a = fs(v,xi)
    root = fs(v,zeta)
    assert fs(v,xi,shift=root) == 0
    root_checks += 1
    assert min(a/l,a/u) <= root <= max(a/l,a/u)
    sandwich_checks += 1
    for t in [Q(0),Q(1,3),Q(2),Q(7,2)]:
        assert a-u*t <= fs(v,xi,shift=t) <= a-l*t
        slope_checks += 1

filtration_checks = 0
examples = []
for m in range(1,33):
    mons = [(a,b) for a in range(m+1) for b in range(m+1-a)]
    W = len(mons)
    A = sum(a+b for a,b in mons)
    assert W == (m+1)*(m+2)//2
    assert A == m*(m+1)*(m+2)//3
    assert Q(A,m*W) == Q(2,3)
    filtration_checks += 1
    if m in [1,2,8,32]:
        examples.append({'m':m,'dimension':W,'jump_sum':A,'S_m':str(Q(A,m*W))})

print(json.dumps({'scope':'Exact finite diagnostic checks only; no exhaustive infinite-domain or analytic verification.',
    'nonproportional_fields': {'xi':['1','1'],'zeta':['1','2']},
    'slope_constants': {'l':str(l),'u':str(u)},
    'root_checks':root_checks,'slope_checks':slope_checks,'sandwich_checks':sandwich_checks,
    'filtration_checks':filtration_checks,'filtration_examples':examples,
    'normalization_diagnostic': {'S_degree_filtration_A2':'2/3','E_constant_shift_1_from_probability_formula':'1','printed_E_equals_S_consistent':False}},indent=2))
