# Full Kähler comparison by bounded truncation — candidate

This packet proves a conditional full-cone comparison. Its explicit new hypotheses are raw-transform upper semicontinuity and dominated divisorial approximation. Their separate candidates are named below. Neither hypothesis is replaced by ordinary density or by equality on a dense set.

Principal author: root. Date: 31 August 2026.

The proposed conclusion is an order isomorphism from the full DXZ space of a Kähler class on a connected compact Kähler manifold to the MP cone, literally given by the raw transform on every semivaluation. There is no projectivity, rational-class, or finite-energy restriction. Extended energies agree by the existing finite-energy comparison and injectivity.

This is not an extension of the unchanged relatively nef model cone to non-nef classes. It does not settle the entire pseudoeffective P14.3 signature or any general Monge–Ampère problem. No live chapter or inventory is changed. The conditional proof and both topological dependencies require independent and production review before any promotion.

## Separate new dependencies

- `p142_raw_transform_usc_research_20260831`: statement `488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949`, proof `bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21`. Independent audit PASS; production pending.
- `p143_dominated_divisorial_research_20260831`: statement `4ab292c9cfcc6c298968fca40819c09d560c12c96279947ddae46f4c22c5191f`, proof `bfd983aa2fa4580a9193bdd3f4fca78e7dd527d6ee1843f5ee647e4485180433`. Fresh independent audit in progress; production pending.

## Proof organization

1. The MP divisorial comparison theorem and dominated approximation give equality between an MP psh extension and the raw transform.
2. An abstract compactness argument proves decreasing closure of a model-defined cone without assuming minima preserve positivity.
3. A bounded DXZ truncation has actual zero levels at the lower parameter end; its volume is positive, so positive-volume recovery applies. The energy integral then has finite parameter support.
4. Bounded truncations on each side and the existing finite-energy correspondence give both directions of the full comparison. The endpoint at the zero valuation is checked using the ray slope, not assumed from nonzero divisorial formulas.

`main.tex` is standalone. Builds must use draft mode here; no PDF creation, book compilation or visual-quality claim is part of this packet. The production gate has not been retried or bypassed.
