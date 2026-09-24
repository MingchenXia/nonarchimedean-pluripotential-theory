# Chapter 64: common models and uniform continuity — 24 September 2026

## Scope and baseline

Baseline: `9f70d484a9fc8d52f7441063cd93c349d1f01b81`. The live main branch was clean and aligned
with the locally recorded origin/main. Drafting and both full builds used
a separate export. No concurrent live build or Git mutation was found.
The first fresh fetch failed with a transient TLS error and was retried.
The six supplied-source integrations in the baseline are preserved.

The continuous comparison previously invoked an unspecified local-height
constant and applied monotone continuity successively in the mixed slots.
This unit reconstructs the estimate and simultaneous limit. Chapter 6's
imported continuity theorem and Chapter 24's projection and bounded
extension are retained. This is a local consequence audit, not a new
research solution or an independent/production verifier receipt.

## Mathematical checks and repairs

Under a common model domination, contracted special-fibre components have
zero pulled-back mixed degree by projection. Above E, degrees multiply
by e_F and sum b_F e_F = b_E follows by pushing forward div(pi). The
analytic point is unchanged, proving invariance with multiplicities.

For f = phi_D on a projective model, clear denominators by q and twist
a sufficiently high relatively ample power by qD. Taking qth-root
metrics expresses f as a difference of two nef model metrics on the
same ample rational line bundle A. Telescoping each metric slot and
symmetry of vertical intersections move its weight difference onto
ddc f. Splitting the latter gives two positive measures, each of mass
c_i = (A L_1 ... omit L_i ... L_n). The bound has constant 2c_i,
independent of all approximating models and metrics.

Positive fixed-mass model measures have Cauchy integrals on every model
test. Density and the 2M epsilon estimate extend this to continuous tests.
Riesz representation works on the compact Hausdorff analytification
without metrizability. Comparing two approximating systems proves
independence. If M=0, every measure is zero; no division occurs. The
estimate also gives uniform-net and joint continuous-tuple continuity.

The BFJ part retains smooth projectivity, discrete valuation, residue
characteristic zero and ample classes in all slots. One common
subsequence has errors at most 2^(-j); adding the rational constant
3*2^(-j) makes every slot decrease while leaving curvature unchanged.
The second pass makes explicit that BFJ Theorem 3.1 uses a single
reference form. For different ample classes, its pure case is applied
to each term of the finite polarization identity. Separate continuity
alone is not used to justify a diagonal limit. The zero-dimensional
empty-product case is stated separately. General singular CLD products
and MP/BJ operator compatibility remain outside this argument.

Pure dimension is now explicit in the model setting, matching the formal
intersection source. The semistable example requires a residue-field-
rational node for E_0 E_1 = 1. The nonreduced example now assumes E_0 is
Q-Cartier before using its model function. These are hypothesis repairs.

Blowing up P1 over C[[pi]] gives a rational skeleton edge with reference
measure d delta_0. The rational model potential -d min(s,t), composed
with retraction, has Laplacian d(delta_t-delta_0). Component degrees are
nonnegative, so the metric is nef. Its uniform distance is d|t-u| and
its measure is d delta_t. As t tends to zero, weak convergence holds,
but the total variation norm of the difference remains 2d. Probability
normalization gives norm 2. Exact arithmetic verifies 363 polarization
tuples (dimensions 1--5 and entries 0,1,2), 171 extreme consecutive-error
pairs, and 390 degree/cutoff pairs on a twelfth-integer grid. The last
checks cover mass, positivity, variation and integration by parts on
common subdivisions. They test examples, not the general proof.

## Primary sources

- [CLD, 25 July 2025](https://webusers.imj-prg.fr/~antoine.chambert-loir/publications/papers/fdceb-20250725.pdf),
  Theorem 18.5.5 and Proposition 18.5.8, printed pp. 528--531:
  pure relative dimension, boundaryless generic fibre, full formal
  factors and the relatively normal discrete-valuation simplification.
  The previously downloaded primary PDF text was consulted.
- [Boucksom--Eriksson, published article](https://research.chalmers.se/publication/522347/file/522347_Fulltext.pdf),
  Advances in Mathematics 378 (2021), 107501, Theorem 8.4 and Lemma 8.6,
  printed pp. 71--73: joint uniform-to-weak extension on continuous
  psh-regularizable metrics and the integration-by-parts estimate.
  The proof invokes Lemma 5.17 for difference-of-FS decomposition.
  The book proves the model counterpart directly; model metrics are
  not represented as smooth CLD metrics.
- [BFJ, published author offprint](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BFJ_nama.pdf),
  Theorem 3.1 and Section 3.2: bounded mixed products for a single ample
  reference class and joint decreasing-net continuity. The published
  source text and induction A(p) were retrieved through web search.
  The single-class restriction is respected by finite polarization.

Direct complete BFJ and BE PDF downloads failed with TLS/time-out errors;
the BE browser screenshots also failed. No successful fresh complete PDF
or visual primary-source inspection is claimed for those papers. The
retrieved primary text supports the cited locators. No bibliography or
source-version record was changed.

## Final checks and preservation

Both full build rounds completed. The second pass rechecked the domains,
signs, constants, zero cases, common subsequences and polarization, then
made the different-class reduction and ample-slot restriction explicit.
The scoped house audit passes strict mode: zero errors and zero warnings.
The final PDF has **4,042 pages** and **19,257,234 bytes**.
No unresolved references/citations, duplicate labels, rerun requests or
horizontal/vertical overflows remain. The 13 inherited Chapter 70 PDF
destination warnings are unchanged.

The full source closure has 396 inputs and 11,795 unique labels, with
no missing inputs, dangling references or structural issues. The inventory
remains 43 atoms in 13 environments with tiers (0,3,8,15,17). First-pass
physical pages 3487--3493, 3495 and 3502 were visually inspected. Final
physical pages 3487--3493, 3495--3496 and 3501--3502 cover every changed
paragraph and formula with their transitions. They fit the existing layout. A final notation pass declares the reference
forms before their weights and clarifies the curve parameter and curvature
notation. Its full rebuild and physical-page 3490--3493 recheck pass.

Before progress records were updated, all 4,169 baseline tracked files
except Chapter 64 were byte-identical. Only Chapter 64 and four current
progress/audit files are delivered. The six supplied integrations, author
originals, archives, P12.1 records, research ledgers, frozen passages,
verifier receipts and dated releases are unchanged. The Chapter 64 DH and
finite-energy comparison blocks retain their baseline bytes. The checked
PDF replaces only the ignored current book.pdf; build files are not staged.

Final PDF SHA-256: `e23833af3463fca1274bfb75407f5f130a2cc534ffa0e65a6d287f00cb947980`.
Final Chapter 64 SHA-256: `d541285d081bac535519efff1e090bebbc43284fe789d14ca841efc4a13d5351`.

From manuscript/, run `python3 editorial/tools/refcheck.py` and
`python3 editorial/tools/check_open_problem_inventory.py`.
Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`.
