"""Exact finite coordinate diagnostics, not a proof certificate."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

RAYS = {1: (1, 0, 0), 2: (0, 1, 0), 3: (0, 0, 1),
        4: (-1, -1, -1), 5: (0, -1, -1),
        6: (-1, 0, -1), 7: (-1, -1, 0)}
CONES = [(1, 2, 3), (1, 2, 5), (2, 5, 6), (4, 5, 6),
         (2, 3, 6), (3, 6, 7), (4, 6, 7), (1, 3, 7),
         (1, 5, 7), (4, 5, 7)]

def det(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -b[0]*(a[1]*c[2]-a[2]*c[1])
            +c[0]*(a[1]*b[2]-a[2]*b[1]))

def add(a, b):
    return tuple(x+y for x, y in zip(a, b))

determinants = {''.join(map(str, c)): det(*(RAYS[i] for i in c)) for c in CONES}
relations = []
for wall, sides, rhs in [((2, 5), (1, 6), (2, 5)),
                         ((3, 6), (2, 7), (3, 6)),
                         ((1, 7), (3, 5), (1, 7))]:
    adjacent = [c for c in CONES if set(wall) <= set(c)]
    vector = [int(i in sides)-int(i in rhs) for i in range(1, 8)]
    relations.append(dict(wall=wall, adjacent=adjacent, sides=sides, rhs=rhs,
                          equality=add(*(RAYS[i] for i in sides)) == add(*(RAYS[i] for i in rhs)),
                          degree_coefficients=vector))
sum_coefficients = [sum(r['degree_coefficients'][i] for r in relations) for i in range(7)]
division_values = []
for i in range(2, 9):
    sigma = Fraction(-1)
    h = (1-Fraction(1, i*i))*sigma
    t = 1-Fraction(1, i)
    divided = h-t*sigma
    division_values.append(dict(i=i, h=str(h), t=str(t), divided=str(divided)))

result = dict(kind='exhaustive exact finite coordinate checks, not mathematical certification',
              rays=RAYS, cones=CONES, determinants=determinants,
              all_unimodular=all(abs(v)==1 for v in determinants.values()),
              wall_relations=relations, sum_degree_coefficients=sum_coefficients,
              division_diagnostic_at_sigma_minus_one=division_values,
              scope_limit='No program proves fan coverage, toric properness, local MA compatibility, or P16.2.')
assert result['all_unimodular']
assert all(r['equality'] and len(r['adjacent'])==2 for r in relations)
assert sum_coefficients == [0]*7
out = Path(__file__).resolve().parent / 'diagnostic-output.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
