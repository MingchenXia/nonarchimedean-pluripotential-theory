#!/usr/bin/env python3
"""Exact finite coefficient diagnostics; not an analytic correctness test."""
from fractions import Fraction
from math import comb
import json
from pathlib import Path

cases = 0
for n in range(1, 17):
    for k in range(n+1):
        for a in range(k+1):
            def c(x, y):
                return comb(x, y) if 0 <= y <= x else 0
            lhs = Fraction(sum(c(j, a)*c(n-j, k-a) for j in range(n+1)), n+1)
            rhs = Fraction(comb(n, k), k+1)
            assert lhs == rhs, (n, k, a, lhs, rhs)
            cases += 1

# Independent n=2 expansion in the concentration example: three mixed terms.
# Order of coefficients is base S, base kappa, epsilon*base kappa_epsilon.
terms = [(0, 2, 2), (1, 1, 2), (2, 0, 2)]
average = [sum(Fraction(t[i], 3) for t in terms) for i in range(3)]
assert average == [1, 1, 2]
report = dict(status='passed', finite_domain='1 <= n <= 16, 0 <= a <= k <= n',
              vandermonde_cases=cases,
              concentration_coefficients=[str(x) for x in average],
              limitation='Exact finite arithmetic diagnostics only; the analytic proofs are in P15.1-argument.md.')
Path('coefficient-check.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
