# Hostile audit

Date: 30 August 2026

Status: staged hostile audit, not a production verdict and not a license for
live integration.

## Verdict

The exact Candidate A and Candidate B proofs close under their displayed
hypotheses. The original idea of a **finite-flat** smooth lattice cover is
false and has been removed rather than hidden. Candidate B uses a finite,
surjective, generally nonflat diagonalizable quotient; its equal-
characteristic $p$-primary factor is handled by Candidate A.

No optional ordinary analytic étale corollary is present in this packet.

## Fatal finite-flat counterexample

Let

```text
N  = Z^2 + Z(1/2,1/2),
N' = Z^2,
sigma = R_{>=0}^2.
```

Then the standard smooth lattice cover is

```text
K[x^2,xy,y^2]  -->  K[x,y].
```

It has generic rank two. At the toric vertex, however, its fibre is

```text
K[x,y]/(x^2,xy,y^2),
```

which has $K$-basis $1,x,y$ and dimension three. A finite flat module of
rank two would have two-dimensional fibres, so the map is not flat. The
calculation is characteristic independent. In characteristic different from
two it is the constant sign quotient; in characteristic two it is the
nonreduced $\mu_2$, radicial quotient. It also shows why residue
characteristic cannot rescue flatness.

**Firewall:** neither statement nor proof uses the words “finite flat” as a
hypothesis or conclusion. GJR Proposition 5.11 is not a dependency.

## Candidate A audit

### 1. Arbitrary real-PL G-cover

- GJR Definition 5.1 supplies unit-log expressions on a G-cover by objects of
  the strict-affinoid-generated G-site.
- The target of the pullback is strict affinoid after localizing on $X$.
  G-quasicompactness gives a finite subcover.
- Gerritzen–Grauert refines each strict affinoid domain by finitely many
  rational domains in the ambient affinoid.
- Restricting an analytic unit to the rational pieces preserves invertibility.

This avoids the invalid move “a G-domain containing a point is an ordinary
neighborhood,” which caused the superseded constant-group proof gap.

### 2. Descent of rational inequalities

For a rational domain defined by $b_0,\ldots,b_s$, the proof sets
$a_i=b_i^q$. Raising a unit-ideal identity to the $q$-th power proves
that the $a_i$ again generate the unit ideal. The inequalities descend
because absolute values satisfy $|b_i|^q=|a_i|$ at the unique lifted point.
The image is therefore a genuine rational analytic domain, not only a subset.
The images form a finite cover, hence a G-cover.

### 3. Descent of units

The proof does not infer invertibility from nonvanishing. It descends both
$t^q$ and $(t^{-1})^q$; injectivity of the target affinoid algebra then
shows their product is one. Injectivity follows from surjectivity of the
finite map and reducedness of the target. Rational domains in a reduced
analytic space remain reduced.

### 4. Affinoid localization and completion

For the toric $A\subset B$, the ring $B$ is finite over $A$. After an
arbitrary target affinoid base change $C$, the inverse algebra is a finite
$C$-module and hence already complete. Every element is a **finite** sum
$\sum c_i\otimes b_i$; there are no infinite-series cross terms. Frobenius
gives

```text
(sum c_i tensor b_i)^q = sum c_i^q tensor b_i^q in C.
```

The same calculation applies after every rational localization. Thus the
uniform $D^q\subseteq C$ hypothesis needed on the descended domains is
actually verified, not assumed from the algebraic generic fibre alone.

### 5. Coefficient firewall

The local expression divides real coefficients by $q$. This is valid for
$\mathbf R$. The proof does not claim integral-PL descent, and it would not
prove it.

## Candidate B audit

### 1. Non-full-dimensional cone

$N_\sigma=N\cap\operatorname{span}_{\mathbf R}\sigma$ is saturated, so
it is a direct summand of the lattice $N$. The $r$ primitive ray vectors
span a finite-index sublattice of $N_\sigma$; adjoining a complement gives
the smooth source
$\mathbf A^r\times\mathbf G_m^{\operatorname{rank}N-r}$. No fixed point
or full-dimensional assumption is smuggled into the proof.

### 2. Field characteristic versus residue characteristic

- In characteristic zero, the whole finite diagonalizable kernel is finite
  étale, even when the residue characteristic divides its order.
- In characteristic $p>0$, only the prime-to-$p$ factor is made constant.
- The verified constant-group theorem has no residue-order restriction.

Any replacement of `char K` by residue characteristic in the factorization
would be false.

### 3. Missing roots of unity

The proof does not assume that $K$ contains roots of unity. It passes to a
finite Galois splitting field for the exponent of the étale factor. The
relevant cyclotomic polynomial is separable: automatically in characteristic
zero and because the exponent is prime to $p$ in characteristic $p$.
The $p$-primary group scheme is **not** claimed to become constant; a
$\mu_{p^e}$ factor remains nonreduced after every extension.

### 4. Exact quotient restriction

After splitting, the group order is nonzero in $L$, so the Reynolds
operator is a bounded idempotent on every finite affinoid base change. Its
image is exactly the invariant algebra. It does not matter that the group
order may fail to be a unit of $L^\circ$. This verifies the analytic
categorical quotient hypothesis of the already-verified constant-group
descent theorem on each affinoid chart.

### 5. Classical pluriharmonic pullback

Scalar extension and arbitrary analytic pullback use exactly
Gubler–Rabinoff Proposition 7.2(6),(7). No pullback theorem for CLD currents
is invoked. Relative boundary is harmless because the published
pluriharmonic functoriality is for arbitrary analytic morphisms.

### 6. Scalar descent

The final extension $L/K$ is finite algebraic and complete. GJR Corollary
5.12 applies to the good strict domain $U$ with divisible coefficient group
$\mathbf R$. Galois invariance is not substituted for this theorem.

### 7. Harmonicity

Only after real-PL regularity is established does the proof apply
Gubler–Rabinoff Theorem 4.3 to $h$ and $-h$. GJR Definition 7.2 then gives
harmonicity. No pure-dimensional or boundaryless hypothesis is added by
these cited statements.

## Scope firewalls

Candidate B covers exactly:

- split affine toric varieties;
- strongly convex simplicial rational cones of arbitrary dimension;
- good strict analytic domains;
- arbitrary complete nontrivially valued ground fields;
- equal-characteristic wild $p$-primary lattice indices.

It does not cover:

- non-simplicial cones;
- nonsplit toric forms without a separate splitting/descent argument;
- ordinary analytic étale charts (deliberately omitted here);
- log-étale or general toroidal charts;
- arbitrary singular analytic germs;
- arbitrary finite radicial maps lacking the displayed uniform affinoid
  $q$-power property;
- integral or rational PL coefficients.

Candidate B narrows the toric residual of P06.1 but does not retire P06.1 or
change the atom count, tier count, or queue position.

## Freeze disposition

The exact bytes may be treated as a **staged candidate** after the clean
compile and SHA-256 check. They are not production verified. Any future
statement that restores flatness, omits reducedness from Candidate A without
repairing the unit argument, conflates field and residue characteristic,
claims a constant $p$-primary group, or adds the excluded chart scopes must
undergo a new proof and hostile audit.
