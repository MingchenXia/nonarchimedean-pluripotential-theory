#!/usr/bin/env python3
"""Exact finite witnesses for the Chapter 5 face/localization repair.

These checks support the examples; the general contraction theorem is proved
in the chapter. SymPy is used only for exact polynomial arithmetic.
"""
from fractions import Fraction
from itertools import product
import json
import sympy as sp

w, z = sp.symbols('w z')
assert sp.expand(w + (z - w)) == z
# At the face v(z)=1, v(w)=0, the two terms each have value zero,
# while their sum has value one. The old arbitrary-coefficient minimum
# assertion cannot follow from the ultrametric inequality alone.
for n in range(1, 11):
    partial = sum(w**i for i in range(n))
    assert sp.cancel(1 / (1 - w) - partial - w**n / (1 - w)) == 0
    # This nonzero rational function of w has z-adic value zero.

weights = [
    (Fraction(1),),
    (Fraction(2, 3),),
    (Fraction(1), Fraction(1)),
    (Fraction(1), Fraction(2)),
    (Fraction(1, 2), Fraction(3, 2)),
    (Fraction(2, 3), Fraction(1)),
]
thresholds = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3)]
quotients = 0
injective_multipliers = 0
excluded_multipliers = 0
for alpha in weights:
    for threshold in thresholds:
        basis = [
            beta
            for beta in product(*(range(int(threshold / a) + 1) for a in alpha))
            if sum(a * b for a, b in zip(alpha, beta)) < threshold
        ]
        basis.sort(key=lambda beta: (sum(beta), beta))
        indices = {beta: i for i, beta in enumerate(basis)}
        size = len(basis)
        assert size > 0
        shifts = [tuple(int(j == i) for j in range(len(alpha))) for i in range(len(alpha))]
        for constant in (w, 1 + w):
            matrix = sp.zeros(size)
            for column, beta in enumerate(basis):
                matrix[column, column] = constant
                for i, shift in enumerate(shifts):
                    target = tuple(a + b for a, b in zip(beta, shift))
                    if target in indices:
                        matrix[indices[target], column] += w**i
            assert matrix.is_lower
            assert sp.expand(matrix.det() - constant**size) == 0
            assert matrix.det() != 0
            injective_multipliers += 1
        # A positive-weight variable lies in the localized prime; its
        # multiplier is nilpotent on these finite quotients and is excluded
        # from the saturation argument.
        nilpotent = sp.zeros(size)
        for column, beta in enumerate(basis):
            target = tuple(a + b for a, b in zip(beta, shifts[0]))
            if target in indices:
                nilpotent[indices[target], column] = 1
        assert nilpotent.det() == 0
        excluded_multipliers += 1
        quotients += 1

print(json.dumps({
    'status': 'PASS',
    'finite_weighted_monomial_quotients': quotients,
    'exact_injective_multiplier_checks': injective_multipliers,
    'excluded_positive_weight_multiplier_checks': excluded_multipliers,
    'zero_weight_truncation_witnesses': 10,
    'cancellation_witness': 'w + (z - w) = z; minimum 0, sum value 1',
    'scope': 'finite exact examples; not a substitute for the general proof or an independent verifier verdict',
}, indent=2))
