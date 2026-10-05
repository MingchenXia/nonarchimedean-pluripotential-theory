"""Exact rational fan and tropical Borel--Moore complex diagnostic.

This computation concerns one explicit research example, not a general proof,
and never edits active TeX or changes an admission status.
"""

from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json


def rref(rows, columns):
    a = [[F(x) for x in row] for row in rows]
    pivots = []
    k = 0
    for j in range(columns):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        divisor = a[k][j]
        a[k] = [x/divisor for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                scale = a[i][j]
                a[i] = [x-scale*y for x, y in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
    return a, pivots


def nullspace(rows, columns):
    a, pivots = rref(rows, columns)
    out = []
    for j in range(columns):
        if j not in pivots:
            v = [F(0)]*columns
            v[j] = F(1)
            for i, p in enumerate(pivots):
                v[p] = -a[i][j]
            out.append(v)
    return out


def basis(vectors):
    if not vectors:
        return []
    rows = [[v[i] for v in vectors] for i in range(len(vectors[0]))]
    _, pivots = rref(rows, len(vectors))
    return [vectors[i] for i in pivots]


def coefficients(v, b):
    if not b:
        assert not any(v)
        return []
    rows = [[w[i] for w in b]+[v[i]] for i in range(len(v))]
    a, pivots = rref(rows, len(b))
    assert len(pivots) == len(b)
    assert not any(not any(row[:-1]) and row[-1] for row in a)
    return [a[i][-1] for i in range(len(b))]


def positively_collinear(v, w):
    k = next(i for i, x in enumerate(w) if x)
    ratio = F(v[k], w[k])
    return ratio > 0 and all(F(x) == ratio*y for x, y in zip(v, w))


ed = Path(__file__).resolve().parents[1]
input_path = ed / 'arroid_projection_exact_checks_20261005.json'
source = json.loads(input_path.read_text())
degrees = source['degrees']
points = [(tuple(row['point']), row['multiplicity']) for row in source['incidence_data']]
assert degrees == [1,1,1,1,2,2]


def quotient(v):
    return [v[j]-v[0]*degrees[j] for j in range(1,6)]


rays = []
for j in range(6):
    rays.append({'key': ('divisor',j), 'v': quotient([int(k == j) for k in range(6)])})
for p, weight in points:
    rays.append({'key': ('point',p), 'v': quotient([int(k in p) for k in range(6)])})
ray_index = {r['key']: i for i, r in enumerate(rays)}
assert len(rays) == 22
assert all(not positively_collinear(r['v'],s['v']) for r,s in combinations(rays,2))
facets = []
for p, weight in points:
    for j in p:
        indices = [ray_index[('divisor',j)],ray_index[('point',p)]]
        facets.append({'rays': indices, 'divisor': j, 'point': p, 'weight': weight,
                       'u': rays[indices[0]]['v'], 'v': rays[indices[1]]['v']})
assert len(facets) == 33

# Check every cone-pair intersection, not only the abstract incidence graph.
# Extreme rays of {a,b,c,d >=0 : a*u+b*v=c*s+d*t} have a minimal
# positive support with a one-dimensional nullspace.  Enumerate all supports.
intersection_pairs = 0
positive_circuits = 0
for left,right in combinations(facets,2):
    columns = [left['u'],left['v'],[-x for x in right['u']],[-x for x in right['v']]]
    shared = set(left['rays']) & set(right['rays'])
    assert len(shared) <= 1
    for size in range(1,5):
        for support in combinations(range(4),size):
            rows = [[columns[j][i] for j in support] for i in range(5)]
            ker = nullspace(rows,size)
            if len(ker) != 1:
                continue
            w = ker[0]
            if all(x < 0 for x in w):
                w = [-x for x in w]
            if not all(x > 0 for x in w):
                continue
            full = [F(0)]*4
            for i,j in enumerate(support):
                full[j] = w[i]
            image = [full[0]*left['u'][i]+full[1]*left['v'][i] for i in range(5)]
            assert any(image), 'Facets must be pointed and have no positive zero circuit'
            assert shared, 'Unexpected cone intersection outside a common face'
            assert positively_collinear(image,rays[next(iter(shared))]['v'])
            positive_circuits += 1
    intersection_pairs += 1
assert intersection_pairs == 528


def wedge(u,v):
    return [u[i]*v[j]-u[j]*v[i] for i,j in combinations(range(5),2)]


def multiply(a,b):
    assert len(a[0]) == len(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


checks = []
for p in range(3):
    facet_bases = []
    for facet in facets:
        if p == 0:
            facet_bases.append([[1]])
        elif p == 1:
            facet_bases.append([facet['u'],facet['v']])
        else:
            facet_bases.append([wedge(facet['u'],facet['v'])])
    ray_bases = [basis([w for k,f in enumerate(facets) if r in f['rays'] for w in facet_bases[k]]) for r in range(len(rays))]
    origin_basis = basis([w for b in facet_bases for w in b])
    facet_offsets = []
    ray_offsets = []
    n2 = n1 = 0
    for b in facet_bases:
        facet_offsets.append(n2)
        n2 += len(b)
    for b in ray_bases:
        ray_offsets.append(n1)
        n1 += len(b)
    n0 = len(origin_basis)
    d2 = [[F(0)]*n2 for _ in range(n1)]
    d1 = [[F(0)]*n1 for _ in range(n0)]
    for k,facet in enumerate(facets):
        for slot,r in enumerate(facet['rays']):
            sign = 1 if slot == 0 else -1
            for j,v in enumerate(facet_bases[k]):
                for i,c in enumerate(coefficients(v,ray_bases[r])):
                    d2[ray_offsets[r]+i][facet_offsets[k]+j] += sign*c
    for r,b in enumerate(ray_bases):
        for j,v in enumerate(b):
            for i,c in enumerate(coefficients(v,origin_basis)):
                d1[i][ray_offsets[r]+j] = -c
    assert not any(x for row in multiply(d1,d2) for x in row)
    rank2 = len(rref(d2,n2)[1])
    rank1 = len(rref(d1,n1)[1])
    dimensions = [n0-rank1,n1-rank1-rank2,n2-rank2]
    assert dimensions[:2] == [0,0]
    if p == 2:
        beta = [F(degrees[f['point'][0]]*degrees[f['point'][1]]) if len(f['point']) == 2 else F(0) for f in facets]
        gamma = [F(1) if len(f['point']) == 3 else F(-1) if set(f['point']) <= {3,4,5} else F(0) for f in facets]
        assert all(sum(x*y for x,y in zip(row,beta)) == 0 for row in d2)
        assert all(sum(x*y for x,y in zip(row,gamma)) == 0 for row in d2)
        assert all(b+c == f['weight'] for b,c,f in zip(beta,gamma,facets))
        assert len(basis([beta,gamma])) == dimensions[2] == 2
    checks.append({'p':p,'chain_dimensions_q_0_1_2':[n0,n1,n2],
                   'boundary_ranks_q_1_2':[rank1,rank2],
                   'BM_homology_dimensions_q_0_1_2':dimensions,
                   'ordinary_tropical_H_p_0_dimension':n0,
                   'd1_d2_zero':True,
                   'ray_multitangent_dimensions':[len(b) for b in ray_bases]})
assert [r['BM_homology_dimensions_q_0_1_2'][2] for r in checks] == [12,8,2]
assert [r['ordinary_tropical_H_p_0_dimension'] for r in checks] == [1,5,10]
record = {
    'scope':'Exact rational cellular-complex computation for one research example; not an independent production-model receipt or general theorem.',
    'input':{'path':str(input_path),'sha256':hashlib.sha256(input_path.read_bytes()).hexdigest()},
    'ambient_lattice_rank':5,'ray_cells':22,'two_dimensional_cones':33,
    'all_cone_pair_intersections_checked':intersection_pairs,
    'minimal_positive_circuits_checked':positive_circuits,
    'all_cone_pair_intersections_are_common_faces':True,
    'rational_coefficients':True,
    'orientation':'Each facet oriented by (e_j,v_p); + at e_j, - at v_p; each ray has - incidence at the origin.',
    'complexes':checks,
    'BM_homology_below_top_q_vanishes_in_this_example':True,
    'global_Poincare_duality_fails_by_dimensions':True,
    'Poincare_dual_dimension_pairs':[[1,2],[5,8],[10,12]],
    'global_top_balancing_space_dimension':2,
    'top_balancing_parameters':'Pair weights beta*d_i*d_j, subtract gamma on the three pairs among M,C,D; triple weight gamma.',
    'actual_weights':'beta=gamma=1',
    'all_weights_strictly_positive_condition':'beta>0 and 0<gamma<2*beta',
    'Lemma_5_1_counterexample_in_this_example':False,
    'general_Lemma_5_1_proved':False,
    'Theorem_5_4_or_6_2_counterexample_claimed':False,
    'active_TeX_or_inventory_modified':False,
}
path = ed / 'arroid_bm_complex_exact_checks_20261005.json'
if path.exists():
    assert json.loads(path.read_text()) == record, 'Refuse to overwrite different dated evidence'
else:
    path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'output':str(path),'cone_pair_checks':intersection_pairs,
                  'BM_top_dimensions':[12,8,2],'ordinary_dimensions':[1,5,10],
                  'all_differentials_compose_to_zero':True,'exact_checks_passed':True}))
