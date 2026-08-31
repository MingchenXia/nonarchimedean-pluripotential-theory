# Source interface for the irrational Tate-period packet

Date: 2026-08-31. Status: source-checked proof candidate; independent mathematical audit and strict production verification are still required. This file does not report a verifier verdict.

The exact claim is in `statement.tex` and its proof is in `proof.tex`. The claim concerns the **uniform closure of nef Q-formal metrics on one fixed algebraic line bundle**. It does not concern an enlarged cone allowing varying line bundles or ample perturbations.

## 1. Source versions

| Abbreviation | Primary source and copy used |
|---|---|
| Tate95 | John Tate, *A review of non-archimedean elliptic functions*, original 1959 argument published in the 1995 proceedings, pp. 162–184. Author article: [University of Texas copy](https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf), also [Harvard copy](https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf). Downloaded Texas copy is `sources/Tate_review_nonarchimedean_elliptic_functions.pdf`; local pagination 1–24. |
| BPR14 | M. Baker, S. Payne, J. Rabinoff, *On the structure of nonarchimedean analytic curves*, arXiv:1404.0279v1, 2014-04-01. Supplied copies `/private/tmp/BPR14040279.pdf` and `/private/tmp/BPR14040279.txt`. |
| GM19 | W. Gubler, F. Martin, *On Zhang's semipositive metrics*, Documenta Math. 24 (2019), 331–372; supplied arXiv:1608.08030 PDF `/private/tmp/GM1608.08030.pdf` and text `/private/tmp/GM1608.08030.txt`. Proposition numbers cited below refer to that supplied version. |
| GJKM19 | W. Gubler, P. Jell, K. Künnemann, F. Martin, *Continuity of plurisubharmonic envelopes in non-Archimedean geometry and test ideals*, Ann. Inst. Fourier 69 (2019), 2331–2376. [Official publisher PDF](https://aif.centre-mersenne.org/item/10.5802/aif.3296.pdf), downloaded as `sources/GJKM_published_2019.pdf`. Supplied arXiv v3 `/private/tmp/GJKuM1712.00980.pdf` was checked as well. |
| CLD25 | A. Chambert-Loir, A. Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, supplied 608-page PDF `/private/tmp/CLD25.pdf`, with text `/private/tmp/CLD25_20260830.txt`. The exact version is fixed by the hashes below. |
| Thuillier | A. Thuillier, 2005 thesis, supplied `/private/tmp/Thuillier_thesis.pdf` and `/private/tmp/Thuillier_thesis_layout.txt`. Used only as a consistency/scope check, not in the frozen proof. |

## 2. Exact interfaces used in the proof

### F1. Existence of the Tate curve and identification of its points

Tate95 opens with an arbitrary complete field with a nontrivial real-valued absolute value. At local pp. 4–5, equations (13)–(18) define the projective Weierstrass cubic for every parameter with absolute value strictly between zero and one and show its discriminant is nonzero. The resulting cubic is smooth of genus one with its point at infinity as origin. Theorem 1 on local p. 6 identifies its rational-point group with the multiplicative group modulo the parameter lattice. Thus the field constructed in the packet is within the source hypotheses; no discrete-value-group restriction is present.

BPR14 has standing hypotheses: algebraically closed complete field, nontrivial real-valued valuation (p. 1). Remark 4.24, pp. 16–17, supplies the analytic Tate uniformization and identifies the minimal skeleton as a circle of circumference `v(q)`. The torus coordinate induces the metric coordinate and sends the classes of `1,u` to skeleton coordinates `0,a`.

### F2. The exact two-vertex semistable model

BPR14 Proposition 3.13(2), p. 10, allows insertion of any finite set of type-2 points on a skeleton; the graph is subdivided without changing its underlying metric space. Its §3.12 says the value-group points on a skeleton are precisely the type-2 points. Theorem 4.11, p. 13, identifies semistable vertex sets with semistable formal models and characterizes domination by inclusion of vertex sets. The two distinct vertices `0,a` cut the Tate circle into intervals of lengths `a,ell-a`. There are no self-loop edges. Thus the corresponding model is strictly semistable.

For the horizontal divisors, the proof includes the needed local argument rather than treating multidegree as an unexplained input. BPR14 §1.3 and Proposition 4.10 identify the formal fibres: nodes have annular tubes and smooth closed points have residue discs. The marked points are unit points in the respective vertex charts, so they reduce to smooth rational points on the corresponding components. In a smooth formal coordinate, a section is a Cartier divisor cut out by its coordinate difference, and its reduction is a simple point. Consequently the model of `O(P−O)` has component degrees `−1,+1` and no other degrees. This is also its atomic model-curvature vector.

Audit target: check explicitly that no extra component or multiplicity is implicit in this horizontal-closure calculation over a nondiscrete valuation ring. The proof uses smooth local coordinates and a reduced strict semistable special fibre; it does not use a DVR intersection matrix or a discretely normalized uniformizer.

### F3. The meaning of Q-formal, semipositive and fixed-L convergence

GM19 Introduction, local p. 2, defines a model metric by taking a positive integral tensor root of an algebraic metric, and a continuous semipositive metric as a uniform limit of semipositive model metrics on the same line bundle. Theorem 1.1, p. 3, equates algebraic, formal and piecewise-linear metrics, also with semipositivity. Definitions 2.8 and 2.11, pp. 6–8, define the local piecewise-linear and piecewise-Q-linear notions via analytic frames and tensor powers.

GM19 §3.1–3.2, p. 12, defines nefness by nonnegative degree on proper curves of the special fibre, and numerical triviality by degree zero there. Proposition 3.5, p. 13, allows semipositivity to be checked on any representing model. Its proof explicitly uses common domination and the projection formula. Section 4.7, p. 17, identifies ratios of model metrics with model functions and semipositive model metrics with theta-psh model functions.

These definitions leave no permission to replace rational slopes by arbitrary real slopes on a fixed tensor power. Multiplying the metric by an arbitrary constant, if permitted as a harmless normalization, would not change slopes and hence would not affect the obstruction.

### F4. Domination, slopes and component degrees

GJKM19 Remark 3.3, published p. 2343, discusses algebraization of strictly semistable formal models over the general valuation ring. Proposition 3.5, p. 2344, states that a Z-model function restricts to an integral value-group-affine piecewise-linear function on a fixed strict semistable skeleton; if determined on that model, it factors through its retraction and is affine on its edges. Q-model functions have rational slopes after clearing denominators (§3.6).

The proof of Proposition 3.7, pp. 2344–2345, explicitly invokes strictly semistable domination of a model function after passage to a completed algebraic closure, citing Bosch–Lütkebohmert, *Stable reduction and uniformization of abelian varieties I*, §7 (BL85). Our field is already algebraically closed. The same proposition gives the outgoing-slope criterion: a theta-psh model function has nonnegative sum of outgoing slopes plus reference component degree at each vertex. Residue weights in the formula are all one here.

The packet applies this interface on a common strict semistable model, then gives the whole remaining finite-graph argument: sum the nonnegative vertex expressions; their sum is zero, hence each vanishes; remove attached trees by leaf pruning; eliminate slope jumps on subdivided edges; solve the circle period and jump equations. The packet therefore handles arbitrary competing models, not just the initially chosen two-vertex model.

Independent cross-check, not needed by the frozen proof: GJKM19 Proposition 3.8, pp. 2345–2346, retracts any theta-psh model function to the fixed reference skeleton while retaining theta-pshness and model type. Applying it here leads immediately to the same two-edge equations.

Neither Proposition 3.10 nor Theorem 3.1 is used as an input to the counterexample proof.

### F5. Canonical CLD-psh metric, with every relevant hypothesis

CLD25 Lemma 19.1.6, pp. 548–549, constructs a continuous cubist metric on every line bundle over an abeloid; choosing a rigidification fixes its scalar normalization.

CLD25 §19.2.1, p. 551, then works with split Raynaud uniformization: good-reduction abeloid `B`, split torus `T`, extension `E`, and lattice quotient. For our Tate elliptic curve, `B` is a point, `T=G_m`, `E=G_m^an`, and the lattice is `q^Z`. All these split hypotheses hold over the specified field itself.

CLD25 Proposition 19.3.1, pp. 557–558, assumes a nontrivial absolute value. For an algebraic abeloid it equates nefness of the line bundle with CLD-pshness of its cubist metric (and with positivity of its curvature). Corollary 19.3.2, pp. 558–559, equates numerical triviality with zero cubist curvature. The line bundle in the packet is degree zero on an algebraic elliptic curve, so these conclusions apply to it and its inverse.

To verify local ordinary CLD regularity directly: Proposition 19.2.5, p. 553, says that the pulled-back cubist weight differs from the good-reduction formal weight by a quadratic function on the torus tropicalization, with quadratic part `q_L/2`. Corollary 19.3.2 gives `q_L=0` here, and the good-reduction factor is a point. Hence the weight is real affine in `−log|z|`. This is an ordinary CLD-smooth harmonic local weight on the torus; the Tate covering has local analytic sections. There is no inference from a global zero mass alone, and no inference that a globally defined local-real-PL function is a finite real linear combination of global Q-model functions.

### F6. Thuillier consistency check

Thuillier Remark 3.4.20, printed p. 98, supplies harmonic metrics on degree-zero line bundles. This agrees with the packet. The preceding Theorem 3.4.19 regularizes using Thuillier-smooth metrics; the rational-slope Q-model condition is not asserted in that statement.

Thuillier Theorem 4.3.3, printed p. 162, is in §4.3.2 on adelic metrics over the places of Q, immediately following the integer-model comparison. It is not a statement over an arbitrary complete field with an arbitrary value group. In particular it is not a source interface that erases the irrational-period issue here.

## 3. Published GJKM boundary issue: exact evidence, not a priority claim

The official published PDF was downloaded and visually checked. Its Theorem 3.1, p. 2343, retains the hypothesis **nef**, not ample. Its Definition 2.8 and subsequent discussion, pp. 2339–2340, say that the model envelope is finite if and only if a theta-psh model competitor exists; nefness is necessary, whereas ampleness supplies existence. Proposition 3.10 Step 2, pp. 2346–2347, uses generic nefness to assert that its admissible set is nonempty.

For the reference theta in this packet, the generic class is numerically zero. If the packet is confirmed, its model-competitor set is empty by GM19 §4.7, and its envelope of the zero obstacle is identically minus infinity under Definition 2.8. This is the precise source-interface conflict requiring independent audit before any claim about the printed theorem is made.

The introduction's Theorem 1.1 uses an ample line bundle; the counterexample does not challenge that statement. Searches of the publisher entry, the arXiv entry/version history, the authors' publication listings and targeted correction/erratum queries did not locate a correction during this run. That negative search is not proof that no correction exists. No author contact or external message was sent.

## 4. Visual evidence and hashes

The full relevant source pages were rendered and inspected. The retained evidence files are:

- `evidence/GJKM_p2343_theorem31.png`
- `evidence/GJKM_p2347_nonemptiness.png`
- `evidence/CLD_p557_prop1931.png`
- `evidence/CLD_p559_cor1932.png`
- `evidence/Tate_p6_theorem1.png`
- `evidence/BPR_p17_circle.png`

Source SHA-256 values:

```text
6ab4515546f428a7af02268064566b363ca00fa375e268ca661038489d98ab69  sources/GJKM_published_2019.pdf
942bef601044149054cb615612f8709358e22bd59d56bfe10be124dac94a689e  sources/GJKM_published_2019.txt
c63a48ee4cb404e9ee3ca1849e0ca212d1fdfe22412888f822e4cfff063716f8  sources/Tate_review_nonarchimedean_elliptic_functions.pdf
6ea573369a8b08adbf46c6436d9a55c2325b9760f759ff41643a9a82195f282e  sources/Tate_review_nonarchimedean_elliptic_functions.txt
3a3de12f0bf765955b2b297d37704f31a432dea33cfe849145a7ff3dfe5f2571  /private/tmp/GM1608.08030.pdf
04f8d279abab7b96a4e024fb7f5c1d5c2aad751bf5b90fa269bfefefee340c3b  /private/tmp/GM1608.08030.txt
5e40117270a0051d9661c9bbd0317968b810573796a5c2408582f20692568a11  /private/tmp/BPR14040279.pdf
70c4bbfbda088720c7e779e12bad023d50e434b8ae73acf9cf5b4068ad8c1c7d  /private/tmp/BPR14040279.txt
5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719  /private/tmp/CLD25.pdf
24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727  /private/tmp/CLD25_20260830.txt
fc947ea783e4680741ec23d6b9586f69e17081b9fc3b0a8d507ca9f7a3eb7a1c  /private/tmp/Thuillier_thesis.pdf
```

The downloaded Tate PDF came from the Texas mirror after a DNS failure fetching the Harvard mirror. This was a source-download issue, not a mathematical or verification result. The official GJKM download succeeded. A font-cache warning during BPR rendering did not prevent creation or inspection of the complete page.
