# Upper-semicontinuous regularization of local FS envelopes

The unconditional universal assertions are no longer active: they were
disproved by the continuous-obstacle nodal counterexample in
`prop:ch15-nodal-local-envelope`, verified in production run
`20260825T094005Z_10ac70696f69`, item
`pi_31f95353b7e94f3cb98b09b6`.  This packet remains active only for the
sharp positive classification, beginning with normal or analytically
unibranch domains.  The already-upper-semicontinuous raw-envelope theorem
remains valid.

Let \(U\) be a good strict Berkovich analytic domain over a complete
nontrivially valued non-Archimedean field and let
\(f:U\to\mathbf R\cup\{-\infty\}\) be an upper-semicontinuous obstacle.
Define
\[
 P^{\mathrm{raw}}_U f
 =\sup\{h:h\text{ is local FS or semipositive real PL on }U,\ h\leq f\}.
\]
The raw supremum is classically psh whenever it is already upper
semicontinuous: finite maxima form an increasing net and
Gubler--Rabinoff Theorem 6.5 applies to an upper-semicontinuous pointwise
limit of an arbitrary net of classically psh functions.  Here finite maxima
are classically psh by the general stability of classical psh functions.
Do not instead invoke closure of semipositive real PL functions under maxima
with arbitrary real coefficients: the strict-topology PL statement has a
coefficient-group caveat in that source.

Determine sharp hypotheses under which
\[
                         (P^{\mathrm{raw}}_Uf)^*
\]
is classically psh, and determine separately when it is CLD-v2 psh.  For the
continuity subproblem, restrict \(f\) to continuous real-valued obstacles and
determine when the regularized envelope is continuous.  Start with:

1. normal or analytically unibranch curves and higher-dimensional domains;
2. smooth analytic curves;
3. polystable tropical charts;
4. boundaryless domains carrying a relatively ample formal model;
5. smooth higher-dimensional analytic spaces;
6. spaces with relative boundary.

The proof must address whether upper-semicontinuous regularization commutes
with pullback to every analytic curve after scalar extension. It may use
Choquet nets, barriers, local model envelopes, or capacity, but may not assume
this commutation. Search for a counterexample at a relative boundary or on a
singular/non-normal chart.

Keep the local approximation theorem in its exact scope:
Gubler--Rabinoff Theorem 1.5 starts with a semipositive real PL function on a
boundaryless strict analytic space and gives local **uniform** approximation
by locally Fubini--Study functions.  It neither proves monotone approximation
nor the obstacle-envelope assertion for a general classical psh function.

Return the strongest verified positive classification, with complete proofs,
and test every proposed hypothesis against the integrated nodal
counterexample.  Distinguish the raw supremum, usc regularization, classical
psh, CLD-v2 psh, and continuity.
