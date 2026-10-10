"""Exact bookkeeping for named source examples, with rational cube chains.

No general theorem or original-result admission follows from these checks.
The integral tripod compares Chow relations with actual multi-tangent
lattices. The cube fan checks AP24b Example 8.3 over Q. The literal
standard-lattice clause of Example 8.2 is retained as a source diagnostic.
"""

from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd
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


def determinant(rows):
    if not rows:
        return Q(1)
    if len(rows) == 1:
        return Q(rows[0][0])
    return sum((-1) ** j * Q(rows[0][j]) * determinant(
        [row[:j] + row[j + 1:] for row in rows[1:]]) for j in range(len(rows)))


def inverse(matrix):
    n = len(matrix)
    augmented = [list(row) + [int(i == j) for j in range(n)]
                 for i, row in enumerate(matrix)]
    reduced, pivots = rref(augmented, 2 * n)
    assert pivots == list(range(n))
    return [row[n:] for row in reduced]


def orthogonal_quotient(rays, sedentarity):
    identity = [[Q(int(i == j)) for j in range(3)] for i in range(3)]
    basis = [rays[i] for i in sorted(sedentarity)]
    if not basis:
        return identity
    gram = [[sum(x * y for x, y in zip(a, b)) for b in basis] for a in basis]
    inv = inverse(gram)
    return [[identity[i][j] - sum(basis[k][i] * inv[k][h] * basis[h][j]
                                for k in range(len(basis)) for h in range(len(basis)))
             for j in range(3)] for i in range(3)]


def matrix_vector(matrix, vector):
    return [sum(x * y for x, y in zip(row, vector)) for row in matrix]


def cube_fan_check():
    rays = list(product([-1, 1], repeat=3))
    edges = [frozenset({i, j}) for i, j in combinations(range(8), 2)
             if sum(a != b for a, b in zip(rays[i], rays[j])) == 1]
    fan = [frozenset()] + [frozenset({i}) for i in range(8)] + edges
    cells = [(sigma, frozenset(tau)) for sigma in fan
             for k in range(len(sigma) + 1) for tau in combinations(sorted(sigma), k)]
    cells.sort(key=lambda pair: (len(pair[0]) - len(pair[1]),
                                 tuple(sorted(pair[0])), tuple(sorted(pair[1]))))
    positions = {cell: k for k, cell in enumerate(cells)}
    facets = []
    for sigma, tau in cells:
        boundary = {}
        for k, ray in enumerate(sorted(sigma - tau)):
            boundary[positions[(sigma - {ray}, tau)]] = (-1) ** (k + 1)
            boundary[positions[(sigma, tau | {ray})]] = (-1) ** k
        facets.append(boundary)
    for k, boundary in enumerate(facets):
        composed = {}
        for h, c in boundary.items():
            for g, other in facets[h].items():
                composed[g] = composed.get(g, 0) + c * other
        assert all(c == 0 for c in composed.values())
    quotients = {tau: orthogonal_quotient(rays, tau) for _, tau in cells}
    results = []
    for p in range(3):
        coordinates = list(combinations(range(3), p))
        width = len(coordinates)
        bases = []
        for sigma, tau in cells:
            projected = quotients[tau]
            rows = []
            for larger in fan:
                if not sigma <= larger:
                    continue
                vectors = [matrix_vector(projected, rays[j]) for j in sorted(larger)]
                for chosen in combinations(vectors, p):
                    rows.append([determinant([[v[j] for j in c] for v in chosen])
                                 for c in coordinates])
            bases.append(rref(rows, width))
        groups = [[] for _ in range(3)]
        index = {}
        for k, (sigma, tau) in enumerate(cells):
            d = len(sigma) - len(tau)
            for b in range(len(bases[k][0])):
                index[(k, b)] = len(groups[d])
                groups[d].append((k, b))
        boundaries = [[] for _ in range(3)]
        for d in [1, 2]:
            for k, b in groups[d]:
                column = {}
                for h, sign in facets[k].items():
                    tau = cells[h][1]
                    proj = quotients[tau]
                    exterior = [[determinant([[proj[i][j] for j in old] for i in new])
                                 for old in coordinates] for new in coordinates]
                    value = matrix_vector(exterior, bases[k][0][b])
                    target, pivots = bases[h]
                    coefficients = [value[t] for t in pivots]
                    assert all(sum(c * row[t] for c, row in zip(coefficients, target))
                               == value[t] for t in range(width))
                    for j, c in enumerate(coefficients):
                        if c:
                            row = index[(h, j)]
                            column[row] = column.get(row, Q(0)) + sign * c
                boundaries[d].append({j: c for j, c in column.items() if c})
        for column in boundaries[2]:
            composed = {}
            for j, c in column.items():
                for i, other in boundaries[1][j].items():
                    composed[i] = composed.get(i, Q(0)) + c * other
            assert all(c == 0 for c in composed.values())
        ranks = [0]
        for d in [1, 2]:
            matrix = [[col.get(j, 0) for col in boundaries[d]]
                      for j in range(len(groups[d - 1]))]
            ranks.append(len(rref(matrix, len(groups[d]))[1]))
        homology = [len(groups[d]) - ranks[d] - (ranks[d + 1] if d < 2 else 0)
                    for d in range(3)]
        expected = [[1, 0, 0], [0, 5, 0], [0, 2, 1]][p]
        assert homology == expected
        results.append({'p': p, 'chain_dimensions': [len(g) for g in groups],
                        'boundary_ranks_over_Q': ranks[1:],
                        'homology_dimensions': homology})
    return {'rays': rays, 'two_cones': [sorted(e) for e in edges],
            'canonical_cells_by_dimension': [sum(len(s) - len(t) == d for s, t in cells)
                                            for d in range(3)],
            'coefficients': 'Q; no integral cohomology or torsion computed for the cube.',
            'complexes': results}


def smith_data_two_rows(rows):
    entries = [abs(int(x)) for row in rows for x in row]
    d1 = gcd(*entries)
    minors = [abs(int(determinant([[row[i], row[j]] for row in rows])))
              for i, j in combinations(range(len(rows[0])), 2)]
    d12 = gcd(*minors)
    assert d1 and d12
    return {'smith_nonzero_invariants': [d1, d12 // d1],
            'cokernel_free_rank': len(rows[0]) - 2}


chow_relations = [[-2, 1, 1], [3, 0, -3]]
tangent_relations = [[-2, 1, 1], [1, 0, -1]]
chow = smith_data_two_rows(chow_relations)
tangent = smith_data_two_rows(tangent_relations)
assert chow['smith_nonzero_invariants'] == [1, 3]
assert tangent['smith_nonzero_invariants'] == [1, 1]
assert [3 * a + 2 * b for a, b in zip(*chow_relations)] == [0, 3, -3]
assert Q(2, 3).denominator != 1
standard_rays = [(-1, -1), (1, 0), (0, 1)]
standard_determinants = [int(determinant([list(a), list(b)]))
                         for a, b in combinations(standard_rays, 2)]
assert all(abs(d) == 1 for d in standard_determinants)
report = {'scope': 'Exact source-example bookkeeping; no general theorem, independent model receipt, original-result admission or problem retirement.',
          'AP24b_Example_8_1': {'lattice_basis_in_standard_coordinates': [['1', '0'], ['1/3', '-1/3']],
                               'primitive_rays_in_this_lattice_basis': [[-2, 3], [1, 0], [1, -3]],
                               'Chow_A1_relation_rows': chow_relations, 'Chow_A1': chow,
                               'multi_tangent_origin_lattice': 'Ze1+Ze2, index three in N',
                               'H_1_1_relation_rows': tangent_relations, 'H_1_1': tangent,
                               'torsion_class': 'x_rho1-x_rho2; exact order three',
                               'three_times_torsion_class_relation_coefficients': [3, 2]},
          'AP24b_literal_Example_8_2_diagnostic': {'printed_lattice': 'Z^2',
                                                'printed_rays': standard_rays,
                                                'pair_determinants': standard_determinants,
                                                'literal_fan_is_unimodular': True,
                                                'literal_nonunimodular_example_imported': False,
                                                'claim_that_theorem_1_1_is_refuted': False},
          'AP24b_Example_8_3_rational_check': cube_fan_check()}
target = Path(__file__).resolve().parents[1] / 'canonical_fan_examples_exact_checks_20261005.json'
encoded = json.dumps(report, indent=2, sort_keys=True) + '\n'
if target.exists():
    assert target.read_text() == encoded, 'Refusing to replace different dated evidence.'
else:
    target.write_text(encoded)
print(json.dumps(report, indent=2))
