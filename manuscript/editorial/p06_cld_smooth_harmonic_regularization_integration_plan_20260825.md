# P06.3 integration plan after guarded production verification

Date: 25 August 2026 (Asia/Shanghai)

Status: executed after the P11 handoff and after a fresh exact-live production
gate.  The historical plan is retained below; the authoritative counts remain
18 formal problem environments and 59 active atoms.

## Controlling production object

- Run: `20260825T055907Z_b5c8f0719b60`.
- Item: `pi_d80993bb01a748f0422ae6a5`.
- Model / scrutiny: `gpt-5.6-sol` / `xhigh`.
- Verdict: `final/correct`; zero critical errors and zero gaps.
- Statement SHA-256:
  `b5c8f0719b606707b8055f0ead8c1baa96b5d9732cccf51a0e86ec02c5e64f24`.
- Proof SHA-256:
  `ba402983b6d88c03437c79af66dfd541c5a37b89c0bb2a6a67438ac84120565b`.
- Production receipt:
  `rethlas_receipts_20260825/p06_cld_smooth_harmonic_nonregularization_live_production_receipt_20260825.md`.

The source-aware round 1 was `final/wrong` because of one incorrect CLD
pinpoint citation and remains preserved.  The source-aware round-2 pass and a
premature local-lift exact-live pass are also historical rather than
controlling: the final live proof uses the global model function constructed
in the proof of GJR Proposition 17.4.

## Exact mathematical disposition

The verified proposition constructs a smooth proper genus-three Berkovich
curve, a type-2 point with residual elliptic curve, an open three-arm star,
and an integral PL harmonic function whose residual class is nonzero in
`Pic^0(E) tensor R`.  It proves that this function is not a locally uniform
limit, hence not a decreasing pointwise limit, of ordinary CLD-smooth
harmonic functions.

This disposes of only the literal phrase “CLD-smooth harmonic approximants.”
It does **not** disprove decreasing approximation by ordinary CLD-smooth psh
functions.  Positive curvature destroys the fixed-slope closure argument.
The psh problem from Wanner Remark 5.5 remains open.

## Planned live changes

1. `manuscript/parts/part2/ch19_cld_examples.tex`

   Insert an untitled proposition with a full proof immediately after the
   warning “Three statements that look alike” in the Wanner-scope subsection,
   before the Thuillier-current subsection.  Use no optional theorem name.
   Suggested internal label:
   `prop:ch19-cld-smooth-harmonic-nonregularization`.

   Preserve these equation labels, in proof order, so later references remain
   stable:

   - `eq:ch19-harmonic-reg-support`;
   - `eq:ch19-harmonic-reg-nonzero-class`;
   - `eq:ch19-harmonic-reg-open-star`;
   - `eq:ch19-harmonic-reg-fixed-support`;
   - `eq:ch19-harmonic-reg-picard-kernel`;
   - `eq:ch19-harmonic-reg-slope-values`;
   - `eq:ch19-harmonic-reg-divisor-limit`.

   Preserve every mathematical step of the production proof:

   - the GJR Section 17 theta-curve construction;
   - nonvanishing of `[z]-[x]` after tensoring;
   - the outer affinoid star and fixed inner compact star;
   - model-independence of Thuillier's `H(Y)` and fixed tangent support;
   - the finite-dimensional Picard-kernel closure;
   - endpoint recovery of slopes;
   - the net form of Dini's theorem;
   - the explicit psh firewall.

   Convert packet-only arXiv prose to the existing bibliography keys
   `CLD25`, `GJR26`, `Thu05`, and `Wanner19`.  Use `\Cref`/`\cref` for
   theorem references internal to the book and `\eqref` for the seven
   displayed internal equations.  Use `\dprimeddprime` or explicit
   `\mathrm d'\mathrm d''`; never plain italic `d`.  Give the proposition no
   conventional name and make no novelty or priority claim.

2. `manuscript/parts/part2/ch18_delta_forms.tex`

   Do not duplicate the proposition or its proof.  Immediately after the
   paragraph containing `eq:cld-weak-inclusion` and GJR Proposition 10.17,
   add one forward cross-reference with this exact mathematical content:

   > The inclusion is strict already for functions on smooth curves, and
   > monotone approximation by ordinary smooth harmonic functions does not
   > close the gap: `\Cref{prop:ch19-cld-smooth-harmonic-nonregularization}`
   > gives an integral PL weakly smooth harmonic function which is not even a
   > locally uniform limit of ordinary CLD-smooth harmonic functions.  The
   > statement does not concern ordinary CLD-smooth psh approximation.

   This is the only planned Chapter 18 change.

3. `manuscript/parts/part6/ch72_major_open_problems.tex`

   Keep the first two questions in `prob:frontier-pluriharmonic`.  Replace
   the third literal harmonic question by the genuine remaining question:
   decreasing regularization by ordinary CLD-smooth **psh** approximants.
   Use the following source-exact wording:

   > On the analytification of every smooth proper curve over an
   > algebraically closed complete nontrivially valued field, is every
   > continuous current-psh function---equivalently, by Wanner's comparison,
   > every continuous Thuillier-subharmonic function---locally a decreasing
   > limit of ordinary CLD-smooth psh functions, without the supplementary
   > residue-field or curve hypotheses of Wanner Corollary 5.4?

   Immediately after the problem, state that the formerly written
   harmonic-approximant version is false by the new Chapter 19 proposition.
   Do not say that the psh problem is solved.

4. `manuscript/editorial/open_problem_atomic_inventory_20260824.md`

   Retain P06.3 and its tier, but change its wording to
   `[T2; open after the literal harmonic variant]`: decide unrestricted
   decreasing ordinary CLD-smooth psh approximation.  Record the verified
   counterexample only as the boundary that forces this re-scoping.  Do not
   delete P06.3.

5. `RESEARCH_QUESTION_LEDGER.md` and
   `manuscript/editorial/major_open_problem_program.md`

   Record the literal harmonic version as disproved by the controlling run;
   retain the psh version as open.  Keep all aggregate open-problem counts
   unchanged.

6. `manuscript/editorial/rethlas_verified_results.md`,
   `manuscript/editorial/rethlas_open_problem_attempts.md`, and
   `manuscript/editorial/theorem_provenance.md`

   Add the exact run/item/digests and scope firewall.  Preserve the round-1
   rejection before the round-2 pass.  Do not characterize the result as an
   unrestricted smooth-regularization counterexample.

7. `manuscript/appendices/appL_provenance.tex`

   Add the Chapter 19 proposition with sources GJR Section 17, GJR
   Propositions 10.14, 10.17, 15.7, GJR Remark 15.10, Thuillier Lemma 2.3.22,
   Wanner Corollary 5.4 and Remark 5.5, and the controlling production
   receipt.  State the psh firewall in the provenance note.

8. Do not alter the authoritative totals of `18` formal problem environments
   and `59` active atoms, or any completed/open count.

## Planned checks after authorization

- Diff only the intended live files and verify that no P11 edits were
  overwritten.
- Search for accidental claims that all CLD-smooth regularization fails.
- Check every new internal theorem reference uses `\Cref`/`\cref`, every
  equation reference uses `\eqref`, and every differential uses the book's
  roman-d convention.
- Run label/reference/citation/static checks.
- Compile a focused Chapter 19/Chapter 72 slice, then the ordinary main
  compile target if the shared worktree is stable.
- Write a live-integration receipt binding the inserted proposition and
  ledgers to the production run while preserving the round-1 rejection.

No novelty or priority claim is intended.
