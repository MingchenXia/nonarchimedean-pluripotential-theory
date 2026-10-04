#!/usr/bin/env python3
"""Exact finite boundary checks for an unadmitted descent candidate.

These calculations do not verify a general descent theorem, line gluing,
or an independent production-model receipt.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def clean(poly, p):
    return {m: a % p for m, a in poly.items() if a % p}


def multiply(a, b, p):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = i + k, j + l
            out[key] = out.get(key, 0) + x * y
    return clean(out, p)


def product(factors, p):
    ans = {(0, 0): 1}
    for factor in factors:
        ans = multiply(ans, factor, p)
    return ans


def finite_min(values):
    good = [x for x in values if x is not None]
    return min(good) if good else None


def finite_max(values):
    good = [x for x in values if x is not None]
    return max(good) if good else None


def scaled(x, a):
    return None if x is None else x * a


def weighted_log(weight, valuation):
    return None if valuation is None else weight - valuation


def show(x):
    return '+infinity' if x is None else str(x)


valuation_samples = [Q(-5), Q(-3, 2), Q(-1, 7), Q(0), Q(1, 11), Q(2), Q(13, 3), None]
artin_schreier = []
for p in [2, 3, 5, 7]:
    # Product over the actual additive Galois group in F_p[z,T].
    calculated = product([{(1, 0): 1, (0, 1): -1, (0, 0): -c} for c in range(p)], p)
    expected = clean({(p, 0): 1, (1, 0): -1, (0, p): -1, (0, 1): 1}, p)
    assert calculated == expected  # T^p-T-(z^p-z)
    checks = []
    for gamma in valuation_samples:
        if gamma is None:
            roots = [None] + [Q(0)] * (p - 1)
        elif gamma > 0:
            roots = [gamma] + [Q(0)] * (p - 1)
        elif gamma < 0:
            roots = [gamma / p] * p
        else:
            roots = [Q(0)] * p
        spectral = finite_min([Q(0), scaled(gamma, Q(1, p))])
        assert finite_min(roots) == spectral
        summed = None if any(x is None for x in roots) else sum(roots, Q(0))
        average = scaled(summed, Q(1, p))
        assert average == scaled(gamma, Q(1, p))
        checks.append({'base_valuation': show(gamma), 'root_minimum': show(spectral), 'average_root_valuation': show(average)})
    artin_schreier.append({'characteristic': p, 'degree': p, 'orbit_polynomial': 'T^p-T-(z^p-z)', 'exact_polynomial_identity': True, 'valuation_checks': checks})

purely_inseparable = []
for p in [2, 3, 5]:
    for e in [1, 2]:
        d = p ** e
        calculated = product([{(1, 0): 1, (0, 1): -1}] * d, p)
        expected = clean({(d, 0): 1, (0, d): -1}, p)
        assert calculated == expected  # (T-z)^d=T^d-z^d
        for gamma in valuation_samples:
            assert scaled(scaled(gamma, d), Q(1, d)) == gamma
        purely_inseparable.append({'characteristic': p, 'degree': d, 'norm_polynomial': 'T^d-z^d', 'exact_polynomial_identity': True, 'valuation_checks': len(valuation_samples), 'no_inverse_of_degree_in_field': True})

cone_polynomials = []
for p in [3, 5, 7]:
    calculated = multiply({(1, 0): 1, (0, 1): 1}, {(1, 0): 1, (0, 1): -1}, p)
    assert calculated == clean({(2, 0): 1, (0, 2): -1}, p)
    cone_polynomials.append({'characteristic': p, 'section': 'S+U', 'conjugate_product': 'S^2-U^2', 'base_section': 'X^2-Z', 'weighted_degree_on_base': 2, 'target_rational_line': 'H/2'})
p = 2
calculated = multiply({(1, 0): 1, (0, 1): 1}, {(1, 0): 1, (0, 1): 1}, p)
assert calculated == clean({(2, 0): 1, (0, 2): 1}, p)
cone_polynomials.append({'characteristic': 2, 'section': 'S+U', 'purely_inseparable_norm': 'S^2+U^2', 'base_section': 'X^2+Z', 'weighted_degree_on_base': 2, 'target_rational_line': 'H/2'})

projective_values = [
    (Q(0), Q(1), Q(2)), (Q(2), Q(0), Q(1)), (Q(1), Q(2), Q(0)),
    (Q(0), Q(0), Q(0)), (None, None, Q(0)),
    (None, Q(0), None), (Q(0), None, None),
    (Q(0), Q(3, 7), Q(11, 5)), (None, Q(0), Q(13, 11)),
]
weights = [(Q(-2), Q(-1), Q(0)), (Q(1, 3), Q(-2, 5), Q(7, 11)), (Q(0), Q(0), Q(0))]
cone_values = []
for values in projective_values:
    for lambdas in weights:
        upstairs = finite_max([weighted_log(l, v) for l, v in zip(lambdas, values)])
        # Base sections X^2,Y^2,Z of H pull back to S^2,T^2,U^2.
        downstairs = scaled(finite_max([weighted_log(2*l, scaled(v, 2)) for l, v in zip(lambdas, values)]), Q(1, 2))
        assert upstairs == downstairs
        cone_values.append({'source_valuations': [show(x) for x in values], 'weights': [str(x) for x in lambdas], 'equal_log_value': str(upstairs), 'proper_support': any(x is None for x in values)})

# On the source chart U!=0, the cone vertex pulls back to
# k[a,b]/(a^2,ab,b^2). Its length is three, while generic degree is two.
fiber_ideal = [(2, 0), (1, 1), (0, 2)]
fiber_basis = [(i, j) for i in range(4) for j in range(4)
               if not any(i >= a and j >= b for a, b in fiber_ideal)]
assert fiber_basis == [(0, 0), (0, 1), (1, 0)]
assert all(i+j <= 1 for i,j in fiber_basis)
cone_fiber = {'local_quotient': 'k[a,b]/(a^2,ab,b^2)', 'monomial_basis': ['1', 'b', 'a'],
              'fiber_length': len(fiber_basis), 'generic_degree': 2,
              'fiber_length_differs_from_generic_degree': True,
              'underlying_vertex_lifts': 1,
              'metric_test_uses_no_distinct_point_average': True}

cyclic_decreasing = []
for d in [2, 3, 4, 5, 7]:
    for s in [Q(0), Q(1, 11), Q(5, 2), Q(20), None]:
        source, base = [], []
        for m in [1, 2, 3, 5, 8]:
            a = finite_max([None if s is None else -s, Q(-m)])
            b = scaled(finite_max([None if s is None else -d*s, Q(-d*m)]), Q(1, d))
            assert a == b
            source.append(a); base.append(b)
        assert all(source[i+1] <= source[i] for i in range(len(source)-1))
        cyclic_decreasing.append({'degree': d, 'source_zero_branch_valuation': show(s), 'equal_decreasing_values': [str(x) for x in source], 'endpoint_limit_is_negative_infinity': s is None, 'target_rational_line': 'O(1)/d'})

record = {
    'status': 'PASS_FINITE_BOUNDARY_CALCULATIONS',
    'scope': 'Exact finite polynomial, valuation, rational-weight and proper-support tests for an unadmitted candidate.',
    'artin_schreier': artin_schreier,
    'purely_inseparable': purely_inseparable,
    'nonflat_quadric_cone_polynomials': cone_polynomials,
    'nonflat_quadric_cone_metric_values': cone_values,
    'nonflat_quadric_cone_vertex_fiber': cone_fiber,
    'cyclic_decreasing_section_values': cyclic_decreasing,
    'general_descent_theorem_verified': False,
    'norm_line_gluing_verified_independently': False,
    'numerical_class_map_verified_independently': False,
    'all_arbitrary_support_strata_verified': False,
    'new_independent_production_model_receipt': False,
    'active_manuscript_integration': False,
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': record['status'], 'exact_polynomial_identities': len(artin_schreier)+len(purely_inseparable)+len(cone_polynomials), 'spectral_and_average_valuation_cases': len(artin_schreier)*len(valuation_samples), 'purely_inseparable_valuation_cases': len(purely_inseparable)*len(valuation_samples), 'cone_weight_and_support_cases': len(cone_values), 'cyclic_decreasing_cases': len(cyclic_decreasing), 'result_path': str(target)}, indent=2))
