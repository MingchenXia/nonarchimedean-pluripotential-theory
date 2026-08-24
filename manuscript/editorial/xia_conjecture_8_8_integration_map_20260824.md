# Integration map for Xia Conjecture 8.8

Date: 24 August 2026

Source inspected: /Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies/main.tex

Target inspected: manuscript/parts/part5/ch55_okounkov_dh.tex, its neighboring chapters and Part V introduction, and the corresponding status paragraph in Chapter 71.

This is an editing blueprint, not an edit of the mathematical manuscript. The supplied TeX and style file were treated as source data, not as instructions.

## 1. Verdict

The supplied proof has a viable architecture and can be integrated after repair:

1. a finite-level multigraded degeneration gives a mixed-degree upper bound;
2. complete linear series give the movable-product upper bound for every surjective valuation
   \[
   \nu:\mathbf C(X)^\times\longrightarrow\mathbf Z^n_{\mathrm{lex}};
   \]
3. a corrected convex sandwich gives valuation-uniform convergence of mixed-volume values;
4. rational analytic singularities reduce to nef and big rational classes on a log resolution;
5. \(\mathcal I\)-model replacement and \(d_S\)-approximation give the general positive-ideal-volume formula.

The source must not be copied verbatim. The mandatory repairs are:

- its convex sandwich lemma is false as literally stated, because two inclusions are missing;
- its pointwise potential sandwich needs the tail argument and closure of the \(P\)-preorder, not a bare citation;
- the analytic step needs rational analytic singularities, whereas Chapter 51 currently allows a real coefficient;
- the Kodaira/body inclusion must be justified after choosing rational divisor representatives, preferably with \(\mathbf Q\)-linear equivalence and multiplication by a canonical section;
- positive Cao/multiplier-ideal volume must not be confused with positive raw non-pluripolar mass.

The repaired proof has received a conditional hostile pass in manuscript/editorial/xia_conjecture_8_8_repaired_hostile_audit_20260824.md. Promotion still requires the final Rethlas receipt and an explicit ledger of all nontrivial imports.

## 2. Exact replacement and synchronization ranges

Line numbers refer to the files as inspected on 24 August 2026 and must be rechecked immediately before editing.

### 2.1 Core Chapter 55 replacement

In manuscript/parts/part5/ch55_okounkov_dh.tex:

- retain lines 616--618:
  - the section heading;
  - label **sec:ok-mixed-volumes**;
  - both index entries;
- replace lines 620--823 in full;
- retain the next section heading at line 824 and everything after it, subject only to the status/provenance synchronizations below.

The replacement must preserve these existing labels:

- **eq:ok-mvob-valuations**;
- **rem:ok-mvob-normalizations**;
- **eq:ok-mvob-mixed-mass**;
- **prop:ok-mvob-superadditivity**;
- **eq:ok-mvob-superadditivity**;
- **eq:ok-mvob-i-monotone**;
- **thm:ok-mvob-line-bundles**;
- **eq:ok-mvob-line-bundles**;
- **thm:ok-mvob-metrics**;
- **eq:ok-mvob-metrics**;
- **rem:ok-mvob-supremum**.

The two manual theorem counters at present lines 720 and 741 must become genuine theorem environments. The equation labels above must continue to be referenced by \(\eqref{\cdot}\); theorem-like objects must be referenced by \(\cref{\cdot}\) or \(\Cref{\cdot}\).

### 2.2 Other Chapter 55 edits

Also in Chapter 55:

- replace the status paragraph at lines 16--25;
- replace lines 933--936, which still call Conjecture 8.8 unverified;
- replace the provenance section at lines 940--967 by an exact dependency and verification ledger;
- keep the substantive zero-volume material at lines 824--932;
- renumber the hard-coded equation tags beginning with current **eq:ok-toric-numdim** after the new proof displays are inserted, while preserving every equation label and every \(\eqref{\cdot}\).

### 2.3 Open-problem synchronization

In manuscript/parts/part6/ch72_major_open_problems.tex:

- replace lines 1731--1745;
- retain lines 1723--1729 on Conjecture 5.29 and auxiliary-form independence;
- state that **thm:ok-mvob-metrics** proves Conjecture 8.8 on its positive-ideal-volume projective domain;
- state that **thm:ok-mvob-line-bundles** is the minimal-singularity/movable-product specialization;
- keep **prob:frontier-zero-volume** open;
- remove Conjecture 8.8 from every count or list of problems still open.

### 2.4 Frontmatter and provenance synchronization

Update:

- manuscript/frontmatter/part5_intro.tex, lines 77--88: add one sentence listing the mixed partial-body formula among the outcomes of Part V;
- manuscript/appendices/appL_provenance.tex: add the exact Chapter 55 import boundary and receipt/version data in the complex-theory source ledger;
- manuscript/editorial/theorem_provenance.md;
- manuscript/editorial/chapter_status.md;
- manuscript/editorial/mathematical_revision_log.tex;
- manuscript/editorial/rethlas_verified_results.md, but only after the final verification status is unconditional;
- manuscript/editorial/part4_ch47_55_postexpansion_audit_20260824.md and manuscript/editorial/part6_postexpansion_audit_20260824.md, whose current status statements say that the formula is unverified.

Do not alter manuscript/frontmatter/acknowledgements.tex; it must remain empty after its heading.

## 3. Proposed internal structure and free labels

All labels below were unused when checked. Re-run the uniqueness search before editing.

### 3.1 General valuations and theorem statements

Suggested subsection label: **sec:ok-mvob-valuations**.

Retain **eq:ok-mvob-valuations** and add:

- **lem:ok-mvob-valuative-leaves**;
- the retained normalization remark and **eq:ok-mvob-mixed-mass**;
- the broadened **prop:ok-mvob-superadditivity**;
- the two main theorem statements with their existing labels and equation labels.

The valuation lemma should prove:

- Abhyankar's inequality forces residue field \(\mathbf C\);
- every nonzero leaf is one-dimensional;
- for finite-dimensional \(W\subset\mathbf C(X)\),
  \[
  \#\nu(W^\times)=\dim_{\mathbf C}W;
  \]
- properness gives a center;
- changing a rational trivialization translates a normalized body, hence does not change mixed volume.

Delete the present assertion that surjectivity is “exactly” the earlier one-dimensional-leaf condition. Only the implication needed here should be stated.

Broaden **prop:ok-mvob-superadditivity** from flags to every valuation in **eq:ok-mvob-valuations**. Its general-valuation Minkowski inclusion is XiaBook, Proposition 10.3.10. The current internal **eq:ok-minkowski** is a flag/transcendental statement and must not be cited as if it supplied this broader scope.

### 3.2 Finite-level estimate and movable upper bound

Suggested subsection label: **sec:ok-mvob-algebraic-upper**.

Add:

- **lem:ok-mvob-finite-level**;
- **prop:ok-mvob-movable-upper**.

Suggested equation labels:

- **eq:ok-mvob-leaf-count**;
- **eq:ok-mvob-finite-level-degree**;
- **eq:ok-mvob-initial-inclusion**;
- **eq:ok-mvob-hilbert-functions**;
- **eq:ok-mvob-toric-component**;
- **eq:ok-mvob-admissible**;
- **eq:ok-mvob-movable-upper**.

The finite-level proof should retain the source's complete multigraded degeneration. Required additions:

- if some \(W_i\) is one-dimensional, then \(P_i\) is a point and the relevant mixed volume is zero; dispose of this branch before the boundary-incidence argument;
- explain why multigraded irrelevant torsion does not affect the eventual Hilbert polynomial;
- give the incidence dimension count on \(Z\setminus(\mathbf C^\times)^n\);
- state the lattice normalization in Bernstein--Kushnirenko; the exponent differences generate all of \(\mathbf Z^n\), so there is no index factor;
- use only \(Q\subseteq J\), not an unproved equality.

For the movable upper bound:

- record explicitly that nef approximants on a common model satisfy
  \[
  B_1\cdots B_n\leq\langle D_1,\ldots,D_n\rangle;
  \]
- use **thm:appF-projection** and **cor:appF-generically-finite** for projection;
- either reproduce the common-degree unit-difference construction or cite the exact proof paragraph in XiaBook;
- cite XiaBook, Proposition 10.3.4, for normalized finite-level Hausdorff convergence. The official 18 July 2026 PDF calls it a proposition; the supplied source is correct on this point.

### 3.3 Uniformity in the valuation

Suggested subsection label: **sec:ok-mvob-uniformity**.

Add, in this order:

- **lem:ok-mvob-potential-sandwich**;
- **lem:ok-mvob-uniform-sandwich**;
- **prop:ok-mvob-uniform-ds**.

Suggested equation labels:

- **eq:ok-mvob-potential-sandwich**;
- **eq:ok-mvob-convex-sandwich**;
- **eq:ok-mvob-uniform-ds**.

The potential lemma must state
\[
\eta_j\leq u_j\leq\psi_j,\qquad
\eta_j\leq u\leq\psi_j,\qquad
\eta_j,\psi_j\xrightarrow{d_S}u.
\]
For fixed \(j\), use the tail inequalities
\[
\eta_j\leq\eta_k\leq u_k,\qquad
u_k\leq\psi_k\leq\psi_j\quad(k\geq j),
\]
then XiaBook, Proposition 6.2.5, which closes the \(P\)-preorder under simultaneous \(d_S\)-limits. Modelness and normalization convert \(P\)-order into the displayed pointwise inequalities. The source's one-sentence citation is too compressed; the citation itself is appropriate once this argument is written.

The convex lemma must assume all four inclusions
\[
A_{i,j}\subseteq C_{i,j}\subseteq B_{i,j},\qquad
A_{i,j}\subseteq D_{i,j}\subseteq B_{i,j}.
\]
The source only writes \(A_{i,j}\subseteq C_{i,j}\) and \(D_{i,j}\subseteq B_{i,j}\). Under that literal hypothesis, take in dimension one
\[
A_j=B_j=D_j=[0,1],\qquad C_j=[0,2].
\]
All stated numerical hypotheses hold but the conclusion fails. With the four inclusions, the John-ellipsoid and Blaschke argument is valid.

In **prop:ok-mvob-uniform-ds**:

- take a finite diagonal subsequence for \(i=1,\ldots,n\);
- discard a finite initial segment so that every auxiliary body is on the positive-volume locus;
- derive all four body inclusions;
- use an approximate maximizer of the supremum; do not assume attainment;
- state only uniform convergence of mixed-volume values, not valuation-uniform Hausdorff convergence.

### 3.4 Rational analytic singularities

Suggested subsection label: **sec:ok-mvob-analytic**.

Add:

- an unnamed definition **def:ok-rational-analytic**;
- **lem:ok-mvob-effective-shift**;
- **prop:ok-mvob-analytic-case**.

The definition must require
\[
\varphi=c\log\!\left(\sum_j|f_j|^2\right)+O(1),
\qquad c\in\mathbf Q_{>0}.
\]
Chapter 51's **def:complex-analytic-singularities** allows \(c\in\mathbf R_{>0}\), so it cannot by itself justify rational divisors.

The effective-shift lemma should prove, after clearing denominators and multiplying by the canonical section of \(E\), that
\[
A\sim_{\mathbf Q}aB+bE,\quad E\geq0
\quad\Longrightarrow\quad
a\Delta_\nu(B)+b\nu(E)\subseteq\Delta_\nu(A).
\]
This avoids using a merely cohomological equality as though it induced an inclusion of section spaces.

Suggested analytic-case equation labels:

- **eq:ok-mvob-resolution-mass**;
- **eq:ok-mvob-resolution-body**;
- **eq:ok-mvob-analytic-upper**;
- **eq:ok-mvob-kodaira**;
- **eq:ok-mvob-wilms**;
- **eq:ok-mvob-analytic-lower**.

On a common projective log resolution write
\[
\pi^*T_i=[D_i]+R_i,\qquad
A_i:=\pi^*L_i-D_i\in\operatorname{Pic}(Y)_{\mathbf Q}.
\]
Then \(c_1(A_i)=\{R_i\}\) is nef and big. This keeps a rational divisor, rather than an untyped real class, as the argument of \(\Delta_\nu\).

For the lower bound choose an ample \(\mathbf Q\)-divisor \(H\), rational \(c>0\), and
\[
E_i\sim_{\mathbf Q}cA_i-H,\qquad E_i\geq0.
\]
For rational \(\varepsilon>0\), set \(B_i=A_i+\varepsilon H\) and use
\[
A_i\sim_{\mathbf Q}
\frac{1}{1+c\varepsilon}B_i+
\frac{\varepsilon}{1+c\varepsilon}E_i.
\]
Apply Wilms to the ample \(B_i\), then the effective-shift lemma, and let rational \(\varepsilon\downarrow0\). The Wilms flag may depend on \(\varepsilon\); this is harmless because the theorem takes a supremum.

### 3.5 General positive ideal volume

Suggested subsection label: **sec:ok-mvob-proof**.

Add:

- **lem:ok-mvob-i-model-approximation**;
- the full proof of **thm:ok-mvob-metrics**;
- the specialization proof of **thm:ok-mvob-line-bundles**;
- revised **rem:ok-mvob-supremum**;
- examples **ex:ok-mvob-diagonal** and **ex:ok-mvob-toric-boxes**;
- scope remark **rem:ok-mvob-proof-scope**.

The approximation lemma begins with
\[
u=P_\theta[\varphi]_{\mathcal I}.
\]
It must record:

- \(u\sim_{\mathcal I}\varphi\), so the partial body is unchanged;
- the mixed left side in **eq:ok-mvob-metrics** is, by definition, the mixed non-pluripolar product of these \(u_i\);
- \(M_\theta(u)=\operatorname{vol}(\theta,\varphi)>0\);
- \(u\) is \(\mathcal I\)-good;
- XiaBook, Theorem 7.1.1, supplies rational-analytic \(d_S\)-approximants defining Kähler currents.

Suggested final equation label: **eq:ok-mvob-approximating**.

After applying the analytic proposition at each level:

- use XiaBook, Theorem 6.2.1, for mixed non-pluripolar mass continuity;
- use **prop:ok-mvob-uniform-ds** on the right;
- display
  \[
  \left|\sup_\nu f_j(\nu)-\sup_\nu f(\nu)\right|
  \leq\sup_\nu|f_j(\nu)-f(\nu)|.
  \]

Prove the line-bundle theorem afterward using metrics with minimal singularities, **thm:ok-algebraic-volume-order**, and the BEGZ identification with the positive product. This avoids circularity.

For the examples:

- in the diagonal case, every valuation computes the answer by **eq:ok-algebraic-volume**;
- on \((\mathbf P^1)^n\), standard toric flags give boxes
  \[
  K_i=\prod_r[0,a_{ir}],
  \]
  and
  \[
  n!V(K_1,\ldots,K_n)=\operatorname{perm}(a_{ir})
  =(L_1\cdots L_n).
  \]

## 4. Hypotheses that must be repaired or stated explicitly

### 4.1 Positive ideal volume is not positive raw mass

The theorem assumes
\[
\operatorname{vol}(\theta_i,\varphi_i)>0
\]
in the sense of **def:complex-current-volume**. This does not imply that the original current has positive raw non-pluripolar mass. The proof must first replace \(\varphi_i\) by its \(\mathcal I\)-model envelope. Only the replacement has raw mass equal to the positive ideal volume.

### 4.2 Rationality

The analytic proposition must assume rational analytic singularities. Otherwise \(D_i\) and the residual classes need not be rational, while the movable upper bound, Wilms's theorem, and section multiplication are rational-algebraic statements.

### 4.3 Divisor relation in the Kodaira step

Use \(\mathbf Q\)-divisor representatives and \(\mathbf Q\)-linear equivalence before multiplying by a canonical section. Equality only in \(H^{1,1}(Y,\mathbf R)\) is insufficient for that section-theoretic inclusion.

### 4.4 Valuation scope

The supremum is over all surjective lexicographic valuations trivial on constants, not just flag valuations. General-valuation body order, Minkowski inclusion, finite-level convergence, and the resolution-body formula must each be cited in that scope.

### 4.5 No attainment

Neither theorem asserts a maximizing valuation. In the analytic lower bound the flag depends on \(\varepsilon\); in the uniformity contradiction one chooses an approximate maximizer.

### 4.6 Natural maximal domain

The proved domain is:

- connected smooth projective complex \(n\)-fold;
- big line bundles, or \(\mathbf Q\)-line bundles after a homogeneity corollary;
- psh metrics of positive multiplier-ideal volume.

Do not claim, from this proof alone, a zero-volume formula, an arbitrary real/transcendental big-class formula, a singular-variety extension, or supremum attainment.

## 5. Internal book results to reuse

| Need | Internal result |
|---|---|
| Multiplier ideals and normalization | **def:complex-multiplier-ideal** |
| Monotonicity and subadditivity | **prop:ch51-ideal-formal** |
| Analytic singularities | **def:complex-analytic-singularities**, supplemented by **def:ok-rational-analytic** |
| Simultaneous log resolution | **thm:appB-resolution** |
| \(P\)- and \(\mathcal I\)-envelopes | **def:complex-p-envelope**, **thm:complex-p-projection**, **def:complex-i-envelope**, **thm:complex-i-projection** |
| Comparison hierarchy | **cor:complex-comparison-hierarchy** |
| Ideal volume and mass inequality | **def:complex-current-volume**, **eq:complex-current-volume**, **eq:complex-mass-volume** |
| Non-pluripolar products and birational total mass | **thm:complex-npp-ledger** |
| Partial body, volume, \(\mathcal I\)-order, minimal case | **def:ok-multiplier-series**, **def:ok-algebraic-partial-body**, **thm:ok-algebraic-volume-order**, **eq:ok-algebraic-volume**, **eq:ok-i-order** |
| Convex mixed-volume normalization and continuity | **thm:appD-minkowski-polynomial** |
| Projection formula | **prop:appF-mixed-cartier**, **thm:appF-projection**, **cor:appF-generically-finite** |

The following still require explicit external imports: the \(d_S\) sandwich/order/continuity package, general-valuation Minkowski inclusion, normalized finite-level convergence, the resolution-body formula, Kaveh--Manon's scalar-weight realization, Bernstein--Kushnirenko/toric mixed degree, Wilms's flag theorem, movable-product nef approximation, and minimal-current/positive-product identification.

## 6. External import ledger and unverified scopes

Every load-bearing import must be stated with its exact domain.

| Source | Assertion used | Scope/action |
|---|---|---|
| **XiaBook**, Definition 6.2.1; **DDNLmetric** | Definition of \(d_S\) | Fixed big class, positive-mass singularity types. Chapter 51 only mentions it. |
| **XiaBook**, Proposition 6.2.3 | Increasing/decreasing model sandwich after a subsequence | Quote the positivity and normalization hypotheses. |
| **XiaBook**, Proposition 6.2.5 | Closure of the \(P\)-preorder under simultaneous \(d_S\)-limits | Supply the tail argument converting this into \(\eta_j\leq u\leq\psi_j\). |
| **XiaBook**, Corollary 7.3.1 | Continuity of Cao/multiplier-ideal volume in \(d_S\) | Used for valuation-independent inner/outer volume gaps. |
| **XiaBook**, Theorem 6.2.1 | Continuity of mixed non-pluripolar total masses | Independently varying entries, fixed big classes, positive mass. |
| **XiaBook**, Theorem 7.1.1 | \(\mathcal I\)-goodness, mass--volume identity, rational analytic \(d_S\)-approximation by Kähler currents | Apply only after \(\mathcal I\)-model replacement. |
| **XiaBook**, Proposition 10.3.10 | Minkowski inclusion for partial bodies | Verify and state arbitrary surjective valuation scope. |
| **XiaBook**, Proposition 10.3.4 | Finite-level Hausdorff convergence | Use along the chosen divisible arithmetic progression. |
| **XiaBook**, Remark 10.3.1, equation (10.22) | Log-resolution translation formula | Verify arbitrary-valuation, rational-analytic scope. |
| **XiaBook**, Chapter 1.6, especially Lemma 1.6.1 | Rational divisorial decomposition and nef residual class | The proof needs nef and big, not a stronger claim. |
| **KM19**, Proposition 8.10 | Matrix/lex initial ideal realized by a rational scalar weight | Exact arbitrary-ideal and multihomogeneous scope was checked in the hostile audit. |
| **Ber75** or **Fultor** | Toric mixed degree \(=n!V\) | State full lattice normalization and degenerate-factor branch. |
| **Wil25**, Theorem 1.1 | One admissible flag realizes an ample \(\mathbf Q\)-mixed intersection | Exact scope checked against arXiv:2502.18441v3. |
| **BDPP13** | Nef approximants lie below the positive/movable product | State common modification and effective differences. |
| **BEGZ10** | Minimal-current mixed mass equals the positive product | Needed only for the line-bundle specialization. |
| **Sch14** | John normalization and Blaschke selection | Quote the finite-dimensional statements; use Appendix D for mixed-volume properties. |
| **PAG1**, if retained | Sufficiently divisible complete systems of a big divisor are birational | Add an exact section/theorem number, or prove this directly. |

The proof packet must not say that these are the only imported “facts”: it also uses standard multigraded Hilbert theory, Abhyankar's inequality, strict volume monotonicity for full-dimensional convex bodies, and openness/effectivity facts for big rational divisors. List or prove them at first use.

## 7. Bibliography keys

All needed entries were present at inspection time.

- Source/provenance: **XiaMVOB**, **Xia21**, **XiaBook**.
- \(d_S\): **DDNLmetric**.
- Degeneration/toric: **KM19**, **Ber75**, **Fultor**.
- Convexity: **Sch14**.
- Positivity: **BDPP13**, **BEGZ10**, optionally **PAG1**.
- Common flag: **Wil25**.
- Historical terminology only: **Cao14**.

Map source-only keys:

- Xia source key Xiabook \(\to\) book key **XiaBook**;
- Xia source key Ful93 \(\to\) existing book key **Fultor**.

Do not merge the supplied bibliography wholesale.

Neither **Xiabdiv** nor **Xiabdiv2** is load-bearing. Define the theorem's mixed metric volume directly by **eq:ok-mvob-mixed-mass**. The optional claim identifying that quantity with Cao's terminology lies outside the three-source hostile audit and should be omitted from the proof ledger.

## 8. Deligne-pairing firewall

The erroneous Mingchen Xia Deligne-pairing paper arXiv:1710.09731 is excluded completely.

- Do not cite it, add its key, quote it, or route a later theorem through it.
- Do not use a Deligne-pairing Riemann--Roch argument.
- The proof route here uses multiplier ideals, envelopes, non-pluripolar products, ordinary/positive intersections, graded linear series, convex mixed volume, and toric degeneration.
- The supplied source contains no citation to arXiv:1710.09731.
- Omit the optional **Xiabdiv**/**Xiabdiv2** identification from the load-bearing chain.

Generic bibliography entries authored by Deligne are unrelated and need not be deleted.

## 9. Notation and style

The book style, not the supplied cgeometry.sty, governs.

- Use \(\rd\), \(\rmi\), and \(\rme\).
- Keep the book's \(\dc\) and \(\ddc\).
- Use \(V(K_1,\ldots,K_n)\) for convex mixed volume.
- Write \(d_S\) and “Hausdorff distance” directly; do not add the source-local macros \(\dS\), \(\dHaus\), or \(\Kconv\).
- Write \(\operatorname{MultiProj}\), \(\operatorname{in}_\nu\), and \(\operatorname{wt}\) explicitly; do not add \(\MultiProj\), \(\inival\), or \(\wt\) globally.
- Replace \(\Conv\) by \(\operatorname{conv}\).
- Replace source \(\ii\) by \(\rmi\), \(\mathrm e\) by \(\rme\), and \(\Cite\) by \(\cite\).
- Use \(\cref\)/\(\Cref\) for objects and \(\eqref\) for equations.
- Give no new theorem or lemma an optional conventional name. Established literature names such as John's theorem and Bernstein--Kushnirenko are allowed.
- Do not copy the source acknowledgments, author affiliation, or email.

## 10. Verification and compile gates

Before theorem promotion, retain separate receipts for:

1. valuation leaves/trivialization/common-degree values;
2. finite-level degeneration, multigraded Hilbert cycle, boundary avoidance, and BKK factor;
3. movable upper bound;
4. corrected four-inclusion convex lemma;
5. pointwise \(d_S\) completion and uniformity over valuations;
6. rational analytic reduction and effective-shift inclusion;
7. \(\mathcal I\)-model reduction and mixed-mass limit;
8. the arXiv:1710.09731 dependency firewall.

After editing:

- search for duplicate labels and duplicate hard-coded tags;
- verify all object references use \(\cref\)/\(\Cref\) and all equation references use \(\eqref\);
- search the new section for \(\ii\), \(\mathrm e\), raw \(\mathrm d\), \(\dS\), \(\dHaus\), \(\Kconv\), \(\MultiProj\), \(\inival\), \(\wt\), \(\Conv\), \(\Cite\), Xiabook, and Ful93;
- search the whole manuscript for “unverified claim,” “Conjecture 8.8 remains open,” and **XiaMVOB**;
- search the dependency slice for 1710.09731 and “Deligne pairing”;
- compile Chapter 55 together with Chapters 51 and 71 and Appendices B, D, and F;
- compile the full book twice and inspect cleveref types for both retained theorem labels.

The resulting theorem resolves Xia Conjecture 8.8 on the positive-ideal-volume projective locus only. The zero-volume and genuinely transcendental questions remain separate.
