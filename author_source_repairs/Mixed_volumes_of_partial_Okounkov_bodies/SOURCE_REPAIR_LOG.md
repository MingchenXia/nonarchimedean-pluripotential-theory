# Source repair log

Date: 24 August 2026

## Exact files and backups

The repair started from the three files in
`/Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies`.
Before the repaired files were written back, the original source files were
preserved in the same directory as

- `main.tex.pre_repair_20260824_9a039a5070d2f82a.bak`, SHA-256
  `9a039a5070d2f82ae258d56eec22c8cb998c473b4234158ac1ddd5ebbef78298`;
- `ComplexGeometry.bib.pre_repair_20260824_40b2872e09f01661.bak`, SHA-256
  `40b2872e09f016612fe79403173e94e08ce0bfadab3a4afd84db399963630030`.

The repaired source now installed in Downloads has the following exact
identities:

- `main.tex`, SHA-256
  `5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`;
- `ComplexGeometry.bib`, SHA-256
  `e3e48c5c503cd6cdaa7bb2e02bdbc02767031e3084c52eff7415258d9483813e`;
- `cgeometry.sty`, SHA-256
  `0457ca10bb144696ec525375467832130acab7dad7a40b4f174dc3f8a8bb6ead`.

The style file was not changed: its original and working-copy hashes were
already identical.  The bibliography change updates the dated `XiaBook`
record to the supplied 18 July 2026 version.  No use or citation of
arXiv:1710.09731 was introduced.

The bibliography's exact 18 July 2026 PDF was downloaded again from its
recorded URL and checked directly (PDF SHA-256
`c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`).
It confirms the four load-bearing locators used in `main.tex`:
Proposition 10.3.10 for the Minkowski inclusion, Proposition 10.3.4 for the
finite-level Hausdorff limit, Proposition 6.2.5 for closure of the
`P`-order under simultaneous `d_S` limits, and Remark 10.3.1, equation
(10.22), for the log-resolution formula.  A later automated suggestion of
different section numbers was therefore rejected against the primary PDF;
the installed source already had these locators right.

## Mathematical repairs to `main.tex`

1. **The Cao-volume domain and the \(\mathcal I\)-model reduction.**
   The pure and mixed Cao volumes are defined for the actual theorem domain,
   without assuming positive raw non-pluripolar mass.  At the start of the
   main proof each input is replaced by its \(\mathcal I\)-model envelope.
   This preserves all partial bodies, turns positive Cao volume into positive
   raw mass, and only then enters the \(d_S\)-approximation theory.

2. **Exact volume-comparison sources.**  Definition 3.2, Proposition 3.3,
   and Theorem 3.5 of *Transcendental b-divisors I* are cited for the mixed
   volume used in the statement.  The BFJ and BEGZ sources needed for the
   movable-product specialization are stated precisely.

3. **The potential sandwich.**  The proof now obtains both pointwise traps
   \(\eta_j\leq u_j,u\leq\psi_j\).  Raw-mass continuity is used only to
   discard a finite initial segment; the inequalities involving the limit
   follow from closure of the \(P\)-order under \(d_S\)-limits and modelness.
   A finite successive extraction supplies one subsequence for all inputs.

4. **The convex sandwich.**  The abstract lemma now assumes all four
   inclusions
   \(A_{i,j}\subseteq C_{i,j},D_{i,j}\subseteq B_{i,j}\).  The John-ellipsoid
   normalization controls the determinant in both directions, and the
   Blaschke subsequence argument proves convergence of the full sequence.

5. **General valuations and finite leaves.**  The proof works for every
   surjective valuation to \(\mathbb Z^n_{\mathrm{lex}}\), not only flag
   valuations.  Abhyankar's inequality and the algebraic closedness of
   \(\mathbb C\) give residue field \(\mathbb C\), one-dimensional leaves,
   and the exact value count in finite-dimensional subspaces.

6. **Finite-level degeneration.**  The proof separates the
   one-dimensional-factor case before using general hyperplanes.  It uses
   only the valid inclusion between the matrix initial ideal and the toric
   ideal, treats multigraded irrelevant torsion before passing to
   `MultiProj`, retains component multiplicities, and then applies the
   Bernstein--Kushnirenko formula with the full-lattice hypothesis.

7. **The movable upper bound.**  One divisible degree simultaneously gives
   birational Kodaira maps and unit valuation differences.  A common
   resolution of the base ideals produces the nef approximants; BFJ
   Propositions 2.12--2.13 give the intersection bound, and the finite-level
   bodies converge along the same divisible sequence.

8. **Uniformity in the valuation.**  Both convex-body sandwich chains are
   displayed, the positive-volume locus is entered after one finite discard,
   and the containing Minkowski sums are bounded by the ordinary body of the
   tensor product.  The final passage to suprema uses the explicit uniform
   estimate \(\lvert\sup f_j-\sup f\rvert\leq\sup\lvert f_j-f\rvert\).

9. **Rational analytic singularities.**  On a common log resolution the
   residual classes are kept in the rational divisor category.  General-
   valuation numerical invariance is sourced from Proposition 10.3.2 of the
   supplied book.  The reverse inequality is obtained by multiplying with
   the canonical sections of effective divisors and applying Wilms's common-
   flag theorem to the ample perturbations.  No maximizing valuation is
   asserted.

10. **The ordinary-body theorem.**  The first theorem now has a complete
    proof.  For minimal metrics, containment of the partial body in the
    ordinary body and equality of their positive Euclidean volumes force
    equality of the bodies.  BEGZ and BFJ then identify the mixed mass with
    the movable product, reducing the statement to the already proved metric
    theorem without circularity.

All original theorem, proposition, lemma, section, and equation labels were
preserved.  Existing `\eqref` targets remain unchanged, and object references
use `\cref`.

## Audit and verification

The repaired proof packet has SHA-256
`9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`.
Production Rethlas (`gpt-5.6-sol`, `xhigh`) returned `correct`, with zero
critical errors and zero gaps, for that exact mathematical proof object.

The exact source snapshot above then received a separate hostile line-by-line
audit.  Its verdict was PASS with no must-fix finding.  The frozen
`main.tex` was also submitted verbatim as the proof object in a second
production Rethlas run.  Run `20260824T032252Z_b8adabf0730c`, using
`gpt-5.6-sol` at `xhigh`, returned `correct`, with zero critical errors and
zero gaps.  Its proof digest is the installed `main.tex` digest above; the
checked item is `pi_b80d4a29bb37992748e896a6`, the aggregate context digest
is `fd4588256a3682f58b525f88ce4289d20806a11590cafe5ef30b2d70483a541a`,
and the adaptive-context digest is
`f93d73c0b08f46c520b1d7cffe8960cd9499e557c825d0b8de11086cffbeb143`.

## Compilation after installation in Downloads

The installed files were rebuilt in their original Downloads directory with

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The build exited with status 0 and produced an A4 `main.pdf` of 12 pages and
445824 bytes.  The final `main.log` and `main.blg` contain no unresolved
reference, unresolved citation, LaTeX error, overfull box, or underfull box.
The only terminal diagnostic is the benign pdfTeX font-expansion message.
