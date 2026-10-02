# Chapter 60 completion audit

Date: 2 October 2026

Base: local Chapter 59 commit `7a1c0f7`.

Scope: `parts/part5/ch60_mp_psh.tex`, under the sequential quality programme.
Chapter 61 is next; the whole-book goal continues. Independent Chapter 72
research remains paused. Frozen receipts and releases are preserved.

## Mathematical and expository review

The complete source and all seventeen preceding Chapter 60 unit audits
were read. All 37 formal assertions retain a proof or a precise imported
interface. There are 63 labelled reusable environments and 152 labels.
The seven numbered sections, thirteen new subsections and source note
have semantic labels. The subsections expose the order of model positivity,
operations, closedness, monotone completion, finite-energy measures, rays,
mixed slopes, entropy and stability.

The principal checks and repairs are:

- The probability convention is now compared explicitly with the book's
  unnormalized convention: MA, E, J, complex energy and the complex d1
  metric have the stated volume factors. Mixed intersection pairings keep
  their unnormalized values. Arbitrary model functions can have signed
  measures of mass one; positivity requires the psh hypothesis.
- A new connected-curve calculation allows any real positive volume V.
  On the point blowup, relative nefness is exactly 0<=c<=V, the raw atoms
  have masses V-c and c, and probability energy is -c^2/(2V). Reduced
  entropy is c/V in probability normalization and c before normalization.
  Replacing reduced discrepancy by total discrepancy adds the measure's
  mass. Both endpoints and the signed measures outside the nef interval
  are included.
- Rational scaling now has the correct ideal power, without the stray
  comma in its exponent. The review distinguishes the scaling action from
  ordinary scalar multiplication, retains central multiplicities, and
  checks proper-support and infinite ideal values. The resolved ramified
  map is proper and surjective; it need not remain finite. Finite pullback
  permits a nonsurjective source map with its stated Kähler hypothesis.
- Relative positivity and descent use the exact Demailly--Paun inputs.
  A component of the full inverse image supplies the descent argument,
  including subvarieties contained in the exceptional image. The maximum
  construction keeps its bounded-potential regularization input. Two
  citations now use the exact author-version key and page locators.
- Divisorial closedness keeps the analytic-cycle step explicitly imported.
  The numerical reduction retains the normalized polynomial B_d(s,0)=1,
  its prefactor d, uniform small-parameter choice and iteration to zero.
  No common model for an entire arbitrary net is assumed.
- The Zariski calculation keeps actual positive intersection weights.
  Its kernel can be larger than the constants when weights vanish. Energy
  first variation and the cocycle are polynomial identities on real
  divisors; positivity is used only for psh monotonicity and concavity.
- Model regularization constructs a decreasing rational sequence on one
  model with explicit error bands. General psh completion still uses nets.
  The downward-directed majorants use continuous minima only as comparison
  functions, without asserting that a psh minimum is psh.
- Negativity, finite-vertex tests and the fixed-model weighted graph bound
  retain exceptional support, the contracted-curve argument and genuine
  edge weights. Divisorial determination applies to a psh function compared
  with an arbitrary usc function. The spike example explains why density
  alone is insufficient.
- Extended pairings take nonempty infima and allow minus infinity. Finite
  energy is established before differences are taken. The PL test-function
  extension uses a sufficiently positive vertical divisor on a higher
  model; merely enlarging the pulled-back background is not substituted.
  Riesz representation gives probability measures, with net convergence
  proved by density and mass. Weak measure convergence alone does not imply
  finite energy of the limiting potential.
- The radial convention remains s=-log|tau|^2. Multiplier ideals use weight
  exp(-mV), and the comparison with Demailly's doubled weight is explicit.
  Flag extraction, logarithmic cutoff, dyadic regularization and restoration
  of the original background retain their separate limits and the fixed
  divisorial error bound. The cutoff and constant-ray example tests the
  integer floor, zero weight and unit ideal.
- Maximal-ray existence, sequential regularization and identification of
  the limiting datum remain precise imported inputs. The projective BBJ
  ordered-energy identification is not transferred to a general Kähler
  class. Order, translations, ordered distance and locally uniform time
  convergence are deduced from the stated inputs. The two counterexamples
  retain the distinction between maximal geodesic rays and general psh rays.
- The test-curve comparison retains its finite-energy, I-maximal and closed
  terminal-level hypotheses. The mass-defect formula uses the reference
  volume, including at a non-full-mass terminal level. The full-cone
  projective comparison keeps its real Neron--Severi scope and does not
  supply energy or operator compatibility for a transcendental class.
- The mixed-slope proof keeps the full imported PL/general-initial-value
  theorem. Its direct finite-energy approximation separates centered
  estimates from restored averages, with the actual signed translation
  coefficients. Average slope is obtained independently of the theorem
  being proved. Ordered d1 and the two-point J functional are distinguished.
- Reduced entropy, finite twisted energies and the factor n in the scalar
  coefficient are retained. The snc log-volume reconstruction includes
  multiplicities, branches, simplex volume and logarithmic growth. Its
  constants depend on the fixed model. The total-discrepancy unit
  obstruction, extended entropy, Radon increasing-net argument and
  lower-slope scope remain explicit.
- Uniform stability uses one constant for all finite-energy potentials.
  The ratio test excludes constants and includes infinite entropy safely.
  The P1 endpoint prevents a converse from cscK existence with ordinary J.
  Fixed-ray growth does not assert global coercivity. The cscK implication
  and subsequent normalized-model reduction remain exact later-source
  inputs, with the raw big-class boundary stated.

Inline mathematics follows the house convention. Rendered review also
keeps three short warnings and the compact energy, maximal-ray and
ray-stability statements together. The preceding unit audits remain
historical evidence for their identified revisions, not independent
receipts for this complete chapter pass.

## Direct source interfaces

Ten primary PDFs and 64 source pages were read and inspected in rendered
contact sheets. Demailly's introductory local formulation was also read.
The inspected page list is version-specific:

| Source | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Mesquita-Piccione, arXiv 2409.06221 v2 | Models, cofinality, positivity, scaling, closedness, energy, completion, rays, mixed slopes and the total-discrepancy issue | 14--15, 20, 26--27, 33--52 |
| Demailly--Paun, published Annals 159 (2004) | Numerical Kähler component, extension, finite unions and nef criterion | 2, 16--17, 21--22 |
| Demailly, author-hosted 1992 regularization PDF | Bergman regularization, curvature bounds, gluing and weight normalization | 13--17 |
| Boucksom--Hisamoto--Jonsson, published JEMS 21 (2019) author offprint | Logarithmic relative canonical model, snc volume and its proof | 19--21 |
| BHJ, published 2022 erratum | Affected later theorem and the stated unaffected scope through Section 4 | 1--2 |
| Boucksom--Jonsson, published JAMS 38 (2025) author offprint | Ordered two-point J and the mixed-energy estimate with proof | 19--20, 32--33 |
| Berman--Boucksom--Jonsson, arXiv 1509.04561 v3 | Ordered Darvas metric and projective maximal-ray energy identification | 10, 25--26 |
| Darvas--Xia--Zhang, published 2025 PDF | Squared radial convention, Legendre correspondence, terminal level and mass defect | 12--14, 31 |
| Mesquita-Piccione--Witt Nystrom, arXiv 2509.09442 v1 | Reduced entropy, stability, normalized-model approximation and raw-model boundary | 13, 31, 34--35 |
| Boucksom--Jonsson, published AFST 31 (2022) | Algebraic model operations, positivity, scaling, extended pairings and finite energy | 41--42, 48--49, 102--103, 107--109 |

PDF SHA-256 values, in table order:

1. `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`
2. `0fa73d0742f6990e14dd15b6b19dd49b2c3a1b7db69c89785cca98e8edc9c41f`
3. `3dbc4cb1d915168cfc00d23da74acf1a53fdc1c0ed4a2d7ede85e2b6d159dc90`
4. `e0042513cdb7e565a4d63b556f478bb588dd85561305e2ce4240aab8b76e0832`
5. `62efc671a6e837f9166144dc93ab4dfe6fbca52b64ad7dcea11519641097e873`
6. `4ecf20801f0871223ddfc1ea3e09927904affaab75bb5e195bfe55a2b0f09498`
7. `6973d1df47b527ce9c27e2496d8bd91b949c8e28b4123c2f708e45ccc6836b00`
8. `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`
9. `54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`
10. `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`

Fresh access included the [Annals PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf),
[Demailly PDF](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization.pdf),
[BHJ published offprint](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BHJ2.pdf),
[BHJ erratum](https://ems.press/content/serial-article-files/32635?nt=1),
[JAMS published offprint](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BJ_synthetic.pdf),
and [BBJ v3](https://arxiv.org/pdf/1509.04561v3).
The author offprints resolve the access limitations recorded in earlier
scoped audits for the specific passages reviewed here. No uninspected
later theorem is inferred from that access.

[Stacks Tag 0D2S](https://stacks.math.columbia.edu/tag/0D2S), including its
proof, was freshly checked for the algebraic fiberwise-ampleness warning.
Its saved HTML SHA-256 is
`5a7685694ed3d18d083f8ca6d7b3b60da33fbaeccabdbd801c82eaf7d203a8a1`.
This criterion is not substituted for the analytic positivity inputs.

## Verification

The exact-arithmetic supplement passes 42,871 checks across nineteen
families: rational scaling, finite pullback, arbitrary-volume curve
masses/energy/entropy, stability endpoints, weighted Zariski and
Cauchy--Schwarz identities, energy cocycles, regularization error bands,
multiplier floors, dyadic cutoffs, Demailly--Paun polynomial moments,
snc branch/simplex factors and the constant/hyperplane ray examples.
These checks supplement the proof review; finite calculations do not
establish the general imported analytic theorems.

The legacy house-audit executable is unavailable in this workspace.
The manual house review and scoped structural substitute both pass:
balanced environments, no duplicate or missing reusable labels, no
proofless formal assertions, no legacy inline delimiters, no double
dollars, and no unfinished-work markers. Imported inputs remain named.

Post-render verification passes for 425 input files and 12,187 labels,
with all six reference-checker tests passing. The open-problem inventory
remains 42 atoms in twelve environments, tiers (0,3,7,15,17).
`git diff --check` passes.

Final full build: **4,128 pages, 19,271,700 bytes**. PDF SHA-256:
`67fca7a82075f3846a384889ef1b3ceae48c34990beee5e97c52c1f9c407c4f3`.
Final chapter SHA-256:
`464a26e21671b6f9d1845a53ad46e21c1632f050559fbfa027f2412cc4a298eb`.
No unresolved references or citations, missing glyphs, rerun requests or
fatal errors remain. Chapter 60 has no overfull boxes or LaTeX/package
warnings. The nineteen overfull boxes elsewhere and thirteen duplicate
PDF destinations in Chapter 70 are unchanged.

All 54 physical chapter pages 3195--3248 (printed 3125--3178) and both
adjoining seams were inspected at detail size. The final warning-layout
repair changed thirteen page images; all thirteen were reinspected, and
every other chapter/seam render was compared byte for byte with the
inspected preceding build. Physical 3248 is intentionally blank.
No reviewed chapter layout defect remains. A review PDF is saved in
`/workspace/book-completion-drafts/Chapter_60_Review_2026-10-02.pdf`.

This is a direct editorial/source audit, not a new independent verifier
verdict. Verified work remains local pending explicit remote-push approval.
