# Root technical review: bounded model-net normalization

31 August 2026. Reviewed the two complete replacement proofs, their scope
ledger, exact assembly data and read-only validator. Their author is p081;
root assigned the bounded-tail route and reviewed the resulting arguments.
This is a parent technical review, not a claim of completely fresh
independent invention/review, formal verification, or production acceptance.

No gap was found in the two replacement proofs relative to the precise
standard BFJ inputs stated below. Neither full copied chapter is thereby
certified. In particular the excluded Chapter30 maximum and final descent
claims remain incorrect as written and require separate correction.

Exact reviewed fragments:

- ch26_bounded_energy_replacement.tex:
  c8c3726d0eedd6d3d7bdea91a82ff13661cde8dac246e8a9fcd395622c86708c.
- ch30_bounded_projection_replacement.tex:
  7c684d99bd2efe525d8eef019e419a492a0038f1d6f4b97ad9d5baeadcadf005.
- Full Ch26: e37465c226a13e766ed2eecce014913fca3e5cdc2002e1766c151c83c73c6a74.
- Full Ch30: 02fa119b5732e3270989e3fddc0aa431add6eb04b27c40c208de9b3411ed2e28.
- Author manifest:
  dd2a97d28da10305eab36272cad26a210d2a10b13dd50bb504efe8d9b45184b8.

## Boundedness without modifying potentials

For continuous f_alpha decreasing pointwise to a bounded f on compact X,
the open sets {f_alpha < sup(f)+1} cover X. A finite subcover and one
upper index give the same strict upper bound on a cofinal tail. Every
term already majorizes f, which supplies the lower bound. This works
for arbitrary directed sets, not just sequences, and does not assert
uniform convergence. No minimum, maximum, or translation alters the net.

For a net whose members are only bounded psh functions, a fixed initial
member bounds its cofinal tail from above, and the bounded limit bounds it
from below. Thus Chapter26 Step4 has the same uniform boundedness without
assuming its members continuous.

## Chapter26 proof

The stated weighted monotone continuity from Chapter24 applies with the
weight phi_alpha and each measure slot either phi_alpha or zero. All are
bounded omega-psh; zero is allowed because the chapter's reference omega
is semipositive. This yields the bounded energy formula independently of
the approximation. The additional compact comparison argument in Step2 is
valid: the closed decreasing sets {phi'_beta >= phi_alpha+epsilon} have
empty intersection and hence some member is empty. The epsilon translation
is a comparison majorant only, and model energy has the stated translation
law. Passing first in beta, then alpha, then epsilon is legitimate.

In Step3 finite products of cofinal index sets preserve decreasingness.
Differences in integrands are split into two decreasing psh weights before
applying the weighted continuity theorem; no continuity theorem for an
arbitrary varying signed weight is presumed. The variation formulas come
from finite-degree polynomial identities, whose coefficients are finite
linear combinations of these mixed integrals. Thus differentiation is of
finite polynomials after coefficient convergence, not an interchange of an
uncontrolled derivative and a limit. Step4 then applies the already proved
bounded formula and the earlier Chapter24 theorem, avoiding the invalid
approximation-from-below diagonal in the original text.

The use of Chapter24 is conditional on its bounded MA construction and
weighted monotone continuity, together with original-scope decreasing
regularization and the model energy identities. The exact Chapter24
statement and its weak-continuity/uniqueness conclusion were read; the
replacement does not purport to reprove that entire construction or to
clear its separate upstream manuscript proof gates.

## Chapter30 proof

Each of finitely many input nets is restricted to a cofinal bounded tail,
then indexed on their finite product. Pullback preserves order and bounds;
only the actual divisor and curvature items of the model pullback lemma
are used, not its erroneous real-model maximum item. On each model tuple
the established model projection formula applies. Bounded decreasing MA
continuity supplies weak convergence on both spaces. Testing downstairs
against an arbitrary continuous h, its pullback is continuous upstairs,
and the exact model identities pass to the limit. This proves equality
of Radon measures and retains every original bounded input.

The corrected test-function remark makes no false assertion that every
continuous function is a difference of two psh functions. It invokes the
already proved weak convergence against all continuous tests. No new
assumption of metrizability, countability, curve dimension, rational
reference class or skeletal support is introduced.

## Assembly and gates

The read-only author validator was inspected before execution. It checks
the exact source replacements, byte-identical theorem statements, all474
old labels, the unchanged weighted Chapter26 fragment, the excluded
Chapter30 descent paragraph, referenced label owners, source hashes and
both patch routes; the combined patch check does not apply it. The root
check independently rehashes all16 author manifest entries and records the
validator result. The author syntax tests are syntax evidence only.

The two patch routes are alternatives: one includes the weighted Ch26
parent against live source, the other starts from that parent already
installed. They must not be cumulatively applied. No live mathematical
integration or production Rethlas call was made in this review.
