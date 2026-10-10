"""Exact check of BHM arXiv:2010.06088v5 Example 3.7 over Q.

Reconstruct the augmented Chow quotient, the named canonical complements,
and the Lefschetz pairing for the all-one positive class. This checks a
named primary-source example; it admits no new general result or model receipt.
"""

from fractions import Fraction as Q
from itertools import combinations_with_replacement
from pathlib import Path
import json


def rref(rows, width):
    a = [[Q(x) for x in row] for row in rows]
    pivots = []
    k = 0
    for j in range(width):
        h = next((h for h in range(k, len(a)) if a[h][j]), None)
        if h is None:
            continue
        a[k], a[h] = a[h], a[k]
        c = a[k][j]
        a[k] = [x / c for x in a[k]]
        for h in range(len(a)):
            if h != k and a[h][j]:
                c = a[h][j]
                a[h] = [x - c * y for x, y in zip(a[h], a[k])]
        pivots.append(j)
        k += 1
        if k == len(a):
            break
    return a[:k], pivots


def kernel(rows, width):
    reduced, pivots = rref(rows, width)
    result = []
    for j in range(width):
        if j not in pivots:
            row = [Q(int(i == j)) for i in range(width)]
            for k, i in enumerate(pivots):
                row[i] = -reduced[k][j]
            result.append(row)
    return result


def determinant(rows):
    a = [[Q(x) for x in row] for row in rows]
    value = Q(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            value = -value
        c = a[j][j]
        value *= c
        for k in range(j + 1, len(a)):
            scale = a[k][j] / c
            for h in range(j + 1, len(a)):
                a[k][h] -= scale * a[j][h]
    return value


flats = [f for f in range(16) if f.bit_count() < 3]
assert len(flats) == 11


def comparable(f, g):
    return f & g in (f, g)


def allowed(monomial):
    return all(comparable(flats[i], flats[j]) for i in monomial for j in monomial)


def add(*polynomials):
    result = {}
    for p in polynomials:
        for m, c in p.items():
            result[m] = result.get(m, Q(0)) + c
    return {m: c for m, c in result.items() if c}


def multiply(*polynomials):
    result = {(): Q(1)}
    for p in polynomials:
        out = {}
        for m, c in result.items():
            for n, b in p.items():
                monomial = tuple(sorted(m + n))
                if allowed(monomial):
                    out[monomial] = out.get(monomial, Q(0)) + c * b
        result = {m: c for m, c in out.items() if c}
    return result


x = [{(i,): Q(1)} for i in range(11)]
y = [add(*(x[j] for j, f in enumerate(flats) if not f & (1 << i))) for i in range(4)]
monomials = {}
relations = {}
free = {}
for degree in range(4):
    monomials[degree] = [m for m in combinations_with_replacement(range(11), degree) if allowed(m)]
    rows = []
    if degree >= 2:
        for i in range(4):
            for j, f in enumerate(flats):
                if f & (1 << i):
                    continue
                for m in monomials[degree - 2]:
                    p = multiply(y[i], x[j], {m: Q(1)})
                    rows.append([p.get(n, Q(0)) for n in monomials[degree]])
    relations[degree] = rref(rows, len(monomials[degree]))
    free[degree] = [i for i in range(len(monomials[degree])) if i not in relations[degree][1]]
assert [len(free[k]) for k in range(4)] == [1, 11, 11, 1]


def coordinates(p, degree):
    row = [p.get(m, Q(0)) for m in monomials[degree]]
    basis, pivots = relations[degree]
    for b, i in zip(basis, pivots):
        c = row[i]
        row = [v - c * z for v, z in zip(row, b)]
    return [row[i] for i in free[degree]]


flag = multiply(x[flats.index(0)], x[flats.index(1)], x[flats.index(3)])
normalization = coordinates(flag, 3)[0]
assert normalization


def degree(p):
    return coordinates(p, 3)[0] / normalization


def linear_combination(coefficients, polynomials):
    return add(*({m: c * b for m, b in p.items()} for c, p in zip(coefficients, polynomials)))


K1 = [x[flats.index(0)]] + [x[flats.index(1 << i)] for i in range(4)]
K2 = [multiply(K1[0], K1[0])] + [multiply(K1[i + 1], y[i]) for i in range(4)]
IH1_rows = kernel([[degree(multiply(k, v)) for v in x] for k in K2], 11)
IH1 = [linear_combination(row, x) for row in IH1_rows]
degree2_basis = [{monomials[2][i]: Q(1)} for i in free[2]]
IH2_rows = kernel([[degree(multiply(k, v)) for v in degree2_basis] for k in K1], 11)
IH2 = [linear_combination(row, degree2_basis) for row in IH2_rows]
assert len(IH1) == len(IH2) == 6
K_pairing = [[degree(multiply(a, b)) for b in K2] for a in K1]
assert K_pairing == [[Q((3 if i == 0 else -2) if i == j else 0) for j in range(5)] for i in range(5)]
assert all(degree(multiply(v, k)) == 0 for v in y for k in K2)
assert all(degree(multiply(a, b, k)) == 0 for a in y for b in IH1 for k in K1)
pair_flats = [f for f in flats if f.bit_count() == 2]
named_IH1 = []
for f in pair_flats:
    row = [Q(0)] * 11
    row[0] = Q(1, 3)
    row[flats.index(f)] = Q(1)
    for i in range(4):
        if f & (1 << i):
            row[flats.index(1 << i)] = Q(1, 2)
    named_IH1.append(row)
assert IH1_rows == named_IH1
square_witness = [degree(multiply(k, IH1[0], IH1[0])) for k in K1]
assert any(square_witness)
pairing = [[degree(multiply(a, b)) for b in IH2] for a in IH1]
assert determinant(pairing)
ell = add(*y)
L_images = [multiply(ell, v) for v in IH1]
assert all(degree(multiply(k, v)) == 0 for k in K1 for v in L_images)
L_rank = len(rref([coordinates(v, 2) for v in L_images], 11)[1])
assert L_rank == 6
L_pairing = [[degree(multiply(ell, a, b)) for b in IH1] for a in IH1]
assert determinant(L_pairing)
primitive_rows = kernel([[degree(multiply(ell, ell, v)) for v in IH1]], 6)
primitive = [linear_combination(row, IH1) for row in primitive_rows]
assert len(primitive) == 5
HR = [[-degree(multiply(ell, a, b)) for b in primitive] for a in primitive]
minors = [determinant([row[:k] for row in HR[:k]]) for k in range(1, 6)]
assert all(v > 0 for v in minors)
assert degree(multiply(ell, ell, ell)) == 24
assert len(rref([coordinates(v, 1) for v in y], 11)[1]) == 4
assert len(rref([coordinates(multiply(a, b), 2) for a in y for b in IH1], 11)[1]) == 6
assert len(rref([coordinates(multiply(a, b), 3) for a in y for b in IH2], 1)[1]) == 1
flat_counts = [1, 4, 6, 1]
# Rank-one and rank-two contractions have constant KL polynomial 1.
# Z=P+4t+6t^2+t^3 must be palindromic, with deg(P)<3/2.
recurrence_P = [1, flat_counts[2] - flat_counts[1]]
recurrence_Z = [1, recurrence_P[1] + flat_counts[1], flat_counts[2], 1]
assert recurrence_P == [1, 2] and recurrence_Z == recurrence_Z[::-1] == [1, 6, 6, 1]

report = {
    'source': 'BHM arXiv:2010.06088v5 Example 3.7; Definitions 2.2/2.5 and 3.4; separate finite rank-flat palindromic recurrence for P/Z',
    'matroid': 'U_(3,4), loopless, labelled ground set {1,2,3,4}',
    'coefficients': 'Q',
    'proper_flat_masks_in_variable_order': flats,
    'comparable_monomial_counts_degrees_0_to_3': [len(monomials[k]) for k in range(4)],
    'relation_ranks_degrees_0_to_3': [len(relations[k][1]) for k in range(4)],
    'augmented_Chow_dimensions': [1, 11, 11, 1],
    'Mobius_dimensions': [1, 4, 6, 1],
    'IH_dimensions': [1, 6, 6, 1],
    'IH1_basis_in_proper_flat_coordinates': [[str(c) for c in row] for row in IH1_rows],
    'K_degree1_degree2_pairing': [[str(c) for c in row] for row in K_pairing],
    'Mobius_action_preserves_IH_checked': True,
    'square_of_u12_pairing_with_K1': [str(c) for c in square_witness],
    'IH_embedding_is_not_a_subring': True,
    'PD_IH1_IH2_pairing': [[str(c) for c in row] for row in pairing],
    'PD_pairing_determinant': str(determinant(pairing)),
    'Lefschetz_class': 'ell=y1+y2+y3+y4, all rank-one-flat coefficients positive',
    'degree_ell_cubed': 24,
    'degree_x_empty_cubed': str(degree(multiply(x[0], x[0], x[0]))),
    'degrees_x_singleton_squared_y_i': [str(degree(multiply(x[flats.index(1 << i)], x[flats.index(1 << i)], y[i]))) for i in range(4)],
    'Lefschetz_IH1_to_IH2_rank': L_rank,
    'Lefschetz_pairing': [[str(c) for c in row] for row in L_pairing],
    'primitive_IH1_dimension': 5,
    'primitive_basis_in_IH1_basis_coordinates': [[str(c) for c in row] for row in primitive_rows],
    'signed_HR_primitive_matrix': [[str(c) for c in row] for row in HR],
    'positive_leading_principal_minors': [str(v) for v in minors],
    'IH_mod_positive_Mobius_ideal_dimensions': [1, 2, 0, 0],
    'independent_rank_flat_palindromic_recurrence_P': recurrence_P,
    'independent_rank_flat_palindromic_recurrence_Z': recurrence_Z,
    'P_M': '1+2t',
    'Z_M': '1+6t+6t^2+t^3',
    'scope': 'Exact named-source example only; no general theorem, integral extension, independent model receipt, original-result admission or different-compactification identification.'}
output = Path(__file__).resolve().parents[1] / 'singular_hodge_u34_exact_checks_20261005.json'
output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
