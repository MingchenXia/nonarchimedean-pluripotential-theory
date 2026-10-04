"""Exact local saturated-normal diagnostic, not an analytic/global theorem."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from pathlib import Path
import json

# Q(sqrt(2)); no floating arithmetic.
class R:
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    def __add__(self,x):
        x=x if isinstance(x,R) else R(x)
        return R(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return R(-self.a,-self.b)
    def __sub__(self,x): return self+-x if isinstance(x,R) else self+R(-x)
    def __mul__(self,x):
        x=x if isinstance(x,R) else R(x)
        return R(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __eq__(self,x):
        x=x if isinstance(x,R) else R(x)
        return (self.a,self.b)==(x.a,x.b)
    def data(self): return {'rational':str(self.a),'sqrt2':str(self.b)}

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def coordinates(u,a,b,c):
    d=det(a,b,c); assert d
    return (Q(det(u,b,c),d),Q(det(a,u,c),d),Q(det(a,b,u),d))
def linear(u,a,b,c,values): return sum((x*y for x,y in zip(coordinates(u,a,b,c),values)),R())

e=(1,1,1)
rays=[(1,0,0),(1,2,0),(-1,1,0),(-2,-1,0),(0,-1,0)]
weight=R(0,1)
assert det(e,(1,0,0),(0,1,0))==1
n=len(rays)
cones=[(i,(i+1)%n) for i in range(n)]
indices=[abs(det(e,rays[i],rays[j])) for i,j in cones]
assert indices==[2,3,3,2,1]
normals={}
rows=[]
for i,r in enumerate(rays):
    face_normal=cross(e,r)
    assert gcd(gcd(abs(face_normal[0]),abs(face_normal[1])),abs(face_normal[2]))==1
    incident=[(a,b) for a,b in cones if i in (a,b)]
    chosen=[]
    for a,b in incident:
        j=b if a==i else a
        sign=1 if dot(face_normal,rays[j])>0 else -1
        u=next(u for u in product(range(-4,5),repeat=3) if dot(face_normal,u)==sign)
        normals[(i,j)]=u
        chosen.append({'other_ray':j,'normal':list(u),'primitive_quotient_pairing':dot(face_normal,u)})
    summed=tuple(sum(normals[(i,(b if a==i else a))][k] for a,b in incident) for k in range(3))
    t=next(v for v in [(1,0,0),(0,1,0),(0,0,1)] if det(e,r,v))
    coeff=coordinates(summed,e,r,t)
    assert coeff[2]==0
    rows.append({'ray':i,'primitive_facet_normal':list(face_normal),'incident_normals':chosen,'normal_sum':list(summed),'sum_face_coefficients':[str(x) for x in coeff]})

# Direct facet recursion in the saturated Z^3 lattice.
def first(values,face_value):
    result=[]
    for i,r in enumerate(rays):
        incident=[(a,b) for a,b in cones if i in (a,b)]
        s=[0,0,0]; value=R()
        for a,b in incident:
            j=b if a==i else a; u=normals[(i,j)]
            value+=linear(u,e,r,rays[j],[face_value,values[i],values[j]])
            s=[s[k]+u[k] for k in range(3)]
        t=next(v for v in [(1,0,0),(0,1,0),(0,0,1)] if det(e,r,v))
        value-=linear(s,e,r,t,[face_value,values[i],R()])
        result.append(weight*value)
    assert all(sum((result[i]*rays[i][k] for i in range(n)),R())==0 for k in range(3))
    return result

# Independent codimension-two quotient matrix, including the diagonal term.
matrix=[[R() for j in range(n)] for i in range(n)]
for (i,j),chi in zip(cones,indices):
    matrix[i][j]+=weight*Q(1,chi); matrix[j][i]+=weight*Q(1,chi)
for i,r in enumerate(rays):
    other=[(j,chi) for (a,b),chi in zip(cones,indices) if i in (a,b) for j in [b if a==i else a]]
    s=tuple(sum(Q(rays[j][k],chi) for j,chi in other) for k in range(3))
    k=next(k for k in range(3) if r[k]); tangent=Q(s[k],r[k])
    assert all(s[k]==tangent*r[k] for k in range(3))
    matrix[i][i]=-weight*tangent
assert all(matrix[i][j]==matrix[j][i] for i in range(n) for j in range(n))

checks=[]
for trial in range(12):
    f=[R((trial+2*i)%7-3,Q(i-trial,5)) for i in range(n)]
    g=[R((2*trial+3*i)%9-4,Q(trial-i,7)) for i in range(n)]
    af=first(f,R(trial+1,Q(trial,3)))
    ag=first(g,R(2-trial,Q(trial+2,11)))
    assert af==first(f,R(-37,Q(29,13)))
    assert ag==first(g,R(41,Q(-17,19)))
    assert af==[sum((matrix[i][j]*f[j] for j in range(n)),R()) for i in range(n)]
    fg=sum((af[i]*g[i] for i in range(n)),R())
    gf=sum((ag[i]*f[i] for i in range(n)),R())
    assert fg==gf
    checks.append({'trial':trial,'f':[x.data() for x in f],'g':[x.data() for x in g],'first_f':[x.data() for x in af],'first_g':[x.data() for x in ag],'second_fg':fg.data(),'second_gf':gf.data(),'common_face_linear_change_invariant':True,'first_cycle_balanced':True,'matrix_match':True})

print(json.dumps({'scope':'LOCAL codimension-two saturated quotient diagnostic in Z^3 with actual lineality face; not a global contact, regularization or analytic proof','lattice':'Z^3','common_face_primitive_generator':list(e),'ray_lifts':[list(x) for x in rays],'actual_3D_indices':indices,'actual_positive_real_cone_weight':weight.data(),'facet_normal_data':rows,'full_quotient_matrix':[[x.data() for x in row] for row in matrix],'checks':checks,'zero_failures':True,'admission_boundary':'Written after round24 input admission; not injected into its worker or independent review.'},indent=2))
