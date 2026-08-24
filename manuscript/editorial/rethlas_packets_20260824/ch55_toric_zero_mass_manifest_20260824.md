# Manifest: Chapter 55 toric zero-volume numerical dimension

**Snapshot date:** 2026-08-24 (Asia/Shanghai)  
**Submission status:** valid production Rethlas receipt archived  
**Live source:** `manuscript/parts/part5/ch55_okounkov_dh.tex`  
**Target label:** `thm:ok-toric-zero-mass`  
**Classification:** book-level synthesis of the toric multiplier-ideal
criterion, toric character counting, and Cao's numerical criterion  
**Forbidden dependency:** arXiv:1710.09731 and every argument traceable
through it are excluded.

SHA-256 values identify exact bytes.  Line numbers are navigation aids for
this snapshot; the live-chapter and extract hashes are controlling.

| File | Role | Live lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `manuscript/parts/part5/ch55_okounkov_dh.tex` | complete post-repair live chapter after primary-source locator restoration and Schneider locator audit | 1--end | 64938 | `b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab` |
| `ch55_toric_zero_mass_target_statement.txt` | exact Rethlas `statement` field: complete live theorem environment | 1304--1319 | 558 | `703e3b50120292333f6b00a3e18e887a2a67f2aa7d5dbaf5197c3f4e1a3296aa` |
| `ch55_toric_zero_mass_statement_exact.tex` | duplicate exact TeX extract for independent statement-boundary checks | 1304--1319 | 558 | `703e3b50120292333f6b00a3e18e887a2a67f2aa7d5dbaf5197c3f4e1a3296aa` |
| `ch55_toric_zero_mass_proof_exact.tex` | exact adjacent complete post-repair proof environment | 1321--1522 | 9017 | `69df8ceb670f2f3db57f97fece992373849bff9057b2e04d9c4780a922434b03` |
| `ch55_toric_zero_mass_statement_proof_exact.tex` | exact contiguous theorem-plus-proof payload | 1304--1522 | 9576 | `7262697860f52b7ab28712c95333be3f96d8f3400527cb2325358885c4b2f2c6` |
| `ch55_toric_zero_mass_section_packet_exact.tex` | exact contiguous setup, theorem, post-repair proof, and scope boundary | 1294--1531 | 10352 | `e4a77f88ab81bbcf403ef3b740af409e53a5454bed95ecf0321f42fd1a25bb58` |
| `ch55_toric_zero_mass_proof_context_cao_attested_20260824.tex` | Rethlas proof context: the exact section packet as a byte-identical prefix, followed by a packet-only Cao primary-source attestation | 1294--1531 prefix + attestation | 11260 | `f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d` |
| `ch55_toric_zero_mass_rethlas_locator_false_positive_diagnostic_20260824T045229Z_703e3b501202.json` | archived raw response for the rejected locator-only run | n/a | 1510 | `1ec991412e444efc9dc5c1cfe685d6612a82726cdcb635c8b44687e2fa07935c` |
| `../rethlas_receipts_20260824/ch55_toric_zero_mass_cao_attested_response.json` | archived valid raw response; original 820 bytes plus one terminal LF | n/a | 821 | `6ae6fdf288771b75f49d2a2745863394faab260fc9057458545627bf9f7984ac` |
| `../rethlas_receipts_20260824/ch55_toric_zero_mass_cao_attested_receipt.md` | exact-current production receipt for run `20260824T052605Z_703e3b501202` | n/a | 4024 | `24faa6146b132fc54f815aa5c240698452e9c3e3af2c4c283ae54753511fddca` |

## Byte-identity checks

All four exact TeX extracts and the exact target text compared byte-for-byte equal
to their stated contiguous line slices of the live chapter.  All `cmp` checks
returned exit status zero.
No title, annotation, line number, macro expansion, whitespace normalization,
or explanatory preface was inserted into an exact extract.

The theorem-plus-proof file includes exactly the single blank line between the
theorem and its proof.  The section packet is one continuous source interval;
it is not stitched.  It begins with `\section{The zero-volume boundary}`,
includes the paragraph distinguishing the direct toric Newton body from the
positive-volume partial body, and ends with the complete adjacent exact-scope
remark.

The first 10,352 bytes of the Cao-attested proof-context file compare
byte-for-byte equal to the complete exact section packet.  Only after that
prefix does the clearly marked packet-only attestation begin.  The archived
JSON preserves all 1,509 source bytes in order and adds one terminal LF so
that the diagnostic is a conventional text file; its source response had
SHA-256 `69d97485a2e810fac0a3bbc88d9c4706c6f8260a742432d1e6a0d86fc811fee0`.

## Intended Rethlas fields

- `statement`: exact bytes of
  `ch55_toric_zero_mass_target_statement.txt`;
- `proof` for a source-aware rerun: exact bytes of
  `ch55_toric_zero_mass_proof_context_cao_attested_20260824.tex`.

The exact section packet, shorter proof-only file, and theorem-plus-proof file
are retained for independent live-source boundary and hash checks.  The valid
source-aware receipt records the target hash `703e3b...3296aa` and submitted
proof digest `f978d2...3896d`.  Subsequent locator-only edits earlier in the
chapter changed the live-chapter digest to `b2134d...619ab` without changing
any submitted target or proof-context byte; all live-slice comparisons were
repeated against that current chapter.

## Framework and normalization carried by the packet

- `X` is a smooth projective toric complex variety of dimension `n`.
- `T` is invariant and positive in an integral or rational big toric class.
- Clearing a denominator replaces `(T,K)` by a positive homothetic pair and
  preserves both Cao numerical dimension and convex dimension.
- `M` and `N` are the character and cocharacter lattices; `lambda_M` gives a
  fundamental parallelepiped of `M` volume one.
- `A` is an integral very ample toric divisor, `Q` is its full-dimensional
  moment polytope, and `epsilon` is positive rational.
- `K` is the closure of the effective domain of the conjugate of the convex
  toric norm weight.  The theorem does not invoke the positive-volume
  definition of a partial Okounkov body at volume zero.
- The book multiplier ideal uses a squared-norm weight `Phi_sigma` and
  integrability against `e^{-m Phi_sigma}`.  The proof sets
  `psi_sigma=Phi_sigma/2`, so Guenancia's norm-weight convention uses
  `e^{-2m psi_sigma}` with exactly the same ideal and lattice scale.
- Guenancia's possibly nonclosed local Newton set and its full-dimensional
  closure have the same interior.
- The inclusion `K subset P_D` shows that the strict shifted Newton condition
  automatically forces every local Laurent exponent to be holomorphic.
- The inner section-count limit runs through integers with
  `m epsilon in Z`.  Lattice-normalized volume appears with no factor `n!`.

## Proof audit map

1. Clear rational denominators and fix the lattice-volume normalization.
2. Use convex conjugacy to obtain
   `Delta(T+epsilon omega_A)=K+epsilon Q`.
3. On each smooth maximal toric chart, write the local exponent of a
   character section using the Cartier data of `D` and `A`.
4. Convert the local squared-norm weight to Guenancia's half-weight, identify
   the interior of its Newton set with the interior of the displayed closed
   body, and use `K subset P_D` to recover holomorphicity.
5. Apply `Guenancia12`, Theorem 1.13, retaining both strict interior and the
   fixed anticanonical shift `kappa_sigma`.
6. Intersect the chart conditions.  Completeness of the fan and strict
   separation prove
   `B=intersection_sigma(B+sigma^vee)`.
7. Divide by `m`.  Finiteness of the fan makes the shifted open intersections
   exhaust the interior of `B_epsilon` and remain in every prescribed outer
   neighborhood.
8. Squeeze their lattice counts between homothetic inner bodies and outer
   parallel bodies.  The fundamental-cell Riemann-sum proof gives the actual
   normalized `m`-limit and confirms the absence of an `n!` factor.
9. Insert that limit into `Cao14`, Proposition 4.4, with the ordinary
   multiplier ideal used in the character count.
10. The two-sided tubular estimate
   `lambda_M(K+epsilon Q) asymp epsilon^(n-dim K)` identifies Cao's logarithmic
   exponent and proves the theorem.

## Imported source boundaries

- `Guenancia12`, Theorem 1.13: exact local monomial membership criterion for
  a toric psh multiplier ideal.
- `CLS11`, Section 4.3: character basis and local toric-frame dictionary.
- `Cao14`, Proposition 4.4: projective logarithmic section-growth criterion
  for Cao numerical dimension.  The controlling persistent PDF is
  `tmp/pdfs/Cao14_arxiv1210.5692_primary.pdf`, SHA-256
  `17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6`;
  physical page 19 contains Proposition 4.4 and its ordinary-versus-
  upper-regularized multiplier-ideal comparison.  Physical page 17 contains
  Lemma 4.3; the paper has no Proposition 4.3.
- Elementary convex duality, strict separation, finite complete-fan gluing,
  and lattice Riemann sums are proved or unfolded in the exact packet rather
  than hidden behind an asymptotic Riemann--Roch slogan.

## Scope firewalls

- No irrational real toric class is included.
- No equality with the positive-volume partial body is invoked at zero
  volume.
- The character condition is not asserted as an unshifted finite-level
  equality with `m(K+epsilon Q) intersect M`.
- The proof establishes an actual normalized limit only after fixing rational
  `epsilon` and taking the indicated divisible subsequence.
- No novelty or publication claim is attached to this synthesis.
- No excluded Deligne-pairing source is used.

## Verification status

The earlier whole-chapter Rethlas run concerned a different chapter hash and
reported this proof interface as a gap before the expansion.  The first
expanded packet still suppressed the book-to-Guenancia half-weight
conversion, the closure/interior passage, and automatic holomorphicity.
Those interfaces are now explicit in the exact post-repair packet identified
above.

Run `20260824T045229Z_703e3b501202`, whose proof digest was the exact section
hash `e4a77f...5bb58`, returned `wrong` for one reason only: it claimed that
Cao's criterion and multiplier-ideal comparison were Proposition 4.3 rather
than Proposition 4.4.  Direct inspection of the controlling primary PDF
proves the reverse.  The run's sole finding is therefore rejected as a
locator false positive; its raw response is archived in the diagnostic file
listed above.  The independent audit is
`manuscript/editorial/ch55_cao_locator_primary_source_audit_20260824.md`,
SHA-256
`225780abbeda94e39d7eda64714a087da1fd90ef5c8f19a5c256e30a714c6e1a`.

The source-attested context was then submitted unchanged in production run
`20260824T052605Z_703e3b501202`.  It returned status `final`, verdict
`correct`, one checked item, zero failed or blocked items, zero critical
errors, and zero gaps.  Its request SHA-256 is
`a4be04e568428d2de5ce8c657f27bc5a595cb8aa89e8d0c157386c26c9a6e649`;
its proof, aggregate-context, adaptive-context, and item-context digests are,
respectively,
`f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`,
`a7b2810ae9892efcd25ab816b6ca81b1ef2d260705055da11156f3b430d98535`,
`c16ee814024761038c55fc1416f8804a31290b5fad272704962fc2771a74ea8b`,
and
`477d75874ccdbdfdda9f02a0617f62e91c4b816a096393c0ce25d50b0c2d01a5`.
The controlling receipt and archived response are the two files listed in
the manifest table.
