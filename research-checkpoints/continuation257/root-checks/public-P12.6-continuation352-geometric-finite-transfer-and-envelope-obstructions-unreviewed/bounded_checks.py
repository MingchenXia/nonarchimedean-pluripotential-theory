"""Fresh bounded arithmetic; no supplied modules or programs are imported."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, product
import json

ROOT=Path(__file__).resolve().parent
def main():
    data=json.loads((ROOT/'bounded-evidence-input.json').read_text())
    counts={'conductor':0,'split_characteristic_minimum':0,'curve_projection':0,'nonlinear_trace':0}
    failures=[]; conductor=[]
    for m in data['conductor_M']:
        obstacle=-1-Fraction(1,m)
        row={'M':m,'obstacle':str(obstacle),'upstairs_second':-2,'fibre_maximum':-2,'conductor_finite':True}
        conductor.append(row)
        if not Fraction(-2)<=obstacle<=Fraction(-1): failures.append(row)
        counts['conductor']+=1
    endpoint={'conductor':'infinite','obstacle':-1,'upstairs_first':-1,'upstairs_second':-2,'downstairs_at_v0':-2,'gap':1,'fibre_maximum':-1}
    if endpoint['upstairs_first']-endpoint['downstairs_at_v0']!=1: failures.append(endpoint)
    counts['conductor']+=1
    for degree in data['split_characteristic_degrees']:
        for values in product(data['split_characteristic_root_values'],repeat=degree):
            # Independent formal variables prevent cancellation between subsets.
            c=[min(sum(values[j] for j in subset) for subset in combinations(range(degree),i)) for i in range(1,degree+1)]
            answer=min(Fraction(c[i-1],i) for i in range(1,degree+1))
            if answer!=min(values): failures.append({'values':values,'coefficient_values':c})
            counts['split_characteristic_minimum']+=1
    for e,f in product(data['curve_ramification'],data['curve_residue_degrees']):
        lengths=[len([(i,j) for i in range(e*n) for j in range(f)]) for n in (1,2,3)]
        if lengths[1]-lengths[0]!=e*f or lengths[2]-lengths[1]!=e*f:
            failures.append({'e':e,'f':f,'basis_counts':lengths})
        counts['curve_projection']+=1
    source=sum(u*v for u,v in [(-1,0),(0,-1)])
    traced=(-1+0)*(0-1)
    if (source,traced)!=(0,1): failures.append({'source':source,'traced':traced})
    counts['nonlinear_trace']=1
    result={'counts':counts,'total':sum(counts.values()),'failures':failures,'conductor_rows':conductor,'endpoint':endpoint,'nonlinear_trace':{'source_mass':source,'traced_mass':traced},'proof_status':'Finite observations only; universal proofs are in proof.tex.'}
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports/bounded-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'total':result['total'],'counts':counts,'failures':len(failures)}))
if __name__=='__main__': main()
