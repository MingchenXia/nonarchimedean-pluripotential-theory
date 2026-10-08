"""Fresh, bounded Fraction arithmetic checks. No historical emitter is executed."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json

cfg = json.loads(Path('inputs/exact-checks.json').read_text())
count = 0

def check(condition):
    global count
    count += 1
    assert condition

def huber(t):
    t = F(t)
    return t*t/2 if abs(t) <= 1 else abs(t)-F(1,2)

def knots(n, offset):
    return sorted(set([F(-1)+F(j,2**n) for j in range(2**(n+1)+1)] + [-offset]))

def interp(t, ks):
    if t <= -1 or t >= 1:
        return huber(t)
    for a,b in zip(ks,ks[1:]):
        if a <= t <= b:
            return (a+b)*t/2-a*b/2
    raise AssertionError('missing interpolation cell')

grid = [F(x) for x in cfg['grid']]
report = {'kind':'exact finite checks plus explicitly stated algebraic identities', 'mesh':[], 'assertions':None}
for n in cfg['mesh_levels']:
    branch_reports=[]
    for branch in cfg['branches']:
        scales = list(map(F, branch['scales']))
        offsets = list(map(F, branch['offsets']))
        ks = [knots(n,o) for o in offsets]
        bounds=[]
        for scale,off,k in zip(scales,offsets,ks):
            slopes=[]
            max_error=F(0)
            for a,b in zip(k,k[1:]):
                # Exact coefficient identity: chord(t)-t^2/2=(t-a)(b-t)/2.
                chord_slope=(huber(b)-huber(a))/(b-a)
                chord_intercept=huber(a)-chord_slope*a
                left_coeff=[F(-1,2),chord_slope,chord_intercept]
                right_coeff=[F(-1,2),(a+b)/2,-a*b/2]
                check(left_coeff == right_coeff)
                check(interp(a,k)==huber(a) and interp(b,k)==huber(b))
                midpoint=(a+b)/2
                err=interp(midpoint,k)-huber(midpoint)
                check(err==(b-a)**2/8)
                max_error=max(max_error,err)
                slopes.append((a+b)/2)
            check(all(a<=b for a,b in zip([F(-1)]+slopes,slopes+[F(1)])))
            check(interp(-off,k)==huber(-off))
            check(interp(F(-3),k)==huber(F(-3)) and interp(F(3),k)==huber(F(3)))
            bounds.append(scale*max_error)
        bound=sum(bounds,F(0))
        check(bound <= F(1,2**n))
        def functions(x,y):
            coords=[F(row[0])*x+F(row[1])*y for row in branch['matrix']]
            base=sum((s*huber(t-o)-s*huber(-o) for s,t,o in zip(scales,coords,offsets)),F(0))
            approx=sum((s*interp(t-o,k)-s*huber(-o) for s,t,o,k in zip(scales,coords,offsets,ks)),F(0))
            return base,approx
        check(functions(F(0),F(0))==(F(0),F(0)))
        for x,y in product(grid,repeat=2):
            f,fn=functions(x,y)
            check(F(0)<=fn-f<=bound)
            if n < max(cfg['mesh_levels']):
                ksnext=[knots(n+1,o) for o in offsets]
                coords=[F(row[0])*x+F(row[1])*y for row in branch['matrix']]
                fnnext=sum((s*interp(t-o,k)-s*huber(-o) for s,t,o,k in zip(scales,coords,offsets,ksnext)),F(0))
                check(fn+F(4,2**n) >= fnnext+F(4,2**(n+1)))
        branch_reports.append({'global_error_bound_from_quadratic_identity':str(bound),
                               'exact_origin':'0','shifted_origin':str(F(4,2**n)),
                               'tail_slopes':list(map(str,scales)),
                               'rational_knots':[list(map(str,k)) for k in ks]})
    report['mesh'].append({'n':n,'branches':branch_reports})

# A mixed difference shows the first example depends jointly on its coordinates.
a=F(1,4)
def example(x,y): return huber(x+y)+huber(y)
mixed=example(a,a)-example(a,0)-example(0,a)+example(0,0)
check(mixed==F(1,16))
report['nonseparable_example_mixed_difference']=str(mixed)

# Literal obstacle on the line. All recorded evaluations use exact rationals.
def gamma(t):return abs(t)
def obstacle(t):return min(F(1,2),max(F(0),1-abs(t)))
def envelope(t):return max(abs(t),(abs(t)+1)/2)
for t in grid:
    check(envelope(t)<=gamma(t)+obstacle(t))
for t in [F(-1),F(0),F(1)]:
    check(envelope(t)==gamma(t)+obstacle(t))
q=F(cfg['literal_obstruction_slope']); length=F(cfg['literal_obstruction_segment_length'])
dist=min(q-q.numerator//q.denominator,1-(q-q.numerator//q.denominator))
report['literal_uniform_error_floor']=str(length*dist/4)
check(report['literal_uniform_error_floor']=='1/8')

# Compact chart example: (R/Z)^2 with a literal periodic tent obstacle.
c=F(cfg['compact_torus_offset'])
def tent(t):return min(t,1-t)
vertex_values=[c+tent(x)+2*tent(y) for x,y in product([F(0),F(1,2),F(1)],repeat=2)]
check(min(vertex_values)==c)
report['compact_torus_component_minimum']=str(c)
report['assertions']=count
report['limitations']=[
 'The grid assertions are exhaustive only for the explicitly listed finite examples.',
 'The global error bounds use the stated quadratic coefficient identity and exact linear tails.',
 'No arbitrary real coefficient, singular star, PC classification or mathematical proof audit is performed.',
 'No Monge-Ampere operator is assigned in this check.'
]
Path('evidence/exact-checks-output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'passed','assertions':count,'mesh_levels':cfg['mesh_levels'],
                  'mixed_difference':str(mixed),'literal_error_floor':'1/8','compact_minimum':str(c)},indent=2))
