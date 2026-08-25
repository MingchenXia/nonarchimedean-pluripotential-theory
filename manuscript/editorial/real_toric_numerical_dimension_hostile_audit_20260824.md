# Real toric numerical dimension: hostile audit

Date: 24 August 2026.

## Verdict

**PASS (mathematical statement and current repaired proof packet).**

**HOLD (production status only).** The first exact-current gate rejected the
old proof solely because it conflated the multiplier-ideal conventions.  The
current proof repairs that point at lines 77--94, but the repaired digest does
not yet have a final production receipt.  This is not a mathematical gap; it
is a release-protocol item.

Audited files:

- `manuscript/editorial/rethlas_packets_20260824/real_toric_numerical_dimension_statement_exact.tex`
  (SHA-256 `1d4f8f942fe141bec18cca5a19ad51ce6266d13639b1b8dac955e68c9b02ef5d`);
- `manuscript/editorial/rethlas_packets_20260824/real_toric_numerical_dimension_source_aware_proof_exact.tex`
  (SHA-256 `1c5e17c07cf9a1419e3aef488f7231e0fae274dfb0e69912813ba58ae80b2b70`);
- `manuscript/editorial/solver_dossiers_20260824/real_toric_numerical_dimension_solution_candidate.md`
  (SHA-256 `ca2b19717dc6fab7c1bb41984a5e5ae6afc524d56ef3ff5d139707e49c07172c`).

## Load-bearing checks

1. **Cao for arbitrary real currents.** Cao Definition 3 is stated for
   arbitrary closed positive `(1,1)`-currents on a compact Kahler manifold;
   integrality enters only Definition 4 and the later section-growth result.
   The current proof correctly converts conventions via
   `I_C(a phi)=I_B(2a phi)` and uses `lambda=2m`,
   `lambda'=2m(1+delta)`.  This exactly repairs the failed round-one gate.

2. **Polynomiality after smooth addition.** One fixed gentle
   quasi-equisingular approximation is used for both `T` and `T+s omega`.
   The identity for absolutely continuous parts and the finite binomial
   expansion commute with Cao's defining limits.  No continuity in a varying
   cohomology class is assumed.

3. **Cao top mass equals non-pluripolar top mass.** For `s>0`, `T+s omega`
   is a Kahler current and its toric potential is I-good.  The supplied book
   explicitly gives convergence of any quasi-equisingular approximation in
   this situation (Theorem 7.1.1) and mixed non-pluripolar mass continuity
   (Theorem 6.2.1).  Gentleness supplies on a modification
   `pi^*(R_j+s omega)=[E_j]+beta_{j,s}` with `beta_{j,s}` smooth; positivity
   off the divisor and continuity make it semipositive, and both relevant
   masses equal `int beta_{j,s}^n`.

4. **Arbitrary-real-class toric mass formula.** The proof does not enlarge a
   global ample-class theorem.  It uses the published local complex/real
   Monge--Ampere formula on the dense torus, local boundedness of the finite
   convex weight, and the fact that the non-pluripolar measure does not charge
   the toric boundary.  This yields
   `int <(T+s omega)^n>_np = n! vol(K+sQ)` for every `s>0`, independently of
   integrality or bigness of the original class.

5. **Closures and Minkowski addition.** The proof consistently uses
   `K=closure(dom F^*)`.  Its recession-function argument proves
   `closure(dom(F+sG)^*)=K+sQ` without relying on the overstrong/unjustified
   unclosed-domain assertions in Proposition A.2.2 and Lemma A.3.1 of the
   supplied 18 July 2026 PDF.  The test `F(x)=log(1+e^x)` directly disproves
   Proposition A.2.2's final equality by exposing the missing endpoints.

6. **Mixed-volume positivity.** If `d=dim K`, repeated copies of `K` give
   zero mixed volume for `k>d`.  For `k<=d`, choose `k` independent segments
   in copies of `K` and complementary small segments in the interior of `Q`;
   their determinant is nonzero, so monotonicity gives strict positivity.

7. **Current versus class.** The conclusion is only for the current-level
   Cao and non-pluripolar product classes.  The class-level interpretation is
   false: on `P^1`, `T=lambda[0]` has point Newton body and current-level
   numerical dimension zero, while its positive class has numerical
   dimension one.  The `P^1 x P^1` segment example similarly separates a
   current-level dimension one from a big class of dimension two.

## Exact cleanup before integration

- Add the explicit empty-product convention
  `\langle T^0\rangle=1` for both products.  This removes the only definitional
  ambiguity at `k=0`, especially for `T=0`; it does not alter the proof.
- Update the solver dossier's verification block: round one was run and
  failed on the factor-of-two convention, the repair is now present, and a
  final receipt for the repaired digest is pending.  Do not describe the
  repaired packet as production-verified until that receipt exists.
- Retain the dossier's firewall around the supplied PDF's overstrong
  unclosed convex-domain statements.  No live integration should replace
  the closed Newton body by an unclosed gradient image.

No counterexample was found to the repaired current-level theorem.  No live
chapter was edited in this audit.
