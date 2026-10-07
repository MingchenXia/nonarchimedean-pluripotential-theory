#!/usr/bin/env python3
"""Exact finite diagnostics for continuation 265. No analytic certification."""
from fractions import Fraction as F
from itertools import product
from math import lcm
import json
from pathlib import Path

class Q2:
    """a+b sqrt(2), with exact order (no floating point decisions)."""
    def __init__(self,a=0,b=0):
        if isinstance(a,Q2): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=Q2(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+-Q2(o)
    def __rsub__(self,o): return Q2(o)+-self
    def __mul__(self,o):
        o=Q2(o);return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Q2(o);d=o.a*o.a-2*o.b*o.b
        assert d;return self*Q2(o.a/d,-o.b/d)
    def __rtruediv__(self,o):return Q2(o)/self
    def sign(self):
        a,b=self.a,self.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        d=a*a-2*b*b
        assert d # nonzero rational pair cannot be zero here
        return ((d>0)-(d<0))*(1 if a>0 else -1)
    def __eq__(self,o):
        o=Q2(o);return self.a==o.a and self.b==o.b
    def __lt__(self,o):return (self-Q2(o)).sign()<0
    def __le__(self,o):return (self-Q2(o)).sign()<=0
    def __gt__(self,o):return (self-Q2(o)).sign()>0
    def __ge__(self,o):return (self-Q2(o)).sign()>=0
    def __repr__(self):return f"({self.a})+({self.b})sqrt(2)"
    def as_json(self):return {'a':str(self.a),'b':str(self.b)}

def floor_q2(x):
    lo,hi=-1,1
    while x<lo:lo*=2
    while not x<hi:hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if x<mid:hi=mid
        else:lo=mid
    return lo

def solve(A,b):
    A=[[Q2(x) for x in row]+[Q2(y)] for row,y in zip(A,b)]
    n=len(A)
    for c in range(n):
        r=next(r for r in range(c,n) if A[r][c]!=0)
        A[c],A[r]=A[r],A[c]
        p=A[c][c];A[c]=[x/p for x in A[c]]
        for r in range(n):
            if r!=c:
                p=A[r][c];A[r]=[x-p*y for x,y in zip(A[r],A[c])]
    return [row[-1] for row in A]

def laplacian(n,edges):
    A=[[Q2(0) for _ in range(n)] for _ in range(n)]
    for v,w,length in edges:
        if v==w:continue # two loop incidences cancel at equal heights
        c=1/length
        A[v][v]-=c;A[w][w]-=c;A[v][w]+=c;A[w][v]+=c
    return A

def anchored_solution(n,edges,rhs,z=0):
    assert sum(rhs,Q2())==0
    if n==1:return [Q2()]
    A=laplacian(n,edges);indices=[i for i in range(n) if i!=z]
    h=solve([[A[i][j] for j in indices] for i in indices],[rhs[i] for i in indices])
    out=[Q2() for _ in range(n)]
    for i,x in zip(indices,h):out[i]=x
    assert all(sum((a*x for a,x in zip(row,out)),Q2())==b for row,b in zip(A,rhs))
    return out

G=[
 {'name':'singleton','n':1,'edges':[]},
 {'name':'one_retained_loop','n':1,'edges':[(0,0,Q2(0,1))]},
 {'name':'parallel_irrational_cycle','n':2,'edges':[(0,1,Q2(1)),(0,1,Q2(0,1))]},
 {'name':'triangle','n':3,'edges':[(0,1,Q2(1)),(1,2,Q2(0,1)),(2,0,Q2(1,1))]},
 {'name':'cycle_and_branch','n':4,'edges':[(0,1,Q2(1)),(0,1,Q2(0,1)),(1,2,Q2(1,1)),(2,3,Q2(2))]},
 {'name':'subdivided_loop','n':2,'edges':[(0,1,Q2(0,1)/2),(1,0,Q2(0,1)/2)]}
]

def main():
    count=0;orientation_count=0;minimum=None;example=None
    for graph in G:
        n,edges=graph['n'],graph['edges']
        val=[0]*n
        for v,w,_ in edges:val[v]+=1;val[w]+=1
        for weights in product(range(1,4),repeat=n):
            D=5;d=7
            target=[F(D*w,sum(weights)) for w in weights]
            a=[D]+[0]*(n-1)
            h=anchored_solution(n,edges,[Q2(x-y) for x,y in zip(target,a)])
            for mesh_factor in (1,2,4):
                # explicit sufficient slack for every tested target and incidence
                mesh=mesh_factor*max(128,int(32*max(val+[1])/min(target))+1)
                for perturb in (-1,0,1):
                    heights=[x+F(perturb*(i%3-1),mesh*mesh) for i,x in enumerate(h)]
                    deg=[Q2(x) for x in a];bends=[];slopes=[]
                    for v,w,length in edges:
                        s=(heights[w]-heights[v])/length
                        p=F(floor_q2(mesh*s)-1,mesh)
                        q=F(floor_q2(mesh*s)+2,mesh)
                        assert p<s<q
                        t=(q*length-(heights[w]-heights[v]))/(q-p)
                        assert 0<t<length
                        assert heights[v]+p*t+q*(length-t)==heights[w]
                        deg[v]+=p;deg[w]-=q
                        bends.append(Q2(q-p));slopes.extend((p,q))
                        # reverse orientation gives the identical divisor and metric
                        rp,rq=-q,-p;rt=length-t
                        assert heights[w]+rp*rt+rq*(length-rt)==heights[v]
                        assert heights[v]+p*t==heights[w]+rp*rt
                        assert rq-rp==q-p
                        orientation_count+=1
                    all_deg=deg+bends
                    assert all(x>0 for x in all_deg)
                    assert sum(all_deg,Q2())==D
                    k=lcm(*[x.denominator for x in slopes]) if slopes else 1
                    assert all(x.b==0 and (k*x.a).denominator==1 for x in all_deg)
                    raw=[x*k/F(k*d) for x in all_deg]
                    assert sum(raw,Q2())==F(D,d)
                    # Euler characteristic is unchanged by one subdivision per edge
                    assert (len(edges)*2-(n+len(edges))+1)==(len(edges)-n+1)
                    m=min(all_deg)
                    if minimum is None or m<minimum:minimum=m
                    count+=1
                    if graph['name']=='parallel_irrational_cycle' and weights==(1,2) and perturb==1 and mesh_factor==1:
                        example={'graph':graph['name'],'mesh':mesh,'target':list(map(str,target)),
                                 'vertex_heights':[x.as_json() for x in heights],
                                 'old_and_new_degrees':[x.as_json() for x in all_deg],
                                 'integer_slope_denominator':k,'original_bundle_denominator':d,
                                 'raw_mass':str(F(D,d))}
    # Dirichlet symmetry, positivity, and adding a genuinely attached tree.
    kernels=0;extensions=0
    for g in G:
        n,edges=g['n'],g['edges']
        J=[]
        for y in range(n):
            rhs=[Q2() for _ in range(n)];rhs[0]+=1;rhs[y]-=1
            J.append(anchored_solution(n,edges,rhs))
        for x,y in product(range(n),repeat=2):
            assert J[y][x]==J[x][y] and J[y][x]>=0;kernels+=1
        attach=n-1;length=Q2(1,1)
        new=edges+[(attach,n,length)]
        rhs=[Q2() for _ in range(n+1)];rhs[0]+=1;rhs[n]-=1
        H=anchored_solution(n+1,new,rhs)
        for x in range(n):assert H[x]==J[attach][x];extensions+=1
        assert H[n]==J[attach][attach]+length;extensions+=1
    inputs=[{'name':g['name'],'vertices':g['n'],
             'edges':[[v,w,l.as_json()] for v,w,l in g['edges']]} for g in G]
    Path('finite-inputs.json').write_text(json.dumps({'graphs':inputs,'target_weights':'every tuple in {1,2,3}^n','mass_of_integral_bundle':5,'d':7,'mesh_factors':[1,2,4],'height_perturbations':[-1,0,1]},indent=2)+'\n')
    result={'status':'PASS','arithmetic':'exact Q(sqrt(2)); no floating-point decisions',
            'positive_pair_interpolation_cases':count,'orientation_checks':orientation_count,
            'kernel_entry_checks':kernels,'attached_tree_checks':extensions,
            'smallest_degree':minimum.as_json(),'example':example,
            'limitations':'finite algebra only; not formal-model, affinoid, FS, CLD, target existence, or uniqueness certification'}
    Path('finite-output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
