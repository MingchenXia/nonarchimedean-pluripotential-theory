from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

target=Path('/tmp/lin_face_calculation_20261004.json')
assert not target.exists(), 'Calculation already recorded; do not rerun.'
slopes=[(0,0),(1,1),(2,1),(0,-3),(1,-3),(2,-3)]

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull(points):
    points=sorted(set(points))
    if len(points)<3: return points
    lower=[]
    for p in points:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def area(points):
    polygon=hull(points)
    if len(polygon)<3: return F(0)
    return abs(sum(polygon[i][0]*polygon[(i+1)%len(polygon)][1]-polygon[i][1]*polygon[(i+1)%len(polygon)][0] for i in range(len(polygon))))/F(2)

def atoms(constants):
    candidates=set()
    for i,j,k in combinations(range(6),3):
        a,b=slopes[j][0]-slopes[i][0],slopes[j][1]-slopes[i][1]
        c,d=slopes[k][0]-slopes[i][0],slopes[k][1]-slopes[i][1]
        determinant=a*d-b*c
        if not determinant: continue
        rhs1,rhs2=constants[i]-constants[j],constants[i]-constants[k]
        x,y=(rhs1*d-b*rhs2)/determinant,(a*rhs2-rhs1*c)/determinant
        values=[F(s[0])*x+F(s[1])*y+constant for s,constant in zip(slopes,constants)]
        maximum=max(values)
        if values[i]==values[j]==values[k]==maximum: candidates.add((x,y))
    result=[]
    for x,y in sorted(candidates):
        values=[F(s[0])*x+F(s[1])*y+constant for s,constant in zip(slopes,constants)]
        active=[s for s,value in zip(slopes,values) if value==max(values)]
        volume=area(active)
        if volume>0: result.append({'point':(x,y),'active_slopes':active,'area':volume,'geometric_mass':2*volume})
    return result

def line_atoms(constants):
    # Restrict all six affine functions, rather than entering the proposed
    # one-dimensional formula or its anticipated two jump coefficients.
    restricted=list(set((F(s[0]),c) for s,c in zip(slopes,constants)))
    candidates=set()
    for (a,c),(b,d) in combinations(restricted,2):
        if a!=b:
            x=(d-c)/(a-b)
            if x>0: candidates.add(x)
    result=[]
    for x in sorted(candidates):
        maximum=max(a*x+c for a,c in restricted)
        active=[a for a,c in restricted if a*x+c==maximum]
        jump=max(active)-min(active)
        if jump: result.append((x,jump))
    return result

records=[]
degree=2*area(slopes)
assert degree==15
for lam in [F(1),F(1,7),F(5)]:
    constants=[F(0),-lam,-3*lam,F(0),-lam,-3*lam]
    varied=[F(0),-lam,-3*lam,-lam,-2*lam,-4*lam]
    original,variation=atoms(constants),atoms(varied)
    assert [(a['point'],a['geometric_mass']) for a in original]==[((lam,F(0)),F(7)),((2*lam,F(0)),F(8))]
    assert sum(a['geometric_mass'] for a in original)==degree
    assert sum(a['geometric_mass'] for a in variation)==degree
    assert not any(a['point'][0]>0 and a['point'][1]==0 for a in variation)
    assert line_atoms(constants)==line_atoms(varied)==[(lam,F(1)),(2*lam,F(1))]
    records.append({'lambda':lam,'original_atoms':original,'same_face_variation_atoms':variation,'intrinsic_one_dimensional_atoms':line_atoms(constants)})

def serialize(obj):
    if isinstance(obj,F): return str(obj)
    raise TypeError(type(obj).__name__)
result={'source':'Lin, arXiv:2609.12969v1, Remark 9.8, PDF pages 29–30','scope':'Exact independent enumeration of all active affine triples, subgradient hull areas, and one-dimensional slope jumps for the published example and a direct constant-shift variation. This is a calculation audit, not a new verifier receipt.','degree':degree,'records':records}
target.write_text(json.dumps(result,default=serialize,indent=2)+'\n')
print(json.dumps(result,default=serialize))
