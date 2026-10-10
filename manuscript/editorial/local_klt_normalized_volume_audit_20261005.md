# Local algebraic klt comparison and uniform integrability — 5 October 2026

This checkpoint continues the dependency question recorded in the global-klt
audit without rewriting that frozen historical record. The new Chapter 68.8
subsections and provenance L.43 explain known primary-ideal approximation,
ordinary polar-mass comparison, pointwise alpha and uniform alpha results.
They are imports and explicitly identified explanations of known results;
there is no original priority claim or independent production-model receipt.

## Category and normalizations

The b-divisor argument is restricted to isolated normal complex algebraic
Q-Gorenstein klt germs of dimension at least two, with psh functions on the
analytification. BdFF's controlling approximation theorem is algebraic.
It is not silently extended to every complex analytic germ. The local
neighborhood is bounded strongly pseudoconvex with smooth regular boundary.
Some rK is trivial on a neighborhood of its closure, permitting a larger
domain and extension of the flat adapted probability measure.

The operator is i partial partialbar/(2 pi). The primary ideal potential
is log(sum |f_j|^2); its divisorial coefficient is the ideal order and
its ordinary residual mass is the Hilbert–Samuel multiplicity. The published
GT main text uses the same convention. The unsquared generator sum in
Appendix A.9 is not copied. BBJ v3 instead uses log|s| and an L2 weight;
half of the book potential gives its coefficients and the adapted L1
exponent exactly. All local top measures here are ordinary Cegrell measures
retaining polar mass, independently of the global nonpluripolar equation.

## Controlling files and selected inspection

- GT institutional published-format PDF: 44 actual pages including two
  covers, 947555 bytes, SHA-256
  `82521b158a23b0a0e1f8b782383520a9206e9a78d2a170af43174abdd3dcf472`.
  Compositio Mathematica 161(4) (2025), 714–755,
  DOI 10.1112/S0010437X24007619, with Boucksom's appendix.
  Fourteen selected actual pages freshly displayed: 7–9, 11–12, 19–20,
  26–28 and 38–41. Earlier selected readings also cover the MT bounds
  and existence proof. No full-paper reading or byte comparison with
  the unacquired publisher download is claimed.
- BdFF author-hosted published-format PDF: 66 actual pages, 424875 bytes,
  SHA-256 `44f52824c1bec3fd59631ec78567c587b718bda70bfc2241ec5311fc50346666`.
  Duke Mathematical Journal 161(8) (2012), 1455–1520,
  DOI 10.1215/00127094-1593317. Twenty-five selected actual pages
  freshly displayed: 1, 8–10, 18–24, 40–42, 44–50 and 60–63.
  Selected extracted ranges are recorded separately; no full reading.
- BBJ reused arXiv:1509.04561v3, revised 8 September 2020: 40 actual
  pages, 751879 bytes, SHA-256
  `6973d1df47b527ce9c27e2496d8bd91b949c8e28b4123c2f708e45ccc6836b00`.
  Appendix B's definitions, Lemmas B.3–B.4 and Theorem B.5 with its
  proof were read; all actual pages 31–36 freshly displayed.
  A separate bibliography key prevents journal-pagination transfer.
- Liu arXiv:1605.01034v5, revised 23 May 2018: 29 actual pages,
  402031 bytes, SHA-256
  `c10314baae930f34b37bcf3d17ee54acbf1442f426ce4582304bfb5c8c4a9fec`.
  Selected text 175–267 and 900–994, and actual pages 4–5 and 17–19
  inspected. The separate published 2018 file is unacquired.
- Darvas–Zhang arXiv:2608.23505v2, revised 13 September 2026:
  reuse of the earlier full 33-page source reading, SHA-256
  `c79f474903068d25d1ca3092f1afb27ff9f6f069333b61bfc2a705f3c0b02d7a`.
  The local introduction and Section 8 were reread for this application.
  No new full-primary-reading receipt replaces the frozen one.

Fifty primary pages were freshly displayed in 27 sheets. Matching manifests:
`/tmp/local_klt_bdivisor_primary_selected_v1_20261005/manifest.json`,
`/tmp/local_klt_integrability_primary_selected_v1_20261005/manifest.json`,
and `/tmp/local_klt_trace_primary_selected_v1_20261005/manifest.json`.
The ignored cache has fresh reading and supplement records; earlier
acquisitions and reading records keep their bytes.

## What supplies the missing comparison

GT Lemma 5.9 is existential. Its displayed single valuation-ideal
asymptotic order (5.9) does not by itself imply a full psh singularity
comparison with all other divisors. The new explanation uses Appendix
Proposition A.9's nefness, BdFF Proposition 2.12/Corollary 2.13, and
Theorem 4.11 to select different primary ideals.

Fix a divisor F with c=v_F(u)>0. Choose a smooth determination containing
F and isomorphic away from p. Approximate its finite real trace from
above by a rational trace D with D_F<−(1−epsilon/2)c. Its nef envelope
W lies above B=Z(u), while B_F<=W_F<=D_F. Clearing the Cartier denominator
and applying positive homogeneity allows Theorem 4.11 in its stated
integral setting. It produces rational q_k and primary I_k with
q_k Z(I_k)>=W>=B and coefficientwise convergence to W. Thus, for some k,
q_k v_F(I_k)>=(1−epsilon)c.

The simultaneous coefficient inequality on a log resolution of I_k
allows subtraction of the analytic divisorial current. The remainder
is positive, so its psh potential is bounded above on a finite cover of
the compact exceptional fiber. Consequently u<=q_k log(sum |f_j|^2)+O(1),
and nu_I(u)>=q_k>=(1−epsilon)c/v_F(I). This proves precisely the known
existential comparison in the displayed algebraic scope. No claim that
the original particular valuation ideals satisfy that comparison is made.
Differences of potentials are formed off the divisor before psh extension,
not by subtracting two infinities on the divisor.

## Approximation and sign checks

BdFF Theorem 4.11 gives positive rational multiples from above. It does
not promise a decreasing sequence. The proof of Theorem 4.14 states the
needed intersection convergence for every from-above coefficientwise
convergent family, using upper semicontinuity and monotonicity. A positive
rational coefficient a/b can be written as b^−1 Z(I^a). Real traces can
be approximated by rational traces using Corollary 2.7. These properties
give the primary approximants in GT Lemma A.8 without copying its
extra decreasing-sequence assertion.

Intersection products increase with b-divisors; e(B)=−B^n therefore
decreases. The direction B<=v(u)Z(v) gives e(B)>=v(u)^n vol(v), and
e(B)<=the ordinary residual mass follows by analytic singularity
comparison and the supremum of primary-ideal multiplicities.
The residual-mass argument retains local boundedness away from p.
The all-F1 pointwise theorem is separately identified and uses total
mass and the existential ideal selection, not a false isolated-pole
assumption on every potential. Zero coefficients impose no threshold
constraint; zero residual mass is treated directly, with no 0 times infinity.

Other visible source slips are not reproduced. Liu v5 Lemma 26 ends
with alpha vol(v) although the length scaling requires alpha^n vol(v).
BBJ v3's SNC step on page 36 requires c(V)−c(U)<1. BdFF's appendix
Lemma A.4 on actual page 63 ends its telescoping sum with Z_n−W_n,
where W_n−Z_n is required. These are direct displayed-formula checks,
not counterexamples to the corresponding known theorems.

## Uniformity and critical parameter

The local adapted continuity theorem acts on a compact set strictly
inside its domain. DZ Section 8 first extends each continuous test
potential by an obstacle envelope to Omega-prime containing closure(Omega).
Ordinary contact concentration gives an extended mass bound <=1.
Compactness then supplies an L1 limit in F1(Omega-prime). The pointwise
volume formula on that larger domain provides an exponent strictly
above lambda; continuity bounds the exponential integrals on the
smaller domain, contradicting the proposed divergence. Neither domain
extension nor the strict larger exponent is omitted.

Known published GT Theorem 5.1 is the lower MT bound and Theorem 4.5
is the upper bound. Published 3.5 is an energy lemma, while the old
arXiv has a different numbered upper bound. The final formula is
gamma_crit=(n+1) volhat^(1/n)/n; GT Theorem C and DZ Corollary 1.7
give strict subcritical existence. This does not give endpoint existence,
uniqueness or nonexistence of all supercritical solutions.

## Preservation

This is an explanation of established local results, not a resolution
of the canonical general non-Archimedean Siu/closure or A2–A4 questions.
The BJ22 changing-divisor proof gap stays explicit. All forty-two full
canonical status rows, the native catalogue and its PDF, the separate
research-only toric candidate, preceding primary receipts, and frozen
manifests/exports retain their bytes. The previous boundary release,
including its index hook, is the comparison baseline. No new independent
model call, isolated archive compilation or full-book rereading is claimed.

## Final source and rendered-book checks

The final full build has 4,340 pages. TeX errors, unresolved references
and citations, package/pdfTeX warnings, missing characters, overfull boxes
and rerun requests are zero. The 954 underfull-box diagnostics are the
existing book count. BibTeX uses 341 entries with no warnings; MakeIndex
accepts 747 entries with no rejection or warning. All 46,738 internal links,
21,756 named destinations and 407 distinct numeric index destinations pass.
The reference checker finds 425 inputs and 12,743 unique labels, all clean.
The inventory checker passes 42 atoms in 12 families and tiers 0/3/7/15/17.

Thirty-two matching final book pages were actually displayed in sixteen
sheets, including all new subsection pages, both repaired transitions,
all of L.43, the new index entry and the complete sixteen-page bibliography.
The review manifest is
`/tmp/local_klt_normalized_volume_book_pages_v2_20261005/manifest.json`.
The earlier v1 render selected inherited boundary pages by mistake; none
of those sheets is claimed as viewed or included in this release review.
The first full build's three long-reference overflows were repaired using
breakable DOI links and a shorter citation sentence. The final source and
PDF gates are fresh v2 records, preserving all v1 diagnostic bytes.

Two active inputs changed; the other 423 are byte-preserved. Forty-six
existing formal statement/proof blocks in Chapter 68 and Appendix L,
108 protected inputs, forty-one preceding frozen manifests, all complete
canonical status rows, previous exports and the native catalogue pass
their byte-preservation checks. Four appended bibliography keys identify
the controlling GT, BdFF, Liu and BBJ editions; prior bibliography bytes
remain intact. Routine work-branch publication uses the user's standing
GitHub authorization and preserves main.
