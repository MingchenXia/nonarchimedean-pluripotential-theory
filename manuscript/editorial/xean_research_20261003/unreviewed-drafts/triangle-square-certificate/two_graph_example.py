"""Small exact full divisor recursion for the actual cyclic product example.

No external libraries or solvers. Spatial coverage and envelope equality are
proved separately in P05.2-argument.md. This file checks finite coefficients.
"""
from fractions import Fraction as F
from math import gcd
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ZERO = (F(0),) * 4

def scalar(x):
    return str(x.numerator) if x.denominator == 1 else str(x)

def vec_json(x):
    return [scalar(F(v)) for v in x]

def add(x, y):
    return tuple(a+b for a, b in zip(x, y))

def scale(k, x):
    return tuple(k*a for a in x)

def lift(x, factor):
    return tuple(F(v) for v in ((tuple(x)+(0, 0)) if factor == 0
                               else ((0, 0)+tuple(x))))

GRAPH = {
    'A': {'point': (0, 0), 'g': 0,
          'directions': [(1, 0), (0, 1), (-1, -1)],
          'slopes': [1, 1, 2]},
    'B': {'point': (1, 0), 'g': 1,
          'directions': [(-1, 0), (-1, 1), (2, -1)],
          'slopes': [-1, 0, 3]},
    'C': {'point': (0, 1), 'g': 1,
          'directions': [(0, -1), (1, -1), (-1, 2)],
          'slopes': [-1, 0, 3]},
}

class Fan:
    def __init__(self):
        self.rays = {}
        self.values = {}
        self.cones = []

    def ray(self, name, vector, value):
        vector = tuple(F(v) for v in vector)
        assert any(vector)
        assert all(v.denominator == 1 for v in vector)
        common = 0
        for v in vector:
            common = gcd(common, abs(v.numerator))
        assert common == 1, ('nonprimitive ray', name, vector)
        if name in self.rays:
            assert self.rays[name] == vector and self.values[name] == value
        self.rays[name] = vector
        self.values[name] = F(value)

    def cone(self, x, y, x_coords, y_coords, basis):
        # basis is the ACTUAL saturated product plane basis: one primitive
        # graph direction in each direct factor. This is proved in the note.
        u, v = basis
        assert self.rays[x] == add(scale(F(x_coords[0]), u), scale(F(x_coords[1]), v))
        assert self.rays[y] == add(scale(F(y_coords[0]), u), scale(F(y_coords[1]), v))
        chi = abs(x_coords[0]*y_coords[1]-x_coords[1]*y_coords[0])
        assert chi > 0 and F(chi).denominator == 1
        self.cones.append({'rays': (x, y), 'index': F(chi), 'weight': F(1)})

    def recurse(self):
        divisor = {}
        tangential = {}
        for name, ray in self.rays.items():
            neighbor_sum = ZERO
            value_sum = F(0)
            for cone in self.cones:
                if name not in cone['rays']:
                    continue
                other = next(n for n in cone['rays'] if n != name)
                ratio = cone['weight']/cone['index']
                neighbor_sum = add(neighbor_sum, scale(ratio, self.rays[other]))
                value_sum += ratio*self.values[other]
            coordinate = next(i for i, v in enumerate(ray) if v)
            t = neighbor_sum[coordinate]/ray[coordinate]
            assert neighbor_sum == scale(t, ray), ('carrier not balanced', name)
            tangential[name] = t
            divisor[name] = value_sum-t*self.values[name]
        balancing = ZERO
        for name, coefficient in divisor.items():
            assert coefficient >= 0, ('negative first divisor', name, coefficient)
            balancing = add(balancing, scale(coefficient, self.rays[name]))
        assert balancing == ZERO, ('first divisor not balanced', balancing)
        mass = sum((divisor[name]*self.values[name] for name in self.rays), F(0))
        assert mass >= 0
        return {
            'rays': [{'id': name, 'ambient_primitive_vector': vec_json(ray),
                      'germ_value': scalar(self.values[name]),
                      'tangential_multiple': scalar(tangential[name]),
                      'first_divisor_weight': scalar(divisor[name])}
                     for name, ray in self.rays.items()],
            'cones': [{'rays': list(c['rays']),
                       'actual_saturated_plane_index': scalar(c['index']),
                       'weight': scalar(c['weight'])} for c in self.cones],
            'first_divisor_balancing_vector': vec_json(balancing),
            'mass': scalar(mass),
        }

def product_fan(first, second, c, flat=False):
    fan = Fan()
    ga, gb = GRAPH[first], GRAPH[second]
    for factor, data in enumerate((ga, gb)):
        for i, (direction, slope) in enumerate(zip(data['directions'], data['slopes'])):
            fan.ray(f'{factor}:{i}', lift(direction, factor), F(0) if flat else c*slope)
    for i, a in enumerate(ga['directions']):
        for j, b in enumerate(gb['directions']):
            basis = (lift(a, 0), lift(b, 1))
            fan.cone(f'0:{i}', f'1:{j}', (1, 0), (0, 1), basis)
    return fan

def cut_fan(j, c, transpose=False):
    fan = Fan()
    star_factor, line_factor = (1, 0) if transpose else (0, 1)
    direction = GRAPH['A']['directions'][j]
    b = GRAPH['A']['slopes'][j]
    z = lift(direction, line_factor)
    fan.ray('z+', z, c*b)
    fan.ray('z-', scale(F(-1), z), 0)
    for i, (direction_a, a) in enumerate(zip(GRAPH['A']['directions'], GRAPH['A']['slopes'])):
        u = lift(direction_a, star_factor)
        d = gcd(a, b)
        ridge = add(scale(F(b//d), u), scale(F(-a//d), z))
        fan.ray(f'h:{i}', u, c*a)
        fan.ray(f'R:{i}', ridge, 0)
        basis = (u, z)
        fan.cone('z-', f'R:{i}', (0, -1), (b//d, -a//d), basis)
        fan.cone(f'R:{i}', f'h:{i}', (b//d, -a//d), (1, 0), basis)
        fan.cone(f'h:{i}', 'z+', (1, 0), (0, 1), basis)
    return fan

def main():
    data = json.loads((ROOT/'example-input.json').read_text())
    c, r, eta, epsilon = (F(data[k]) for k in ('c', 'r', 'eta', 'epsilon'))
    assert c > 0 and 0 < r < 1 and eta > 0 and epsilon > 0
    stars = {}
    for label, row in GRAPH.items():
        dirs = row['directions']
        assert all(gcd(abs(a), abs(b)) == 1 for a, b in dirs)
        assert tuple(sum(x[k] for x in dirs) for k in (0, 1)) == (0, 0)
        determinants = [dirs[i][0]*dirs[j][1]-dirs[i][1]*dirs[j][0]
                        for i in range(3) for j in range(i+1, 3)]
        assert any(abs(v) == 1 for v in determinants)
        assert sum(row['slopes']) == (4 if label == 'A' else 2)
        stars[label] = {'primitive_directions': dirs,
                        'pair_determinants': determinants,
                        'kernel_dimension': 1,
                        'positive_balancing_vector': [1, 1, 1],
                        'g_divisor': sum(row['slopes'])}
    points = []
    for first in GRAPH:
        for second in GRAPH:
            flat = (first, second) == ('A', 'A')
            fan = product_fan(first, second, c, flat).recurse()
            value = c*max(F(GRAPH[first]['g']+GRAPH[second]['g']), r)
            mass = F(fan['mass'])
            expected = 0 if flat else 2*c*c*sum(GRAPH[first]['slopes'])*sum(GRAPH[second]['slopes'])
            assert mass == expected
            gap = eta*r if flat else F(0)
            points.append({'label': first+','+second,
                           'point': vec_json(tuple(GRAPH[first]['point'])+tuple(GRAPH[second]['point'])),
                           'H': scalar(value), 'f': scalar(value+gap), 'H_minus_f': scalar(-gap),
                           'mass': scalar(mass), 'full_recursion': fan})
    for j, (direction, b) in enumerate(zip(GRAPH['A']['directions'], GRAPH['A']['slopes'])):
        q = tuple((r/b)*v for v in direction)
        for transpose in (False, True):
            fan = cut_fan(j, c, transpose).recurse()
            assert F(fan['mass']) == 4*c*c*b
            point = q+(F(0), F(0)) if transpose else (F(0), F(0))+q
            points.append({'label': f'Q{j+1},A' if transpose else f'A,Q{j+1}',
                           'point': vec_json(point), 'H': scalar(c*r), 'f': scalar(c*r),
                           'H_minus_f': '0', 'mass': fan['mass'], 'full_recursion': fan})
    points.append({'label': 'M,M', 'point': ['1/2']*4, 'H': scalar(2*c),
                   'f': scalar(2*c+epsilon/2), 'H_minus_f': scalar(-epsilon/2),
                   'mass': '0', 'full_recursion': {
                       'reason': 'H is ambient constant on an ordinary neighborhood; all divisor terms vanish.'}})
    total = sum((F(p['mass']) for p in points), F(0))
    integral = sum((F(p['mass'])*F(p['H_minus_f']) for p in points), F(0))
    assert total == 128*c*c and integral == 0
    max_index = max(F(cone['actual_saturated_plane_index']) for p in points
                    for cone in p['full_recursion'].get('cones', []))
    pcc_endpoints = [tuple((r/b)*v for v in direction)+(F(0), F(0))
                     for direction, b in zip(GRAPH['A']['directions'], GRAPH['A']['slopes'])]
    pcc_coefficients = (F(1, 4), F(1, 4), F(1, 2))
    barycentre = ZERO
    for a, point in zip(pcc_coefficients, pcc_endpoints):
        barycentre = add(barycentre, scale(a, point))
    assert barycentre == ZERO
    output = {
        'scope': 'Exact finite arithmetic for the actual PA family. Envelope equality and spatial coverage are separate mathematical proofs.',
        'input': data, 'factor_stars': stars,
        'tested_points': points,
        'tested_count': len(points),
        'positive_atoms': sum(F(p['mass']) > 0 for p in points),
        'negative_first_divisor_weights': 0,
        'maximum_actual_cone_index': scalar(max_index),
        'total_mass': scalar(total),
        'reference_mass_from_direct_product_recursion': scalar(2*(8*c)**2),
        'complete_contact_integral': scalar(integral),
        'envelope_mixed_difference': scalar(c*r),
        'obstacle_mixed_difference': scalar(epsilon/2),
        'noncontact_product_junction_tight_PCC': {
            'centre': vec_json(ZERO), 'endpoints': [vec_json(p) for p in pcc_endpoints],
            'coefficients': [scalar(a) for a in pcc_coefficients],
            'endpoint_H_and_f': [scalar(c*r)]*3,
            'centre_H': scalar(c*r), 'centre_f': scalar((c+eta)*r),
            'exact_barycentre': vec_json(barycentre),
            'actual_cofaces': 'three candidate flat edges Q1-A, Q2-A, Q3-A incident to (A,A)'},
        'failed_bilinear_interpolation': {
            'domain': 'actual AB times AB rectangle, primitive coordinates',
            'rational_endpoints': [[0, 1], [1, 0]], 'real_coefficients': ['1/2', '1/2'],
            'rational_centre': ['1/2', '1/2'],
            'q_centre': '1/4', 'weighted_endpoint_value': '0',
            'conclusion': 'same-cell PCC violated; diagnostic only, not a PA envelope or a contact obstruction.'},
    }
    (ROOT/'two-graph-output.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: output[k] for k in ('tested_count', 'positive_atoms',
                    'maximum_actual_cone_index', 'total_mass', 'complete_contact_integral')}))

if __name__ == '__main__':
    main()
