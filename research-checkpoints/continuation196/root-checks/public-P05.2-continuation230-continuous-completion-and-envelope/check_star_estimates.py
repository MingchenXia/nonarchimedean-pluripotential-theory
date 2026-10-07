"""Exact finite checks of the displayed barycentric identities; not a proof solver."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, t):
    return tuple(t * x for x in a)


def vsum(items, d):
    result = (F(0),) * d
    for a in items:
        result = add(result, a)
    return result


def main():
    inp = json.loads(Path('star-input.json').read_text())
    grid = [F(i, inp['grid_denominator']) for i in inp['grid_numerators']]
    results = []
    for ex in inp['examples']:
        z = tuple(map(F, ex['anchor']))
        d = len(z)
        v = [tuple(map(F, a)) for a in ex['generators']]
        lam = tuple(map(F, ex['lambda']))
        eps, const = F(ex['epsilon']), F(ex['C'])
        assert all(a > 0 for a in lam)
        assert vsum([scale(a, t) for a, t in zip(v, lam)], d) == (F(0),) * d
        zi = [add(z, scale(a, eps)) for a in v]
        if 'germ_lengths' in ex:
            assert all(eps <= F(length) for length in ex['germ_lengths'])

        def value(point, variant):
            x = tuple(a - b for a, b in zip(point, z))
            if ex['norm'] == 'l1':
                norm = sum(map(abs, x))
            else:
                coords = x + (F(0),)
                norm = max(coords) - min(coords)
            return norm if variant == 0 else norm - 2 * x[0] + x[-1] / 3

        count = jensen = 0
        max_B = F(0)
        for cone in ex['cones']:
            for entries in product(grid, repeat=len(cone)):
                a = [F(0)] * len(v)
                for i, entry in zip(cone, entries):
                    a[i] = entry
                displacement = vsum([scale(vi, ai) for vi, ai in zip(v, a)], d)
                y = add(z, displacement)
                norm = max(map(abs, displacement))
                A = sum(a)
                assert A <= eps
                assert A <= const * norm
                # Upper endpoints with positive coefficients are generators of this cone.
                assert all(ai == 0 or i in cone for i, ai in enumerate(a))
                upper = vsum([scale(z, 1-A/eps)] + [scale(p, ai/eps) for p, ai in zip(zi, a)], d)
                assert upper == y
                t = max(ai/li for ai, li in zip(a, lam))
                b = [(t*li-ai)/eps for ai, li in zip(a, lam)]
                assert all(bi >= 0 for bi in b)
                B = sum(b)
                H = const * sum(lam) / (eps * min(lam))
                assert B <= H * norm
                lower = vsum([scale(y, 1/(1+B))] + [scale(p, bi/(1+B)) for p, bi in zip(zi, b)], d)
                assert lower == z
                if 'germ_lengths' in ex:
                    assert all(ai <= F(ex['germ_lengths'][i]) for i, ai in enumerate(a))
                for variant in (0, 1):
                    qz, qy = value(z, variant), value(y, variant)
                    qi = [value(p, variant) for p in zi]
                    m, M = min([qz, qy] + qi), max([qz, qy] + qi)
                    upper_value = (1-A/eps)*qz + sum(ai/eps*val for ai, val in zip(a, qi))
                    lower_value = (qy + sum(bi*val for bi, val in zip(b, qi))) / (1+B)
                    assert qy <= upper_value
                    assert qz <= lower_value
                    assert qy-qz <= (M-m)*A/eps
                    assert qy-qz >= -(M-m)*B
                    L = const/eps * max(F(1), sum(lam)/min(lam))
                    assert abs(qy-qz) <= (M-m)*L*norm
                    jensen += 1
                max_B = max(max_B, B)
                count += 1
        results.append({'name':ex['name'], 'barycentric_cases':count,
                        'convex_function_cases':jensen, 'max_other_coefficient_sum':str(max_B),
                        'status':'passed'})
    output = {'scope':'Exhaustive only for the specified finite lists; no continuum theorem or MA domain certified.',
              'examples':results, 'total_barycentric_cases':sum(x['barycentric_cases'] for x in results),
              'total_convex_function_cases':sum(x['convex_function_cases'] for x in results)}
    Path('evidence/star-check-output.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
