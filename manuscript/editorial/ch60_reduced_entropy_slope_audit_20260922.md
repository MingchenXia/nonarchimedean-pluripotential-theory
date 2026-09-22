# Chapters 59, 60 and 62: reduced entropy slopes — 22 September 2026

## Normalization and analytic volume estimate

The previous warning correctly disproved the total-discrepancy slope
inequality in MP24 arXiv version 2, Proposition 6.2.2 and Corollary 6.2.3,
by the trivial ray. That counterexample is retained. The new argument
proves the reduced inequality with the lost normalizing term accounted for.

For a smooth dominating analytic snc model, put

D = K_(model/(X x P1)) + (central fibre)_red - central fibre.

The coefficient along E is k_E+1-b_E. Dividing by b_E gives
A_total(v_E)-1, so the model function of D is the reduced discrepancy
test g_model=A_total composed with the retraction, minus one.

A smooth invariant Hermitian metric on the logarithmic relative
canonical bundle induces fibre volume forms nu_tau. The test
f_s=log(nu_tau/mu), with s=-log|tau|^2, has local expression
-log|h_D|^2 plus a smooth function. This checks the divisor sign and
the squared-norm compatibility convention directly.

The proof supplies the local analytic calculation in
[BHJ19 arXiv version 5, Lemma 3.11, pages 18–19](https://arxiv.org/pdf/1603.01026v5).
In coordinates tau=product z_j^(b_j), the fibre logarithmic canonical
frame has p logarithmic factors. Its radial integral is the volume of
a p-dimensional region of size O(s), hence O((1+s)^p).
The angular variables, ordinary coordinates and finite branches only
affect constants. A finite chart cover and properness give an upper
bound C(1+s)^n. A chart at a point on just one central component gives
a positive uniform lower bound. Therefore
log integral exp(f_s) dmu divided by s tends to zero.

This local proof uses analytic snc coordinates and compactness; it
does not invoke a projective global theorem for a transcendental
Kähler class. The constants need not be uniform over models.
The [official BHJ19 erratum](https://ems.press/content/serial-article-files/32635?nt=1)
was also checked: it concerns Theorem 5.6, which this argument does
not use. The checked version 5 already incorporates that correction.

For the total divisor D+central fibre, the test becomes f_s+s and
the logarithmic normalizer has slope one. This explicitly identifies
the term incorrectly discarded in the total-discrepancy argument.

## Entropy and Mabuchi deductions

For each fixed model, the entropy variational inequality with test
f_s is combined with the imported mixed-slope theorem, using the
testing slot (0,f_s). The pairing is divided by V_alpha, matching
the probability-normalized Monge--Ampère measure. The fibre-volume
normalizer contributes slope zero.

The increasing continuous reduced model discrepancies have supremum
A_NA. The proof handles their directed net without appealing to an
invalid unrestricted monotone-convergence statement: a continuous
minorant is dominated up to epsilon by one model, using a finite
open cover of the compact spectrum and a common dominating model.
The Radon characterization of the integral of a nonnegative lower
semicontinuous function then gives the supremum of model integrals.
This includes infinite entropy.

The finite energy and twisted-energy slopes yield the Mabuchi
liminf inequality. Chapter 59's normalization warning and Chapter
62's model-ray comparison now point to this proved reduced lower
bound. Chapter 62 retains the factor V converting normalized
potentials to its model invariant.

No entropy-slope equality is inferred. The full mixed-slope theorem,
maximal-ray existence and sequential regularization remain the
explicit imports from
[MP24 arXiv version 2](https://arxiv.org/html/2409.06221v2).
The cscK existence implication still uses
[MPWN25 arXiv version 1, Theorem 2.4.3](https://arxiv.org/html/2509.09442v1)
as a deep source theorem; it is not claimed to follow from the
entropy calculation alone. No research question is retired.

## Validation

The second pass checked the canonical divisor identity, central
multiplicities, local metric sign, logarithmic density, finite
branches and chart cover, the one-component lower bound, fixed-model
order of limits, the probability factor, extended-real entropy,
Radon net passage and the remaining source dependencies.

The complete entropy block and Chapter 62 companion block pass the
strict writing audit with zero errors and zero warnings.
The pre-final scoped Chapter 60 build has 101 pages and no unresolved
reference, citation or overfull box; physical pages 85–89 were
rendered and inspected. The final prose adjustment to the testing-slot
sentence was verified in the complete build and in its rendered pages,
not represented as part of that earlier scoped build.

The final full build succeeds with 3,407 pages and 18,009,799 bytes.
There are zero unresolved references or citations, 38 horizontal
overflows and zero vertical overflows. Physical pages 2936–2938
(printed 2868–2870) and 2956 (printed 2888) were rendered and inspected.
The new entropy material and companion model inequality fit the pages.

The source closure has 389 TeX files and 11,486 unique labels, with
zero missing input, duplicate, dangling reference or structural
defect. The inventory check passes at 46 active atoms in 14 problem
environments, with tiers (0,5,8,16,17). The source diff is whitespace-clean.

Final PDF SHA-256:
`5dff17a3b461214d712aec413fb4ccbb4331eda4c7f1bff6c99a6d8295b780fa`

Chapter 59 SHA-256:
`39dff8ba53b71e71dd752591e35c19b5ca0107530f3364338380c096b178c662`

Chapter 60 SHA-256:
`c03f66742653e9d1d5957349a3b957efa406f3b7830f3f613f6256fa71327659`

Chapter 62 SHA-256:
`d959f06205a2009fb201fdfa26166ef3dfa0679c6f12775a84fa046dfad2d706`

These are the only three production files changed since bc9241f.
The restored CURVE_PSH.tex and the entire frozen Chapter 71 retain
their previously recorded SHA-256 checksums. Historical build and
research-verification receipts are not rewritten.

The next layout check will investigate the different body size
observed between the scoped Chapter 60 build and the complete book.
Its cause is not yet established. The 38 existing overflows remain
an outstanding layout task, not a failure of the source-reference check.
