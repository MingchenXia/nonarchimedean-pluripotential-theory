# P00.1 full MP--BJ cone comparison: production and exact-live receipt

**Date:** 28 August 2026
**Model:** `gpt-5.6-sol`
**Reasoning effort:** `xhigh`
**Live theorem:** `thm:pseff-projective-full-mp-bj` in Chapter 71
**Disposition:** `correct`; zero critical errors; zero gaps

## Exact scope

Let `X` be a connected smooth projective complex variety and let `alpha` be
an ample real Néron--Severi class.  Under the canonical GAGA homeomorphism,
the Mesquita--Piccione and Boucksom--Jonsson rational PL relative-nef model
cones agree, and their full decreasing completions agree on all
semivaluations.  If `alpha=c1(L)` for an ample rational line bundle, the full
Darvas--Xia--Zhang cone is consequently order-isomorphic to the MP cone, with
no finite-energy hypothesis.

The receipt does not cover a nonprojective compact Kähler manifold, a
transcendental class outside the real Néron--Severi space, a non-nef class,
or compatibility of Monge--Ampère operators, mixed products, or energy.

## Verification chain

1. Two independent exact-byte mathematical/source audits passed the frozen
   candidate.  They checked the GAGA/flag-ideal algebraization, the
   nonalgebraizable analytic-model firewall, common refinements, analytic
   versus algebraic relative nefness, generic finiteness, decreasing nets,
   and the precise MP/BJ/DXZ citations.
2. The frozen candidate passed the direct production endpoint:
   `p001_mp_bj_full_cone_run_20260828`, with verdict `correct`, zero critical
   errors, and zero gaps.
3. The first integrated live adaptation passed
   `p001_mp_bj_full_cone_live_run_20260828`, again `correct` with zero/zero.
   Its statement was then superseded only by replacing three numbered
   `equation` environments with mathematically identical display wrappers to
   eliminate duplicate PDF anchors.
4. The final live theorem and proof were resubmitted byte for byte in
   `p001_mp_bj_full_cone_live_run2_20260828`.  The response again returned
   `correct`, zero critical errors, and zero gaps, and explicitly confirmed
   every cited numbered statement against the primary sources.

## Hash closure

Frozen candidate:

- statement:
  `e40829e3586bcabeeb866229dc068c2e518a736fc908dec32f3bf3957c59c9ab`;
- proof:
  `baad23068e9dcae47619f3e2d81cfd26fa5bd51b1e4c4d4baa1a7c024824e671`.

Final exact-live bytes:

- statement:
  `949819c48c8d0e991acbb92ed7c15d504dd691056f06553c58ac1d4ab564d33e`;
- proof:
  `58c2954ad1e541ab41e0649c4e84e22252299265b422159df41fe5772f2e8064`.

Final exact-live archive:

- request:
  `0117a2a2669e2980b620e9fedc53d9ca6fb59c9b8d312f9fa46935dad82bcea6`;
- response:
  `aa83284548a249c6e1538a7d0c352e6181936e4d79455b5a8f980400aec8b960`;
- safe headers:
  `1bf4eb42373b4422429660ca6be4c02fd27681fdd3ea3e76a52dd1edbe05c862`.

The statement and proof extracted from the current Chapter 71 source have
the final exact-live hashes above.  The request materialization has the same
two hashes.

## Integration consequence

The full proof is integrated in Chapter 71 and synchronized through Chapters
57, 58, 60, 63, 64, 65, 72, Appendix L, and the mutable editorial ledgers.
The former P00.1 problem environment is removed.  The current literal
frontier consists of 15 formal problem environments, all in Chapter 72, and
54 active atoms with tier counts `(0,6,14,17,17)`.

This theorem is presented as a book-level, source-explicit synthesis of
published Mesquita--Piccione, Boucksom--Jonsson, and Darvas--Xia--Zhang
inputs.  No novelty, publication, or priority claim is made.
