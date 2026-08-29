# P07.1 infinite-endpoint interval subproblem (staging only)

This packet isolates the endpoint excluded from the finite constant-collar
packet.  The model is the interval

\[
S=[-\infty,R_0)\subset \mathbf R\cup\{-\infty\},
\]

with ordinary smoothness on the finite stratum and exact constancy on a
neighbourhood of \(-\infty\).  Stage-zero psh means ordinary convexity on
the finite stratum.

The question is to determine the sheaf generated from stage zero by sheaf
localization and decreasing sequential limits, and to decide whether its
ordinal filtration collapses at stage one on this model.

The candidate answer is exact finite-stratum convexity plus the endpoint
trace condition

\[
u(-\infty)=\lim_{t\to-\infty}u(t)\in\mathbf R\cup\{-\infty\}.
\]

An endpoint-minimum inequality alone is insufficient: it admits downward
jumps that cannot be decreasing limits of continuous collar-constant
generators.  Conversely, the value \(-\infty\) at the endpoint does **not**
force local identically \(-\infty\); the basic counterexample to that false
claim is \(u(t)=t\).

The proof packet constructs a genuinely decreasing sequence on one fixed
endpoint neighbourhood.  It combines monotone Gaussian heat regularization
of a global convex Lipschitz extension with a smooth exact maximum that
clamps the coordinate to \(-n\) on a terminal tail.  No uniform-to-monotone
subsequence argument is needed, so the construction also handles endpoint
trace \(-\infty\).

Status: isolated candidate only.  It is not a live-book input, has not been
submitted to production Rethlas, and does not retire P07.1.  Even after
verification it resolves only this one-dimensional interval model, not the
star examples or the general CLD hierarchy question.
