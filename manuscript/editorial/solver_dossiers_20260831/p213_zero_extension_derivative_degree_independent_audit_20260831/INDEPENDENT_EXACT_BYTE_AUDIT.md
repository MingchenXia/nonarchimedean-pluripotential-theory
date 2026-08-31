# Independent exact-byte audit: zero extension and derivative degrees

Date: 31 August 2026. Reviewer: /root/p213_skeletal_hostile.

## Verdict and independence

Independent mathematical PASS for the bounded claims of DIAGNOSTIC_NOTE.md, SHA-256 ecded1c81172a2f42c1d2b00acb2663ee6bc06b4a2929c2ea5b1a3eb634d800c. No substantive gap was found in the logarithm counterexample, the sufficient derivative-degree conditions, the positive closed-(0,0) modification correspondence, or the continuous-product proper-pushforward identities.

This is not production acceptance, an official erratum, a theorem about arbitrary-current pullback, a divisor-borderline removability theorem for continuous products, or a solution of P21.3. In particular, equation (9) of the candidate is not certified in the divisor case.

The candidate was authored by /root/p082_independent_reaudit; /root supplied the original punctured-line example. This reviewer did not author the candidate, supply its replacement proof, or edit its frozen inputs. The reviewer has authored other product/torsor and wall research packets, but none is an input to this diagnostic: neither their assertions nor a skeletal representation premise (R) is used in this audit. The parent independently read sources in parallel; that reading does not substitute for the direct checks recorded here.

One qualification concerns the candidate's bounded Chapter 14 commentary, not its mathematical proofs. The live excerpt's phrase “bidimension-(0,0) currents, that is, ... measures” is too broad without positivity or an explicit measure-valued hypothesis. The note's endorsement of the degree distinction must NOT be read as endorsement of that shorthand. Positive bidimension-(0,0) currents are Radon measures; arbitrary currents of this bidimension need not be. The continuous-product proof correctly uses positive-current coefficient measures throughout.

## 1. Exact objects reviewed

The entire candidate note, source ledger, numbered Chapter 14 excerpt, manifest and checksum file were read. Candidate directory:

/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_zero_extension_derivative_degree_diagnostic_20260831

| Frozen object | SHA-256 |
| --- | --- |
| DIAGNOSTIC_NOTE.md | ecded1c81172a2f42c1d2b00acb2663ee6bc06b4a2929c2ea5b1a3eb634d800c |
| SOURCE_LEDGER.md | c231cd12173a71f075f03c9b7e5b36b3e2d546d496551480cc55395cd5d58aaa |
| CH14_REVIEWED_EXCERPTS.txt | 987d0c51ae6f56f7831c97ddae0d51998419c65a2433c38de4ea7620cfd91b4d |
| MANIFEST.json | 0d18ac6d059e0a61672e962be5c4b59f372e0ba148bd4d0096d1024d911dff7c |
| SHA256SUMS | f8e0dd1fc9bf2aaba769849aed02c089c5dd81266e15d867313367596e32c539 |

All nine candidate manifest entries and all ten candidate checksum entries were independently recomputed with zero mismatches. The contemporaneous live Chapter 14 file still has the candidate's pinned hash, and all 216 numbered source lines in the excerpt match exactly. Detailed machine-readable results are preserved in VALIDATION.json.

## 2. Literal conventions, not an inferred intended correction

Candidate lines 17-31 are correct. In CLD Definition 7.1.1, bidimension (r,s) means duality against compact smooth forms of bidegree (r,s). On a pure n-dimensional space the current bidegree is (n-r,n-s). The signed transposes in 7.7.1-7.7.3 therefore lower bidimension:

\[
 d':(r,s)\mapsto(r-1,s),\qquad
 d'':(r,s)\mapsto(r,s-1),\qquad
 d'd'':(r,s)\mapsto(r-1,s-1).
\]

For a current of bidegree (a,b), both first derivatives have transpose sign \((-1)^{a+b+1}\). CLD uses \(J(d'x)=d''x\), \(J(d''x)=-d'x\), not the unnormalized swap convention. Its first derivatives anticommute. These conventions give the positive Poincare--Lelong sign used by the candidate.

The final sentence of printed CLD 7.1.12, p.159, is literally unqualified: after defining zero extension through compactness of the degree-specific wedge support, it asserts commutation with the differential operators. Visual inspection confirms that the missing qualification is not a text-extraction accident. The reviewer does not attribute an unpublished correction or an intended interpretation to the authors.

CLD 7.1.13, pp.159-160, is a distinct fixed-bidimension statement. Its support proof is valid: the ambient tests of degree (r,s) already have support inside U under the pointwise bound. The complementary indices in one displayed test-space line of its printed proof are inconsistent with Definition 7.1.1 and the preceding sentence; the candidate explicitly records rather than exploits this issue.

Restriction of a current to an ordinary open subset does commute with derivatives. Here the zero extension being differentiated is that of a compactly supported TEST FORM. Its support stays inside the open subset and all derivatives remain compact tests. This fact supplies no commutation theorem for the extension of an arbitrary current.

## 3. The logarithm counterexample survives all degree and sign checks

Candidate lines 35-65 use the smooth boundaryless analytic affine line and its punctured open subset. At the removed K-rational point 0, \(d_K(0)=d_{\rm trop}(0)=0\).

On the punctured line, \(S_U=[\log|z|]\) has current bidegree (0,0), bidimension (1,1). The analytic unit z gives an affine tropical logarithm, so \(d'd''S_U=0\). The boundaryless form-to-current identities in CLD 7.7 and Lemma 16.7.4 justify this at the current level.

Every compact ambient (1,1)-test avoids an ordinary neighbourhood of 0, by CLD 15.2.1(b). Thus the original extension condition in 7.1.12 holds, and the fixed-degree theorem makes the extension unique. CLD 16.7.2 explicitly defines its logarithm current by this extension. There is no alternative choice of logarithm distribution being smuggled into the example.

For the regular coordinate z, \({\rm div}(z)=[0]\), and CLD 16.7.3 gives

\[
 d'd''[\log|z|]=\delta_0.
\]

The point has multiplicity and residue degree one. Thus the right side evaluates a scalar test \(\rho\) as \(\rho(0)\), with positive sign, and a compact smooth cutoff equal to one near 0 detects its nonzero value. In contrast, the zero current \(d'd''S_U\) extends to zero. This directly refutes the unqualified differential-commutation sentence while preserving fixed-degree extension.

The first-derivative version is also correct. With \(Q_U=d''S_U\), its bidimension is (1,0), so it extends uniquely. Restriction commutation plus uniqueness, not extension commutation, identifies \(Q_X=d''S_X\). Then \(d'Q_U=0\) but \(d'Q_X=\delta_0\). The corresponding \(d''d'\) defect is \(-\delta_0\). Thus merely requiring both the input and its derivative to admit extension does not repair the sentence.

The example does not satisfy separate d'- and d''-closedness on U. It also does not extend as a finite continuous function at 0. It is therefore not a counterexample to either the positive closed-(0,0) modification result below or an independently hypothesized continuous-potential theorem. No such inference is made in the candidate.

## 4. Degree-qualified and proper-support commutation

The table in candidate lines 69-86 is correct. For an operator D, the displayed bound is imposed in its OUTPUT bidimension. It implies the input bound, supplies extensions, and makes restriction injective on the difference
\(D(j_!S)-j_!(DS)\). That difference restricts to zero because ordinary restriction commutes with D. The proof never differentiates the disputed formula.

For \(d'd''\), the bound with \(\max(r-1,s-1)\) also supplies each intermediate first-derivative degree. If an index is negative, the corresponding differential component is zero by the dimension conventions; the table is only asserted for meaningful derivatives. These bounds are sufficient conditions, not necessary conditions for an individual current.

The separate proper-support condition in line 88 is also valid. For an open inclusion j, every compact set in X meeting supp(S) compactly in U is precisely the support-properness condition used in CLD 7.1.11. On each test pairing, a compact smooth cutoff in U can be chosen equal to one near the compact support intersection. Its derivative terms miss supp(S). Since differentiation does not enlarge a test's support, the same construction proves all stated commutations by signed transposition. This is stronger than the original degree-specific extension condition; the punctured logarithm lacks it.

## 5. Modification correspondence does not assume a general pullback

Candidate lines 92-106 retain the needed hypotheses: pi is proper, both spaces are good separated boundaryless and pure n-dimensional, n is positive, E and Z are closed analytic subsets of dimension less than n, and the complements are genuinely analytically isomorphic. No component lying entirely in E is allowed.

Starting from a current of bidegree (0,0), restriction, actual-isomorphism transport and unique extension all take place in bidimension (n,n). Positivity is preserved: every compact positive top test on Y has compact support disjoint from E, and its transported test is positive and compact on the isomorphic open subset. Its zero extension as a TEST FORM to X is legitimate.

Closedness is established separately in the two first-derivative degrees. The derivatives of \(T_Y\) are supported in E and have bidimensions (n-1,n) and (n,n-1). In each case the maximum is n, so the analytic dimension bound forces the derivative current to be zero. This remains true for n=1, when the degrees are (0,1) and (1,0). It is not an assertion that bidimension-(0,0) point masses vanish.

Proper pushforward preserves positivity and closedness. Outside Z, \(\pi_*T_Y\) equals \(T_X\); fixed-degree injectivity in bidimension (n,n) makes them equal globally. In the reverse direction the transported extension and the starting current on Y agree off E, so uniqueness recovers that starting current. This proves the stated bijection of positive closed cones.

This is a special correspondence built from a genuine isomorphism away from lower-dimensional analytic sets. It constructs no unrestricted pullback along arbitrary analytic maps, and it establishes no scalar rigidity.

## 6. Continuous products and the projection formula

Candidate lines 110-134 are correct in their stated global scope.

Positivity of T supplies the Radon coefficient measures of CLD 7.2.11. For a finite continuous u, CLD 7.2.12 defines uT by integrating u against these coefficient measures. The function need not be globally bounded: each compact test restricts the calculation to a compact set on which u is bounded. The product need not remain positive or closed.

For a compact top test alpha on X, properness makes \(\pi^*\alpha\) compact on Y. Testing the coefficient measures against a compact smooth scalar rho yields

\[
 \langle T_Y,(\rho\circ\pi)\pi^*\alpha\rangle
 =\langle\pi_*T_Y,\rho\alpha\rangle
 =\langle T_X,\rho\alpha\rangle.
\]

The pulled-back scalar test and top form are actual smooth pullbacks; there is no pullback of a current here. Smooth scalar density (CLD 15.2.7), together with compact-support coefficient measures, upgrades this to equality of signed Radon measures. The decomposition of a compact symmetric form into two compact positive forms is available by CLD 6.5.2 in this good analytic setting. Antisymmetric terms are invisible to a symmetric positive current; CLD's normalized J fixes top-degree forms. Thus the passage to signed coefficients introduces no sign or positivity assumption on alpha.

Integrating u against that equality proves

\[
 \pi_*((u\circ\pi)T_Y)=uT_X.
\]

If desired, one inserts a compact smooth scalar cutoff equal to one near the compact measure support before evaluating u; no compact support of u itself is required. Proper pushforward commutes with each signed-transpose derivative, hence

\[
 \pi_*d'd''((u\circ\pi)T_Y)=d'd''(uT_X).
\]

This second equality differentiates already-defined GLOBAL products and then uses proper pushforward. It is not proved by differentiating a zero extension.

The candidate correctly refuses to infer its equation (9). Its output bidimension is (n-1,n-1); the dimension-only uniqueness argument applies when \(\dim Z<n-1\), but not to a possibly divisorial Z. The existence of the restricted derivative's zero extension and disappearance of an exceptional residual current then require an additional argument. This audit makes no claim that finite continuity is insufficient, only that this packet does not analyze it as such an argument. The noncontinuous logarithm does not resolve that separate question.

## 7. Chapter 14 diagnosis and the dimension firewall

The source excerpt is exact, and the candidate's principal editorial distinction is warranted.

1. Lines 389-423 give fixed-bidimension extension, not the unqualified differential-commutation sentence. The directly relevant sources are CLD 3.3.6/7.1.13 and, for analytic subsets, 15.2.1(b). Chapter 12's cited proposition is a tropical-image dimension bound for an analytic cycle; it is not itself the required ambient-support statement. No broad audit or rejection of that Chapter 12 proposition is included.

2. The rigid-point degree distinction at lines 425-457 is compatible with the logarithm example. The proof does not incorrectly make the entire rigid locus a closed analytic set. However, the shorthand “currents, that is, ... measures” at line 453 must be restricted to positive/measure-valued bidimension-(0,0) currents. This reviewer does not endorse it for arbitrary currents, and the present projection-formula proof does not need it.

3. The later proposition at lines 2196-2207 is phrased using INTRINSIC local tropical dimension of Z and concludes only pullback vanishing. The candidate explicitly does not prove an equivalence between that intrinsic hypothesis and an ambient pointwise tropical-dimension hypothesis. This audit likewise does not supply such an equivalence.

4. Abstract pullback vanishing alone is weaker than ambient support avoidance. Under the additional CLOSED ANALYTIC dimension bound \(\dim Z<\max(r,s)\), CLD 15.2.1(b) directly proves the stronger ambient support avoidance. Consequently the form vanishes on an ordinary neighbourhood of Z, and fixed-bidimension extension is unique. These statements follow from the actual support theorem, not from replacing intrinsic dimension with ambient dimension without proof.

5. The later support theorem and proper-pushforward calculus have the appropriate safe hypotheses for the uses made here. This is not an audit of every current operation in Chapter 14 or elsewhere. In particular, a downstream argument requiring equation (9) must be examined separately.

## 8. Verification boundary

The PDF skill was used for read-only source verification. The reviewer independently viewed the already-rendered full source pages 159, 160, 423 and 460, and read the additional precise text passages listed in SOURCE_RECHECK.md. No PDF was authored or edited, and no TeX/PDF compilation is claimed.

No candidate amendment is required for the bounded mathematical claims. The Chapter 14 measure shorthand qualification above is recorded separately from those claims. This audit does not modify the candidate, the live chapters, any older audit or any production gate. No git or production action was performed.

