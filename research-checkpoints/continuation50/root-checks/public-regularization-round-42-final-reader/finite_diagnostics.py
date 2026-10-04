"""Exact finite diagnostics only. These are not mathematical proof certificates."""
from fractions import Fraction as F
from pathlib import Path
import json

def solve(matrix, rhs):
    a=[list(row)+[b] for row,b in zip(matrix,rhs)]
    n=len(a)
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        scale=a[j][j]; a[j]=[v/scale for v in a[j]]
        for i in range(n):
            if i!=j:
                scale=a[i][j]
                a[i]=[v-scale*w for v,w in zip(a[i],a[j])]
    return [row[-1] for row in a]

edges=[(0,1,F(1)),(1,2,F(2)),(1,2,F(3)),(2,3,F(1))]
interior=[1,2]; boundary=[0,3]; source={1:F(1),2:F(2)}
matrix=[[F(0) for _ in interior] for _ in interior]
for v,w,length in edges:
    for centre,other in [(v,w),(w,v)]:
        if centre in interior:
            i=interior.index(centre); matrix[i][i]-=1/length
            if other in interior: matrix[i][interior.index(other)]+=1/length
q={0:F(0),3:F(0)}
q.update(zip(interior,solve(matrix,[source[v] for v in interior])))
lap={v:sum((q[w]-q[v])/length if a==v else (q[a]-q[v])/length
           for a,w,length in edges if a==v or w==v) for v in interior}
assert lap==source
constant=max(abs(value) for value in q.values())
assert all(value+constant>=0 for value in q.values())

def interpolation(x,level):
    count=2**level
    left=min(int(x*count),count-1); a=F(left,count); b=F(left+1,count)
    return a*a+(x-a)*(b*b-a*a)/(b-a)

checks=0; maximum_errors={}
for level in range(1,8):
    maximum=F(0)
    for i in range(257):
        x=F(i,256); perturb=abs(x-F(1,2))
        current=interpolation(x,level)+F(1,2**level)*perturb
        following=interpolation(x,level+1)+F(1,2**(level+1))*perturb
        assert x*x<=following<=current
        err=current-x*x; maximum=max(maximum,err)
        assert err<=F(1,4*4**level)+F(1,2**(level+1))
        checks+=1
    maximum_errors[str(level)]=str(maximum)

result=dict(evidence_type='exhaustive finite rational diagnostics on the stated finite inputs only',
    graph=dict(edges=[(v,w,str(length)) for v,w,length in edges],boundary=boundary,
        source={str(k):str(v) for k,v in source.items()},
        potential={str(k):str(v) for k,v in q.items()},
        outgoing_slope_sums={str(k):str(v) for k,v in lap.items()},
        nonnegative_shift=str(constant)),
    interpolation=dict(target='x^2',knots='dyadic knots at levels 1 through 8',
        perturbation='abs(x-1/2)',epsilon='2^(-level)',
        sample_grid='i/256, i=0,...,256',checks=checks,
        maximum_sample_errors=maximum_errors,passed=True),
    limitation='No diagnostic verifies analytic realization, residue semiampleness, arbitrary targets, scalar extension, or the original characterization.')
Path('finite-diagnostics.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
