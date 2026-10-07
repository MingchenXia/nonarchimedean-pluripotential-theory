# P05.2: a strict-growth obstruction on the U(3,4) fan

Status: independently proved scoped obstruction; the original necessary-and-sufficient classification remains open in this submission. This argument uses no supplied mathematical assertion as a grant. The source supplies the definitions being tested. All geometric, convexity, envelope, and intersection calculations used here are reconstructed below.

## Conventions and exact scope

Let N=Z^3, e1=(1,0,0), e2=(0,1,0), e3=(0,0,1), e4=(-1,-1,-1), and eij=ei+ej. Set X=union_{i<j} sigma_ij, where sigma_ij=R_{≥0}ei+R_{≥0}ej. The fine fan Sigma subdivides each sigma_ij at eij. All twelve two-dimensional cones have weight one. Tangent lattices are saturated: N_sigma=N intersect span_R(sigma). Primitive normals point into the adjacent face. For a piecewise affine f and a balanced k-cycle c, the raw divisor coefficient at a (k-1)-face tau is

    (f.c)(tau) = sum_{sigma>tau} c(sigma) f_sigma(n_sigma/tau)
                 - f_tau(sum_{sigma>tau} c(sigma)n_sigma/tau).

MA_poly(f) is f.(f.[X]) in dimension two, with no further factorial inserted. The Alexandrov convention is ordinary lattice-normalized subgradient area; on a weight-one complete two-dimensional affine germ the raw intersection mass is twice that area. This equality will be checked directly for our atoms.

PA_Z means integral linear parts and rational constants on a finite rational subdivision. PA_R means arbitrary real affine coefficients on a finite rational subdivision. PC means the polyhedral Jensen inequalities: x=sum alpha_i x_i, sum alpha_i=1, alpha_i>=0, with x in a face tau and each x_i in a face sigma_i containing tau, on some rational structure. Our proof works with rational endpoints as printed in BMPS v1, and hence also with all endpoints for the continuous functions constructed here. PAPC in each category is PA intersect PC. PC_reg in that category consists of uniform decreasing PAPC limits with bounded difference from the reference. The envelope is the supremum of all PC competitors q<=Gamma+U, q<=Gamma+O(1); it is not restricted to integral-slope competitors.

Only finite PA envelopes receive an MA measure in the main theorem. Their membership in the appropriate PC_reg follows from the constant approximating sequence. We do not need, or assert, regularity for every obstacle on this fan. BMPS Definition 6.9 assumes pair-level regularity; consequently the conclusion is exclusion from simultaneous regularity and universal orthogonality, together with an actual failure of contact at a demonstrably regularizable endpoint. A separate explicit obstacle below proves literal pair-level regularity fails for the simplest reference.

Strict convexity is relative to the fine fan Sigma, in the local-support sense: at every proper face there is an affine support equal on that face and strictly smaller nearby off it. This implies strict Jensen inequalities for active (positive-coefficient) nontrivial PCCs on Sigma. Zero-coefficient terms are discarded before testing strictness; the weak PC definition is unchanged. This convention makes explicit a degeneracy in the wording of source Definition 3.8, which allows zero coefficients in Definition 3.2. Under a reading that counts zero-coefficient endpoints, no strict function could satisfy the printed condition. Our local strict supports and positive divisor tests do not depend on that wording.

## Geometry, balancing, and lattices

Any three of e1,e2,e3,e4 form a Z-basis of N. In particular (ei,ej) and (ei,eij) generate the full saturated two-dimensional tangent lattice. At a singleton ray ei, use the inward normals ej for the three adjacent fine cones (ei,eij). Their sum is -ei, hence zero modulo Zei. At a pair ray eij, use inward normals ei and ej; their sum is eij, hence zero modulo Zeij. This proves balancing of the weight-one fan.

Identify N with Z^4/Z(1,1,1,1). The images of the four standard vectors are the ei. A point of X has a representative with two coordinates possibly positive and two zero; equivalently its smallest coordinate is attained at least twice. The uniform rank-three matroid on four elements has exactly one circuit, the full ground set. Thus the minimum-attained-twice circuit definition gives this support. Its nonempty proper flats have sizes one and two, and their inclusion chains give precisely the twelve fine cones. This establishes the U(3,4) Bergman description without using a matroid realization theorem. All its cones are unimodular in their saturated tangent lattices. At ei the transverse fan has three primitive directions with their unique positive relation; at eij the support is a two-dimensional affine plane locally; at zero it is this Bergman fan. These are the concrete matroidal and lattice properties meant here. We do not identify them with an unspecified stronger future smoothness condition.

## Elementary local-support lemma

Suppose f is continuous on X and every z has an ambient affine local support L_z, equal to f at z and <=f near z. Then f is convex on every line segment contained in X. To prove this, subtract the chord on such a segment. If the result has a positive maximum, its maximum set is a nonempty closed subset of the open segment. At any maximum point the slope of a local affine support must be zero (use both directions); the support inequality then makes the maximum set open. Connectedness contradicts zero endpoint values. This proves convexity.

For a PCC centered at x, each [x,x_i] lies in its face sigma_i and hence in X. Convexity along that segment propagates the local supporting slope at x to its endpoint: f(x_i)>=f(x)+dL_x(x_i-x). Summing with the alpha_i proves PC. If a support equals f along a face tau, then for any nonnegative balanced cycle c the divisor formula gives

    (f.c)(tau)=sum c(sigma)(f_sigma-dL_x)(n_sigma/tau)>=0.

The correction term disappears because balancing makes sum c n tangent to tau and f_tau=dL_x there. Each remaining term is nonnegative by the inward support inequality. This proves the source's intersection-positive PAPC condition for the functions we construct, without invoking its equivalence theorem. Independence of normal lifts is the same cancellation: changing an inward normal by a tangent vector changes the two terms equally.

For our two-dimensional complexes, refinement causes no new intersection mass: an added edge inside an affine cell has cancelling opposite normal contributions; along an existing bent edge its old coefficient is retained; an inserted vertex on an affine edge of the resulting one-cycle has cancelling endpoint slopes. Old vertex sums are preserved. This also establishes that the raw calculations below define the same MA on common refinements.

## Functions and theorem

Write x=a ei+b ej in sigma_ij, a,b>=0, and let E={{1,2},{3,4}} be the exceptional pairs. Define

    h(x)=max(a,b) on every sigma_ij,
    eta(x)=|a-b| if {i,j} is in E, and max(a,b) otherwise,
    u_epsilon(x)=(epsilon-min(a,b))_+ if {i,j} is in E,
                 epsilon otherwise.

Here epsilon is a positive rational number. These definitions agree on common singleton rays and at zero, so the functions are continuous. The bounded roof satisfies 0<=u_epsilon<=epsilon and is literal PA: its slopes are integral and its sole new threshold is rational. The functions h and eta are also literal PA on Sigma. On R^4/R(1,1,1,1), h is the ambient convex norm max_i z_i-min_i z_i, restricted to X. It is positive in every nonzero direction.

Theorem. Let A>=0, B>0 and C>B be real numbers, S=A+B, Gamma=A eta+B h, and U=C u_epsilon. In the explicit real scalar category,

    P_Gamma(U)=P=Gamma+B u_epsilon,
    MA_poly,R(P)=4 S^2 delta_0+B(4A+3B)(delta_{epsilon e12}+delta_{epsilon e34}),
    integral_X (P-(Gamma+U)) MA_poly,R(P)=-4(C-B)epsilon S^2<0.

The reference is strictly convex relative to Sigma and positive at infinity. Both reference and endpoint are PC and finite real PA on rational structures; P-Gamma is bounded. If A,B,C are integers, the same construction is entirely in the literal integral-slope/rational-constant category, and its endpoint belongs to PC_reg,Z. The mass formula in this case is exactly the literal source intersection operator, not a replacement operator. More generally, real coefficients use only the real-linear extension of that identical finite divisor formula, not a claimed extension to every non-PA PC function.

## Convexity and strictness proof

On each coarse cone, h and eta are convex. At a point r ei, r>0, let j be its exceptional partner and k,l the other two indices. The germ of eta is ambient affine, with linear values (1,-1,0,0) on (ei,ej,ek,el); these values sum to zero, so they define an ambient linear form. At zero eta>=0 gives the zero support. At each pair ray the surrounding support lies in its coarse two-dimensional plane, where the displayed convex formulas give supporting affine forms. Interior points have the usual affine support. Thus the local-support lemma proves eta is PC. The same conclusion for h also follows directly from its ambient norm formula.

Near r ei, Gamma has longitudinal slope S and transverse slopes -A,0,0 in directions ej,ek,el. The ambient form with values

    S, -A-B/3, -B/3, -B/3

supports Gamma and has strictly positive transverse slack B/3 in each adjacent cone. At an exceptional pair ray the two conewise gradients differ by a convex bend 2A+B>0; at every other pair ray the bend is S>0. Their average supplies a strict support equal on the ray. At zero, the zero support is strict since Gamma>=B h>0 off zero. These supports prove strictness on every proper face. Strict local slack propagates along each incident face by convexity, so the active strict Jensen version follows too. Positivity at infinity holds because each nonzero recession direction lies in a cone where Gamma>=B h>0, with Gamma conical and linear on fine faces.

For P, on an exceptional coarse cone,

    P=max{Gamma, B epsilon+S|a-b|};

on the other four coarse cones P=Gamma+B epsilon=B epsilon+S max(a,b). Therefore it is convex on every coarse cone. Near r ei it is ambient affine across all three adjacent cones: the longitudinal slope is S, the exceptional transverse slope -S, and the other two slopes zero. At zero its germ is B epsilon+S eta, with the constant B epsilon as support. Every other point is either inside a coarse cone or on one of its pair rays, where the surrounding support lies in a single plane and convexity gives a support. The local-support lemma proves P is PC and intersection-positive. The finite rational structure can be read explicitly: in each exceptional ordered half-cone a>=b, split at b=epsilon; its two cells have vertices zero and epsilon eij and recession generators ei and eij as appropriate. Interchange a,b for the other half-cone. On other cones use Sigma. There are sixteen top cells and exactly three vertices. All formula coefficients are integral when A,B are integers. Finally P<=Gamma+U because C>B and u_epsilon>=0, and P-Gamma=B u_epsilon is bounded. Hence P is an envelope competitor and a valid PA/regularizable endpoint.

## Envelope upper bound for every PC competitor

Let q be any competitor. The two rational points +epsilon e12 and -epsilon e12=epsilon e34 both have obstacle value B epsilon. Their midpoint combination gives q(0)<=B epsilon. On any singleton ray q(r ei)<=S r+C epsilon. For rational r,R with R>r, combine 0 and R ei and let R tend to infinity; this gives q(r ei)<=S r+B epsilon. Exactly the same estimate holds on every nonexceptional pair ray, whose reference slope is S.

On an exceptional pair ray, joining zero to epsilon eij gives q(r eij)<=B epsilon for 0<=r<=epsilon; for r>=epsilon, the obstacle itself gives q(r eij)<=B r. These inequalities use only rational endpoints and do not assume continuity or PA regularity of q.

Consider an exceptional cone and rational a>=b>=0, d=a-b. For rational theta in (0,1), use the facewise convex combination

    a ei+b ej = theta (d/theta)ei+(1-theta)(b/(1-theta))eij.

If b<epsilon, choose theta small enough that b/(1-theta)<=epsilon. The ray bounds give q(x)<=S d+B epsilon=P(x). If b>=epsilon, the same combination gives q(x)<=S d+B b+theta B epsilon; letting theta decrease to zero gives q(x)<=S d+B b=Gamma(x)=P(x). The case d=0 is already the pair-ray bound; b=0 is the singleton bound. Swap a,b for the other half-cone.

In a nonexceptional half-cone use its singleton and pair rays with both bounds S r+B epsilon; the same combination gives q(x)<=S max(a,b)+B epsilon=P(x). We have proved q<=P at all rational points of X.

For any irrational x, take successively smaller rational simplices in the relative face containing x, with rational vertices y_k and x a convex combination of those vertices. Such simplices exist in every rational affine face by approximation in rational coordinates. This is a PCC after inserting the simplex into a rational subdivision. Then q(x)<=sum alpha_k q(y_k)<=sum alpha_k P(y_k), and continuity of P gives q(x)<=P(x). Thus every competitor is bounded above by P on all of X. Since P itself is a competitor, it is the exact envelope. The displayed envelope is continuous, so its upper-semicontinuous regularization is the same function. No envelope regularization theorem or all-obstacle regularity antecedent is hidden in this argument.

## Raw divisor calculations and exact contact integral

For any conical f on Sigma, put a_i=f(ei), b_ij=f(eij). The inward normals already chosen give

    (f.[X])(ei)=sum_{j!=i} b_ij-2 a_i,
    (f.[X])(eij)=a_i+a_j-b_ij.

For the first equation the adjacent linear slope on ej is b_ij-a_i and sum ej=-ei. For the second use normals ei,ej with sum eij. At a vertex a weighted one-cycle is intersected by summing its weights times outgoing slopes; constants make no contribution.

The germ of P at zero is B epsilon+S eta: a_i=S; the exceptional b_ij are zero and the others S. The first cycle has weights zero on singleton rays, 2S on the two exceptional rays, and S on the other four pair rays. It is balanced: e12+e34=0, and the sum of the other four pair vectors is zero. Intersecting again gives raw mass 4 S^2 at zero.

At p=epsilon e12, use the saturated basis e1,e2 of its plane and local coordinates x,y. Removing the constant B epsilon, the four affine gradients of P are

    (S,-A), (-A,S), (S,-S), (-S,S).

The local first cycle has primitive rays (1,1),(-1,-1),(1,0),(0,1), weights respectively 2A+B,2S,B,B, and outgoing slopes B,0,S,S. The weight balance is

    (2A+B)(1,1)+2S(-1,-1)+B(1,0)+B(0,1)=0.

These coefficients can be verified directly: on the positive diagonal use normals (1,0),(0,1), whose slope sum is 2S, and subtract the tangent slope B; on the negative diagonal use the same inward normals and tangent slope zero, giving 2S. Across each positive coordinate axis the opposing normal slope difference is B. The second intersection mass is therefore B(2A+B)+2BS=B(4A+3B). The other special vertex is identical. There are no other vertices in the described rational structure, so there are no other atoms. This also verifies globally that the first intersection cycle is balanced: only these three vertex balances need testing; along open edges the cycle is a straight weighted line.

The gradient polygon at a special vertex has ordered vertices (S,-S),(S,-A),(-A,S),(-S,S). Its shoelace area is B(4A+3B)/2. Thus the direct recursive calculation equals 2! times lattice-normalized Alexandrov area, as required, without appealing to toric Riemann--Roch or any analytic comparison. There is no ordinary full-dimensional Alexandrov formula at the singular origin being substituted for its raw mass.

For the reference Gamma, the first weights are B at every singleton ray, 2A+B at the exceptional pair rays, and S at the other four pair rays. Its raw degree is

    4BS+2B(2A+B)+4S^2=4A^2+16AB+10B^2.

The endpoint has total mass 4S^2+2B(4A+3B), exactly the same number. Nonetheless P-(Gamma+U)=(B-C)u_epsilon. This gap is (B-C)epsilon at zero and zero at both special vertices. The integral is exactly -4(C-B)epsilon S^2. In particular A=0,B=1,C=2 gives the integral -4 epsilon, MA(P)=4 delta_0+3 delta_{epsilon e12}+3 delta_{epsilon e34}, and degree ten. All these functions have literal integral slopes and rational constants.

## Literal regularity fails for the simplest reference

For Gamma=h and any integer n>=2, let c=1/n and define the bounded literal obstacle

    v_n=min{c,(1-h)_+}.

It has slopes zero or minus those of h and rational break levels, so belongs to PA_Z,b. Its exact envelope is

    Q_n=max{h,(1-1/n)h+1/n}.

Indeed the displayed function is ambient convex, has bounded difference from h, and is below h+v_n (on h<=1, the gap (1-h)/n is at most both 1/n and 1-h; outside it is zero). Every competitor has q(0)<=1/n and q(y)<=1 at h(y)=1. For rational x with h(x)<=1, take y=x/h(x) and the radial segment from zero; the convex bound is q(x)<=(1-h(x))/n+h(x). Outside h>=1, the obstacle is h. The irrational-point argument above finishes the proof.

On the primitive ray e1 and segment [0,1], Q_n(r e1)=1/n+(1-1/n)r. Let psi be any literal PA PC function and delta its uniform error. Its one-sided slope at the midpoint is an integer k. Convexity makes slopes nondecreasing. If k>=1, the right-half increment of psi is at least 1/2, whereas that of Q_n is (1-1/n)/2. Hence 2 delta>=1/(2n). If k<=0, the left-half increment is at most zero, yielding 2 delta>=(1-1/n)/2>=1/(2n). Thus delta>=1/(4n). No sequence of literal PAPC functions can converge uniformly to Q_n. Therefore (X,h) fails literal regularity. We assign no literal MA measure to Q_n through the source's regularizable operator. This does not affect the genuine finite literal PA measure of the main endpoint h+u_epsilon.

## Evidence, interpretation, and unresolved work

The script check_obstruction.py uses Python's standard-library Fraction arithmetic. Four parameter tuples are in obstruction-input.json. It checks all twelve cone saturation calculations, all vertex balances, the raw masses, polygon areas, and degree identity exactly. For each tuple it also exhausts 1,014 prescribed rational point checks and 1,800 midpoint checks, for totals 4,056 and 7,200. This is an exhaustive result only for those explicitly finite lists, not a proof of envelope equality or strictness for a continuum. The proofs above supply those claims independently. The simplest tuple reports degree ten, masses 4,3,3, special Alexandrov area 3/2, and integral -4.

The result improves the flat-reference obstruction in the supplied data by checking a strictly convex, coercive, integral reference on the same matroidal fan, computing an actual PA endpoint instead of a regularity/orthogonality dichotomy. It does not classify general pairs, establish real regularity for all obstacles on this fan, or settle any future smoothness hypothesis stronger than the precise matroidal and lattice properties proved here. In the literal category the simplest pair fails regularity separately; in the real category it is excluded from simultaneous regularity and universal contact by the main obstacle alone.

The source's three-dimensional embedding of this two-dimensional fan matters. A proof of contact using a full-dimensional ambient subgradient volume cannot substitute that volume for the singular fan's raw top intersection mass. Here the noncontact origin has positive raw mass while the envelope is affine along its exceptional two-sided line. Similarly, adding strict growth to the reference does not make the envelope germ strictly convex. A continuity-in-a-changing-reference strategy was considered and abandoned: it would require local continuity and an independently justified common operator domain. The explicit formula avoids those unproved premises.

The supplied cross-fan obstacle in its Example 4.25 takes incompatible values +epsilon and -epsilon at the shared origin on its two axes. It is therefore not a continuous admissible obstacle as printed. We do not use it. The present roof is continuous, equals epsilon at the origin on every cone, and satisfies all coefficient requirements. The control glyphs essential to our work are unambiguous in the fixed source: the face relation is inclusion as a face, and the contact formula uses ordinary grouping parentheses. Other dossier statements remain ungranted.

Current literature was searched first, and the exact fixed primary PDF/HTML was inspected. No later resolving primary result was found by these searches; this is not a proof that none exists. The quote-free application ledger is source-application-ledger.md. Retrieval evidence is saved as UTF-8 web-tool JSON, not as an original PDF byte stream: shell curl failed through the preconfigured proxy, whose settings were not changed. Provenance hashes therefore apply only to the retained actual response files. A supervised compute facility was not exposed; none was needed for these small finite rational checks. The requested model designation was not independently selectable from this turn; no claim is made that the execution runtime was changed.

Rerun: python check_obstruction.py; python source_provenance.py; pdflatex -interaction=nonstopmode -halt-on-error P05.2-paper.tex (twice). The manuscript, full argument, structured notes, inputs, programs, logs, and provenance reside in this workspace. All notes are unverified drafts. Candidate remains false because no necessary-and-sufficient structural criterion for all general pairs and all admissible obstacles has been established.
