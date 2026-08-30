# P06.1 finite-quotient real-PL descent: hostile source-aware audit

Date: 30 August 2026

Status: **research audit and replacement proof candidate only**.  This file is
not a Rethlas verdict, is not licensed for live-book integration, and does not
alter the open-problem inventory.

Audited file:

`manuscript/editorial/rethlas_packets_20260830/`
`p061_finite_quotient_toroidal_research_20260830/`
`p061_finite_quotient_toroidal_research_note_20260830.md`

## 1. Verdict

The displayed statement of Lemma A is true, but its current proof is not.
Lines 91--152 of the audited note have a genuine Berkovich
Grothendieck-topology gap.  Orbit topology and an invariant structure sheaf do
not repair that gap.  A replacement proof is available from the following
three inputs:

1. Gubler--Jell--Rabinoff Proposition 5.8 and the model theorem in 5.6 replace an
   $\mathbf R$-PL function, on an ordinary open neighbourhood, by a finite
   real linear combination of integral PL model functions.
2. On a common equivariant formal model, tensor induction
   $\bigotimes_{\gamma\in H}\gamma^*\mathfrak L$ replaces the nonexistent
   finite-flat norm.
3. Zavyalov Theorems 3.3.4 and 4.4.1 construct the formal coarse quotient and
   identify its generic fibre with the analytic quotient.  The tensor-induced
   line bundle descends by an elementary invariant-frame argument that is
   valid without flatness and without any assumption on $|H|$.

Thus the current proof should be replaced wholesale.  It should not be
patched by declaring its set $Z$ to be a neighbourhood.

## 2. Exact failure of the current proof

### 2.1 A real-PL function need not have one unit expression on an ordinary
neighbourhood

Gubler--Jell--Rabinoff Definition 5.1 defines $\mathbf R$-PL using a
$G$-cover by strictly analytic domains.  It does **not** imply the assertion
at lines 91--98 that there is an ordinary neighbourhood $W$ of $y$ on which

\[
                 u=\sum_i a_i\log|f_i|
\]

for units on that one neighbourhood.  At a PL corner the defining
$G$-cover may require several analytic domains, none of which is asserted to
be an ordinary neighbourhood of the corner.  The correct ordinary-topology
statement actually proved in the source is Gubler--Jell--Rabinoff
Proposition 5.8: locally in the ordinary topology, an $\mathbf R$-PL function
is a finite real linear combination of **integral PL functions**.  It does
not identify the chosen ordinary open itself with one unit-log chart.

### 2.2 Intersecting a $G$-domain with a clean ordinary open does not make it
an ordinary neighbourhood

If $W$ at lines 91--98 is interpreted correctly as a strictly analytic
domain from a $G$-cover, then

\[
       C\cap\bigcap_{\gamma\in H}\gamma W
\]

need not contain any ordinary open neighbourhood of $y$.  Membership of a
Berkovich point in an analytic domain is weaker than membership in its
topological interior.  Consequently lines 108--116 do not prove that $Z$ or
$q(S)$ is an ordinary neighbourhood.

### 2.3 The quotient theorems do not assert the missing domain statement

Hansen--Johansson Theorem 5.3 constructs the rigid quotient, proves
finiteness, and identifies the quotient topology and invariant structure
sheaf.  It works with ordinary adic opens obtained from clean slices.  It does
not say that the image of the arbitrary Berkovich analytic domain in 2.2 is
an ordinary open or an analytic domain.  Zavyalov likewise gives invariant
open-affinoid bases and quotient compatibility, but does not turn the
particular $Z$ in the audited proof into an ordinary neighbourhood merely
because it contains $y$.

Therefore equations (2.2)--(2.4) in the audited note are being applied on a
quotient neighbourhood that has not been constructed.  The multiplication
of units in (2.3) is correct on a genuinely $H$-stable chart; the proof does
not supply such a chart with the required neighbourhood property.

## 3. Corrected statement

Let $K$ be a complete non-Archimedean field with nontrivial absolute value.
Let $Y=\mathcal M(A)$ be a separated strict $K$-affinoid space, let a finite
constant group $G$ act analytically on $Y$, and let

\[
                    q:Y\longrightarrow X=Y/G
\]

be the analytic categorical quotient.  Let $g:X\to\mathbf R$ be continuous.
If $q^*g$ is $\mathbf R$-PL, then $g$ is $\mathbf R$-PL.

No flatness, freeness, reducedness, normality, or hypothesis on $|G|$ in
$K$ or in the residue field is required.

## 4. Two auxiliary facts

### 4.1 Equivariant common formal model

Let $N$ be a strict affinoid space with an action of a finite group $H$, and
let $h_1,\ldots,h_m$ be integral PL functions on $N$.  There is an admissible
formal $K^\circ$-model $\mathfrak N$ of $N$ with an $H$-action and line
bundles $\mathfrak L_i\in M(\mathfrak N)$ such that

\[
                         h_i=h_{\mathfrak L_i}.
\]

Moreover, $\mathfrak N$ may be chosen with quasi-projective special fibre.

Here is a construction, included to close the equivariance dependency.  A
finite group acting on the strict affinoid algebra of $N$ preserves an
admissible affine formal model after one enlarges a finite set of topological
generators by all of its $H$-translates (and first scales the finite set so
that all translates are power-bounded).  Call this affine model
$\mathfrak N_0$.  Gubler--Jell--Rabinoff 5.6, using Gubler--Martin
Proposition 2.10, puts each $h_i$ on a formal model
$(\mathfrak N_i,\mathfrak L_i)$.  The precise common-model argument is as
follows.  Raynaud cofilteredness gives, for each $i$, an admissible formal
blowup

\[
             \mathfrak P_i\longrightarrow\mathfrak N_0
\]

and a morphism $\mathfrak P_i\to\mathfrak N_i$ inducing the identity on the
generic fibre.  Form the fibre product over $\mathfrak N_0$ of all
$\gamma^*\mathfrak P_i$, for $i=1,\ldots,m$ and $\gamma\in H$, and take the
schematic closure of its common diagonal generic fibre.  Equivalently, take
the $K^\circ$-torsion-free strict transform of that diagonal.  Denote the
result by $\mathfrak N$.  It is an admissible formal model of $N$; $H$
permutes the factors, preserves the diagonal, and hence acts on
$\mathfrak N$.  Projection to the factor $\mathfrak P_i$ and then to
$\mathfrak N_i$ pulls $\mathfrak L_i$ back to $\mathfrak N$.

Each $\mathfrak P_i\to\mathfrak N_0$ is projective, because it is an
admissible formal blowup.  Thus $\mathfrak N$ is a closed formal subscheme of
a projective formal scheme over the affine $\mathfrak N_0$.  Its special
fibre is projective over the affine finite-type scheme
$\mathfrak N_{0,s}$, hence quasi-projective over the residue field.  This is
the equivariant diagonal-closure version of Raynaud's common-model argument;
in particular, quasi-projectivity is not being inferred merely from the
existence of an arbitrary dominating model.

Zavyalov Remark 3.3.3 now shows that every $H$-orbit of $\mathfrak N$ lies
in an affine open.  Hence Zavyalov Theorem 3.3.4 applies to
$\mathfrak N/H$.

### 4.2 Tensor induction descends through a possibly wild coarse quotient

Let $\pi:\mathfrak N\to\mathfrak X=\mathfrak N/H$ be the formal quotient
from Zavyalov Theorem 3.3.4, and let $\mathfrak L$ be a line bundle on
$\mathfrak N$.  Put

\[
       \operatorname{TI}_H(\mathfrak L)
          :=\bigotimes_{\gamma\in H}\gamma^*\mathfrak L.
\]

Reindexing the factors gives this line bundle a canonical $H$-linearization.
It descends to a line bundle $\overline{\mathfrak L}$ on $\mathfrak X$.

This assertion does not use a tame-stack descent criterion.  Fix
$x\in\mathfrak X$.  Its inverse image is one finite $H$-orbit.  By the
affine-orbit property and semilocal triviality of a rank-one projective
module, there is an open neighbourhood $V$ of this whole orbit on which
$\mathfrak L$ has one frame $s$.  Intersecting the finitely many translates
of $V$ makes $V$ $H$-stable while preserving the frame.  On $V$ the section

\[
                         S=\bigotimes_{\gamma\in H}\gamma^*s
\]

is an $H$-invariant frame of $\operatorname{TI}_H(\mathfrak L)$.  The image
$U=\pi(V)$ is open, $\pi^{-1}(U)=V$, and the quotient structure sheaf is the
invariant structure sheaf.  On overlaps, ratios of two such frames $S$ are
$H$-invariant units, so they descend to units and glue trivial line bundles
on the corresponding $U$'s.  This constructs
$\overline{\mathfrak L}$ and an isomorphism

\[
       \pi^*\overline{\mathfrak L}
          \simeq \operatorname{TI}_H(\mathfrak L).
\]

If $\mathfrak L$ is a model of the analytically trivial line bundle, then so
is $\overline{\mathfrak L}$.  To see the point that is sometimes hidden in
this sentence, tensor the given generic trivializations of
$\gamma^*\mathfrak L$.  Their tensor product is an $H$-invariant global
frame of $\operatorname{TI}_H(\mathfrak L)_\eta$.  Relative to each invariant
formal frame $S$ above, its ratio is an invariant analytic unit, hence
descends through the invariant generic-fibre structure sheaf.  The descended
ratios glue to a global frame of $\overline{\mathfrak L}_\eta$ whose pullback
is the tensor-product trivialization.

Zavyalov Theorem 4.4.1 identifies the adic generic fibre of $\mathfrak X$
with the adic quotient of $N$.  Passing to the associated strict Berkovich
space (the maximal Hausdorff/rank-one realization for these taut spaces)
identifies it with the Berkovich affinoid quotient $N/H$; on affinoids this
is also immediate from the invariant algebra.  Thus no ordinary-open claim
is being imported from the adic spectral topology.  Compatibility of model
metrics with pullback gives

\[
 q_N^*h_{\overline{\mathfrak L}}
       =h_{\operatorname{TI}_H(\mathfrak L)}
       =\sum_{\gamma\in H}\gamma^*h_{\mathfrak L}.       \tag{4.1}
\]

After passage to a geometric point with stabilizer $J$, the canonical
$J$-action on the fibre of $\operatorname{TI}_H(\mathfrak L)$ merely
permutes one-dimensional tensor factors, so its stabilizer character is
trivial.  The qualification ``geometric point'' avoids confusing a
stabilizer character with a possible action on the residue field of a
non-geometric point.  More importantly, the invariant-frame construction
above proves descent directly even in wild residue characteristic; no
exactness of invariants is being assumed.

## 5. Proof of the corrected statement

Put $u=q^*g$.  Fix $x\in X$, choose $y\in q^{-1}(x)$, and let
$H=G_y$.  Since the Berkovich affinoid $Y$ is Hausdorff, choose a
$G$-clean ordinary open neighbourhood $C$ of $y$: it is $H$-stable and
its distinct $G/H$-translates are disjoint.  This is the elementary clean
slice in Hansen--Johansson Lemma 5.2.  The quotient topology and invariant
structure sheaf identify

\[
                         C/H\simeq q(C),                 \tag{5.1}
\]

where $q(C)$ is an ordinary open neighbourhood of $x$ in $X$.

Apply Gubler--Jell--Rabinoff Proposition 5.8 to $u$ at $y$.  There are an
ordinary open neighbourhood $U$ of $y$, real numbers $a_1,\ldots,a_m$, and
integral PL functions $h_1,\ldots,h_m$ on $U$ such that

\[
                            u=\sum_{i=1}^m a_i h_i.       \tag{5.2}
\]

By adjoining the zero integral PL function with coefficient zero if
necessary, assume $m\geq1$.

After replacing $U$ by

\[
                         C\cap\bigcap_{\gamma\in H}\gamma U,
\]

it is an $H$-stable ordinary open neighbourhood contained in $C$, and
(5.2) remains valid after restriction.  Choose a strict affinoid
neighbourhood $N_0$ of $y$ inside $U$.  Since $Y$ is separated,

\[
                         N=\bigcap_{\gamma\in H}\gamma N_0
\]

is a strict affinoid domain; because every $\gamma N_0$ is an ordinary
neighbourhood of the fixed point $y$, $N$ is an $H$-stable strict affinoid
**neighbourhood** of $y$.  Let $N^\circ$ be its interior relative to $C$.
It is an $H$-stable ordinary open neighbourhood of $y$.

Restrict the $h_i$ to $N$ and use 4.1 to obtain a common equivariant formal
model $\mathfrak N$ and model line bundles $\mathfrak L_i$.  By 4.2, each

\[
                   \bigotimes_{\gamma\in H}\gamma^*\mathfrak L_i
\]

descends to a model line bundle $\overline{\mathfrak L}_i$ on
$\mathfrak N/H$.  Define on $N/H$

\[
             v:=\frac1{|H|}\sum_{i=1}^m
                    a_i h_{\overline{\mathfrak L}_i}.     \tag{5.3}
\]

This is $\mathbf R$-PL.  By (4.1), (5.2), and the $H$-invariance of $u$,

\[
\begin{aligned}
 q_N^*v
 &=\frac1{|H|}\sum_i a_i\sum_{\gamma\in H}\gamma^*h_i \\
 &=\frac1{|H|}\sum_{\gamma\in H}\gamma^*u
 =u|_N .                                                   \tag{5.4}
\end{aligned}
\]

The quotient $N^\circ/H$ is an ordinary open subset of both $N/H$ and
$C/H$.  Under (5.1), it is an ordinary open neighbourhood of $x$.  Since
$q_N$ is surjective, (5.4) says that the restriction of $v$ there is exactly
$g$.  Thus $g$ is $\mathbf R$-PL on an ordinary open neighbourhood of the
arbitrary point $x$, and hence is $\mathbf R$-PL on $X$.

The only division is by the positive integer $|H|$ in the real coefficient
space.  Nothing is divided in $K$, $K^\circ$, or its residue field.

## 6. Consequences for the rest of the audited note

With the proof of Lemma A replaced by Sections 3--5 above, Theorem B's
finite-quotient step survives.  Its other inputs are Gubler--Rabinoff
Proposition 7.2(6),(7), the already production-verified quasi-smooth P06.1
result, Gubler--Jell--Rabinoff Corollary 5.12 for finite ground-field descent,
and the PL/classical-psh comparison.

Corollary C also survives its quotient step under the stated field-
characteristic hypothesis: if $\operatorname{char}(K)\nmid d$, the finite
diagonalizable kernel becomes a finite constant group after a finite
separable splitting extension.  For an analytic-domain or etale base change,
quotient compatibility is the flat-base-change clause in Zavyalov's quotient
theorems.  This audit has not independently reverified every toroidal phrase,
so the theorem and corollary still require separate hostile and production
verification before live integration.

## 7. Primary-source ledger

1. Walter Gubler, Philipp Jell, and Joseph Rabinoff, *Forms on Berkovich
   spaces based on harmonic tropicalizations*, **Bulletin de la Societe
   Mathematique de France** 154 (2026), 135--238:
   Definition 5.1 (the $G$-local definition), 5.6 (integral PL functions are
   model functions), Proposition 5.8 (ordinary-open decomposition),
   Corollary 5.9 (local model realization), Proposition 5.11 (finite-flat
   descent, deliberately not used here), and Corollary 5.12 (ground-field
   descent).
2. Bogdan Zavyalov, *Quotients of admissible formal schemes and adic spaces
   by finite groups*, **Algebra & Number Theory** 18 (2024), 409--475:
   Remark 3.3.3 (quasi-projective special fibre gives the affine-orbit
   hypothesis), Theorem 3.3.4 (formal quotient, finite map, orbit fibres, and
   invariant local structure), Theorem 4.3.4 (adic quotient), Lemma 4.3.6
   (affinoid neighbourhood of a finite set in a separated rigid space), and
   Theorem 4.4.1 (formal quotient commutes with adic generic fibre).
3. David Hansen and Christian Johansson, *Perfectoid Shimura varieties and
   the Calegari--Emerton conjectures*, **Journal of the London Mathematical
   Society** (2023), DOI 10.1112/jlms.12799: Lemma 5.2 (clean ordinary
   neighbourhood) and Theorem 5.3 (finite rigid quotient).  These support
   (5.1), not the invalid analytic-domain inference in the original proof.
4. Walter Gubler and Florent Martin, *On Zhang's semipositive metrics*,
   **Documenta Mathematica** 24 (2019), 331--372: Proposition 2.10, as cited
   in Gubler--Jell--Rabinoff 5.6.

## 8. Release gate

Before any live integration:

- convert Section 5 to the book's theorem/proof style without an optional
  conventional theorem name;
- have at least two independent audits check the equivariant common-model
  construction and the invariant-frame descent;
- submit the exact statement and proof to production Rethlas with
  `gpt-5.6-sol` at `xhigh`;
- require final/correct/verified and zero errors/zero gaps;
- separately audit Theorem B and Corollary C after replacing their dependency
  on the old proof.
