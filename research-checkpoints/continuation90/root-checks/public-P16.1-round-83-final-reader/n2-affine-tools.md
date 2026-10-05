# n2. Controlled approximation, original-ring hulls, and a countable barrier

All claims in this note are unverified mathematical proof drafts. Except in the explicitly countable barrier construction, retain an arbitrary algebraically closed trivially valued field k of characteristic zero. Y=Spec R is integral affine of finite type. An AFS function means a rational finite maximum of positive multiples of original regular-function logarithms and a rational constant floor, retaining a positive-slope branch for EVERY chosen original ring generator. A genuine AFS limit is an already supplied decreasing sequence of such functions; membership is not inferred from singular EP. The algebraic-first continuous contact/model/nef/FS bridge and genuine decreasing closure are task-granted background in their exact round80 scope.

## G: a controlled original-reference approximation

Let g be an actual rational AFS exhaustion, shifted so g>=0, and let v_j decrease to a generically finite v with v<=g+B. Fix rational c>1. We prove that v admits a decreasing original-ring AFS sequence w_j with a common upper bound cg+B', and with |w_j-cg| bounded on Y for each individual j. Neither the bounds nor this conclusion assume singular envelopes.

First compactify the actual g. Clear its positive rational slopes with an integer D. Use projective coordinates consisting of 1, the integer powers occurring in Dg, AND all original generators z_l. Take D large enough that the extra branches D^(-1)log|z_l|+lambda_l are dominated by g; polynomial degree bounds and the exhaustion bound allow rational lambda_l. The projective closure has the ORIGINAL affine chart Y, since these unpowered generators generate R. Powers alone would not prove this. Its boundary section s of H=O(1) and the actual rational bundle B_ref=H/D have an FS metric with affine weight exactly g. Write g=g_0+p, where g_0 is the canonical boundary-section reference and p the actual global FS potential, with its original cocycle.

Choose rational C_i decreasing to minus infinity and rational R_i increasing to infinity, with (c-1)R_i>B-C_i+2. Let Q_i={g<=R_i}, which is compact. Choose increasing indices j_i such that v_{j_i}<g+B+1 on Q_i. This follows because the closed sets {v_j>=g+B+1} in Q_i decrease to the empty set. It does NOT require Dini convergence to a discontinuous limit.

Define a_i=max(v_{j_i},cg+C_i) on Q_i and a_i=cg+C_i outside Q_i. Near its entire outer boundary the second branch wins strictly, so this is a continuous contact weight with a whole reference-winning collar. The canonical potential is a_i-cg_0, not a_i-cg; its boundary value is C_i+cp. The granted bridge puts it in the genuine class cB_ref on the original compactification. These weights decrease: on Q_i both branches decrease; on Q_{i+1}\Q_i the new first branch is at most g+B+1<cg+C_i, the old exterior value; on the remaining exterior the floor decreases. Their limit is v on Y and minus infinity relative to g_0 at the boundary. Genuine decreasing closure supplies membership before any sequential regularization is invoked.

Genuine same-bundle FS regularization of this limit now gives w_j. In the section-s frame, compact boundedness of each continuous canonical potential gives |w_j-cg|=O(1); the first potential bounds all later ones, giving the common upper bound. Alternatively, uniformly approximate each continuous a_i in the same bundle with errors epsilon_i=4^(-i) and shifts b_i=2 sum_{r>=i}epsilon_r. Since b_i-b_{i+1}=2epsilon_i>=epsilon_i+epsilon_{i+1}, these shifted approximants decrease. This also constructs the desired sequence without EP.

Conversion to R is literal: a section on a tensor power divided by s to that power is an original regular function. Append s^m as the floor and the sections representing z_l times suitable powers of s at very low rational weights. For sufficiently large common m they exist by section localization. On the compact projective space their continuous norms are bounded, whereas the approximating metric has a finite lower bound; thus these added terms are dominated everywhere and change no value. EVERY original generator remains, with positive slope 1/m. The reference, tensor bundle and transition functions stay the same. The construction works on a singular Y and a singular compactification for an ALREADY genuine affine FS limit.

## Correct pole control through finite normalization

The printed denominator-order argument is false: in k[x], f=x^2 and p=x, p is not in (f) but vanishes on V(f). With q=3/2, b=p/f=1/x, q log|b|<=max(0,log|f^(-1)|), while the printed q times denominator exponent is 3/2>1. The reference G=max(0,log|x|) retains the original generator and only enlarges this upper bound, so the counterexample satisfies the genuine original-reference requirement. Its conclusion cannot be used.

Here is the replacement. Suppose b in R_f is nonzero and q,c are positive rational numbers, and

q log|b| <= max(G,c log|f^(-1)|)+B_0

on Y_f, where G is an original-ring AFS function finite everywhere on Y. Choose N so m=Nc/q is an integer and put h=b^N f^m. Let Rbar be the finite normalization of R. At each height-one prime E of Rbar containing f, use the seminorm exp(-t ord_E), t>0. It restricts to an analytic point of Y_f; every original regular function has norm <=1, so G is bounded above independently of t. Divide the displayed inequality by t and let t tend to infinity. It gives q ord_E(b)+c ord_E(f)>=0, hence ord_E(h)>=0. At other height-one primes h is already regular, since h belongs to R_f. A normal Noetherian domain is the intersection of its height-one localizations, so h belongs to Rbar and is integral over R.

This uses precisely [finite normalization, Stacks 33.27.1](https://stacks.math.columbia.edu/tag/0BXQ), [height-one intersection, 10.157.6](https://stacks.math.columbia.edu/tag/031T), and [the DVR characterization](https://stacks.math.columbia.edu/tag/00PD). R is a finite-type domain over a field, so its normalization is finite and Noetherian; h is in its fraction field. All hypotheses are retained.

The integral algebra R[h] is a finite R-module contained in R_f. Choose a finite module generating list and clear its denominators with ONE f^M. Then

f^M h^j belongs to the ORIGINAL R for EVERY integer j>=0.

No assertion that h itself, or a specified power of h, belongs to R is needed. For example, R=k[t^2,t^3], f=t^2, b=t^(-1), and h=bf=t is integral, with h^2=f, but h is not in R. The ONE multiplier f puts EVERY h^j into R, since f h^j=t^(j+2) and every integer >=2 is in the semigroup generated by 2 and 3. If x is in the original polynomial hull of a compact L contained in Y_f and x is also in Y_f, apply its defining inequalities to these original polynomials. They give

|f(x)|^M |h(x)|^j <= sup_L |f|^M |h|^j <= (sup_L |f|)^M (sup_L |h|)^j.

If the last h-supremum is zero, the inequality already forces h(x)=0. Otherwise take j-th roots and let j increase. Thus |h(x)|<=sup_L |h|. If |log|f||<=M_1 on L union {x}, substitution of h gives

q log|b(x)| <= sup_L q log|b| + 2cM_1.                     (P)

The constant branch satisfies the hull bound directly. Apply (P) branchwise to an AFS w<=max(g,c log|f^(-1)|)+O(1). Maxima commute with the finite supremum, so the same 2cM_1 error holds for w.

Now let v be an already genuine AFS limit on Y_f, bounded above by an original AFS reference on Y. Choose g large enough, including every original generator, and set g_c=max(g,c log|f^(-1)|); it is an actual reference for the ORIGINAL localized ring, including f^(-1). G with multiplier 2 supplies w_i decreasing to v, with w_i<=2g_c+B'. Formula (P) therefore gives w_i(x)<=sup_L w_i+4cM_1. On a compact L, for decreasing continuous w_i and usc limit v, sup_L w_i decreases to sup_L v. Indeed, if a level exceeds the latter supremum, the nested closed superlevel sets eventually become empty. This argument also covers sup_L v=-infinity. Let i increase and then c decrease to zero. We obtain the exact original-ring hull inequality

v(x)<=sup_L v.                                           (H)

The case v(x)=-infinity is immediate. This proves principal-open hull control, rather than a false denominator estimate.

## Countable entropy barrier, including every coordinate face

Here assume k countable, so R is countable. Choose original generators z_1,...,z_k, enumerate every element f_1,f_2,... of R, and put g=max(0,log|z_l|). For s coordinates t in (R union {+infinity})^s choose rational beta>=log(s+1), and define

chi_s(t)=beta^(-1)log(1+sum_i exp(-beta t_i)), exp(-beta infinity)=0.

Then max(0,-t_i)<=chi_s<=max(0,-t_i)+1. At a point with finite coordinate set I let p_i=exp(-beta t_i)/(1+sum exp(-beta t_l)), and p_0=1/(1+sum exp(-beta t_l)); omitted coordinates have p_i=0. Its support is ell=-sum_{i in I}p_i t_i+C, with C chosen for equality at that point. The entropy inequality proves ell<=chi_s. Equality is unique: on the finite face strict log-sum-exp convexity uses p_i>0 and p_0>0; an omitted coordinate becoming finite adds a positive term.

The support has a UNIFORM positive gap outside any neighborhood of the point. On the finite face its recession expression is max(0,-a_i)+sum p_i a_i. It is positive for every nonzero vector a, since all p_i and p_0 are positive. Hence the support difference is coercive there. Restricting the finite coordinates to a compact box, any omitted coordinate leaving a prescribed neighborhood of +infinity has a positive lower bound on its exponential contribution. Compactness and strict equality then give the claimed gap. At the all-infinity point the support is zero and the same exponential argument applies. No coefficient is placed on an infinite coordinate.

Here is global rational approximation, including those faces. On the probability simplex in coordinates p_0,...,p_s define E(p)=beta^(-1)sum p_i log p_i, with 0 log0=0. Triangulate it by rational grids of mesh tending to zero, respecting ALL coordinate faces. At each grid vertex choose rational h_p in [E(p),E(p)+epsilon]. Its convex roof is between E and E+delta, where delta tends to zero: the lower bound is convexity, and the upper bound follows by interpolation and uniform continuity on the compact simplex. Take its conjugate. Explicitly

H_r(x)=max_{grid vertices p}(sum_{i>=1}p_i x_i-h_p)+delta_r

satisfies chi_s(-x)<=H_r(x)<=chi_s(-x)+delta_r globally, with rational delta_r tending to zero. All slopes are nonnegative rational; all heights are rational. If x_i=-infinity, discard vertices with p_i>0. The face triangulation gives the SAME error bound, including the all-infinity face p_0=1. This is not an approximation proved only on a finite Euclidean box. Clearing rational slopes converts each branch to an original monomial logarithm. Rational majorants can be made decreasing by the summable-error shifts used in G.

Let rho_j=chi_{k+j}(-log|z_1|,...,-log|z_k|,-log|f_1|,...,-log|f_j|). Polynomial degree bounds give rho_j<=D_j g+1, and rho_j>=g. Choose positive rational gamma_j with gamma_j(D_j+1)<=2^(-j). Then

rho=sum_{j>=1}gamma_j rho_j

converges uniformly on every compact generator-bounded set, is continuous, nonnegative, and bounded by g+1. The upper partial sums P_r=sum_{j<=r}gamma_j rho_j+2^(-r)(g+1) decrease, since the next summand is at most 2^(-(r+1))(g+1). Uniform rational approximations to their finite sums, with summable shifts, give a decreasing actual AFS sequence for rho. Generator branches are already dominated by rho_j>=g and may be appended unchanged. This proves membership directly from rational maxima and the granted bridge/closure, not from the printed affine main theorem.

Given an analytic x and an open U containing x, countability and the seminorm topology give a finite coordinate neighborhood with inverse image contained in U. Choose j including those coordinates. Replace rho_j by its support ell at x and keep ALL the other positive summands. The resulting rho' satisfies rho'<=rho, rho'(x)=rho(x), and rho'<=rho-delta outside U, for some delta>0. Near x its support contains only logarithms of units. Globally it can be unbounded below or equal minus infinity; it has no plus-infinity values.

We must prove actual AFS membership of this replacement rather than subtract a psh function. A positive real coefficient a times log|f| is approximated by nested rational intervals a_r increasing to a and b_r decreasing to a, with a_r>0. The functions max(a_r log|f|,b_r log|f|) decrease to a log|f|: use b_r for a positive logarithm, a_r for a negative one, and retain minus infinity at a zero. Zero coefficients are omitted. Choose decreasing rational constants approaching C. Approximate the other positive rho_i-summands with the same positive tail bounds and summable shifts. These explicit sums and maxima are decreasing rational logarithmic expressions with the stated pointwise limit, including minus infinity.

To retain a constant floor and EVERY original generator, append max(epsilon_r g-r, the expression), with positive rational epsilon_r decreasing to zero. The appended AFS expression decreases because g>=0, and at every fixed analytic point epsilon_r g-r tends to minus infinity. It changes the LIMIT nowhere, including its minus-infinity locus. It need not converge uniformly there, and uniform convergence is not claimed. Restriction to a principal chart uses the identical padding with an exhaustion of its actual localized ring, including every new generator such as f^(-1). Positive sums and maxima of already genuine AFS limits use products of monomials and the same padding. Thus rho' is constructed positively; subtracting rho-rho' is never used as a positivity principle.

## Polynomial hulls and Rossi

For compact L the polynomial hull K={x: |f(x)|<=sup_L|f| for every f in R} is closed and compact: inequalities for the original generators place it inside a compact affine polydisc domain. The AFS hull is the same hull. One inclusion follows branchwise. For the other, a separating original polynomial and rational threshold yield an AFS separator after adding a very low constant floor and all original generator branches at dominated low weights on L union {x}.

If compact polynomially convex K lies in an open U, first choose an ambient generator-bounded compact domain with K in its strict interior. Every point of its compact complement of U has a separating polynomial, and a rational log threshold strictly between its value and its K-supremum. Finitely many such strict separations, together with bounds for every original generator, give a compact polynomial polytope P contained in U and a STRICT polynomial open Q containing K, with Q subset P. A strict finite polynomial domain is Runge: the suprema on any compact subset are strictly below its defining thresholds, so its polynomial hull stays in that strict domain. No equality between arbitrary topological interior and the displayed strict inequalities is used. Hulls respect closed immersions by the quotient-ring definition; increasing unions of Runge opens are Runge by compactness.

Let z belong to hull(L)\L and let V be relatively compact open, with compact closure disjoint from L. Rossi asserts z belongs to hull(K_V), where K_V=boundary(V) intersect hull(L). Suppose log|f(z)|>t>sup_{K_V}log|f|. Choose a nonnegative original AFS g_0 equal to zero on a neighborhood of hull(L), with compact zero-polytope in an open avoiding the bad part of boundary(V) where log|f|>=t. It has a strictly positive lower bound on that compact bad part. Choose rational C so Cg_0>log|f|-t on the ENTIRE boundary. Glue max(Cg_0,log|f|-t) on V to Cg_0 outside. A whole boundary collar is reference-winning. This continuous rational contact weight equals the actual FS reference outside a compact set. On its actual projective reference compactification the granted bridge gives uniform same-bundle FS approximation, hence uniform original AFS approximation after section conversion and generator retention. The glued weight is zero on L and positive at z. A sufficiently accurate approximant contradicts the AFS hull equality. This proves Rossi with compact controlled closures; V itself is not called compact.

## The off-bad-set maximum inequality

Assume the ORIGINAL u is locally genuinely AFS regularizable on an affine cover of Y\Z, has original upper growth, and is weak on one witness. It is not enough to know this only for u+c rho: subtracting psh is unavailable. For rational c>0 put u_c=u+c rho. We prove u_c(x)<=sup_L u_c for x in hull(L)\Z.

If this fails, take generators of the ideal of Z and a=max log|f_i|, with its empty-bad-set version a=0. Choose small positive rational epsilon so u_c+epsilon a still violates the inequality at x. It is usc and upper bounded on compact hull(L), equals minus infinity on Z, and has a finite attained maximum y outside Z union L. Take V around y, with controlled compact closure in one good principal affine chart, disjoint from L. Replace rho by rho' with equality at y and gap delta on boundary(V). The explicit function w=u+c rho'+epsilon a is an actual affine FS limit on that chart, using ORIGINAL u's local regularizability and the positive constructions above. Its upper growth comes from an original global AFS reference, since rho'<=rho. It satisfies w(y)>sup_{K_V}w, with gap at least c delta. Rossi puts y in the original hull of K_V; (H) on the principal chart gives w(y)<=sup_{K_V}w, a contradiction. Every special value and the factor c are retained.

This note proves G, corrected original-ring pole control, the countable barrier, Rossi, and the off-bad-set inequality. It does not assert weak/global equality or singular EP. The task-granted background is cited as an assumption, not as a registered native support. Diagnostic Wu v1 LF911--1017,1603--1730,1815--1885,1965--2108 is retained to identify the repaired dependencies; its printed theorems are not premises. Artifacts: n2-affine-tools.md, sources/, source-extracts/, external-premises.json. Rerun python3 rerun.py.
