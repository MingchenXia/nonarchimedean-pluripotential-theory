#!/usr/bin/env python3
"""Small exact observations only. These do not prove analytic descent."""
from fractions import Fraction as F
import json

# Explicit finite tree; involution swaps the first two arms.
vertices = ['a', 'l', 'o', 'r', 'b', 'c']
edges = [('a','l',F(1)), ('l','o',F(2)), ('o','r',F(2)),
         ('r','b',F(1)), ('o','c',F(2))]
swap = dict(a='b', b='a', l='r', r='l', o='o', c='c')
adj = {v: [] for v in vertices}
for v,w,length in edges:
    adj[v].append((w,length)); adj[w].append((v,length))
def dist(v,w):
    stack = [(v,None,F(0))]
    while stack:
        x,prev,d = stack.pop()
        if x == w: return d
        stack.extend((y,x,d+length) for y,length in adj[x] if y != prev)
    raise AssertionError('disconnected tree')
for v in vertices:
    for w in vertices:
        assert dist(v,w) == dist(swap[v],swap[w])
diam = max(dist(v,w) for v in vertices for w in vertices)
assert diam == 6
assert max(dist('o',v) for v in vertices) == diam/2
assert swap['o'] == 'o'
# Check every half-unit point of all specified edges against every vertex.
grid_checks=0; minimizers=set()
for v,w,length in edges:
    for k in range(int(2*length)+1):
        t=F(k,2)
        ds={x: min(t+dist(v,x),length-t+dist(w,x)) for x in vertices}
        eccentricity=max(ds.values())
        assert eccentricity >= diam/2
        if eccentricity == diam/2:
            if t==0: minimizers.add(v)
            elif t==length: minimizers.add(w)
            else: minimizers.add((v,w,str(t)))
        grid_checks += 1
assert minimizers == {'o'}

# Polynomial arithmetic over Q(i). A polynomial is a dict of (s,t) degrees.
def add(*polys):
    out={}
    for p in polys:
        for m,c in p.items(): out[m]=out.get(m,F(0))+c
    return {m:c for m,c in out.items() if c}
def mul(p,q):
    out={}
    for (a,b),x in p.items():
        for (c,d),y in q.items():
            m=(a+c,b+d); out[m]=out.get(m,F(0))+x*y
    return {m:c for m,c in out.items() if c}
def scale(c,p): return {m:c*x for m,x in p.items() if c*x}
X={(2,0):F(1),(0,2):F(-1)}
Y_without_i={(2,0):F(1),(0,2):F(1)}
Z={(1,1):F(2)}
assert not add(mul(X,X),scale(F(-1),mul(Y_without_i,Y_without_i)),mul(Z,Z))
assert add(X,Y_without_i) == {(2,0):F(2)}
assert add(scale(F(-1),X),Y_without_i) == {(0,2):F(2)}

# All 15 probability vectors with denominator 4 on the specified three leaves.
# Use the root-o common-path kernel, with diagonal depths 3,3,2.
leaves=['a','b','c']; kernel=[[F(3),F(0),F(0)],
                            [F(0),F(3),F(0)], [F(0),F(0),F(2)]]
target_checks=0
for i in range(5):
    for j in range(5-i):
        nu=[F(i,4),F(j,4),F(4-i-j,4)]
        mu=[2*x for x in nu]
        u=[-sum(kernel[r][s]*mu[s] for s in range(3)) for r in range(3)]
        target_integral=sum(mu[r]*u[r] for r in range(3))
        energy=target_integral/2  # root value and reference integral are zero
        objective=energy-target_integral
        quadratic=sum(mu[r]*kernel[r][s]*mu[s] for r in range(3) for s in range(3))
        assert energy == -quadratic/2 and objective == quadratic/2
        assert sum(mu)==2 and energy<=0
        target_checks+=1
assert target_checks == 15
# The explicit conic example has two arms of depth 1, masses 1 each.
example_integral=F(-2); example_energy=example_integral/2
assert example_energy==-1 and example_energy-example_integral==1

# Arithmetic in Q(sqrt(2)), pairs (constant, sqrt(2) coefficient).
def qadd(x,y): return (x[0]+y[0],x[1]+y[1])
def qscale(c,x): return (c*x[0],c*x[1])
ell=(F(0),F(1)); difference=(F(1),F(0)); split=(F(-1),F(1))
s1=F(0); s2=F(1)
remaining=qadd(ell,qscale(F(-1),split))
assert qadd(qscale(s1,split),qscale(s2,remaining))==difference
assert remaining==(F(1),F(0))
# sqrt(2)>1 gives split>0; remaining=1 gives split<ell, without floats.
assert F(2)>F(1)**2 and s2-s1>=0

result={
  'status':'PASS; finite observations, not mathematical certification',
  'tree': {'vertices':vertices,'edges':[(v,w,str(d)) for v,w,d in edges],
           'half_unit_grid_checks':grid_checks,'diameter':str(diam),
           'unique_grid_center':'o','center_fixed_by_involution':True},
  'conic_parametrization_polynomial_identity':True,
  'finite_target_energy_checks':target_checks,
  'explicit_conic_target':{'mass':'2','energy':'-1','target_integral':'-2','objective':'1'},
  'subdivision':{'length':'sqrt(2)','endpoint_difference':'1',
                 'slopes':['0','1'],'split':'sqrt(2)-1','bend':'1'},
  'limitations':'No analytic carrier, psh realization, Galois quotient, or allpoint theorem is verified by this program.'
}
print(json.dumps(result,indent=2))
