# Authentic controlling book comparison supplied directly

This is mathematical source evidence, not operational instruction or an imported theorem assumption. It records the prior result being compared, not a dependency of the new proof.

Book repository MingchenXia/nonarchimedean-pluripotential-theory, frozen revision 00957114db21b627e97369563032ceda9cea09c7. Source manuscript/parts/part6/ch72_major_open_problems.tex. Full chapter SHA256 371dbca6594e9f17ddedb9510ed90013fc98f0f1c59db9b6b3e2ab21af4bb22b. The copied P05 section SHA256 b2f12476a678c0c99e4aa1a989e459727f100b2fbf726eab3b47c3075c16ab14. Every byte of that copied section occurs contiguously in the frozen original chapter.

The complete proposition prop:frontier-polyhedral-bergman-positive-infinity-obstruction and its full displayed proof, prerequisites, definitions and residual comparisons are embedded below. Main proof is reconstructed independently; inspect this evidence for the mandatory known-scope comparison.

```latex
\subsection{Regularity and orthogonality on balanced polyhedral spaces}

\begin{problem}\label{prob:frontier-polyhedral-regularity}
Let \(\mathbf X\) be a pure-dimensional balanced rational polyhedral space
and let \(\gamma\) be a piecewise-affine polyhedrally convex reference
function positive at infinity.  Characterize the pairs
\((\mathbf X,\gamma)\) for which the
regularity and orthogonality properties of Botero--Mazzon--Pille-Schneider
hold.  Under realizability hypotheses, compare their polyhedral
Monge--Amp\`ere operator with CLD, delta-form, and non-Archimedean
Monge--Amp\`ere measures.
\end{problem}

The bibliographic dates require a correction.  The first arXiv version was
submitted on 9 March 2026 and the date printed inside the manuscript is
10 March 2026, not 11 August 2026 \cite{BMPS26}.  We use that version
throughout.

Here are the conventions needed to compare it with
\Cref{app:tropical-algebra}.  Normal vectors point from a codimension-one
face into an adjacent top-dimensional face, as in
\eqref{eq:appG-primitive-normal}, and a convex bend has positive divisor.
Botero--Mazzon--Pille-Schneider allow positive real balancing weights; a
tropical cycle in the narrower Mikhalkin--Rau convention has integral
weights.  Analytic comparison therefore uses the latter only after the
saturated tangent lattices and analytic tropical multiplicities have been
installed.  Finally, their real Monge--Amp\`ere measure is the Alexandrov
measure of \Cref{thm:appD-alexandrov-measure}, without a factorial.  Their
polyhedral intersection convention consequently gives
\begin{equation}
 \one_{\RelInt(\sigma)}\MA_{\mathrm{poly}}(\varphi)
 =d![\mathbf X](\sigma)\,
   \MA_{\mathbf R}(\varphi|_{\RelInt(\sigma)})
 \label{eq:frontier-polyhedral-real-local}
\end{equation}
on the relative interior of every top-dimensional face
\cite[Propositions~4.12 and~4.20]{BMPS26}.  This is exactly the factorial
firewall in \Cref{app:normalizations}.

We first separate the source results from the new deduction below.  For a
piecewise-affine polyhedrally convex reference \(\gamma\) positive at
infinity, \cite[Theorem~4.13 and Proposition~4.16]{BMPS26} constructs the
positive mixed operator
\[
 \MA_{\mathrm{poly}}:
 \mathrm{PC}_{\mathrm{reg}}(\mathbf X,\gamma)^d
 \longrightarrow\mathcal M^+(\mathbf X),
 \qquad
 \int_{\mathbf X}\MA_{\mathrm{poly}}=\deg(\gamma),
\]
and proves its continuity under uniform, in particular decreasing,
regularizable approximation.  Its Theorem~6.4 says that regularity is
equivalent to each of
\[
 \begin{split}
 &P_\gamma(u)\in\mathrm{PC}_{\mathrm{reg}}(\mathbf X,\gamma)
       \quad\text{for every bounded piecewise-affine }u,\\
 &\mathrm{PAPC}(\mathbf X,\gamma)
       \text{ is uniformly dense in }\mathrm{PC}(\mathbf X,\gamma),\\
 &\mathrm{PC}(\mathbf X,\gamma)
       =\mathrm{PC}_{\mathrm{reg}}(\mathbf X,\gamma).
 \end{split}
\]
The source states one-dimensional regularity in Proposition~6.13 and
complete-affine and conical regularization in Remark~6.6.  These statements
must be separated from its literal coefficient convention: Definition~2.28
requires integral linear parts and rational constants, while the proofs of
the cited regularization statements use arbitrary real affine functions.
The theorem and counterexample below give the precise one-dimensional
repair.  Orthogonality is the further
identity
\begin{equation}
 \int_{\mathbf X}
 \bigl(P_\gamma(u)-(\gamma+u)\bigr)
 \MA_{\mathrm{poly}}(P_\gamma(u))=0.
 \label{eq:frontier-polyhedral-orthogonality}
\end{equation}
The source proves \eqref{eq:frontier-polyhedral-orthogonality} on
one-dimensional polyhedrally smooth spaces and obtains existence and
uniqueness, modulo constants, for compactly supported positive measures of
mass \(\deg(\gamma)\)
\cite[Proposition~6.21 and Theorem~6.22]{BMPS26}.

\input{editorial/solver_dossiers_20260925/p051_one_dimensional_regularity_repair_v1_20260925/STATEMENT.tex}
\input{editorial/solver_dossiers_20260925/p051_one_dimensional_regularity_repair_v1_20260925/PROOF.tex}

\begin{proposition}\label{prop:frontier-polyhedral-bounded-reference-shift}
Let \(\gamma\) and \(\widetilde\gamma\) be piecewise-affine
polyhedrally convex references on the same pure-dimensional balanced
rational polyhedral space \(\mathbf X\), both positive at infinity, and put
\[
             \delta:=\widetilde\gamma-\gamma\in
             \mathrm{PA}_{b}(\mathbf X).
\]
Then, as classes of functions on \(\mathbf X\),
\[
\begin{gathered}
 \mathrm{PC}(\mathbf X,\widetilde\gamma)
 =\mathrm{PC}(\mathbf X,\gamma),\qquad
 \mathrm{PAPC}(\mathbf X,\widetilde\gamma)
 =\mathrm{PAPC}(\mathbf X,\gamma),\\
 \mathrm{PC}_{\mathrm{reg}}(\mathbf X,\widetilde\gamma)
 =\mathrm{PC}_{\mathrm{reg}}(\mathbf X,\gamma).
\end{gathered}
\]
For every \(u\in\mathrm{PA}_{b}(\mathbf X)\), their envelopes satisfy
\[
 P_{\widetilde\gamma}(u)=P_\gamma(u+\delta).
 \tag{\(\star\)}\label{eq:frontier-polyhedral-bounded-shift-envelope}
\]
Consequently regularity holds for \((\mathbf X,\widetilde\gamma)\) if and
only if it holds for \((\mathbf X,\gamma)\); when these equivalent
regularity conditions hold, orthogonality holds for one reference if and
only if it holds for the other.

The same assertions hold in the real scalar extension after replacing
\(\mathrm{PA}_{b}\), \(\mathrm{PAPC}\), and
\(\mathrm{PC}_{\mathrm{reg}}\) throughout by their
\(\mathbf R\)-subscripted versions and assuming
\(\delta\in\mathrm{PA}_{\mathbf R,b}(\mathbf X)\).
\end{proposition}

\begin{proof}
The obstacle in the left member of
\eqref{eq:frontier-polyhedral-bounded-shift-envelope} is
\(
 \widetilde\gamma+u=\gamma+(u+\delta)
\), while \(u\mapsto u+\delta\) is a bijection of
\(\mathrm{PA}_{b}(\mathbf X)\).  Since \(\delta\) is bounded, the
\(\gamma+O(1)\) and \(\widetilde\gamma+O(1)\) growth conditions coincide.
Thus the two defining competitor sets agree, proving
\eqref{eq:frontier-polyhedral-bounded-shift-envelope}.  The same coincidence
of the growth condition identifies the three displayed classes, including
the regularizable closure; this is exactly the reference dependence in
\cite[Definitions~3.14 and~3.23]{BMPS26}.  The source's regularity
characterization quoted above now gives the equivalence of regularity.

Assume it holds.  For corresponding obstacles, the two envelope functions
are equal by \eqref{eq:frontier-polyhedral-bounded-shift-envelope}, so their
polyhedral Monge--Amp\`ere measures are the same.  Moreover
\[
 P_{\widetilde\gamma}(u)-(\widetilde\gamma+u)
 =P_\gamma(u+\delta)-\bigl(\gamma+(u+\delta)\bigr).
\]
The two orthogonality integrals therefore agree, and the bijection
\(u\mapsto u+\delta\) proves the assertion.
\end{proof}

\input{editorial/solver_dossiers_20260925/p051_one_vertex_integral_nonregularity_v2_20260925/STATEMENT.tex}
\input{editorial/solver_dossiers_20260925/p051_one_vertex_integral_nonregularity_v2_20260925/PROOF.tex}

Thus the P05.1 classification factors through bounded piecewise-affine
reference shifts within either fixed coefficient category.  On every
one-vertex balanced rational fan, the real scalar category has regularity,
whereas the literal integral-slope category never does.  In particular, the
source's conical regularization statement cannot be promoted to regularity
for arbitrary bounded integral-slope obstacles: that statement concerns
conical functions, while
\Cref{thm:frontier-polyhedral-one-vertex-integral-nonregularity} produces a
nonregularizable envelope for every positive-at-infinity literal reference.

The author-supplied one-vertex note is now explicitly withdrawn
\cite{SuppliedP05220260925}.  Its withdrawal records the same coefficient
conflict: the stated positive theorem used the literal integral-slope class
but invoked a real-affine envelope.  The criterion below is therefore not
cited from that note.  It is a book-local theorem in the explicit real
scalar extension, proved by the displayed contact and obstruction arguments
and using the local convexity test from
\cite[Definitions~3.2--3.3]{BMPS26} and the real-linear one-dimensional
Laplacian formula from
\cite[Definition~6.15 and Proposition~6.17]{BMPS26}.

\input{editorial/solver_dossiers_20260925/p052_one_vertex_polyhedral_orthogonality_v63_20260925/STATEMENT_LIVE.tex}
\input{editorial/solver_dossiers_20260925/p052_one_vertex_polyhedral_orthogonality_v63_20260925/PROOF_LIVE.tex}

The same contact perturbation is local and therefore survives bounded
edges.  Applying it at every vertex whose cone of nonnegative balancing
relations is one-dimensional gives the following graph-level extension.

\input{editorial/solver_dossiers_20260925/p052_local_rank_one_graph_candidate_v1_20260925/STATEMENT.tex}
\input{editorial/solver_dossiers_20260925/p052_local_rank_one_graph_candidate_v1_20260925/PROOF.tex}

The remaining converse is a global realization question: a local
higher-rank obstruction must be extended through the graph without changing
the prescribed growth.  Positivity at infinity supplies exactly that
extension.  A sufficiently slow ambient rational-polyhedral norm can be
raised above the reference near any chosen vertex and then cut off by taking
the maximum with the reference.  Rational chordal interpolation retains its
vertex slopes and restores the required rational subdivision.

\input{editorial/solver_dossiers_20260925/p052_graph_accessible_mass_classification_v2_20260925/STATEMENT.tex}
\input{editorial/solver_dossiers_20260925/p052_graph_accessible_mass_classification_v2_20260925/PROOF.tex}

The same local relation cones also sharpen the negative result in the
literal coefficient category.  The one-vertex construction used positivity
of each ray slope.  In a graph, the exact replacement is strict positivity
of the whole slope vector on every nonzero local balancing relation.

\input{editorial/solver_dossiers_20260926/p051_strict_vertex_integral_nonregularity_v1_20260926/STATEMENT.tex}
\input{editorial/solver_dossiers_20260926/p051_strict_vertex_integral_nonregularity_v1_20260926/PROOF.tex}

The degree-zero case has the opposite behaviour.  Positivity at infinity
makes every unbounded end contribute strictly positive degree.  When the
degree vanishes, the graph is compact, and balancing at a maximum vertex
forces every polyhedrally convex function to be componentwise constant.

\input{editorial/solver_dossiers_20260926/p051_zero_degree_literal_regularity_v1_20260926/STATEMENT.tex}
\input{editorial/solver_dossiers_20260926/p051_zero_degree_literal_regularity_v1_20260926/PROOF.tex}

The remaining positive-degree boundary admits a global obstruction which
does not depend on a strict reference vertex.  The point is to place a
rational convex combination strictly between the reference and a second
literal convex function.  Edgewise integral-slope concave roofs then give a
literal obstacle whose convex envelope is that combination.

\input{editorial/solver_dossiers_20260926/p051_one_dimensional_literal_classification_v1_20260926/STATEMENT.tex}
\input{editorial/solver_dossiers_20260926/p051_one_dimensional_literal_classification_v1_20260926/PROOF.tex}

In higher dimension the edgewise concave roof has no canonical analogue, but
the vertex-contact mechanism does.  For each vertex, an integral
piecewise-affine lattice norm gives a cone majorizing the rational gap.
Taking the minimum of these cones and the original integral gap preserves
the prescribed vertex values while forcing the obstacle to vanish on every
unbounded cell.  This removes dimension, balancing, and local-relation
hypotheses from the noncompact literal obstruction.

\input{editorial/solver_dossiers_20260926/p051_noncompact_literal_nonregularity_v1_20260926/STATEMENT.tex}
\input{editorial/solver_dossiers_20260926/p051_noncompact_literal_nonregularity_v1_20260926/PROOF.tex}

This completely classifies the repaired real-piecewise-affine version of
P05.2 on every one-dimensional balanced rational polyhedral space admitting
a finite structure.  Orthogonality holds exactly when every local cone of
nonnegative balancing relations is one-dimensional.  The theorem allows
bounded edges and cycles and shows that lattice saturation is irrelevant.
In the literal coefficient category, one-dimensional regularity holds
exactly in degree zero, equivalently exactly when the space is compact.
Every positive-degree graph reference fails literal regularity,
independently of the local relation cones.  More generally, literal
regularity fails on every noncompact finite rational polyhedral space in
every dimension, whether or not it is balanced; in particular, the
source's literal complete-affine assertion fails in every positive
dimension.  The earlier strict-vertex theorem remains a local quantitative
form of this obstruction.  Thus every graph on which real-polyhedral
orthogonality holds is negative for literal regularity when the literal
degree is positive, but the literal failure is not confined to that graph
class.  The
one-vertex orthogonality theorem and its bounded-reference-shift corollary
are book-local real-scalar results, not results cited from the withdrawn
note.  The classification also explains
\Cref{ex:frontier-polyhedral-cross-orthogonality}: the four-ray cross has a
two-dimensional cone of nonnegative balancing relations.  Conversely,
\Cref{ex:frontier-polyhedral-nonsaturated-tripod} shows that lattice
smoothness is sufficient but not necessary in this class.  The
higher-dimensional real-PA classification, compact higher-dimensional
literal case, arbitrary nonseparable product obstacles, and the source
coefficient-convention repair remain open, so P05.1 and P05.2 remain active.

The following elementary convex-envelope fact is the missing contact
mechanism on a complete affine space.

% RETHLAS-VERIFIED: balanced-polyhedral-affine-contact; receipt 20260814T174427Z_438bf42ae745
\begin{lemma}\label{lem:frontier-polyhedral-affine-contact}
Let \(f:\mathbf R^d\to\mathbf R\) be continuous and coercive, and let
\(P\) be its greatest lower-semicontinuous convex minorant.  Suppose that
\(P\) is polyhedral.  If \(\partial P(x)\) has positive
\(d\)-dimensional volume, then \(P(x)=f(x)\).
\end{lemma}

\begin{proof}
Choose a Euclidean norm and a point \(p\) in the interior of
\(\partial P(x)\).  For some \(\eta>0\),
\(p+\eta\overline B^\vee\subset\partial P(x)\).  For \(y\ne x\), choose
\(q_y\) in the dual unit sphere with
\(\langle q_y,y-x\rangle=\lVert y-x\rVert\).  Applying the subgradient
inequality to \(p+\eta q_y\) gives
\begin{equation}
 P(y)-\langle p,y\rangle
 \geq P(x)-\langle p,x\rangle+\eta\lVert y-x\rVert.
 \label{eq:frontier-polyhedral-exposed-contact}
\end{equation}
Thus \(x\) is the unique minimizer of
\(P-\langle p,\cdot\rangle\).

Set
\[
                 m:=\inf_y\{f(y)-\langle p,y\rangle\}.
\]
The affine function \(y\mapsto\langle p,y\rangle+m\) is bounded above by
\(f\); maximality of \(P\) therefore puts it below \(P\).  Since
\(P\leq f\), the two opposite inequalities between the infima give
\begin{equation}
 m=\inf_y\{P(y)-\langle p,y\rangle\}
  =P(x)-\langle p,x\rangle.
 \label{eq:frontier-polyhedral-contact-infimum}
\end{equation}
By \eqref{eq:frontier-polyhedral-exposed-contact} and \(f\geq P\), the
function \(f-\langle p,\cdot\rangle\) is coercive, so it attains its
infimum at some \(y_0\).  Equations
\eqref{eq:frontier-polyhedral-exposed-contact}--
\eqref{eq:frontier-polyhedral-contact-infimum} force \(y_0=x\), and equality
at the minimum gives \(f(x)=P(x)\).
\end{proof}

\begin{theorem}\label{thm:frontier-polyhedral-affine-orthogonality}
Let \(N\) have rank \(d\), let
\(\mathbf X=N_{\mathbf R}\) carry the constant balancing weight
\(c>0\), and let
\(\gamma\in\mathrm{PA}_{\mathbf R}(N_{\mathbf R})\) be polyhedrally
convex and positive at infinity.  Then
\((\mathbf X,\gamma)\) has real-polyhedral regularity in every dimension.
Moreover, for every \(u\in\mathrm{PA}_{\mathbf R,b}(N_{\mathbf R})\),
writing \(P=P_\gamma(u)\) and
\[
             \MA_{\mathrm{poly},\mathbf R}(P)
             :=d!c\,\MA_{\mathbf R}(P),
\]
one has
\[
 \int_{N_{\mathbf R}}
 \bigl(P-(\gamma+u)\bigr)\,
 \MA_{\mathrm{poly},\mathbf R}(P)=0.
\]
No strict-convexity hypothesis beyond positivity at infinity is needed.
\end{theorem}

\begin{proof}
Let \(u\in\mathrm{PA}_{\mathbf R,b}(N_{\mathbf R})\), put
\(f=\gamma+u\), and choose
\(C\) with \(|u|\leq C\).  Positivity of \(\gamma\) at infinity and
boundedness of \(u\) make \(f\) coercive.  On all of
\(N_{\mathbf R}\), polyhedral
convexity is ordinary convexity.  The envelope \(P_\gamma(u)\) is therefore
the greatest lower-semicontinuous convex minorant \(P\) of \(f\): indeed,
\(\gamma-C\leq f\) is a competitor, while every convex minorant between
\(\gamma-C\) and \(f\) has the required \(\gamma+O(1)\) growth.

On a common finite rational polyhedral decomposition, the epigraph of
\(f\) is a finite union of polyhedra.  The closed convex hull of a finite
union of polyhedra is polyhedral: write each member as the convex hull of
finitely many points plus a finitely generated recession cone, then take the
convex hull of all points and the cone generated by all recession directions.
Since
\[
 \operatorname{epi}(P)
 =\overline{\operatorname{conv}}\bigl(\operatorname{epi}(f)\bigr),
\]
its lower boundary is real piecewise affine.  The inequalities
\(
 \gamma-C\leq P\leq f\leq\gamma+C
\)
show that
\(P\in\mathrm{PAPC}_{\mathbf R}(\mathbf X,\gamma)\).  This proves
real-polyhedral regularity.

For a real-piecewise-affine convex function on \(N_{\mathbf R}\), apply
the real-scalar version of
\eqref{eq:frontier-polyhedral-real-local} to the coarsest complex with the
single face \(N_{\mathbf R}\); the domains of affinity of \(P\) are merely
an auxiliary refinement.  This gives the global identity
\begin{equation}
                  \MA_{\mathrm{poly},\mathbf R}(P)
                  =d!c\,\MA_{\mathbf R}(P).
 \label{eq:frontier-polyhedral-affine-global-ma}
\end{equation}
The right-hand side is atomic, and its mass at \(x\) is
\(\operatorname{vol}(\partial P(x))\), by
\Cref{ex:appD-polyhedral-atom}.  Every atom of positive mass is therefore
on the contact set \(\{P=f\}\), by
\Cref{lem:frontier-polyhedral-affine-contact}.  The integrand in
the displayed identity in the theorem vanishes on the support of the
measure, proving real-polyhedral orthogonality.
\end{proof}

The epigraph proof in \Cref{thm:frontier-polyhedral-affine-orthogonality}
is the real-affine argument underlying the complete-space discussion in
\cite[Remark~6.6]{BMPS26}; the contact deduction is book-local.  It cannot
be read as a theorem in the literal integral-slope category:
\Cref{prop:frontier-polyhedral-integral-regularity-counterexample} disproves
that interpretation already for \(N_{\mathbf R}=\mathbf R\).

\input{editorial/solver_dossiers_20260925/p051_separable_product_envelope_v1_20260925/STATEMENT.tex}
\input{editorial/solver_dossiers_20260925/p051_separable_product_envelope_v1_20260925/PROOF.tex}

The next example shows why completeness of the ambient convex geometry
cannot be replaced by strict positivity of the reference alone.

\begin{example}\label{ex:frontier-polyhedral-cross-orthogonality}
Let
\[
 \mathbf X=(\mathbf R\times\{0\})\cup(\{0\}\times\mathbf R)
\]
with all four ray weights equal to one, and put
\(\gamma(x,y)=|x|+|y|\) on \(\mathbf X\).  This reference is positive at
infinity and strictly polyhedrally convex on the four-ray complex.  For
\(\varepsilon>0\), define the obstacle
\[
 f(x,0)=|x|+\varepsilon,
 \qquad
 f(0,y)=\bigl||y|-\varepsilon\bigr|,
 \qquad u=f-\gamma.
\]
Then \(u\) is bounded and piecewise affine, and
\[
 P_\gamma(u)(x,0)=|x|,
 \qquad
 P_\gamma(u)(0,y)=\max\{0,|y|-\varepsilon\}.
\]
\end{example}

Indeed, the displayed candidate is the restriction of the ambient convex
function
\(
 \max\{|x|,|y|-\varepsilon,0\}
\), hence is polyhedrally convex and lies below \(f\).  Conversely, if
\(q\leq f\) is an admissible polyhedrally convex function, convexity between
\((0,\varepsilon)\) and \((0,-\varepsilon)\) gives \(q(0,0)\leq0\).
On either horizontal ray, convexity and the asymptotic slope bound one give
\(q(x,0)\leq|x|\).  On the positive vertical ray, convexity first gives
\(q(0,y)\leq0\) for \(0\leq y\leq\varepsilon\), and then the same slope
bound gives \(q(0,y)\leq y-\varepsilon\) for
\(y\geq\varepsilon\); the negative ray is identical.  This proves the
envelope formula.  Its outgoing slopes at the origin have sum two, so
\[
 \MA_{\mathrm{poly}}(P_\gamma(u))\{(0,0)\}=2,
 \qquad P_\gamma(u)(0,0)-f(0,0)=-\varepsilon.
\]
All other atoms lie on the contact set, and the orthogonality integral is
therefore \(-2\varepsilon\).  Finally, a positive local one-cycle at the
origin has weights \(a,a,b,b>0\) on the two opposing horizontal and two
opposing vertical rays; intersection with \(\gamma\) has coefficient
\(2a+2b>0\).  The strict-convexity criterion of
\cite[Remark~3.9]{BMPS26} applies.  This is the source's Example~6.23 with
its sign and contact calculation made explicit.

There is a complementary smooth-fan warning in
\cite[Example~6.24, Claim~6.25, and Remark~6.26]{BMPS26}.  On the Bergman
fan of the uniform matroid \(U_{3,4}\), assign value zero to the opposite
rays generated by \(e_{12}\) and \(e_{34}=-e_{12}\), and value one to the
other primitive ray generators.  The resulting polyhedrally convex
reference \(\gamma\) admits a bounded piecewise-affine obstacle \(g\geq
\gamma\) for which
\[
 P_\gamma(g-\gamma)=\gamma,
 \qquad
 \MA_{\mathrm{poly}}(\gamma)\{0\}=4,
 \qquad
 \gamma(0)<g(0).
\]
The source proves the envelope identity cone by cone: equality first holds
on the line \(\mathbf R e_{12}\), then on the original rays by one-variable
convexity, and finally on each two-dimensional cone by joining its boundary
to the diagonal ray.  The mass is the direct iterated-divisor computation
on that fan.  This example is tropically smooth but \(\gamma\) is identically
zero on \(\mathbf R e_{12}\).  Hence it is neither strictly convex nor
positive at infinity.  It does not disprove the conjunction of a suitable
higher-dimensional smoothness condition with the strict growth hypotheses
in \Cref{prob:frontier-polyhedral-regularity}.

The same Bergman-fan mechanism nevertheless survives the growth condition
itself.  The point is to retain a finite flat segment of the exceptional
line, which forces contact at the origin, while making the reference grow
outside that segment.

\begin{proposition}\label{prop:frontier-polyhedral-bergman-positive-infinity-obstruction}
In the notation of \cite[Example~6.24 and Claim~6.25]{BMPS26}, let
\(g\geq\gamma\) be its obstacle and put \(u=g-\gamma\).  Write
\(\ell(x_1,x_2,x_3)=x_1+x_2\), so that
\[
 \ell(e_{12})=2,
 \qquad
 \ell(e_{34})=-2,
 \qquad
 \bigl(\ell(e_1),\ell(e_2),\ell(e_3),\ell(e_4)\bigr)
   =(1,1,0,-2).
\]
For \(\lambda\in\mathbf Q\cap(0,\tfrac12)\) and
\(R\in\mathbf Q\) with \(R>2\lambda\varepsilon\), set
\[
 \gamma_{\lambda,R}
   :=\max\{\gamma,\lambda\ell-R,-\lambda\ell-R\}.
\]
Then \(\gamma_{\lambda,R}\) is piecewise-affine polyhedrally convex and
positive at infinity.  If
\[
 P:=P_{\gamma_{\lambda,R}}(u),
\]
then \(P=\gamma\) on a neighbourhood of the origin.  Moreover, either
\[
 P\notin
 \mathrm{PC}_{\mathrm{reg},\mathbf R}
     (\mathbf X,\gamma_{\lambda,R}),
\]
or
\[
 \int_{\mathbf X}
 \bigl(P-(\gamma_{\lambda,R}+u)\bigr)\,
 \MA_{\mathrm{poly},\mathbf R}(P)
 \leq -4\varepsilon<0.
\]
Consequently \((\mathbf X,\gamma_{\lambda,R})\) cannot have both
real-polyhedral regularity and real-polyhedral orthogonality.  The same
dichotomy precludes simultaneous literal regularity and orthogonality.
\end{proposition}

\begin{proof}
The restrictions of the two affine functions in the displayed maximum are
polyhedrally convex, as is \(\gamma\); a finite maximum preserves the
polyhedral-convex-combination inequalities.  Thus
\(\gamma_{\lambda,R}\) is piecewise-affine polyhedrally convex by
\cite[Definitions~3.1 and~3.3 and Lemma~3.4]{BMPS26}.  On every recession
direction \(v\), its recession slope is
\[
 \max\{\gamma^{\infty}(v),\lambda|\ell(v)|\}.
\]
The source's ray values show that \(\gamma^{\infty}\) can vanish only on
the line \(\mathbf R e_{12}=\mathbf R e_{34}\), where
\(|\ell|\) is nonzero.  This proves positivity at infinity.

Set
\[
 \gamma_{\infty}:=\max\{\gamma,\lambda\ell,-\lambda\ell\}.
\]
This is a conical piecewise-affine polyhedrally convex function on the
conical fan, and
\[
 \gamma_{\infty}-R\leq\gamma_{\lambda,R}\leq\gamma_{\infty}.
 \tag{\(\dagger\)}\label{eq:frontier-polyhedral-bergman-bounded-reference-shift}
\]
Thus \(\delta:=\gamma_{\lambda,R}-\gamma_{\infty}\) lies in
\(\mathrm{PA}_{b}(\mathbf X)\).  For every
\(v\in\mathrm{PA}_{b}(\mathbf X)\),
\Cref{prop:frontier-polyhedral-bounded-reference-shift} gives
\[
 P_{\gamma_{\lambda,R}}(v)
   =P_{\gamma_{\infty}}(v+\delta).
 \tag{\(\ddagger\)}\label{eq:frontier-polyhedral-bergman-envelope-shift}
\]
This identity is only a reference-change formula.  Remark~6.6 of the source
regularizes conical functions; it does not prove regularity for the
nonconical obstacle \(v+\delta\).

Since \(u\geq0\), \(\gamma_{\lambda,R}\) is a competitor for its own
envelope, hence
\[
 \gamma_{\lambda,R}\leq P\leq\gamma_{\lambda,R}+u.
 \tag{\(*\)}\label{eq:frontier-polyhedral-bergman-growth-envelope-bounds}
\]
On both exceptional rays beyond the source's length-\(\varepsilon\)
modification, \(u=0\).  Choose
\(a\) with \(\varepsilon<a<R/(2\lambda)\).  At the opposite points
\(ae_{12}\) and \(-ae_{12}=ae_{34}\), the two bounds in
\eqref{eq:frontier-polyhedral-bergman-growth-envelope-bounds} agree and
are zero.  Convexity on their connecting line, together with the lower
bound, therefore gives
\[
 P=\gamma=0
 \quad\text{on }[-ae_{12},ae_{12}],
 \qquad\text{in particular }P(0)=0.
 \tag{\(**\)}\label{eq:frontier-polyhedral-bergman-central-contact}
\]
On every other primitive ray of the Bergman fan, the choice
\(\lambda<\tfrac12\) gives
\(\gamma_{\lambda,R}=\gamma\), while the source obstacle has
\(u=\varepsilon\).  The restriction of \(P\) to such a ray is convex,
starts at zero by \eqref{eq:frontier-polyhedral-bergman-central-contact},
and lies between \(t\) and \(t+\varepsilon\).  Its excess over \(t\)
cannot be positive at any point: a positive secant slope would persist by
convexity and contradict boundedness by \(\varepsilon\).  Hence it equals
\(\gamma\) on every such ray.  On the two exceptional rays it equals
\(\gamma\) on the central segment by
\eqref{eq:frontier-polyhedral-bergman-central-contact}.

Near the origin the two affine terms \(\pm\lambda\ell-R\) are negative,
so \(\gamma_{\lambda,R}=\gamma\).  In each of the six two-dimensional
cones, a point sufficiently near the origin lies on a segment joining a
boundary ray to the added diagonal ray.  The source reference \(\gamma\)
is affine on the corresponding side of that diagonal.  Applying convexity
of \(P\) to this segment and using the ray equalities just proved gives
\(P\leq\gamma\); the lower bound in
\eqref{eq:frontier-polyhedral-bergman-growth-envelope-bounds} gives the
reverse inequality.  Thus \(P=\gamma\) on a neighbourhood of \(0\).

If
\(P\notin\mathrm{PC}_{\mathrm{reg},\mathbf R}
(\mathbf X,\gamma_{\lambda,R})\), then this obstacle already disproves
real-polyhedral regularity.  Otherwise its real-scalar Monge--Amp\`ere
measure is defined.  Locality and the source computation
\(\MA_{\mathrm{poly},\mathbf R}(\gamma)\{0\}=4\) give
\(\MA_{\mathrm{poly},\mathbf R}(P)\{0\}=4\).  Finally \(P\leq
\gamma_{\lambda,R}+u\) everywhere, whereas
\(P(0)=0<\gamma_{\lambda,R}(0)+u(0)=\varepsilon\).  The displayed
integral is therefore at most \(-4\varepsilon\), which is incompatible
with real-polyhedral orthogonality.  Since the literal regularizable class
is contained in the real one and the measures agree on literal
approximants, the same alternative rules out the simultaneous literal
properties.
\end{proof}

Thus a higher-dimensional smoothness-and-orthogonality theorem requires
more than a polyhedrally convex reference positive at infinity: even on
this Bergman fan, that growth condition is compatible with a forced
noncontact Monge--Amp\`ere atom.  The proposition leaves open whether an
additional combined intrinsic-smoothness and strict-convexity package restores
orthogonality.

Balancing also does not, by itself, produce an analytic space.  Once a
proper calibrated tropical morphism has been supplied, however, the
recursive comparison can be proved rather than assumed; genuine algebraic
tropicalizations give the principal local analytic case.

\input{parts/part6/fragments/ch72_p053_projection_recursion}

The proposition and its algebraic-chart corollary remove the recursive
projection and local delta-form comparison gaps formerly isolated as
P05.3 and P05.4.  They do not supply a proper polarized realization, a
global semipositive lift, or the mass calibration required by P05.5.

The final boundary step in a polarized realization is nevertheless formal
once the local comparison and the exact total masses are known:

\input{parts/part6/fragments/ch72_p055_mass_completion}

At the model level, the local comparison, mass identity, and calibration
inputs can be packaged into an explicit common-measure statement.  The
following proposition also records exactly where the GK comparison is not
being asserted under the standing discretely valued field hypotheses.

\input{parts/part6/fragments/ch72_p055_model_bridge}

Thus no separate compactification argument is needed after those two hard
inputs have been established.  The two propositions do not construct a
proper polarized realization or the componentwise calibration and therefore
narrow, but do not retire, P05.5.

The unconditional analytic result in the source is narrower.  For the
toric degenerations of Calabi--Yau complete intersections in its
\S7, let \(\mathbf X\) be the tropicalization, let
\(\gamma\) be the polarization weight, and let \(\mu_0\) be Lebesgue
measure on the essential skeleton.  Under the three assumptions
\[
 (L^d)=\deg(\gamma),\qquad
 \varphi\in\mathrm{PC}_{\mathrm{reg}}(\mathbf X,\gamma),
 \quad\MA_{\mathrm{poly}}(\varphi)=\mu_0,
\]
and semipositivity of
\(
 \Psi=\varphi_0+(\varphi-\gamma)\circ\operatorname{trop}
\), Proposition~7.2 of \cite{BMPS26} proves
\(
 \MA_{\NA}(\Psi)=\mu_0
\)
and, over \(\mathbf C((t))\), the comparison property.  Its Lemma~7.3
computes every maximal-cell weight as one from analytic degree divided by
lattice index.  The local equality is then
\eqref{eq:frontier-polyhedral-real-local} together with Vilsmeier's
real/non-Archimedean comparison \cite[Theorem~1.1]{Vil20}; equality away
from lower-dimensional skeleton faces and equality of total masses force
the global identity.  None of this is a realization theorem for an abstract
balanced space.

The source itself formulates three sharper tasks that organize this broad
problem: enlarge the notion of polyhedral smoothness so that higher-dimensional
regularity and orthogonality hold; characterize polarized Calabi--Yau
families whose tropicalizations satisfy those properties; and determine
which matroids have Bergman fans satisfying orthogonality
\cite[pp.~3--4, \S1.5, and Remark~6.27]{BMPS26}.  By contrast, the analytic
realization of the cross-fan was a diagnostic problem formulated in this
book, not a question attributed to Botero--Mazzon--Pille--Schneider.  Its
literal compact-source and weighted-current parts are now settled by
\Cref{prop:verified-cross-compact-obstruction,prop:verified-cross-analytic-realization}.
The source's only stronger strict-positivity prospect is expressly assigned
to its upcoming sequel: its bibliography lists that sequel as ``in
preparation.''  It is therefore not used here as an available theorem on
regularity or orthogonality \cite[pp.~4 and 45]{BMPS26}.
The stronger upstairs-equality problem in
\Cref{prob:frontier-cross-fan-upstairs} is not merely book-local: after
removing an ill-defined delta-current alternative, it is precisely the
analytic specialization of the Bedford--Taylor question posed in
\cite[\S8.6.1 and Definition~8.6.2]{CLD25}.

Thus the audit gives six verdicts.  The real-scalar complete affine case in
\Cref{thm:frontier-polyhedral-affine-orthogonality} is \emph{verified},
whereas literal integral-slope regularity already fails on the affine line
by \Cref{prop:frontier-polyhedral-integral-regularity-counterexample};
strict positivity alone is \emph{disproved} by
\Cref{ex:frontier-polyhedral-cross-orthogonality}; positive growth alone,
even on the displayed Bergman fan, cannot force the conjunction of
regularity and orthogonality by
\Cref{prop:frontier-polyhedral-bergman-positive-infinity-obstruction}; the
recursive CLD and
delta-form comparison is \emph{verified} under the intrinsic proper
calibration hypotheses of
\Cref{prop:p053-projection-recursion-repaired-candidate}, with the genuine
algebraic tropicalization supplied by
\Cref{cor:p053-algebraic-chart-repaired-candidate}; the global polarized
non-Archimedean Monge--Amp\`ere comparison remains \emph{open} beyond the
realized source cases because the proper polarization, lift, mass, and
component calibration are additional inputs; and the main
higher-dimensional local contact problem remains \emph{open}.  The missing local
assertion is a contact theorem on singular fans: under an intrinsic
smoothness and strict-positivity package, positive top intersection mass of
an envelope should force contact with the obstacle.  Neither a proof nor a
counterexample satisfying both parts of that package is presently known.

\subsection{Pluriharmonic regularity}

The supplied singular descent theorem

```
