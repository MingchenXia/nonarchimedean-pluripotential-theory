# Local critical concentration and ordinary pole masses

This known-result checkpoint follows `02231e2`. It adds Chapter 68.11
and provenance L.41, after the fixed-class Orlicz section. It contains
identified known results and direct formal calculations, with no
original-result claim and no new independent model call. The separate
toric entropy candidate remains research-only OPEN.

## Controlling sources and honest reading scope

The sources are cached under `source_material/BB_critical_dependencies_20261005/`,
except the previously acquired Berman–Berndtsson publisher PDF under
`source_material/meanfield_entropy_dependencies_20261005/`. Every source
is version identified; journal and preprint locators are kept separate.

| Source | Controlling file and anchors | Actual pages displayed |
| --- | --- | --- |
| Berman–Berndtsson | AFST 31(3), 2022, 595–645, DOI 10.5802/afst.1704; 52 actual pages including cover. Section 4.2 at actual 30/printed 623, Theorems 7.2 and 7.4 at actual 46–48/printed 639–641, radial prototype actual 26/printed 619 and later discussion actual 49/printed 642 | 4, 7–8, 13–14, 26, 30–34, 45–52: nineteen |
| Rashkovskii | CR Math. 353(1), 2015, 21–24; DOI 10.1016/j.crma.2014.11.002. Complete four-page publisher text. Lemma 1.1, Theorem 1.2 and Corollary 1.3 actual 2/printed 22; Lemma 2.1 and equality proof actual 3/printed 23 | All four |
| Chi Li | Public author file, dated 23 August 2014, fifteen pages. Theorem 3 actual 3, identity and proof actual 7–8; separate from fourteen-page arXiv v1 and the 2016 journal version | 2–3, 7–9, 13: six |
| Åhag–Cegrell–Kołodziej–Pham–Zeriahi | arXiv:0804.3954v3, revised 21 May 2008, twenty-two pages. Theorem 5.5 actual 15, Proposition 6.3 actual 19 | 2, 4–5, 13–15, 18–19: eight |
| Demailly–Kollár | Original 2001 publisher PDF, thirty-two pages; Main Theorem 0.2(2) and differential convention actual 2/printed 526 | One |
| Åhag–Cegrell–Czyż–Hiep | arXiv:0706.0169v3, revised 19 August 2008, sixteen pages. Ordered identity principle Theorem 3.6 actual 7; Theorem 3.7 actual 8 is a different nonpolar statement | 3, 7–8: three |
| Błocki | Original 1996 publisher PDF, twenty-eight pages including cover. Theorems 5.1(i), 5.3 and complete stability proof at actual 22–24/printed 741–743; hyperconvex approximation actual 25/printed 744 | Four |
| Demailly with Zeriahi's Appendix | arXiv:0709.3524v2, revised 27 November 2007, fourteen pages. Convention actual 2, Observation A.3 and closure/mass proof actual 13–14 | Three |

These are forty-eight actual pages in twenty-six sheets. All were actually
displayed. Only Rashkovskii's four-page paper was read in full; selected
readings of the other seven sources are not called complete readings.
The cached `reading_progress_v1` remains a research-only historical record;
a new `reading_progress_v2` records the admitted known inputs. Earlier
mean-field, entropy and Orlicz reading records are unchanged.

PDF SHA-256 digests, in table order:

- BB: `82d7e74c3dae2fdcb718a1d3b4bcdcc2ba60af1ab8b8dbca3f215a7d5f7708f3`.
- Rashkovskii: `af6eb521abb6b044455e9fb4127458d11bcdc032e65bc076fcf0df4a13df9c50`.
- Li author version: `c26086cc8c0431ec27a3e358f50a4fec5db8465f3290bda8c01ef9734e845025`.
- ACKPZ v3: `800baa894fd41f08f2948e9edf2b25e5e93ed4b29664a1384ce08ced9d83ebfe`.
- DK: `379322970ebebef6d8d88245db371f9e4070673d5d0392a27102934fd84303a5`.
- ACCH v3: `28ee2872f751b1f276c1a7a5d2ab48816e06e8fd85a95f8e5e586bb2dec4469b`.
- Błocki: `79defba77313129636c0e7387548e0aaca1678767474f1b3943d8a089438727c`.
- Demailly v2: `fe6eef001e2518377593220fd3a573adf52824c8c0da0c693dee87169a3391c8`.

The original Cegrell–Persson 1992 publisher endpoint returned a web
protection page instead of a PDF. The admitted stability citation is
Błocki's theorem with its complete proof, not an allegedly read original.
Li's 2016 publisher download returned HTTP 403. His public author file,
linked from his current publication page, controls this import. No access
control was bypassed and neither inaccessible PDF is claimed acquired.
The Demailly arXiv file's generated print date does not change its version
or assign the later proceedings pagination.

## Signature, signs and selected maximizers

The domain is bounded hyperconvex in C^n, n>=1, with ordinary local
Monge–Ampère, zero boundary values, book ddc=i/(2pi) partial-barpartial,
and Euclidean probability volume. The equation has ordinary mass one.
The E^1 class uses finite positive energy in decreasing E0 approximation;
the F class separately uses finite total mass. No general inclusion of
E^1 into the finite-mass F class is asserted.

BB's Section 4.2 defines E=(n+1)^(-1) integral u MA(u), which is negative,
and G_gamma=E+gamma^(-1) log Z_gamma. Its later display (7.3) has the
wrong positive sign on the (-u) term. The book uses the controlling
Section 4.2 definition. Probability normalization changes G by a constant
at each gamma, leaving maximizing potentials unchanged.

Theorem 7.2 supplies continuous zero-boundary variational maximizers for
0<gamma<n+1. Theorem 7.4 concerns those selected maximizers as gamma
increases to n+1 and explicitly assumes no boundary blow-up and an
L1_loc limit in F. It is not asserted for arbitrary solutions. Its two
alternatives are uniform convergence to a critical maximizer/solution,
or a unit-pole Green limit. No all-parameter uniqueness is imported.

## Bounded branch and density convergence

For t=n+delta and uniformly bounded Z_t, Gibbs entropy is
H=gamma b-log Z_gamma with b=integral(-u) MA(u). The entropy variational
inequality gives H>=t b-log C, so the direct formal identity
G=nb/(n+1)-H/gamma bounds it above by
-delta b/(n+1)+log C/gamma. A fixed test function and maximizing property
bound b. The known subcritical Moser–Trudinger estimate after scaling
gives every fixed exponential moment. This controls the varying exponents
and yields strong L2 convergence of normalized densities.

Błocki's Theorem 5.1(i) is used on pairs of approximating solutions:
both potentials and both densities are continuous on the closure and the
boundary values agree. Theorem 5.3 supplies (infinity,2) stability. The
sequence is uniformly Cauchy before continuity of its limit is invoked.
The book does not silently replace the source's continuous-density
hypothesis by a theorem for arbitrary rough densities. Constants absorb
operator normalization. The known limiting variational argument yields
the critical equation and maximizing property.

## Unbounded branch and Green identification

No boundary blow-up gives a uniform lower bound outside one compact K.
DK's effective exponent semicontinuity and a finite cover of K imply that
some limit exponent is at most n when every exponential bound above n
fails. The mass bound is separate: Zeriahi's Observation A.3 replaces
the approximants by upper regularized suprema of tails, uses comparison,
and then Cegrell monotone convergence to obtain total ordinary mass <=1.
No general L1 continuity of the original top measures is inferred.

ACKPZ's local estimate c_z>=n/m_z^(1/n), where m_z is the ordinary pole
atom, forces that bad point's atom to be at least one. The total bound
then forces a Dirac measure of mass one and exponent n. BB's (7.14)
omits the top-power superscript; the book restores it.

The final equality is not justified by dropping Rashkovskii's unit
Lelong-number premise. In his half-potential units, the mixed-mass
equality analysis in Theorem 1.2 supplies that unit Lelong number, and
Corollary 1.3 applies with global mass one. His proof passes through
greenification, whose equality of singularity type is not an automatic
equality with the original potential. The order in Lemma 2.1 and the
ordered identity principle completes the identification. The latter is
Theorem 3.6 in ACCH arXiv v3; published numbering quoted elsewhere is
not used as a locator in this different file.

DK, Rashkovskii, ACKPZ and Demailly use twice the book operator.
Putting u_source=u_book/2 keeps currents and residual masses identical;
their exponential exp(-2c u_source) equals exp(-c u_book). BB uses the
book operator itself. This local conversion is different from the
compact class-form rescaling used in the preceding chapter imports.

## Ball scaling and limits of the smooth obstruction

With r=|z|^2 and a=epsilon^2, q=log((r+a)/(1+a)) has mass (1+a)^(-n).
The correct mass-one potential is u=(1+a)q and gamma=(n+1)/(1+a).
The radial determinant gives density n! a/[pi^n(r+a)^(n+1)] for q;
radial integration gives Z_gamma(u)=(1+a)/a. Thus u solves the normalized
equation, tends to log r, and its ordinary top measure tends to delta_0.
The exponent-scaled potential gamma u=(n+1)q has limit (n+1)log r.
BB's later identification with that exponent-scaled prototype omits
the mass-one scaling. The book includes the direct integral calculation.
The separate symbolic check of dimensions 1–4 is diagnostic only;
the displayed radial derivative establishes the mass calculation in
general dimension. No independent verifier receipt is claimed for it.

Li's Theorem 3 excludes psh C2(closure) intersect C4(interior) ball
solutions when the determinant-equation constant is at least
(n+1)^n pi^n/n!. The book's constant is gamma^n pi^n/n!, giving
gamma>=n+1 in this regularity class without symmetry. No absence of
all bounded weak solutions is inferred without additional regularity.
No unrestricted maximizing property or all-solution radial symmetry
is inferred from the explicit family. BB's 2022 Conjecture 7.6 is
described as that source's question; the 2025 small-parameter result
does not answer it, and no exhaustive current symmetry survey is claimed.

The Green pole has infinite E^1 energy. Its ordinary top measure has
mass one and its non-pluripolar top measure has mass zero. The import
does not alter singular local klt, non-Archimedean entropy, Siu/general
closure, spectral or A2–A4 boundaries, or retire a canonical problem.

## Release checks

The source and final release gates are recorded in the accompanying
integration manifest. Earlier source and PDF exports, frozen manifests,
forty-two complete canonical status rows and the native catalogue remain
byte preserved. A scoped release page review is distinguished from a
new complete reading of the whole book. No isolated source-archive
compilation or new independent model receipt is claimed.

The final book has 4,332 pages, 20,139,287 bytes and SHA-256
`f9dea5492cfd3feea0e1fb7c0ea7f839f864770a4a9a719ee92adf1b8c637ce1`.
Final TeX errors, LaTeX/package and pdfTeX warnings, missing characters,
overfull boxes, unresolved references/citations and rerun requests are zero.
The 954 underfull boxes are recorded. The first-pass citations resolve
through the completed latexmk/BibTeX passes; the final log controls this
claim. A reference check initially run at the repository root had a
missing book.tex and zero closure; the corrected manuscript-root check
reports the actual 425 inputs and 12,715 unique labels with no missing
inputs or dangling references. No zero-input check is counted as evidence.

The two edited active TeX files retain all forty-six pre-existing formal
blocks/proofs byte for byte. No formal environment is added. Twelve new
labels, seven manual tags 68.23ae–68.23ak, seven new bibliography keys
and two index entries accompany the import. Prior bibliography bytes are
preserved; the totals are 631 keys and 336 cited entries. All 108 protected
inputs and thirty-nine previous frozen manifests retain their digests.

The index accepts 745 entries without rejection or warnings, with 744
hyperpage groups and 405 valid numeric destinations. All 21,715 named
destinations, 46,676 internal links, 163 URL links and 2,513 contents
entries have valid applicable targets; all six part roots remain.
Thirty-four matching final-book pages were freshly displayed, including
all new Chapter 68 and L.41 pages, their transitions, current contents,
index boundaries and the complete sixteen-page bibliography. A preliminary
unviewed selection inadvertently retained the preceding Orlicz page list;
it is preserved separately and contributes no visual-check claim. The
corrected v2 selection controls the release review. No TeX repair or
second full-book reading is inferred from this selection correction.
