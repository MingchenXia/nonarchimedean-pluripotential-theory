#!/usr/bin/env python3
"""Own quote-free source ledger generator from immutable metadata and own analysis."""
import pathlib,json
P=pathlib.Path(__file__).resolve().parent
math=json.loads((P/'mathematical-packet-bindings.json').read_text())
primary=json.loads((P/'private-primary-packet-bindings.json').read_text())
bind=json.loads((P/'source-byte-bindings.json').read_text())
units=json.loads((P/'primary-unit-coverage.json').read_text())['units']
text='''# Source application ledger

This public ledger contains metadata and our own analysis only. No third-party passages, PDF pixels, or full source bodies are republished here. Long primary tool reads remain LOCALONLY. Hashes bind bytes; labels and execution do not establish mathematical correctness. All 25 bound mathematical objects were read in whole bounded chunks, including duplicated arguments and every associated scope, ledger and acceptance object. Exactly six WHOLE mathematical grants, not 25 separate grants, are recognized. The entire new289 object is unreviewed data.

## Six grants and their actual applications

A224: real coefficients and rational geometry remain separate requirements. We preserve the actual reference, never turn a real maximum into a rational carrier by assertion, and do not interpret rational-density impossibility as real-density impossibility. Its whole mathematical scope and clarification are retained; it is not invoked as a density theorem for the new book sector.

B225: finite embedded compact positive-balanced constraints are distinct from abstract compact polyhedral categories. Its obstruction is retained in the exclusions; our pages are complete noncompact affine spaces. No abstract compact classification is inferred.

R230: under its complete finite rational positive-balanced and actual continuous positive-growth reference hypotheses, actual unrestricted bounded-continuous obstacle envelopes are continuous, finite, real-endpoint PC and bounded relative to that actual reference. We use this result only to supply continuous input f. It is not PA density, and its usc conclusion is not a license to assign MA before genuine closure.

S262: its WHOLE finite signed primitive tangent-corrected calculus, raw balance/commutativity/refinement, rational-reference gluing and representation/completion foundations are retained in their qualified domains. We verify the page support argument for all nonnegative local cycles independently. Arbitrary zero intermediate weights are allowed; positivity follows from support induction rather than an unsigned definition. Its literal noncompact failures remain distinct from the continuous scoped theorem. Its source references do not enlarge the four bound primaries or authorize AR10 as a new primary.

S272: its WHOLE actual-real-reference mixed completion is used only after the new genuine regularization. Native210 whole historical evidence remains INCONCLUSIVE; the ROOT mathematical acceptance does not relabel it. The fixed-C moment is (2d/epsilon) C deg(gamma)+J0. Ordinary weak/net continuity and global vague uniform continuity are retained; weak/BL uniformity is only fixed-C. The actual-reference flat-jet theorem is used on every specified rational tangent refinement, with actual positive real page weights, continuous finite gamma and positive branch recession. Its finite positive rational-reference simplex decomposition creates a COMMON rational germ in every summand; it does not add the unrelated remainder to the flat jet. The entire unrestricted roof proof is checked, including rational boundary endpoints, real barycentric centers, and shrinking rational simplices without continuity of competitors. No arbitrary-irrational-jet exact realization is asserted.

S282: only its WHOLE mathematical paper with ALL SIX clarifications is granted. Its full-affine above approximation was independently reconstructed, including exact finite interpolation, graph-face spatial rationality, scalar-extension membership, and global error. Its inherited-complex clarification determines our page convexity proof. Native215 historical whole evidence remains INCONCLUSIVE, without automatic acceptance. Historical Author213 saved four-note draft differs in every prose field from FINAL; Auditor215 saved output equals its five-note FINAL. First-pass warnings versus final clean build and lost builtin handles 249/204/27 remain as supplied historical data. No inaccessible original output was opened, recreated, or promoted. All previous whole qualifications and original OPEN status remain.

Whole new289: every proposed used affine, trace, and book step is independently proved or assigned a specific one-of-six dependency in proof-source-coverage.md. It supplies no seventh grant. No compact291/native218, isolated288/native217, ROOT290, unbound/private ACTIVE paper, or hot feedback was read.

All six clarification controls are itemized in our own clarification-control.md, including the earlier chart/continuity restrictions, graph half-jump/count conventions, cutoff task typo and historical native210/215 evidence status.

## Mathematical input byte metadata

LF counts below count newline bytes. Character-range read records are distinct from LF units. The complete mathematical read coverage is recorded in whole-read-coverage.json. Initial aggregate output truncations were corrected by bounded rereads; read-coverage.jsonl records both attempts rather than presenting the first attempts as complete visible evidence.

| Index | Bound object | Bytes | LF | SHA-256 |
|---|---|---:|---:|---|
'''
for b in bind:
 if b['kind']=='math':text+=f"| {b['index']} | {b['label']} | {b['bytes']} | {b['LF_lines']} | {b['sha256']} |\n"
text+='''
## Four sole primary byte objects

All four full byte objects were hash-read, and the pertinent complete immediate statement/proof units were read in the LF text counterparts. No web fetch was performed. No long source passage or pixel appears in the public ledger. The arXiv v1 and BBGS version of record are distinct frozen versions. The following analysis does not silently import their wider domains.

| Primary/format | Frozen version | URL | Bytes | LF | SHA-256 |
|---|---|---|---:|---:|---|
'''
for i,e in enumerate(primary):
 b=next(x for x in bind if x['kind']=='primary' and x['index']==i)
 text+=f"| {e['label']}/{e['format']} | {e['version']} | {e['literal_url']} | {b['bytes']} | {b['LF_lines']} | {b['sha256']} |\n"
text+='''
## Complete pertinent original units and own application analysis

LF numbering splits only on newline, not PDF form-feed. Extra adjacent definition beginnings, where read, do not acquire authority. All applied immediate proof units below are complete.

| Source | LF unit | Statement/proof unit |
|---|---|---|
'''
for label,rs in units.items():
 for a,b,title in rs:text+=f'| {label} | {a}--{b} | {title} |\n'
text+='''
BMPS affine/polyhedral definitions fix finite rational carrying structures, tangent lattices, quotient normals and refinements. Its divisor includes tangential correction, necessary with arbitrary inward lifts. Full normal-independence and refinement proofs were checked rather than substituting the Euclidean formula. Its Lemma 3.4 forward proof inserts the center as a rational vertex, which cannot be done automatically for irrational centers; its integer gcd adjustment is not an automatic proof for real weights. We therefore prove common supports and all-cycle positivity directly for our sector. Definition 3.2 has rational endpoints but real coefficients and centers. The automatic continuity sentence referencing BBGS does not eliminate downward irrational spikes in this domain. Our continuous hypothesis is essential.

BMPS Proposition 3.22/Definition 3.23 fixes the decreasing/uniform convention. We prove a global shift schedule ourselves and do not import compactification/Dini as an ungranted argument on the whole noncompact book. Its raw and degree units calibrate the unnormalized recursion, edge integration-by-parts sign, and finite mass, without appended factorial. Definition 4.15 requires positivity in all nonzero recession directions. The complete Section 6 envelope statements were inspected, but their broad literal regularization assertions do not substitute for R230 plus our genuine construction. Delegated AR10 arguments are not used as fresh primary evidence.

BBGS works with a Euclidean quasi-embedding and unit normals and uses the opposite concavity/product sign from our primitive convex convention. Definitions 3.1--3.9 and full restriction/subdivision Proposition 3.12, commutativity Proposition 3.15, balance Lemma 3.18 and Proposition 3.19 were read in their immediate proof units. We do not convert them into primitive saturated lattice calculations without the whole grants' calibrated calculus. The full Definition 5.1 and Lemma 6.1/Theorem 6.2 use real endpoints and subdivisions through the center. Their automatic continuity proof is not imported into printed rational-endpoint PC. Our all-face book proof explicitly supplies real-endpoint completion for continuous data only.

Ordinary convex duality, compactness, separation, finite polyhedral generation and rational projection are reasoned in the paper. Their recursively deeper ordinary foundations are disclosed rather than claimed rebuilt. The granted raw completion and jet gluing retain their full qualifications, actual reference, signed intermediates, and zero-mass case. No mathematical conclusion is drawn from a PASS label or historical native evidence status alone.
'''
(P/'source-application-ledger.md').write_text(text)
print('Quote-free source ledger generated: six whole grants, 25 metadata objects, four primaries, all pertinent LF units.')
