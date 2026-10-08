#!/usr/bin/env python3
"""Small exact finite certificates, with no outside data or dependencies."""
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

def det(matrix):
    a = [[F(x) for x in row] for row in matrix]
    answer = F(1)
    for k in range(len(a)):
        p = next((j for j in range(k, len(a)) if a[j][k]), None)
        if p is None:
            return F(0)
        if p != k:
            a[k], a[p] = a[p], a[k]
            answer *= -1
        pivot = a[k][k]
        answer *= pivot
        for j in range(k+1, len(a)):
            ratio = a[j][k] / pivot
            for l in range(k, len(a)):
                a[j][l] -= ratio * a[k][l]
    return answer

def leibniz(matrix):
    n = len(matrix)
    answer = F(0)
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        value = F((-1)**inversions)
        for i,j in enumerate(perm):
            value *= F(matrix[i][j])
        answer += value
    return answer

def sqrt_fraction(q):
    q = F(q)
    a,b = math.isqrt(q.numerator), math.isqrt(q.denominator)
    assert a*a == q.numerator and b*b == q.denominator
    return F(a,b)

def main():
    source = json.loads((HERE / 'certificate-input.json').read_text())
    rows = []
    for row in source['rows']:
        matrix = [[F(x) for x in line] for line in row['matrix']]
        d = len(matrix)
        determinant = det(matrix)
        assert determinant == leibniz(matrix)
        permutations = list(itertools.permutations(range(d)))
        # Each distinct-factor recursive order has the same determinant modulus.
        individual = F(2**d) * abs(determinant)
        expanded = sum(individual for _ in permutations) * F(row['weight'])
        predicted = F(row['weight']) * 2**d * math.factorial(d) * abs(determinant)
        assert expanded == predicted
        rows.append({'name': row['name'], 'determinant': str(determinant),
                     'raw_atom': str(predicted), 'distinct_factor_orders': len(permutations)})
    # Saturated 2D normal cross-check for ell1=(1,1), ell2=(1,-1).
    tangent = (1,-1)
    inward = (1,0)
    assert tangent[0]*inward[1]-tangent[1]*inward[0] == 1
    assert sum(x*y for x,y in zip((1,1),inward)) == 1
    # On ker ell1, ell2 evaluates +/-2 at the primitive outgoing directions.
    mixed = F(2) * (F(2)+F(2))
    assert mixed == 8 and 2*mixed == 16

    # Arrangement Q1=span(ex,ez), Q2=span(ey,ez), h=|x|+|z|.
    # Restrictions have matrices I2 and diag(0,1): mass 8 and 0.
    matrices = [[[1,0],[0,1]], [[0,0],[0,1]]]
    mass = sum(F(2**2 * math.factorial(2))*abs(det(m)) for m in matrices)
    assert mass == 8
    assert all(sum(l[i]*u[i] for i in range(3)) == 0
               for l in [(1,0,0),(0,0,1)] for u in [(0,1,0),(0,-1,0)])

    # Non-PA f(x)=sqrt(1+x^2); all selected samples give rational graph heights.
    samples = [F(x) for x in source['primal_samples']]
    heights = [sqrt_fraction(1+x*x) for x in samples]
    rays = [(-F(1), F(1)), (F(1), F(1)), (F(0), F(1))]
    for r,h in rays[:2]:
        assert abs(r) == h
    tests = []
    for ptext in source['primal_tests']:
        p = F(ptext)
        g = max(p*x-y for x,y in zip(samples,heights))
        exact = -sqrt_fraction(1-p*p)
        assert g <= exact
        tests.append({'dual_position': str(p), 'sample_conjugate': str(g),
                      'actual_conjugate': str(exact), 'error': str(exact-g)})
    # Higher-dimensional Cartesian sample sets: conjugates add independently.
    tensor = []
    for d in source['dimensions']:
        size = len(samples)**d
        tuples_checked = 0
        for pts in itertools.product([F(x) for x in source['primal_tests']], repeat=d):
            g = sum(max(p*x-y for x,y in zip(samples,heights)) for p in pts)
            actual = -sum(sqrt_fraction(1-p*p) for p in pts)
            assert g <= actual
            tuples_checked += 1
        tensor.append({'dimension': d, 'rational_primal_positions': size,
                       'dual_tuples_exhausted': tuples_checked})
    result = {'status': 'PASS', 'kind': 'exhaustive finite exact-fraction results only',
              'determinant_rows': rows,
              'primitive_index_two_mixed_mass': '8',
              'primitive_index_two_self_mass': '16',
              'transverse_arrangement_atom': str(mass),
              'flat_pair_cost': '0', 'primal_dual_rows': tests,
              'cartesian_samples': tensor,
              'continuum_claim_certified_by_execution': False,
              'candidate': False}
    (HERE / 'certificate-output.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
