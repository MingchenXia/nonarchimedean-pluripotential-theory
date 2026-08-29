# P06.2 proper full-rank moment factor: source and hostile audit

Date: 29 August 2026

Status: **quarantined staging candidate; not a live-book theorem and not yet
production-Rethlas verified.** No novelty or priority claim is made. The
packet does not change P06.2's open status outside the printed factorized
scope.

## Exact packet

- `p062_proper_full_rank_moment_statement_20260829.tex`
- `p062_proper_full_rank_moment_proof_20260829.tex`
- `p062_proper_full_rank_moment_problem_20260829.md`
- `p062_proper_full_rank_moment_compile_20260829.tex`

The principal proposition assumes the constant calibrated identity
explicitly. The automatic-weight statement is a separate corollary. If its
balancing proof fails exact source verification, delete or quarantine the
corollary without weakening the principal proposition.

## Terminal claim and exact scope

Let `K` be complete and nontrivially valued and let `X` be good, separated,
strict, and pure of dimension `n>=1`. A global pleasant moment with exactly
`n` unit coordinates gives

```text
F=(-log|f_1|,...,-log|f_n|): X -> Omega.
```

The hypotheses are:

1. with `Sigma_F^(n):=Sigma_f^(n)`, one has the literal full-image identity
   `Omega=F(X)=Pi_F=F(Sigma_F^(n))`, and this is a nonempty connected open
   subset of `R^n`;
2. `F:X->Omega` is proper in the printed, unambiguous sense that
   `F^{-1}(C)` is compact in `X` for every compact `C subset Omega`;
3. if `mu_Sigma` is the canonical calibration on `Sigma_F^(n)`, then the
   exact direct-image identity is
   `(F|Sigma_F^(n))_*mu_Sigma=mu_F=m|e_1 wedge ... wedge e_n|` on `Omega`.

For `h=phi o F` with `phi` continuous, zero CLD curvature current forces
`phi` affine. Thus `h` is an affine real combination of negative logarithms
of analytic units and is ordinary smooth, real PL, GJR harmonic, and
classically pluriharmonic.

If `X` is boundaryless, the statement is an equivalence: an affine `phi`
gives zero source current by CLD Poincare--Lelong for the unit coordinates
and closedness of the constant integration current. This reverse direction
is deliberately not asserted when `X` has boundary.

No assertion is made for an arbitrary continuous function that does not
factor through this moment, for a singular or lower-rank tropical image, or
for a nonconstant calibrated weight.

Boundarylessness is not a hypothesis of the forward constant-calibration
implication. It appears only in the proposition's explicitly conditional
converse and in the automatic-calibration corollary, where it removes the
exceptional boundary image in CLD Theorem 6.6.8.

## Dependency closure

1. **Current well-definedness.** A continuous function is bounded on the
   compact support of each top-degree test form. CLD §§5.8.5--5.8.6 make
   that form a finite Radon measure, and Corollary 7.2.10 defines `[h]`.
2. **Legal source tests and current pushforward.** For every smooth
   compactly supported Lagerberg form `gamma` on `Omega`, in every
   bidegree, the ordinary smooth pullback `F^*gamma` has support inside
   `F^{-1}(Supp(gamma))`. The printed compact-inverse-image definition of
   properness makes this compact. CLD §7.1.11 therefore defines `F_*` on
   currents with no source cutoff.
3. **Exact constant-multiplicity identity.** For a top-degree test `gamma`,
   CLD Proposition 5.10.1(c),(d) applies to the compactly supported Borel
   top form `phi gamma`; its pullback is used in the Borel-coefficient sense
   of that proposition and is not claimed smooth. The explicit equality
   `mu_F=(F|Sigma)_*mu_Sigma=m e` gives the current identity
   `F_*[phi o F]=m[phi]`, not merely an equality on one selected test.
4. **Differential pushforward.** CLD §7.7.8 gives
   `d'd''F_*[h]=F_*d'd''[h]`. Hence the zero source current and `m>0` imply
   `d'd''[phi]=0` on all of `Omega`. No current is pulled back and no
   equality between a current differential and the current of a form
   differential is asserted.
5. **Euclidean recognition.** Continuity makes `phi` locally Lebesgue
   integrable on `Omega`, hence `[phi]` is defined. CLD §1.6.4 identifies
   the coefficients of `d'd''[phi]` with the distributional Hessian. On
   every convex ball,
   CLD Proposition 8.3.2 makes both `phi` and `-phi` convex, hence `phi`
   affine. Connectedness globalizes the local affine coefficients.
6. **Terminal recognition.** The affine pullback is an ordinary CLD-smooth
   real PL function. GJR Definition 7.2 and Remark 7.3(5),(6) give
   harmonicity directly from the log-unit expression, and GR Proposition
   7.2(2),(3) gives classical pluriharmonicity.
7. **Safe converse.** If `X` is boundaryless, CLD Theorem 16.7.3 gives
   `d'd''[log|f_i|]=delta_div(f_i)=0` because each `f_i` is a unit; CLD
   §7.7.4 makes the constant integration current closed. Thus affine target
   functions give zero source current. Boundarylessness cannot be deleted
   from this reverse implication.

Every node above has a direct consumer in the terminal claim. No curve
pullback, scalar extension, regularization, or real-PL skeletal separation
argument is used.

## Sign ledger

CLD uses `tau=(log|f_i|)`. The packet uses `F=L o tau` for `L=-id` and
defines `F^*alpha=tau^*(L^*alpha)`.

- Equivalently, `F` is the tropical chart of the inverse-coordinate moment
  `(f_1^{-1},...,f_n^{-1})`; an affine isomorphism preserves pleasantness.
- Affine pullback commutes with `d'` and `d''` by CLD §§3.3.11--3.3.12.
- The calibration is an absolute positive vector-volume, so `L_*e=e`.
- In top bidegree, the factor `-1` occurs in both the primed and
  double-primed directions. Hence there is no residual `(-1)^n`.
- The final formula is therefore
  `h=b+sum_i a_i(-log|f_i|)` with no coefficient-sign correction.

## Properness, image, and boundary ledger

- Properness is stated for `F:X->Omega`, not for `F:X->R^n`. This permits
  proper open tropical tubes such as `trop^{-1}(Omega)->Omega`; a proper map
  to all of `R^n` would have closed image.
- `Omega=F(X)=Pi_F=F(Sigma_F^(n))` is literal. If only
  `F(X) subsetneq Omega` were known,
  the current could not constrain `phi` away from the image.
- For every compactly supported target form `gamma`,
  `Supp(F^*gamma) subset F^{-1}(Supp(gamma))`; the explicit
  compact-inverse-image hypothesis makes the pullback a compactly supported
  analytic test form.
- The proof uses CLD's proper current pushforward and its differential
  functoriality, not Stokes. Target tests have compact support inside the
  open target. No boundary term is omitted.
- Boundarylessness is not used by the forward constant-calibration
  implication. It is independently load-bearing in the reverse implication
  and in the
  automatic-weight corollary because CLD Theorem 6.6.8 allows discordance
  over the image of the source boundary.

## Automatic-calibration corollary audit

The corollary uses this additional chain.

1. Pleasantness is explicit before the tropical polyhedron and calibration
   are named, exactly as required by CLD Definition 14.1.7. The affine
   isomorphism `L` makes `F` a pleasant chart in Definition 5.4.3. No
   inference from properness of the topological map `F:X->Omega` to
   properness of the analytic moment is used.
2. Since `X` is boundaryless, CLD Theorem 6.6.8 makes the canonical
   calibrated tropical polyhedron harmonious everywhere.
3. Definition 14.3.5 makes the skeleton calibration standard; Definition
   14.5.1 defines its image calibration and makes that standard; Definition
   4.5.1 makes a standard calibration strictly positive. On a face-to-face
   cellular decomposition of the open full-dimensional target, it is
   `m_C e` on every top cell, with `m_C>0`.
4. At the relative interior of an internal facet, openness supplies two
   opposite local sides. Harmony gives `(m_+-m_-)nu=0`.
5. A generic polygonal path in the connected Euclidean open set avoids the
   codimension-two skeleton and crosses finitely many facets by local
   finiteness. Thus every top-cell weight is one constant `m>0`. CLD Remark
   4.6.10 records the same two-cell discordance propagation calculation.

This is a complete elementary consequence of the cited harmony theorem,
but it is kept separate because it has more moving hypotheses than the
principal constant-calibration argument.

## Primary-source ledger

### Chambert--Loir--Ducros

Primary PDF: `/private/tmp/CLD25_1204.6277.pdf`

SHA-256:
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`

Official source: <https://arxiv.org/abs/1204.6277>

Exact uses:

- §§3.3.11--3.3.12: pullback commutes with `d'` and `d''`;
- §1.6.4: Euclidean currents as forms with distribution coefficients;
- Definition 4.5.1 and Remark 4.6.10: positivity of standard calibrations
  and propagation of weights across harmonious facets;
- Definition 5.4.3 and Definition 14.1.7: pleasant chart/moment;
- Proposition 5.10.1(c),(d): equality of Radon pushforwards and calibrated
  integration for Borel-coefficient top forms;
- §§5.8.5--5.8.6 and Corollary 7.2.10: local integrability and `[h]`;
- Theorem 6.6.8: harmony outside the image of the source boundary;
- §7.1.11 and §7.7.8: proper current pushforward and commutation with
  `d'`, `d''`;
- §7.7.4: closedness of the integration current on a boundaryless space;
- Remark 7.8.3: the general continuous zero-current recognition problem is
  not known even in the abstract tropical setting;
- Proposition 8.3.1: CLD-psh implies positive current, with converse stated
  there only for smooth functions;
- Proposition 8.3.2: on Euclidean convex opens, local integrability plus
  positive Hessian current is equivalent to finite convexity;
- Definition 14.3.5, Definition 14.5.1, §14.5.2, and Proposition 14.5.3:
  canonical positive calibration and its local-degree description;
- Proposition 14.4.2: finite-map calibration, used only for the example
  below.
- Theorem 16.7.3: Poincare--Lelong, used only for the boundaryless converse.

### Gubler--Jell--Rabinoff

Primary PDF: `/private/tmp/GJR_2111.05741.pdf`

SHA-256:
`572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42`

Official source: <https://arxiv.org/abs/2111.05741>

- Definition 7.2 and Remark 7.3(5),(6) show directly that real linear
  combinations of logarithms of analytic units are GJR harmonic.
- Corollary 7.15 is only the direction harmonic implies zero CLD current on
  the boundaryless locus; the packet proves that same safe reverse direction
  here instead from CLD Poincare--Lelong, and never uses it as a converse for
  arbitrary continuous functions.
- Proposition 15.7 identifies GJR and Thuillier harmonicity on rig-smooth
  curves, but is not needed for the higher-dimensional proposition.

### Gubler--Rabinoff

Primary PDF: `/private/tmp/GublerRabinoff_2506.13548.pdf`

SHA-256:
`83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`

Official source: <https://arxiv.org/abs/2506.13548>

- Definitions 4.1 and 7.1 give classical psh and pluriharmonicity.
- Proposition 7.2(2),(3) makes logarithms of units pluriharmonic and the
  pluriharmonic functions a real vector space.
- Proposition 7.8 proves PL regularity only under a strictly semistable
  formal-model hypothesis; the paper explicitly leaves unrestricted
  pluriharmonic-to-PL regularity open.

### Wanner and Thuillier curve scope

Wanner source archive: `/private/tmp/wanner180104713v3.tar`

SHA-256:
`041d4032e4dba67dc8677981a0f40ac0230ad3404460ea05bd22f7e86d641686`

Official source: <https://arxiv.org/abs/1801.04713>

Wanner Theorem 4.7 and Corollary 4.8 recognize continuous current-psh
functions on smooth proper algebraic curves over algebraically closed
complete nontrivially valued fields. They do not cover the general
higher-dimensional problem.

Thuillier thesis PDF: `/private/tmp/Thuillier_thesis.pdf`

SHA-256:
`fc947ea783e4680741ec23d6b9586f69e17081b9fc3b0a8d507ca9f7a3eb7a1c`

## Internal verified and quarantined scopes

- The live real-PL zero-current result is controlled by production run
  `20260825T061351Z_655e7f503e5d`. It does not apply before affinity or PL
  regularity has been recovered.
- Recent P21.3 packets classify positive closed `(0,0)` currents and prove
  Bedford--Taylor independence for **continuous CLD-psh pairs** in stated
  curve scopes. They cannot be read as a converse from positive curvature
  current to CLD-psh membership. An arbitrary continuous `h` with zero
  current is therefore not covered merely because the zero current is
  positive for both signs.
- The moment-factor proof consumes CLD Proposition 8.3.2 only after it has
  legally transported the current equality to a Euclidean open set. This is
  the essential recognition bridge.

## Hostile counterexample checks

### Singular cross target

On the four-ray cross with unit weights, the continuous function

```text
h(s,0)=|s|,     h(0,t)=-|t|
```

has zero balanced tropical current but is not the restriction of one
ambient affine function. The cross is not open in a one-dimensional affine
space. In the book's analytic cross realization, the horizontal and
vertical curvature atoms lie at distinct points upstairs, so the analytic
current is not zero. Thus neither version contradicts the proposition; the
test shows that the full-open-rank hypothesis is essential.

### Variable calibration

On `Omega=(-1,1)`, assign weight `w=1` for `x<0` and `w=2` for `x>0`, and
put

```text
phi(x)=x       for x<=0,
phi(x)=x/2     for x>=0.
```

Then `w phi=x`, so `integral w phi alpha''=0` for every compactly supported
smooth test function `alpha`, although `phi` is continuous and nonaffine.
This calibration is not harmonious at zero. It shows that constant weight,
or the exact boundaryless harmony argument in the corollary, is
load-bearing.

### Image not equal to target

If `F(X) subsetneq Omega`, choose a continuous `phi` that vanishes on
`F(X)` but is nonaffine elsewhere. Then `h=0` has zero current and says
nothing about `phi` off the image. This is why the statement prints
`Omega=F(X)=Pi_F`.

### Disconnected target

Different affine coefficients may occur on different components. The proof
still works componentwise, but connectedness is required for the one-formula
conclusion printed in the proposition.

### Nonproper chart

Without properness, the pullback of a compactly supported target test form
need not have compact support upstairs. Multiplying it by a cutoff changes
its `d'd''` and introduces uncontrolled terms. The present proof gives no
claim in that scope.

### Theta-curve approximation obstruction

The live theta-curve example rules out ordinary-smooth harmonic
approximation of every weakly smooth harmonic function. It does not
contradict the present proposition: here ordinary smoothness follows from
the recovered explicit affine formula, not from an approximation theorem.

## Nonvacuous examples

1. Let `X=F^{-1}(Omega)` in the split analytic torus, where `F=-trop` and
   `Omega` is a connected open polyhedral subset of `R^n`. Standard
   tropicalization is proper over compact subsets of `Omega`, the tropical
   polyhedron is `Omega`, and the calibration is `e`.
2. If `Y->X` is a finite flat cover of constant degree `d`, pull back the
   torus coordinates and compose with `F`. The resulting map remains proper
   onto `Omega`, and CLD Proposition 14.4.2 gives calibrated weight `d`.

These examples are higher-dimensional when `n>=2` and do not use the
already known curve or real-PL recognition theorems to obtain affinity.

## Literature verdict and production gate

The audited primary sources and targeted searches through 29 August 2026
revealed no theorem or analytic counterexample settling unrestricted P06.2
in higher dimension. CLD Remark 7.8.3 directly records the analogous
general tropical uncertainty. The correct status is therefore:

- unrestricted arbitrary continuous P06.2: **open**;
- real-PL and weakly smooth scopes: already known/verified as recorded in
  the live book;
- published Wanner curve scope: known under its exact hypotheses;
- present proper full-rank calibrated factor scope: **staging candidate**.

Before promotion, freeze exact hashes of the statement and proof, submit
those exact bytes with this source ledger to production Rethlas, require a
`correct` verdict with zero critical errors and zero gaps for the principal
proposition, record a separate verdict for the corollary, archive all
request/response/service evidence, and run an independent hostile audit.
Until then, do not cite this packet as established and do not edit Chapter
72 or the atomic inventory.
