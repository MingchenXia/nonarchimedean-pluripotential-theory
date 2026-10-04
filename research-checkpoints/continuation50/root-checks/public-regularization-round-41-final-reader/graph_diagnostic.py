#!/usr/bin/env python3
"""Exact finite star examples; not a proof about analytic regularization."""
from fractions import Fraction as Q
import json
from pathlib import Path

weights = [1, 2, 2]
slopes = [Q(-3, 2), Q(1, 2), Q(1, 4)]
corners = [Q(1, 3), Q(2, 5), Q(3, 7)]
jumps = [Q(7, 3), Q(4, 5), Q(9, 7)]

def potential(e, t):
    return slopes[e] * t + jumps[e] * max(Q(0), t - corners[e])

def chord(e, n, t):
    mesh_size = 2 ** (n + 5)
    if t == 1:
        return potential(e, t)
    i = int(t * mesh_size)
    left, right = Q(i, mesh_size), Q(i+1, mesh_size)
    return ((right-t)*potential(e, left)+(t-left)*potential(e, right))/(right-left)

records = []
previous = None
for n in range(1, 9):
    size = 2 ** (n + 5)
    central_mass = sum(weights[e] * (chord(e,n,Q(1,size))-chord(e,n,Q(0))) * size
                       for e in range(3))
    minimum_new_mass = None
    maximum_error = Q(0)
    maximum_increase = None
    for e in range(3):
        for i in range(1, size):
            t = Q(i, size)
            mass = weights[e] * size * (chord(e,n,t+Q(1,size))
                                        - 2*chord(e,n,t) + chord(e,n,t-Q(1,size)))
            minimum_new_mass = mass if minimum_new_mass is None else min(minimum_new_mass,mass)
        check_points = set(Q(i,size) for i in range(size+1)) | {corners[e]}
        if previous is not None:
            check_points |= set(Q(i,2**(previous+5)) for i in range(2**(previous+5)+1))
        for t in check_points:
            error = chord(e,n,t)-potential(e,t)
            assert error >= 0
            maximum_error = max(maximum_error,error)
            if previous is not None:
                # f_n = F+2^-n, g_n = chord_n(F)+2^-n, q_n = g_n+2^-n.
                difference = chord(e,n,t)+Q(2,2**n)-chord(e,previous,t)-Q(2,2**previous)
                maximum_increase = difference if maximum_increase is None else max(maximum_increase,difference)
    assert central_mass >= 0 and minimum_new_mass >= 0
    assert maximum_error <= Q(1,2**n)
    assert maximum_increase is None or maximum_increase <= 0
    records.append({'n':n, 'segments_per_arm':size, 'central_weighted_mass':str(central_mass),
                    'minimum_new_weighted_mass':str(minimum_new_mass),
                    'maximum_chord_error':str(maximum_error),
                    'maximum_shifted_interstage_increase':None if maximum_increase is None else str(maximum_increase)})
    previous=n

output = {'kind':'exhaustive exact rational checks of the displayed eight finite examples only',
          'weights':weights, 'initial_slopes':list(map(str,slopes)),
          'corners':list(map(str,corners)), 'positive_jumps':list(map(str,jumps)),
          'initial_central_weighted_mass':str(sum(weights[e]*slopes[e] for e in range(3))),
          'method':'An affine difference attains its extremum at a union-of-breakpoints vertex; '
                   'all such vertices are checked for each finite graph.',
          'records':records, 'checks_passed':True,
          'limits':'This does not certify analytic PL membership or the general mathematical theorem.'}
out = Path(__file__).resolve().parent / 'diagnostics'
out.mkdir(exist_ok=True)
(out/'graph-output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
