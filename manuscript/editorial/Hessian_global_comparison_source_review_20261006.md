# Hessian domination, local comparison and approximation: source review

Recorded 6 October 2026. Baseline: `c3103322c67aab61c71a4d762c28643839688d04`.
This is a source-only continuation of the
[bounded regularity audit](Fang_Hessian_bounded_regularity_source_review_20261006.md).
No active TeX, canonical problem status or general Siu/closure boundary changes.

## Decision and exact reading scope

The continuous global Hessian domination input has a directly located
primary proof. It does not alone prove continuity of an arbitrary
bounded solution. The older local bounded theory distinguishes a
locally conformal Kähler reference metric from a general Hermitian
metric, while its smooth approximation theorem has a broader scope.
The Monge--Ampère background comparison proof uses positivity of
psh currents and cannot simply be relabelled as an intermediate Hessian
proof. These distinctions narrow the remaining application checks for
Fang's new bounded regularity preprint; they neither refute its main
conditional assertion nor complete an independently certified repair.

Read and displayed **44 physical research-text pages in 23 sheets**:

| Source and exact edition | Acquired PDF | Actual pages read and displayed | Scope |
| --- | --- | --- | --- |
| Guedj--Lu, *Degenerate complex Hessian equations on compact Hermitian manifolds*, `2302.03354v1`, submitted 7 February 2023, 09:55:38 UTC | 15 pages | 1--15 | Complete preprint, including references |
| Boucksom--Guedj--Lu, *Volumes of Bott-Chern classes*, `2406.01090v1`, submitted 3 June 2024, 08:18:34 UTC | 33 pages | 1--4, 28--29 | Six selected pages; no full-paper or full nonpluripolar construction review |
| Gu--Nguyen, *The Dirichlet problem for a complex Hessian equation on compact Hermitian manifolds with boundary*, published Ann. Sc. Norm. Super. Pisa (5) XVIII (2018), 1189--1248 | 60 pages | 1--17, 50--53 | Twenty-one selected pages, printed 1189--1205 and 1238--1241 |
| Kołodziej--Nguyen, *Weak solutions of complex Hessian equations on compact Hermitian manifolds*, `1507.06755v2`, submitted 10 March 2016, 11:24:27 UTC | Previously acquired 27-page preprint | 12--13 | Two additional pages; the preceding selected reading record remains frozen |

The initial plan covered forty pages and twenty-one sheets. Two additional
sheets contain Gu--Nguyen actual 7--8 and Kołodziej--Nguyen actual 12--13.
Only the fifteen-page Guedj--Lu preprint is freshly read in full. No
publisher cover occurs in this selection. Every listed page was displayed
and its full extracted text read. Gu--Nguyen's extraction has badly mapped
symbols despite empty extraction diagnostics; the displayed PDF controls
the powers, inequalities and differential convention.

The attempted Guedj--Lu publisher PDF returned HTTP 403 without a PDF.
The publicly accessible arXiv v1 was then acquired successfully. Its
fifteen pages are not the twenty-four pages of the 2025 journal edition;
no journal-proof identity or journal-page review is claimed. The other
two fresh acquisitions returned HTTP 200 with unchanged final URLs.
Gu--Nguyen's arXiv v4 was located as metadata only and was not downloaded;
all Gu--Nguyen proof locators here use the acquired published edition.

The exact acquisition and reading records are cached under
`source_material/Hessian_global_comparison_review_20261006/`:

- `acquisition_v1_20261006.json` records attempts, editions, URLs, HTTP results, PDF and extraction hashes; it remains a historical acquisition record with false reading flags.
- `selected_reading_v1_20261006.json` freezes the forty-page reading and its twenty-one displayed sheets.
- `supplement_reading_v1_20261006.json` freezes the four supplementary pages and two sheets.
- `literal_diagnostics_v1_20261006.json` records the four narrow checks below.

The separate preparation records retain their original false reading
flags. The accompanying tracked manifest pins the completed records,
displayed sheets, actual PDFs, extracted texts and preservation baseline.

## Continuous global domination in Guedj--Lu

The paper fixes a compact complex manifold, a reference Hermitian form
`omega_X`, and Hessian order `1 < k < n`. The background `omega` is
semipositive and big in the main degenerate existence statement.
The operator is
`H_k(u) = (omega + ddc u)^k wedge omega_X^(n-k)`.
The reference metric remains part of both admissibility and the operator.
Section 1.2.1, actual 5--6, defines the general Hermitian Hessian measure
for **continuous** admissible potentials using smooth decreasing
approximation and uniform convergence. The text explicitly describes
the merely bounded case as delicate. This edition predates the later
bounded Hermitian operator construction.

Theorem 1.7, actual 4--5, proves global smooth decreasing approximation
for a Hermitian background. Its penalized obstacle argument solves
`H_k(phi_j) = exp(j(phi_j-u)) f` for a fixed smooth obstacle `u` and a
smooth positive density dominating its smooth Hessian. At a maximum
against `(1+1/j)phi_j`, the mixed linear elliptic test and Gårding
inequality give an error of order `log(j)/j`, establishing uniform
convergence to the smooth-obstacle envelope. The positive background
and fixed smooth obstacle are used in this step; it is not a uniform
smooth approximation to an arbitrary discontinuous bounded potential.

Definition 1.8 and Proposition 1.9, actual 6, define the degenerate
operator for bounded potentials continuous on the smooth locus of a
strictly positive analytic-singularity barrier. The measure is extended
by zero across its complement. Uniform continuity of the operator and
Lemma 1.10's maximum/contact inequalities are then used in the envelope
arguments. The contact-support and regularity results collected in
Section 1.2.3, actual 7, are cited imports; their original external proofs
are not freshly read by this checkpoint.

Theorem 2.1, actual 8, gives positive total Hessian mass for a bounded
admissible potential continuous on the barrier's smooth locus. Its
proof compares with a maximum against the strictly positive barrier
on a compact small sublevel set and controls the nonclosed terms.
The displayed difference-of-powers expansion has a literal degree
error, recorded below. The ordinary difference identity supplies the
correct algebra; this observation does not certify every antecedent
estimate in the proof or refute positive mass.

For **Hermitian** background and **continuous** potentials, Theorem 2.2
and Corollaries 2.3--2.4, actual 9, establish:

1. `H_k(u)=0` on `{u<v}` implies `u>=v`.
2. `H_k(u)<=c H_k(v)` on `{u<v}`, with one constant `0<=c<1`, implies `u>=v`.
3. `exp(-v)H_k(v)>=exp(-u)H_k(u)` implies `u>=v`.

The first proof uses `P_(omega,k)(b u-(b-1)v)`, positive total mass,
contact support, and compactness of normalized admissible functions.
The contact inequality forces a contact point with `u=v`, which
prevents the decreasing envelopes from converging identically to
minus infinity. If `{u<v-a}` were nonempty, continuity would make it
an open set on which the limit is minus infinity, contradicting local
integrability. The second proof chooses `(1-1/b)^k>=c` and reduces to
zero Hessian on the relevant contact sublevel. The third applies the
second on `{u<v-a}` with the **uniform** factor `exp(-a)<1`, then lets
`a` decrease to zero. This supplies the sublevel-gap step omitted in
the literal wording of the new preprint's analogous corollary.

Theorem 3.1 and Theorem 3.3, actual 10--12, give a priori oscillation
and stability estimates. Their inputs include fixed geometry,
`p>n/k`, controlled density norms and the relevant lower/upper
potential bounds. The stability proof constructs a positive psh
Monge--Ampère perturbation and uses the exponential comparison.
When following it, keep the Hessian reference form fixed: its sentence
changing that form to a dominating Gauduchon metric cannot be interpreted
as invariance of an intermediate Hessian operator. A separate auxiliary
Gauduchon form and its volume comparison constants can be used for the
Monge--Ampère mass estimate; no all-background uniform constant is
claimed here beyond the source's stated and checked application inputs.

Actual 12--13 constructs solutions to `H_k(phi)=c f omega_X^n`, with
`f>=0`, `f` in `L^p`, `p>n/k`, and positive integral. Smooth positive
density and positive-background approximants have normalization constants
bounded away from zero and infinity. Stability gives local uniform
convergence on the barrier's smooth locus. This constructs a continuous
solution there; it does not establish continuity of every preassigned
bounded solution of the same equation. Remark 3.4 explicitly separates
global continuity at degenerate points and uniqueness without an
exponential. The constants `c` are not discarded by importing a Kähler
fixed-mass normalization into a nonclosed setting.

The source convention, explicitly stated on actual 2, is
`ddc_source=2i partial barpartial`. With the book's
`ddc_book=i/(2pi) partial barpartial`, a book potential `phi` corresponds
to source potential `phi/(4pi)` when the background forms are retained.
A dependence on the potential must be composed with that conversion.
This is distinct from the new Fang paper, which does not explicitly
restate a differential convention.

## Local background comparison in Boucksom--Guedj--Lu

The six selected pages identify a different operator and function class.
The paper treats quasi-closed quasi-positive currents and the
Monge--Ampère operator `(theta+ddc u)^n` on **theta-psh** potentials.
The global nonpluripolar construction in Theorem A assumes the bounded
mass property. Section 4, actual 28, explicitly drops that global
property and works on the smooth locus of a big analytic barrier;
the two scopes are not conflated.

Lemma 4.1, actual 28, treats bounded theta-psh potentials on a coordinate
ball with the appropriate boundary order. Its proof replaces `v` by
`max(u,v-epsilon)`, takes a psh envelope of the bounded difference,
and uses the contact measure inequality and the ordinary psh
Bedford--Taylor comparison. Positivity of the two `(1,1)` currents
allows the added psh current's top-degree measure to be controlled.
The maximum/contact input cites Proposition 2.11, outside this selected
scope; a fresh proof of that antecedent is not claimed. One display
immediately after the maximum inequality writes `v` where the subsequent
argument uses `v_epsilon`; the proof must retain the maximum potential.

Lemma 4.2, actual 28--29, gives global domination with a factor strictly
less than one, a common analytic lower barrier and an upper bound on
`v-u`. Its proof perturbs `v` toward the barrier, then adds a small
coordinate bump at a minimizing sequence to invoke Lemma 4.1. It
does not require continuity of the bounded differences at the limit
point. Corollary 4.3 retains bounded difference and the common lower
barrier before deducing that a global constant comparing the two
Monge--Ampère measures cannot be less than one.

These selected results support the **Monge--Ampère** auxiliary argument
already scoped in Chapter 68.9.4. A function that is only
`(omega,omega_X,k)`-subharmonic for `k<n` need not be psh. Its Hessian
current need not be positive as a `(1,1)` current. Transferring this
envelope proof therefore requires the intermediate Hessian mixed-current
and contact-measure inputs in their exact bounded background class;
the Monge--Ampère proof itself does not supply them.

The introductory higher regularity and uniqueness questions on actual 4
are the authors' 2024 questions, not newly added or solved canonical
problems. Their hypotheses are not identified with every later
semipositive or prescribed bounded-solution regularity theorem.

## Gu--Nguyen's published local theory and its broader approximation

The paper distinguishes the reference Hermitian form `alpha` and a
general real background `(1,1)` form `chi`. Definitions 2.1--2.4,
printed 1191--1192 (actual 3--4), use canonical subharmonic
representatives for every mixed linear elliptic test. The background
term is removed from each individual linear test by solving a smooth
linear equation; this is not an assertion that the form `chi` has
a local scalar potential. Distributional positivity alone must be
accompanied by the canonical representative. Corollary 9.7 and
Lemma 9.10, printed 1238--1239 (actual 50--51), explain equality
almost everywhere and the unique subharmonic representative.

Section 3, printed 1194 (actual 6), fixes a ball on which
`omega=exp(G)alpha` is Kähler. It defines the mixed operator for
bounded locally smooth-decreasing-approximable potentials using
this closed reference form and a smooth remainder
`tau=ddc varphi-chi`. Printed 1195--1196 (actual 7--8) expands the
products and proves monotone continuity. The expansion's printed
`n-k` power of `tau` must be `m-k`, as the degree check below shows.
Remark 3.2 explicitly explains why the same inductive definition is
not automatically available for bounded potentials and an arbitrary
nonclosed reference form. The later published 2026 construction is
a separate source, already selected in the preceding Fang review.

Lemma 3.8, printed 1197--1198 (actual 9--10), retains an integration
by parts error involving `ddc T`. Its preliminary display that removes
all derivatives of the `chi_v` factors is false for nonclosed `chi`,
even when `G=0`; the explicit smooth test below records that identity
only. Lemmas 3.9--3.10, printed 1199--1200 (actual 11--12), subsequently
retain torsion bounds for **both** `alpha` and `chi`. One may not drop
the background derivative terms when applying these estimates.

Corollary 3.11, printed 1200 (actual 12), gives the local comparison
`H(u)<=H(v)` and boundary `u>=v` implying interior `u>=v`, in the
Section 3 bounded approximable class and reference setting. Its proof
refers to an earlier comparison argument rather than reproducing all
details. Lemmas 3.13--3.17, printed 1201--1203 (actual 13--15), use
this comparison and positive psh perturbations for local stability,
Dirichlet solutions and positive-exponent solutions. Their geometry
and background constants remain part of the application, including
the metric dependence visible in the stability proof.

Theorem 3.18, printed 1204--1205 (actual 16--17), establishes local
smooth decreasing approximation by penalized envelopes of smooth
obstacles. **Remark 3.19(a)** extends that theorem to a general
Hermitian metric, because its measure computations use continuous
potentials. It instructs the reader to use a counterpart of
Kołodziej--Nguyen Theorem 2.16 in the last maximality step, instead of
Corollary 3.11. This broader approximation scope is not an assertion
that every preceding bounded comparison proof has the same broader
scope. Section 4, actual 17, repeats the locally conformal Kähler
assumption for its bounded potential theory.

The two additional Kołodziej--Nguyen v2 pages contain the cited
Theorem 2.16, Lemma 2.17, their complete local proofs and Remark 2.18.
Theorem 2.16 permits a bounded admissible competitor `v`, but its
zero-Hessian potential `u` is continuous and the uniform limit of
smooth admissible functions. Its proof tests the nonsmooth competitor
against smooth mixed linear elliptic forms, keeps the torsion variation
and successively forces lower Hessian degrees down to the strictly
positive reference volume on a small sublevel. This is the required
asymmetric maximality input for the smooth-obstacle approximation
argument; it is not a symmetric global domination theorem between
arbitrary bounded potentials. The background there is the same
reference form `omega`. Remark 2.18 states a compact-manifold extension
with modifications, not a separately reproduced proof for every pair
of reference and background forms.

Gu--Nguyen's explicit convention on actual 4 is
`ddc_source=i/pi partial barpartial`. Its source potential is half
the book potential for the retained forms. Neither this convention
nor Guedj--Lu's distinct convention is silently assigned to Fang's
new paper. Conformal rescaling preserves the pointwise admissibility
cone, but multiplies the reference powers in the measure; the
appropriate density factor is retained.

## Four narrow literal checks

All four checks use displayed primary pages and smooth exterior algebra.
They are formula or application-scope checks, not counterexamples to
the cited main existence, comparison or regularity theorems.

1. **Gu--Nguyen (3.5), actual 7:** for dimension three and Hessian order
   two, every summand with the printed `tau^(n-k)` has bidegree `(4,4)`
   and vanishes. With `alpha=chi=beta=ddc|z|^2`, zero potentials and
   `varphi=2|z|^2`, the left side is the positive measure `beta^3`.
   The binomial sign and power are `m-k`.
2. **Gu--Nguyen `ddc T` display, actual 10:** take dimension three,
   order two, `alpha=beta`, `G=0`, `chi=(1+|z1|^2)beta`, and `v1=0`.
   Then `T=chi wedge beta` and `ddc T=(1/3)beta^3>0`, whereas the
   printed expression containing only `ddc exp((m-n)G)` is zero.
   The later torsion estimates are not refuted by this identity test.
3. **Guedj--Lu's difference expansion, actual 8:** locally choose
   dimension three, order two, `j=0`, `omega=omega_X=beta`, `u=0` and
   `phi=|z|^2`. The left difference is `3 beta^3`; the printed right
   side has bidegree `(4,4)`. The correct general sum has upper limit
   `k-j-1` and includes the factor `omega_u^j`.
4. **Reference-metric scope, Guedj--Lu actual 11:** in dimension three
   and order two, the diagonal form `(0,1,1)` wedged twice with
   reference `(1,1,1)` gives `1/3` of its volume, while reference
   `(2,1,1)` gives `2/3` of the original volume. Both reference forms
   are closed. Changing the Hessian reference therefore changes the
   operator, even between Gauduchon metrics. An auxiliary mass-bound
   metric is distinguished from the fixed Hessian reference.

## What the new reading resolves, and what remains

The full Guedj--Lu reading supplies the original continuous global
domination and the uniform strict-sublevel factor for exponential
comparison. The additional Kołodziej--Nguyen pages identify the precise
maximality input behind general Hermitian smooth approximation.
Gu--Nguyen's published version now supplies the exact distinction
between the bounded locally conformal theory and the broader continuous
approximation theorem. The selected Boucksom--Guedj--Lu proof explains
the background Monge--Ampère comparison already relevant to the book.

For admitting a passage from Fang's new paper, retain separate checks:

- An arbitrary given bounded Hessian solution must first be continuous,
  using the exact later bounded operator, local comparison and global
  domination in its background class; construction of a continuous
  solution alone is insufficient.
- The positive-exponent auxiliary equation must have uniform estimates
  and convergence in the required class. Its limit is compared on
  strict sublevels with a uniform factor; a frozen approximation must
  actually converge to the prescribed potential.
- The specialized second-order estimate must retain the chosen
  differential convention, symmetric-polynomial normalization,
  linearization weights and the fixed smooth approximation bound.
  The apparent extra mixed-term factor cleared in the preceding audit
  remains cleared.
- Liouville blow-up and Hölder regularity use their own hypotheses.
  The original equation may have arbitrary smooth dependence on its
  unknown; positive-coefficient uniqueness of its auxiliary equation
  does not imply uniqueness or unconditional existence of the original.

A suitable next book passage can explain continuous Hessian domination
and conditional auxiliary identification from known inputs. It must
not promote the entire new bounded Hermitian smoothness proof until
the remaining class and estimate checks are reconciled.

## Preservation and validation

The companion manifest verifies the 5,047 tracked-file baseline and
the two edited progress files, while preserving all 425 active inputs,
108 protected inputs, 62 prior frozen manifests, 118 prior exports,
the checked 4,392-page book and all generated book files. All 42
complete canonical problem statuses, the native catalogue source/PDF,
and the BJ22 Theorem 6.21 proof-gap qualification retain their bytes.
Source hashes, actual-reading flags, selected-page unions, exterior
degree diagnostics, canonical inventory and whitespace gates pass.
This checkpoint requires no unchanged-book rebuild, native compilation
or editor/tab change. It makes no original-result admission, independent
model call, production verification receipt or complete proof-repair claim.
