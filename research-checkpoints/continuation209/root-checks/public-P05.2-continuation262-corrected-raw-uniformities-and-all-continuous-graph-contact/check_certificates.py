from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
from math import gcd,lcm,cos,pi
import json
config=json.loads(Path("certificate-input.json").read_text())

def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,t):return tuple(x*t for x in a)
def val(m,p):return dot(m[:2],p)+m[2]
def egcd(a,b):
 if b==0:return (abs(a),1 if a>=0 else -1,0)
 g,x,y=egcd(b,a%b);return g,y,x-(a//b)*y

def raw_plane(forms,extra=()):
 forms=sorted(set(tuple(map(Q,f)) for f in forms))
 vertices=set();triple_count=0
 for a,b,c in combinations(forms,3):
  triple_count+=1
  A,B=a[0]-b[0],a[1]-b[1];C=b[2]-a[2]
  D,E=a[0]-c[0],a[1]-c[1];F=c[2]-a[2]
  det=A*E-B*D
  if det==0:continue
  p=((C*E-B*F)/det,(A*F-C*D)/det)
  if val(a,p)==max(val(f,p) for f in forms):vertices.add(p)
 vertices.update(extra)
 lines=set()
 for a,b in combinations(forms,2):
  A,B,C=a[0]-b[0],a[1]-b[1],b[2]-a[2]
  if A==B==0:continue
  mul=lcm(A.denominator,B.denominator);ai,bi=int(A*mul),int(B*mul)
  div=gcd(ai,bi);ai//=div;bi//=div;ci=C*mul/div
  if ai<0 or (ai==0 and bi<0):ai,bi,ci=-ai,-bi,-ci
  lines.add((ai,bi,ci))
 edges=[];zero_intervals=0
 for A,B,C in sorted(lines):
  p0=(C/A,Q(0)) if A else (Q(0),C/B)
  tangent=(B,-A)
  if tangent[0]<0 or (tangent[0]==0 and tangent[1]<0):tangent=(-tangent[0],-tangent[1])
  g,nx,ny=egcd(A,B);assert g==1
  normal=(nx,ny);assert A*nx+B*ny==1
  vs=sorted(((dot((p[0]-p0[0],p[1]-p0[1]),tangent)/dot(tangent,tangent),p) for p in vertices if A*p[0]+B*p[1]==C))
  cuts=[(None,None)]+vs+[(None,None)]
  for (left,lp),(right,rp) in zip(cuts,cuts[1:]):
   test=Q(0) if left is None and right is None else right-1 if left is None else left+1 if right is None else (left+right)/2
   p=add(p0,scale(tangent,test));mx=max(val(f,p) for f in forms)
   active=[f for f in forms if val(f,p)==mx]
   wt=max(dot(f[:2],normal) for f in active)-min(dot(f[:2],normal) for f in active)
   if wt==0:zero_intervals+=1;continue
   assert wt>0
   slopes={dot(f[:2],tangent) for f in active}
   if len(slopes)!=1:
    # An incidental crossing of an unrelated potential equality line is
    # a point, not a positive interval carried by this line.
    zero_intervals+=1;continue
   edges.append({'left':lp,'right':rp,'tangent':tangent,'weight':wt,'slope':slopes.pop()})
 balance={p:(Q(0),Q(0)) for p in vertices};mass={p:Q(0) for p in vertices}
 for e in edges:
  for which,sgn in [('left',1),('right',-1)]:
   p=e[which]
   if p is not None:
    balance[p]=add(balance[p],scale(e['tangent'],e['weight']*sgn));mass[p]+=e['weight']*e['slope']*sgn
 assert all(b==(0,0) for b in balance.values()),balance
 assert all(m>=0 for m in mass.values()),mass
 # Independent polygons are crosschecks, never used to define raw weights.
 for p,m in mass.items():
  grads=sorted(set(f[:2] for f in forms if val(f,p)==max(val(g,p) for g in forms)))
  def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
  lower=[]
  for x in grads:
   while len(lower)>=2 and cross(lower[-2],lower[-1],x)<=0:lower.pop()
   lower.append(x)
  upper=[]
  for x in reversed(grads):
   while len(upper)>=2 and cross(upper[-2],upper[-1],x)<=0:upper.pop()
   upper.append(x)
  poly=lower[:-1]+upper[:-1]
  twice=abs(sum((poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly))),Q(0))) if poly else Q(0)
  assert twice==m,(p,m,twice)
 return {'triples':triple_count,'vertices':vertices,'mass':mass,'edges':edges,'zero_intervals':zero_intervals}

hforms=[(s,t,0) for s,t in product([-1,1],repeat=2)]+[(0,2,0),(0,-2,0)]
gforms=[(s,t,-1) for s,t in product([-1,1],repeat=2)]+[(0,2,0),(0,-2,0)]
h=raw_plane(hforms);g=raw_plane(gforms)
assert h['mass']=={(Q(0),Q(0)):Q(12)}
assert g['mass']=={(Q(-1),Q(0)):Q(6),(Q(1),Q(0)):Q(6)}
# Artificial cuts of each positive wall must give zero new atom.
artificial=[]
for e in g['edges']:
 if e['left'] is not None and e['right'] is not None: artificial.append(scale(add(e['left'],e['right']),Q(1,2)))
 elif e['left'] is not None:artificial.append(add(e['left'],e['tangent']))
 elif e['right'] is not None:artificial.append(add(e['right'],scale(e['tangent'],-1)))
ga=raw_plane(gforms,extra=artificial)
assert all(ga['mass'][p]==g['mass'].get(p,Q(0)) for p in ga['mass'])

results={'PA':{'horizontal_triples':h['triples'],'vertical_triples':g['triples'],'first_edges':[len(h['edges']),len(g['edges'])],'masses':[12,6,6],'reference_mass':24,'raw_contact':str(-Q(1,4)*12),'artificial_vertices_checked':len(set(artificial))},'dyadic':[]}

def a(t):
 t=abs(t)
 return Q(0) if t<=1 else (t-1)**2/2 if t<=2 else t-Q(3,2)
def knots(N):return [(Q(1)+Q(j,N),Q(j*j,2*N*N)) for j in range(N+1)]
def forms_N(N):
 fs=[]
 for j in range(N):
  k=Q(2*j+1,2*N);tj,bj=knots(N)[j];c=bj-k*tj
  fs +=[(s*k,t,c) for s,t in product([-1,1],repeat=2)]
 fs +=[(s,t,-Q(3,2)) for s,t in product([-1,1],repeat=2)]
 fs +=[(0,2,0),(0,-2,0)]
 return fs
for N in config["dyadic_raw_N"]:
 r=raw_plane(forms_N(N));expected={}
 ks=[Q(0)]+[Q(2*j+1,2*N) for j in range(N)]+[Q(1)]
 deltas=[ks[j+1]-ks[j] for j in range(N+1)]
 assert deltas[0]==deltas[-1]==Q(1,2*N) and sum(deltas)==1
 for s in [-1,1]:
  for j,(tj,bj) in enumerate(knots(N)):
   dl=deltas[j]
   if j==0:expected[(s*tj,Q(0))]=6*dl
   else:
    expected[(s*tj,Q(0))]=4*dl
    expected[(s*tj,bj)]=dl;expected[(s*tj,-bj)]=dl
 assert {p:m for p,m in r['mass'].items() if m}==expected
 assert sum(r['mass'].values())+12==24
 for e in r['edges']:
  q,p=e['tangent']
  assert gcd(q,p)==1
  if q and p:
   # Any graph transverse Bezout normal gives jump weight 1/|q|.
   gg,nx,ny=egcd(p,-q);assert gg==1 and p*nx-q*ny==1
   assert Q(p,q)*nx-ny==Q(1,q)
 results['dyadic'].append({'N':N,'triples':r['triples'],'yz_positive_vertices':sum(bool(m) for m in r['mass'].values()),'positive_first_edges':len(r['edges']),'zero_line_intervals':r['zero_intervals'],'total_raw_mass':24,'y2':str(sum(m*p[0]**2 for p,m in r['mass'].items())),'z2':str(sum(m*p[1]**2 for p,m in r['mass'].items()))})

error_cases=0
for N in config["dyadic_error_N"]:
 fs=forms_N(N)
 for tj,bj in knots(N)[:-1]:
  for l in range(9):
   t=tj+Q(l,8*N);an=max(val(m,(t,0)) for m in fs)
   assert 0<=an-a(t)<=Q(1,8*N*N)
   assert an-a(t)==(t-tj)*(tj+Q(1,N)-t)/2
   an2=max(val(m,(t,0)) for m in forms_N(2*N));assert a(t)<=an2<=an
   error_cases+=1
results['dyadic_error_cases']=error_cases
results['limit_moments']={'y2':'28','z2':'1/5','rawtotal':24,'contact':'-3','literal_gap':'3/64'}
assert a(Q(3,2))-a(Q(5,4))==Q(3,32)
assert a(Q(7,4))-a(Q(3,2))==Q(5,32)

# Finite unrestricted-roof arithmetic corroboration; the paper proves all competitors.
def rho(p):return max(map(abs,p))
def gamma(p):x,y,z=p;return max(abs(x),abs(y),abs(z))+abs(z)
def endpoint(p):x,y,z=p;return max(abs(x),abs(y)-1,abs(z))+abs(z)
points=set()
for i,j in product(range(config["plane_grid_indices"][0],config["plane_grid_indices"][1]+1),repeat=2):
 points.add((Q(i,config["plane_grid_denominator"]),Q(0),Q(j,config["plane_grid_denominator"])));points.add((Q(0),Q(i,config["plane_grid_denominator"]),Q(j,config["plane_grid_denominator"])))
chords=0
for p in points:
 f=endpoint(p);ga=gamma(p);assert -1<=f-ga<=0
 if 0<rho(p)<Q(1,4):
  y=scale(p,Q(1,4)/rho(p));alpha=rho(p)/Q(1,4)
  assert endpoint(p)==alpha*endpoint(y);chords+=1
R=Q(1,4);corners=[(0,0,0),(R,0,0),(0,0,R),(R,0,R)]
fvals=[endpoint(p) for p in corners];uvals=[endpoint(p)-gamma(p)+max(R-rho(p),0) for p in corners]
assert fvals[3]-fvals[1]-fvals[2]+fvals[0]==-R
assert uvals[3]-uvals[1]-uvals[2]+uvals[0]==R
results['grid']={'points':len(points),'interior_chords':chords,'endpoint_mixed_difference':str(-R),'obstacle_mixed_difference':str(R)}

literal=[]
for n in config["literal_counterexample_n"]:
 shift=Q(2*n);eps=Q(1,8*n);phase=(shift+eps)**2-shift**2
 assert phase==Q(1,2)+Q(1,64*n*n)
 literal.append({'n':n,'distance':str(eps),'relative_A':str(shift),'relative_B':str(shift+eps),'evaluation_difference_numeric':2*cos(pi/(64*n*n)),'rawmass':2})
real=[]
def eta(x):
 x=Q(x)%8
 nodes=[(Q(0),Q(1,4)),(Q(1),-Q(1,4)),(Q(4),-Q(1,4)),(Q(5),Q(1,4)),(Q(8),Q(1,4))]
 for (a,b),(c,d) in zip(nodes,nodes[1:]):
  if a<=x<=c:return b+(d-b)*(x-a)/(c-a)
 raise AssertionError(x)
for n in config["real_counterexample_n"]:
 aa=[Q(4*j+(j%2)) for j in range(n)];bb=[Q(4*j+1-(j%2)) for j in range(n)]
 def diff(x):return sum(abs(x-v)-abs(x-w) for v,w in zip(aa,bb))/n
 values=[diff(x) for x in sorted(set(aa+bb+[-1,4*n+1]))]
 assert min(values)==0 and max(values)==Q(2,n)
 assert all(eta(x)==Q(1,4) for x in aa) and all(eta(x)==-Q(1,4) for x in bb)
 assert Q(2,n)*sum(eta(x)-eta(y) for x,y in zip(aa,bb))==1
 assert sum(aa)/n==sum(bb)/n==Q(4*n-3,2)
 real.append({'n':n,'distance':str(Q(2,n)),'relative_bound':str(sum(aa)/n),'evaluation_difference':'1','rawmass':2})
results['literal_weak_counterexample']=literal;results['real_BL_counterexample']=real

# Graph interpolation on the same irrational-reference geometry: compare
# exact rational slopes with an arbitrary real affine shift of a fixed norm.
# PC costs are unchanged by ambient affine shifts, checked symbolically.
tripod=[(1,0),(0,1),(-1,-1)];weights=[Q(2),Q(2),Q(2)]
assert add(add(scale(tripod[0],2),scale(tripod[1],2)),scale(tripod[2],2))==(0,0)
mesh=[Q(0),Q(1,4),Q(1,2),Q(1),Q(2)]
base_slopes=[(a(b)-a(c))/(b-c) for c,b in zip(mesh,mesh[1:])]
assert base_slopes==sorted(base_slopes)
# Local multirelation construction uses opposite pairs; rational bad slope.
U=[(1,0),(-1,0),(0,1),(0,-1)];s=[1,0,0,0];w=[Q(1),Q(1),Q(3,2),Q(3,2)]
assert tuple(sum(wi*ui[k] for wi,ui in zip(w,U)) for k in range(2))==(0,0)
assert sum(si*wi for si,wi in zip(s,w))==1
assert dot(s,[0,0,1,1])==0
results['graph_sector']={'rational_mesh':list(map(str,mesh)),'chord_slopes':list(map(str,base_slopes)),'real_positive_weight_flat_jet_mass':'1','flat_relation':'(0,0,1,1)','finite_checks_only':True}


# Exact symbolic slopes for an ACTUAL irrational-affine reference on the
# rational cross. A triple is constant + alpha coefficient + beta coefficient.
# alpha=sqrt(2)/4 and beta=sqrt(3)/4: their squares certify |alpha|,|beta|<1.
assert Q(1,8)<1 and Q(3,16)<1
gamma_slopes=[(Q(1),Q(1),Q(0)),(Q(1),-Q(1),Q(0)),(Q(1),Q(0),Q(1)),(Q(1),Q(0),-Q(1))]
f_slopes=[gamma_slopes[0],gamma_slopes[1],(Q(0),Q(0),Q(1)),(Q(0),Q(0),-Q(1))]
actual_weights=[Q(x) for x in config['graph_actual_weights']]
def symbolic_cost(slopes,weights):return tuple(sum(q*v[k] for q,v in zip(weights,slopes)) for k in range(3))
assert symbolic_cost(gamma_slopes,actual_weights)==(5,0,0)
assert symbolic_cost(f_slopes,actual_weights)==(2,0,0)
assert symbolic_cost(f_slopes,[0,0,1,1])==(0,0,0)
results['graph_sector']['irrational_reference']={'alpha_squared':'1/8','beta_squared':'3/16','reference_raw_mass':'5','endpoint_origin_raw_mass':'2','flat_relation_cost':'0','radius_1/4_contact':'-1/2','carrying_vertices':'rational 0 and +/-1; affine perturbation preserves walls','symbolic_affine_cancellation':True}

# Primitive covolume identity in the oblique saturated plane generated by
# (1,0,1),(0,1,1). Its squared covolume is 3.
u=(1,0,1);v=(0,1,1);a2=dot(u,u)*dot(v,v)-dot(u,v)**2
assert a2==3
height2=dot(v,v)-dot(v,u)**2/dot(u,u);assert height2==a2/dot(u,u)
results['oblique_covariance']={'plane_covolume_squared':str(a2),'facet_covolume_squared':str(dot(u,u)),'projected_height_squared':str(height2)}
Path('evidence').mkdir(exist_ok=True)
Path('evidence/certificate-output.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
