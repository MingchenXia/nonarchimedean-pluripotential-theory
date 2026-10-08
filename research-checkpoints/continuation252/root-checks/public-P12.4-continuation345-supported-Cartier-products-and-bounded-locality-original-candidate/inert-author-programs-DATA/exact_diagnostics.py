"""Owned exact finite Newton arithmetic. Does not import supplied programs."""
from pathlib import Path
from fractions import Fraction
from math import gcd
import hashlib
import json

OUT = Path(__file__).resolve().parent

def ideal(points):
    pts = set(tuple(x) for x in points)
    return tuple(sorted(p for p in pts if not any(q != p and q[0] <= p[0] and q[1] <= p[1] for q in pts)))

def hull(points):
    result = []
    for p in sorted(points):
        while len(result) >= 2:
            a, b = result[-2:]
            cross = (b[0]-a[0])*(p[1]-b[1])-(b[1]-a[1])*(p[0]-b[0])
            if cross > 0:
                break
            result.pop()
        result.append(p)
    return result

def atoms(points):
    h = hull(points)
    mu = {}
    for a, b in zip(h, h[1:]):
        dx, dy = b[0]-a[0], a[1]-b[1]
        g = gcd(dx, dy)
        nx, ny = dy//g, dx//g
        scale = min(nx, ny)
        if scale <= 0:
            raise ValueError((a, b))
        nu = (Fraction(nx, scale), Fraction(ny, scale))
        mu[nu] = mu.get(nu, 0) + g*scale
    return mu

def gauge(points, nu):
    return min(x*nu[0]+y*nu[1] for x, y in points)

def pair(points, test):
    return sum(weight*gauge(test, nu) for nu, weight in atoms(points).items())

def area2(points):
    p = [(0,0)] + hull(points) + [(0,0)]
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:])))

def product(a, b):
    return ideal((x+u, y+v) for x,y in a for u,v in b)

def main():
    spec = json.loads((OUT/'bounded-evidence-input.json').read_text())
    ideals = set()
    for a in spec['axis_exponents']:
        for b in spec['axis_exponents']:
            for extra in spec['optional_generators']:
                ideals.add(ideal([(a,0),(0,b)] + ([] if extra is None else [extra])))
    ideals = sorted(ideals)
    counts = {'diagonal': 0, 'symmetry': 0, 'mixed_area': 0, 'product_atoms': 0, 'strict_maximum': 0}
    failures = []
    def check(kind, condition, data):
        counts[kind] += 1
        if not condition:
            failures.append({'kind': kind, 'data': data})
    for i, a in enumerate(ideals):
        check('diagonal', pair(a,a) == area2(a), [i])
        for j, b in enumerate(ideals):
            ab = product(a,b)
            check('symmetry', pair(a,b) == pair(b,a), [i,j])
            check('mixed_area', 2*pair(a,b) == area2(ab)-area2(a)-area2(b), [i,j])
            ma, mb, mp = atoms(a), atoms(b), atoms(ab)
            expected = {nu: ma.get(nu,0)+mb.get(nu,0) for nu in set(ma)|set(mb)}
            check('product_atoms', mp == expected, [i,j])
            mm = atoms(ideal(a+b))
            strict = [nu for nu in set(ma)|set(mm) if gauge(a,nu) < gauge(b,nu)]
            check('strict_maximum', all(ma.get(nu,0) == mm.get(nu,0) for nu in strict), [i,j])
    residue = []
    for d in [2,3,5]:
        for r in [1,2,4]:
            lengths = [1+d*(r*N-1) for N in [1,2,3]]
            residue.append({'d':d,'r':r,'lengths':lengths,'first_difference':lengths[1]-lengths[0]})
    report = {'status': 'PASS' if not failures else 'FAIL', 'distinct_ideals': len(ideals),
              'counts': counts, 'failures': failures, 'residue_arithmetic': residue,
              'polynomial_warning': {'at_2_3': (2-3)**2, 'st_coefficient': -2},
              'scope': spec['domain'], 'universal_proof_claim': False,
              'input_sha256': hashlib.sha256((OUT/'bounded-evidence-input.json').read_bytes()).hexdigest(),
              'ideal_input_list': ideals}
    (OUT/'reports'/'exact-diagnostics.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','distinct_ideals','counts','failures']}))

if __name__ == '__main__':
    main()
