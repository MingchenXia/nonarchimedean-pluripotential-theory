# Chapter 60: logarithmic volume growth and reduced entropy slopes

Date: 24 September 2026.
Baseline: `c70d19097678e0e5021913ff4c7556f48e06bbff`.
Scope: the reduced entropy definition through its slope theorem, before
the existing finite-energy stability definition; one corresponding BHJ
locator and description in the source note are also updated. The preceding
mixed-slope proof and all other Chapter 60 source retain their baseline
bytes. This is a reconstruction of a published model calculation and
elementary consequences of the existing slope theorem, not a new
research-frontier closure.

## Logarithmic volume calculation

The normalizing integral Z(s) is now bounded on both sides by positive
constants times (1+s)^d, where d is the dimension of the fixed model's
dual complex. This is the precise exponent in BHJ Lemma 3.11; the former
book bound had only a constant lower bound and a degree-n upper bound.
The logarithmic estimate is d log(1+s)+O(1), so its quotient by s tends
to zero. Constants and the threshold in s depend on the fixed model and
metric, not uniformly on the directed collection of all models.

The divisor is K_(model/product)+B_red-model_0. Its coefficient divided
by central multiplicity is A_tot(v_E)-1. The local canonical-frame
identity gives f_s=-log|h_D|^2+smooth, retaining the squared-norm sign
and the parameter s=-log|tau|^2. The test is smooth on each nonzero
fibre; it is not required to be psh.

On tau=z_0^(b_0)...z_p^(b_p), the logarithmic relative canonical frame
has coefficient 1/b_0. After fixing coordinate radii, the p logarithmic
radial variables form a weighted simplex of volume
L_s^p/(p! product_(j=1)^p b_j), where L_s=s/2-sum b_j a_j. The b_0
branches of the projection away from z_0 multiply the density factor
b_0^(-2), giving the displayed coefficient proportional to
1/(product_(j=0)^p b_j). Smooth positive metric factors are bounded
above and below on the closed smaller polydisc. This is a comparison,
not a claim to compute the global leading coefficient for an arbitrary
metric. The p=0 case is treated separately.

A finite chart cover gives the upper exponent d, and a chart through a
deepest nonempty stratum gives the matching lower exponent. Properness
places small fibres in that cover. The proof requires analytic snc
coordinates and properness; it does not import a polarization into the
transcendental setting.

The product model has Z=1 after the natural metric choice. Blowing up
one point of P1 times the zero fibre gives two multiplicity-one components,
one node tau=z_0 z_1, and D=E. The discrepancy test has vertex values
0 and 1; the radial interval has length s/2-a_0-a_1. Thus Z is comparable
to 1+s and log Z is unbounded. This tests why the logarithmic correction
cannot simply be replaced by O(1).

## Entropy and limiting conventions

Complex entropy is explicitly defined for Borel probability measures,
with 0 log 0=0 and value +infinity for failure of absolute continuity.
The negative part of the density expression is integrable. A bounded
smooth log-density h for a reference change gives the extended-real
identity H_(exp(h)mu)(sigma)=H_mu(sigma)-integral h d sigma. It proves
independence of finite entropy and of both normalized liminf and limsup
along any family of probability measures. No difference of two infinite
entropies is formed. Applying this identity to the normalized exponential
tilt and using entropy nonnegativity proves the smooth-test inequality
directly.

The reduced entropy slope theorem now allows any smooth positive
probability reference volume. The Mabuchi functional retains its specified
reference omega^n/V. For each fixed model, the proof displays the error
(d log(1+s)+log C)/s and applies the full PL-testing mixed-slope theorem.
General initial values and that mixed-slope input remain explicitly cited
analytic dependencies.

The passage from model tests to discrepancy uses a continuous minorant,
a finite open subcover and one common dominating model on the compact
spectrum. The Radon characterization then gives the supremum of model
integrals, with no sequential substitute for the directed system. If
non-Archimedean entropy is infinite, one first chooses a model with test
integral greater than R+1, then takes time sufficiently large. This proves
eventual lower bounds for every R and hence divergence to +infinity.
The finite nonentropy slopes permit addition in the Mabuchi expression,
including the infinite case.

The zero-dimensional convention now assigns zero to the scalar-curvature
coefficient and twisted energy term, avoiding a negative-power
intersection expression. On a connected point both entropy and Mabuchi
functionals vanish. Total discrepancy adds one even at infinite entropy;
the existing zero-potential counterexample is retained. No entropy upper
bound or slope equality is asserted for finite non-Archimedean entropy.

## Primary-source checks

- The [published BHJ author offprint](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BHJ2.pdf),
  JEMS 21 (2019), 2905–2944, DOI 10.4171/JEMS/894: indexed primary-source
  text of Lemma 3.11 on p. 2924 explicitly gives comparability with the
  power determined by the dimension of the dual complex. The adjacent
  statement of Lemma 3.10 gives the logarithmic entropy error. The
  [author's publication list](https://sebastien.boucksom.perso.math.cnrs.fr/publis.html)
  confirms the published record. The proof's local frame, simplex and
  multiplicity computations were reconstructed directly here. Direct
  PDF retrieval failed through the web tool and at TLS connection setup
  locally, so no local published-PDF checksum or source-page visual check
  is claimed. The exact published lemma locator replaces the former
  arXiv-version locator; bibliography data are unchanged.
- The [published erratum](https://ems.press/journals/jems/articles/4218779)
  identifies the flaw in Theorem 5.6 and states that the main asymptotic
  theorem is independent of it. No use of that flawed theorem is made
  in this unit; the record of the erratum already exists in the bibliography.
- The [exact MP v2](https://arxiv.org/html/2409.06221v2), printed pp. 51–52,
  was read and both pages rendered and visually checked: formula (6.1.2),
  Definition 6.2.1, Proposition 6.2.2 and Corollary 6.2.3. The source
  PDF retains SHA-256
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  The existing total-normalization obstruction is preserved rather than
  inheriting the source's missing unit.
- [MP–Witt Nyström v1](https://arxiv.org/html/2509.09442v1), Definition
  2.4.1, was checked directly in HTML for integration of A_tot-1.
  Its Definitions 2.4.2 and Theorem 2.4.3 remain the existing later
  stability input, outside this revision. The
  [author's current publication page](https://pietropic.github.io/publications/)
  still lists this work as a preprint; no new journal publication was
  established. The two reviewed house-audit warnings concern MPWN25
  and the deliberately exact-version MPTropicalV2 key. They are not
  treated as a warning-free strict pass.

Internal inputs are the Chapter 59 model discrepancy envelope and its
monotonicity, probability-normalized mixed testing and finiteness, and
the preceding full mixed-slope theorem. The cscK existence theorem,
uniform-stability definition, scalar-normalization reference to Chapter 62
and the analytic full-PL scope are unchanged.

## Two passes and validation

The first full build produced 3,987 pages and 18,975,807 bytes, with no
overflow or unresolved citation/reference. Physical pages 3379–3385
were rendered and inspected. The complete second statement/proof/source/
notation pass rechecked the snc frame, fibre degree, simplex volume,
deepest-stratum lower bound, probability mass, singular measures,
extended-real identities, reference changes, directed model supremum,
infinite-entropy quantifiers and dimension zero. It declared the reference
volume and real smooth log-density at the point of use, clarified the
case of failure of absolute continuity, sharpened the wording of the
one-sided conclusion, and kept display introductions with their formulas
inside the local volume statement and proof.

The second full build produced 3,987 pages and 18,975,950 bytes.
Its scoped visual review identified two definition introductions and
the slope proof's first display split across pages. A final local
pagination adjustment keeps those introductions with their formulas;
it changes no mathematical statement or proof. The whole book was rebuilt.

Final full build: **3,987 pages, 18,975,921 bytes**. Physical pages
3379–3385 were rendered and inspected in full, covering the revised
block and its following boundary. This is a scoped visual review.

- Input/reference check: 390 TeX files, 11,654 unique labels; no missing
  input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply defined label,
  rerun request or horizontal/vertical overflow. Existing class and
  underfull warnings remain.
- Scoped strict house audit: zero errors and two reviewed bibliography
  warnings about MPWN25 and MPTropicalV2; exit status 1, not a
  warning-free strict pass. The normal scoped audit exits successfully
  with those reviewed warnings.
- Inventory: PASS, 45 active atoms across 14 formal environments,
  tiers (0,5,8,15,17).
- The Chapter 60 prefix and suffix outside the declared block retain
  their baseline bytes, except for the stated BHJ source-note update.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`646f775b3d586d84595c8a0ddc5b380bde6b973af5c4524330e474bc4cfb9bcc`.
Final live PDF SHA-256:
`7fdeefb147e0cb3ee4c4f5fec28588d2d053eb66a7ca2d7709f663688169e101`.

The preserved P12.1 fragment has SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The supplied CURVE_PSH.tex retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

The 45 active atoms, P12.1 integration/provenance, P12.2–P12.6 residuals,
supplied originals, bibliography, frozen packets, verifier receipts and
dated releases are preserved. No independent-agent or production-verifier
pass is claimed. The live PDF remains an ignored build product.
Next work is the remaining finite-energy stability interface and Chapter 60
closing provenance; the existence theorem remains an imported deep input.
