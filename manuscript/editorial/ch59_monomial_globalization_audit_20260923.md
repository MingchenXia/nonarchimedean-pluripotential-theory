# Chapter 59 monomial-valuation audit

Date: 23 September 2026.
Baseline: `bc2f00239db7d0e30ea76fb71d4770eeaa17dc83`.
Scope: the monomial construction and examples in Section 59.3, before
the section on models. The earlier integral-closure unit is preserved.

## Findings and reconstruction

The former proof invoked coordinate invariance without giving its
mechanism. Its injectivity argument distinguished weight vectors within
one cone but did not separate distinct components of the same divisor
intersection. The cone's face identifications were not defined. The
rational-realization sentence omitted the scalar between rational weights
and the primitive integer order of a prime divisor. The point-blowup
example also described an exceptional divisor without excluding curves.

The revised construction works on the local ring of the smooth model Y
and evaluates a global ideal on X through its extended ideal on Y.
Cones retain their intersection components. A zero-weight face is glued
to the cone of the component of the larger intersection containing the
original stratum. Empty index sets, the common vertex and zero weights
are included explicitly.

Positive-weight coordinates are separated from zero-weight coefficient
variables. Initial forms lie in a polynomial ring over a convergent-power-
series domain, proving multiplicativity even when weights are rationally
dependent. The valuation-ideal filtration is a finite sum of intrinsic
products of divisor ideals. Monomial membership in convergent series
proves coordinate independence; finite generation follows from the
upward-closed exponent set. The zero-weight coefficient variables are
retained as germs, not evaluated as numbers.

On an adapted product polydisc, each normal coefficient is a holomorphic
function of tangential variables. The identity theorem preserves the set
of nonzero coefficient germs when the point moves. Coherent generators
and connectedness give independence along the whole stratum. This is
also valid for zero normal weights, and therefore proves face compatibility
without assuming it. Nonzero global ideals have finite values, giving
full support. The center is the component of the intersection indexed
by the strictly positive weights. Here an ideal's image in O_W is meant,
not its tensor product with O_W, which need not vanish.

Global divisor ideals distinguish unequal extended weight vectors.
For equal vectors with different positive-support components W and W',
the ideal I_W has values min(w_i)>0 and zero, respectively. This supplies
the missing comparison between different cones. The checked bimeromorphic
full-support bijection then transports injectivity to X. Finite minimal
supports of convergent expansions express every ideal coordinate as a
minimum of finitely many linear forms on each closed cone. This proves
continuity in the pointwise ideal topology, including all boundary faces.
No unproved homeomorphism property of the full bimeromorphic bijection
is used to assert this continuity.

For a rational nonzero weight, write w=c a with a primitive positive
integer vector after zero coordinates are omitted. Blow up its smooth
center and choose a chart indexed by a minimum weight a_j. The weights
become a_j and a_i-a_j. The exponent substitution is injective and preserves
weights, so it preserves the original character on pulled-back ideals.
The reduced boundary stays snc and the new positive-weight stratum
defines a global smooth center. The positive weight sum decreases by
(k-1)a_j while the greatest common divisor is unchanged. The process
terminates at a single weight one; the original valuation is c ord_F.
With one positive coordinate no exceptional divisor is needed, and the
zero vector gives the trivial valuation. This is an explicit ordinary-
blowup proof of the rational realization, not an appeal to a locally
defined weighted blowup with unproved globalization.

## Examples and second pass

For weights (a,0), the germ ut+u^2 has value a even at t=0. Replacing
the coefficient germ by its numerical value would incorrectly give 2a.
The ordinary point-blowup example now requires dimension at least two
for its exceptional divisor; on a smooth curve the point-ideal blowup
is the identity and the valuation is ord_p.

On P1 x P1, the section y=0 and the graph y=x^2-1 are smooth and meet
transversely at (1,0) and (-1,0). Their cone complex has two quadrants
sharing their boundary rays. The interior vectors (1,1) have the same
values on both boundary-divisor ideals but different values on I_(1,0).
The rational vector (2/3,1) is explicitly realized as (1/3) ord_F,
using (2,3) -> (2,1) -> (1,1) -> (1,0). The ideal (u^3,v^2) has value 2.

After the first complete draft, full build and page inspection, the second
local pass checked valuation axioms, attained minima, convergent monomial
division, coordinate changes, connectedness, face gluing, centers,
cross-component separation, continuity, blowup substitutions, the integer
descent, dimension one and all-zero weights. It made the positive-coordinate
indices precise, justified reading divisor weights away from the remaining
boundary, wrote the exponent substitution explicitly and tightened the
published cone citation. It then repeated the style/build/page checks. The rational-weight example
was tightened once more to keep the introductory sentence with its display,
and the full build and rendered pages were checked again.

## Primary sources and verification limits

- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
  18 September 2025, Section 2.3.1, pp. 16--17: the cone gluing definition,
  Proposition 2.3.4 and Remark 2.3.5. The exact author PDF pages were read,
  rendered and inspected. The source's displayed injectivity explanation
  compares points of a single cone; the global ideal I_W supplies the
  additional comparison in this reconstruction. Its rational-realization
  remark is expanded into the chart argument above. PDF SHA-256:
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  Direct access to the published DOI 10.1016/j.aim.2025.110543 again failed.
  The existing MP24 entry is preserved; the changed unit cites MPTropicalV2
  rather than claiming to have checked the publisher's theorem locators.
- Jonsson--Mustata, *Valuations and asymptotic invariants for sequences
  of ideals*, Ann. Inst. Fourier 62 (2012), no. 6, 2145--2209,
  [published DOI 10.5802/aif.2746](https://www.numdam.org/articles/10.5802/aif.2746/).
  Proposition 3.1 and proof, pp. 2166--2168, give the algebraic coordinate,
  zero-weight and continuity statements. Lemma 4.5 and the following
  paragraph, p. 2176, retain the different intersection components in the
  algebraic cone structure. Physical PDF pages 23--25 and 33 were rendered
  and checked. This is cited as the algebraic counterpart; the analytic
  proof above does not assume an algebraic function field for X.
  The existing JM12 bibliography entry is unchanged. Published PDF SHA-256:
  `b0360dbfeb5b19601500e3ed03e8b186f4ac84b6c771a2a300fe25efa0d5fb57`.

These are textbook reconstructions with explicit deductions and examples.
No new research theorem, independent-agent audit, production-verifier pass
or research-atom closure is claimed. The exact-version preprint warning
from the bibliography-aware style audit was reviewed with the access
limit above; the strict audit of the changed TeX has zero errors and
zero warnings.

## Final validation and preservation

The final full build passes: 3,951 pages, 18,789,892 bytes, 389 TeX
inputs and 11,579 unique labels. There are no missing inputs, duplicate
labels, dangling references, unresolved citations or horizontal or vertical
layout overflows.

The first and final builds were rendered and inspected on physical pages
3315--3320 (printed 3247--3252), covering the full unit and adjacent text.
Pre-existing underfull-box and class warnings remain; compilation is not
a mathematical verifier. `git diff --check` passes.

All Chapter 59 bytes outside this monomial unit, Chapter 58 and the whole
bibliography match the baseline. The inventory remains 46 active atoms
in 14 formal environments, tiers `(0,5,8,16,17)`. The supplied and restored
CURVE_PSH.tex, author sources, frozen proofs, verifier receipts and dated
release artifacts are unchanged. The generated live PDF remains ignored
and is not a new release or a committed artifact.

SHA-256:

- Chapter 59: `fd9a69ae660592e09836cc800acc3b10608db4f194bba09027a71e46a5a9481d`.
- Unchanged bibliography: `f77736549ed82a38bc6db488b2527629b2cb2ebf5b47475f3c94e08e0e068219`.
- Generated live PDF: `5f8718f1bae31e05388874c56bd9f4017328ea767ac240352a1f0af5ef562b77`.
- Supplied and restored CURVE_PSH.tex: `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

The next bounded unit is the invariant vertical-divisor comparison in
Chapter 59: distinguish projection pullback from restriction to a fiber,
check the precise local algebra hypotheses and confirm that the global
realization produces a model trivial away from the central fiber.
