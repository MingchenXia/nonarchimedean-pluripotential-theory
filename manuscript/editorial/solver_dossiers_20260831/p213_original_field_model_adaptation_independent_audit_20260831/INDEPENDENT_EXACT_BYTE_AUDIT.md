# Independent exact-byte audit: original-field model adaptation

Reviewer: `/root/p081_weighted_repair_fresh`. Date: 31 August 2026.

## Verdict and independence

PASS for the frozen diagnostic's positive claims, elementary obstructions and
explicit conditional reduction. No unresolved substantive mathematical gap or
mandatory candidate correction was found. This is not a proof of model-cell
capture, a mixed-wall or ordinary-W locality theorem, whole-current rigidity, or
production acceptance.

The candidate is authored by `/root/p082_independent_reaudit`. This reviewer did
not author it or supply its rational approximation, resolution construction or
obstruction arguments. The reviewer previously audited the separately referenced
finite-projection packet, reduced-wall packet, common-moment packet and displayed
representation R. Those prior contributions are disclosed. In this audit R and
the common-moment comparison are conditional interfaces, not self-certified anew;
the finite-projection paragraph is a status reference, not a premise for the new
positive construction.

The entire 194-line note, 58-line source ledger and candidate manifest were read.
The derivative-degree predecessor was read in full for the narrow transport
claim; the exact displayed R statement and relevant common-moment comparison
were checked. Exact primary source locators were inspected independently; the
source and visual-review limits are recorded below and in the companion ledger.

## Exact frozen bytes

Candidate directory:
`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_original_field_model_adaptation_diagnostic_20260831/`

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 26239 | e3ea5b70de107973afbbd6839385dc90e445ec0415285cc09ba9c931b0654596 |
| SOURCE_LEDGER.md | 8637 | 7837e6bdd718ecff2aa96c7c8e58ed27bc3dd2ad7c4cd078fadaf89a0abc5ecd |
| MANIFEST.json | 10373 | 7836fc091e7cb114af08748b7e04a538b4ba8cdc2231a3e63c18026c4b7e6515 |
| SHA256SUMS | 4610 | 3166ebbdccd87b59b913c2eaa3ffbd18ef7457943fd13acd380a8c6d7d649096 |

All 23 candidate manifest entries, including historical and primary local inputs,
matched size and SHA-256. All 24 checksum entries matched. Authored Markdown has
zero CR bytes, forbidden controls below 32 other than LF/tab, or DEL bytes. The
complete read-only results are preserved in INPUT_CHECKS.json. Hash agreement is
not used as a substitute for mathematical review.

## 1. Rational replacement and compact ordinary partition

Note lines 34-73, equations (2.1)-(2.5), check in the full stated algebraic scope.
This argument does not require the point to lie over the generic scheme point,
to be divisorial, or to be rational over K.

Let xi be the scheme image of an analytic point x. On an affine algebraic
neighbourhood Spec(A), a sufficiently large closed analytic ball has an affinoid
algebra in which A is dense. For a nonzero denominator in the residue seminorm,
approximate both numerator and denominator closely by elements of A. The
denominator remains nonzero and the quotients converge. Thus the completion of
Frac(A/ker(x)) is H(x), with the same absolute value. This justifies the note's
use of kappa(xi), rather than incorrectly asserting density of K itself. It also
handles xi of positive codimension: lift the selected residue fraction to A
with denominator outside ker(x).

The strict approximation |f_i(x)-c_i|<|f_i(x)| implies c_i is nonzero and has
the same norm as f_i(x). Consequently both chosen algebraic numerator and
denominator are nonzero at x. On their principal algebraic open, the fraction
is genuinely an analytic unit. The strict norm inequality persists on an
ORDINARY open neighbourhood by continuity. A finite intersection works for all
coordinates simultaneously. The ultrametric inequality then proves pointwise
exact norm equality throughout that neighbourhood. Since an ordinary CLD
moment presentation depends on these real norm functions, its pulled-back
superform is exactly unchanged; no limiting argument for currents or derivatives
is being used.

The passage to finitely many source terms is also valid. X^an is locally compact,
Hausdorff and good; the same is true locally in W. Shrink a cover of the compact
support K_0 to finitely many compact neighbourhoods within the ordinary O_i.
CLD 15.2.5 supplies cutoffs there. Squaring them gives nonnegative phi_i; grouping
those assigned to the same O_i is harmless. Their sum H is positive near K_0.
For eta supported compactly inside {H>0}, the expression eta*phi_i/H is smooth
there and vanishes on a neighbourhood of its complement, so zero extension is
smooth. Its support is a closed subset of the compact support of phi_i inside
O_i. The sum is eta, hence one near K_0. Outside K_0 the original form is zero,
so the asserted global finite sum holds everywhere.

No rationality of the cutoffs, compactness of a tropical target in place of source
support, formal-Zariski-to-ordinary-topology identification, or global
algebraization of the analytic units is needed. In particular analytic
transcendence is not a counterexample to this local exact-norm construction.
CLD 12.2.3 corroborates the strict-shrinking mechanism. Its 18.4.5 proof is only
precedent in a narrower setting; that proposition's algebraically closed and
full-dimensional hypotheses are NOT silently applied to arbitrary x here.

## 2. Original-field SNC support and the characteristic restriction

Note lines 77-95 check. The conclusion is deliberately a regular model of a
proper birational generic modification Y of X, not necessarily a regular model
with identical generic fibre after the horizontal boundary is resolved.

The input needed for compactification is available even when X is not
projective. K=R[1/pi] is a finite-type R-algebra, so the smooth proper K-variety
is separated and finite type over R. The integral scheme-theoretic closure of
the Nagata open immersion is proper over R. Its generic fibre is X: the open
immersion of the proper K-scheme X into a separated K-scheme is proper, hence
closed, and X is dense in the closure. Integrality makes the model torsion-free
and therefore flat over the DVR. [Stacks 0F41](https://stacks.math.columbia.edu/tag/0F41).

The model is noetherian and excellent by finite type over the complete local
ring R. [Stacks 0HA6](https://stacks.math.columbia.edu/tag/0HA6).
Residue characteristic zero makes every nonzero integer a unit of R, so R
contains Q. Conversely an R containing Q has residue characteristic zero. Merely
assuming characteristic zero for K does not suffice.

Temkin 1.1.6 with empty initial boundary preserves the regular generic fibre.
Then 1.1.3 applies to an ordered list of the finitely many prime divisors on the
regular model. Their total support becomes SNC. All these modifications are over
R; horizontal centres may modify X birationally. The source's definition 2.1.9
of strictly monomial retains multiplicity, and 1.1.18 separately allows a finite
DVR extension. Neither is reduced original-field domination.
[Temkin, arXiv:0912.2570v2](https://arxiv.org/pdf/0912.2570v2).

For completeness, the local monomial identities do follow from this divisor
output. A regular noetherian local ring is factorial. The support of the divisor
of each pulled-back g_i is contained in the boundary: outside it the original
g_i and its inverse are units. Dividing by the product of boundary parameters
with the prescribed integer orders leaves a local unit. The same argument for
pi has strictly positive exponents exactly on vertical components. The finite
boundary includes all vertical components even when g_i has vertical order or
pi is the only divisor datum. Thus constants such as g_i=pi pose no exception.

On a formal chart where such a unit and its inverse are both regular, both have
norm at most one, hence its norm is one. This does not assert that every ordinary
neighbourhood stays in that chart. The note correctly postpones that source-local
question. The construction requires neither representation premise (R) nor the
finite-projection result.

## 3. The two original-field obstructions

### 3.1 Multiplicity-two divisor under domination

Note lines 99-110 are correct. The first blowup of the smooth point on P^1_R's
special fibre creates two multiplicity-one components meeting with local
equation xy=pi. Blowing up this node, the chart y=xv gives pi=x^2 v. The total
space is still regular: eliminating pi leaves the expected regular parameters
in its completed local charts. At the generic point of the new exceptional
divisor x=0, v is invertible and x is a uniformizer; its order on pi is exactly
two. The reduced support is SNC, although the special fibre is not reduced.

The persistence claim is stronger than tracking only successive blowups and has
the required hypothesis. The target is noetherian and normal in codimension
one; the source of the proposed proper birational domination is reduced. The
isomorphism locus therefore contains the exceptional divisor's generic point.
The unchanged DVR has unchanged order of pi. [Stacks 0BBQ](https://stacks.math.columbia.edu/tag/0BBQ),
with the direct scheme statement [Stacks 0BFP](https://stacks.math.columbia.edu/tag/0BFP).
Taking product with, for example, (P^1_R)^(n-1) preserves this computation and
gives examples in every requested relative dimension.

This refutes cofinal REDUCED domination of arbitrary original-field model
blowups. It does not say that this blowup is required by every chosen moment,
that an unmarked reduced model of the original generic variety does not exist,
or that the SNC-support conclusion in Section 2 is impossible.

### 3.2 Ramified horizontal boundary, including generic modifications

Note lines 114-127 are correct. Over C((pi)), z^2-pi defines a prime divisor on
P^1_K with ramified quadratic residue field. A horizontal component in a
regular strict semistable pair over this DVR is itself regular with reduced
special fibre: locally quotient by its distinct horizontal coordinate, leaving
the same product-of-vertical-coordinates equation for pi. For a relative curve
this horizontal component is smooth of relative dimension zero and proper,
hence finite etale, which is inconsistent with that generic residue field.

The higher-dimensional valuation argument avoids reliance on a finite horizontal
component. D=(z^2-pi=0) times the other projective factors is integral with
function field L(t_2,...,t_n), where L contains s with s^2=pi. A proper birational
modification of smooth X is an isomorphism at the generic point of D, by the
same codimension-one principle, so the strict transform retains this function
field. Its proper closure H in the alleged adapted pair dominates Spec(R).
Its nonempty special fibre has a codimension-one generic point because pi is a
nonzero nonunit in the regular integral H. At that DVR, ord(pi)=2 ord(s) is even,
whereas the reduced special fibre requires ord(pi)=1. This is a contradiction.

The pair condition is essential. Ambient unmarked semistable reduction is not
what this example excludes. It also does not preclude retaining positive even
vertical multiplicities. GRW 3.1-3.6 supplies the local-coordinate comparison;
its algebraically closed-field theorems are not used to produce any original-DVR
pair.

## 4. Source scope, current transport and conditional comparison

Note lines 129-162 respect the checked sources. Altered local uniformization
uses a field extension and a rig-etale/quasi-etale cover, not the requested
proper birational map of the original space. Its affine algebraization statement
does not algebraize a global proper model with prescribed functions. GRW's
faithful tropicalization starts with a given strictly semistable pair; it does
not construct that pair from a prescribed ordinary analytic moment. GRW 9.6
also expressly warns that its chosen rational map need not factor through the
retraction. No unknown-current pullback under an alteration is defined here.

The positive closed-current transport assertion at line 143 is valid in the
present algebraic modification setting. Take dense algebraic opens on which
p is an isomorphism; their closed complements in the integral n-dimensional
varieties have dimension at most n-1. Intersect their analytifications with W
and p^(-1)(W). Every compact top-degree test avoids the upstairs exceptional
set by CLD 15.2.1(b). Transport on the actual isomorphism locus and unique
fixed-bidimension extension therefore define T_Y; positivity is preserved by
that isomorphism. The two derivatives have bidimensions (n-1,n) and (n,n-1),
whose maximum is still n. They vanish off the exceptional set, and the same
support theorem forces them to vanish globally. No extension theorem in
bidimension (n-1,n-1) and no blanket differential-commutation assertion is used.
Proper pushforward agrees with the original current off the downstairs
exceptional set and hence everywhere by the top-degree uniqueness statement.

This only transports the domain W to p^(-1)(W). It does NOT extend a local T
across the ordinary boundary of W. The whole residual-curve tube and all compact
primitives required by a wall argument still need to lie in the transported
domain. A global T avoids that one domain obstruction, not the capture or mixed
wall problems.

The last comparison is correctly conditional. Its input must provide one
specified common ratio c for all cells and summands used in this compact test.
One relatively open full-dimensional patch per coefficient-constant original
cell suffices: on the actual common-moment patch the nonzero determinant
comparison transfers the normalized ratio; constancy transfers it to the
original cell. R then evaluates arbitrary compact source multipliers, and its
no-lower-cell clause removes no unrelated full-dimensional rank-drop family.
The finite partition sums the resulting equality for this test. Neither mere
connectedness of X, coincidence of target images, nor resolution of divisor
support supplies any of these capture, incidence or common-ratio premises.

The good-reduction unmarked skeleton example is coherent: a smooth irreducible
special fibre gives only a vertex, while a torus coordinate moment has
n-dimensional Gauss families. Similarly, incidences in an extended marked
skeleton may involve horizontal components with vertical multiplicity zero.
The already frozen vertical-wall calculation does not treat those incidences.

## 5. Separate finite projection: no circularity

Lines 164-186 faithfully identify the previously frozen finite-projection
candidate and this reviewer's earlier report. Aggregate finite-flat degree and
individual source-cell comparison are not conflated. The latter needs its
additional unramified original-DVR generic-Gauss argument and R. This paragraph
does not prove that argument, construct ordinary analytic sheets, or prove the
prospective completed model equation in every future adaptation. Removing the
paragraph leaves Sections 2-6's positive proofs and conditional logic unchanged.
There is no circular import into the use of resolution.

## 6. Optional exposition and genuine remaining work

No mandatory edit is requested. Two optional clarifications could help a later
integration, without changing frozen bytes:

- Line 28's phrase about what the earlier packet's 'exclusions ... do not include'
  is grammatically awkward. 'The theorem does not cover nonreduced or non-strict
  models' would state the intended limitation directly. The surrounding text
  already makes the actual reduced scope unambiguous.
- Before summing in line 158, reiterate that the SAME c is assumed for every
  summand of the compact partition. The present requirement of one specified
  ratio throughout the cells used for comparison is read in that sense.

Genuinely unresolved by this diagnostic are: ordinary-W outer-collar support;
mixed vertical-horizontal wall identities; realization/capture of each
prescribed source cell on the original field; and propagation of one normalized
ratio through all incidences needed for a test, let alone all tests. The
nonreduced global wall construction mentioned as separate ongoing work is not
certified here. Neither all-field model adaptation nor nonalgebraizable proper
analytic scope follows from the residue-characteristic-zero construction.

## 7. Validation, source QA and preservation

All 22 selected complete local source-PDF pages were rendered and visually
inspected: CLD 159,160,298,302,334,335,423,424,426,427,521,522; GRW 1,8,9,33,34;
Temkin altered-local-uniformization 1,2,11,12,13. Every render exited zero and all
mathematical content was readable. Four renders emitted nonfatal Fontconfig
cache-writability diagnostics. No permission/cache workaround was attempted.

The versioned embedded-resolution PDF's theorem text and definitions were read
successfully from the primary arXiv endpoint and checked against the author's
mirror. Screenshots of pages 2,3,4,5,9 failed with cache-miss/timeout errors at
both endpoints; visual inspection and a local byte hash for this remote PDF
are NOT claimed. This is an access/visual-evidence limitation, not an unresolved
mathematical premise hidden behind a PASS.

SOURCE_VISUAL_QA.json records exact render results, temporary PNG hashes and
failed remote screenshots. The 22 owned scratch PNGs were deleted after the
evidence was saved; they are regenerable from the unchanged pinned PDFs. No PDF
was created or edited, so the PDF artifact marker was not invoked. No candidate,
prior packet, source, live manuscript, inventory or gate was changed. No git or
production operation occurred. All new audit bytes remain separate from any
production decision.
