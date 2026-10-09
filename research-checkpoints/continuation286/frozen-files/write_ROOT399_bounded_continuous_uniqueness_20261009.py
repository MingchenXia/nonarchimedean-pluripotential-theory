from pathlib import Path
R=Path('/workspace/research'); K=R/'root-checks'
source=K/'P16.7-continuation398-local-analytic-divisor-tests-and-pluriharmonic-defects-working-paper-20261009.tex'
target=K/'P16.7-continuation399-bounded-continuous-uniqueness-by-coordinate-curves-working-paper-20261009.tex'
assert not target.exists()
s=source.read_text()
s=s.replace(r'\title{Local analytic divisor tests for bounded solution differences\\and the remaining pluriharmonic recognition gate}',r'\title{Bounded continuous Monge--Ampere uniqueness\\by coordinate curves and Gauss rays}')
a=s.index(r'\begin{abstract}'); b=s.index(r'\end{abstract}',a)+len(r'\end{abstract}')
s=s[:a]+r'''\begin{abstract}
For the specified compact analytic torus quotient, two bounded
continuous potentials in the entire minimal continuous CLD psh sheaf
with the same actual Monge--Ampere measure differ by a constant.
We include the bounded Green argument and divisor testing, then prove
a bounded harmonic Liouville lemma for the analytic multiplicative
group over finite extensions of the actual base field. Finite Galois
descent of signed Radon Laplacians, calibrated Gauss-ray integration,
and density of closed rigid points suffice. Coordinate algebraic
curves then connect the values of the difference; no recognition by
all analytic curves after arbitrary scalar extensions is assumed.
All claims are working claims pending independent review. The result
does not settle unbounded finite-energy uniqueness, finite-energy
compactness, obstacle orthogonality, or general equation existence.
\end{abstract}'''+s[b:]
stop=s.index(r'\section{An exact sufficient recognition criterion}')
bib=s[s.index(r'\begin{thebibliography}'):]
new=r'''
\section{From a divisor-current identity to a curve Laplacian}
We work first in the torus cover $Y=(\mathbb G_m^2)_K^{\rm an}$.
Let $d$ denote the pullback of the bounded continuous difference $u-v$.
The quotient map is a local analytic isomorphism. The divisor identities
proved above therefore hold on the ordinary open torus atlas of $Y$.

Let $P\in K[T]$ be a nonconstant irreducible polynomial with nonzero
constant term. Characteristic zero makes $P$ separable. The smooth,
reduced principal curve
\[
 C_P=\{P(z_1)=0\}\subset Y
\]
is $\mathbb G_{m,L}^{\rm an}$ viewed as a $K$-analytic space, where
$L=K[T]/(P)$. Its closed immersion $j$ is proper. The divisor current
of $P(z_1)$ is exactly $j_*\delta_{C_P}$, with multiplicity one.
For every chartwise continuous dpsh function $d$, continuous
multiplication and pushforward give
\[
 d\,j_*\delta_{C_P}=j_*((j^*d)\delta_{C_P}),\qquad
 \DD(d\delta_{\operatorname{div}P(z_1)})
       =j_*\DD_{C_P}[j^*d].                 \tag{1}
\]
Here $d$ is locally a difference of continuous psh functions because
the smooth reference potential cancels; pullback preserves this
minimal sheaf. The whole continuous projection-formula argument is
CLD8.5.6, extended by linearity; commutation of pushforward and both
differentials is CLD7.7.8. The same identity follows directly by
testing the weighted integration currents, so it does not require
closedness of a continuously weighted divisor current.

On the curve, $\DD_{C_P}[j^*d]$ is locally a difference of positive
scalar currents and thus a signed Radon measure. A proper closed
embedding pushes such a measure by the ordinary measure pushforward.
That pushforward is injective: a Borel set of the closed subspace is
a Borel subset of the ambient space. CLD7.2.8 identifies signed
Radon measures with their scalar currents, using density of compact
smooth functions. Equation(1) and the preceding divisor identity give
\[
                    \DD_{C_P}[d|_{C_P}]=0.                 \tag{2}
\]
This local conclusion glues along the whole noncompact curve.
The same assertion holds for the horizontal curve $z_2=1$.

There is a normalization to record before using(2) over $L$.
The underlying analytic functions and moment maps on $C_P$ are the
same when it is viewed over $K$ or over $L$. CLD14.4.3 states and
proves that its $K$-calibration is $[L:K]$ times its $L$-calibration.
Consequently the corresponding integration currents and Laplacians
have this same positive factor. Vanishing in(2) therefore gives
vanishing for the $L$-analytic curve with its own normalization.
We do not identify these two calibrations without their factor.

\section{Finite Galois base change of a zero signed Laplacian}
\begin{lemma}\label{finitegalois}
Let $L$ be a complete nontrivially valued field of characteristic zero,
let $E/L$ be a finite Galois extension, and let
$\pi:\mathbb G_{m,E}^{\rm an}\longrightarrow\mathbb G_{m,L}^{\rm an}$
be the base-change map. If $h$ is continuous, locally dpsh, and
$\DD[h]=0$, then $\DD[h\circ\pi]=0$ with the canonical
$E$-analytic normalization.
\end{lemma}
\begin{proof}
Pullback preserves continuous psh functions: the assertion holds for
smooth psh generators, pullback preserves locally uniform convergence,
and the inverse-image sheaf minimality proves it at every stage.
Thus $h\circ\pi$ is locally dpsh and
$\mu=\DD[h\circ\pi]$ is a signed Radon measure. It is invariant under
$G=\operatorname{Gal}(E/L)$, since $h\circ\pi$ is invariant and
the isometric automorphisms preserve the canonical calibration.

With the canonical normalization over the varying base field,
CLD15.3.1 and16.1.1 give $\pi_*\delta_{\mathbb G_{m,E}}
=\delta_{\mathbb G_{m,L}}$. Bounded continuous multiplication
locally on a compact test support therefore gives
\[
 \pi_*[h\circ\pi]=[h],\qquad
 \pi_*\mu=\DD\pi_*[h\circ\pi]=\DD[h]=0.        \tag{3}
\]
For clarity, if the source is instead viewed as an $L$-analytic
finite cover, its calibration is multiplied by $[E:L]$ and both
equalities acquire that factor. Either convention proves the same
vanishing. We use the varying-base convention in(3).

Every fibre of $\pi$ is a single $G$-orbit. Indeed it is the spectrum
of the finite etale algebra $\mathscr H(x)\otimes_L E$, a product
of finite field extensions of the complete field $\mathscr H(x)$.
The Galois group permutes its factors transitively: its invariant
algebra is $\mathscr H(x)$, which has no nontrivial idempotent.
Each factor has a unique extending absolute value and contributes
one analytic point. The finite proper surjective map $\pi$ is closed,
hence a topological quotient.

For $\varphi\in C_c(\mathbb G_{m,E}^{\rm an})$ put
$\overline\varphi=|G|^{-1}\sum_{\sigma\in G}\varphi\circ\sigma$.
It is continuous, compactly supported, and constant on each fibre,
so it descends to $\psi\in C_c(\mathbb G_{m,L}^{\rm an})$.
Invariance of $\mu$ and(3), interpreted as signed measures through
CLD7.2.8, imply
\[
 \int\varphi\,d\mu=\int\overline\varphi\,d\mu
                      =\int\psi\,d(\pi_*\mu)=0.
\]
Hence $\mu=0$. This proves only the stated finite Galois passage;
no unrestricted pullback theorem for distributional currents is used.
\end{proof}

\section{Gauss-ray Liouville lemma}
\begin{lemma}\label{liouville}
Let $L$ be a complete nontrivially valued field of characteristic zero.
A bounded continuous locally dpsh function $h$ on
$\mathbb G_{m,L}^{\rm an}$ with $\DD[h]=0$ is constant.
\end{lemma}
\begin{proof}
Write $\eta_{a,r}$ for the Gauss point of the closed disk centred at
$a$ with radius $r>0$; its polynomial norm is
$\left|\sum b_i(z-a)^i\right|=\max_i|b_i|r^i$.
Put $H_0(t)=h(\eta_{0,e^{-t}})$ for $t\in\mathbb R$.
For $\phi\in C_c^\infty(\mathbb R)$ the function
$\phi(-\log|z|)$ is smooth with compact support in a closed annulus
inside $\mathbb G_m$. The canonical one-dimensional torus calibration
and integration give
\[
 0=\langle\DD[h],\phi(-\log|z|)\rangle
       =\int_{\mathbb R} H_0(t)\phi''(t)\,dt.       \tag{4}
\]
This is the ordinary calibrated torus moment $z$, of degree one:
$\DD\phi(t)=\phi''(t)d't\wedge d''t$ and its scalar measure is
the pushforward of $\phi''(t)dt$ by the Gauss section. This follows
directly by integrating the one-dimensional calibrated cell; there
is no multiplicity from a larger ground field in the $L$-normalization.
The section and its norm formula are CLD12.1.2,12.1.5.
Equation(4) makes $H_0$ affine as a distribution on $\mathbb R$.
Continuity identifies it with that affine function; boundedness
forces its slope to vanish. Denote its constant value by $c$.

Take $a\in L^*$. On the punctured disk $0<|z-a|<|a|$ the coordinate
$z-a$ is a unit and the disk is contained in $\mathbb G_m$.
The same degree-one annulus calculation, with compact test support,
makes
\[
 H_a(t)=h(\eta_{a,e^{-t}}),\qquad t>-\log|a|,
\]
affine on this half-line. Boundedness as $t\to+\infty$ forces slope
zero. As $r\downarrow0$, $\eta_{a,r}$ converges to the rational
point $a$; this follows from the displayed polynomial norm and the
initial seminorm topology. As $r\uparrow|a|$, it converges to
$\eta_{a,|a|}=\eta_{0,|a|}$. The equality follows by expanding
polynomials at either centre and applying the ultrametric inequality
in both directions. Continuity now gives $h(a)=c$.

A closed rigid point $x$ of $\mathbb G_{m,L}^{\rm an}$ has finite
residue field over $L$. Choose a finite Galois normal closure $E/L$
of that residue field; characteristic zero supplies separability.
Lemma\ref{finitegalois} applies to $h_E=h\circ\pi$. Its Gauss
section at zero projects to the original Gauss section by the norm
formula (also CLD12.1.8(a)). Thus the constant in its Gauss-ray
calculation is the same $c$. A lift of $x$ is an $E$-rational point,
and the previous paragraph proves $h(x)=c$.

We justify the density used to finish the proof. Every nonempty
ordinary open subset of the strict analytic torus contains a
nonempty strict rational affinoid domain: move finite absolute-value
bounds inward while keeping a chosen point inside and replace their
endpoints by elements of $|L^*|^{\mathbb Q}$; that group is dense
since the valuation is nontrivial. Integral powers realize these
constraints with scalars in $L$, using the common-denominator
unit-ideal construction given above. A compact polyannulus containing
the construction can likewise be given a strict presentation by
integral powers. The resulting nonzero strict affinoid algebra has
a maximal ideal. The Tate Nullstellensatz gives a finite residue
extension of $L$, with its unique absolute value, and therefore a
closed rigid analytic point in that domain. Here the Nullstellensatz
is the named ordinary affinoid foundation; Van der Put1.6 records
the exact finite-residue statement, and Papikian3.2(d) corroborates it.
Their short immediate passages do not contain a whole proof of
Weierstrass preparation. No fresh proof of that deeper result is claimed.
Closed rigid points are therefore dense. Since $h$ is continuous and
equals $c$ on them, it is identically $c$.
\end{proof}

\section{Coordinate fibres prove bounded uniqueness}
\begin{theorem}\label{boundedunique}
On the compact analytic quotient specified in the first section, let
$u,v\in\mathcal C$. If their actual recursively defined measures
$\MA(u)$ and $\MA(v)$ agree, then $u-v$ is constant pointwise on $X$.
\end{theorem}
\begin{proof}
The difference pulled back to $Y$ is bounded and continuous.
Equations(1)--(2) and the calibration comparison show that its
restriction to every vertical $C_P\cong\mathbb G_{m,L}^{\rm an}$
is locally continuous dpsh with zero Laplacian over $L$.
Lemma\ref{liouville} makes each such restriction constant.
The same lemma on the horizontal $K$-curve $z_2=1$ makes its
restriction a single constant $c$ there.

Let $y$ be any closed rigid point of $Y$. Its coordinates have values
$(a,b)$ in a finite extension $E/K$. Let $P$ be the minimal polynomial
of $a$ over $K$ and $L=K(a)$. Then $y$ lies on $C_P$.
The point $(a,1)$ of that curve lies also on $z_2=1$ and has value
$c$. Constancy on $C_P$ therefore gives $d(y)=c$, irrespective of
whether $b$ lies in $L$ or in a larger finite extension. This uses
the entire $L$-analytic curve, not just its $L$-rational points.

Closed rigid points are dense in $Y$ by the same strict rational
domain and Nullstellensatz argument in dimension two.
Continuity gives $d=c$ on all of $Y$. The surjective quotient map
then gives $u-v=c$ on all of $X$.
\end{proof}
The proof of Theorem\ref{boundedunique} needs only the Laurent
divisor tests, although the full local holomorphic divisor extension
has also been retained above. General curve recognition, normalization
of arbitrary curve images, and infinite scalar extension are not
premises of the coordinate-fibre proof.

\section{Exact reading scope and original residual}
The whole mathematical body of the earlier working paper398 through
its local analytic divisor theorem has been included above. The new
steps are the injective scalar-measure passage on coordinate curves,
the finite Galois averaging argument with the explicit normalization,
the Gauss-ray calculation, and the pointwise coordinate-fibre connection.
All of these working claims are UNREVIEWED.

For CLD the retained whole v2 body has SHA256
\texttt{64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085}.
The entire immediate applied8.5.6 projection proof,7.2.8 scalar measure
proof,7.7.8 differential commutation passage,14.4.3 calibration
comparison,15.3.1 base-change integration proof,16.1.1 current proof,
and12.1.2/5/8(a) Gauss norm passages were freshly read in bounded
literal-LF chunks. The whole immediate Poincare--Lelong statement
and proof16.7.3 were already freshly read for398. Whole primary source
bodies, exact literal units and actual pixels remain local; the public
record reports their bindings and qualifications. Whole8.6.7 was read
but its arbitrary continuous multiplier closedness is not a premise.
The Van der Put actual original PDF page3 (printed J7-02), including
the finite-residue statement1.6 and its immediate reference to1.2,
was freshly viewed; the entire deeper normalization proof1.2 is not
claimed newly audited. Its pages5--6, containing the whole2.2 rational
presentation argument, were freshly viewed for398. Papikian3.2 is
corroborating statement evidence, with no complete immediate proof
printed there. Bounded proofreading is not an audit of every recursive
source dependency. Ordinary affinoid foundations remain explicit.

Bounded continuous uniqueness is the scope of
Theorem\ref{boundedunique}. Original P16.7 still requires much more:
intrinsic recognition of unbounded generated finite-energy functions,
integration and pointwise restrictions outside bounded strata,
actual compactness of finite-energy sublevels, obstacle envelopes and
orthogonality, existence for every eligible arbitrary-support measure,
and uniqueness for the full unbounded equation domain. None of these
is established by a Liouville lemma whose proof uses boundedness.
No original catalogue item is closed and no accepted-paper count is
increased. New papers398--399 were not supplied as hot feedback to
the independently running native278--279 campaigns; their frozen
inputs and criteria remain unchanged.
'''
target.write_text(s[:stop]+new+'\n'+bib)
print(str(target))
