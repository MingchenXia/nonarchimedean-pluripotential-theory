# Weak geodesic directions, contact data and September nonuniqueness

Controlling work baseline: `0a195c2bd3a4b7dccd900d130d1403529943650d`.
This checkpoint imports identified external results and gives source-dated
descriptions of seven questions. It does not introduce an original theorem,
extend a historical verification receipt or alter an active problem atom.
The native LaTeX catalogue remains unchanged and open in its existing tab.

## 1. Controlling sources and actual reading

The source files were acquired from their version-specific arXiv PDF URLs.
Initial acquisition records remain immutable, with their initial unread
flags. Separate reading-progress records describe subsequent work.

| Source | Controlling version | Pages / bytes | SHA-256 |
| --- | --- | --- | --- |
| Darvas, *A decade of metric geometry in the space of Kähler metrics* | 2604.18981v2, 28 August 2026 | 12 / 318127 | `77542f79dfcf2cd9cd8fab29b073693dec88aabff0d2ac8a7b284280292984ba` |
| Xiao, *Nonuniqueness of Model Potentials and Weak Geodesic Rays* | 2609.03296v1, 3 September 2026 | 21 / 420197 | `84a473f7b2824759044e79986705fb4a7ea3d7a40bfab3a1665b730be778503a` |
| Di Nezza–Trapani, *Monge–Ampère measures on contact sets* | 1912.12720v1, 29 December 2019 | 11 / 174841 | `11d9a65e04b1d10cd4df51d995607ae6eb6581674b4faed6088cddf65f652302` |
| Darvas–George–Smith, *Optimal asymptotic of the J functional with respect to the d1 metric* | 2101.02589v1, 7 January 2021 | 17 / 227822 | `76c87e8e3f7e3c362b580104f6cd9f3582138a1224d99861d7cb91625e5b1029` |

All four extracted texts, including references, were read in full:

- Survey: all 622 Python-split lines, in ranges 1–305 and 306–622.
- Xiao: all 1008 lines, in ranges 1–270, 271–520, 521–760, 761–1008.
- Contact paper: all 623 lines, in ranges 1–140, 141–350, 351–430,
  431–505 and 506–623.
- J paper: all 980 lines, in ranges 1–215, 216–495, 496–750 and 751–980.

Successful actual image inspection covers all twelve survey pages, all
twenty-one Xiao pages, contact pages 2, 6, 7, 8, 9, and J pages 1–4,
13–16: 46 actual primary pages. Manifests are
`/tmp/darvas_metric_survey_primary_20261005/manifest.json` and
`/tmp/darvas_uniqueness_followup_primary_20261005/manifest.json`.
The font mismatch warning from survey extraction is preserved; the
actual printed pages, rather than extracted font guesses, control.

The live arXiv pages were checked on 5 October and display survey v2
and Xiao v1 as their latest versions. The survey comment “v2. final
version” does not establish journal publication. The J paper's arXiv
page records Selecta Math. (N.S.) 28 (2022), no. 2, Paper 43; this is
metadata, not an assertion that its publisher file was acquired.
The existing published DNT21 reference is preserved, and a separate
preprint key pins the locators actually inspected.

Darvas–Zhang 2608.23505v2 was acquired separately. Only lines 1–850
have been read at this checkpoint, no actual PDF pages yet inspected;
it is not part of this import. Its announced applications do not become
book results by acquisition or by the authors' AI-assistance statement.

## 2. All seven survey questions, with exact domains and dated status

Throughout the questions, X is a compact connected smooth complex
Kähler manifold of dimension n>=1. Potentials are additive complex
potentials, not non-Archimedean metrics. A bounded ray means bounded
at each finite time, with sublinear growth; it need not be bounded
uniformly for all time. Unless stated otherwise rays start at zero.

### Question 2.3: strict positivity along a weak segment

Given two smooth potentials with strictly positive Kähler forms, does
the weak homogeneous-Monge–Ampère segment retain one positive lower
bound omega(u_t)>=epsilon omega for every t in [0,1]? Epsilon may
depend on the endpoints and fixed background. A second-derivative
upper bound does not answer the lower-positivity question.

Survey page 4 reports partial affirmative work by Hu and
Chen–Feldman–Hu and mentions Ross–Witt Nyström maximal-rank phenomena
as motivation for a possible negative answer. Those citations are
reported as the survey's account, without claiming a new full reading
of their proofs or a verified general counterexample. No later absence
of progress is certified.

### Conjecture 3.3: sharp global d1/J comparison

On the energy-zero level I(u)=0 in E1, the normalized distance and
J functional have comparison m J(u)-D<=d1(0,u)<=M J(u)+D. The survey
conjectures the sharp lower coefficient
m_n=2/(n+1)*(n/(n+1))^n for general Kähler backgrounds. An appropriate
D is independent of u. The known upper coefficient is 2.

The independently read J paper has normalized Finsler norm
V^{-1} integral |xi| omega_u^n. Its Theorem 1.1 gives the proposed
comparison on smooth torus-invariant potentials. Its Theorems 1.3
and 5.5 give m_n J{U}<=d1(0,u_1)<=2 J{U} for all finite-energy
weak rays from zero with I(u_t)=0, without torus invariance.
Thus a radial inequality on arbitrary backgrounds is already known.
It does not give a single additive D on the whole potential space.
Sharpness for a particular fixed polytope/background must not be
inferred merely from universal extremizers across dimension n.

### Question 4.2: a description of chordal ray interpolation

Given two bounded weak rays from zero, the Darvas–Lu construction
provides a constant-speed geodesic interpolation in chordal d1.
Can this particular interpolation, or its time-Legendre dual, be
specified by an extremal problem or an equation? Chordal distance is
lim(t->infinity) d1(u_t,v_t)/t. The metric constant-speed identity
alone does not single out one d1 geodesic. The source's phrase “the
geodesic” is interpreted as the identified construction.

Survey page 8 states this as a question. Existence/completeness of
ray space already imported from Gupta does not settle it.

### Conjecture 4.3: preserving algebraic approximability

If the two endpoint rays are approximable, must the identified
chordal interpolation remain approximable at every parameter?
The source characterizes the relevant rays by I-model finite dual
slices: the envelope remembers multiplier ideals at every positive
scale, rather than only ordinary bounded-change singularity type.

Survey page 8 points to projective tools of Blum–Liu–Xu–Zhuang,
Finski and Reboulet, and emphasizes the transcendental direction.
This account is not a general interpolation-closure theorem.
Ordinary modelity in the Legendre correspondence is insufficient
to certify I-modelity or algebraic approximability.

### Question 4.4: decreasing real C1,1 approximation of rays

Does each bounded weak ray U from zero admit bounded weak rays U^j
from zero decreasing pointwise to U, with real C1,1 slices at every
finite time and chordal d1(U^j,U)->0? Both the monotone approximation
and the all-time distance conclusion are part of the question.

The survey reports decreasing bounded-Laplacian C1,bar1 approximation
under finite K-energy slope. The question removes that restriction
and asks for all-real Hessian control. Compact-time convergence
does not imply the supremum over the whole time half-line required
for chordal distance. Survey-dated status does not certify no later
solution.

### Question 5.1: uniqueness from the pointwise initial tangent

For bounded weak segments U,W on [0,a], a>0, from zero, the
pointwise right derivative exists by time convexity. Does equality
of this derivative at every x imply equality of the segments?
The ray case uses the same question for all finite intervals.

Survey page 9 states it open and reports a nondegenerate C3
foliation argument in a more regular category; its real C1,1
case is also stated unresolved. Xiao v1, Theorem 5.2, subsequently
constructs distinct bounded weak rays from zero with the same
pointwise tangent. Restriction to a finite interval where they
differ answers the bounded weak-segment question negatively.
This import does not assert that either ray is real C1,1 or smooth,
so it does not settle those more regular versions.

### Question 5.2: uniqueness from literal zero-contact sets

For normalized model potentials phi=P[phi](0), psi=P[psi](0),
both with strictly positive nonpluripolar mass, does equality
{phi=0}={psi=0} as literal subsets imply phi=psi?

Survey pages 9–10 relate the question to initial tangents.
DNT Corollary 3.4(ii) implies MA(phi)=1_{phi=0} omega^n.
The measure equivalence is exactly equality of indicators almost
everywhere, and does not supply literal equality of sets.

Xiao's Theorem 4.1 provides two different model potentials with
equal measures, zero point Lelong numbers and identical multiplier
ideals. Its contact comparison is almost everywhere. The separate
Proposition 5.1 supplies distinct positive-mass model slices with
literal contact equality at every relevant parameter and hence
answers the literal question negatively as well. The two arguments
must not be substituted for each other.

None of these descriptions creates a new inventory atom. The
September results are external known results, not solutions first
proved by this book or new VERIFIED production receipts.

## 3. Primary proof audit of the nonuniqueness construction

The source uses dd^c_source log|z|=delta_0, half the logarithmic
Fubini–Study potential, and unit volume. The book uses
dd^c_book log|z|^2=delta_0. Thus dd^c_source=2 dd^c_book, and the
book's additive potentials are twice the source's. Dual slope
parameters are doubled with time unchanged. The background current,
nonpluripolar masses and literal contact sets are unchanged.

For the survey, J paper and contact paper's i partial partial-bar
convention, choose their background Omega=2pi omega_book with the
same additive potential. Then Omega_u=2pi omega_book,u and the
normalized volume measure, normalized distance, energy and J are
unchanged. Their raw Monge–Ampère identity is divided by (2pi)^n.
This conversion differs from Xiao's fixed unit-volume convention:
there the background is kept fixed and potentials and slopes double.
The two changes of convention are not conflated.

The cap B_rho has current 1_Crho omega+rho delta_infinity.
Its two pieces have matching value and first radial derivative.
In the infinity coordinate it is rho log|zeta|^2+O(1). No boundary
current is silently added. Its positive nonpluripolar mass 1-rho
is supported on its zero-contact set. The criterion of DNT
Corollary 3.4(iv), not an unsupported modelity assertion, supplies
P[B_rho](0)=B_rho.

For a Vitali packing the finite partial sums are psh because the
negative caps are disjoint: their smooth negative curvatures remove
the background only on disjoint disks. They decrease and remain
zero on a fixed contact disk, hence their limit is not identically
minus infinity. The decreasing-limit and L1 current arguments give
the countable polar sum. Every residual atom occurs at a pole.
The missed packing set is area-null; it can contain infinity and
adds literal zeroes. This is why one packing gives measure equality
without literal contact equality.

For Theorem 4.1, the binary polar set has cylinder lengths at most
exp(-2^(3n)) and masses 2^(-n); the logarithmic potential on its
support is bounded above by -2^(2n)+log 2. Each nonfixed latitude
orbit maps this set to a polar set. The average is L1 by Fubini
and upper semicontinuous by reverse Fatou using the common upper
bound zero. To retain the canonical psh representative, one can
also integrate the local submean inequalities after adding the
fixed local background potential; this directly proves that the
pointwise average is psh. Mere upper semicontinuity plus a positive
distributional current would not suffice for an arbitrary spiked
representative, so that shortcut is not used as a general rule.

The orbit estimate gives minus infinity at every point carrying
the diffuse polar remainder. This is essential: a measure being
carried by a polar set alone would not justify discarding it for
an unspecified potential. The pushforward of an atomless angular
measure under an injective nonfixed orbit map remains atomless.
The countable weighted sum remains atomless, so all point Lelong
numbers vanish. The asserted all-scale multiplier-ideal equality
is an identified conclusion of the source, not a claim of I-modelity.
Two angular measures in arcs separated by a continuous test
function produce different polar curvature currents, hence
different potentials with the same nonpluripolar measure.

For the literal test-curve construction choose
0<delta<s0^2<T^2<1 and lambda_r=epsilon(r-s0)^2.
The source's d=h-b_delta is used only off infinity, with the psh
extension used at infinity. Its positive part is bounded by
-b_delta. The perturbation has current
1_Cr^2 omega+(r^2-delta lambda_r) delta_infinity+lambda_r nu.
Choosing lambda_r<1 leaves the infinity coefficient positive.
All finite atoms remain poles. For finite nonpoles,
q_r<= (1-lambda_r)b_r^2<0 on the negative cap; it equals zero
exactly on C_r^2. Positive mass 1-r^2 permits the same DNT model
criterion, including at r=T. This gives literal model nonuniqueness.

Parameter positivity alone would not make a test curve. The source
separately differentiates b_r^2 in the cap-area coordinate a:
b_r^2=-D(r^2||a)/2, its first derivative is -r L_r(a), and its
second is -L_r(a)-2/(1-r^2). The ratios controlling the positive
perturbation extend boundedly at a->0 and a->delta, uniformly
over r in [s0,T]. A single epsilon controls both derivatives.
It also enforces lambda<1. At s0, lambda and lambda' vanish.
At a finite polar point the parameter function is finite through
s0 and minus infinity afterward; this remains concave and upper
semicontinuous in the extended-real sense. At infinity it is
zero through parameter zero and minus infinity thereafter.
The high cutoff T is finite and included. These endpoint facts
were checked rather than replaced by finite-valued differentiation.

In book slopes sigma=2r both curves have zero contacts
P1 for sigma<=0, C_(sigma/2)^2 for 0<sigma<=2T, and the empty
set above 2T. Their inverse rays have bounds 0<=u_t,w_t<=2Tt.
The contact identity yields the direct displayed tangent
2 min(T,sqrt(q(x))), with q(infinity)=0. This is a formal reading
of the source's explicit contact filtration, not a new original
result. A finite pole distinguishes the duals at every r>s0;
Legendre bijectivity distinguishes the rays. The full pointwise
tangent fails to recover the ray even before taking its distribution.

## 4. Literal source clauses kept outside the import

The survey's printed Theorem 2.2 has a classical C2 norm but its
following text says C2 regularity fails. It is not imported as
classical C2 regularity. Its bounded-endpoint lemma references a
boundary problem whose literal display includes strict slice
positivity; the bounded Bedford–Taylor solution is semipositive,
and arbitrary bounded endpoints do not supply the strict clause.
The raw Finsler integral and probability-normalized energy in the
survey require a volume conversion; its J display omits the volume
form. The book uses the independently read normalized J paper
and never copies those displays literally.

The J paper's auxiliary Lemma 5.3 and Corollaries 1.4/5.7 omit
V^{-1} in some initial-tangent integrals. Its Theorem 5.5 proof
uses normalized integrals correctly. Lemma 5.1 has a repeated
same-ray chordal distance in one line. The negative-tail layer
cake on page 14 prints a positive threshold where -x is needed;
the immediately following explanation uses -x<=0. These
literal auxiliary clauses are not copied. No intended main
comparison theorem is refuted by recording the inconsistencies.

The contact paper uses C1,bar1 for continuous functions with
bounded distributional Laplacian. Its smooth obstacle zero
satisfies this condition; it is not a theorem that arbitrary
continuous obstacles satisfy the same contact formula.
Corollary 3.4(ii),(iv) and their proof were inspected in the
controlling preprint, not authenticated from a secondary citation
or a different edition.

The survey's claimed literal-set/measure equivalence requires
care: the independently checked density formula supplies only
almost-everywhere set equality in the reverse direction. Xiao's
single-packing example explicitly demonstrates the distinction.
Its separate perturbation, rather than Theorem 4.1 alone, supplies
the literal counterexample.

## 5. Integration and admission boundaries

Chapter 65 adds one section, four subsections and six equation
tags 65.60–65.65 after the minimum-mass discussion. Appendix L
records the source versions, actual reading, normalization and
proof boundaries. Four bibliography keys are appended; the
existing published DNT21 entry is preserved. The old formal
statements/proofs in changed files must remain byte identical.

The counterexamples have strictly positive but deficient mass,
so full-mass normalized Monge–Ampère uniqueness is unaffected.
Bounded weak rays are not promoted to C1,1 counterexamples.
No arbitrary continuous-initial-velocity spectral law follows,
nor a general NA ray identification, A2–A4 minimizer limit,
Siu division or repair of BJ's closure argument. The Rethlas
protocol exempts identified imports and explicitly identified
direct formal consequences from original-result promotion,
while retaining ordinary source and mathematical audits.
No independent model invocation or new production receipt is
claimed. The 42 complete statuses and native catalogue remain
byte unchanged; all previous frozen releases retain their hashes.

The matching cloud build has 4,303 pages, 319 cited references,
614 bibliography keys and 12,650 unique labels. The reference,
inventory, bibliography, index and PDF-navigation checks pass;
there are no compile errors, unresolved references, missing glyphs,
package/PDF warnings or overfull boxes. The underfull count remains
954. All 49 old formal blocks, including their proofs, in the two
changed TeX files remain byte identical; the complete closure has
425 active inputs, of which 423 are unchanged.

Sixteen actual final book pages were inspected: 1, 61, 67,
3469–3474, 4069–4071, 4293–4294 and 4302–4303. They include
all four pages of the new section, both provenance pages and the
new bibliography entries. Their hashes and the matching review
extract are recorded with the source closure in the integration
manifest. No new whole-book reading or isolated archive compilation
is claimed by this scoped research import.
