# Fail-closed hostile-audit obligations

Any failure in items 1--8 blocks production submission. Even if they all
pass, exact-byte production Rethlas verification is still required before
live integration.

1. **Source semantics.** Verify directly from CLD Remark 17.8.10,
   Corollary 17.8.9, and §17.8.5 that the second question is the extension
   of “parlinear implies globally dpsh.” Reject any argument that silently
   replaces it by “locally psh implies globally psh.”

2. **Formal-twistor scope.** Verify that the HMS formal twistor deformation
   is smooth and proper over `Spf(C[[t]])`, has the chosen projective K3
   surface as special fibre, and has a connected proper strict Raynaud
   generic fibre over the nontrivially valued field `C((t))`. Check that the
   “very general” hypothesis in HMS Proposition 2.10(i) is exactly the one
   imposed in the statement. For connectedness, audit the exact sequences
   on all infinitesimal thickenings, the uses of `H^0(O_S)=C` and
   `H^1(O_S)=0`, the inverse limit, and HMS Remark 2.2/Proposition 2.3.
   Reject the weaker shortcut “formal affine charts are domains.” Verify
   strictness, smoothness, and properness against Temkin §5.2.2 and Fact
   5.2.2.4, including the boundaryless step from rig-smooth to smooth.

3. **Analytic Picard bridge.** Check every step, without replacing it by a
   slogan:
   - CLD Theorem B.1.8(a) produces a coherent model of an arbitrary analytic
     line bundle on the *fixed* formal twistor model;
   - removing `t`-power torsion leaves the generic fibre unchanged;
   - `t`-torsion-free plus rank-one locally free generic fibre implies full
     module torsion-freeness over each formal local domain;
   - the formal local rings are regular by the exact flat-local criterion
     in Stacks tag `031E`, before using tag `0AG0`;
   - the double dual is coherent rank-one reflexive in the exact scope of
     Stacks tags `0AV3`, `0AVB`, and `0AVC`;
   - regular local UFDs make that double dual free of rank one, including in
     total dimension three;
   - localization of the double dual recovers the original analytic line
     bundle;
   - HMS Proposition 2.10(i) applies to this formal line bundle.

4. **Admissible blow-up.** Verify that
   `J=ker(O_mathfrakX -> (i_p)_* C)` is coherent and open, that its formal
   blow-up is admissible, and that `J[1/t]=O[1/t]` makes the generic-fibre
   morphism an isomorphism in the exact Raynaud/Temkin and Bosch scopes
   cited in the proof. Check that the tautological transform really is
   the invertible ideal `O(-E)` and hence defines a formal metric on the
   analytically trivial bundle. Independently audit that its special-fibre
   morphism is a relative `Proj`, hence projective over `S`, and that this
   metric-defining model itself has projective special fibre.

5. **Two-component calculation.** In the completed regular local ring at
   the centre, first audit the passage to that completion: Stacks tag `00MC`
   must make it faithfully flat, Stacks Lemma 31.33.3 (tag `01OF`) must
   identify the scheme blow-up after flat base change, and Bosch §8.2
   Proposition 6 must identify the formal blow-up with the adic completion
   of the scheme blow-up. Check that these facts really permit the charts,
   reduced components, and multiplicities to be computed in the completed
   ring. Then audit the blow-up of `(t,x,y)`. Verify
   the explicit `x`-chart `t=xT`, `y=xY`, `E=(x)`, and `S'=(T)`;
   `div(t)=S'+E`, both multiplicities one; and the global description
   `Bl_p(S) ∪ P^2` with intersection `P^1`. Check the existence of both
   corresponding divisorial points, the identity `1=x^{-1}x` in the
   `O(-E)` frame, and the signs in
   `||1(x_S')||=1` and `||1(x_E)||=|t|^{-1}`. Finally distinguish
   `log||1||=-log|t|` from the CLD weight
   `log||1||^{-1}=log|t|` at the exceptional point.

6. **Global-psh constancy.** Verify that each smooth psh approximating weight
   is CLD-psh, hence classically psh in the exact Gubler--Rabinoff scope.
   Check compactness, boundarylessness, and connectedness of `X`, and check
   the open-and-closed maximum-locus argument. Verify that uniform limits of
   the resulting constants remain constant.

7. **Global-dpsh constancy.** Verify that CLD's definition supplies an
   isometric decomposition by two globally psh metrized line bundles. Use
   `Pic(X)=0` to trivialize both factors, but retain the global analytic unit
   in the comparison isomorphism. Check the sign of its contribution to the
   weight and use Gubler--Rabinoff Proposition 7.2(2) plus the maximum
   principle to show that its absolute value is constant.

8. **Scope firewall.** The conclusion must be only a counterexample to the
   second CLD question. It must not claim a counterexample to the first
   continuous-psh/global-psh question, must not call the exceptional metric
   psh, and must not use the erroneous Deligne-pairing manuscript.

## Secondary obligations

9. Check that “constant metric on `O_X`” means that the norm of the canonical
   section `1` is constant; on this compact connected space changing a
   trivialization changes the weight only by a constant `log|f|`.

10. Check every bibliography locator against the versions in
    `PRIMARY_SOURCE_LOCATORS.md` and record any source-version drift.

11. Compile the exact statement and proof in a minimal harness and freeze
    their SHA-256 values before production verification.

12. No live-book paragraph, controlling inventory entry, atom count, or
    retirement ledger may change before an independent hostile audit and a
    dependency-closed production Rethlas verdict of `correct` with zero
    critical errors and zero gaps.
