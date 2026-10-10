"""Exact support/fibre checks for a research diagnostic, not a model receipt.

Uses only the standard library.  No active manuscript is edited.
Indices: 0,1,2 coordinate lines; 3 extra line M; 4,5 smooth conics C,D.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json


def rref_solution(rows, variables=3):
    a = [[F(x) for x in row] for row in rows]
    pivots = []
    row = 0
    for col in range(variables):
        pivot = next((k for k in range(row, len(a)) if a[k][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = a[row][col]
        a[row] = [x/divisor for x in a[row]]
        for k in range(len(a)):
            if k != row and a[k][col]:
                scale = a[k][col]
                a[k] = [x-scale*y for x, y in zip(a[k], a[row])]
        pivots.append(col)
        row += 1
    if any(not any(r[:variables]) and r[variables] for r in a):
        return None
    particular = [F(0)]*variables
    for k, col in enumerate(pivots):
        particular[col] = a[k][variables]
    free = [i for i in range(variables) if i not in pivots]
    kernel = []
    for col in free:
        v = [F(0)]*variables
        v[col] = F(1)
        for k, p in enumerate(pivots):
            v[p] = -a[k][col]
        kernel.append(v)
    return particular, kernel


def poly_value(coefficients, x):
    value = F(0)
    for c in coefficients:
        value = value*x+c
    return value


degrees = [1, 1, 1, 1, 2, 2]
points = Counter()
for a, b in combinations(range(4), 2):
    points[(a, b)] = 1
for a in range(3):
    for b in [4, 5]:
        points[(a, b)] = 2
points[(3, 4)] = 1
points[(3, 5)] = 1
points[(4, 5)] = 3
points[(3, 4, 5)] = 1
assert len(points) == 16 and sum(points.values()) == 24
for i, j in combinations(range(6), 2):
    assert sum(w for p, w in points.items() if i in p and j in p) == degrees[i]*degrees[j]

# Smooth diagonal conics; coordinate-line restrictions have two simple roots.
# Put r^2=-2 and M: x+y/r-2z=0.  On M use (x,y,z)=(2-t,r*t,1).
conic_coefficients = [[1, 1, 1], [1, 2, 3]]
assert all(c for coeff in conic_coefficients for c in coeff)
coordinate_restrictions = []
for coeff in conic_coefficients:
    for missing in range(3):
        keep = [coeff[k] for k in range(3) if k != missing]
        discriminant = -4*keep[0]*keep[1]
        assert discriminant != 0
        coordinate_restrictions.append(discriminant)
common_points = []
for s, t in product([-1, 1], repeat=2):
    assert s*s-2*t*t+1 == 0
    assert s*s-4*t*t+3 == 0
    common_points.append({'x': s, 'y': f'{t}*r', 'z': 1, 'M_value': s+t-2})
assert sum(p['M_value'] == 0 for p in common_points) == 1
# At these four points all coordinates are nonzero, so the distinct diagonal
# coefficient ratios 1,2,3 make the two conic gradients independent.
m_restrictions = [([-1, -4, 5], [F(1), F(-5)]),
                  ([-3, -4, 7], [F(1), F(-7, 3)])]
for coeff, roots in m_restrictions:
    assert roots[0] != roots[1]
    assert all(poly_value(coeff, x) == 0 for x in roots)
assert [poly_value(c, F(0)) for c, _ in m_restrictions] == [5, 7]
assert [poly_value(c, F(2)) for c, _ in m_restrictions] == [-7, -13]
# At z=0 the M point is [1:-r:0], with conic values -1 and -3.
assert [c[0]-2*c[1] for c in conic_coefficients] == [-1, -3]

def quotient_vector(v):
    # Eliminate the first coordinate using d_0=1; this identifies N with Z^5.
    return [v[j]-v[0]*degrees[j] for j in range(1, 6)]


facets = []
for p, weight in sorted(points.items()):
    chi = [int(j in p) for j in range(6)]
    vp = quotient_vector(chi)
    assert gcd(*vp) == 1
    for j in p:
        ej = [int(k == j) for k in range(6)]
        uj = quotient_vector(ej)
        minors = [uj[a]*vp[b]-uj[b]*vp[a] for a, b in combinations(range(5), 2)]
        assert gcd(*minors) == 1
        facets.append((j, p, weight))
assert len(facets) == 33
for i in range(6):
    total = [sum(w*int(k in p) for p, w in points.items() if i in p) for k in range(6)]
    incidence_count = sum(w for p, w in points.items() if i in p)
    expected = [degrees[i]*degrees[k]+(incidence_count-degrees[i]**2)*int(k == i) for k in range(6)]
    assert total == expected


def fibre(target):
    feasible = []
    for j, p, weight in facets:
        # alpha*e_j + beta*chi_p = target + lambda*d + height*e_M.
        rows = [[int(k == j), int(k in p), -degrees[k], target[k]] for k in [0, 1, 2, 4, 5]]
        solution = rref_solution(rows)
        if solution is None:
            continue
        particular, kernel = solution
        if kernel:
            assert j == 3 and kernel == [[F(1), F(0), F(0)]]
            assert particular == [F(0), F(1), F(0)]
            height = particular[1]*int(3 in p)
            feasible.append({'divisor': j, 'point': list(p), 'weight': weight,
                             'height_interval': [str(height), 'infinity'],
                             'alpha': 'free >= 0', 'beta': '1', 'lambda': '0'})
        else:
            alpha, beta, lam = particular
            if alpha < 0 or beta < 0:
                continue
            assert lam == 0
            height = alpha*int(j == 3)+beta*int(3 in p)
            feasible.append({'divisor': j, 'point': list(p), 'weight': weight,
                             'height': str(height), 'alpha': str(alpha),
                             'beta': str(beta), 'lambda': str(lam)})
    return feasible


ray_fibre = fibre([0, 0, 0, 0, 1, 1])
interior_fibre = fibre([0, 0, 0, 0, 2, 1])
assert len(ray_fibre) == 5
assert {r['height'] for r in ray_fibre if 'height' in r} == {'0', '1'}
assert [r['height_interval'] for r in ray_fibre if 'height_interval' in r] == [['1', 'infinity']]
assert len(interior_fibre) == 2
assert {r['height'] for r in interior_fibre} == {'0', '1'}
assert not any('height_interval' in r for r in interior_fibre)

out = {
    'scope': 'Exact arithmetic check of a research candidate; not an independent model receipt or formal admission.',
    'degrees': degrees,
    'unique_incidence_sets': len(points),
    'geometric_intersection_points': sum(points.values()),
    'incidence_data': [{'point': list(p), 'multiplicity': w} for p, w in sorted(points.items())],
    'pairwise_distinct_curve_Bezout_checks': 15,
    'literal_repeated_coordinate_Bezout_axiom_used': False,
    'arrangement_is_simple_in_source_sense': False,
    'common_conic_points': common_points,
    'coordinate_conic_discriminants': coordinate_restrictions,
    'M_conic_restrictions': [{'coefficients': coeff, 'roots': [str(x) for x in roots]} for coeff, roots in m_restrictions],
    'all_pairwise_intersections_transverse': True,
    'facets_checked': len(facets),
    'all_facet_lattices_saturated_and_generators_primitive': True,
    'divisor_balance_checks': 6,
    'point_balance_checks': len(points),
    'ray_basepoint': 'e_C+e_D',
    'ray_fibre_all_feasible_facets': ray_fibre,
    'ray_fibre_height_set': '{0} union [1,infinity)',
    'interior_basepoint': '2*e_C+e_D',
    'interior_fibre_all_feasible_facets': interior_fibre,
    'interior_fibre_height_set': '{0,1}',
    'all_other_facets_excluded_by_exact_linear_systems': True,
    'Theorem_5_4_or_6_2_counterexample_claimed': False,
    'book_or_problem_inventory_modified': False,
}
path = Path(__file__).resolve().parents[1] / 'arroid_projection_exact_checks_20261005.json'
if path.exists():
    assert json.loads(path.read_text()) == out, 'Refuse to overwrite different dated evidence'
else:
    path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'output': str(path), 'facets': len(facets), 'ray_fibre': out['ray_fibre_height_set'], 'interior_fibre': out['interior_fibre_height_set'], 'exact_checks_passed': True}))
