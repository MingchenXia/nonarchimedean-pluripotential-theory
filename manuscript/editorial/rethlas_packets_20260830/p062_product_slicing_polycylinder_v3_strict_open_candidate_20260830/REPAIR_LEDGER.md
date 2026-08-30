# P06.2 v3 strict-open repair ledger

## Provenance and fail-closed status

This packet is a new byte sequence.  It does not overwrite either failed
packet.  Its source files were obtained from the exact v2 statement and proof
and then narrowed by deletion only, apart from quarantine comments and the
explicit scope firewall.

- v2 statement SHA-256:
  `147612fc96ddb973f5dd2df7ccc3da38798e3f3df46b462cd38b6cfaa9f1167b`
- v2 proof SHA-256:
  `e146c0eec6372995f881a3db054719969575515a913474a14d073ec17010627d`
- production response SHA-256:
  `9343e51748df7764fddf021ce2cee6ead02983b2931c95951bae7ad546a9c58c`
- production verdict: `wrong`

The response expressly reports that the strict-open core passed:

> The strict open-domain arguments, including rational-centred traces,
> algebraically closed base change, finite-flat continuous trace,
> arbitrary-field disc constancy, exact fibre slicing, strict-open annulus
> affinity, and strict-open polycylinder joint affinity, pass sequential and
> reference checks.

## Exact rejected material

The critical-error location is quoted verbatim as
`Proof of Theorem thm:p062-arbitrary-field-polycylinder-candidate, final endpoint paragraph`.
The production response gives the following critical error verbatim:

> The assertion that the absolute analytic interior of a closed or half-closed
> standard polycylinder 'is the corresponding open polycylinder' is false.
> Already for a strict closed Berkovich disc, the absolute interior is the
> closed disc minus its Gauss boundary point, and it contains open residue
> branches centered at points of boundary modulus; it is strictly larger than
> {|T|<R}. Consequently the coordinatewise strict open polycylinder is not
> dense in the whole closed/half-closed domain, and applying only the open
> theorem there plus continuity does not prove the endpoint assertion.

The gap location is quoted verbatim as
`Proof of Proposition prop:p062-arbitrary-field-annulus-candidate, final endpoint sentence`.
It gives the following gap verbatim:

> The open-annulus proof does not by itself prove the closed and half-closed
> variants. The absolute analytic interior of a strict closed annulus is not
> the coordinatewise strict annulus r<|T|<R: it also contains the residue-disc
> branches at the endpoint radii (only the analytic boundary Gauss points are
> omitted). The strict annulus is not dense in those endpoint branches, so the
> sentence 'Restriction to the absolute interior and continuity' skips the
> argument identifying h on those branches with the limiting affine skeleton
> value. One must apply the disc theorem on every endpoint branch or rerun the
> polynomial-trace comparison for rigid endpoint points, then glue through the
> endpoint Gauss point by continuity and invoke rigid density.

## Repair implemented

The repair is deliberately narrower than the suggested endpoint repair.

1. The annulus proposition no longer contains the sentence claiming closed or
   half-closed variants.
2. The annulus proof no longer contains the sentence purporting to obtain
   those variants by restriction to the absolute interior and continuity.
3. The polycylinder theorem no longer contains its closed/half-closed variant.
4. The polycylinder proof no longer identifies the absolute analytic interior
   with the strict-open polycylinder and no longer invokes density to extend to
   endpoints.
5. The statement file ends with an explicit firewall: only strict open
   domains are asserted, and no endpoint conclusion is claimed.

No endpoint-residue-branch theorem is smuggled into v3.  The retained
mathematical content is exactly: strict-open product fibre slicing,
arbitrary-field strict-open annulus affinity, and the arbitrary-field
strict-open polycylinder formula (together with its stated regularity
consequences).

## Quarantine

This is an author-prepared repair candidate, not a verified theorem packet.
It remains unavailable for live-book integration until a fresh independent
exact-byte audit and a fresh production Rethlas verification both pass.
