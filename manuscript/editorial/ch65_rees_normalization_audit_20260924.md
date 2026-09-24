# Chapters 33 and 65: Rees reconstruction and normalization — 24 September 2026

## Scope and baseline

Baseline: `fa82618a8f67d0432298b0b7856967e9cb59d2aa`. The main checkout was
clean, no concurrent build or Git mutation was found, and a fresh fetch
confirmed no divergence from the designated GitHub origin. Drafting and
full builds used a separate export. This unit repairs the algebraic
filtration/test-configuration correspondence and its normalization rules.
The analytic ray correspondence and BHJ19 erratum quarantine retain their
previous scope. No new research atom is resolved and no independent-agent
or production-verifier verdict is claimed.

## Mathematical corrections

Chapter 65 first takes the filtration of the actual relatively ample
model. The parameter has weight -1, so a regular section s varpi^(-lambda)
has weight lambda. Full equivariant lattices give integral attained jumps;
ceil(lambda)+ceil(mu)>=ceil(lambda+mu) gives multiplicativity for real
indices. The generator weight/degree ratios give uniform linear bounds.
An algebraic character shift is rational after clearing polarization
denominators; arbitrary real shifts exist only as filtration operations.
Chapter 33's invariant-extension calculation now uses varpi^(mc), giving
the claimed plus sign in the weight shift.

Relative Proj of a degree-one Veronese Rees algebra is projective and flat:
its affine charts are torsion-free over the parameter PID. Exhaustivity
identifies the punctured product. The returned section algebra is its
section saturation; finite normalization can enlarge it further.
Normalization commutes with homogeneous localization, and section
saturation recovers all sections of the pulled-back polarization.
The normal ample correspondence therefore uses saturated integral-closure
classes of filtrations, a common Veronese index, and fixed linearization
and rational polarization. A relatively semiample total space contracts
to its ample model; a large multiple need not embed the original space.
Both erroneous semiample reconstruction steps in Chapter 33 are corrected.

The full ample section ring has a finite Fubini--Study supremum at every
semivaluation, including proper-support points. Global generation gives
a section with value zero at its center and supplies the lower linear
bound. Individual terms can equal minus infinity, but the full supremum
lies between the two linear-bound constants.

For integral-closure invariance, let b be this finite supremum. In a local
frame extend the semivaluation by a Gauss variable z of value b for section
degree and by W(varpi)=1. Every Rees element has nonnegative value. A
monic integral equation precludes a new element of negative value; this
bounds every new Fubini--Study contribution by b. Quotienting by the
support first includes infinite-valued semivaluations. The same power
argument used for Veronese restriction handles section saturation.
This proves invariance of the supremum, not of each base ideal or weight.

The explicit example on P1 uses

    A = C[varpi,x,y,varpi^(-2)x^2],
    chi_m(x^a y^(m-a)) = 2 floor(a/2).

Its integral closure is C[varpi,x/varpi,y], with new weight a. In degree
one the threshold-one space changes from zero to Cx, so the individual
base ideal and its value change. Both Fubini--Study functions are
max(-v(y),1-v(x)), including proper-support cases. The normal ring
A0=C[t,x,y,t^(-1)x^2] has weights floor(a/2); its raw double base change
is A. Thus normalization after base change need not multiply finite
weights exactly by two, even in arbitrarily large divisible degrees.

The second Veronese algebras are the relative conics V^2=tUW and
V^2=varpi^2 UW, with rational polarization O(1)/2. Their full section
lattices equal the indicated graded pieces: the hypersurface sequence
has obstruction H1(P2_B,O(k-2))=0. The weight discrepancy therefore
occurs on actual test configurations, not just in an unsaturated
low-degree presentation. Raw base change dilates weights exactly;
normalization preserves the limiting DH measure by the separately cited
normalization theorem. Relative integral closure has the same full
normalization, so the Chapter 33 convention gives the same conclusion.

The algebraic commutative diagram now specifies the raw ample Rees model
and section-saturated filtration. Its lower functions are preserved by
normalization, while the upper filtration can change.

## Sources and two review passes

- [BHJ, published article](https://aif.centre-mersenne.org/item/10.5802/aif.3096.pdf),
  Section 1.2 and Corollary 1.4, printed pp. 754--755: equivariant lattices,
  invariant extensions and the parameter sign. Equation (2.1), Lemma 2.13
  and Proposition 2.15, pp. 768--769: section filtration, invariance under
  a pullback with pushforward O equal to O, and the ample Rees
  correspondence. Proposition 2.17, p. 770: the ample contraction of a
  semiample configuration. Theorem 3.14, p. 778, and Corollary 5.8 and
  Proposition 5.9, p. 792: normalization invariance of DH and identification
  with the filtration limit. The primary PDF's indexed text, including
  the relevant proofs, was checked. A fresh full download encountered a
  TLS error; a fresh local copy or visual BHJ source inspection is not claimed.
- [BJ, published article](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf),
  Proposition 2.30, Theorem 2.31 and Corollary 2.32, printed pp. 685--686:
  unique ample integrally closed representative and the PL/FS
  correspondence. The previously downloaded published PDF was read;
  physical pages 40--41 were visually inspected. The exact existing
  bibliography entries are retained.

The first pass reconstructed the lattice, Rees and Gauss arguments,
checked the primary sources and found the weight/base-ideal
counterexample. The second pass reread the complete adapted statements
and proofs, supplied the relative conic realization, distinguished raw
from normalized base change in the dependent DH proof, clarified
homogeneous localization, and repaired an orphan warning heading.

Exact arithmetic checks cover 495 monomial weights, 400 multiplicative
pairs, 49 rational FS values, 1,271 normal-semigroup membership tests,
and 30 complete conic section bases with normalized weight-measure
comparisons. These test the examples and conventions, not the general
proofs. A fresh hash comparison identifies the three attachments with
the already integrated originals, and all 17 preserved-original hashes
pass. The six supplied proof integrations retain their exact bytes.

## Validation and preservation

Both review passes completed full-book builds. Final output: **4,050
pages**, **19,287,426 bytes**. The source closure has **396 inputs and 11,804
unique labels**, with no missing inputs, dangling references, duplicate
labels or per-file structure errors. The inventory remains **43 active
atoms in 13 environments**, tiers **(0,3,8,15,17)**. There are no unresolved
references/citations, rerun requests or horizontal/vertical overflows.
The 13 inherited Chapter 70 duplicate PDF destination warnings are unchanged.

The scoped house audit has zero errors. The Chapter 65 scope has one
reviewed warning for the inherited `warn:rf-infinite-generation` label;
its established anchor and warning environment are retained. The changed
Chapter 33 prose has zero warnings. The first visual pass covered physical
pages 2284--2287, 3507--3513 and 3516--3517. Final changed-page review covered
2284--2287, 2295--2296, 3507--3514 and 3516--3518 (17 pages).

Before progress records were updated, all 4,171 baseline tracked files
except the two revised chapters retained their exact bytes. The supplied
source integrations, original attachments, CURVE_PSH, P12.1 material,
research ledgers, frozen packets, verifier records and dated releases
are unchanged. The BHJ19 erratum quarantine is byte-identical. Only the
two chapters and four current progress/audit files are delivered. The
checked PDF replaces only the ignored current manuscript/book.pdf.
No build auxiliaries or temporary source downloads are staged.

From manuscript/, run `python3 editorial/tools/refcheck.py` and
`python3 editorial/tools/check_open_problem_inventory.py`.
Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`.

- `manuscript/book.pdf` SHA-256: `1c77aa215ecde4667fd176db6e7b646744dd2028d1fc888adf50e4b97206cd26`.
- `manuscript/parts/part4/ch33_test_configurations.tex` SHA-256: `1f06d4b1e3cfd1ab8a5c72feaf9e4ddf378052e8f4a60795fc31ef3807b8c7c7`.
- `manuscript/parts/part6/ch65_rays_filtrations.tex` SHA-256: `f8f1a3989c46b172b712bf77862248335ca4c99ad060792099fdab64e4516cd3`.
