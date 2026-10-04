# Research record and residual claims

This run addresses the new all-dimensional finite-Galois current-ascent
gate. It preserves the original P06.2 task in original-task.json and
original-problem.txt and the assignment in assignment-verbatim.txt. The
original scope has not been replaced by the gate.

The entire root proposal was read from the read-only source and copied to
sources/proposal.md for reproducibility. It was treated as fallible. The
root argument was independently reconstructed: actual point stabilizers,
actual Banach-algebra root lifting, the same-carrier calibration comparison,
actual tensor idempotents, norm-unit form matching, finite ordinary compact
cutoffs, calibrated collar bounds, and weak convergence against continuous
functions. Two clarifications are essential: rank-one boundary-face contact
uses vanishing on ambient W; and the smooth-multiplier Stokes step uses an
enlarged moment including the multiplier's own coordinates.

The read-only earlier quadratic argument in
/workspace/research/deliverables/round-12/P06.2-all-separable-quadratic-ascent-argument.md
was inspected to understand the distinction between scalar projection and
same-carrier restriction. Its theorem, proof, receipts, and verdicts were
not premises. No older special case is represented as new progress. The
purely inseparable route was not needed or imported. The relevant original
book scope was checked in Chapter 72 and the input catalogue; recognition
results described there were not used as theorem grants.

The exact new claim is (T): equivalence of ordinary zero-Hessian currents
under every finite Galois extension, for finite continuous real functions
on actual good, separated, strict, boundaryless, pure positive-dimensional
spaces. Forward transport is tested against all compact complementary
forms, not only pulled-back forms; the reverse uses canonical scalar
projection without a field-degree factor. There is no psh or curve
recognition input.

The remaining original atom is continuous zero-current recognition outside
the catalogue's verified scopes. In particular, this proof does not
regularize both signs into the CLD-psh hierarchy or produce classical
pluriharmonic approximants. No finite-stage descent and gluing of arbitrary
complementary forms through a completed algebraic extension is proved.
Those are separate tasks, and no ascent along transcendental extensions
is claimed. The non-strict arbitrary-radius counterexample remains outside
this strict theorem and is not contradicted.

Finite diagnostics are deliberately auxiliary. The exterior test checks
all n^2 complementary basis components for n=1,...,12 (650 components
total) and finds exactly one second-normal-cutoff survivor in each
dimension. Polynomial collar scaling shows a nonvanishing scalar
coefficient yields variation proportional to delta^-1, whereas first-order
vanishing yields a bounded delta^0 scale. The cutoff used in that symbolic
diagnostic is only C3 after zero extension; it is not substituted for the
smooth cutoff in the proof. The exhaustive algebra diagnostic checks 4096
elements and 3840 units of F_16[u]/u^3; it finds eight invariant elements,
all unit norms in F_2[u]/u^3, and nilpotence index three. These are exact
finite results about a toy algebra, not analytic verification or a
counterexample in the original ambient scope.

The environment is Python 3.12.14 with installed SymPy 1.14.0 and installed
Pandoc/XeLaTeX. No network, installation, extra model, subagent, external
message, old-artifact write, SQL operation, credential change, proxy/CA
change, or resource-heavy computation was used. The cloud environment
status tool was absent from the installed metadata; no network or runtime
configuration was needed. No supervised heavy-compute facility was supplied
or required.

Commands and outputs are retained in the fresh workspace. Rerun with
`python embed_sources.py`,
`python diagnostics/finite_checks.py > diagnostics/output.json`,
`python build_documents.py`, and `python validate_artifacts.py`.
Compilation and self-audit are not formal verification or priority
certification. The final native notes have candidate=false.
