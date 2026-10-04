"""Small exact diagnostics; these do not verify the analytic theorem.

Rerun: python diagnostics/finite_checks.py > diagnostics/output.json
"""
from fractions import Fraction as F
from itertools import product
from math import prod
import json

# Possible norms of two elements differing by an error of norm < bound:
# unequal norms must both be < bound; otherwise the norms must coincide.
norms = [F(0), F(1,4), F(1,2), F(1), F(2), F(4)]
def allowed(a, b, bound):
    return a == b or max(a,b) < bound

cases = equality_cases = failures = 0
for radii in product([F(1,2), F(1), F(2)], repeat=2):
    for g, f1, f2 in product(norms, repeat=3):
        if max(g,f1/radii[0],f2/radii[1]) < 1:
            continue
        opts = [[b for b in norms if allowed(a,b,bound)]
                for a,bound in [(g,F(1)),(f1,radii[0]),(f2,radii[1])]]
        for g0, f10, f20 in product(*opts):
            cases += 1
            fs = (f1,f2); fs0 = (f10,f20)
            weak = all(f <= r*g for f,r in zip(fs,radii))
            strict = all(f < r*g for f,r in zip(fs,radii))
            weak0 = all(f <= r*g0 for f,r in zip(fs0,radii))
            strict0 = all(f < r*g0 for f,r in zip(fs0,radii))
            eq = tuple(f == r*g for f,r in zip(fs,radii))
            eq0 = tuple(f == r*g0 for f,r in zip(fs0,radii))
            if weak and any(eq):
                equality_cases += 1
            failures += int((weak,strict) != (weak0,strict0) or (weak and eq != eq0))
assert failures == 0

# Full complementary exterior basis: d't and d''t wedge annihilate every
# basis component except the one missing the transverse index in both.
exterior_components = 0
def exterior_wedge(left, right):
    joined = list(left)+list(right)
    if len(set(joined)) != len(joined):
        return 0, ()
    inversions = sum(joined[i] > joined[j] for i in range(len(joined)) for j in range(i+1,len(joined)))
    return (-1)**inversions, tuple(sorted(joined))

for n in range(1,21):
    survivors = []
    for omitted_prime, omitted_double in product(range(n),repeat=2):
        exterior_components += 1
        prime = [i for i in range(n) if i != omitted_prime]
        double = [i for i in range(n) if i != omitted_double]
        prime_sign, prime_top = exterior_wedge([n-1],prime)
        double_sign, double_top = exterior_wedge([n-1],double)
        if prime_sign*double_sign:
            assert prime_top == double_top == tuple(range(n))
            survivors.append((omitted_prime,omitted_double))
    assert len(survivors) == 1
    assert survivors[0] == (n-1,n-1)

# Actual unreduced characteristic-two algebra
# F2(t)[s,u]/(s^2-t,u^3), a finite E[u]/u^3 with E=F2(t)(s).
# Sparse polynomials encode t^i s^j u^k and use the actual relations.
def add(a,b):
    return a.symmetric_difference(b)
def mul(a,b):
    c = set()
    for i,j,k in a:
        for i1,j1,k1 in b:
            kk = k+k1
            if kk >= 3:
                continue
            jj = j+j1
            term = (i+i1+jj//2,jj%2,kk)
            if term in c: c.remove(term)
            else: c.add(term)
    return c
def shift_u(a,k):
    return {(i,j,kk+k) for i,j,kk in a if kk+k < 3}
one = {(0,0,0)}
monomials = [(i,j,0) for i,j in product(range(2),repeat=2)]
coeffs = [{m for idx,m in enumerate(monomials) if mask & (1<<idx)} for mask in range(16)]
unit_checks = 0
for a,b in product(coeffs,repeat=2):
    f = add(add(one,shift_u(a,1)),shift_u(b,2))
    inverse = add(add(one,shift_u(a,1)),shift_u(add(b,mul(a,a)),2))
    assert mul(f,inverse) == one
    assert all(j == 0 for i,j,k in mul(f,f))
    assert all(j == 0 for i,j,k in mul(inverse,inverse))
    unit_checks += 1

output = {
    'kind':'exact finite diagnostics, not mathematical verification',
    'rational_norm_cases':cases,
    'valid_domain_equality_cases':equality_cases,
    'rational_weak_strict_equality_failures':failures,
    'exterior_dimensions':list(range(1,21)),
    'exterior_components':exterior_components,
    'one_survivor_per_dimension':True,
    'unreduced_unit_inverse_frobenius_checks':unit_checks,
    'actual_algebra':'F2(t)[s,u]/(s^2-t,u^3); constant-one units with a,b in span{1,t,s,ts}',
    'actual_E_artinian_length':3,
    'actual_K_vector_space_dimension':6,
    'inseparable_local_tensor_basis_dimensions':[{'q':q,'basis_count':len(list(product(range(q),range(3)))),'length':3*q} for q in (2,4,8)],
    'formal_verification':False,
}
print(json.dumps(output,indent=2))
