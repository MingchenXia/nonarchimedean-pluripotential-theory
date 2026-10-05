#!/usr/bin/env python3
"""Rational finite checks of explicit research candidates, not receipts."""

from fractions import Fraction as Q
from math import comb
import json


def integrated_beta(k, j, a):
    # Expand (1-p)^(k-j), then integrate each polynomial term.
    integral = sum(Q((-1) ** ell * comb(k - j, ell), j + ell + 1)
                   * a ** (j + ell + 1) for ell in range(k - j + 1))
    return (k + 1) * comb(k, j) * integral


def binomial_tails(k, a):
    values = [Q(0)] * (k + 1)
    current = Q(0)
    for ell in range(k + 1, 0, -1):
        current += comb(k + 1, ell) * a ** ell * (1 - a) ** (k + 1 - ell)
        values[ell - 1] = current
    return values


beta_count = 0
min_count = 0
kernel_count = 0
det_count = 0
caps = [Q(1, 4), Q(1, 2), Q(3, 4)]
cap_samples = []
for k in range(1, 49):
    half = None
    for a in caps:
        values = binomial_tails(k, a)
        for j, value in enumerate(values):
            assert integrated_beta(k, j, a) == value
            assert 0 < value < 1
            if j < k: assert value > values[j + 1]
            beta_count += 1
        assert min(values) == a ** (k + 1)
        min_count += 1
        if a == Q(1, 2): half = values
        if k in [1, 8, 48]:
            cap_samples.append({'degree': k, 'cap_parameter': str(a),
                                'smallest_eigenvalue': str(values[-1])})
    assert half is not None
    for j in range(k + 1):
        if 2 * j <= k:
            assert half[j] >= Q(1, 2)
        else:
            assert half[j] >= Q(comb(k + 1, j + 1), 2 ** (k + 1))
            assert comb(k + 1, j + 1) >= comb(k, j)
    for p in [Q(0), Q(1, 8), Q(1, 4), Q(3, 8), Q(1, 2)]:
        summands = [(k + 1) * comb(k, j) * p ** j * (1 - p) ** (k - j)
                    / (2 * half[j]) for j in range(k + 1)]
        assert all(term <= k + 1 for term in summands)
        assert sum(summands) <= (k + 1) ** 2
        kernel_count += 1
    # Direct diagonal Gram determinant before and after the rank-one
    # squared evaluation at infinity, as well as the determinant lemma.
    diagonal = [2 * value for value in half]
    original = Q(1)
    modified = Q(1)
    for j, value in enumerate(diagonal):
        original *= value
        modified *= value + (k + 1 if j == k else 0)
    ratio = modified / original
    assert ratio == 1 + (k + 1) / diagonal[-1]
    assert ratio == 1 + (k + 1) * 2 ** k
    det_count += 1

# Degenerate cap endpoints are finite boundary checks, not admissible
# symbols in the source's nonzero/essential-infimum-zero category.
for k in range(1, 9):
    assert binomial_tails(k, Q(0)) == [Q(0)] * (k + 1)
    assert binomial_tails(k, Q(1)) == [Q(1)] * (k + 1)

dyadic = []
for n in range(1, 61):
    degree = 2 ** n
    exponents = [2 ** (n - i) for i in range(1, n + 1)]
    assert 1 + sum(exponents) == degree
    assert sum(Q(exp, degree) for exp in exponents) == 1 - Q(1, degree)
    mean = 1 - Q(1, 2) * (sum(Q(exp, degree) for exp in exponents) + Q(1, degree))
    assert mean == Q(1, 2)
    assert n <= 2 ** (n - 1)
    if n in [1, 8, 30, 60]:
        dyadic.append({'n': n, 'degree': degree, 'mean_log_norm_per_degree': str(mean),
                       'squared_weighted_norm_bound': degree,
                       'Toeplitz_upper_bound_prefactor': degree * (degree + 1)})

print(json.dumps({
    'date': '2026-10-05', 'all_checks_passed': True,
    'cap_degrees': 48, 'cap_parameters': [str(a) for a in caps],
    'independent_beta_integral_and_binomial_tail_equalities': beta_count,
    'exact_cap_minimum_checks': min_count,
    'half_cap_kernel_checks': kernel_count,
    'rank_one_Gram_determinant_checks': det_count,
    'degenerate_cap_endpoint_degree_cases': 8,
    'dyadic_section_degree_and_mean_checks': 60,
    'cap_samples': cap_samples, 'dyadic_samples': dyadic,
    'scope': 'Exact finite rational consistency checks. Infinite-density convergence, '
             'essential support, analytic norm gaps, envelope regularity and weak-BM '
             'asymptotics remain the research proofs in the audit. No independent '
             'production-model receipt or promoted source-counterexample verdict.',
}, indent=2))
