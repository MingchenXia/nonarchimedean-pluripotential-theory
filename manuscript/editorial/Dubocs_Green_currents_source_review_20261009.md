# Model Green currents: valid elementary constructions and the blowup interface

Date: 9 October 2026. This is a source checkpoint following the verified
4,651-page edition, with no change to the active manuscript or catalogue.
The exact source is Léo Dubocs, *Non-archimedean Green currents for the
zero-locus of a regular section*, arXiv:2606.19160v1, posted 17 June 2026
and internally dated 18 June. Its 27-page PDF has SHA256
c732d21846bb4e4827a864c23be232da2af084a887e86fb706110d28a7251b7a.

All 27 physical pages were read with their complete extracted text and
14 individually displayed matching rendered images, in source order.
Fourteen sequential notes and receipts bind the PDF, texts and images.
Preparation flags remain false; preparation, export and upload add no
reading credit. The full source reading straddles the UTC date boundary
from 8 to 9 October; the acquisition/view directory retains its original
8 October name. No new complete book pass is claimed.

The main distinction is between the source's algebraic model-Chow currents
and CLD analytic currents. A second distinction is between a regular
section, whose components form a regular sequence, and a smooth zero scheme.
The general higher-rank formula is not imported in this checkpoint:
its printed proof uses the inverse Poincaré duality of a blowup that has
not been shown regular. This is a gap in the stated framework and proof,
not a counterexample to an intended Green identity after a valid additional
resolution or extension construction.

## The precise category

Section 1 works over the fraction field $K$ of an excellent DVR $R$.
The generic variety is proper smooth over $K$. Its models are **regular,
proper, flat** $R$-schemes with that exact generic fibre. Existence and
common domination of the required regular models are standing hypotheses;
resolution of excellent $R$-schemes is a sufficient stronger premise.
These assumptions must accompany every use of the model current groups.

For a pure $n$-dimensional generic variety, the four groups use different
Chow types and transitions:

| Group | Model group | Transition for a dominating model map |
| --- | --- | --- |
| $A_c^{k,k}$ | operational $\mathrm{CH}^k(\mathcal X_0)$ | pullback $\pi_0^*$ in a colimit |
| $\widetilde A^{k,k}$ | $\mathrm{CH}_{n-k}(\mathcal X_0)$ | refined pullback $\pi_0^!$ in a colimit |
| $D_c^{k,k}$ | operational $\mathrm{CH}^k(\mathcal X_0)$ | proper operational pushforward $\pi_{0!}$ in an inverse limit |
| $\widetilde D^{k,k}$ | $\mathrm{CH}_{n-k}(\mathcal X_0)$ | proper cycle pushforward $\pi_{0*}$ in an inverse limit |

Poincaré duality $E_{\mathcal X}$ is available on the regular total model,
not automatically on its possibly singular special fibre. The differential
is the algebraic composition

$$
dd^c=i^*\circ E_{\mathcal X}^{-1}\circ i_*.
$$

For a codimension-$k$ cycle $Z$ on the generic fibre, its integration current
has component $i^*E_{\mathcal X}^{-1}[\overline Z]$. This uses the scheme
cycle, retaining multiplicities. A model operational form can multiply a
current. The construction supplies no product of two arbitrary currents,
no natural restriction of these currents to an arbitrary open generic
variety, and no comparison map to CLD test-form functionals.

Proposition 1.3 and Lemma 1.4 give the projection and $dd^c$ pushforward
identities for morphisms of **proper smooth** generic schemes, using
compatible regular models and the stated bivariant hypotheses. The proof's
Fulton/BGS axioms are attributed classical inputs. They have not been
recursively reread in this checkpoint.

## Metrics and the safe rank-one identity

Definition 2.1 uses a vector-bundle model, identified after pullback to
common models. It does not define every continuous analytic metric.
The induced and quotient metrics use the locally free flattening of a
generic quotient on a suitable dominating model. The operational Chern
forms then satisfy exact Whitney multiplicativity on the common model.
This explains the absence of the complex Bott–Chern correction in this
particular model category; it does not remove such a correction from an
analytic vector-bundle construction.

For a line bundle with such a model metric and a nonzero Cartier section,
Definition 2.5 takes the vertical part of the divisor of its meromorphic
model extension. Its sign is explicitly opposite to BGS95's
$\operatorname{div}_\nu$. Proposition 2.6 proves

$$
dd^c\operatorname{div}_v(s)+\delta_{\operatorname{div}(s)}
=[c_1(\mathcal L)].
$$

The proof cancels the horizontal closure and uses
$c_1(\mathcal L)\cap[\mathcal X]=[\operatorname{div}(s_{\mathcal X})]$.
Uniformizer rescaling changes the vertical current but its total principal
divisor has zero Chow class, so its $dd^c$ vanishes. These are supported
rank-one model calculations in their exact hypotheses.

The source calls the vertical current an analog of $[-\log\|s\|^2]$.
For the elementary normalization $v(t)=1$, $|t|=e^{-1}$, the values of
$-\log|t|$ and $-\log|t|^2$ are respectively 1 and 2. A comparison also
requires the respective $dd^c$ normalizations and an actual current map;
the norm-square observation alone does not fix a CLD comparison.
No such map is proved in the source. The book's minus-log conventions
therefore remain unchanged.

## What the minimum and gluing constructions actually prove

For top-dimensional special-fibre cycles, $\mathrm{CH}_n=\mathrm Z_n$.
A proper birational morphism to a regular total model has a unique
codimension-one strict transform above each target divisor, with residue
degree one. Contracted divisors push forward to zero. Thus coefficientwise
minimum commutes with the transition pushforward:

$$
\pi_{0*}\min(\alpha,\beta)
=\min(\pi_{0*}\alpha,\pi_{0*}\beta).
$$

This defines a minimum on $\widetilde D^{0,0}$, not on every degree.
Two distinct $k(x)$-rational points on an exceptional projective line give
the source's higher-degree failure: their coefficientwise minimum is zero,
while both pushforwards are $[x]$. Arbitrary closed points would need their
residue-degree factors.

The model-open gluing construction requires actual overlap-compatible
cycles on every dominating model and local compatibility with proper
pushforward. It uses open restriction/proper pushforward base change at
the cycle level. The source explicitly declines to interpret it as
restriction to generic opens.

For a vector section, the local coefficient at a vertical DVR is
$\min_j\operatorname{ord}_V(f_j)$. Integral transition matrices and their
inverses prove frame independence. Use $\operatorname{ord}(0)=+\infty$
when a component vanishes identically. This gives the section-ideal
current on the original proper smooth variety. It is not a psh envelope,
an arbitrary-current minimum, or analytic weak-psh descent.

## The higher-rank blowup formula and its unprovided regularity

Sections 4–6 use a regular rank-$r$ section $\sigma$ of $F$ with zero
scheme $Z$. With the convention
$\mathbf P(F)=\operatorname{Proj}\operatorname{Sym}(F^\vee)$, the
blowup embeds into $\mathbf P(F)$, and the tautological line pulls back
to $\mathcal O(E)$. The canonical section $s$ maps to $\pi^*\sigma$
under this line's inclusion into $\pi^*F$; they are not untyped sections
of the same rank-$r$ bundle.

The announced Green current is

$$
\Lambda=\pi_*\bigl(\operatorname{div}_v(s)
       \wedge f^*c_{r-1}(Q_F)\bigr),\qquad
dd^c\Lambda+\delta_Z=[c_r(F)].
$$

The printed proof uses the raw model blowup
$\widetilde{\mathcal X}=\operatorname{Bl}_J\mathcal X$, where $J$
is generated by the extended section. Identifying its generic fibre
with $\operatorname{Bl}_Z X$ does **not** establish the regularity required
by the model definition. Physical page 19 explicitly applies
$E_{\widetilde{\mathcal X}}^{-1}$ and the bivariant pushforwards to this
raw blowup. No later section supplies a regularization or extends the
current framework to singular generic varieties.

There are two separate elementary diagnostics.

1. Take $K=\mathbf Q((t))$, $X=\mathbf P^2_K$,
   $F=\mathcal O(2)\oplus\mathcal O(2)$ and
   $\sigma=(X^2,Y^2)$. Around $[0:0:1]$, the ideal
   $(x^2,y^2)$ is a regular sequence; its quotient has basis
   $1,x,y,xy$ and length four. A generic blowup chart is
   $$K[x,y,u]/(y^2-ux^2).$$
   At $(x,y,u)=(0,0,1)$ all partial derivatives vanish. In local coordinates
   $w=u-1$, the equation is $y^2-(1+w)x^2$, with no linear term.
   The local ring has dimension two and embedding dimension three, so it
   is singular. A regular $R$-scheme cannot have this exact generic
   fibre, because regularity localizes. Cofinality asserted only for
   proper smooth generic schemes does not cover it.
2. Even with a smooth generic centre, the **particular total blowup**
   can be singular. On $\mathbf P^2_{\mathbf Q[[t]]}$, take the model
   section $(tX,Y)$ of $\mathcal O(1)\oplus\mathcal O(1)$.
   Generically its ideal is $(x,y)$ and its blowup is smooth.
   One raw total chart is
   $$\mathbf Q[[t]][x,y,v]/(tx-vy).$$
   At $(t,x,y,v)=(0,0,0,0)$ its dimension is three and its embedding
   dimension four. Inverting $t$ solves $x=vy/t$, confirming that this
   defect is in the total model. A suitable regular dominating model
   must actually be constructed before applying its Poincaré duality.

A possible repair would replace the singular generic blowup by a suitable
proper smooth principalization, construct compatible regular total models
and induced metrics, and prove the exceptional cycle and pushforward
identities on that new system. This is a **research route**, not a completed
repair or a new general theorem here. Requiring a smooth centre addresses
the first diagnostic but does not by itself regularize the raw total model.

Under a valid model computation, Lemma 4.3's exceptional-closure argument
uses the regular generic sequence's linear-type relations and contraction
of the ideal after inverting the uniformizer. The projective-bundle Segre
formula then leaves the $k=r-1$ term. The classical algebraic inputs are
attributed, and their intended computation is distinguished from the
missing admissible model.

## Split metrics, Levine coefficients and the proper/global limitation

For $F=L^{\oplus r}$ with a genuinely split model metric, set
$\alpha=\pi^*c_1(L)$ and
$\beta=f^*q^*c_1(\mathcal O_{\mathbf P^{r-1}}(1))$. The coefficient
calculation in Theorem 6.1 is elementary:

$$
\sum_{j=k}^{r-1}
\binom r{r-1-j}\binom jk(-1)^{j-k}=1,\qquad 0\leq k\leq r-1.
$$

The displayed derivative on physical page 26 omits $(-1)^k$:

$$
\sum_{j\geq k}\binom jk z^j(-1)^{j-k}
=\frac{z^k}{k!}(-1)^k
  \frac{d^k}{dz^k}(1+z)^{-1}
=\frac{z^k}{(1+z)^{k+1}}.
$$

Inserting the sign gives the stated final coefficient identity. The local
sign slip does not refute that identity. The geometric Levine formula
still inherits the blowup/current gap in the general stated scope.
The coordinate-linear projective example has a smooth generic centre
and standard regular blowup models; it illustrates better-controlled
geometry without proving every regular-section case.

Corollary 6.2's trivial-bundle Martinelli specialization retains proper $X$
and **global regular** components. On a proper integral variety,
$H^0(X,\mathcal O_X)$ is a finite field extension of $K$, so every nonzero
global function is a unit. A regular section of $\mathcal O_X^{\oplus r}$
for $r>0$ cannot have all components zero; thus its zero scheme is empty.
The same reasoning applies componentwise. The displayed identity does
not supply a nontrivial affine local Martinelli theorem. Such a theorem
would need additional local-current constructions, which the paper
explicitly does not provide.

## Local notation corrections and retained dependencies

| Physical page | Printed issue | Precisely limited reading |
| --- | --- | --- |
| 4 | undefined Martinelli exponent $p-1$ | $r-1$, as in Section 6 |
| 9 | a composition in Lemma 1.4 has the wrong order | $g\circ j=i\circ g_0$ |
| 11 | Chern operators called ordinary Chow classes | retain the operational interpretation |
| 14 | arbitrary closed exceptional points pushed to $[x]$ | choose $k(x)$-rational points, or retain residue degrees |
| 19 | equation (11) fixes $r-1$ on the left but branches in $k$ | retain general $k$ on that intermediate left side |
| 19 | undefined $\delta_Y$ | $\delta_Z$ |
| 20 | blowup structure sheaf used as a graded polynomial quotient | interpret the Rees presentation before taking Proj |
| 21 | $\pi^*\sigma=s$ between different bundle types | use the tautological-line inclusion with induced metric |
| 23 | symmetric algebra uses $F$ rather than $F^\vee$ | use the dual as in Section 4 |
| 23 | divisor of a homogeneous coordinate $x_j$ on the $x_k$ chart | divisor of the dehomogenized ratio $x_j/x_k$ |
| 26 | missing differentiation sign | insert $(-1)^k$ as above |

These local corrections are distinct from the substantive model/generic
regularity issue. The earlier BGS95, Fulton98, Raynaud–Gruson71,
resolution, and complex BGS94 inputs are not recursively certified by
this source reading. No author contact is made.

Six exact diagnostic families pass: singular generic blowup, singular
raw total model with smooth generic fibre, typed minimum/pushforward,
DVR frame invariance, split Chern coefficients/sign, and supported
coordinate/normalization/proper-global boundaries. The first diagnostic
helper failed before producing output because SymPy was given a Python
integer where it expected a symbolic expression. It remains frozen;
fresh v2 uses the symbolic integer and passes. This helper failure changes
no mathematical conclusion or reading credit.

The 4,651-page book, all 425 core TeX inputs, both bibliographies and the
native catalogue/editor remain unchanged at this checkpoint. The 42
canonical atoms and twelve formal problems keep their statuses. General
BJ22 critical homogeneous Siu/envelope bridges remain OPEN; LPWZ density
remains UNVERIFIED. The warning concerning BJ22 Theorem 6.21 remains
binding. The last complete ordered whole-book pass is 4 October.
No original general theorem or independent gpt-6.1-sol xhigh receipt
is asserted.
