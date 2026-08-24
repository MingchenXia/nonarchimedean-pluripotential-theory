# Exact Rethlas input: pseudoeffective MP--DXZ chapter

Source: `nonarchimedean_pluripotential_theory/manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex`

Verification instruction: audit every block below exactly as written, including all hypotheses, extended-real conventions, order directions, endpoint claims, and source interfaces. A block passes only if its full stated conclusion follows from its displayed proof and the dependency ledger. In particular, reject any hidden upgrade from \(\mathcal I\)-equivalence to \(P\)-equivalence, from rational divisorial points to arbitrary semivaluations, or from an injective realization to a bijection.

## Dependency ledger

- MP24, Definitions 2.5.1 and 4.1.2; Remark 2.5.2; Definition 4.3.1; Theorems 4.3.8, 5.1.4, and 5.1.7.
- DXZ23, Proposition 3.1; Definition 3.3; Theorems 3.14 and 3.17; formula (43).
- Xia23Operations, Definitions 2.3, 2.6, 2.7, 4.1, 4.3, 4.5, 4.7, 4.9, 4.11, and 4.12; Lemmas 4.2, 4.10, and 4.17; Corollary 4.8; Theorem 4.13.
- BFJ08, Theorem A, together with GZ15 strong openness, for recovery of exact multiplier ideals from divisorial generic Lelong numbers.
- BBJ21, Lemma B.4, for asymptotic divisorial orders of multiplier ideals.
- Darvas--Di Nezza--Lu, Theorem 1.1, for unrestricted monotonicity of total
  nonpluripolar mass (the earlier BEGZ theorem only covered small unbounded
  locus).
- The relative Kodaira criterion for projective morphisms.
- Internal imported results: `prop:va-gauss-identity`, `thm:tna-positive-volume`, `cor:tna-positive-no-ambiguity`, `thm:mp-maximal-ray`, `thm:comp-dxz`, `thm:ts-algebraic-recovery`, and `thm:ch21-continuous-zhang`.

## Global hypotheses and scope (verbatim)

```latex
\chapter{Pseudoeffective classes and ideal-valuative realizations}
\label{chap:pseff-mp-dxz}
\index{pseudoeffective class!ideal-valuative realization}
\index{comparison!Mesquita--Piccione--Darvas--Xia--Zhang}

The tropical spectrum \(X^{\bethan}\) is attached to the coherent ideals
of \(X\), independently of a positivity class.  Positivity enters later and
in two different ways.  Mesquita--Piccione use relatively nef
cohomological models and assume that the background class is K\"ahler.
Darvas--Xia--Zhang instead attach an inverse system of positive-mass test
curves to every pseudoeffective class.  The purpose of this chapter is to
put the inverse-system data on the tropical spectrum without identifying
objects that the existing theories do not identify.

Throughout, \(X\) is a connected compact K\"ahler manifold of dimension
\(n\), \(\theta\) is a smooth closed real \((1,1)\)-form, and
\[
                    \alpha:=\{\theta\}
       \in H^{1,1}_{\mathrm{BC}}(X,\mathbf R)
\tag{71.1}\label{eq:pseff-background}
\]
is pseudoeffective.  The smoothness of \(X\) is used for multiplier ideals,
their valuative characterization, and strong openness.  The DXZ space
\(\PSH^{\NA}(X,\theta)\) is the inverse system constructed in
\Cref{chap:transcendental-metrics}.  The MP space \(X^{\bethan}\), its
semivaluations, and its divisorial locus were constructed in
\Cref{chap:tropical-spectra-complex,chap:mp-dual-complexes}.

There are three conclusions to keep separate.
\begin{enumerate}
\item Every DXZ metric has a canonical ideal-valuative function on all of
      \(X^{\bethan}\).
\item The function is independent of the K\"ahler perturbation and is
      injective as a representation of the DXZ metric.
\item Outside the finite-energy K\"ahler locus and the projective rational
      locus, it is not proved that this function belongs to an MP psh cone,
      and no surjectivity theorem is asserted.
\end{enumerate}
The third clause is part of the result, not a temporary omission.

```

## Required definitions and firewalls (verbatim)

### Ideal-valuative definitions and the P--I firewall

```latex
Let \(v\in X^{\bethan}\).  For a coherent ideal sheaf \(\mathfrak a\),
we use the convention
\[
 v(\mathfrak a):=\min\{v(f):f\text{ is a local generator of }
 \mathfrak a\text{ at the centre of }v\}.
\tag{71.6}\label{eq:pseff-ideal-value}
\]
The value is independent of the generators.  It lies in
\([0,+\infty]\), and it is allowed to be infinite.  If \(\varphi\) is a
quasi-psh function on \(X\), set
\[
 \nu_v^{\mathcal I}(\varphi)
 :=\lim_{m\to\infty}\frac{1}{m}
      v\bigl(\mathcal I(m\varphi)\bigr).
\tag{71.7}\label{eq:pseff-ideal-valuative-number}
\]

\begin{proposition}\label{prop:pseff-ideal-valuative-basic}
The limit in \eqref{eq:pseff-ideal-valuative-number} exists in
\([0,+\infty]\), and
\[
 \nu_v^{\mathcal I}(\varphi)
 =\sup_{m\geq1}\frac{1}{m}
      v\bigl(\mathcal I(m\varphi)\bigr).
\tag{71.8}\label{eq:pseff-fekete-formula}
\]
For \(s\geq0\), one has
\(\nu_{sv}^{\mathcal I}(\varphi)=s\nu_v^{\mathcal I}(\varphi)\), with
the usual extended-real convention.  If
\(v=r\ord_E\), where \(E\) is a prime divisor over \(X\) and
\(r>0\), then
\[
             \nu_{r\ord_E}^{\mathcal I}(\varphi)
             =r\nu_E(\varphi).
\tag{71.9}\label{eq:pseff-divisorial-lelong}
\]
\end{proposition}

\begin{proof}
The subadditivity theorem for multiplier ideals gives
\[
 \mathcal I((m+\ell)\varphi)
 \subseteq\mathcal I(m\varphi)\mathcal I(\ell\varphi).
\tag{71.10}\label{eq:pseff-multiplier-subadditivity}
\]
Since inclusion reverses ideal values and \(v(\mathfrak a\mathfrak b)
=v(\mathfrak a)+v(\mathfrak b)\), the sequence
\(b_m:=v(\mathcal I(m\varphi))\) is superadditive.  Fekete's lemma,
valid also with the value \(+\infty\), proves
\eqref{eq:pseff-fekete-formula}.  Homogeneity follows first at every
finite stage from \((sv)(\mathfrak a)=s v(\mathfrak a)\), and then by
taking the supremum.  Finally, the asymptotic divisorial order of the
multiplier ideals is the generic Lelong number:
\[
 \lim_{m\to\infty}m^{-1}\ord_E\mathcal I(m\varphi)
 =\nu_E(\varphi).
\]
This is \cite[Lemma~B.4]{BBJ21}, and multiplying by \(r\) proves
\eqref{eq:pseff-divisorial-lelong}.
\end{proof}

The next statement records precisely how much singularity data
\eqref{eq:pseff-ideal-valuative-number} remembers.

\begin{proposition}\label{prop:pseff-i-equivalence-valuative}
For quasi-psh functions \(\varphi\) and \(\psi\) on the smooth manifold
\(X\), the following conditions are equivalent:
\begin{enumerate}
\item \(\mathcal I(m\varphi)=\mathcal I(m\psi)\) for every integer
      \(m\geq1\);
\item \(\nu_E(\varphi)=\nu_E(\psi)\) for every prime divisor \(E\)
      over \(X\);
\item \(\nu_v^{\mathcal I}(\varphi)=\nu_v^{\mathcal I}(\psi)\) for
      every divisorial semivaluation \(v=r\ord_E\).
\end{enumerate}
Consequently these conditions are equivalent to
\(\mathcal I\)-equivalence in the sense of
\cite[Definition~2.7]{Xia23Operations}.
\end{proposition}

\begin{proof}
The first condition implies the third by
\eqref{eq:pseff-ideal-valuative-number}, and the third is equivalent to
the second by \eqref{eq:pseff-divisorial-lelong}.  Suppose now that the
second condition holds.  The valuative characterization of multiplier
ideals in \cite[Theorem~A]{BFJ08} characterizes the upper-regularized
ideal \(\mathcal I_+(m\varphi)\) by inequalities involving precisely the
numbers \(\nu_E(\varphi)\) and the log discrepancies \(A_X(E)\).
Hence
\(\mathcal I_+(m\varphi)=\mathcal I_+(m\psi)\) for every \(m\).
Strong openness \cite{GZ15} gives
\(\mathcal I_+(m\varphi)=\mathcal I(m\varphi)\), and likewise for
\(\psi\), proving the first condition.  Finally,
\cite[Definition~2.3]{Xia23Operations} defines the
\(\mathcal I\)-envelope by equality of all the integer multiplier ideals;
its normalized fixed points are therefore classified by the same data.
This is exactly the equivalence relation of
\cite[Definition~2.7]{Xia23Operations}.
\end{proof}

\begin{warning}{The \(P\)-versus-\(\mathcal I\) firewall}
\label{warn:pseff-p-i-firewall}
The transform below records multiplier ideals, hence
\(\mathcal I\)-equivalence.  It must not be used to identify arbitrary
\(P\)-equivalence classes.  The two relations agree at an
\(\mathcal I\)-good positive-mass potential, where by definition
\[
                  P_\eta[\varphi]
                  =P_\eta[\varphi]_{\mathcal I},
\tag{71.11}\label{eq:pseff-i-good-firewall}
\]
but no such identity is asserted outside that locus.  In particular, a
future theory sensitive to movable mass may have to retain more data than
the function in \eqref{eq:pseff-ideal-valuative-number}.
\end{warning}

```

### One-curve transform definitions

```latex
Let \(\eta\) be a smooth closed real \((1,1)\)-form with big class, and
let
\(\Gamma=(\Gamma_\tau)\in\PSH^{\NA}(X,\eta)_{>0}\) be a DXZ
\(\mathcal I\)-model positive-mass test curve.  Write
\(c:=\Gamma_{\max}\).  Thus the interior levels
\(\Gamma_\tau\), \(\tau<c\), are normalized
\(\mathcal I\)-model potentials.  Define
\[
 \mathfrak T_\Gamma(v)
 :=\sup_{\tau<c}
       \{\tau-\nu_v^{\mathcal I}(\Gamma_\tau)\}
 \in[-\infty,c]
 \qquad (v\in X^{\bethan}).
\tag{71.12}\label{eq:pseff-test-curve-transform}
\]
For \(b>0\), it is convenient to homogenize this function by
\[
 \widehat{\mathfrak T}_\Gamma(v,b)
 :=b\mathfrak T_\Gamma(b^{-1}v)
 =\sup_{\tau<c}
       \{b\tau-\nu_v^{\mathcal I}(\Gamma_\tau)\}.
\tag{71.13}\label{eq:pseff-homogeneous-transform}
\]

```

### Radial and rational Gauss conventions

```latex
\section{The radial convention and rational Gauss weights}

We now fix one convention for the rest of the chapter.  The radial
variable is
\[
                         t=-\log|z|^2.
\tag{71.19}\label{eq:pseff-radial-convention}
\]
The inverse Legendre transform of \(\Gamma\) is
\[
 u_t:=\uscsup[\tau<c]\{\Gamma_\tau+t\tau\},
 \qquad t\geq0.
\tag{71.20}\label{eq:pseff-inverse-legendre}
\]
On \(X\times\Delta^*\), write
\(U(x,z):=u_{-\log|z|^2}(x)\).  If \(q>c\), then
\[
 W_q(x,z):=U(x,z)+q\log|z|^2
          =u_t(x)-qt
\tag{71.21}\label{eq:pseff-shifted-radial-potential}
\]
extends as a quasi-psh function across \(X\times\{0\}\).

Let \(v=r\ord_E\), with \(r\in\mathbf Q_{>0}\), and let
\(b\in\mathbf Q_{>0}\).  Its weight-\(b\) Gauss extension is
\[
 \sigma_{v,b}\!\left(\sum_{j\geq0}f_jz^j\right)
 :=\min_j\{v(f_j)+bj\}.
\tag{71.22}\label{eq:pseff-weighted-gauss}
\]
It is a rational divisorial valuation over \(X\times\Delta\), after a
common resolution and a ramified base change.  In particular the generic
Lelong number \(\nu_{\sigma_{v,b}}(W_q)\) is defined.  Our normalization is
\[
                  \nu_{\sigma_{v,b}}(\log|z|^2)=b.
\tag{71.23}\label{eq:pseff-gauss-log-normalization}
\]

```

### Inverse-system transform setup

```latex
\section{Passage to a pseudoeffective class}

Let now
\(\boldsymbol\Gamma=(\Gamma^{\theta+\omega})_\omega\in
\PSH^{\NA}(X,\theta)\) be a compatible DXZ inverse-system metric as in
\Cref{def:tna-pshna}.  The common endpoint is denoted by
\(c=\boldsymbol\Gamma_{\max}\).  Choose any K\"ahler perturbation
\(\omega\), and set
\[
 \mathfrak T_{\boldsymbol\Gamma}(v)
 :=\sup_{\tau<c}
   \{\tau-\nu_v^{\mathcal I}
       (\Gamma^{\theta+\omega}_\tau)\}.
\tag{71.27}\label{eq:pseff-inverse-system-transform}
\]

```

### Finite ideal approximants

```latex
\section{Divisorial piecewise-linear approximation}

The transform can be approached by finite ideal data, but the order of the
two limits matters.  Fix a perturbation component and a finite set
\(T\subset(-\infty,c)\).  For \(M\geq1\), put
\[
 a_{\tau,M}(v)
 :=\max_{1\leq m\leq M}
      \frac1m v\bigl(\mathcal I(m\Gamma_\tau)\bigr),
\qquad
 \mathfrak T_{T,M}(v)
 :=\max_{\tau\in T}\{\tau-a_{\tau,M}(v)\}.
\tag{71.36}\label{eq:pseff-finite-ideal-approximant}
\]

```

## Exact marked statements and proofs

### relative-nef-generic-fibre-obstruction

```latex
% RETHLAS-NEW: relative-nef-generic-fibre-obstruction
\begin{proposition}\label{prop:pseff-relative-nef-obstruction}
Let \(\pi:\cX\to\mathbf P^1\) be a cohomological test configuration in
the sense of \cite[Definitions~2.5.1 and 4.1.2]{MP24}; thus \(\cX\) is a
normal compact K\"ahler space, but need not be smooth.  Let
\(\mathcal B\in H^{1,1}_{\mathrm{BC}}(\cX,\mathbf R)\) be relatively nef.
Assume that, under the canonical identification
\(\cX_t\simeq X\) for \(t\ne0\),
\[
                        \mathcal B|_{\cX_t}=\alpha.
\tag{71.2}\label{eq:pseff-generic-restriction}
\]
Then \(\alpha\) is nef.  More generally, any vertically corrected class,
on \(\cX\) or on a modification that is an isomorphism away from the
central fibre, which is relatively nef and has generic-fibre restriction
\(\alpha\), still forces \(\alpha\) to be nef.
\end{proposition}

\begin{proof}
By the definition used in \cite[Definition~4.1.2]{MP24}, relative
nefness implies that the restriction of \(\mathcal B\) to each fibre is
nef.  Since the equivariant trivialization identifies \(\cX_t\) with the
smooth manifold \(X\) for \(t\ne0\),
\eqref{eq:pseff-generic-restriction} therefore says directly that
\(\alpha\) is nef.  Equivalently, if \(\mathcal H\) is a relatively K\"ahler
class and one uses the approximation definition of relative nefness, then
restriction to a noncentral fibre gives the K\"ahler classes
\[
        \alpha+\varepsilon\,\mathcal H|_{\cX_t}
              \in H^{1,1}_{\mathrm{BC}}(X,\mathbf R)
\tag{71.3}\label{eq:pseff-nef-restriction}
\]
for every \(\varepsilon>0\), and letting \(\varepsilon\downarrow0\) gives
the same conclusion.

If \(D\) is a vertical divisor, then
\([D]|_{\cX_t}=0\) for \(t\ne0\), so a corrected class
\(\mathcal B+[D]\) has the same generic-fibre restriction.  If this
corrected class is relatively nef, the first paragraph applied to
\(\mathcal B+[D]\) proves the assertion.  Similarly, if
\(\mu:\cX'\to\cX\) is an isomorphism away from \(\cX_0\), then
\(\mu:\cX'_t\to\cX_t\) is an isomorphism for \(t\ne0\).  Every exceptional
vertical class restricts to zero on \(\cX'_t\); hence the restriction of
\(\mu^*\mathcal B\), with any such correction, is still \(\alpha\).
If the corrected pullback class on \(\cX'\) is relatively nef, applying
the first paragraph to that corrected relatively nef class on \(\cX'\)
proves the last assertion.  No claim is made that an arbitrary vertical
correction preserves relative nefness.  No smoothness of either total
space is used.
\end{proof}
```

### ideal-valuative-transform-one-test-curve

```latex
% RETHLAS-NEW: ideal-valuative-transform-one-test-curve
\begin{proposition}\label{prop:pseff-one-curve-transform}
The transform in \eqref{eq:pseff-test-curve-transform} has the following
properties.
\begin{enumerate}
\item \(\mathfrak T_\Gamma(0)=c\), and
      \(\mathfrak T_\Gamma\leq c\) on \(X^{\bethan}\).
\item For every \(v\), the restriction of
      \(s\mapsto\mathfrak T_\Gamma(sv)\) to \((0,+\infty)\) is either
      identically \(-\infty\), or finite, convex, and nonincreasing.
\item For \(\lambda>0\),
      \[
       \widehat{\mathfrak T}_\Gamma(\lambda v,\lambda b)
       =\lambda\widehat{\mathfrak T}_\Gamma(v,b).
      \tag{71.14}\label{eq:pseff-joint-homogeneity}
      \]
\item If \(C\in\mathbf R\), then
      \(\mathfrak T_{\Gamma+C}=\mathfrak T_\Gamma+C\).
\item If \(\Gamma\leq\Gamma'\) level by level, then
      \(\mathfrak T_\Gamma\leq\mathfrak T_{\Gamma'}\).
\end{enumerate}
No upper semicontinuity or MP plurisubharmonicity on all of
\(X^{\bethan}\) is included in the statement.
\end{proposition}

\begin{proof}
Ideal values are nonnegative, so each term in
\eqref{eq:pseff-test-curve-transform} is at most \(\tau<c\).  This proves
\(\mathfrak T_\Gamma\leq c\).  At the zero semivaluation all ideal values
vanish, whence
\(\mathfrak T_\Gamma(0)=\sup_{\tau<c}\tau=c\).

By homogeneity in \Cref{prop:pseff-ideal-valuative-basic},
\[
 \mathfrak T_\Gamma(sv)
 =\sup_{\tau<c}
      \{\tau-s\nu_v^{\mathcal I}(\Gamma_\tau)\}.
\tag{71.15}\label{eq:pseff-raywise-affine-supremum}
\]
If every coefficient that occurs is \(+\infty\), the right side is
identically \(-\infty\) for \(s>0\).  Otherwise the terms with infinite
coefficient can be discarded, and the right side is a finite-valued
supremum of affine functions of \(s\).  It is therefore convex; since all
slopes are
nonpositive, it is nonincreasing.  The second expression
in \eqref{eq:pseff-homogeneous-transform} and the same homogeneity give
\eqref{eq:pseff-joint-homogeneity} immediately.

By \cite[Definition~4.3]{Xia23Operations},
\((\Gamma+C)_\tau=\Gamma_{\tau-C}\).  Substituting
\(\rho=\tau-C\) in \eqref{eq:pseff-test-curve-transform} proves the fourth
claim.  Finally, \(\Gamma_\tau\leq\Gamma'_\tau\) makes
\(\Gamma_\tau\) at least as singular as \(\Gamma'_\tau\).  The valuative
criterion for multiplier ideals therefore gives
\(\nu_v^{\mathcal I}(\Gamma_\tau)\geq
\nu_v^{\mathcal I}(\Gamma'_\tau)\).  Taking the supremum in
\eqref{eq:pseff-test-curve-transform} proves the fifth claim.
\end{proof}
```

### rational-weighted-radial-formula

```latex
% RETHLAS-NEW: rational-weighted-radial-formula
\begin{proposition}\label{prop:pseff-weighted-radial-formula}
With the hypotheses and conventions above,
\[
 \widehat{\mathfrak T}_\Gamma(v,b)
 =qb-\nu_{\sigma_{v,b}}(W_q).
\tag{71.24}\label{eq:pseff-weighted-radial-formula}
\]
The right side is independent of the chosen \(q>c\).
The statement is restricted to rational divisorial \(v\) and rational
\(b>0\); it asserts no formula for an arbitrary nondivisorial
semivaluation.
\end{proposition}

\begin{proof}
Translate the test curve by \(-q\).  By
\Cref{prop:pseff-one-curve-transform}, its endpoint is \(c-q<0\), its
dual ray is \(u_t-qt\), and its complexification is precisely \(W_q\).
The divisorial Gauss identity, \cite[Proposition~3.1]{DXZ23} or
\Cref{prop:va-gauss-identity}, applied to the divisorial valuation
\(b^{-1}v\), gives
\[
 \mathfrak T_\Gamma(b^{-1}v)-q
 =-\nu_{\sigma_{b^{-1}v,1}}(W_q).
\tag{71.25}\label{eq:pseff-unit-gauss-step}
\]
The definitions give an exact equality of valuations
\[
                 \sigma_{v,b}=b\sigma_{b^{-1}v,1}.
\tag{71.26}\label{eq:pseff-gauss-scaling}
\]
Generic Lelong numbers are homogeneous under positive rescaling of a
divisorial valuation.  Multiplying \eqref{eq:pseff-unit-gauss-step} by
\(b\), and using \eqref{eq:pseff-homogeneous-transform} and
\eqref{eq:pseff-gauss-scaling}, proves
\eqref{eq:pseff-weighted-radial-formula}.

If \(q'>c\), then
\(W_{q'}=W_q+(q'-q)\log|z|^2\).  By
\eqref{eq:pseff-gauss-log-normalization},
\[
 \nu_{\sigma_{v,b}}(W_{q'})
 =\nu_{\sigma_{v,b}}(W_q)+(q'-q)b.
\]
Thus \(q'b-\nu_{\sigma_{v,b}}(W_{q'})\) equals the right side of
\eqref{eq:pseff-weighted-radial-formula}, proving independence of \(q\).
\end{proof}
```

### perturbation-independent-transform

```latex
% RETHLAS-NEW: perturbation-independent-transform
\begin{theorem}\label{thm:pseff-perturbation-independent-transform}
The right side of \eqref{eq:pseff-inverse-system-transform} is independent
of \(\omega\).  It therefore defines a canonical map
\[
 \mathfrak T_\theta:
 \PSH^{\NA}(X,\theta)
 \longrightarrow[-\infty,+\infty)^{X^{\bethan}},
 \qquad
 \boldsymbol\Gamma\longmapsto
 \mathfrak T_{\boldsymbol\Gamma}.
\tag{71.28}\label{eq:pseff-canonical-transform-map}
\]
For every \(\boldsymbol\Gamma\), its image satisfies all five conclusions
of \Cref{prop:pseff-one-curve-transform}.  In particular,
\(\mathfrak T_{\boldsymbol\Gamma}(0)=\boldsymbol\Gamma_{\max}\).
The theorem makes no assertion that the raw function in
\eqref{eq:pseff-inverse-system-transform} is upper semicontinuous or MP
psh at nondivisorial points.
\end{theorem}

\begin{proof}
Let \(\omega\) and \(\omega'\) be two perturbations.  Choose a third
perturbation dominating both in the directed system.  It is enough to
compare either original component with its image under one transition.
By \eqref{eq:tna-transition}, at every \(\tau<c\) that image is
\[
 P_{\theta+\omega'}
 [\Gamma^{\theta+\omega}_\tau]_{\mathcal I}
\tag{71.29}\label{eq:pseff-transition-level}
\]
with the forms relabelled according to the order convention of
\eqref{eq:tna-kahler-order}.  The \(\mathcal I\)-envelope is
\(\mathcal I\)-equivalent to its input.  By
\Cref{prop:pseff-i-equivalence-valuative}, this gives the exact equality
\[
 \mathcal I\!\left(mP_{\theta+\omega'}
 [\Gamma^{\theta+\omega}_\tau]_{\mathcal I}\right)
 =\mathcal I(m\Gamma^{\theta+\omega}_\tau),
 \qquad m\in\mathbf Z_{>0}.
\tag{71.30}\label{eq:pseff-transition-ideal-equality}
\]
Taking ideal values, dividing by \(m\), and passing to the limit proves
that \(\nu_v^{\mathcal I}\) is unchanged for every
\(v\in X^{\bethan}\).  The endpoint is common by
\Cref{prop:tna-common-terminal}.  Thus
\eqref{eq:pseff-inverse-system-transform} is independent of the
component.  All remaining assertions follow by applying
\Cref{prop:pseff-one-curve-transform} to any one component.
\end{proof}
```

### divisorial-inversion-injectivity

```latex
% RETHLAS-NEW: divisorial-inversion-injectivity
\begin{theorem}\label{thm:pseff-divisorial-inversion}
Fix \(\boldsymbol\Gamma\in\PSH^{\NA}(X,\theta)\), a perturbation
\(\omega\), and a prime divisor \(E\) over \(X\).  For \(\tau<c\), put
\[
 a_E(\tau):=\nu_E(\Gamma^{\theta+\omega}_\tau).
\tag{71.31}\label{eq:pseff-divisorial-profile}
\]
Then \(a_E\) is finite, convex, and nondecreasing on \(( -\infty,c)\).
For every \(p>0\),
\[
 a_E^*(p):=\sup_{\tau<c}\{p\tau-a_E(\tau)\}
 =p\,\mathfrak T_{\boldsymbol\Gamma}(p^{-1}\ord_E),
\tag{71.32}\label{eq:pseff-divisorial-conjugate}
\]
and, for \(\tau<c\),
\[
 a_E(\tau)
 =\sup_{p>0}
    \{p\tau-p\mathfrak T_{\boldsymbol\Gamma}
                         (p^{-1}\ord_E)\}.
\tag{71.33}\label{eq:pseff-divisorial-inversion}
\]
The supremum in \eqref{eq:pseff-divisorial-inversion} is unchanged if
\(p\) is restricted to \(\mathbf Q_{>0}\).  Consequently
\(\mathfrak T_\theta\) is injective; in fact, the values on the rational
points of the divisorial rays, together with the value at \(0\), determine
the DXZ metric.  Moreover,
\[
 \boldsymbol\Gamma\leq\boldsymbol\Gamma'
 \quad\Longleftrightarrow\quad
 \mathfrak T_{\boldsymbol\Gamma}(p^{-1}\ord_E)
 \leq\mathfrak T_{\boldsymbol\Gamma'}(p^{-1}\ord_E)
\tag{71.34}\label{eq:pseff-order-reflection}
\]
for every prime divisor \(E\) and every \(p\in\mathbf Q_{>0}\), where on
the right the inequality is required simultaneously for all such
\((E,p)\), together with
\(\mathfrak T_{\boldsymbol\Gamma}(0)
\leq\mathfrak T_{\boldsymbol\Gamma'}(0)\).
\end{theorem}

\begin{proof}
The test-curve condition says that
\(\tau\mapsto\Gamma^{\theta+\omega}_\tau\) is decreasing and concave.
Generic Lelong numbers reverse the first order and are affine under
positive affine combinations of quasi-psh functions.  It follows that
\(a_E\) is nondecreasing and convex.  It is finite at every interior
level because a quasi-psh function that is not identically \(-\infty\)
has finite generic Lelong number along a fixed divisor.

By \eqref{eq:pseff-divisorial-lelong} and the perturbation independence
just proved,
\[
 \begin{split}
 p\mathfrak T_{\boldsymbol\Gamma}(p^{-1}\ord_E)
 &=p\sup_{\tau<c}\{\tau-p^{-1}a_E(\tau)\}\\
 &=\sup_{\tau<c}\{p\tau-a_E(\tau)\},
 \end{split}
\]
which is \eqref{eq:pseff-divisorial-conjugate}.

Let \(a_E(c)\) denote the left limit at \(c\), possibly \(+\infty\),
and extend \(a_E\) by this value at \(c\) and by \(+\infty\) on
\((c,+\infty)\).  This is a proper lower-semicontinuous convex function
on \(\mathbf R\).  Its conjugate is infinite for \(p<0\): indeed,
\(a_E\) is nonnegative and bounded above on each interval
\(( -\infty,\tau_0]\), while \(p\tau\to+\infty\) as
\(\tau\to-\infty\).  The Fenchel--Moreau theorem therefore reconstructs
the function using \(p\geq0\).  The value at \(p=0\) is the right limit
of the finite convex function \(a_E^*\) on \([0,+\infty)\), so for an
interior point \(\tau<c\) it may be recovered by letting \(p\downarrow0\).
This proves \eqref{eq:pseff-divisorial-inversion} with \(p>0\).
Continuity of the finite convex function \(a_E^*\) on
\((0,+\infty)\) and density of \(\mathbf Q_{>0}\) show that rational
\(p\)'s suffice.

Suppose that two transforms agree on the stated rational divisorial
points and at \(0\).  Their endpoints agree by
\Cref{thm:pseff-perturbation-independent-transform};
\eqref{eq:pseff-divisorial-inversion} then shows that the two components
have the same generic Lelong number along every \(E\), at every
\(\tau<c\).  By \Cref{prop:pseff-i-equivalence-valuative}, the levels
have the same multiplier ideals.  Both are normalized
\(\mathcal I\)-model potentials, so the defining maximality of the
\(\mathcal I\)-envelope makes the levels equal.  Their left limits at
the endpoint and their \(-\infty\) levels above it also agree.  This holds
for every perturbation, proving injectivity.

It remains to prove \eqref{eq:pseff-order-reflection}.  The forward
implication is \Cref{prop:pseff-one-curve-transform}.  Conversely, for
each \(E\) one has
\[
 \lim_{p\to+\infty}
 \mathfrak T_{\boldsymbol\Gamma}(p^{-1}\ord_E)=c.
\tag{71.35}\label{eq:pseff-endpoint-ray-limit}
\]
Indeed, the left side is at most \(c\), while for every fixed
\(\tau<c\), \eqref{eq:pseff-test-curve-transform} bounds it below by
\(\tau-p^{-1}a_E(\tau)\), which tends to \(\tau\).  Thus the assumed
inequality at the zero semivaluation gives \(c\leq c'\).  When a prime
divisor exists, \eqref{eq:pseff-endpoint-ray-limit} shows that this endpoint
inequality already follows from the rational divisorial inequalities; the
explicit zero-semivaluation clause also covers dimension zero.  Equations
\eqref{eq:pseff-divisorial-conjugate}--\eqref{eq:pseff-divisorial-inversion}
then give
\(a_E(\tau)\geq a'_E(\tau)\) for every \(E\) and every \(\tau<c\).
The valuative multiplier-ideal criterion and strong openness yield the
corresponding \(\mathcal I\)-singularity order, and normalized
\(\mathcal I\)-model envelopes convert it into
\(\Gamma^{\theta+\omega}_\tau\leq
\Gamma'^{\theta+\omega}_\tau\).  Equivalently, this last implication is
\cite[Lemma~4.2]{Xia23Operations}.  It holds at every perturbation, hence
\(\boldsymbol\Gamma\leq\boldsymbol\Gamma'\).
\end{proof}
```

### divisorial-ideal-pl-approximation

```latex
% RETHLAS-NEW: divisorial-ideal-pl-approximation
\begin{proposition}\label{prop:pseff-divisorial-pl-approximation}
Each \(\mathfrak T_{T,M}\) is an extended-real-valued finite ideal
expression on \(X^{\bethan}\).  On the zero-support valuation locus---in
particular, on every dual complex and at every rational divisorial
point---it is a real piecewise-linear function.  For fixed \(T\), it
decreases as \(M\) increases, and
\[
 \lim_{M\to\infty}\mathfrak T_{T,M}(v)
 =\max_{\tau\in T}
    \{\tau-\nu_v^{\mathcal I}(\Gamma_\tau)\}.
\tag{71.37}\label{eq:pseff-finite-grid-limit}
\]
Let \(D\) be a countable dense subset of \(( -\infty,c)\), and let
\(T_1\subset T_2\subset\cdots\) be finite subsets whose union is \(D\).
Then, at every rational divisorial point \(v=r\ord_E\),
\[
 \mathfrak T_{\boldsymbol\Gamma}(v)
 =\lim_{N\to\infty}\lim_{M\to\infty}
       \mathfrak T_{T_N,M}(v).
\tag{71.38}\label{eq:pseff-iterated-pl-limit}
\]
The proposition neither asserts that the iterated limit in
\eqref{eq:pseff-iterated-pl-limit} holds at arbitrary nondivisorial
points nor that any finite approximant is MP psh.
\end{proposition}

\begin{proof}
For a coherent ideal \(\mathfrak a\), the function
\(v\mapsto-v(\mathfrak a)\) is piecewise linear on every dual complex
carrying \(\mathfrak a\), and these functions are compatible under
refinement; see \Cref{chap:tropical-spectra-complex}.  Thus
\(-m^{-1}v(\mathcal I(m\Gamma_\tau))\) is real piecewise linear there.
Finite minima and maxima of piecewise-linear functions are piecewise
linear after passing to a common subdivision.  Since
\[
 \tau-a_{\tau,M}(v)
 =\min_{1\leq m\leq M}
   \left\{\tau-\frac1m
             v\bigl(\mathcal I(m\Gamma_\tau)\bigr)\right\},
\]
the second formula in \eqref{eq:pseff-finite-ideal-approximant} is
piecewise linear on that locus.  At a semivaluation with nonzero support,
an appearing ideal may have value \(+\infty\); the same finite formula then
takes values in \([ -\infty,+\infty)\), which is why no globally
real-valued PL assertion is made.

By \eqref{eq:pseff-fekete-formula},
\(a_{\tau,M}(v)\) increases to
\(\nu_v^{\mathcal I}(\Gamma_\tau)\).  For a finite set \(T\), the maximum
of finitely many decreasing extended-real sequences decreases to the
maximum of their limits.  This proves
\eqref{eq:pseff-finite-grid-limit}.

If \(v=r\ord_E\), then
\(\nu_v^{\mathcal I}(\Gamma_\tau)=r a_E(\tau)\) by
\eqref{eq:pseff-divisorial-lelong}.  The convex function \(a_E\) is
continuous on \(( -\infty,c)\), so
\(\tau\mapsto\tau-r a_E(\tau)\) is continuous there.  Its supremum over
the dense set \(D\) equals its supremum over the whole interval.
Combining this observation with \eqref{eq:pseff-finite-grid-limit} and
then letting \(N\to\infty\) proves
\eqref{eq:pseff-iterated-pl-limit}.
\end{proof}
```

### projective-rational-full-mp-dxz-identification

```latex
% RETHLAS-NEW: projective-rational-full-mp-dxz-identification
\begin{theorem}\label{thm:pseff-projective-rational-full-link}
Assume that \(X\) is a smooth projective manifold and
\(\alpha=c_1(L)\), where \(L\) is an ample \(\mathbf Q\)-line bundle.
Choose a smooth metric on \(L\) with K\"ahler curvature \(\theta\).  Under
the canonical homeomorphism
\(X^{\bethan}\simeq X^{\mathrm{an,triv}}\) of
\Cref{thm:ts-algebraic-recovery}, the map
\[
 \mathfrak T_\theta:
 \PSH^{\NA}_{\mathrm{DXZ}}(X,\theta)
 \longrightarrow\PSH_{\mathrm{MP}}(\alpha)
\tag{71.41}\label{eq:pseff-projective-full-bijection}
\]
is an order isomorphism, without a finite-energy hypothesis.  In this
setting the raw function
\(\mathfrak T_{\boldsymbol\Gamma}\) is the MP psh representative on all
of \(X^{\bethan}\).  This theorem does not apply to a nonprojective
K\"ahler class or to a big non-nef class.
\end{theorem}

\begin{proof}
GAGA identifies coherent analytic ideals on \(X\) with algebraic ideals,
and \Cref{thm:ts-algebraic-recovery} identifies their evaluation
functions on the two semivaluation spaces.  We first compare the two
model cones.  An algebraic semipositive model metric gives a relatively
nef cohomological test configuration, hence an MP model psh function.
Conversely, let \(\phi_D\) be an MP model psh function represented by the
relatively nef class \(\alpha_{\cX}+[D]\).  By
\cite[Remark~2.5.2]{MP24}, we may pass to a smooth model projective over
\(X\times\mathbf P^1\); because \(X\) is projective, this model is itself
projective.  Choose a relatively K\"ahler cohomological class
\(\alpha_{\cX}+[H]\) with the same generic-fibre restriction.  For
\(\varepsilon>0\),
\[
 \alpha_{\cX}+
 \left[\frac{D+\varepsilon H}{1+\varepsilon}\right]
 =\frac{(\alpha_{\cX}+[D])
       +\varepsilon(\alpha_{\cX}+[H])}{1+\varepsilon}
\tag{71.42}\label{eq:pseff-model-kahler-approximation}
\]
is relatively K\"ahler and has generic-fibre restriction \(\alpha\).
After an additive central-fibre normalization we may arrange
\(\phi_H\geq\phi_D\).  The corresponding model functions
\[
 \phi_\varepsilon
 =\frac{\phi_D+\varepsilon\phi_H}{1+\varepsilon}
\tag{71.43}\label{eq:pseff-model-monotone-approximation}
\]
then decrease to \(\phi_D\) as \(\varepsilon\downarrow0\).

For fixed \(\varepsilon>0\), the class in
\eqref{eq:pseff-model-kahler-approximation} belongs to the finite-dimensional
real N\'eron--Severi space generated by \(\alpha_{\cX}\) and the vertical
components.  Relative K\"ahlerness is open there, so it can be approximated
by rational relatively K\"ahler classes having generic-fibre restriction
\(c_1(L)\).  On the projective morphism \(\cX\to\mathbf P^1\), these are
first Chern classes of relatively ample \(\mathbf Q\)-line bundles by the
relative Kodaira criterion.  Their model functions converge uniformly to
\(\phi_\varepsilon\).  Uniform limits of semipositive model functions are
Boucksom--Jonsson psh by \Cref{thm:ch21-continuous-zhang}; hence each
\(\phi_\varepsilon\) is Boucksom--Jonsson psh.  Equation
\eqref{eq:pseff-model-monotone-approximation} is a decreasing
regularization of \(\phi_D\), so decreasing closedness makes \(\phi_D\)
Boucksom--Jonsson psh as well.  The converse was proved in the first
sentence, and both theories are defined by decreasing model
approximation.  Therefore
\[
 \PSH_{\mathrm{MP}}(\alpha)=\PSH(L^{\mathrm{an,triv}})
\tag{71.44}\label{eq:pseff-mp-bj-cones}
\]
under the homeomorphism of the underlying spaces.

Finally, \Cref{thm:comp-dxz} gives an order isomorphism between the DXZ
inverse-system space and the Boucksom--Jonsson psh cone.  Its
analytification is defined by the same multiplier-ideal formula
\eqref{eq:pseff-inverse-system-transform}; see
\Cref{prop:va-fekete,prop:va-divisorial-formula}.  Combining this
identification with \eqref{eq:pseff-mp-bj-cones} gives
\eqref{eq:pseff-projective-full-bijection} and identifies the raw
functions at every semivaluation.
\end{proof}
```

### big-nonnef-surviving-dxz-core

```latex
% RETHLAS-NEW: big-nonnef-surviving-dxz-core
\begin{proposition}\label{prop:pseff-big-nonnef-surviving-core}
Assume that \(\alpha\) is big and non-nef, and put
\(V:=\vol(\alpha)>0\).  Then the unchanged MP relatively nef model cone
with generic-fibre class \(\alpha\) is empty.  Nevertheless, every
\(\boldsymbol\Gamma\in\PSH^{\NA}(X,\theta)\) has the canonical injective
ideal-valuative realization of
\Cref{thm:pseff-perturbation-independent-transform,thm:pseff-divisorial-inversion}.

If \(\vol(\boldsymbol\Gamma)>0\), then
\(\boldsymbol\Gamma\) is represented by a unique unperturbed
positive-mass \(\mathcal I\)-model test curve \(\Gamma\), and its DXZ
energy is
\[
 I_\theta^{\NA}(\Gamma)
 =c+\frac1V\int_{-\infty}^{c}
   \left(
    \int_X\left\langle
       (\theta+\ddc\Gamma_\tau)^n
    \right\rangle-V
   \right)\rd\tau.
\tag{71.49}\label{eq:pseff-big-dxz-energy}
\]
On the complement of this embedded positive-mass locus, the DXZ
functional is \(-\infty\) by definition.  None of these facts constructs
an MP psh cone, an MP Monge--Amp\`ere measure, or an MP energy in the
non-nef class.
\end{proposition}

\begin{proof}
The emptiness statement is
\Cref{prop:pseff-relative-nef-obstruction}: any member of the unchanged
model cone would restrict to a relatively nef class and force \(\alpha\)
to be nef.  The transform and its injectivity are independent of nefness
by
\Cref{thm:pseff-perturbation-independent-transform,thm:pseff-divisorial-inversion}.

The positive-volume recovery and uniqueness are
\Cref{thm:tna-positive-volume,cor:tna-positive-no-ambiguity}.  For a big
class, \cite[formula~(43)]{DXZ23} defines the energy on the recovered
positive-mass test curve by exactly
\eqref{eq:pseff-big-dxz-energy}, and defines it to be \(-\infty\) on the
rest of the inverse-system space.  The last sentence follows because no
step changes the generic-fibre class in the MP model signature or defines
intersection measures for a non-nef cohomological model.
\end{proof}
```

### zero-volume-normalization-obstruction

```latex
% RETHLAS-NEW: zero-volume-normalization-obstruction
\begin{proposition}\label{prop:pseff-zero-volume-boundary}
Assume that \(\vol(\alpha)=0\).  Then every
\(\varphi\in\PSH(X,\theta)\) satisfies
\[
 \int_X\left\langle
       (\theta+\ddc\varphi)^n
 \right\rangle=0.
\tag{71.50}\label{eq:pseff-zero-top-mass}
\]
Consequently, neither the probability normalization
\(V^{-1}\langle(\theta+\ddc\varphi)^n\rangle\) nor the normalized energy
formula \eqref{eq:pseff-big-dxz-energy} is defined when \(V=0\).
The inverse-system space and the injective transform
\eqref{eq:pseff-canonical-transform-map} still make sense.  The statement
does not rule out a future unnormalized or lower-dimensional boundary
theory.
\end{proposition}

\begin{proof}
Let \(V_\theta\) have minimal singularities.  It is less singular than
\(\varphi\).  The unrestricted monotonicity theorem for total
nonpluripolar mass \cite[Theorem~1.1]{DDNL18mono} gives
\[
 0\leq\int_X\left\langle
       (\theta+\ddc\varphi)^n
      \right\rangle
 \leq\int_X\left\langle
       (\theta+\ddc V_\theta)^n
      \right\rangle
 =\vol(\alpha)=0,
\]
which proves \eqref{eq:pseff-zero-top-mass}.  Division by \(V=0\) is
undefined, proving the normalization statements.  DXZ define
\(\PSH^{\NA}(X,\theta)\) as the inverse limit over the big classes
\(\theta+\omega\), so its definition does not divide by \(V\).
The construction and proof of
\Cref{thm:pseff-perturbation-independent-transform} likewise use only
multiplier ideals and endpoints.  This proves the last assertion.
\end{proof}
```
