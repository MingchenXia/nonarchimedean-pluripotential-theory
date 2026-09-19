# Dangling cross-reference targets in the built manuscript

Generated 14 September 2026 by a text scan of every file reachable from
`book.tex` (parts, appendices, frontmatter, style, including
`parts/part6/fragments/`).  A target is listed when it is used by
`\ref`/`\Cref`/`\cref`/`\eqref` in a built file but carries no `\label`
in any built file.  Definitions that exist only under `manuscript/editorial/`
do not count, because `book.tex` does not input that tree.

**149 distinct targets, referenced from 15 files.**

Caveat: the 13 September `book.log` records no undefined-reference warnings,
which is inconsistent with this scan.  Either that log is not from a build of
exactly this source, or some resolution mechanism was not found by the scan.
This list should be confirmed against a fresh build before acting on it.

## Count by referencing file

- `manuscript/parts/part6/ch72_major_open_problems.tex` — 109
- `manuscript/appendices/appL_provenance.tex` — 82
- `manuscript/parts/part2/ch18_delta_forms.tex` — 59
- `manuscript/parts/part2/ch16_bedford_taylor.tex` — 34
- `manuscript/parts/part6/ch70_local_valuative_psh.tex` — 9
- `manuscript/parts/part2/ch15_poincare_lelong.tex` — 8
- `manuscript/parts/part2/ch19_cld_examples.tex` — 7
- `manuscript/parts/part2/ch17_metrized_bundles.tex` — 6
- `manuscript/parts/part6/ch69_verified_extensions.tex` — 4
- `manuscript/frontmatter/part2_intro.tex` — 3
- `manuscript/parts/part2/ch14_currents.tex` — 2
- `manuscript/parts/part3/ch21_bfj_psh.tex` — 1
- `manuscript/parts/part1/ch08_examples.tex` — 1
- `manuscript/parts/part3/ch25_capacity.tex` — 1
- `manuscript/parts/part3/ch31_bfj_examples.tex` — 1

## Targets

`NEW` marks a target that is dangling now but was not at HEAD (i.e. it comes
from currently uncommitted work in Chapters 70--72).

- `cor:p021-invariant-toric-semipositive-rpl-regularization`  **NEW**
- `cor:p022-invariant-toric-lfs-regularization`  **NEW**
- `cor:p023-invariant-toric-weakly-smooth-regularization`  **NEW**
- `cor:p024-invariant-toric-cld-smooth-regularization`  **NEW**
- `cor:p031-local-fs-envelope-on-unibranch-curves`  **NEW**
- `cor:p033-invariant-toric-lfs-minorant-envelope`  **NEW**
- `cor:p033-invariant-toric-semipositive-real-pl-envelope`  **NEW**
- `cor:p061-algebraic-split-analytic-toric-forms`  **NEW**
- `cor:p061-algebraic-split-toric-forms`  **NEW**
- `cor:p061-analytic-standard-etale-algebraic-split-forms`  **NEW**
- `cor:p061-analytic-standard-etale-all-orbits`  **NEW**
- `cor:p061-analytic-standard-etale-toroidal-charts`  **NEW**
- `cor:p061-finite-curve-products-ph-rpl`  **NEW**
- `cor:p061-iterated-relative-weighted-cone-closure`  **NEW**
- `cor:p061-split-toric-quasismooth-products`  **NEW**
- `cor:p061-split-toric-varieties`  **NEW**
- `cor:p061-v3-zariski-etale-toric-charts`  **NEW**
- `cor:p061-zariski-etale-algebraic-split-toric-charts`  **NEW**
- `cor:p062-algebraic-split-invariant-scalar-stable-zero-current`  **NEW**
- `cor:p062-local-algebraic-split-invariant-scalar-stable-zero-current`  **NEW**
- `cor:p062-proper-full-rank-moment-automatic-calibration`  **NEW**
- `cor:p09-good-reduction-positive-cone-counterexample`  **NEW**
- `cor:p213-endpoint-mixed-tower-basis-bt`  **NEW**
- `cor:p213-endpoint-mixed-tower-bt`  **NEW**
- `cor:p213-endpoint-mixed-tower-cover-bt`  **NEW**
- `cor:p213-polycylinder-basis-v2-candidate`  **NEW**
- `cor:p213-residual-picard-mixed-tower-basis-bt`  **NEW**
- `cor:p213-residual-picard-mixed-tower-bt`  **NEW**
- `cor:p213-residual-picard-mixed-tower-cover-bt`  **NEW**
- `eq:ch16-curve-junction-jensen`  **NEW**
- `eq:p121-change-normalizing-ideal`  **NEW**
- `ex:p061-iterated-weighted-cone-no-common-grading`  **NEW**
- `ex:p061-nodal-cuspidal-products`  **NEW**
- `ex:p061-standard-etale-weighted-cone-nonhomogeneous`  **NEW**
- `ex:p121-node-cusp-normalized-links`  **NEW**
- `ex:p122-curve-psh-pullback-bottom`  **NEW**
- `ex:p122-cusp-radial-psh-classification`  **NEW**
- `ex:p126-curve-variable-degree-average`  **NEW**
- `itm:ch14-cld-support-corrected-nontrivial`  **NEW**
- `itm:ch14-cld-support-corrected-trivial`  **NEW**
- `itm:ch18-dm:delta`  **NEW**
- `lem:ch18-delta-metric-gluing`  **NEW**
- `lem:p061-nilpotent-rpl-invariance`  **NEW**
- `lem:p061-parameterized-rigid-point`  **NEW**
- `lem:p061-product-factor-reduction`  **NEW**
- `lem:p061-rational-section-tube`  **NEW**
- `lem:p061-v3-contractive-standard-etale-tube`  **NEW**
- `lem:p213-euclidean-one-dimensional-current-revised`  **NEW**
- `lem:p213-triv-interval-current`  **NEW**
- `lem:p213-trivial-gauss-rigid-zero-atom`  **NEW**
- `lem:p213-variation-graph-source-cutoff`  **NEW**
- `lem:p21p3-componentwise-normal-rigid-zero-atom`  **NEW**
- `lem:p21p3-gf-legal-source-localization`  **NEW**
- `lem:p21p3-gfc-rigid-zero-atom`  **NEW**
- `prop:ch14-cld-support-printed-exponent-counterexample`  **NEW**
- `prop:p031-modulus-controlled-envelope-candidate`  **NEW**
- `prop:p031-nodal-product-envelope-obstruction-candidate`  **NEW**
- `prop:p031-nonsplit-node-open-disc-envelope-obstruction`  **NEW**
- `prop:p033-invariant-toric-real-pl-envelope`  **NEW**
- `prop:p061-analytic-standard-etale-toric-product`  **NEW**
- `prop:p061-curve-product-normalization-descent`  **NEW**
- `prop:p061-finite-group-rpl-descent-candidate`  **NEW**
- `prop:p061-frobenius-rpl-descent`  **NEW**
- `prop:p061-integral-pl-counterexample`  **NEW**
- `prop:p061-parameterized-toric-fixed-fibre`  **NEW**
- `prop:p061-relative-positive-weighted-cone-descent`  **NEW**
- `prop:p061-v3-etale-toric-product`  **NEW**
- `prop:p061-v3-single-shilov-factorization`  **NEW**
- `prop:p062-annulus-endpoint-arbitrary-field`  **NEW**
- `prop:p062-arbitrary-field-annulus-v4-source-correct`  **NEW**
- `prop:p062-arbitrary-field-disc`  **NEW**
- `prop:p062-explicit-base-change`  **NEW**
- `prop:p062-finite-flat-continuous-trace`  **NEW**
- `prop:p062-invariant-split-toric-boundary-zero-current-candidate`  **NEW**
- `prop:p062-nonstrict-boundary-resonance-counterexample`  **NEW**
- `prop:p062-nonstrict-scalar-stable-repair`  **NEW**
- `prop:p062-projective-bundle-descent`  **NEW**
- `prop:p062-proper-full-rank-moment`  **NEW**
- `prop:p062-proper-smooth-curve-bundle-descent`  **NEW**
- `prop:p062-rational-centred-traces`  **NEW**
- `prop:p062-strict-product-fibre-slicing-v4-research`  **NEW**
- `prop:p082-formal-twistor-counterexample-candidate`  **NEW**
- `prop:p09-irrational-nef-ray-obstruction`  **NEW**
- `prop:p126-curve-conductor-principal-realization`  **NEW**
- `prop:p126-finite-reduced-curve-link`  **NEW**
- `prop:p213-componentwise-arbitrary-valuation`  **NEW**
- `prop:p213-fixed-polycylinder-v2-candidate`  **NEW**
- `prop:p213-hessian-regular-basis-v2-candidate`  **NEW**
- `prop:p213-normal-curve-arbitrary-valuation-current-revised`  **NEW**
- `prop:p213-residual-picard-smooth-curve`  **NEW**
- `prop:p213-triv-abstract-cross-counterexample`  **NEW**
- `prop:p213-triv-algebraic-curve-current-rigidity`  **NEW**
- `prop:p213-triv-four-puncture-no-go`  **NEW**
- `prop:p213-triv-p1-current-rigidity`  **NEW**
- `prop:p21p3-componentwise-rigid-exceptions`  **NEW**
- `prop:p21p3-curve-rigidity`  **NEW**
- `prop:p21p3-curve-rigidity-nonreduced`  **NEW**
- `prop:p21p3-delta-module`  **NEW**
- `prop:p21p3-gf-virtual-annulus-bridge`  **NEW**
- `prop:p21p3-gfc-smooth-rigidity`  **NEW**
- `prop:p21p3-rigid-exception-extension`  **NEW**
- `rem:ch14-cld-support-corrected-index`  **NEW**
- `rem:p213-componentwise-av-scope`  **NEW**
- `rem:p213-normal-rigid-zero-atom-scope`  **NEW**
- `rem:p21p3-componentwise-residual`  **NEW**
- `rem:p21p3-curve-scope`  **NEW**
- `rem:p21p3-nr-double-line`  **NEW**
- `rem:p21p3-nr-scope`  **NEW**
- `rem:p21p3-rigid-exception-scope`  **NEW**
- `thm:ch14-cld-support-corrected-packet`  **NEW**
- `thm:ch16-collapse-finite-tropical-curves`  **NEW**
- `thm:p031-perfected-unibranch-curve-envelope`  **NEW**
- `thm:p061-algebraic-etale-weighted-cone-towers`  **NEW**
- `thm:p061-algebraic-etale-weighted-cone-zero-section`  **NEW**
- `thm:p061-analytic-standard-etale-toroidal-ph-rpl`  **NEW**
- `thm:p061-arbitrary-curve-factors-ph-rpl`  **NEW**
- `thm:p061-curve-product-ph-rpl`  **NEW**
- `thm:p061-positive-weighted-cone-vertex-constancy`  **NEW**
- `thm:p061-quasismooth-ph-rpl`  **NEW**
- `thm:p061-simplicial-toric-ph-rpl`  **NEW**
- `thm:p061-split-toric-all-orbits`  **NEW**
- `thm:p061-standard-etale-weighted-cone-tube`  **NEW**
- `thm:p061-toric-fixed-point-constancy`  **NEW**
- `thm:p061-v3-etale-toroidal-ph-rpl`  **NEW**
- `thm:p062-arbitrary-field-polycylinder-v4-source-correct`  **NEW**
- `thm:p062-endpoint-polycylinder-v4-research`  **NEW**
- `thm:p062-polydisc-zero-current-candidate`  **NEW**
- `thm:p063-current-psh-ordinary-regularization`  **NEW**
- `thm:p071-cld-constant-collar-endpoint`  **NEW**
- `thm:p071-cld-infinite-collar-endpoint`  **NEW**
- `thm:p071-finite-star-euclidean-collapse`  **NEW**
- `thm:p071-finite-star-polyhedral-collapse`  **NEW**
- `thm:p071-infinite-star-collapse-candidate`  **NEW**
- `thm:p071-stone-finite-star-polyhedral-collapse`  **NEW**
- `thm:p071-stone-infinite-star-collapse`  **NEW**
- `thm:p081-corrected-curve-comparison`  **NEW**
- `thm:p081-irrational-tate-period-obstruction`  **NEW**
- `thm:p09-signed-semipositive-span`  **NEW**
- `thm:p09p2-product-gauss-candidate`  **NEW**
- `thm:p09p2-reduction`  **NEW**
- `thm:p121-reduced-nagata-curve-link`  **NEW**
- `thm:p122-conductorial-disc-radial-psh-classification`  **NEW**
- `thm:p122-curve-ideal-psh-functoriality`  **NEW**
- `thm:p122-curve-principal-ideal-envelope`  **NEW**
- `thm:p122-multinode-radial-psh-classification`  **NEW**
- `thm:p126-curve-finite-flat-norm-descent`  **NEW**
- `thm:p126-curve-generic-norm-trace-descent`  **NEW**
- `thm:p213-endpoint-mixed-tower-classification`  **NEW**
- `thm:p213-residual-picard-mixed-tower`  **NEW**
