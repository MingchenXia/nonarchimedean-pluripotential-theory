# Independent addendum: six unit-weight follow-up replacements

Date: 31 August 2026. Auditor: p213_skeletal_hostile.
This is a bounded independent exact-byte review, not a production verdict.

## Verdict

No mathematical gap was found in the SIX changes recorded by the frozen
follow-up replacements.json, or in their incorporation of the previously
audited Ch20 weighted-intersection parent. The numerical examples now state
the missing residue-degree-one hypothesis. The general Ch20 proposition
continues to allow arbitrary node residue degrees and real divisor
coefficients; its initial algebraic identity continues to allow nonreduced
regular models. No general theorem has been restricted to rational nodes.

This addendum closes the separate Ch20 numerical-example and Ch24 weighted
sign/example findings in the earlier bounded audit, and checks the newly
identified Ch22 consumer as well. It does NOT certify all of Ch20, Ch22, or
Ch24, nor resolve the previously recorded Ch25 issues. The unchanged general
nonreduced edge-length remark is still not independently reproved here.
No live source or frozen input was changed. No production call, patch
application, PDF generation, or full-book compilation occurred.

## Frozen inputs and exact scope

Repository: /private/tmp/nappt_p071_20260827.
Author follow-up directory:
manuscript/editorial/solver_dossiers_20260831/p081_ch20_ch22_ch24_unit_weight_followup_20260831/.

Principal exact bytes:

- patched/ch20_model_forms.tex, 172302 bytes, SHA256
  bc479b67a29261f001d0409656e150bc3bf9441dbdf1ff90fb4298fe3c1ad414.
- patched/ch22_compactness.tex, 162016 bytes, SHA256
  0acc3463796d93d0fd56c5f8f2fbc2d1de75f9c8c46607a5fddc0d91844bcc0a.
- patched/ch24_bfj_ma.tex, 171406 bytes, SHA256
  391930d26a49779b10a96ac7e381fefade0677642669e7a20e93c7902e660eae.
- combined.patch, 10885 bytes, SHA256
  f0974928b5068c240f9a013842825734614b6f159843b8a9907044e29ae3a2a1.
- replacements.json, 1794 bytes, SHA256
  4284490d6a19dde9389cfed3a57ef415550606ef58d1c2a4e580bb947acf2dd9.
- Author MANIFEST.json, 3932 bytes, SHA256
  489eff65ec42617d697ef5c7e1500f4765ddecef3e14482b8b0d482335fd0a56.

The Ch20 parent copied into this proposal is the exact 172270-byte file
with SHA256
42f0c9dd4e957d7038c8bfb3d7c9742c5e5d023d732a219748c6906f447e1b7d.
Its previous independent audit is
p081_ch20_weighted_intersection_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md,
SHA256
6c7690f178189f60598bed57f99132e87d337a7f4085eb0d2dc6bba2b6ab0374.
That report was reread completely. The present addendum supplements, rather
than overwrites or silently broadens, its acceptance boundary.

All 12 entries of the follow-up author manifest and all six entries of the
parent author manifest were independently rehashed and size-checked:
zero mismatches. VALIDATION.json records the exact checks and all 12
follow-up entry hashes; this addendum's MANIFEST.json also identifies
the parent and prior-audit inputs.

## Mathematical check of the six changes

Line references below are to the frozen proposed chapter copies. For a
regular reduced two-component special fiber E0+E1 with a single transverse
closed node z, put c=[kappa(z):k]. Intersection multiplicity at the node is
one over kappa(z), hence its degree over k is c. The principal-fiber
relations give

    (E0.E1)=c,  (E0.E0)=(E1.E1)=-c.

Consequently the matrix is c[-1,1;1,-1]. For vertex values a0,a1, the
divisor D=a0 E0+a1 E1 has

    D^2=-c(a0-a1)^2,
    ddc(phi_D)=c(a1-a0) delta_0+c(a0-a1) delta_1.

This direct computation checks both the missing factor and the sign. The
single-node condition alone does not set c=1; rationality of z over k does.

1. Ch20 line 3076, ex:ch20-semistable-curve: the single node is now explicitly
   rational over the residue field. Therefore the unchanged matrix in
   eq:ch20-two-component-matrix and its following square are correct with
   c=1. The earlier general componentwise nef test is unchanged.

2. Ch22 line 1838, ex:ch22-two-vertex: the transverse point is explicitly
   residue-field-rational. Reducedness gives b0=b1=1; rationality gives
   (E0.E1)=1, which is a logically separate conclusion. The principal-fiber
   relation then gives both self-intersections -1. The inequalities
   -d0 <= u1-u0 <= d1 and the displayed unit incidence weights follow.
   The subsequent ex:ch22-modulus-segment explicitly keeps this model, so
   it inherits the unit-node hypothesis. This does not impose that
   hypothesis on the preceding general compactness estimates.

3. Ch24 line 902, rem:ch24-sign-audit: the outgoing-slope sum is now explicitly
   residue-degree-weighted. Positive edge weights preserve the convex-corner
   sign. This is the curve interpretation of the cited Ch20 proposition;
   the edit is not a new higher-dimensional slope theorem.

4. Ch24 line 908, the same remark: its displayed square is now explicitly
   the residue-rational-node two-component case. Thus
   integral f ddc f=-(u0-u1)^2 is correct for a function determined on this
   two-component model. For a degree-c node the right-hand side would instead
   have the factor c; no such general formula is asserted by this numerical
   sentence.

5. Ch24 line 2828, ex:two-vertex-ma: the unique node is explicitly rational
   over the residue field. With the stated unit length the two signed masses
   are a1-a0 and a0-a1, and adding reference masses gives the displayed
   Monge--Ampere coefficients. Their nonnegativity is exactly the degree
   test for nefness; their sum is m0+m1. For m0=m1=1 this gives precisely
   |a0-a1|<=1.

6. Ch24 lines 2861--2862, ex:ch24-curve-mixed: both length and residue weight
   are explicitly one, consistently with the preceding example that it
   retains. The mixed intersection equals
   -(a0-a1)(c0-c1); the symmetry, energy pairing, and numerical instance
   displayed in the complete example therefore keep their existing values.
   The later ex:ch24-uniqueness-curve explicitly keeps the model of
   ex:two-vertex-ma, so it also inherits the rational-node specialization.

The full examples and immediate inheritance sentences were read, not just
the six old/new strings. No change to a label's numerical meaning was
found, except that the previously implicit and mathematically necessary
unit-node hypothesis is now explicit.

## Parent incorporation and assembly checks

The complete combined.patch, replacements.json, GATE.md, MANIFEST.json,
and assemble.mjs were read. The author assembly script was NOT executed:
it writes the author packet. A separate read-only in-memory reconstruction
established:

- Ch20 equals the exact previously audited parent chapter plus only
  replacement 1.
- Ch22 equals its frozen live base plus only replacement 2.
- Ch24 equals its frozen live base plus only replacements 3--6.
- Every old replacement string occurs exactly once in its prescribed
  starting text.
- The concatenation of independently generated unified diffs is byte-for-byte
  the frozen combined.patch. There are no extra changes.
- git apply --check passes against the recorded live bases; it was not applied.
- All 572 prior labels are retained: Ch20 208 to 209, Ch22 185 to 185,
  Ch24 179 to 179. The only added label is
  eq:ch20-node-intersection-residue-degree from the parent. There are
  no missing or duplicate chapter labels.
- The three live-source hashes remained identical after these checks.

The combined patch already includes the parent Ch20 correction. It must
not be applied cumulatively with that parent patch. The proposed Ch20 file
is the complete replacement copy for this assembly baseline.

The general parent proposition at proposed Ch20 lines 1073--1155 retains
its real-linear algebraic identity, symmetric multiplicity factors, and
residue-weighted reduced-semistable graph identity. Its statement has not
acquired the numerical rational-node restriction. The adjacent remark's
new curvature-mass reminder b_i(D.E_i) is still correct. The unchanged
general metric-length assertion there remains outside this audit's
reproving scope, just as in the prior report.

## Remaining boundaries

The previous Ch25 findings concerning omitted residue weights, a false
original-field reduced-semistable determining-model step, and unit-weight
segment normalization are not changed by this packet. The live Ch25
hash remains
47c5c5897173168f9d5e21cbb7bdd86338ccf4e72b466f84acea917ea2b25fad.
Any separate Ch25 repair requires its own exact-byte review.

Likewise this bounded check is not a general acceptance of the untouched
Ch22/Ch24 arguments. In particular the existing Ch24 model-uniqueness
proof is checked in its stated reduced-semistable scope, not silently
extended to nonreduced models by omitting the necessary b_E factor.

No new envelope existence, continuous-obstacle continuity, arbitrary-field
semipositivity promotion, or open-problem retirement is established by these
six normalization repairs. Independent review of this exact bounded
follow-up is complete; production and coordinated manuscript validation
remain separate gates.

