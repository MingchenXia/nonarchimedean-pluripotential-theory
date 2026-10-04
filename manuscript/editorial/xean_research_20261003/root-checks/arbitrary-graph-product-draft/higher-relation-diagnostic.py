"""Finite exact primitive-normal diagnostics, using Q(sqrt(2)), no numerical rounding."""
from dataclasses import dataclass
from fractions import Fraction as R
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import json

@dataclass(frozen=True)
class Q:
    a:R=R(0)
    b:R=R(0)
    def __add__(self,o):
        o=qq(o);return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,o):return self+-qq(o)
    def __rsub__(self,o):return qq(o)+-self
    def __mul__(self,o):
        o=qq(o);return Q(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def sign(self):
        if not self.b:return (self.a>0)-(self.a<0)
        if not self.a:return (self.b>0)-(self.b<0)
        if self.a>0 and self.b>0:return 1
        if self.a<0 and self.b<0:return -1
        z=self.a*self.a-2*self.b*self.b
        assert z!=0 # sqrt(2) irrational, nonzero rational pair
        return ((z>0)-(z<0))*((self.a>0)-(self.a<0))
    def js(self):return {'rational':str(self.a),'sqrt2':str(self.b)}

def qq(o):
    if isinstance(o,Q):return o
    if isinstance(o,list):return Q(R(o[0]),R(o[1]))
    return Q(R(o))
def zeros(n):return [Q() for _ in range(n)]
def add(v,u):return [a+b for a,b in zip(v,u)]
def mul(c,v):return [c*qq(a) for a in v]
def rank(rows):
    a=[[R(x) for x in row] for row in rows];r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];s=a[r][j];a[r]=[x/s for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                s=a[k][j];a[k]=[x-s*y for x,y in zip(a[k],a[r])]
        r+=1
    return r
def sat_index(a,b):
    minors=[abs(a[i]*b[j]-a[j]*b[i]) for i,j in combinations(range(len(a)),2)]
    return reduce(gcd,minors,0)

def run(x):
    qs=x['directions']; ws=[qq(w) for w in x['weights']];c=list(map(R,x['relation']))
    r=x['other_direction'];wh=qq(x['other_weight']);delta=qq(x['delta'])
    epsilon=R(x['epsilon']);A=R(x['A']);T=R(x['T']);B=R(x['B']);D=R(x['D'])
    s=[int(ci==0) for ci in c];n=len(qs[0]);m=len(r)
    assert len(qs)==len(ws)==len(c)
    assert all(reduce(gcd,map(abs,q),0)==1 for q in qs)
    assert reduce(gcd,map(abs,r),0)==1
    assert all(w.sign()>0 for w in ws) and wh.sign()>0 and delta.sign()>0
    assert epsilon>0 and A>0 and 0<B<T and D>0
    balance=zeros(n)
    for w,q in zip(ws,qs):balance=add(balance,mul(w,q))
    assert all(v==Q() for v in balance)
    assert all(sum(ci*q[j] for ci,q in zip(c,qs))==0 for j in range(n))
    assert any(c) and any(ci==0 for ci in c)
    kernel_dimension=len(qs)-rank(list(zip(*qs)))
    assert kernel_dimension>=2
    support=[q for ci,q in zip(c,qs) if ci]
    assert len(support)-rank(list(zip(*support)))==1 # specified relation is an extreme ray
    S=sum(c);alpha=[ci/S for ci in c]
    slopes=[sum(map(abs,q)) for q in qs];b=sum(map(abs,r))
    ti=[A/(ri-epsilon*si) for ri,si in zip(slopes,s)]
    assert all(R(0)<t<R(1) for t in ti) and T<min(ti)
    M=sum((w*si for w,si in zip(ws,s)),Q());assert M.sign()>0
    k=delta*epsilon;l=delta*b
    rays=[q+[0]*m for q in qs]+[[0]*n+r,[0]*n+[-a for a in r]]
    values=[k*si for si in s]+[l,l]
    first=[2*l*w*wh for w in ws]+[k*M*wh,k*M*wh]
    primitive_normals=[]
    for i,q in enumerate(qs):
        for sign in (1,-1):
            a=q+[0]*m;bb=[0]*n+[sign*a for a in r]
            assert sat_index(a,bb)==1
            primitive_normals.append({'graph_ray':i,'other_sign':sign,'saturated_plane_index':1,
                'normal_at_graph_axis':bb,'normal_at_other_axis':a,'top_weight':(ws[i]*wh).js()})
    # Full first-cycle balance, not merely nonnegative weights.
    bal=zeros(n+m)
    for d,v in zip(first,rays):bal=add(bal,mul(d,v))
    assert all(v==Q() for v in bal) and all(d.sign()>=0 for d in first)
    graph_sum=sum((d*v for d,v in zip(first[:-2],values[:-2])),Q())
    transverse_sum=sum((d*v for d,v in zip(first[-2:],values[-2:])),Q())
    expected=4*delta*delta*epsilon*b*M*wh
    assert graph_sum==transverse_sum==2*k*l*M*wh
    assert graph_sum+transverse_sum==expected and expected.sign()>0
    # Genuine supported PCC at rational z: endpoints at t=T have zero bump.
    displacement=[sum(a*T*q[j] for a,q in zip(alpha,qs)) for j in range(n)]
    assert all(v==0 for v in displacement) and sum(alpha)==1
    assert sum((a*k*si*T for a,si in zip(alpha,s)),Q())==Q()
    assert max(R(0),1-T/B)==0
    assert all(ri>epsilon*si for ri,si in zip(slopes,s))
    star_span_index=reduce(gcd,[abs(q[0]*p[1]-q[1]*p[0]) for q,p in combinations(qs,2)],0)
    return {'name':x['name'],'relation_cone_rank':kernel_dimension,'whole_star_ray_span_index':star_span_index,
        'support':[i for i,a in enumerate(c) if a],'cap_outgoing_slopes':[str(epsilon*si) for si in s],
        'cap_comparison_points':[str(t) for t in ti], 'actual_slope_mass_M':M.js(),
        'all_primitive_normals_and_top_weights':primitive_normals,
        'rays':rays,'function_values':[v.js() for v in values],
        'first_weights':[d.js() for d in first], 'first_balance':[v.js() for v in bal],
        'graph_axis_second_contribution':graph_sum.js(), 'transverse_axis_second_contribution':transverse_sum.js(),
        'complete_mass':expected.js(),'predicted_complete_integral':(-expected).js(),
        'supported_PCC_coefficients':[str(a) for a in alpha],'PCC_barycentre_displacement':[str(a) for a in displacement],
        'all_assertions_passed':True,
        'scope':'Exact exhaustive arithmetic for this specified finite local fan. Global envelope equality and the complete-integral interpretation require the mathematical proof, not this program.'}

data=json.loads(Path('higher-relation-input.json').read_text())
out={'field':'Q(sqrt(2)), exact rational-pair arithmetic','inputs':[run(x) for x in data],
     'not_formal_verification':True}
Path('higher-relation-output.json').write_text(json.dumps(out,indent=2)+'\n')
for x in out['inputs']:
    print(json.dumps({k:x[k] for k in ['name','relation_cone_rank','whole_star_ray_span_index','complete_mass','graph_axis_second_contribution','transverse_axis_second_contribution','all_assertions_passed']}))
