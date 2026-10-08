"""Own bounded standard-library exact checks; no source/emitter execution."""
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path


def det(a):
    if not a:
        return F(1)
    return sum(((-1) ** j) * a[0][j] * det([r[:j] + r[j + 1:] for r in a[1:]])
               for j in range(len(a)))


def egcd(a, b):
    if b == 0:
        return abs(a), (1 if a >= 0 else -1), 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def recurse(rows):
    """Kernel bases from unimodular column operations, with primitive lifts."""
    d = len(rows[0])
    cols = [[int(i == j) for i in range(d)] for j in range(d)]
    mass = F(1)
    trace = []
    for row in rows:
        den = math.lcm(*(x.denominator for x in row))
        integral = [int(x * den) for x in row]
        if not cols or all(dot(integral, col) == 0 for col in cols):
            trace.append({"zero_restriction": True})
            return F(0), trace
        for j in range(1, len(cols)):
            a, b = dot(integral, cols[0]), dot(integral, cols[j])
            if a == b == 0:
                continue
            g, s, t = egcd(a, b)
            old0, oldj = cols[0], cols[j]
            cols[0] = [s * x + t * y for x, y in zip(old0, oldj)]
            cols[j] = [(-b // g) * x + (a // g) * y for x, y in zip(old0, oldj)]
        value = dot(integral, cols[0])
        if value < 0:
            cols[0] = [-x for x in cols[0]]
            value = -value
        assert value > 0
        assert all(dot(integral, col) == 0 for col in cols[1:])
        factor = F(2 * value, den)
        mass *= factor
        trace.append({"denominator": den, "primitive_lift": cols[0],
                      "integral_evaluation": value, "factor": str(factor),
                      "saturated_kernel_basis": cols[1:]})
        cols = cols[1:]
    return mass, trace


def rref_solve(a, b):
    m = [[F(x) for x in row] + [F(y)] for row, y in zip(a, b)]
    n = len(a[0])
    pivot_row = 0
    pivots = []
    for j in range(n):
        k = next((k for k in range(pivot_row, len(m)) if m[k][j]), None)
        if k is None:
            continue
        m[pivot_row], m[k] = m[k], m[pivot_row]
        val = m[pivot_row][j]
        m[pivot_row] = [x / val for x in m[pivot_row]]
        for k in range(len(m)):
            if k != pivot_row:
                val = m[k][j]
                m[k] = [x - val * y for x, y in zip(m[k], m[pivot_row])]
        pivots.append(j)
        pivot_row += 1
    assert all(any(row[:n]) or not row[n] for row in m)
    assert len(pivots) == n
    sol = [F(0)] * n
    for k, j in enumerate(pivots):
        sol[j] = m[k][n]
    return sol


data = json.loads(Path("certificate-input.json").read_text())
out = {"kind": "exhaustive only for the listed finite exact inputs", "matrices": []}
for case in data["matrices"]:
    rows = [[F(x) for x in row] for row in case["rows"]]
    d = len(rows)
    determinant = det(rows)
    expected = 2 ** d * abs(determinant)
    orders = []
    for perm in itertools.permutations(range(d)):
        mass, trace = recurse([rows[j] for j in perm])
        assert mass == expected
        orders.append({"order": perm, "mixed_mass": str(mass), "trace": trace})
    sum_words = F(0)
    repeat_count = 0
    for word in itertools.product(range(d), repeat=d):
        mass, trace = recurse([rows[j] for j in word])
        if len(set(word)) < d:
            assert mass == 0
            repeat_count += 1
        sum_words += mass
    assert sum_words == math.factorial(d) * expected
    out["matrices"].append({"id": case["id"], "det": str(determinant),
                            "ordered_permutations": orders,
                            "repeated_words_zero": repeat_count,
                            "all_words": d ** d, "raw_sum_mass": str(sum_words)})

a = [F(1, 2), F(0), F(0), F(0)]
b = [F(0), F(0), F(1, 2), F(0)]
c = [F(-1, 2), F(0), F(-1, 2), F(0)]
assert [x + y + z for x, y, z in zip(a, b, c)] == [0] * 4
values = [abs(a[0] - 1) + abs(a[1]) - 1,
          abs(b[2] - 1) + abs(b[3]) - 1,
          abs(c[0]) + abs(c[1])]
assert values == [F(-1, 2), F(-1, 2), F(1, 2)]
assert sum(values) / 3 == F(-1, 6)
out["dependent_PCC"] = {"values": list(map(str, values)), "barycenter": ["0"] * 4,
                         "average": "-1/6", "origin": "0"}

# Q_i = origin_i + column basis_i. The third translated plane has three distinct meetings.
origins = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
bases = [[[1, 0, 0, 0], [0, 1, 0, 0]],
         [[0, 0, 1, 0], [0, 0, 0, 1]],
         [[1, 0, 1, 0], [0, 1, 0, 1]]]
meetings = []
for i, j in itertools.combinations(range(3), 2):
    matrix = [[bases[i][k][h] for k in range(2)] + [-bases[j][k][h] for k in range(2)]
              for h in range(4)]
    assert det([[F(x) for x in row] for row in matrix]) != 0
    rhs = [origins[j][h] - origins[i][h] for h in range(4)]
    solution = rref_solve(matrix, rhs)
    point = [F(origins[i][h]) + sum(solution[k] * bases[i][k][h] for k in range(2))
             for h in range(4)]
    meetings.append({"pair": [i + 1, j + 1], "point": list(map(str, point))})
assert len({tuple(x["point"]) for x in meetings}) == 3
out["distinct_meetings"] = meetings

extraction = []
for n in data["dyadic_n"]:
    eta = F(1, 2 ** n)
    assert 5 * eta / 2 < 4 * eta
    extraction.append({"n": n, "upper_next": str(5 * eta / 2),
                       "lower_current": str(4 * eta), "drop_at_least": str(3 * eta / 2)})
out["extraction_finite_list"] = extraction

# f(x)=x^2/2 on [-1,1], and |x|-1/2 on its tails. Exact chord error.
mesh = []
for n in data["quadratic_mesh_N"]:
    xs = [F(-1) + F(j, n) for j in range(2 * n + 1)]
    ys = [x * x / 2 for x in xs]
    slopes = [(ys[j + 1] - ys[j]) / (xs[j + 1] - xs[j]) for j in range(len(xs) - 1)]
    assert slopes == sorted(slopes) and slopes[0] >= -1 and slopes[-1] <= 1
    for j in range(len(slopes)):
        for t in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
            x = xs[j] + t * (xs[j + 1] - xs[j])
            chord = ys[j] + slopes[j] * (x - xs[j])
            error = chord - x * x / 2
            assert error == (x - xs[j]) * (xs[j + 1] - x) / 2
            assert 0 <= error <= F(1, 8 * n * n)
    mesh.append({"N": n, "rational_samples": len(xs), "global_error_formula": str(F(1, 8 * n * n)),
                 "tails_exact": True, "every_sample_touched": True})
out["chord_example"] = mesh
out["status"] = "PASS for the finite lists; not a continuum certificate"
Path("certificate-output.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"status": out["status"], "matrix_cases": len(out["matrices"]),
                  "mixed_permutations": sum(len(x["ordered_permutations"]) for x in out["matrices"]),
                  "all_words": sum(x["all_words"] for x in out["matrices"]),
                  "repeated_words_zero": sum(x["repeated_words_zero"] for x in out["matrices"]),
                  "PCC_average": "-1/6", "distinct_meetings": meetings}, indent=2))
