# Exact-current Rethlas intake: Chapter 49 truncation-energy lemma

**Prepared:** 2026-08-24 (Asia/Shanghai)  
**Live target:** `manuscript/parts/part4/ch49_linear_growth.tex`,
`lem:ch49-truncation-energy` and the adjacent
`rem:ch49-truncation-sharp`  
**Status:** PRODUCTION VERIFIED AFTER REPAIR; run
`20260824T041218Z_0c95825dbb06`, item
`pi_8189ce12c89257c9acec4eef`, returned final verdict `correct`, with zero
critical errors and zero gaps; see the exact receipt  
**Classification:** book-local sharp consequence of the imported
Boucksom--Jonsson normalized mixed-energy and mixed Monge--Ampere package,
with explicit internal sharpness computations; not a verbatim published
theorem  
**Forbidden dependency:** arXiv:1710.09731 and every argument traceable
through it are excluded.

## Submission payload

Use the exact bytes of `ch49_truncation_energy_target_statement.txt` as the
Rethlas `statement` field.  Use the exact bytes of
`ch49_truncation_energy_statement_proof_sharpness_exact.tex` as the `proof`
field.  The shorter exact extracts permit independent statement/proof/remark
hash checks.  Do not normalize whitespace, expand macros, add line numbers,
or substitute this explanatory Markdown file for the exact combined payload.

The exact environment boundaries are:

- lemma statement: complete `lemma` environment at live chapter lines
  968--992, label `lem:ch49-truncation-energy`;
- proof: immediately adjacent complete `proof` environment at lines 994--1099;
- sharpness: immediately adjacent complete `remark` environment at lines
  1101--1219, label `rem:ch49-truncation-sharp`;
- lemma plus proof: contiguous lines 968--1099;
- full verification payload: contiguous lines 968--1219.

Line numbers are navigation aids.  Labels, byte identity, and SHA-256 values
in the manifest are controlling.

## Natural framework and normalization

- `k` is algebraically closed and trivially valued.
- `X` is an integral, unibranch, projective `k`-variety of dimension `n>=1`.
- `L` is ample, `omega=c_1(L)`, and `V=(omega^n)>0`.
- The Monge--Ampere operator is probability normalized:
  `MA_omega(phi)=V^{-1}(omega+dd^c phi)^n`.
- `E_omega(0)=0` and `E_omega(phi+t)=E_omega(phi)+t`.
- Every `omega`-psh function has supremum equal to its value at the trivial
  valuation.

## Exact dependencies exposed in the proof

The repaired payload no longer asks the verifier to infer the content of a
bare cross-reference.  It records the following inputs in the proof itself.

1. **Energy calculus, exact form.**  Equation `(49.6a)` states
   `E_omega(t)=t`, `E_omega(eta+t)=E_omega(eta)+t`, and monotonicity.
   The sandwich `c-a<=psi<=c` therefore proves finite energy directly.
2. **Fixed-class regularization, exact form used.**  The proof states that an
   `omega`-psh function admits a decreasing Fubini--Study net in the fixed
   ample class and then proves the maximum principle from the weighted-section
   formula.
3. **Pairing continuity and mixed-measure duality.**  Coordinatewise
   decreasing continuity of the extended pairing is stated explicitly.
   Equation `(49.6b)` gives positivity, mass one, and the exact normalized
   duality formula
   `integral f d nu_j=V^{-1}(0,f)(omega,eta)^j(omega,0)^(n-j)`.
4. **Mixed-energy formula derived, not assumed.**  Equation `(49.6c)` is the
   PL telescoping identity.  Each summand is rewritten as a difference of two
   finite psh pairings before passing to the decreasing limit; division by
   `V` and `(49.6b)` then gives `(49.6d)`.
5. **Trivial reference measure computed.**  The proof identifies the sole
   reduced central-fibre component of the trivial test configuration, its
   point `v_triv`, and its coefficient `V`; hence `mu_0=delta_(v_triv)`.
6. **Toric energy input, exact form.**  The remark displays
   `E_omega(eta)=-V_P^{-1} integral_(-P) f_eta^vee dm`, computes
   `f_psi^vee=1+m_1`, and integrates it using the barycenter of the standard
   simplex.
7. **Surface checks computed in place.**  The maximal-ideal and smooth-conic
   assertions now include the model classes, all nonzero intersection numbers,
   the cubics, the positivity ranges, and the endpoint energies.

The permitted route to the mixed-energy identity is thus the Chapter 46 PL
intersection/polarization identity and its decreasing-pairing extension.
The excluded Deligne-pairing paper plays no role.

## Failed-check diagnosis and repair

The superseded payload with proof digest
`188eccbbd1752ef86ba9528e41d06bf9a626c5416e771b56e5faf6fa4679f7b9`
was checked in production and returned `wrong` with no critical error but
eight missing-context gaps; a copy of the diagnostic, normalized only by a
terminal newline, is archived as
`ch49_truncation_energy_failed_gate_20260824.json`.  Every listed gap was a missing
dependency statement or omitted calculation.  The current payload repairs
all eight: finite energy is derived by monotonicity; the mixed identity is
passed from PL level explicitly; mass and the trivial Dirac measure are
spelled out; and all three sharpness computations are now local.  The repaired
bytes subsequently passed the production gate identified above.

## Proof audit map

1. Monotonicity between the two constant functions proves
   `c-a<=E_omega(psi)<=c`, in particular finite energy.
2. Fixed-class regularization proves `sup psi=psi(v_triv)` and the PL
   telescoping identity passes to bounded `psi` through finite pairing
   differences, yielding the normalized mixed-energy identity.
3. The trivial test-configuration calculation makes the `j=0` term exactly
   `c`.  Subtract `(n+1)c`; probability mass one changes each remaining integral
   to `integral(psi-c) d mu_j`, giving the displayed exact refinement.
4. Since `-a<=psi-c<=0`, every one of the `n` remaining integrals lies in
   `[-a,0]`.  Division by `n+1` proves both bounds.  Taking the actual
   oscillation and translating to supremum zero gives the stated corollaries.
5. Constants give equality in the upper bound.  On projective `n`-space,
   weight comparison gives `-1<=psi<=0`; the conjugate is `1+m_1` on `-P`,
   whose normalized integral is `n/(n+1)`, proving lower sharpness.
6. On the point blowup of `P^2`, `(H-E)^3=-1`, hence energy `-1/3`.  On the
   conic deformation, `(H-cE)^3=-6c^2+4c^3`; at `c=1/2` the energy is
   `-1/3=-(2/3)(1/2)`, giving the non-toric equality case.

## Scope firewall

- The lemma concerns bounded potentials only; it makes no unbounded
  finite-energy approximation claim.
- Probability normalization is essential.  In unnormalized conventions the
  displayed formula and constants must be rescaled by `V`.
- The centering at the actual supremum is essential.  No lower bound of the
  displayed form is claimed for an uncentered interval.
- The toric example proves optimality of the coefficient, not uniqueness or
  classification of equality cases.

## Mathematical extraction audit

The algebra of the lemma is exact: after the trivial Dirac term is removed,
there are exactly `n`, not `n+1`, integrals, which explains the coefficient
`n/(n+1)`.  The toric conjugate and both surface intersection cubics have
been recomputed against their source examples.  A focused 59-page LaTeX
slice compiled successfully after the repair.  The current mathematical
audit finds no remaining local gap.  Production verification returned final
verdict `correct`; the controlling receipt is
`../rethlas_receipts_20260824/ch49_truncation_energy_receipt.md`.

## Answered production-verification question

Does the exact proof establish the refined identity and optimal two-sided
estimate under the stated probability normalization, and do the three
sharpness/cross-check examples support every assertion in the adjacent
remark without using the forbidden source?

Production Rethlas answered this question `correct` for target SHA-256
`0c95825d...f378e7` and full proof-object SHA-256
`312ac465...6c99a2`.  The exact request object was not retained and is not
reconstructed; the exact target, proof object, run metadata, and raw response
are retained.
