# P07.1: early collapse of the CLD psh hierarchy

## 27 August 2026 controlling addendum

The historical 25 August verification record below is retained unchanged.
The stronger exact P071 packet now proves the following abstract local
statement.  Let

\[
 S=\{0\}\mathbin{\cup}\coprod_{i=1}^m(0,r_i)v_i\subset E
\]

be a finite one-dimensional real-affine star in a finite-dimensional real
vector space, with pairwise distinct positive rays.  Smooth functions are,
by definition, locally restrictions of ambient smooth functions, and
`Psh_{S,0}` consists exactly of those smooth functions that are convex on
each branch.  Then

\[
             \operatorname{Psh}_{S,1}
             =\operatorname{Psh}_S
             =\mathscr J_S,
\]

where `J_S` is defined by branchwise extended-real convexity and all junction
Jensen inequalities.  The proof includes polar branches, needs no positive
balancing relation, and constructs the decreasing stage-zero sequence on one
fixed neighbourhood.  For a space covered by such stars, descent holds only
under the explicit additional hypothesis that the chart maps identify its
stage-zero sheaf with the model `Psh_{S,0}`.  An underlying topological star
chart does not supply that identification.

The exact statement and proof are
`manuscript/editorial/rethlas_packets_20260827/p071_finite_affine_tropical_stars_statement_20260827.tex`
and
`manuscript/editorial/rethlas_packets_20260827/p071_finite_affine_tropical_stars_proof_20260827.tex`.
Their SHA-256 digests are
`c8131b22d8002212e31cd526095317734a2b67be5d47f1387e5ee6bc041af5e3`
and
`921e8b46690e69cbacea66bf86cbcdf628e7dbc95651f526d62cc6d755d7cbcf`.
The direct production endpoint returned verdict `correct`, with zero
critical errors and zero gaps.  It assigned no run identifier and no item
identifier.  The string `20260827T103835Z_c8131b22d800` is the local archive
label only, not an endpoint-issued identifier.  The request, response, and
headers digests are respectively
`ac68faee9ddb39bd3a30373e193196fc0a25431477a34e5c9cea6b49947299ed`,
`4f9a8b82e6eb7134cf76a5eac5ac0313db8f0e6cca082d369976db04ec115cfe`,
and
`2d161b58dbf027d6e9461e11cb0008b582425f0adb2d1ad29318d4c43398d17e`.

The exact scope firewall is essential.  The abstract result uses no lattice,
rationality, weights, balancing, calibration, harmony, or boundary
designation.  This does not by itself identify the CLD stage-zero sheaf in a
positive-sedentarity or other tropical boundary chart, nor does it cover a
nonambient-induced smooth structure, an infinite star, or a
higher-dimensional local model.  Thus both live atoms P07.1 and P07.2 remain
active.  The inventory is unchanged at 16 problem environments and 55 active
atoms.  No post-integration or whole-book build gate is recorded by this
addendum.

## Disposition

The unrestricted problem in Chapter 72 remains open after this pass.  Two
substantial natural cases do close at the first stage.

1. On every tropical toric partial compactification `N_Sigma`, equipped with
   its standard Lagerberg smooth structure, the CLD-generated psh sheaf, its
   first decreasing-limit stage, and the psh sheaf of Burgos Gil--Gubler--
   Jell--Künnemann coincide.  This is a short sheaf-theoretic consequence of
   their local regularization theorem.
2. On a one-dimensional boundaryless affine tropical space whose local stars
   are finite balanced polyhedral fans with the ordinary induced smooth
   structure, the CLD hierarchy also collapses at stage one.  A direct proof
   is given below.  Its key points are a finite-star Jensen inequality, a
   Farkas support covector, chordal approximation on the branches, and a
   regularized maximum which is exactly affine near the vertex.

The exact theorem/proof packet is
`manuscript/editorial/rethlas_packets_20260825/p07_cld_hierarchy_toric_curve_exact.tex`.
Production Rethlas verified these exact bytes with `gpt-5.6-sol/xhigh` on
25 August 2026: run `20260825T024707Z_d1b8d7eaf79e`, item
`pi_ccfb83de7a7be82ef602cd72`, `verification_status = final`, `verdict =
correct`, no critical errors, no gaps, and no expanded-proof request.  The
controlling proof SHA-256 is
`316a774fbb4eda54150b63cae0c9f23a1edab17a75b89beeee6d56d402f8c4a0`.
The statement and request SHA-256 values are respectively
`d1b8d7eaf79e155ecf7b347e4fcc1717c72d5a8090e346b2cb2fc9c9a0996e63`
and
`9490d443d40011c15fbd146e3b3b740876006752f75a5698fd1972da1b7940dd`.
After the production pass, the result was integrated into Chapter 16 at
`sec:ch16-collapse-positive-cases`, between the Euclidean-chart discussion
and the subsection on composition and maxima.  The live version preserves
the verified hypotheses and fixed-neighbourhood conclusion, adds a complete
proof of the finite-dimensional Farkas alternative used in the packet, and
includes the weighted-tripod example `ex:ch16-collapse-weighted-tripod`.
No novelty or priority assertion is made for the toric synthesis or the
standard convex-duality input.

## Live integration map

- Toric comparison: `prop:ch16-collapse-tropical-toric`, with equality
  `eq:ch16-collapse-tropical-toric`.
- Finite-dimensional support criterion:
  `lem:ch16-farkas-ray-support`, with
  `eq:ch16-farkas-ray-support` and
  `eq:ch16-farkas-ray-relations`.
- Finite-valence curve collapse:
  `thm:ch16-collapse-finite-tropical-curves`, with the fixed-neighbourhood
  conclusion and the main equality
  `eq:ch16-collapse-finite-tropical-curves`.
- Load-bearing equations in the curve proof:
  `eq:ch16-curve-branch-convexity`,
  `eq:ch16-curve-balanced-star`,
  `eq:ch16-curve-junction-jensen`,
  `eq:ch16-curve-support-covector`,
  `eq:ch16-curve-regularized-approximant`, and
  `eq:ch16-curve-uniform-sandwich`.
- Exact boundary of the result: `rem:ch16-collapse-scope-firewall`.

The targeted `git diff --check` and uniqueness check for all labels above
passed.  A full `latexmk` run parsed Chapter 16 and continued through
Chapter 68; it stopped later at an unrelated pre-existing/concurrent
undefined `\an` command in Chapter 69.  Thus the integrated block is
TeX-syntactically clear, while the whole-book build remains externally
blocked beyond Chapter 16.

## Exact live question and source correction

The live atom is `P07.1`, represented by
`prob:frontier-cld-hierarchy` in
`manuscript/parts/part6/ch72_major_open_problems.tex`.  If
`Psh_{X,0}` is the sheaf of smooth functions with nonnegative
`d'd''`, `Psh_{X,alpha+1}` consists locally of decreasing sequential
limits from the preceding stage, and a limit stage is the local union, the
question is whether

\[
                         \operatorname{Psh}_{X,1}
                         =\operatorname{Psh}_X.
\]

CLD Definition 8.1.13 calls membership in `Psh_{X,1}` *localement
approchable*.  CLD Lemma 8.1.4 already proves eventual stationarity by a
cardinality argument.  The literal sentence in Remark 8.1.6 saying that
stationarity is unknown contradicts that lemma and the later uses of it.
Thus the coherent analytic problem is first-stage collapse, not eventual
set-theoretic stationarity.  The live Chapter 16 now states this correctly.

## Primary sources checked

### Chambert--Loir--Ducros

The local full text is `tmp/pdfs/cld25.txt`, extracted from
arXiv:1204.6277v2 (25 July 2025).

- Definition 8.1.1 defines the generated psh sheaf.
- Lemma 8.1.4 defines the ordinal filtration and proves eventual
  stationarity.
- Proposition 8.1.5 gives stagewise pullback.
- Definition 8.1.13 calls first-stage psh functions locally approachable.
- Proposition 8.2.1 gives stagewise smooth convex nondecreasing
  composition.

### Burgos Gil--Gubler--Jell--Künnemann

Primary source: *Pluripotential theory for tropical toric varieties and
non-Archimedean Monge--Ampère equations*, Kyoto J. Math. 65 (2025),
55--152; arXiv:2102.07392.

- Definition 3.1.2 defines psh functions on an open subset of `N_Sigma` by
  upper semicontinuity, convexity on the dense stratum, and the boundary
  inequality.
- Proposition 3.1.3 proves locality and stability under decreasing
  sequences.
- Theorem 3.1.4 identifies this condition with continuity plus convexity on
  the dense stratum.
- Section 2.2 uses the standard sheaf of smooth Lagerberg forms on
  `N_Sigma`; this is the smooth structure used in the comparison packet.
- Theorem 3.3.4 proves that their psh functions are exactly the functions
  locally representable as decreasing sequences of smooth psh functions.

The toric conclusion is therefore not a new regularization theorem.  The
only synthesis is to observe that the BGJKK psh sheaf is a decreasing-limit
stable sheaf containing the CLD smooth psh generators, while Theorem 3.3.4
puts every BGJKK psh function in the first CLD stage.

### Botero--Mazzon--Pille-Schneider

Primary source checked at arXiv full-text level (submitted 9 March 2026;
the current v1 manuscript itself is dated 24 August 2026):
*Monge--Ampère measures on balanced polyhedral spaces*,
arXiv:2603.08664v1, manuscript dated 24 August 2026.

- Definition 3.20 defines their global polyhedral PSH class directly by a
  decreasing sequence of piecewise-affine polyhedrally convex functions.
- Theorem 6.4 isolates the **regularity property**, equivalent to uniform
  density of piecewise-affine polyhedrally convex functions among finite
  polyhedrally convex functions with fixed growth.
- Proposition 6.13 proves that regularity property in dimension one.
- Remark 6.6 records the complete affine-space case and the conical
  homogeneous case, while explaining that the general polyhedral hull issue
  is unclear.

This paper does not state the CLD ordinal-collapse problem, and its
piecewise-affine approximants are not CLD-smooth.  It does, however, identify
the higher-dimensional obstruction very accurately: after the finite-star
Jensen reduction, one still needs a polyhedral regularization theorem.  The
one-dimensional proof below supplies the additional bridge from
piecewise-affine convex approximants to CLD-smooth psh approximants.

## The tropical toric case

Let `Psh^tor` denote the BGJKK sheaf on `N_Sigma`.  A standard Lagerberg-
smooth function `f` with `d'd''f >= 0` is continuous and its restriction to
the dense vector space is convex, since its Hessian is positive
semidefinite.  BGJKK Theorem 3.1.4 therefore gives `f in Psh^tor`.
BGJKK Proposition 3.1.3 says that `Psh^tor` is local and stable under
decreasing sequences.  By the minimality in CLD Definition 8.1.1,

\[
                  \operatorname{Psh}^{\mathrm{CLD}}_{N_\Sigma}
                  \subseteq \operatorname{Psh}^{\mathrm{tor}}_{N_\Sigma}.
\]

Conversely, BGJKK Theorem 3.3.4 writes every toric psh function locally as
a decreasing sequence of smooth toric psh functions.  The smooth structures
and positivity cones are the same standard Lagerberg ones, so this says

\[
                  \operatorname{Psh}^{\mathrm{tor}}_{N_\Sigma}
                  \subseteq
                  \operatorname{Psh}^{\mathrm{CLD}}_{N_\Sigma,1}.
\]

The reverse inclusion of the first stage into the generated sheaf is
tautological.  Hence all three sheaves coincide, for an arbitrary fan and on
arbitrary open subsets.  This strictly enlarges the Euclidean-chart case
currently displayed in Chapter 16, since it includes all toric boundary
strata.

## The finite one-dimensional case

### Interior edges

On a one-dimensional local polyhedral complex, the functions whose
restrictions to connected edge segments are extended-real convex form a
subsheaf stable under decreasing limits and containing all smooth psh
functions.  CLD minimality therefore makes every CLD-psh function
branchwise convex.  On an open interval an extended-real convex function
with no `+infinity` value is either finite everywhere or identically
`-infinity`: if `u(x)=-infinity` and `u(y)` is finite, choose a point `z`
beyond `y` in the direction from `x` to `y`; convexity on `[x,z]` forces
`u(y)=-infinity`.

The identically `-infinity` germ is a decreasing limit of constants.  In
the finite case, fix `V` with compact closure in an interval `K`.  Chordal
interpolants on `K` converge uniformly from above to `u`.  Each is the
maximum of the affine extensions of finitely many pieces, so applying a
smooth convex nondecreasing regularized maximum yields smooth convex
functions converging uniformly on `K`.  CLD Lemma 8.1.10 converts a
subsequence, after constant shifts, into a decreasing sequence on the one
fixed open interval `V`.  Thus the conclusion at an edge interior is
genuinely stage one.

### Local model

At a vertex, shrink to a star

\[
 S=\{0\}\cup\coprod_{i=1}^m(0,r_i)v_i\subset\mathbf R^N,
 \qquad
 \sum_{i=1}^m w_i v_i=0,
 \qquad w_i>0.
\]

The weights are the positive calibration weights.  The local smooth
structure is the restriction of ambient smooth functions.  Along an open
edge, the problem is ordinary one-dimensional convex regularization.

### A closed Jensen class containing the CLD generators

For `u:S -> R union {-infinity}`, impose:

1. each branch function `u_i(t)=u(tv_i)` is convex in the extended-real
   sense;
2. whenever `alpha_i >= 0`, `sum alpha_i=1`, `t_i in [0,r_i)`, and
   `sum alpha_i t_i v_i=0`, one has

   \[
       u(0)\leq\sum_i\alpha_i u_i(t_i).
   \]

Every smooth psh function has these properties.  Indeed, its restriction to
each ray is convex.  If `ell` is its ambient affine tangent at the vertex,
then branchwise convexity gives `u_i(t)>=ell(tv_i)`, and the displayed
inequality follows after taking the convex combination.

The sheaf-locality point is load bearing.  Suppose the condition holds on
the members of an open cover, and fix an admissible tuple in a vertex star.
Choose a cover member containing the vertex.  Since the star is finite,
there is one `s in (0,1)` such that all scaled points `s t_i v_i` lie in a
smaller star in that member.  The local inequality gives

\[
             u(0)\leq\sum_i\alpha_i u_i(s t_i).
\]

If `u(0)=-infinity`, the desired unscaled inequality is automatic.  If it
is finite, branchwise convexity gives

\[
 u_i(s t_i)\leq (1-s)u(0)+s u_i(t_i).
\]

Taking the weighted sum and cancelling the finite term propagates the
inequality to the original tuple.  Hence the Jensen class is a genuine
subsheaf, not merely a collection of starwise conditions with shrinking
radii.  It is stable under decreasing limits because every sum is finite.
CLD minimality now applies and shows that every CLD-psh function satisfies
the two conditions.

### The extended values do not create an extra local rank

If `u(0)` is finite, put

\[
                    L_i=\lim_{t\downarrow0}u_i(t).
\]

Upper semicontinuity gives `L_i<=u(0)`.  Apply the junction inequality to
`alpha_i=w_i/sum_j w_j` and to a common small `t`.  Letting `t` tend to zero
gives

\[
 u(0)\leq\sum_i\alpha_iL_i\leq u(0).
\]

All weights are positive, hence every `L_i=u(0)`.  No branch can take the
value `-infinity` away from the vertex: convexity would then force its limit
at the vertex to be `-infinity`.  Thus `u` is finite and continuous on a
smaller star.

If `u(0)=-infinity`, convexity shows on each of the finitely many branches
that `u` is identically `-infinity` on an initial interval.  After one common
shrinking, `u` is identically `-infinity`.  It is then the decreasing limit
of the smooth psh constants `-k`.

### Chordal polyhedral approximation and the support covector

Assume now that `u` is finite.  On each branch choose a partition beginning
at zero, with mesh tending to zero, and let `h_i` be the chordal interpolant
of `u_i`.  The resulting `h` is continuous, convex and piecewise affine on
each branch, lies above `u`, and converges uniformly to `u` on a compact
smaller star.

Let `t_i>0` be the first partition point and set

\[
                   A_i=\frac{u_i(t_i)-u(0)}{t_i}.
\]

There is a covector `xi in (R^N)^*` with `xi(v_i)<=A_i` for every `i`.
Indeed, Farkas' lemma says this is equivalent to

\[
      \sum_i\lambda_iA_i\geq0
      \quad\text{whenever}\quad
      \lambda_i\geq0,
      \quad\sum_i\lambda_i v_i=0.
\]

For such a nonzero `lambda`, take

\[
 \beta_i=
 \frac{\lambda_i/t_i}{\sum_j\lambda_j/t_j}.
\]

Then `sum beta_i t_i v_i=0`, and the junction inequality at the points
`t_i v_i` is exactly the required Farkas inequality after clearing the
positive denominator.  Since the slopes of a convex chordal interpolant are
nondecreasing, the affine function

\[
                         \ell(x)=u(0)+\xi(x)
\]

lies below `h` on the whole star.

### From a polyhedral approximant to a CLD-smooth one

Write the restriction of `h` to branch `i` as the maximum of its finitely
many affine pieces `L_{ij}(t)`.  For `C>0`, put

\[
                         B_i(t)=u(0)+C+\xi(tv_i).
\]

Let `M_eta` be a smooth convex regularized maximum which is nondecreasing in
all entries, differs from the maximum by at most `eta`, and equals a
dominant entry whenever it exceeds every other entry by at least `2 eta`.
For `2 eta<C`, define

\[
               g_i(t)=M_\eta(B_i(t),L_{i1}(t),\ldots,L_{iq_i}(t)).
\]

At the vertex, `B_i(0)=u(0)+C` while every affine piece is at most `u(0)`.
Thus `g_i=B_i` on an initial interval.  The branch functions consequently
glue near the vertex to the single ambient affine function
`u(0)+C+xi(x)`.  Away from the vertex they are ordinary smooth functions on
open edges.  Each `g_i` is convex, so the glued function `g` is CLD-smooth
and psh.  Since `ell<=h`,

\[
                         h\leq g\leq h+C+\eta.
\]

Letting `C,eta` tend to zero gives uniform smooth psh approximation of every
chordal `h`.

Choose one such smooth approximation for each chordal interpolant.  The
resulting smooth psh sequence converges uniformly to `u`.  CLD Lemma 8.1.10
applied on the fixed compact smaller star says that, after adding twice the
uniform error and passing to a subsequence, the sequence decreases to `u`.
Hence `u` lies in `Psh_{S,1}`.  This proves first-stage collapse on every
finite balanced one-dimensional local star.

## Hostile checks on the curve proof

- **No hidden minimum.**  The construction uses only chordal interpolation,
  Farkas' lemma, and a regularized maximum.  It never smooths a minimum.
- **One fixed neighbourhood.**  All approximants are built on a fixed
  smaller compact star and then restricted to its interior.  No countable
  intersection of shrinking neighbourhoods is used.
- **Sheaf locality.**  A junction inequality known only on a cover member
  near the vertex is scaled there and propagated to the original tuple by
  branchwise convexity.  Thus no countable intersection of the local
  neighbourhoods attached to successive CLD stages is hidden in the
  minimality argument.
- **Monotonicity.**  The branch smoothing itself need not be monotone.
  Uniform convergence on the fixed star and CLD Lemma 8.1.10 supply a
  genuinely decreasing subsequence after constant shifts.
- **Singular values.**  The value `-infinity` is handled before uniform
  approximation.  Balancing forces a nontrivial psh germ to be finite and
  continuous at a vertex; the identically `-infinity` germ is approximated
  by constants.
- **Singular finite stars.**  No smoothness or matroidal hypothesis on the
  fan is used.  Extra linear relations among the rays are handled by the
  full Farkas condition, not by assuming that balancing is the only
  relation.
- **Boundary.**  The proof uses a positive balancing relation through every
  branch and is stated only at boundaryless vertices.  It must not be
  silently applied to a tropical boundary point.
- **Infinite stars.**  Finiteness is used in taking one common shrinking,
  one finite regularized maximum, and one common affine neighbourhood.  The
  CLD infinite-star examples in Section 6.7.3 are outside the statement.

## Why the higher-dimensional problem remains open

On a finite polyhedral star in any dimension, the same tangent-plane
argument puts every CLD generator in the sheaf of polyhedrally convex
functions, and decreasing limits preserve the corresponding Jensen
inequalities.  What is missing is the higher-dimensional analogue of the
one-dimensional chord construction: uniform approximation by
piecewise-affine polyhedrally convex functions, followed by smoothing which
is compatible across all faces.

The regularity property of Botero--Mazzon--Pille-Schneider isolates exactly
the first half of this issue.  Their paper proves it in dimension one and in
some complete or homogeneous conical settings, but does not prove it for an
arbitrary balanced polyhedral space.  Even where piecewise-affine
regularization is available, a comparison with the CLD smooth structure has
to be checked.  The toric theorem avoids this obstruction because BGJKK
construct a boundary-compatible convolution directly on `N_Sigma`.

Therefore the unrestricted atom should not be retired.  The recommended
post-verification book disposition is:

- enlarge the positive-case discussion from Euclidean charts to tropical
  toric partial compactifications;
- add finite boundaryless tropical curves as a second positive class;
- retain the higher-dimensional finite-polyhedral problem and the
  infinite-star/boundary variants as the open remainder.

## Current-literature search status

An arXiv/primary-source search was run on 25 August 2026 for the phrases
`locally approachable`, `localement approchable`, tropical psh smooth
regularization, and CLD hierarchy.  No later source explicitly resolving
the general CLD first-stage problem was found.  The directly relevant new
source was arXiv:2603.08664, whose regularity property is incorporated above
without claiming that it proves the CLD comparison.

## Rethlas verification history

Round 1, run `20260825T022650Z_d1b8d7eaf79e`, checked proof SHA-256
`63d98be6f65dd00ebf56c0ce25e901140012ffa15f325f70e6a97bd8da3fdfb1`
and returned `final/wrong`, with no critical error and two proof gaps.  It
required (i) an explicit interior-edge construction on one fixed open
interval and (ii) a proof that the junction-Jensen class satisfies the
sheaf gluing axiom.  The exact failed proof, statement, request, response,
manifest, item verification, log, and process guards are preserved under
the `p07_cld_hierarchy_toric_curve_round1_gap_` prefix.

Round 2 added the fixed-interval chordal/regularized-maximum proof and the
scaling-and-convexity locality argument.  Run
`20260825T024707Z_d1b8d7eaf79e`, item
`pi_ccfb83de7a7be82ef602cd72`, checked proof SHA-256
`316a774fbb4eda54150b63cae0c9f23a1edab17a75b89beeee6d56d402f8c4a0`
and returned `final/correct`, with zero critical errors, zero gaps, and no
expanded-proof request.  The exact pass artifacts are preserved under the
`p07_cld_hierarchy_toric_curve_round2_` prefix in
`manuscript/editorial/rethlas_receipts_20260825/`.
