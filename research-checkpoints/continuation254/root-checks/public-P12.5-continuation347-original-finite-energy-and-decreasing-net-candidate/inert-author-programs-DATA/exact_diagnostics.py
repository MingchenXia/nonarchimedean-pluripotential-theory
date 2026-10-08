"""Own bounded exact checks. No supplied helper imports or execution."""
import itertools, json, pathlib
from fractions import Fraction as Q

ROOT=pathlib.Path(__file__).resolve().parent
data=json.loads((ROOT/'bounded-evidence-input.json').read_text())
counts={}
lo,hi=data['surface_thickening']['multiplicities']
tlo,thi=data['surface_thickening']['twists']
counts['supported_thickening_polynomial']=0
for k in range(lo,hi+1):
    for t in range(tlo,thi+1):
        actual=sum(t+j+1 for j in range(k))
        assert actual==k*t+k*(k+1)//2
        counts['supported_thickening_polynomial']+=1

def monomial_colength(a,b,c,d,t,s):
    gens=[(a*i+c*j,b*(t-i)+d*(s-j)) for i in range(t+1) for j in range(s+1)]
    xmax=a*t+c*s
    return sum(min(y for x,y in gens if x<=column) for column in range(xmax))

counts['rectangular_ideal_mixed_differences']=0
lo,hi=data['rectangular_primary_ideals']['exponent_range']
nlo,nhi=data['rectangular_primary_ideals']['difference_base_N']
for a,b,c,d in itertools.product(range(lo,hi+1),repeat=4):
    for N in range(nlo,nhi+1):
        mixed=monomial_colength(a,b,c,d,N+1,N+1)-monomial_colength(a,b,c,d,N+1,N)-monomial_colength(a,b,c,d,N,N+1)+monomial_colength(a,b,c,d,N,N)
        assert mixed==min(a*d,b*c)
        assert mixed*mixed<=a*b*c*d
        counts['rectangular_ideal_mixed_differences']+=1

d=data['three_dimensional_branch_tensors']
vectors=list(itertools.product(map(Q,d['slopes']),repeat=2))
weights=d['residue_weights']; gauges_a=d['primary_orders_a']; gauges_b=d['primary_orders_b']
def form(*entries):
    return sum(Q(weights[q])*entries[0][q]*entries[1][q]*entries[2][q] for q in range(2))
counts.update(holder=0,conditional_cauchy=0,signed_direction=0,gauge_and_pairing=0,reference_cocycle=0)
for x,y,z in itertools.product(vectors,repeat=3):
    mixed=form(x,y,z)
    assert mixed**3<=form(x,x,x)*form(y,y,y)*form(z,z,z)
    assert mixed**2<=form(x,x,z)*form(y,y,z)
    difference=tuple(x[q]-y[q] for q in range(2))
    assert form(difference,difference,z)>=0
    counts['holder']+=1;counts['conditional_cauchy']+=1;counts['signed_direction']+=1
    ma=[Q(weights[q])*gauges_a[q]*x[q]*y[q] for q in range(2)]
    mb=[Q(weights[q])*gauges_b[q]*x[q]*y[q] for q in range(2)]
    for q in range(2):
        factor=Q(gauges_b[q],gauges_a[q])
        assert mb[q]==factor*ma[q]
    assert sum(Q(z[q],gauges_a[q])*ma[q] for q in range(2))==mixed
    assert sum(Q(z[q],gauges_b[q])*mb[q] for q in range(2))==mixed
    counts['gauge_and_pairing']+=1
    Ex=-form(x,x,x)/3; Ey=-form(y,y,y)/3; Ez=-form(z,z,z)/3
    telescoped=-sum(form(difference,*(([x]*j)+([y]*(2-j)))) for j in range(3))/3
    assert telescoped==Ex-Ey
    assert (Ex-Ey)+(Ey-Ez)==Ex-Ez
    counts['reference_cocycle']+=1

out={'status':'PASS','input_domain':data,'counts':counts,'total_assertion_cases':sum(counts.values()),'evidence_kind':'Exhaustive on the declared finite arithmetic domain only; no mathematical proof certification.'}
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports'/'exact-diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'counts':counts,'total_assertion_cases':out['total_assertion_cases']}))
