"""Exact finite arithmetic in Q(sqrt(2)); diagnostics, not a theorem check."""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json


@dataclass(frozen=True)
class Q2:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        if not isinstance(other, Q2):
            other = Q2(F(other))
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Q2) else -F(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, Q2):
            other = Q2(F(other))
        return Q2(self.a*other.a + 2*self.b*other.b,
                  self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def positive(self):
        """Exact sign using sqrt(2)>0 and squared rational comparisons."""
        if self.b == 0:
            return self.a > 0
        if self.a == 0:
            return self.b > 0
        if self.a > 0 and self.b > 0:
            return True
        if self.a < 0 and self.b < 0:
            return False
        if self.a > 0:
            return self.a*self.a > 2*self.b*self.b
        return 2*self.b*self.b > self.a*self.a

    def encode(self):
        return {'rational':str(self.a), 'sqrt2_coefficient':str(self.b)}


theta = Q2(F(-1), F(1))
assert theta.positive() and (1-theta).positive()
gamma_coefficient = theta*1 + (1-theta)*2
assert gamma_coefficient == Q2(F(3), F(-1))
eps = theta*F(1,7) + (1-theta)*F(1,5)
assert eps == Q2(F(9,35), F(-2,35)) and eps.positive()
mass = 8*eps*eps
assert mass == Q2(F(712,1225), F(-288,1225)) and mass.positive()
C = theta*3 + (1-theta)*4
assert C == Q2(F(5), F(-1))

# On a ray with rho=t, H=t, the two auxiliary max walls are rational.
walls = [F(3)/(1-F(1,7)), F(4)/(2-F(1,5))]
assert walls == [F(7,2), F(20,9)]
# The positive sum is affine on this common rational subdivision.
slopes = [eps, theta*F(1,7)+(1-theta)*2, gamma_coefficient]
constants = [C, theta*3, Q2()]
for i, wall in enumerate(sorted(walls)):
    assert slopes[i]*wall+constants[i] == slopes[i+1]*wall+constants[i+1]
assert all((slopes[i+1]-slopes[i]).positive() for i in range(2))

result = {
 'kind':'exact finite arithmetic diagnostic for one specified Q(sqrt(2)) example',
 'reference':'gamma=(3-sqrt(2))*rho on the product of two standard embedded tripods',
 'convex_weights':[theta.encode(),(1-theta).encode()],
 'rational_references':['rho','2*rho'],
 'gamma_coefficient':gamma_coefficient.encode(),
 'rational_localization_coefficients':['1/7','1/5'],
 'rational_localization_constants':['3','4'],
 'local_sum_constant':C.encode(),
 'local_sum_epsilon':eps.encode(),
 'normalized_complete_local_mass':mass.encode(),
 'formal_actual_full_contact_integral':'-8*epsilon^2*a*b (requires the global proof)',
 'sample_ray_common_rational_walls':[str(x) for x in sorted(walls)],
 'sample_ray_affine_slopes':[x.encode() for x in slopes],
 'sample_ray_affine_constants':[x.encode() for x in constants],
 'exact_continuity_at_walls':True,
 'exact_positive_weights_growth_epsilon_mass':True,
 'limitation':'No global envelope computation, all-centre cone enumeration, or formal verification.'
}
Path('real-sum-output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
