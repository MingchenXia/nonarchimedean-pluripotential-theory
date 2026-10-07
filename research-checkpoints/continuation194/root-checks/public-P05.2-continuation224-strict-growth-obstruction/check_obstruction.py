#!/usr/bin/env python3
"""Exact finite checks, not a proof of the envelope or analytic assertions."""
from fractions import Fraction as F
from itertools import combinations, product
from functools import reduce
from math import gcd
import json, platform, shutil
from pathlib import Path

E = [(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)]
pairs = list(combinations(range(4), 2))
exceptional = {(0,1),(2,3)}
add = lambda x,y: tuple(a+b for a,b in zip(x,y))
scale = lambda c,x: tuple(c*a for a in x)
def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def saturated(a,b):
    return reduce(gcd, (abs(a[i]*b[j]-a[j]*b[i]) for i,j in combinations(range(3),2))) == 1
def fan_divisor(single, double):
    sr=[sum(double[tuple(sorted((i,j)))] for j in range(4) if j!=i)-2*single[i] for i in range(4)]
    dr={ij:single[ij[0]]+single[ij[1]]-double[ij] for ij in pairs}
    balance=(0,0,0)
    for i,w in enumerate(sr): balance=add(balance,scale(w,E[i]))
    for (i,j),w in dr.items(): balance=add(balance,scale(w,add(E[i],E[j])))
    assert balance==(0,0,0)
    return sr, dr, sum(w*v for w,v in zip(sr,single))+sum(dr[ij]*double[ij] for ij in pairs)
def polygon_area(points):
    return abs(sum(points[k][0]*points[(k+1)%len(points)][1]-points[(k+1)%len(points)][0]*points[k][1] for k in range(len(points))))/F(2)
def values(ij,a,b,A,B,C,eps):
    h=max(a,b)
    eta=abs(a-b) if ij in exceptional else h
    u=max(eps-min(a,b),F(0)) if ij in exceptional else eps
    ref=A*eta+B*h
    return ref,ref+C*u,ref+B*u,u

inp=json.loads(Path('obstruction-input.json').read_text())
cases=[]
for raw in inp['parameters']:
    A,B,C,eps=map(F,raw)
    assert A>=0 and B>0 and C>B and eps>0
    S=A+B
    singles=[S]*4
    doubles={ij:(B if ij in exceptional else S) for ij in pairs}
    sr,dr,degree=fan_divisor(singles,doubles)
    germ_doubles={ij:(0 if ij in exceptional else S) for ij in pairs}
    osr,odr,origin=fan_divisor(singles,germ_doubles)
    assert sr==[B]*4 and osr==[0]*4
    assert origin==4*S*S
    # Primitive local rays at either special vertex: +diag,-diag,+axis1,+axis2.
    local_weights=[2*A+B,2*S,B,B]
    local_slopes=[B,0,S,S]
    local_vectors=[(1,1),(-1,-1),(1,0),(0,1)]
    assert tuple(sum(w*v[k] for w,v in zip(local_weights,local_vectors)) for k in range(2))==(0,0)
    special=sum(w*s for w,s in zip(local_weights,local_slopes))
    poly=[(S,-S),(S,-A),(-A,S),(-S,S)]
    area=polygon_area(poly)
    assert special==B*(4*A+3*B)==2*area
    assert degree==origin+2*special==4*A*A+16*A*B+10*B*B
    integral=(B-C)*eps*origin
    sample_count=midpoints=0
    grid=[F(k,4)*eps for k in range(13)]
    for ij in pairs:
        for a,b in product(grid,repeat=2):
            ref,obs,env,u=values(ij,a,b,A,B,C,eps)
            assert ref<=env<=obs
            assert env-obs==(B-C)*u
            sample_count+=1
        points=[(F(k,2)*eps,F(l,2)*eps) for k in range(5) for l in range(5)]
        for (a,b),(c,d) in combinations(points,2):
            pm=values(ij,(a+c)/2,(b+d)/2,A,B,C,eps)[2]
            assert 2*pm<=values(ij,a,b,A,B,C,eps)[2]+values(ij,c,d,A,B,C,eps)[2]
            midpoints+=1
    cases.append({'A':str(A),'B':str(B),'C':str(C),'epsilon':str(eps),'degree':str(degree),'origin_mass':str(origin),'each_special_mass':str(special),'each_special_Alexandrov_area':str(area),'contact_integral':str(integral),'point_checks':sample_count,'midpoint_checks':midpoints})

cone_checks=[]
for i,j in pairs:
    d=add(E[i],E[j])
    for k in (i,j):
        assert saturated(E[k],d)
        cone_checks.append({'generators':[E[k],d],'saturated':True})
    # Balancing across a pair ray uses e_i+e_j=e_ij.
    assert add(E[i],E[j])==d
for i in range(4):
    assert add(add(E[(i+1)%4],E[(i+2)%4]),E[(i+3)%4])==scale(-1,E[i])
assert all(abs(det3(*[E[k] for k in ijk]))==1 for ijk in combinations(range(4),3))

report={'kind':'exhaustive finite algebraic and sampled inequality checks; mathematical proofs are in the manuscript','fine_cones':len(cone_checks),'cone_checks':cone_checks,'cases':cases,'all_assertions_passed':True}
Path('evidence/check-output.json').write_text(json.dumps(report,indent=2)+'\n')
env={'python':platform.python_version(),'platform':platform.platform(),'dependencies':'Python standard library only','tools':{n:shutil.which(n) for n in ['pdflatex','latexmk','pdftotext','curl']},'supervised_compute':'none exposed; no resource-heavy computation attempted'}
Path('evidence/environment.json').write_text(json.dumps(env,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='cone_checks'},indent=2))
