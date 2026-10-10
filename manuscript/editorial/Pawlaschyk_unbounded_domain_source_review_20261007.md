# Unbounded-domain Perron envelopes: comparison classes and literal source gates

Date: 7 October 2026; reading started 6 October. Baseline
`1137ce4763180560da059a1c5ff5750eef690a6d`; publication branch `work`.
`main` is `00957114db21b627e97369563032ceda9cea09c7`.

The new related source is Thomas Pawlaschyk, arXiv:2606.16584v1,
*The Perron–Bremermann envelope for q-plurisubharmonic functions on
unbounded domains in C^n*, submitted 15 June 2026, 11:30:28 UTC.
All thirteen actual pages were read as complete text and displayed in
seven sheets. Its bounded/capped existence assertions are kept separate
from the false literal uncapped uniqueness clause in Theorem 4.19(5).

The full returned Nguyen–Hung 2008 publisher PDF and a precisely selected
Słodkowski 1984 publisher sequence add 37 actual pages in nineteen sheets.
The checkpoint therefore reads fifty distinct source/page pairs on
twenty-six displayed sheets. Two additional enlarged details repeat
already-read main-paper pages 9 and 12 and add no source pages.
Fifteen exact elementary diagnostics pass. No entire external proof chain,
new original theorem, independent model call, production receipt or
canonical open-problem solution is certified.

## Exact primary files and reading scope

The PDFs are cached under
`source_material/Pawlaschyk_unbounded_domain_sources_20261006/`:

| Source | Returned layout and actual reading | SHA-256 |
| --- | --- | --- |
| Pawlaschyk 2606.16584v1 | 13 pages; all 1–13 read | `68b2b984637ca9d1fc75b333d56cde90dd05f637ba9e015d004d8c66500f7807` |
| Nguyen–Hung, AIF 58(4) (2008), 1383–1406, DOI 10.5802/aif.2388 | 25 returned pages including publisher wrapper; all read | `90ad6bddf741061caae99cba5e49d82b15ed9ead67916e025cbe310eadc12e09` |
| Słodkowski, Ann. Scuola Norm. Sup. Pisa, Ser.4, 11(2) (1984), 303–326 | 25 returned pages including wrapper; actual 1–5 and 16–22 read | `169dcf771a360867d71f14d4f1b2e12f9b5b47c0eb6a41dfe4a9992bbb4ec093` |

For both publisher files, actual page 2 is the first journal page.
Słodkowski's thirteen remaining returned pages are not declared read.
Hunt–Murray, Kalka, Bungart, Walsh, the full approximation/convex-estimate
dependencies and the Simioniuc–Tomassini 2007 preprint/2008 publication
are not acquired or read by this checkpoint. The 2026 quasi-B-regular
publication is not substituted for the separately read 2025 v1.

The main-reading record has SHA-256
`36b2aa99b730a04566a8e7456019fda035116ffd36d7442b9b9a45d3671e624b`.
The dependency-reading record has SHA-256
`7a17e2c535f4156ea9eac739c8355b71663fef711673af8341ae7dfdb797b28f`.
That second record explicitly corrects an initial notation overreading:
Definition 4.15 requires the witness to be continuous on the **open domain**,
not on its closure. An enlarged view of actual page 9 controls this
correction. The earlier immutable reading notes are retained, not silently
rewritten. The exterior-disk diagnostic uses a closure-continuous witness
and therefore remains valid under either condition.

## Scoped records

**PU01 — Exact version and reading.** The main source is the complete
June v1, with actual numbering 1–13. The publisher selections retain their
wrapper offsets and printed locators. The fifty-page reading count is
not a count of journal pages alone or a claim to read every dependency.

**PU02 — Which q-class.** Definition 2.3 on actual 2 and Theorem 2.8
on actual 3 use Hunt–Murray comparison on complex `(q+1)`-planes. A smooth
function has at most q negative complex-Hessian eigenvalues. This differs
from nonnegative sums of p eigenvalues and from the Hessian cones in
Appendix H.9. Słodkowski actual 2–5/printed 303–306 confirms the convention.

**PU03 — The Monge–Ampère meaning.** Definition 2.11 and Remark 2.12,
actual 3–4, define continuous q-Bremermann functions by q-psh and dual
`(n-q-1)`-super properties. In the C2 case the `(q+1)`-st ascending Hessian
eigenvalue is zero, so the determinant vanishes. A continuous function
with q>0 need not be psh or even subharmonic. For example the Hessian
`diag(-2,0,1)` in C³ has both required index bounds but negative trace.
The abstract's determinant parenthesis does not specify a general
Bedford–Taylor positive measure for this non-psh class.

**PU04 — Local and global comparison.** Definitions 2.16 and
Propositions 2.18–2.20, actual 4–5, distinguish comparison on all open
subsets from comparison on bounded open subsets. Almost q-Bremermann
functions give the latter; the new existence theorem uses a capped global
class. Ordinary local maximality does not control arbitrary growth at
infinity. The converse proof in 2.20 unnecessarily switches to global
maximality; a contradiction on the selected ball is the relevant local
argument. The last sentence of 2.14 must retain the qualifier “almost.”

**PU05 — The capped envelope.** Definition 3.1 and Remarks 3.2–3.3,
actual 5–6, use closure-continuous competitors below f on the finite
boundary and below M everywhere. This is a function-class condition,
not extra boundary data at every escape direction. Proposition 3.4's
bounded-cap gluing preserves M by the bounded-domain maximum principle.
Its general uncapped finiteness assertions are not certified. Proposition
3.6(1)'s proof also needs F itself to obey its cap before saying F≤P.

**PU06 — Bounded type.** Definition 4.15, actual 9, requires a negative
`PSH(D) ∩ C(D)` witness Ψ with uniform limit `-∞` outside large balls.
The `C(D)` here has no closure bar. Nguyen–Hung Definition 2.6,
actual 8/printed 1389, requires a finite negative psh witness and does not
add interior continuity. Neither condition is mere boundary regularity.
The new Proposition 4.17 writes a continuous closure extension without
assuming one; the bounded maximum argument can instead use the
nonpositive boundary upper limits of the negative witness.

**PU07 — Infinity maximum principle.** Proposition 4.17, actual 9–10,
perturbs a bounded-above q-psh competitor by εΨ, then compares on large
bounded intersections and lets ε decrease to zero. Addition of the psh
witness preserves q. This applies to bounded-above competitors, with
finite boundary upper-limit control; it does not apply to `log|z|` on an
exterior disk. Słodkowski Theorem 5.1, actual 18–19/printed 319–320,
adds the q-indices. Thus differences of two bounded q-Bremermann functions
are `(n-1)`-psh, giving bounded uniqueness by the same infinity comparison.
This is a direct formal consequence of the attributed comparison inputs,
not a new promoted result.

**PU08 — Peaks and parameter range.** The new Theorems 4.6 and 4.19,
actual 8 and 10, retain `0≤r≤q≤n-r-1` and an r-peak at every finite
boundary point. Słodkowski's Theorem 5.6, actual 20/printed 321, literally
omits the lower restriction r≤q. The printed range admits r=2,q=0,n=3
on the shell `1<|z|<2`, which is strictly 2-pseudoconvex near its boundary
but has no continuous psh extension of inner value 1 and outer value 0.
The full modern range is controlling; the old printed range is not imported.

**PU09 — Exhaustion and almost solutions.** Theorem 4.19(1–3),
actual 10–11, solves on bounded intersections with outer boundary cap M,
orders those solutions downward and retains an almost q-Bremermann limit.
A nonnegative closure-continuous q-psh extension supplies the lower
boundary bound. Disconnected intersections can be solved componentwise;
the source's notation suppresses that point. The extension lemma's
`max(Fi,0)<0` sentence is literally inconsistent; the required fact is
that the maximum equals zero near the artificial boundary.

**PU10 — Interior continuity with infinity control.** Claim 4,
actual 11–12, scales Ψ to be small near the chosen point and sufficiently
negative beyond a large ball. Translated comparison functions are glued
using finite boundary collars. The perturbation stays in the same capped
class and yields lower semicontinuity of the upper limit. Its boundary
ε/4 estimates, artificial-ball margin and local equality of overlapping
pieces must remain explicit. This is an account of the displayed proof,
not certification of all underlying q-Dirichlet inputs.

**PU11 — Continuous and USC capped classes.** Theorem 4.19(4) and
Remark 4.20, actual 10–12, identify the continuous capped envelope with
the capped USC envelope and the bounded continuous q-Bremermann solution
on a bounded-type domain. A finite cap may be replaced by the supremum
of the bounded boundary datum. This does not identify the `M=∞` envelope.
Theorem 4.19 assumes nonnegative bounded f; an additive shift treats a
general bounded real datum without removing boundedness.

**PU12 — False literal uncapped uniqueness.** Theorem 4.19(5),
actual 10, and Claim 5, actual 12, omit a bound on the competing
q-Bremermann function. Take n=1,r=q=0 and `D={|z|>1}`. The witness
`Ψ=-1-log|z|` is negative harmonic, continuous on the closure and tends
uniformly to `-∞`. For each `|p|=1`, `Re(p/z)-1` is a global harmonic
peak: negative inside, zero only at p on the boundary. Every function
`F_c=c log|z|`, c real, is continuous on the closure and harmonic in D,
with the same zero boundary trace. Hence the literal uniqueness clause
is false. The bounded solution Φ is zero. Claim 5's first step improperly
uses a bounded-above maximum principle for `F_1`; its second step assumes
`Φ+εΨ≤F_-1` at infinity, although for `0<ε<1` their difference is
`(1-ε)log|z|-ε→+∞`. This diagnoses a growth omission in that exact clause;
it does not refute bounded/capped existence or certify a general corrected
version. Nguyen–Hung Theorem 4.4, actual 17/printed 1398, expressly
restricts uniqueness to bounded solutions.

**PU13 — Arbitrary-map residual example.** The consequence in Example
2.13, actual 4, claiming `log||F||` is 0-Bremermann for every holomorphic
map is false as written. In C take `F(z)=(1,z)`. The Levi coefficient of
`log(1+|z|²)/2` is `1/[2(1+|z|²)²]>0`, so it is not 0-Bremermann.
Neither scalar nonvanishing logs nor restricted-rank examples justify
that arbitrary-map inference. This is an auxiliary example defect.

**PU14 — Literal unbounded hull.** The enlarged actual 12 detail
confirms Remark 4.21 takes the relative q-hulls of
`closure(D∩Br(0))` inside `closure(D)`. Every such compact is contained
in its displayed hull. Their union therefore already equals the whole
closure, contrary to the asserted proper inclusion. On the exterior disk,
f=0 and M=∞ give P=∞ in D from positive multiples of `log|z|`, also
contradicting the claimed hull exclusion of E∞. An intended hull of
boundary subsets is a different definition and is not silently substituted
or certified from the unread Simioniuc–Tomassini source.

**PU15 — Polynomial degree.** The bounded-type example on actual 9
and Nguyen–Hung's remark, actual 19/printed 1400, need positive polynomial
degree. The constant p=2 satisfies the printed inequality on every domain,
whereas C^n cannot carry the required negative psh witness tending to
`-∞`. The old proof itself divides by deg(p). Only a positive-degree
version may be used for these examples.

**PU16 — Jensen function classes.** Nguyen–Hung actual 4 and 12,
printed 1385 and 1393, uses bounded USC functions nonpositive at infinity
and positive regular Borel Jensen measures of mass at most one. A1 is
the compactly supported closure-continuous psh cone; A2 is the USC* psh
cone. A2 contains negative constants; A1 does not. Local peaks force a
Dirac mass at that boundary point. Neither a general probability measure
convention nor a convex fixed-q Hunt–Murray cone follows from this setup.

**PU17 — Negative-obstacle duality gate.** The literal arbitrary-cone
Theorem 3.1, actual 9–11/printed 1390–1392, fails on a one-point closed
space X with A={0} and g=-1. Its envelope is the empty supremum `-∞`,
while the infimum over subprobability masses is -1. Its proof's claim
that every Sϕ is finite lacks a negative-constant/minorant assumption.
Proposition 3.4(b→c), actual 12–13, also applies the explicitly
nonnegative-obstacle Proposition 3.3 to a negative obstacle. The audit
records these precise failures without claiming a counterexample to the
bounded nonnegative envelope existence result or a completed replacement
duality theorem.

**PU18 — Other older proof gates.** In Nguyen–Hung, actual 17–18,
the real 2n-dimensional mollifier is printed with δ^(-n), whose integral
is δ^n; a mass-one convolution needs δ^(-2n). The proof also drops the
negative ψ convolution at the fixed point without first scaling it to
an arbitrarily small value. Theorem 2.1(c), actual 5, omits negativity of
its exhaustion: `|z|²` then satisfies the literal condition even on a
non-B-regular punctured disk. Lemma 3.2's USC maximum does not establish
continuity by itself. Proposition 5.1's local-to-global normal argument
and Proposition 5.3's infinity bound for a nonproper pullback retain
separate unverified steps. These printed formulas are not reproduced as
load-bearing inputs, and no full external Jensen/transfer proof is certified.

**PU19 — Classical q comparison scope.** Słodkowski actual 16–22,
printed 317–323, reads the Peano-Hessian formulation, index-addition proof,
bounded uniqueness and Perron construction. Semiconvex approximation and
convex estimates from the unread pages remain cited inputs. Definition
5.2 limits determinant-zero to the smooth case. Proposition 1.2(i)'s
restriction direction and the final minimum-theorem proof's printed
`max` in place of `min` are literal auxiliary inconsistencies. No general
same-q convolution or full-proof certification is inferred.

**PU20 — Book interface and further directions.** A short Appendix H
connection can distinguish unbounded domains with bounded capped data
from the bounded domains with unbounded obstacles in H.10. It should
keep growth restrictions, finite-boundary peaks, the full r/q range and
the generalized eigenvalue branch separate from the p-plane Hessian class.
Uncapped growth-selected solutions, an intended boundary-hull formulation,
proper-map infinity control and the corrected negative-obstacle Jensen
interface remain literature/research directions. None changes the forty-two
canonical Chapter 72 atoms or supplies non-Archimedean envelope closure.

## Diagnostics and preservation

The successful fifteen-record diagnostic has SHA-256
`5821b63308a018509871c8d9b309d5eea2bf2ad657de6a438fb107aed38fb7eb`.
It retains exact symbolic differentiation of the log-norm pullback,
harmonic exterior family, negative witness, peak function and shell
defining function, together with growth, matrix-index and literal
set-containment checks. An initial helper compared equivalent SymPy
expressions by structural equality and stopped before creating a record;
the successful v2 changed that check to zero of their difference. Its
ten-check record is retained, and v3 adds five separately scoped older
signature/normalization checks. No successful record is overwritten.

The source-only checkpoint preserves all 425 active and 108 protected
inputs, both bibliographies, the 4,452-page generated book and index,
94 preceding frozen manifests and 163 exports. Only README and the
continuation programme change among the 5,142 baseline tracked files;
the other 5,140 retain their bytes. The native 86-page catalogue source,
PDF and open editor are untouched. Canonical statuses, tiers and all
historical proof receipts keep their scope. No new book build is needed
for this source-only checkpoint. General BJ22 homogeneous Siu/envelope
closure remains conditional.

## Publication and continuation

Fetch both main and work, publish this exact-source review normally and
update the existing draft PR. Next add only the attributed, correctly
scoped infinity-comparison interface to Appendix H and its provenance
account. Compile that subsequent manuscript edit and read matching final
pages, index and bibliography before its separate integration release.
Continue incoming author progress and recent related primary-source
research; do not promote the literal uniqueness or hull clauses, repair
an entire external proof by editorial implication, or extend a historical
production receipt to this new source audit.
