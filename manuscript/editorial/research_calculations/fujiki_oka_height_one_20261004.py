#!/usr/bin/env python3
"""Exact finite check of Sato--Sato v4, Example 3.10.

This checks one known toric example; it certifies no general resolution
criterion, no nontoric obstruction and no new open-problem solution.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def determinant(matrix):
    a = [list(map(F, row)) for row in matrix]
    result = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        value = a[i][i]
        result *= value
        for j in range(i + 1, len(a)):
            factor = a[j][i] / value
            for k in range(i + 1, len(a)):
                a[j][k] -= factor * a[i][k]
    return result


def columns(vectors):
    return [[v[i] for v in vectors] for i in range(len(vectors))]


def coordinates(basis, vector):
    matrix = columns(basis)
    denominator = determinant(matrix)
    assert denominator
    result = []
    for i in range(len(basis)):
        replaced = [row[:] for row in matrix]
        for j in range(len(basis)):
            replaced[j][i] = vector[j]
        result.append(determinant(replaced) / denominator)
    return result


def main():
    weights = (1, 2, 4, 8)
    index = 15
    rays = {
        f'E{i + 1}': tuple(F(i == j) for j in range(4))
        for i in range(4)
    }
    for j in (1, 2, 4, 8):
        rays[f'Q{j}'] = tuple(F(j * a % index, index) for a in weights)
    assert all(sum(v) == 1 for v in rays.values())
    for j in (1, 2, 4, 8):
        assert all((x - j * y).denominator == 1
                   for x, y in zip(rays[f'Q{j}'], rays['Q1']))

    cones = {('E1', 'E2', 'E3', 'E4')}
    stages = []
    for name in ('Q1', 'Q2', 'Q4', 'Q8'):
        refined = set()
        affected = 0
        for cone in sorted(cones):
            c = coordinates([rays[x] for x in cone], rays[name])
            positive = [i for i, x in enumerate(c) if x > 0]
            if all(x >= 0 for x in c) and len(positive) >= 2:
                affected += 1
                for i in positive:
                    replacement = list(cone)
                    replacement[i] = name
                    refined.add(tuple(sorted(replacement)))
            else:
                refined.add(cone)
        cones = refined
        multiplicities = [index * abs(determinant(columns([rays[x] for x in c])))
                          for c in sorted(cones)]
        assert all(x.denominator == 1 and x > 0 for x in multiplicities)
        assert sum(multiplicities) == index
        stages.append({'inserted_ray': name, 'affected_maximal_cones': affected,
                       'maximal_cones': len(cones),
                       'lattice_multiplicities': list(map(int, multiplicities))})
    assert len(cones) == 15
    assert all(index * abs(determinant(columns([rays[x] for x in c]))) == 1
               for c in cones)

    # An explicit rational upper-concave lifting checks coherence as well
    # as basicness. Each maximal cell's plane lies strictly above every
    # vertex outside that cell.
    lifting = {f'E{i + 1}': F(0) for i in range(4)}
    lifting.update({'Q1': F(1), 'Q2': F(1, 8) + F(1, 2**10),
                    'Q4': F(1, 4) + F(1, 2**20),
                    'Q8': F(1, 2) + F(1, 2**30)})
    certificates = []
    for cone in sorted(cones):
        basis = [rays[x] for x in cone]
        values = [lifting[x] for x in cone]
        slacks = {}
        for name, vector in rays.items():
            c = coordinates(basis, vector)
            slack = sum(x * y for x, y in zip(c, values)) - lifting[name]
            assert slack == 0 if name in cone else slack > 0
            slacks[name] = str(slack)
        certificates.append({'cone': list(cone), 'support_plane_slacks': slacks})

    terms = []
    queue = [((), weights, index)]
    while queue:
        path, numerator, denominator = queue.pop()
        assert sum(numerator) == denominator
        terms.append({'word': list(path), 'numerator': list(numerator),
                      'denominator': denominator, 'age': 1})
        for i in range(1, 4):
            d = numerator[i]
            if d == 0:
                continue
            remainder = tuple((-denominator if k == i else a) % d
                              for k, a in enumerate(numerator))
            if any(remainder):
                assert d < denominator
                queue.append((path + (i + 1,), remainder, d))
    terms.sort(key=lambda t: (len(t['word']), t['word']))
    assert len(terms) == 8
    result = {
        'status': 'PASS_EXACT_KNOWN_EXAMPLE',
        'source': 'Sato--Sato arXiv:2004.03522v4, Example 3.10, physical page 12',
        'group_order': index, 'weights': list(weights),
        'rays': {k: list(map(str, v)) for k, v in rays.items()},
        'all_ray_heights': 1, 'ray_lattice_membership_verified': True,
        'star_subdivision_order': ['Q1', 'Q2', 'Q4', 'Q8'],
        'stages': stages, 'final_maximal_cones': [list(c) for c in sorted(cones)],
        'final_cones': 15, 'all_final_lattice_multiplicities': 1,
        'lifting_heights': {k: str(v) for k, v in lifting.items()},
        'coherence_certificate': certificates,
        'all_120_support_inequalities_exactly_verified': True,
        'remainder_polynomial_terms': terms,
        'scope': 'One exact fan and remainder polynomial; no general algorithm or nontoric claim.',
        'new_independent_model_verification': False,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'stages', 'final_cones',
                     'all_final_lattice_multiplicities', 'lifting_heights',
                     'all_120_support_inequalities_exactly_verified',
                     'remainder_polynomial_terms']}, indent=2))


if __name__ == '__main__':
    main()
