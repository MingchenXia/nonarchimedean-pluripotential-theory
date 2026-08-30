# P06.2 strict-polydisc zero current: production receipt

**Date:** 30 August 2026  
**Production run:** `20260830T001728Z_017f3da108ae`  
**Model:** `gpt-5.6-sol`  
**Reasoning effort:** `xhigh`  
**Verdict:** `correct`  
**Critical errors:** 0  
**Gaps:** 0  
**Endpoint status:** HTTP 200  
**Endpoint item identifier:** none assigned

The frozen theorem proves that a continuous function with vanishing
Chambert--Loir--Ducros current on a strict open polydisc over an algebraically
closed complete nontrivially valued field is constant.  The same conclusion
holds for a strict closed polydisc when the current vanishes on its analytic
interior.  The proof restricts the current to translated punctured-polydisc
torus charts, identifies the signed top-form measure with the pushforward
from the multiplicity-one Gauss section, obtains zero distributional Hessian
for every radial trace, kills all affine slopes by coordinate-radius
collapse, and separates rigid points by translation-invariant Gauss norms.

An independent audit passed on the exact frozen bytes before production
submission.  It checked current restriction and extension by zero, the sign
in the double-current differential, support of sign-changing top forms on
the torus skeleton, signed Radon pushforward, passage from smooth to
continuous multipliers, properness of tropicalization, coordinate-stratum
limits, translation equality, rigid-point density, non-Abhyankar points, and
the closed-polydisc analytic-interior argument.  The editorial text notes
that Berkovich Proposition 1.5.5(i) is used together with part (ii), the
composition formula expressly invoked in the frozen proof.

## Frozen hashes

- statement:
  `017f3da108ae737e4bbc1d490d6988faf76ce643b4cb52104aae53c4dcda75d6`
- proof:
  `3763bf9a7e4b1f47602544ad2c3248d9b8abd7b9d34109e3c14259e422393bbd`
- independent exact-byte hostile audit:
  `2419e2c7abb2c07b5ee1ffc4feae40fc6e54c0a784a716f4db71abc73b03ba8c`
- archived request:
  `7ac08a78130251f6153f21e5fe4e191e2fe8c93562e235b8ed4e8f69dd86bd8e`
- archived response:
  `416af3bce60e90de51898e9f95b5addbfd1d99f47a396df65bb03a6af14304b5`
- archived safe headers:
  `a15e345955c74239824ad2585ec60d0364a07279c4ea9de902ce208ef7b06843`
- service verification:
  `c579d471bc58fc5cbbf9dfbb2fd90298708b19d3f6962750316c4c9f19c6c93f`
- final service log:
  `4bdfb338942617653749877cd7df91df37094aa26304aad3ecd230610221c5cf`

The exact statement and proof extracted from the archived request have the
same hashes as the frozen files.  The controlling service log begins with
the command-line provenance
`-m gpt-5.6-sol --config model_reasoning_effort=xhigh`.  The endpoint response
and service verification both report `correct`, no critical error, and no
gap.

## Integration scope

Chapter 18 inputs the exact frozen statement and proof, suppressing only the
redundant outer proof heading in the surrounding local theorem style.
Chapter 72 records the strict-polydisc range and its limitations.  The
result is factorization-free but assumes an algebraically closed ground field
and a strict-polydisc domain.  It neither proves arbitrary-field descent nor
uniformizes arbitrary analytic germs.  P06.2 remains active, and the
inventory remains 53 atoms in 14 formal problem environments.
