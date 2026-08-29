# P07.1 infinite-endpoint staging audit — 29 August 2026

## Status

This is an isolated, non-live, non-Rethlas-verified candidate.  It does not
alter the monograph, the atomic inventory, or the status of P07.1.

## Exact mathematical scope

The candidate treats only the CLD extended-real interval
[-infinity,R_0) whose smooth functions are ordinary smooth on the finite
stratum and exactly constant on a terminal tail.  It characterizes the
generated psh sheaf as finite-stratum extended-real convex functions whose
value at -infinity equals their finite-side limit in
R union {-infinity}, and proves collapse at ordinal stage one on one fixed
endpoint neighbourhood.

The proof handles the two distinct -infinity cases:

- identically -infinity on the finite stratum, approximated by constants;
- finite at every finite point but with endpoint trace -infinity, such as
  u(t)=t, handled by a monotone heat-and-clamp construction.

It does not treat CLD stars, general G-tropical spaces, or arbitrary
Berkovich spaces.

## Source and hostile audit

The exact source firewall and ten hostile checks are recorded in
p071_infinite_endpoint_source_and_hostile_audit_20260829.md.  The key
checks are necessity and decreasing-limit stability of the trace equality,
Gaussian integrability from a global slope bound, literal rather than
asymptotic collar constancy, and exact monotonicity of the approximants.

An independent exact-byte hostile audit then found one mandatory early-index
quantifier repair and three minor repairs.  The proof now uses \(u(-n)\) only
for sufficiently large \(n\), intersects each collar with its actual domain,
proves the finite-trace continuity assertion, gives the endpoint term in the
uniform estimate explicitly, and cites the exact CLD source locations.  A
second exact-byte audit of the repaired files closed every finding and
reported no remaining counterexample, mathematical gap, or source-scope
problem.

## Compile audit

The isolated article compiled successfully with pdfLaTeX through latexmk.
The final log has no warnings, undefined references, overfull boxes,
underfull boxes, or fatal errors.  The PDF has 5 A4 pages, an empty author
field, and size 257062 bytes.  All five pages of the repaired PDF were
rendered and inspected; no clipping, overlap, broken glyph, or other layout
defect was found.

## Frozen candidate hashes

- statement:
  779b1304255d6e803cf34d9e429acb085eb5cf827e54c6a30a15ba3058182d9a
- proof:
  dacaa96b68c5ddb260736d40075d229ffbe843dbe4994436c1a18428aa407f5b
- problem note:
  9547c554d3843cd638f501490db057c78a336fdb77cce7744343d69042f2d8ca
- source and hostile audit:
  519afeee511a8782f58c6490483cddf1d24ede0c063e3ddc3377cb9658edc4ff
- compile source:
  9ad37746fb6c5d8375959e6437f8956f68810b932e3e04febc6d971d2173450f
- compile PDF:
  6fe6a4b4c48f532cb5bf74a220e496f872cdb23dbc810d378551fe755539883b

## Required gate

Before any live integration, the exact statement and proof bytes must receive
an independent source-aware audit and a production gpt-5.6-sol/xhigh Rethlas
verdict of correct with zero critical errors and zero gaps.  A later edit
invalidates the frozen hashes and requires a fresh gate.
