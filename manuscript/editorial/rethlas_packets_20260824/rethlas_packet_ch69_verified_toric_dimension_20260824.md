# Exact-current Rethlas intake: Chapter 69 toric numerical dimension

**Prepared:** 2026-08-24 (Asia/Shanghai)  
**Live target:** `manuscript/parts/part6/ch69_verified_extensions.tex`,
`thm:verified-toric-dimension`  
**Status:** PRODUCTION VERIFIED; run `20260824T070302Z_d706dc98ccca`, item
`pi_bbf8518d7f87e9372b79f4ff`, returned final verdict `correct`, with zero
critical errors and zero gaps; see the exact-current receipt  
**Classification:** synchronized restatement of the Chapter 55 toric
character calculation, followed by an elementary convex-dimensional
tube estimate  
**Forbidden dependency:** arXiv:1710.09731 and every argument traceable
through it are excluded.

## Submitted exact gate

Use the exact bytes of
`ch69_verified_toric_dimension_target_statement.txt` as the Rethlas
`statement` field.  This file is byte-for-byte identical to the complete live
theorem environment.  Use the exact bytes of
`ch69_verified_toric_dimension_source_aware_composite_context_20260824.tex`
as the `proof` field.  This source-aware composite first embeds the complete
current Cao-attested Chapter 55 proof context and then embeds the complete
exact Chapter 69 section packet.  The Chapter 69 target theorem and its proof
are consequently the last mathematical proof item.  Do not normalize
whitespace, expand macros, insert line numbers, or replace either field by
this Markdown explanation.

The shorter exact files are retained for independent boundary checks:

- setup and Cao criterion: live lines 485--536;
- theorem statement: the complete environment at lines 538--544;
- adjacent proof: the complete environment at lines 546--620;
- theorem plus adjacent proof: contiguous lines 538--620;
- full exact Chapter 69 section packet: contiguous live lines 485--620;
- source-aware composite: component~1 occupies composite lines 10--264 and
  is byte-identical to the complete 255-line Chapter 55 Cao-attested context;
  component~2 occupies lines 268--403 and is byte-identical to the complete
  136-line Chapter 69 section packet.  Only packet-comment boundary markers
  occur outside the two components.

Line numbers are navigation aids.  The live-chapter and extract hashes in the
manifest control the snapshot.

## Natural framework carried by the exact setup

- `X=X_Sigma` is a smooth projective toric variety of dimension `n`.
- `D` is an integral or rational big toric divisor, `theta` is torus
  invariant, `varphi` is a torus-invariant `theta`-psh potential, and
  `T=theta+dd^c varphi`.
- `K=Delta(T)` is the compact convex Newton body in the character space.
- Clearing one rational denominator replaces `(D,T,varphi,K)` by
  `(qD,qT,qvarphi,qK)` and changes neither Cao numerical dimension nor
  convex dimension.
- For a very ample integral toric divisor `A` and positive rational
  `epsilon`, the exact setup defines `S_A(epsilon)` with its indicated
  divisible `m`-subsequence and records Cao's logarithmic criterion
  `lim log S_A(epsilon)/log epsilon = n-nu_Cao(T)`.

## Authenticated Chapter 55 dependency

The Chapter 69 proof deliberately delegates the complete local
character-by-character calculation to the proof of
`thm:ok-toric-zero-mass`.  The exact-current authenticated dependency is:

- Chapter 55 live source SHA-256:
  `b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`;
- Chapter 55 exact theorem SHA-256:
  `703e3b50120292333f6b00a3e18e887a2a67f2aa7d5dbaf5197c3f4e1a3296aa`;
- Chapter 55 adjacent proof SHA-256:
  `69df8ceb670f2f3db57f97fece992373849bff9057b2e04d9c4780a922434b03`;
- Chapter 55 theorem-plus-proof SHA-256:
  `7262697860f52b7ab28712c95333be3f96d8f3400527cb2325358885c4b2f2c6`;
- Chapter 55 full contiguous setup-and-proof packet SHA-256:
  `e4a77f88ab81bbcf403ef3b740af409e53a5454bed95ecf0321f42fd1a25bb58`;
- Chapter 55 complete Cao-attested proof-context SHA-256:
  `f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`;
- Chapter 55 valid-receipt packet-manifest SHA-256 (metadata only):
  `5b15b44725133bd0d113a8dc636e135bba15a1978c384f2980fc8ac9d6ab6d34`.

The exact Chapter 55 proof and full section packet compare byte for byte with
their stated slices of the current live source.  The first component of the
composite is the complete Cao-attested context just identified: its initial
10352-byte
prefix is byte-identical to the live Chapter 55 section packet, and its final
packet-only quote records the primary-source Proposition~4.4 attestation.

Production run `20260824T052605Z_703e3b501202` returned `final/correct`
with zero critical errors and zero gaps for exactly that target and
Cao-attested proof context.  Its controlling receipt is
`../rethlas_receipts_20260824/ch55_toric_zero_mass_cao_attested_receipt.md`,
and its authenticated proof digest is now recorded in this intake and in the
composite header as

`CH55_VALID_RECEIPT_PROOF_DIGEST = f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`.

The earlier run `20260824T045229Z_703e3b501202` is not such a receipt: its locator
diagnostic incorrectly replaced Cao's Proposition 4.4 by Proposition 4.3.
The primary article gives the required section-growth criterion as
Proposition 4.4.  That invalid diagnostic does not authenticate the
dependency; the later source-attested valid run does.

## Exact content imported from the Chapter 55 calculation

The authenticated dependency is used only for the following chain.

1. Addition of invariant convex weights gives
   `Delta(T+epsilon omega_A)=K+epsilon Q`.
2. On every maximal smooth toric chart, after the squared-norm/norm-weight
   conversion, Guenancia's criterion retains the strict interior condition
   and the fixed all-ones shift `kappa_sigma`; that condition also forces the
   local Laurent exponent to be holomorphic.
3. The Cartier signs and complete-fan gluing identity are checked exactly,
   and the shifted strict bodies are squeezed between inner and outer convex
   bodies.
4. The character-lattice Riemann sums prove an actual normalized inner limit,
   not a finite-level count identity and not merely a limsup:
   `S_A(epsilon)=vol_n(K+epsilon Q)`, with lattice normalization and no
   factor `n!`.

The Chapter 69 exact proof restates this output and does not pretend to
rederive the local chart calculation.

## Proof audit after the delegated calculation

Put `d=dim K`.  After translations and a splitting of the ambient real
character space into the direction space of `K` and a complement, relative
interior of `K` and full-dimensionality of `Q` give

`c epsilon^(n-d) <= vol_n(K+epsilon Q) <= C epsilon^(n-d)`

for sufficiently small positive `epsilon`.  Hence
`log vol_n(K+epsilon Q)=(n-d)log epsilon+O(1)`.  Combining the authenticated
section-count equality with Cao's exact criterion yields
`n-nu_Cao(T)=n-d`, and therefore `nu_Cao(T)=dim K`.

## Scope firewall

- The result covers integral and rational classes only; it makes no
  irrational real-class approximation claim.
- `K` is the direct toric Newton body, not an unsupported continuation of a
  positive-volume partial Okounkov body to volume zero.
- The finite-level character condition is not simplified to an unshifted
  lattice-point identity.
- The equality with volume is asserted after the normalized divisible
  `m`-limit; no factor `n!` is introduced.
- This gate verifies that the Chapter 69 synchronized restatement follows
  from the authenticated Chapter 55 calculation and Cao's recorded
  criterion.  It is not a second unauthenticated proof of the delegated
  local calculation.

## Answered production-verification question

Given that the valid Chapter 55 receipt authenticates exactly the first
source component recorded above, does the source-aware composite make the
Chapter 69 target theorem its final proof item and correctly transport the
character-count identity into Cao's criterion to prove
`nu_Cao(T)=dim K`, without changing normalization or scope?

Production Rethlas answered this question `correct` for target SHA-256
`d706dc98...9700` and composite proof SHA-256 `8aefa509...5d618`.
All component and live-slice comparisons passed both before and after the
gate, and the frozen Chapter 69 source was not edited.
