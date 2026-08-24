# Exact-current Rethlas intake: Chapter 23 fixed-skeleton selection

**Prepared:** 2026-08-24 (Asia/Shanghai)  
**Live target:** `manuscript/parts/part3/ch23_bfj_envelopes.tex`,
`prop:ch23-fixed-skeleton-selection`  
**Status:** PRODUCTION VERIFIED; run `20260824T044830Z_25024c43d265`, item
`pi_4cc2365c9c77af25df553e8e`, returned final verdict `correct`, with zero
critical errors and zero gaps; see the exact receipt  
**Classification:** book-local finite-maximum selection consequence of
imported BFJ skeletal regularity and standard compactness, not a published
BFJ theorem  
**Forbidden dependency:** arXiv:1710.09731 and every argument traceable
through it are excluded.

## Submission payload

Use the exact bytes of
`ch23_fixed_skeleton_selection_target_statement.txt` as the Rethlas
`statement` field.  Use the exact bytes of
`ch23_fixed_skeleton_selection_statement_proof_exact.tex` as the `proof`
field.  The separate statement and proof extracts exist to permit independent
hash checks.  Do not normalize whitespace, expand macros, add line numbers, or
replace the combined extract by this explanatory Markdown file.

The exact environment boundaries are:

- statement: the complete `proposition` environment at live chapter lines
  1228--1237, label `prop:ch23-fixed-skeleton-selection`;
- proof: the immediately adjacent complete `proof` environment at lines
  1239--1365;
- combined payload: the contiguous live slice at lines 1228--1365, including
  the single blank line between the two environments.

Line numbers are navigation aids.  Labels, byte identity, and SHA-256 values
in the manifest are controlling.

## Natural framework

- `K` is complete and discretely valued, with residue characteristic zero;
  `X` is smooth, connected, projective, and of dimension `n` over `K`.
- `theta` is a closed model `(1,1)`-form with ample generic class.
- `Delta=Delta_Xcal` is the finite dual complex of one SNC model `Xcal` on
  which `theta` is determined.
- Every `theta`-psh function is real-valued and continuous on `Delta`.
- The assertion is made only on this fixed `Delta`.  No countable cofinal
  model system and no global sequential selection are assumed.

## Authenticated inputs restated exactly in the proof

1. **Skeletal finiteness.**  Chapter 21,
   `thm:bfj-skeletal-characterization`(1): for every `theta`-psh function and
   every determining SNC model, its restriction to that model's dual
   complex is finite, real-valued, and continuous.  This full specialization
   is repeated in Step 1 of the submitted proof.
2. **Uniform facewise modulus.**  Chapter 22,
   `thm:bfj-skeletal-equicontinuity`(1): after compatible norms have been
   fixed on the faces of the determining dual complex, there is one constant
   `L=L(Xcal,theta)`, independent of the `theta`-psh function, bounding its
   Lipschitz constant on every face.  The exact quantified inequality is
   displayed in Step 1.
3. **Finite connected complex.**  Chapter 5,
   `lem:dual-complex-simplicial`: the dual complex of the fixed SNC model is
   a connected finite simplicial complex.

Everything after these three authenticated geometric inputs is proved
inside the submitted proof.  In particular, the proof independently
constructs the compatible piecewise path metric, proves that it is a metric
inducing the simplicial topology, derives the global modulus, proves the
finite-maximum modulus by an elementary inequality, and proves the required
sequential Dini statement from compactness.  It no longer invokes psh
stability of finite maxima, since that assertion is not needed by the
proposition.

These inputs are context axioms for the intake.  The verifier should audit
whether the proof uses them correctly; it should not attempt to reprove the
entire BFJ theory.

## Proof audit map

1. State the two BFJ inputs in their exact fixed-model form and the precise
   finite-connected-complex conclusion used for `Delta`.
2. Choose compatible face norms and define the path length as an infimum over
   facewise segment chains.  A geometric realization and uniform norm
   equivalence give both nondegeneracy and equality of the path-metric and
   simplicial topologies.  Summing the facewise estimate then gives a global
   modulus.
3. Choose one member of the nonempty family to bound the supremum from below,
   and use the assumed common upper bound to bound it from above.  The
   supremum inherits the same two-sided modulus and is continuous.
4. Choose a countable dense set in `Delta`.  For every dense point and every
   positive reciprocal tolerance, select a member of the family whose value
   is within that tolerance of the pointwise supremum.
5. Take successive finite maxima of the selected functions.  The sequence is
   increasing, lies below `u`, and has the same common modulus.  Its pointwise
   limit is therefore continuous and agrees with `u` on the dense set, hence
   everywhere.
6. Prove sequential Dini directly: the nested open sets
   `{u_j>u-epsilon}` cover the compact complex, so one of them already covers
   it, giving uniform convergence.

No regularization of the supremum is used: the common modulus proves that the
raw supremum is already continuous.

## Scope firewall

- The sequence depends on the fixed `Delta`, its path metric, its dense set,
  and the selections at the dense points.
- The claim does not select a sequence uniform on all dual complexes.
- It does not assert a countably cofinal system of models.
- It does not replace the global net-valued envelope theorem or suppress its
  upper-semicontinuous regularization.

## Formal repairs applied after the failed predecessor

The predecessor payload was rejected because five exact dependencies were
not available to the verifier.  The repaired proof now:

1. repeats the exact skeletal-finiteness and common facewise-Lipschitz inputs;
2. defines the path metric instead of referring to a step of another proof;
3. proves that metric induces the simplicial topology and derives the global
   modulus using the same compatible face norms;
4. removes the unnecessary assertion that finite maxima are psh and proves
   only their elementary common-modulus property; and
5. proves the sequential Dini conclusion inline.

The earlier enumeration repair is retained: the proof enumerates the index
set, not the possibly finite image of the double-indexed family.  Thus every
selected pair occurs at a finite index while repeated functions cause no
problem.

## Answered production-verification question

Does the repaired exact adjacent proof establish the fixed-dual-complex
statement from the three explicitly restated geometric inputs, with the
metric, global modulus, finite-maximum estimate, dense-set selection, and
sequential Dini argument all closed inside the payload and with no hidden
global sequential claim?

Production Rethlas answered this question `correct` for the exact target
SHA-256 `25024c43...3595e8` and proof SHA-256
`d91003dd...51d7786`.  The current live chapter differs from the submission
snapshot only in a later provenance paragraph; the exact theorem and proof
slice still compares byte for byte with the verified payload.
