# Six supplied solution manuscripts: integration audit, 24 September 2026

## Baseline and scope

Baseline commit: `8dd0f876c6a870bc4f76841bb570fcfd2841a956` on main,
synchronized with the designated GitHub origin. Drafting and full builds
used a temporary copy. The supplied P06.1 PDF duplicates one of the five
papers in the ZIP. Together with P12.6 there are six distinct manuscripts.
All six proofs are integrated into the mathematical chapters; Chapter 72
and the editorial ledgers record the exact remaining boundaries.

| Question | Integrated result | Editorial consequence |
| --- | --- | --- |
| P06.1 | Classical pluriharmonic functions on good separated strict boundaryless analytic spaces over a complete nontrivially valued field are real PL, including arbitrary singularities | Retire P06.1 in its original scope; retain P06.2, which starts from a current equation |
| P07.1 | First-stage collapse on good separated analytic spaces over any complete field; positive-coordinate approximation on finite products of arbitrary stars at node tuples | Record the analytic positive range |
| P07.1 | A compact CLD star with restricted affinage carries a bounded continuous second-stage function outside stage one | Retire the unrestricted affine G-tropical universal question with a negative answer; no analytic realization is claimed |
| P03.1 | A geometrically integral seminormal pinched bidisc, smooth away from a codimension-two point, has an explicit finite USC obstacle whose regularized envelope fails the curve test | Codimension-one sufficiency is false; the general classification and P03.2--P03.3 remain active |
| P21.3 | Zero-Hessian continuous functions on full products of open discs and annuli are affine in annular logarithms | Independent proof of the already established polycylinder range; general P21.3 remains active |
| P12.6 | Finite restriction, extrema, norm traces, conductor-compatible branch descent, determinant traces, towers and gauge changes | The valuative transfer layer is established; independently geometric psh and Monge--Ampere compatibility remain active |

The active inventory changes from 45 to **43 atoms**, from 14 to **13
formal problem environments**, with tier totals **(0,3,8,15,17)**.
The remaining P06 problem contains P06.2 only. The former P07 problem is
a resolved-scope remark retaining its old label, so historical references
remain valid. The inventory checker now counts labels within actual
problem environments and separately checks the retained P07 label.
The original source index keeps its broader P07 research campaign active;
that campaign status does not change the negative answer to the book's
literal unrestricted universal question. Non-good analytic spaces and
other transfinite phenomena are not classified here.

## Proof integration and two local passes

The first pass read all five TeX manuscripts and the complete P12.6 PDF,
matched statements to the book's current hypotheses and notation, and
checked the following proof mechanisms and edge cases. The second pass
reread the adapted fragments against the originals and primary inputs,
then checked the cross-references, status transitions and final layout.
These are two local reviews by the integrating assistant, not two
independent reviewers or a fresh production-verifier receipt.

For P06.1, the closed-subspace argument is stated in ambient affinoid
germs: choose W first and write T0=T intersect W. Unit-norm tubes lift
real-logarithmic presentations. Finite descent separates finite-group
invariants, radicial Frobenius powers, normal separable descent and
conductor induction. Proper descent uses a generically finite
multisection and dimension induction, retaining the locus where the
modification is an isomorphism. A regular alteration cover supplies the
quasi-smooth charts over an algebraically closed field. The semistable
input includes the boundary of the covering affinoid. The final
completed-algebraic-extension argument descends the finite presentation;
it does not claim that a general quasi-etale cover is finite or
boundaryless in the Berkovich sense. The nontrivial-valuation assumption
is now explicit throughout this fragment.

For the analytic P07.1 result, convex combinations synchronize finitely
many descending rows on compact domains, by separation and the signed
Riesz representation theorem. A fixed-domain diagonal is obtained before
passing to the sheaf closure. Logarithmic barriers and a regularized
maximum glue the rows while keeping a common core. Truncation handles
minus-infinity values. Positive psh coordinates separately handle
arbitrary star products, without importing analytic realization for a
general affine tropical space.

For the negative P07.1 result, the restricted rational slope vectors are
ell_(j,n)=e_(r_j)-n e_(b_j)-e_(a_(j,n)). The unchanged star G-site and PL
sheaf satisfy the ambient definitions with this smaller affinage.
Each first-stage block uses a single neighbourhood missing the appropriate
r_j tail and explicit smooth approximants with error O(1/n). The weighted
sum has a descending first-stage sequence and hence lies in stage two.
Every ordinary neighbourhood of the node contains a whole block.
Nonnegative full-branch psh slopes and the restricted slope relations
force the relevant block slopes to vanish, contradicting the witness's
nonconstant b_j branch. This is an affine G-tropical obstruction only.

For P03.1, B=C direct-sum uC and A=C direct-sum u(s,v)C verify finiteness
and identify the two-point pinch. The square-cube criterion and base
change establish geometric seminormality and integrality. The envelope
calculation uses a finite USC obstacle, global explicit FS minorants and
a positive curve-point spike after upper regularization. No continuous
obstacle theorem or general envelope classification is inferred.

For P21.3, the Cartier-cut restriction is justified by smooth truncations,
Poincare--Lelong and a local positivity mass bound. Rational-point density
passes from fibres to the whole polydisc. On a full polyannulus the
mixed Hessian coefficients, not only coordinatewise linearity, force
affinity in all annular logarithms. The result's product geometry and
algebraically closed nontrivially valued base remain explicit.

For P12.6, the image of finite restriction includes prime supports, and
the extremum semicontinuity directions are checked separately. The
normal-domain coefficient ideal includes inseparable multiplicity and
does not assume flatness. Density of rational ideal gauges constructs
the continuous positive trace, with its full fibre support and degree.
Normal towers require one common section and compare unnormalized
traces. For singular rings, only dominant normalization branches have
degree traces; vertical branches still have extremum operators. The
conductor equalizer is the exact domain for descent and for intermediate
tower operations. The ideal-generated cone is kept distinct from an
independently geometric psh cone. The cusp example tests the fractional
ideal gauge, and the two surface branches with limiting gauge values
1 and 2 rule out an unrestricted continuous degree trace. Finite-flat
determinants give a separate full-domain construction. The e_i f_i
formula is confined to DVRs; no defect term is silently omitted for an
arbitrary valuation. Raw traces compose, while normalized averages with
unequal component ranks need not. Nonprimary radial changes are defined
only on the positive finite gauge locus.

## Primary-source checks and explicit corrections

The adapted book text, not the preserved originals, contains the following
source clarifications. Primary statements and their hypotheses were read
directly; this list records the exact inputs rather than relying on a
paper's bibliography alone.

* [CLD, 25 July 2025 revision](https://webusers.imj-prg.fr/~antoine.chambert-loir/publications/papers/fdceb-20250725.pdf):
  Sections 3.1.2--3.1.4, 6.1.1--6.1.2 and 6.7.3 for G-sites,
  PL functions, affinages and the arbitrary star; the closure,
  regularized-maximum and curve-test definitions used in Chapter 15;
  12.4.6 and 16.7.3--16.7.4 for pullback and Poincare--Lelong inputs.
* [Ducros, published article](https://www.numdam.org/article/CML_2012__4_4_A3_0.pdf):
  **Theorem 3.2**, replacing the supplied imprecise Theorem A pointer,
  gives the finite tropical presentation on compact strict domains.
* [ILO, Expose VII](https://www.cmls.polytechnique.fr/perso/orgogozo/travaux_de_Gabber/07-uniformisation-locale/uniformisation-faible.pdf):
  Theorem 1.1 gives the ordinary regular alteration cover needed here.
  The book does not attribute an unnecessary prime-to-ell strengthening
  to that theorem. [Expose II](https://www.cmls.polytechnique.fr/perso/orgogozo/travaux_de_Gabber/02-topologies/topologies.pdf),
  Theorem 3.2.1 with ell=1, supplies domination with Zariski local
  factorizations. The consulted author copies are dated 14 November 2016;
  the bibliography identifies the 2014 Asterisque publication.
* [Berkovich 1993](https://www.wisdom.weizmann.ac.il/~vova/IHES_1993_78_etale.pdf),
  Proposition 2.6.9, checks the relative analytification properties.
  [Berkovich 2015](https://www.wisdom.weizmann.ac.il/~vova/IJM_2015_210_formIII.pdf),
  proof of Theorem 1.3.1, checks the excellence and regular-chart route.
* [Temkin, altered local uniformization](https://math.huji.ac.il/~temkin/papers/Altered_Local.pdf),
  Corollary 3.3.2 and Section 3.4, distinguishes the rigid etale covering
  from its Berkovich quasi-etale interpretation.
  [Gerritzen--Grauert](https://math.huji.ac.il/~temkin/papers/Gerritzen_Grauert.pdf),
  **Theorem 3.1**, applies to the required nonstrict affinoid domains.
* [Gubler--Rabinoff, version 2](https://arxiv.org/html/2506.13548v2),
  Definitions 2.16, 4.1 and 7.1, Proposition 7.2(6)--(7), and the whole
  quasi-compact strictly semistable statement cited as Proposition 7.8.
  Its assertion includes the boundary. The supplied archived source
  report corroborates the PDF locator; the statement was also reread
  directly in the current HTML version.
* [de Jong--van der Put](https://emis.de/ft/32614), Proposition 3.2.2,
  checks G-sheaf descent plus finite etale surjective equalizers.
* [Jonsson--Horawa notes](https://www.math.uni-bonn.de/people/horawa/math_715_Berkovich.pdf):
  Theorem 5.4 (factoriality), Theorem 5.18 (Noether normalization), and
  **Corollary 5.19** (Nullstellensatz). The previous vague BGR section
  pointer for normalization is replaced by Theorem 5.18, with the
  bounded-coordinate Tate construction made explicit in the proof.
* [Buttenschoen, Hahn--Banach notes](https://www.buttenschoen.ca/MATH725/build/hahn-banach-9dc0cd2bd68d1ccec7dc89ef1e953f30.pdf),
  Theorem 2.1, and [Schenker's functional analysis notes](https://math.jhu.edu/~js/Math637/functionalanalysis.notes.pdf),
  Theorem 18.1, give closed-convex separation and the compact-Hausdorff
  signed Riesz representation used in convex synchronization. Schenker's
  name and the notes' title were taken from the primary title page.
* Stacks [0BD2](https://stacks.math.columbia.edu/tag/0BD2),
  [00HS](https://stacks.math.columbia.edu/tag/00HS) and
  [0EUL](https://stacks.math.columbia.edu/tag/0EUL) check determinant
  base change, flat going-down and the square-cube seminormality input.
  Earlier Chapter 70 valuation-extension and normalization inputs retain
  their exact existing tags and scopes.

The two preprint-only warnings in the scoped house audit are reviewed:
CLD's author page and the Gubler/Rabinoff publication pages still list
the consulted works as preprints. Their exact revisions are retained.
No publication is invented and strict zero-warning mode is not claimed.

## Supplied evidence and preservation

The 17 original files and their SHA-256 manifest are in
[`author_sources_20260924`](../author_sources_20260924/README.md).
All 31 supplied PDF pages were rendered and visually inspected in addition
to the full text/TeX review. Only the research sources were extracted;
no supplied program or runtime was executed.

The original P06.1 campaign database was opened read-only. The derived
`p061_archived_verification_excerpt.json` records entries 312, 319, 322,
325, 332 and 351, retaining the correctness, source, requirements and
reconstruction reports and their qualifications. Its database hash is
`487eadc9f4310ed87bbb02960e2255fac772242200aa6dfbd59e550843f0fc18`.
These are archived Xean checks of the supplied n87 argument. They neither
verify the later book adaptation nor constitute a new Rethlas receipt.
Claims in other supplied README files are identified as source metadata,
not as independently retrieved verifier records. No quarantined book
packet is promoted and no historical receipt is changed.

The existing Chapter 60--64 sources, P12.1 fragment and original PDF,
CURVE_PSH source, frozen statements/proofs, solver dossiers, verifier
receipts and dated release outputs are retained byte for byte. Only the
explicit integration manifest is delivered. The generated current
`manuscript/book.pdf` remains ignored; no dated release is overwritten.

## Final checks

The full-book build completed after the proof/source passes and the final
layout repairs. The current PDF has **4,040 pages**, **19,244,014 bytes**,
and SHA-256 `c87fde89c6653232f02b53ab1599aecad68346e42ed1aeadfcc5051c8bee726f`.
There are no unresolved references/citations, duplicate labels, rerun
requests, or horizontal/vertical overflows. The 13 inherited PDF destination
warnings from the earlier Chapter 70 manual tags are unchanged from the
baseline. They are not newly introduced or represented as a warning-free
PDF build.

The source closure check passes with **396 inputs and 11,788 unique
labels**, zero missing inputs, zero dangling references and clean
per-file structure. The inventory check passes with the exact 43-atom,
13-environment, (0,3,8,15,17) crosswalk. The six-fragment house audit has
zero errors and two reviewed preprint-version warnings, as explained above.
The inventory checker also passes Python compilation.

The first scoped book review covered 10 pages. The complete addition review
covered printed pages 726--742, 1012--1016, 1357--1368 and 3593--3600,
plus 3663, 3670, 3715, 3733--3734, 3744, 3750 and 3949--3951: 52 pages.
The last scoped recheck covered the five edited proof captions, the
43-atom summary on page 3772 and bibliography pages 3963, 3967,
3969--3970. The corresponding physical PDF page is the printed page plus
68. The surface-obstruction display was split to fit; duplicated proof
caption wording and one resulting line overflow were repaired. Proper
names in the new bibliography titles retain their capitalization.

All 17 supplied-original hashes pass. A boundary-aware credential-pattern
scan of the 32 members of the five source archives found no matches;
no archive member was executed. Against the 4,141 tracked baseline files,
only the 14 listed existing integration files differ; the other 4,127
files are byte-identical, including all frozen mathematical/verifier
records. The source checksum ledger below covers the changed TeX,
bibliography and checker together with the six new fragments; its paths
are relative to the repository root.

Reproduce the source and inventory checks from `manuscript/` with
`python3 editorial/tools/refcheck.py` and
`python3 editorial/tools/check_open_problem_inventory.py`.
Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`.
See [`supplied_solutions_source_sha256_20260924.txt`](supplied_solutions_source_sha256_20260924.txt)
for the checked adaptation bytes. Original-source hashes have their
separate manifest in `author_sources_20260924/SHA256SUMS`.
