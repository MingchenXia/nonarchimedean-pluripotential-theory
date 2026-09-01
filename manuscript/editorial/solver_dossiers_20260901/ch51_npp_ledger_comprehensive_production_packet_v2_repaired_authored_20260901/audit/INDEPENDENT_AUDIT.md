# Independent hostile audit of the Chapter 51 comprehensive nonpluripolar ledger v2

Date: 1 September 2026

## Binary verdict

**PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET.**  The blocker list is
empty.  The exact v2 postimage repairs every blocker in the independent v1
audit, reproduces the local and compact/global nonpluripolar-product ledger
with the stated scope, and completes a clean focused and full-book build.

This is an independent mathematical, source, exact-byte, and assembly audit.
It is not a production Rethlas verdict, live integration authorization, or a
novelty claim.  The accepted narrow no-pluripolar-charge paragraph remains a
separate already verified input; this report does not recycle that receipt as
verification of the larger ledger.

## Frozen target

The audited sibling is

`ch51_npp_ledger_comprehensive_candidate_v2_20260901`.

Its controlling identities are:

| object | SHA-256 |
|---|---|
| candidate `SHA256SUMS` | `ffddd14e1d8b195fe1ec01ce3ee26b4c6ec2947865bc999c15e88da23c1535a2` |
| frozen base | `4db4d9028c80b47994143172c356c39419954471af222b8a4f9740b9b5fcf834` |
| local replacement | `9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575` |
| ledger replacement | `187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70` |
| exact postimage | `e22e579757ac55a3363be1a55d7692ae8efef921a79f7eb537d2de08c2a88b73` |
| exact splice patch | `07da864f22f1ff3d23b6083557018d3117ec0e7408fb5e66ad3f1e1f3e7da17d` |
| preserved accepted no-charge block | `6cb839bc8a05dc354ac5b035c7e6841eb707c28a9168b10a406731bfbccd9731` |
| focused PDF | `5653f02b7a2984d849741a21567b568b41c01bfa28a8b87f59dd948eca749112` |
| full-book PDF | `fc16c0e60e90954c7b74e6856ef5d505876e7928b30a345779b2e9382faa905e` |
| full-book log | `1a7437aee39bf5eed901ddf087a0b477e112c5e842c6d350f4be81f9fb0991b2` |

The candidate checker returns `PASS_AUTHORED_ONLY_V2`, reconstructs the
postimage from two unique anchors, and checks the 3,518-page full-book
evidence.  I reran that checker read-only and independently recomputed the
manifest and all identities above.

## Mathematical audit

### Local definition and auxiliary choices

The local mass condition is the correct condition for the increasing
indicator-restricted Bedford--Taylor products to have locally finite
coefficient measures.  Uniform comparability of strictly positive trace
forms on compact subsets makes it independent of the auxiliary form.  The
Kiselman example is used only for the required warning that local finiteness
can fail for `p >= 2`.

For a bounded pluriharmonic change `u'_j=u_j+h_j`, the proof now contains
both locus inclusions, both trace-mass inequalities, and the common
exhaustion.  On the common exhaustion the two bounded Bedford--Taylor
currents are termwise equal.  Only after the capacity argument proves that
both locally finite limits charge no pluripolar set does the proof invoke the
admissible-exhaustion rule.  The dependence-on-potentials argument is
therefore two-directional and noncircular.

The admissible-exhaustion statement specifies the truncation depth, the
restricted current, increasing Borel sets, and a pluripolar complement.  Its
conclusion follows from dominated convergence for the locally finite trace
measure and is exactly the form needed later.

### No pluripolar charge

For each fixed truncation level, all factors are locally bounded psh
functions on a relatively compact strongly pseudoconvex coordinate domain.
After affine normalization into `(0,1)`, the arithmetic mean is an admissible
Bedford--Taylor capacity test.  Multilinearity and positivity give the mixed
coefficient bound by its Monge--Ampere measure.  Zero outer capacity of a
pluripolar set annihilates every fixed-level measure; continuity from below
then annihilates the locally finite limit.  No potential-independence or
closedness conclusion is used in this step.

### Positive-cone multilinearity

The common-exhaustion identity uses the level `2k` for `u+v` and level `k`
for the two summands, so it is an identity only where all untruncated
potentials are visible; it does not assert a false global levelwise
truncation formula.  If both summand products are locally finite, positivity
bounds the canonical truncations of the sum.  Conversely, for a fixed level
of one summand, removing the other potential's pole set is legitimate because
that bounded Bedford--Taylor measure does not charge pluripolar sets.  On the
remaining locus it is dominated by the level `m+k` truncation of the sum.
The uniform bound followed by the supremum over `m` proves both converse
local-finiteness implications.

### Compact Kahler finiteness and closedness

Repeated positive-cone additivity reduces compact-Kahler finiteness to
Kahler cohomology classes.  The proof then chooses positive representatives,
not arbitrary smooth representatives.  Local smooth psh potentials and
global bounded positive truncations give the uniform cohomological mass
bound.  This is independent of the later closedness proof.

The closedness argument keeps the indicator-restricted currents distinct
from closed truncation currents.  The cutoff `w_k`, the second cutoff, the
Bedford--Taylor chain rule, both Cauchy--Schwarz factors, and the integration
by parts estimate have the required boundedness and support properties.  The
first factor is uniformly bounded by the already established local mass
condition.  The second tends to zero by dominated convergence and the
already established no-charge property.  Constant-coefficient positive test
forms span the missing bidegrees, so the resulting current is closed.

### Singularities and mixed masses

The singularity orientation agrees with Darvas--Di Nezza--Lu: replacing
each potential by a less singular one increases the total mixed
nonpluripolar mass.  For `p<n`, adjoining `n-p` copies of the smooth Kahler
form turns the imported `n`-fold theorem into the displayed mixed statement.
No pointwise current inequality is asserted.

### Modifications

The pullback of a positive `(1,1)`-current is constructed from local psh
potentials.  Compositions with the modification are psh because every source
component meets the biholomorphic dense locus; pluriharmonic transition
functions patch the local currents.

For the analytic exceptional pair, the proof imposes the exact identity
`F=mu^{-1}(Z)`.  The upstairs nonpluripolar product gives no trace mass to
`F`.  Comparing the pullback of a Hermitian trace form downstairs with a
Kahler trace form upstairs and applying the smooth projection formula proves
that its pushforward gives no trace mass to `Z`.

On the biholomorphic locus, every downstairs fixed truncation is dominated
by the pushforward.  The fixed-level bounded Bedford--Taylor capacity
argument gives zero mass on the analytic set `Z`, so the domination yields a
uniform local trace-mass bound downstairs.  The downstairs limit is thus
locally finite.  Both it and the pushforward vanish on `Z` and agree off
`Z`, hence agree globally.  This proves the current identity before the
top-degree mass equality is integrated.

## Primary-source audit

I checked the pinned source interfaces rather than relying only on the
candidate's source ledger:

- BEGZ arXiv:0812.3674v2, extracted lines 189--478: local definition,
  Kiselman example, Proposition 1.4, Lemma 1.5, compact-Kahler finiteness,
  the Fujiki-class modification formula, closedness, and the chain rule;
- Bedford--Taylor, pinned extraction lines 462--469, 960--981, and
  1104--1118: inner/outer capacity and the zero-capacity characterization;
- Darvas--Di Nezza--Lu arXiv:1705.05796, extracted lines 62--86: the
  orientation and full mixed-mass theorem.

The candidate expands compressed or omitted source arguments but does not
strengthen their mathematical scope.  The broader modification statement is
the standard Fujiki-class formula already present in BEGZ Remark 1.7.

## Assembly and style

The v1 fatal cleveref enumeration form is replaced by the tested `item
\cref{...}` construction.  The focused ten-page harness and the exact
3,518-page full-book postimage build both complete without fatal errors,
undefined controls/references/citations, duplicate labels, or cleveref
hyperlink failures.  The accepted no-charge block is byte-identical to its
production-verified predecessor.  The replacement preserves `\eqref`, uses
the book's differential and constant conventions, adds no exercises, and
does not give a conventional name to the theorem.

## Scope firewall and next gate

This ledger does not retire a Chapter 72 atom and does not claim that every
compact complex manifold outside Fujiki class has locally finite
nonpluripolar products.  It supplies a self-contained foundation needed by
later chapters and P14.8.

The only next permissible promotion step is a source-closed production
Rethlas submission of the exact v2 statement/proof closure, followed by an
independent receipt audit.  Until that succeeds, the live Chapter 51 source
must remain unchanged.

