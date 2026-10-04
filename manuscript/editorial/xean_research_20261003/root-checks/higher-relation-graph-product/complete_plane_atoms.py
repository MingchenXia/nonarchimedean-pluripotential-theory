"""Exact finite diagnostic; not a proof of arbitrary graph-product classification."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json

C,delta,A,epsilon=Q(1),Q(1,2),Q(1,4),Q(1,4)
def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    points=sorted(set(points))
    if len(points)<2:return points
    lo=[];hi=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def mass(points):
    p=hull(points)
    if len(p)<3:return Q(0)
    # Twice polygon area = the dimension-two intersection normalization.
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p))))
def plane(s):
    forms=sorted(set([(sx,sy,Q(0)) for sx,sy in product([-Q(1),Q(1)],repeat=2)]
        +[(delta*sx,delta*sy,C) for sx,sy in product([-Q(1),Q(1)],repeat=2)]
        +[(delta*epsilon*s*sx,delta*sy,C+delta*A) for sx,sy in product([-Q(1),Q(1)],repeat=2)]))
    vertices={(Q(0),Q(0))}
    for f,g,h in combinations(forms,3):
        a,b=g[0]-f[0],g[1]-f[1];c,d=h[0]-f[0],h[1]-f[1]
        det=a*d-b*c
        if not det:continue
        e,k=f[2]-g[2],f[2]-h[2]
        x,y=(e*d-b*k)/det,(a*k-e*c)/det
        value=f[0]*x+f[1]*y+f[2]
        if all(z[0]*x+z[1]*y+z[2]<=value for z in forms):vertices.add((x,y))
    atoms=[]
    for x,y in sorted(vertices):
        value=max(f[0]*x+f[1]*y+f[2] for f in forms)
        active=[f[:2] for f in forms if f[0]*x+f[1]*y+f[2]==value]
        coefficient=mass(active)
        gap=-max(Q(0),Q(1)-8*abs(x)-8*abs(y))
        atoms.append({'point':[str(x),str(y)],'active_gradient_hull':[[str(a),str(b)] for a,b in hull(active)],
                      'mass':str(coefficient),'contact_gap':str(gap),'contact_term':str(gap*coefficient)})
    return {'s':s,'affine_forms':[[str(x) for x in f] for f in forms],'atoms':atoms,
            'total_mass':str(sum(Q(a['mass']) for a in atoms)),
            'contact_integral':str(sum(Q(a['contact_term']) for a in atoms))}

planes=[plane(1),plane(0)]
assert [p['total_mass'] for p in planes]==['8','8']
assert [p['contact_integral'] for p in planes]==['-1/2','0']
merged={}
for index,p in enumerate(planes):
    for a in p['atoms']:
        x,y=a['point']
        key=(x,'0',y) if index==0 else ('0',x,y)
        merged[key]=merged.get(key,Q(0))+Q(a['mass'])
assert merged[('0','0','0')]==Q(1,2)
assert sum(merged.values())==16
assert len(merged)==19
# Both supporting plane lattices are saturated: a primitive 2x2 minor is one.
bases=[[(1,0,0),(0,0,1)],[(0,1,0),(0,0,1)]]
from math import gcd
indices=[]
for a,b in bases:
    minors=[abs(a[i]*b[j]-a[j]*b[i]) for i,j in combinations(range(3),2)]
    indices.append(gcd(*minors))
assert indices==[1,1]
result={'diagnostic_scope':'Cross graph with four unit weights times the unit-weight affine line. Fixed gamma=|x|+|y| on either component plane. Exact rational max-affine area diagnostic only; not an analytic proof or universal graph-product theorem.',
    'parameters':{'C':str(C),'delta':str(delta),'A':str(A),'epsilon':str(epsilon)},
    'P':'max(|x|+|y|, C+delta*|x|+delta*|y|, C+delta*A+delta*epsilon*s*|x|+delta*|y|), with s=1 on horizontal plane and0 on vertical plane.',
    'obstacle':'u_total=P-gamma+max(0,1-8|x|-8|y|); gap=-max(0,1-8|x|-8|y|).',
    'support_bound':'P=gamma when |x|+|y|>=9/4; bump supported where |x|+|y|<=1/8.',
    'primitive_plane_bases':bases,'saturated_plane_indices':indices,'component_planes':planes,
    'all_merged_atoms':[{'point':list(k),'mass':str(v)} for k,v in sorted(merged.items())],
    'merged_spatial_vertices':len(merged),'complete_total_mass':'16','complete_contact_integral':'-1/2',
    'origin_mass':'1/2','all_other_nonzero_mass_atoms_have_zero_gap':True,
    'limits':'Finite exact diagnostic from component-plane Alexandrov dual areas with factorial2 and unit saturated indices. Global actual-PC/PAPC/raw-envelope proof and the unrestricted graph-product classification require separate reconstruction and independent review.'}
Path('output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'vertices':len(merged),'total_mass':16,'contact_integral':'-1/2','indices':indices}))
