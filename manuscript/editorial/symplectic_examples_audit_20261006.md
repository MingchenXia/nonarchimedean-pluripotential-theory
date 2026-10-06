# Nilpotent and hypertoric minimizing gradings, with a cyclic surface

Baseline: `ecdb73643766ddcfd4a004b2e2cfb78e516a513d`, matching
`origin/work`; `origin/main` remains
`00957114db21b627e97369563032ceda9cea09c7`.

Four explanatory subsections in Chapter 68.8 and Appendix L.47 continue
the known symplectic cone discussion. The chapter section heading now
covers both its global stability and local singularity material. The
chapter introduction points to the examples. This checkpoint imports
known results and explicitly identified direct computations; no original
theorem, priority claim or new production-verification receipt is added.

## Primary sources and actual reading

- Xu–Zhuang with Guenancia appendix, arXiv:2606.02401v2: the completed
  earlier full reading and all 54 actually displayed pages are reused.
  The current locators are Lemmas 7.1–7.3 and proofs on actual 32–34,
  Lemma 7.4 and Theorem 7.5 with proofs on 35–36, and Definition 7.7,
  Lemmas 7.8–7.9 and Theorem 7.10 with proofs on 36–38. Selected relevant
  text was reread. This is not a new independent proof of every dependency
  in that source.
- Brylinski–Kostant, JAMS 7(2) (1994), 269–298: a public mirror of the
  printed 30-page journal article was acquired after publisher access
  returned HTTP 403. Title, authors, journal header and first/last printed
  pages were checked against journal metadata. Proposition 1.2 and proof
  are on actual 3, printed 271; Theorem 7.1 and proof on actual 26,
  printed 294. Selected introduction, assumptions and these locators were
  read; four actual pages were displayed. Its earlier theorem dependencies
  are not claimed completely audited. The different 1992 seven-page
  announcement is not substituted for the 1994 theorem locator.
- Namikawa I, arXiv:2408.03012v5, revised 18 October 2025: the acquired
  arXiv edition has 46 actual pages, distinct from the separately
  published 49-page edition. The selected introduction, Hamiltonian
  preliminaries, moment-map equidimensionality, quotient construction and
  final classification text were read. Seventeen actual pages were
  displayed. Lemma 1.1 and the local-model discussion are on 5–7,
  Proposition 2.1 and proof on 8–9, Example 3.5 on 22–23, Corollary 5.4,
  Theorem 5.5 and Corollary 5.6 on 41–43, and Theorem 5.8, Remark 5.9
  and Question 5.10 on 44. This is a selected reading of a known analytic
  classification, not a complete dependency audit of its proof.
- Namikawa II, arXiv:2603.27454v2, revised 6 April 2026: the whole six-page
  text, proof and bibliography were read and all six actual pages were
  displayed. The main theorem is unnumbered in Section 1, actual 1–2;
  the proof occupies 2–5. It is not Theorem 2.1. Its cited Part I input
  and its torus-fiber mechanism have the selected scopes stated above.

The final reading record is
`source_material/symplectic_examples_20261006/full_II_and_selected_dependencies_reading_v2_20261006.json`.
The fourteen fresh contact sheets contain 27 actually displayed pages.
Earlier acquisition and in-progress records retain their historical flags
and bytes. A first installer stopped while matching the reused main-source
image schema, before editing any active manuscript source. The separate
second installer uses the source PDF hash to match those historical
images; it does not rerender them or rewrite their actual-view records.

## Mathematical scope and repairs

1. The centrality argument requires a reductive group preserving the
   valuation. Triangular order-preserving automorphisms show why that
   hypothesis matters. A one-dimensional connected center and the
   form-line centralizer criterion identify a minimizing grading ray.
2. The nilpotent theorem concerns the normalization of a nonzero orbit
   closure in a semisimple complex Lie algebra. Factors with zero orbit
   projection are discarded for the rank argument. The KKS form has
   weight one. The effective image of the group times scaling is used,
   and its connected center is the scaling torus. Semisimplicity does
   not imply a trivial finite center. The quotient is the known
   K-semistable Fano variety; no general K-polystability or metric
   assertion for all orbit closures or Slodowy slices is imported.
3. The hypertoric sequence has injective B, primitive nonzero rows and
   torsion-free cokernel. The standard reduction uses `sum dz wedge dw`
   and `dH = contraction`. Standard scaling has form weight two and
   gives the known global volume minimizer. Unimodularity is an extra
   smooth-resolution condition, not part of that minimizer signature.
4. Swapping z and w leaves the moment products unchanged and preserves
   the zero fiber; it pulls the form back to its negative. It preserves
   the line used by the actual automorphism group, rather than the exact
   form. The full center can also have finite two-torsion. The argument
   uses the connected center of the effective image. Torus-invariant
   homogeneous Hamiltonians justify isotropy of general torus orbits.
5. The cyclic surface is `uv = w^q`, q at least two, with degree-q
   crepant quotient from the plane. Its normalized volume is 4/q.
   Primitive weights divide `(q,q,2)` by `gcd(q,2)`, changing both
   discrepancy and form weight while preserving normalized volume.
   The q=2 case agrees with the sl2 nilpotent cone. The reduced form is
   `du wedge dw / u`, pulls back to `q ds wedge dt`, and has residual
   moment Hamiltonian w in the stated convention.
6. Alternate positive weights `(a,2q-a,2)` have normalized volume
   `4q/[a(2q-a)]`, at least 4/q, with equality exactly at a=q. This is
   a direct weighted-hypersurface computation; it does not exhaust all
   valuations or independently prove global minimality. The latter is
   supplied by the known finite-degree and hypertoric theorems. Exact
   rational arithmetic also checks 899 alternate integer weight cases
   for q=2 through 30 as a normalization sanity check.
7. The alpha value 2/sqrt(q) and critical MT value 3/sqrt(q) are distinct
   with the book's existing dimension-two energy convention. They retain
   isolated algebraic, adapted-probability and ordinary-pole-mass scope.
   No endpoint existence, supercritical nonexistence or general
   all-solution uniqueness is inferred.
8. Namikawa II retains form weight two, projective symplectic resolution,
   an effective Hamiltonian half-dimensional torus and compatibility
   with the good action. Changing the action by a torus cocharacter is
   allowed and can be necessary. It answers Part I Question 5.10 under
   that exact signature. Its global analytic conjugacy removes the
   linear resonance before positive-weight algebraization. Part I/II
   use the opposite form and Hamiltonian sign pair, explicitly separated
   from the book's quotient convention. General cone algebraization
   alone does not supply the prescribed Hamiltonian-torus equivariance.

The general product sketch in Xu–Zhuang Remark 7.11, arbitrary hyperKähler
quotient assertions and unrestricted metric existence are not imported.
General Siu/closure, the recorded BJ22 proof gap and A2–A4 retain their
previous status. The newly acquired September positive-characteristic
twisted loop-slice paper remains research-only. These known imports and
direct consequences lie in the verification protocol's ordinary
mathematical/source-audit scope.

## Source checks before compilation

The 425-input build closure has 423 unchanged active sources. All 108
protected inputs, 46 previous formal statement/proof blocks and all 42
complete canonical status rows are byte-preserved. Thirteen new labels,
eight equation tags and three index entries are added; all 12,787 labels
and 655 bibliography keys are unique, and all 360 cited keys resolve.
The previous bibliography prefix is unchanged. All 45 preceding frozen
integration manifests, previous exports, native catalogue and inactive
toric candidate retain their bytes. The section-heading and introduction
edits are separately checked; the historical claim ledger and all prior
local mathematical subsections are unchanged. Final compilation, PDF
rereading and exports are recorded below after they complete.

## Final build and actual PDF rereading

The final second build has 4,361 pages, 20,278,298 bytes, SHA-256
`0365d3d3ea1a618c1435d2a9a12846df70c17e40b0828394dbf239ab127b4718`.
There are no TeX errors, LaTeX/package/pdfTeX warnings, missing
characters, unresolved references/citations, overfull boxes or rerun
requests. The existing 954 underfull boxes are unchanged. BibTeX uses
360 entries without warnings. The index accepts 758 entries, rejects
none and has no warnings; all 415 distinct numeric destinations exist.
PDF checks find 21,840 named destinations, 46,876 internal links, 171
external links and 2,541 contents entries across six parts; all checked
destinations are valid.

The first 4,361-page build passed compilation but its partial visual
review of sixteen actual pages found a mathematical sign error in the
new moment-map paragraph: the products z_j w_j are unchanged by the
swap, so `mu(w,z) = mu(z,w)`. The form sign remains negative. A separate
source version corrects that equality. A crowded contents heading was
also shortened to “Hypertoric algebraization with form weight two.”
The first build, first source check and partially viewed image record
are historical; they do not certify the final PDF.

The final PDF was reread on actual pages 60–61, 68, 3565, 3582,
3598–3604, 4124–4128 and 4335–4361: forty-four matching pages in
twenty-two contact sheets. All new chapter and provenance material,
the adjacent metric and big-class transitions, the next appendix
opening, full index and complete bibliography were actually displayed.
The corrected moment identity, negative form pullback, primitive
weights, cyclic constants and controlling editions were inspected.
No complete whole-book rereading is claimed for this checkpoint.

Final records are `/tmp/symplectic_examples_source_gates_v2_20261006.json`,
`/tmp/symplectic_examples_release_gates_v2_20261006.json` and
`/tmp/symplectic_examples_book_pages_v2_20261006/manifest.json`.
The complete new source-reading record and all earlier frozen reading
records retain their bytes after admission. The native catalogue remains
open and has not been edited, reopened or recompiled.

The final 603-member source archive includes the full active closure,
current bibliography, inherited support and provenance, this audit and
manifest, and the preceding export record. Every member is checked
against its source bytes. No fresh isolated archive compilation is
claimed. The PDF, matching 44-page review and archive hashes are in
the current artifact record; earlier reviews certify their own PDFs.
