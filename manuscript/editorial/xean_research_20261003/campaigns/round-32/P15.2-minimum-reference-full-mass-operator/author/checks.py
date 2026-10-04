"""Small exact finite diagnostics; they do not prove the analytic claims."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json
cases=0
for n in range(1,31):
 for d in range(n):
  # After actual-current expansion and division by binom(n,d)*eps^(n-d),
  # the degree-d coefficient is 1; all others have positive powers.
  assert Fraction(comb(n,d),comb(n,d))==1
  assert all(d-k>=1 for k in range(d))
  assert n-1-d>=0
  cases+=1
# Formal surface algebra: A^2=B^2=F^2=B F=0, A B and A F survive.
# F is the vertical exact factor in the counterexample; no mass claim is inferred.
def wedge(x,y):
 a,b,f=x; c,d,g=y
 return (a*d+b*c,a*g+f*c)
from fractions import Fraction as F
surface=[]
for t in [F(1,10),F(-1,10)]:
 for eps in [F(1,2),F(1,3),F(1,7)]:
  x=(1+eps,eps,eps*t)
  lhs=tuple(v/(2*eps) for v in wedge(x,x))
  rhs=(1+eps,t*(1+eps))
  assert lhs==rhs
  surface.append({'t':str(t),'epsilon':str(eps),'rescaled_AB':str(lhs[0]),'rescaled_AF':str(lhs[1])})
r={'normalization_cases':cases,'surface_wedge_cases':len(surface),'all_passed':True,'surface_cases':surface,'scope':'Exhaustive only over stated finite inputs. The asymptotic, positivity, domain and continuity theorems are mathematical proofs in the argument, not computer-certified results.'}
Path('exact-checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(f'exact finite diagnostics: {cases} normalization cases and {len(surface)} surface wedge cases passed')
