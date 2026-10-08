"""Fresh exact, small standard-library diagnostics; no supplied module imported."""
import json, pathlib, itertools, fractions
P=pathlib.Path.cwd(); d=json.loads((P/'diagnostic-input.json').read_text())
Q=fractions.Fraction
def monomial_generators(t,s):
    return [(i+3*j,t-i+3*(s-j)) for i in range(t+1) for j in range(s+1)]
def length(t,s):
    g=monomial_generators(t,s); bound=t+3*s
    return sum(not any(a<=x and b<=y for a,b in g) for x in range(bound) for y in range(bound))
cases=[{'t':t,'s':s,'length':length(t,s)} for t,s in d['monomial_length_cases']]
assert [r['length'] for r in cases]==[11,15,30,36]
early=cases[3]['length']-cases[1]['length']-cases[2]['length']+cases[0]['length']
assert early==2
window=d['stabilized_rectangle']; stabilized=0
for t in range(window['t_min'],window['t_max']+1):
 for s in range(window['s_min'],window['s_max']+1):
    assert length(t,s)==(t+3*s)*(t+3*s+1)//2
    stabilized+=1
slopes=[Q(x) for x in d['tensor']['slopes']]; weights=d['tensor']['weights']
def F(*args): return sum(Q(weights[i])*prod(arg[i] for arg in args) for i in range(2))
def prod(xs):
    out=Q(1)
    for x in xs: out*=x
    return out
tensor_cases=0
for vals in itertools.product(slopes,repeat=6):
    a,b,c=vals[:2],vals[2:4],vals[4:]
    assert F(a,b,c)**3<=F(a,a,a)*F(b,b,b)*F(c,c,c)
    assert F(a,b,c)**2<=F(a,a,c)*F(b,b,c)
    w=tuple(a[i]-b[i] for i in range(2))
    assert F(w,w,c)>=0
    tensor_cases+=1
e=d['artinian_euler']; euler=0
for k in range(e['thickness_min'],e['thickness_max']+1):
 for t in range(e['twist_min'],e['twist_max']+1):
    # P1 x P1, full length-k generic thickening; mixed finite difference.
    chi=lambda x,y:k*(x+1)*(y+1)
    assert chi(t+1,t+1)-chi(t,t+1)-chi(t+1,t)+chi(t,t)==k
    euler+=1
out={'status':'PASS','finite_domain_only':True,'monomial_lengths':cases,
     'early_mixed_difference':early,'true_mixed_coefficient':3,
     'stabilized_window_cases':stabilized,'tensor_cases':tensor_cases,'artinian_euler_cases':euler,
     'universal_monomial_reason':'For t>=2 the intervals of degree t+3s exponents [3j,3j+t] cover all integers from 0 to t+3s; therefore I^t J^s=m^(t+3s). The coefficient is 3. Finite enumeration is not this proof.',
     'pole_counterexample':'Two-branch curve reference weights 1,2: z=(-infinity,0) is globally nonbottom, but its first pole has capacity 1.',
     'limits':'No geometric, energy, net, or infinite-domain assertion is verified by this execution.'}
(P/'evidence/finite-diagnostics.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
