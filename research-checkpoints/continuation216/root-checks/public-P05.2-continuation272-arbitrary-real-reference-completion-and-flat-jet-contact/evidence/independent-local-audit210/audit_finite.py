"""Independent small exact checks; does not reproduce an unavailable author grid.

Run: python audit_finite.py
Uses only Python's standard library. All certificate data below are explicit.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd
import json
from pathlib import Path

class E:
    """Exact Q(sqrt(2),sqrt(3)) in basis 1,A,B,AB."""
    def __init__(self, *v):
        self.v=tuple(map(Q, v or (0,)))+(Q(0),)*(4-len(v or (0,)))
    def __add__(self,o):
        o=conv(o); return E(*(a+b for a,b in zip(self.v,o.v)))
    __radd__=__add__
    def __neg__(self): return E(*(-a for a in self.v))
    def __sub__(self,o): return self+-conv(o)
    def __rsub__(self,o): return conv(o)+-self
    def __mul__(self,o):
        o=conv(o); v=[Q(0)]*4
        for i,a in enumerate(self.v):
            for j,b in enumerate(o.v):
                v[i^j]+=a*b*(2 if i&j&1 else 1)*(3 if i&j&2 else 1)
        return E(*v)
    __rmul__=__mul__
    def __eq__(self,o): return self.v==conv(o).v
    def out(self): return list(map(str,self.v))
    def bounds(self):
        aa=(Q(1414213,1000000),Q(1414214,1000000))
        bb=(Q(1732050,1000000),Q(1732051,1000000))
        assert aa[0]**2<2<aa[1]**2 and bb[0]**2<3<bb[1]**2
        bases=[(Q(1),Q(1)),aa,bb,(aa[0]*bb[0],aa[1]*bb[1])]
        lo=hi=Q(0)
        for c,(l,h) in zip(self.v,bases):
            lo+=c*(l if c>=0 else h); hi+=c*(h if c>=0 else l)
        return lo,hi
    def positive(self): return self.bounds()[0]>0

def conv(o): return o if isinstance(o,E) else E(o)
A=E(0,1); B=E(0,0,1)
def dot(u,v): return sum(a*b for a,b in zip(u,v))
def add(u,v): return tuple(a+b for a,b in zip(u,v))
def neg(u): return tuple(-a for a in u)
def balance(ds,ws):
    return [sum(conv(w)*d[k] for d,w in zip(ds,ws)) for k in range(len(ds[0]))]

def positive_kernel(ds):
    """Return primitive positive integer generator iff supported kernel has rank 1."""
    n=len(ds)
    mat=[[Q(d[k]) for d in ds] for k in range(len(ds[0]))]
    piv=[]; row=0
    for col in range(n):
        found=next((r for r in range(row,len(mat)) if mat[r][col]),None)
        if found is None: continue
        mat[row],mat[found]=mat[found],mat[row]
        x=mat[row][col]; mat[row]=[a/x for a in mat[row]]
        for r in range(len(mat)):
            if r!=row:
                x=mat[r][col]; mat[r]=[a-x*b for a,b in zip(mat[r],mat[row])]
        piv.append(col); row+=1
        if row==len(mat): break
    free=[j for j in range(n) if j not in piv]
    if len(free)!=1: return None
    vec=[Q(0)]*n; vec[free[0]]=1
    for r,p in enumerate(piv): vec[p]=-mat[r][free[0]]
    if all(x<0 for x in vec): vec=[-x for x in vec]
    if not all(x>0 for x in vec): return None
    den=1
    for x in vec: den=den*x.denominator//gcd(den,x.denominator)
    ints=[int(x*den) for x in vec]; g=0
    for x in ints:g=gcd(g,x)
    return [x//g for x in ints]

def circuits(ds,ss):
    rows=[]; examined=0
    for size in range(1,min(4,len(ds))+1):
        for inds in combinations(range(len(ds)),size):
            examined+=1; lam=positive_kernel([ds[i] for i in inds])
            if lam is not None:
                cost=dot(lam,[ss[i] for i in inds]); assert cost>=0
                rows.append(dict(support=list(inds),relation=lam,cost=str(cost)))
    return dict(supports_examined=examined,circuits=rows)

def plane():
    ref=2*(2*B)*A+2*(2*A)*B
    assert ref==8*A*B
    cuts=[]
    for j in [1,2,3,8]:
        ds=[(-1,0),(1,0),(-1,1),(-1,-1)]
        ws=[2*(B-1),2*B,1,1]
        slopes=[-(A-1),A,B-A,B-A]
        assert all(z==0 for z in balance(ds,ws))
        origin=8*(A-1)*(B-1)
        xatom=sum(w*s for w,s in zip(ws,slopes))
        yatom=-2*(A-1)*(B-1)+2*A*B+2*(A-B)
        ydirs=[(0,-1),(0,1),(1,-1),(-1,-1)]
        yweights=[2*(A-1),2*A,1,1]
        yslopes=[-(B-1),B,A-B,A-B]
        assert all(z==0 for z in balance(ydirs,yweights))
        assert yatom==sum(w*s for w,s in zip(yweights,yslopes))
        cdirs=[(1,0),(-1,0),(0,1),(0,-1)]
        cweights=[2*(B-1)]*2+[2*(A-1)]*2
        assert all(z==0 for z in balance(cdirs,cweights))
        assert origin==sum(w*s for w,s in zip(cweights,[A-1,A-1,B-1,B-1]))
        assert xatom==4*B-2 and yatom==4*A-2
        total=origin+2*xatom+2*yatom; assert total==ref
        height=j*(2*xatom+2*yatom); bound=32*j*A*B
        assert height==8*j*(A+B-1) and (bound-height).positive()
        assert origin.positive() and xatom.positive() and yatom.positive()
        cuts.append(dict(j=j,origin=origin.out(),each_horizontal=xatom.out(),
                         each_vertical=yatom.out(),total=total.out(),
                         height=height.out(),bound=bound.out(),
                         horizontal_first_balance=[z.out() for z in balance(ds,ws)],
                         vertical_first_balance=[z.out() for z in balance(ydirs,yweights)],
                         central_first_balance=[z.out() for z in balance(cdirs,cweights)]))
    vertices=[(1,1),(2,1),(1,3)]
    weights=[E(Q(5,2))-A-Q(1,2)*B,A-1,Q(1,2)*(B-1)]
    assert sum(weights)==1 and all(w.positive() for w in weights)
    assert sum(w*v[0] for w,v in zip(weights,vertices))==A
    assert sum(w*v[1] for w,v in zip(weights,vertices))==B
    return dict(reference_mass=ref.out(),cutoffs=cuts,simplex_vertices=vertices,
                simplex_weights=[w.out() for w in weights])

def u34():
    es=[(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)]
    ps=list(combinations(range(4),2)); pair=[add(es[i],es[j]) for i,j in ps]
    bs=[0 if p in [(0,1),(2,3)] else 1 for p in ps]
    ds=es+pair; ss=[1]*4+bs
    origin=circuits(ds,ss)
    origin['h_circuits']=circuits(ds,[1]*10)['circuits']
    assert origin['supports_examined']==385 and len(origin['circuits'])==14
    assert sum(r['cost']=='0' for r in origin['circuits'])==1
    cases=[]; cones=[]
    for i,e in enumerate(es):
        transverse=[j for j in range(4) if j!=i]
        vals=[1,-1]+[bs[ps.index(tuple(sorted((i,j))))]-1 for j in transverse]
        cur=circuits([e,neg(e)]+[es[j] for j in transverse],vals)
        cur['h_circuits']=circuits([e,neg(e)]+[es[j] for j in transverse],[1,-1,0,0,0])['circuits']
        assert add(tuple(sum(es[j][k] for j in transverse) for k in range(3)),e)==(0,0,0)
        assert len(cur['circuits'])==2 and cur['supports_examined']==30
        cases.append(dict(face=f'singleton{i+1}',directions=[e,neg(e)]+[es[j] for j in transverse],slopes=vals,**cur))
    for k,(i,j) in enumerate(ps):
        e=pair[k]; vals=[bs[k],-bs[k],1,1]
        cur=circuits([e,neg(e),es[i],es[j]],vals)
        cur['h_circuits']=circuits([e,neg(e),es[i],es[j]],[1,-1,1,1])['circuits']
        assert add(es[i],es[j])==e
        assert len(cur['circuits'])==2 and cur['supports_examined']==15
        cases.append(dict(face=f'pair{i+1}{j+1}',directions=[e,neg(e),es[i],es[j]],slopes=vals,**cur))
        for q in [i,j]:
            d=es[q]; minors=[d[a]*e[b]-d[b]*e[a] for a,b in combinations(range(3),2)]
            g=0
            for x in minors:g=gcd(g,abs(x))
            assert g==1
            cones.append(dict(singleton=q+1,pair=[i+1,j+1],minors=minors,saturation_index=g))
            vals=[1,-1,bs[k],-bs[k]]
            cur=circuits([d,neg(d),e,neg(e)],vals)
            cur['h_circuits']=circuits([d,neg(d),e,neg(e)],[1,-1,1,-1])['circuits']
            assert len(cur['circuits'])==2 and cur['supports_examined']==15
            cases.append(dict(face=f'top{q+1}-{i+1}{j+1}',directions=[d,neg(d),e,neg(e)],slopes=vals,**cur))
    singles=[sum(bs[k] for k,p in enumerate(ps) if i in p)-2 for i in range(4)]
    pairs=[2-b for b in bs]
    assert singles==[0]*4 and all(z==0 for z in balance(ds,singles+pairs))
    raw=dot(singles+pairs,ss); assert raw==4
    weights=[2-Q(1,2)*A-Q(1,2)*B,Q(1,2)*(A-1),Q(1,2)*(B-1)]
    vertices=[(1,1),(3,1),(1,3)]
    assert sum(weights)==1 and all(w.positive() for w in weights)
    assert sum(w*v[0] for w,v in zip(weights,vertices))==A
    assert sum(w*v[1] for w,v in zip(weights,vertices))==B
    alpha,r,t,delta=Q(1,16),Q(1,4),Q(1,512),Q(1,64)
    assert delta*2<=alpha/2 and t<alpha*r/4
    collar_margin=alpha*r/4-t
    assert collar_margin>0 and raw*delta**2==Q(1,1024)
    active=[]
    for case in [origin]+cases:
        for circuit in case['circuits']:
            cost=Q(circuit['cost'])
            gamma_cost=(A+B)*cost; gamma0_cost=2*cost
            assert (gamma_cost==0)==(gamma0_cost==0)
            if cost:assert gamma_cost.positive()
            active.append(dict(cost_eta=str(cost),cost_gamma=gamma_cost.out(),cost_gamma0=str(gamma0_cost),
                               exactly_active=cost==0))
    return dict(origin=origin,face_cases=cases,saturated_cones=cones,
                first_weights=dict(singletons=singles,pairs=pairs),raw_eta_atom=raw,
                simplex_vertices=vertices,simplex_weights=[w.out() for w in weights],
                parameters=dict(alpha=str(alpha),r=str(r),t=str(t),delta=str(delta)),
                continuum_collar_lower_margin=str(collar_margin),scaled_atom=str(raw*delta**2),
                germ_active_cost_comparison=active,
                historical_291_point_list_available=False)

def main():
    result=dict(status='PASS: independent exact finite algebra',arithmetic='Fraction and Q(sqrt2,sqrt3)',
                plane=plane(),U34=u34(),
                limitations='No author checker/input or 291-point list is supplied. No finite test proves continuum envelopes or all-refinement classification.')
    Path('audit-finite-output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],plane_levels=4,origin_supports=385,
                         origin_circuits=14,zero_cost_circuits=1,other_faces=22,
                         saturated_cones=12,raw_eta_atom=4,scaled_atom='1/1024')))

if __name__=='__main__': main()
