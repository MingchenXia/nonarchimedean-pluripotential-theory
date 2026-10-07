"""Small exact polynomial checks. These do not verify non-Archimedean analysis."""
from fractions import Fraction as F
from math import comb
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
INPUT = {
    "coefficient_dimensions": [1, 16],
    "defect_grid_dimensions": [2, 6],
    "defect_coordinates": ["0", "1", "3/2"],
    "interpretation": "formal nonnegative Dirichlet coefficients, not actual metrics",
}

def bernstein(n, j):
    p = [F(0)] * (n + 1)
    for k in range(n - j + 1):
        p[j + k] = F(comb(n, j) * comb(n - j, k) * (-1)**k)
    return p

def integral(p, a=F(0), b=F(1)):
    return sum((x * (b**(i+1) - a**(i+1)) / (i+1)
                for i, x in enumerate(p)), F(0))

def multiply(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return r

def value(p, t):
    return sum((a*t**i for i,a in enumerate(p)), F(0))

def twice_integrate_negative(p):
    return [F(0), F(0)] + [-a/F((i+1)*(i+2)) for i,a in enumerate(p)]

rows = []
for n in range(1, 17):
    alphas = []
    for j in range(n):
        p = [n*x for x in bernstein(n-1, j)]
        alpha = (integral(multiply(p, [F(0),F(1,2)]), F(0), F(1,2))
                 + integral(multiply(p, [F(1,2),F(-1,2)]), F(1,2),F(1)))
        g = twice_integrate_negative(p)
        assert alpha == value(g,F(1,2)) - (value(g,0)+value(g,1))/2
        assert integral(multiply(p,[F(1),F(-1)])) == F(n-j,n+1)
        assert integral(multiply(p,[F(0),F(1)])) == F(j+1,n+1)
        alphas.append(alpha)
    c = (1-F(1,2)**n)/F(2*(n+1))
    assert min(alphas) == c == alphas[0] == alphas[-1]
    assert alphas == alphas[::-1]
    assert sum(alphas) == F(n,8)
    for j in range(n-1):
        if 2*(j+1) <= n:
            assert alphas[j+1] >= alphas[j]
    rows.append({"n": n, "c_n": str(c), "alpha": list(map(str,alphas))})

grid_count = 0
for n in range(2,7):
    alphas = list(map(F,rows[n-1]["alpha"]))
    c = F(rows[n-1]["c_n"])
    for d in product([F(0),F(1),F(3,2)], repeat=n):
        I = sum(d)
        delta = sum(a*x for a,x in zip(alphas,d))
        left = sum(F(n-j,n+1)*d[j] for j in range(n))
        right = sum(F(j+1,n+1)*d[j] for j in range(n))
        assert left + right == I
        assert I/F(n+1) <= left <= F(n,n+1)*I
        assert c*I <= delta
        assert (delta==0) == (I==0) == all(x==0 for x in d)
        grid_count += 1

out = {
    "status": "PASS", "coefficient_rows": sum(range(1,17)),
    "dimension_rows": 16, "formal_defect_grid_rows": grid_count,
    "exact_coefficients": rows,
    "limits": "Exhaustive only for the stated finite arithmetic grids; no analytic certification.",
}
(ROOT/"finite-inputs.json").write_text(json.dumps(INPUT,indent=2)+"\n")
(ROOT/"finite-output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k!="exact_coefficients"},indent=2))
