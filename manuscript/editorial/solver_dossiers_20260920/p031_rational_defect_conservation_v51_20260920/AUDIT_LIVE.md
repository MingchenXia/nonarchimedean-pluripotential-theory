# P03.1 rational globalization-defect conservation: live audit

Audit date: 2026-09-20.

## Scope and baseline

- Live integration baseline: `d31ab621e4ce77bbfbc784c865d658c9f7d7e713`.
- Live files: `STATEMENT_LIVE.tex` and `PROOF_LIVE.tex`.
- Integration sites: Chapter 15, Chapter 72, and the atomic open-problem
  inventory.
- The packet is a standalone formal consequence of the already integrated
  v47 local PL--LFS defect split and v50 rational finite-flat pullback
  theorem.
- No model-backed verifier was used for this packet.

## Mathematical ledger

1. A global rational LFS minorant is simultaneously a global LFS and
   semipositive real-PL minorant. It makes every local and global envelope in
   the packet finite.
2. The global rational-coefficient gap
   `A = s_LFS - s_Q` and rational globalization defect
   `Delta_Q = P_Q^loc - s_Q` are therefore finite and nonnegative.
3. On a boundaryless space, v50 identifies the local rational and local LFS
   envelopes, while v47 identifies the local LFS and local PL envelopes.
   Subtracting the three global envelopes from their common local value gives
   the exact ledger
   `Delta_Q = Delta_LFS + A = Delta_PL + A + B`.
4. For a finite flat surjection, v50 gives both exact local rational pullback
   in the presence of the pulled-back global baseline and exact global
   rational-envelope pullback. Their difference proves conservation of the
   rational globalization defect.
5. Rewriting the LFS and PL envelopes as `s_Q + A` and `s_Q + A + B`
   converts exact rational pullback into the two gain identities. Pullback of
   global LFS or PL competitors supplies the required nonnegative signs.
6. The gain identities show that LFS compatibility is equivalent to
   preservation of `A`, while full P03 compatibility is equivalent to
   preservation of the total gap `A + B`.
7. If the base rational defect vanishes, the nonnegative summands in the
   three-level ledger vanish at the base. Conservation gives the same zero
   rational defect on every cover point, so all defects and both gaps vanish
   on the complete fiber.
8. In the finite-orbit range, the established identification of the PL gain
   with the symmetry-breaking defect `Sigma` turns the PL two-gap balance
   into the stated orbit decomposition.

## Hostile checks

- Every subtraction is between finite real numbers; no `infinity - infinity`
  expression is used.
- The local pullback theorem is invoked only after the global rational
  minorant supplies an LFS baseline near the complete fiber.
- The proof does not assume local-to-global rational cofinality; it isolates
  its failure as `Delta_Q`.
- The proof does not infer separate monotonicity of the branch gap `B`; only
  the total PL gain `A + B` is asserted to be nonnegative.
- No analytic section, finite-orbit presentation, or scalar-extension
  presentation is used in the main finite-flat conservation theorem.
- The orbit corollary is explicitly restricted to finite analytic orbit
  presentations.
- The packet imports neither the quarantined v38 collar formulas nor the v49
  repair thresholds.

## Verdict

PASS. The packet gives an exact conservation law and two sharp compatibility
criteria for the finite-flat range. It does not prove vanishing of the base
rational globalization defect and does not construct a finite-flat
presentation for arbitrary scalar extension. Accordingly, no P03 atom is
retired.
