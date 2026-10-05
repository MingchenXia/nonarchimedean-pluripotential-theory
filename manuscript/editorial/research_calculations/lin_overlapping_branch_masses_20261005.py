#!/usr/bin/env python3
"""Exact finite checks for the known BPR curve and a weighted model metric.

The graph slope calculation and Newton polygon are computed separately.
This is a calculation supplement, not a general theorem or model receipt.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def q(x):
    return str(x)


def newton_roots(c):
    # T^2-pT-X, with v(p)=1 and v(X)=c; lower convex hull.
    points = [(F(0), c), (F(1), F(1)), (F(2), F(0))]
    hull = []
    for point in points:
        while len(hull) >= 2:
            a, b = hull[-2:]
            cross = (b[0]-a[0])*(point[1]-a[1])-(b[1]-a[1])*(point[0]-a[0])
            if cross > 0:
                break
            hull.pop()
        hull.append(point)
    roots = []
    for a, b in zip(hull, hull[1:]):
        slope = (b[1]-a[1])/(b[0]-a[0])
        roots.extend([-slope] * int(b[0]-a[0]))
    return sorted(roots), hull


def graph_atoms(c):
    # Annular-length coordinates. Only interior break points contribute here.
    edges = [('middle', F(0), F(1), F(2), F(0)),
             ('zero', F(1), None, F(1), F(1)),
             ('p', F(1), None, F(1), F(1))]
    atoms = []
    for edge, lo, hi, slope, intercept in edges:
        alpha = (c-intercept)/slope
        if lo < alpha and (hi is None or alpha < hi):
            atoms.append({'edge': edge, 'alpha': alpha, 'mass': slope,
                          'image': (slope*alpha+intercept, F(0))})
    # One-sided directional derivatives at the common Gauss point.
    outgoing = [-F(2)*int(F(2) > c), F(int(F(2) >= c)), F(int(F(2) >= c))]
    mass = sum(outgoing)
    assert mass >= 0
    if mass:
        atoms.append({'edge': 'junction', 'alpha': F(1), 'mass': mass,
                      'image': (F(2), F(0))})
    return atoms, outgoing


def main():
    samples = [F(1,17), F(1,3), F(1,2), F(1), F(3,2), F(7,4),
               F(199,100), F(2), F(201,100), F(9,4), F(3), F(7,2), F(5), F(19,2)]
    rows = []
    for c in samples:
        roots, hull = newton_roots(c)
        atoms, outgoing = graph_atoms(c)
        assert sum(a['mass'] for a in atoms) == 2
        assert all(a['image'] == (c,F(0)) for a in atoms)
        # Values of t on the computed Gauss discs; this includes val(t)=1
        # on the p-centred disc of radius strictly less than |p|.
        source_roots = []
        for a in atoms:
            v_t = F(1) if a['edge'] in ('p','junction') else a['alpha']
            source_roots.extend([v_t] * int(a['mass']))
        assert sorted(source_roots) == roots
        if c > 2:
            assert len(atoms) == 2 and all(a['alpha'] > 1 for a in atoms)
            assert all(a['mass'] == 1 for a in atoms)
        else:
            assert len(atoms) == 1 and atoms[0]['mass'] == 2
        rows.append({'c':q(c), 'newton_hull':[[q(x),q(y)] for x,y in hull],
                     'newton_root_values':list(map(q,roots)),
                     'junction_outgoing_slopes':list(map(q,outgoing)),
                     'analytic_atoms':[{'edge':a['edge'],'alpha':q(a['alpha']),
                                        'mass':q(a['mass']),
                                        'image':list(map(q,a['image']))} for a in atoms],
                     'total_mass':2,'merged_tropical_mass':2,
                     'wrong_mass_if_global_weight_used_on_each_branch':4 if c>2 else None})
    limits = []
    for n in [2,3,5,11,29]:
        left, _ = graph_atoms(F(2)-F(1,n))
        right, _ = graph_atoms(F(2)+F(1,n))
        assert F(1)-left[0]['alpha'] == F(1,2*n)
        assert all(a['alpha']-F(1) == F(1,n) for a in right)
        limits.append({'n':n,'left_distance_to_junction':q(F(1,2*n)),
                       'right_branch_distance_to_junction':q(F(1,n)),
                       'mass_on_either_side':2})
    result = {'status':'PASS','source':'BPR arXiv:1104.0320v2, Examples 2.6, 8.7, 8.11; Lin arXiv:2609.12969v1, Example 10.1',
              'field':'C_p, v(p)=1','metric':'g_c(u,w)=max(0,u-c), c positive rational',
              'sample_count':len(rows),'rows':rows,'limit_samples':limits,
              'scope':'Exact selected slope, Newton-polygon, image and degree checks. General formulas are proved symbolically in the book example; finite output alone does not prove them.',
              'new_independent_model_receipt':False,'new_general_theorem':False,
              'general_siu_division_repaired':False,'open_problem_solved':False}
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','sample_count','new_independent_model_receipt','open_problem_solved']}))


if __name__ == '__main__':
    main()
