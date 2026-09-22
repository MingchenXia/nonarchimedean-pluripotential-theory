# Chapter 60: maximal rays and the order of limits — 22 September 2026

## Source boundary

The previous proof inferred E_alpha(U^NA)=E_alpha(phi) directly from
monotone continuity of the model energies. The checked projective
argument actually uses two further inputs: the lower bound of
[BBJ21, arXiv version 3, Theorem 6.4](https://arxiv.org/pdf/1509.04561v3)
and strict monotonicity on ordered finite-energy potentials in Lemma
6.3. The proof of its Theorem 6.6 explicitly uses both. The book now
displays the two-sided energy comparison and explains its projective
polarized scope.

For a general compact Kähler class, existence and identification of
the limiting non-Archimedean data remain imported from
[MP24, arXiv version 2, Theorem 5.1.7](https://arxiv.org/html/2409.06221v2).
This revision does not claim an independent proof of the analytic
existence theorem. In particular, the passage from the model nets
available by definition to a decreasing model sequence is identified as
a further regularization input. The model construction's relative
Kähler hypothesis is recorded from Lemma 5.1.8; its model energy
identity is Remark 5.1.9. The earlier account's unsupported direct
inference has been removed rather than treated as a proved limit rule.

The new definition states the geodesic comparison of MP Definition
5.1.6 on the finite-energy rays used here. Uniqueness follows by
applying comparison in both directions; it does not require a new
domination principle. The projective BBJ definition compares with
general psh rays and is not silently substituted for this definition.

## Direct deductions and example

The new proposition proves order preservation in the initial potential
and in the non-Archimedean datum. It also proves
U(u+b,phi+c)_s=U(u,phi)_s+b+cs. The normalized Lelong formula verifies
the c shift, while b is a bounded constant. Comparison after subtracting
b+cs proves maximality of the translated ray. A uniform bound between
initial potentials therefore persists with the same constant at every
time when the non-Archimedean datum is fixed.

The example U^j_s=-min(s,j) is a spatially constant psh ray on every
compact Kähler manifold. Each approximating ray has non-Archimedean
datum zero, while its decreasing limit U_s=-s has datum -1.
Its normalized energies are exactly -min(s,j) and -s. Taking the time
limit before the approximation limit gives slope zero; reversing the
order gives -1. The approximating rays have a corner and are not
geodesic. Thus the example diagnoses the invalid general interchange
without purporting to contradict maximal-ray existence.

## Validation

The second pass checked the competing-ray class, both directions of
uniqueness, finite-energy domains, the two independent translation
constants, the signs of all normalized Lelong values, both iterated
limits, and the precise scope of each source input. The source energy
comparison was expanded and one new line overflow was removed.
The complete new block passes the strict writing audit with zero errors
and zero warnings.

The scoped Chapter 60 build has 97 pages, no unresolved reference or
citation and no overfull box. Physical pages 79–82 were rendered and
inspected after the final edits. The full build completes all required
LaTeX, BibTeX and index passes and produces 3,405 pages, 17,989,767
bytes, with zero unresolved references or citations. Its 38 horizontal
overflows and zero vertical overflows match the preceding full build.

The complete source check reports 389 TeX files and 11,480 unique
labels, with no missing input, duplicate, dangling reference or
structural defect. The exact open-problem inventory remains 46 active
atoms in 14 environments, with tiers (0,5,8,16,17). No research
question is retired.

PDF SHA-256:
`2057ba32e21949f497655b56fef2b19a0e56a418c692556f2d75834bdcee314b`

Chapter 60 SHA-256:
`59156b1406e3505d27c175edb300866962dd484957d67d0fe3e70384b55b272e`

The only production source changed since commit 4899749 is Chapter 60.
The frozen recovery checksum ledger and research proofs remain
untouched. The next audit concerns the test-curve base point and the
quantitative hypotheses in the mixed-slope passage. The general
Kähler analytic inputs described above remain dependencies, not new
independent certifications.

