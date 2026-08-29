# Exact-source audit: the trivially valued rigid-point Gauss transfer

Date: 29 August 2026

## Verdict

**PASS** for the quarantine statement and proof frozen below: zero mass at
a rigid interior point on a normal strict analytic curve over a complete
trivially valued field follows from scalar extension to `K((varpi))`, the
CLD Shilov-support and pushforward identities, and the already verified
nontrivially valued normal rigid-point estimate.

The argument remains valid for imperfect `K` and for a finite inseparable
extension `H(y)/K`.  It does **not** use the exponent printed in CLD
Corollary 16.8.6.  That exponent is an index error; a direct appeal to the
printed corollary for singleton zero mass is rejected.

Audit counts for the frozen transfer packet:

- critical mathematical errors: **0**;
- proof gaps: **0**;
- source-scope mismatches: **0**;
- unresolved inseparability assumptions: **0**.

This is a source/hostile audit, not a production Rethlas receipt.  The new
bytes remain quarantined until the dependency-closed packet receives the
required production verdict.

## Frozen source

The exact CLD source inspected was:

- `sources/CLD25.pdf`, SHA-256
  `f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`;
- its extracted text `sources/CLD25.txt`, SHA-256
  `24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727`.

These files are in
`p213_trivially_valued_curve_candidate_audit_20260829/sources/`.  The PDF
metadata identifies Chambert-Loir--Ducros, arXiv:1204.6277v2, 25 July
2025, 608 pages.

The scalar-extension assertions were also checked against Ducros's primary
source, *Les espaces de Berkovich sont excellents*, Ann. Inst. Fourier 59
(2009), author PDF
`https://webusers.imj-prg.fr/~antoine.ducros/Excellents.pdf` (111 pages):
Definition 1.6 defines analytic separability; Example 1.7 says a `K`-free
polyradius extension is analytically separable; Example 1.9 says the Gauss
Shilov residue field is universally multiplicative; Theorem 3.1(b,c),
printed p. 50, gives ascent of `S_m` and of `R_m` under analytically
separable scalar extension; and Section 3.4 identifies normality with
`R_1+S_2`.  The relevant local-ring map with geometrically regular fibres
is also recorded in Ducros, *Families of Berkovich spaces*, Ast\'erisque
400 (2018), Theorem 2.6.5; the official publication record is
`https://smf.emath.fr/publications/familles-despaces-de-berkovich`.

## Frozen candidate and dependency

- statement:
  `p213_trivial_gauss_rigid_zero_atom_statement_20260829.tex`, SHA-256
  `ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a`;
- proof:
  `p213_trivial_gauss_rigid_zero_atom_proof_20260829.tex`, SHA-256
  `789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66`;
- compile harness:
  `p213_trivial_gauss_rigid_zero_atom_compile_20260829.tex`, SHA-256
  `60212145c344530a5a74829bbfe869d4776ab611d8e4ad3645a3727cec8de53b`;
- clean two-page compile:
  `p213_trivial_gauss_rigid_zero_atom_compile_20260829.pdf`, SHA-256
  `d03d48f3e764c5020720bb48610c161bef2ba352366ec8bf49e97dd48732c5fd`.

The sole new mathematical dependency is the already production-verified
nontrivially valued result
`lem:p21p3-componentwise-normal-rigid-zero-atom`:

- statement SHA-256
  `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`;
- proof SHA-256
  `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`;
- production item `pi_0d4235a44db2b33950f8dd55`, final
  `correct`, zero critical errors and zero gaps, as recorded in
  `p213_normal_rigid_zero_atom_rethlas_receipt_20260829.md`.

## Source ledger

Line numbers below refer to the frozen extracted text; printed page
numbers refer to the CLD PDF.

| Claim used | Exact CLD support |
|---|---|
| The one-radius Gauss algebra is a complete field when the radius is `K`-free | Example 11.1.3, printed p. 299, text lines 14925--14936.  For a trivially valued field and `0<r<1`, the class of `r` has infinite order, hence the one-term polyradius is `K`-free. |
| `K_r/K` is analytically separable, without assuming `K` perfect | Section 11.1.9, printed p. 301, text lines 15043--15050: every finite `K`-free polyradius extension is analytically separable.  This is the consequence of Ducros, *Les espaces de Berkovich sont excellents*, Definition 1.6, and *Families of Berkovich spaces*, Theorem 2.6.5. |
| Normality survives this scalar extension | Section 11.3.1, printed p. 309, text lines 15444--15481: normality is `R_1+S_2`; `S_n` is preserved under scalar extension, and `R_n` ascends for an analytically separable extension. |
| Pure dimension one survives arbitrary scalar extension | Section 11.2.5, printed p. 308, text lines 15402--15406: every scalar-extended irreducible component has the same dimension as, and surjects onto, a base component. |
| Interior/boundaryless status survives | Section 11.4.1, printed pp. 310--311, formula (11.4.1.3) and text lines 15517--15528: open subspaces of the interior are boundaryless and boundarylessness is stable under analytic base change. |
| The required continuous Shilov section exists for the Gauss extension | Section 12.1.10, printed p. 333, text lines 16693--16702; more directly Section 12.7.4, printed p. 355, text lines 17955--17967: `H(eta_r)` is universally multiplicative and its maximal tensor-norm point defines a continuous section. |
| Pullback preserves CLD-psh | Proposition 8.1.5, printed p. 196, beginning at text line 9772. |
| Scalar-extended curvature is supported on the Shilov section | Proposition 16.8.2, printed pp. 463--464, text lines 23594--23603.  In dimension one with one curvature factor, the smooth factor is `1` of bidegree `(0,0)`, satisfying `max(0,0)>=1-1`. |
| Curvature pushes forward exactly | The reminder immediately after Proposition 16.8.2, text line 23603, invokes Proposition 8.7.5; the same equality of currents and measures is written explicitly in the proof of Corollary 16.8.6, printed p. 465, text lines 23691--23695. |

## The rigid lift, including inseparability

Let `L=H(y)`.  Since `y` is rigid, `L/K` is finite.  Any absolute value on
a finite algebraic extension of a trivially valued field is trivial: the
minimal polynomial gives `|a|<=1` for every integral algebraic element,
and applying the same observation to `a^{-1}` gives `|a|>=1` for `a!=0`.

Choose any `K`-basis `(e_1,...,e_d)` of `L`.  Because both ground norms are
trivial, it is an orthonormal basis.  Coefficientwise expansion gives

```text
L completed_tensor_K K((varpi))  --->  L((varpi)),
sum_j e_j tensor f_j             |->   sum_j e_j f_j.
```

Every Laurent series over `L` has a unique such expansion.  Its Gauss norm
is `max_j |f_j|_r`, so the map is an isometric algebra isomorphism.  The
right side is a field finite over `K((varpi))`; no linear-disjointness or
separability assertion is being smuggled in.  Consequently the analytic
scalar fibre over `y` is the singleton `sigma(y)`, and
`H(sigma(y))=L((varpi))`; in particular `sigma(y)` is rigid even when
`L/K` is purely inseparable.

The possible imperfection of `K` also does not threaten normality: the
extension used is analytically separable because its radius is `K`-free,
not because `K` is perfect.

## Measure transfer

After shrinking inside the normal locus and analytic interior, write
`Omega_r=Omega completed_tensor_K K_r`, `u_r=pi^*u`, and
`mu_r=d'd''[u_r]`.  Proposition 16.8.2 and Proposition 8.7.5 give

```text
supp(mu_r) subset sigma(Omega),        pi_* mu_r = mu_u.
```

As `pi o sigma=id`, the Shilov image meets the fibre over `y` only in
`sigma(y)`.  Hence

```text
mu_u({y}) = mu_r(pi^{-1}{y}) = mu_r({sigma(y)}).
```

All hypotheses of the frozen nontrivially valued normal rigid-point lemma
hold at `sigma(y)`: the field is nontrivially valued; the point is rigid
and interior; the scalar-extended local ring is normal; the space is good,
separated, strict, and purely one-dimensional.  That lemma makes the last
quantity zero.

## The index error in Corollary 16.8.6

The error can be diagnosed internally and conclusively.

1. Theorem 16.8.5 (printed p. 464, text lines 23629--23632) concerns a
   positive closed current of **bidimension `(q,q)`**, a smooth form of
   bidegree `(q,q)`, and a tropical `H^q`-negligible set.
2. A product of `p` curvature currents on an `n`-space has bidegree
   `(p,p)` and therefore bidimension `(n-p,n-p)`.  The smooth complementary
   factor in Corollary 16.8.6 has bidegree `(n-p,n-p)`.
3. Thus applying Theorem 16.8.5 forces `q=n-p`, and the negligibility
   exponent must be `n-p`.  The printed `H^p` in text lines 23671--23674
   reuses the number of curvature factors where the bidimension is needed.
4. The proof itself says the nontrivially valued assertion is a special
   case of Theorem 16.8.5 (lines 23675--23677), confirming the intended
   substitution.  Its trivially valued continuation repeats the same
   index typo at lines 23684--23696.
5. Keeping the printed exponent produces a concrete contradiction.  On a
   nontrivially valued analytic projective line, the continuous psh model
   weight `max{0,log|T|}` has curvature a unit Dirac mass at the unit Gauss
   point.  That singleton is tropically `H^1`-negligible.  For `n=p=1`,
   the printed corollary would say the Dirac mass does not charge its own
   support.  With the corrected exponent `H^0`, the singleton is not
   negligible, and the contradiction disappears.

Accordingly, Corollary 16.8.6 is usable only after replacing `H^p` by
`H^{n-p}`.  The corrected result cannot prove the rigid-point assertion on
a curve; the separate Gauss transfer above is essential.

## Final integration gate

The exact frozen transfer is mathematically source-complete and suitable
for dependency-closed production verification.  It may be used to prove
the arbitrary-valuation componentwise curve theorem only after such a
production run returns `correct` with zero critical errors and zero gaps.
Any proof that instead cites the printed `H^p` version of CLD Corollary
16.8.6 must be rejected.
