"""Small, exact finite geometry and full recursive-divisor diagnostic.

The proof of raw envelope equality is in P05.2-argument.md. This program
does not sample or establish arbitrary PCC inequalities. It enumerates all
domains of the specified gamma in the actual 36 product edge planes.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'counterexample-input.json').read_text())

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def primitive(a):
    den=1
    for x in a: den=den*x.denominator//gcd(den,x.denominator)
    z=[int(x*den) for x in a]
    g=0
    for x in z: g=gcd(g,abs(x))
    assert g
    return tuple(F(x//g) for x in z)
def textq(a):
    if isinstance(a,F): return str(a)
    if isinstance(a,(list,tuple)): return [textq(x) for x in a]
    if isinstance(a,dict): return {str(k):textq(v) for k,v in a.items()}
    return a
def rho(z): return sum(abs(x) for x in z)
def gamma(z): return max(abs(z[0]-z[2])+abs(z[1]-z[3]),rho(z)/4-1)
def obstacle(z): return max(F(1)-10*rho(z),F(0))
def geom(constraints):
    """Vertices and recession rays of a pointed plane polyhedron."""
    hs=list(dict.fromkeys(constraints))
    if any(a==b==0 and c<0 for a,b,c in hs): return [],[]
    hs=[h for h in hs if h[0] or h[1]]
    vs=set()
    for (a,b,c),(d,e,f) in combinations(hs,2):
        k=a*e-b*d
        if not k: continue
        x=(b*f-c*e)/k; y=(c*d-a*f)/k
        if all(aa*x+bb*y+cc>=0 for aa,bb,cc in hs): vs.add((x,y))
    rs=set()
    for a,b,c in hs:
        for r in ((b,-a),(-b,a)):
            if all(aa*r[0]+bb*r[1]>=0 for aa,bb,cc in hs):
                rs.add(primitive(r))
    return sorted(vs),sorted(rs)
def full_dim(vs,rs):
    if not vs: return False
    ds=[(v[0]-vs[0][0],v[1]-vs[0][1]) for v in vs[1:]]+rs
    return any(det(a,b) for a,b in combinations(ds,2))

edges=[]
for e in DATA['edges']:
    b=tuple(F(x) for x in e['base']); d=tuple(F(x) for x in e['direction'])
    # g is affine on each of the six actual graph edges.
    g0=sum(abs(x) for x in b)
    g1=sum(abs(x+y) for x,y in zip(b,d))-g0
    edges.append(dict(e,b=b,d=d,g=(g0,g1)))

domains=[]
for e,f in product(edges,repeat=2):
    base=e['b']+f['b']; dirs=(e['d']+(F(0),F(0)),(F(0),F(0))+f['d'])
    # Restrict the four affine pieces of the difference norm and the
    # single affine rho/4-1 to this product edge cell.
    forms=set()
    for sx,sy in product((-1,1),repeat=2):
        cov=(F(sx),F(sy),F(-sx),F(-sy))
        forms.add((dot(cov,dirs[0]),dot(cov,dirs[1]),dot(cov,base)))
    forms.add((e['g'][1]/4,f['g'][1]/4,(e['g'][0]+f['g'][0])/4-1))
    bounds=[(F(1),F(0),F(0)),(F(0),F(1),F(0))]
    if e['length'] is not None: bounds.append((F(-1),F(0),F(e['length'])))
    if f['length'] is not None: bounds.append((F(0),F(-1),F(f['length'])))
    for form in sorted(forms):
        hs=bounds+[tuple(a-b for a,b in zip(form,g)) for g in forms if g!=form]
        vs,rs=geom(hs)
        if not full_dim(vs,rs): continue
        domains.append({'edges':(e['id'],f['id']),'base':base,'dirs':dirs,
                        'form':form,'constraints':hs,'vertices':vs,'rays':rs})

def spatial(D,z): return add(D['base'],add(mul(z[0],D['dirs'][0]),mul(z[1],D['dirs'][1])))
def coordinates(D,z):
    zs=[]
    for off in (0,2):
        k=next(i for i in range(off,off+2) if D['dirs'][off//2][i])
        zs.append((z[k]-D['base'][k])/D['dirs'][off//2][k])
    w=tuple(zs)
    return w if spatial(D,w)==z else None

vertices=sorted({spatial(D,v) for D in domains for v in D['vertices']})
assert (F(0),)*4 in vertices
assert all(v==(F(0),)*4 or rho(v)>=1 for v in vertices)

def recursion(v):
    cones=set(); values={}; ray_faces={}
    for D in domains:
        z=coordinates(D,v)
        if z is None or not all(a*z[0]+b*z[1]+c>=0 for a,b,c in D['constraints']): continue
        # In a common polyhedral complex, every incident 2-cell has this
        # 0-face as a vertex. Verify, rather than assuming, that property.
        assert z in D['vertices'], (v,D['edges'],z)
        active=[(a,b,F(0)) for a,b,c in D['constraints'] if a*z[0]+b*z[1]+c==0]
        _,rs=geom(active)
        assert len(rs)==2,(v,D['edges'],rs)
        r,s=rs; chi=abs(det(r,s)); assert chi>0
        actual=[]
        for q in rs:
            a=primitive(add(mul(q[0],D['dirs'][0]),mul(q[1],D['dirs'][1])))
            # Direct primitive factor directions imply no hidden scaling.
            assert a==add(mul(q[0],D['dirs'][0]),mul(q[1],D['dirs'][1]))
            h=D['form'][0]*q[0]+D['form'][1]*q[1]
            if a in values: assert values[a]==h
            values[a]=h; actual.append(a)
        key=(tuple(sorted(actual)),chi)
        assert key not in cones
        cones.add(key)
    for (r,s),chi in cones:
        ray_faces.setdefault(r,[]).append((s,chi))
        ray_faces.setdefault(s,[]).append((r,chi))
    first={}; rows=[]
    for r in sorted(ray_faces):
        nbr=ray_faces[r]
        S=tuple(sum((s[i]/k for s,k in nbr),F(0)) for i in range(4))
        pivot=next(i for i,x in enumerate(r) if x)
        t=S[pivot]/r[pivot]
        assert S==mul(t,r),('unbalanced top cycle',v,r,S)
        w=sum((values[s]/k for s,k in nbr),F(0))-t*values[r]
        assert w>=0,('negative first divisor',v,r,w)
        first[r]=w
        rows.append({'primitive_ray':r,'germ_value':values[r],
                     'tangential_multiple':t,'first_divisor_weight':w,
                     'neighbors':[{'ray':s,'saturated_cone_index':k} for s,k in sorted(nbr)]})
    assert tuple(sum((w*r[i] for r,w in first.items()),F(0)) for i in range(4))==(F(0),)*4
    mass=sum((w*values[r] for r,w in first.items()),F(0))
    assert mass>=0
    return {'point':v,'gamma':gamma(v),'u':obstacle(v),'gap':-obstacle(v),
            'mass':mass,'integral_contribution':-obstacle(v)*mass,
            'local_top_cones':len(cones),'first_divisor':rows,
            'max_saturated_cone_index':max(k for _,k in cones)}

atoms=[recursion(v) for v in vertices]
origin=next(a for a in atoms if a['point']==(F(0),)*4)
assert origin['mass']==8 and origin['integral_contribution']==-8
assert sum(a['integral_contribution'] for a in atoms)==-8
ui=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(-1))]
pcc=[mul(F(1,4),w+w) for w in ui]
assert tuple(sum(p[i]/3 for p in pcc) for i in range(4))==(F(0),)*4
assert all(gamma(p)==obstacle(p)==0 for p in pcc)

# Independently reconstruct the supplied rectangle-roof diagnostic.
eps=F(1,4); t=F(1,2)
roof_values=[max(1-eps/2,1+eps/2-t),max(1-eps/2,eps/2+t),F(1)]
roof={'epsilon':eps,'center':F(1),'endpoints':roof_values,
      'mean':sum(roof_values)/3,'defect':1-sum(roof_values)/3}
assert roof['defect']==F(1,12)

output={'kind':'exact exhaustive finite diagnostic for specified gamma, not proof verification',
        'product_edge_cells':36,'gamma_top_domains':len(domains),
        'candidate_vertices':len(vertices),'positive_atoms':sum(a['mass']>0 for a in atoms),
        'zero_atoms':sum(a['mass']==0 for a in atoms),
        'total_mass':sum(a['mass'] for a in atoms),
        'complete_contact_integral':sum(a['integral_contribution'] for a in atoms),
        'max_saturated_cone_index':max(a['max_saturated_cone_index'] for a in atoms),
        'all_nonorigin_vertices_have_rho_at_least_one':True,
        'all_first_divisors_balanced_and_nonnegative':True,
        'pcc':{'endpoints':pcc,'coefficients':[F(1,3)]*3,'gamma_values':[gamma(p) for p in pcc],
               'u_values':[obstacle(p) for p in pcc]},
        'origin':origin,'atoms':atoms,'rectangle_roof':roof}
(ROOT/'counterexample-output.json').write_text(json.dumps(textq(output),indent=2)+'\n')
(ROOT/'domain-enumeration.json').write_text(json.dumps(textq(domains),indent=2)+'\n')
print(json.dumps(textq({k:v for k,v in output.items() if k not in ('origin','atoms')}),indent=2))
