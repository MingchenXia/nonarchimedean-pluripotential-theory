# Dossier: A P-valued refinement of analytic trace

> **Superseded source audit (23 August 2026).**  The supplied complete trace
> chapter already proves the positive statement: trace depends only on the
> input \(\mathcal I\)-class, every output is \(\mathcal I\)-good, and two
> outputs are \(P\)-equivalent.  Equivalently, the source provides
> \(D_Y/{\sim_{\mathcal I}}\to\QPSH(\widetilde Y)/{\sim_P}\).  The former
> book problem was therefore removed from the active open-problem inventory.
> This dated dossier is retained only as a record of an audit performed from
> incomplete web-extracted source text; its ``open'' and
> ``candidate-proposition'' dispositions are not current mathematical
> claims and carry no Rethlas receipt.

Date: 2026-08-15. Solver-stage output for the packet
`/home/claude/work/refs/trace_p_valued_refinement.md`; book environment:
`ch72_major_open_problems.tex`, `prob:frontier-trace-p` (lines 1555–1590);
supporting book chapters: `ch54_operations_trace.tex` (Def 54.21–Thm 54.26),
`ch67_functoriality_trace.tex` (Thms `functor-split-trace`,
`functor-retraction-trace`, diagram (67.19)).

Integrity notes. All quotations from arXiv sources below were obtained on
2026-08-15 through the WebFetch channel (arXiv HTML renderings, extracted by an
intermediate summarizer); direct download was proxy-blocked. Quotations are
faithful to the fetched text but numbering/wording carries a residual
transcription risk; items so obtained are tagged [F]. Items I could not
confirm verbatim are tagged UNCONFIRMED with my best reconstruction. No
priority is claimed for any statement; several "proved here" items are likely
known to the authors of the sources. Dispositions are candidate-only; nothing
is promoted (no Rethlas receipt exists for any statement below).

---

## Stage 1. Status audit

**Sourced statement (exact scope).** Xia, *Operations on transcendental
non-Archimedean metrics*, arXiv:2312.17150v3 [F]:

- Definition 2.11 [F]: "Suppose that \(\varphi\) has analytic singularities,
  then we let \(\mathrm{Tr}_E(\varphi)=\varphi|_{\widetilde E}\). In general,
  fix a Kähler form \(\omega\) on \(X\) and take a quasi-equisingular
  approximation \((\varphi_j)_j\) of \(\varphi\) in
  \(\mathrm{PSH}(X,\theta+\omega)\). We define \(\mathrm{Tr}_E(\varphi)\) as a
  \(d_S\)-limit of \(\varphi_j|_{\widetilde E}\)." Here \(E\) is an
  irreducible reduced closed subspace, \(\widetilde E\) its normalization.
- Proposition 2.12 [F]: "Given \(\varphi\in\mathrm{PSH}(X,\theta)\) with
  \(\nu(\varphi,E)=0\), its trace operator \(\mathrm{Tr}_E(\varphi)\) as a
  quasi-psh function on \(\widetilde E\) is well-defined up to
  \(\mathcal I\)-equivalence. Moreover, \(\mathrm{Tr}_E(\varphi)\) depends
  only on the \(\mathcal I\)-equivalence class of \(\varphi\)." Plus the
  sequential \(d_S\)-continuity clause along decreasing \(\mathcal I\)-good
  sequences. The trace construction is cited to [DX24].
- Definition 2.3 [F] (\(\mathcal I\)-good): \(\int_X\theta_\varphi^n>0\) and
  \(P_\theta[\varphi]=P_\theta[\varphi]_{\mathcal I}\).

**The decisive upstream source.** [DX24] = Darvas–Xia, *The trace operator of
quasi-plurisubharmonic functions on compact Kähler manifolds*,
arXiv:2403.08259 (v2). Standing setting of §3 [F]: "Let \(X\) be a connected
compact Kähler manifold" — no projectivity in §3; \(Y\subseteq X\) a connected
complex submanifold of dimension \(m\); \(\mathrm{PSH}_>(X,\theta)\) :=
potentials \(u\) with \(\theta_u:=\theta+dd^cu\) a Kähler current [F].

- Theorem 2.2 [F] (Demailly-type approximation): there is
  \(u_k^D\in\mathrm{PSH}(X,\theta+\varepsilon_k\omega)\),
  \(\varepsilon_k\searrow0\), \(u_k^D\searrow u\), analytic singularity
  types, with the two-sided pinching
  \(\mathcal I\bigl(\tfrac{s2^k}{2^k-s}u_k^D\bigr)\subseteq\mathcal I(su)
  \subseteq\mathcal I(su_k^D)\) for all \(s>0\), and locally
  \(u_k^D=2^{-k}\log\sum_j|f_j|^2+O(1)\) with \(f_j\) generators of
  \(\mathcal I(2^ku)\).
- Definition 2.4 [F] (quasi-equisingular approximation, general):
  \(u_k\in\mathrm{PSH}(X,\theta+\varepsilon_k\omega)\),
  \(\varepsilon_k\searrow0\), (i) \(u_k\searrow u\); (ii) analytic
  singularity types; (iii) for any \(\lambda'>\lambda>0\):
  \(\mathcal I(\lambda'u_k)\subseteq\mathcal I(\lambda u)\) for all \(k\)
  large.
- Definition 3.1 [F]: for \(u\in\mathrm{PSH}_>(X,\theta)\),
  \(\nu(u,Y)=0\):
  \(\ \mathrm{Tr}_Y^\theta(u):=\lim_{j\to\infty}
  P_{\theta|_Y}[u_j^D|_Y]\) — a **decreasing limit of model-potential
  envelopes**, i.e. an actual potential, not merely a \(d_S\)-class.
- Lemma 3.4 [F]: "The definition of \(\mathrm{Tr}_Y^\theta(u)\) does not
  depend on the choice of quasi-equisingular approximation. More precisely,
  \(\mathrm{Tr}_Y^\theta(u)=\lim_j
  P_{\theta|_Y+\varepsilon_j\omega|_Y}[v_j|_Y]\) for any quasi-equisingular
  approximation \(v_j\)." The fetched proof text ends: "Due to [DDNL18,
  Theorem 1.3] we obtain that \(\mathrm{Tr}_Y^\theta(u)=w\)" — **equality of
  potentials**, via volume convergence plus the DDNL rigidity theorem
  (comparable model potentials of equal positive volume coincide;
  UNCONFIRMED exact numbering of [DDNL18, Thm 1.3]).
- Lemma 3.9 [F]: (i) \(v\preceq_{\mathcal I}w\Rightarrow
  \mathrm{Tr}_Y^\theta(v)\le \mathrm{Tr}_Y^\theta(w)\); in particular
  \(v\simeq_{\mathcal I}w\Rightarrow \mathrm{Tr}_Y^\theta(v)=
  \mathrm{Tr}_Y^\theta(w)\) (equality). (ii)
  \(\mathrm{Tr}_Y^\theta(u)=P_{\theta|_Y}[\mathrm{Tr}_Y^\theta(u)]\) (model),
  and \(\varepsilon\)-masses decrease to the trace mass. (iii)–(iv)
  \(\mathcal I\)-invariance under form/class change.
- Example 3.7 [F]: \(u\) analytic, \(\nu(u,Y)=0\):
  \(\mathrm{Tr}_Y^\theta(u)=P_{\theta|_Y}[u|_Y]_{\mathcal I}
  =P_{\theta|_Y}[u|_Y]\simeq[u|_Y]\).
- Theorem 1.1 [F]: Bonavero-type identity
  \(\int_Y(\theta|_Y+dd^c\mathrm{Tr}_Y^\theta(u))^m
  =\lim_k \frac{m!}{k^m}\dim H^0(Y,\dots\otimes\mathcal
  I(k\,\mathrm{Tr}_Y^\theta(u)))\) (big line bundle setting).
- Theorem 1.3 [F]: \(\mathcal I(\lambda\,\mathrm{Tr}_Y^\theta(u))\subseteq
  \mathcal I(\lambda u)|_Y\).

**Auxiliary sources.** [DDNL21] = Darvas–Di Nezza–Lu, *The metric geometry of
singularity types*, arXiv:1909.00839: two-sided bound [F]
\[
 d_S([u],[v])\ \le\ \sum_{j=0}^n\Bigl(2\int_X\theta_{V_\theta}^j\wedge
 \theta_{\max(u,v)}^{n-j}-\int_X\theta_{V_\theta}^j\wedge\theta_u^{n-j}
 -\int_X\theta_{V_\theta}^j\wedge\theta_v^{n-j}\Bigr)\ \le\ C\,d_S([u],[v]),
\]
completeness of \((\mathcal S_\delta,d_S)\), and \(d_S([u],[v])=0\) iff
\(u,v\) lie in the same relative full mass class (equivalently
\(P[u]=P[v]\); this is the packet's \(\sim_P\)). Caution: one fetched
sentence ("\(u_j\searrow u\Rightarrow d_S\to0\)") is **false** as an
unconditional statement (truncation of an Evans potential is a
counterexample, §7.1); I treat it as a fetch artifact and do not use it.
[DX22] = Darvas–Xia, *The closures of test configurations and algebraic
singularity types*, arXiv:2003.04818 (Adv. Math. 2022): the \(d_S\)-closure of
algebraic singularity types is characterized by Bonavero's identity
\(\lim_k k^{-n}h^0(X,L^k\otimes\mathcal I(k\varphi))
=\frac1{n!}\int_X\omega_\varphi^n\) [F] (ample \(L\); used only as
corroboration below, never as a load-bearing step).

**Book audit.** `ch54` Thm 54.22–54.26 and `ch67` (67.19), (67.23), (67.33),
(67.36) faithfully render Prop 2.12 and stop at the \(\mathcal I\)-level; Rem.
54 (`operations-trace-p-boundary`) explicitly declines the \(P\)-refinement.
The book cites only Xia's Prop 2.12 formulation; it does not use [DX24]'s
finer potential-level statements (Def 3.1, Lemma 3.4, Lemma 3.9(i)-equality,
Thm 1.1). That finer layer changes the status of `prob:frontier-trace-p`.

---

## Stage 2. Formalization

Fix \(X\) compact Kähler, \(\theta\) smooth closed real \((1,1)\), big class;
\(Y\subseteq X\) a connected complex submanifold (the book Problem's
hypothesis; Xia's singular \(E\) with normalization \(\widetilde E\) is
treated in §7.3). \(\omega\) a Kähler form.

- \(D_Y:=\{\varphi\in\mathrm{PSH}(X,\theta):\nu(\varphi,Y)=0\}\) (generic
  Lelong number along \(Y\)).
- Types: \([u]=[v]\) iff \(u=v+O(1)\); \([u]\preceq[v]\) iff \(u\le v+O(1)\).
- \(P\)-envelope: \(P_\theta[u]:=\mathrm{usc}\sup\{\psi\in
  \mathrm{PSH}(X,\theta):\psi\le0,\ [\psi]\preceq[u]\}\) (Ross–Witt
  Nyström/DDNL model envelope; identification with the
  \(\lim_{C}P(u+C,V_\theta)\) definition: standard, [DDNL18], UNCONFIRMED
  numbering). \(u\sim_P v\) iff \(P_\theta[u]=P_\theta[v]\); by [DDNL21] this
  is equality of the relative full-mass class, equivalently of the relevant
  mixed nonpluripolar masses (packet's convention).
- \(\mathcal I\)-envelope: \(P_\theta[u]_{\mathcal I}:=\mathrm{usc}
  \sup\{\psi\le0:\mathcal I(\lambda\psi)\subseteq\mathcal I(\lambda u)\
  \forall\lambda>0\}\). \(u\sim_{\mathcal I}v\) iff
  \(\mathcal I(\lambda u)=\mathcal I(\lambda v)\) for all \(\lambda>0\)
  (packet's convention; Xia's Def 2.7 via equality of \(\mathcal
  I\)-envelopes is implied by it, and the two agree on every class used
  below — flagged where relevant).
- \(u\) is \(\mathcal I\)-good iff \(\int\theta_u^n>0\) and
  \(P[u]=P[u]_{\mathcal I}\) (Xia Def 2.3 [F]).
- Quasi-equisingular approximation: [DX24] Def 2.4 quoted above. Trace:
  [DX24] Def 3.1 quoted above; Xia Def 2.11 output := any \(d_S\)-limit of
  \(\varphi_j|_Y\).
- Positivity regime: all \(P\)-statements are made where the trace has
  positive mass; per the source, replace \(\theta\) by \(\theta+\omega\)
  (components of the book's inverse system, cf. (54.30)) so inputs are in
  \(\mathrm{PSH}_>\) and traces have positive mass. Boundary \(=\) §7.1.

**Three-layer statement of the problem.**
(L1) Existence of a map \(\mathrm{Tr}^P:D_Y/{\sim_P}\to
\mathrm{QPSH}(Y)/{\sim_P}\) whose composition with the \(\mathcal
I\)-quotient is the sourced trace. (L2) Strong canonicity: every output of
every admissible computation (any quasi-equisingular approximation, any
\(d_S\)-limit) lies in a single \(P\)-class. (L3) \(P\)-sensitivity: can any
lift see input \(P\)-data beyond the input \(\mathcal I\)-class?

---

## Stage 3–4. Attack and line-by-line

**Naive route and its FIRST unsupported implication.** Working only from
Prop 2.12: one would need "two quasi-equisingular approximations
\((\varphi_j),(\varphi'_k)\) of the same \(\varphi\) have restricted
\(d_S\)-limits at \(d_S\)-distance \(0\)." The interlacing supplied by Def
2.4(iii) is only asymptotic in \(k\) for each fixed pair
\(\lambda'>\lambda\); for fixed \(k\) no comparison of the analytic types
\(\varphi_k,\varphi'_k\) follows, and the scaling gap \(\lambda'/\lambda\to1\)
cannot be closed by the multiplier-ideal data alone. This is the exact point
where the \(\mathcal I\)-level proof stops; it is the first unsupported
implication, and the book's Rem. `operations-trace-p-boundary` is correct
that no formal consequence of Prop 2.12 repairs it. The repair below uses
[DX24]'s potential-level construction plus two lemmas proved here.

**Lemma A (valuative domination by analytic types).** Let \(w\) be a potential
with analytic singularity type on a compact Kähler \(Y\) (locally
\(w=c\log\sum|g_i|^2+O(1)\), \(c>0\), \(\mathfrak a\) a coherent ideal), and
let \(\psi\in\mathrm{PSH}(Y,\theta_Y)\) satisfy
\(\mathcal I(\lambda\psi)\subseteq\mathcal I(\lambda w)\) for all
\(\lambda>0\). Then \([\psi]\preceq[w]\), i.e. \(\psi\le w+C_\psi\).

*Proof.* (1) For a divisorial valuation \(v\) over \(Y\) with generic point on
a modification, Demailly's Bergman-kernel comparison gives
\(\psi\le\varphi_\lambda+C(\lambda)\) with
\(\varphi_\lambda:=\frac1{2\lambda}\log\sum|h_i|^2\), \(h_i\) local
generators of \(\mathcal I(\lambda\psi)\); hence
\(\nu(\psi,v)\ge\nu(\varphi_\lambda,v)=v(\mathcal I(\lambda\psi))/\lambda\).
(2) \(\mathcal I(\lambda\psi)\subseteq\mathcal I(\lambda w)\Rightarrow
v(\mathcal I(\lambda\psi))\ge v(\mathcal I(\lambda w))\). (3) The
Ohsawa–Takegoshi lower bound for multiplier ideals gives
\(v(\mathcal I(\lambda w))\ge\lambda\nu(w,v)-A(v)\) with \(A(v)\) independent
of \(\lambda\) (standard; Demailly, *Analytic Methods*, regularization
estimates). Combining and letting \(\lambda\to\infty\):
\(\nu(\psi,v)\ge\nu(w,v)\) for every divisorial \(v\). (4) Take a log
resolution \(\mu:Y'\to Y\) of \(\mathfrak a\), \(\mathfrak a\cdot\mathcal
O_{Y'}=\mathcal O(-\sum a_iE_i)\), so
\(\mu^*w=c\sum a_ig_{E_i}+O(1)\) locally with \(g_{E_i}\) local potentials of
\([E_i]\). By (3) applied to \(v=\mathrm{ord}_{E_i}\):
\(\nu(\mu^*\psi,E_i)\ge c\,a_i\). Subtracting the divisorial potentials one
prime at a time (Siu decomposition; the generic Lelong number along \(E_i\)
is unchanged when other primes' potentials are subtracted, since their
supports miss the generic point of \(E_i\)), the residual
\(R:=\mu^*\psi-c\sum a_ig_{E_i}\) is quasi-psh on the compact \(Y'\), hence
bounded above; thus \(\mu^*\psi\le\mu^*w+C\) and \(\psi\le w+C\). \(\square\)

**Lemma B (analytic types are \(\mathcal I\)-good; envelopes preserve the
type).** For \(w\) as in Lemma A with \(\int(\theta_Y)_w^{\dim Y}>0\):
\[
 P[w]_{\mathcal I}=P[w],\qquad [P[w]_{\mathcal I}]=[P[w]]=[w] .
\]
*Proof.* \(P[w]\le P[w]_{\mathcal I}\): every competitor \(\psi\) of \(P[w]\)
has \([\psi]\preceq[w]\), hence \(\mathcal I(\lambda\psi)\subseteq\mathcal
I(\lambda w)\), so it competes for \(P[w]_{\mathcal I}\). Conversely each
competitor \(\psi\) of \(P[w]_{\mathcal I}\) satisfies the hypothesis of
Lemma A; the constant \(C_\psi\) is a priori non-uniform, but running Lemma
A's step (4) for the whole family at once on the fixed resolution: all
residuals \(R_\psi=\mu^*\psi-c\sum a_ig_{E_i}\) are \(\theta''\)-psh for one
fixed form \(\theta''\), and their usc-regularized sup is again
\(\theta''\)-psh on a compact space, hence bounded above by a single
\(C_0\). Therefore \(P[w]_{\mathcal I}\le w+C_0\), so
\([P[w]_{\mathcal I}]\preceq[w]\); with \(w\le P[w]\le P[w]_{\mathcal I}\)
(after the \(\le0\) normalization) all three types coincide and the envelopes
are equal. \(\square\)

Consequences recorded for later: (B1) for analytic types, the
\(\preceq_{\mathcal I}\) order coincides with the \(O(1)\)-order
\(\preceq\) (Lemma A both ways); (B2) two analytic types are
\(P\)-equivalent iff \(\mathcal I\)-equivalent iff of bounded difference iff
(ideal presentation \(c\log|\mathfrak a_1|\), \(c\log|\mathfrak a_2|\)) the
integral closures satisfy
\(\overline{\mathfrak a_1^{\,m}}=\overline{\mathfrak a_2^{\,m}}\) for all
\(m\) (for equal coefficients: \(\overline{\mathfrak a_1}
=\overline{\mathfrak a_2}\)) — via the Lejeune-Jalabert–Teissier metric
characterization \(h\in\overline{\mathfrak a}\Leftrightarrow
|h|\le C\|\mathfrak a\|\) locally (classical). This answers the audit demand
"is your \(P\)-equivalence criterion for analytic singularities a theorem":
it is, with the proof above.

**Proposition C (the trace is the \(\mathcal I\)-model potential of its
class).** Let \(u\in\mathrm{PSH}_>(X,\theta)\), \(\nu(u,Y)=0\), and suppose
\(\int_Y(\theta|_Y)_{\mathrm{Tr}}^m>0\). Then
\[
 \mathrm{Tr}_Y^\theta(u)\ =\ P_{\theta|_Y}\bigl[\mathrm{Tr}_Y^\theta(u)
 \bigr]_{\mathcal I}.
\]
*Proof.* Write \(T:=\mathrm{Tr}_Y^\theta(u)=\lim_j\downarrow
P[v_j|_Y]\) for a quasi-equisingular \((v_j)\) ([DX24] Def 3.1/Lemma 3.4).
Each \(v_j|_Y\) is an analytic type on \(Y\) (\(\nu(v_j,Y)\le\nu(u,Y)=0\), so
\(Y\not\subseteq V(\mathfrak a_j)\)). \(T\le P[v_j|_Y]\) and, by Lemma B,
\(P[v_j|_Y]\le v_j|_Y+C_j\); hence \(\mathcal I(\lambda T)\subseteq\mathcal
I(\lambda\,v_j|_Y)\) for all \(\lambda,j\). Now let \(\psi\) be any
competitor of \(P[T]_{\mathcal I}\): \(\mathcal I(\lambda\psi)\subseteq
\mathcal I(\lambda T)\subseteq\mathcal I(\lambda\,v_j|_Y)\), so Lemma A
gives \([\psi]\preceq[v_j|_Y]\), so \(\psi\le P[v_j|_Y]\) (definition of the
model envelope as a sup — no uniformity needed). Taking sup over \(\psi\)
and then \(j\to\infty\): \(P[T]_{\mathcal I}\le\lim_j\downarrow
P[v_j|_Y]=T\). The inequality \(T\le P[T]_{\mathcal I}\) holds since \(T\) is
its own competitor (\(T\le0\); Lemma 3.9(ii) normalization). \(\square\)

(Envelope classes: the \(v_j|_Y\) live in \(\theta|_Y+\varepsilon_j\omega|_Y\);
the displayed inequalities are read in the common larger class and pass to
the limit as in [DX24] Lemma 3.4/3.9(iv); multiplier ideals are local and
unaffected. Consistency check: Prop C is the transcendental shadow of [DX24]
Thm 1.1 (Bonavero identity for the trace) and of [DX22] Thm 1.4; neither is
used in the proof.)

**Theorem D (single \(P\)-class of all computations).** Same hypotheses. Let
\((\varphi_j)\) be ANY quasi-equisingular approximation of \(u\) and let
\(\psi\) be ANY \(d_S\)-limit of \((\varphi_j|_Y)\) (existence per Prop 2.12
[F]). Then \(P[\psi]=\mathrm{Tr}_Y^\theta(u)\); in particular all outputs of
Xia's Definition 2.11, over all approximations and all limit choices, lie in
the single \(P\)-class of \(\mathrm{Tr}_Y^\theta(u)\).
*Proof.* Set \(T:=\mathrm{Tr}_Y^\theta(u)\). (a) \([\psi]_{\mathcal I}
=[T]_{\mathcal I}\) by Prop 2.12 / [DX24] Lemma 3.4. (b) Hence
\(\psi\le P[\psi]_{\mathcal I}=P[T]_{\mathcal I}=T\) (the \(\mathcal
I\)-envelope depends only on the \(\mathcal I\)-data; Prop C), so
\([\psi]\preceq[T]\). (c) Masses: \(|\,\mathrm{Vol}(\psi)-
\mathrm{Vol}(\varphi_j|_Y)|\le C\,d_S\to0\) ([DDNL21] two-sided bound), and
\(\mathrm{Vol}(\varphi_j|_Y)=\mathrm{Vol}(P[\varphi_j|_Y])\to
\mathrm{Vol}(T)\) (envelope preserves mass, [DDNL18] UNCONFIRMED numbering;
convergence of volumes is the content of [DX24] Lemma 3.4's proof [F]). So
\(\mathrm{Vol}(\psi)=\mathrm{Vol}(T)>0\). (d) Rigidity: \([\psi]\preceq[T]\),
equal positive masses \(\Rightarrow P[\psi]=P[T]=T\) ([DDNL18, Thm 1.3] as
invoked by [DX24] [F]). \(\square\)

**Corollary E (answer to L1, L2).** On a compact Kähler \(X\) with \(Y\) a
connected submanifold, in the positive-mass regime (inputs in
\(\mathrm{PSH}_>\), trace mass \(>0\); attainable componentwise as in the
book's (54.30)):
1. The map \([\varphi]_P\mapsto[\mathrm{Tr}_Y^\theta(\varphi)]_P\) is a
   well-defined canonical lift
   \(D_Y/{\sim_P}\to\mathrm{QPSH}(Y)/{\sim_P}\) whose composition with the
   \(\mathcal I\)-quotient is the sourced trace (it factors through
   \(D_Y/{\sim_{\mathcal I}}\), by [DX24] Lemma 3.9(i)-equality).
2. Strong canonicity holds: the output \(P\)-class is independent of every
   quasi-equisingular approximation and auxiliary choice (Theorem D), and the
   canonical representative is the \(\mathcal I\)-model potential
   \(P[\mathrm{Tr}]_{\mathcal I}=\mathrm{Tr}\) (Prop C). Equivalently: every
   trace output is \(\mathcal I\)-good, and \(\mathcal I\)-equivalent
   \(\mathcal I\)-good potentials are \(P\)-equivalent.

**L3 (sensitivity) is answered negatively, and this is forced.** Since the
sourced trace map is constant on input \(\mathcal I\)-classes (Lemma 3.9(i)
gives equality of potentials), ANY lift compatible with it forgets all input
\(P\)-data beyond the \(\mathcal I\)-class. Explicit witness in §6.4: two
non-\(P\)-equivalent, \(\mathcal I\)-equivalent inputs with identical traces.
This is not a counterexample to the lift (the packet's warning is heeded:
those inputs are not \(P\)-equivalent); it shows the lift is canonical but
lossy, and pins the book's phrase "the \(P\)-data escapes" to its exact
mechanism: quasi-equisingular approximation retains exactly
\(\{\mathcal I(\lambda\varphi)\}_\lambda\), and Prop C shows the output is
exactly the \(\mathcal I\)-model envelope of the restricted asymptotic ideal
data; mixed masses of the input within a fixed \(\mathcal I\)-class are
unrecoverable in principle.

---

## Stage 5. Self-adversarial audit

1. *Is the \(P\)-criterion for analytic singularities a theorem?* Yes: Lemma
   B/B2 with full proof; the metric characterization of integral closure is
   classical (Lejeune-Jalabert–Teissier, *Clôture intégrale des idéaux et
   équisingularité*).
2. *Does \(\nu(\varphi,E)=0\) hold in the examples?* Verified pointwise in
   §6 for each example.
3. *Does the quasi-equisingular limit commute with restriction for analytic
   singularities?* Yes at the \(P\)-level, proved: for analytic \(u\), the
   constant sequence \(u_k:=u\) satisfies Def 2.4 ((iii) reduces to
   \(\mathcal I(\lambda'u)\subseteq\mathcal I(\lambda u)\), true since
   \(\lambda'u\le\lambda u\) for \(u\le0\)); Def 3.1 then yields
   \(\mathrm{Tr}=P[u|_Y]\sim_P u|_Y\), which is [DX24] Ex. 3.7 [F]. Without
   this, §6.1's engine would indeed collapse; with it, the engine is valid
   but (see §6.1) provably cannot produce a counterexample.
4. *Where exactly would the old argument break?* The FIRST unsupported
   implication is documented in Stage 3–4; it is repaired only by the
   potential-level [DX24] layer plus Lemmas A–B; no formal consequence of
   Prop 2.12 alone suffices.
5. *Fetch-level risks.* Lemma 3.4's "equality of potentials" reading and the
   DDNL rigidity citation are [F]-grade. If Lemma 3.4 asserted only
   \(\mathcal I\)-equivalence, Corollary E.1 would survive unchanged with
   representative \(P[\mathrm{Tr}]_{\mathcal I}\) (Prop C's proof only needs
   Def 3.1 for one approximation), and Theorem D's step (a) would survive via
   Prop 2.12; step (c)'s volume convergence for arbitrary approximations
   would then need [DX24]'s Lemma 3.4 proof content, which is exactly what
   the fetch reports. Residual risk: low, flagged.
6. *Normalization conventions* (\(\psi\le0\) vs \(\sup=0\)) shift envelopes
   by \(O(1)\) only; all statements are type/class statements.

---

## Stage 6. Mandated test cases

### 6.1 Analytic singularities; the integral-closure engine (task item (1))

Setup: \(\mathfrak a_1,\mathfrak a_2\subseteq\mathbb C[x,y,z]\),
\(E=\{z=0\}\); restriction means the image ideal
\(\mathfrak a_i\cdot\mathcal O_E\subseteq\mathbb C[x,y]\).

**Theorem 6.1 (impossibility of the engine).** If
\(\overline{\mathfrak a_1}=\overline{\mathfrak a_2}\) then
\(\overline{\mathfrak a_1\mathcal O_E}=\overline{\mathfrak a_2\mathcal
O_E}\). Hence two \(P\)-equivalent analytic-singularity inputs (equal
coefficient) can never have non-\(P\)-equivalent naive restrictions.
*Proof.* \(\overline{\mathfrak a_1}=\overline{\mathfrak a_2}\) iff
\(\sum|f_i|\asymp\sum|g_j|\) locally, for generators \(f_i\) of
\(\mathfrak a_1\), \(g_j\) of \(\mathfrak a_2\) (LJ–Teissier). The two-sided
bound restricts verbatim to \(E\), giving
\(\sum|f_i|_E|\asymp\sum|g_j|_E|\); applying the characterization on the
reduced space \(E\) yields equality of the integral closures of the image
ideals. \(\square\)
Equivalently at the potential level: equal closure \(\Rightarrow\)
\(\varphi_1=\varphi_2+O(1)\) on \(X\) \(\Rightarrow\)
\(\varphi_1|_E=\varphi_2|_E+O(1)\): bounded differences restrict; nothing
finer is needed. The task's hoped-for "standard example" (same closure
upstairs, different closures of restrictions) therefore does not exist. The
genuine classical phenomenon behind the task's warning — restriction does
not commute with integral closure as an *operation*,
\(\overline{\mathfrak a}\cdot\mathcal O_E\subsetneq
\overline{\mathfrak a\cdot\mathcal O_E}\) in general — lives one level below
the closure-class and is invisible to \(P\)-classes.

**Illustrative pair, carried in full.** \(\mathfrak a_1=(x^2,y^2,z^2)\),
\(\mathfrak a_2=(x,y,z)^2\). (i) Same closure:
\(|x|^4+|y|^4+|z|^4\asymp(|x|^2+|y|^2+|z|^2)^2\) (elementary norm
equivalence), so \(\overline{\mathfrak a_1}=\overline{\mathfrak a_2}
=(x,y,z)^2\). (ii) Compactification: on \(X=\mathbb P^3\), class
\(\theta=2\omega_{FS}\), set
\(\varphi_i=\tfrac12\log\bigl(\sum_{\text{gens }g}|g^{\mathrm h}|^2/
\|\cdot\|^4\bigr)\) with degree-2 homogenizations; the same norm equivalence
holds homogeneously on \(\mathbb C^4\), so \(\varphi_1=\varphi_2+O(1)\)
globally: \(\varphi_1\sim_P\varphi_2\) (this verifies precisely the packet's
"same integral closure globally \(\Rightarrow P\)-equivalence" step — here
by bounded difference, which is stronger). (iii) Membership in \(D_E\),
\(E=\{z=0\}\simeq\mathbb P^2\): at a generic point of \(E\) (where
\((x,y)\neq(0,0)\)) both potentials are finite and smooth, so
\(\nu(\varphi_i,E)=0\). (iv) Traces: by audit item 3, \(\mathrm{Tr}_E
(\varphi_i)\sim_P\varphi_i|_E\); the restricted ideals are
\(\mathfrak a_1\mathcal O_E=(x^2,y^2)\neq(x^2,xy,y^2)=\mathfrak a_2\mathcal
O_E\) — the ideals differ, but
\(\overline{(x^2,y^2)}=(x,y)^2=\overline{(x^2,xy,y^2)}\), and indeed
\(|x|^4+|y|^4\asymp(|x|^2+|y|^2)^2\): the traces are \(P\)-equivalent (same
type). Lelong check on \(E\): at \(p=[0:0:1]\in E\subset\{z=0\}\) (affine
coords \((x,y)\)) both traces have \(\nu=2\); everywhere else \(0\); all
Lelong data on modifications agree by bounded difference. No counterexample;
the discrepancy the task hoped to exploit occurs only at ideal level, never
at closure/\(P\) level.

### 6.2 Positive direction on the analytic subcone (task item (2))

**Proposition 6.2.** On analytic-singularity inputs in \(D_Y\), the trace of
the \(P\)-class is well-defined and computed by naive restriction:
\(\varphi_1\sim_P\varphi_2\) analytic \(\Rightarrow\) (Lemma B2)
\(\varphi_1=\varphi_2+O(1)\) \(\Rightarrow\)
\(\varphi_1|_Y=\varphi_2|_Y+O(1)\) \(\Rightarrow\)
\(\mathrm{Tr}(\varphi_1)=P[\varphi_1|_Y]\sim_P
\varphi_1|_Y\sim_P\varphi_2|_Y\sim_P\mathrm{Tr}(\varphi_2)\). Fully proved;
consistent with Cor. E, of which it is the analytic shadow.

### 6.3 Toric/monomial engine (task item (3))

**Lemma 6.3 (slice lemma).** For a monomial ideal
\(\mathfrak a\subseteq\mathbb C[x_1,\dots,x_n]\) and \(E=\{x_n=0\}\):
\[
 \mathrm{Newt}(\mathfrak a\cdot\mathcal O_E)
 =\mathrm{Newt}(\mathfrak a)\cap\{a_n=0\},
\]
i.e. the Newton polyhedron of the sliced ideal EQUALS the slice of the
polyhedron. *Proof.* \(\mathfrak a\cdot\mathcal O_E\) is generated by the
images of the monomials of \(\mathfrak a\); a monomial survives iff its
\(x_n\)-exponent is \(0\), so \(\mathrm{Newt}(\mathfrak a\mathcal O_E)=
\mathrm{conv}\{a'\,:\,(a',0)\in\mathfrak a\}+\mathbb R^{n-1}_{\ge0}\).
Conversely, a point \((a',0)\) of \(\mathrm{Newt}(\mathfrak a)\) dominates a
convex combination \(\sum\lambda_iv_i\) of exponents of \(\mathfrak a\)
componentwise; the \(n\)-th coordinates \(v_{i,n}\ge0\) must satisfy
\(\sum\lambda_iv_{i,n}\le0\), forcing \(v_{i,n}=0\) for all contributing
\(i\): only \(x_n\)-free exponents support the slice. The two sets coincide.
\(\square\)
**Consequence.** Equal Newton polyhedra in \(3\) variables (\(=\) equal
integral closures, Howald/monomial theory) force equal slices, hence equal
Newton polyhedra — equal closures — of the restrictions. The engine "same
polyhedron, different slices" is IMPOSSIBLE; the warned-against gap between
"slice of polyhedron" and "polyhedron of sliced ideal" closes at the level
of closures (it is real only at ideal level, cf. \((x^2,y^2)\) vs
\((x^2,xy,y^2)\) in §6.1(iv), which have the same polyhedron). This is the
toric face of Theorem 6.1, and it terminates step (3) with a proof of
impossibility, as the task permits.

### 6.4 Split products and retractions; the exact escape of \(P\)-data (task item (4))

Book finding confirmed: (67.23)/(67.33) identify the trace only at the
\(\mathcal I\)-level, and correctly so at their level of technology.
Sharpening available from Prop C: under the hypotheses of
`thm:functor-split-trace`, with \(T=p_Y^*S+p_Z^*\eta\),
\[
 \mathrm{Tr}_{Y\times\{z_0\}}(T)\ =\ P_{\alpha_Y}[\psi]_{\mathcal I}
 \quad\text{(equality of potentials, hence of \(P\)-classes)},
\]
and \(\mathrm{Tr}(T)\sim_P S\) **iff** \(S\) is \(\mathcal I\)-good; same for
the retraction variant. Sharpness witness (Evans construction): on
\(Y=\mathbb P^1\) take a polar Cantor set \(K\) and (Evans) an atomless
probability-type measure \(\mu\) on \(K\) with \(\mu(K)=s\in(0,1)\) whose
potential \(u\) satisfies \(u|_K=-\infty\), all Lelong numbers \(0\). Set
\(\psi:=tu\), \(S:=\omega_Y+dd^c\psi\ge(1-t)\omega_Y\) (Kähler current),
\(S_0:=\omega_Y\). Then \(\mathcal I(\lambda\psi)=\mathcal O\) for all
\(\lambda\) (zero Lelong numbers on all modifications), so
\(T:=p_Y^*S+p_Z^*\eta\simeq_{\mathcal I}T_0:=p_Y^*S_0+p_Z^*\eta\); both lie
in \(D_{Y\times\{z_0\}}\) (the polar set \(K\times Z\) meets the slice in the
polar set \(K\times\{z_0\}\) of the slice; generic Lelong along the slice is
\(0\)). Masses on \(X=Y\times Z\) (\(Z=\mathbb P^1\), product class):
\(\langle T^2\rangle=2\,\mathrm{Vol}_Y(S)\cdot\mathrm{Vol}_Z(\eta)
=2(1-ts)\neq2=\langle T_0^2\rangle\): the inputs are NOT \(P\)-equivalent.
Their traces coincide exactly (\(=V_{\alpha_Y}\)-model, by Lemma 3.9(i) or
directly: all multiplier ideals trivial, quasi-equisingular approximants
bounded, restrictions bounded). Verification against the packet's rule: this
is a legal demonstration of non-injectivity (L3), NOT a counterexample to
the lift, since the inputs are not \(P\)-equivalent. The mechanism claimed
by the book — "quasi-equisingular approximants control multiplier ideals,
not mixed masses" — is thereby made exact: the trace output is precisely the
\(\mathcal I\)-model envelope of the restricted ideal data (Prop C), and the
input mass deficit \(ts\) is stored in no \(\mathcal I(\lambda\varphi)\).

### 6.5 Curve targets: unconditional strong canonicity, self-contained

For \(\dim Y=1\) (any \(\mathrm{codim}\)), Theorem D admits a proof
independent of [DX24] Lemma 3.4, worth recording as a boundary-check. Types
on a compact curve decompose as (countable atomic part \(=\) Lelong data
\(=\mathcal I\)-data) \(+\) (diffuse polar mass, \(\mathcal I\)-invisible);
\(\mathrm{Vol}=\deg-\)(polar mass). For \(\sigma\) a finite-atomic (analytic)
type and any \(\tau\): \(\max(\sigma,\tau)\) has polar mass
\(\sum_q\min(\nu_\sigma(q),\nu_\tau(q))\) (diffuse part killed: it would
need support in the finite set \(\mathrm{polar}(\sigma)\)). Hence, with
\(s:=\) diffuse mass of \(\tau\), the [DDNL21] lower bound gives
\(C\,d_S(\sigma,\tau)\ge2\mathrm{Vol}(\sigma\vee\tau)-\mathrm{Vol}(\sigma)
-\mathrm{Vol}(\tau)\ge2s-|{\mathrm{Vol}(\sigma)-\mathrm{Vol}(\tau)}|\), so
\(d_S\)-limits of analytic types on a curve carry no diffuse polar mass, are
\(\mathcal I\)-good, and \(\mathcal I\)-equivalent \(\mathcal I\)-good types
are \(P\)-equivalent. All trace outputs on curve targets lie in one
\(P\)-class, unconditionally.

---

## Stage 6bis. Boundary examples

1. **Zero trace mass.** \(\varphi=\log(|x|/\|\cdot\|)\)-type on
   \(\mathbb P^2\), class \(\omega_{FS}\), \(E\) a line through
   \(p=\{x=0\}\cap E\) transversally: \(\nu(\varphi,E)=0\), trace type
   \(=\) atom of mass \(1\) at \(p\), \(\mathrm{Vol}=0\): the \(d_S\)/
   rigidity apparatus degenerates (\(\mathcal S_\delta\)-completeness fails
   at \(\delta=0\)); this is exactly why the source and the book (54.30)
   enlarge the class before taking envelopes. The lift is asserted only in
   the positive-mass regime.
2. **Truncation/Evans.** \(u_j=\max(u,-j)\downarrow u\) (Evans):
   \(d_S(u_j,u)\ge s>0\) for all \(j\): decreasing sequences are NOT
   \(d_S\)-continuous in general; also \((u_j)\) is a legitimate
   quasi-equisingular approximation of an \(\mathcal I\)-trivial \(u\)
   (Def 2.4(iii) is vacuous there), and its restricted \(d_S\)-limit is the
   trivial type — consistently with Theorem D, NOT the naive restriction:
   trace \(\neq\) restriction beyond the analytic cone.
3. **No increasing continuity.** Book Rem. `operations-trace-not-increasing`
   stands; nothing here upgrades it.
4. **Singular \(E\) (Xia's normalization setting).** Lemmas A–B on
   \(\widetilde E\) need resolutions of the normal space and the
   model-envelope/\(d_S\) package there ([Xia23Op] works on unibranch
   spaces); the rigidity input and mass theory on normal Kähler spaces are
   not verified here. OPEN-AFTER-ATTEMPT for singular \(E\); for the book's
   Problem (submanifold \(Y\)) this does not arise.
5. **Nets.** Only sequential \(d_S\)-continuity is sourced (Prop 2.12); no
   net extension is claimed, matching the book's firewall.

---

## Stage 7. Dispositions

- **Main lifting question (book Problem `prob:frontier-trace-p`,
  \(Y\) submanifold, positive-mass regime): CANDIDATE-PROPOSITION
  (positive).** The lift exists, is canonical, is independent of every
  quasi-equisingular approximation and auxiliary choice, with canonical
  representative \(P[\mathrm{Tr}]_{\mathcal I}=\mathrm{Tr}\). Assembled from
  [DX24] (Def 3.1, Lemma 3.4, Lemma 3.9, Ex 3.7 — [F]-grade) plus Lemmas
  A–B, Prop C, Thm D proved here. Not literature-resolved verbatim: the
  \(P\)-statement is in no fetched source; the assembly is new packaging.
- **Counterexample search (task's central alternative): closed negatively at
  output level.** No two \(P\)-equivalent inputs in \(D_Y\) can have
  non-\(P\)-equivalent traces (Thm D + Lemma 3.9(i)); the mandated engines
  (1),(3) are provably empty (Thm 6.1, Lemma 6.3).
- **Analytic subcone: CANDIDATE-PROPOSITION (proved, §6.2).**
- **Split/retraction sharpening (`ch67`): CANDIDATE-PROPOSITION** —
  \(\mathrm{Tr}(T)=P_{\alpha_Y}[\psi]_{\mathcal I}\) as potentials;
  \(\sim_P S\) iff \(S\) \(\mathcal I\)-good; sharpness by the Evans product
  (§6.4). Book's \(\mathcal I\)-level finding confirmed; its "P-data
  escapes" statement is upgraded from heuristic to theorem (loss occurs at
  the input quotient, necessarily and exactly).
- **Singular \(E\), zero-mass boundary, net continuity:
  OPEN-AFTER-ATTEMPT** (§6bis.1, 6bis.4, 6bis.5).
- **Curve targets: CANDIDATE-PROPOSITION (proved, §6.5), independent
  corroboration.**

## Proposed ledger lines (candidate-only)

- CANDIDATE: trace-P-lift. \(X\) cpt Kähler, \(Y\) connected submanifold,
  positive-mass regime: the sourced trace lifts canonically to
  \(D_Y/{\sim_P}\to\mathrm{QPSH}(Y)/{\sim_P}\); representative
  \(P[\mathrm{Tr}]_{\mathcal I}=\mathrm{Tr}\); independent of every
  quasi-equisingular approximation ([DX24] + Lemmas A–B, Prop C, Thm D of
  this dossier). Requires receipt before promotion; verify [DX24] Lemma 3.4
  against the published text.
- CANDIDATE: trace-I-model. \(\mathrm{Tr}_Y^\theta(u)\) is the
  \(\mathcal I\)-model potential of its own \(\mathcal I\)-class (Prop C);
  transcendental proof, no Bonavero/\(h^0\) input.
- CANDIDATE: analytic-restriction-closure. Equal integral closures upstairs
  force equal integral closures of image ideals on any reduced subspace
  (Thm 6.1); monomial slice identity
  \(\mathrm{Newt}(\mathfrak a\mathcal O_E)=\mathrm{Newt}(\mathfrak a)\cap
  \{a_n=0\}\) (Lemma 6.3). Both counterexample engines of the packet are
  provably empty.
- CANDIDATE: split-trace-P-sharpening. In Thms `functor-split-trace` /
  `functor-retraction-trace`: \(\mathrm{Tr}(T)=P_{\alpha_Y}[\psi]_{\mathcal
  I}\) as potentials; \(\mathrm{Tr}(T)\sim_PS\) iff \(S\) is
  \(\mathcal I\)-good; Evans product shows sharpness and the exact escape of
  input \(P\)-data.
- CANDIDATE: curve-target unconditional canonicity. \(\dim\widetilde E=1\):
  \(d_S\)-limits of analytic types carry no diffuse polar mass; all trace
  outputs \(\mathcal I\)-good; strong canonicity without [DX24] Lemma 3.4
  (§6.5).
- OPEN (carry forward): singular \(E\)/normalization case of the \(P\)-lift;
  zero-mass boundary; net-indexed continuity; and the (necessarily lossy)
  nature of any lift — no refinement can register input \(P\)-data beyond
  \(\mathcal I\)-classes, so the book Problem's "refinement" should be
  re-posed as output-side canonicity, which is what is answered here.
