#!/usr/bin/env python3
"""Small exact-arithmetic diagnostics, never mathematical proof certificates."""
from fractions import Fraction as F
from itertools import product
import json


def vertices(slopes):
    out = []
    for j, a in enumerate(slopes):
        if a >= 0:
            w = [F(0)] * len(slopes)
            w[j] = F(1)
            out.append(w)
    for j, a in enumerate(slopes):
        for k, b in enumerate(slopes):
            if a > 0 and b < 0:
                w = [F(0)] * len(slopes)
                w[j], w[k] = F(-b, a-b), F(a, a-b)
                out.append(w)
    return out


def projected_left(values, slopes):
    visible = [j for j, x in enumerate(values) if x is not None]
    if not visible or max(slopes[j] for j in visible) < 0:
        return None
    breaks = {F(0)}
    for j in visible:
        for k in visible:
            if slopes[j] != slopes[k]:
                r = F(values[k]-values[j], slopes[j]-slopes[k])
                if r >= 0:
                    breaks.add(r)
    candidates = [max(F(values[j])+r*slopes[j] for j in visible) for r in breaks]
    if max(slopes[j] for j in visible) == 0:
        candidates.append(max(F(values[j]) for j in visible if slopes[j] == 0))
    return min(candidates)


def projected_right(values, slopes):
    results = []
    for w in vertices(slopes):
        if all(values[j] is not None for j in range(len(w)) if w[j]):
            results.append(sum(w[j]*values[j] for j in range(len(w)) if w[j]))
    return max(results) if results else None


def determinant(columns):
    a, b, c = columns
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - b[0]*(a[1]*c[2]-a[2]*c[1])
            + c[0]*(a[1]*b[2]-a[2]*b[1]))


def main():
    cases = 0
    for slopes in product([-1, 0, 1], repeat=3):
        if max(slopes) < 0:
            continue
        for values in product([-2, -1, 0, 1, 2, None], repeat=3):
            lhs, rhs = projected_left(values, slopes), projected_right(values, slopes)
            assert lhs == rhs, (values, slopes, lhs, rhs)
            cases += 1
    rays = {
        1: (1, 0, 0), 2: (0, 1, 0), 3: (0, 0, 1), 4: (-1, -1, -1),
        5: (0, -1, -1), 6: (-1, 0, -1), 7: (-1, -1, 0),
    }
    cones = [(1,2,3),(1,2,5),(2,5,6),(4,5,6),(2,3,6),
             (3,6,7),(4,6,7),(1,3,7),(1,5,7),(4,5,7)]
    dets = {''.join(map(str, c)): determinant([rays[j] for j in c]) for c in cones}
    assert all(abs(d) == 1 for d in dets.values())
    walls = [[1,-1,0,0,-1,1,0], [0,1,-1,0,0,-1,1], [-1,0,1,0,1,0,-1]]
    wall_sum = [sum(row[j] for row in walls) for j in range(7)]
    assert wall_sum == [0]*7
    coefficients = [F(1,i)-F(1,i*i) for i in range(2,8)]
    assert all(coefficients[i+1] < coefficients[i] for i in range(len(coefficients)-1))
    result = {
        'kind': 'finite exact-arithmetic diagnostic only',
        'homogeneous_projection': {
            'cases': cases, 'slopes': [-1,0,1],
            'values': [-2,-1,0,1,2,'minus infinity'], 'matches': cases,
            'limitations': 'Only three branches in the displayed finite grid; the paper proves the general formula separately.',
        },
        'toric_determinants': dets,
        'wall_degree_coefficient_sum': wall_sum,
        'quotient_coefficients_at_indices_2_through_7': [str(c) for c in coefficients],
        'negative_sigma_quotients': 'These decrease in coefficient and therefore increase in value; quotient monotonicity fails.',
        'proof_status': 'No computation certifies the paper, the local bridge, or P16.2.',
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
