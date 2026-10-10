# Volume and covolume operators, and Richardson volume models: source review

Date: 7 October 2026. Baseline `work`
`e5d303048f402ab2d1fa32fa1615830564929714`; observed `main`
`00957114db21b627e97369563032ceda9cea09c7`.

This checkpoint reads **158 distinct source/page pairs in 81 individually
displayed matching sheets**, with complete selected text and sequential
notes. Six PDFs are read completely and four partially. Every reading is
fresh; acquisition, text search and bibliography entries receive no reading
credit. The two main papers are Grund--Huh--Michalek--Suess--Wang,
*Linear operators preserving volume polynomials*, arXiv:2506.22415v1,
and Khai-Hoan Nguyen-Dang, *Richardson volume models for skew Schur and
skew Schur P/Q-functions*, arXiv:2608.10516v2, **with an appendix by
Zhenpeng Wang**. Both main PDFs were read in full, including the appendix.

The proposed reader path connects Appendix D's Lorentzian normalization
to Appendix F's globally generated Chern intersection polynomials, then
to Grassmannian Richardson models and tableau coefficients. Exact volume
realizability is stronger than Lorentzianity. A separately read proof of
finite-variable skew-Schur Lorentzianity and the original reverse
Khovanskii--Teissier argument clarify this distinction. Source claims and
historical questions retain their exact versions and field hypotheses.

This is a **source-only checkpoint**. The 4,524-page book, all 425 active
TeX inputs, both bibliographies, 108 protected inputs, 116 prior frozen
manifests and 196 prior exports are byte preserved. The native catalogue
and its open editor are unchanged. No new book compilation, whole-book
reread, independent-model receipt, original theorem, canonical solved
status, or repair of BJ22 Theorem 6.21's general critical Siu-division
input is claimed. The LPWZ elliptic-density candidate remains unverified.
The canonical 42-atom/12-problem inventory is unchanged. Reading a
complete displayed proof does not recursively certify its cited foundations.

## Editions and actual reading

All page numbers below are physical PDF pages. The companion manifest
contains exact PDF, text and image hashes, acquisition URLs and all 81
sequential reading notes. These locators are version-specific.

| Controlling source | Pages actually read | Whole PDF? |
| --- | --- | --- |
| Grund et al., arXiv:2506.22415v1, 27 June 2025 | 1--27 | yes |
| Nguyen-Dang, with Wang appendix, arXiv:2608.10516v2, 25 August 2026 | 1--42 | yes |
| Huang--Huh--Michalek--Botong Wang--Shouda Wang, arXiv:2505.08881v2, 14 June 2025 | 1--9 of 40 | no |
| June Huh, *Volume polynomials*, arXiv:2601.13249v4, 4 June 2026 | 1--24 | yes |
| Ross--Suess, arXiv:2502.13305v1, 18 February 2025 | 1--10 | yes |
| Philip B. Zhang, arXiv:2608.12266v1, 12 August 2026 | 1--9 | yes |
| Kresch--Tamvakis, Lagrangian paper, author-hosted May 3, 2003 version | 1--4, 12--13 of 27 | no |
| Kresch--Tamvakis, orthogonal paper, published Compositio 140 (2004), 482--500 | 1--3, 7--8 of 19 | no |
| Castillo--Cid-Ruiz--Li--Montano--Naizhen Zhang, published Adv. Math. 374 (2020), 107382 | 1--4, 17--20, 22--25 of 34 | no |
| Jiang--Li, arXiv:2112.02847v3, 21 August 2023 | 1--14 | yes |

The Lagrangian author PDF is not the unacquired 34-page published edition.
An initial UZH download failed with HTTP 503; the observed author-site
link supplied the exact May 2003 file subsequently read. The orthogonal
PDF is the published publisher file. Jiang--Li's arXiv file is not
asserted byte-identical to Math. Z. 305 (2023), paper 26, even though the
bibliographic metadata identifies that publication. Its internal date is
22 August 2023. Nguyen-Dang v1, the earlier Grund--Suess paper and
unselected foundational dependencies were not read. Neither metadata
survey nor source-era conjecture status certifies current worldwide status.

## Operator and realization gates

**V01 -- Rational realization and a closed cone are different.** GHMSW
Definition 1.1, pp.1--3, uses an algebraically closed field, a reduced
irreducible projective variety, semiample Cartier divisors and a
nonnegative rational scalar times `1/d!` of their top intersection.
A volume polynomial is a limit of such realizations. With
`x^[alpha]=x^alpha/alpha!`, a homogeneous differential polynomial
`g=sum c_alpha partial^alpha` is realizable covolume when its cutoff
reversal `sum c_alpha x^[mu-alpha]` is realizable volume. Increasing the
cutoff does not change this property. Zero is allowed. An arbitrary
nonnegative real scale belongs to the limiting discussion, not
unconditionally to exact rational realization.

**V02 -- Two preservation iff statements have different test spaces.**
GHMSW Theorem 1.3 and Corollary 1.4, pp.3--4 and 12--13, characterize
covolumes by constant-coefficient differentiation preserving all volumes;
Theorem 1.9 and Corollary 1.10, pp.5 and 16--17, give the dual
characterization. The dual converse uses auxiliary variables: Remark
3.4 must not be replaced by a same-variable iff. The paper's separately
stated quartic counterexample omits its lengthy proof; that omitted proof
is not audited here.

**V03 -- The symbol condition is sufficient.** Theorem 1.12, pp.6,
14--15, uses a homogeneous linear map between bounded multidegree
spaces with a constant degree shift. Its symbol is
`sum_alpha T(x^[alpha]) y^[mu-alpha]` (rename the source variables
consistently). The cosymbol and evaluation contraction retain all
factorials. A realizable volume symbol implies preservation; no
converse is asserted. Products, rational nonnegative substitutions,
truncations and polarization follow in their stated scopes.
`N(f_1 f_2)` is a volume when both `N(f_i)` are; normalization is not
multiplicative on overlapping variables.

**V04 -- A geometric component argument replaces unsupported
irreducibility.** GHMSW Lemma 2.1, pp.7--9, uses the generic
translated intersection on a complete homogeneous space and algebraic
equivalence of its components, supported by Huang et al. Lemma 2.6.
That lemma's entire statement and proof were read on physical p.9 of
v2; proper surjectivity, integral varieties, generic fibres and positive
component multiplicities matter. An expected-dimensional intersection
need not be irreducible. Disconnected fibres and inseparable
multiplicities cannot be suppressed.

GHMSW p.5 footnote 2 explicitly identifies a gap in Ross--Suess
Proposition 2.6 and the earlier two-author Grund--Suess route. The fully
read Ross--Suess v1, pp.3--7, asserts that a Schubert degeneracy class
is represented by an irreducible subvariety and invokes that assertion
in its diagonalization argument. The cited Fulton 1992 Theorem 8.2 was
not recursively read here. The gap is recorded as an attribution and
proof-route issue; it is not a disproof of all preservation conclusions.
Future integration uses the alternative GHMSW argument.

**V05 -- Do not remove the multiaffine or parameter hypotheses.**
GHMSW Proposition 4.4, physical p.19, concerns
`t f(x_1,x_2,...)+(1-t)f(x_2,x_1,...)` for rational `0<=t<=1`,
and **multiaffine** inputs. Its symbol Hessian has eigenvalues
`2,0,2(t-1),-2t`. The intro and Huh survey's nonnegative-parameter
shorthand does not control this displayed mixing parametrization.
The average of `x_1^2` and `x_2^2` has two positive Hessian eigenvalues.
Interlacing, polarization and coefficient normalization have their
own hypotheses. Huang et al. v2's p.5 notation explicitly extends its
quadratic realization framework to arbitrary algebraically closed
fields with listed exceptions; a provisional reading note about a
complex-only limitation was corrected by the following notes. The
later full quadratic classification proof was not selected.

**V06 -- Supports: a historical question has an attributed answer.**
Castillo et al. Theorem 3.12, pp.17--18, says an irreducible
multiprojective variety has positive multidegree `alpha` exactly when
`|alpha|=dim X` and `sum_{i in A} alpha_i<=dim pi_A(X)` for **every**
subset A. Corollary 3.13, pp.19--20, requires all inequalities on
one top-dimensional component for a reducible scheme. Proposition
5.1, p.23, identifies its rank function by joins of factor function
fields. Section 5 distinguishes linear, Chow and algebraic
polymatroids; the Cohen--Macaulay reducible example shows why
irreducibility matters.

GHMSW Proposition 5.4, physical p.21, explicitly states equivalence
for **any field** and explicitly answers Castillo et al. Question 5.8
positively. Its finite-generator affine graph closure realizes the
algebraic rank function as projection dimensions. Section 5's
arbitrary-field scope is explicit on p.19; it must not automatically
broaden every operator definition from Section 1. A clarification
record supersedes provisional field/status comparisons made while
reading the older paper. Exact support classification does not
classify all supports of the closed or analytic cones. Fano exact
realizability depends on characteristic; its closed-cone status outside
characteristic two is still a question in these sources. Matroid
intersection means the dual of the union of duals, not common
independent sets; loop/coloop zero boundaries require care.

## Richardson, finite-alphabet and inequality gates

**V07 -- A total Chern coefficient polynomial becomes a normalized
volume.** Nguyen-Dang Theorem 3.1, pp.6--9, starts with an irreducible
projective complex d-fold and globally generated bundles `F_i`.
Choose enough generators in `0 -> K_i -> W_i O_X -> F_i -> 0` so
`s_i=rank K_i>=1`; `G_i=K_i^dual` is globally generated. On the
product of quotient projective bundles `P(G_i)`, the tautological
classes are nef, the dimension is `D=d+sum(s_i-1)`, and
`pi_*(xi_i^(s_i-1+m))=c_m(F_i)`. Consequently the divisor-volume
polynomial equals `N(x^eta T_X,F)`, with `eta_i=s_i-1`, and its
`partial^eta` derivative equals `N(T_X,F)`. This exact factorial
statement is stronger than only declaring the normalization
Lorentzian. Singular bases are allowed. The characteristic-zero
smooth realization uses resolution; the source's later all-field
intersection identities do not imply arbitrary-characteristic smooth
resolution.

**V08 -- Ordinary Richardson complement and finite-alphabet
complement differ.** Theorems 4.1--4.2, pp.9--13, use a rectangle
inside `Gr(r,r+c)`, the dual tautological subbundle, opposite
Schubert flags, the irreducible Richardson variety of dimension
`|lambda|-|mu|` and the complement
`(c-lambda_r,...,c-lambda_1)`. Pieri and Schubert duality recover the
ordinary skew Kostka coefficients. The projective-bundle shift is
`r-1`. Zero specializations and the empty diagram are separate cases.

Zhang v1, fully read, proves finite-variable normalized skew-Schur
Lorentzianity by a different route: shifted 321-avoiding flagged
Schubert specialization, dually Lorentzian preservation under
nonnegative substitutions, and dual Jacobi--Trudi. Its complementary
shape is `(R^n,mu)/lambda`, with nonzero n-variable specialization
and `R>=lambda_1`; it has `nR-|lambda/mu|` boxes and exponent bound
`(R,...,R)`. Its finite dual is exactly `N(s_lambda/mu)`.
Complementation and finite dualization do not commute with deleting
an alphabet variable. Nonnegative LR expansion alone does not prove
Lorentzianity. This paper does not claim exact volume realization or
skew P/Q results.

**V09 -- Type C and type D keep their different factors and ranks.**
Nguyen-Dang Section 5, pp.13--17, uses the Hopf-dual ordinary `P` and
`Q` bases; `Q_lambda/mu=2^(length(lambda)-length(mu)) P_lambda/mu`.
The classical LG Schubert class is **modified-Q**, evaluated by
sending its elementary generator to the tautological quotient Chern
class; ordinary Schur-Q evaluated literally on the bundle is not
that class. Kresch--Tamvakis Lagrangian pp.2 and 12 directly confirm
the modified Pfaffian convention and set-of-parts Poincare complement.
Rank N gives shift `N-1`.

Wang's fully read appendix, pp.28--42, supplies the spinor
modified-P transform and direct Q realization. Rank `N+1` gives
shift N; `c_i(Q_D)=2 tau_i` and top Chern class vanishes. The
published orthogonal paper pp.1--3 and 7 confirms the integral
modified-P subring and duality. Characteristic-two factors remain
integers in Chow groups, not scalar coefficients reduced modulo two.
The all-field cycle construction and characteristic-zero smooth
clause remain separate. Ambient characteristic-two maps are finite
flat radicial; their restrictions to singular Richardson varieties
are not asserted flat. For `d=|lambda|-|mu|` and
`r=length(lambda)-length(mu)`, the restricted degrees are
`2^r` and `2^(d-r)`, with product `2^d`. A mistaken preliminary note
was explicitly corrected before any book edit. The regular-section
bridge has codimension equal to the number of projective-bundle
factors and yields the stated derivative identity with factor `2^r`.
No complex type-C/type-D isomorphism is inferred.

**V10 -- Tableau descendants have controlled strength.** Nguyen-Dang
Sections 6--8, pp.18--27, give exact normalized product/substitution
and polarization descendants, root-direction coefficient
log-concavity, a nonzero one-positive-direction Hessian criterion,
reverse KT, and precise ordinary skew-Schur support. The dominant
partition has pth part equal to the number of skew columns of length
at least p; vertex coefficients are one. The paper gives implicit
support data for general skew P/Q, not that same column formula.
Covariance estimates concern the factorial-normalized polynomial
law `c_alpha z^alpha/(alpha! f(z))`, not a uniform tableau law or
negative association. Two-row LR conclusions concern cumulative
sums, not individual LR multiplicity log-concavity.

**V11 -- Reverse KT is a stricter necessary condition.** Jiang--Li
Theorems 1.1 and 3.5, pp.1--2 and 8--9, apply to nef Cartier divisors
on a projective variety over an algebraically closed field of any
characteristic. The mixed version permits separate `B_1,...,B_k`
and `C_1,...,C_(n-k)` and keeps factor `1/binomial(n,k)`. The
complete proof uses multipoint Okounkov bodies, very-general cuts
over an uncountable extension, sums their volumes, and descends by
base change and nef approximation. It needs no general positive-
characteristic resolution. Ample inputs give strict inequality;
nef product-variety examples attain the constant. Smooth-surface
Proposition 5.1, p.12, characterizes **nonzero** equality by positive
numerical span and square-zero B,C. Its higher-dimensional proposed
equality description is a guess, not a theorem.

Huh v4 pp.14--15 supplies a rational Lorentzian cubic outside every
volume cone. Exact checks verify its M-convex support and each
first-derivative Hessian, while the necessary coefficient inequality
fails: `3*12*12=432 < 84*6=504`. Thus a Lorentzianity-only proof
cannot establish exact or limiting volume realization.

## Status and transcription boundaries

Huh v4 p.3 footnote 1 reports a counterexample to the **exact**
five-dimensional codimension-two convex projection conjecture:
its six entries on indices 1--4 equal one and its four entries
involving index 5 equal zero. It attributes the report to Helen W. J.
Zhang and Chengdong Zhao and distinguishes Shouda Wang's approximating
convex bodies and the still-open closure variant. No complete
counterexample proof or independent primary-paper locator was supplied
there, so this checkpoint records an attributed report, not an
independent proof certificate or a blanket disproof of the closure
question. It is different from the area-projection conjecture.

The same survey distinguishes closed-volume field independence,
analytic volume/covolume preservation, support questions, and
algebraic matroid duality. Its normalized-general-Schubert question
is not settled merely by skew-Schur results. These are source-era
question locators; they do not replace the canonical book problems.
The 2020 Chow question answered by GHMSW is identified separately.
Recent tropical arXiv:2608.25987v2 and the 2026 dual-mixed-volume
candidate remain metadata-only deferred directions, not read sources.

Displayed transcription diagnostics are retained in the notes: missing
multiple in a complete linear system (GHMSW p.7), missing `-alpha`
in a cutoff exponent (p.8), a degree-reversed Chow class (p.12),
calling an ordinary coefficient-one quadratic Lorentzian instead
of using its covolume reversal (p.16), and product terminology
(p.24). Ross--Suess's unscaled volume identities also omit harmless
positive global binomial/factorial factors and transpose a displayed
Y-degree. Huh's ball example uses an undivided scale despite an earlier
`1/d!` convention; its printed quadratic triangle condition must
retain all pairings. Jiang--Li's final restricted-volume display
transposes Y/Z dimension exponents and its graph-model composition
notation reverses domain order. None is promoted as an original
repair or a disproof of the main imported theorems. Only checked,
dimensionally correct controlling statements will be integrated.

Nine exact rational/symbolic diagnostics pass in the final arithmetic
receipt: finite tableau complementation, empty/zero alphabets and
normalization, Chern shift/derivative factorials, bounded symbol
contraction, the coefficient-one quadratic, swap-symbol spectrum,
the survey cubic, reverse-KT factors, and matroid zero boundaries.
The first arithmetic helper failed an erroneous degree-three expected
reversal for a degree-two expression; the second reached all assertions
but failed JSON serialization. Both failed attempts are frozen;
only the corrected third receipt is a pass. Finite checks do not
prove universal geometric preservation or create an independent-model
verification receipt. Subsequent live integration requires its own
source and build gates, rendered-page reading and publication record.
