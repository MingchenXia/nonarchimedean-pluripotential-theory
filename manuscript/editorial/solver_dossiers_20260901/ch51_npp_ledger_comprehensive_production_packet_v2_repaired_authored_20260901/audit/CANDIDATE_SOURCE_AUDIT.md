# Primary-source audit for the Chapter 51 ledger candidate v2

Status: **authored only; not production accepted**.  This audit records the
interfaces used to author the candidate.  It is not an independent hostile
review and not a Rethlas receipt.

## Frozen base

The sole manuscript base is the v2 narrow no-charge packet's exact postimage,
copied here as
`FROZEN_BASE_FROM_V2_POSTIMAGE_ch51_complex_prerequisites.tex`, SHA-256
`4db4d9028c80b47994143172c356c39419954471af222b8a4f9740b9b5fcf834`.
The live chapter is neither read by the splice builder nor modified.

## BEGZ

Pinned arXiv v2 PDF:
`source_pins/BEGZ10_arXiv0812.3674v2.pdf`, SHA-256
`43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd`.
Pinned `pdftotext` extraction:
`source_pins/BEGZ10_arXiv0812.3674v2.txt`, SHA-256
`890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7`.
Line numbers below refer to that extraction.

- Lines 189--227: the truncation identity, the local mass condition (1.2),
  and the warning that the positive Borel object need not be locally finite.
- Lines 243--248: Kiselman's example showing failure of local finiteness for
  a bidegree-two product.
- Lines 250--303: Proposition 1.4, including plurifine locality, independence
  of potentials, and the precise positive-cone additivity assertion.  The
  source leaves additivity to the reader; the candidate supplies the common-
  exhaustion proof and the two directions of local finiteness.
- Lines 305--323: Lemma 1.5 and its dominated-convergence mechanism.  The
  candidate only uses increasing common exhaustions and explicitly invokes
  the no-pluripolar-charge estimate, avoiding any ambiguity in the printed
  formulation.
- Lines 326--352: Proposition 1.6.  The candidate follows the source's actual
  reduction: add a Kähler multiple using multilinearity, choose Kähler
  representatives `omega_j`, use local smooth psh potentials `psi_j`, and
  compare `max(u_j,-k)` with `psi_j+max(phi_j,-k)` on the truncation locus.
- Lines 353--361: Remark 1.7 and the exact pushforward formula under a
  modification.  The candidate states that formula, rather than an ambiguous
  assertion about pullback preserving a norm of a lower-bidegree current.
- Lines 364--442: Theorem 1.8 and its Skoda--El Mir cutoff proof of closedness.
  The candidate reproduces the cutoff, energy estimate, and dominated-
  convergence argument, and never treats the indicator-restricted
  truncations as closed.
- Lines 443--478: Lemma 1.9, the chain rule used in the closedness proof.  Its
  smooth decreasing approximation and Cauchy--Schwarz justification are
  summarized in the candidate.

## Bedford--Taylor capacity

Pinned PDF: `source_pins/BT82_A_new_capacity.pdf`, SHA-256
`e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758`.
Pinned extraction: `source_pins/BT82_A_new_capacity.txt`, SHA-256
`716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b`.

- Extraction lines 462--469: Definition 3.1 of the inner capacity.
- Lines 960--981: the outer capacity and its elementary properties.
- Lines 1104--1118: Theorem 6.9, identifying pluripolar sets with sets of
  zero outer capacity on a strongly pseudoconvex domain.

The no-charge paragraph in `LEDGER_REPLACEMENT.tex` is byte-for-byte equal to
the independently prepared v2 paragraph between its heading and the following
monotonicity heading; its SHA-256 is
`6cb839bc8a05dc354ac5b035c7e6841eb707c28a9168b10a406731bfbccd9731`.

## Darvas--Di Nezza--Lu

Pinned arXiv PDF: `source_pins/DDNL18mono_arXiv1705.05796.pdf`, SHA-256
`1e614744bc4d769f377827ca81774b5f6c3d345a2619216fb6f4c81682d599cc`.
Pinned `pdftotext -layout` extraction:
`source_pins/DDNL18mono_arXiv1705.05796.txt`, SHA-256
`c46d0c5d9ef56e4788337baef00e53bd099f130cf13913cd94b1ba19e9c5004f`.
Extraction lines 62--65 fix the source's orientation of “less singular,” and
lines 74--86 state Theorem 1.1.  Taking the remaining `n-p` classes and
potentials to be `omega` and zero gives the mixed inequality used in the
candidate.  The candidate correctly translates the book's convention
`phi \preceq psi` as “psi is less singular than phi.”  This theorem remains a
declared import through `itm:ch51-import:monotone`; no new proof is claimed.

## Scope conclusion

The v1 hostile audit is frozen in this dossier.  The v2 potential comparison
now writes the two inequalities implicit in BEGZ Proposition 1.4, lines
283--301, and then uses the exact restricted current of Lemma 1.5, lines
305--321.  The modification proof expands Remark 1.7, lines 353--359: local
psh potentials construct the pullback; the analytic pair is chosen with
\(F=\mu^{-1}(Z)\); and a trace-form comparison proves that the pushforward
has no mass on \(Z\).  These additions do not strengthen the source formula;
they supply the details needed for a self-contained proof.

The source audit supports the local construction and all v2 ledger repairs.
It does not establish novelty, does not resolve a Chapter 72 atom, and does not
turn the authored candidate into a production theorem.  An independent
hostile mathematical audit and an exact production Rethlas run remain
mandatory before any live integration.
