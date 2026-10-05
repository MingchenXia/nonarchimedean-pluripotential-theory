"""Exact rational checks for a source-audit candidate, not a model receipt.

The common refinement of the positive orthant fan with two central
hyperplane fans is a genuine fan.  Projection along a two-dimensional
ambient face nevertheless produces a cone and a proper full-dimensional
subcone in the collection of Lee26 Definition A.5.  No active TeX is edited.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json


def rref(rows, n=4):
    a = [[F(x) for x in row] for row in rows]
    pivots = []
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        divisor = a[k][j]
        a[k] = [x / divisor for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                c = a[i][j]
                a[i] = [x - c*y for x, y in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
    return a, pivots


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def primitive(v):
    denominator = lcm(*(x.denominator for x in v))
    w = [int(x*denominator) for x in v]
    divisor = gcd(*w)
    return tuple(x // divisor for x in w)


def rays(rows):
    """Enumerate all extreme rays of a pointed cone in the orthant."""
    answer = set()
    for active in combinations(rows, 3):
        a, pivots = rref(active)
        if len(pivots) != 3:
            continue
        j = next(j for j in range(4) if j not in pivots)
        v = [F(0)]*4
        v[j] = F(1)
        for k, p in enumerate(pivots):
            v[p] = -a[k][j]
        for sign in [1, -1]:
            w = [sign*x for x in v]
            if all(dot(row, w) >= 0 for row in rows):
                answer.add(primitive(w))
    return tuple(sorted(answer))


coordinates = [tuple(int(i == j) for j in range(4)) for i in range(4)]
h1 = (1, -1, 1, -1)
h2 = (1, -1, -1, 1)


def inequalities(mask, signs):
    rows = list(coordinates)
    rows += [tuple(-x for x in coordinates[i]) for i in range(4)
             if not mask & (1 << i)]
    for h, s in zip([h1, h2], signs):
        rows += [tuple(s*x for x in h)] if s else [h, tuple(-x for x in h)]
    return rows


descriptions = {}
for mask in range(16):
    for signs in product([-1, 0, 1], repeat=2):
        rows = inequalities(mask, signs)
        descriptions[(mask, signs)] = {'rows': rows, 'rays': rays(rows)}
fan = {}
for label, c in descriptions.items():
    fan.setdefault(c['rays'], label)

# Each common refinement cone is closed under all faces.  Pairwise
# intersections are obtained by making every conflicting sign zero and
# intersecting coordinate supports.  Explicit nonnegative supporting forms
# certify that the intersection is a face of each cone.
pair_count = 0
for (ra, la), (rb, lb) in combinations(fan.items(), 2):
    ma, sa = la
    mb, sb = lb
    signs = tuple(a if a == b else 0 for a, b in zip(sa, sb))
    ri = descriptions[(ma & mb, signs)]['rays']
    assert set(ri) <= set(ra) and set(ri) <= set(rb)
    for r, m, ss, other_m, other_ss in [(ra, ma, sa, mb, sb),
                                       (rb, mb, sb, ma, sa)]:
        supporting = [0]*4
        for i in range(4):
            if m & (1 << i) and not other_m & (1 << i):
                supporting[i] += 1
        for h, s, other_s in zip([h1, h2], ss, other_ss):
            if s and s != other_s:
                supporting = [x+s*y for x, y in zip(supporting, h)]
        assert all(dot(supporting, v) >= 0 for v in r)
        assert {v for v in r if dot(supporting, v) == 0} == set(ri)
    pair_count += 1

# Delta is the orthant and all its coordinate faces.  For every such eta,
# its coordinate generators occur in refinement cones contained in eta.
# The common-refinement construction covers eta, hence Definition A.3's
# support equality holds.  Record the exact coordinate-generator check.
for mask in range(16):
    contained = [c for (m, s), c in descriptions.items() if m == mask]
    for i in range(4):
        if mask & (1 << i):
            assert any(coordinates[i] in c['rays'] for c in contained)

cpp = descriptions[(15, (1, 1))]
cpm = descriptions[(15, (1, -1))]
assert len(rref(cpp['rays'])[1]) == len(rref(cpm['rays'])[1]) == 4
boundary_pp = (2, 1, 0, 0)
boundary_pm = (1, 1, 0, 0)
for c, v in [(cpp, boundary_pp), (cpm, boundary_pm)]:
    assert v[0] > 0 and v[1] > 0 and v[2:] == (0, 0)
    assert all(dot(row, v) >= 0 for row in c['rows'])

project_pp = sorted(set(v[2:] for v in cpp['rays']) - {(0, 0)})
project_pm = sorted(set(v[2:] for v in cpm['rays']) - {(0, 0)})
assert (1, 0) in project_pp and (0, 1) in project_pp
assert all(z >= 0 and w >= 0 for z, w in project_pp)
assert (1, 0) in project_pm and (1, 1) in project_pm
assert all(z >= w >= 0 for z, w in project_pm)

# Exact universal lift formulas (proved algebraically in the note):
# C++: t=abs(z-w), y=1, x=1+t; C+-: t=0, x=y=1 for z>=w.
# The grid independently catches sign/transcription mistakes; it does not
# replace the all-real-parameters algebraic certificate.
grid_count = 0
for z, w in product([F(0), F(1, 3), F(1), F(2), F(7, 2)], repeat=2):
    v = (1+abs(z-w), F(1), z, w)
    assert all(dot(row, v) >= 0 for row in cpp['rows'])
    if z >= w:
        assert all(dot(row, (F(1), F(1), z, w)) >= 0 for row in cpm['rows'])
    grid_count += 1

# D=C++ cap C+- is proper but contains an interior point of C++; thus it
# cannot be a face of C++.
interior = (2, 1)
outside_d = (1, 2)
assert all(x > 0 for x in interior) and interior[0] >= interior[1]
assert all(x > 0 for x in outside_d) and outside_d[0] < outside_d[1]
# An explicit addition certificate fails the defining property of a face.
# u,v belong to C, u+v belongs to D, yet v does not belong to D.
u, v = (2, 0), (0, 1)
assert tuple(a+b for a, b in zip(u, v)) == interior
assert u[0] >= u[1] and v[0] < v[1]

dimension_counts = {}
for r in fan:
    d = len(rref(r)[1])
    dimension_counts[str(d)] = dimension_counts.get(str(d), 0)+1
report = {
    'scope': 'Exact rational source-audit candidate; no independent model receipt or theorem admission.',
    'target': 'Lee, arXiv:2604.00750v1, Definition A.3/A.5 and Proposition A.6, pp. 24-25',
    'ambient_dimension': 4,
    'coordinates': ['x', 'y', 'z', 'w'],
    'hyperplane_forms': [list(h1), list(h2)],
    'Delta': 'positive orthant and all its coordinate faces',
    'Sigma': 'common refinement with the two central hyperplane fans',
    'cone_descriptions_enumerated': len(descriptions),
    'distinct_cones': len(fan),
    'dimension_counts': dimension_counts,
    'cone_pairs_with_exact_common_face_certificates': pair_count,
    'coordinate_faces_checked': 16,
    'boundary_face_zeta': [[1, 0, 0, 0], [0, 1, 0, 0]],
    'projection': '(x,y,z,w) -> (z,w)',
    'sigma_pp_extreme_rays': [list(r) for r in cpp['rays']],
    'sigma_pm_extreme_rays': [list(r) for r in cpm['rays']],
    'relative_interior_boundary_witnesses': [list(boundary_pp), list(boundary_pm)],
    'sigma_pp_projected_generators': [list(r) for r in project_pp],
    'sigma_pm_projected_generators': [list(r) for r in project_pm],
    'projected_cones': ['C={(z,w):z>=0,w>=0}', 'D={(z,w):z>=w>=0}'],
    'intersection_is_face_of_C': False,
    'nonface_addition_certificate': {'u': list(u), 'v': list(v), 'u_plus_v_in_D': list(interior), 'v_not_in_D': True},
    'rational_lift_grid_pairs_checked': grid_count,
    'universal_projection_identity_justification': 'Exact extreme generators plus algebraic lift formulas, not a floating-point or finite-grid inference.',
    'counterexample_to_matroid_Theorem_1_1_or_1_2_claimed': False,
    'active_TeX_modified': False,
}
target = Path(__file__).resolve().parents[1]/'lee_boundary_projection_exact_checks_20261005.json'
encoded = json.dumps(report, indent=2, sort_keys=True)+'\n'
if target.exists():
    assert target.read_text() == encoded, 'Refusing to replace different dated evidence.'
else:
    target.write_text(encoded)
print(json.dumps({'status': 'PASS', 'distinct_cones': len(fan), 'dimension_counts': dimension_counts,
                  'cone_pairs': pair_count, 'nonface_witness': list(interior),
                  'output': str(target)}))
