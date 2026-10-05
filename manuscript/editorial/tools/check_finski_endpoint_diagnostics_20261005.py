#!/usr/bin/env python3
"""Exact finite diagnostics; not an analytic theorem or verifier receipt."""

from fractions import Fraction as Q
from math import comb, factorial
import json


def stirling_second(p, ell):
    if p == ell == 0:
        return 1
    if ell == 0 or ell > p:
        return 0
    row = [1]
    for degree in range(1, p + 1):
        row = [0] + [
            (row[j - 1] if j - 1 < len(row) else 0)
            + j * (row[j] if j < len(row) else 0)
            for j in range(1, degree + 1)
        ]
    return row[ell]


def power_sum(k, p):
    return sum(
        stirling_second(p, ell) * factorial(ell)
        * (comb(k + 1, ell + 1) if ell + 1 <= k + 1 else 0)
        for ell in range(p + 1)
    )


def uniform_shift_moment(p, c):
    return sum(Q(comb(p, j), j + 1) * (-c) ** (p - j)
               for j in range(p + 1))


degrees = []
moment_count = 0
shift_count = 0
shifts = [Q(-3, 2), Q(0), Q(1, 3), Q(2)]
for k in range(1, 241):
    jumps = [Q(j, k) for j in range(k + 1)]
    moments = [sum(x ** p for x in jumps) / (k + 1) for p in range(9)]
    for p, value in enumerate(moments):
        assert value == Q(power_sum(k, p), (k + 1) * k ** p)
        assert abs(value - Q(1, p + 1)) <= Q(1, k + 1)
        moment_count += 1
    assert moments[1] == Q(1, 2)
    assert moments[2] == Q(2 * k + 1, 6 * k)
    variance = moments[2] - moments[1] ** 2
    assert variance == Q(k + 2, 12 * k)
    for c in shifts:
        for p in range(6):
            actual = sum((x - c) ** p for x in jumps) / (k + 1)
            via_binomial = sum(comb(p, j) * (-c) ** (p - j) * moments[j]
                               for j in range(p + 1))
            assert actual == via_binomial
            shift_count += 1
        assert uniform_shift_moment(1, c) == Q(1, 2) - c
        assert (1 - c) - uniform_shift_moment(1, c) == Q(1, 2)
    degrees.append({'degree': k, 'mean': str(moments[1]),
                    'second_moment': str(moments[2]), 'variance': str(variance)})

# Rational finite differences evaluate the actual max-function corner.
corner_cases = 0
energy_cases = 0
for t in [Q(0), Q(1, 7), Q(1, 2), Q(1), Q(5, 3)]:
    r = -t
    for step in [Q(1, 100), Q(1, 37), Q(1, 3)]:
        for c in shifts:
            value = lambda rr, tt: max(Q(0), rr + tt) - c * tt
            assert (value(r, t + step) - value(r, t)) / step == 1 - c
            corner_cases += 1
    for c in shifts:
        initial_circle_difference = max(Q(0), t) - c * t
        moving_circle_difference = -c * t - max(Q(0), -t)
        energy = (initial_circle_difference + moving_circle_difference) / 2
        assert energy == t * uniform_shift_moment(1, c)
        energy_cases += 1

# Unit balls for diagonal norms 2^{-a_j}|z_j| have real volume
# ratio 2^{2 sum a_j}; ordinary log norm ratios are a_j log 2.
volume_cases = []
for dimension in range(1, 17):
    exponents = list(range(1, dimension + 1))
    dp1_log2_coefficient = Q(sum(exponents), dimension)
    real_log_volume_log2_coefficient = 2 * sum(exponents)
    corrected = Q(real_log_volume_log2_coefficient, 2 * dimension)
    literal = Q(real_log_volume_log2_coefficient, dimension)
    assert corrected == dp1_log2_coefficient
    assert literal == 2 * dp1_log2_coefficient
    volume_cases.append({'complex_dimension': dimension,
                         'ordinary_norm_log2_coefficient': str(corrected),
                         'literal_unhalved_volume_coefficient': str(literal)})

print(json.dumps({
    'date': '2026-10-05',
    'degree_cases': len(degrees),
    'powers': list(range(9)),
    'independent_power_sum_equalities': moment_count,
    'finite_moment_error_bounds_checked': moment_count,
    'character_shift_moment_equalities': shift_count,
    'corner_right_difference_cases': corner_cases,
    'dimension_one_energy_cases': energy_cases,
    'complex_ball_real_volume_cases': len(volume_cases),
    'all_checks_passed': True,
    'unshifted_limiting_candidate_means': {'jumping_distribution': '1/2',
                                         'literal_endpoint_pushforward': '1'},
    'sample_degrees': [degrees[i] for i in [0, 1, 9, 99, 239]],
    'volume_samples': [volume_cases[0], volume_cases[-1]],
    'scope': 'Exact finite consistency checks only. Analytic limits, curvature measures, '
             'weak-geodesic construction and determining-measure candidate are proved '
             'in research prose, not certified by this code. No independent model receipt; '
             'no source theorem counterexample promoted to the book.',
}, indent=2))
