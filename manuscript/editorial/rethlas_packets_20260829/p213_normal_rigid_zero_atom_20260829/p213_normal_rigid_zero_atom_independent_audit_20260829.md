# Independent hostile audit: P21.3 normal rigid-point zero atom

Date: 29 August 2026

## Final repaired-byte re-audit

Verdict on the repaired exact bytes: **PASS for independent mathematical
and source audit.**  The frozen hashes are:

- statement SHA-256:
  `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`;
- proof SHA-256:
  `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`.

The repaired statement restricts `Omega` to the pure one-dimensional
neighborhood supplied by the hypotheses and defines the curvature measure
on `Omega^circ=Omega cap Int(X/K)`.  This set is boundaryless by CLD
(11.4.1.3), and pure dimension one is preserved by passage to an open
subspace.  Thus its integration current is positive and closed, CLD Lemma
8.5.5 applies, and Proposition 7.2.8 identifies the resulting positive
bidimension-`(0,0)` current with a Radon measure.

The repaired proof uses ordinary normality only to obtain a DVR at the
rigid point via CLD (11.5.5.1) and official Stacks Tag `00PD`.  It then uses
CLD Remark 11.4.7 exactly as required: the finite local algebra is
torsion-free, hence free and flat over the target DVR, and relative
interiority upgrades local-ring flatness to analytic flatness.  CLD 11.6.3
therefore supplies the compact finite-flat tube with the chosen point as
the sole zero-fibre point.  No geometric regularity or separability is
inserted.  The calibrated step now also cites CLD Lemma 13.3.8, so the
factor in Proposition 14.4.2 is exactly the finite-flat degree `d`, even
over an imperfect field and with inseparable residue extension.  The
cutoff, sign, total-variation `2d`, transposition, and atom estimate checks
below apply unchanged.

A forced standalone rebuild of these exact files succeeded in three pages.
The log contains no TeX error, undefined reference or citation, multiply
defined label, or overfull/underfull box.  The resulting PDF SHA-256 is
`63d5f90dd1a6638062d39a29f9a5088090db2f660a37e51cc664975e6df47858`.
This PASS is an independent gate only; production Rethlas verification of
the two frozen source hashes is still required before live integration.

## Superseded-byte audit record

Verdict on the earlier exact bytes audited: **REPAIR REQUIRED; do not submit these
hashes to production Rethlas and do not integrate them.**  The local radial
argument is mathematically sound after the repairs below, but the statement
as frozen calls a current on an arbitrary possibly bordered and possibly
non-one-dimensional neighborhood a positive Radon measure.  That assertion
is not justified and is false in that generality.

## Exact bytes audited

- statement SHA-256:
  `20d5dec71297dc1cb378865b541f846771f46aca5790778341128ef5012e2235`;
- proof SHA-256:
  `c9d9b949c9528b326978da19163523a04e1798f7c8fe0d94fdc55205b9c99e78`.

The source comparison used
`/private/tmp/p21_bridge_sources/cld25.pdf`, SHA-256
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`,
and the official Stacks Project pages for Tags `00PD` and `04GH`.

## Blocking formulation defect

The statement lets `Omega` be an arbitrary open neighborhood of the
interior point `y` and declares

`mu_u = d'd''[u]`

to be a positive curvature measure on `Omega`.  An ordinary open analytic
subspace can retain analytic boundary: by CLD (11.4.1.3), its absolute
boundary is its intersection with the boundary of the ambient space.  In
particular, one may take `X=Omega` to be a closed strict disc and `y=0`.
The constant function is continuous and psh, but the integration current
of the closed disc is not closed; its differential carries boundary terms.
Thus `d'd''[1]` is not supplied as a positive Radon measure by CLD Lemma
8.5.5.  Section 8.5 explicitly works with a boundaryless ambient tropical
space, and CLD 7.7.4 is what makes its integration current closed.

The proof itself avoids this defect by shrinking to a boundaryless open
set `U` inside `Omega cap Int(X/K)`.  Hence the zero-atom conclusion is a
valid local conclusion, but the displayed global measure in the frozen
statement is not defined with the asserted positivity.

There is a second, independent scope defect.  The hypotheses make `X`
purely one-dimensional only on some unspecified neighborhood of `y`, while
`Omega` is allowed to be any open neighborhood.  Thus `Omega` may also meet
higher-dimensional components (for example, take a disjoint union of a
curve containing `y` and a surface).  On an `n`-dimensional component with
`n>1`, `d'd''[u]` has bidimension `(n-1,n-1)`, not `(0,0)`, so Proposition
7.2.8 does not turn it into a Radon measure.  Intersecting with the analytic
interior fixes the boundary problem but not this dimension problem.

### Exact repaired statement wording

Fold the local-pure-dimension hypothesis into the choice of `Omega`: require
that `Omega` be an open neighborhood of `y` **on which `X` is purely
one-dimensional**.  (Such a subneighborhood exists by the original local
hypothesis, and the given function restricts to it.)  Then replace the
conclusion by the following text:

```tex
Put
\[
                 \Omega^\circ:=\Omega\cap\operatorname{Int}(X/K).
\]
Then \(\Omega^\circ\) is a boundaryless open neighborhood of \(y\), and
the current
\[
        \mu_u:=\mathrm d'\mathrm d''[u|_{\Omega^\circ}]
\]
is a positive Radon measure on \(\Omega^\circ\).  It has no atom at
\(y\):
\begin{equation}
\label{eq:p213-normal-rigid-zero-atom}
                         \mu_u(\{y\})=0.
\end{equation}
```

This preserves the natural local formulation and does not impose an
unnecessary global boundarylessness hypothesis.  In the proof, apply CLD
Lemma 8.5.5 first on `Omega^circ` with its closed integration current, and
then restrict the resulting measure to the smaller normal coordinate
neighborhood `U`.  Differential currents and Radon measures restrict as
sheaves, so the radial estimate on `U` computes the atom of the displayed
`mu_u`.

## Local algebra and analytic flatness

The dimension calculation is correct.  At a rigid point the kernel in a
strict affinoid chart is maximal: the affinoid quotient embeds in the
finite-dimensional `K`-space `H(y)`, hence is a finite-dimensional domain
and therefore a field.  Thus the central dimension is zero.  CLD
(11.5.5.1), goodness, and pure local dimension one give
`dim O_{X,y}=1`.  Official Stacks Tag `00PD` then applies exactly and makes
the normal local ring a DVR.

The frozen Tag `04GH`/idempotent/free-locus route is defensible: finiteness
at `y` makes the local ring finite over the target local DVR; a finite
morphism has a product of local stalks over the target point; henselianity
isolates the factor through `y`; an idempotent germ extends after
shrinking; and freeness of the corresponding coherent direct image is an
open condition.  Nevertheless this route is longer than necessary and
leaves several standard extension steps implicit.

The cleaner exact repair is to cite CLD Remark 11.4.7.  Once the local map

`A=O_{A^1,0} -> B=O_{X,y}`

sends `T` to the uniformizer `pi`, it is injective; `B` is finite over `A`
by CLD 11.4.4 and torsion-free because it is a domain, hence finite free
over the DVR `A`.  Therefore `B` is flat over `A`.  Since the proof already
establishes `y in Int(X/A^1)`, CLD Remark 11.4.7 upgrades this ordinary
local-ring flatness to analytic flatness at `y`, without any separability
or geometric-regularity hypothesis.  CLD 11.6.3 then directly supplies
compact finite-flat neighborhoods and permits the source neighborhood to
be chosen with `f^{-1}(0)={y}`.  Restricting the target neighborhood to a
sufficiently small closed disc yields the displayed finite flat tube.

## Radial and calibrated calculation

After the repaired measure formulation and the direct flatness citation,
the remainder of the proof passes the hostile audit.

- The choices of `R`, `r`, and `epsilon_0` place both transition bands
  strictly inside the finite tube.  The radial function is constant near
  the unique zero fibre and on an outer collar, so its two extensions are
  CLD-smooth by Corollary 15.1.2 and have compact support.
- `q_r''=rho_r'` has one sign on each transition band and
  `int |q_r''| = 2` exactly.
- CLD Proposition 14.4.2 pushes the canonical calibration forward.  For
  complete source traceability, the repaired proof should cite CLD Lemma
  13.3.8 at this point: finite analytic flatness identifies the calibrated
  degree with the ordinary finite-flat degree `d`.  This includes
  ramification, inseparable residue extensions, and every residue-degree
  factor.  The two disjoint bands then give exact total variation `2d`.
- CLD Lemma 7.7.5 gives the positive transpose sign.  Positivity of
  `chi_r` gives `H_r mu_u({y}) <= int chi_r dmu_u`; taking the absolute
  value of the transposed pairing before applying total variation gives
  the stated uniform bound.
- Nontrivial valuation supplies a cofinal sequence of admissible radii
  tending to zero.  Strictness, continuity, the interior hypothesis, and
  local pure dimension one are all genuinely consumed.

No step uses geometric normality, rig-smoothness, a separable residue
extension, or algebraic closedness.  Consequently the repaired argument
also survives over imperfect fields.  It makes no claim at nonrigid,
nonnormal, or boundary points, over a trivially valued field, or for a
discontinuous psh function.

## Re-audit gate

After the statement and proof are patched, their new hashes must be frozen
and re-audited.  Only those repaired exact bytes may proceed to production
Rethlas.  The two hashes recorded above have failed this independent gate.
