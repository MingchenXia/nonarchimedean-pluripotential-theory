#!/usr/bin/env python3
"""Exact contact-set computation for supplied finite metric graphs.

This checks a finite graph theorem. It has no analytic-space implementation.
Only Python's standard library is used.
"""
import argparse
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path


def solve(matrix, rhs):
    n = len(rhs)
    a = [[Q(x) for x in row] + [Q(b)] for row, b in zip(matrix, rhs)]
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            raise ValueError('singular Dirichlet system')
        a[j], a[k] = a[k], a[j]
        c = a[j][j]
        a[j] = [x / c for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                c = a[i][j]
                a[i] = [x - c * y for x, y in zip(a[i], a[j])]
    return tuple(a[i][-1] for i in range(n))


def laplacian(n, edges):
    rows = [[Q(0) for _ in range(n)] for _ in range(n)]
    for u, v, length in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        length = Q(str(length))
        assert length > 0
        c = 1 / length
        rows[u][u] -= c
        rows[u][v] += c
        rows[v][v] -= c
        rows[v][u] += c
    return rows


def dot(row, u):
    return sum((a * b for a, b in zip(row, u)), Q(0))


def compute(example, obstacle=None):
    g = tuple(Q(str(x)) for x in (example['obstacle'] if obstacle is None else obstacle))
    n = len(g)
    boundary = frozenset(example['boundary'])
    assert boundary <= set(range(n))
    rows = laplacian(n, example['edges'])
    seen, stack = {0}, [0]
    while stack:
        v = stack.pop()
        for w in range(n):
            if w != v and rows[v][w] and w not in seen:
                seen.add(w)
                stack.append(w)
    assert len(seen) == n, 'input graph must be connected'
    interior = sorted(set(range(n)) - boundary)
    retained = []
    counts = {'enumerated_contact_sets': 0, 'retained_contact_solutions': 0}
    for bits in itertools.product((False, True), repeat=len(interior)):
        contact = set(boundary) | {v for v, bit in zip(interior, bits) if bit}
        if not contact:
            # Entire graph harmonic: the nonempty contact set needed for the
            # greatest obstacle minorant excludes this singular representation.
            continue
        counts['enumerated_contact_sets'] += 1
        matrix, rhs = [], []
        for v in range(n):
            if v in contact:
                matrix.append([Q(int(v == w)) for w in range(n)])
                rhs.append(g[v])
            else:
                matrix.append(rows[v])
                rhs.append(Q(0))
        u = solve(matrix, rhs)
        if all(u[v] <= g[v] for v in range(n)) and all(dot(rows[v], u) >= 0 for v in interior):
            retained.append((u, sorted(contact)))
    counts['retained_contact_solutions'] = len(retained)
    assert retained, 'at least the greatest contact solution must be present'
    tops = [u for u, _ in retained if all(all(w[v] <= u[v] for v in range(n)) for w, _ in retained)]
    assert tops and len(set(tops)) == 1
    p = tops[0]
    slopes = tuple(dot(row, p) for row in rows)
    assert all(p[v] <= g[v] for v in range(n))
    assert all(p[v] == g[v] for v in boundary)
    assert all(slopes[v] >= 0 for v in interior)
    assert all(p[v] == g[v] or slopes[v] == 0 for v in interior)
    if not boundary:
        assert p == (min(g),) * n
    return p, slopes, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text())
    output = {'arithmetic': 'fractions.Fraction; exact rational',
              'scope': 'exhaustive contact sets of supplied finite graphs only',
              'analytic_checks': 'none', 'examples': []}
    for example in data['examples']:
        p, slopes, counts = compute(example)
        expected = tuple(Q(str(x)) for x in example['expected'])
        assert p == expected, (example['id'], p, expected)
        # Translation stability is a substantive independent structural check.
        shift = Q(7, 3)
        shifted, _, _ = compute(example, [Q(str(x)) + shift for x in example['obstacle']])
        assert shifted == tuple(x + shift for x in p)
        output['examples'].append({
            'id': example['id'], 'greatest_vertex_values': list(map(str, p)),
            'outgoing_slope_sums': list(map(str, slopes)), **counts,
            'expected_values_match': True, 'feasible': True,
            'dominates_all_retained_contact_solutions': True,
            'complementarity': True, 'translation_check': True})
    output['passed'] = True
    Path(args.output).write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
