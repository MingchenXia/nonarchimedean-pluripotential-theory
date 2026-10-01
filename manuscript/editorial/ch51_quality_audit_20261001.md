# Chapter 51 completion audit

Date: 1 October 2026

Base: local Chapter 50 commit `6a056fc`.

Scope: `parts/part5/ch51_complex_prerequisites.tex`, under the sequential
quality programme. Chapter 52 is next; the whole-book goal continues.
Independent Chapter 72 research remains paused.

## Mathematical and expository review

The full chapter source, proofs, examples, import register and provenance
discussion were reviewed. There are 31 formal assertions in theorem-like
environments (sixteen propositions, seven corollaries, four lemmas and four
theorems), plus two separately numbered foundational input interfaces for
strong openness and the valuative criterion. These have proofs, deductions
or explicit source boundaries. All 84 reusable environments have semantic
labels; the chapter has 260 labels.

Substantive repairs include:

- Nonpluripolar products now require local finiteness. The proof of
  potential independence compares both cutoff masses; positive-cone
  additivity includes the finiteness equivalence. Global Kähler finiteness
  uses positive Kähler representatives. Restricted cutoff currents are not
  incorrectly asserted to be closed. Closedness uses the BEGZ cutoff,
  chain-rule and Cauchy--Schwarz argument. The modification proof establishes
  local mass downstairs and the mixed smooth-form projection formula.
- The Lelong-number convention distinguishes log from log squared by its
  factor of two. The radial comparison uses Demailly's multiplicative
  Harnack constant. Increasing-net continuity uses convex radial maxima and
  a uniform logarithmic barrier, rather than unproved spherical net
  integration. Divisorial pullback, generic values and Skoda's
  nonintegrability implication have their actual arguments.
- The valuative multiplier-ideal criterion has a locally uniform margin
  over divisors above a neighbourhood of each point. The one-sided ideal
  inequality is proved explicitly. Monomial lattice minima include zero;
  the single-pole example respects strict jump endpoints. Quasi-equisingular
  recovery uses the union over strictly larger exponents followed by the
  intersection over approximants, in the stated limit order. Real analytic
  weights and real resolution divisors are distinguished from rational
  gentle approximations.
- Rooftop contact and limiting contact use the exact DDNL statements.
  The projection argument invokes domination relative to an arbitrary
  common positive-mass reference; it does not assume the idempotence being
  proved. The recent big-class zero-mass idempotence input is separate from
  positive-mass domination. Background independence and ideal-detected
  volume record changes of smooth representative as well as potentials.
- The projective-line half-pole envelope is proved from the full
  rotation-invariant competitor family and convex slopes. It gives explicit
  strictness examples for envelope concavity and maxima. Duplicate proofs
  and an unsupported converse envelope-order argument were removed.
- The Cantor example constructs its probability measure, proves a sufficient
  zero-capacity condition by logarithmic energy and exact telescoping, and
  proves its Green potential is minus infinity at every point of the set.
  Upper semicontinuity, integrability, the zero endpoint, vanishing ideal
  data and the mass loss are justified separately. The trace conclusions
  retain their additional theorem inputs.
- Compactness, Choquet reduction, Hartogs arguments, cohomological mass and
  monotone/capacity convergence retain their precise hypotheses. The import
  register records principal groups without claiming to list every later
  analytic input. Reusable objects are labelled and legacy inline
  delimiters have been removed.

The nonpluripolar-product repairs adapt the already authored repaired
production packet in
`editorial/solver_dossiers_20260901/ch51_npp_ledger_comprehensive_production_packet_v2_repaired_authored_20260901`.
Its source-exact and proof material was read. Frozen packet files, source
pins and receipts were not modified. This is an editorial integration of
known mathematics, not a new research or independent-verifier result.

## Direct primary-source interfaces

Eight critical primary PDFs were checked at the relevant statements and
proofs; 32 source pages were rendered and inspected. The ignored local
cache is `source_material/ch51_audit_20261001`.

| Source and checked version | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Xia, supplied book snapshot dated 18 July 2026, matching its historical source pin | Proposition 1.5.1; Theorem 1.6.2; Theorem 2.4.5; Section 3.1 rooftop, contact and projection; Lemma 6.1.1 | 45, 49--50, 87--88, 98--102, 210--211 |
| BEGZ, arXiv 0812.3674 v2 | Definition 1.1, Example 1.3, Proposition 1.4, Lemma 1.5, Proposition 1.6, Remark 1.7, Theorem 1.8 and Lemma 1.9 | 5--10 |
| Bedford--Taylor 1982, A new capacity for plurisubharmonic functions | Theorem 6.9, pluripolarity and zero outer capacity | 25 |
| Boucksom, L2 notes | Corollary 10.18 and its locally uniform valuative margin proof | 45--46 |
| DDNL, arXiv 1705.05796 v3, 6 May 2018 | Theorems 2.3--2.4; Lemma 3.7; Theorem 3.8; Proposition 3.11; Theorem 3.12 | 7--8, 12--15 |
| Darvas--Xia trace, arXiv 2403.08259 v2, 13 March 2026 | Theorem 2.2 and Definition 2.4, decreasing dyadic approximation and exponent recovery | 8--9 |
| Pang--Sun--Wang--Zhou, arXiv 2607.12797 v1, 14 July 2026 | Theorem 1.2, big-class zero-mass idempotence | 4 |
| Demailly, Complex analytic and differential geometry | Chapter III Section 6, Corollary 6.8 and Example 6.9 | 164--165 |

PDF SHA-256 values, in that order:

1. `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`
2. `43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd`
3. `e75ea91e48c14a9838a800aee25b68ed04169c4372f2ce4b399967b53005b758`
4. `5e3b9441461c6eab35f546c35087cdec0dd146daa84460a00058750eb5cd0909`
5. `1e614744bc4d769f377827ca81774b5f6c3d345a2619216fb6f4c81682d599cc`
6. `5d6f43d96be101f6aa1a3ddbdd92b5bc49131a0deabbf199e03111d6c0fbaa3c`
7. `58d5aabb51eb5b4f14a3a72b892cb6cd794cf79945de88222ec350e3e54b0362`
8. `d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1`

Other historical inputs retain their explicit citations. No fresh direct
inspection of every historical reference is claimed.

## Calculation and verification

The independent exact-rational/symbolic supplement passes 119,417 checks:
monomial lattice minima and generators, strict radial integrability jumps,
Cantor energy telescoping, the projective-line half-envelope slopes and
mass, the blowup mass/Duistermaat--Heckman density, and the direction of the
quasi-equisingular exponent limit in a logarithmic-pole model. These are
calculation checks, not a substitute for the written analytic proofs.

Scoped reviews before and after rendering find no unlabelled reusable
environments, proofless formal assertions, duplicate labels, nesting errors,
legacy inline delimiters, double-dollar displays or TODO/FIXME/TBD markers.
The legacy writing-audit executable is unavailable; no warning counts from
that executable are claimed.

The project reference checker passes: 425 inputs, 12,037 labels, no missing
inputs, duplicate labels, dangling references or structural defects. All
six checker regression tests pass. The unchanged research inventory has
42 atoms in twelve environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17.
The post-render scoped and reference checks and `git diff --check` pass.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds using workspace-local TeX Live 2025. The final PDF has
4,108 pages and 19,178,175 bytes, SHA-256
`9517ae756b4e52bdee198581acf5a63a7b01a8aaedc0c1580a3c9b1db7421c66`.
Final chapter source SHA-256:
`724b3bad739e8e843ffb4837c3ed8d4088bb6c64cb9b0d2579f8f15f49548d05`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 51 has zero overfull boxes and zero
LaTeX/package warnings. Nineteen overfull boxes elsewhere and thirteen
duplicate PDF destinations in Chapter 70 remain recorded.

All 70 chapter pages, physical 2959--3028 (printed 2891--2960), were scanned
in both pre-final and final builds; physical 3028 is intentionally blank.
Thirty detail/seam pages were inspected in the first review, and seventeen
detail pages in the final review, giving 32 distinct chapter detail pages
and two adjoining seams across the reviews. Final detail pages are 2968,
2976, 2986--2988, 2999, 3004--3006, 3008, 3012--3013, 3016--3018, 3020
and 3027. All final reflowed pages were rescanned. Adjoining physical
pages 2958 and 3029 were inspected. No reviewed clipping, overlap, bad glyph,
formula overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent or
current-model verifier verdict. Generated PDFs are local review artifacts.
Frozen releases, dated checksum ledgers and research atoms are unchanged.
Verified work remains local pending explicit remote-push approval.
