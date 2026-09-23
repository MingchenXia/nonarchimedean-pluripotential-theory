# Chapter 60: simultaneous mixed-energy slopes

Date: 24 September 2026.
Baseline: `051492f62ffcc86e98de34771d4eaad59a959016`.
Scope: the opening of Section 60.7 through equation (60.25), before the
reduced entropy definition. Earlier Chapter 60 text and the reduced
entropy definition onward retain their baseline bytes. This is a proof
and source audit of an existing theorem, not a research-frontier closure.

## Normalization and the simultaneous limit

The two-point quantity is now defined by
J(u,v)=E(u)-E(v)+integral(v-u) MA(u), with probability-normalized energy
and measure. It is distinguished typographically from the one-point
J(u)=J(0,u). Translation in either argument cancels exactly between the
energy and integral terms. For u<=v, the energy cocycle and positivity of
each mixed measure prove 0<=J(u,v)<=n(E(v)-E(u))=n d1(u,v).
This supplies the precise invariant used after subtracting the two
different averages. No separate-translation invariance of d1 is asserted.

The translation formula for the unnormalized mixed pairing retains, in
every slot, the signed cohomological coefficient integral(product of the
other n forms). Stokes and finite-energy approximation give this mass;
constant translations in other slots leave it unchanged. The formula
also explains the absence of cross terms involving two constants.

The average slope for a maximal ray starting at zero is recovered from
the preceding cutoff identity sup U_s=s phi(v_triv), together with the
cited compactness bound for normalized complex psh potentials. It does
not depend on the mixed-slope theorem under proof. The already imported
affine energy identity is also used independently of that theorem.

All n+1 finite-energy slots are now regularized simultaneously in a common
Kähler background. The maximum energy gap delta_m tends to zero, as do
the trivial-valuation gaps epsilon_(i,m). Ordered ray distances are at
most s delta_m. The one-point J values of both tuples are bounded by
s(c_(i,1)-E(phi_i)), uniformly in m. The normalized tuple estimate with
exponent 2^(-n) therefore has a constant independent of m and s. Restoring
the averages gives the sum of their absolute cohomological coefficients
times the corresponding average gaps. After division by s the error is
bounded in limsup by C delta_m^(2^(-n))+sum |C_i| epsilon_(i,m), which
tends to zero. Model slopes and decreasing continuity of the finite
non-Archimedean pairing then close the triangle inequality.

For arbitrary smooth signed background forms, the exact pair identity
(eta,U)=(omega,U)+(eta-omega,0) is followed by an explicit decomposition
of the zero-potential term into two Kähler-background terms, with a fixed
large A. The continuity theorem is thus used only on its stated domain.
Fixed maximal model slots may be left unapproximated. The all-finite-energy
case is explicitly included by the empty-PL-block convention k=-1.

The dimension-zero case is treated separately: a connected space is one
point, the two-point J quantity vanishes, and the mixed slope is the
affine coefficient of the sole potential. No positive-dimensional
Hölder estimate is needed there.

The curve example with backgrounds lambda omega and omega and constant
rays as, bs gives slope V(a+lambda b). Its centered pairing vanishes.
It tests the volume factor, the signed coefficient, and the necessity of
restoring averages. The same example has J(0,bs)=0 but d1(0,bs)=bs for
b>0, directly testing the distinction between the two quantities.

## Sources and imported boundaries

The [exact MP author version](https://arxiv.org/html/2409.06221v2),
18 September 2025, was checked at Lemmas 5.3.1 and 5.3.2, Remark 5.3.3,
and Theorem 5.3.4, printed pp. 48–50. Those three pages of the local PDF
were rendered and visually inspected. Its SHA-256 remains
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
The checked estimate is for a whole normalized tuple and uses two-point
J. The present proof restores the cohomological coefficients and expands
the simultaneous approximation step that the source leaves implicit.

The [published BJ author offprint](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BJ_synthetic.pdf)
was checked through indexed primary-source text: Proposition 2.2 and its
proof, pp. 177–178, fix the two-point J orientation; Theorem 3.6, p. 190,
gives the normalized Hölder estimate in the smooth domain. The extension
used here is cited separately to MP Lemma 5.3.2. Direct full-PDF web
retrieval timed out or failed; no new local BJ PDF checksum or visual
source-page inspection is claimed. The compactness constant is cited to
the checked MP Lemma 5.3.1 and Remark 5.3.3, rather than assigning an
unchecked published locator to its extension.

The existing bibliography records the published MP article, Advances in
Mathematics 481 (2025), 110543, DOI 10.1016/j.aim.2025.110543, and the
published BJ chapter, Contemporary Mathematics 810 (2025), 159–208,
DOI 10.1090/conm/810/16207. Publisher full-text access for MP was not
available, so the checked locators explicitly use MPTropicalV2. The
single reviewed house-audit warning about that version-specific key is
not a claim that MP is unpublished. No bibliography file is changed.

The full PL theorem, the compatible model-ray slope input (including
maximal model representatives), the analytic normalized mixed estimate,
general initial values, maximal-ray existence and sequential model
regularization remain explicitly imported. The reconstructed argument
proves the simultaneous limit in the common-background, zero-initial-value
sector. It does not claim to reconstruct the general PL decomposition,
or to show that every PL potential is an unscaled difference of two model
potentials in one fixed positive class.

## Two passes and validation

The first complete proof/source/notation pass produced a full build of
3,985 pages and 18,967,600 bytes. Physical pages 3376–3380 were rendered
and inspected. A 3.37259pt horizontal overflow came from the proof heading
and opening citation. The second complete pass shortened that heading,
made tuple variables and constants explicit, restricted the compactness
display to the finite-energy domain actually used, checked the published
smooth estimate, supplied the fixed Kähler-background decomposition, and
restricted the zero-error observation to maximal model slots. Prose
paragraphs now use structural rather than fixed-column source breaks.
The second full build had no overflow. One accent-escape copyedit was
then made in the new decomposition paragraph and the entire book rebuilt.

Final full build: **3,985 pages, 18,968,072 bytes**. Physical pages
3376–3380 were rendered and inspected in full, covering the revised block
and its following boundary. This is a scoped visual review.

- Input/reference check: 390 TeX files, 11,652 unique labels; no missing
  input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply defined label,
  rerun request or horizontal/vertical overflow. Existing class and
  underfull warnings remain.
- Scoped strict house audit: zero errors and one reviewed exact-version
  warning about MPTropicalV2; exit status 1, not a warning-free strict pass.
  The normal scoped audit exits successfully with that reviewed warning.
- Inventory: PASS, 45 active atoms across 14 formal environments, tiers
  (0,5,8,15,17).
- Surrounding Chapter 60 source is byte-identical to the baseline.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`e54b0d52b110114a3301007ce625f1bde80969fafe1f01c257972d1fd8af0b3c`.
Final live PDF SHA-256:
`e42d6e362a96400f8b140994a4ef286e130d4273384ecbe0f626807abdfa758d`.

The preserved P12.1 fragment has SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The supplied CURVE_PSH.tex retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

The 45 active research atoms, P12.1 integration and provenance, P12.2–P12.6
residuals, supplied originals, bibliography, frozen packets, verifier
receipts and dated release artifacts are preserved. This record is a local
proof/source/build audit; no independent-agent or production-verifier pass
is claimed. The live PDF remains an ignored build product.
Next work is the reduced entropy/Mabuchi slope argument and the scope of
its stability application, preserving the established normalization warning.
