"""Exact finite transcription checks, not mathematical certification."""
from fractions import Fraction as Q
from math import comb
import json

def rank(rows):
    a=[list(map(Q,r)) for r in rows]
    if not a:return 0
    r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]; v=a[r][c]
        a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                v=a[i][c];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def run():
    midpoint=[]
    for n in range(1,13):
        # Homogeneity permits y=1; check every coefficient, not samples.
        rhs=[Q(0)]*(n+2)
        for j in range(n):
            for k,v in enumerate([1,-2,1]):rhs[j+k]-=(n-j)*v
        lhs=[Q(0)]*(n+2);lhs[0]=-n;lhs[1]=n+1;lhs[n+1]-=1
        assert lhs==rhs,(n,lhs,rhs)
        vals=[]
        for j in range(n):
            k=n-1-j
            def half(a,b):
                return sum((Q((-1)**i*comb(b,i))*Q(1,2)**(a+i+2)/Q(a+i+2) for i in range(b+1)),Q(0))
            v=Q(n*comb(n-1,j),2)*(half(j,k)+half(k,j))
            assert v>=Q(n,4**(n+1));vals.append(v)
        assert sum(vals)==Q(n,8)
        midpoint.append(dict(n=n,minimum_coefficient=str(min(vals)),sum=str(sum(vals))))
    graph=[]
    for mult,orders,edges in [([1,2,3],[Q(-2),Q(1),Q(4)],[(0,1,2),(1,2,3),(0,2,1)]),
                              ([2,3,5,7],[Q(-3,2),Q(-1,4),Q(2,3),Q(5,2)],[(0,1,1),(1,2,4),(2,3,2),(0,3,3)])]:
        raw=sum(Q(mult[i]*mult[j]*w)*(orders[i]-orders[j])**2 for i,j,w in edges)
        absolute=sum(Q(mult[i]*mult[j]*w)*(abs(orders[i])-abs(orders[j]))**2 for i,j,w in edges)
        assert absolute<=raw
        graph.append(dict(multiplicities=mult,orders=list(map(str,orders)),raw=str(raw),absolute=str(absolute)))
    # A subspace not spanned by the flag's adapted coordinate vectors.
    s=[[1,1,0],[0,0,1]];weights=[-2,0,3]
    levels=sorted(set(weights)); dims=[]
    for level in levels:
        f=[[int(i==j) for i in range(3)] for j,w in enumerate(weights) if w>=level]
        quotient_dim=rank(f+s)-rank(s)
        subspace_dim=len(f)+rank(s)-rank(f+s)
        assert len(f)==quotient_dim+subspace_dim
        dims.append(dict(level=level,full=len(f),subspace=subspace_dim,quotient=quotient_dim))
    assert dims==[dict(level=-2,full=3,subspace=2,quotient=1),
                  dict(level=0,full=2,subspace=1,quotient=1),
                  dict(level=3,full=1,subspace=1,quotient=0)]
    assert sum(weights)==(-2+3)+0
    # Explicit curve truncation: B=a/2, mass is 1 at its slope break.
    cap=[]
    for a in [Q(1,3),Q(1),Q(7)]:
        for c in [Q(1,2),Q(1),Q(3)]:
            tv=Q(0) if a<=c else Q(2)
            assert tv<=2*2*(a/2)/c
            cap.append(dict(a=str(a),C=str(c),TV=str(tv),bound=str(2*a/c)))
    zero_masses=[str(2*Q(1,m)*(1+Q(1,m))) for m in [1,2,10,100]]
    return dict(classification='finite exact checks; not a theorem over all models',
                dimensions=list(range(1,13)),midpoint=midpoint,graphs=graph,
                quotient_flags=dims,curve_cap=cap,zero_volume_perturbation_masses=zero_masses)

if __name__=='__main__':print(json.dumps(run(),indent=2))
