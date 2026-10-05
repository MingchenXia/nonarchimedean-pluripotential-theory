#!/usr/bin/env python3
"""Small exact finite diagnostics. These checks are not mathematical certificates."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from pathlib import Path
import json

NEG_INF = None

def emax(values):
    finite = [x for x in values if x is not None]
    return max(finite) if finite else None

def lp_ray(x, slopes):
    """Independent evaluation at all nonnegative breakpoints of the upper envelope."""
    active = [j for j in range(len(x)) if x[j] is not None]
    if not active or max(slopes[j] for j in active) < 0:
        return None
    points = {F(0)}
    for i, j in combinations(active, 2):
        if slopes[i] != slopes[j]:
            r = (x[j] - x[i]) / (slopes[i] - slopes[j])
            if r >= 0:
                points.add(r)
    return min(max(x[j] + r * slopes[j] for j in active) for r in points)

def polytope_vertices(slopes):
    vertices = []
    for j, slope in enumerate(slopes):
        if slope >= 0:
            w = [F(0)] * len(slopes)
            w[j] = F(1)
            vertices.append(w)
    for i, j in combinations(range(len(slopes)), 2):
        if slopes[i] * slopes[j] < 0:
            w = [F(0)] * len(slopes)
            w[i] = -slopes[j] / (slopes[i] - slopes[j])
            w[j] = 1 - w[i]
            vertices.append(w)
    return vertices

def vertex_value(x, w):
    if any(w[j] > 0 and x[j] is None for j in range(len(x))):
        return None
    return sum((w[j] * x[j] for j in range(len(x)) if w[j] > 0), F(0))

def main():
    counts = {"polytope": 0, "rounding": 0, "rounding_directedness_shadow": 0,
              "zero_ray": 0, "signed_zero_product": 0, "reference_mass": 0}
    for slopes in product(map(F, (-2, -1, 0, 1, 2)), repeat=3):
        if max(slopes) < 0:
            continue
        vertices = polytope_vertices(slopes)
        for x in product((None, F(-2), F(-1), F(0)), repeat=3):
            assert lp_ray(x, slopes) == emax(vertex_value(x, w) for w in vertices), (x, slopes)
            counts["polytope"] += 1
    # Direct coefficient rounding, including a common pole coordinate.
    for m in (1, 2, 3):
        for delta in (F(1, 2), F(1, 3), F(1, 5)):
            grid = m * delta / 2
            for lambdas in product((F(-3, 2), F(-1, 7), F(0), F(5, 4)), repeat=2):
                rounded = tuple(-((-z / grid).numerator // (-z / grid).denominator) * grid for z in lambdas)
                for x in product((None, F(-2), F(0)), repeat=2):
                    old = emax(xj + lj for xj, lj in zip(x, lambdas) if xj is not None)
                    new = emax(xj + lj for xj, lj in zip(x, rounded) if xj is not None)
                    if old is None:
                        assert new is None
                    else:
                        assert old / m <= new / m <= old / m + delta
                    counts["rounding"] += 1
    for phi1, phi2 in product((None, F(-2), F(0), F(1)), repeat=2):
        phi3 = None if phi1 is None or phi2 is None else min(phi1, phi2) - 1
        for d1, d2 in product((F(1, 2), F(1, 3), F(1, 5)), repeat=2):
            d3 = min(d1, d2) / 3
            for phi, d in ((phi1, d1), (phi2, d2)):
                if phi is None:
                    assert phi3 is None
                else:
                    assert phi3 is None or phi3 + 2 * d3 <= phi + d
            counts["rounding_directedness_shadow"] += 1
    ray_examples = []
    for b, c in combinations((F(1, 2), F(1), F(2), F(3)), 2):
        values = []
        for t in (F(0), b / 2, b, c, c + 1):
            ub = max(F(0), b - t) - b
            uc = max(F(0), c - t) - c
            values.append((str(t), str(ub), str(uc)))
            counts["zero_ray"] += 1
        assert any(row[1] != row[2] for row in values)
        ray_examples.append({"b": str(b), "c": str(c), "values": values})
    for n in range(1, 9):
        assert sum((-1) ** (n - j) * comb(n, j) * F(7, 3) for j in range(n + 1)) == 0
        counts["signed_zero_product"] += 1
    mass_examples = []
    for n in range(1, 6):
        for t in (F(1, 4), F(1, 2), F(3, 4), F(1)):
            mass = t ** n * F(7, 3)
            assert 0 < mass <= F(7, 3)
            if t < 1:
                assert mass < F(7, 3)
            counts["reference_mass"] += 1
            mass_examples.append({"n": n, "t": str(t), "raw_mass": str(mass)})
    report = {"status": "passed", "arithmetic": "Python fractions.Fraction exact rational",
              "domain": {"polytope_slopes": [-2, -1, 0, 1, 2],
                         "polytope_intercepts": ["-infinity", -2, -1, 0], "coordinates": 3,
                         "restriction": "at least one nonnegative slope; 117 slope tuples, 64 intercept tuples"},
              "counts": counts, "zero_ray_examples": ray_examples,
              "reference_mass_examples": mass_examples,
              "volume_growth_observations": [{"m": m, "numerical_zero_upper_bound_h0_over_m2": str(F(1, m*m)),
                                              "P1_product_h0_over_m2": str(F(m+1, m*m))} for m in (1, 2, 4, 8, 16)],
              "limits": "Exhaustive only on the declared finite diagnostic domains. No infinite net, cone, analytic product, energy, or equation theorem is certified."}
    Path("checks-output.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "counts": counts}))

if __name__ == "__main__":
    main()
