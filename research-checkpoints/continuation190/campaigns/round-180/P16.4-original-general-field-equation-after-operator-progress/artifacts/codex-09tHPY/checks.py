#!/usr/bin/env python3
"""Small exact checks. These do not certify an analytic theorem."""
from fractions import Fraction as Q
from itertools import product, combinations
from math import factorial
from pathlib import Path
import json


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first,) + rest


def polarization():
    records = []
    for n in range(1, 8):
        sets = [set(I) for r in range(1, n + 1)
                for I in combinations(range(n), r)]
        mass = sum(Q((-1) ** (n - len(I)) * len(I) ** n, factorial(n))
                   for I in sets)
        assert mass == 1
        count = 0
        for e in compositions(n, n):
            labels = {j for j, x in enumerate(e) if x}
            multinomial = Q(factorial(n), 1)
            for x in e:
                multinomial /= factorial(x)
            coefficient = sum(Q((-1) ** (n - len(I)), factorial(n))
                              * multinomial for I in sets if labels <= I)
            assert coefficient == (1 if e == (1,) * n else 0)
            count += 1
        c = Q((n + 1) ** (n + 1), factorial(n))
        selected = Q(factorial(n), (n + 1) ** (n + 2))
        assert c * selected == Q(1, n + 1)
        assert Q(2 ** (n + 1) * (n + 1)) * Q(1, 2 ** (n + 1)) == n + 1
        records.append({"dimension": n, "monomials_exhausted": count,
                        "polarization_mass": str(mass),
                        "selected_integrability_coefficient": str(selected),
                        "integrability_constant": str(c)})
    return records


def interp(u, x):
    # Specified metric tree is the length-two interval with vertices 0,1,2.
    if x == 2:
        return u[2]
    j = int(x)
    return u[j] + (x - j) * (u[j + 1] - u[j])


def measure(u):
    # Reference atoms have weight one at each vertex: raw mass V=3.
    return {Q(0): 1 + u[1] - u[0],
            Q(1): 1 + u[0] + u[2] - 2 * u[1],
            Q(2): 1 + u[1] - u[2]}


def max_measure(u, v):
    points = {Q(0), Q(1), Q(2)}
    for j in (0, 1):
        d0, d1 = u[j] - v[j], u[j + 1] - v[j + 1]
        if d0 * d1 < 0:
            points.add(Q(j) + d0 / (d0 - d1))
    pts = sorted(points)
    values = [max(interp(u, x), interp(v, x)) for x in pts]
    slopes = [(values[j + 1] - values[j]) / (pts[j + 1] - pts[j])
              for j in range(len(pts) - 1)]
    out = {}
    for j, x in enumerate(pts):
        mass = Q(1) if x in (0, 1, 2) else Q(0)
        if j:
            mass -= slopes[j - 1]
        if j < len(slopes):
            mass += slopes[j]
        out[x] = mass
    return out


def metric_tree():
    all_inputs = [tuple(map(Q, u)) for u in product(range(-2, 3), repeat=3)]
    valid = [u for u in all_inputs if min(measure(u).values()) >= 0]
    pairs = crossings = 0
    for u in valid:
        mu = measure(u)
        for v in valid:
            mv = measure(v)
            mm = max_measure(u, v)
            assert sum(mm.values()) == 3 and min(mm.values()) >= 0
            crossings += len(mm) - 3
            for x in set(mu) | set(mv) | set(mm):
                if interp(u, x) > interp(v, x):
                    assert mm.get(x, 0) == mu.get(x, 0)
                if interp(v, x) > interp(u, x):
                    assert mm.get(x, 0) == mv.get(x, 0)
            lv = sum(m for x, m in mv.items() if interp(u, x) < interp(v, x))
            lu = sum(m for x, m in mu.items() if interp(u, x) < interp(v, x))
            assert lv <= lu
            # Check the epsilon mass-complement argument with nonintegral ties.
            for eps in (Q(1, 2), Q(1), Q(3, 2)):
                ve = tuple(x - eps for x in v)
                me = max_measure(u, ve)
                A = lambda x: interp(u, x) < interp(ve, x)
                B = lambda x: interp(u, x) > interp(ve, x)
                left = sum(m for x, m in mv.items() if A(x))
                assert left == sum(m for x, m in me.items() if A(x))
                assert left <= 3 - sum(m for x, m in me.items() if B(x))
                assert sum(m for x, m in me.items() if B(x)) == sum(m for x, m in mu.items() if B(x))
                assert left <= lu
            pairs += 1
    return {"tree": "interval [0,2], unit edges, reference atoms 1 at 0,1,2",
            "raw_mass": 3, "all_nodal_inputs": len(all_inputs),
            "positive_curvature_inputs": len(valid), "ordered_pairs_exhausted": pairs,
            "inserted_strict_crossings_total": crossings,
            "epsilon_values": ["1/2", "1", "3/2"]}


def cutoff():
    def chi(x, e):
        return max(Q(0), min(Q(1), x / e))
    count = 0
    for a, b, r, s, e in product(map(Q, range(-2, 3)), map(Q, range(-2, 3)),
                                (Q(0), Q(1, 2), Q(1)), (Q(0), Q(1, 2), Q(1)),
                                (Q(1, 4), Q(1, 2), Q(1))):
        assert abs(chi(a + r - b - s, e) - chi(a - b, e)) <= (r + s) / e
        count += 1
    return {"rational_cases_exhausted": count,
            "epsilon_values": ["1/4", "1/2", "1"],
            "bound": "abs(chi_e(a+r-b-s)-chi_e(a-b)) <= (r+s)/e"}


def main():
    result = {"status": "PASS", "evidence_type": "exhaustive finite algebra/model checks",
              "analytic_theorem_certified": False, "polarization": polarization(),
              "metric_tree": metric_tree(), "cutoff": cutoff()}
    Path('check-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
