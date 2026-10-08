"""Owned exact finite diagnostics; no supplied executable is used."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def mul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i+k, j+l)
            out[key] = out.get(key, 0) + x*y
    return {k:v for k,v in out.items() if v}

def add(*terms):
    out = {}
    for sign, a in terms:
        for key, value in a.items():
            out[key] = out.get(key, 0) + sign*value
    return {k:v for k,v in out.items() if v}

def main():
    # Polynomial variables T,Z; exact coefficient dictionaries.
    t, z = {(1,0):1}, {(0,1):1}
    s = add((1,mul(t,t)), (-1,t))
    v, j = mul(t,s), mul(t,z)
    checks = {
        'V^2-SV-S^3': add((1,mul(v,v)), (-1,mul(s,v)), (-1,mul(mul(s,s),s))),
        'J^2-ZJ-SZ^2': add((1,mul(j,j)), (-1,mul(z,j)), (-1,mul(s,mul(z,z)))),
        'VZ-SJ': add((1,mul(v,z)), (-1,mul(s,j))),
    }
    assert all(not value for value in checks.values())
    n = 32
    coeff = [Fraction((-1)**k * comb(2*k,k), 4**k) for k in range(n+1)]
    assert all(c.denominator % 3 != 0 for c in coeff)
    square = [sum((coeff[k]*coeff[d-k] for k in range(d+1)), Fraction()) for d in range(n+1)]
    formal = [square[0]] + [square[d] + square[d-1] for d in range(1,n+1)]
    assert formal == [Fraction(1)] + [Fraction(0)]*n
    data = {'polynomial_relations_checked': list(checks), 'all_residuals_zero': True,
            'binomial_coefficients': n+1, '3_adic_integrality_through_degree': n,
            '(1+t)B(t)^2_identity_checked_through_degree': n,
            'scope': 'Exact finite diagnostics. Does not prove the infinite series identity, analytic convergence, geometry, or envelope positivity.'}
    (ROOT/'evidence').mkdir(exist_ok=True)
    (ROOT/'evidence'/'diagnostics.json').write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data))

if __name__ == '__main__':
    main()
