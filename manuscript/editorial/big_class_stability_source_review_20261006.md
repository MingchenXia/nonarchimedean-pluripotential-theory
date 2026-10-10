# Big-class stability: source and proof-dependency review

**Research-only checkpoint; no theorem or repaired proof is imported into
active TeX.** The baseline is `139e9e22c28740b1d6958362cbaff479939ee78f`.
The controlling source is Ruadhaí Dervan and Rémi Reboulet,
*A birational version of K-stability for big classes*,
[arXiv:2603.25605v1](https://arxiv.org/abs/2603.25605v1), submitted
26 March 2026 at 16:22:15 UTC. All 40 actual PDF pages, the complete
extracted text, proofs and references were read. Every actual page was
displayed; pages 27–30 were redisplayed separately after a truncated
multi-image response. No other edition controls these observations.

The main PDF has 649,217 bytes and SHA-256
`04f4e18f71c44026038be9d287fa56b81004e9610f34f783aa0a79099e3ebd31`.
The full reading record is
`source_material/big_class_stability_followup_20261006/full_reading_v1_20261006.json`.
The [manifest](big_class_stability_source_review_manifest_20261006.json)
embeds the reading evidence and preservation checks. Historical acquisition
and preparation records keep their original flags.

## Category, normalization and claimed scope

The ambient variety is smooth and complex projective, the polarization
is big, and its volume `V=vol(L)` is positive. The source allows real
classes and generically big test configurations, made globally big by
adding a sufficiently positive class from the base. Its model energy
subtracts that base twist after dividing the top positive product by
`(n+1)V`. Its Monge–Ampère measure is a probability measure with
central-fibre multiplicities in the component masses.

Remark 2.8 on page 10 expressly calls the ample specialization
**uniform K-stability with respect to models**. It must not be identified
silently with a test restricted to ample test configurations. The source
compares this model condition with stability tested on finite divisorial
probability measures, and studies pullback and effective exceptional
changes of polarization under birational maps. The full big-class
constant-scalar-curvature existence picture remains a conjectural
direction; it is not a consequence admitted by this review.

These claims do not supply the book's general Siu or closure input.
They do not settle a canonical problem in the 42-row inventory. In
particular, the finite-dimensional model argument must be kept separate
from the unrestricted non-Archimedean envelope and Calabi–Yau arguments.

## Selected primary dependencies: 58 actual pages

All listed pages were displayed and read in thirty sheets. Exact extracted
passages were additionally reread when comparing formulas. This is a
selected PDF reading, not a claim that every extracted dependency text,
every paper or its complete chain of external inputs was read in full.

| Controlling primary edition | Actual PDF pages | Checked use |
| --- | --- | --- |
| Boucksom–Favre–Jonsson, JAG 18 (2009), 279–308, author-hosted published offprint | 1–3, 12–20, 23–28 | Dominated nef approximants, big-cone continuity, volume differentiation and orthogonality, restricted products, Theorem B and its proof |
| Ein–Lazarsfeld–Mustaţă–Nakamaye–Popa, `math/0607221v2`, 10 January 2008 | 1, 6–15 | Moving parts, effective fixed parts, restricted Fujita approximation, Theorem 2.13 and its displayed proof |
| Boucksom–Hisamoto–Jonsson, `1504.06568v3`, 30 November 2016 | 1, 25–27, 33–37, 47–51 | Probability tails and first moments, relative log canonical divisors, discrepancy identity, base-change degree, model energy and Mabuchi normalization |
| Boucksom–Jonsson, `1805.11160v1`, 28 May 2018 | 1, 25–27 | Lemma 4.15 in the cited edition, Veronese degree and factorial convention |
| Witt Nyström, `2510.03044v1`, 3 October 2025 | 1–6, 11–15 | Fixed-model theorem and probability signature, restricted-volume inputs, continuity, separating vertical classes and the simplex argument |

The published BFJ PDF is
[the author's offprint](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BFJ_differentiability.pdf).
The remaining controlling PDFs are the explicitly versioned
[ELMNP](https://arxiv.org/pdf/math/0607221v2),
[BHJ](https://arxiv.org/pdf/1504.06568v3),
[BJ18](https://arxiv.org/pdf/1805.11160v1) and
[Witt Nyström](https://arxiv.org/pdf/2510.03044v1) files. BHJ's PDF was
reused byte-for-byte from the earlier Chapter 50 audit; its selected
pages were freshly displayed. Journal pagination is not substituted
for the three cited arXiv locators.

The selected reading record is
`source_material/big_class_stability_dependencies_20261006/selected_reading_v1_20261006.json`.
Its SHA-256 is
`15f1b76cea7ddedab5398fd6e4468767161330782644c4848e7b7870b3e3dc89`.
Witt Nyström's analytic restricted-volume inputs from Collins–Tosatti
and earlier work, and the remaining asymptotic filtration inputs,
are not fully audited here. No complete verification certificate is
inferred from the selected reading.

## Inputs that the primary reading does support

BFJ Definition 2.5 on printed pages 290–291 (actual pages 12–13)
uses **effective** Cartier divisors: nef approximants are dominated by
the original big class. Proposition 2.13 on printed page 293 (actual
page 15) permits the corresponding pseudo-effective order, and
Proposition 2.9 on printed page 292 (actual page 14) gives continuity
inside the big cone. Theorem A and its proof on printed pages 295–296
(actual pages 17–18) give the derivative
`d vol(alpha)[gamma] = dim(X) <alpha^(dim(X)-1)> . gamma`.
Corollary 3.6 records orthogonality. These are positive-intersection
and volume statements in their stated category, not order statements
for every coefficient of a Monge–Ampère measure.

BFJ **Theorem B is not missing a hypothesis that the prime divisor
avoid the augmented base locus**. Its published statement on printed
page 281 (actual page 3) applies to any prime divisor on a smooth
projective variety and any big line bundle. Section 4.3 on printed
pages 305–306 (actual pages 27–28) treats the non-`D`-big case by
vanishing and orthogonality before treating the positive case. Thus
the citation supporting Dervan–Reboulet Equation (2.2) on page 7 is
cleared in that algebraic prime-divisor scope. It must not be confused
with ELMNP Theorem 2.13, whose restricted Fujita formula for a general
subvariety explicitly retains `V` outside the augmented base locus.

ELMNP Definition 2.6 on page 7 and Theorem 2.13 on page 9 use the
moving part of a resolved linear series after subtracting an effective
fixed part. The proof on pages 12–14 retains both the fixed base
ideal and the asymptotic multiplier ideal. It does not assert that
the unmodified pullback of an arbitrary big polarization becomes
semiample by adding only a vertical divisor on a degeneration.

BHJ Proposition 3.12(iii), actual page 25, and Lemma 7.3, actual
page 47, give the first moment as the top intersection divided by
`(n+1)V`. Theorem 5.3 on pages 35–36 uses graded volumes normalized
by `n!`, with the distributional **negative derivative** of the tail
divided by `V`. Proposition 5.9 and its proof on pages 36–37 compare
that probability measure with the Duistermaat–Heckman measure.
These formulas fix both factors and the derivative convention.

BHJ pages 33–34 use the relative logarithmic divisor
`K_(total/base) + fibre_red - fibre`, before subtracting the relevant
background pullback in the discrepancy formula. Corollary 4.12 gives
the resulting vertical discrepancy coefficients. Proposition 7.14,
pages 50–51, makes the Mabuchi functional homogeneous of degree one
under normalized base change of degree `d`, not invariant with factor
one. Its argument uses the finite map's degree in the projection formula.

## Literal formulas and proof steps requiring repair

The following are diagnostics of the **specified v1 bytes**. They
separate an invalid printed expression or unsupported step from the
truth of a suitably corrected main theorem. The elementary checks
are normalization and scope tests, not original general results or
independently certified counterexamples to the main stability theorem.

1. **Dominance in the positive-product definition, page 6.** The displayed
   supremum over `pi^*L-D` being nef omits `D >= 0` or an equivalent
   pseudo-effective domination condition. Without it, taking negative
   large multiples of an ample class on the identity model makes the
   alleged top supremum unbounded. BFJ Definition 2.5 supplies the
   missing condition. Later uses must use that corrected definition.

2. **Log canonical sign, page 9.** The source defines the correction as
   `fibre - fibre_red` and explicitly uses that sign again in its entropy
   definition. It differs from BHJ's relative correction by
   `2(fibre-fibre_red)`. The discrepancy identity in Lemma 4.18 on
   pages 29–30 consequently needs reconciliation for nonreduced fibres.
   The difference disappears on a reduced fibre; that special case
   does not justify the printed general convention.

3. **Semistable reduction, Lemma 2.9, page 10.** The proof describes the
   map to the original total space as both birational and generically
   finite, and its displayed top positive product and Mabuchi invariant
   omit the degree of the covering. The compactified base map is also
   described as branched only at the origin, omitting infinity. A
   birational modification has degree one; the covering followed by
   such a modification need not. BHJ Proposition 7.14 verifies the
   required degree factor in the ample case. The intended reduction
   can preserve a uniform inequality after scaling its two sides by
   the same positive degree, but the printed equalities do not prove it.

4. **Generic polarization in Lemma 3.10(iv), pages 15–16.** The printed
   approximants retain `pi_m^*L + D_m` with `D_m` vertical, although
   the proof first replaces the generic polarization by the moving
   part `L_m`. A vertical change cannot make a non-nef generic
   polarization semiample. For the elementary surface
   `X=Bl_p(P^2)`, `L=2H+E` is big but `L.E=-1`; its pullback still
   has degree `-1` on the strict transform of `E`. Relative
   semiampleness would restrict to a nef bundle on that generic
   fibre, contradicting that degree. An intended version must use
   `L_m`, track the horizontal fixed part, and divide energy by
   `vol(L_m)` before taking a limit. This diagnostic does not rule out
   an ample-generic specialization with vertical base ideals, or
   prove that the intended concavity theorem is false.

5. **Tail and probability factors, Equations (4.3)–(4.4), page 18.** The
   source's raw tail is `lim k^(-n) dim F^(k lambda) R_k`. For that
   definition, the probability tail is `n!/V` times the raw tail; the
   same factor is needed in its first-moment integral. Its displayed
   measure instead omits `n!`. A constant weight shift by one on
   `(P^1,O(2))` gives mean one, whereas the printed integral in (4.3)
   gives two. On `(P^2,O(1))` the raw tail has height `1/2`, so the
   displayed measure has mass `1/2`. Using standard graded volume
   with the factorial included avoids both discrepancies.

6. **Trivial-valuation cutoff, Definition 2.12 and Theorem 4.1,
   pages 10–11 and 19–20.** The theorem states the section formula
   only between `lambda_min` and `lambda_max`, correctly setting
   `gamma(triv)=0`, but then integrates that formula to infinity
   without its cutoff. For support consisting only of the trivial
   valuation and coefficient zero, the filtration is trivial and
   its mean is zero; the displayed uncapped integral is infinite
   because its integrand is the constant `V`. The correct tail must
   retain `lambda <= t_triv` whenever the trivial valuation is
   present. Finite nontrivial thresholds give further upper cutoffs.
   Omitting indices which impose no constraint is valid for the
   actual filtration; it does not remove this truncation condition
   from the proposed volume integral.

7. **Approximation identities, Theorem 4.10, pages 24–25.** The
   intermediate limit-measure display lacks the distributional
   derivative and its sign, and the subsequent first-moment chain
   uses incompatible degree and `(n+1)` factors. The final desired
   energy/mean convention agrees with BHJ, but that agreement does
   not validate the intermediate equalities. Lemma 4.11 on page 25
   also uses `W_1^m=V_1` where the cited BJ18 Lemma 4.15 uses
   `W_1^(m)=V_1^(m)=V_m` for the mth Veronese grading. The exact
   controlling BJ18 statement and proof are on pages 26–27.

8. **Danskin difference quotient, page 28.** The proof of Theorem
   4.15 multiplies differences with increment `k^(-1)` by `k^(-1)`
   again, where the derivative quotient needs multiplication by
   `k`. The stated theorem is a standard optimization input; this
   is a printed proof defect, not a disproof of the theorem. The
   application uses a finite-dimensional compact coefficient set,
   where subsequence extraction is available. A statement for an
   arbitrary compact space would require nets or a metrizable
   restriction instead of that sequential argument. Its cited
   optimization books have not been newly checked in this review.

9. **Componentwise measure comparison, Lemma 5.2, page 33.** The proof
   uses positive-product monotonicity to assert an inequality between
   the individual Monge–Ampère masses. Positive-product order is an
   order on cycle classes; contracting it with an arbitrary effective
   central component need not preserve order. BFJ page 23 expressly
   warns that restriction to a divisor destroys pseudo-effective
   monotonicity in general. Equality of the induced filtrations
   supplies additional information, but the stated monotonicity
   argument does not explain the required implication. A scalar
   energy comparison followed by first variation is a possible
   repair route; it is not supplied or certified here. Remark 5.6
   offers an alternative approximation route whose convergence and
   generic-polarization bookkeeping still require an audit.

10. **Background class in birational constructions, pages 34 and 36.**
    Equations (5.1) and (5.3) display a line class made only from
    vertical components. Read literally, it restricts to zero on
    the generic fibre, rather than the stated big polarization.
    The background pullback and the multiplicity convention from
    the preceding divisorial-filtration construction must be restored
    before those models can be used downstream.

## Fixed-model Calabi–Yau and the scope of a possible follow-up

The finite simplex mechanism in Dervan–Reboulet Theorem 3.6,
pages 13–15, is closely related to Witt Nyström's Theorem A and
Lemma 6.2. The latter theorem is stated on page 6, in the model
signature on pages 3–5, and proved on pages 13–15. It prescribes a
probability measure supported on the fixed central components of
an SNC model by a **big** vertical modification. It does not assert
that the modified class is Kähler or nef, or that the solution is
unique. The simplex map's continuity, total mass and face property
are separate inputs; a picture of the simplex cannot replace them.

The graph-distance construction in Lemma 6.2 keeps the central-fibre
multiplicities and uses separating half-spaces for the component
pseudo-effective cones. Convex combinations preserve the half-space
condition. The surjectivity argument then uses the map on the
boundary being homotopic to the identity. The algebraic volume and
prime-divisor inputs have selected primary support above; the full
transcendental input chain remains outside this checkpoint. This
model theorem must not be used to remove the book's explicitly
conditional general Siu/closure boundary.

The source's birational statements also distinguish pullback from
adding an **effective exceptional** class. Its Weil b-divisor
definition on page 38 restricts to a compatible subsystem with
that property. It does not cover arbitrary unrelated Weil b-divisor
realizations. A follow-up must track the chosen subsystem, its
existence and directed compatibility, rather than generalize the
word "birational" without those data.

## Preservation and next work

This checkpoint changes only this audit, its manifest, README and
the sequential programme. All 425 active TeX inputs, 108 protected
inputs, 42 canonical problem rows, the inactive toric candidate,
the open native catalogue, 51 earlier frozen manifests and 103
earlier exports retain their baseline bytes. The existing checked
book has 4,380 pages. No fresh build, rendered book review, source
archive compilation, native-editor compilation, independent model
verdict or original-result receipt is claimed for unchanged sources.

The next useful step is to isolate the **ample generic polarization**
Fujita input needed by Chapter 68's ordered comparison, keeping
vertical base ideals and a common energy normalization. It can be
studied without importing the full arbitrary-big stability theorem.
Entropy convergence remains another input. The fixed-model simplex
argument is a second possible scoped import after its remaining
volume assumptions have been cleared. Neither direction is assigned
a new canonical solved status by this source review.
