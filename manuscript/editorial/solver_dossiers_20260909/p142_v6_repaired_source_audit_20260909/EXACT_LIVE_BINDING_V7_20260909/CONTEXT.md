# P14.2 V7 exact-live binding context

This local audit binds the frozen V6 source-stage targets to exact current
Chapter 71 bytes. It is not an independent hostile audit, a final-path smoke
receipt, or a production-verification result.

Candidate manifest SHA-256: `3511b635413d7ace9013edd278216017096d7359ac5dd2b3155cbf179c83e97f`.
Current Chapter 71 SHA-256: `629403ddde7f6dce25a8d1edd3d0d5a7a45bd1eec276b3125612b83c5e0ab6c9`.

## target/STATEMENT.tex ← Chapter 71 lines 615-692, 850-865

```tex
\begin{lemma}\label{lem:p142-monotone-parameter-supremum}
Let $Y$ be a topological space, let $c\in\mathbf R$, and, for each
$\tau<c$, let $a_\tau:Y\to[0,+\infty]$ be lower semicontinuous.
Assume that $a_s\leq a_t$ whenever $s\leq t<c$. Then
\[
 F(y):=\sup_{\tau<c}\{\tau-a_\tau(y)\}
 \in[-\infty,c]
\]
is upper semicontinuous. For every dense subset $D\subset(-\infty,c)$,
\[
 F(y)=\sup_{\tau\in D}\{\tau-a_\tau(y)\}
 \quad(y\in Y).
 \tag{71.33a}
 \label{eq:p142-dense-parameter-formula}
\]
No continuity in $\tau$, countability assumption on $Y$, or finiteness
assumption on $a_\tau(y)$ is required.
\end{lemma}

\begin{theorem}\label{thm:p142-raw-transform-usc}
Let $X$ be a complex manifold, and give the tropical spectrum
$X^{\bethan}$ of its coherent ideal sheaves the topology of pointwise
convergence on ideals. Let $c\in\mathbf R$ and let
$(\Gamma_\tau)_{\tau<c}$ be a
decreasing family of quasi-plurisubharmonic functions on $X$, none
identically $-\infty$ on a connected component. Put
\[
 \nu_v^{\mathcal I}(\Gamma_\tau)
 :=\sup_{m\geq1}\frac1m v\bigl(\mathcal I(m\Gamma_\tau)\bigr),
 \qquad
 F_\Gamma(v):=\sup_{\tau<c}
       \{\tau-\nu_v^{\mathcal I}(\Gamma_\tau)\}.
 \tag{71.33b}
 \label{eq:p142-raw-transform}
\]
The supremum defining $\nu_v^{\mathcal I}$ equals the limit as
$m\to\infty$. Then $F_\Gamma$ is upper semicontinuous on all of
$X^{\bethan}$, including semivaluations with nonzero support. Formula
\eqref{eq:p142-dense-parameter-formula} holds for $F_\Gamma$ at every
semivaluation.

More precisely, for $N,M\in\mathbf Z_{>0}$ set
\[
 \tau_{N,j}:=c-N+\frac jN \qquad(0\leq j<N^2).
 \tag{71.33c}
 \label{eq:p142-mesh}
\]
\[
 A_{\tau,M}(v):=\max_{1\leq m\leq M}
       \frac1m v\bigl(\mathcal I(m\Gamma_\tau)\bigr).
 \tag{71.33d}
 \label{eq:p142-finite-ideal-values}
\]
\[
 B_{N,M}(v):=\frac1N+
   \max\left\{c-N,
       \max_{0\leq j<N^2}
        \bigl(\tau_{N,j}-A_{\tau_{N,j},M}(v)\bigr)\right\}.
 \tag{71.33e}
 \label{eq:p142-upper-approximants}
\]
\[
 f_k(v):=\min_{1\leq N,M\leq k}B_{N,M}(v).
 \tag{71.33f}
 \label{eq:p142-decreasing-sequence}
\]
Every $B_{N,M}$ and $f_k$ is a bounded, real-valued continuous function
given by a finite expression in negative ideal evaluations $-v(\mathfrak a)$,
real translations, positive rational scaling, minima and maxima. Moreover,
\[
 f_k\searrow F_\Gamma\quad\hbox{pointwise on }X^{\bethan}.
 \tag{71.33g}
 \label{eq:p142-exact-sequential-limit}
\]
The approximants are not asserted to be MP plurisubharmonic or
semipositive.
\end{theorem}

\begin{corollary}\label{cor:p142-pseudoeffective-raw-usc}
Let $X$ be a connected compact K\"ahler manifold, let $\theta$ be a
smooth closed real $(1,1)$-form with pseudoeffective class, and let
$\boldsymbol\Gamma\in\PSH^{\mathrm{NA}}(X,\theta)$ be a DXZ
inverse-system metric. Its perturbation-independent raw ideal-valuative
transform is upper semicontinuous on $X^{\bethan}$ and has the decreasing
continuous finite-ideal approximation in
\eqref{eq:p142-decreasing-sequence}--\eqref{eq:p142-exact-sequential-limit},
formed from any one perturbation component. Every dense parameter set
computes the same transform at all semivaluations.

This assertion requires neither projectivity nor rationality, bigness,
nefness, or positive volume of the unperturbed class. It asserts no MP
positivity, positive approximation, Monge--Amp\`ere construction, or
identification of $P$-equivalence with $\mathcal I$-equivalence.
\end{corollary}
```

## target/PROOF.tex ← Chapter 71 lines 693-849, 867-897

```tex
\begin{proof}[Proof of \cref{lem:p142-monotone-parameter-supremum}]
For $N\geq1$ put $a=c-N$, and partition $[a,c)$ into the $N^2$
half-open intervals
\[
 [\tau_{N,j},\tau_{N,j}+1/N),\qquad
 \tau_{N,j}=c-N+j/N,\quad 0\leq j<N^2.
\]
Only left endpoints are sampled; the family is never evaluated at $c$.
Set
\[
 F_N:=\max\{c-N,F\},\qquad
 G_N:=\max\left\{c-N,
      \max_{0\leq j<N^2}
       (\tau_{N,j}-a_{\tau_{N,j}})\right\}.
\]
Every sampled term occurs in the supremum defining $F$, so $G_N\leq F_N$.
If $\tau<c-N$, nonnegativity gives $\tau-a_\tau\leq c-N$.
Otherwise there is $j$ with
$\tau_{N,j}\leq\tau<\tau_{N,j}+1/N$. Monotonicity in the parameter
gives, in extended-real order,
\[
 \tau-a_\tau
 \leq \tau-a_{\tau_{N,j}}
 \leq \tau_{N,j}-a_{\tau_{N,j}}+1/N
 \leq G_N+1/N.
\]
This also holds when one or both of the ideal-type quantities are infinite:
only a finite real number minus $+\infty$ occurs. Taking the supremum and
including the floor proves
\[
             G_N\leq F_N\leq G_N+1/N.
 \tag{71.33h}
 \label{eq:p142-grid-sandwich}
\]

Each $G_N$ is a finite-valued upper-semicontinuous function, since
$-a_{\tau_{N,j}}$ is upper semicontinuous. The sandwich gives the exact
identity
\[
                  F=\inf_{N\geq1}(G_N+1/N).
 \tag{71.33i}
 \label{eq:p142-usc-infimum}
\]
Indeed, $F\leq F_N\leq G_N+1/N$, and
$G_N+1/N\leq F_N+1/N$ tends pointwise to $F$ as $N\to\infty$.
If $F(y)=-\infty$, then $F_N(y)=c-N$, so the same conclusion holds
at that point. An arbitrary infimum of upper-semicontinuous functions is
upper semicontinuous: its strict sublevel set is the union of the strict
sublevel sets of its terms. This proves the first assertion on an
arbitrary topological space.

For the dense-parameter assertion, fix $y$ and $\tau<c$ with
$a_\tau(y)<+\infty$. Given $\varepsilon>0$, choose
$s\in D\cap(\tau-\varepsilon,\tau)$. Then
\[
 s-a_s(y)\geq s-a_\tau(y)
              >\tau-a_\tau(y)-\varepsilon.
\]
Thus the supremum over $D$ is at least every finite term in the full
supremum, after letting $\varepsilon$ tend to zero. Terms equal to
$-\infty$ impose no further condition. If all terms are $-\infty$,
both suprema are $-\infty$. The opposite inequality follows from
$D\subset(-\infty,c)$, proving
\eqref{eq:p142-dense-parameter-formula}.
\end{proof}

\begin{proof}[Proof of \cref{thm:p142-raw-transform-usc}]
Multiplier ideal sheaves of quasi-psh functions on a complex manifold
are coherent. Their subadditivity \cite[Theorem~2.6(ii)]{DEL00} gives
\[
 \mathcal I((m+\ell)\Gamma_\tau)
 \subseteq\mathcal I(m\Gamma_\tau)
               \mathcal I(\ell\Gamma_\tau).
\]
Ideal values reverse inclusion and add under multiplication. Hence
$b_m=v(\mathcal I(m\Gamma_\tau))$ is a nonnegative extended-real
superadditive sequence. If some $b_q=+\infty$, superadditivity implies
$b_m=+\infty$ for every $m\geq q$: use $m=q+r$ for $r\geq1$.
Otherwise, for a fixed $q$, writing $m=kq+r$, with $0\leq r<q$, gives
$b_m\geq kb_q$ (put $b_0=0$). Therefore
\[
 \liminf_{m\to\infty}\frac{b_m}{m}\geq\frac{b_q}{q}.
\]
Taking the supremum over $q$ and comparing with the immediate upper
bound proves the limit assertion, including an infinite supremum. This
is the multiplier-ideal argument recorded in
\cref{prop:pseff-ideal-valuative-basic}.

By the topology of the tropical spectrum, the function
$v\mapsto v(\mathfrak a)$ is continuous into $[0,+\infty]$ with its
order topology for every coherent ideal $\mathfrak a$; see
\cite[Definition~1.3.1]{MP24} and \eqref{eq:ts-evaluation}.
It follows that
\[
 v\longmapsto\nu_v^{\mathcal I}(\Gamma_\tau)
   =\sup_{m\geq1}\frac1m
          v(\mathcal I(m\Gamma_\tau))
\]
is lower semicontinuous. If $s\leq t<c$, then
$\Gamma_s\geq\Gamma_t$. Local integrability immediately implies
\[
 \mathcal I(m\Gamma_t)\subseteq\mathcal I(m\Gamma_s),
 \qquad
 \nu_v^{\mathcal I}(\Gamma_s)
       \leq\nu_v^{\mathcal I}(\Gamma_t).
\]
For the first inclusion, multiplication of the weight by the bounded
factor associated to an additive local constant would also suffice;
the given pointwise order already yields it directly. No assertion
about continuity of multiplier ideals in the parameter is used.
The hypotheses of \cref{lem:p142-monotone-parameter-supremum} are now
verified, and that lemma proves upper semicontinuity and the dense-set
formula at every semivaluation.

We prove the stronger explicit approximation assertion separately.
For fixed $N,M$, all ideal evaluations in
\eqref{eq:p142-upper-approximants} are continuous extended-real
functions. Their displayed finite maxima and positive scalings are
continuous in the order topology; subtracting from the finite
$\tau_{N,j}$ gives a continuous function into $[-\infty,\tau_{N,j}]$.
The outer maximum with $c-N$ then yields an ordinary real-valued
continuous function. In particular,
\[
        c-N+1/N\leq B_{N,M}\leq c+1/N.
\]
This establishes boundedness without invoking compactness of $X^{\bethan}$.

As $M$ increases, $A_{\tau,M}\nearrow\nu^{\mathcal I}(\Gamma_\tau)$.
For the finite number of sampled parameters, taking the maximum commutes
with these decreasing limits after changing the sign. To see this even
at $-\infty$, if every limiting term is below a chosen real threshold,
then every term is eventually below it; a maximum of finitely many
indices works for all terms. The fixed finite floor is retained throughout.
Consequently, with $G_N$ as in the preceding proof,
\[
           B_{N,M}\searrow G_N+1/N\quad(M\to\infty).
\]
The sandwich \eqref{eq:p142-grid-sandwich} gives
\[
 F_\Gamma\leq B_{N,M},\qquad
 \inf_{N,M\geq1}B_{N,M}
      =\inf_{N\geq1}(G_N+1/N)=F_\Gamma.
 \tag{71.33j}
 \label{eq:p142-double-infimum}
\]
Every $f_k$ is a finite minimum of bounded continuous real-valued
functions. The squares $\{1,\ldots,k\}^2$ increase and exhaust
$\mathbf Z_{>0}^2$, so their minima decrease to the double infimum
in \eqref{eq:p142-double-infimum}. This is
\eqref{eq:p142-exact-sequential-limit}.

The construction is explicit. It does not extract a sequence from an
arbitrary net on a nonmetrizable space. Nor does a minimum of these
continuous functions acquire a positivity property merely because it
is formed from ideal values. No positive approximation is asserted.
\end{proof}

\begin{proof}[Proof of \cref{cor:p142-pseudoeffective-raw-usc}]
Fix one K\"ahler perturbation component
$\Gamma=(\Gamma^{\theta+\omega}_\tau)_{\tau<c}$, where
$c=\boldsymbol\Gamma_{\max}$. The DXZ test-curve definition supplies
a decreasing family of quasi-psh functions with finite terminal
parameter, and its interior levels are not identically $-\infty$;
see \cite[Section~2.2, Definition~3.3]{DXZ23}.
\Cref{thm:p142-raw-transform-usc} therefore applies to this component.

The identification with the raw inverse-system transform uses only the
already established transition identity, not an MP comparison theorem.
Under a transition the interior level is replaced by its
$\mathcal I$-model envelope in the larger class. This preserves every
integer multiplier ideal by \cite[Proposition~2.18(ii)]{DX22}; the
standing hypotheses of its Section~2.4 allow an arbitrary compact
K\"ahler manifold and a pseudoeffective background class. A common
dominating component compares any
two choices, and their terminal parameters coincide. Evaluating those
same ideals at any semivaluation proves that both the raw transform and
the explicit expressions \eqref{eq:p142-finite-ideal-values}--
\eqref{eq:p142-decreasing-sequence} are unchanged. These are precisely
the ideal equalities in
\cref{thm:pseff-perturbation-independent-transform}; the source
transition is \cite[formula~(28), Definition~3.3]{DXZ23}.

All arguments take place on a perturbed component. No potential of
positive mass in the unperturbed class is chosen, so zero-volume
pseudoeffective classes are included. The proof does not construct
relatively nef cohomological models, a Monge--Amp\`ere operator, or an
energy. Those are distinct questions.
\end{proof}
```

## target/EXAMPLE.tex ← Chapter 71 lines 899-927

```tex
\begin{example}\label{ex:p142-infinite-ideal-value}
On $X=\mathbf P^1$, choose a point $p$, a smooth Hermitian metric on
$\mathcal O(p)$, and its canonical section $s_p$. Fix $\lambda>0$ and
put $\psi=\lambda\log|s_p|^2$. The family $\Gamma_\tau=\psi$ for
$\tau<c$ satisfies the elementary hypotheses of
\cref{thm:p142-raw-transform-usc}; no assertion that this particular
representative is an $\mathcal I$-model potential is needed.

Writing $\mathfrak m_p$ for the ideal sheaf of $p$, one has
\[
       \mathcal I(m\psi)=\mathfrak m_p^{\lfloor m\lambda\rfloor}.
\]
Indeed, near $p$ a coordinate $z$ expresses $\psi$ as
$\lambda\log|z|^2$ plus a smooth function. A germ of order $q$ is
integrable with the weight $\mathrm e^{-m\psi}$ exactly when
$q-m\lambda>-1$, which is equivalent to $q\geq\lfloor m\lambda\rfloor$.
Away from $p$ the ideal is the unit ideal. It follows that
\[
 \nu_v^{\mathcal I}(\psi)=\lambda v(\mathfrak m_p),
 \qquad F_\Gamma(v)=c-\lambda v(\mathfrak m_p).
\]
At a semivaluation with $v(\mathfrak m_p)=+\infty$, each sufficiently
large multiplier-ideal value is infinite, so the displayed formulas give
$F_\Gamma(v)=-\infty$. For the smaller integers with
$\lfloor m\lambda\rfloor=0$, the ideal is the unit ideal and its value
is zero; no expression $0\cdot(+\infty)$ is used. Thus the infinite-value
case in the theorem records actual support information and cannot be
discarded by restricting to divisorial valuations.
\end{example}
```
