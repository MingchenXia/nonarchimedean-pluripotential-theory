"""Exact finite checks for the book-external determinant repair candidate.

The output is guarded: do not overwrite or rerun an already recorded check.
These finite calculations do not certify a principal convergence theorem.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json
import sympy as sp

output = Path(__file__).with_suffix('.json')
assert not output.exists(), 'A successful record already exists; do not rerun.'
t = sp.Symbol('t')


def order(expr):
    numerator, denominator = sp.fraction(sp.cancel(expr))
    assert numerator != 0
    lowest = lambda p: min(mon[0] for mon, coefficient in sp.Poly(p, t).terms() if coefficient)
    return lowest(numerator) - lowest(denominator)


matrices = [
    sp.Matrix([[1, 0], [0, 1], [1, 1], [1, t]]),
    sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1],
               [1, t, t**2], [t, 1, 1], [1, 1+t, t]]),
    sp.Matrix([[1/t, 0], [0, t], [1, 1], [1, 1+t], [t**2, 1]]),
]
records = []
coefficient_identities = weight_cases = selected_basis_cases = 0
for matrix in matrices:
    q, d = matrix.shape
    bases = []
    for indices in combinations(range(q), d):
        square = matrix[list(indices), :]
        determinant = sp.cancel(square.det())
        if determinant == 0:
            continue
        inverse = square.inv()
        coefficients = matrix * inverse
        for j in range(q):
            for position in range(d):
                replaced = square.copy()
                replaced[position, :] = matrix[j, :]
                assert sp.cancel(coefficients[j, position] - replaced.det()/determinant) == 0
                coefficient_identities += 1
        bases.append((indices, order(determinant), coefficients))
    assert bases
    matrix_record = {'matrix': str(matrix), 'nonzero_maximal_minors': len(bases),
                     'weight_cases': 0, 'selected_minimum_bases': 0}
    for a in range(1, 6):
        for b in range(4):
            for denominator in (1, 3, 7):
                weights = [Fraction((a*(j+1)+b*j*j) % 11 - 5, denominator)
                           for j in range(q)]
                costs = [Fraction(v)-sum(weights[i] for i in indices)
                         for indices, v, _ in bases]
                minimum = min(costs)
                for (indices, _, coefficients), cost in zip(bases, costs):
                    if cost != minimum:
                        continue
                    selected_basis_cases += 1
                    matrix_record['selected_minimum_bases'] += 1
                    for j in range(q):
                        for position, i in enumerate(indices):
                            coefficient = sp.cancel(coefficients[j, position])
                            if coefficient != 0:
                                assert Fraction(order(coefficient))+weights[i]-weights[j] >= 0
                weight_cases += 1
                matrix_record['weight_cases'] += 1
    records.append(matrix_record)

# Independent polynomial-truncation check of the source quotient collapse.
# Two different coordinate increases each retain the other basis direction.
collapse_cases = 0
for exponents in ((0, 0), (0, 2), (3, 1), (2, 4)):
    cutoff = max(exponents) + 5
    ambient = 2 * cutoff
    def generators(increased):
        vectors = []
        for i, initial in enumerate(exponents):
            for degree in range(initial + (i == increased), cutoff):
                vector = [0] * ambient
                vector[i * cutoff + degree] = 1
                vectors.append(vector)
        return vectors
    original = generators(None)
    higher_sum = generators(0) + generators(1)
    assert sp.Matrix.hstack(*map(sp.Matrix, higher_sum)).rank() == len(original)
    collapse_cases += 1

result = {'status': 'PASS_EXACT_FINITE_CHECKS', 'sympy_version': sp.__version__,
          'scope': 'Fixed symbolic matrices and finite weight/truncation cases only; no universal proof or independent principal-theorem verdict.',
          'cramer_coefficient_identities': coefficient_identities,
          'rational_weight_cases': weight_cases,
          'selected_minimum_basis_cases': selected_basis_cases,
          'common_basis_quotient_collapse_cases': collapse_cases,
          'matrices': records}
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
