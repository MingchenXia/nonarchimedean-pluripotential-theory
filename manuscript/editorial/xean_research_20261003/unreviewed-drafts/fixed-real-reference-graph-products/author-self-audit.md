# Author audit of the fixed-real-reference proof

This is a same-model author audit. It is not formal verification, an independent
proof review, a certification of priority, or a grant from prior PASS records.

| Requirement | Argument and check |
|---|---|
| Each prescribed real gamma unchanged | Exact identity (FC6), positive sum (RS1), P=gamma off a compact set. |
| Actual PC on all structures | (FC1)--(FC4), segment convexity and arbitrary-coface grouping; rational generators establish necessity with genuine PCCs. |
| Tangent cone lineality and centres | Active inequalities on each relative interior; every real centre has the same tangent family. |
| Exact rational decomposition | Rational continuity space; active face subspace; small rational coordinate box; positive real barycentric weights. |
| Every recession slope strict | (FC5) retained at each box vertex; recession-generator decomposition covers every nonzero vector. |
| Rational spatial domains | Each rational P_j has rational comparison walls; common rational refinement before summing; no real-reference maximum. |
| All graph cases | Kernel proof, connected real-weight normalization, unbranched complete lines; bounded edges/cycles remain in incidence system; components handled separately and in global norm. |
| Arbitrary positive real weights | Primitive integer star relations times actual real scales a,b; actual weights restored to full operator. |
| Actual saturated lattices | (5)--(7), (41)--(44); product primitive planes and all actual kink indices retained. |
| All PAPC local tests | Rational tangent correction at every tested facet on every ordinary open; rational balancing cone generators extend to real cycles. |
| Two-stage algebra | Refinement case split; first-divisor balancing; mixed symmetric formula (M); ambient affine invariance and germ locality. |
| Sole upper raw growth | (4), rational-slice support proof in cylinder; (38) for global obstruction, no lower bound or continuity of raw q. |
| Positive cylinder rational domains | Supergradient intervals have rational gradients despite real constants; (21)--(22) give rational polyhedra and exhaustive possible zero-faces. |
| Positive cylinder complete contact | Noncontact exposed interval yields zero vertex Laplacian; every incident slope affine in dual variable; first divisor supported where residual vanishes, hence full second coefficient zero. |
| Exact negative raw envelope | Original-product PCC (36); all other vertex bounds; pointed-cell far rational endpoint argument (38)--(39). |
| Full negative integral | (40)--(47) include all axes/kinks and tangential terms; (48) uses every operator vertex, not a visible-atom lower bound. |
| Refinement vertices and infinity | Newly inserted vertices inherit zero second coefficient; identical P+1/n measures on X, no added point at infinity. |
| Authentic source boundary | Cached v1 definitions appear directly in authoritative proof; no essential external theorem used without proof. |
| Original criteria | Full atom remains open; five-key partial status; candidate=false. |

Corrections retained from the accepted rational rendering: the axis correction
uses (5)--(6) with (44), not the diagonal PCC equation (36). The recession norm
rho_0 is homogeneous, and each norm ball is intersected with the carrier.
The list of local rays now points to (41), rather than the neighbourhood
formula (35). The new mixed commutativity calculation is explicit.

The proof fragments and supporting argument were checked for zero directions,
zero coefficients, dim-zero cone quotient, face lineality, nonpointed tangent
cones, bounded cells, whole-line components, remote endpoints, rational vs real
centres, boundary dual slopes, nonsaturated factor ray spans, and singular axes.
No indispensable step remains identified as unclosed in this subclass. The
remaining gaps are those of the original arbitrary-balanced-space atom, listed
in status.json. This statement records an author's judgement, not certification.

Execution evidence is in local-output.json, real-sum-output.json and
build-evidence.json. Local arithmetic only evaluates the specified finite
inputs. Compilation only establishes that the standalone text builds.
