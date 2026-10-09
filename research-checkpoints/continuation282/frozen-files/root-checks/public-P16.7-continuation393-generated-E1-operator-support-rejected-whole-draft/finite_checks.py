#!/usr/bin/env python3
"""Own small exact polynomial checks; no analytic proof is certified."""
from fractions import Fraction as F
import itertools
import json
import pathlib

O = pathlib.Path(__file__).resolve().parent

def multiply(a,b):
    c = [F(0)] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c

def lagrange(nodes):
    result = []
    for i,x in enumerate(nodes):
        p, den = [F(1)], F(1)
        for j,y in enumerate(nodes):
            if j != i:
                p = multiply(p,[-y,F(1)])
                den *= x-y
        result.append([v/den for v in p])
    return result

def derivative_at(p,x):
    return sum(F(i)*p[i]*x**(i-1) for i in range(1,len(p)))

def rank(a):
    a = [row[:] for row in a]
    r = 0
    for c in range(len(a[0])):
        pivot = next((j for j in range(r,len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r],a[pivot] = a[pivot],a[r]
        scale = a[r][c]
        a[r] = [v/scale for v in a[r]]
        for j in range(len(a)):
            if j != r:
                scale = a[j][c]
                a[j] = [v-scale*w for v,w in zip(a[j],a[r])]
        r += 1
    return r

def main():
    nodes = [F(0),F(1,3),F(2,3),F(1)]
    basis = lagrange(nodes)
    d0 = [derivative_at(p,F(0)) for p in basis]
    d1 = [derivative_at(p,F(1)) for p in basis]
    for degree in range(4):
        values = [x**degree for x in nodes]
        assert sum(w*v for w,v in zip(d0,values)) == (F(1) if degree==1 else F(0))
        assert sum(w*v for w,v in zip(d1,values)) == F(degree)
    monomials = [(a,b) for a in range(4) for b in range(4-a)]
    grid = [(F(i,3),F(j,3)) for i in range(4) for j in range(4-i)]
    matrix = [[t**a*s**b for a,b in monomials] for t,s in grid]
    assert rank(matrix) == 10
    count = 0
    for a,b,c,d,e,f in itertools.product(range(3),repeat=6):
        u = (F(a),F(b),F(c))
        v = (F(d),F(e),F(f))
        def square(x):
            return x[0]*x[2]-x[1]*x[1]
        avg = tuple((x+y)/2 for x,y in zip(u,v))
        polarization = 2*square(avg)-(square(u)+square(v))/2
        mixed = (u[0]*v[2]+v[0]*u[2]-2*u[1]*v[1])/2
        assert polarization == mixed
        count += 1
    r,delta,epsilon = F(1,4),F(1,128),F(1,1024)
    assert delta < r*r/4
    assert delta+epsilon < r*r/2
    assert max(F(0),delta-4*epsilon) < delta
    result = {'evidence_kind':'exact finite observations, not analytic correctness',
              'cubic_nodes':[str(x) for x in nodes],
              'derivative_at_zero_weights':[str(x) for x in d0],
              'derivative_at_one_weights':[str(x) for x in d1],
              'four_monomials_verified':True,
              'bivariate_total_degree_three_dimension':len(monomials),
              'simplex_grid_rank':10,
              'matrix_polarization_cases':count,
              'separation_parameter_example':{'r':str(r),'delta':str(delta),'epsilon':str(epsilon),
                'upper_boundary_term':str(delta+epsilon),'boundary_quadratic':str(r*r/2),
                'smaller_point_value':str(max(F(0),delta-4*epsilon))}}
    (O/'finite-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
