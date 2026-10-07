#!/usr/bin/env python3
"""Small exact tests in Q(sqrt(2)); observations, not analytic certification."""
from fractions import Fraction as F
from itertools import product
from math import floor, lcm
import json

class Q2:
    def __init__(self, a=0, b=0):
        if isinstance(a, Q2): self.a, self.b = a.a, a.b
        else: self.a, self.b = F(a), F(b)
    def __add__(self, other):
        t=Q2(other); return Q2(self.a+t.a,self.b+t.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self, other): return self+-Q2(other)
    def __rsub__(self, other): return Q2(other)+-self
    def __mul__(self, other):
        t=Q2(other); return Q2(self.a*t.a+2*self.b*t.b,self.a*t.b+self.b*t.a)
    __rmul__=__mul__
    def __truediv__(self, other):
        t=Q2(other); d=t.a*t.a-2*t.b*t.b
        if not d: raise ZeroDivisionError
        return self*Q2(t.a/d,-t.b/d)
    def __rtruediv__(self, other): return Q2(other)/self
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if a==0: return (b>0)-(b<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        d=a*a-2*b*b
        return ((d>0)-(d<0))*(1 if a>0 else -1)
    def __eq__(self, other):
        t=Q2(other); return self.a==t.a and self.b==t.b
    def __lt__(self, other): return (self-Q2(other)).sign()<0
    def __le__(self, other): return (self-Q2(other)).sign()<=0
    def __gt__(self, other): return (self-Q2(other)).sign()>0
    def __ge__(self, other): return (self-Q2(other)).sign()>=0
    def __float__(self): return float(self.a)+float(self.b)*2**.5
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f'({self.a})+({self.b})*sqrt(2)'

def solve(matrix, rhs):
    n=len(rhs)
    rows=[[Q2(x) for x in row]+[Q2(b)] for row,b in zip(matrix,rhs)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if rows[i][col]!=0)
        rows[col],rows[pivot]=rows[pivot],rows[col]
        q=rows[col][col]; rows[col]=[x/q for x in rows[col]]
        for i in range(n):
            if i!=col:
                q=rows[i][col]; rows[i]=[x-q*y for x,y in zip(rows[i],rows[col])]
    return [row[-1] for row in rows]

def graph_laplacian(n, edges):
    # Positive L=-Delta. Edges have (a,b,length,weight).
    matrix=[[Q2() for _ in range(n)] for _ in range(n)]
    for a,b,length,weight in edges:
        if a==b: continue
        c=Q2(weight)/length
        matrix[a][a]+=c; matrix[b][b]+=c
        matrix[a][b]-=c; matrix[b][a]-=c
    return matrix

def poisson(n,edges,rhs,anchor=0):
    assert sum(rhs,Q2())==0
    if n==1: return [Q2()]
    mat=graph_laplacian(n,edges); ids=[v for v in range(n) if v!=anchor]
    vals=solve([[mat[i][j] for j in ids] for i in ids],[-rhs[i] for i in ids])
    out=[Q2() for _ in range(n)]
    for i,x in zip(ids,vals): out[i]=x
    assert delta(n,edges,out)==[Q2(x) for x in rhs]
    return out

def delta(n,edges,values):
    out=[Q2() for _ in range(n)]
    for a,b,length,weight in edges:
        s=(values[b]-values[a])*Q2(weight)/length
        out[a]+=s;out[b]-=s
    return out

def energy(edges,values,other=None):
    if other is None: other=values
    return sum((Q2(w)*(values[b]-values[a])*(other[b]-other[a])/ell
                for a,b,ell,w in edges),Q2())

def bracket(chord, denominator):
    # The float supplies a guess only; exact inequalities verify and repair it.
    k=floor(float(chord)*denominator)
    while Q2(F(k,denominator))>chord: k-=1
    while Q2(F(k+1,denominator))<=chord: k+=1
    lower=F(k,denominator); upper=F(k+1,denominator)
    if Q2(lower)==chord: lower-=F(1,denominator)
    assert Q2(lower)<chord<Q2(upper)
    return lower,upper

def interpolate(n,edges,theta,mu,eps):
    V=sum(theta,Q2());rho=[V/n for _ in range(n)]
    target=[(1-eps)*m+eps*r for m,r in zip(mu,rho)]
    f=poisson(n,edges,[m-t for m,t in zip(target,theta)])
    denominator=8
    while True:
        masses=[Q2(x) for x in theta]; newedges=[]; values=list(f); slopes=[]; bends=[]
        for a,b,ell,w in edges:
            assert a!=b
            q1,q2=bracket((f[b]-f[a])/ell,denominator)
            t=(f[b]-f[a]-q2*ell)/(q1-q2)
            assert 0<t<ell
            c=len(values);values.append(f[a]+q1*t)
            newedges.extend([(a,c,t,w),(c,b,ell-t,w)])
            masses[a]+=w*q1; masses[b]-=w*q2
            bends.append(Q2(w*(q2-q1)));slopes.extend([q1,q2])
        if all(m>0 for m in masses): break
        denominator*=2
        assert denominator<2**24
    allmasses=masses+bends
    actual=[Q2(x) for x in theta]+[Q2() for _ in bends]
    actual=[t+d for t,d in zip(actual,delta(len(values),newedges,values))]
    assert actual==allmasses
    assert all(x>0 for x in allmasses)
    assert sum(allmasses,Q2())==V
    slope_denominator=lcm(*(s.denominator for s in slopes)) if slopes else 1
    assert all((s*slope_denominator).denominator==1 for s in slopes)
    for a,b,ell,w in newedges: assert (values[b]-values[a])/ell in [Q2(s) for s in slopes]
    assert -sum((x*d for x,d in zip(values,delta(len(values),newedges,values))),Q2())==energy(newedges,values)
    return f,denominator,masses,bends,newedges,values

def kernel(n,edges,anchor=0):
    mat=[]
    for y in range(n):
        rhs=[Q2() for _ in range(n)];rhs[anchor]+=1;rhs[y]-=1
        mat.append(poisson(n,edges,rhs,anchor))
    for x in range(n):
        for y in range(n):
            assert mat[x][y]==mat[y][x]
            assert mat[x][y]>=0
            assert energy(edges,mat[x],mat[y])==mat[x][y]
    return mat

def compositions(total,n):
    for tup in product(range(total+1),repeat=n):
        if sum(tup)==total: yield tup

def run():
    s=Q2(0,1)
    graphs=[('parallel-irrational-cycle',2,[(0,1,Q2(1),F(1)),(0,1,s,F(1))],[Q2(1),Q2(1)]),
            ('signed-theta-triangle',3,[(0,1,Q2(1),F(1)),(1,2,s,F(1)),(2,0,Q2(1,1),F(1))],[Q2(-1),Q2(1),Q2(3)]),
            ('weighted-cycle',3,[(0,1,s,F(2)),(1,2,Q2(2),F(3)),(2,0,Q2(1),F(1))],[Q2(0),Q2(0),Q2(3)]),
            ('subdivided-self-loop',2,[(0,1,s/2,F(1)),(0,1,s/2,F(1))],[Q2(2),Q2(0)])]
    count=0;max_denominator=0
    for name,n,edges,theta in graphs:
        V=sum(theta,Q2());kernel(n,edges)
        for tup in compositions(6,n):
            mu=[V*F(k,6) for k in tup]
            for eps in [F(1,8),F(1,64)]:
                _,den,*_=interpolate(n,edges,theta,mu,eps)
                max_denominator=max(max_denominator,den);count+=1
    assert poisson(1,[],[Q2()])==[Q2()]
    assert kernel(1,[])==[[Q2()]]
    # The exact working-observation prototype, checked independently.
    d=F(9,10)*(2-s);old=[Q2(),d];edges=graphs[0][2]
    qlist=[(F(52,100),F(53,100)),(F(37,100),F(38,100))]
    prototype=[];masses=[Q2(1),Q2(1)]
    for (a,b,ell,w),(q1,q2) in zip(edges,qlist):
        assert q1<(d/ell)<q2
        t=(d-q2*ell)/(q1-q2);assert 0<t<ell
        prototype.append({'length':repr(ell),'bend_position':repr(t),'bend_mass':str(q2-q1)})
        masses[a]+=q1;masses[b]-=q2
    assert masses==[Q2(F(189,100)),Q2(F(9,100))]
    assert sum(masses,Q2())+F(2,100)==2
    # Add two edges forming a branch at vertex 1 of a core with a cycle.
    base=graphs[1][2];oldj=kernel(3,base)
    expanded=base+[(1,3,Q2(F(2,3)),F(1)),(3,4,s/2,F(1))]
    newj=kernel(5,expanded)
    r=[0,1,2,1,1];h=[Q2(),Q2(),Q2(),Q2(F(2,3)),Q2(F(2,3))+s/2]
    for x in range(5):
        for y in range(5):
            common=min(h[x],h[y]) if x in [3,4] and y in [3,4] else Q2()
            assert newj[x][y]==oldj[r[x]][r[y]]+common
    # Raw-mass constants, using exactly specified finite probability grid.
    raw_checks=0
    for tup in compositions(4,5):
        nu=[F(k,4) for k in tup]
        I=sum((nu[x]*nu[y]*newj[x][y] for x in range(5) for y in range(5)),Q2())
        for V in [F(1,2),F(1),F(3)]:
            pot=[-V*sum((nu[y]*newj[x][y] for y in range(5)),Q2()) for x in range(5)]
            theta=[Q2(V)]+[Q2() for _ in range(4)]
            curvature=[a+b for a,b in zip(theta,delta(5,expanded,pot))]
            assert curvature==[Q2(V*q) for q in nu]
            integral=sum((u*V*q for u,q in zip(pot,nu)),Q2())
            E=integral/2;assert E==-V*V*I/2
            assert E-integral==V*V*I/2
            raw_checks+=1
    return {'status':'all exact assertions passed','interpolation_cases':count,
            'maximum_slope_grid_denominator':max_denominator,'raw_mass_cases':raw_checks,
            'single_point_checked':True,'subdivided_self_loop_checked':True,
            'kernel_symmetry_and_branch_extension_checked':True,
            'prototype_original_masses':[repr(x) for x in masses],'prototype_edges':prototype,
            'limitation':'Exhaustive only for the specified finite grids. Q(sqrt(2)) arithmetic checks no formal, algebraic, psh, or analytic assertion.'}

if __name__=='__main__': print(json.dumps(run(),indent=2,sort_keys=True))
