# P14.3 repaired candidate — local source-alignment audit

## Verdict

**PASS for exact local citation alignment; not an independent mathematical verdict.**

This audit checks that the review packet names the corrected claim and that
the cited statements required by its proof are present in the durable local
source copies. It does not validate every deduction, does not replace a
source-closed proof-verifier run, and does not retire P14.3.

## Exact inputs

| Input | SHA-256 |
| --- | --- |
| VERIFICATION_STATEMENT.md | 41d8df251140fe37b4ead8b73b5e02deb22dd3103949f8759db6f78c51eca988 |
| VERIFICATION_PROOF.md | d7d6f91eb7e4d5c8a4928ae8f479603c0dc538189a006a0c6cab0fd93418ba9d |
| frozen P14.3 statement | 4ab292c9cfcc6c298968fca40819c09d560c12c96279947ddae46f4c22c5191f |
| repaired disposable proof postimage | 04f10c6dc7ae7f60ac6e71f8834f8712e7761d24d0e6a3614134f101c0b08614 |
| MP24 source text | 0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62 |
| DXZ23 source text | 7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244 |

The statement is a faithful review rendering of the frozen P14.3 claim.
The proof is a review rendering of the repaired postimage, including the
positive-coefficient convention and explicit directed-net clause.

## Source checks

The following locally preserved sources support the cited interface:

- MP24 describes X^beth as a compact Hausdorff tropical spectrum
  (introduction; §1.2), so the closed-image argument in Step 1 has its
  stated topological premise.
- MP24, Lemma 2.1.1 gives the maximal positive central ideal used to
  conclude that a coherent ideal which is the unit near the central
  variety has value zero.
- MP24, Remark 2.3.2, Proposition 2.3.4, and Remark 2.3.5 respectively
  give birational invariance of divisorial valuations, point-independence
  of monomial valuations on a connected stratum, and divisoriality for
  rational monomial weights.
- MP24, Theorem 2.3.6 is exactly the ordinary density statement
  X^div dense in X^beth, used in Step 1.
- MP24, Theorem 4.3.8 states that an MP potential below a usc function on
  X^div is below it on all of X^beth, which supplies the reverse
  inequality in the comparison corollary.
- MP24, Theorems 5.1.4 and 5.1.7 plus §5.2 supply the MP-side extension
  and finite-energy correspondence interface used conditionally in the
  final corollary.
- DXZ23, Theorem 3.17 states the bijection between I-maximal
  finite-energy rays and finite-energy non-Archimedean metrics.

The raw-transform upper semicontinuity is deliberately treated only as the
stated P14.2 hypothesis. This audit does not assert its production status.

## Local check

On 8 September 2026, an exact-marker check confirmed the theorem claim,
the repaired extended-value convention, MP24 Theorems 2.3.6 and 4.3.8,
and DXZ23 Theorem 3.17 in the files identified above. It returned:

    local source-alignment marker check: PASS

## Production boundary

The local verifier service was started successfully, but no proof was
submitted: the submission gate required explicit approval to send the
packet to a model-backed reviewer. VERIFICATION_RUN/ therefore does not
exist, and there is no verifier verdict. The review packet is retained so
that one authorized, reproducible submission can be made later without
changing the candidate.

This audit is evidence for documentation and source alignment only. P14.3
remains open; the Chapter 72 count and status are unchanged.
