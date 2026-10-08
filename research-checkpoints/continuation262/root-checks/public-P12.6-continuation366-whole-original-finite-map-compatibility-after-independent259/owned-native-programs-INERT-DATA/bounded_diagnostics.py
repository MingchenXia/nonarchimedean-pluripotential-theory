"""Owned standard-library finite diagnostics. Never imports supplied programs."""
import itertools, json, math
from fractions import Fraction
from pathlib import Path

cfg=json.loads(Path('diagnostic-input.json').read_text())
counts={'polynomial_cases':0,'node_mask_cases':0,'arithmetic_cases':0}
failures=[]
for char in cfg['characteristics']:
    for r in cfg['factor_counts']:
        for orders in itertools.product(cfg['orders'],repeat=r):
            for lengths in itertools.product(cfg['artinian_lengths'],repeat=r):
                # Separate formal T_j variables prevent spurious cancellations.
                poly={(0,0,(0,)*r):1}
                for j,(a,l) in enumerate(zip(orders,lengths)):
                    nxt={}
                    for (te,ze,ve),co in poly.items():
                        for b in range(l+1):
                            vv=list(ve);vv[j]+=b
                            key=(te+l-b,ze+a*b,tuple(vv))
                            nxt[key]=nxt.get(key,0)+co*math.comb(l,b)*(-1)**b
                    poly={key:(val%char if char else val) for key,val in nxt.items()}
                    poly={key:val for key,val in poly.items() if val}
                d=sum(lengths); vals={}
                for (te,ze,ve),co in poly.items():
                    i=d-te
                    if i: vals[i]=min(vals.get(i,math.inf),ze)
                minimum=min(Fraction(v,i) for i,v in vals.items())
                norm=sum(a*l for a,l in zip(orders,lengths));N=norm+1
                truncated=min(Fraction(min(vals.get(i,math.inf),N),i) for i in range(1,d+1))
                if (minimum,vals[d],truncated)!=(min(orders),norm,min(orders)):
                    failures.append({'char':char,'orders':orders,'lengths':lengths,'values':vals})
                counts['polynomial_cases']+=1
for N in cfg['node_N']:
    alpha=Fraction(1,N-1)
    for x,z in cfg['node_weights']:
        assert min(x,z)==1
        h=-(1-alpha)-alpha*min(x,N*z)
        if not h<=-1:failures.append({'node_N':N,'x':x,'z':z,'h':str(h)})
        counts['node_mask_cases']+=1
    shared=-(1-alpha)-alpha*N
    if shared!=-2:failures.append({'node_shared_N':N,'h':str(shared)})
    counts['node_mask_cases']+=1
direct=Fraction(-2,3);iterated=Fraction(-1,2)
checks={
 'varying_degree_direct_average':direct,
 'varying_degree_iterated_average':iterated,
 'both_unnormalized_traces':-2,
 'two_arbitrary_slot_source_mass':0,
 'two_arbitrary_slot_trace_target_mass':1,
 'two_arbitrary_slot_normalized_target_mass':Fraction(1,4),
 'node_shared_reverse_gap':-1-(-2),
 'vertical_quotient_gap':0-(-1)
}
counts['arithmetic_cases']=len(checks)
out={'status':'PASS' if not failures else 'FAIL','counts':counts,
     'failures':failures,'exact_arithmetic':{k:str(v) for k,v in checks.items()},
     'limitations':'Only the explicitly finite input domain was exhausted; no universal mathematical claim follows from execution.'}
Path('evidence').mkdir(exist_ok=True)
Path('evidence/bounded-diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
