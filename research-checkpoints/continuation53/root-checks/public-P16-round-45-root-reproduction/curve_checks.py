#!/usr/bin/env python3
"""Small exact-rational consistency examples, not a verification of the theorem."""
from fractions import Fraction as Q
import json
from pathlib import Path

V = Q(5)
mu = {'a': [(Q(1), Q(1)), (Q(3), Q(1))], 'b': [(Q(2), Q(1))]}
eta = {'a': [(Q(1, 2), Q(2)), (Q(4), Q(1, 2))], 'c': [(Q(2), Q(1))]}

def ray_mass(m):
    return sum((w for atoms in m.values() for t, w in atoms), Q(0))

def inner(m, n):
    return sum((w * z * min(t, u)
                for ray, atoms in m.items()
                for t, w in atoms
                for u, z in n.get(ray, [])), Q(0))

def phi(m, ray, t):
    return -sum((w * min(t, u) for u, w in m.get(ray, [])), Q(0))

def energy(m):
    return -inner(m, m) / (2 * V)

Dmu = inner(mu, mu)
Deta = inner(eta, eta)
cross = inner(mu, eta)
objective = energy(mu) - sum((w * phi(mu, ray, t)
                              for ray, atoms in mu.items() for t, w in atoms), Q(0)) / V
derivative = (Dmu - cross) / V
integral_derivative = sum((w * (phi(eta, ray, t) - phi(mu, ray, t))
                           for ray, atoms in mu.items() for t, w in atoms), Q(0)) / V
assert V - ray_mass(mu) == Q(2)
assert V - ray_mass(eta) == Q(3, 2)
assert objective == Dmu / (2 * V)
assert derivative == integral_derivative

ray_generators = []
for e in [1, 2, 3, 7]:
    a = Q(5, 3)
    for t in [Q(0), Q(1, 4), a, Q(10)]:
        value = max(-e * t, -e * a) / e
        assert value == -min(t, a)
        ray_generators.append({'e': e, 'a': str(a), 't': str(t), 'value': str(value)})

out = {
    'classification': 'Exact finite arithmetic examples; not an exhaustive finite theorem or a proof check.',
    'raw_mass': str(V), 'mu_root_mass': str(V - ray_mass(mu)),
    'eta_root_mass': str(V - ray_mass(eta)),
    'D_mu': str(Dmu), 'D_eta': str(Deta), 'cross_inner_product': str(cross),
    'mu_potential_energy': str(energy(mu)), 'mu_dual_objective': str(objective),
    'expected_dual_energy': str(Dmu / (2 * V)),
    'segment_energy_derivative': str(derivative),
    'MA_integral_derivative': str(integral_derivative),
    'point_ideal_ray_checks': ray_generators,
    'node_atom_example': {'raw_atom_mass': str(V), 'atom_parameter': '1',
                          'upstairs_endpoint_drop_q1': str(V),
                          'upstairs_endpoint_drop_q2': '0',
                          'upstairs_dual_energy': str(V / 2)},
    'result': 'All asserted arithmetic identities hold.'
}
Path('curve-checks.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k != 'point_ideal_ray_checks'}, indent=2))
