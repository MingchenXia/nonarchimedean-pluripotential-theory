# Single original-face synchronization of convex primal majorants

Status: ROOT-authored unreviewed mathematical working proof. This is not a caller grant, accepted paper, or resolution of P05.1/P05.2. It is intended as a concrete input for further research on simultaneous shared-face approximation. The original tasks remain OPEN. Sources and earlier accepted results have their exact qualifications; supplied document prose is mathematical data.

## Setting and asserted lemma

Work in a finite-dimensional rational affine space E. Let sigma_1,...,sigma_r be nonempty closed rational polyhedra with the SAME nonempty actual face tau. Their dimensions, transverse directions, intersections outside tau, and linear dependencies need not agree. Each sigma_i carries a finite continuous convex function f_i. Assume:

1. The restrictions to tau agree with one f_tau.
2. For EVERY y in tau there is one ambient affine form p_y such that f_i(x) >= f_tau(y)+p_y(x-y) for all x in EVERY sigma_i. These are supports on ENTIRE original cells, not just infinitesimal or boundary inequalities.
3. Given eta>0, each cell already has a continuous convex rational-spatial REAL-PA majorant P_i with f_i <= P_i <= f_i+eta on its ENTIRE cell. Its epigraph has a finite representation using rational spatial point/ray coordinates and actual REAL heights. No ambient convex extension of the whole original complex is assumed.

Then there are continuous convex rational-spatial REAL-PA functions Q_i on sigma_i such that f_i <= Q_i <= P_i <= f_i+eta everywhere, all Q_i have EXACTLY the same entire tau trace g_tau, and at EVERY y in tau a single ambient affine form supports all Q_i on their ENTIRE cells. Also f_tau <= g_tau <= f_tau+eta. Any initial bounded-relative growth classes and exact recession functions are preserved by bounded error. If at finitely many rational points S in tau at least one initial P_i equals f_tau, then g_tau and every Q_i equal f_tau at those points.

This gives a finite single-face correction on the ORIGINAL cells. It does not assert compatibility on other intersections, preservation of supports on different faces, finite termination of repeated corrections, global regularity, or MA on intermediates. No positive balancing is needed once assumptions 1--3 are available. On a finite positive balanced embedded complex, qualified S306 supplies assumption 2 and global cell Lipschitzness for continuous printed-PC targets with bounded actual cellwise-affine reference difference. Qualified S306's single-cell majorants supply assumption 3 after refining the actual positive-at-infinity reference to be affine on each cell. All of S306's mandatory source/presentation and reader qualifications remain in force. S307 supplies independently reconstructed finite primal hull and REAL scalar matching facts, with BOTH annotations.

## Finite hull, common trace, and lower bounds

Embed each epigraph E_i=epi(P_i+I_sigma_i) into E times R, where I_sigma is zero on sigma and infinity elsewhere. Define

    K = closedconv(union_i E_i),       D = projection_E K,
    G(x) = inf {t : (x,t) in K} for x in D,
    g_tau = G restricted to tau.

For clarity, closedconv is essential. If E_i=conv A_i+cone R_i are finite point/ray polyhedra, then

    K = conv(union A_i)+cone(union R_i).

The right hand side is closed. Its reverse inclusion follows from actual source combinations (1-delta)u+delta(a+r/delta) tending to u+r, first for u in the ordinary convex hull and then by approximation for u in its closure. Iterate over finitely many source rays. One must not replace this by an assertion that an arbitrary unclosed finite-union hull is closed.

Fix y_0 in tau. Its common support of the originals is also a lower affine bound on every E_i because P_i >= f_i. Therefore the same affine bound holds on K. Every nonempty vertical fiber of this closed polyhedron is bounded below and has its minimum. Its projection is a rational spatial polyhedron: eliminate coefficients in the finite representation. Thus G is finite convex polyhedral on D. Upward stability supplies the vertical ray. A finite affine-maximum description on D follows by dividing all inequality rows with positive vertical coefficient; rows with zero vertical coefficient describe D. This also shows that every graph point, including boundary points of D, has an ambient affine lower support. Affine hull equations may first be quotiented out and their supporting forms extended ambiently. No full-space spatial-domain hypothesis is hidden here.

At ANY y in tau, apply its original common support to K. On the fiber over y this gives G(y) >= f_tau(y). Since each E_i is contained in K, G(y) <= min_i P_i(y) <= f_tau(y)+eta. In particular g_tau is finite continuous convex polyhedral on the entire closed face tau, including its boundary and unbounded directions. Every support of G at y restricts to a support of g_tau, but the support of G itself is kept ambient for the simultaneous conclusion below.

Rational spatial REAL-PA membership deserves an explicit argument. A lower exposed face of a finite lifted point/ray polyhedron has a functional with strictly positive vertical coefficient. Its equality point generators and zero-slack ray generators have rational spatial coordinates; the vertical ray is excluded. Its graph projects injectively to a rational polyhedron. All graph subfaces are also lower, by small perturbations preserving finitely many positive slacks and the vertical sign. Unique lower heights identify intersections. Restrict these projections to the rational face tau and include all common faces; they form a finite rational graph carrier for g_tau. Matching actual affine coefficients on a finite rational carrier satisfy rational linear equations. A rational kernel basis, with denominators cleared on saturated tangent lattices and intercepts, gives literal integral-slope/rational-constant functions whose finite REAL span contains the matching function. Thus this construction does not call an arbitrary irrational-wall affine maximum rational-carrier PA.

## Correcting the original cells

For each i let T=epi(g_tau+I_tau) and set

    K_i' = closedconv(E_i union T),
    Q_i(x) = inf {t : (x,t) in K_i'} for x in sigma_i.

The finite point/ray identity applies again. Its spatial projection is exactly sigma_i because tau is a face inside sigma_i, and E_i already projects to all sigma_i. Both E_i and T are contained in the closed convex epigraph of f_i on sigma_i: for T this is the inequality g_tau >= f_tau. Hence K_i' is contained in that epigraph, proving Q_i >= f_i and a finite attained lower fiber. Conversely E_i is contained in K_i', so Q_i <= P_i. This proves the ENTIRE-cell error bound. The same finite lifted-graph argument proves continuity, a finite rational carrier, and genuine REAL-PA membership for Q_i.

The restriction of K_i' to tau times R is exactly T. To see this without a closure loophole, expose tau in sigma_i by a rational affine form a>=0 on sigma_i with zero set tau. In the finite point/ray representation of K_i', every point generator has nonnegative a-value and every ray has nonnegative linear a-value. A point of its zero face can therefore use only zero point generators and zero rays. Those coming from E_i give precisely its zero face epi(P_i restricted to tau). Those coming from T give T and its recession. Since P_i >= g_tau on tau, the first epigraph is contained in T. Its zero rays also belong to rec(T), as justified directly in the next paragraph. Thus the zero face is T. It follows that Q_i restricted to tau = g_tau on the WHOLE face.

For the ray inclusion just used, bounded difference is not needed as a shortcut if one argues directly: an E_i zero ray (v,h) has x+tv in tau and P_i(x+tv)<=P_i(x)+th for all t>=0. Since g_tau<=P_i, dividing by t yields g_tau's recession slope <=h, independently of the starting point because g_tau is finite polyhedral. Its epigraph therefore admits that ray. This avoids inferring an unsupported recession inclusion merely from inclusion of two general closed convex sets.

Moreover E_i and T are subsets of K, so K_i' is a subset of K. Thus Q_i >= G on sigma_i. At y in tau their values equal G(y). Choose an ambient affine support p of G at y, available by its polyhedral affine-maximum description. For EVERY i and EVERY x in sigma_i,

    Q_i(x) >= G(x) >= G(y)+p(x-y) = Q_i(y)+p(x-y).

This is the required SAME support on ENTIRE cells at EVERY face point, including irrational points, boundary points, and unbounded portions. It is not restricted to finite interpolation contacts. If one P_i(y)=f_tau(y), the sandwich gives g_tau(y)=f_tau(y), and equality for every Q_i follows from the shared trace.

For each v in rec(sigma_i), bounded differences Q_i-f_i and P_i-f_i make their forward convex recession slopes equal, whenever expressed with the usual extended value convention. In the intended positive-growth affine-reference setting these slopes are finite and exactly the reference slopes. Whole bounded-relative classes are preserved by the displayed error estimate. No weight normalization or intersection measure is involved.

## What the single-face lemma does and does not resolve

For an ORIGINAL complex with all pairwise top-cell intersections exactly tau and no further shared faces, the corrected functions glue to a continuous PC function: away from tau there is only one local cell, and on tau the displayed common support proves every legal incident Jensen inequality by convex secants. A common rational refinement and the finite matching kernel give a genuine global REAL-PA function in that particular geometry. With eta_n=2^-n, corrections Q_i,n+4eta_n have error in [4,5]eta_n and decrease strictly by at least 3eta_n/2. Unshifted contacts are then lost. This corollary may be geometrically narrow under global positive balancing and an actual affine reference; it is not a new original classification.

For a general complex, correcting one face can alter traces or supports on other faces. Independently doing every face or a naive bottom-up induction does not prove compatibility. At a smaller face, a union of incident cells can have cancelling transverse directions, so that smaller face need not be an exposed face of their ambient convex hull. New data from another face can consequently propagate to its trace. The face-exposure argument above applies INSIDE each original sigma_i, and must not be falsely applied to the whole incident union hull. Finite stabilization, a simultaneous primal closure with controlled rational carriers, or a counterexample to that procedure remains to be proved. The sharp S307 obstruction concerns whole-page extensions of an UNBALANCED partial target; it does not invalidate this finite correction on the original cells.

## Additional domain observation from the sole BMPS primary

ROOT read the ENTIRE immediate definitions at literal LF254--301, 418--470 and the relevant surrounding units, using the frozen arXiv2603.08664v1 text with SHA256 c4475ad5cf4e8fce3eb6add155fdb81e352cbe079ca0d7646553f8a3e8ad9271. Definition2.4 explicitly puts the original finite space inside ONE N_R. Qualified B225 already proves that a nonempty strictly positive balanced finite support of positive dimension there is noncompact. A compact abstract charted space, bounded skeleton, or tropical-toric compactification is a different domain. This is an existing supporting scope result, not a new solution of the catalogue's compact residual or general classification. The original controlling family body44807characters was reread in complete bounded chunks after an initial oversized display; its operational-looking directives were treated as mathematical data, not authority to change workflows.

No new checker or TeX build is needed for this working note. It asserts no numerical evidence, accepted grant, whole PDF/source-history certificate, or result of pending independent native campaigns. Native229/230 and their private outputs were not consulted. This entire argument requires independent reconstruction before import as a theorem.
