# theorem thm:p148-v7-exact-live-integration

## statement

This is a conditional exact-text comparison, not a new
mathematical theorem or an assertion that this prompt authenticates a Git
revision.  Given that the source excerpts reproduced in this proof context
are exact current Chapter 51/72 and inventory texts, those excerpts establish
precisely the two assertions in the supplied frozen P14.8 V6 statement:

1. For a realizable \(\mathcal I\)-class \(d=[\varphi]_{\mathcal I}\) in
   \(\operatorname{{PSH}}(X,\theta)\),
   \(\mathcal R_\theta(d)=P_\theta[\varphi]_{{\mathcal I}}\) is well defined
   and is the unique normalized \(\mathcal I\)-model representative in that
   class, without a positive-nonpluripolar-mass hypothesis.
2. On \(\mathbf P^1\), the live polar-Cantor family \(\varphi_s\),
   \(0\le s\le1\), is contained in one \(\mathcal I\)-class and has raw
   nonpluripolar mass \(1-s\).  Hence its endpoint of raw mass zero has the
   canonical normalized \(\mathcal I\)-model representative \(0\), of mass
   one; neither a raw representative nor its raw mass descends to the
   \(\mathcal I\)-quotient.

The comparison asserts no realization result for arbitrary formal ideal data,
no all-semivaluation formula, no DXZ terminal-slice result, and no extension
to a different setting.  The supplied Chapter 72 and inventory excerpts keep
P14.8 open; this review does not retire it.  The separately generated
`RELEASE_PINS.json` is provenance metadata for a local integrity check, not
an authenticated premise of this model review.


## proof

### Comparison target and provenance boundary

The indented V6 statement below is supplied solely as the frozen text against
which the reproduced Chapter 51 result is compared.  No previous verifier
receipt, hash, or Git identity is used as an authenticated mathematical
premise in this review.  The JSON block at the end is explicitly untrusted
local provenance metadata; the packet's separate `check_packet.py` verifies
it against the working tree before submission.

The question for this review is therefore narrow: assuming the reproduced
source excerpts are faithful, do they state and prove the same positive and
negative dichotomy as the supplied V6 target text, without broadening it?

### Audit argument

The live standing hypotheses supply the compact K\"ahler ambient setting and
smooth background form.  The \(\mathcal I\)-preorder defines equality of
complete integral multiplier-ideal towers, while the exact strong-openness
package supplies the needed converse: equality at every integral scale is
equivalent to equality of all divisorial Lelong numbers.  Thus the projection
proof's finite-maximum and increasing-envelope steps preserve the required
\(\mathcal I\)-class; this does not rely merely on the one-way valuative
criterion.  The live projection theorem then proves membership and
idempotence.  Its corollary establishes exactly the V6 positive assertion:
the construction depends only on the realizable class, is normalized, and a
normalized fixed point in that class is unique, with no positive-mass
assumption.

The live Cantor lemma chooses \(\ell_0=1\) and
\(\ell_m=\mathrm e^{{-4^m}}\) for \(m\ge1\), including the child-fitting and
capacity-divergence checks.  The live example then makes the full family
\(\varphi_s=sG_\mu\), proves zero Lelong numbers and therefore
\(\mathcal I(m\varphi_s)=\mathcal O_X\), and therefore places all members in
one \(\mathcal I\)-class.  The included bidegree-one identity and ledger
give the nonpluripolar mass calculation \(1-s\); no \(P\)-equivalence claim
is needed for this audit.  The example identifies the envelope of the common
class with \(0\), and its endpoint sentence is exactly V6's
non-reconstruction conclusion.

The Chapter 72 and inventory excerpts preserve the same exclusions: the
terminal filtration corollary is not being reused to reconstruct an arbitrary
zero-mass potential, and P14.8 is not declared retired by this audit.  Thus
the comparison neither adds a theorem nor promotes the result beyond the two
stated readings.

### Frozen V6 target statement (comparison-only)

The following indented block is a verbatim copy of `STATEMENT_V6.md`.
Indentation prevents it from being parsed as a second theorem item in this
audit.

    Let $X$ be a connected compact Kähler manifold, and let $\theta$ be a smooth
    closed real $(1,1)$-form such that $\operatorname{PSH}(X,\theta)\ne\varnothing$.
    Write
    
    $$
    \mathscr D_{\mathcal I}(X,\theta)
    :=\operatorname{PSH}(X,\theta)/{\sim_{\mathcal I}}
    $$
    
    for the set of *realizable* $\mathcal I$-data. Thus an element is induced by
    an actual $\varphi\in\operatorname{PSH}(X,\theta)$ and is represented by the
    tower $(\mathcal I(m\varphi))_{m\ge1}$, equivalently by its divisorial Lelong
    profile; it is not an arbitrary formal sequence of ideals. For
    $d=[\varphi]_{\mathcal I}$, define
    
    $$
    \mathcal R_\theta(d):=P_\theta[\varphi]_{\mathcal I}.
    $$
    
    **Theorem (P14.8 v5).**
    
    1. The map $\mathcal R_\theta$ is well defined and returns the unique
       normalized $\mathcal I$-model potential in the class $d$. Hence full
       realizable $\mathcal I$-data reconstructs its canonical normalized
       $\mathcal I$-model representative, with no hypothesis on nonpluripolar
       mass.
    
    2. Raw nonpluripolar mass is not part of $\mathcal I$-data. On
       $X=\mathbf P^1$, equipped with the Fubini--Study form $\omega$ normalized
       by $\int_X\omega=1$, there is one $\mathcal I$-class containing potentials
       $\varphi_s$, $0\le s\le1$, such that
    
       $$
       [\varphi_s]_{\mathcal I}=[0]_{\mathcal I},\qquad
       \int_X\left\langle\omega+\operatorname{dd}^c\varphi_s\right\rangle=1-s.
       $$
    
       In particular, the raw zero-mass representative $\varphi_1$ has canonical
       normalized $\mathcal I$-model representative $0$, whose mass is one. So
       neither a raw zero-mass representative nor its mass can be reconstructed
       from its $\mathcal I$-class.
    
    These settle the two defined readings of the former P14.8 wording: complete
    realizable $\mathcal I$-data determines the canonical normalized
    $\mathcal I$-model representative, while neither a raw representative nor
    its raw mass descends to the $\mathcal I$-quotient.
    
    **Scope.** On a smooth projective variety, the separate all-mass order
    isomorphism for full realized DXZ--Boucksom--Jonsson objects in a
    pseudoeffective real Néron--Severi class remains distinct. The literal
    all-semivaluation ideal formula is used only for a $\mathbf Q$-line-bundle
    class. This theorem asserts neither a compact-Kähler nor a genuinely
    transcendental extension of that result. Realization of arbitrary formal
    ideal or valuative data remains P14.1, and the P14.7 terminal-left-limit
    corollary is not used here.
    
    The exact source excerpts used by the proof are appended to its frozen V6
    packet: Boucksom's multiplier-ideal notes, BEGZ's nonpluripolar-product
    paper, and Kellay--Mashreghi, arXiv:1102.5596, formula (3.4), for the
    generalized-Cantor capacity criterion.
    


### Exact live Chapter 51 extract: ambient scope and comparisons

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
96–166.

```tex
consume and no more.  The division is recorded item by item in
\Cref{sec:ch51-interface}, so that a reader can check any later citation
against a single list.

\subsection{Four comparisons, and why there are four}
\label{sec:ch51-four}

Let \(\varphi\) and \(\psi\) be quasi-psh functions on \(X\).  Four
relations between them occur in this book, and each is used somewhere in
\cref{part:complex,part:comparisons}:
\begin{enumerate}
\item pointwise order, \(\varphi\leq\psi\);
\item ordinary singularity type, \(\varphi\preceq\psi\), meaning
      \(\varphi\leq\psi+O(1)\);
\item \(P\)-comparison, \(\varphi\preceq_P\psi\), meaning
      \(P_\theta[\varphi]\leq P_\theta[\psi]\);
\item \(\mathcal I\)-comparison, \(\varphi\preceq_{\mathcal I}\psi\),
      meaning \(\mathcal I(m\varphi)\subseteq\mathcal I(m\psi)\) for every
      \(m\geq1\).
\end{enumerate}
Each is coarser than the one before it, and the induced equivalence
relations \(=\), \(\sim\), \(\sim_P\), \(\sim_{\mathcal I}\) are
correspondingly coarser.  The four are genuinely distinct.  Bounded
perturbations separate the first from the second.  The function
\(-\log(-\log|z|^2)\) of \Cref{ex:appH-loglog} separates the second from
the third: it is unbounded, hence not ordinarily equivalent to \(0\), but
its \(P\)-envelope is \(0\).  \Cref{ex:ch51-cantor} separates the third
from the fourth, by exhibiting a potential all of whose Lelong numbers
vanish --- so that it is \(\mathcal I\)-equivalent to \(0\) --- but whose
nonpluripolar mass is \(1/2\) while the mass of \(0\) is \(1\).  The
\(P\)-projection theorem then forbids \(P\)-equivalence.

There is a useful mnemonic.  The relation \(\sim\) remembers the
potential up to a bounded error; \(\sim_P\) remembers exactly the
data that nonpluripolar masses and relative energies can see; and
\(\sim_{\mathcal I}\) remembers exactly the data that divisorial
valuations can see.  The last of these is what analytification produces
(\Cref{chap:valuative-analytification}), and it is also the datum on which
the analytic trace of \Cref{chap:operations-trace} depends.  The target of
that operator is nevertheless a \(P\)-class: every trace is
\(\mathcal I\)-good, and two choices are \(P\)-equivalent.  This upgrade
from \(\mathcal I\)-data at the source to \(P\)-uniqueness at the target is
a theorem about restricted quasi-equisingular approximants, not a formal
property of the three quotients.

\subsection{Standing hypotheses}
\label{sec:ch51-hypotheses}

Throughout, \(X\) is a connected compact K\"ahler manifold of complex
dimension \(n\), and \(\theta\) is a smooth closed real \((1,1)\)-form.
Three hypotheses are quantified explicitly at every statement rather than
assumed globally.

\emph{Positivity of the class.}  We distinguish pseudoeffective (some
closed positive current in \(\{\theta\}\)), big (some K\"ahler current),
nef, and K\"ahler.  These are not synonyms, and the difference is visible
already in \Cref{ex:ch51-blowup-mass}, where a big non-nef class on a
blown-up surface has \(\int_X\{\theta\}^2=0\) but nonpluripolar volume
\(1\).

\emph{Positivity of the mass.}  Several theorems below, in particular
\Cref{thm:complex-p-projection}, require
\(\int_X\langle\theta_\varphi^n\rangle>0\).  The book reserves the term
\emph{model potential} for the positive-mass case; the zero-mass regime is
handled in \Cref{chap:transcendental-metrics} by a directed system of
K\"ahler perturbations, and no statement of this chapter is silently
extended to it.

\emph{Smoothness of \(X\).}  The manifold is smooth.  Compact K\"ahler
\emph{spaces} appear from \Cref{chap:tropical-spectra-complex} onwards, and
the modifications needed there are introduced at that point.  Nothing in
```

### Exact live Chapter 51 extract: strong openness and Lelong recovery

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
1553–1638.

```tex
\subsection{Strong openness and the valuative criterion}
\label{sec:ch51-openness}

\refstepcounter{theorem}\label{thm:complex-strong-openness}
\begin{quote}
\textbf{Foundational input \thetheorem\ (strong openness and its
valuative package; source boundary).}
Let \(\varphi\) be quasi-psh.
\begin{enumerate}
\item\label{itm:ch51-so:openness} The strong openness identity holds:
      \[
      \mathcal I(\varphi)
       =\bigcup_{\epsilon>0}\mathcal I((1+\epsilon)\varphi).
      \tag{51.11}\label{eq:complex-strong-openness}
      \]
\item\label{itm:ch51-so:lelong} For every prime divisor \(E\) over \(X\),
      \[
      \nu(\varphi,E)
       =\lim_{m\to\infty}\frac1m
                    \ord_E\mathcal I(m\varphi).
      \tag{51.12}\label{eq:complex-lelong-from-ideals}
      \]
\item\label{itm:ch51-so:equivalence} For quasi-psh \(\varphi,\psi\), equality
      \(\mathcal I(m\varphi)=\mathcal I(m\psi)\) for all
      \(m\geq1\) is equivalent to equality
      \(\mathcal I(\lambda\varphi)=\mathcal I(\lambda\psi)\) for
      every \(\lambda>0\), and to
      \(\nu(\varphi,E)=\nu(\psi,E)\) for every prime divisor over \(X\).
\end{enumerate}
\par
Item \cref{itm:ch51-so:openness} is imported from
\cite[Theorem~1.1]{GZ15}; item \cref{itm:ch51-so:lelong} uses Demailly's
approximation theorem \cite{Dem92reg}; and item
\cref{itm:ch51-so:equivalence} uses Boucksom's valuative criterion
\cite[Corollary~10.18]{Bou17}.  These analytic inputs are not reproved
here.  The deductions and normalization checks are recorded below.
\end{quote}

Before the proof we isolate the imported valuative statement, in the exact
form in which it is used, and check its normalization.

\refstepcounter{proposition}\label{prop:ch51-valuative-criterion}
\begin{quote}
\textbf{Foundational input \theproposition\ (valuative criterion for
multiplier ideals; source boundary).}
Let \(\varphi\) be quasi-psh on \(X\), let \(\lambda>0\), let \(U\subseteq
X\) be open, and let \(f\in\cO_X(U)\).  For a prime divisor \(E\) over
\(X\), write \(A(E)\) for its log discrepancy, that is,
\(A(E)=1+\ord_E(K_{Y/X})\) for any modification \(\pi:Y\to X\) on which
\(E\) appears.  Then
\[
 f\in\mathcal I(\lambda\varphi)(U)
 \quad\Longleftrightarrow\quad
 \begin{aligned}[t]
 &\text{there is }\eta>0\text{ such that}\\
 &\ord_E(f)\geq(1+\eta)\lambda\,\nu(\varphi,E)-A(E)\\
 &\text{for every prime divisor }E\text{ over }U .
 \end{aligned}
\]
In particular \(\mathcal I(\lambda\varphi)\) is determined by the family
\((\nu(\varphi,E))_E\).
This equivalence is imported from \cite[Corollary~10.18]{Bou17}; no proof
is claimed here.  We only check its normalization.

This is \cite[Corollary~10.18]{Bou17}.  That source normalizes Lelong
numbers by \(\log|z|\) and multiplier ideals by the weight
\(\rme^{-2\varphi}\); the substitution
\(\varphi\rightsquigarrow\lambda\varphi/2\) converts its statement into the
displayed one, both rescalings being applied simultaneously as required by
\Cref{warn:ch51-half-log}.  Two unit tests confirm the result.  First, with
\(\varphi=\log|z|^2\) on the unit disk, the only relevant divisor is
\(E=\{0\}\) with \(A(E)=1\) and \(\nu(\varphi,E)=1\); the criterion reads
\(\ord_0(f)\geq(1+\eta)\lambda-1\) for some \(\eta>0\), that is
\(\ord_0(f)>\lambda-1\), which reproduces
\eqref{eq:complex-multiplier-example} including the endpoint behaviour at
\(\lambda\in\mathbf Z\).  Second, for \(f=1\) the criterion says
\(\mathcal I(\lambda\varphi)=\cO_X\) exactly when
\(\lambda<\inf_EA(E)/\nu(\varphi,E)\), which is the standard valuative
formula for the log canonical threshold of \Cref{ex:ch51-lct}.  The single
\(\eta\), uniform over all \(E\), is essential; replacing it by pointwise
strict inequalities gives a strictly larger set of \(f\).
\end{quote}

\paragraph{Deductions and normalization checks.}
\emph{Item \cref{itm:ch51-so:openness}.}  The inclusion \(\supseteq\) is
\Cref{prop:ch51-ideal-formal}, item \cref{itm:ch51-if:scale}.  The
```

### Exact live Chapter 51 extract: \(\mathcal I\)-preorder

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
3210–3237.

```tex

\subsection{The \texorpdfstring{\(\mathcal I\)}{I}-preorder}
\label{sec:ch51-i-preorder}

\begin{definition}[\(\mathcal I\)-preorder]
\label{def:complex-i-preorder}
For quasi-psh \(\varphi,\psi\), write
\[
 \varphi\preceq_{\mathcal I}\psi
 \quad\Longleftrightarrow\quad
 \mathcal I(m\varphi)\subseteq\mathcal I(m\psi)
 \quad\text{for every }m\geq1.
\tag{51.26}\label{eq:complex-i-preorder}
\]
Equivalently, \(\nu(\varphi,E)\geq\nu(\psi,E)\) for every prime divisor
over \(X\).  Write \(\varphi\sim_{\mathcal I}\psi\) for equality in both
directions.
\end{definition}

The asserted equivalence of the two descriptions is
\Cref{thm:complex-strong-openness}, item
\cref{itm:ch51-so:equivalence}, applied to the pair of one-sided
statements; note that the ideal inclusion and the Lelong inequality point
in opposite directions, because a more singular potential has larger
Lelong numbers and smaller multiplier ideals.  Reading the direction
backwards is the commonest error in this circle of ideas, and it is
detected by the one-pole test of \Cref{sec:ch51-unit-tests}: with
\(\varphi=\log|z|^2\) and \(\psi=0\) one has
```

### Exact live Chapter 51 extract: envelope, projection, and reconstruction

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
3290–3461.

```tex

\begin{definition}[\(\mathcal I\)-envelope]
\label{def:complex-i-envelope}
For \(\varphi\in\PSH(X,\theta)\), set
\[
 P_\theta[\varphi]_{\mathcal I}
 :=\uscsup\{\psi\in\PSH(X,\theta)\mid
          \psi\leq0,\ \psi\sim_{\mathcal I}\varphi\}.
\tag{51.27}\label{eq:complex-i-envelope}
\]
It is \(\mathcal I\)-model if it is fixed by this operator.
\end{definition}

\begin{theorem}\label{thm:complex-i-projection}
For every \(\varphi\in\PSH(X,\theta)\),
\[
 \varphi\sim_{\mathcal I}P_\theta[\varphi]_{\mathcal I},
\qquad
 P_\theta[P_\theta[\varphi]_{\mathcal I}]_{\mathcal I}
      =P_\theta[\varphi]_{\mathcal I}.
\tag{51.28}\label{eq:complex-i-projection}
\]
Furthermore,
\[
 P_\theta[\varphi]\leq P_\theta[\varphi]_{\mathcal I},
\qquad
 \varphi\sim_{\mathcal I}P_\theta[\varphi].
\tag{51.29}\label{eq:complex-p-i-comparison}
\]
If \(\varphi\) has analytic singularities, then
\[
 \varphi\sim P_\theta[\varphi]
        \sim P_\theta[\varphi]_{\mathcal I}.
\tag{51.30}\label{eq:complex-analytic-envelope-agreement}
\]
\end{theorem}

\begin{proof}
Choquet reduction replaces the family in
\eqref{eq:complex-i-envelope} by an increasing sequence.  Finite maxima
preserve divisorial Lelong numbers, and strong openness shows that its
usc supremum has the same multiplier ideals as \(\varphi\).  This proves
\eqref{eq:complex-i-projection}.  Formula
\eqref{eq:complex-p-envelope-rooftop}, again with strong openness, gives
\(\varphi\sim_{\mathcal I}P_\theta[\varphi]\), hence
\eqref{eq:complex-p-i-comparison}.  For analytic singularities, pass to
a log resolution.  Divisorial orders then control the whole singularity
up to \(O(1)\), so the two envelopes cannot be strictly less singular
than \(\varphi\).
\end{proof}

\begin{proof}[The steps in full]
Write \(F:=\{\psi\in\PSH(X,\theta)\mid\psi\leq0,\
\psi\sim_{\mathcal I}\varphi\}\) for the competitor family in
\eqref{eq:complex-i-envelope}.

\emph{Step 1: \(F\) is nonempty and directed.}  It contains
\(\varphi-\sup_X\varphi\).  If \(\psi_1,\psi_2\in F\), then
\(\max\{\psi_1,\psi_2\}\in\PSH(X,\theta)\) by
\Cref{prop:ch51-psh-operations}, item \cref{itm:ch51-op:max}, it is
\(\leq0\), and by \Cref{prop:ch51-lelong-calculus}, item
\cref{itm:ch51-lc:max}, applied at a generic point of each prime divisor
\(E\) over \(X\),
\[
 \nu(\max\{\psi_1,\psi_2\},E)
 =\min\{\nu(\psi_1,E),\nu(\psi_2,E)\}
 =\nu(\varphi,E).
\]
Hence \(\max\{\psi_1,\psi_2\}\in F\), and \(F\) is directed.

\emph{Step 2: the envelope lies in \(F\), which gives
\eqref{eq:complex-i-projection}.}  By Step 1 and
\Cref{lem:ch51-lelong-increasing},
\[
 \nu\bigl(P_\theta[\varphi]_{\mathcal I},E\bigr)
 =\inf_{\psi\in F}\nu(\psi,E)
 =\nu(\varphi,E)
\]
for every prime divisor \(E\) over \(X\).  Since
\(P_\theta[\varphi]_{\mathcal I}\leq0\), this says
\(P_\theta[\varphi]_{\mathcal I}\in F\); it is therefore the largest
element of \(F\), and in particular
\(\varphi\sim_{\mathcal I}P_\theta[\varphi]_{\mathcal I}\).  As \(F\)
depends only on the \(\mathcal I\)-class of \(\varphi\), the family
attached to \(P_\theta[\varphi]_{\mathcal I}\) is the same \(F\), and
idempotence follows.

\emph{Step 3: \(\varphi\sim_{\mathcal I}P_\theta[\varphi]\).}  By Step 1
of the proof of \Cref{thm:complex-p-projection}, the rooftops
\(u_C=(\varphi+C)\wedge_\theta V_\theta\) satisfy \(u_C\sim\varphi\) for
\(C\) large, hence \(\nu(u_C,E)=\nu(\varphi,E)\) for every \(E\) by
\Cref{prop:ch51-lelong-calculus}, item \cref{itm:ch51-lc:bounded}.  The
family \((u_C)\) is increasing, and
\(P_\theta[\varphi]=\uscsup_Cu_C\); so
\Cref{lem:ch51-lelong-increasing} gives
\(\nu(P_\theta[\varphi],E)=\nu(\varphi,E)\), which is the second half of
\eqref{eq:complex-p-i-comparison}.  This step uses no positivity of
mass.

\emph{Step 4: \(P_\theta[\varphi]\leq P_\theta[\varphi]_{\mathcal I}\).}
By Step 3 and \(P_\theta[\varphi]\leq V_\theta\leq0\), the potential
\(P_\theta[\varphi]\) belongs to \(F\); by Step 2 it is therefore at most
the largest element of \(F\).

\emph{Step 5: analytic singularities.}  Assume \(\varphi\) has analytic
singularities, and let \(\rho:Z\to X\) be a log resolution with
\[
 \rho^*\varphi=c\log|s_D|_h^2+O(1),
\]
\(D\) an effective divisor with simple normal crossing support, \(h\) a
smooth metric on \(\cO_Z(D)\), and \(c>0\).  Put
\(\Psi:=P_\theta[\varphi]_{\mathcal I}\), which by Step 2 satisfies
\(\Psi\sim_{\mathcal I}\varphi\).  By
\Cref{prop:ch51-divisorial-calculus}, items
\cref{itm:ch51-dc:pullback} and \cref{itm:ch51-dc:analytic}, for every
prime divisor \(E\subset Z\),
\[
 \nu(\rho^*\Psi,E)=\nu(\Psi,E)=\nu(\varphi,E)=c\,\ord_E(D).
\]
The Siu decomposition of \Cref{sec:ch51-divisorial}, applied to the
closed positive current \(\rho^*\theta+\ddc\rho^*\Psi\), therefore gives
\[
 \rho^*\theta+\ddc\rho^*\Psi\ \geq\ c\,[D].
\]
Writing \(\Theta_D=c_1(\cO_Z(D),h)\) and using Poincar\'e--Lelong
\eqref{eq:appJ-complex-section-pl} in the form
\(\ddc\log|s_D|_h^2=[D]-\Theta_D\), we obtain
\[
 \bigl(\rho^*\theta-c\,\Theta_D\bigr)
 +\ddc\bigl(\rho^*\Psi-c\log|s_D|_h^2\bigr)\ \geq\ 0 ,
\]
so \(\rho^*\Psi-c\log|s_D|_h^2\) is quasi-psh on the compact manifold
\(Z\), hence bounded above.  Thus
\(\rho^*\Psi\leq c\log|s_D|_h^2+C=\rho^*\varphi+C'\), and since \(\rho\)
is an isomorphism over a dense open subset of \(X\) and both sides are
upper semicontinuous, \(\Psi\preceq\varphi\).  Combining with
\(\varphi\preceq P_\theta[\varphi]\leq\Psi\) from
\Cref{prop:ch51-p-elementary}, item \cref{itm:ch51-pe:above}, and Step 4,
\[
 \varphi\ \sim\ P_\theta[\varphi]\ \sim\ P_\theta[\varphi]_{\mathcal I},
\]
which is \eqref{eq:complex-analytic-envelope-agreement}.
\end{proof}

\begin{corollary}[Canonical reconstruction from realizable
\texorpdfstring{\(\mathcal I\)}{I}-data]
\label{cor:ch51-i-canonical-reconstruction}
For a realizable \(\mathcal I\)-class
\(d=[\varphi]_{\mathcal I}\) in \(\PSH(X,\theta)\), the formula
\[
 \mathcal R_\theta(d):=P_\theta[\varphi]_{\mathcal I}
\]
is well defined.  It is the unique \(\mathcal I\)-model potential in the
class \(d\) with \(\sup_X\mathcal R_\theta(d)=0\).  Thus realizable
\(\mathcal I\)-data determines its canonical normalized
\(\mathcal I\)-model representative, without a positive-mass hypothesis.
\end{corollary}

\begin{proof}
The competitor family in \eqref{eq:complex-i-envelope} depends only on
\(d\).  The proof of \Cref{thm:complex-i-projection} shows that its
envelope lies in that family and is its largest element; the formula is
therefore well defined.  The second identity in that theorem says that the
output is \(\mathcal I\)-model.  It is at most zero by
\eqref{eq:complex-i-envelope}.  If its supremum were strictly negative,
adding a sufficiently small positive constant would give another competitor
in the same defining family, contradicting maximality.  Finally, a
normalized \(\mathcal I\)-model potential in the class \(d\) is the fixed
point of the envelope attached to that same competitor family, and hence is
\(\mathcal R_\theta(d)\).
\end{proof}

```

### Exact live Chapter 51 extract: polar-Cantor family

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
3780–3885.

```tex

\subsection{A potential that is
\texorpdfstring{\(\mathcal I\)}{I}-equivalent, but not
\texorpdfstring{\(P\)}{P}-equivalent, to zero}
\label{sec:ch51-cantor}

The construction uses one classical input: a compact set of vanishing
logarithmic capacity carrying a probability measure without atoms.  We
recall it explicitly so that the numbers below can be checked.

\begin{lemma}\label{lem:ch51-polar-cantor}
Let \((\ell_m)_{m\geq0}\) be lengths with \(\ell_0=1\) and
\(\ell_{m+1}\leq\ell_m/2\), and let
\(F=\bigcap_mF_m\subset[0,1]\subset\mathbf C\) be the generalized Cantor
set in which \(F_m\) is a disjoint union of \(2^m\) closed intervals of
length \(\ell_m\), each containing two intervals of the next stage.  Let
\(\mu\) be the measure giving each of the \(2^m\) intervals of \(F_m\)
mass \(2^{-m}\).  Then \(\mu\) is a nonatomic Borel probability measure
carried by \(F\), and if
\[
 \sum_{m\geq0}2^{-m}\log\frac{1}{\ell_m}=+\infty ,
\]
then \(F\) has vanishing logarithmic capacity, hence is polar.  The
choice \(\ell_0=1\) and \(\ell_m=\rme^{-4^m}\) for \(m\geq1\)
satisfies both hypotheses, since the summands for \(m\geq1\) equal \(2^m\).
\end{lemma}

\begin{proof}[Classical, with the divergence check]
The measure \(\mu\) is the weak limit of the normalized Lebesgue measures
on \(F_m\); it is nonatomic because every point of \(F\) lies in nested
intervals of \(\mu\)-mass \(2^{-m}\to0\).  The capacity criterion for
generalized Cantor sets is \cite[p.~31]{Car83}: the set is polar exactly
when the displayed series diverges.  With \(\ell_0=1\) and
\(\ell_m=\rme^{-4^m}\) for \(m\geq1\), one has
\(\ell_1/\ell_0=\rme^{-4}\leq1/2\); for \(m\geq1\),
\(\ell_{m+1}/\ell_m=\rme^{-3\cdot4^m}\leq1/2\) and
\(2^{-m}\log(1/\ell_m)=2^m\), so the series diverges.
\end{proof}

\begin{example}[\(\mathcal I\)-equivalent, not \(P\)-equivalent]
\label{ex:ch51-cantor}
Let \(X=\mathbf P^1\) with \(\omega=\ddc\log(1+|z|^2)\), normalized by
\(\int_X\omega=1\), and let \(G_p\) be the Green function of
\Cref{sec:ch51-unit-tests}, so that
\[
 G_p(z)=\log\frac{|z-p|^2}{(1+|z|^2)(1+|p|^2)}\leq0,
 \qquad
 \omega+\ddc G_p=\delta_p .
\]
Let \(F\) and \(\mu\) be as in \Cref{lem:ch51-polar-cantor}, and set
\[
 G_\mu(z):=\int_XG_p(z)\,\rd\mu(p).
\]

For \(0\leq s\leq1\), put \(\varphi_s:=sG_\mu\).

\emph{The \(\varphi_s\) are genuine potentials.}  Each \(G_p\leq0\), so
\(G_\mu\leq0\).  For \(z\) at chordal distance at least \(\delta\) from
\(F\) one has \(G_p(z)\geq2\log\delta\) for every \(p\in F\), so
\(G_\mu(z)\geq2\log\delta>-\infty\); in particular
\(G_\mu\not\equiv-\infty\).  Fubini gives
\[
 \omega+\ddc G_\mu=\mu ,
 \qquad
 \omega+\ddc\varphi_s=(1-s)\omega+s\mu\ \geq0,
\]
so \(\varphi_s\in\PSH(X,\omega)\) with \(\varphi_s\leq0\).

\emph{All Lelong numbers vanish.}  On a Riemann surface every
modification is an isomorphism, so the prime divisors over \(X\) are the
points of \(X\), and
\Cref{prop:ch51-lelong-three}, item \cref{itm:ch51-lelong:mass}, gives
\[
 \nu(\varphi_s,x)=(\omega+\ddc\varphi_s)(\{x\})
 =(1-s)\omega(\{x\})+s\mu(\{x\})=0
\]
for every \(x\), because \(\omega\) is smooth and \(\mu\) is nonatomic.
By \Cref{thm:complex-strong-openness}, item
\cref{itm:ch51-so:equivalence}, or directly by Skoda's bound
\Cref{prop:ch51-lelong-calculus}, item \cref{itm:ch51-lc:smooth}, applied
to \(m\varphi_s\) for every \(m\),
\[
 \mathcal I(m\varphi_s)=\cO_X\quad(m\geq1),
 \qquad\text{hence}\qquad
 \varphi_s\sim_{\mathcal I}0 .
\]

\emph{The nonpluripolar mass is \(1-s\).}  The set \(F\) is polar,
hence pluripolar, and \(\mu(F)=1\).  Also \(\omega(F)=0\), since \(F\)
has vanishing Lebesgue measure.  By
\Cref{lem:ch51-npp-bidegree-one} and
\Cref{thm:complex-npp-ledger}, the nonpluripolar product charges no
pluripolar set, so
\[
 \MA_\omega(\varphi_s)
 =\one_{X\setminus F}\bigl((1-s)\omega+s\mu\bigr)
 =(1-s)\omega,
 \qquad
 M_\omega(\varphi_s)=1-s .
\]
The envelope of \(0\) is \(0\), since \(0\) is a competitor and every
competitor is at most zero.  Thus one \(\mathcal I\)-class carries every
mass in \([0,1]\), while
\Cref{cor:ch51-i-canonical-reconstruction} identifies its canonical
normalized \(\mathcal I\)-model representative with \(0\), of mass one.

```

### Exact live Chapter 51 extract: bidegree-one product

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
2112–2154.

```tex
\subsection{Bidegree one}
\label{sec:ch51-npp-bidegree-one}

In bidegree \((1,1)\) the nonpluripolar product has a completely explicit
description, and every mass computation in this chapter uses it.

\begin{lemma}\label{lem:ch51-npp-bidegree-one}
Let \(\varphi\in\PSH(X,\theta)\).  Then
\[
 \langle\theta_\varphi\rangle
 =\one_{\{\varphi>-\infty\}}\,\theta_\varphi
\]
as measures on \(X\) when \(n=1\), and as currents in general.  In
particular \(\langle\theta_\varphi\rangle\leq\theta_\varphi\), the two
agree if and only if \(\theta_\varphi\) puts no mass on the pluripolar
set \(\{\varphi=-\infty\}\), and, for \(n=1\),
\[
 M_\theta(\varphi)
 =\int_X\theta_\varphi-\theta_\varphi(\{\varphi=-\infty\})
 =\int_X\{\theta\}-\theta_\varphi(\{\varphi=-\infty\}).
\]
\end{lemma}

\begin{proof}
Take \(p=1\) in \eqref{eq:complex-npp-truncation}.  With
\(O_k=\{\varphi>-k\}\) and \(\varphi_k:=\max\{\varphi,-k\}\), plurifine
locality gives
\[
 \one_{O_k}\theta_\varphi=\one_{O_k}\theta_{\varphi_k}
\]
for every \(k\), since \(\varphi=\varphi_k\) on \(O_k\).  The sets
\(O_k\) increase to \(\{\varphi>-\infty\}\), so the increasing limit of
the left-hand sides is \(\one_{\{\varphi>-\infty\}}\theta_\varphi\), while
the increasing limit of the right-hand sides is by definition
\(\langle\theta_\varphi\rangle\).  The inequality
\(\langle\theta_\varphi\rangle\leq\theta_\varphi\) and the criterion for
equality are immediate, and the mass formula for \(n=1\) follows because
then \(\theta_\varphi\) is a positive measure of total mass
\(\int_X\{\theta\}\), by Stokes.
\end{proof}

\begin{remark}[The higher-degree analogue fails]
\label{rem:ch51-npp-no-restriction}
```

### Exact live Chapter 51 extract: nonpluripolar ledger

Source: `manuscript/parts/part5/ch51_complex_prerequisites.tex`, lines
2168–2185.

```tex
\subsection{The ledger}
\label{sec:ch51-npp-ledger}

\begin{theorem}\label{thm:complex-npp-ledger}
The product \eqref{eq:complex-global-npp} is a closed positive
\((p,p)\)-current.  It is symmetric and multilinear in the currents,
local for the plurifine topology, agrees with the Bedford--Taylor
product for locally bounded potentials, and charges no pluripolar set.
If \(\varphi_j\) is replaced by a less singular potential in the same
class, every mixed total mass can only increase.  Proper bimeromorphic
pullback preserves total masses.
\end{theorem}

\begin{proof}[Why truncation is sufficient]
Plurifine locality makes the truncations in
\eqref{eq:complex-npp-truncation} compatible.  Their masses on relatively
compact sets are uniformly controlled after wedging with a K\"ahler
form, so the increasing limit is locally finite.  Bedford--Taylor
```

### Exact live Chapter 72 status boundary

Source: `manuscript/parts/part6/ch72_major_open_problems.tex`, lines
2861–2892.

```tex
The terminal left-limit consequence in
\Cref{cor:pseff-terminal-filtration-slice} does not reconstruct an arbitrary
zero-mass potential.  The separate atom P14.8 therefore remains active.  A
frozen exact-dichotomy candidate now specifies its input as a realizable
\(\mathcal I\)-class in a compact K\"ahler class, its target as the normalized
\(\mathcal I\)-model representative, and its reconstruction map as the
corresponding \(\mathcal I\)-envelope.  Its independently audited proof gives
the positive reconstruction result for that canonical representative and a
polar Cantor-family obstruction to reconstructing a raw representative or
its raw nonpluripolar mass.  An exact primary-source v4 packet has received a
zero-finding independent verification of this proof.  A later three-source
v5 successor makes the generalized-Cantor capacity interface explicit through
the frozen Kellay--Mashreghi formula and has also received a final
zero-finding review.  The source-bound V6 successor appends the exact
Boucksom sequential/valuative-Lelong, BEGZ locality/polar-set, and
Kellay--Mashreghi capacity excerpts to its frozen proof.  Its independent
model-backed review returned final \texttt{correct}, with zero critical
errors and zero gaps, for item
\nolinkurl{pi_af3d4e7db16b025b3ed90770}.  Its statement and proof SHA-256
values are
\begin{center}
\small
\begin{tabular}{@{}c@{}}
\nolinkurl{4e4256d738ec65dea040e82b3b40bffb233197e9f466c07166760196cc13c04e}\\
\nolinkurl{a51d3e150958265f8b2aa0067d8cf7d64a6c68e14d65e6520fed52bb94489648}.
\end{tabular}
\end{center}
The exact reconstruction and the full Cantor family are now recorded in
\Cref{cor:ch51-i-canonical-reconstruction,ex:ch51-cantor}.  The separate
exact-live integration audit remains, so P14.8 does not retire or change the
inventory count.  It is not a second zero-mass interval strictly before
\(\tau_L(\mathcal F)\).
```

### Exact live inventory status boundary

Source: `manuscript/editorial/open_problem_atomic_inventory_20260824.md`,
lines 892–929.

```markdown
- **P14.8** `[T5; open; source-bound exact dichotomy verified]` A
  frozen, independently audited candidate specifies reconstruction from a
  realizable \(\mathcal I\)-class in a compact K\"ahler class to its canonical
  normalized \(\mathcal I\)-model representative.  It proves that this
  canonical representative is reconstructible, while a polar Cantor family
  shows that neither a raw representative nor raw nonpluripolar mass descends
  to the \(\mathcal I\)-quotient.  The source-bound V6 packet appends the
  exact Boucksom, BEGZ, and Kellay--Mashreghi extracts and passed final
  independent model-backed review as `pi_af3d4e7db16b025b3ed90770`, with zero
  critical errors and zero gaps.  A separate exact-live integration audit
  remains required; this is not a zero-mass strict-interior range of the DXZ
  filtration curve.

The divisorial realization, the finite-energy K\"ahler comparison, and the
projective real N\'eron--Severi DXZ--Boucksom--Jonsson comparison are known
in their stated domains.  P14.7 is retired by
`thm:pseff-filtration-maximality`, which proves raw maximality for every
strict-interior parameter without finite generation.  The equality of the
ordinary and multiplier-ideal envelopes remains attributed to DXZ,
Lemma 4.5.  Finski's March 2026 approximation theorem
[arXiv:2603.22194v1, Theorem 4.3](https://arxiv.org/html/2603.22194v1)
provides a separate published route after identifying its resolved envelope
with the DXZ ordinary envelope.  This is an explicitly attributed inference,
not a claim that Finski states the DXZ conjecture verbatim.

P14.8 remains active and separate.  The terminal left-limit corollary
`cor:pseff-terminal-filtration-slice` applies only to the particular DXZ
terminal slice; it does not reconstruct arbitrary zero-mass data.  The
frozen exact-dichotomy candidate in
`solver_dossiers_20260901/p148_zero_mass_reconstruction_candidate_v2_20260901`
is a source-scoped answer to the two defined reconstruction readings, but it
is not yet a production-verified retirement and not a sourced second interval
of zero-mass slices.
The exact source comparison is preserved in
`solver_dossiers_20260831/p147_source_correction_independent_audit_20260831/SOURCE_CORRECTION_AUDIT.md`.
That source-only correction did not itself retire an atom; the complete
proof integrated in Chapter 71 is the retirement basis used here.

```

### Untrusted local provenance metadata

```json
{
  "files": {
    "chapter51": {
      "path": "manuscript/parts/part5/ch51_complex_prerequisites.tex",
      "sha256": "e9cfd36efc6a202cb1f320bac5297085ae3417dfcdc73ff0f054c7fef75e01d1"
    },
    "chapter72": {
      "path": "manuscript/parts/part6/ch72_major_open_problems.tex",
      "sha256": "71739091c63272c98edfbbae26659f9e2167d992a025134e61450f68f5bf9871"
    },
    "inventory": {
      "path": "manuscript/editorial/open_problem_atomic_inventory_20260824.md",
      "sha256": "34251488bbbb3a792e763aeb18787b56d99afaaa9be08908fe282039b69d2bd8"
    },
    "v6_statement": {
      "path": "manuscript/editorial/solver_dossiers_20260909/p148_v6_source_closed_packet_20260909/STATEMENT_V6.md",
      "sha256": "4e4256d738ec65dea040e82b3b40bffb233197e9f466c07166760196cc13c04e"
    }
  },
  "git_head": "ff333ee24648faa9ae23cf8d87a4bea1ec62e961",
  "ranges": {
    "ch51_cantor_family": [
      3780,
      3885
    ],
    "ch51_i_envelope_and_projection": [
      3290,
      3461
    ],
    "ch51_i_preorder": [
      3210,
      3237
    ],
    "ch51_npp_bidegree_one": [
      2112,
      2154
    ],
    "ch51_npp_ledger": [
      2168,
      2185
    ],
    "ch51_scope_and_comparisons": [
      96,
      166
    ],
    "ch51_strong_openness": [
      1553,
      1638
    ],
    "ch72_p148_status": [
      2861,
      2892
    ],
    "inventory_p148_status": [
      892,
      929
    ]
  },
  "v6_statement_sha256": "4e4256d738ec65dea040e82b3b40bffb233197e9f466c07166760196cc13c04e"
}
```
