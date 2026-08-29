# P21.3 rigid-exception extension: staging audit

Date: 29 August 2026

Status: **quarantined candidate**.  This packet is neither a live-book input
nor a production-Rethlas-verified result.  It does not retire or narrow
P21.3 in the authoritative open-problem inventory.

## Candidate result

For a nonempty connected good separated strict normal boundaryless analytic
curve over a complete nontrivially valued field, with a locally finite rigid
set `E` and rig-smooth complement `Y`, the candidate proves:

1. `Y` is connected by injective arcs;
2. every positive `d'`- and `d''`-closed CLD `(0,0)` current on `X` is a
   unique `c delta_X`, `c>=0`;
3. every such current has Bedford--Taylor independence for continuous psh
   pairs with equal curvature currents.

The proof imports only the exact production-verified rig-smooth
classification.  It uses Ducros's graph/unibranch/pluribranch results for
connectedness and CLD Proposition 3.3.6 together with Proposition 15.2.1(a)
for removability across the rigid set.  It does not import a rejected packet,
pull back an arbitrary current, multiply a current by a cutoff, or replace
test-form removability by an atom argument.

## Current exact bytes

- statement:
  `cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5`;
- proof:
  `cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce`;
- production-verification problem:
  `82d156726b66f835389b43b170aa6c2cc3179e22c18a239b77afa60cc83c4063`;
- source audit:
  `568fdd57d9ee11714f50ef25c6b53bc9e60ce7821df57fe60b572950eea6ba67`;
- compile harness:
  `7232343868d790c0794d7ce84d9346d3c84b3cf1c393ef97498cf93ff5df4d8a`;
- compiled PDF:
  `c4abb2ddf5d645c46b6b3c04c5a71c69b1cb7db709fc04d0c1465f4c77b3e5b6`;
- final compile log:
  `c84ac512c33b95ded72099f2865e67266ad677fb4ee7efc227351d02ba9e3689`.

The imported live rig-smooth statement and proof hashes are respectively
`c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`
and
`01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`.

## Compile gate

The standalone harness compiled with `latexmk` and `pdfTeX` in two passes.
The resulting diagnostic PDF has two A4 pages, 158252 bytes, blank
author/title metadata, and the PDF hash recorded above.  Its final log has the
hash recorded above and contains no TeX error, undefined reference or
citation, multiply defined label, rerun request, warning, overfull box, or
underfull box.  Text extraction confirms that the statement, equations,
proof, and references are present in dependency order.  Both rendered pages
were inspected at 150 dpi; no clipping, overlap, broken glyph, orphaned
bibliography item, or layout defect remains.

## Audit status

- Primary-source audit: complete for every citation used in the candidate;
  exact local source files and hashes are recorded in the source audit.
- Independent whole-proof, topology, and current-theoretic hostile audits:
  **passed on the exact statement and proof hashes above**.  No counterexample
  was found within the printed scope, including over imperfect fields, at
  finite inseparable rigid points, or for an infinite locally finite set
  `E`.  The audits separately checked normality at rigid points,
  connectedness after removing them, compact support after restriction, the
  distinction between `(1,1)` test-form vanishing and `(0,0)` point masses,
  local differential separation, current multiplication, and all bidegrees
  and signs in the Bedford--Taylor calculation.
- A hostile audit correctly rejected the former citation of CLD Section
  7.3.4 for arbitrary continuous coefficients.  The frozen proof now uses
  CLD Corollary 7.2.10, Example 7.2.12, Section 7.3.1, and the explicit test
  pairing.  Both the current-specialist re-audit and the final whole-packet
  re-audit passed these repaired exact bytes.
- Exact production Rethlas (`gpt-5.6-sol`, `xhigh`): **pending**.
- Live integration, whole-chapter compile, provenance update, and inventory
  change: **forbidden until the production gate passes**.

## Scope firewall

The packet does not assert a result over a trivially valued field, at a
nonrigid exceptional point, on a nonnormal or boundary-bearing curve, for an
exceptional set not known to be locally finite, when the complement is not
rig-smooth, for discontinuous psh functions, or in higher dimension.
