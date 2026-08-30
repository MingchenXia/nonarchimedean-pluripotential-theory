# Fail-closed production verdict

Date: 30 August 2026

The dependency-closed v2 request returned `verdict: wrong`, with one
critical error and one gap.  Nothing in the v2 packet is authorized for
live-book integration.

## Frozen v2 identity

- statement:
  `147612fc96ddb973f5dd2df7ccc3da38798e3f3df46b462cd38b6cfaa9f1167b`;
- proof:
  `e146c0eec6372995f881a3db054719969575515a913474a14d073ec17010627d`.

## Production archive

- request:
  `f621e7c836079a2c79764cc10e67373b2815756d8cf054362752d2d61c6c4740`;
- response:
  `9343e51748df7764fddf021ce2cee6ead02983b2931c95951bae7ad546a9c58c`;
- headers:
  `79ecfd63e00edf6121af113306693bf7e84ded0079f0a12cf4a3e901a8b0c0e1`.

## Controlling objections

The production verifier accepted the strict-open rational-centred trace,
finite-flat trace, arbitrary-field disc, fibre-slicing, annulus, and joint
polycylinder arguments.  It rejected only the closed and half-closed
endpoint variants.

The critical error is the false assertion that the absolute analytic
interior of a strict closed or half-closed polycylinder is the
coordinatewise strict open polycylinder.  Endpoint residue-disc branches
also lie in the absolute interior, so the strict open locus is not dense in
the whole domain.

The gap is the analogous omission for closed or half-closed annuli: the
proof does not identify the function on the endpoint residue branches with
the affine skeleton value.  Such a result would require a separate disc
argument on each endpoint branch and a gluing argument through the endpoint
Gauss point.

## Disposition

V2 remains permanently quarantined.  A new v3 packet deletes every endpoint
claim and retains only the strict-open conclusions that the verifier
expressly accepted.  Any future endpoint theorem must be separately stated,
audited, and verified; it may not inherit a positive verdict from the
strict-open proof.
