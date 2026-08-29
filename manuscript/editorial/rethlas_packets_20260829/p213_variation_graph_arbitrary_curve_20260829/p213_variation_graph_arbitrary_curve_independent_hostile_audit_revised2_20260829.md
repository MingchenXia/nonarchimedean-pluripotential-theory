# Independent hostile audit of the second-revision arbitrary-valued curve packet

Date: 29 August 2026  
Auditor: independent read-only audit  
Disposition: quarantine only; no live-book edit and no Rethlas submission

## Verdict

**FAIL for the exact second-revision packet: 0 critical errors and 1
mathematical proof gap.**

The gap is confined to the auxiliary quasi-smooth-locus dichotomy.  The
retained core consisting of the source-cutoff lemma, the Euclidean
one-dimensional-current lemma, and the normal-curve current-classification
proposition passes this hostile audit with **0 critical errors and 0
mathematical gaps**.  This split verdict does not make the exact packet
production-ready: every statement in the submitted packet must be proved, so
the exact second-revision bytes remain rejected and must not be integrated or
submitted to Rethlas.

## Exact bytes audited

- Statement:
  `p213_variation_graph_arbitrary_curve_statement_revised2_20260829.tex`
  
  SHA-256
  `e2fdfcc73d777f2cc34f36f3f9c0b6ef7872bcfe35c23a7a7dd83c26422e8695`.
- Proof:
  `p213_variation_graph_arbitrary_curve_proof_revised2_20260829.tex`
  
  SHA-256
  `ef986f039dd53c5fe146e3d7d9824c62570a41d32451a1b7c07b9e6a09eaa0c6`.
- Dependency-closed compile harness:
  `p213_variation_graph_arbitrary_curve_compile_revised2_20260829.tex`
  
  SHA-256
  `67bc64efb050ee48233f8d23ecf68b8d6006bf51593518891dcd7604a45b3738`.
- Freshly compiled PDF:
  `p213_variation_graph_arbitrary_curve_compile_revised2_20260829.pdf`
  
  SHA-256
  `2d9f5f451574c8604455fe7a546b4fca3dabb910bda292d813cd3a6c4d80b20a`.
- Candidate source audit:
  `p213_variation_graph_arbitrary_curve_source_audit_revised2_20260829.md`
  
  SHA-256
  `2ec339b1caee943dd49b4772530c837eb07d2dadc0bb99aacfdc22aa12df64c2`.

The frozen CLD and Ducros source copies independently consulted have SHA-256
hashes

- CLD25: `f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`;
- Ducros curve structure:
  `b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`.

## Independent compilation

The exact harness was rebuilt with `latexmk -pdf -interaction=nonstopmode
-halt-on-error`.  It produced an eleven-page, 250443-byte PDF.  The final log
contains no TeX error, undefined citation, undefined reference, or duplicate
label.  It contains only two harmless overfull boxes, of 0.55191pt and
4.6854pt.  The rebuilt PDF has the exact hash recorded above.

## Hostile audit of the retained core

### 1. Hypotheses, slope convention, and source separation: pass

The source-cutoff statement has the hypotheses actually used: completeness of
the ground field, goodness and separatedness for compact smooth cutoffs,
normality for the nonrigid local-field identity, pure dimension one for the
curve graph, and boundarylessness for the normalized node relation.  It is
restricted to type--2 and type--3 points and to ordinary CLD moments and
currents, so it does not silently claim the weakly smooth theory.

Proof lines 8--24 correctly distinguish the normalized integral slope
`dlog_b |f| = epsilon r [s(b):K]` of Ducros 4.5.21.4 from the canonical-metric
derivative `epsilon r`.  Lines 103--146 use the normalized integer slope only
for the lattice and primitive target ray; the residue-degree factor cancels
from the direction and is not later substituted for the analytic
calibration.

At a type--2 point, lines 43--157 construct first-order residual functions at
the finitely many branches on which the initial moment varies.  The two jet
blocks have the required effect: the first gives a named standard coordinate
on each selected primitive ray; the second marks every extra zero or pole of
the first block.  A source branch activated only by the initial moment has
zero separator block.  Hence a selected ray cannot collide with another
source ray.  At a type--3 point, lines 158--167 use a non-torsion modulus and
the two-branch node relation to separate the two rays.  The statement properly
claims separation of ray germs, not an unjustified global description of a
ray's inverse image.

### 2. Nonnegative compact source cutoff and closed pushforward: pass

CLD Corollary 15.2.5 supplies the compactly supported smooth plateau `psi`
used at lines 179--181.  Lines 182--190 then postcompose it with a scalar
smooth function `rho:R->[0,1]` which is zero near zero and one near one.  Thus
`chi=rho composed with psi` is genuinely smooth, satisfies `0<=chi<=1`, is
one near the source point, and has support contained in the compact support of
`psi`; no unstated sign property of `psi` is needed.

The derivative support is compact and avoids the source vertex.  Injectivity
on each sufficiently short active arm makes its tropical image avoid the
target vertex.  Lines 207--227 correctly use compact-support pushforward from
CLD 7.1.11 and the current Leibniz rule.  On the variation graph the target
test form misses the derivative support, while off that graph the moment is
locally constant and pulls every positive-degree target form back to zero.
This establishes both closedness equations on the target germ without a
global properness or target-tube assertion.

### 3. Euclidean edge decomposition and balance: pass

Positivity gives order zero, so on a finite coordinate ball the current is a
positive-semidefinite matrix of Radon measures.  The column-divergence
equations at lines 244--249 are the local form of `d'R=0`.  The normal-linear
tests at lines 251--258 kill every normal row and column; the remaining
tangential measure has zero one-variable distributional derivative and is a
constant nonnegative multiple of primitive edge integration.

After these edge currents are removed, positivity leaves a
positive-semidefinite matrix atom at a vertex.  Its derivative-of-Dirac part
and the Dirac boundary contributions of the incident edges are linearly
independent.  Lines 264--277 consequently kill the vertex atom and give the
primitive-vector balance relation.  Local finiteness makes the resulting edge
sum legitimate.

### 4. Actual calibration and the inseparable stress test: pass

Lines 294--313 define `m_b(F)` as the **actual** coefficient of the
integration-current pushforward and expressly refuse to identify it with the
normalized slope gcd `q_b(F)`.  This is the needed calibration correction.
CLD Proposition 14.3.1, Section 14.3.2, and Definition 14.5.1 give positivity
of the canonical local degree.  CLD Remark 14.4.3 says that when an
`F`-analytic space is viewed over `K`, the canonical calibration is multiplied
by `[F:K]`.

The printed test case is therefore calibrated correctly.  For
`K=F_p((t))`, `L=K(t^(1/p))`, and the coordinate moment on a type--3 segment
of `A^1_L`, the normalized primitive slope is one, whereas the same space
viewed over `K` has integration-current edge coefficient multiplied by
`[L:K]=p`.  Hence `q_b(F)=1` and `m_b(F)=p`.  The intrinsic quantity
`t_b(F)/m_b(F)` retains the inseparable factor instead of silently erasing it.

### 5. Refinement functoriality of the actual edge weights: pass

For a common refinement `H` and target projection `A`, lines 323--329 give
`A u_b(H)=r u_b(F)`, with positive integral expansion
`r=q_b(F)/q_b(H)`.  Direct pullback of a `(1,1)`-form and change from the
primitive `H`-parameter to the primitive `F`-parameter give
`A_*[u_b(H)]=r[u_b(F)]`; this is the correct factor, rather than `r^2` or
one.

The already-separated `F`-ray excludes any other noncollapsed source branch
from projecting onto it.  Rays collapsed by `A` pull positive-degree target
forms back to zero.  Compact-support pushforward functoriality thus yields
both equalities at lines 334--337,

`t_b(F)=r t_b(H)` and `m_b(F)=r m_b(H)`.

Their quotient is refinement-invariant.  Lines 343--350 also give a valid
germ argument for cutoff independence for both currents: the difference of
two common cutoffs vanishes near the source vertex, its active-arm image is
bounded away from the target vertex, and its off-graph pullback is zero.

### 6. Type--2 calibration weights and divisor functionals: pass

For a residual closed point `P`, a moment containing a lift of a residual
uniformizer has every normalized coordinate slope divisible by `d_P` and one
coordinate of slope exactly `d_P`.  Its gcd is therefore exactly `d_P`.
The same remains true after any common refinement containing that
uniformizer.  Thus the projection expansion integer is one, and lines
360--374 correctly make the **actual** integration coefficient `m_P>0`
intrinsic without asserting an unsupported formula in terms of `d_P` or
`deg(P)`.

In the common moment at lines 386--405, the primitive coordinate belonging to
a residual rational function `g` is `ord_P(g)`.  Vertex balance for `T` and
for the integration current gives, respectively,

`sum_P a_P m_P ord_P(g)=0` and `sum_P m_P ord_P(g)=0`.

Consequently both displayed divisor functionals are additive, nonnegative on
effective divisors, and zero on principal divisors.

The Riemann--Roch step at lines 407--425 is valid over the actual constant
field and does not require geometric integrality or a rational point.  For a
degree-zero divisor `D`, choose an effective `A` with
`deg(A)+chi(O_C)>0`.  Riemann--Roch gives a section of `A+nD` for every
positive and negative integer `n`; nonnegativity then forces `L(D)=0`.
Thus each functional is a constant multiple of degree on the subgroup of
degrees occurring on `C`.  Positivity of every `m_P` makes the integration
constant positive, so division proves that all branch ratios at the type--2
point agree.

### 7. Curvature/current identification and spatial propagation: pass

Lines 439--459 test against an arbitrary sufficiently local ordinary smooth
top-degree form.  Appending the separator preserves its original moment
representative.  Rays activated only by the separator have zero tangent in
the original coordinates and hence make no contribution; the Euclidean
lemma rules out a target-vertex current.  This gives the claimed local current
equality.

Lines 467--492 supply the previously needed explicit overlap propagation.
One fixed separated varying moment and one plateau cutoff work on a compact
source edge segment.  Both the given current and the integration current have
separately constant coefficients on the connected target edge, so their
quotient is locally constant.  The type--2 and type--3 star arguments identify
incident ratios, and a finite cover of a path in the connected type--2/3 core
globalizes the constant.

Ordinary compactly supported `(1,1)`-forms are supported on that core by the
cited CLD local-presentation and dimension results.  A finite smooth partition
of unity therefore upgrades the local identity to `T=c delta_Y`.  CLD Example
8.6.4 supplies the Bedford--Taylor property of the integration current, and
nonnegative scalar multiplication preserves its defining identity.  The
conclusion is exactly about ordinary currents, as stated.

## The one proof gap in the exact packet

**Location:** statement lines 86--100 and proof lines 505--521, specifically
proof lines 510--514.

The proof argues that a zero-dimensional proper closed analytic subspace is
finite on every strict affinoid domain and invokes Tate's strict-affinoid
Nullstellensatz, then says these descriptions prove local finiteness and
rigidity.  Under the strict-germ convention used by CLD over a trivially
valued ground field, however, strict affinoid domains do not form a local
cover.  CLD 11.8.1 explicitly broadens “strict” in the trivially valued case,
and CLD Remark 11.8.4 exhibits the strict open annulus `0<|T|<1`, which has no
nonempty compact strict analytic domain.  The strict-affinoid
Nullstellensatz therefore cannot be localized at an arbitrary point by the
argument printed at lines 510--514.

This audit does not assert that the dichotomy statement is false.  It records
the narrower and decisive defect: the exact proof has not established the
implication “strict zero-dimensional analytic germ implies rigid” in the
absence of a compact strict representative.  Deleting the auxiliary
dichotomy and its dependent example would remove this defect from the core
classification packet; repairing it while retaining the statement would
require a separate germ-level argument or an explicit stronger strictness
hypothesis.

The example at statement lines 102--110 and proof lines 523--542 is itself a
correct inseparable example: `Omega^1_{L[T]/K}` has independent generators
`d alpha` and `dT`, hence fibre rank two while the curve dimension is one, so
the curve is nowhere quasi-smooth over `K`.  It does not repair the missing
local argument in the first alternative of the dichotomy.

## Final gate disposition

- Exact revised2 packet: **FAIL — 0 critical errors / 1 mathematical gap**.
- Retained classification core (statement lines 7--84; proof lines 8--503):
  **PASS in this independent audit — 0 critical errors / 0 mathematical
  gaps**.
- Rethlas submission of the exact revised2 bytes: **not authorized or
  recommended**.
- Live integration or P21.3 retirement on the basis of these exact bytes:
  **not authorized or recommended**.

