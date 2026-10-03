## Q-conclusion. The probe consequence and its limits

At an arbitrary source point $y$ of the smooth strict curve $Y$ in
Theorem P, the local-image result just proved has two cases. In the rigid
constant case $h\circ f$ is locally constant. Otherwise it supplies an
actual strict affinoid target neighbourhood $V$ of $x=f(y)$, a reduced
closed pure curve $C\hookrightarrow V$, and a finite map onto that image
from a source affinoid neighbourhood. Put $V^o=\operatorname{int}_U V$.
It is an ordinary neighbourhood of $x$ and is good separated strict
boundaryless pure of dimension $n$. Its closed subspace
$C^o=C\cap V^o$ is a good separated strict boundaryless pure curve.
The current equation on $U$ restricts to $V^o$, with compact ordinary
tests extended by zero. The closed-curve restriction proof above supplies
the intrinsic actual equation $D[h|_{C^o}]=0$.

Apply R to $C^o$ over this same possibly imperfect field. It recognizes
$h|_{C^o}$ as GR-harmonic, with no scalar stability or smoothness assumption
on the image. On the ordinary source neighbourhood
$\operatorname{int}_Y W\cap f^{-1}(V^o)$, the actual map factors through
$C^o$. GR 3.14(7) pulls back the **recognized** harmonic function.
Consequently $h\circ f$ is harmonic near $y$. The source is smooth strict,
so GR 3.4.2 and 3.12 identify this with Thuillier harmonicity. Sheafiness
treats every analytic source point and proves P. GR 4.1.2 and 3.15 then
give the stated classical and real-PL/GJR conclusions on that curve.

The local-image proof also constructs the finite lift to the normalization.
Over an imperfect field its normalization is not asserted smooth; R makes
that unnecessary. The restriction proof has already checked component
weights, singular intersections, rigid punctures, and nilpotents before
recognition. No finite-current direct image is inverted, no graph-product
current is assumed, and no admissible cover replaces ordinary interiors.

# Scope ledger, failed routes, and reproduction

R covers every field and every pure analytic curve in the original strict
boundaryless scope. The completed-algebraic current gate is proved in T;
recognition and full function-theory scalar descent are separately proved
in C and B. The result extends the algebraically closed recognition evidence
and the catalogue's algebraically closed smooth-proper-algebraic comparison,
without imposing scalar stability on the input function. It retains the
ordinary CLD equation, actual nilpotent lengths, purity, and every ordinary
open. P is an additional ground-field consequence on a pure ambient space
in any dimension. The source in P is a **smooth strict** curve, matching
the reduced testing class GR 4.1.3. No claim about arbitrary non-strict
ground-field source curves is added.

Neither statement solves original P06.2 in dimension at least two. On
such an ambient space, complementary Hessian tests have positive bidegree;
the finite separable proof T5--T9 approximates scalar tests on curves only.
Exact compact scalar-test descent after completion cannot fill that missing
finite differential-form gate. P tests over the actual ground field and
therefore does not cover probes into $X_L$ for arbitrary transcendental
$L/K$. The universal quantifiers of R apply to **curve targets**, not to
the higher-dimensional ambient of P. No counterexample in the original
strict ambient scope is constructed. The non-strict invisible-boundary
polycylinder is excluded by the original strict/boundaryless hypotheses.
P05.2 is not addressed.

The optional assertion $D[h_L]=0$ under **every** analytic extension on
curves is not claimed here. GR harmonicity and classical pluriharmonicity
of $h_L$ do follow for every extension. However, this submission has not
reconstructed a harmonic-to-**ordinary analytic CLD** zero-current theorem
against every ordinary analytic test in that upstairs scope. Wanner's
reverse comparison on algebraic test charts alone would not prove that
larger test statement. The proved ordinary current transport here remains
the completed-algebraic theorem T. This explicitly separates a remaining
optional implication from the proved recognition theorem.

No two-sign ordinary smooth decreasing psh regularization is proved for
arbitrary-field arbitrary analytic curves or higher-dimensional targets.
Weak smoothness, real PL, and GJR harmonicity do not give ordinary smooth
harmonic approximants. The known nonapproximation phenomenon for harmonic
approximants is unaffected. The convex cutoffs in Q regularize a divisor
logarithm; they are not positive approximants of $h$ or $-h$. The
mollification in T controls a fixed differentiated test; it is not
positivity-preserving regularization of the input function.

The authoritative file is `P06.2-argument.md`. It contains all reconstructed
proofs and the essential primary bodies below. `P06.2-partial.tex` is a
standalone typesetting of it; `P06.2-partial.pdf` is built twice. The exact
five-key `status.json` records the partial scope and the concrete gaps.
`self-audit.md` and `research-notes.md` record the fallible author audit
and discarded routes. `source-manifest.json`, `evidence/source-checks.json`,
and `evidence/commands.json` record input hashes, newline extraction checks,
and actual commands. No old artifact or research database is modified.

Rerun in this fresh directory with `python3 prepare.py`, followed by
`python3 build-and-check.py`. The programs use installed local tools and
bounded standard-library diagnostics; no additional model, subagent, network,
installation, or resource-heavy computation is used. No supervised compute
facility was exposed, and none was needed for these text/build operations.
The checks bind excerpts and outputs to bytes and test limited finite
lemmas; they do not establish mathematical correctness, verification,
priority, or the full atom. Native notes are returned through the required
response schema; no local alternate notes file is treated as canonical memory.

