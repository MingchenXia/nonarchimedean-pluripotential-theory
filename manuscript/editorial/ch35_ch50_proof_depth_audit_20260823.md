# Chapters 35 and 50 proof-depth audit (2026-08-23)

## Scope

This audit covers only the critical endpoint in the homogeneous Siu
decomposition of Chapter 35 and the norm/measure completion theorem of
Chapter 50.

## Chapter 35

The strict case `sup_{K_E} psi<-1` is proved inside the chapter.  In the
critical case `sup_{K_E} psi=-1`, the text now reconstructs the approximation
used in BJ22, Theorem 6.21, and isolates its exact unresolved step.  If
`psi_a` decreases and `t_a -> 1`, the residuals
`psi_a-t_a log|s_E|` decrease only if

`t_b-t_a <= inf_{K_E}(psi_a-psi_b)` for `b>=a`.

The inequalities displayed in the published proof do not by themselves
imply this condition.  The chapter therefore imports the endpoint statement
as BJ22, Theorem 6.21, rather than presenting the source sketch as an
internal proof.  Boucksom--Jonsson, *Non-Archimedean Green's functions and
Zariski decompositions*, Proposition 17, is recorded only as a later
post-envelope confirmation under its smooth characteristic-zero standing
hypotheses; it is not used to prove the envelope theorem.

The previous claim that later chapters use only the strict case was removed:
the borderline examples and the later envelope argument genuinely use the
endpoint and hence inherit this imported boundary.

A separate solver dossier constructs a candidate counterexample to the
published monotonicity step and a conditional endpoint repair from an
independently known envelope property.  Those claims are not integrated into
Chapter 35: they are frozen in
`editorial/solver_dossiers_20260823/` and remain pending production Rethlas
review.

## Chapter 50

The text now defines the quotient pseudometric explicitly and Hausdorffizes
zero-distance classes.  It separates the imported analytic package from the
formal completion argument.  The imported inputs are:

- BJKS1, Theorem B and Theorems 5.5 and 5.11: the compatible strong metrics,
  density on the potential side, measure-side completeness, and the envelope
  property completeness criterion;
- BJ22, Theorems 10.12 and 10.14: the strong quasi-metric comparison and
  completeness estimates underlying that package;
- BJKS1, Theorem 3.18: canonical finite-type approximation of norms;
- BJKS1, Lemma 7.1: the dense test-norm Monge--Ampere isometry.

After these inputs, the chapter proves the extension formally: it sends an
approximating net to the limit of its Monge--Ampere measures, proves
choice-independence on the product directed set, passes the distance identity
to the limit, and proves uniqueness, density, and both completion statements.
For a general norm the measure is thus defined by metric/strong completion;
Calabi--Yau representation is a later consequence when the envelope property
holds, not the definition.

## Focused build

The two-chapter proof-depth driver compiles successfully to
`build_part4_proof_depth/part4_ch35_ch50_proof_depth.pdf`.  Its final log has
no fatal error, unresolved local citation or reference, duplicate label, or
overfull box.

## Dependency and novelty status

Neither audited passage cites or depends on the author's Deligne-pairing
paper.  The pairings occurring in these chapters are respectively coefficient
evaluation for b-divisors and the established energy/intersection pairing.

No new mathematical result is asserted in either chapter.  The Chapter 35
change is a source reconstruction and an explicit quarantine of a
foundational endpoint; the Chapter 50 change is the standard uniqueness
theorem for extending an isometry from a dense subspace into a complete
metric space.  No new receipt is claimed for these chapter edits.  Any later
promotion of the separate endpoint repair or proof-step counterexample does
require the pending Rethlas receipt.
