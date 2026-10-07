from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from itertools import combinations,product
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
P=K/'P05.2-continuation249-PC-hypothesis-repair-and-coupled-plane-counterexample-working-proof-20261007.json'
assert not P.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def hull(points):
    points=sorted(set(points))
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[];hi=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1] if len(points)>1 else points
def shoelace(points):
    h=hull(points)
    return abs(sum(h[i][0]*h[(i+1)%len(h)][1]-h[i][1]*h[(i+1)%len(h)][0] for i in range(len(h)))) if h else F(0)
def vertices(branches):
    out={}
    for a,b,c in combinations(branches,3):
        u=(b[0]-a[0],b[1]-a[1]);v=(c[0]-a[0],c[1]-a[1]);det=u[0]*v[1]-u[1]*v[0]
        if not det:continue
        d=a[2]-b[2];e=a[2]-c[2];p=(F(d*v[1]-u[1]*e,det),F(u[0]*e-d*v[0],det))
        vals=[F(q[0])*p[0]+F(q[1])*p[1]+F(q[2]) for q in branches];m=max(vals)
        active=[(F(q[0]),F(q[1])) for q,t in zip(branches,vals) if t==m]
        mass=shoelace(active)
        if mass:out[p]=mass
    return out
def value(y,z,shift):return max(abs(y)-shift,abs(z))+abs(z)
branches0=[(s,t,0) for s,t in product((-1,1),repeat=2)]+[(0,2,0),(0,-2,0),(0,0,0)]
branches1=[(s,t,-1) for s,t in product((-1,1),repeat=2)]+[(0,2,0),(0,-2,0),(0,0,0)]
xz=vertices(branches0);yz=vertices(branches1)
assert xz=={(F(0),F(0)):F(12)} and yz=={(F(-1),F(0)):F(6),(F(1),F(0)):F(6)}
rays_xz=[((1,0),2,1),((-1,0),2,1)]+[((s,t),1,2) for s,t in product((-1,1),repeat=2)]
rays_yplus=[((-1,0),4,0),((1,0),2,1),((1,1),1,2),((1,-1),1,2)]
rays_yminus=[((1,0),4,0),((-1,0),2,1),((-1,1),1,2),((-1,-1),1,2)]
for rays,m in [(rays_xz,12),(rays_yplus,6),(rays_yminus,6)]:
    assert tuple(sum(w*v[j] for v,w,s in rays) for j in (0,1))==(0,0)
    assert sum(w*s for v,w,s in rays)==m
rho=F(1,4);corners=[value(y,z,0) for y,z in [(0,0),(rho,0),(0,rho),(rho,rho)]]
assert corners[0]+corners[3]-corners[1]-corners[2]==-rho
checks=dict(all_assertions_passed=True,exhaustive_active_affine_triples=True,xz_f_positive_vertices=[dict(point=[str(q) for q in p],twice_newton_polygon_area=str(m)) for p,m in sorted(xz.items())],yz_f_positive_vertices=[dict(point=[str(q) for q in p],twice_newton_polygon_area=str(m)) for p,m in sorted(yz.items())],independent_primitive_first_cycle_balance_and_second_mass_checks=[12,6,6],reference_plane_masses=[12,12],reference_total_raw_mass=24,endpoint_total_raw_mass=24,roof_radius=str(rho),raw_contact_integral=str(-rho*12),endpoint_product_mixed_difference=str(-rho),finite_algebraic_checks_only=True,polygon_area_used_only_as_independent_finite_crosscheck=True,operator_proof_requires_complete_first_cycle_and_recursive_raw_definition=True)
steps=[
dict(id='R1',text=r"""The WHOLE196 verdict on unchanged247 is FAIL. Preserve it, both native/canonical outputs and every original source byte. Lemma3 must explicitly assume a PA PC germ, equivalently nonnegative costs on every positive tangent relation. For general relative PA it is false: on the balanced real line f=-|x| for |x|<=1 and f=|x|-2 outside, gamma=|x|. At zero the relation cone is {(a,a):a>=0}, every nonzero cost is -2a, hence no zero-cost relation, but no strict affine floor exists. Under PC, costs are nonnegative, and absence of zero cost makes the compact normalized-relation minimum strictly positive; then the existing separation proof works. Adding PC is an explicit MATERIAL hypothesis correction, not a harmless typo."""),
dict(id='R2',text=r"""The old f=max(|x|,|y|-1,0)+|z| on X=({y=0} union {x=0}) is separable on the product of the two-axis cross with the z-line. Only the old roof obstacle was nonseparable. ROOT's prior description of f as nonseparable was incorrect. Replace the example and reference together: gamma=max(|x|,|y|,|z|)+|z| and f=max(|x|,|y|-1,|z|)+|z|. They are actual ambient convex integral PA restrictions to the same balanced X. All affine slopes are integral, constants are rational, and their finitely many carrying hyperplanes are rational. Every printed rational-endpoint PCC inequality follows by the actual ambient convex function; no completion theorem is needed for these endpoints. Pointwise -1<=f-gamma<=0, by the 1-Lipschitz maximum under shifting only the |y| term. Thus actual relative growth is bounded. Gamma is positively homogeneous and positive in every nonzero recession direction of X."""),
dict(id='R3',text=r"""This f is genuinely nonseparable on the original product cross times z: on the horizontal xz-plane, f(x,0,z)=max(|x|,|z|)+|z|. At (x,z)=(0,0),(R,0),(0,R),(R,R) its values are0,R,2R,2R. The mixed difference is -R!=0. Hence there are no functions F on the cross and H on the z-line with f(q,z)=F(q)+H(z). The same test proves gamma nonseparable. This is the precise product decomposition at issue; no claim of excluding every arbitrarily reparametrized affine product decomposition is made."""),
dict(id='R4',text=r"""The actual unit-weight balanced carrying cycle is [P_xz]+[P_yz], each coordinate plane with its saturated lattice Z^2 in Z^3. Refine both planes by their rational piecewise-affine walls and the shared z-axis; all top cells keep weight1 and all normal classes are primitive in the saturated quotient lattice. Linearity of the raw divisor in the carrying cycle gives D_f^2[X]=D_f^2[P_xz]+D_f^2[P_yz]. This is actual additivity on a SUM of carrying planes, not a normalization or a determinant asserted for an abstract local jet. Along a straight wall where f has two affine gradients m1,m2 agreeing tangentially, take an integral primitive transverse lift n1 with det(tangent,n1)=+/-1, opposite lift n2=-n1. The raw tangent correction cancels and the first weight is (m1-m2)(n1). Explicit gradients give the following cycles."""),
dict(id='R5',text=r"""On P_xz, f=gamma=h=max(|x|,|z|)+|z|. Its first divisor has the two x-axis rays with weight2 and the four diagonal rays (s,0,t), s,t in{+/-1}, with weight1. The z-axis has weight0: the gradients on its two sides coincide where z!=0. The coordinate ray primitive directions are (s,0,0), on which h has slope1. On each diagonal primitive direction h has slope2. At origin the first cycle balances: the two opposite x directions cancel and the four diagonal directions cancel. The second raw weight is 2*1+2*1+4*(1*2)=12. There are no other first-cycle vertices on this plane and no other second atoms. These integer normal weights can be checked, e.g. at a diagonal tangent(1,1), with primitive transverse lift(1,0): adjacent gradient difference(1,-1) evaluates to1."""),
dict(id='R6',text=r"""On P_yz, write g(y,z)=max(|y|-1,|z|)+|z|. Its first divisor has the central segment {z=0,-1<=y<=1} of weight4, the two outward y-axis rays starting at p+=(0,1,0), p-=(0,-1,0) of weight2, and four diagonal rays starting at p_epsilon in directions(0,epsilon,+/-1), each weight1. It has no nonzero z-axis weight and no vertical line over y=+/-1. Indeed in the central region |y|<=1+|z| the function is2|z|; outside, it is|y|-1+|z|. At p+, inward central direction -e_y has first weight4 and slope0, outward +e_y has weight2 and slope1, and the two diagonal directions have weight1 and slope2. Their balance is -4e_y+2e_y+(e_y+e_z)+(e_y-e_z)=0, and their second raw weight is0+2+2+2=6. The same calculation at p- gives6. If the central segment is subdivided at origin to meet P_xz, its two directions have opposite equal weights4 and local f slopes0, hence contribute zero second mass. All refinements of straight affine portions introduce zero atoms by the explicit opposite-direction cancellation."""),
dict(id='R7',text=r"""For gamma the same homogeneous h occurs on BOTH coordinate planes. Each has the R5 mass12 at origin; raw MA(gamma)=24 delta_0. For f, R5-R6 give RAW MA(f)=12 delta_0+6 delta_p++6 delta_p-. Their total masses both equal24. This identity is a check, not a proof by total mass or a field-degree normalization. At origin f has the genuine flat relation between the two small rational y-axis endpoints: f(0,+/-r,0)=0=f(0) for0<r<1. Nevertheless m_0(f)=12>0. This uses the actual globally realized f and gamma with bounded difference."""),
dict(id='R8',text=r"""Take R=1/4, rho(x)=max(|x|,|y|,|z|), B_R=(R-rho)_+, and u=f-gamma+B_R. This is a bounded actual literal integral-slope/rational-constant PA obstacle on a finite rational structure. The endpoint obstacle is gamma+u=f+B_R, and f is an allowed PC competitor. For EVERY printed-PC competitor q<=f+B_R with q<=gamma+O(1), the flat PCC at origin using endpoints(0,+/-R,0) forces q(0)<=f(0)=0 because B_R=0 at those endpoints. For any rational point x in the roof ball, let y=Rx/rho(x) on its radial boundary. In a sufficiently small rational carrying subdivision the segment [0,y] lies in an incident linearity cell of f; here explicitly f is homogeneous on each plane inside rho<1. Jensen with the actual rational center0/boundary endpoint y gives q(x)<=f(x). Outside the roof q<=f by obstacle. For an arbitrary real point choose shrinking rational simplices in its minimal rational face, whose vertices already satisfy q<=f. Printed PCC inequalities at the real center and continuity of f give the same bound. Thus the UNRESTRICTED actual envelope is exactly f, including every competitor that can differ from its continuous completion. Its usc regularization is f and its constant decreasing PA regularization is literal. The roof ball contains neither p+ nor p-, so the RAW contact integral is (f-(f+B_R))(0)*12=-R*12=-3. Additional carrying vertices for the obstacle contribute no artificial f mass by refinement invariance."""),
dict(id='R9',text=r"""On the xz-plane f-gamma=0. The roof obstacle u has values R,0,0,0 at the same four corners, with mixed difference R!=0, so it also is genuinely nonseparable. Both the endpoint and the obstacle now satisfy the claimed cross-times-z coupling. This is an explicit finite PA obstruction with actual admissible growth and exact raw operator. It does NOT prove pair regularity for EVERY obstacle, full original necessary/sufficient classification, general regularization of continuous envelopes, a fixed uniform refinement bound, or realization of every local convex jet."""),
dict(id='R10',text=r"""A new manuscript must state the PC hypothesis in Lemma3 and every downstream use, identify the old endpoint's separability as an actual correction, include the NEW gamma and f and ALL first/second cycles, and re-prove the radial envelope independently. The reader196 commentary that other arguments check out is not a whole PASS or a new caller grant. Exactly complete A224/B225/R230 with all clarifications remain mathematical grants. All new outputs should use only valid local note IDs in support fields; printed caller-source labels are data context, not registered kernel note IDs. Full original P05.2 remains open.""")]
j=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P05.2',continuation=249,status='Unreviewed explicit material hypothesis repair and new genuinely coupled endpoint working proof',mathematical_grant=False,new_accepted_paper=False,original_closed=False,whole196_failure_binding=str(K/'P05.2-round196-whole-finite-contact-FAIL-review-binding-20261007.json'),whole196_failure_binding_sha256=sha(K/'P05.2-round196-whole-finite-contact-FAIL-review-binding-20261007.json'),steps=steps,exact_finite_checks=checks,original247_preserved=True,no_private_active_output_read=True,no_hot_feedback=True,sent_to_active195=False,protected_editor_unchanged_open=True)
P.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(path=str(P),sha256=sha(P),bytes=P.stat().st_size,raw_masses=[12,6,6],reference_mass=24,raw_contact=-3,endpoint_mixed_difference=str(-rho),original_closed=False),indent=2))
