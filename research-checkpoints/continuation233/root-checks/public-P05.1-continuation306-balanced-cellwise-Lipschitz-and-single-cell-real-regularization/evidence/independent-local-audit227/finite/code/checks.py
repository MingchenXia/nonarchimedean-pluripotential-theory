#!/usr/bin/env python3
"""Small exact checks, explicitly not proofs of the continuum theorems."""
from fractions import Fraction as Q
import hashlib
import json
import pathlib

HERE=pathlib.Path(__file__).resolve().parent.parent

def r2_add(x,y):return (x[0]+y[0],x[1]+y[1])
def r2_mul(x,y):return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def r2_sign(x):
    """Exact sign in Q(sqrt(2)); no approximation to sqrt(2)."""
    a,b=x
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    difference=a*a-2*b*b
    sign=(difference>0)-(difference<0)
    return sign if a>0 else -sign

def main():
    data=(HERE/'inputs/check-input.json').read_bytes()
    inp=json.loads(data)
    out={'arithmetic':'fractions.Fraction; integers; no floating-point tolerances',
         'input_sha256':hashlib.sha256(data).hexdigest(),
         'status':'finite exact sanity checks, not independent mathematical acceptance',
         'checks':{}}
    # e1,e2,(-1,-1) are primitive balanced ray directions; a common
    # actual positive real weight, e.g. sqrt(2), multiplies their zero sum.
    generators=[(1,0),(0,1),(-1,-1)]
    assert tuple(sum(v[i] for v in generators) for i in [0,1])==(0,0)
    radius=inp['star_integer_radius'];count=0;max_cost2_ratio=Q(0)
    for x in range(-radius,radius+1):
        for y in range(-radius,radius+1):
            for sign in [1,-1]:
                xx,yy=sign*x,sign*y
                c=max(0,-xx,-yy);a=xx+c;b=yy+c
                assert min(a,b,c)>=0
                assert (a-c,b-c)==(xx,yy)
                cost=a+b+c;norm2=xx*xx+yy*yy
                assert cost*cost<=9*norm2
                if norm2:max_cost2_ratio=max(max_cost2_ratio,Q(cost*cost,norm2))
                count+=1
    out['checks']['positive_star']={'vectors':generators,'common_real_weight_example':'sqrt(2)',
        'both_direction_tests':count,'coefficient_bound_K':3,
        'largest_enumerated_cost_squared_over_norm_squared':str(max_cost2_ratio),
        'coverage':f'integer square [-{radius},{radius}]^2, both signs'}
    # Nearest point to the positive orthant: active outward normals are -e_i.
    radius=inp['distance_integer_radius'];count=0
    for x in range(-radius,radius+1):
        for y in range(-radius,radius+1):
            z=(max(x,0),max(y,0));w=(x-z[0],y-z[1])
            lambdas=(-w[0],-w[1]);norm2=w[0]**2+w[1]**2
            assert min(lambdas)>=0
            assert sum(lambdas)**2<=2*norm2
            violation=max(0,-x,-y)
            assert norm2<=2*violation**2
            assert norm2==lambdas[0]*(-x)+lambdas[1]*(-y)
            count+=1
    out['checks']['distance']={'tests':count,'H_squared':2,'example':'positive orthant; exact projection',
                                'note':'general active-normal lemma is proved in the paper'}
    delta=Q(inp['inset_margin']);rows=[]
    for p in inp['inset_points']:
        y=tuple(Q(t) for t in p);assert y[0]>=0
        z=(max(y[0],delta),y[1]);norm2=(z[0]-y[0])**2
        assert z[0]>=delta and norm2<=delta**2
        rows.append({'y':[str(t) for t in y],'z':[str(t) for t in z],'distance_squared':str(norm2)})
    out['checks']['uniform_inset']={'face':'[0,infinity) x R','margin':str(delta),
                                   'D_squared':str(delta**2),'points':rows}
    # Saturated facet lattice <(1,1)> in Z^2, lift (1,0): determinant -1.
    u=(1,1);lift=(1,0);det=u[0]*lift[1]-u[1]*lift[0]
    projected_length2=Q(sum(t*t for t in lift))-Q(sum(u[i]*lift[i] for i in [0,1])**2,sum(t*t for t in u))
    ratio2=Q(det*det,sum(t*t for t in u))
    assert abs(det)==1 and projected_length2==ratio2==Q(1,2)
    out['checks']['saturated_covolume']={'facet_basis':u,'primitive_lift':lift,'basis_determinant':det,
        'projected_length_squared':str(projected_length2),'cell_over_facet_covolume_squared':str(ratio2)}
    rows=[]
    for n in inp['dyadic_n']:
        eta=Q(1,2**n);gap=4*eta-5*eta/2
        assert gap==Q(3,2)*eta and gap>0
        rows.append({'n':n,'eta':str(eta),'minimum_decrease':str(gap)})
    out['checks']['dyadic_shifts']={'error_interval':'[4 eta_n,5 eta_n]','rows':rows}
    # Exact primal construction from (-1,sqrt(2)),(1,sqrt(2)) plus epi |v|.
    # F=sqrt(1+x^2), P=sqrt(2)+max(0,|x|-1), eta=sqrt(2)-1.
    radius=inp['primal_grid_radius'];denom=inp['primal_grid_denominator']
    sample_x=[Q(i,denom) for i in range(-radius,radius+1)]+[Q(-1024),Q(1024)]
    count=0
    for x in sample_x:
        r=abs(x);P=(max(Q(0),r-1),Q(1));F_squared=1+x*x
        assert r2_sign(r2_add(r2_mul(P,P),(-F_squared,Q(0))))>=0
        assert r2_sign(P)>0
        P_minus_eta=(max(Q(0),r-1)+1,Q(0))
        assert F_squared>=P_minus_eta[0]**2
        if r==1:assert r2_mul(P,P)==(F_squared,Q(0))
        count+=1
    out['checks']['actual_real_primal_majorant']={
        'F':'sqrt(1+x^2)','reference':'|x|','primal_samples':'(-1,sqrt(2)), (1,sqrt(2))',
        'exact_recession_cone':'epi |v|','P':'sqrt(2)+max(0,|x|-1)',
        'global_analytic_error':'sqrt(2)-1','rational_walls':[-1,1],
        'exact_rational_sample_tests':count,'arithmetic':'Q(sqrt(2)) sign by squared rational comparisons',
        'scope':'finite sample verification; whole-real-line inequalities separately proved in paper'}
    rows=[];L=Q(inp['illustrative_PA_L'])
    for n in inp['orthant_n']:
        x=Q(n*n);y=Q(1,n*n)
        assert x*y==1
        floor=(1-L*y)/2
        rows.append({'n':n,'distance':str(y),'product_at_w':str(x*y),
                     'necessary_error_lower_bound_for_L_3':str(floor),
                     'function_difference':str(1-y)})
    out['checks']['orthant']={'rows':rows,'continuum_limit_error_floor':'1/2',
                              'warning':'finite list does not establish continuum limit; analytic proof does'}
    (HERE/'reports').mkdir(exist_ok=True)
    (HERE/'reports/exact-checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
