#!/usr/bin/env python3
"""Small exhaustive rational diagnostics; no mathematical proof certification."""
from fractions import Fraction as F
import hashlib, itertools, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
checks=[]
def green(x,z,R):return min(x,z)*(R-max(x,z))/R
for R in range(2,10):
    for z in range(1,R):
        vals=[green(F(x),F(z),F(R)) for x in range(R+1)]
        assert vals[0]==vals[-1]==0
        for x in range(1,R):
            lap=vals[x-1]+vals[x+1]-2*vals[x]
            assert lap==(-1 if x==z else 0)
            checks.append(('green-sign',R,z,x))
        for a in [F(0),F(1,7),F(1,3),F(2)]:
            p=[-a*v for v in vals]
            for x in range(1,R):
                assert p[x-1]+p[x+1]-2*p[x]==(a if x==z else 0)
                checks.append(('negative-green-correction',R,z,str(a),x))
# Fixed poles: positive coefficients need not be monotone, but a common bound works.
fixed=[]
for i in range(1,101):
    a,b=F(1,i),F(1+(i%2),i)
    values=[-a*green(F(x),F(1),F(4))-b*green(F(x),F(3),F(4)) for x in range(5)]
    norm=max(abs(x) for x in values)
    bound=(a+b)*F(3,4)
    assert norm<=bound and bound<=F(9,4*i)
    checks.append(('fixed-support-bound',i,str(norm),str(bound)))
    fixed.append({'i':i,'mass':str(a+b),'norm':str(norm),'bound':str(bound)})
# A graph diagnostic only: mass 1/n and interval length n^2 give correction n/4.
moving=[]
for n in range(2,21,2):
    R=F(n*n); pole=R/2; mass=F(1,n); norm=mass*green(pole,pole,R)
    assert norm==F(n,4)
    moving.append({'n':n,'interval_length':str(R),'mass':str(mass),'correction_norm':str(norm)})
    checks.append(('moving-domain-diagnostic',n))
# A finite compact-set analogue of strict-epsilon feasibility of decreasing majorants.
for gaps in itertools.product([F(0),F(1,4),F(1)],repeat=3):
    for eps in [F(1,2),F(1,3),F(1,7),F(1,11)]:
        f=[F(0),F(2),F(-1)];q=[f[j]-gaps[j] for j in range(3)]
        index=2*eps.denominator
        h=[q[j]+F(1,index) for j in range(3)]
        assert all(h[j]-eps<=f[j] for j in range(3))
        checks.append(('finite-majorant-feasibility',tuple(map(str,gaps)),str(eps),index))
# Finite exponent check of a conductor/Rees chart for A=k[u^2,u^3], B=k[u].
# I=u^2 B. (u^(2+r)t)/(u^2t)=u^r; not a proof of the general Proj calculation.
for r in range(101):
    assert (2+r)-2==r
    checks.append(('rees-chart-exponent',r))
payload={'status':'pass','count':len(checks),'groups':{},'domain':'Explicit finite integer/rational grids in this script',
 'fixed_support_samples':fixed,'moving_graph_samples':moving,
 'limitations':'Exhaustive only on declared finite grids. Graph diagnostics do not construct algebraic metrics; checks, hashes and compilation do not prove the manuscript.'}
for c in checks:payload['groups'][c[0]]=payload['groups'].get(c[0],0)+1
payload['case_digest']=hashlib.sha256(json.dumps(checks,sort_keys=True).encode()).hexdigest()
(ROOT/'finite-checks.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({k:payload[k] for k in ['status','count','groups','limitations']}))
