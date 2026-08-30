# Independent exact-byte hostile-audit receipt

Date: 30 August 2026

Auditor task: `/root/p082_k3_hostile_pre_audit`

## Verdict

**PASS for the independent mathematical and source audit.**  The frozen
statement and proof contain no critical error, fatal flaw, or unclosed
mathematical bridge found by this audit.  No repair to their frozen bytes is
required.

This receipt is not a production Rethlas verdict and does not authorize live
integration.  Exact-byte production verification with `gpt-5.6-sol` at
`xhigh` must still return `correct` with zero critical errors and zero gaps
before any live-book paragraph, controlling inventory entry, atom count, or
retirement ledger is changed.

## Frozen-byte identity

The following SHA-256 values were checked both before and after the audit:

- statement:
  `1e9b7c31a70c55f407de07d76c67d6912e61e1673ef81c66c60789afd2202d2f`;
- proof:
  `78fab726abcdfb3086988150359568ccd8a9b29d63c3a94e0c513f14b9fc148c`;
- primary-source locators:
  `02078187bae43279712e523c694ef517884ea5a5bd75580ac0810e2cdf80902e`;
- source matrix:
  `bc8d0f36c3dc0211641dab08175e30186e7746d27418de17ab92a1e5e637428d`;
- hostile-audit obligations:
  `983214dd78ca4d3d46774483d1b92b4600c6ad2c6c0b0597af293a27236b1e21`;
- minimal compile harness:
  `b11879bf519bfb4245420ed1dedced13714472d21c88e2eb239bf4310bd4416b`.

## Primary-source versions checked

- CLD v2 PDF:
  `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`;
- HMS orientation PDF:
  `99d374cd4678e3a5dd75522fed90c6b8637b8ba080f47e710c2e243e1b62e2f0`;
- HMS formal-fibre PDF:
  `3e9beae6c911051535230fb560becfe321e76a5dce9a203aecb8efafe22a5868`;
- Gubler--Rabinoff v2 PDF:
  `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`;
- Temkin PDF:
  `b8a7ac414e98fdd46db3961c43e08068203aec7225457f455dc077f87b32b914`;
- Bosch PDF:
  `2f39e9e9bc71e34ce255278f09291412d7e0a9dadff673e4a2b8484df4685d7f`.

No source-version or locator drift was found.  In particular, CLD Theorem
B.1.8(a) begins on printed page 579 and its proof continues on page 580.

## Obligation-by-obligation findings

1. **PASS -- source semantics.**  Read literally with Corollary 17.8.9 and
   Section 17.8.5, the second paragraph of CLD Remark 17.8.10 asks whether
   every parlinear metrized line bundle is globally dpsh in the enlarged
   proper-strict/projective-special-fibre scope.  The candidate does not
   replace this by the first paragraph's continuous-psh/global-psh question.

2. **PASS -- formal-twistor scope and connectedness.**  The HMS construction
   supplies a smooth proper formal deformation over
   `Spf(C[[t]])`, with the prescribed projective K3 surface as special fibre,
   and the statement uses exactly the very-general condition of HMS
   Definition 2.8 and Proposition 2.10(i).  The infinitesimal exact sequences,
   `H^0(S,O_S)=C`, `H^1(S,O_S)=0`, and inverse limit give
   `Gamma(mathfrak X,O)=C[[t]]`.  HMS Remark 2.2 and Proposition 2.3 then give
   `Gamma(X,O_X)=C((t))`, so a nontrivial clopen decomposition is impossible.
   Temkin's strictness, properness, and rig-smoothness statements apply; the
   proper generic fibre is boundaryless, so rig-smoothness is smoothness.

3. **PASS -- analytic Picard bridge.**  CLD Theorem B.1.8(a) produces a
   coherent extension on the fixed formal model.  Removing parameter-power
   torsion preserves the generic fibre and makes multiplication by `t`
   injective.  In every formal local ring, flatness over `C[[t]]` and
   regularity of the closed fibre give regularity by Stacks tag `031E`, hence
   a domain and, by tag `0AG0`, a UFD.  The argument from parameter
   torsion-freeness and generic rank-one local freeness to full module
   torsion-freeness is valid.  Tags `0AV3`, `0AVB`, `0AVC`, and `0EBM` support
   the coherent rank-one reflexive double dual, and the local UFD property
   makes it free of rank one, including in total dimension three.
   Localization of finite duals recovers the original analytic line bundle.
   HMS Proposition 2.10(i) therefore gives `Pic(X)=0`.  The standard formal
   affinoid/coherent-module correspondence justifies the implicit passage
   from analytic local freeness to a projective rank-one generic module.

4. **PASS -- admissible blow-up and projectivity.**  The ideal
   `J=ker(O -> (i_p)_* C)` is coherent and open because it contains `t`.
   Its admissible formal blow-up has unchanged generic fibre since
   `J[1/t]=O[1/t]`.  The tautological transform is the invertible ideal
   `O(-E)`, whose inclusion supplies the stated generic-fibre trivialization
   and formal metric.  The special fibre is a relative Proj of a finitely
   generated graded algebra over the projective K3 surface, hence is itself
   projective.

5. **PASS -- completion, components, valuations, and signs.**  The proof
   cleanly distinguishes two completions.  Lines 195--198 call the first
   passage the maximal-ideal completion and use only its faithful flatness.
   Lines 199--201 explicitly identify the formal blow-up with the
   **`(t)`-adic completion** of the scheme blow-up.  Thus the phrase in line
   205 that adic completion does not alter reduction modulo `t` refers to
   this latter completion, not to the preceding maximal-ideal completion.
   The source matrix further says "the final adic completion."  The earlier
   requested "subsequent `(t)`-adic completion" distinction is therefore
   present in substance and unambiguous; no byte repair is needed.

   Faithful flatness and flat base change permit detection of the reduced
   components and their multiplicities after passing to
   `C[[t,x,y]]`.  On the `x`-chart, `t=xT`, `y=xY`, `E=(x)`, and `S'=(T)`, so
   `div(t)=S'+E`, both with multiplicity one.  Globally the special fibre is
   `Bl_p(S) union P^2`, with intersection `P^1`.  The two components define
   the two asserted divisorial points.  For the `O(-E)` frame `x`, the chosen
   generic-fibre trivialization gives `1=x^{-1}x`; hence
   `||1(x_E)||=|x(x_E)|^{-1}=|t|^{-1}`, while
   `||1(x_{S'})||=1`.  The logarithmic norm and CLD-weight signs in the proof
   are consequently correct.

6. **PASS -- global-psh constancy.**  Each smooth CLD-psh approximating
   weight is classically psh in the Gubler--Rabinoff scope.  Compactness gives
   a maximum, boundarylessness permits the local maximum principle at every
   point of the maximum locus, and connectedness makes that open-and-closed
   locus all of `X`.  Uniform limits of the resulting constants are constant.

7. **PASS -- global-dpsh constancy.**  CLD's definition supplies the stated
   isometric quotient of two globally psh metrized line bundles.  After
   applying `Pic(X)=0`, both factors have constant weights, but the proof
   correctly retains the global analytic unit in the comparison
   isomorphism.  If `1` maps to `f s_1 tensor s_2^{-1}`, then the weight is
   exactly `u=u_1-u_2-log|f|`.  Gubler--Rabinoff Proposition 7.2(2) and the
   maximum principle make `log|f|` constant.  The earlier identity
   `Gamma(X,O_X)=K` independently gives the same conclusion.

8. **PASS -- scope firewall.**  The conclusion concerns only the second
   paragraph of CLD Remark 17.8.10.  The exceptional metric is not called
   psh, the first paragraph is not answered, and the erroneous
   Deligne-pairing manuscript is not used.

9. **PASS -- meaning of constant metric.**  Constancy is measured using the
   canonical section `1` of `O_X`.  A change of global trivialization changes
   the weight by `log|f|`, which is constant here.

10. **PASS -- references.**  Every load-bearing locator was checked against
    the versions fingerprinted above.  No locator drift was found.

11. **PASS -- exact compile and freeze.**  The exact harness compiled
    independently with `latexmk -pdf -interaction=nonstopmode
    -halt-on-error` in three PDFLaTeX passes.  The result has seven pages and
    251951 bytes.  The final log contains no error, warning, undefined
    reference, overfull box, or underfull box.  The independently generated
    PDF has SHA-256
    `cad04d40fd913764a7b18506cb2e1ee6746165b8fe72dd5d69d5fdbe412867c8`.
    Its difference from the stored PDF hash is attributable to PDF metadata;
    the page count and byte size agree and all frozen source hashes remained
    unchanged.

12. **PASS for the audit-side quarantine; production gate remains open.**
    This audit made no change to the frozen statement, proof, source locators,
    source matrix, live book, controlling inventory, atom count, or retirement
    ledger.  Only this receipt was added.  Production Rethlas verification is
    still mandatory and fail-closed.

## Required action

There is no required mathematical or textual repair to the frozen statement
or proof.  The sole remaining action is exact-byte production Rethlas
verification of the hashes recorded above.  Any verdict other than `correct`
with zero critical errors and zero gaps blocks integration.
