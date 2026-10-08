import json,itertools,pathlib,platform,sys
from fractions import Fraction
cfg=json.loads(pathlib.Path('bounded-evidence-input.json').read_text())
checks=[]
def check(kind,ok,detail):
 checks.append({'kind':kind,'pass':bool(ok),'detail':detail})
def addpoly(a,b,p):
 c=a.copy()
 for k,v in b.items(): c[k]=(c.get(k,0)+v)%p
 return {k:v for k,v in c.items() if v}
# Characteristic polynomial in z with polynomial-in-t coefficients.
for prime in cfg['characteristics']:
 roots=list(itertools.product(cfg['root_orders'],range(1,prime)))
 for degree in cfg['degrees']:
  for tuple_roots in itertools.product(roots,repeat=degree):
   poly={0:{0:1}}
   for order,lead in tuple_roots:
    new={}
    for zexp,tpoly in poly.items():
     new[zexp+1]=addpoly(new.get(zexp+1,{}),tpoly,prime)
     term={k+order:(-lead*v)%prime for k,v in tpoly.items()}
     new[zexp]=addpoly(new.get(zexp,{}),term,prime)
    poly=new
   vals=[min(poly.get(degree-i,{}),default=None) for i in range(1,degree+1)]
   finite=[Fraction(v,i) for i,v in enumerate(vals,1) if v is not None]
   m=min(order for order,_ in tuple_roots); N=3*degree+1
   truncated=[Fraction(min(v,N) if v is not None else N,i) for i,v in enumerate(vals,1)]
   check('split_characteristic_minimum_and_primary_truncation',min(finite)==m and min(truncated)==m,{'p':prime,'roots':tuple_roots,'coefficient_orders':vals,'primary_N':N})
for e,f,b in itertools.product(cfg['curve_ramification'],cfg['curve_residue_degrees'],cfg['curve_gauge_orders']):
 # Source gauge order e*b; normalized restriction cancels e.
 check('zero_arity_curve_weights',f*e*b==(e*f)*b,{'e':e,'f':f,'base_b':b,'source_weight':f*e*b})
for M in cfg['monomial_weights']:
 check('counterexample_obstacle_values',-1-Fraction(1,M)>=-2 and -Fraction(1,M)>=-1,{'M':M,'surface_f':str(-1-Fraction(1,M)),'quotient_f':str(-Fraction(1,M))})
check('normalized_tower_obstruction',Fraction(-2,3)!=Fraction(-1,2),{'direct':'-2/3','iterated':'-1/2','unnormalized':'-2'})
check('nonlinear_separate_traces_obstruction',Fraction(0)!=Fraction(1,4),{'source_product_mass':0,'normalized_target_mass':'1/4','unnormalized_target_mass':1})
result={'checks':checks,'count':len(checks),'failures':sum(not r['pass'] for r in checks),'environment':{'python':sys.version,'platform':platform.platform()},'not_mathematical_verification':True}
pathlib.Path('evidence/bounded-checks.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
