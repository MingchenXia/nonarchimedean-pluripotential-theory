# Chapter 60: order and quantitative stability of maximal rays

Date: 24 September 2026.
Baseline: `dab8cc37f71a6565d2e5c8d73b89fa9d038a96f7`.
Scope: the converse/maximal-ray paragraph in Section 60.5 through the
two convergence examples, before the test-curve comparison section.
The preceding radial-limit construction and all text from the test-curve
comparison onward retain their baseline bytes. No research atom is retired.

## Mathematical changes

The cited maximal-ray theorem now states its probability-normalized
energy identity explicitly. Its proof still imports existence, decreasing
model regularization and identification of the non-Archimedean datum.
The model energy identity is passed through the construction described
in the source. Uniqueness is proved directly by the two comparisons.
No independent construction of a general Kähler maximal ray is claimed.
The retained source-boundary remark distinguishes complex energy
continuity from identification of the limiting non-Archimedean datum;
the projective polarized energy argument is not silently applied to a
transcendental class.

The order proposition now proves both directions. The reverse implication
uses a common admissible growth correction, reversed monotonicity of
generic Lelong numbers, and the already proved divisorial order test.
Affine translation changes initial values by b and data by c. It gives
the bound B+C s when the initial potentials differ by at most B and
the non-Archimedean potentials differ by at most C. A bound only in
the initial value persists uniformly for all time when the data agree.
The comparisons are inequalities between extended-valued psh functions,
not an undefined subtraction at simultaneous poles.

The complex metric is fixed locally with the probability normalization.
For ordered potentials its rooftop formula reduces to an energy difference.
Together with the cited maximal-ray energy identity this proves

`d1(U(u,phi)_s,U(v,psi)_s) = d1(u,v) + s(E(psi)-E(phi))`

when u<=v and phi<=psi. Every term is finite. For a finite-energy
geodesic W whose non-Archimedean datum phi also has finite energy,
maximality compares W to U(W_0,phi). Complex energy affinity gives

`d1(W_s,U(W_0,phi)_s) = s(E(phi)-e_W)`,

where e_W is the complex energy slope. The difference is nonnegative,
and it vanishes exactly when W is the specified maximal ray. The
finite-energy hypothesis on phi is explicit; the proof does not infer
it for every geodesic ray in an arbitrary Kähler class. This is a formal
deduction from the existence input and metric nondegeneracy, not a new
independent proof of the general slope comparison.

For u_j decreasing to u and phi_j decreasing to phi, with both limits
of finite energy, order gives U<=U^(j+1)<=U^j. The exact metric formula
gives the supremum of the distance on [0,T] as the initial energy gap
plus T times the data energy gap. Both tend to zero by the previously
established monotone energy laws. The pointwise limit is identified
using the finite-energy lower barrier U and the ordered energy formula.
This conclusion concerns already existing maximal rays; it is not used
in a circular construction of their existence or data identification.

The constant rays U(0,1/j)_s=s/j show that convergence is uniform on
each finite time interval but need not be uniform on the whole half-line.
The same constant family attains the perturbation bound B+C s. The
previous example -min(s,j) is preserved with its exact non-Archimedean
values and iterated energy limits. Its approximants are general psh rays
with a corner, not geodesic rays, so the new closure corollary does not
apply. The scalar calculations also cover a zero-dimensional X.

## Sources and dependencies

The [18 September 2025 Mesquita-Piccione version](https://arxiv.org/html/2409.06221v2)
was checked at Definition 5.1.6, Theorem 5.1.7 and its proof, Lemma
5.1.8 and Remark 5.1.9. Printed page 47 was rendered and visually
inspected. The updated citations use `MPTropicalV2`. PDF SHA-256:
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.

The existing BBJ comparison was rechecked against
[arXiv version 3](https://arxiv.org/pdf/1509.04561v3), Section 1.4,
p. 10, and Lemma 6.3, Theorems 6.4 and 6.6, and Corollary 6.7,
pp. 25–26. These locators refer explicitly to that version. Its
projective scope and its stronger competitor class in Definition 6.5
are kept separate from the MP definition. Attempts to read the
published source via the AMS DOI returned an access error; the author's
published-PDF URL failed TLS hostname validation. No publication locator
was inferred from the preprint numbering, and TLS checking was not disabled.
The existing bibliographic metadata are unchanged.

The rooftop metric, its nondegeneracy and complex energy affinity use
Appendix H, Definition `def:appH-i-d1` and Theorem
`thm:appH-weak-geodesic`. Monotone continuity of the non-Archimedean
energy uses the previously proved extended-pairing continuity. The new
arguments prove their formal deductions from those inputs. They do not
claim a new proof of the Darvas metric theorem or a production-verifier
or independent-agent receipt.

## Two passes and validation

The first full build produced 3,981 pages (18,949,337 bytes). Physical
pages 3369–3373 were rendered and inspected. It had one 9.52pt
horizontal overflow caused by the long proof heading, and no unresolved
reference or citation. The second full statement/proof/source/notation
pass checked the competitor class, both order directions, common growth
correction, finite-energy domains, normalization of d1, all nonnegative
energy gaps, the case T=0 and the two examples. It shortened the proof
heading, declared the metric's domain, made linear growth explicit in
the energy-gap assertion, and replaced the L1 convergence argument by
a direct ordered-energy proof of the pointwise limit. It also gave
explicit constant data attaining both perturbation bounds.

The final full build and page-by-page inspection of physical pages
3369–3373 are complete. This is a scoped visual review, not an all-page audit.

- Full build: PASS, **3,981 pages, 18,949,676 bytes**.
- Reference/input check: **390 TeX files, 11,643 unique labels**; no
  missing input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply-defined label,
  rerun request or horizontal/vertical overflow. Existing class and
  underfull warnings remain.
- Scoped strict house audit: zero errors and one reviewed exact-author-version
  arXiv warning; strict mode returns 1, not a warning-free strict pass.
- Inventory: PASS, **45 active atoms / 14 environments**, tiers
  **(0,5,8,15,17)**.
- Surrounding Chapter 60 text is byte-identical to the baseline.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`71cff9f54c42e1bdc4883976530499a4d89cda15aa2ea4ea7a476669add78295`.
Final live PDF SHA-256:
`a8ee8b793b90939e690edc1951e3667aa6f04cb3f17dff5779a132987fb768c4`.

The P12.1 fragment retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The supplied CURVE_PSH.tex retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
All 45 active atoms, P12.2–P12.6, supplied originals, bibliography,
frozen packets, verifier receipts and dated releases are preserved.
The PDF remains an ignored live build product. Next work is the
finite-energy test-curve comparison and its exact normalization; the
general Kähler existence inputs above remain explicit dependencies.
