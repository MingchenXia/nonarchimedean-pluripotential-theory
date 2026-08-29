# Independent hostile audit: P17.1 closed-immersion finite-level reduction

Date: 29 August 2026

Status: **FAIL (repairable; quarantine must remain).**

This is a read-only audit of the frozen candidate theorem.  It does not alter the
statement, proof, live manuscript, open-problem inventory, or verified-results
ledger.  The algebraic Segre--Veronese reduction is correct.  The final
``Consequently`` clause is not correct as written because its Monge--Ampere
quantity is not type-defined under the hypotheses actually stated.

## Exact bytes audited

~~~text
3ad32111cfa564815c91dfa9aad30070495611b9f59bb677e2d0050820e38dfb  p171_closed_immersion_reduction_statement_20260829.tex
f43c83f12b738b60f26e534989552805d812126bfb3b4a9fdfc177eb9b020e13  p171_closed_immersion_reduction_proof_20260829.tex
c609c772b64f18518e51b6d7df02c0163b4cf3cd1552699791f30a10fd0f4835  p171_closed_immersion_reduction_compile_20260829.tex
77c48309e0a56f0c7281933eb463f156a1ac35f9bf2fa22cc9c089ca8b18f183  research_memo_20260829.md
b9b3b5a507977d28c87d268e3a47647ae566b1ab983716cd65c3f53a28f713cd  packet_manifest_20260829.md
~~~

The two theorem files were rehashed after the audit and remained byte-identical.

## Counts

- critical statement errors: **1**;
- mathematical proof gaps after imposing the missing source hypotheses: **0**;
- source/citation defects: **2**;
- defects in the Segre--Veronese construction or max identity: **0**;
- overclaims that P17.1 is solved: **0**.

## Critical statement error

Statement lines 49--56 assume only that `A` is a Banach ring and `X/A` is
projective, and then display an `n`-fold mixed Monge--Ampere measure.  These
hypotheses neither make every complete-residue-field fibre `n`-dimensional nor
even attach a geometric meaning to the integer `n` other than the number of
listed line bundles.  Thus the displayed quantity is not defined in the cited
Pille--Schneider framework.  For example, with `A=K` a complete field,
`X=Spec K`, and one listed line bundle, the claimed one-fold top-degree
Monge--Ampere measure is outside the dimension-zero definition.

This is not a merely cosmetic omission.  Pille--Schneider, Definition 4.8,
assumes an **integral** Banach ring and an **n-dimensional** projective
`A`-scheme before defining the family of `n`-fold Monge--Ampere measures;
Question 4.9 adds **flatness**.  The research memo records those hypotheses
correctly at lines 79--96, but the candidate proposition drops them.

The smallest P17.1-compatible repair is to replace statement lines 49--51 by
the following hypothesis sentence (with the existing finite-level conclusion
then unchanged):

> Consequently, in the setting of Pille--Schneider, Definition 4.8 and
> Question 4.9, let `A` be an integral Banach ring, let `X/A` be a flat,
> n-dimensional projective scheme, let `L_1,...,L_n` carry tropical
> Fubini--Study metrics `phi_1,...,phi_n`, and let `psi` be a DFS function.

If one deliberately wants a theorem independent of P17.1, the logically minimal
replacement is instead to assume explicitly that every analytic fibre under
consideration is `n`-dimensional.  The source-compatible formulation above is
preferable because it removes any ambiguity about the target scope.

## Audit of the retained mathematics

Subject to that repair, the proof genuinely establishes only a finite algebraic
expansion and does so correctly.

1. Statement lines 7--40 and proof lines 7--35 are valid over an arbitrary
   scheme.  The basepoint-free sections give `f_s`; the graph of `f_s` is closed
   because projective space is separated; the other factor is the fixed closed
   immersion followed by the degree-`m` Veronese immersion; and Segre gives the
   coordinate family `s_j t^alpha` on `m(L+H)`.  Redundant source sections cause
   no problem.
2. Proof lines 37--57 prove the max identity exactly.  The pure powers `t_k^m`
   give equality, not merely an inequality, and arbitrary real weights are
   carried unchanged.
3. Pille--Schneider, Definitions 2.13 and 2.15, justify the global FS and DFS
   presentations used at proof lines 59--67.  A DFS function is a difference of
   FS metrics on line bundles whose difference is `O_X`; the proof explicitly
   fixes the required isomorphism.  The two defining exponents need not agree:
   the first part is applied separately and the same metric `eta` can still be
   added to both.
4. Proof lines 69--84 are the formal `2^n`-term expansion supplied by
   Pille--Schneider, Proposition 4.2 (equivalently Boucksom--Eriksson,
   Proposition 8.5).  Every positive metric occurring in every expanded slot is
   indeed induced by a closed-immersion system.
5. Proof lines 85--89 are valid by Boucksom--Eriksson, Theorem 8.16, formula
   (8.9): the difference between the two Deligne metrics equals the integral of
   the metric difference against the mixed Monge--Ampere measure.  That theorem
   applies to continuous dpsh metrics on an arbitrary n-dimensional projective
   scheme over every complete valued field, including a trivially valued field,
   and retains the generic lengths in the top-dimensional fundamental cycle.
6. Proof lines 91--96 assert only uniformity of the finite combinatorial
   expansion.  All section systems and weights are global over `A`, closed
   immersions survive arbitrary base change, and the finite index set and signs
   are independent of the Berkovich point.  The proof does **not** infer
   continuity of the individual fieldwise Deligne weights.
7. The scope firewall in statement lines 65--71 is accurate.  Nothing here
   constructs a relative Chow/resultant section, identifies its field fibres,
   proves its norm comparison, or assembles the weights continuously.  Hence the
   candidate does not settle Question 4.9 or P17.1.

## Source and citation audit

The following frozen primary sources were checked:

~~~text
68d1bf470a78d4021e126ec1d491ad002cb64a1689d06beec3dd3fc9f9dee71e  PS23Hybrid.pdf
51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2  BE_1805.01016.pdf
89828d2fe257736d0a51d8152d47b29ba0da207b61f6e04137fd9f28f89d5b1f  ChenMoriwaki2103.15646.pdf
4978bf5a6b0b09dbb43a273fe0eba1e2368ce60b9f78730e567f59d605be0b44  ChenMoriwakiIntersectionAccepted.pdf
~~~

The Pille--Schneider anchors in research-memo lines 113--128 are accurate:
Definitions 2.13 and 2.15 give tropical FS and DFS metrics, Theorem 2.16 gives
global DFS density, Definition 4.8 defines the fibrewise family under the
integral/n-dimensional hypotheses, Question 4.9 adds flatness, and its following
paragraph plus Lemma 4.10 give the DFS/FS reduction.  Proposition 4.2, omitted
from the memo's short ledger, is the exact source for symmetry and
multilinearity used by the candidate.

The Chen--Moriwaki claims are mathematically accurate but the edition labels
must be made fully explicit:

- arXiv 2103.15646v1: resultant Definition 1.6.3; dimension-zero Example
  1.6.4; normalized scalar Definition 1.6.7; field-base-change Remark 1.6.8;
  nontrivially valued closed-immersion formula Theorem 3.8.7; trivially valued
  formula Proposition 3.9.3; Proposition 3.9.7 is only the stated regular-curve
  special comparison;
- the frozen later author-hosted revision: resultant Definition 1.6.4;
  dimension-zero Example 1.6.5; normalized scalar Definition 1.6.9;
  field-base-change Remark 1.6.10; broad formula Theorem 3.9.7; trivially
  valued formula Proposition 3.10.3.

Research-memo lines 149--179 currently spell out the theorem-number drift but
not the simultaneous shifts of the Section 1.6 anchors.  The phrase "Exact
usable anchors in this frozen version" is therefore edition-ambiguous after two
different frozen versions have just been listed.  The smallest citation repair
is to label the existing 1.6.3/1.6.4/1.6.7/1.6.8 list explicitly "arXiv v1" and
add the four later-edition shifts listed above.

The candidate theorem itself contains no external citations.  Its two
non-elementary steps should cite Pille--Schneider, Proposition 4.2, at proof
lines 75--76 and Boucksom--Eriksson, Theorem 8.16, formula (8.9), at proof lines
85--88.  Chen--Moriwaki is **not** an input to this finite reduction: its
resultant formula is a downstream, closed-immersion metric-comparison input and
must not be used to disguise the unresolved relative assembly problem.

These two source issues account for the two citation defects counted above:
(a) omitted citations in the theorem packet, and (b) incomplete edition labels
for the later Chen--Moriwaki Section 1.6 numbering.

## Independent compile and visual check

The exact frozen harness was compiled afresh with PDF LaTeX through `latexmk`
in a separate temporary output directory.  The final pass has zero warnings,
undefined references, undefined citations, overfull boxes, underfull boxes,
multiply defined labels, emergency stops, and fatal errors.  It produces three
A4 pages with empty Author metadata.  All three pages were rendered at 120 dpi
and inspected; no clipping, overlap, missing glyph, or margin defect was found.

The independently generated PDF has SHA-256

~~~text
6fe6e0e16051d5151d71c4bdb92796f80fca910c46be613411939d34d329e7ef
~~~

Its differing hash from the archived PDF is ordinary PDF-build
non-reproducibility; the exact TeX harness and both included theorem inputs were
identical.

## Disposition

Do not submit these exact statement/proof bytes to production verification and
do not integrate them live.  Repair the hypotheses in the `Consequently` clause,
add the two exact theorem citations, clarify the Chen--Moriwaki edition map, then
freeze, rehash, compile, independently audit, and only then submit the revised
theorem bytes.  No change to the open-problem inventory is warranted: even after
repair, this remains only a finite-level reduction and P17.1 remains open.
