# Exact live-patch plan after the Chapter 16 node-example move

Date: 29 August 2026  
Status: prepared but **not applied**.  The normal revised3 gate is satisfied.
Every hunk below remains blocked until the exact revised3-bound componentwise
request returns final `correct`, zero critical errors, zero gaps, and the exact
proof digest
`cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.

The plan is anchored to live Chapter 16 SHA-256
`d4e5fb3b6b76029853b583cd534e57eff878b2cfddf79277d99d0d6385702fa4`.
The nodal/double-thickening example is now the input at line 1309, before the
trivially valued subsubsection at line 1311.  Do not apply this plan if that
hash or those textual anchors change without first refreshing the hunks.

Tokens of the form `@@COMPONENT_*@@` must be replaced from the independently
audited componentwise receipt.  Their presence is a hard stop, not permission
to infer missing provenance.

## Hunk 1: replace the dimension-one overview

Target: `manuscript/parts/part2/ch16_bedford_taylor.tex`, current lines
1212--1259.  Preserve lines 1261--1264 defining `\operatorname{Rat}(C)`.
Use the following exact replacement prose.

```tex
In analytic dimension one the ambiguity can be removed throughout the normal
category over an arbitrary complete non-Archimedean ground field, including a
trivially valued one.  On every connected good separated normal boundaryless
pure curve, a positive closed ordinary current of bidegree $(0,0)$ is a
nonnegative constant multiple of the integration current.  Neither strictness
nor any quasi-smoothness or rig-smoothness hypothesis is needed.  Since an
integration current is Bedford--Taylor, this gives the full predicate of
\cite[Definition~8.6.2]{CLD25} on such a normal curve.

There is also a componentwise statement.  Let $X$ be a good separated strict
boundaryless pure one-dimensional analytic space, with no reducedness
assumption.  Over either a trivial or nontrivial valuation, every positive
closed ordinary current of bidegree $(0,0)$ is a unique locally finite
nonnegative linear combination of the currents obtained from the
normalizations of the reduced irreducible components.  Nilreduction preserves
ordinary CLD forms, currents, positivity, closedness, and the continuous psh
sheaf, whereas the fundamental integration current retains the generic
component multiplicities.  Equality of the curvature currents defined by the
nonreduced fundamental current is equivalent to equality on the reduction,
and every classified current has Bedford--Taylor independence for continuous
psh pairs.

The results are printed in the order in which their proof mechanisms were
developed.  The first chain treats a nontrivially valued field by legal source
localization, exact virtual-annular collars, finite normalization, and
rigid-point zero-atom estimates.  Its collar constructions and examples remain
useful, but its classification theorems are subsumed by the later
arbitrary-valued statements.  The controlling normal proof instead localizes
with a compact smooth source cutoff.  It keeps the actual analytic
calibration coefficient distinct from the integral slope gcd, proves that
their ratio is invariant under moment refinement, uses Riemann--Roch on the
residual curve, and propagates the resulting ratio along the connected
type--$2/3$ graph.  The componentwise proof then combines this classification
with the two valuation-specific zero-atom estimates at the conductor and
component-intersection locus.

The direct trivially valued packet printed last is retained independently.  It
exhibits the infinite-star geometry of the projective line and a smooth
projective curve by finite analytic moments, treats the two boundaryless CLD
interval structures, constructs the abstract weighted-cross counterexample,
and explains by a refined analytic moment why the natural four-punctured
algebraic cross cannot carry the unequal weights.  Its analytic curve
classifications are special cases of the general normal theorem, but the
explicit calculations remain useful examples.
```

## Hunk 2: insert the exact arbitrary-valued block after the node example

Target anchor:

```tex
\input{editorial/rethlas_packets_20260828/p21p3_canonical_collar_reducible_node_example_live_ready_staging_20260828.tex}

\subsubsection{Direct trivially valued cases}
```

Insert the following exact block between those two lines.  The already-live
nontrivial zero-atom statement/proof at current lines 1296--1297 remains in
place and must not be duplicated.

```tex
\subsubsection{Arbitrary-valued curves}
\label{sec:ch16-arbitrary-valued-curves}

The preceding collar, normalization, and nodal results record the earlier
nontrivially valued route.  We now give the controlling argument over an
arbitrary complete non-Archimedean field.  Its first additional local input is
the trivially valued counterpart of
\Cref{lem:p21p3-componentwise-normal-rigid-zero-atom}.  Scalar extension to a
Gauss field transfers the atom to a rigid Shilov lift; the proof includes
imperfect and inseparable residue extensions.

\input{editorial/rethlas_packets_20260829/p213_trivial_gauss_rigid_zero_atom_20260829/p213_trivial_gauss_rigid_zero_atom_statement_20260829.tex}
\input{editorial/rethlas_packets_20260829/p213_trivial_gauss_rigid_zero_atom_20260829/p213_trivial_gauss_rigid_zero_atom_proof_20260829.tex}

The next exact packet constructs the source-cutoff pushforward, proves the
one-dimensional Euclidean current decomposition and balancing statement, and
classifies positive closed ordinary currents on a connected normal curve.
The proof uses the analytic integration-current calibration rather than
identifying it with a lattice gcd.

\input{editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_statement_revised3_20260829.tex}
\begingroup
\emergencystretch=2em
\input{editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_proof_revised3_20260829.tex}
\endgroup

Finally, nilreduction and finite componentwise normalization give the
arbitrary-valued reducible and nonreduced endpoint.  The two preceding
zero-atom lemmas exclude cancellation of component curvature measures at the
locally finite rigid conductor and intersection locus.

\input{editorial/rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_statement_live_ready_20260829.tex}
\begingroup
\emergencystretch=2em
\input{editorial/rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_proof_live_ready_20260829.tex}
\endgroup

The pre-promotion sentence in
\Cref{rem:p213-componentwise-av-scope} is retained verbatim to preserve the
exact production-verified source bytes.  Its two gates are discharged by the
production receipts recorded in the source notes below.
```

The new editorial section label `sec:ch16-arbitrary-valued-curves` is absent
from the current live manuscript.  All labels in the three exact input pairs
are likewise collision-free; the complete manifest is in
`p213_arbitrary_curve_conditional_live_integration_map_20260829.md`.

## Hunk 3: replace the direct trivially valued transition

Target: current lines 1314--1325, which will move downward after Hunk 2.  Keep
the existing statement/proof inputs byte-for-byte.  Replace only the prose by

```tex
The next packet gives an independent calculation and an example bank.  Its
interval classification and abstract weighted-cross counterexample are not
instances of the normal analytic-curve theorem.  Its projective-line and
smooth algebraic-curve classifications are now special cases of
\Cref{prop:p213-normal-curve-arbitrary-valuation-current-revised}, but their
direct finite-moment proofs display the infinite-star mechanism explicitly.
The four-punctured calculation then shows why coarse balancing is insufficient:
one additional analytic unit detects the forbidden unequal weights.  The
statements are grouped before their proofs to preserve the exact bytes
accepted by production verification.
```

## Hunk 4: Chapter 16 source-note insertion

In the `Harmonic ambiguity` provenance block, after the historical paragraph
ending at current line 4183 and before the direct trivially valued paragraph,
insert the following normal-packet paragraph exactly:

```tex
The controlling arbitrary-valued normal-curve result is
\Cref{lem:p213-variation-graph-source-cutoff,lem:p213-euclidean-one-dimensional-current-revised,prop:p213-normal-curve-arbitrary-valuation-current-revised}.
Its exact statement and proof have SHA-256 values
\texttt{339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7}
and
\texttt{d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660}.
The independent hostile audit has SHA-256
\texttt{534154de06a9c7c63d5a060c4feac5d47a274af168177a305f64972483134c41}.
Production item \nolinkurl{pi_d9543424f0492e1412e0d203}, using
\texttt{gpt-5.6-sol} at \texttt{xhigh}, returned final
\texttt{correct}, zero critical errors, and zero gaps; its proof digest is
the exact proof hash.  The controlling receipt has SHA-256
\texttt{5e3c0e39ce7c7cd520291fe7dc7b1c00760a9b5aa5369779e8488e5cdfe3a101}.
The calibration-defective first revision and the second revision's unrelated
smooth-locus gap remain preserved as noncontrolling rejected provenance.
```

Immediately after it, insert a componentwise paragraph of the following exact
form only after replacing every token from the final receipt:

```tex
The arbitrary-valued componentwise endpoint is
\Cref{prop:p213-componentwise-arbitrary-valuation}.  Its principal statement
and proof have SHA-256 values
\texttt{91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0}
and
\texttt{098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1}.
The complete revised3-bound materialization has statement and proof hashes
\texttt{d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6}
and
\texttt{cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f}.
Production item \nolinkurl{@@COMPONENT_ITEM@@}, using
\texttt{gpt-5.6-sol} at \texttt{xhigh}, returned final
\texttt{correct}, zero critical errors, and zero gaps; its proof digest is
the exact materialized proof hash.  The controlling receipt has SHA-256
\texttt{@@COMPONENT_RECEIPT_SHA256@@}.
```

Replace the obsolete scope paragraph at current lines 4199--4209.  Its new
content must distinguish the scopes exactly: the normal theorem allows either
valuation and does not assume strictness; the componentwise theorem allows
either valuation but assumes strictness and proves only the continuous-pair
conclusion; the older collar results remain specialized chronology.

## Hunk 5: exact Chapter 72 residual problem

Keep the section title and replace the current problem environment at lines
2321--2345 by the following exact text.  This preserves both equation labels.

```tex
\begin{problem}
\label{prob:frontier-cross-fan-upstairs}
Let $K$ be a complete non-Archimedean field, let $n\geq2$, and let $X$ be a
good separated strict boundaryless pure $n$-dimensional $K$-analytic space.
Determine whether every positive $\mathrm d'$- and
$\mathrm d''$-closed CLD current $T$ of bidegree $(p,p)$,
$0\leq p\leq n-1$, has the following property: for every open
$W\subseteq X$ and all continuous psh functions $U,V$ on $W$,
\begin{equation}
                  \mathrm d'\mathrm d''[U]
                  =\mathrm d'\mathrm d''[V]
 \label{eq:p21p3-post-nonreduced-residual-equal-curvature}
\end{equation}
implies
\begin{equation}
 \mathrm d'\mathrm d''\bigl(U\,T|_W\bigr)
 =\mathrm d'\mathrm d''\bigl(V\,T|_W\bigr).
 \label{eq:p21p3-post-nonreduced-residual-bt}
\end{equation}
If this fails, construct a counterexample.  A counterexample could provide an
analytic weighted-gluing defect before tropical pushforward.
\end{problem}

No one-dimensional case remains inside the displayed ambient hypotheses.
Indeed, \Cref{prop:p213-componentwise-arbitrary-valuation} treats either
valuation, arbitrary reducibility and nilpotent structure, and normalizations
with no smoothness assumption.  Non-good, non-separated, non-strict, and
boundary cases lie outside the displayed problem rather than forming hidden
residual atoms.
```

Replace the opening summary at current lines 2290--2319 consistently, citing
the new normal and componentwise propositions and both zero-atom lemmas.  Keep
the older run history at lines 2358--2452, then append the two new production
records.  At lines 2454--2461, retain the discontinuous-potential firewall and
state exactly: P21.3 remains one T2 atom, now only in dimension at least two;
the inventory stays at 15 environments and 54 atoms, with tier totals
`0/6/14/17/17`.

## Hunk 6: exact atomic-inventory statement

Replace the P21.3 bullet at current lines 423--439 of
`open_problem_atomic_inventory_20260824.md` by

```markdown
- **P21.3** `[T2; open residual]` In analytic dimension at least two,
  determine whether every positive closed CLD current of bidegree
  \((p,p)\), \(0\le p\le n-1\), on a good separated strict boundaryless
  pure \(n\)-dimensional analytic space has Bedford--Taylor independence for
  continuous psh pairs of equal curvature, or construct a counterexample.
  The entire one-dimensional case inside these ambient hypotheses is settled
  by `prop:p213-componentwise-arbitrary-valuation`, over either a trivial or
  nontrivial valuation and without reducedness or normalization-smoothness
  assumptions.  The literal discontinuous-potential predicate of CLD
  Definition 8.6.2 is a stronger scope boundary and is not a separately
  counted atom.
```

Preserve the dated earlier addenda.  Replace the controlling status at current
lines 544--549 by a receipt-backed addendum stating that the one-dimensional
residual is retired, but the higher-dimensional P21.3 atom and all counts are
unchanged.

## Hunk 7: ledger entries and receipts

After the direct trivially valued curve entry ending at current line 993 of
`rethlas_verified_results.md`, add two entries:

1. an exact normal-curve entry using the hashes and item in Hunk 4, request
   hash
   `d9a4ad02796009280917f1c0d1de216503c5fdcd25aef28c073570e26baebf1f`,
   response hash
   `93c586e3de8884e30e7e7c320e6364cb2bb9c6c35d38593361e34c9a85f06860`,
   headers hash
   `0f0bcd114f923264cbcfb398d5d8fc10b556eda20373330912c3ef8fe3eca217`,
   and exact non-Archimedean scope;
2. a dependency-closed componentwise entry using the eight source hashes, the
   two materialized hashes, request hash
   `6920d2582649e1fcedcc3a729242e1ca02fded05502cc878a36f4e8652929365`,
   and only the final response/header/item/receipt data supplied by the
   validated response.

Do not call the normal theorem Archimedean: the receipt's phrase “arbitrary
complete valued field” is an editorial imprecision.  Use “arbitrary complete
non-Archimedean field, possibly trivially valued.”

Create immutable integration receipts only after applying and auditing the
live patch.  They must record the old and new live-file hashes, exact source
hashes, transport hashes, proof digests, compile result, and visually inspected
page range.  Preserve all earlier rejection and historical verification files.

## Hard-stop validation

Before any application:

1. require the current live hashes to match the refreshed anchors;
2. require no `@@COMPONENT_*@@` token to remain;
3. independently validate the componentwise response and receipt;
4. rehash all eight source inputs and both materialized request fields;
5. require the componentwise proof digest to equal the prepared materialized
   proof hash;
6. only then apply the patch, clean-build the full book, scan labels and
   references, inspect every new Chapter 16 and 72 page, and run a separate
   post-integration audit.
