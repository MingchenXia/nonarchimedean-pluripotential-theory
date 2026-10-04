#!/usr/bin/env python3
"""Small exact diagnostics. These do not certify analytic theorems."""
from fractions import Fraction as Q
from itertools import product
import heapq
import json

def prufer_tree(n, sequence):
    degree = [1] * n
    for v in sequence:
        degree[v] += 1
    leaves = [v for v in range(n) if degree[v] == 1]
    heapq.heapify(leaves)
    edges = []
    for v in sequence:
        u = heapq.heappop(leaves)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heapq.heappush(leaves, v)
    edges.append(tuple(leaves))
    return edges

totals = []
for n in range(2, 7):
    cases = 0
    trees = 0
    for sequence in product(range(n), repeat=n-2):
        edges = prufer_tree(n, sequence)
        adjacency = [[] for _ in range(n)]
        for k, (u, v) in enumerate(edges):
            length = Q(k + 2, k + 1)
            adjacency[u].append((v, length))
            adjacency[v].append((u, length))
        for mask in range(1, 1 << n):
            boundary = {v for v in range(n) if mask & (1 << v)}
            root = min(boundary)
            mu = [Q(0) if v in boundary else Q(1) for v in range(n)]
            mu[root] = -sum(mu)
            parent = {root: None}
            order = [root]
            for u in order:
                for v, length in adjacency[u]:
                    if v not in parent:
                        parent[v] = (u, length)
                        order.append(v)
            subtree = list(mu)
            for v in reversed(order[1:]):
                u, _ = parent[v]
                subtree[u] += subtree[v]
            values = [Q(0)] * n
            for v in order[1:]:
                u, length = parent[v]
                values[v] = values[u] - subtree[v] * length
            laplacian = [sum((values[v] - values[u]) / length for v, length in adjacency[u]) for u in range(n)]
            assert laplacian == mu
            assert all(laplacian[v] == 1 for v in range(n) if v not in boundary)
            cases += 1
        trees += 1
    totals.append({'vertices': n, 'labelled_trees': trees, 'nonempty_boundary_cases': cases})

# Elements of Q(sqrt(2)) are pairs. sqrt(2)*q = (0,q).
# Continuity along the fixed parallel edges requires (q1,0) = (0,q2).
bound = 6
rationals = sorted({Q(a,b) for a in range(-bound,bound+1) for b in range(1,bound+1)})
solutions = [(a,b) for a,b in product(rationals, repeat=2) if (a,Q(0)) == (Q(0),b)]
assert solutions == [(Q(0),Q(0))]
for n in range(1, 101):
    bn = Q(1,4**n)
    cn = Q(5,3) * bn
    bnext = bn/4
    cnext = Q(5,3) * bnext
    assert cn-cnext == bn+bnext
    assert bn+cn == Q(8,3)*bn

print(json.dumps({'scope': 'exact finite graph/algebra diagnostics, no analytic-curve inference',
                  'tree_tests': totals,
                  'labelled_trees_total': sum(x['labelled_trees'] for x in totals),
                  'boundary_cases_total': sum(x['nonempty_boundary_cases'] for x in totals),
                  'tree_laplacian_failures': 0,
                  'rational_candidate_count': len(rationals),
                  'parallel_edge_candidate_pairs': len(rationals)**2,
                  'parallel_edge_continuous_pairs': [[str(a), str(b)] for a,b in solutions],
                  'tail_shift_exact_checks': 100,
                  'universal_claims_require_the_written_proofs': True}, indent=2))
