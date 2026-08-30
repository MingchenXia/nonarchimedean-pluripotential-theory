# Hostile self-audit

Verdict: **PASS as a frozen research candidate in the stated scope**.

This is not a production verdict and does not authorize live-book
integration.

## Repair of the sole independent v2 audit gap

The controlling audit has SHA-256
`d884005655ff604eea9e45d90c243f8751ed8505d92700033d90ac2ef8ae4d10`.
It passed the positive-rank argument and every source check, but correctly
failed the exact v2 bytes because `rank(N)=0` left an undefined maximum over
an empty family.

V3 now branches before choosing nonzero monoid generators.  In rank zero,

```text
N=0, rho={0}, S={0}, U_k=M(K), q=0,
R_k=K, A=A_n=B, J=0.
```

Thus every fixed coefficient error is literally zero in every `A_n`; the
standard-etale coefficient-contraction hypothesis is immediate and the
proof never forms an empty-family maximum.  The later positive-rank estimate
is unchanged.  The source-Zariski proof also identifies the dense torus
orbit with this rank-zero transverse factor.

## Repair of the v1 production defects

### 1. GJR scope

The general singleton-Shilov result now concludes only

\[
                        h=p^*s^*h.
\]

No PL conclusion appears there.  The separate corollary assumes a
nontrivially valued field and good strict analytic source and target before
invoking GJR Lemma 5.4(1).  Thus neither the trivially valued nor nonstrict
case is smuggled into the citation.

### 2. One radius and four root problems

For a polynomial (F\) at (z\), the proof writes the Newton fixed-point map
and proves the explicit Lipschitz bound (MHr<1\).  Fixed inverse norms and
all higher Taylor coefficients are bounded uniformly.  The proof chooses
one (r\) before enlarging (n\), and applies it to exactly:

| algebra | polynomial | centre | role |
|---|---|---|---|
| (E_n\) | (g\) | (t\) | constructs (t_n\) |
| (E_n\) | (g_0\) | (t\) | exact-root uniqueness for (\alpha_n\beta_n\) |
| (C_n\) | (g_0\) | (T\) | constructs (T_n^0\) |
| (C_n\) | (g\) | (T\) | exact-root uniqueness for (\beta_n\alpha_n\) |

The central (D\)-expansion is included in the same (H\)-bound before
choosing (r\), so reduction to the identity also uses a proved uniqueness
ball.  The composite estimates are written explicitly and contractivity
keeps both images in the correct balls.

### 3. Algebraic chart to strict affinoid source

The construction checks each missing bridge.

1. Tag 025C gives an open immersion into
   `Spec R[Theta,G'(Theta)^(-1)]/(G)` with (G\) monic.
2. A principal open inside the image is represented by (F\), and
   (H=G'F\).  Inverting (H\) retains both the principal shrink and the
   derivative inverse.
3. A product strict affinoid (U_m\times V\) is placed inside the affine
   target open.
4. Bounds ( |\Theta|\leq|c|\) and
   ( |H(\Theta)|^{-1}\leq|d|\) are chosen strictly at (x\), then variables
   are rescaled to unit Tate bounds.
5. The first bound gives `A<T>/(g)` and the second is the rational domain
   `A<T,U>/(g,hU-1)`.  This proves the displayed strict quotient rather than
   assuming it.
6. The semigroup, tensor, and source algebras carry the stated quotient
   Gauss/projective norms, and every structural map used in Newton's method
   is contractive.
7. The fixed toric point is in the ordinary interior of every deeper weighted
   tube; ( |T(x)|<1\) and ( |U(x)|<1\) persist.  Hence every (C_n\), and
   the fixed fibre (D\), is an actual affinoid neighbourhood of (x\).

### 4. Quasi-smooth dependency

The only imported conclusion is the already production-verified
quasi-smooth PH theorem.  Its descent lemma and theorem proof, original lines
5--146, are copied exactly.  The v1 production objection concerned the
unrelated counterexample at original lines 148--195; those bytes and that
claim are absent.

### 5. Updated all-orbits status

The all-orbits dependency has since passed dependency-closed production with
verdict `correct`, zero critical errors, and zero gaps.  V3 records that
status and the exact response hash; it does not repeat the stale v1 wording.

## Additional hostile checks

- The zero-rank case uses the fixed norm on `B` for `A=A_n=B`, so all four
  retraction maps remain contractions and the Banach--Newton lemma applies
  without a toric decay estimate.
- In rank zero, `H(d)\langle S\rangle=H(d)` has its single Berkovich point as
  its singleton Shilov boundary, agreeing with the uniform final fibre
  argument.
- The product is (U_n\times D\), not (U_n\times V\); no etale cover is
  silently trivialized.
- The two localization inverses have norm at most one by a strict Neumann
  estimate, so both algebra maps are genuinely contractive Tate-algebra maps.
- No flatness or injectivity of the Banach base-change maps is used.
- The normalized toric restriction sends each nonconstant generator to a
  scalar of norm tending to zero times a unit-ball generator.  This proves
  coefficient decay for the finite error set.
- After scalar extension to every (\mathscr H(d)\), coefficients of a
  nonzero semigroup Tate series attain their maximum.  Reduction of two
  normalized series has nonzero product in
  (\widetilde{\mathscr H(d)}[S]\), so the Gauss norm is multiplicative and
  defines the unique Shilov point.
- Harmonicity is asserted only after real-PL regularity, by applying the
  classical-psh/semipositivity comparison to both signs.

## Fail-closed residuals

The residuals in `SCOPE_FIREWALL.md` remain open here.  In particular, this
packet does not claim a product or a descent theorem for a bare log-etale or
Kummer chart, a merely formal toroidal chart, an etale source chart available
only after an unmaterialized cover, or a trivially valued field.

## Compile and visual audit

The standalone wrapper compiled by `latexmk -pdf` through stable
cross-references to a twelve-page letter-size PDF.  The final log contains no
undefined reference, citation warning, multiply defined label, overfull or
underfull box, package warning, or fatal error.  All twelve pages were
rendered at 120 dpi and inspected individually.  No clipping, collision,
missing glyph, broken display, bad page break, or margin overflow was found.
