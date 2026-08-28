# P07.1 constant-collar endpoint: staging audit

Date: 29 August 2026.

Status: audited staging material only.  The statement and proof in this
directory are not inputs of the live book and have not received a production
Rethlas verdict.  P07.1 therefore remains in the open-problem inventory.

## Result under audit

The packet treats one exact residual model from Chambert--Loir--Ducros,
Example 6.7.2: a **finite** endpoint with the nonambient smooth structure in
which every smooth profile is exactly constant on some endpoint collar.  It
identifies the generated psh sheaf with the extended-real convex functions
whose endpoint value is a minimum, proves that the transfinite hierarchy
collapses at its first decreasing-limit stage, and constructs the
approximants on one fixed neighbourhood.

This does not cover the infinite endpoint in the trivially valued open-disc
realization, the infinite-star model, or higher-dimensional tropical spaces.
In particular, the proof never treats the ordinary inward coordinate as a
nonconstant affine coordinate through the endpoint.

## Source and hostile audits

The source audit checked the current 2025 revision of
Chambert--Loir--Ducros against Sections 6.1.1 and 6.1.6, Definition 6.2.1,
Example 6.7.2, Definition 8.1.1, and Lemmas 8.1.4 and 8.1.10.  The exact local
source copies used are recorded in the separate source-audit file.

Two independent hostile mathematical readings were then performed.  The
first found no counterexample in the finite-endpoint scope and required the
following source-boundary repairs, all now incorporated:

1. state the source interval as a subset of the extended real line and
   distinguish finite from infinite boundary points;
2. use the ordinary inward coordinate on the finite stratum, extended only
   topologically to the endpoint;
3. exclude explicitly the infinite endpoint and the open-unit-disc model.

The second reading found no blocker and required four proof-level repairs,
all now incorporated:

1. make the finite/infinite endpoint firewall exact;
2. derive collar constancy of chart coordinates from Sections 6.1.1 and
   6.1.6;
3. supply a Lebesgue-number argument for local-to-global convexity;
4. construct the interior convex extension explicitly from endpoint
   subgradients.

A final independent re-audit of the repaired bytes closed all seven findings
and reported no remaining mathematical or source-scope issue.

## Compilation and visual audit

The isolated wrapper compiles to a six-page A4 PDF.  The PDF metadata has an
empty author field.  The final log contains no LaTeX warnings, undefined
references, overfull boxes, underfull boxes, fatal errors, or emergency
stops.  Every rendered page was inspected; no clipping, overlap, broken
glyph, or other layout defect was found.

## Frozen payload

SHA-256 values of the audited current bytes are:

- statement:
  `69f04be69f70be0abfdb720fa6aceaad799240421046d14333cfd542e2e56498`;
- proof:
  `5e7d96e8badf030b64d063b26fb353aa4be097438ae267cdd72911907c2a5c7c`;
- problem specification:
  `a54976c906a568db2a93dc63b172275dd622b71d53dae370f6d6191f384a0073`;
- source audit:
  `2153e8b93bec9ac833322ccd43000a6d7c71bfcf22eb7d95adc6cc73c3d4e178`;
- compile wrapper:
  `2db131b7bebcf44667ad2e2e381fea4c9c616b78c016452c11e2c312877247fe`;
- compiled PDF:
  `42fad12e1b956656247520d32f4d0a0981e978030de8d044fe8fa16b5604c783`.

Any change to the statement or proof invalidates this audit and requires a
new exact-byte review.

## Production gate

Live integration, any claim that the result is established, and removal or
narrowing of P07.1 are forbidden until these exact statement and proof bytes
receive a production gpt-5.6-sol/xhigh Rethlas verdict of `correct`, with zero
critical errors and zero gaps.  The present staging audit is not a substitute
for that gate.
