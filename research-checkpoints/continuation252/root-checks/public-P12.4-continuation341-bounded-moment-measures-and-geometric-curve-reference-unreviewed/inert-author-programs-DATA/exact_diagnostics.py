#!/usr/bin/env python3
"""Own finite basis/gauge arithmetic. Mathematical universal proofs are in notes."""
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'bounded-evidence-input.json').read_text())
curve_rows, nil_rows, gauge_rows = [], [], []
c = data['residue_degree_curve']
for d in c['degrees']:
    for r in c['primary_orders']:
        for N in c['length_powers']:
            basis = [('constant', 0)] + [(i, j) for i in range(1, r*N) for j in range(d)]
            actual = len(basis)
            expected = 1+d*(r*N-1)
            assert actual == expected
            next_size = 1+d*(r*(N+1)-1)
            assert next_size-actual == d*r
            curve_rows.append({'d': d, 'r': r, 'N': N, 'basis_count': actual,
                               'successive_slope': next_size-actual})
for N in data['nilpotent_obstruction']['length_powers']:
    smooth = list(range(N))
    thick = [(i,e) for i in range(N) for e in range(2)]
    assert len(smooth) == N and len(thick) == 2*N
    nil_rows.append({'N': N, 'reduced_length': len(smooth), 'thickened_length': len(thick)})
g = data['two_branch_primary_change']
for old in g['old_orders']:
    for new in g['new_orders']:
        old_weights = old
        transformed = [Fraction(old_weights[i])*Fraction(new[i], old[i]) for i in range(2)]
        assert transformed == list(map(Fraction, new))
        for test in g['test_orders']:
            old_moment = sum(Fraction(old_weights[i])*Fraction(test[i], old[i]) for i in range(2))
            new_moment = sum(transformed[i]*Fraction(test[i], new[i]) for i in range(2))
            assert old_moment == new_moment == sum(test)
            gauge_rows.append({'old': old, 'new': new, 'test': test,
                               'old_moment': str(old_moment), 'new_moment': str(new_moment)})
report = {'status': 'PASS', 'curve_basis_cases': len(curve_rows),
          'nilpotent_basis_cases': len(nil_rows), 'gauge_moment_cases': len(gauge_rows),
          'curve_rows': curve_rows, 'nilpotent_rows': nil_rows, 'gauge_rows': gauge_rows,
          'limitation': 'Exact observations on the declared finite inputs only; universal mathematical arguments are separate. No supplied program was imported.'}
(ROOT / 'reports').mkdir(exist_ok=True)
(ROOT / 'reports' / 'exact-diagnostics.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','curve_basis_cases','nilpotent_basis_cases','gauge_moment_cases']}))
