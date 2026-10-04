"""Exact finite primitive-normal diagnostics; no universal certification."""
from fractions import Fraction as F
from functools import reduce
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import json


def determinant(matrix):
    a = [[F(x) for x in row] for row in matrix]
    out = F(1)
    for k in range(len(a)):
        j = next((j for j in range(k, len(a)) if a[j][k]), None)
        if j is None:
            return F(0)
        if j != k:
            a[j], a[k] = a[k], a[j]
            out = -out
        v = a[k][k]
        out *= v
        for j in range(k + 1, len(a)):
            t = a[j][k] / v
            a[j] = [x - t * y for x, y in zip(a[j], a[k])]
    return out


def check_factor(factor):
    rays, rel, groups = factor['rays'], factor['relation'], factor['groups']
    dim = len(rays[0])
    assert len(rays) == dim + 1
    assert all(reduce(gcd, map(abs, v)) == 1 for v in rays)
    assert reduce(gcd, rel) == 1 and min(rel) > 0
    assert all(sum(rel[i] * rays[i][k] for i in range(len(rays))) == 0 for k in range(dim))
    minors = [abs(int(determinant([[rays[i][k] for i in subset] for k in range(dim)])))
              for subset in combinations(range(len(rays)), dim)]
    assert any(minors), 'The relation kernel must be one-dimensional.'
    assert sorted(i for g in groups for i in g) == list(range(len(rays)))
    assert len(groups) == 3 and all(groups)
    sums = [sum(rel[i] for i in group) for group in groups]
    labels = {i: k for k, group in enumerate(groups) for i in group}
    nu = [(1, 0), (0, 1), (-1, -1)]
    projected = [tuple(F(x, sums[labels[i]]) for x in nu[labels[i]]) for i in range(len(rays))]
    assert all(sum(rel[i] * projected[i][k] for i in range(len(rays))) == 0 for k in range(2))
    return sums, labels, reduce(gcd, minors)


def run(example):
    first, second = example['first'], example['second']
    S, I, first_index = check_factor(first)
    T, J, second_index = check_factor(second)
    v, w = first['rays'], second['rays']
    lam, mu = first['relation'], second['relation']
    n1, n2 = len(v[0]), len(w[0])
    dim = n1 + n2
    c = [1, 1, 2]
    rays = {}
    cones = []
    for i, vi in enumerate(v):
        rays[f'a{i}'] = {'vector': tuple(vi + [0]*n2), 'h': F(c[I[i]], S[I[i]])}
    for j, wj in enumerate(w):
        rays[f'b{j}'] = {'vector': tuple([0]*n1 + wj), 'h': F(c[J[j]], T[J[j]])}
    for i in range(len(v)):
        for j in range(len(w)):
            omega = F(lam[i]*mu[j])
            if I[i] != J[j]:
                cones.append({'r': f'a{i}', 's': f'b{j}', 'index': 1, 'omega': omega})
            else:
                q, p = F(1, S[I[i]]), F(1, T[J[j]])
                D = lcm(q.denominator, p.denominator)
                Q, P = int(D*q), int(D*p)
                g = gcd(Q, P)
                dr = f'd{i}_{j}'
                vector = tuple(P//g*x for x in v[i]) + tuple(Q//g*x for x in w[j])
                assert reduce(gcd, map(abs, vector)) == 1
                rays[dr] = {'vector': vector, 'h': F(0)}
                cones.append({'r': f'a{i}', 's': dr, 'index': Q//g, 'omega': omega})
                cones.append({'r': f'b{j}', 's': dr, 'index': P//g, 'omega': omega})
    for name, ray in rays.items():
        vector = ray['vector']
        neighbors = []
        normal_sum = [F(0) for _ in range(dim)]
        first_term = F(0)
        for cone in cones:
            if name not in (cone['r'], cone['s']):
                continue
            other = cone['s'] if cone['r'] == name else cone['r']
            ratio = cone['omega'] / cone['index']
            neighbors.append({'ray': other, 'index': cone['index'], 'weight_over_index': ratio})
            normal_sum = [x + ratio*y for x, y in zip(normal_sum, rays[other]['vector'])]
            first_term += ratio * rays[other]['h']
        nz = next(k for k,x in enumerate(vector) if x)
        tangent = normal_sum[nz] / vector[nz]
        assert all(normal_sum[k] == tangent*vector[k] for k in range(dim))
        weight = first_term - tangent*ray['h']
        assert weight >= 0
        ray.update(neighbors=neighbors, tangent=tangent, first_weight=weight)
        if name.startswith('a'):
            i = int(name[1:])
            assert weight == lam[i]*(4-2*c[I[i]])
        elif name.startswith('b'):
            j = int(name[1:])
            assert weight == mu[j]*(4-2*c[J[j]])
        else:
            i,j = map(int,name[1:].split('_'))
            q,p = F(1,S[I[i]]),F(1,T[J[j]])
            D=lcm(q.denominator,p.denominator)
            g=gcd(int(D*q),int(D*p))
            assert weight == F(2*c[I[i]]*lam[i]*mu[j]*g,D)
    assert all(sum(r['first_weight']*r['vector'][k] for r in rays.values()) == 0 for k in range(dim))
    mass = sum(r['first_weight']*r['h'] for r in rays.values())
    assert mass == 8
    # Rational original-product PCC with tau=1 for a purely local arithmetic check.
    endpoints = []
    for k in range(3):
        for i in first['groups'][k]:
            for j in second['groups'][k]:
                alpha = F(lam[i]*mu[j],3*S[k]*T[k])
                z = tuple(S[k]*x for x in v[i])+tuple(T[k]*x for x in w[j])
                endpoints.append({'alpha':alpha,'vector':z})
    assert sum(z['alpha'] for z in endpoints) == 1
    assert all(sum(z['alpha']*z['vector'][k] for z in endpoints) == 0 for k in range(dim))
    return {'name':example['name'],'first_ray_generated_index_in_actual_span':first_index,
            'second_ray_generated_index_in_actual_span':second_index,'group_relation_sums':[S,T],
            'top_cones':len(cones),'rays':len(rays),'max_actual_cone_index':max(c['index'] for c in cones),
            'normalized_complete_second_coefficient':mass,'symbolic_actual_coefficient':'8*a*b',
            'top_balancing':True,'first_nonnegative':True,'first_balancing':True,'pcc_barycentre':True,
            'cones':cones,'ray_data':rays,'pcc_endpoints':endpoints}


def encode(x):
    if isinstance(x,F):
        return str(x)
    raise TypeError(type(x))


if __name__ == '__main__':
    inputs = json.loads(Path('local-input.json').read_text())
    outputs = [run(e) for e in inputs['examples']]
    result = {'kind':'exhaustive finite local calculation for two specified inputs only',
              'interpretation':'Not global domain enumeration and not mathematical certification.',
              'examples':outputs}
    Path('local-output.json').write_text(json.dumps(result,default=encode,indent=2)+'\n')
    for out in outputs:
        print(json.dumps({k:v for k,v in out.items() if k not in ('cones','ray_data','pcc_endpoints')},default=encode))
