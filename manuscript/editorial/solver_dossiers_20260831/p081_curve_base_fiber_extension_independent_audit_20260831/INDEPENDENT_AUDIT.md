# Independent mathematical audit: nonconstant curve-base extension

Date: 31 August 2026.
Reviewer: /root/p081_weighted_repair_fresh.
Authoring provenance of the reviewed packet: /root and /root/p082_independent_reaudit.

## Verdict and exact object

No substantive mathematical gap was found in the frozen statement and proof,
within their stated hypotheses and relative to the explicitly external ambient
BJ envelope-property input. This is an independent mathematical audit of this
bridge, NOT production verification, permission to integrate, or a verification
of the supplied unibranch-envelope proof.

Reviewed directory:
../p081_curve_base_fiber_extension_research_20260831/

Exact principal hashes:

| File | SHA256 |
| --- | --- |
| statement.tex | 6122b495f877fc78c861a99a3a29ce06d015ac3c9d27de982f7526fd245aace4 |
| proof.tex | 96434222904dd0d66b60b67a2cf32230789f0cff139aac0d784be5bf382ca77e |
| SHA256SUMS | a70a097b770c5077a9c42fa8215b3dd2f2921ff4b7858a900ea4e90e0eb4d7e0 |

All 15 entries of the supplied SHA256SUMS were independently checked, including
the six packet files, seven local primary-source files and both constant-case
predecessor principal files. All match. I read all 109 statement lines and all
392 proof lines, plus README.md, SOURCE_LEDGER.md, CHECKS.md and references.bib.

I did not author this nonconstant packet. My earlier independent audit of the
constant packet is a predecessor, not an assumed proof of the new algebraic
steps. Normal completion, the integral unit ball, relative generation and the
graph/Serre arrangement were independently checked here.

The conclusions separate as follows:

1. The exact FS extension is unconditional under the displayed normal-family,
   ample actual line-bundle and relative-generation hypotheses.
2. The envelope transfer is conditional on ambient BJ EP for the stated actual
   ample bundles B_C on the normal projective S.
3. The arrangement proposition supplies those algebraic hypotheses for a power of
   any ample polarization already defined on a smooth geometrically integral
   projective variety over k(t); positive tensor scaling returns the metric
   conclusion to the original polarization.

The scope is algebraically closed trivial k in arbitrary characteristic,
F_0=k(t), R_0=k[t]_(t), R=k[[t]], K=k((t)), with |t|=exp(-1).
It is not an algebraization theorem for arbitrary K-varieties.

## 1. Completion and the normal integral model — proof lines 3–20

The flatness argument is valid at every point of the regular base curve: a
dominant map from integral S injects the local base DVR into each local domain,
so these local rings are torsion-free base modules. Flatness follows from
[Stacks 0539](https://stacks.math.columbia.edu/tag/0539).
Flatness and projectivity survive the indicated base change.

R_0 is excellent: fields are excellent, and localization of a finite-type algebra
preserves excellence. An excellent local ring is a G-ring, so its completion map
is regular. The exact statements are
[07QS](https://stacks.math.columbia.edu/tag/07QS) and
[07GH](https://stacks.math.columbia.edu/tag/07GH).
The use of [07C1](https://stacks.math.columbia.edu/tag/07C1) is correctly restricted
to finite-type affine charts over R_0. Those charts and their R-base changes
are Noetherian. Their base-change maps are flat with regular, hence normal,
fibres, and [0C22](https://stacks.math.columbia.edu/tag/0C22) gives normality from
the already normal localized S chart. No assertion that an arbitrary completion
of an arbitrary normal ring is normal is needed.

Geometric integrality of Y ensures that Y_K is integral. On any nonempty affine
chart of the flat completed model, t is a nonzerodivisor, so localization at t is
injective and nonzero. The localization is the coordinate ring of an affine open
of integral Y_K, hence a domain; the original chart is therefore a domain.
All these generic opens intersect, so the whole completed model is integral.
This justifies the single function field and rational-section language later.

## 2. The exact unit ball with nonreduced special fibre — lines 22–59

The forward inclusion uses the valuative centre on the proper R-model and a
norm-one local frame. This works for every analytic point, including points
whose support is a proper generic-fibre subvariety.

For the converse, a generic-fibre section is a rational section on the integral
model. Horizontal height-one points lie in the generic fibre, where the section
is already regular. A vertical height-one point gives a DVR by normality.
With b_E=ord_E(t), the normalized valuation ord_E/b_E restricts to the prescribed
valuation on all of K: each nonzero Laurent series is t^n times a unit of R, and
that unit remains a unit in the height-one local ring. The associated
Berkovich point therefore lies in the FULL analytic fibre. In a model frame,
the norm is exp(-ord_E(s)/b_E), so the sup bound forces nonnegative order.

On each affine trivialization every height-one test is now nonnegative.
[Stacks 031T(2)](https://stacks.math.columbia.edu/tag/031T) applies to its
Noetherian normal domain and makes the rational coefficient regular. These
sections glue. There is no omitted higher-codimension pole condition.

BE Example 4.11 and Section 5.3 support the model point/frame interfaces.
The proof correctly avoids the stronger and generally false discrete-case
inference that normality forces equality of the entire lattice and sup norms.
BE Theorem 4.19 distinguishes that equality from integral closure. Equality of
their unit balls here is independently proved by the height-one test; special
fibre reducedness is never assumed, and b_E is never suppressed.

## 3. Flat H0 base change and integral monomial coefficients — lines 61–86

The base change is R_0 to its flat completion R, NOT to its residue field.
Projectivity gives the quasi-compact/quasi-separated hypothesis of
[Stacks 02KH](https://stacks.math.columbia.edu/tag/02KH). The stalk notation
(E_m)_0 is correctly an R_0-module. Localization first identifies the stalk
with generic-neighbourhood sections; flat H0 base change gives the displayed
tensor formula.

A finite generating system of E_1 gives a finite free-module surjection onto it.
Symmetric powers and the ASSUMED surjections Sym^m E_1 -> E_m give generation by
degree-m monomials. Tensoring with R preserves the surjection; thus arbitrary
integral sections admit coefficients in R. Uniqueness is unnecessary.

The additional generation of A, not just of E_1, is explicitly present.
At every centre one generator is a unit in a local frame. Thus the maximum of
the generator norms is one, for both the trivial metric on S and the restricted
model metric. Frame compatibility proves that these two references agree on
the fibre. This is essential to both the tail bound and the later restriction.

## 4. Exact truncation, global padding and one fixed twist — lines 88–165

The weight decomposition lambda_j=n_j+alpha_j, 0<=alpha_j<1, has the correct sign:
a_j=t^(-n_j)s_j converts exp(lambda_j)|s_j| into exp(alpha_j)|a_j|.
The upper bound f<=0 puts every a_j in the integral unit ball.

With D=mC, the weighted tail is at most exp(alpha_j-D-1), strictly smaller than
exp(-D), and hence strictly smaller than the positive maximum exp(mf).
This strictness holds even when C=M and even when alpha_j approaches one.
The finite ultrametric maximum argument is pointwise in the normed residue-field
line; it does not assume independent leading monomials or absence of cancellation.
Proper-support points are included because at least one term of the original
basepoint-free FS presentation is nonzero there.

Homogenized sections all belong to B_C^m with the SAME C. The two padding
systems q^nu U^D and q^nu T^D alone have no common zero anywhere on S.
Their negative weights make them invisible to the fibre maximum, while they
remove base loci at zero, other finite base points and infinity. Arbitrary
Laurent-series coefficients of the original sections cause no extra twist:
only the bounded-degree retained coefficients are homogenized.

The global bounds follow from trivial norms of global sections and from the
unweighted padding maximum being one. Normalized weights are -C or alpha_j/m,
so their absolute values are uniformly bounded by C. Rational input weights
remain rational. A tensor product of an ample bundle with a globally generated
bundle is ample; the product-embedding/Segre proof supplied here verifies this
for B_C without any family-specific extra hypothesis.

## 5. Full analytic fibre, collar and usc transport — lines 168–215

Temkin Definition/Exercise 4.1.7.1 and Section 5.1.1 give the completed-residue-field
fibre interface. Here H(eta)=K. The affine seminorm extension/restriction argument
identifies that entire fibre with Y_K^an; compactness of the projective source
and Hausdorffness of the target give the stated subspace homeomorphism.
No Gauss-section image is substituted.

On 0<|t|<1, a polynomial over trivial k has a unique dominant lowest term.
Thus the base seminorm is exactly a ord_0 for a=-log|t|>0.
Positive scaling and its inverse produce the displayed collar homeomorphism.
This depends on S being over trivial k, not on the family S/P1 being constant.
The relevant joint continuity is the actual BJ22 Section 1.1.4 scaling action.

BJ22 Remark 1.24 gives homogeneity of section norms under scaling with unchanged
centre. Comparing maxima with normalized weights bounded by C gives the first
radial estimate; |f_i|<=M<=C gives the second. The bound is uniform in ALL
family indices and presentations. Taking suprema preserves it.

The neighbourhood argument proves the difficult ambient-star upper bound; the
fibre inclusion gives the opposite bound. It uses a genuine open collar
neighbourhood, not merely a closed-fibre inclusion. Its validity does not depend
on sequences or metrizability. The topological counterexample is correctly
labelled as a warning, not a claimed fixed-class FS counterexample.

## 6. Fixed-bundle regularization and explicit restriction — lines 217–232

I checked BJ22 Definition 2.18, Example 3.9 and Theorem 4.15(iii), including the
latter proof. Since B_C is ample, Hdom(c1(B_C)) lies in H(B_C)=H_Q(B_C) for the
actual Q-line-bundle class, and these representations can be taken in powers
of the fixed honest bundle B_C. The proof does NOT use the varying-class
approximants of parts (i)–(ii) as if their restrictions were fixed-L metrics.

Each globally generating section system remains generating after the algebraic
base change to X. The base factor is trivialized by U^(mC), of norm one on the
fibre. Together with the reference agreement checked above, this gives literal
FS potentials on the fixed L. Their decreasing limit is the fibre envelope by
the already proved usc identity. No general singular-psh restriction theorem
over K or comparison with another psh definition is imported.

## 7. Closure, product nets and removal of the lower bound — lines 234–301

BE Definition 7.2 is exactly the chosen target class, apart from the explicitly
excluded identically-minus-infinity function. BE Proposition 5.4(iii),(vi),
Lemma 7.4 and Corollary 7.5 provide the stated tensor, maximum and decreasing-net
closure facts without an envelope-property assumption.

The recalled compact diagonal argument has a strict positive constant margin,
so it genuinely produces a directed approximating set. Finite maxima are maxima
of FS presentations after common tensor powers; this is not a claim about
maxima of actual real vertical-divisor model functions.

For bounded psh inputs, compactness provides each cofinal tail bounded above
by one, while the lower bound persists automatically. The product of the
directed sets is directed with ordinary choice. The bounded-FS theorem applies
after subtracting one, with a common bound and twist for all coordinates.
The resulting usc envelopes form a decreasing bounded psh net.

For every continuous majorant v of the raw supremum, compactness separately
chooses each coordinate below v+epsilon. Thus the infimum of these envelopes
lies below every continuous majorant. The compact-Hausdorff majorant formula
is proved with a normal-space bump function, and identifies this infimum with
the required usc regularization. This is not an unsupported inf-sup interchange.

Finally, finite maxima with constants give the clamps. Supremum and usc
regularization commute with the fixed lower clamp; the clamped envelopes
decrease to the desired envelope. Nonemptiness and one nontrivial family member
ensure that this final limit is not identically minus infinity.

## 8. Arranging the family and descending the tensor power — lines 305–392

The scheme-theoretic projective closure of the given embedded Y is integral.
Finite-type k-schemes are Nagata, and
[Stacks 035S](https://stacks.math.columbia.edu/tag/035S) makes its normalization
finite. Normalization commutes with localization; smooth Y is normal, so the
generic fibre is still the original Y. The finite normalization is surjective,
and [Stacks 0B5V](https://stacks.math.columbia.edu/tag/0B5V) applies to the ample
restricted Segre bundle over the Noetherian field k.

After a very ample power, the graph of pi in P^r x P1 is a closed immersion with
B the restriction of O(1,0). On each affine base chart, P^r over the Noetherian
chart ring is proper and O(1) is ample. The coherent graph ideal therefore
satisfies [Stacks 0B5T(4)](https://stacks.math.columbia.edu/tag/0B5T).
One threshold for the two charts gives the polynomial-system surjection in
EVERY degree n>=n0, as a sheaf map.

For d>=max(1,n0), degree-md monomials are products of m degree-d monomials.
This grouping works in arbitrary characteristic and needs no division by
factorials. It proves Sym^m E_1 -> E_m is onto for every m, not only for large
m. The chosen A is very ample, E_1 globally generated, and combining global
systems supplies generators of both E_1 and A.

The factor N=nr_0d is correct. Dividing the model reference by N is an FS metric
on L_0,K using the A-generators in degree N. BE Proposition 5.4(iii) identifies
the full FS and decreasing-FS metric classes under multiplication by N.
Positive scaling commutes with supremum and usc regularization. A continuous
reference change subtracts the same continuous function and commutes with the
star operation. Thus the conditional conclusion is about metrics on L_0,K,
not only metrics on the chosen tensor power.

## Source record and remaining gates

The exact local BE v3, BJ22 published text, Temkin v2 and supplied EP source
hashes are retained in the reviewed SHA256SUMS and rechecked by check_packet.mjs.
The supplied EP introduction and final theorem statements were read only to
check the signature. Its full proof was deliberately NOT audited here.

All ten Stacks stable-tag statements were directly opened on 31 August 2026;
their relevant hypotheses and applications are recorded above. No hash of
remote HTML content is claimed. Bibliographic links:
[BJ22 publisher](https://afst.centre-mersenne.org/articles/10.5802/afst.1705/),
[BE exact v3](https://arxiv.org/abs/1805.01016v3),
[Temkin exact v2](https://arxiv.org/abs/1010.2235v2).

There is no unresolved mathematical gap identified in this bridge's written
scope. The ambient unibranch EP remains an external conditional input, and
production review remains gated. Nothing here establishes arbitrary-field
descent, arbitrary K-equation algebraization, real numerical-class transfer,
CLD/BFJ comparison, or continuity of envelopes for continuous obstacles.

No candidate, live manuscript, predecessor or production state was changed.
No PDF was produced, and no compilation or visual-QA claim is made by this audit.
