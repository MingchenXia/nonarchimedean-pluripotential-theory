# Upper-semicontinuous regularization of local FS envelopes

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

Determine when
\[
                         (P^{\mathrm{raw}}_Uf)^*
\]
is classically psh, CLD-v2 psh, or continuous. Try first on:

1. smooth analytic curves;
2. polystable tropical charts;
3. boundaryless domains carrying a relatively ample formal model;
4. smooth higher-dimensional analytic spaces;
5. spaces with relative boundary.

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

Return the strongest verified theorem, explicit counterexamples if any, and
an exact conditional reduction for the remaining cases. Distinguish raw
supremum, usc regularization, and continuity.
