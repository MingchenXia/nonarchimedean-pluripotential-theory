"""Check Binder arXiv:2606.07490v1 Example 3.20 over Q.

Use the ordinary Bergman Stanley--Reisner ring and its full Koszul
differentials in internal degrees 0 through 6. Verify named cycles and
their independence modulo boundaries, and ranks for a specified class.
Also construct the complete finite square-free subcomplex in degrees
0 through 3, using the source's identified quasi-isomorphism. This is a
finite named-source audit, not a new general theorem or an independent
production-model receipt. Global identifications retain their source inputs.
"""

from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import json


def rank(rows, width):
    a = [[Q(x) for x in row] for row in rows]
    k = 0
    for j in range(width):
        h = next((h for h in range(k, len(a)) if a[h][j]), None)
        if h is None:
            continue
        a[k], a[h] = a[h], a[k]
        c = a[k][j]
        a[k] = [x / c for x in a[k]]
        for h in range(k + 1, len(a)):
            if a[h][j]:
                c = a[h][j]
                a[h] = [x - c * y for x, y in zip(a[h], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def kernel(rows, width):
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
    result = []
    for j in range(width):
        if j not in pivots:
            v = [Q(int(t == j)) for t in range(width)]
            for h, t in enumerate(pivots):
                v[t] = -a[h][j]
            result.append(v)
    return result


flats = [f for f in range(1, 16) if f.bit_count() < 3]
assert len(flats) == 10


def allowed(m):
    return all(flats[a] & flats[b] in (flats[a], flats[b]) for a in m for b in m)


monomials = {p: [m for m in combinations_with_replacement(range(10), p) if allowed(m)] for p in range(7)}
# Character basis m_i=ell_(i+1)-ell_4 for i=0,1,2.
linear = [[Q(bool(f & (1 << i))) - Q(bool(f & 8)) for f in flats] for i in range(3)]
bases, differentials, ranks, homology = {}, {}, {}, {}
rows = []
for j in range(7):
    for i in range(4):
        bases[i, j] = [(m, e) for m in monomials.get(j - i, []) for e in combinations(range(3), i)]
    for i in range(1, 4):
        target = {v: h for h, v in enumerate(bases[i - 1, j])}
        matrix = [[Q(0)] * len(bases[i, j]) for _ in target]
        for col, (m, e) in enumerate(bases[i, j]):
            for h, a in enumerate(e):
                for v, c in enumerate(linear[a]):
                    n = tuple(sorted(m + (v,)))
                    if c and allowed(n):
                        matrix[target[n, e[:h] + e[h + 1:]]][col] += (-1) ** h * c
        differentials[i, j] = matrix
        ranks[i, j] = rank(matrix, len(bases[i, j]))
    ranks[0, j] = ranks[4, j] = 0
    for i in range(2, 4):
        a, b = differentials[i - 1, j], differentials[i, j]
        for col in range(len(bases[i, j])):
            v = [sum(x * b[h][col] for h, x in enumerate(row)) for row in a]
            assert not any(v), (i, j, col)
    for i in range(4):
        homology[i, j] = len(bases[i, j]) - ranks[i, j] - ranks[i + 1, j]
    rows.append({'internal_degree': j, 'chain_dimensions_i0_to_i3': [len(bases[i, j]) for i in range(4)], 'differential_ranks_i1_to_i3': [ranks[i, j] for i in range(1, 4)], 'homology_dimensions_i0_to_i3': [homology[i, j] for i in range(4)]})
expected = {(0, 0): 1, (0, 1): 7, (0, 2): 1, (1, 2): 6, (1, 3): 3}
assert {k: v for k, v in homology.items() if v} == expected


def character_difference(a, b):
    return [Q(int(a == i + 1) - int(b == i + 1)) for i in range(3)]


def monomial_cycle(flat_masks, exterior_difference=None):
    m = tuple(sorted(flats.index(f) for f in flat_masks))
    if exterior_difference is None:
        return {(m, ()): Q(1)}
    return {(m, (i,)): c for i, c in enumerate(character_difference(*exterior_difference)) if c}


named = {
    (0, 0): [monomial_cycle([])],
    (0, 1): [monomial_cycle([8])] + [monomial_cycle([f]) for f in flats if f.bit_count() == 2],
    (0, 2): [monomial_cycle([8, 12])],
    (1, 2): [],
    (1, 3): [monomial_cycle([4, 6], (1, 4)), monomial_cycle([8, 10], (1, 3)), monomial_cycle([8, 12], (1, 2))]}
for f in [3, 5, 9, 6, 10, 12]:
    complement = [i + 1 for i in range(4) if not f & (1 << i)]
    named[1, 2].append(monomial_cycle([f], complement))


def vector(p, i, j):
    return [p.get(v, Q(0)) for v in bases[i, j]]


def boundaries(i, j):
    if i == 3:
        return []
    m = differentials[i + 1, j]
    return [[m[h][k] for h in range(len(m))] for k in range(len(bases[i + 1, j]))]


for (i, j), polys in named.items():
    vecs = [vector(p, i, j) for p in polys]
    if i:
        assert all(not any(sum(a * b for a, b in zip(row, v)) for row in differentials[i, j]) for v in vecs)
    assert rank(boundaries(i, j) + vecs, len(bases[i, j])) == ranks[i + 1, j] + homology[i, j]

# Separately construct Definition A.4's finite square-free subcomplex.
# Repeated terms force contractions by each ray of the support to vanish.
# Lemma A.5 of arXiv:2412.05732v2 is the identified quasi-isomorphism input.
sq_basis, sq_ranks, sq_rows = {}, {}, []
for j in range(7):
    for i in range(4):
        exterior = list(combinations(range(3), i))
        target_ext = list(combinations(range(3), i - 1)) if i else []
        vecs = []
        for m in monomials.get(j - i, []):
            if len(m) != len(set(m)):
                continue
            contraction = []
            for v in m:
                for n in target_ext:
                    row = []
                    for e in exterior:
                        row.append(sum((-1) ** h * linear[a][v] for h, a in enumerate(e) if e[:h] + e[h + 1:] == n))
                    contraction.append(row)
            for coefficients in kernel(contraction, len(exterior)):
                p = {(m, e): c for e, c in zip(exterior, coefficients) if c}
                vecs.append(vector(p, i, j))
        sq_basis[i, j] = vecs
        assert rank(vecs, len(bases[i, j])) == len(vecs)
        sq_ranks[0, j] = sq_ranks[4, j] = 0
    for i in range(1, 4):
        images = [[sum(a * b for a, b in zip(row, v)) for row in differentials[i, j]] for v in sq_basis[i, j]]
        assert rank(sq_basis[i - 1, j] + images, len(bases[i - 1, j])) == len(sq_basis[i - 1, j])
        sq_ranks[i, j] = rank(images, len(bases[i - 1, j]))
    sq_homology = [len(sq_basis[i, j]) - sq_ranks[i, j] - sq_ranks[i + 1, j] for i in range(4)]
    assert sq_homology == [homology[i, j] for i in range(4)]
    if j > 3:
        assert not any(len(sq_basis[i, j]) for i in range(4))
    if j <= 3:
        sq_rows.append({'internal_degree': j, 'chain_dimensions_i0_to_i3': [len(sq_basis[i, j]) for i in range(4)], 'differential_ranks_i1_to_i3': [sq_ranks[i, j] for i in range(1, 4)], 'homology_dimensions_i0_to_i3': sq_homology})
for (i, j), polys in named.items():
    assert rank(sq_basis[i, j] + [vector(p, i, j) for p in polys], len(bases[i, j])) == len(sq_basis[i, j])


def multiply_class(p):
    out = {}
    for (m, e), c in p.items():
        for v, f in enumerate(flats):
            n = tuple(sorted(m + (v,)))
            if allowed(n):
                out[n, e] = out.get((n, e), Q(0)) + c * f.bit_count() * (4 - f.bit_count())
    return out


maps = []
for i, j, power in [(0, 0, 1), (0, 0, 2), (0, 1, 1), (1, 2, 1)]:
    images = []
    for p in named[i, j]:
        for _ in range(power):
            p = multiply_class(p)
        if i:
            v = vector(p, i, j + power)
            assert not any(sum(a * b for a, b in zip(row, v)) for row in differentials[i, j + power])
        images.append(vector(p, i, j + power))
    image_rank = rank(boundaries(i, j + power) + images, len(bases[i, j + power])) - ranks[i + 1, j + power]
    assert image_rank == min(homology[i, j], homology[i, j + power])
    maps.append({'i': i, 'source_internal_degree': j, 'power': power, 'source_dimension': homology[i, j], 'target_dimension': homology[i, j + power], 'rank': image_rank})

report = {
    'source': 'Binder arXiv:2606.07490v1, Definitions 2.1/2.3/2.4 and Example 3.20',
    'matroid': 'U_(3,4), ordinary Bergman fan, ten proper nonempty flats',
    'ambient_lattice': 'Z^4/Z(1,1,1,1)', 'coefficients': 'Q',
    'flat_masks_in_variable_order': flats,
    'character_basis': ['ell1-ell4', 'ell2-ell4', 'ell3-ell4'],
    'linear_forms_in_flat_coordinates': [[str(c) for c in row] for row in linear],
    'computed_internal_degree_range': [0, 6],
    'degree_tables': rows,
    'all_computed_differential_squares_zero': True,
    'all_named_cycles_and_basis_independence_mod_boundaries_checked': True,
    'separate_square_free_complex_tables': sq_rows,
    'square_free_subcomplex_inclusion_and_dimensions_checked': True,
    'identified_square_free_quasi_isomorphism_source': 'Binder arXiv:2412.05732v2, Definition A.4 and Lemma A.5; complete finite example uses this source input, not a newly proved general quasi-isomorphism.',
    'nonzero_Koszul_bigraded_dimensions': [{'homological_i': i, 'internal_j': j, 'dimension': v, 'cohomological_degree_2j_minus_i': 2 * j - i, 'weight_2j': 2 * j} for (i, j), v in sorted(expected.items())],
    'ordinary_Chow_dimensions_degrees_0_to_2': [1, 7, 1],
    'singular_cohomology_dimensions_degrees_0_to_5': [1, 0, 7, 6, 1, 3],
    'Hodge_Poincare_polynomial': '1+7x+x^2+6wx^2+3wx^3',
    'singular_cohomology_Poincare_polynomial': '1+7t^2+6t^3+t^4+3t^5',
    'checked_class': 'sum_F |F|(4-|F|) x_F = 3 sum_singleton x_i + 4 sum_pair x_ij',
    'checked_multiplication_maps': maps,
    'scope': 'Finite named-source example: full polynomial Koszul degrees 0..6 and the separate complete finite square-free subcomplex in degrees 0..3. The global quasi-isomorphism, topological/cohomological and weight identifications retain their controlling source inputs. No new general quasi-isomorphism or matroid Lefschetz theorem, integral extension, original-result admission or independent model receipt.'}
out = Path(__file__).resolve().parents[1] / 'uniform_singular_cohomology_u34_exact_checks_20261005.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
