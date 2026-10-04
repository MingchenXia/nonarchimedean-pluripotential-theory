#!/usr/bin/env python3
"""Small exact checks on specified rational trees, not theorem verification."""
from fractions import Fraction as Q
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
edges = [(0, 1, Q(3, 2)), (1, 2, Q(1, 3)),
         (1, 3, Q(2, 5)), (0, 4, Q(7, 4))]
nodes = list(range(5))
parent = {v: (u, length) for u, v, length in edges}

def path(v):
    out = []
    while v != 0:
        u, length = parent[v]
        out.append((u, v, length))
        v = u
    return out[::-1]

paths = {v: path(v) for v in nodes}
K = [[sum((e[2] for e in paths[x] if e in paths[y]), Q(0))
      for y in nodes] for x in nodes]

def potential(mass):
    return [sum((K[x][y]*mass[y] for y in nodes), Q(0)) for x in nodes]

def laplacian(values):
    # Independent weighted graph computation: outward slopes.
    out = [Q(0) for _ in nodes]
    for a, b, length in edges:
        slope = (values[b]-values[a])/length
        out[a] += slope
        out[b] -= slope
    return out

def dirichlet(a, b):
    return sum(((a[y]-a[x])*(b[y]-b[x])/length
                for x, y, length in edges), Q(0))

def pairing(values, measure):
    return sum((a*b for a, b in zip(values, measure)), Q(0))

def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, list):
        return [encode(v) for v in value]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    return value

d = Q(2)
mu = [Q(1, 5), Q(1, 7), Q(2, 3), Q(4, 9), Q(0)]
mu[4] = d-sum(mu)
nu = [Q(1, 3), Q(1, 4), Q(1, 2), Q(2, 7), Q(0)]
nu[4] = d-sum(nu)
assert min(mu+nu) >= 0
p = potential(mu)
q = potential(nu)
u = [-v for v in p]
v = [Q(2, 5)-value for value in q]
theta = [d, Q(0), Q(0), Q(0), Q(0)]
curvature = [a+b for a, b in zip(laplacian(u), theta)]
assert curvature == mu
assert sum(curvature) == d
I = pairing(p, mu)
assert I == dirichlet(p, p)
assert pairing(q, mu) == dirichlet(p, q)
assert pairing(u, laplacian(v)) == -dirichlet(u, v)
E = (pairing(u, mu)+d*u[0])/2
assert E == -I/2
b = [vv-uu for vv, uu in zip(v, u)]
derivative = d*b[0]-dirichlet(u, b)
assert derivative == pairing(b, mu)

# Rooted projection F={0,1,4}: leaves 2 and 3 are collapsed onto 1.
projected = [mu[0], mu[1]+mu[2]+mu[3], Q(0), Q(0), mu[4]]
pF = potential(projected)
assert pF[2] == pF[1] == pF[3]
IF = pairing(pF, projected)
assert pairing(pF, mu) == IF
assert dirichlet(pF, p) == IF
tail = [a-b for a, b in zip(p, pF)]
assert dirichlet(tail, tail) == I-IF
assert -IF/2 + pairing(pF, mu) == IF/2

# Check the comparison identity on the set of edges after inserting breakpoints
# w=0 and w=epsilon, rather than only checking vertices.
w = [vv-uu for vv, uu in zip(v, u)]
epsilon = Q(1, 3)
eta = [min(Q(1), max(Q(0), ww/epsilon)) for ww in w]
nonnegative_pair = Q(0)
for x, y, length in edges:
    lo, hi = sorted([w[x], w[y]])
    if lo == hi:
        continue
    active = max(Q(0), min(hi, epsilon)-max(lo, Q(0)))
    nonnegative_pair += (hi-lo)*active/(length*epsilon)
lhs = pairing(eta, [nn-mm for nn, mm in zip(nu, mu)])
assert lhs == -nonnegative_pair <= 0

truncations = []
for N in [1, 2, 3, 10, 100]:
    masses = [d/Q(j*(j+1)) for j in range(1, N)] + [d/Q(N)]
    tail_masses = [sum(masses[j-1:]) for j in range(1, N+1)]
    assert tail_masses == [d/Q(j) for j in range(1, N+1)]
    kernel_integral = sum((Q(min(j, k))*masses[j-1]*masses[k-1]
                           for j in range(1, N+1) for k in range(1, N+1)), Q(0))
    expected = d*d*sum((Q(1, j*j) for j in range(1, N+1)), Q(0))
    endpoint = -sum((Q(j)*masses[j-1] for j in range(1, N+1)), Q(0))
    assert sum(masses) == d
    assert kernel_integral == expected
    assert endpoint == -d*sum((Q(1, j) for j in range(1, N+1)), Q(0))
    truncations.append({'N': N, 'raw_mass': str(d),
                        'I_over_d_squared': str(expected/(d*d)),
                        'minus_u_endpoint_over_d': str(-endpoint/d)})

report = {'kind': 'Exact finite observations on one branched rational tree and five finite ray truncations.',
          'limitations': 'Neither exhaustive over all trees nor a mathematical proof of the infinite/analytic theorem.',
          'edges': encode(edges), 'mu': encode(mu), 'nu': encode(nu),
          'kernel_matrix': encode(K), 'p_mu': encode(p), 'MA_u': encode(curvature),
          'I_mu': str(I), 'E_u': str(E), 'I_projection': str(IF),
          'directional_derivative': str(derivative),
          'comparison_cutoff_integral': str(lhs),
          'unbounded_example_truncations': truncations,
          'passed': ['raw curvature mass', 'kernel versus weighted Laplacian sign',
                     'kernel versus Dirichlet energy', 'integration by parts',
                     'energy derivative', 'orthogonal projection energy identity',
                     'dual-energy test value', 'comparison contraction identity',
                     'five exact ray truncation identities']}
(ROOT/'finite-tree-output.json').write_text(json.dumps(report, indent=2, default=str)+'\n')
print('PASS: 9 groups of exact checks; mass d=2, five-node branched tree, N=1,2,3,10,100.')
print('I(mu) =', I, '; E(u) =', E, '; I(projection) =', IF)
print('Directional derivative =', derivative, '; comparison cutoff integral =', lhs)
