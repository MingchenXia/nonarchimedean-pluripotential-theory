from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json
ROOT=Path(__file__).resolve().parent
counts={}
# A finite diagnostic of the explicitly false printed denominator claim.
q=F(3,2); f_order=2; p_order=1
assert q*(f_order-p_order)<=f_order and q*1>1
counter={'ring':'k[x]','f':'x^2','p':'x','displayed_denominator':1,'q':str(q),'c':'1','actual_q_pole_order_in_x':str(q),'reference_pole_order_in_x':2,'false_displayed_conclusion':'q*1 <= 1','growth_holds':'(3/2) log|x^-1| <= max(0,2 log|x^-1|)'}
# Cusp diagnostic; the infinite assertion has an independent semigroup proof in the paper.
def cusp_member(n):return n==0 or (n>=2 and (n%2==0 or n>=3))
for j in range(101):assert cusp_member(j+2)
counts['cusp_uniform_f_multiplier_j_0_to_100']=101
# Exhaustive finite shift checks for errors 4^-i, including worst-sign errors.
n=0
for i in range(1,41):
 e=F(1,4**i);e2=e/4;gap=2*e
 for a,b in product([-1,0,1],repeat=2):
  assert gap+a*e-b*e2>0;n+=1
counts['summable_shift_worst_sign_cases']=n
# Exact finite split bound, all positive tested gamma and selected canonical m.
n=0
for gamma in range(1,31):
 for m in range(1,gamma+1):
  for delta in [F(1,7),F(1,2),F(1),F(11,3)]:
   value=-delta if gamma==1 else -m*delta+(gamma-m)*delta/(2*(gamma-1))
   assert value<=-delta/2;n+=1
counts['split_positive_weights_including_gamma_one']=n
# Expanding-annulus arithmetic; logical neighborhood choices are not finite-certified.
n=0
for c,B,C in product([F(3,2),F(2),F(3)], [F(0),F(1),F(2)], [F(-1),F(-3),F(-8)]):
 R=(B-C+3)/(c-1)
 for inc in [F(0),F(1,5),F(1),F(5)]:
  g=R+inc
  assert g+B+1<c*g+C;n+=1
counts['controlled_annulus_margin_cases']=n
# Finite polynomial coefficient-radius arithmetic, zero coefficient == infinity.
n=0
for b,a1,a2,s in product([F(-2),F(0),F(3)], [None,F(-4),F(0),F(2)], [None,F(-3),F(1),F(4)], [F(-3),F(-1),F(0),F(2),F(5)]):
 bounds=[(a1-b)] if a1 is not None else []
 if a2 is not None:bounds.append((a2-b)/2)
 a=max(bounds) if bounds else None
 strict_at_radius=all(v-i*s<b for i,v in [(1,a1),(2,a2)] if v is not None)
 assert strict_at_radius==(a is None or s>a);n+=1
counts['coefficient_gauss_strict_radius_cases']=n
out={'status':'pass','total_finite_cases':sum(counts.values()),'counts':counts,'counterexample':counter,'cusp_example':{'R':'k[t^2,t^3]','f':'t^2','b':'t^-1','h':'t','integral_equation':'h^2-f=0','h_not_in_R':True,'uniform_M':1,'reason_for_ALL_j':'f*h^j=t^(j+2), and every integer >=2 is 2a+3b with a,b nonnegative.'},'epistemic_limit':'Exact exhaustive results only on the enumerated finite rational grids. No geometric witness, analytic theorem, entropy uniform bound, EP or equation is computationally certified.'}
(ROOT/'finite-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'total_finite_cases':out['total_finite_cases'],'counts':counts}))
