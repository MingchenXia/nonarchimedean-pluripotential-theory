# Do–Hiep local maximality and comparison: exact-source review, 6 October 2026

Two new preprints give useful complex reference material: a local-to-global
maximality theorem for locally analytic singularities, and comparison for
local Cegrell potentials with applications to residual currents in complex
dimension two. This checkpoint records their actual hypotheses and the
dependency issues encountered. It admits no original result and certifies
no complete repair of an external proof. None of the literal checks below
is a counterexample to either new main theorem.

The checked book remains the 4,426-page index-diacritics edition, work
`87ebbca13db2f0901cdfd983d3a447fa39cf07ce`; main is
`00957114db21b627e97369563032ceda9cea09c7`. This source-only checkpoint
changes no active mathematical input, bibliography, generated book product,
native catalogue/editor, canonical problem status or historical receipt.

## Exact editions and actual reading

| Source | Exact edition | Actual physical PDF pages read and displayed |
|---|---|---|
| Do–Hiep, *Local-to-global maximality for plurisubharmonic functions with locally analytic singularities* | [2610.05937v1](https://arxiv.org/abs/2610.05937v1), submitted 5 October 2026, 07:54:37 UTC | All 13 |
| Do–Hiep, *Comparison principles for local plurisubharmonic potentials on complex manifolds and applications* | [2610.05948v1](https://arxiv.org/abs/2610.05948v1), submitted 5 October 2026, 08:03:58 UTC; internal date 3 October | All 19 |
| Błocki, *On the definition of the Monge–Ampère operator in C²* | [Author-hosted published PDF](https://gamma.im.uj.edu.pl/~blocki/publ/defc2.pdf), Math. Ann. 328 (2004), 415–423; [DOI](https://doi.org/10.1007/s00208-003-0491-0) | All 9 |
| Lejeune–Jalabert–Teissier, *Clôture intégrale des idéaux et équisingularité* | [Published 2008 PDF](https://www.numdam.org/item/AFST_2008_6_17_4_781_0/), reused exact cached PDF with cover | 1, 20–26, 29–33: 13 selected pages of 80 |
| Do–Hiep, *Comparison principles for Monge-Ampère measures on pluripolar sets* | [2604.19347v2](https://arxiv.org/abs/2604.19347v2), submitted 3 October 2026, 03:44:33 UTC; internal date 6 October | All 14 |
| Same polar comparison paper, version cited by the new papers | [2604.19347v1](https://arxiv.org/abs/2604.19347v1), submitted 21 April 2026, 11:30:43 UTC; internal date 22 April | 1–2, 6–8: 5 selected pages of 14 |
| Åhag–Cegrell–Czyż–Pham, *Monge-Ampère measures on pluripolar sets* | [0706.0169v3](https://arxiv.org/abs/0706.0169v3), distinct from the published 2009 layout | 1–2, 8–10: 5 selected pages of 16 |

Thus **78 distinct edition/page pairs** were read as complete selected text
and actually displayed in **42 sheets**. Four PDFs were read in full; three
further PDF editions have selected reading only. Acquiring a PDF or comparing
its extracted text is not counted as reading it. A full-page text comparison
of the polar paper's v1 and v2 finds only physical page 1 different; it does
not turn the five-page v1 reading into a full v1 reading.

McAdam's *Asymptotic prime divisors and analytic spreads*, Proc. Amer.
Math. Soc. 80 (1980), 555–559, has exact
[DOI 10.1090/S0002-9939-1980-0587926-0](https://doi.org/10.1090/S0002-9939-1980-0587926-0).
Crossref metadata were checked. Attempts at both original AMS PDF paths and
the publisher page returned access failures; **no original McAdam PDF or
proof was read**. Its integral-closure/associated-prime theorem remains an
explicit external input. No full fresh reading of Siu, normal-space psh
extension, Cegrell's weighted convergence, CKZ05, NP09 or Vu's local-current
calculus is claimed.

## Main-paper scope and dependency diagnostics

**D01 — 2610.05937v1, Theorem 1.1 and Corollary 1.4, pages 1–2, 12.**
The domain is an open domain in Cⁿ, n ≥ 2. Locally analytic singularities
mean u = c log|I| + O(1) with c > 0 and a two-sided locally bounded
remainder. Local maximality then implies global maximality. The criterion
combines zero ordinary Bedford–Taylor mass off the pole set with analytic
spread ℓ(I_z) < n at pole points. Zero nonpluripolar mass alone omits the
second condition. For the principal divisor case, spread one is strictly
less than n; this argument has no dimension-one extension.

**D02 — 2610.05937v1, Lemma 2.6, pages 5–6; McAdam dependency.**
The full-spread obstruction needs the maximal ideal in the associated
primes of some integral-closure power. A germ g outside that closure,
but with each z_j g inside it, yields |z||g| ≤ A|I|ᵏ and an annular
psh competitor. Maximality would force g back into the closure. The
analytic criterion is source-supported by the selected Teissier pages;
the McAdam implication is attributed external input, not a freshly
verified original algebraic proof.

**D03 — 2610.05937v1, Lemma 2.7 and Proposition 1.2, pages 6–11.**
Local coefficients need not initially agree. On overlapping pole germs,
generic-line vanishing orders make their ratios rational. Clearing
denominators and taking integral closures produces coherent ideal data
on finitely many relevant charts. Nonpole overlaps are unit-ideal
overlaps. The proof does not assume one globally defined holomorphic
map or one initially global coefficient.

**D04 — 2610.05937v1, normalized blow-up argument, pages 9–11.**
The normalized blow-up principalizes the glued ideal and its fibres
have dimension ℓ(I_z) − 1. Under ℓ < n each relevant exceptional prime
has positive-dimensional image. A further resolution can introduce
exceptional primes over points; the spread bound must not be silently
transported to every divisor on an arbitrary resolution. The total
principalized ideal divisor is Cartier, although its individual prime
components need not be Cartier.

**D05 — 2610.05937v1, pages 10–12.**
The generic Siu coefficients are determined on a nonempty open part
outside the competitor's compact support. Normal-space psh extension
and subtraction of the effective real Cartier divisor provide residual
potentials. The u-residual has two-sided bounds; the competitor's
residual has local upper bounds. Compactness of a blow-up fibre then
gives a local upper bound on v − u. The final scalar comparison uses
(1 + ε)v for negative potentials and takes ε ↓ 0. Normal psh extension
and classical complex Siu theory remain cited inputs.

**D06 — 2610.05948v1, Definition 1.1 and Theorem 1.2, pages 2–3.**
Local E-potentials u_j and v_j have the **same pluriharmonic transition
functions**. Boundary auxiliaries h_k,j increase to zero almost
everywhere. The functions max(u_j, v_j + h_k,j) must again have the
common transitions. Locally chosen auxiliaries do not automatically
give this gluing condition. These are hypotheses on a pair of
currents in one potential class, not a comparison for arbitrary
positive currents in arbitrary classes.

**D07 — 2610.05948v1, Theorem 1.2, pages 3, 10–13.**
With A = {u < v}, E = {u = v = −∞}, R = D max(u,v), T = Du,
S = Dv, and D = (i/π)∂∂̄, the weighted inequality retains both
∫_E(−φ₁)Rⁿ on the left and ∫_E(−φ₁)Tⁿ on the right, as well
as the nonpolar difference term and integrals over A. Differences
are set to zero at common poles only in that difference term.
Extended nonnegative integrals are not cancelled before localization
gives finite polar masses. D is twice the book's ddᶜ; alternatively
one scales every potential by two. The factorial and all operator
normalizations must be kept together.

**D08 — 2610.05948v1, Lemma 3.2 and Proposition 3.3, pages 7–11.**
The compact-support ordered comparison first treats bounded v − u,
using truncations and the positive energy measure of the difference.
Its trace is nonpolar because a smooth factor has zero polar mass
and ACCP's polar Hölder estimate applies. Cutoff gradients cancel
under the shared transitions. The general compact case follows
through max(u,v − t) and full local Cegrell convergence. This route
does not require the polar paper's general mixed capacity theorem.

**D09 — 2610.05948v1, Theorem 1.3 and Examples 4.6–4.7, pages 3, 14–16.**
Domination uses a global psh ρ in E_loc with full Monge–Ampère
measure at least f dV, f > 0 almost everywhere. A globally strictly
psh function is stronger. On the blow-up of a ball, |π|² has
positive density off its exceptional curve, which has volume zero,
while that compact curve prevents global strict psh functions.
Conversely P¹ × C has distinct compactly differing potentials
|z|² and max(|z|²,1), both with zero top mass. Omitting the density
input would invalidate that broader domination statement. These
are the source's examples, not new examples promoted as research.

**D10 — 2610.05948v1, Theorem 1.5 and its proof, pages 4, 16–18.**
In dimension two the hypotheses sandwich u and an analytic potential
φ using a local ψ ∈ E: φ + ψ ≤ u and u + ψ ≤ φ. The surface
factorization f = h₀g separates the divisor from isolated residual
zeros. Błocki's two-dimensional Sobolev criterion controls the latter,
and excludes additional divisorial Lelong numbers in ψ. The residual
current T_u = Du − S_u is positive and has local E-potentials.
Its **full** Cegrell square, including polar mass, is a globally
well-defined Radon measure. The criterion is global maximality ⇔
local maximality ⇔ T_u² = 0. Residual potentials are obtained from
current subtraction, not from the undefined value −∞ − (−∞).
There is no claim that arbitrary higher-dimensional Siu residuals
belong to E, nor a non-Archimedean Siu/envelope closure repair.

**D11 — Błocki04, Theorems 1.1 and 4.1, physical pages 1, 9.**
The identification of the local operator domain with psh W¹,² is
specific to C². The source's Kiselman example is W¹,² in dimensions
n ≥ 3 and still outside the operator domain. Błocki uses
D_B = 2i∂∂̄ = 4π ddᶜ_book = 2πD. Its constants cannot be
copied into either new paper without rescaling.

**D12 — Błocki04, proof of Theorem 3.4, physical page 6 / printed 420.**
The displayed lower estimate with a −Cε² error suppresses the
linear mixed term. For the same nontrivial relative extremal w in
both positions and a negative test ψ with A = ∫ψ(D_Bw)² < 0,
the weighted change is (2ε + ε²)A. It cannot be bounded below
by −Cε² uniformly as ε ↓ 0. The mixed term must remain; an
O(ε) estimate requires its own uniform bound. This checks a
printed intermediate estimate, not the validity of Theorem 1.1
or a complete revised proof of Theorem 3.4.

**D13 — Błocki04, proof of Theorem 3.5, physical page 8 / printed 422.**
The equality replacing v_j − v_k by v_j − u_j is justified only
on the inner ball B₁, where u_j = v_k. It is printed over B₂.
The usable chain first integrates on B₁, substitutes there, then
uses positivity to bound that energy by the B₂ energy. No
identity of the two differences outside B₁ is supplied.

**D14 — Lejeune–Jalabert–Teissier08, Lemma 2.4, physical page 22 / printed 801.**
Perturbing only the first coordinate by t^(α+1) need not make
q∘h nonzero. For p = z₁, q = z₂, and the arc (t,0), the
printed perturbed arc (t+t²,0) still has q∘h identically zero.
A suitable coordinate or generic transverse direction is needed.
This literal construction failure does not refute the integral
closure criterion used for complex analytic ideals.

**D15 — Lejeune–Jalabert–Teissier08, cusp illustration, physical page 30 / printed 809.**
For A = C{t²,t³}, U ↦ t²T, V ↦ t³T, the kernel cannot be
generated just by t³U − t²V as printed. The relation
V² − t²U² maps to zero, while every multiple of the proposed
generator has its V² coefficient in (t²); the displayed relation
has coefficient one. Further relations are needed. The stated
non-normality is still witnessed by the integral element t = V/U.
The selected analytic spread and normalized blow-up statements
are not refuted by this example.

**D16 — 2604.19347v2, Example 2.10, physical page 5.**
For ψ = −(−log|z|)^a, 0 < a < 1, on the unit ball, the radial
mass of B_r is proportional to [a(−log r)^(a−1)]ⁿ. It tends
to infinity as r ↑ 1. Thus the printed global Fᵃ membership
does not follow and is false on that ball, although local Eᵃ
membership and the vanishing local capacity tail hold. Also
ψ ≤ φ gives ψ ⪯_Cap φ, not the reversed relation printed in
one sentence. The subsequent conclusion φ not ⪯_Cap ψ
is consistent with the logarithmic pole example.

**D17 — 2604.19347v1/v2, Lemma 3.2, physical pages 6–7.**
If v_t = max((1−ε)φ−t,−2t/ε), then
v_t+t = max((1−ε)φ,−t(2/ε−1)). The following page instead
retains −t in the first argument while changing the second.
That is not a constant translate of v_t. The capacity bound
must use the correctly translated bounded psh function. The
working range is 0 < ε < 1 and t > 0; the endpoint wording
needs separate treatment. For ε = 1/2, t = 1, φ = −5,
the correct bounded function has value −5/2, whereas the
printed one has value −3.

**D18 — 2604.19347v2, Lemmas 3.3–3.4 and Theorem 1.2, physical pages 7–8, 12–13.**
Definition 1.1 uses a **liminf**, visible as an underlined lim.
One must choose a vanishing t-sequence; independent liminf
sequences cannot simply be added. A local capacity condition
also does not immediately give a global tail bound in Lemma 3.3.
The compact polar restriction/envelope localization is required.
The new 2610.05948v1, pages 6–7, supplies explicit localization
and the strict-to-nonstrict set step. For general mixed
polarization, positive-addition closure and finite compact polar
integrals must be justified before coefficients are compared.
Theorem 1.2 cites Lemma 3.5, which **does exist later**, but
its proof uses Theorem 1.2; the scalar Lemma 3.4 is the
noncircular intended input. Theorem 1.7 also cites its (i)⇒(ii)
where the already preceding ordered Lemma 3.5 (ii)⇒(i) is
needed. No arbitrary-function preorder or complete mixed
capacity proof repair is certified here.

**D19 — 2604.19347v2, Theorem 1.3(ii), physical page 10; Theorem 1.5(ii), page 11.**
The envelopes u_j for u ∈ N increase to zero quasi-everywhere;
they are printed as decreasing to u. More seriously, one
intermediate comparison on page 10 drops the common-pole
mass from the right side. In dimension one take φ = ψ =
log|z| on the unit disk, boundary auxiliary u = 0, negative
constant weight −1, and a positive ε. Then A_j is empty
but the retained left common-pole term is a positive atom;
the displayed first right side is zero. The polar term must
remain before cancellation. This is a counterexample to that
intermediate line, not to the final comparison inequality.
The new 2610.05948v1, pages 12–13, retains both polar terms
and auxiliaries increasing to zero.

## Integration boundary and preservation

The immediate book candidate is an attributed complex-reference
subsection: analytic spread on the normalized blow-up, the two-sided
surface E-sandwich, and the distinction between full residual mass
and a nonpluripolar product. The compact-support comparison route
can be explained with its shared-transition and positive-density
hypotheses. The general mixed capacity theorem is not imported
as a newly certified black box.

All **425 active inputs**, **108 protected inputs**, both bibliographies,
all generated book/index files, **85 preceding frozen manifests** and
**148 preceding exports** retain their bytes. Only README and the
research programme change among the 5,113 tracked baseline files;
5,111 retain their bytes. The native catalogue source/PDF and open
editor are preserved. There is no fresh book build, final-book page
review or native compilation in this research-only checkpoint; its
unchanged book reuses the preceding checked artifact.

The manifest pins exact acquisition records, all selected images/text,
the 19 scoped records and direct elementary checks. No model call,
production verifier, verification receipt, canonical problem addition,
status promotion or extension of a historical receipt is claimed.
BJ22 Theorem 6.21's proof gap remains distinguished from a false
statement; general Siu/envelope closure remains conditional.

Save the immutable audit manifest, fetch main and work, push normally
on work and update the existing draft PR under standing authorization.
Then integrate the scoped complex material and build/read its final
pages; keep researching related recent sources and incoming author work.
