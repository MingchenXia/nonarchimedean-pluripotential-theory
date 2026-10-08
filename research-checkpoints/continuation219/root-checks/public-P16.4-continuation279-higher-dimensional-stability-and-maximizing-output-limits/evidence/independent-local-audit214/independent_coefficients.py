"""Own exact algebra diagnostics. No actual metric or analytic certification."""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product
from pathlib import Path
import json

root=Path(__file__).resolve().parent/'reproduction'/'independent-coefficients'
root.mkdir(exist_ok=True,parents=True)
def primitive_integral(p,a,b):
    return sum((x*(b**(k+1)-a**(k+1))/Q(k+1) for k,x in enumerate(p)),Q(0))
def shifted(p): return [Q(0)]+p
def add(a,b):
    return [(a[k] if k<len(a) else Q(0))+(b[k] if k<len(b) else Q(0))
            for k in range(max(len(a),len(b)))]
def scale(p,c): return [c*x for x in p]
def bernstein(m,j):
    return [Q(0)]*j+[Q(comb(m,j)*comb(m-j,k)*(-1)**k) for k in range(m-j+1)]

rows=[]
for n in range(1,33):
    alphas=[]
    for j in range(n):
        p=scale(bernstein(n-1,j),n)
        beta_left=primitive_integral(add(p,scale(shifted(p),-1)),Q(0),Q(1))
        beta_right=primitive_integral(shifted(p),Q(0),Q(1))
        alpha=(primitive_integral(shifted(p),Q(0),Q(1,2))+
               primitive_integral(add(p,scale(shifted(p),-1)),Q(1,2),Q(1)))/2
        assert beta_left==Q(n-j,n+1) and beta_right==Q(j+1,n+1)
        alphas.append(alpha)
    c=(1-Q(1,2)**n)/Q(2*(n+1))
    assert min(alphas)==c and alphas==alphas[::-1]
    assert sum(alphas)==Q(n,8)
    for j in range(n-1):
        # Exact polynomial verification of the derivative identity.
        b=bernstein(n,j+1)
        derivative=[(k+1)*b[k+1] for k in range(len(b)-1)]
        rhs=scale(add(bernstein(n-1,j),scale(bernstein(n-1,j+1),-1)),n)
        assert derivative==rhs
        lhs=alphas[j+1]-alphas[j]
        assert lhs==(primitive_integral(b,Q(0),Q(1,2))-
                     primitive_integral(b,Q(1,2),Q(1)))/2
    polar_sum=sum((-1)**(n-k)*comb(n,k)*k**n for k in range(1,n+1))
    assert polar_sum==factorial(n)
    rows.append({'n':n,'minimum':str(c),'alpha':list(map(str,alphas)),
                 'polarization_numerator':polar_sum})
inputs={'dimensions':[1,32],'arithmetic':'fractions.Fraction',
        'checks':['two beta weights','tent integral','symmetry','endpoint minimum',
                  'sum n/8','Bernstein derivative and adjacent alpha identity',
                  'polarization coefficient sum'],
        'scope':'formal polynomial identities, not actual metrics'}
output={'status':'PASS','coefficient_rows':sum(range(1,33)),'rows':rows,
        'limitation':'Finite n=1..32 diagnostics. All-n argument is separately proved in the audit.'}
(root/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
(root/'outputs.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:output[k] for k in ['status','coefficient_rows','limitation']},indent=2))
