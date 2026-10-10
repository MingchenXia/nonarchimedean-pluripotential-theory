# Special Fujita approximation: full source and selected dependency review

**Research-only checkpoint.** This review does not admit a new theorem,
a repaired full proof, an entropy-regularization theorem or a YTD theorem
into active TeX. The baseline is
`7e4dc1a2496198c8a92909a6a7e56446c70b3a73`.
The controlling primary source is Antonio Trusiani,
*A solution to the Yau-Tian-Donaldson Conjecture through Special Fujita
Approximations*, with an appendix by Sébastien Boucksom,
[arXiv:2605.30063v2](https://arxiv.org/abs/2605.30063v2).
The official version history gives 17 August 2026, 08:55:46 UTC for v2
and 28 May 2026, 15:13:52 UTC for v1. Every one of the 25 actual PDF
pages, the complete extracted text, proofs, appendix and references was
read; all pages were displayed in thirteen sheets. The source file was
reused byte-for-byte from the preceding selected review. That preceding
review covered pages 1–6 and 16–19; the present reading additionally
covers pages 7–15 and 20–25 and freshly displays all 25 pages.

The controlling PDF has 511,182 bytes and SHA-256
`aa00afeb58947e0f839d5f1af752c83c429b407d387166b624cb3f6315589712`.
The full-reading record is
`source_material/special_Fujita_full_review_20261006/full_reading_v1_20261006.json`,
SHA-256 `b9a1f7856f4d59afdc74be84a3bbff3dac1f7b0b7c4e1d4cada8f0c9d5e1976c`.
The [manifest](special_Fujita_source_review_manifest_20261006.json)
embeds source evidence and preservation checks. Historical acquisition
and preparation records retain their original flags.

## Claimed results and categories

Theorem B, on page 2, concerns a big line bundle on a smooth complex
projective variety of positive dimension. It claims ample rational
approximants on smooth blowups, effective fixed parts, convergence of
top volumes, and convergence of canonical intersections to the positive
product paired with the canonical divisor on the original variety.
It also claims a compatible construction for a linearized reductive
group action. Ordinary Fujita top-volume approximation alone does not
supply the canonical-intersection limit.

Corollary A, on page 3 and proved on page 16, applies this construction
to big models whose generic polarization is ample. It claims an
approximation by ample test configurations with strong and entropy
convergence. The ample generic polarization must remain the same
throughout the construction. Theorems A and C and Corollary B then use
additional analytic and stability inputs. The weighted statements use
positive weights on a compact moment polytope and an extra
log-concavity assumption on the weight in the existence argument.
The present review does not verify those entire analytic chains.

Appendix Theorem A.3 has a separate signature: a smooth projective
variety with an ample polarization over `K=k((t))`, with `k`
algebraically closed of characteristic zero. Its Monge–Ampère measures
are probability measures. Entropy is relative to a reference model
metric on the canonical bundle. Proposition A.6 first treats the
envelope of a metric on a specified snc model, using its complete base
ideals. The reduction from all finite-energy metrics is a separate step.
This discretely valued argument is not a proof of the book's general
trivially valued Siu or closure input.

## Selected primary dependencies: 55 actual pages

Every selected page was displayed and its extracted passage read, in
twenty-seven main sheets and one supplemental sheet. This is not a full
reading of any of the five dependency papers. The two supplemental DEL
pages contain the restriction statement used by its diagonal argument;
the external proof of restriction is not freshly audited here.

| Controlling edition | Actual PDF pages | Checked use |
| --- | --- | --- |
| Demailly–Ein–Lazarsfeld, `math/0002035v2`, 17 April 2000, 17:09:29 UTC | 1, 4–8, 10–17 | Restriction statement, Nadel vanishing and uniform generation, asymptotic ideals, subadditivity and the complete displayed proof of Theorem 3.2 |
| Chi Li, *K-stability and Fujita approximation*, `2102.09457v1`, 18 February 2021, 16:21:56 UTC | 1, 4–13 | Big models, finite envelope support, logarithmic canonical correction, strong convergence and the first Riemann–Roch coefficient condition |
| Chi Li, *Geodesic rays and stability in the cscK problem*, `2001.01366v4`, 29 March 2021, 14:10:30 UTC | 1, 33–38 | Proposition 6.3 and its proof, the two-stage entropy-density reduction, and the conditional model-regularization step |
| Boucksom–Favre–Jonsson, *Singular semipositive metrics in non-Archimedean geometry*, author-hosted prepublication PDF | 1, 45–49, 52–58 | The discretely valued signature, full displayed proof of Theorem 8.5, decreasing nets, and Appendix B vanishing and multiplier-ideal inputs |
| Boucksom–Jonsson, *The Yau–Tian–Donaldson conjecture*, `2509.15016v1`, 18 September 2025 | 1, 31–36, 63–65 | Lemma 4.8 and its proof, entropy on dual complexes, and Proposition 7.14 with Lemmas 7.15–7.17 |

The exact files are the versioned
[DEL](https://arxiv.org/pdf/math/0002035v2),
[Li–Fujita](https://arxiv.org/pdf/2102.09457v1),
[Li–geodesic](https://arxiv.org/pdf/2001.01366v4) and
[BJ](https://arxiv.org/pdf/2509.15016v1) PDFs, and the archived BFJ
author file already used in the Chapter 63 audit. Its placeholder JAG
copyright/pagination identifies an author prepublication edition;
published page numbers are not substituted for its actual PDF locators.
The Li–geodesic PDF has 45 actual pages, although its official arXiv
comments say 44. The files, hashes and page selections control this review.
DEL Proposition 3.6 continues on unselected page 18, and BFJ Lemma 8.9
continues on unselected page 50; their complete proofs are not claimed read.

The selected-reading record is
`source_material/special_Fujita_dependencies_20261006/selected_reading_v1_20261006.json`,
SHA-256 `840b3a5147d40bd72cc765eafbde396c66a764b2e4521b731590fc931d7e225a`.
The earlier BFJ09, ELMNP and BHJ selected dependency reading is reused
as recorded in the big-class stability audit. Lazarsfeld's books,
all non-Archimedean Calabi–Yau dependencies, the Han–Liu weighted
regularization inputs and the full analytic YTD chains remain outside
the present complete-reading claim.

## Proof structure supported by the reading

The useful separation is between top volume, the trace of a fixed divisor,
relative discrepancy, and entropy. Trusiani Lemma 4.3 on page 14 contains
a route to convergence against each fixed ample divisor: apply volume
differentiability and the algebraic Morse inequality to dominated nef
approximants whose top volumes converge. Writing a fixed Cartier divisor
as a difference of ample divisors then gives its trace convergence.
This uses the precise BFJ09 big-cone inputs already selected and checked;
it does not use the invalid scalar-supremum formula discussed below.
The remaining special condition is the vanishing of the intersection
against the relative canonical divisor.

For base ideals `a_m` and asymptotic multiplier ideals `b_m`, page 15
uses uniform generation with a fixed auxiliary divisor, together with
subadditivity, to bound `v(a_m)-v(b_m)` by twice the value of one fixed
ideal for all sufficiently large `m`. This is a uniform fixed-error
estimate, not entropy convergence by itself. Rees discrepancies then
convert that error into an intersection estimate. Orthogonality on the
augmented base locus is the final vanishing input.

Appendix Proposition A.1 on page 18 gives an independent algebraic
argument for the Rees discrepancy estimate. It works on the normalized
blowup and bounds discrepancies on its Rees divisors, using relative
generation at generic points and multiplier-ideal subadditivity.
It is not a coefficientwise bound on all divisors of every higher
resolution. Its extension in Remark A.2 is in the regular vertical
ideal setting over `k[[t]]` and invokes BFJ Appendix B.

BFJ Theorem 8.5 on actual pages 47–48 proves uniform approximation by
the full base-ideal sequence for a continuous model obstacle in its
nontrivially discretely valued, residue-characteristic-zero setting.
The proof uses a fixed auxiliary twist and multiplier ideals to obtain
a uniform error tending to zero. The whole integer sequence need not
be monotone. BFJ Theorem 8.7 uses a decreasing net; Corollary 8.8 supplies
uniform sequential approximation for continuous metrics.

Li Proposition 6.3 uses two stages: retract a finite-energy measure to
dual complexes and solve the corresponding Monge–Ampère equation,
then approximate such solutions by model envelopes. Entropy converges
because discrepancy is continuous on each fixed dual complex.
BJ Proposition 7.14 uses the weighted version of the same separation.
It requires the weighted Calabi–Yau homeomorphism, support/retraction
properties and continuous potentials on the complex; those prerequisites
are not cleared merely by reading its short density proof.

For a fixed model envelope in Appendix A.6, uniform convergence gives
weak convergence of Monge–Ampère measures. Lemma A.7 on page 21 bounds
the difference of logarithms of graded and antigraded ideals by a
fixed model function. Finite envelope support outside the augmented
base locus makes the integral of the limiting error zero. Thus the
method needs support information and discrepancy control in addition
to ordinary uniform or strong convergence. When using A.7 without an
explicit zero-index ideal convention, the strict range `m>m_0` avoids
the endpoint in the printed formulation.

## Literal source defects and unverified steps

These observations distinguish a false intermediate formula or an
unsupported printed step from a counterexample to a corrected main
theorem. No such main-theorem counterexample is claimed.

1. **An effective divisor is not an order-preserving scalar test.**
   Trusiani page 7 writes the pairing of the positive product with an
   arbitrary effective divisor as the supremum of its pairings with
   dominated nef approximants. Li–Fujita Definition 2.5, equation (11),
   on page 6 uses the same formula. On the blowup of the projective plane
   at one point, let `H` be the pullback of a line and `E` the exceptional
   curve. Then `H` is big and nef and `H·E=0`. For rational `0<ε<1`,
   `P=H-εE` is ample, `H-P=εE` is effective, and `P·E=ε>0`.
   These standard surface intersections diagnose the printed supremum
   formula. They are not an original theorem or a claimed counterexample
   to special Fujita approximation. The fixed-divisor trace route in
   Lemma 4.3 must replace this scalar-supremum justification where used.

2. **The analytic Rees proof has a normal-direction problem.**
   Pages 11–12 claim that the blowup map is injective on normal vectors
   along a Rees divisor, so that adding its pulled-back Kähler form makes
   a proposed form Kähler near that divisor. The normalized blowup of
   the local ideal `(x^3,y^2)` has Rees weights `(2,3)`; at a generic
   smooth point of its exceptional divisor both pulled-back coordinates
   vanish to order at least two. The differential of the map is zero
   there, and rescaling the pulled-back form cannot supply the asserted
   normal positivity. The displayed volume comparison using that form
   is therefore not cleared as printed. Appendix A.1 provides a separate
   algebraic route; failure of the analytic step does not refute its bound.
   The omitted negative term in the `dd^c` calculation on page 12 also
   calls for an inequality rather than the displayed equality.

3. **Canonical pullbacks require a definition on the intermediate model.**
   Page 15 writes pullbacks of the canonical divisor of a normalized
   blowup without establishing that it is rational Cartier.
   Intersection against nef Cartier classes and pushforward of canonical
   Weil cycles offer a way to formulate the required projection argument
   without that assumption. The precise cycle formulation and all its
   hypotheses must be supplied before describing a repaired proof as
   certified. This checkpoint records the route rather than admitting
   an original complete repair.

4. **The displayed ample total-space class lacks a base contribution.**
   In the page 16 proof of Corollary A, a class consisting of a pullback
   from `X` minus exceptional classes is called globally ample. On a
   product section avoiding the blowup centres its degree is zero.
   An appropriate positive base twist is needed for global ampleness.
   Subsequently subtracting the twist and perturbing the moving class
   must preserve the original generic polarization; vertical fixed
   parts and a suitable vertical auxiliary class are essential.

5. **Finite support has a normalization typo in the cited proof.**
   BJ Lemma 4.8, actual page 35, writes
   `L_ε=(L-εA)/(1+ε)` and calls it a test configuration for the same
   generic `L`, although both original generic restrictions equal `L`.
   The displayed restriction is `(1-ε)/(1+ε)L`. Replacing the denominator
   by `1-ε` retains the desired polarization and uniform convergence
   for small positive `ε`. Its augmented-to-diminished-base-locus argument
   still depends on the stated envelope and orthogonality inputs.
   Neither that typo correction nor its selected proof supplies the
   missing general Siu/closure input.

6. **Whole-sequence monotonicity cannot be inferred from graded ideals.**
   Li–Fujita's Dini step on pages 7–8 needs a divisibility subsequence
   or a different uniform-approximation argument. BFJ Theorem 8.5 supplies
   the latter in its stated category. Li's page 8 energy sum also has
   an extra terminal index producing a negative exponent; the standard
   mixed-intersection formula ends at the dimension.

7. **Selected inputs do not certify every printed antecedent.**
   BFJ Appendix B.3's proof on actual pages 54–55 uses a nef assertion
   stronger than its displayed `L-D` positivity hypothesis at that point.
   A covering or coefficient-reduction step must be made explicit if
   that line is used. The known vanishing statement is not declared
   false. Similarly, an unrestricted supremum of rational piecewise
   linear functions need not be a finite piecewise linear function;
   the toric passage in Li–geodesic page 38 needs its finite polyhedral
   model data. Neither observation licenses a full-chain failure claim.

## Research directions and preservation

Useful follow-up work is to write the fixed-error argument with explicit
graded/antigraded conventions; formulate the canonical-intersection
estimate using Weil cycles; check the relative ample perturbation while
fixing the generic polarization; and separately audit the remaining
Calabi–Yau, envelope/support and weighted analytic inputs. Page 6 also
identifies algebraic comparisons between stability notions,
transcendental extensions and singular/moduli questions. A cited
transcendental item marked “to appear” has not been acquired and is not
treated as established evidence. These are source-level research leads,
not new rows or solved entries in the canonical inventory.

All 425 active inputs, 108 protected inputs, 53 prior frozen manifests,
106 prior exports and 5,020 other tracked baseline files retain their
bytes. The book remains the checked 4,382-page edition; this source-only
checkpoint makes no fresh unchanged-book compilation, PDF-review or
isolated archive-build claim. The native catalogue stays open and
unchanged. All 42 canonical statuses, the open toric candidate and the
general Siu/closure boundary retain their scope. No original result,
independent production model call or verification receipt is claimed.
