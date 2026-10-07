# Mixed Segre zeta functions: source review

Date: 7 October 2026. Baseline `work`
`56b08a74684846ca70f83fc618657475bf9e1a63`; observed `main`
`00957114db21b627e97369563032ceda9cea09c7`.

Yairon Cid-Ruiz, *Mixed Segre zeta functions and their log-concavity*,
arXiv:2507.06424v2, was read completely: 29 physical pages. Three
dependencies were read in explicit scopes, adding 31 distinct source/page
pairs. The total is **60 source/page pairs in 31 individually displayed
sheets**, with complete selected-text reading, matching-image inspection
and sequential notes. One PDF is completely read; three are partial.
No reading attestation is reused. The Brändén--Huh PDF uses previously
acquired exact published bytes, but its eleven selected pages are freshly
read for this checkpoint.

The relevant addition is a global mixed intersection invariant linking
Appendix C's integral closure and stabilized Segre zeta discussion to
Appendix D's Lorentzian polynomials and Appendix F's positivity. The
modified numerator, its degree of homogenization and its factorial
normalization must remain explicit. This is not a coordinatewise
comparison theorem for the local Jacobian Segre numbers in H.19, and
does not repair BJ22's critical Siu-division input.

This source-only checkpoint preserves the 4,518-page book, all 425 active
inputs, both bibliographies, 108 protected inputs, 114 preceding frozen
manifests and 193 frozen exports. It preserves canonical problem statuses
and the native catalogue/editor. No fresh book compilation, final-book
reading, original theorem, independent-model receipt or solved-status
promotion is claimed. Reading the displayed proofs does not recursively
certify their cited foundations.

## Version and reading scope

All page locators below are physical PDF pages. Full byte, text and image
identities, acquisition URLs and actual sequential notes are in the manifest.

| Controlling source | Pages actually read | Complete PDF? |
| --- | --- | --- |
| Cid-Ruiz, 2507.06424v2 | 1--29 | yes |
| Brändén--Huh, published Ann. Math. 192 (2020), 821--891 | 2--3, 11, 14--15, 25, 34, 51--53, 58 of 71 | no |
| Aluffi, 2304.02043v4 | 1--3, 5--9, 13--18 of 29 | no |
| Aluffi, 1606.03098v2 | 1--2, 9--12 of 19 | no |

The mixed paper's v1 was submitted 8 July 2025 at 22:00:18 UTC; v2 was
submitted 10 July 2026 at 20:56:10 UTC. Its internal PDF date is
14 July 2026. These dates are recorded separately. The arXiv comments
and author's website identify *Algebra & Number Theory*, to appear;
no published edition was acquired. The mixed v1 PDF was not acquired
or read, and v2's numbering controls every admitted locator.

Aluffi's covolume v4 was submitted 17 December 2023 at 04:27:35 UTC;
its internal date is 1 December 2023. The arXiv metadata identifies
Adv. Math. 437 (2024), article 109440, 37 published pages,
DOI `10.1016/j.aim.2023.109440`. The actually read file has 29 pages
and is explicitly v4, not the uninspected published edition. Likewise,
the 19-page Segre-zeta v2 was submitted 27 July 2016 at 07:12:55 UTC;
the recorded journal reference Adv. Math. 320 (2017), 1201--1226,
DOI `10.1016/j.aim.2017.09.023`, does not establish byte identity with
the unread published file. HTML reading is limited to the displayed
title, authors, version history, comments and corresponding publication
metadata; no complete-HTML reading is claimed.

## Definition and rationality gates

**M01 -- Two different multivariable constructions.** Mixed v2
Definition 3.2, pp.5--6, concerns a sequence of ideal sheaves on one
scheme. For the common product-ideal center, it uses the joint
deformation/blowup construction on `X × A1` and powers of the
tautological classes on its transform. This transform is not assumed
Cartier: Remark 3.4 and Example 3.5 explicitly distinguish it from
the Cartier inverse image of `t=0`. The associated ordinary joint
blowup has `O_B(e_i)=O_B(-E_i)`. Empty-center or all-unit boundaries
need their own convention check before dimension assertions are reused.

Aluffi v4 instead stabilizes the ordinary Segre class of **one**
multihomogeneous ideal on a product of projective spaces, pp.13--15.
Its denominator has factors `1 + sum_j e_jk t_j`; the mixed denominator
has factors `1 + d_ij t_i`. Similar terminology does not identify these
invariants, their numerators or their proof signatures.

**M02 -- Signs, multinomials and pushforward.** Mixed Theorem 3.7,
pp.7--9, writes the pushed class as `[X]` minus the pushforward of
`prod_i(1+E_i t_i)^(-1)[B]`. Positive multi-index terms carry sign
`(-1)^(|alpha|-1)`; the zero-index term has its stated supported-class
convention. Corollary 3.9 reconstructs the ordinary product-ideal Segre
class using multinomial coefficients. Proposition 5.7, p.20, therefore
uses a multinomially reweighted series before diagonal specialization.
The raw mixed series cannot simply be evaluated on the diagonal.
Theorem 3.10's proper-pushforward statement retains equidimensionality,
nowhere-dense centers, irreducible target and dominance of every source
component; generic degree and component multiplicities are not suppressed.

**M03 -- Equal-degree graph formula has limited scope.** Setup 3.11
and Corollary 3.12, pp.11--12, assume each ideal is generated in a
single positive degree and express the joint blowup through a graph in
a product of projective spaces. High truncation preserves a fixed
projective ideal sheaf, not automatically its homogeneous ideal at the
vertex or its stabilized zeta function. Aluffi v2 Example 5.6, p.9,
exhibits two ideals defining the same empty projective scheme with
different stabilized zeta functions. Saturating or truncating first is
not an invariant-preserving shortcut.

**M04 -- Join formulas retain dimension bounds.** Mixed Setup 4.1,
pp.12--14, uses a dominant rational map resolved by a blowup with flat
target projection and compatible sections/bundles. Lemma 4.4 and
Proposition 4.7 require the base dimension to be less than
`N-sum r_i`; Theorem 4.8 requires the stronger
`N-m-sum r_i` bound. The extra `m` cannot be discarded when passing
from graph/shadow identities to the Chern-times-Segre join formula.

**M05 -- Rationality is not positivity of the raw series.** Definition
5.2, Lemmas 5.4--5.6 and Theorem A = Theorem 5.3, pp.16--20,
give `zeta=P/D`, where
`D=prod_i prod_{j=0}^{r_i}(1+d_ij t_i)` and `P` has nonnegative
integer coefficients. The stabilization threshold is
`n >= m + sum_i r_i`, the total number of generators. The coefficients
of the power-series expansion itself can have either sign. The
factors of this chosen denominator are candidate poles and can cancel;
they are not asserted to be poles of the reduced rational function.
For integration, use nonzero proper homogeneous ideals with nonzero
positive-degree generators, as the displayed proofs require. A literal
zero/unit extension is not imported without checking its separate
conventions. Aluffi v2's reduced-denominator “monic” wording in
Theorem 5.8 is not imported; the explicit constant-term-one product
presentation suffices here.

**M06 -- Integral closure gives invariance, not an unqualified converse.**
Mixed Proposition 5.8, pp.20--21, is invariant under replacing each
ideal by its integral closure. Its proof uses eventual reductions,
finite birational Rees maps and polynomial-extension compatibility.
Aluffi v2 Proposition 5.12, p.11, supplies the one-ideal antecedent.
This does not yield a converse for arbitrary mixed sequences or remove
the nested-ideal premise from C.9's separately audited published
integral-dependence criterion.

## Lorentzian and primary-locator gates

**M07 -- Keep the factorials.** Mixed Definition 6.1, p.21, uses
`N(sum a_alpha t^alpha)=sum a_alpha t^alpha/alpha!`.
A polynomial is denormalized Lorentzian when its normalization is
Lorentzian. Brändén--Huh published Definition 2.6 and Theorem 2.25,
physical pp.11/25, provide the nonnegative coefficients, M-convex
support and derivative-quadratic criterion, including the zero
polynomial convention. Published Corollary 3.7, physical p.34 /
printed p.854, says normalization preserves Lorentzian polynomials;
the converse fails. One cannot silently remove factorials from an
assertion that a normalization is Lorentzian.

**M08 -- Correct the controlling published volume locator.** Mixed
v2 pp.3 and 23 cite `[7, Theorem 4.16]` for the volume theorem.
Its bibliography, p.28, identifies the published Brändén--Huh article.
In those exact published bytes, physical p.58 / printed p.878,
**4.16 is a Corollary about M-matrix support**. The required volume
result is **Theorem 4.6**, physical pp.52--53 / printed pp.872--873.
Its preceding context on physical p.51 / printed p.871 requires an
irreducible projective variety over an algebraically closed field.
The divisors are nef. The complete displayed proof passes to very
ample divisors, cuts to an irreducible surface and applies Hodge index
on a surface resolution. No explanation involving an older numbering
is inferred. Future live citations use the cleared published 4.6,
without overwriting the frozen main reading's record of the literal
source citation. This locator defect is not a disproof of the mixed
theorem.

**M09 -- The Chern-to-volume construction is global.** Mixed
Proposition 6.2, pp.22--23, assumes an irreducible N-dimensional
variety over an algebraically closed field, proper `q:X→P^n` and a
sequence of globally generated vector bundles. After taking an ample
supply of generating sections, the product of projectivized kernels
is irreducible. Its regular-section class has a proper image in a
multiprojective space. Taking derivatives of that image's volume
polynomial produces the **factorial normalization** of the
degree-N coefficient polynomial. Positive kernel rank is arranged
explicitly. If the image loses dimension, its proper cycle pushforward
is zero: treat this separately, rather than call a degree-d expression
the nonzero volume polynomial of a smaller-dimensional image.
Derivative closure is checked in the published recursive definition
and Corollary 2.11, physical pp.11/15.

**M10 -- Apply positivity to the modified numerator.** Mixed
Theorem B = Theorem 6.3, p.24, concerns `Q=D-P`, the chosen numerator
of `1-zeta`. On the irreducible joint blowup of projective space, it
uses the globally generated quotients
`b*E_i/O_B(-e_i)` and Proposition 6.2. The line subbundle is
`O_B(-e_i)=O_B(E_i)` under the convention in M01. This is a
denormalized Lorentzian statement about a homogenization of Q,
not about raw P, the alternating zeta expansion or local Segre tuples.
If `s=deg Q` and `n>=s`, the explicit identity
`partial_t0^(n-s) N(h_n(Q)) = N(h_s(Q))` explains the passage
from the degree-n coefficient polynomial in the proof to the usual
degree-s homogenization, using derivative closure. This elementary
reformulation is exposition of the attributed result, not an original
theorem or receipt.

**M11 -- Covolume does not settle the different conjecture.** Aluffi
v4 Definition 2.1, p.5, records cohomology classes of irreducible
multiprojective subvarieties and their positive-scalar limits. In
Example 2.7, pp.7--8, a covolume polynomial has a normalization whose
quadratic derivative Hessian has two positive eigenvalues. Proposition
2.8, pp.8--9, instead reverses exponents `u^n P(1/u)` and then
normalizes; the result is a volume polynomial up to a scalar.
Proposition 3.9, pp.16--18, obtains covolume from a globally generated
bundle and a proper map to a multiprojective ambient via its kernel
incidence. These are distinct cohomology/homology coefficient
constructions. The conjecture on p.3 about directly normalized
homogenization of the multiprojective `1-zeta` numerator is a
**source-era conjecture**; its current literature status has not yet
been certified. Mixed Theorem 6.3 does not formally solve it.

Aluffi Theorems 3.5/3.6, pp.15--16, respectively use degree r and
degree r+1 homogenizations for r+1 chosen generators; the latter also
requires irreducibility of the projectivized normal cone. Their
statements and the start of their proof on p.18 are read; the
remaining proof on pp.19--20 is unselected. They are contextual
attributed statements, not independently certified proof imports.

## Computations and integration boundary

**M12 -- Disjoint-variable examples have an extra premise.** Mixed
Examples 7.1--7.3, pp.24--27, give two complete intersections in
disjoint sets of variables. Only in this stated setting is the
fiber-product blowup argument used to obtain
`zeta_12=zeta_1+zeta_2-zeta_1 zeta_2`.
The product-ideal expression then uses binomial convolution. The
general rational-convolution input attributed to Gessel--Kar is not
read here and will not be imported as a separately certified theorem.
The exponential-generating integral is interpreted coefficientwise
or in its actual convergence range, not on all parameter values.

**M13 -- Exact arithmetic agrees with the displayed examples.**
For Example 7.4, p.27,
`I=(x0^2 x1^2,x0^2 x2^3)`, the chosen numerator is
`2t+20t^2`, denominator `(1+4t)(1+5t)`, and modified numerator
`1+7t`. Its expansion starts
`2t+2t^2-58t^3+482t^4-3178t^5`.

For Example 7.6, p.28,
`I1=(x0^2,x1^2)` and `I2=(x2^2,x3^3)` in disjoint variables,
the denominator is `(1+2t1)^2(1+2t2)(1+3t2)` and the numerator is
`4t1^2+6t2^2+20t1^2t2+24t1t2^2+24t1^2t2^2`.
Subtracting gives `Q=1+4t1+5t2+20t1t2`. Its ordinary degree-two
homogenization has Hessian characteristic polynomial
`lambda(lambda^2-2lambda-441)` and inertia `(1,1,1)`.
After factorial normalization, the Hessian is
`[[1,4,5],[4,0,20],[5,20,0]]`, with exact LDL pivots
`(1,-16,-25)` and inertia `(1,2,0)`.
Aluffi v4 Example 2.7's Hessian
`[[2,2,2],[2,2,4],[2,4,0]]` has determinant `-8` and, after
permutation `(0,2,1)`, exact LDL pivots `(2,-2,2)` and inertia
`(2,1,0)`. Inertia is ordered positive, negative, zero.
These are exact SymPy rational/integer checks of attributed existing
examples, not new counterexamples or numerical eigenvalue estimates.
No Macaulay2 execution or verification of the author's linked code
is claimed; that code was not acquired or read.

**M14 -- Proof boundaries remain visible.** Fulton intersection
theory, particularly Example 12.1.7(a) on globally generated Chern
classes, projective-bundle identities and regular-section classes,
is imported by the read papers but was not acquired as a controlling
primary book file here. Kleiman--Thorup, Vasconcelos, Bertini, Hodge
index, surface resolution and the unselected portions of the
Brändén--Huh proof chain are not recursively certified. Effective
algebraic Chern cycles are not identified with curvature-form
positivity. No new original-result status can bypass the independent
`gpt-6.1-sol` at `xhigh` gate requested by the user; no such model
call or receipt is fabricated.

**M15 -- Next admissible integration.** Add an explicitly attributed
mixed-zeta discussion after C.9.1; connect it to the existing
Lorentzian normalization and intersection material, with a version
ledger in L. Keep product-ideal multinomial weighting, positive-degree
generators, generator-dependent denominators, zero-pushforward cases,
degree of homogenization and normalization visible. Preserve H.19's
local componentwise frontier and Chapter 72's canonical atomic
statuses. A live integration requires its own source gate, required
repository validation and actual reading of the changed final pages;
this source-only review is not that release certificate.
