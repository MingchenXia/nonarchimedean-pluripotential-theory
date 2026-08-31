# Exact sources, interfaces, and scope ledger

Date: 2026-08-31. Authoring agent: `/root/p082_independent_reaudit`.
Status: author-checked research candidate, not an independent audit or
production acceptance. The parent contributed substantive ideas, as
disclosed in README.md. There is no novelty or priority claim.

## 1. Proposed result and dependency boundary

The unconditional part is an exact weighted-FS extension lemma for a
constant smooth integral projective X over algebraically closed trivial k,
K=k((t)) with |t|=exp(-1), and an ample L defined over k. For a canonical
reference and -M<=f<=0, ANY integer C>=max(1,M) works. The extension is in
the actual fixed line bundle p*L tensor q*O(C), globally between -C and 1,
with normalized weights in [-C,1). It preserves rational weights. An
arbitrary fixed FS reference only adds its fixed upper/lower oscillation
to the bound for C.

The conditional part assumes trivial-field EP on X x P1 in these ample
classes and concludes EP on L_K for the decreasing-FS metric class. This
is precisely the non-identically-minus-infinity part of the metric class
in Boucksom--Eriksson Definition 7.2, written as relative potentials.
The supplied unibranch theorem asserts the required EP input. No theorem
about arbitrary K, nonconstant varieties, all numerical classes on X_K,
or equivalence with CLD/BFJ definitions is part of the conclusion.

## 2. Exact local primary sources

### S0: Actual supplied unibranch-envelope paper

- File: `/Users/mingchen/Projects/Yethlas/bj_envelope_latex_source/bj_envelope.tex`.
- SHA256: `6a075400ead7837a254d7b16eaf5ab6da3d65fa720ac0da272f2958faf20f3bf`.
- Title: *The envelope property for unibranch projective varieties*;
  author field empty in the supplied source.
- Read this turn: abstract, introduction including `thm:intro-main`,
  conventions, `prop:BJ-package`, `prop:EP-criterion`, start of
  `sec:smooth` including `thm:smooth-EP`, finite-normal openness and its
  usc identity, and complete final `thm:main` statement/proof.
- Input: for any integral projective unibranch variety over algebraically
  closed trivial k, in any characteristic and real numerical class, the
  usc regularized supremum of a nonempty globally bounded-above psh
  family is psh. Since X x P1 is smooth and integral, it lies in scope.
- This dossier does not re-audit that entire paper. The bridge theorem
  states the needed EP hypothesis explicitly; it does not silently treat
  continuous-obstacle continuity as the hypothesis. The paper's use of
  open finite maps for usc pullback does not apply directly to a closed
  analytic fibre, so a separate collar proof is supplied here.

### S1: Published BJ22

- Boucksom--Jonsson, *Global pluripotential theory over a trivially valued
  field*, Ann. Fac. Sci. Toulouse (6) 31(3) (2022), 647-836.
- DOI: [10.5802/afst.1705](https://doi.org/10.5802/afst.1705).
- [Publisher page](https://afst.centre-mersenne.org/articles/10.5802/afst.1705/)
  and [publisher PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf).
- Exact local PDF: `/private/tmp/bj22.pdf`, SHA256
  `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.
  Identical local copy: `/Users/mingchen/Projects/Yethlas/tmp/BJ22.pdf`.
- Exact local extracted text: `/private/tmp/bj22.txt`, SHA256
  `0caf7da441e678675b1ec1bc3461cc21e293cee6809fcf8dfdbe1947b5617777`.

Exact interfaces read directly:

| Location in published source | Permitted use here | Scope check |
| --- | --- | --- |
| Section 1.1.2, p. 660 | Compact Hausdorff analytification and topology by regular-function evaluations | Includes semivaluations with proper support |
| Section 1.1.4, p. 662 | Jointly continuous positive-real scaling of valuations | Over the trivially valued field, on S itself |
| Section 1.3, pp. 666-667 | Generic Gauss formula min(v(a_n)+n) | Used only at the generic Gauss point for integrality, not at arbitrary fibre points |
| Remark 1.24, p. 671 | Trivial metric and section norm at most one | Section evaluation at centres, with homogeneous scaling |
| Formula (2.8), p. 679; Definition 2.18 and (2.9), p. 680 | Finite real/rational weighted section systems; tensor powers | Negative weights explicitly allowed; no-common-zero means finite FS |
| Definition 3.8 and Example 3.9, p. 694 | Hdom(L) is a subset of H_Q(L) for a fixed ample Q-line bundle | Not merely approximation in unspecified nearby numerical classes |
| Lemma 4.6, pp. 708-709 | Abstract decreasing-net diagonal closure | Singleton class parameter suffices; no EP assumption |
| Theorem 4.15(iii), p. 713 | A psh function in a fixed ample class decreases from Hdom of that same line bundle | Applicable to bounded ambient envelope on S, any characteristic |
| Definition 5.8, p. 723 | Exact meaning of EP | Distinct from the separate continuous-obstacle issue |

The full cited statements and nearby definitions were read, rather than
only theorem names. The proof of Theorem 4.15 and Example 3.9 were also
checked for the fixed-line-bundle interface.

**Remark 1.9 precision:** the full-image identification in the published
text is not a valid identification of X_K^an with the image of the Gauss
section. The parent inspected the actual local PDF and confirmed that the
sentence is printed, not merely an extraction artifact. This dossier does
not use it. The analytic fibre is obtained from completed residue fields;
the collar acts on the entire fibre. Only the legitimate Gauss valuation
formula enters the coefficient-integrality step.

### S2: Boucksom--Eriksson, exact v3

- *Spaces of norms, determinant of cohomology and Fekete points in
  non-Archimedean geometry*, [arXiv:1805.01016v3](https://arxiv.org/abs/1805.01016v3),
  submitted 8 January 2021, internal date 11 January 2021, 99 pages.
- PDF `/private/tmp/BoucksomEriksson_1805.01016.pdf`, SHA256
  `51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2`.
- Text `/private/tmp/BoucksomEriksson_1805.01016.txt`, SHA256
  `1ab23277bee5b344a371e6d6ca3685ef55bbcaac4848c2febac708948c658286`.
- Section 5.1, pp. 37-38: metrics form an affine space over functions;
  a relative potential is a difference of metric weights, with the sign
  norm_new=norm_reference exp(-potential).
- Definition 5.2, p. 38: over any complete non-Archimedean field, FS uses
  a finite section system without common zeros and arbitrary real weights.
  Proposition 5.4, pp. 38-39: tensor powers, pullback and finite maxima.
- Section 5.3, p. 40: a model metric gives norm one to a local frame on
  the inverse image of its model trivialization; Example 5.9 identifies
  the trivial metric when the field itself is trivial.
- Definition 7.2, p. 48: non-Archimedean psh metrics on a semiample
  Q-line bundle are pointwise decreasing-net limits of FS metrics on that
  same bundle. This is exactly the target definition used here, excluding
  the identically minus-infinity limit.
- Lemma 7.4 and Corollary 7.5, p. 48: abstract decreasing-net closure
  and finite-max stability, with the complete diagonal proof read. These
  do not use an envelope theorem. No claim from its later envelope section
  or its nef/psh comparison is used.

The isolated bibliography deliberately cites this exact preprint version,
so its theorem numbering is unambiguous.

### S3: Temkin analytic fibre interface

- *Introduction to Berkovich analytic spaces*,
  [arXiv:1010.2235v2](https://arxiv.org/abs/1010.2235v2), 16 December 2011.
- PDF `/private/tmp/Temkin_Berkovich_Intro.pdf`, SHA256
  `b8a7ac414e98fdd46db3961c43e08068203aec7225457f455dc077f87b32b914`.
- Text `/private/tmp/Temkin_Berkovich_Intro.txt`, SHA256
  `65e4ba4c4071fd09115f640470ba3b6987cd0a255cd5fe3a0a4d2ddda5ce5980`.
- Fact 4.1.5.1 and Definition/Exercise 4.1.7.1, pp. 26-27: analytic
  fibre products, fibre over a point as base change to its completed
  residue field, and ground-field extension using completed tensor
  products. Section 5.1.1, pp. 33-34: analytification by affine
  semivaluations, gluing, and the universal property.
- Use: F is the full X_K^an, with its usual subspace topology; K is the
  completion of (k(t),ord_0). The proof describes the affine construction.
  No rigid/Berkovich properness theorem or algebraization theorem is used.

An early search also inspected the old arXiv:1801.08229v1 text for
orientation. It is superseded for this packet and is not a dependency.

## 3. Proof checks and genuinely new steps

The sources provide definitions, standard geometry and regularization.
They are not claimed to state the new uniform extension or transfer.

1. **Canonical vs relative metrics.** All truncation uses the constant
   model. For a different reference rho, apply it to rho_K+phi-a, then
   add a back at the metric level. The relative function obtained by
   subtracting p*rho is not falsely declared FS relative to the trivial
   metric.
2. **Integrality.** After absorbing integer weights into powers of t,
   evaluate the normalized finite maximum at the generic Gauss point.
   Finite-dimensional H0 over k and its first nonzero Laurent coefficient
   give the exact lattice V tensor k[[t]]. No arbitrary-point cancellation
   claim, normal-model lattice theorem, or non-Noetherian construction is
   required.
3. **Tail margin.** With D=mC and 0<=alpha_j<1, the weighted tail is at
   most exp(alpha_j-D-1), STRICTLY less than exp(-D), hence strictly below
   the pointwise weighted maximum. The ultrametric normed-line argument
   proves exact preservation at all analytic points, including proper
   support. A rational/real weight denominator never enters C.
4. **Global generation.** The sections q_l U^D and q_l T^D remove every
   common zero on the product. Weight -mC makes their fibre contributions
   invisible. In particular central-fibre base points are not silently
   retained. Unweighted padding would not justify this step.
5. **Boundedness and one class.** Every global k-section has trivial norm
   <=1; the padding maximum has norm exactly one. Thus all extensions are
   between -C and 1 in the SAME ample A, with normalized weight modulus
   <=C. C>=1 ensures A is ample even when M=0.
6. **Collar.** The open region 0<|t|<1 is canonically F x R_{>0} by
   scaling all valuations. This is not the Gauss-section parametrization.
7. **USC.** A uniform estimate
   |Phi_i(ax)-Phi_i(x)|<=2C|a-1| controls nearby-fibre overshoot. The
   neighborhood proof works for arbitrary nets/nonmetrizable spaces.
   Merely restricting a supremum's regularization to a closed fibre
   would give only one inequality. The continuous collar functions
   min(1,n|a-1|) illustrate failure without uniform radial control; they
   are not asserted to be an FS/psh family in one class.
8. **Restriction.** After ambient EP, BJ22 gives decreasing FS
   approximants on the actual A. Restrict their section systems and use
   the norm-one frame U^{mC} for the base factor. This explicitly yields
   decreasing FS approximants on L_K, without assuming a general psh
   restriction theorem.
9. **Bounded psh families.** Individual decreasing FS nets have cofinal
   tails <=1 by compactness and an open-cover argument. The coordinatewise
   product is directed (using choice). The infimum of the resulting
   decreasing psh family equals the fibre regularized supremum because
   every continuous majorant can be met up to any positive epsilon in
   every coordinate. The continuous-majorant identity is proved using
   normality of a compact Hausdorff space. No countable cofinal subset or
   interchange of arbitrary infimum/supremum is asserted.
10. **Unbounded below.** Integer clamps preserve the target class; finite
    max commutes with usc regularization. Nonemptiness supplies a member
    finite somewhere, excluding the identically minus-infinity final limit.

## 4. Remaining boundaries and verification status

The author found no unresolved step in the written constant-case proof,
but it has not yet had independent hostile review or production
verification. All mathematical statements must retain candidate status.
The dependency on the supplied unibranch EP theorem is explicit. The
extension lemma itself does not use that theorem.

General nonconstant families over k(t) would require another argument for
integral section lattices and a uniformly generated relative section
algebra; the finite k-basis argument here does not prove those assertions.
Arbitrary complete fields and all real numerical classes remain outside
scope. No continuous-obstacle continuity conclusion or CLD/BFJ
identification is inferred. The historical p081 dossier name does not
claim to close an additional inventory atom.

The packet is uncompiled, so no PDF visual QA is claimed. The exact TeX
control-byte check, principal/source hashes, and manifest verification
are recorded at freeze. No live book, frozen accepted packet, or earlier
Gauss obstruction file was changed; no production tool was called.
