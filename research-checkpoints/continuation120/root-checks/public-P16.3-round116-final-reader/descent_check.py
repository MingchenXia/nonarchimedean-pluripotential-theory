#!/usr/bin/env python3
"""Exact arithmetic for the proven intersection example in the paper.

This checks the displayed coefficients, not algebraic geometry or general descent.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

epsilon = Q(1, 2)
volume = Q(4)
ma_u = [volume-epsilon**2, epsilon**2, Q(0)]
ma_gu = [volume-epsilon**2, Q(0), epsilon**2]
mixed = [volume, Q(0), Q(0)]
averaged_target = [(a+b)/2 for a,b in zip(ma_u, ma_gu)]
ma_averaged_metric = [(a+2*c+b)/4 for a,b,c in zip(ma_u, ma_gu, mixed)]
difference = [a-b for a,b in zip(ma_averaged_metric, averaged_target)]
assert all(x >= 0 for row in [ma_u, ma_gu, mixed, averaged_target, ma_averaged_metric] for x in row)
assert all(sum(row)==volume for row in [ma_u, ma_gu, mixed, averaged_target, ma_averaged_metric])
assert difference == [Q(1,8), Q(-1,16), Q(-1,16)]
assert sum(difference) == 0 and any(difference)
results = {'arithmetic': 'Python fractions.Fraction; exact rational operations',
           'vertices': ['strict special fiber S', 'exceptional E1', 'exceptional E2'],
           'epsilon': str(epsilon), 'raw_volume': str(volume),
           'MA_u': list(map(str,ma_u)), 'MA_gu': list(map(str,ma_gu)),
           'mixed': list(map(str,mixed)), 'averaged_target': list(map(str,averaged_target)),
           'MA_averaged_metric': list(map(str,ma_averaged_metric)),
           'difference': list(map(str,difference)),
           'scope': 'One exact model-intersection example; not an exhaustive result or a proof of geometric premises.'}
Path('descent-check-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
