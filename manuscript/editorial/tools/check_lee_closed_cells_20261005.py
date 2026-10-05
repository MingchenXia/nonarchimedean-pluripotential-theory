"""Exact finite checks of a matroid closed-cell candidate.

The candidate uses closures of coordinate cone pieces, with facets from
finite cone faces, positive endpoints and the largest negative flat.
This script checks its combinatorial incidence and independently computes
multi-tangent chain groups on selected examples. It is not a certificate
that this model equals the extended-polyhedral/sheaf complex in all ranks.
"""

from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import ast
import hashlib
import json


root = Path(__file__).resolve().parents[1]
helper = root / 'tools/check_lee_matroid_strata_20261005.py'
tree = ast.parse(helper.read_text())
definitions = ast.Module(body=[node for node in tree.body
                              if isinstance(node, (ast.Import, ast.ImportFrom,
                                                   ast.FunctionDef))], type_ignores=[])
namespace = {}
exec(compile(definitions, str(helper), 'exec'), namespace)
matroids = namespace['matroids']
flags = namespace['flags']
rank_matrix = namespace['rank_matrix']


def cells_and_facets(n, ground, independent, ranks, flats):
    cells = []
    for f in sorted(flats):
        for j in sorted(independent):
            if j & f != j:
                continue
            chains = flags({g for g in flats if j & g == j
                            and g & f == g and g != f})
            for chain in chains:
                for i in sorted(independent):
                    if j & i != j or i & f != i:
                        continue
                    if all(i & g == i for g in chain):
                        cells.append((j, f, i & ~j, chain))
    cells.sort(key=lambda c: (c[2].bit_count() + len(c[3]), c))
    indices = {cell: k for k, cell in enumerate(cells)}
    assert len(indices) == len(cells)
    facets = []
    for j, f, i, chain in cells:
        edges = []
        positives = [k for k in range(n) if i & (1 << k)]
        d = len(positives) + len(chain)
        for k, element in enumerate(positives):
            bit = 1 << element
            edges.append(((j, f, i ^ bit, chain), (-1) ** (k + 1)))
            edges.append(((j | bit, f, i ^ bit, chain), (-1) ** k))
        for k in range(len(chain)):
            face = (j, f, i, chain[:k] + chain[k + 1:])
            edges.append((face, (-1) ** (len(positives) + k + 1)))
        if chain:
            edges.append(((j, chain[-1], i, chain[:-1]), (-1) ** (d - 1)))
        boundary = {}
        for face, sign in edges:
            assert face in indices, ('missing facet', face)
            k = indices[face]
            assert cells[k][2].bit_count() + len(cells[k][3]) == d - 1
            boundary[k] = boundary.get(k, 0) + sign
        assert all(abs(sign) == 1 for sign in boundary.values())
        facets.append(boundary)
    closures = []
    for k, boundary in enumerate(facets):
        closed = 1 << k
        composed = {}
        for h, sign in boundary.items():
            assert h < k
            closed |= closures[h]
            for g, other in facets[h].items():
                composed[g] = composed.get(g, 0) + sign * other
        assert all(value == 0 for value in composed.values()), ('incidence square', cells[k])
        closures.append(closed)
    closed_cells = set(closures)
    assert len(closed_cells) == len(cells)
    for ca, cb in combinations(closures, 2):
        intersection = ca & cb
        assert intersection == 0 or intersection in closed_cells, 'Nonface cell intersection'
    return cells, facets, closures


def row_basis(rows, width):
    a = [[Q(x) for x in row] for row in rows]
    pivots = []
    k = 0
    for j in range(width):
        h = next((h for h in range(k, len(a)) if a[h][j]), None)
        if h is None:
            continue
        a[k], a[h] = a[h], a[k]
        divisor = a[k][j]
        a[k] = [x / divisor for x in a[k]]
        for h in range(len(a)):
            if h != k and a[h][j]:
                c = a[h][j]
                a[h] = [x - c * y for x, y in zip(a[h], a[k])]
        pivots.append(j)
        k += 1
        if k == len(a):
            break
    return a[:k], pivots


def determinant(matrix):
    if not matrix:
        return Q(1)
    a = [[Q(x) for x in row] for row in matrix]
    result = Q(1)
    for j in range(len(a)):
        h = next((h for h in range(j, len(a)) if a[h][j]), None)
        if h is None:
            return Q(0)
        if h != j:
            a[j], a[h] = a[h], a[j]
            result = -result
        divisor = a[j][j]
        result *= divisor
        for h in range(j + 1, len(a)):
            c = a[h][j] / divisor
            for k in range(j + 1, len(a)):
                a[h][k] -= c * a[j][k]
    return result


def generators(n, cell):
    _, f, i, chain = cell
    return [tuple(int(k == element) for k in range(n))
            for element in range(n) if i & (1 << element)] + [
                tuple(-int(bool((f & ~g) & (1 << k))) for k in range(n))
                for g in chain]


def tangent_complex(n, ranks, flats, cells, facets, closures, p):
    coordinates = list(combinations(range(n), p))
    width = len(coordinates)
    bases = []
    for k, cell in enumerate(cells):
        rows = []
        for h, larger in enumerate(cells):
            if larger[:2] != cell[:2] or not closures[h] & (1 << k):
                continue
            for rays in combinations(generators(n, larger), p):
                rows.append([determinant([[ray[j] for j in coord] for ray in rays])
                             for coord in coordinates])
        bases.append(row_basis(rows, width))
    dimension = max(ranks.values())
    chain_cells = [[] for _ in range(dimension + 1)]
    positions = {}
    for k, cell in enumerate(cells):
        d = cell[2].bit_count() + len(cell[3])
        for b in range(len(bases[k][0])):
            positions[(k, b)] = len(chain_cells[d])
            chain_cells[d].append((k, b))
    boundaries = [[] for _ in range(dimension + 1)]
    for d in range(1, dimension + 1):
        for k, b in chain_cells[d]:
            vector = bases[k][0][b]
            column = {}
            for h, sign in facets[k].items():
                j, f, _, _ = cells[h]
                live = f & ~j
                projected = [value if all(live & (1 << t) for t in coord) else Q(0)
                             for value, coord in zip(vector, coordinates)]
                target, pivots = bases[h]
                coefficients = [projected[t] for t in pivots]
                assert all(sum(c * row[t] for c, row in zip(coefficients, target))
                           == projected[t] for t in range(width)), 'Coefficient map leaves target'
                for u, c in enumerate(coefficients):
                    if c:
                        row = positions[(h, u)]
                        column[row] = column.get(row, Q(0)) + sign * c
            boundaries[d].append({h: c for h, c in column.items() if c})
    for d in range(2, dimension + 1):
        for column in boundaries[d]:
            composed = {}
            for h, c in column.items():
                for g, other in boundaries[d - 1][h].items():
                    composed[g] = composed.get(g, Q(0)) + c * other
            assert all(c == 0 for c in composed.values()), ('Tangent square', p, d)
    differential_ranks = [0]
    for d in range(1, dimension + 1):
        matrix = [[col.get(k, 0) for col in boundaries[d]]
                  for k in range(len(chain_cells[d - 1]))]
        differential_ranks.append(rank_matrix(matrix))
    homology = [len(chain_cells[d]) - differential_ranks[d]
                - (differential_ranks[d + 1] if d < dimension else 0)
                for d in range(dimension + 1)]
    expected = [sum(ranks[f] == p for f in flats) if d == p else 0
                for d in range(dimension + 1)]
    assert homology == expected, ('Tangent homology differs', p, homology, expected)
    return {'p': p, 'chain_dimensions': [len(x) for x in chain_cells],
            'boundary_ranks_over_Q': differential_ranks[1:],
            'homology_dimensions': homology}


records = []
examples = []
for n in range(5):
    for ground, bases, independent, ranks, flats in matroids(n):
        cells, facets, closures = cells_and_facets(n, ground, independent, ranks, flats)
        counts = [sum(c[2].bit_count() + len(c[3]) == q for c in cells)
                  for q in range(max(ranks.values()) + 1)]
        record = {'n': n, 'bases_as_bitmasks': sorted(bases), 'rank': max(ranks.values()),
                  'cells_by_dimension': counts, 'cell_pairs': len(cells) * (len(cells) - 1) // 2,
                  'all_candidate_closed_cell_intersections_are_faces': True,
                  'signed_incidence_square_zero': True}
        records.append(record)
        name = None
        if n == 0:
            name = 'Empty ground set'
        elif n == 3 and bases == frozenset({7}):
            name = 'Boolean U_3_3'
        elif n == 4 and bases == frozenset({7, 11, 13, 14}):
            name = 'Uniform U_3_4'
        elif n == 4 and bases == frozenset({3, 5, 6, 9, 10, 12}):
            name = 'Uniform U_2_4'
        elif n == 4 and bases == frozenset({5, 6}):
            name = 'Parallel pair 0,1; coloop 2; loop 3'
        if name:
            complexes = [tangent_complex(n, ranks, flats, cells, facets, closures, p)
                         for p in range(max(ranks.values()) + 1)]
            examples.append({'name': name, **record, 'multi_tangent_complexes': complexes})
assert len(records) == 92 and len(examples) == 5
report = {'scope': 'Finite candidate closed-cell poset and multi-tangent chains; no general geometric/sheaf identification, model receipt, theorem admission or active TeX import.',
          'source_conventions': 'Lee26 Definitions 2.5/2.11 and Proposition 4.8; EHL23 Definitions 3.2/5.10 including the empty flat.',
          'enumerator_dependency_sha256': hashlib.sha256(helper.read_bytes()).hexdigest(),
          'facet_rule': 'Finite deletion of a positive ray or negative flat; positive endpoint for each independent ray; negative endpoint along the largest flat of the chain.',
          'matroids_checked': 92, 'candidate_cells_checked': sum(sum(r['cells_by_dimension']) for r in records),
          'candidate_cell_pairs_checked': sum(r['cell_pairs'] for r in records),
          'candidate_face_posets_and_signed_incidence_pass': True,
          'selected_multi_tangent_examples': examples,
          'multi_tangent_maps_stay_in_target_and_square_zero': True,
          'selected_rational_homology_matches_flat_counts': True,
          'tropical_cohomology_identification_certified_for_arbitrary_matroids': False,
          'integral_torsion_check_claimed': False, 'records': records}
target = root / 'lee_closed_cells_exact_checks_20261005.json'
encoded = json.dumps(report, indent=2, sort_keys=True) + '\n'
if target.exists():
    assert target.read_text() == encoded, 'Refusing to replace different dated evidence.'
else:
    target.write_text(encoded)
print(json.dumps({k: report[k] for k in ['matroids_checked', 'candidate_cells_checked',
                                       'candidate_cell_pairs_checked',
                                       'candidate_face_posets_and_signed_incidence_pass',
                                       'multi_tangent_maps_stay_in_target_and_square_zero',
                                       'selected_rational_homology_matches_flat_counts']}, indent=2))
print(json.dumps({'examples': examples}, indent=2))
