"""Own exact, bounded standard-library diagnostics. Not theorem verification."""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'inputs/diagnostic-input.json').read_text())

def dot(a,b): return sum((Q(x)*Q(y) for x,y in zip(a,b)),Q(0))
def solve(A,b):
    n=len(b); a=[list(map(Q,row))+[Q(v)] for row,v in zip(A,b)]
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:return None
        a[j],a[p]=a[p],a[j]; z=a[j][j]; a[j]=[x/z for x in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j];a[i]=[x-z*y for x,y in zip(a[i],a[j])]
    return tuple(row[-1] for row in a)

report={'kind':'exhaustive finite arithmetic diagnostics only','matrix':[],
        'counts':{},'all_passed':True}
qc=ic=mc=0
for case in data['matrices']:
    M=case['M'];n=len(M);b=case['b'];A=[[-x for x in row] for row in M]
    Ab=[dot(row,b) for row in A]
    assert all(x>=0 for x in Ab) and any(x>0 for x in Ab)
    for z in product(data['quadratic_coordinates'],repeat=n):
        t=[Q(x)*y for x,y in zip(b,z)]
        lhs=sum(t[i]*dot(A[i],t) for i in range(n))
        rhs=sum(Ab[i]*b[i]*z[i]**2 for i in range(n))
        rhs+=sum(-A[i][j]*b[i]*b[j]*(z[i]-z[j])**2 for i in range(n) for j in range(i+1,n))
        assert lhs==rhs and (lhs>0 or all(x==0 for x in z));qc+=1
    for size in range(1,n+1):
        for ids in combinations(range(n),size):
            sub=[[A[i][j] for j in ids] for i in ids]
            for j in range(size):
                x=solve(sub,[int(i==j) for i in range(size)])
                assert x is not None and all(t>=0 for t in x)
            ic+=1
    # Linear inequalities row*x<=rhs; enumerate all possible vertices.
    inequalities=[]
    for i in range(n):
        e=[int(j==i) for j in range(n)]
        inequalities.extend([(e,Q(case['upper'][i])),([-x for x in e],Q(case['B']*b[i]))])
    inequalities.extend([([-x for x in row],Q(0)) for row in M])
    feasible=lambda x:all(dot(row,x)<=v for row,v in inequalities)
    vertices=set()
    for ids in combinations(range(len(inequalities)),n):
        x=solve([inequalities[i][0] for i in ids],[inequalities[i][1] for i in ids])
        if x is not None and feasible(x): vertices.add(x)
    assert vertices
    for u,v in product(vertices,repeat=2):
        assert feasible(tuple(max(x,y) for x,y in zip(u,v)));mc+=1
    greatest=tuple(max(x[i] for x in vertices) for i in range(n))
    assert feasible(greatest)
    report['matrix'].append({'vertices':len(vertices),'greatest':[str(x) for x in greatest]})
report['counts'].update(quadratic=qc,principal_inverse=ic,vertex_max_pairs=mc)

sc=0
for j,r,s in product(data['smooth_j'],data['smooth_r_s'],data['smooth_r_s']):
    gens=[(r+s-i-h,j*i+h) for i in range(s+1) for h in range(r+1)]
    length=sum(min(y for gx,y in gens if gx<=x) for x in range(r+s))
    expected=r*(r+1)//2+r*s+j*s*(s+1)//2
    assert length==expected;sc+=1
report['counts']['smooth_staircase']=sc

def parity_length(n,k):
    gens=[(2*n*i+2*j,(2*n-2)*j+4*n*(k-i-j))
          for i in range(k+1) for j in range(k-i+1)]
    total=0
    for x in range(2*n*k):
        threshold=min(y+(x-gx)%2 for gx,y in gens if gx<=x)
        # Count nonnegative y<threshold having x+y even.
        total+=max(0,(threshold-(x%2)+1)//2)
    return total

pc=dc=0;samples={}
for n in data['parity_n_k']:
    vals=[parity_length(n,k) for k in data['parity_n_k']]
    for k,val in zip(data['parity_n_k'],vals):
        # Independent direct membership enumeration in the declared finite box.
        gs=[(2*n*i+2*j,(2*n-2)*j+4*n*(k-i-j))
            for i in range(k+1) for j in range(k-i+1)]
        direct=sum(1 for x in range(2*n*k) for y in range(4*n*k)
                   if (x+y)%2==0 and not any(gx<=x and gy<=y for gx,gy in gs))
        assert direct==val;pc+=1
    for i in range(2,len(vals)):
        assert vals[i]-2*vals[i-1]+vals[i-2]==2*n*n+2*n;dc+=1
    samples[str(n)]=vals
report['counts'].update(parity_lengths=pc,parity_second_differences=dc)
report['parity_samples']=samples
fc=0
for n,a_text in product(data['profile_n'],data['profile_a']):
    a=None if a_text=='infinity' else Q(a_text)
    direct=Q(2) if a is None else min(a,(a+n-1)/n,Q(2))
    formula=Q(2) if a is None else min(1+(a-1)/n,Q(2))
    assert direct==formula;fc+=1
report['counts']['profile_cases']=fc
report['jacobian_diagnostic']=[{'L':L,'primary_value':1,'jacobian_value':L}
                               for L in data['jacobian_L']]
(ROOT/'reports/bounded-diagnostics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'all_passed':True,'counts':report['counts'],'greatest':[m['greatest'] for m in report['matrix']]}))
