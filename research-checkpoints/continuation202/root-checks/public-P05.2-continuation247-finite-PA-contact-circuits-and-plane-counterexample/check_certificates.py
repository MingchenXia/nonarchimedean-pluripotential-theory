"""Small exact evidence for the paper. No package dependencies.
The proofs, not this finite enumeration, establish continuum statements."""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt, gcd
import json, pathlib

INPUT = json.loads(pathlib.Path("certificate-input.json").read_text())

def dot(a,b):
    return sum((F(x)*F(y) for x,y in zip(a,b)), F(0))

def kernel_one(columns):
    """Return a positive one-dimensional kernel, or None, by rational RREF."""
    if not columns:
        return None
    n=len(columns)
    a=[[F(columns[j][i]) for j in range(n)] for i in range(len(columns[0]))]
    pivot=[]; row=0
    for col in range(n):
        q=next((k for k in range(row,len(a)) if a[k][col]),None)
        if q is None: continue
        a[row],a[q]=a[q],a[row]
        div=a[row][col]; a[row]=[x/div for x in a[row]]
        for k in range(len(a)):
            if k!=row and a[k][col]:
                div=a[k][col]; a[k]=[x-div*y for x,y in zip(a[k],a[row])]
        pivot.append(col); row+=1
        if row==len(a): break
    free=[i for i in range(n) if i not in pivot]
    if len(free)!=1: return None
    v=[F(0)]*n; v[free[0]]=F(1)
    for i,col in enumerate(pivot):
        v[col]=-a[i][free[0]]
    if all(x<0 for x in v): v=[-x for x in v]
    if not all(x>0 for x in v): return None
    total=sum(v)
    return [x/total for x in v]

def positive_circuits(rays):
    result=[]
    for size in range(2,min(len(rays),len(rays[0])+1)+1):
        for ix in combinations(range(len(rays)),size):
            v=kernel_one([rays[i] for i in ix])
            if v is None: continue
            full=[F(0)]*len(rays)
            for i,x in zip(ix,v): full[i]=x
            assert all(sum(full[i]*rays[i][j] for i in range(len(rays)))==0
                       for j in range(len(rays[0])))
            result.append(full)
    return result

rays=INPUT["rays"]
circuits=positive_circuits(rays)
expected=[]
for pair in [(0,1),(2,3),(4,5)]:
    row=[F(0)]*6
    for i in pair: row[i]=F(1,2)
    expected.append(row)
assert circuits==expected

# Eight saturated quadrants: each pair is a standard basis of its plane.
cones=[(i,j) for i in range(4) for j in (4,5)]
assert len(cones)==8
for i,j in cones:
    assert dot(rays[i],rays[j])==0
    assert dot(rays[i],rays[i])==dot(rays[j],rays[j])==1
for i in range(6):
    normals=[rays[j if i==k else k] for k,j in cones if i in (k,j)]
    assert all(sum(v[a] for v in normals)==0 for a in range(3))

# Oblique saturated plane: basis e_x, (1,2,1), cross-product gcd is one.
# Squared covolumes and projected heights avoid floating point square roots.
u=[1,0,0]; v=[1,2,1]
cross=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
assert gcd(gcd(abs(cross[0]),abs(cross[1])),abs(cross[2]))==1
plane_covolume_squared=dot(u,u)*dot(v,v)-dot(u,v)**2
covariance_checks=[]
for tangent,normal in [(u,v),(v,u)]:
    facet_covolume_squared=dot(tangent,tangent)
    projected_height_squared=dot(normal,normal)-dot(normal,tangent)**2/facet_covolume_squared
    assert projected_height_squared==plane_covolume_squared/facet_covolume_squared
    covariance_checks.append({
      "facet_covolume_squared":str(facet_covolume_squared),
      "plane_covolume_squared":str(plane_covolume_squared),
      "projected_primitive_height_squared":str(projected_height_squared)
    })

def first(slopes):
    return [sum(F(slopes[j if i==k else k]) for k,j in cones if i in (k,j))
            for i in range(6)]
def mass(slopes):
    return dot(first(slopes),slopes)

# Symbolic polynomial using sparse degree-two exponent dictionaries.
poly={}
for i in range(6):
    for k,j in cones:
        if i not in (k,j): continue
        other=j if i==k else k
        exp=[0]*6; exp[i]+=1; exp[other]+=1
        key=tuple(exp); poly[key]=poly.get(key,F(0))+1
expected_poly={}
for i in range(4):
    for j in (4,5):
        exp=[0]*6; exp[i]=exp[j]=1
        expected_poly[tuple(exp)]=F(2)
assert poly==expected_poly

# Exhaustive finite set of slope vectors verifies positivity and balance.
slopes_count=0
for s in product(range(3),repeat=6):
    weights=first(s)
    assert all(sum(weights[i]*rays[i][a] for i in range(6))==0 for a in range(3))
    A=s[0]+s[1]; B=s[2]+s[3]; C=s[4]+s[5]
    assert mass(s)==2*C*(A+B)>=0
    slopes_count+=1
origin=mass(INPUT["origin_slopes"])
reference=mass(INPUT["reference_slopes"])
costs=[dot(c,INPUT["origin_slopes"]) for c in circuits]
assert (origin,reference,costs)==(8,16,[F(1),F(0),F(1)])
side_directions=[[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
side_weights=[F(2),F(2),F(1),F(1)]
assert all(sum(w*d[a] for w,d in zip(side_weights,side_directions))==0 for a in range(3))
side_mass=dot(side_weights,[1,0,1,1])
assert side_mass==4
assert origin+2*side_mass==reference

R=F(INPUT["roof_radius"])
def gamma(p): return sum(map(abs,p))
def f(p):
    x,y,z=p
    return max(abs(x),abs(y)-1,F(0))+abs(z)
def rho(p): return max(map(abs,p))
def roof(p): return max(R-rho(p),F(0))
def obstacle(p): return f(p)+roof(p)
grid=[F(i,INPUT["finite_grid_denominator"]) for i in INPUT["finite_grid_coordinate_indices"]]
points=set()
for a,z in product(grid,repeat=2):
    points.add((a,F(0),z)); points.add((F(0),a,z))
radial_cases=0
for p in sorted(points):
    assert -1 <= f(p)-gamma(p) <= 0
    assert 0 <= roof(p) <= R
    assert f(p)<=obstacle(p)
    if 0<rho(p)<R:
        y=tuple(R*t/rho(p) for t in p)
        alpha=rho(p)/R
        assert roof(y)==0 and f(p)==alpha*f(y)+(1-alpha)*f((F(0),)*3)
        radial_cases+=1
# A smaller rational grid gives nontrivial roof-interior radial tests.
for a,z in product([F(i,32) for i in range(-7,8)],repeat=2):
    for p in [(a,F(0),z),(F(0),a,z)]:
        if p==(F(0),)*3: continue
        assert 0<rho(p)<R
        y=tuple(R*t/rho(p) for t in p)
        alpha=rho(p)/R
        assert roof(y)==0 and f(p)==alpha*f(y)+(1-alpha)*f((F(0),)*3)
        radial_cases+=1
flat_cases=0
for r in map(F,INPUT["flat_relation_samples"]):
    p=(F(0),r,F(0)); q=(F(0),-r,F(0))
    # General scaled relation endpoints, then the chosen roof-boundary ones.
    y1=tuple(R*t/rho(p) for t in p)
    y2=tuple(R*t/rho(q) for t in q)
    assert all((x+y)/2==0 for x,y in zip(y1,y2))
    assert roof(y1)==roof(y2)==0
    assert (f(y1)+f(y2))/2==f((F(0),)*3)==0
    flat_cases+=1
atoms=[((F(0),)*3,origin),((F(0),F(1),F(0)),side_mass),
       ((F(0),F(-1),F(0)),side_mass)]
contact=sum((f(p)-obstacle(p))*m for p,m in atoms)
assert contact==-R*origin==F(-2)

# Rational upper brackets t_n >= sqrt(1/2), certified by integer squares.
# isqrt(2*d*d)//2 equals floor(d/sqrt(2)).
brackets=[]
last=None; kink_cases=0
for d in INPUT["kink_bracket_denominators"]:
    k=isqrt(2*d*d)//2
    assert 2*k*k < d*d < 2*(k+1)*(k+1)
    low=F(k,d); upper=F(k+1,d)
    assert 2*low*low<1<2*upper*upper
    if last is not None:
        assert upper<=last
        for x in grid:
            assert max(x,2*upper-x)<=max(x,2*last-x)
            kink_cases+=1
    brackets.append({"lower":str(low),"upper":str(upper),"uniform_error_upper_bound":str(F(2,d))})
    last=upper

out={
 "classification_claim":"none; original P05.2 remains open",
 "positive_circuit_rays":[[str(x) for x in row] for row in circuits],
 "saturated_top_quadrants":len(cones),
 "primitive_normal_balances_checked":6,
 "oblique_saturated_covolume_checks":covariance_checks,
 "symbolic_mass_polynomial":"2*(s_zplus+s_zminus)*(s_xplus+s_xminus+s_yplus+s_yminus)",
 "finite_slope_vectors_exhausted":slopes_count,
 "origin_first_weights":[str(x) for x in first(INPUT["origin_slopes"])],
 "origin_extreme_relation_costs":[str(x) for x in costs],
 "raw_masses":[str(origin),str(side_mass),str(side_mass)],
 "reference_raw_mass":str(reference),
 "contact_integral":str(contact),
 "finite_grid_distinct_points":len(points),
 "finite_radial_chord_cases":radial_cases,
 "scaled_flat_PCC_cases":flat_cases,
 "kink_brackets":brackets,
 "finite_kink_monotonicity_cases":kink_cases,
 "all_assertions_passed":True,
 "limitations":"Exact finite evidence only. No finite grid establishes continuum PC, envelope maximality, or general regularization."
}
pathlib.Path("evidence/certificate-output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
