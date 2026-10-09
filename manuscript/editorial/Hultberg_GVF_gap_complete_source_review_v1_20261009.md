# Complete GVF gap-principle source reading and primary comparison

Read all **43 physical pages** of Nuno Hultberg, *New gap principle for
semiabelian varieties using globally valued fields*,
[arXiv:2601.04972v1](https://arxiv.org/abs/2601.04972v1), 8 January 2026,
in **22 sequential complete-text/image displays**, including every proof
and reference. The 849,391-byte PDF has SHA256
`6c85d6789a7a6f087ad66b7097d531f939d1c354d1a6c24fa289c71a418cb441`.
A fresh primary arXiv check lists only that v1. This authenticates the
version boundary; it does not recursively verify imported results.

The canonical height is the sum of abelian degree-two and toric
degree-one parts on a split semiabelian compactification. Specialness
uses the quotient by the stabilizer, Chow trace and a zero-height
translation over a GVF extension. Such a translation need not be torsion.
The announced reduction assumes abelian BC; the arbitrary positive-
characteristic abelian input remains open in this version. Characteristic
zero uses GGK potential nondegeneracy; elliptic quotient is a separate
claimed all-characteristic case. The intended main BCSA and strict gap
results remain **UNVERIFIED for book import** after this complete audit.

## Exact normalization and boundary diagnostics

1. Theorem 2.3.6 (pp13–14) omits genericity and prints an extra d+1 in
   the mixed-height denominator. Pull a metrized base line of height c
   back to a canonical abelian variety. Every point has height c and the
   projection formula gives L^d M=c deg_L X, while the printed right side
   is c/(d+1). Forty exact dimension/constant samples record this defect.

2. Remark 2.3.3 says a polarization of mass H1...Hd restricts to that
   multiple of the base height. Definition 2.3.5 divides by (d+1)L^d,
   so it restricts to K[1/(d+1)], rather than being a GVF extension of K.
   Direct dimension-two base scaling is 1/3; iterating two dimension-one
   constructions gives 1/4. Unit-mass normalization is needed before
   the asserted transitivity or base extension can be used.

3. Corollary 2.6.11/Theorem 6 lacks a positive-height or additive-error
   qualification. On E times P1 take canonical L_E plus the pullback of
   canonical O(1) shifted by -c. Its geometric Deligne pairing is
   2 deg(L_E) O(1), big. At infinitely many root-of-unity base points,
   fibre height and every torsion-point height are -c. For 0<epsilon<1,
   all those torsion points fall below (1-epsilon)(-c) and are dense.
   No proper closed subset of the base removes all such points. Fifteen
   exact samples calibrate this literal negative-height endpoint.

4. Theorem 4 (p4) uses a non-strict threshold c1 h(G). A constant
   genus-two curve in its Jacobian over a trivial-height algebraically
   closed characteristic-zero GVF has finite stabilizer and generates
   the Jacobian by differences, while all heights and h(G) are zero.
   The printed <=0 includes every point. The strict threshold in
   Conjecture 4.2.3 excludes all points at zero and avoids this test.
   This diagnosis is not a refutation of BCSA or the strict gap principle.

5. Definition 2.4.3 allows arbitrary GVF factors without uniform triangle
   error. For Q with height scaled by i, sequences 1 and 1 have bounded
   height but their sum 2 has height i log2. Thus the bounded-height
   representatives need not form a field. Common-base families, or the
   positive arithmetic-parameter normalization used later, bound ht(2)
   and avoid this specific failure.

6. Lemma 2.6.6 uses <=C parameter-height cutoffs but its proof asserts
   strict <C witnesses; at a closed cutoff, representatives approaching
   from above need not satisfy the same bound. Its reverse implication
   also chooses thresholds with limit <r and concludes an infimum >r.
   Relaxed-cutoff semicontinuity is distinct from exact hard-cutoff
   equality. Lemma 3.2.7 then compares raw powers with normalized minima:
   its omitted geometric denominator grows as N^dim(pi(X)). A bounded
   negative absolute minimum does not force a nonnegative leading raw
   coefficient. These are proof qualifications, not certified refutations
   of the intended mixed-vanishing or continuity statements.

## Primary Sédillot comparison: exactly five pages

Acquire both March v1 and November v2 of arXiv:2303.03377. The current
primary metadata lists v2, 3 November 2023, and only that version has the
quoted Proposition 5.5. V1 has zero actual page credit. Read **physical
pages 37–41 of v2**, five of 43 pages, in three matching displays, including
the section hypotheses and **the entire Proposition 5.5 proof** (39–40).
This is not a whole-Sédillot-paper reading.

The primary proposition assumes a proper adelic curve, perfect countable
base, normal geometrically integral projective X, relatively ample
semipositive L and a generic small sequence. It gives

    lim h_M(x_n) = (L^d M)/vol(L)
                 - d h_L(X) (L^(d-1) M)/vol(L).

At h_L(X)=0 the first term has no extra d+1. Its proof differentiates
chi-volume divided by (d+1) times geometric volume; the derivative's
d+1 cancels. The Hultberg transcription differences are not present in
this primary proposition. Its deeper CM/BB and differentiability proofs
are not recursively cleared. Separately, Sédillot Lemma 5.7's chosen
archimedean shift divides by the archimedean mass; a zero-mass case needs
another admissible nonzero-mean metric shift or a positive-mass hypothesis.
This separate qualification is not an error in Proposition 5.5's coefficient.

## Zero-height extension uniqueness: UNVERIFIED candidate construction

Lemma 5.4.2 (pp33–34) claims that, for an algebraically closed geometric
GVF K, there is a unique GVF structure on K(x) with ht(x)=0. Its proof
passes from a global height identity to a local Gauss-support assertion.
The following adversarial construction is **UNVERIFIED** and has no
independent production-verifier receipt. It remains outside book theorems.

Let k=Qbar with trivial height and K0=k(a,b), endowed with the hyperplane
height from P2_k. For a projective tuple of polynomial representatives,
cancel their common divisor. Its height is the maximum remaining total
degree. Let F_slope=k(x,y)(t), a=t and b=xt+y, with k(x,y) trivial and
the usual degree-in-t GVF structure. Let F_intercept=k(s,x)(t), a=t and
b=st+x, with k(s,x) trivial. Both are the same abstract field K0(x).

A generic line avoids the finite base locus of a tuple after canceling
its common divisor, including the residual locus at infinity. Substitution
has the original maximum degree and no further common factor. Thus each
extension restricts to the hyperplane height on every projective tuple
over K0. Twenty-two exact symbolic tuple checks corroborate this argument;
the finite checks alone are not its universal proof. In both structures
ht(x)=0, but b-xa equals y in the slope structure and (s-x)t+x in the
intercept structure, of heights zero and one respectively.

To address the algebraically closed-base hypothesis, extend each height
symmetrically to the compositum with K=K0alg. Pure transcendence makes
K0(x) linearly disjoint from K over K0. Galois invariance of the symmetric
extension restricts on K to its fixed symmetric height. This produces
two candidate structures on K(x) preserving the displayed discrepancy.
The complete symmetric-extension/normalization argument still needs the
independent review required for an original-result verdict. Locally, the
slope construction has x-b/a=-y/a of positive order at a=infinity although
b/a has order zero, directly testing the printed Gauss-support leap.

Lemma 5.4.3 and the geometric quasi-split proof depend on this uniqueness
claim. No counterexample to those later intended conclusions is claimed.
Other imported qualifications include characteristic-zero Ueno
base-extension inputs, whole-image versus chosen-component relative
Faltings–Zhang statements, Pic0 versus integral numerical torsion, and
meromorphic multisection norms with their actual covering degree.

## Research questions retained with their exact scope

- **General positive-characteristic abelian GVF Bogomolov.** For an
  algebraically closed geometric GVF K of characteristic p, its constant
  field k and an abelian A/K, characterize integral X with dense canonical
  small points, allowing arbitrary GVF extensions, as trace subvariety plus
  abelian subvariety plus zero-height translate. The paper states this
  arbitrary-GVF input is open; classical polarized function-field results
  and the elementary elliptic case are separate known inputs. No October
  2026 global literature-completeness claim is inferred from this January
  version. Its resolution would feed the semiabelian reduction, once that
  reduction's auxiliary dependencies are cleared.

- **GVF model companion.** Conjecture 2.5.6 asks whether existentially
  closed GVFs remain existentially closed under admissible ultraproducts,
  with uniform height-error control, equivalently the stated model-companion
  formulation. Known examples quoted here are Qbar with ordinary height
  and algebraic closure of k(t) with its standard height. Arbitrary GVFs
  are not thereby existentially closed. The foundations primary conjecture
  and any later resolutions remain a further source-checking target.

- **Base-field zero-height translations.** Remark 3.2.4 asks whether a
  special semiabelian X/Stab(X) always admits its zero-height translating
  point over K itself, instead of only a further GVF extension. The source
  reports no counterexample; it does not prove descent. Finite algebraic
  point-attainment and the BGPS candidate are different problems.

- **Repair the uniform arithmetic-family statement.** Identify the
  additional large/positive fibre-height or additive-error hypotheses
  needed for Corollary 2.6.11 with big geometric Deligne pairing and
  fibre semipositivity. The negative constant-shift calibration rules out
  the literal unrestricted formulation; a dynamical quantitative Zhang
  theorem is not a replacement for this more general family question.

- **Replace the uniqueness dependency.** Determine what constancy,
  base-dimension, independence or existential-closedness hypotheses give
  the Gauss-support statement needed in Lemma 5.4.3, or prove its intended
  traceless canonical-function-field conclusion directly. The generic-line
  candidate has not received the required independent verdict. This is a
  research repair target, not a recognized new closed book problem.

## Preserved book and publication scope

This is a source-only audit: the checked **4,679-page** book, its PDF hash,
the native catalogue/editor, 42 canonical atoms/twelve problems and tiers
(0,3,7,15,17) are unchanged. BJ22 homogeneous Siu/envelopes remain OPEN,
LPWZ density UNVERIFIED and P12.2/P12.3 OPEN. No original theorem,
independent production-verifier receipt or new ordered whole-book reading
is claimed. Primary PDFs, full literal source texts, HTML and page images
are excluded from the authored evidence upload. Executed helpers, failure
record, exact calibration, notes and receipts remain frozen. Upload grants
zero reading credit. Continue cloud-only, with Xean suspended.
