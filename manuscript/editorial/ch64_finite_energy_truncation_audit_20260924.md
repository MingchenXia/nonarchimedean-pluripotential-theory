# Chapters 24, 26 and 64: finite-energy truncations — 24 September 2026

## Scope and baseline

Baseline: `b1926064f5f845a6f4dd109e46f5989f042434e5`. The main checkout was
clean, and no concurrent build or Git mutation was found. Both revision
passes and full builds used a separate export. Fresh GitHub fetch attempts
encountered TLS errors; synchronization is checked separately from the
mathematical and build record below.

This unit reconstructs a consequence of the existing bounded maximum
principle and finite-energy tail estimates. It corrects contradictory
exposition and supplies the proof and normalization of canonical mixed
truncation convergence. It does not resolve a new research atom or certify
compatibility between distinct singular Monge--Ampere constructions. No
independent-agent or production-verifier receipt is claimed.

## Mathematical review

In each of the BFJ and BJ settings separately, use one fixed ample class
and nonpositive finite-energy potentials phi_1,...,phi_n. BFJ retains smooth
projectivity, complete discrete valuation and residue characteristic zero;
BJ uses the integral projective trivially valued setting. The raw energy
has constant-translation factor V=(omega^n), so it is V times the normalized
BJ energy. Dimension is positive; no division by a zero volume is made.

For independently chosen cutoffs t_i, set T=min t_i, U_T=intersection of
{phi_i>-T}, and B_T its complement. The bounded mixed maximum principle
identifies every truncated measure on U_T with the equal-T truncation.
These sets are Borel, not necessarily open. The BJ argument explicitly
polarizes Theorem 7.40 by adding bounded auxiliary potentials to both
maximum arguments and dividing by 1+sum c_j. The strict inequality set
is unchanged; multiplying by (1+sum c_j)^n permits coefficient comparison.
No assertion of ordinary open-set locality on U_T is used.

Positivity of the expansion at the average w_T gives domination by
n^n/n! times its pure measure. One term of the bounded raw energy gives
integral(-w_T) MA(w_T) <= (n+1)(-E^u(w_T)). On B_T, -w_T >= T/n,
while w_T dominates the average of the original potentials. Consequently
nu_T(B_T) <= kappa_n (-E^u(average phi))/T, where
kappa_n=n^(n+1)(n+1)/n!. Convexity of E1 makes the bound finite.

Every bounded truncation has the same mass V, so agreement on U_T gives
the same tail mass on B_T. Comparing an arbitrary cutoff tuple with an
equal-level cutoff r>=T bounds their total variation norm by twice that
tail. Pass r to infinity against continuous tests, then use Radon-measure
duality. The result is

    ||nu_t - mu(phi_1,...,phi_n)||_TV
        <= 2 kappa_n (-E^u(average phi))/min_i t_i.

This proves convergence with independent cutoffs and uniformity on families
with bounded negative average energy. Dividing both measure and energy by
V gives the probability convention without changing kappa_n. The proof
never restricts a weak limit to an arbitrary Borel set.

For the harmonic-series curve potential, the truncated measure has mass
1/m at x_m and masses 1/(k(k+1)) at x_k for k<m. Its difference from the
limit has positive and negative masses 1/(m+1), hence total variation
2/(m+1). Exact rational arithmetic checks full mass, this norm, the energy
identity E_m=-(1/2) sum_{k<=m} 1/k^2, and the dimension-one bound for all
m=1,...,100. These are checks of the example, not numerical proof of the
general theorem.

A logarithmic pole has truncation energy -m/2; its measures converge weakly
to a polar atom while its nonpluripolar measure is zero. Conversely, the
moving-atom model example from the previous unit can be made decreasing
by adding the constant dt: chi_t(s)=d max(t-s,0) decreases uniformly to
zero as t decreases to zero, while the measure difference has norm 2d.
The stronger convergence is specific to canonical truncation, not arbitrary
decreasing approximation.

Two operators on the same analytification coincide on their common
finite-energy domain if they agree on bounded tuples and both have weak
continuity along canonical truncations. Each hypothesis is stated;
a psh-cone order isomorphism by itself supplies neither one.

Chapter 24 now distinguishes mass loss for arbitrary psh entries from
full mass for E1, and no longer denies truncation-limit construction in
E1. Chapter 26 now proves invariance of E1 under bounded changes of the
potential, using energy monotonicity and constant translation. A common
polar set alone does not determine energy. The tail estimate is recorded
only as a consequence, not a sufficient criterion. The product table uses
restricted truncations; the proof records energy's role in uniform tails.
The curve parameter is called divisorial only for rational values. The
infinite-energy example no longer claims sharpness of a bound that does
not apply, and distinguishes partial from total mass loss at lambda=1.

## Sources and two review passes

- [BFJ, published author offprint](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BFJ_nama.pdf),
  Lemma 6.8 and Proposition 6.9, printed p. 646: quantitative diagonal
  truncation estimate and decreasing weak continuity. The primary PDF's
  indexed text, including both proofs, was checked. A fresh complete PDF
  download or visual BFJ inspection is not claimed.
- [BJ, published article](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf),
  Definition 7.6, Proposition 7.7 and Theorem 7.8, printed pp. 751--752:
  normalized energy, constants, monotonicity and convexity of E1;
  Theorem 7.18 and Proposition 7.19, pp. 756--757: mixed measures, total
  mass and simultaneous decreasing-net continuity; Definition 7.24,
  p. 759: probability normalization; Theorem 7.40, p. 768: the Borel
  maximum formula. The previously downloaded published PDF was read;
  physical pages 106, 111, 112 and 123 were visually inspected.
- Internal dependencies: the singularity-type definition in Chapter 21;
  bounded mixed maximum, average domination, mixed tails and mixed E1
  extension in Chapter 26; normalized BJ energy and mixed measure in
  Chapter 46. Existing source versions and bibliography entries remain.

The first pass reconstructed the tail, mass and total variation argument
and checked the examples and sources. The second pass reread the full
statements and proofs, made the BJ polarization and ambient hypotheses
explicit, shortened the product table, and removed wording that could
suggest a converse to the necessary tail estimate.

## Validation and preservation

Both full builds completed. Final output: **4,046 pages**, **19,270,640
bytes**. The scoped house audit has zero errors and zero warnings. The
source closure has **396 inputs and 11,801 unique labels**, no missing
inputs, dangling references, duplicate labels or structural errors. The
inventory remains **43 atoms in 13 environments**, tiers **(0,3,8,15,17)**.
There are no unresolved citations/references, rerun requests or horizontal/
vertical overflows. The 13 inherited Chapter 70 PDF destination warnings
are unchanged.

First-pass physical pages 1776, 1796, 1860, 1879, 1888, 1903, 1905--1906
and 3502--3505 were visually inspected. Final review covered these pages
and 3506, including the changed statements, proofs, table and transitions.

Before progress records were updated, every one of the 4,170 baseline
tracked files except the three revised chapters retained its exact bytes.
The common-model, continuous-comparison and DH portions of Chapter 64
are unchanged. The six supplied source integrations, author originals,
P12.1 material, frozen research passages, verifier records, research
ledgers and dated releases are preserved. Only these three chapters and
four current progress/audit files are delivered. The checked PDF replaces
only the ignored current manuscript/book.pdf; no build auxiliaries are
staged.

From manuscript/, run `python3 editorial/tools/refcheck.py` and
`python3 editorial/tools/check_open_problem_inventory.py`.
Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`.

- `manuscript/book.pdf` SHA-256: `65c9a9452cc6d767e3ee1a2cf95e8713e4746d6942e1828acf7af8ac94cff09d`.
- `manuscript/parts/part3/ch24_bfj_ma.tex` SHA-256: `e638135affbccb672b64a4d40d3b4c94e0b0739d72ecd397fe0ba6dc34c5de59`.
- `manuscript/parts/part3/ch26_energy.tex` SHA-256: `ec9bada82113c296a2e028df4a1a1b02ff1405c6fa7617d309313da52171e281`.
- `manuscript/parts/part6/ch64_compare_ma.tex` SHA-256: `a135be2eb4ae470e6ccfb55e4d983f43494a53357cfae733e26a2c25dd233d79`.
