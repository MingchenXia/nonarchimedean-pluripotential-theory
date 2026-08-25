# P01.1: current positivity and complete-intersection curve slicing

## Disposition

The unrestricted problem in Chapter 72 is **not solved** by this dossier.
It is, however, narrowed in a source-backed way.

1. There is a production-Rethlas-verified complete-intersection slicing
   formula for a continuous real PL function whose ambient current is
   positive.  It proves nonnegativity against restrictions of ambient
   nonnegative smooth compactly supported functions, and hence of an
   isolated curve-Laplacian atom when a tightly supported ambient cutoff
   exists, at a point where the curve is cut out by a regular sequence of
   length `dim(X)-1`.
2. Combining that formula with the local curve-lifting argument of
   Gubler--Rabinoff suggested a converse on a pure rig-smooth boundaryless
   ambient space, but production Rethlas rejected the exact candidate.  The
   cited slope formula does not cover the lifted curve in the generality
   established by the packet: the curve need not be rig-smooth over an
   imperfect ground field, and the packet has no descent/model-current
   formula for arbitrary `K` and possibly nonreduced formal models.
3. The unrestricted problem therefore has two distinct obstructions.  At a
   singular central-dimension-one ambient germ, a regular sequence of length
   `dim(X)-1` need not exist.  Even in a rig-smooth ambient, the present lift
   still lacks a source-backed positive-multiplicity identification between
   the residual negative degree and the atom of the lifted curve current.

The theorem and proof packet in
`manuscript/editorial/rethlas_packets_20260825/p01_rigsmooth_current_converse_exact.tex`
received production verdict **final/wrong**.  The controlling receipt is
`manuscript/editorial/rethlas_receipts_20260825/p01_rigsmooth_current_converse_production_receipt.md`.
The separately frozen slicing proposition in
`manuscript/editorial/rethlas_packets_20260825/p01_lci_slicing_source_aware_proof_exact_20260825.tex`
received production verdict **final/correct**.  Its controlling receipt is
`manuscript/editorial/rethlas_receipts_20260825/p01_lci_slicing_production_receipt.md`.
Nothing from this dossier has been inserted into a live chapter, and no
novelty or priority assertion is made.

## Exact live question

The live problem is `prob:frontier-current-pullback` in
`manuscript/parts/part6/ch72_major_open_problems.tex`.  If `K` is complete
and nontrivially valued, `X` is good, separated and strict, and `h` is a
real-valued real PL function, it asks whether

\[
                     \mathrm d'\mathrm d''[h]\geq 0
\]

on `Int(X)` forces `h` to be residue-nef/model semipositive there.  GJR,
Theorem 7.14 proves the reverse implication.  GR, Remark 1.8 explicitly says
that the converse and positivity-preserving pullback remain unknown.

The previous isolated Rethlas attempt correctly left the implication open,
proved only a conditional curve-restriction reduction, and rejected a
coarse cross-fan tropical argument.  The present route does not use coarse
branch aggregation.

## Primary sources checked

### Gubler--Rabinoff

Primary PDF: Walter Gubler and Joseph Rabinoff, *On semipositive piecewise
linear functions in non-archimedean analytic geometry*, arXiv:2503.05513v1.

- Remark 1.8: an R-PL function with positive CLD current is not known to be
  semipositive; the issue is tied to unknown pullback stability.
- Theorem 4.1: if the closure of a reduction point has dimension `d`, then
  locally one obtains an irreducible `d`-dimensional Zariski-closed analytic
  subspace through a point reducing to it.
- Remark 4.2: any Zariski-closed analytic subspace through that point has
  dimension at least `d_K(z)`.
- Section 5.2: a point is interior exactly when the closure of its reduction
  is proper.
- Proposition 5.1: on a smooth strict analytic curve, the PL curvature
  measure has at a component point the degree of the residual model line
  bundle; positivity is equivalent to residue-nefness.
- Theorem 5.3 and its proof: a negative residual degree is detected by a
  one-dimensional local lift.  Its formal closure has a proper residual
  component finite and surjective over the original residual curve, and the
  projection formula multiplies the negative degree by a positive degree.

### Chambert--Loir--Ducros, version 2

Primary PDF: Antoine Chambert-Loir and Antoine Ducros, *Formes
diff\'erentielles r\'eelles et courants sur les espaces de Berkovich*,
arXiv:1204.6277v2, 25 July 2025.

- Proposition 8.7.2: joint Bedford--Taylor continuity under local uniform
  convergence, including an arbitrary continuous outer factor `u_0`.
- Corollary 18.6.2: for
  `u_r=log max(r,|f_1|,...,|f_d|)`, the current
  `(d'd''u_r)^d` is integration over the Gauss fibre.
- Theorem 18.7.2 and Proposition 18.7.3: the Bochner--Martinelli identity and
  stabilization of Gauss-fibre integrals to the regular complete
  intersection.  Proposition 18.7.3 explicitly permits compactly supported
  G-forms with locally bounded tropically Borel coefficients.  This is the
  clause that permits the coefficient `h` below.
- Section 11.5.5, formula (11.5.5.1): for a good germ,
  `dim_cent(X,z)+dim_Krull(O_{X,z})=dim_z(X)`.
- Corollary 6.2.4 and Corollary 6.2.8: smooth compactly supported cutoffs.

There is a typographical inconsistency in the displayed hypothesis of CLD
Proposition 18.7.3: it says that `f:X->A^d` is purely of relative dimension
`d`, whereas the next sentence and the proof use relative dimension `n-d`.
The proof at printed page 534 explicitly shrinks until the relative
dimension is `n-d`.  The packet uses the proof-correct value `n-d`.

### Gubler--Jell--Rabinoff

Primary published PDF: Walter Gubler, Philipp Jell and Joseph Rabinoff,
*Forms on Berkovich spaces based on harmonic tropicalizations*, Bull. Soc.
Math. France 154 (2026), 135--238.

- Proposition 7.1 and Lemma 7.4: residue-nefness is represented by nefness
  on a formal model and is tested by degrees on proper residual curves.
- Theorem 7.14: semipositive R-PL functions have positive CLD current on the
  relative interior.

### Local algebra input

For a rig-smooth pure `n`-dimensional analytic space, the ordinary local
ring at a good point is regular.  This follows from Ducros, *Families of
Berkovich spaces*, Corollary 5.3.5 (quasi-smoothness agrees with geometric
regularity), hence in particular ordinary regularity.  Together with CLD
(11.5.5.1), a point of
central dimension one has a regular local ring of dimension `n-1`.  In a
regular local ring the maximal ideal is generated by a regular system of
parameters.  Coherence and openness of the non-zero-divisor conditions let
one realize these germs by analytic functions forming a regular sequence
after shrinking.

Production Rethlas found no separate defect in this ambient regular-local
chain, but its final verdict was wrong for the later curve-slope source-scope
failure.  The whole theorem packet is therefore rejected regardless of this
local-algebra calculation.

## The slicing calculation

Let `X` be boundaryless, separated, pure `n`-dimensional and let
`f_1,...,f_{n-1}` be a regular sequence on an open neighbourhood `V`, with
pure one-dimensional zero locus `C`.  Put

\[
 u_r=\log\max\{r,|f_1|,\ldots,|f_{n-1}|\}.
\]

For fixed `r>0`, smooth the maximum by the CLD regularized maximum.  The
truncation property makes

\[
 u_{r,\varepsilon}
 =M_\varepsilon(\log r,\log|f_1|,\ldots,\log|f_{n-1}|)
\]

a globally well-defined smooth psh function: near a zero of some `f_i`, that
entry is sufficiently below the finite maximum and is omitted by the
regularization.  Moreover

\[
 u_r\leq u_{r,\varepsilon}\leq u_r+\varepsilon.
\]

If `psi>=0` is a smooth compactly supported ambient function, positivity of
`T=d'd''[h]` gives

\[
 0\leq \langle T,\psi(\mathrm d'\mathrm d''u_{r,\varepsilon})^{n-1}\rangle.
\]

The factors in the test form are smooth, positive and closed.  Twice
integrating by parts therefore yields

\[
 \langle T,\psi(\mathrm d'\mathrm d''u_{r,\varepsilon})^{n-1}\rangle
 =\int_X h\,\mathrm d'\mathrm d''\psi\wedge
       (\mathrm d'\mathrm d''u_{r,\varepsilon})^{n-1}.
\]

CLD Proposition 8.7.2 applies with the continuous outer factor `u_0=h`, so
the right side converges to the same expression with `u_r`.  Corollary
18.6.2 changes it to integration over `f^{-1}(eta_r)`.  Finally Proposition
18.7.3 applies to

\[
                     \omega=h\,\mathrm d'\mathrm d''\psi.
\]

This is a compactly supported G-form of bidegree `(1,1)` whose coefficients
are locally bounded and tropically Borel: on a finite G-cover of its support,
`h` is represented by a continuous piecewise-affine tropical function.  For
small `r`, stabilization gives

\[
 0\leq \int_C h|_C\,\mathrm d'\mathrm d''(\psi|_C)
   =\langle \mathrm d'\mathrm d''[h|_C],\psi|_C\rangle.       \tag{*}
\]

The equation is local and every test object is compactly supported away from
the boundary.  It does not assert that an arbitrary nonnegative smooth
function on `C` has a nonnegative smooth extension to `X`.

If the curve current is a discrete model measure near `z`, choose an ambient
smooth cutoff equal to one near `z` and with support avoiding all its other
atoms.  Equation (*) proves that its coefficient at `z` is nonnegative.

## Why the rig-smooth route almost closes, and where it fails

Assume a negative residual degree at `x`.  Follow the proof of GR Theorem
5.3 to obtain `z` and an irreducible analytic curve `C` through `z`, with
`red(z)` the generic point of a proper residual curve.

The reduction field gives `d_K(z)>=1`, while GR Remark 4.2 applied to the
one-dimensional `C` gives `d_K(z)<=1`.  Hence `d_K(z)=1`.  Since `C` is a
Zariski-closed germ of dimension one through `z`, central dimension is at
most one; it is always at least `d_K(z)`.  Thus

\[
                         d_K(z)=\dim_{\mathrm{cent}}(X,z)=1.
\]

If `X` is rig-smooth of pure dimension `n`, then `O_{X,z}` is regular and,
by CLD (11.5.5.1), has Krull dimension `n-1`.  The local ring of the
irreducible curve at `z` has Krull dimension zero (the same dimension
formula on `C`), hence it is a field.  Consequently the ideal of `C` at `z`
is the maximal ideal of `O_{X,z}`.  A regular system of parameters therefore
cuts out `C` near `z` by a regular sequence of length `n-1`.

The slicing calculation makes the curve-current atom at `z` nonnegative.
The candidate then asserted that the formal-model degree/slope calculation
used in GR Proposition 5.1 and the proof of Theorem 5.3 identifies the same
atom with the degree on the proper residual component lying over the
original negative curve, up to a strictly positive generic multiplicity.
That assertion is precisely the step which failed verification.  GR
Proposition 5.1 is stated for smooth strict analytic curves; its explicit
coefficient computation passes to an algebraically closed field and a
reduced special fibre.  The lifted curve here is only known to be
irreducible and an ordinary local complete intersection.  Over a possibly
imperfect `K`, ordinary regularity does not imply geometric regularity, and
the packet supplied neither base-change/descent nor a singular-curve model
current formula for nonreduced formal models.  The projected residual degree
is negative, but its identification with the analytic atom is not proved in
the claimed scope, so the contradiction cannot be taken.

## Hostile audit

### Boundary

The current hypothesis is used only on a topologically open boundaryless
neighbourhood of the detecting point, and all cutoffs have compact support
there.  An affinoid neighbourhood from the lifting proof is used to obtain a
formal model and compute the residual degree, not as the boundaryless
ambient space in the CLD slicing formula.

### Compactness

No noncompact fibre integral is taken without a compactly supported form.
The support of `h d'd''psi` is compact, exactly as required in CLD
Proposition 18.7.3.  Only finitely many atoms meet that support.

### Tropicalization

No single coarse tropical chart is used to select a branch.  The refined CLD
current is tested before passing to Gauss fibres; the complete-intersection
current carries analytic multiplicities.  Thus the cross-fan obstruction in
the previous attempt is irrelevant to this calculation.

### Curve restriction

The proof does not assume a pullback of the ambient current.  It proves only
the pairings needed to isolate model atoms.  It also does not assume that
every nonnegative curve test function has a nonnegative ambient extension.

### Singular and excess-intersection locus

This is the genuine remaining gap.  At a singular central-dimension-one
germ, the local ring can have depth smaller than `n-1`; then a regular
sequence of the required length need not exist.  The Bochner--Martinelli
slice above cannot be formed.  Replacing the regular sequence by arbitrary
generators introduces excess-intersection terms for which positivity and
fibre stabilization have not been established.

### Degree atom

Production Rethlas checked this point and rejected it as a critical error.
The cited smooth-curve result does not justify the claimed formula for the
possibly singular lifted curve over arbitrary `K`, and the packet does not
define and establish the positive multiplicity in the possibly nonreduced
formal model.  CLD Corollary 18.8.8 does not fill the gap for arbitrary real
PL functions because its stated equivalence has integral PL scope.

## Skill audit

The `descending-zero-locus-nefness` skill was read and tested against this
problem.  It does not apply directly.  That skill assumes a projective
variety, complete curves, restricted regular sections, and nef comparison
line bundles.  Here the analytic ambient is local/nonproper and no family of
sections or comparison bundles is present.  The only useful common motif is
that proper residual curves can detect a bad sign.  The actual descent is
performed by CLD complete-intersection currents, not by the skill's
zero-locus induction.

## Verdict for the atomic inventory

- **P01.1 globally:** NARROWED, still active.
- **Complete-intersection detecting curves:** VERIFIED in the exact
  ambient-test and tightly supported isolated-atom scope recorded by the
  standalone production receipt.  It does not assert positivity against
  arbitrary nonextendable curve test functions.
- **Pure rig-smooth boundaryless ambient spaces:** NOT SOLVED.  The exact
  candidate received `final/wrong` because the degree-atom multiplicity step
  exceeds the hypotheses of the cited curve slope formula.
- **General singular ambient spaces:** OPEN.  The remaining target is a
  positive excess-intersection slice or an alternative argument at
  non-Cohen--Macaulay central-dimension-one germs, together with a
  source-backed curve-current/degree comparison in the general lifted-curve
  scope.

## Superseding addendum, 25 August 2026

The preceding disposition is retained as the exact history of the rejected
curve-lifting route, but it no longer describes the live problem status.
P01 is resolved in the pure-dimensional CLD framework by
`thm:p01-real-pl-positive-current-candidate`.

The successful proof avoids restriction and pullback of positive currents.
On one projective model of the reduction germ, an ample line bundle is
realized by an integral PL germ `a`.  For the finite integral decomposition
`h=sum lambda_i h_i`, a single integer `N` makes `Na+h_i` and `Na-h_i`
semipositive.  Rational approximants to the coefficients, corrected by a
small positive multiple of `a`, therefore have positive current.  CLD
Corollary 18.8.8 makes their residual classes nef, and their degrees on every
proper integral curve converge to those of the original real residual
class.  This proves the missing implication.

The exact pure-dimensional statement and proof passed production run
`20260825T080059Z_80f35689475f`, item
`pi_33f9d15994f62f668065256e`, with `gpt-5.6-sol` at `xhigh`, final
`correct`, zero critical errors, and zero gaps.  The earlier broader run
`20260825T075050Z_235cca2fd59b` is preserved but noncontrolling because a
fixed-bidegree CLD current is formulated on a pure-dimensional `n`-space.

The later source audit also located CLD Theorem 18.4.7, whose
one-dimensional model-current formula allows singular and nonreduced pure
analytic curves and supplies the degree--atom comparison missing from the
rejected route.  This repairs that historical source gap but is not needed
for the ample-order-unit proof.  The old final verdicts remain part of the
audit trail; they are not evidence against the different successful proof.
P01 is removed from the active inventory.  No novelty or priority claim is
made.
