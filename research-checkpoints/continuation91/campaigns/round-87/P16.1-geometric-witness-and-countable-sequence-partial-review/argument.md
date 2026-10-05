# Independent review of geometric witnesses and local sequences


# UNCHANGED new root91 mathematical deduction; not a grant

# Geometric witnesses and local sequences for the conditional affine chain

New unreviewed reconstruction for original P16.1. The original solved count remains four. Native review85 assesses the unchanged author83 chain, review86 assesses the unchanged reductions89/90, and author84 retains its independently frozen fiber-reference input. None receives feedback from this draft.

## 1. A smooth affine variety has a smooth projective ample-boundary completion

Let \(k\) be algebraically closed of characteristic zero, with no cardinality restriction, and let \(U=\operatorname{Spec}R\) be a smooth integral affine variety. Embed \(U\) as a CLOSED subscheme of an actual affine space using generators of its original ring. Its reduced projective closure \(X_0\) is integral, \(U=X_0\cap D_+(x_0)\), and the hyperplane section \(D_0=V(x_0)|_{X_0}\) is an effective ample Cartier divisor. The defining section is nonzero in the function field, so it is a nonzerodivisor. Its support is exactly \(X_0\setminus U\).

Apply Temkin0904.1592v2, Theorem1.2.1, to \(X_0\). A finite-type scheme over a field is excellent by Stacks0HA6, Lemma29.20.7; \(X_0\) is Noetherian and generically reduced and has a morphism to \(\operatorname{Spec}\mathbb Q\). Thus the theorem supplies a FINITE sequence of blowups with centers disjoint from the preimage of the original regular locus, ending at a regular variety \(X\). Its definition of a blowup sequence is a finite composition (LF480–492). Every center is therefore supported outside the unchanged smooth \(U\). Blowups are projective because the coherent Rees algebra is generated in degree one. The final \(X\) is projective over \(k\), regular, and smooth over the perfect field \(k\), and its map to \(X_0\) is an isomorphism over ALL of \(U\).

An ample boundary can be retained at EVERY blowup, including on intermediate singular varieties. Suppose \(b:X'\to X_j\) blows up a coherent ideal \(\mathcal I\) whose center is supported on an effective ample Cartier divisor \(D_j\). Because the schemes are Noetherian and quasi-compact, some \(N>0\) satisfies
\[
 \mathcal O(-ND_j)\subset\mathcal I.
\]
This is the local radical-ideal criterion for support inclusion, with a uniform exponent on a finite affine cover. Stacks31.33.4 gives the effective Cartier divisor \(E\), \(\mathcal I\mathcal O_{X'}=\mathcal O(-E)\), and \(\mathcal O(-E)=\mathcal O_{X'}(1)\). This last bundle is \(b\)-relatively ample. Pullback of \(D_j\) remains Cartier: each blowup chart is a subring of a localization of the original integral domain, so its nonzero local defining function remains a nonzerodivisor (also Temkin Lemma4.3.1).

The pulled ideal inclusion gives an effective Cartier difference
\[
 Nb^*D_j-E\ge0.
\]
For \(m\ge N+1\), the divisor
\[
 D_{j+1}=mb^*D_j-E
       =(Nb^*D_j-E)+(m-N)b^*D_j
\]
is effective and has support EXACTLY \(b^{-1}(\operatorname{Supp}D_j)\). It contains that full support through its second summand; both summands have no support outside it. This proves positivity without assigning Weil coefficients on a singular intermediate scheme. Stacks29.38.7 makes \(\mathcal O(-E)\otimes b^*\mathcal O(D_j)^m\) ample for all sufficiently large \(m\). Choose \(m\) satisfying both requirements. Iteration yields a smooth projective \(X\supset U\) with an effective AMPLE Cartier divisor \(D\) supported exactly on \(X\setminus U\). A simple-normal-crossings boundary is not needed for the accepted smooth affine gate.

## 2. Projective smooth domination of the ONE original proper witness

Let \(\mu:P\to U\) be the original proper birational morphism of integral finite-type \(k\)-schemes. Do not assume \(P\) is projective or proper over \(k\). Apply relative Chow's lemma, Stacks30.18.1, with the SAME base \(U\). It supplies a proper surjection \(P'\to P\), an isomorphism over a dense open of \(P\), and an immersion \(P'\to\mathbb P_U^r\). By the schematic-closure refinement in Remark30.18.2, take \(P'\) integral and reduced, so \(P'\to P\) is birational. Its composite \(P'\to U\) is proper.

The immersion into \(\mathbb P_U^r\) is a CLOSED immersion. Indeed its graph into \(P'\times_U\mathbb P_U^r\) is closed because the target is separated over \(U\), and projection to \(\mathbb P_U^r\) is proper by base change of \(P'\to U\). Thus the immersion is proper and has closed image; Stacks01IQ makes it closed. Its reduced schematic closure \(Z_0\) in \(X\times_k\mathbb P_k^r\) is integral and projective over \(k\), projective and birational over \(X\), and satisfies
\[
 Z_0\times_X U=P'
\]
as an ACTUAL scheme, since \(P'\) was closed in the restricted projective space. No exceptional part of the proper witness is lost by closing only its generic graph.

Resolve \(Z_0\) by Temkin1.2.1, obtaining a smooth integral projective \(Z\) and a projective birational morphism \(Z\to Z_0\). The composite
\[
 \bar\pi:Z\longrightarrow X
\]
is projective and birational and has a SMOOTH SOURCE. It need not be a smooth morphism. Over \(U\) it factors as
\[
 Z_U\longrightarrow P'\longrightarrow P\stackrel{\mu}{\longrightarrow}U.
\]
The first two arrows are proper, and their composite dominates the original witness. Pulling an original continuous contact approximant through this composite retains its actual value, its same constant support equality, and logarithms of units; take its decreasing limit only AFTER this pullback. This uses the one specified witness, with an actual dominating map to it, rather than silently replacing the input by a different weak function.

For a FINITE collection of proper birational witnesses over the same \(U\), take the reduced closure of their common generic graph in their fiber product over \(U\), apply relative Chow and resolve as above. It dominates each original witness: every proper projection has closed image containing a dense open of that integral witness. This finite construction makes no assertion for an arbitrary family of witnesses.

## 3. Actual affine and pulled metric references

Choose \(r\) so \(B=\mathcal O_X(rD)\) is very ample, with boundary section \(s_D^r\). Section localization shows that each original generator \(z_i\in R=\Gamma(U,\mathcal O_U)\) is a section ratio on a sufficiently large tensor power of \(\mathcal O(D)\). Enlarge \(r\) so ALL finitely many \(z_i s_D^r\) extend to global sections of \(B\). Include them and \(s_D^r\) in a finite globally generating section system of \(B\). Its finite zero-weight FS metric has raw affine weight
\[
 g=\max_j\log|\sigma_j/s_D^r|\quad\text{on }U.
\]
It is nonnegative through the constant branch and dominates \(\log|z_i|\) for EVERY original generator. Polynomial degree bounds therefore dominate any prescribed original finite affine FS exhaustion by \(Ag+C\), with a positive rational \(A\). A growth hypothesis on the original input is retained; the scalar input is not altered.

Write \(g=g_0+p\), with the actual canonical boundary-section reference \(g_0\) and the genuine global FS potential \(p\) on \(B\). The pullback bundle is the actual \(\bar\pi^*B\), not an ample numerical substitute; it is nef and semiample on smooth \(Z\). Its canonical trivial metric and the finite FS formula pull back functorially in the pulled frames. One can see this literally on the product trivial test configuration \(X\times\mathbb A^1\) and its pulled line bundle. Thus the affine reference upstairs is the pullback of \(g_0\), the global FS term is \(\bar\pi^*p\), and the raw weight is \(g\circ\bar\pi\). This is all-value frame compatibility, not identification only on divisorial points.

These constructions supply the geometrical antecedents called GEO in author83 and the accepted round77 smooth upper-growth/principal-removal theorem, on their scheme-theoretic witness domain. They apply separately to each smooth affine open and to its product with \(\mathbb A^1\). The corresponding analytic theorem still retains its contact hypotheses and smooth genuine nef EP input. This new geometric application has not yet passed independent mathematical review, and neither review85 nor the frozen author84 is allowed to treat it as an already granted result.

## 4. A local decreasing net becomes a sequence over countable \(k\)

Suppose now \(k\) is countable. Every finite-type affine coordinate ring is countable. The seminorm topology is the topology induced by all coordinates \(|f|\), \(f\in R\), in a countable product of real half-lines. Its analytic space and every compact analytic domain \(Q\) are second countable. No metrizability is asserted when \(k\) is uncountable.

Here is the exact extraction lemma. Let \(Q\) be second countable, let \((a_i)\) be a directed decreasing net of finite continuous functions on \(Q\), and let \(a=\inf_i a_i\), including possible value \(-\infty\). For each rational \(t\),
\[
 \{a<t\}=\bigcup_i\{a_i<t\}.
\]
Every open subspace of a second-countable space is Lindelöf, so a COUNTABLE subfamily suffices for each \(t\). Collect these indices over all rational \(t\) and enumerate them. Directedness gives increasing indices \(i_j\), with each \(i_j\) above the first \(j\) selected indices and the preceding \(i_{j-1}\). Then \(a_{i_j}\) decreases and its infimum is exactly \(a\): for any \(x\) and rational \(t>a(x)\), one selected open contains \(x\), and its value bounds the sequence eventually below \(t\). This also proves convergence when \(a(x)=-\infty\). It uses open-sublevel covers, not convergence on a dense countable set or uniform convergence at logarithmic poles.

Consequently, IF continuation90's compact local actual-reference affine-FS conversion is correct, its flattened decreasing net on \(Q\) has a decreasing sequence with the SAME pointwise limit over countable \(k\). Each finite raw FS weight has the required finite rational contact form. At a tested point choose one active finite branch; its regular section ratio has nonzero seminorm and is a unit on the corresponding principal Zariski neighborhood. That branch's logarithmic affine support lies below the whole maximum and has the SAME value and SAME additive constant at the point. A floor handles all zero branches. Thus it has precisely the unit-log support property of the accepted contact class, on one common local neighborhood. No subtraction of psh or same-nef-bundle global FS approximation is used.

After all-point fiber constancy and scalar usc descent on a single resolution are independently established, this extraction would put its actual local pulled metric into the sequence form required by the conditional countable affine chain. It does not itself establish fiber constancy, target first membership, target EP or the original equation.

## 5. Exact primary reading and remaining dependence

The cached Temkin0904.1592v2 PDF has SHA256 \(0c5e2f27ff35a48d605ab1573b9acb027b4fd550574855417e643d24336b5cc3\). Its layout text has SHA256 \(c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee\). UTF8 byte decode and one-based inclusive LF83–147,274–405,462–553,1490–1608 were read. This includes the exact Theorem1.2.1 statement, finite blowup-sequence definition, Cartier pullback proof, and the full pertinent main-theorem proof body. The earlier construction and recursively cited resolution algorithms remain published primary background; a complete independent reconstruction of desingularization is not claimed.

Live primary bodies read: Stacks02O2 rendered22–56, including the entire Chow proof and schematic-closure/reduced refinements; 01OF rendered20–56, including the blowup Cartier/twist proof; 01VG rendered69–79, including the ample-pullback-twist proof; 0HA6 rendered61–70, including the finite-type excellence assertion and proof; 01IQ rendered22–26, the entire closed-image immersion proof. Their observations are saved with live URLs and rendered coordinates, not imaginary immutable editions or original-HTML LF pins.

This draft supplies proposed geometric and countable sequence inputs for joining the independently assessed partial chains. It retains the ORIGINAL nonnormal target and generic fiber, uses resolutions only as dominating auxiliary sources, and retains actual line bundles and all analytic values. The decisive resolved-nef fiber descent, singular countable EP, and independent verification of the resulting complete original proof are still required.


# Unchanged original P16.1 full family

{
  "problem": "Original P16.1:\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nComplete unchanged mathematical family:\n\n10     The general non-Archimedean Monge–Ampère equation\nActive items: P16.1, P16.2, P16.3, P16.4, P16.5, P16.6, P16.7. Status: Open in the\nresidual scope.\n\n10.1    Atomic targets\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nP16.2 (T5): Proper nonprojective algebraizable equation theories\nConstruct an appropriate replacement positivity datum and the associated psh, ﬁnite-energy,\ncomparison and equation theory on proper nonprojective algebraizable spaces. A proper\nalgebraic scheme with an ample line bundle is already projective, so retaining that datum\nwhile dropping projectivity is not a new case.\n\nP16.3 (T5): Finite-energy equations in positive residue characteristic\nConstruct the required ﬁnite-energy operator and prove existence and uniqueness when the\noriginal residue-characteristic restriction is removed. Replace the resolution, model-regularity\nand envelope inputs wherever they are used rather than merely changing the standing ﬁeld\nhypothesis.\n\nP16.4 (T4): Finite-energy equations over arbitrary complete valued ﬁelds\nExtend the operator and existence theorem to nondiscrete valuations and arbitrary complete\nnon-Archimedean ﬁelds outside the established invariant-toric, skeleton-supported endpoint.\nA deﬁnition of the ﬁnite-energy space alone does not establish the operator or the equation.\n\nP16.5 (T5): Finite-energy equations for nonample positivity classes\nExtend the equation theory to big or pseudoeﬀective nonample classes, specifying the psh cone,\nreference singularity type, energy and total mass. At zero volume, the existing probability\nnormalization must be replaced rather than retained unchanged.\n\nP16.6 (T4): Arbitrary-support ﬁnite-energy measures\nProve the operator and existence-and-uniqueness theorem for arbitrary ﬁnite-energy measure\nsupport beyond the known toric skeletal regime. Measures must satisfy the correct mass and\nenergy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine\nMonge–Ampère measure by another inverse measure construction.\n\nP16.7 (T5): Finite-energy equations on nonalgebraizable analytic spaces\nConstruct the ﬁnite-energy operator and its existence-and-uniqueness theory on genuinely\nnonalgebraizable analytic spaces, with an explicit positivity datum and the necessary com-\npactness, envelope and comparison replacements.\n\n\n\n\n                                              73\n\n10.2    What constitutes a solution\nFor each axis, state the retained hypotheses and construct the ﬁnite-energy operator together\nwith the corresponding existence-and-uniqueness theorem. Specify the measure mass and\nﬁnite-energy condition, uniqueness modulo constants and the replacement inputs for com-\npactness, envelopes, energy diﬀerentiation and comparison. An endpoint solving a special\ntoric measure class does not remove a general axis.\n\n10.3    Full statement and detailed state of the art\nProblem 10.1. Extend the ﬁnite-energy existence and uniqueness theory for the NA Monge–\nAmpère equation beyond the currently proved combinations of smoothness, projectivity,\nresidue characteristic, valuation, positivity class, support, and algebraizability hypotheses.\n\n    This is not one yes-or-no assertion. Positive characteristic, singular or unibranch varieties,\nnondiscrete valuations, big classes, arbitrary support, and nonalgebraizable analytic spaces\nrequire diﬀerent inputs. The known variational proofs use compactness, envelope regularity,\ndiﬀerentiability of energy, and a comparison principle; deleting a geometric hypothesis is valid\nonly after replacing every place where it enters. The relevant positive results and their distinct\ndomains are surveyed in Book Chapter 28, Book Chapter 29.\n    The projectivity axis has one logical constraint. A proper algebraic K-scheme endowed\nwith an ample line bundle is already projective over K [Stacksb, Tag 0B5N]. Thus P16.2\ncannot mean that one retains the BFJ line-bundle polarization L while simply deleting the\nword “projective.” A nonprojective proper algebraizable extension must ﬁrst replace that\npositivity datum—and then construct the corresponding psh, ﬁnite-energy, and comparison\ntheory—rather than merely rerun the original argument. No canonical replacement with the\nrequired equation theory is asserted here.\n    One exact source-stated axis is especially clean. Pille–Schneider observes that the ﬁnite-\nenergy space can be deﬁned over an arbitrary non-Archimedean ﬁeld, but that the extension of\nthe Monge–Ampère operator is not known there in general; the discretely valued characteristic-\nzero and trivially valued cases are the established endpoints [PS23, Remark 4.4]. This should\nbe solved before bundling all remaining axes into a single theorem.\n\nProposition 10.1 (Arbitrary-ﬁeld invariant toric skeletal endpoint). Let K be a complete\nnontrivially valued non-Archimedean ﬁeld, XΣ a proper toric K-variety, and L an ample toric\nline bundle. If µ is a positive Radon measure on XΣan , is supported on the canonical skeleton\nNΣ , gives zero mass to NΣ \\NR , and has total mass degL (XΣ ), then there is a toric continuous\nsingular psh metric on L whose Monge–Ampère measure is µ. It is unique up to multiplication\nof the metric by a positive constant.\n\n    Thus nondiscreteness and the arbitrary complete ground ﬁeld cause no obstruction in\nthis invariant toric, skeleton-supported range. Here “continuous singular” has the source’s\nextended-valued meaning: local weights are continuous into R ∪ {−∞}, as in [BGGJK25,\n§5.3.1]. It does not imply ﬁnite real-valued weights or ﬁnite energy. This is not an arbitrary-\nﬁeld ﬁnite-energy theorem in the BFJ sense: the result permits a singular potential, requires\ntorus invariance and skeletal support, and does not construct the general extended Monge–\nAmpère operator. In particular, P16.4 and P16.6 retain the respectively nonskeletal and\nnoninvariant ﬁnite-energy residual scopes.\n    There is also a distinct, nonproper algebraic endpoint. Let n > d ≥ 1, let X be a smooth\nprojective Fano complex variety of dimension n, and let D be a reduced simple-normal-crossing\nanticanonical divisor whose dual complex is the standard (d−1)-simplex. For the aﬃne Calabi–\nYau complement X = X \\ D, Wang’s Theorem A constructs a continuous non-Archimedean\npsh function on X an , over the trivially valued ﬁeld C, whose local Monge–Ampère measure\n\n                                               74\n\nis the canonical Lebesgue measure on the essential skeleton [Wan25]. The source is a version-\none preprint and uses a local CLD/tropical–convex construction. In particular, it neither\nconstructs the BFJ ﬁnite-energy operator nor treats arbitrary measures or arbitrary aﬃne\nvarieties. Since X is aﬃne and hence not proper, this endpoint does not answer P16.2; it\nonly records a special nonprojective algebraic solution after the properness requirement is\nalso dropped.\n    There is a separate ﬁnite-atomic inverse statement which must not be called a ﬁnite-energy\nMonge–Ampère theorem. Under its standing assumptions that K is maximally complete and\n|K × | = R>0 , Fang ﬁxes an irreducible projective K-variety with an ample line bundle and a\nﬁnite set of graded birational points on its aﬃne cone. For every probability vector on that\nﬁnite set, the source constructs a Shilov-ﬁnite, possibly singular metric having the prescribed\nequidistribution measure [Fan25, Proposition 4.8]. The source itself says that comparing this\nBanach-algebra measure with the genuine Monge–Ampère measure requires the separate con-\ntinuity property of an envelope metric. Thus it supplies neither a continuous semipositive\nsolution nor the BFJ ﬁnite-energy operator for the prescribed atomic measure, and does not\nnarrow P16.6.\n    There is also a resolved negative regularity chronology. The ﬁrst skeletal-factorization\nquestion of Gubler–Jell–Künnemann–Martin already fails on their toric surface [GJKM19,\nAppendix A]. Boucksom–Jonsson then construct a ﬁnite atomic Monge–Ampère measure sup-\nported on a dual complex whose solution is invariant under no retraction attached to any\nSNC model; they also construct a divisorial Green function that is not Q-PL [BJ24b, Theo-\nrems A and B]. Hence support on a dual complex does not imply factorization through some\nreﬁned skeleton. This is a theorem-level obstruction to a proof strategy, not an open regularity\nexpectation.\n    The Rethlas programme treats each axis separately and ﬁrst searches the post-2020 liter-\nature for an existing theorem. Alterations and universal homeomorphisms can address some\nalgebraic descent questions, but they do not by themselves supply multiplier ideals or dif-\nferentiability in positive characteristic. The unrestricted formulation is open; several strictly\ndelimited axes are already known.\n\n\n\n\n                                               75\n\n",
  "completionCriteria": "Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted."
}


# TASK-GRANTED accepted round77 partial body and binding scope

---
title: "Compact algebraic PL extensions, signed integration by parts, and the smooth gate"
author: "Primary-source reconstruction; unverified mathematical draft"
date: "5 October 2026"
geometry: margin=0.85in
fontsize: 10pt
header-includes:
  - \usepackage{amsmath,amssymb,amsthm}
  - \usepackage{longtable}
---

## 1. Exact target and disposition

The unchanged original P16.1 is **not solved**. Candidate=false. Its complete family and completion criterion remain those of `task-original.json`, reproduced from the preserved input. In particular the criterion is:

> P16.1 (T5): Finite-energy equations on singular or unibranch varieties. Extend the finite-energy non-Archimedean Monge--Ampere operator and its existence-and-uniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in compactness, envelopes, energy differentiation and comparison. State all retained polarization and field hypotheses.

> Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted.

The intended equation domain retains reduced irreducible geometrically unibranch projective varieties over arbitrary algebraically closed trivially valued characteristic-zero fields, ample line bundles, and arbitrary-support finite-dual-energy measures. No smooth special case in this paper replaces that domain. The original P16.2--P16.7 axes also remain unchanged; no result over arbitrary valued fields, nonample classes, or nonalgebraizable spaces is asserted.

This continuation provides new detailed proof drafts for the compact algebraic PL extension and signed-IBP gate, its raw-mass/comparison/domination consequences, and the smooth membership argument. It also gives an explicit route through smooth upper growth and removal, with the geometric witness hypotheses stated. The later singular Runge, envelope, cardinality and normalization chain is not completed. The embedded drafts are mathematical data. No path printed in them was read, and none of their results is imported as an accepted theorem.

Throughout Sections 2--8, $k$ is algebraically closed, trivially valued and of characteristic zero. Except where smoothness is expressly required, $X$ is reduced irreducible projective. $H$ and $L$ denote actual ample rational line bundles, not just numerical classes. Rational PL always means rational slopes and constants. Analytic contact weights mean the following binding hypothesis: on ordinary point neighborhoods the continuous weight is a finite continuous rational-affine selection in finitely many unit logarithms, with an affine local support below it and equal to it at the tested image point. The support inequality and equality have the **same constant**. Finite-floor logarithmic maxima are allowed by deleting inactive zero-coordinate branches before using unit charts. Local decreasing approximants are supplied on one common neighborhood for each finite tuple. These restrictions are substantive: arbitrary positive currents and arbitrary global weak rational approximations are not asserted to satisfy them.

## 2. Compact algebraic extensions on the original variety

### 2.1. Localization and bounded logarithms

Fix a very ample $H$. If $s$ is a nonzero section, then, without normality,
$$\Gamma(D(s),\mathcal O_X)=\varinjlim_m H^0(X,mH)/s^m. \tag{2.1}$$
On a finite affine trivializing cover this is module localization; the finitely many matching equalizers commute with filtered localization. This proves the assertion for the original structure sheaf. Thus inverting finitely many regular functions $\tau_i/s^{d_i}$ gives the literal chart
$$D(a)=D(s)\cap\bigcap_iD(\tau_i),\qquad a=s\prod_i\tau_i. \tag{2.2}$$
The extra factor $s$ retains the old boundary. Every regular function on this chart is $F/a^m$ for a global section of the appropriate power of $H$.

For a global section $F$, let $\mathfrak b_F$ be the coherent ideal locally generated by its coefficient in a center frame. Its logarithmic norm for the canonical trivial metric is $\log|\mathfrak b_F|$. At each analytic point this is independent of the center frame, since changes of center frame are units in its valuation ring. This also follows from BJ 1.24 and the subsequent definition of section evaluation (S1 LF883--900). Therefore
$$A_{F,N}=\max(\log|\mathfrak b_F|,-N)\in\operatorname{PL}(X) \tag{2.3}$$
for positive rational $N$, by the flag ideal $\mathfrak b_F+(t^N)$ after clearing denominators. If $f=F/a^m$ is a unit on a compact set $W\subset D(a)^{\rm an}$, choose rational clipping levels below the minima of both section logarithms on $W$. Then
$$\log|f|=A_{F,N}-m A_{a,N'}\quad\hbox{on a neighborhood of }W. \tag{2.4}$$
The equality is exact. A uniform approximation to a logarithm is not being substituted.

Analytic units can be treated on smaller compact rational domains as well. In the algebraic reduction of published Ducros 3.2 (S9 LF2087--2127), a rational domain is localized at a nonvanishing denominator $h$, and the functions $b/h^r$ in the original ring are dense in its affinoid algebra. For a unit $f$ choose an approximant $g$ with
$$\|f-g\|_W<\min_W|f|.$$
The ultrametric inequality gives $|g|=|f|$ at **every** point of $W$. A finite list is treated simultaneously. The original domain and principal localization are retained. This uses the precise rational-domain density mechanism in that proof, including its finite rational refinements; density of polynomials on an arbitrary analytic open is not claimed. Norm equality remains true after complete field extension because the same uniform inequality and lower bound pull back.

### 2.2. A finite selected weight has an actual PL extension

Suppose a finite continuous rational-affine selection is supplied near a compact set and its used coordinates are unit logarithms there. Choose compact rational neighborhoods inside its original charts with rational upper/lower bounds; their interiors cover the compact set. They are $\Gamma$-strict with $\Gamma=\exp(\mathbb Q)$, even over the trivial field. Ducros 3.2 applies to these **compact**, $\Gamma$-strict spaces and their **invertible** functions. Their logarithmic images are finite rational polytope complexes of dimension at most $\dim X$. No dimension equality is needed.

Refine the images by the finitely many hyperplanes where the selected affine expressions agree. On a relative open convex cell the distinct expressions have a fixed order. Continuity forces the selected expression class to be locally constant, hence constant on that cell. Continuity supplies its affine value on the closed cell. The result is a rational PL function on a finite compact rational polyhedral complex $T$.

Here is an elementary extension, so no unrestricted tropical selection theorem is hidden. Put $T$ in the interior of a rational box. Cut that box by all rational hyperplanes defining its cells and the expression domains, and barycentrically subdivide the resulting finite rational polytopes. This triangulates the box with $T$ as a subcomplex and each affine piece as a union of simplices. Assign the prescribed rational value to each vertex of $T$, assign zero to the box-boundary vertices, and assign arbitrary rational values to the other vertices. Affine interpolation on every simplex, followed by zero outside the box, gives a continuous finite rational PL function $E$ on the whole Euclidean space, equal to the selection on $T$.

Such $E$ is a difference of finite convex rational PL functions. To verify this directly, take all rational supporting hyperplanes $h_j=0$ of its affine cells. Across any wall, continuity makes the gradient jump normal to the wall. There are finitely many jumps. Choose positive rational $C$ so adding $C\sum_j|h_j|$ makes every oriented normal jump nonnegative. Restriction to each generic line is then convex; continuity handles lines through intersections. Hence $E+C\sum_j|h_j|$ is convex and is the maximum of its finitely many rational affine pieces. The penalty is also a finite convex maximum. Thus $E$ is a finite expression using rational affine combinations, maxima and subtraction.

Replace its unit-log coordinates by the actual global PL functions (2.4). BJ's rational PL space is a vector lattice (S1 LF962--1008), so this expression is a global algebraic PL function agreeing exactly with the local selected weight near the chosen compact set. This construction does not require a positive extension. It also does not identify PL on a polytope with PL on the original bundle without constructing the displayed algebraic functions.

### 2.3. Support-controlled gluing without multiplying PL functions

For compact $K\subset U\subset X^{\rm an}$, choose a continuous bump $b$, equal to one on a neighborhood of $K$, with compact support in $U$. Approximate it by a global rational algebraic PL $p$ with error less than $1/8$, using BJ 2.2 and its lattice proof. Put
$$\chi=\min(1,\max(0,2p-1/2)). \tag{2.5}$$
Then $0\le\chi\le1$, it is one near $K$, and
$$\operatorname{Supp}\chi\subset\{p\ge1/4\}\Subset U.$$ 
Outside $U$, $p<1/8$, and the compact threshold set misses the complement of $U$. This proves controlled support, rather than simply extending a bump by zero.

If finitely many local extensions $E_i$ agree with one continuous function $f$ on opens containing $\operatorname{Supp}\chi_i$, and some $\chi_i=1$ near every point of $K$, choose rational $C$ larger than all necessary compact bounds. Then
$$E=\max_i\bigl(E_i-C(1-\chi_i)\bigr) \tag{2.6}$$
equals $f$ near $K$. Indeed a positive $\chi_i$ puts the point in its agreement chart, where its expression is at most $f$; for $\chi_i=0$ the choice of $C$ suppresses the bounded global $E_i$; a winning $\chi_i=1$ gives equality. Only the tested compact neighborhood is used when $f$ is local. For a global $f$ the same argument applies on all of compact $X^{\rm an}$.

Choose another cutoff $\eta$ equal to one near $K$ with support compact in $U$, and rational $B>\sup_{\operatorname{Supp}\eta}|E|$. The compact signed extension
$$\widetilde f=\max(-B\eta,\min(B\eta,E)) \tag{2.7}$$
equals $f$ near $K$, vanishes on a neighborhood of $X^{\rm an}\setminus U$, and satisfies $|\widetilde f|\le B\eta$. Multiplication of two variable PL functions has **not** been used. A product $\eta E$ need not be PL.

Given a finite open cover, choose compact shrinkings $K_i\subset U_i$ covering $X^{\rm an}$ and cutoffs $\chi_i$ as above. The actual rational PL partition is
$$\rho_1=\chi_1,\qquad \rho_i=\min(\chi_i,1-\sum_{j<i}\rho_j). \tag{2.8}$$
Induction gives $\sum_{j\le i}\rho_j=\min(1,\sum_{j\le i}\chi_j)$. Thus every $\rho_i\ge0$, its support is compact in $U_i$, and $\sum_i\rho_i=1$. No variable denominator occurs.

### 2.4. Exact differences in one actual ample class

For any finite list $a_i\in\operatorname{PL}(X)$, BJ 2.25--2.26 gives $a_i=a_i^+-a_i^-$ with $a_i^\pm=c_i^\pm q_i^\pm$, $c_i^\pm\in\mathbb Q_{\ge0}$ and $q_i^\pm\in H(H)$. Choose a common rational $R\ge c_i^\pm$ and set
$$q_{i,R}^\pm=c_i^\pm q_i^\pm+(R-c_i^\pm)0\in H(RH). \tag{2.9}$$
The zero is the actual canonical FS metric on $H$. Tensor products of the generating sections prove the asserted FS membership; denominators are cleared once for the finite list. Thus $a_i=q_{i,R}^+-q_{i,R}^-$ exactly. In original frames $e_\alpha=g_{\alpha\beta}e_\beta$ of $H$, both terms have weights $Rh_{0,\alpha}+q_{i,R}^\pm$ and transition $g_{\alpha\beta}^{NR}$ on the cleared tensor power. Their difference is $a_i$. This is the same algebraic bundle, same cocycle, same reference and same class. Positivity of an abstract numerical class alone is not used.

## 3. Audit and reconstruction of the continuous contact metric bridge

Let a continuous rational contact metric be **already glued** on an ample rational $L$. In a standard very ample frame $e=s_j$ of $qL$, its canonical reference weight is
$$h_{0,j}=q^{-1}\max_l\log|s_l/s_j|,$$
with the $l=j$ term giving a zero floor. Its actual potential is $\phi=b_j-h_{0,j}$, independent of the frame. The finite-floor zero reductions and Section 2 extend its local rational selected weights exactly. Formula (2.6), on the finite compact cover of $X^{\rm an}$, proves
$$\phi\in\operatorname{PL}(X)$$
on the original variety and original $L$.

BJ 2.7/2.31 now supplies an actual algebraic test-configuration line bundle $\mathcal L$ with generic bundle $L$ and model function $\phi$. Take relative integral closure inside that prescribed generic fiber, not absolute normalization. Complete at the test parameter after clearing rational tensor weights over $K=k((t))$, $|t|=e^{-1}$. The model metric is exactly the pullback of the original metric: for a flag ideal its norm is the maximum of the norms of the **separate** ideal generators $a_\lambda t^{-\lambda}$; differences preserve equality. This is an equality at all $K$-analytic points, not only the Gauss section. The model identification uses the original $L$ and its original cocycle.

This is a new resolution of the algebraization dependency in the supplied bridge. GM 2.4 algebraizes a formal blowup ideal, while GM 2.6 cites the separate GK17 8.13 for arbitrary formal line-bundle algebraization (S4 LF249--295). That latter full proof is not in the authorized caches. Here no arbitrary formal line bundle is algebraized: the algebraic test configuration was constructed **first** by BJ's flag-ideal representation. Proper formal-model refinements in the following primary criteria remain background theorems with their precise applications; a title is not presented as their proof.

Over a completed algebraic closure of $K$, pull back a contact support through any smooth analytic curve map into an ordinary weight chart. It becomes
$$h_x=\sum_j a_j\log|f_j|+C,$$
harmonic by Thuillier 2.3.21. If $b-h$ has a local maximum $M$ for any harmonic $h$, then $h_x-h\le b-h\le M$ with equality at $x$. The harmonic maximum principle forces $h_x-h=M$ nearby and then $b-h=M$ nearby. Thuillier 3.1.12 gives subharmonicity. This proves the curve test from supplied local expressions; it does not pull back arbitrary positive currents. For decreasing local approximants, restrict **each** one first and use Thuillier 3.1.8(ii) afterwards. A bounded floor excludes the identically $-\infty$ alternative.

The completed model metric is already rational PL on the original bundle. GR 5.1/5.4, whose full proofs are pinned at S8 LF803--926, therefore give semipositivity on each ordinary point neighborhood. GR's proof lifts the generic reduction point of an entire proper residual curve, retaining the interior condition; its local curve-lifting theorem is pinned at LF489--800. GM 3.11 tests every proper residual curve of the represented global model, using its generic reduction point, a neighborhood and a common dominating model. The closure of that point's reduction remains the **entire** proper curve (S4 LF754--782). GM 3.5 and 3.3 then test nefness on the already supplied algebraic model and detect it before field extension. There is no positivity assertion from a Laurent G-cover alone. GR Remark 1.8 leaves the unrestricted current converse unknown.

BE 7.8 now applies over the nontrivial $K$ to the ample $L_K$. It interpolates the nef model with an ample model of the **same** generic bundle. The resulting semiample models give uniform pure FS approximation. The printed $H/A$ switch in its proof is resolved by using one ample model consistently.

For exact descent, expand each pure FS section on $mL_K$ in the finite $k$-space $H^0(X,mL)$:
$$s_j=\sum_{r\ge r_0}t^r f_{jr}.$$
At the independent-variable Gauss lift of $x$, the FS potential is
$$m^{-1}\max_{j,r}\{\log\|f_{jr}(x)\|_{mh_0}-r\}. \tag{3.1}$$
Every $k$-section has norm at most one in the canonical metric, by its valuation-ring center. The left side is finite continuous on compact $X^{\rm an}$, so has a finite lower bound. Every sufficiently large $r$ term lies uniformly below that bound. The infinite maximum is therefore **exactly** a finite cutoff. Retained coefficients generate, since a common algebraic zero would contradict finiteness and the same tail bound. They are sections of the original $mL$, with rational weights. Uniform errors survive Gauss restriction. BE 7.6 or BJ decreasing closure yields genuine continuous PSH on the original $L$ over $k$.

For a continuous target choose uniform errors $\epsilon_j=4^{-j}$ and shifts $B_j=2\sum_{i\ge j}\epsilon_i$. Then shifted FS approximants decrease, since the consecutive lower bound is $2\epsilon_j-\epsilon_j-\epsilon_{j+1}>0$. This proves the continuous contact bridge without any assertion that every continuous weak metric has global rational weak approximants.

## 4. Genuine collars and bounded local weighted products

The supplied round75 collar is reconstructed, including its reference. On a principal chart (2.2), write the finite defining constraints as $F_j/a^m$. Enlarge $m$ so its tensor power is very ample and append a complete section system; its ratios generate the **original** affine chart ring. Rational strict margins and a negative floor give an actual FS local weight $v$ on a fixed ample $H$, with
$$Q=\{v\le0\}\Subset U,\qquad P=\{v\le-\epsilon\},\qquad x\in\operatorname{int}P.$$ 
If the tensor denominator is $q$, the weight is $q^{-1}\max(q\lambda,\log|F_j/a^m|-C_j)$; the thresholds are $C_j$, not $qC_j$. Generator bounds ensure compactness. Write $v=h_0+p$ in that frame, with $p$ its actual global FS potential and $\omega=c_1(H)$.

Let $u_i$ be a finite tuple of bounded local decreasing contact limits on a neighborhood of $Q$, including a bounded test if needed. Choose rational $M$ bounding the limits there and rational $A$ with $A\epsilon>2M+2$. Put $h=Av+M+1$. On $P$, $h<-M$; on the compact outer strip $v\ge-1/(2A)$, $h\ge M+1/2$. The closed sets $\{u_{ij}\ge M+1/4\}$ on this strip decrease to the empty set. The finite-intersection property gives one common eventual tail strictly below $h$ on the **whole** strip. This is not Dini's theorem for a discontinuous limit.

Define
$$\Psi_{ij}=\max(u_{ij}-h,0)\text{ on }Q,\qquad \Psi_{ij}=0\text{ outside},$$
and
$$\Phi_{ij}=p+A^{-1}\Psi_{ij}. \tag{4.1}$$
Their actual local metric weights on $H$ are $A^{-1}\max(u_{ij}-M-1,Av)$ inside, and $v$ on a whole reference-winning collar and outside. The contact bridge, applied after clearing $A$, proves that these are genuine metrics on the **same** $H$. Their original cocycle is unchanged. The bounded decreasing limits $\Phi_i$ are genuine finite energy by global decreasing closure. On $\operatorname{int}P$,
$$u_i=A\Phi_i+Ah_0+M+1,\qquad
dd^c u_i=A(\omega+dd^c\Phi_i). \tag{4.2}$$
This is the exact reference identity. $\Psi_i/A$ alone is not a canonical-reference potential. The local product is the restriction of $A^n$ times the genuine **raw** mixed measure of the $\Phi_i$.

For continuous inputs this equals the continuous local product: BJ 7.23 invokes actual BE 8.18, whose proof and fundamental-cycle conventions are pinned; BJ 7.42 supplies continuous locality. CLD 8.7.2 is used only within its continuous locally-uniform premise (S3 LF10432--10449). For bounded decreasing inputs, use BJ 7.19/7.21 on the actual global $\Phi_{ij}$.

Independence is checked on a third smaller shared collar. At every continuous stage the old and smaller collar products agree on their common inner open, because their actual weights and scaling agree there. Pass both genuine decreasing limits against compact continuous tests. In the shared collar different supplied sequences have the same explicit global limit $\max(u_i-h,0)$, zero outside. Their genuine measures therefore agree. This proves sequence, collar and reference independence; the local positive Radon measures glue.

For the bounded test, (4.2) is a genuine decreasing potential plus a fixed continuous local reference. BJ 7.21 supplies weighted convergence for its genuine part; ordinary weak convergence supplies the reference part against compact cutoffs. In that source the correct identity is the test-containing pairing **minus** the zero-test pairing (S1 LF4108--4113); the opposite signs at LF4119--4123 are a printed error. Translate the test below zero, apply the positive weighted-measure lemma to its negative, and subtract in the correct order. Signed tests that are differences of such bounded weights are treated term by term; their difference need not decrease.

## 5. Compact signed IBP from actual global pairings

Let $a$ be a rational algebraic PL test with support $K\Subset U$, and let $u_0,u_1,\ldots,u_{n-1}$ be bounded local contact limits on a common neighborhood of $K$. Choose one genuine collar for the finite tuple and an additional compact cutoff equal to one near $K$. For $a=q^+-q^-$ use (2.9) in one actual ample class $RH$. The positive global mixed measures obtained by adding $q^+$ or $q^-$ separately need **not** be supported in $K$. Their **difference** is: on the open complement of $K$, $a=0$, so $q^+=q^-$ and genuine mixed locality makes their measures equal there. The same argument works on every open where $a$ is constant. Cancellation is retained before any outside contribution is discarded.

For each collar, extend the local reference term in (4.2) to a compact signed algebraic PL $G_0$ agreeing with $Ah_0+M+1$ near $K$, using Section 2. Then
$$F_0=A\Phi_0+G_0\in\widetilde{\mathcal E}^{1}$$
is an actual global signed finite-energy function and equals $u_0$ near $K$. The zero-class curvature of $F_0$ agrees there with $dd^cu_0$. To verify the reference cancellation, do it first for the continuous collar approximants, using continuous local compatibility. The difference of the reference curvature and the curvature of the matching $G_0$ is zero on the same open. Pass the bounded genuine mixed limits in each positive term. Thus that cancellation still holds with the discontinuous bounded other factors.

The symmetric global mixed pairing now gives
$$\int_U a\,dd^cu_0\wedge\bigwedge_{i=1}^{n-1}dd^cu_i
=\int_U u_0\,dd^ca\wedge\bigwedge_{i=1}^{n-1}dd^cu_i. \tag{5.1}$$
Precisely, both sides are the global pairing with the two zero-class entries $(0,a)$ and $(0,F_0)$ in opposite orders, multiplied by the other collar scaling factors. The left test vanishes outside $K$; the signed measure on the right vanishes there by the cancellation just proved. Every remaining integral is of bounded functions over a compact set against finite signed Radon measures. This proves compact IBP without first assuming a weak/global theorem.

One can equivalently prove (5.1) at continuous stages and pass each positive global mixed term using weighted convergence from Section 4. The total variations are bounded by the sum of their fixed positive raw intersection masses. No discontinuous local limit is called locally uniform. No difference of decreasing sequences is called decreasing. Extension of each $u_i$ on all of $U$ is neither needed nor asserted; matching near the controlled support suffices.

## 6. Raw mass, comparison, domination, and smooth membership

### 6.1. The support-controlled telescope

Let $\phi$ be bounded on $X^{\rm an}$, locally a contact limit relative to an actual continuous rational semipositive reference on $L$. For notation first take the canonical reference and write $T=\omega+dd^c\phi$, $T_0=\omega$, and
$$S=\sum_{j=0}^{n-1}T^jT_0^{n-1-j}.$$
These are locally defined products, not presumed global genuine products. Choose a finite common-neighborhood cover and (2.8). In each chart use the **same** local reference $g_i$ for $\phi+g_i$ and $g_i$. Subtract their compact IBP identities:
$$\int\rho_i(T^n-T_0^n)=\int\phi\,dd^c\rho_i\wedge S. \tag{6.1}$$
The signed measures on the right have support compact in that chart, and their weighted integrals agree on overlaps by the genuine-collar construction. Summing is legitimate for this finite cover. Locally, multilinearity gives
$$\sum_i dd^c\rho_i\wedge S=dd^c1\wedge S=0.$$
Consequently the global positive local product has raw mass
$$\int_{X^{\rm an}}T^n=\int T_0^n=(L^n)=V. \tag{6.2}$$
Replacing one factor at a time proves mixed mass $(L_1\cdots L_n)$ with actual rational reference bundles. For a noncanonical semipositive reference, use its actual local weights in both subtracted terms; its genuine reference product has the same raw intersection mass. This is a proof of mass, not probability normalization by definition.

### 6.2. Winning loci and comparison

On a shared collar the two floors are inactive on the inner open and
$$\Psi_{\max(u,v)}=\max(\Psi_u,\Psi_v).$$
Genuine BJ 7.40 therefore proves strict winning-locus locality for the bounded local products, including their Borel winning sets. Equal raw masses (6.2), positivity and $\max(\phi,\psi-\epsilon)$ give
$$\int_{\{\phi<\psi\}}T_\psi^n\le\int_{\{\phi<\psi\}}T_\phi^n. \tag{6.3}$$
Letting $\epsilon\downarrow0$ uses ordinary continuity from below of the Borel measures. There is no envelope assumption in this step.

### 6.3. Divisorial order and an atom test without a Dirac equation

If two bounded locally psh potentials with the same reference satisfy $\phi\le\psi$ at every BJ divisorial point, take their shared collar. On divisorial points inside $Q$ their genuine truncations are ordered; outside $Q$ both are zero. BJ 4.22 orders those global genuine potentials everywhere. Recovering their inactive-floor weights on $P$ proves $\phi\le\psi$ at every point. Density plus usc is not the argument.

Fix any BJ divisorial point $v$. BJ 1.20 realizes it as a central component on an actual relatively integrally closed test configuration; dominate the trivial configuration. BJ 2.33 gives an ample model of the original $L$ on this determination. Its genuine rational FS potential $b$ has raw measure with a strictly positive atom at $v$:
$$m_v=b_E(\mathcal L|_E)^n>0.$$ 
The entire component $E$, its multiplicity $b_E=\operatorname{ord}_E(t)$, and its ample intersection degree are retained. A measure equal to a single Dirac and an inverse equation are unnecessary.

Suppose $\phi\le\psi$ almost everywhere for $T_\psi^n$. Translate $b$ so $b<\phi$ uniformly, possible because both are bounded. For rational $t\in(0,1)$ put $\phi_t=(1-t)\phi+tb$. Local mixed positivity yields $T_{\phi_t}^n\ge t^nT_b^n$. Since $\phi_t<\phi\le\psi$ almost everywhere for $T_\psi^n$, (6.3) and (6.2) imply
$$V\le\int_{\{\phi_t<\psi\}}T_{\phi_t}^n\le V.$$
Thus the complement has zero mass and the positive atom forces $\phi_t(v)<\psi(v)$. Let $t\downarrow0$ and use the divisorial order argument. This proves bounded local domination. It does not assume the local cone already equals the genuine cone, and does not invoke a Dirac solution.

### 6.4. EP supplies the first genuine membership

Assume the genuine ample class has EP. For a bounded usc locally psh $\phi$, take the directed decreasing net of all continuous majorants with common bounds, allowing finite minima. Compact Hausdorff separation proves its pointwise infimum is $\phi$; a sequence is not assumed. EP and BJ 5.17 give continuous genuine envelopes $p_j=P(f_j)$. They belong to the local contact class: on the actual rational $L$ they have uniform rational FS approximants, shifted into decreasing sequences as in Section 3. BJ 13.1, under its explicit EP hypothesis, gives $f_j=p_j$ almost everywhere for $T_{p_j}^n$. Hence $\phi\le p_j$ there, and the **local** domination just proved yields $\phi\le p_j\le f_j$ everywhere. Genuine decreasing closure proves $\phi=\inf_jp_j$ is genuine.

In particular BJ 5.20 supplies this EP premise on smooth projective $X$ in characteristic zero, proving smooth local/global equality for the stated exact local class. For unbounded inputs, floor relative to the same actual semipositive reference and let the floor decrease. For a rational nef bundle with an actual continuous semipositive reference, add $\epsilon A$ with its specified FS reference, apply the smooth ample result, and use BJ varying-class closure as $\epsilon\downarrow0$. The local weights are literally the old weight plus $\epsilon h_A$; a numerically nef class alone would not identify them.

This is the first-membership step missing from the old upper-growth attempt. BJ 12.18 is applied only **after** this step.

## 7. Smooth weak upper growth and controlled removal

This section records the analytic deduction with its geometric background explicit. A weak input $u$ on smooth irreducible affine $Y$ is supplied with one proper birational witness whose pullback is locally a decreasing contact limit, and is finite at the generic trivial seminorm. Assume the usual characteristic-zero compactification, projective domination and resolution construction, yielding a smooth projective $X\supset Y$, an effective ample boundary, and a smooth projective morphism $\bar\pi:Z\to X$ dominating that **one** witness over $Y$. These are standard geometric resolution/Chow inputs, not consequences of the analytic proof or pinned Stacks webpages; no full proof of them is claimed in this deliverable.

For completeness the boundary sign is determined: a boundary blowup has effective exceptional $E$ with $-E$ relatively ample. If $D$ is the old ample boundary and the center is supported there, $m\pi^*D-E$ is ample for large $m$ and effective with positive coefficient on every new boundary component. Iterating retains exactly $X\setminus Y$ as support. Choose $B=\mathcal O(rD)$ very ample, its boundary section $s$, and a rational complete FS metric $h=h_0+p$. Shift so
$$g=-\log\|s\|_h=g_0+p\ge1.$$
It is a proper exhaustion tending to infinity at the boundary. Localization (2.1) expresses every original generator and each regular branch of an AFS upper bound as $F/s^d$. Finite section-norm bounds give $\log|F/s^d|\le dg+C_F$. Thus the assumed **upper** growth $u\le H+C$ implies $u\le Ag$ for a rational $A$. The printed lower-growth convention in Wu is not used.

For rational $c>1$ and $M<0$ define, relative to the actual nef metric $cA\bar\pi^*h$,
$$\Psi_M=\max(\bar\pi^*u-cA\bar\pi^*g,M)\text{ over }Y,
\qquad\Psi_M=M\text{ elsewhere}. \tag{7.1}$$
The bound is at most $-(c-1)A\bar\pi^*g$, so each floor has a whole constant boundary collar. Its actual local weights are contact limits with that fixed pulled reference. Section 6.4 on smooth $Z$, including its nef reference argument, gives genuine membership. Let $M\downarrow-\infty$. The limit is nontrivial because the original input is finite at its generic point.

The canonical potential is $Q_M=\Psi_M+cA\bar\pi^*p$. BJ 5.13 applies to the smooth target $X$ with class $cA c_1(B)$: approaching larger **target-side** ample classes have smooth EP. The descended genuine $Q$ equals
$$Q=u-cAg+cAp=u-cAg_0\text{ on }Y,$$
and is $-\infty$ on the boundary, by literal pullback equality and analytic surjectivity. Only now apply BJ 12.18(iii) and Example 3.9 to obtain a decreasing rational FS sequence on the **same** $cAB$. In the boundary-section frame the weights decrease to $u$. Append the constant branch and a complete sufficiently high very ample section system with low rational weights, dominated by each continuous metric on compact $X^{\rm an}$. The values do not change. Their ratios retain every original affine generator. This is actual upper-growth AFS regularization, with exact values and original ring.

### 7.1. Controlled bounds by expanding collars

For an already AFS-regularizable $v\le g$, first compactify the actual AFS reference $g$: clear its positive slopes, include their integer powers **and** all original generators at dominated low weights, and take the projective closure. Its standard chart is exactly $Y$. Powers alone would not establish this.

Take rational $C_r\downarrow-\infty$, $R_r\uparrow\infty$ with $R_r>2-C_r$, and an increasing subsequence of supplied approximants $v_{j_r}<g+1$ on $\{g\le R_r\}$. The latter choice follows from decreasing compact superlevel-set emptiness. Set
$$\phi_r=\max(v_{j_r}-2g,C_r)\text{ on }\{g\le R_r\},\qquad
\phi_r=C_r\text{ outside}. \tag{7.2}$$
The continuous contact bridge gives genuine metrics in twice the actual reference bundle; the outer reference wins on a whole collar. On the expanding annulus the new first branch is at most $1-g\le1-R_{r-1}<C_{r-1}$, and the old function is its old floor. This proves the global decrease, including that annulus. The limit is $v-2g$ on $Y$, and $-\infty$ on the boundary.

Uniform rational FS approximation with summable shifts gives a decreasing FS sequence converging to these truncations' limit. After exact original-generator conversion its affine weights $w_r$ satisfy
$$w_r\downarrow v,\qquad w_r\le2g+B$$
for one constant $B$. Equivalently one can first use genuine decreasing closure for the limit in (7.2), then genuine same-class regularization and a common upper bound on its first approximant. No smoothness or singular EP is used in this controlled step.

### 7.2. Principal-open removal and the values on the original witness

Let $f\ne0$ and let $v$ be actual AFS-regularizable on $Y_f$, bounded above by an AFS reference $g$ from $Y$. For rational $c>0$ take
$$g_c=\max(g,-(c/3)\log|f|)$$
as an actual AFS exhaustion of the original localized ring, including $f^{-1}$. Controlled approximants $w_i\le2g_c+B$ give
$$w_i+c\log|f|\le\max(2g+c\log|f|,(c/3)\log|f|)+B. \tag{7.3}$$
On every bounded neighborhood of $Z(f)$ the right side tends to $-\infty$. Floors $D_i\downarrow-\infty$ make $b_i=\max(w_i+c\log|f|,D_i)$ continuous contact functions on $Y$, equal to $D_i$ on an actual neighborhood of each removed point. Polynomial degree bounds give one AFS $h\ge1$ on $Y$ dominating all $b_i$. Applying whole-floor collars to $b_i-2h$ puts each in the same genuine ample class on the reference compactification. Their decreasing limit and genuine sequential regularization prove an actual AFS extension of
$$v_c=v+c\log|f|\text{ on }Y_f,\qquad v_c=-\infty\text{ on }Z(f).$$

Now use smooth EP, rather than incorrectly assuming these $v_c$ decrease as $c\downarrow0$. On the smooth ample-boundary compactification put their canonical potentials in one fixed ample class, subtracting a common large multiple of $g_0$. The genuine tail envelopes $(\sup_{j\ge m}Q_j)^*$ decrease. On $Y_f$, with $a=\log|f|$ finite,
$$\sup_{j\ge m}c_j a=c_m\max(a,0),$$
including its generally unattained zero value when $a<0$. Their limit is a genuine extension of $v$ with the original upper bound, and a same-class sequence gives its actual AFS regularization.

Exact uniqueness, including agreement with a given original weak $u$, uses **the same original resolved witness**. Pull back the regularized extension and $u$ there. Every divisorial point of that integral birational witness has generic algebraic support; since $f$ is nonzero in its function field, it lies over $Y_f$. Thus the two functions agree at all those points. Near any tested point floor both local functions by the same constant, use the same reference and genuine collar, and apply the divisorial order argument of Section 6.3 in both directions. Let the floor tend to $-\infty$. Their values agree at every tested analytic point, including the removed and exceptional sets. Neither dense-open equality plus usc nor an assertion about lifting a prescribed net is used.

The analytic smooth gate in this section is therefore established under the explicitly retained standard geometric witness construction. It is not a general-field affine theorem over every completed residue field.

## 8. Independent nonflat trace audit and its present limit

The embedded norm-law proposals can be checked algebraically without assuming a weak-trace theorem. Let $A$ be normal integral and $B$ finite integral over it, both finite type in characteristic zero, and set $d=[\operatorname{Frac}B:\operatorname{Frac}A]$. For finite module generators $b_i$, the generic norm $N(\sum T_i b_i)$ and all characteristic coefficients lie in $A[T]$: their conjugate products are integral and belong to the fraction field, and $A[T]$ is normal. Translation by every module relation, multiplication, homogeneity, and Cayley--Hamilton are polynomial identities, valid generically and hence over $A$. Tensoring a finite presentation is right exact, so they define the specialized law on every $B\otimes_A\mathcal H(s)$, including new fiber relations.

Over an algebraic closure of $\mathcal H(s)$, its unit-group character is trivial on the nilpotent units. Indeed the finite polynomial logarithm identifies them with an additive vector group, which has no invertible nonconstant polynomial character. On the residue torus, comparison in $P(xy)=P(x)P(y)$ gives one monomial. Polynomiality gives nonnegative integer exponents and homogeneity makes their sum $d$. Every exponent is positive: otherwise the idempotent zero on that factor and one elsewhere would have nonzero norm and hence be invertible by the specialized characteristic identity, a contradiction. Multiplying an exponent by the separable residue degree gives canonical integers $m_y>0$ on the actual analytic fiber, summing to $d$. Unique norm extension over complete fields and residue-factor degree sums prove compatibility with every complete residue-field extension. On the flat locus these are usual Artinian length times residue degree; nonflat fiber dimensions are not substituted.

For $u=D^{-1}\max_i(\log|b_i|+w_i)$, with a constant floor, expand the actual polynomial $N(\sum T_i b_i)=\sum a_\alpha T^\alpha$. Multiplicativity of arbitrary-radius weighted Gauss norms yields the **whole-base** identity
$$\sum_y m_yu(y)=D^{-1}\max_{|\alpha|=d}\left(\log|a_\alpha|+\sum_i\alpha_iw_i\right). \tag{8.1}$$
The constant-floor coefficient is nonzero. Original base generators are retained by appending dominated branches, using their polynomial expressions in retained source generators. Thus this is actual AFS. The weight bound gives $\|N_\pi a-N_\pi b\|_E\le d\|a-b\|_{\pi^{-1}E}$; only a **continuous** decreasing limit invokes compact Dini. A trace of a clopen indicator is continuous and integer valued, hence locally constant; disconnected opens need not share its integer.

Here are the two necessary elementary details. For weighted Gauss multiplicativity, choose the lexicographically largest exponent among maximal-weight terms in each polynomial. Their sum has a unique contribution among pairs of maximal-weight terms: equality of the sum with a different pair would force one exponent to exceed its selected lexicographic maximum. Lower-weight pairs cannot cancel that coefficient. This works at arbitrary positive real radii, including those outside the coefficient field's value group.

To justify continuity also for a clopen indicator or any continuous input on a compact preimage, differences of actual AFS form a rational vector lattice: positive sums and maxima distribute, and $\max(a-b,c-d)=\max(a+d,c+b)-(b+d)$. Generator branches at sufficiently low intercepts make rational constants available on the compact set. Truncated norms of a distinguishing regular function separate its seminorms. For a continuous target, approximately interpolate at each pair $x,y$ using separation and rational scaling; a finite maximum over $y$ supplies its lower bound everywhere and upper bound near $x$, and a finite minimum over $x$ supplies both bounds everywhere. Thus these differences are uniformly dense there. Their traces are continuous by (8.1), and the degree bound passes continuity to the limit. Applied to an indicator of a clopen piece over an open base neighborhood, its trace is exactly the integer sum on that piece. Only local constancy follows.

As an exact diagnostic, $A=k[x,y]$, $I=(x,y)$ and $B=A\oplus Iz$ inside $z^2=x$ has generic degree two but fiber dimension three at the origin. Its norm is $N(a+uz)=a^2-xu^2$, which specializes to $a(0)^2$. Its sole fiber point has canonical weight two, not three.

This audit proves the finite logarithmic test formula; it does not itself identify an arbitrary weak trace at every nonflat point. Section 7 supplies the smooth open regularization/removal prerequisite in its retained geometric setting. To finish the whole weak trace application, the normalized line slice, proper lift to the single witness, local Gauss map $t=cz^e$, all residue-field refinements, and the limiting equality must be checked together for that input. The embedded radial proof remains a proposed application, not an automatically accepted theorem. In particular no affine regularization theorem over arbitrary $\mathcal H(s)$ follows from Section 7.

## 9. Genuine global equation theory and remaining singular obligations

BJ's conventions (S1 LF435--469) allow reduced nonnormal varieties, and Section 7 explicitly resumes general projective scope (LF3649--3658). Its genuine finite-energy operator is available on that scope. On a relatively integrally closed test configuration its raw model measure is
$$\sum_E b_E\bigl((\omega_{\mathcal X}+D)|_E\bigr)^n\delta_{v_E},\qquad
b_E=\operatorname{ord}_E(t),\quad v_E=b_E^{-1}\operatorname{ord}_E|_{k(X)}.$$ 
The fundamental-cycle multiplicities and vertical DVRs are essential. The generic fiber is the original nonnormal variety. BJ 7.18 extends the actual mixed intersection pairing to a positive Radon operator; 7.19 gives raw mass $V=(L^n)$ and genuine decreasing continuity. This is not an auxiliary inverse measure construction.

Write
$$E_\omega(\phi)=\frac{\langle(\omega,\phi)^{n+1}\rangle}{(n+1)V},\qquad
\mathcal E^1=\{\phi\in\operatorname{PSH}(\omega):E_\omega(\phi)>-\infty\}.$$
The exact raw target is a positive Radon $\nu$ with $\nu(X^{\rm an})=V$ and, for $\mu=\nu/V$,
$$E_\omega^\vee(\mu)=\sup_{\psi\in\mathcal E^1}\left(E_\omega(\psi)-\int\psi\,d\mu\right)<\infty.$$ 
BJ 9.20 equates this intrinsic condition with integrability of every genuine finite-energy potential on irreducible $X$; there is no support restriction. BJ 10.4/10.6 give uniqueness modulo one real constant and genuine domination without EP.

Existence is not unconditional on singular $X$. The actual general-variety theorem is BJ **12.8**, equating genuine EP with onto finite-energy MA. Under EP its proof takes a normalized dual maximizing sequence, uses weak PSH compactness, a bounded-energy estimate and target integral continuity (9.19), then energy usc to get an actual maximizer. Genuine energy differentiation identifies its MA. The raw objective $VE-\int\phi\,d\nu$ is constant invariant exactly at mass $V$. This proves existence on smooth $X$ using 5.20, but requires a proved singular EP on the requested target.

The remaining chain is concrete:

1. Complete the weak whole-base trace application just identified, then reprove the split-piece maximum principle with the original witness, fixed hull neighborhood, positive canonical weights and a locally constant integer sum on **all** subsequently tested fibers. Complete descending-$Z$, strict Hartogs and reduced-singular-stratum inductions, with Runge before coefficient radii and the final empty-$Z$ globalization.
2. Establish resolved-nef fiber constancy using actual varying-class metric references and curve-morphism restrictions, geometrically connected fibers over every completed residue field, and the divisorial minimum-usc descent. The supplied Stacks paraphrases have not been promoted to pinned primary proofs.
3. Obtain countable rational geometrically unibranch EP. Wu v1's complete envelope proof at LF2697--2755 expressly invokes its Proposition 2.24 and weak/global Theorem 6.5 at LF2705--2717. Its printed statement is not an independent validation of those gates.
4. Complete finite-data descent to arbitrary algebraically closed trivial $k$, preserving nonnormal generic fibers, relative integral closure, vertical $R_1,S_2$, component multiplicities, positive raw mass, orthogonality and domination. Individual finite PL/model obstacles and competitors may use different countable enlargements; arbitrary PSH competitors do not simultaneously descend.
5. Prove target-side approaching EP before normalization onto; retain the degree-one fundamental-cycle projection, continuous pairing compatibility, and unbounded $\mathcal E^1$/MA compatibility. Then apply the actual singular compactness/differentiation/attainment theorem to every target above.

These are indispensable missing applications, not nonexistence results and not a counterexample to corrected upper growth. The printed lower-growth quadratic diagnostic is not used to reject EP. An abstract completion or the finite trace law does not solve P16.1. No original problem is declared closed.

## 10. Reproduction, evidence, and epistemic status

Run `python3 rerun.py` in this workspace. It preserves `input.json` byte identically as `input-original.json`, retains the exact task value and assignment string, checks all 23 supplied primary-file hashes, copies only authorized sources, and pins 43 literal statement/proof units. Inclusive one-based coordinates use UTF-8 bytes decode and `split('\n')`. Source versions, whole-file hashes, literal bodies, applications and limits are in `source-extracts/source-provenance.json`.

Existing Pandoc generates `P16.1-paper.tex`; existing pdfLaTeX runs twice to create `P16.1-paper.pdf`. Exact argv, stdout/stderr, both pass logs, environment versions and output hashes are retained. The finite checks concern the PL saturation partition, compact clipping, collar margins, summable shifts and quadratic norm identity on explicitly declared finite rational grids. They are exhaustive only there. Compilation, matching hashes and finite arithmetic are **observations**, not mathematical correctness certificates.

`status.json` has exactly `id`, `status`, `exact_result`, `proof_file`, `concrete_gaps`. `canonical-notes.json` has at most four backward-supported local notes. All mathematical arguments and combined primary applications remain unverified drafts; no independent review is claimed. Only the supplied input, authorized primary caches and fresh workspace were read. No installation, other worker/model/subagent, network request, private/campaign read, source edit, message or runtime/auth change was used. No resource-heavy computation was needed. No supervised compute service was exposed.

## Primary bindings

S1: Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, 1801.08229v4. S2: Wu, *On the local theory of non-archimedean psh functions*, 2609.27610v1, public September 2026 v1. S3: Chambert-Loir--Ducros, 1204.6277v2. S4: Gubler--Martin, *On Zhang's semipositive metrics*, 1608.08030v3. S5: Wanner, 1801.04713v3. S6: Thuillier thesis, tel-00010990v1. S7: Boucksom--Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*, 1805.01016v3. S8: Gubler--Rabinoff, *On semipositive piecewise linear functions in non-archimedean analytic geometry*, 2503.05513v1. S9: Ducros, published *Confluentes Mathematici* 4(4), 1250007, DOI10.1142/S1793744212500077. S10: Gubler--Jell--Rabinoff, *Forms on Berkovich spaces based on harmonic tropicalizations*, 2111.05741v3.


# TASK-GRANTED accepted round77 partial body and binding scope

{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Constructed exact compact algebraic rational PL extensions, support-controlled partitions and same-bundle FS differences. These give an algebraic representation first for supplied continuous contact metrics, avoiding the arbitrary-formal-line-bundle algebraization gap. Arbitrary weak metric approximation is not established.",
      "detailedSummary": "For reduced irreducible projective varieties over algebraically closed trivially valued characteristic-zero fields, finite rational selected unit-log weights admit exact compact algebraic PL extensions through original-ring localization, compact norm-image subdivision and saturation cutoffs. Finite signed tests decompose into genuine FS metrics in one actual ample bundle with the original cocycle. A supplied globally glued continuous rational contact metric is first represented algebraically using BJ flag ideals; ordinary-neighborhood curve tests then establish nefness of its represented Laurent model. Same-class approximation and an exact Gauss cutoff give genuine membership. All combined applications remain unverified proof drafts.",
      "text": "Retain k algebraically closed, trivially valued and characteristic zero, X reduced irreducible projective, and actual ample rational line bundles. The contact hypothesis is binding: on ordinary point neighborhoods a continuous weight is a finite rational-affine selection in analytic-unit logarithms, and at each image point it has an affine support below it and equal there with the SAME constant. Finite-floor maxima handle zero coordinates by deleting inactive branches. This does not assert an unrestricted positive-current converse.\n\nThe new compact extension construction retains the original ring. For a very ample H and a nonzero section s, section localization gives Γ(D(s),O_X)=colim_m H⁰(X,mH)/s^m without normality. On a finite affine trivializing cover this is module localization; the finite matching equalizers commute with filtered localization. If inverted functions are τ_i/s^{d_i}, a=s∏τ_i gives precisely D(a)=D(s)∩⋂D(τ_i). Every regular function on that chart is F/a^m for an appropriate global section F.\n\nLet b_F be the ideal locally generated by a section's coefficient. Its logarithmic ideal norm equals its section norm for the canonical trivial metric, evaluated in a valuation-ring center frame. Consequently A_{F,N}=max(log|b_F|,-N) is an actual global BJ rational PL function, represented by a flag ideal after clearing rational denominators. If f=F/a^m is a unit on a compact W, clipping levels below the minima of the two section logarithms give log|f|=A_{F,N}-mA_{a,N'} exactly on a neighborhood of W.\n\nAnalytic units can first be replaced by regular functions with identical norms on smaller compact rational domains. Published Ducros Theorem 3.2's algebraic reduction localizes at a nonvanishing denominator h and uses density of functions b/h^r in the original affinoid algebra. Choose g with ||f-g||_W<min_W|f|. The ultrametric inequality gives |g|=|f| everywhere on W, also after complete field extension. This is an application on its specified rational domains, not polynomial density on arbitrary analytic opens.\n\nChoose compact rational neighborhoods inside the supplied unit charts, with rational strict margins. They are Γ-strict for Γ=exp(Q). Ducros 3.2 gives finite rational polytope complexes as their unit-log images, of dimension at most dim X. Refine by branch-equality hyperplanes. On each relative open convex cell the distinct affine values have fixed order; continuity makes the selected expression class locally constant, hence constant. Its affine value extends to the closed cell.\n\nTo extend that selected function, put the finite rational complex T inside a rational box, cut by its finitely many defining hyperplanes, and barycentrically subdivide. T and every affine piece become subcomplexes. Give T's vertices their prescribed rational values, box-boundary vertices zero, and other vertices arbitrary rational values. Affine interpolation, followed by zero outside the box, is a continuous finite rational PL extension E. It is a difference of convex rational PL functions: adding C∑|h_j| for the finitely many wall hyperplanes, with sufficiently large rational C, makes every normal gradient jump nonnegative. Generic-line restrictions are convex, and continuity handles intersections. Both convex functions are maxima of finitely many rational affine expressions. Substituting the exact global PL logarithms above therefore produces an actual global algebraic PL extension.\n\nSupport is controlled without multiplying variable PL functions. For compact K⊂U choose a continuous bump b=1 near K supported compactly in U. BJ PL density gives rational PL p with ||p-b||<1/8. Then χ=min(1,max(0,2p-1/2)) is one near K and Supp χ⊂{p≥1/4} compactly contained in U. If local extensions E_i agree with f on neighborhoods of Supp χ_i and some χ_i=1 near each point of K, then max_i(E_i-C(1-χ_i)) equals f near K for a sufficiently large rational C: positive cutoffs lie in agreement charts; zero-cutoff branches are suppressed by the compact bounds. A further cutoff η=1 near K gives the compact signed extension max(-Bη,min(Bη,E)), with |extension|≤Bη, equal to f near K and zero near the complement of U. Products such as ηE are not used.\n\nFor a finite cover choose compact shrinkings and these χ_i. Set ρ_1=χ_1 and ρ_i=min(χ_i,1-∑_{j<i}ρ_j). Induction gives ∑_{j≤i}ρ_j=min(1,∑_{j≤i}χ_j); thus the ρ_i are nonnegative rational PL, subordinate with compact support, and sum to one. No variable denominator occurs.\n\nEvery finite signed PL list decomposes in one actual ample class. BJ2.25–2.26 gives a_i=c_i⁺q_i⁺−c_i⁻q_i⁻ with q_i⁺,q_i⁻ in H(H). Choose common rational R≥c_i⁺,c_i⁻ and replace each term by c_i q_i+(R-c_i)0 in H(RH). Tensor-product generating sections verify FS membership. Both metrics use the same RH, canonical reference and original cleared transition functions g_{αβ}^{NR}; their difference is exactly a_i. Numerical nefness alone is not substituted for these actual metrics.\n\nThere is consequently an algebraic-first bridge for an ALREADY glued continuous rational contact metric on ample L. In standard very ample frames its canonical reference weight is a finite logarithmic maximum with a zero floor. The preceding local extensions and maximum-penalty gluing show that its canonical potential φ is globally in BJ PL(X). BJ2.7/2.31 represents φ by an actual test-configuration bundle with generic bundle L, taking relative integral closure inside the original generic fiber. Completing at t over K=k((t)), |t|=e⁻¹, gives precisely the pulled metric: for flag ideals its norm is the maximum over separate ideal generators a_λt^{-λ}. Thus the algebraic model exists before nefness is tested.\n\nThis avoids the unchecked arbitrary-bundle algebraization step: GM2.4 algebraizes a formal blowup ideal, whereas GM2.6 cites GK17 Proposition8.13 for the separate formal-line-bundle converse. That latter full proof is not in the authorized caches. No arbitrary formal bundle is algebraized in this construction.\n\nFor any smooth analytic curve map over a completed algebraic closure of K, a pulled contact support h_x=∑a_j log|f_j|+C is harmonic by Thuillier2.3.21. If b-h has a local maximum M for harmonic h, then h_x-h≤b-h≤M with equality at x. The harmonic maximum principle makes h_x-h=M nearby and forces b-h=M nearby. Thuillier3.1.12 gives subharmonicity. Each continuous approximant is restricted first; Thuillier3.1.8(ii) is then used for decreasing limits, with bounded floors excluding the identically-minus-infinity alternative.\n\nThe metric is already represented PL. GR5.1/5.4 therefore gives semipositivity on ordinary point neighborhoods. GM3.11 tests every entire proper residual curve at a point reducing to its generic point, retaining its interior condition and a common dominating model. GM3.5/3.3 tests nefness on the represented model and detects it before extension. Positivity is not inferred from a Laurent G-cover alone, and GR Remark1.8's unknown current converse is not used.\n\nBE7.8 interpolates the nef model with an ample model of the SAME generic L_K and gives uniform pure FS approximation. Expand its sections s_j=∑_{r≥r₀}t^r f_{jr} in H⁰(X,mL). At an independent-variable Gauss lift the potential is m⁻¹max_{j,r}(log||f_{jr}||_{mh₀}−r). Every k-section has canonical norm at most one. The finite continuous potential on compact X_an has a finite lower bound, so all sufficiently large r terms lie uniformly below it and can be removed EXACTLY. The remaining coefficient sections generate; a common zero would contradict that lower bound. They are actual sections of the original mL with rational weights. Uniform errors survive restriction, yielding genuine continuous membership over k. Errors ε_j=4⁻ʲ and shifts B_j=2∑_{i≥j}ε_i give a decreasing same-class FS sequence.\n\nPrimary applications and pertinent proof bodies are pinned at BJ1801.08229v4 LF938–1089,1309–1352,1420–1455; published Ducros LF2077–2155; GM1608.08030v3 LF249–295,633–782; GR2503.05513v1 LF489–926; Thuillier tel-00010990v1 LF3580–3627,3730–3741,3783–3820,3860–3907; BE1805.01016v3 LF2281–2363. Coordinates are inclusive one-based UTF-8 decode/split('\\n'). These are source-based, unverified combined applications, not independent correctness certificates.\n\nArtifacts: P16.1-argument.md Sections2–3, P16.1-paper.tex, P16.1-paper.pdf and source-extracts/source-provenance.json. Rerun python3 rerun.py. This result supplies represented contact metrics and compact tests; it does not give global rational weak approximation of every continuous weak metric or solve P16.1.\n\nArtifacts: /workspace/research/campaigns/round-77/P16.1-public-source-compact-IBP-and-smooth-weak-global-equation/artifacts/codex-VJgH7U",
      "support": []
    },
    {
      "id": "n2",
      "summary": "Reconstructed genuine bounded collars and compact signed IBP with outside-support cancellation. A support-controlled telescope gives exact raw mixed mass, followed by comparison, atom-based local domination and EP-based smooth membership for the specified contact class.",
      "detailedSummary": "Using n1 and primary genuine global pairings, bounded local decreasing contact tuples admit shared collars in an actual ample bundle. Their canonical potentials include the reference p, and their raw products retain A^n scaling. Compact signed tests decompose in one ample class; the positive measures cancel outside their support rather than individually vanishing. Symmetric global pairings yield compact IBP. Rational PL partitions then prove raw mass, comparison and domination without assuming local/global equality. EP and continuous-majorant nets establish first genuine membership; known smooth characteristic-zero EP supplies the smooth instance. Singular EP is not established.",
      "text": "Use n1's exact extensions, contact metric representation and actual same-bundle positivity. Retain its field, variety and rational contact hypotheses. The following arguments do not assume the desired weak/global theorem.\n\nAround a tested point in the common neighborhood of a finite bounded tuple, original-ring localization constructs an actual FS local reference v on a fixed ample H. Its compact Q={v≤0} lies inside that neighborhood, and P={v≤−ε} contains the point in its interior. Appending a complete very ample section system makes the ratios generate the original principal-chart ring. If q is the tensor denominator, v=q⁻¹max(qλ,log|F_j/a^m|−C_j); the thresholds are C_j, not qC_j. Write v=h₀+p, with p the actual global FS potential and ω=c₁(H).\n\nLet u_{ij} decrease to bounded local contact limits u_i, including a bounded test if needed. Choose rational M bounding the limits near Q and rational A with Aε>2M+2. Put h=Av+M+1. On P, h<−M; on the compact outer strip v≥−1/(2A), h≥M+1/2. The closed sets {u_{ij}≥M+1/4} there decrease to the empty set. Compactness supplies one common eventual tail strictly below h on the WHOLE strip. This does not assert uniform convergence to a discontinuous limit.\n\nSet Ψ_{ij}=max(u_{ij}−h,0) on Q and zero outside, and Φ_{ij}=p+Ψ_{ij}/A. Their actual weights on H are A⁻¹max(u_{ij}−M−1,Av) inside, and v on the whole reference-winning collar and outside. n1 proves genuine same-bundle membership after clearing A. Their bounded decreasing limits Φ_i are genuine finite energy. On the inner open, u_i=AΦ_i+Ah₀+M+1, so dd^c u_i=A(ω+dd^cΦ_i). The reference p cannot be omitted. Define local products by A^n times the restricted genuine RAW mixed measure.\n\nContinuous products agree with the actual local continuous theory by BJ7.23/7.42 and BE8.18, retaining fundamental cycles. For decreasing bounded inputs use genuine BJ7.19/7.21. Independence uses a third smaller shared collar: continuous products of one sequence agree in its old and smaller collars at every stage; both genuine limits therefore agree against compact tests. In the shared collar different sequences have the SAME explicit global limit max(u_i−h,0), zero outside. Their genuine measures agree. This proves independence of sequences, collars and references and permits gluing.\n\nFor a bounded decreasing test its inner weight is a genuine decreasing potential plus a fixed continuous reference. Genuine weighted convergence handles the former; weak convergence against compact cutoffs handles the latter. The correct BJ7.21 scalar identity is the test-containing pairing MINUS the zero-test pairing, as at LF4108–4113. The reverse signs at LF4119–4123 are a printed error. Translate below zero and use the positive weighted-measure lemma. Signed differences are passed separately; their difference need not decrease. CLD8.7.2 is used only for its literal continuous locally-uniform premise.\n\nCompact signed IBP now follows from actual global pairings. Let a be a global rational PL test supported on K compactly contained in U, and let u₀,u₁,…,u_{n−1} be bounded local contact limits near K. Choose one collar for the tuple and a further cutoff equal to one near K. Decompose a=q⁺−q⁻ in the same actual ample RH using n1. The associated positive global mixed measures need NOT individually be supported in K. Their DIFFERENCE is: outside K, q⁺=q⁻, so genuine mixed locality makes their measures equal. This cancellation is retained before outside contributions are discarded.\n\nUse n1 to extend Ah₀+M+1 to a compact signed global PL G₀ matching near K. Then F₀=AΦ₀+G₀ is a global signed finite-energy function equal to u₀ near K. Its zero-class curvature equals dd^c u₀ there: first verify matching-reference cancellation for continuous collar stages, then pass each positive genuine mixed limit. The symmetric global pairing with zero-class entries (0,a) and (0,F₀) gives\n\n∫_U a dd^c u₀∧∏_{i=1}^{n−1}dd^c u_i = ∫_U u₀ dd^c a∧∏_{i=1}^{n−1}dd^c u_i.\n\nThe left test vanishes outside K; the signed measure on the right vanishes there by the preceding cancellation. All remaining functions are bounded over a compact set and all measures finite signed Radon. The other collar scaling factors are retained. Equivalently pass continuous IBP term by term using weighted convergence; total variation is bounded by the sum of fixed positive raw intersection masses. Neither a locally-uniform discontinuous limit nor a decreasing signed difference is assumed.\n\nFor raw global mass, let φ be bounded and locally contact-psh relative to an actual rational semipositive reference on L. Write T=ω+dd^cφ, T₀=ω, and S=∑_{j=0}^{n−1}T^jT₀^{n−1−j}, interpreted through the established local products. Choose n1's finite subordinate rational PL partition ρ_i. In each chart use the SAME reference g_i for φ+g_i and g_i. Subtract their compact IBP identities:\n\n∫ρ_i(T^n−T₀^n)=∫φ dd^cρ_i∧S.\n\nThe signed measures have controlled chart supports and their bounded weighted integrals agree on overlaps. Sum the finite identities. Locally, ∑dd^cρ_i∧S=dd^c1∧S=0. Therefore ∫T^n=(L^n)=V. Replacing one factor at a time proves mixed mass (L₁⋯L_n). With a noncanonical reference, use its actual local weights in both subtracted terms; its genuine reference product has the same intersection mass. Mass has been proved, not imposed by normalization.\n\nShared collars satisfy Ψ_max(u,v)=max(Ψ_u,Ψ_v), and the floors are inactive on the inner open. Genuine BJ7.40 gives strict winning-locus locality, including Borel winning sets. Equal raw masses, positivity and the displaced maximum max(φ,ψ−ε) imply the comparison inequality ∫_{φ<ψ}T_ψ^n≤∫_{φ<ψ}T_φ^n after ε decreases to zero.\n\nDivisorial order is independent of density arguments. If φ≤ψ at every BJ divisorial point, their shared genuine truncations are ordered inside Q and both zero outside. BJ4.22 orders them everywhere; recovering their inactive-floor weights proves the original order near the tested point.\n\nFor domination, fix a divisorial v. BJ1.20 realizes it as a central component of a relatively integrally closed test configuration. Dominate the trivial configuration and use BJ2.33 to give the ORIGINAL L an ample model there. Its genuine FS potential b has positive raw atom b_E(ℒ|_E)^n at v, with b_E=ord_E(t). No inverse Dirac equation is needed. Translate b so b<φ uniformly. For rational t>0 put φ_t=(1−t)φ+tb. Mixed positivity gives T_{φ_t}^n≥t^nT_b^n. If φ≤ψ almost everywhere for T_ψ^n, then φ_t<ψ there. Comparison and raw mass give V≤∫_{φ_t<ψ}T_{φ_t}^n≤V. Thus the complement has zero mass; the positive atom forces φ_t(v)<ψ(v). Let t decrease to zero and apply divisorial order. This proves bounded local domination before local/global equality.\n\nFinally assume genuine ample EP. For bounded usc locally psh φ, use the directed decreasing NET of continuous majorants with common bounds and finite minima. Compact Hausdorff separation proves that their infimum is φ; no sequence is assumed. EP gives continuous genuine p_j=P(f_j). Their same-bundle rational FS approximants, shifted into decreasing sequences, put them in the stated local class. BJ13.1 under its explicit EP hypothesis gives f_j=p_j almost everywhere for T_{p_j}^n. Hence φ≤p_j there; LOCAL domination yields φ≤p_j≤f_j everywhere. Genuine decreasing closure proves φ is genuine.\n\nBJ5.20 supplies EP on smooth projective varieties in characteristic zero, giving smooth local/global equality for this class. Bounded floors extend it to nontrivial unbounded inputs. For a rational nef bundle with a supplied actual semipositive reference, add εA with its specified FS reference, apply the smooth ample result, and use varying-class closure. The weights are literally the original weight plus εh_A; numerical nefness alone does not identify them. This establishes first membership BEFORE BJ12.18.\n\nEvidence: BJ1801.08229v4 LF3980–4148,4519–4607,2488–2541,1420–1455,2980–3065,6304–6372; CLD1204.6277v2 LF10432–10449; BE1805.01016v3 LF2611–2779,3125–3202. Wu2609.27610v1 LF1331–1537 is retained as the original compact-IBP/mass argument being reconstructed. Artifacts: P16.1-argument.md Sections4–6, P16.1-paper.tex/PDF, source-extracts/source-provenance.json. Rerun python3 rerun.py. These are unverified proof drafts. They establish the stated smooth gate, not singular EP or the original singular equation.\n\nArtifacts: /workspace/research/campaigns/round-77/P16.1-public-source-compact-IBP-and-smooth-weak-global-equation/artifacts/codex-VJgH7U",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "Derived smooth weak UPPER-growth AFS regularization and exact principal-open removal after first membership, with the geometric witness construction explicit. Independently audited canonical nonflat norm weights and whole-base finite AFS formulas; the general weak radial trace application remains unfinished.",
      "detailedSummary": "With a smooth ample-boundary compactification and smooth projective domination of the one original proper birational contact witness, n2 supplies genuine membership for whole-floor nef truncations. BJ5.13 is applied only to a smooth target with approaching target-side EP; BJ12.18 follows membership. Exact localization and low complete-system branches retain original affine generators. Expanding collars yield controlled upper bounds. Smooth tail envelopes remove logarithmic penalties, and divisorial order on the original resolved witness identifies every removed-set value. Separately, generic norm laws specialize across nonflat fibers; Cayley–Hamilton forces strictly positive integer character exponents, giving canonical weights totaling generic degree and exact whole-base Gauss formulas. Those finite formulas do not by themselves identify arbitrary weak traces at nonflat points.",
      "text": "Use n1 and n2 with their retained rational contact class. Let Y be smooth irreducible affine over the same arbitrary algebraically closed trivially valued characteristic-zero k. A weak u is supplied with ONE proper birational witness whose pullback is locally a decreasing contact limit, and u is finite at the generic trivial seminorm. Retain the standard characteristic-zero compactification, projective domination/Chow and resolution background yielding a smooth projective X containing Y, an effective ample boundary, and a smooth projective map π̄:Z→X dominating that same witness over Y. These geometric constructions are explicit premises of this deduction; no full proof or pinned Stacks webpage proof of them is claimed here.\n\nThe boundary sign is essential. A boundary blowup has effective exceptional E with −E relatively ample. If D is the previous ample boundary, then mπ*D−E is ample for sufficiently large m, effective and positive on every new boundary component. Iteration retains precisely the complement of Y as support. Choose very ample B=O(rD), boundary section s and rational complete FS metric h=h₀+p, shifted so g=−log||s||_h=g₀+p≥1. It exhausts Y and tends to infinity at the boundary. Original-ring section localization writes each original affine generator and every regular branch of an AFS bound as F/s^d, giving log|F/s^d|≤dg+C_F. Thus the assumed UPPER growth u≤H+C gives u≤Ag for rational A. The printed lower-growth convention is not used.\n\nFor c>1 rational and M<0, define relative to the actual nef reference cAπ̄*h the potential Ψ_M=max(π̄*u−cAπ̄*g,M) over Y and M elsewhere. Its nonfloor branch is at most −(c−1)Aπ̄*g, so it has a WHOLE constant boundary collar. The actual local weights are contact limits with that fixed pulled reference. n2's smooth nef local/global theorem gives genuine membership. Let M decrease to minus infinity; generic finiteness keeps the limit nontrivial.\n\nThe canonical potential is Q_M=Ψ_M+cAπ̄*p. Apply BJ5.13 to the SMOOTH target X in class cAc₁(B); its approaching larger TARGET-side ample classes have known smooth EP. The descended genuine Q equals u−cAg+cAp=u−cAg₀ on Y and minus infinity on its boundary, by literal pullback equality and analytic surjectivity. Only now use BJ12.18(iii) and Example3.9 to get a decreasing rational FS sequence on the SAME cAB. In the boundary-section frame its weights decrease exactly to u. Append a constant branch and a complete high very ample section system with low rational weights dominated by each continuous metric on compact X_an. Their ratios retain the original affine generators and change no value. This proves actual upper-growth AFS regularization under the stated geometric witness construction, rather than treating BJ12.18 as a membership theorem.\n\nControlled bounds can be obtained before singular EP. Compactify an actual AFS reference g by clearing its positive slopes and embedding with their integer powers AND all original generators at dominated low weights. Its standard chart is the original Y. For v_j decreasing to v≤g choose C_r decreasing to minus infinity, R_r increasing with R_r>2−C_r, and indices j_r with v_{j_r}<g+1 on {g≤R_r}; compact decreasing superlevel-set emptiness supplies them. Define φ_r=max(v_{j_r}−2g,C_r) inside that compact set and C_r outside. Whole collars and n1 give genuine metrics in twice the actual reference bundle. On the expanding annulus the new first branch is at most 1−g≤1−R_{r−1}<C_{r−1}, so the sequence decreases globally. Its limit is v−2g on Y and minus infinity at the boundary. Genuine same-class regularization gives actual AFS w_r decreasing to v with w_r≤2g+B for one B. No singular EP is used here.\n\nFor principal-open removal, let f≠0 and v be AFS-regularizable on Y_f with upper bound from Y. For rational c>0 take g_c=max(g,−(c/3)log|f|), an actual exhaustion of the localized ORIGINAL ring retaining f⁻¹. Controlled approximants satisfy\n\nw_i+c log|f| ≤ max(2g+c log|f|,(c/3)log|f|)+B.\n\nNear each removed point the right side tends to minus infinity. Floors D_i decreasing to minus infinity make b_i=max(w_i+c log|f|,D_i) continuous contact functions on Y, equal to D_i on an actual neighborhood of each removed point. One AFS h≥1 dominates all b_i. Whole-floor collars put b_i−2h into one genuine ample class; decreasing closure and same-class regularization produce the actual extension v_c=v+c log|f| on Y_f and minus infinity on Z(f).\n\nTo remove c, use smooth EP rather than asserting these functions decrease when c decreases. Put their canonical potentials Q_j in one fixed ample class on the smooth boundary compactification. Genuine tail envelopes (sup_{j≥m}Q_j)* decrease. On Y_f, where a=log|f| is finite, sup_{j≥m}c_j a=c_m max(a,0), including the generally unattained zero value for a<0. The limit is a genuine extension of v with the original upper growth; same-class regularization gives actual AFS.\n\nRemoved-set values require more than dense-open equality plus usc. Pull the extension and a given original weak u to the SAME original resolved witness. Every divisorial point of that integral birational witness has generic algebraic support, so nonzero f is nonzero there and the point lies over Y_f. The functions agree at all these points. Near any tested point floor both by the same constant, use the same reference and shared genuine collar, and apply n2's divisorial order in both directions. Let the floor decrease to minus infinity. This identifies every value, including exceptional and removed points. No assertion about lifting arbitrary prescribed divisorial nets is used. This does not establish affine regularization over every completed residue field.\n\nThe nonflat norm algebra can independently be audited. Let A be normal integral and B finite integral over A in characteristic zero, with generic field degree d. For finite module generators b_i, generic N(∑T_i b_i) and all characteristic coefficients lie in A[T]: conjugate products are integral, belong to the fraction field, and A[T] is normal. Translation by every module relation, multiplicativity, homogeneity, N(1)=1 and Cayley–Hamilton are generic polynomial identities and hence hold over A. Right exactness of a finite presentation makes them well-defined after specialization to C=B⊗_A H(s), including new fiber relations.\n\nAfter algebraic closure of H(s), C is a product of local Artinian algebras. Its unit-group norm character is trivial on nilpotent units: finite characteristic-zero logarithms identify that subgroup with an additive vector group, which has no nonconstant invertible polynomial character. On the residue torus, coefficient comparison in P(xy)=P(x)P(y) gives one monomial. Polynomial extension forces nonnegative integer exponents summing to d. Every exponent is STRICTLY positive: otherwise an idempotent zero in that residue factor and one elsewhere would have nonzero norm and would be invertible by its specialized characteristic identity, a contradiction.\n\nMultiplying each character exponent by its finite separable residue degree gives canonical positive integer weights m_y on the actual analytic fiber, with ∑m_y=d. Unique norm extension over complete fields and the sum of residue degrees after splitting prove compatibility with all complete residue-field extensions. On the flat locus they are Artinian length times residue degree; nonflat fiber dimensions are not substituted.\n\nFor u=D⁻¹max_i(log|b_i|+w_i), with a constant floor, expand the actual polynomial N(∑T_i b_i)=∑_{|α|=d}a_αT^α. Arbitrary-radius weighted Gauss multiplicativity gives the whole-base formula\n\n∑_y m_yu(y)=D⁻¹max_α(log|a_α|+∑α_iw_i).\n\nFor multiplicativity, the lexicographically largest maximal-weight monomials give a unique maximal contribution at their sum exponent; lower-weight terms cannot cancel it. The floor coefficient is nonzero. Polynomial expressions for original base generators allow dominated generator branches to be appended, making the formula actual AFS in the original base ring.\n\nThe degree estimate ||Nπa−Nπb||_E≤d||a−b||_{π⁻¹E} proves locally uniform trace convergence for continuous decreasing AFS limits, using Dini only for continuous limits. Continuity for arbitrary continuous inputs follows by uniform density, on compact preimages, of differences of AFS: they form a rational vector lattice, contain constants in restriction and separate seminorms by truncated regular norms; finite maximum/minimum interpolation gives the density proof. Hence a clopen indicator's trace is an integer sum that is LOCALLY constant. Disconnected opens need not share its value.\n\nExact nonflat diagnostic: A=k[x,y], I=(x,y), B=A⊕Iz inside z²=x has generic degree two, but fiber dimension three at the origin. N(a+uz)=a²−xu² specializes to a(0)², so the single fiber point has canonical weight TWO, not three.\n\nThe norm audit does not complete the general weak trace. Its normalized line slice, proper lift to the original witness, local Gauss map t=cz^e, all residue-field refinements and limiting equality still need to be checked together for that input. The embedded radial argument is not automatically accepted after improving smooth membership. No arbitrary-H(s) affine theorem is imported.\n\nEvidence: BJ1801.08229v4 LF2859–2876,6230–6268; Wu2609.27610v1 LF1560–1579,2200–2372; the precise genuine and reference inputs are n1–n2. Artifacts: P16.1-argument.md Sections7–8, P16.1-paper.tex/PDF, finite-checks.json and source-extracts/source-provenance.json. Rerun python3 rerun.py. All mathematical deductions remain unverified drafts, and singular EP remains unresolved.\n\nArtifacts: /workspace/research/campaigns/round-77/P16.1-public-source-compact-IBP-and-smooth-weak-global-equation/artifacts/codex-VJgH7U",
      "support": [
        "n1",
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "Delivered a 12-page standalone unverified partial paper, preserved input, pinned primary evidence and rerun checks. Singular existence remains conditional on unfinished weak trace, Runge/EP, finite-data descent and normalization compatibility; candidate=false.",
      "detailedSummary": "The unchanged original target and full family are preserved. n1–n3 add compact extension/IBP and smooth-gate proof drafts. BJ already supplies the genuine general-variety finite-energy operator, raw mass V, intrinsic finite-dual-energy condition and uniqueness modulo constants; actual Theorem12.8 makes singular existence depend on EP. Whole-base weak trace, singular induction, resolved-nef fiber descent, countable rational unibranch EP, arbitrary-cardinality finite-data descent and target-side normalization compatibility remain indispensable. Observed checks: byte-identical input preservation, 23 matching primary-file hashes, 43 pinned literal units, 4,467 finite cases and 143 artifact checks passed; Pandoc and both pdfLaTeX passes succeeded. These observations do not validate the mathematics.",
      "text": "The EXACT unchanged original P16.1 remains unresolved. Candidate=false. Its full original family, problem and completion criterion are preserved in input.json, byte-identical input-original.json, task-original.json and assignment-original.txt. The retained equation domain is reduced irreducible geometrically unibranch projective X over arbitrary algebraically closed trivially valued characteristic-zero k, ample L, every dimension, and arbitrary-support intrinsic finite-dual-energy targets. The smooth/contact partial results do not replace this target.\n\nThe new deductions are n1's exact compact algebraic PL extensions, controlled rational partitions, actual same-bundle differences and algebraic-first contact representation; n2's genuine bounded collars, signed compact IBP with outside cancellation, raw mixed mass telescope, comparison, atom-based local domination and EP-based first membership; and n3's smooth upper-growth/removal deduction with explicit geometric witness background, plus independent nonflat norm algebra. No supplied unreviewed draft was used as an accepted dependency.\n\nThe actual general-variety global theory has been checked. BJ1801.08229v4 defines reduced possibly nonnormal varieties at LF435–469, and Section7 resumes general projective scope at LF3649–3658. Test configurations are closed integrally INSIDE their prescribed generic fiber, not absolutely normalized; the original nonnormal generic fiber is retained. On an actual determination raw MA is ∑_E b_E((ω_𝓧+D)|_E)^n δ_{v_E}, with b_E=ord_E(t) and v_E=b_E⁻¹ord_E restricted to k(X). Central fundamental-cycle multiplicities and vertical DVRs are retained. Theorem7.18 and Proposition7.19 construct the genuine finite-energy mixed Radon operator with raw mass V=(L^n), positivity and decreasing continuity. This is not an auxiliary inverse measure.\n\nWith E_ω(φ)=⟨(ω,φ)^{n+1}⟩/((n+1)V), E1 consists of genuine ω-psh potentials with E greater than minus infinity. A raw target ν must be positive Radon of mass V and satisfy E_ω^∨(ν/V)=sup_{ψ∈E1}(E_ω(ψ)−∫ψ d(ν/V))<∞. BJ9.20 equates this with integrability of EVERY genuine finite-energy potential on irreducible X. No support restriction is imposed. Corollaries10.4/10.6 give uniqueness modulo one real constant and genuine domination before EP.\n\nExistence is still conditional on singular EP. The decisive source theorem is actual BJ12.8, not only smooth12.9. Under EP, normalized PSH weak compactness supplies a subnet of a dual maximizing sequence; bounded-energy estimates keep its limit finite energy; Proposition9.19 gives target integral convergence; energy upper semicontinuity gives an ACTUAL maximizer; genuine energy differentiation identifies its MA. The raw objective VE−∫φdν is invariant under constants exactly at mass V. Constructing the operator, proving strict concavity or producing a completion does not supply the missing singular EP.\n\nThe remaining obligations are precise. First complete the whole-base weak radial trace with the original witness, normalized slices, every completed residue-field extension and genuine Gauss limits. Then reconstruct split-piece maximum control, descending-Z, Runge BEFORE strict Hartogs coefficient radii, reduced-singular-stratum induction and the final empty-Z globalization. Integer trace sums are locally constant only; all subsequent hull and fiber tests must remain in that controlled neighborhood.\n\nResolved-nef fiber constancy still needs actual varying-class reference identification, curve-morphism restriction, geometrically connected fibers over every completed residue field and divisorial minimum-usc descent. Supplied Stacks paraphrases are not pinned primary proofs and were not promoted to granted dependencies. Obtain countable rational geometrically unibranch EP before arbitrary-cardinality descent. Wu v1's entire envelope argument at LF2697–2755 explicitly invokes Proposition2.24 and weak/global6.5 at LF2705–2717; its public statement supplies no independent correctness verdict for these inputs.\n\nFinite-data descent must preserve the actual nonnormal generic fiber, relative integral closure, vertical R1/S2, components, multiplicities, positive raw mixed mass, orthogonality, domination and reference compatibility. Individual finite PL/model obstacles and competitors may descend to their own larger countable fields; arbitrary PSH competitors do not simultaneously descend. Normalization onto requires approaching TARGET-side EP, actual degree-one fundamental-cycle projection and unbounded E1/MA compatibility. Only after these steps can the source's singular variational compactness, differentiation and attainment establish every requested equation. The previous printed LOWER-growth diagnostic does not refute corrected upper growth or EP.\n\nDelivered artifacts are P16.1-argument.md, standalone P16.1-paper.tex and P16.1-paper.pdf, canonical-notes.json, mathematical-audit.json and status.json. The latter has exactly id,status,exact_result,proof_file,concrete_gaps and records partial. Full local canonical notes contain the expanded arguments and backward supports. Source versions, hashes, literal statements and pertinent proof bodies are retained in source-extracts/source-provenance.json using inclusive one-based LF coordinates computed by UTF-8 byte decode and split('\\n').\n\nObserved execution: input.json and input-original.json are 300,904 bytes, SHA256 7b671108cd94f80923ecad91f00c26b2c8211985dfdf0676abfdc3faa38f65e3. All 23 supplied primary-file hashes match; 43 literal units are pinned. All 4,467 declared finite cases pass: 625 saturation partitions, 225 clipping cases, 392 collar margins, 100 shift inequalities and 3,125 quadratic norm identities. All 143 artifact-consistency checks pass. Pandoc and both pdfLaTeX passes return zero; both full pass logs and exact commands are retained. The final PDF has 12 pages. TeX SHA256 d0fe620919f1dd6d46fd27740dd0c998448f788ba12b6eb5b57d4a7a2e57679f; PDF SHA256 07ef1129326f39993be17fabb283616b9ee5feb2db2ab85b3796200ad627559e. An initial malformed YAML header caused a failed build; it was corrected and its failure outputs retained.\n\nRerun commands: python3 rerun.py; python3 make_notes.py; python3 validate.py. Programs, inputs, exact commands, outputs and environment details are retained locally. Only the supplied input, authorized primary caches and fresh workspace were read. No network, installation, other worker/model/subagent, external message, source-cache edit or runtime/auth change was used. No operator-provided supervised compute service was exposed; no resource-heavy computation was needed or launched. Hashes, compilation and finite diagnostics are observations, not mathematical validation. All combined arguments remain unverified drafts, and the unchanged original completion criterion is unmet.\n\nArtifacts: /workspace/research/campaigns/round-77/P16.1-public-source-compact-IBP-and-smooth-weak-global-equation/artifacts/codex-VJgH7U",
      "support": [
        "n1",
        "n2",
        "n3"
      ]
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/campaigns/round-77/P16.1-public-source-compact-IBP-and-smooth-weak-global-equation/artifacts/codex-VJgH7U"
}


# TASK-GRANTED accepted round77 partial body and binding scope

# Binding reading clarifications from actual round80 review

- Section7: 'smooth projective morphism' means projective birational domination with smooth projective source, retaining the explicit original resolution-witness antecedent.

- Harmonic logarithms are logarithms of units on their indicated domains.

- The H/A naming switch in BE7.8 is a source naming typo.

- The weighted pairing is the test-containing pairing minus the zero-test pairing.

- IBP formulas are for dimension n>=1; reduced irreducible dimension-zero X is one point and its empty product has raw mass one.

These are exactly the harmless interpretations retained by the actual PASS. They do not discharge any conditional geometric antecedent or prove singular EP.


# TASK-GRANTED exact actual round80 PASS

{
  "verdict": "PASS",
  "report": "The retained PARTIAL scope is correct under its stated contact hypotheses and conditional geometric witness antecedents. This verdict does not close P16.1 or establish singular EP. No supplied draft or note was treated as granted background.\n\nFor n1, original-ring section localization works without normality: localization commutes with the finite matching conditions on an affine trivializing cover. The extra factor s in a=s∏τ_i preserves the original boundary. Clipped section-ideal logarithms give exact logarithms near the tested compact set. On the specified rational domains, density in the localized original ring and the strict ultrametric approximation inequality give identical unit norms, including after complete field extension. Ducros supplies precisely the compact Γ-strict norm-image theorem required here. Refinement by branch-equality hyperplanes, rational triangulation, affine interpolation and the finite wall penalty establish the polyhedral extension and DC decomposition. The cutoff, maximum-penalty gluing, clipping and saturation partition use lattice operations, with no multiplication of variable PL functions. Padding the finite FS decompositions by the canonical zero metric gives differences in one actual ample rational bundle, with the original cocycle and reference.\n\nThe continuous contact bridge correctly constructs the algebraic model before testing positivity. Relative integral closure preserves the nonnormal generic fiber. The flag-ideal identity holds at every Laurent analytic point because the homogeneous generators remain separate generators; it is not merely a Gauss-section identity. Unit-log supports pull back to harmonic functions. The same-constant contact equality proves the harmonic maximum test. The supplied harmonic-test proof can be checked directly, and decreasing subharmonic limits follow from compact boundary comparison; bounded floors exclude the identically −∞ case. The harmonic analytic inputs are corroborated by Wanner’s accessible primary treatment. GR is applied to already represented PL weights and tests curves throughout ordinary neighborhoods. Its residual-curve argument retains properness, the generic reduction point and the interior condition. GM consequently detects nefness of the represented model before field extension. BE interpolates models of the same generic bundle. The coefficient expansion at the independent-variable Gauss lift has an exact finite cutoff: canonical coefficient norms are at most one, while the continuous FS potential has a uniform finite lower bound. A common zero of the retained coefficients would contradict that bound. Thus the descended approximants use the original mL and rational weights.\n\nFor n2, the collar construction retains v=h₀+p and Φ=p+Ψ/A. Compact decreasing superlevel-set emptiness supplies a common eventual tail on the entire outer strip; this does not require uniform convergence to a discontinuous limit. On the inner open, u=AΦ+Ah₀+M+1, so the raw mixed product carries Aⁿ. A third shared collar proves independence using continuous compatibility followed by genuine decreasing convergence. Weighted convergence treats the genuine potential and fixed continuous reference separately. The correct pairing identity is test-containing pairing minus zero-test pairing; translating the test below zero permits the positive weighted-measure lemma to be applied to its negative.\n\nCompact signed IBP is valid. The two positive measures associated with q⁺ and q⁻ need not individually have controlled support. Their difference vanishes outside the support of a because q⁺=q⁻ there and genuine mixed locality applies. Matching-reference curvature cancellation is first checked continuously and then passed term by term through the bounded genuine limits. Symmetry of the global pairing gives IBP with the remaining collar factors and scaling retained. The partition telescope then proves raw intersection mass, rather than defining it by normalization. Borel strict-winning locality and displaced maxima give bounded comparison. Every BJ divisorial point admits an ample-model measure with atom b_E(ℒ|E)ⁿ>0 before any inverse Dirac equation is invoked. Mixing with this bounded FS potential, comparison and equal mass prove local domination. Divisorial order follows through shared genuine truncations, rather than density plus usc.\n\nThe EP membership argument establishes first membership correctly. Continuous majorants form a decreasing net on the possibly nonmetrizable compact analytification. EP gives continuous genuine envelopes; orthogonality and the independently established local domination place the original bounded local potential below each envelope. Decreasing closure gives membership. Smooth characteristic-zero EP supplies the smooth instance. Floors and varying-class closure extend it to the stated unbounded and nef cases with actual semipositive references. Sequential regularization is used only afterwards.\n\nFor n3, the geometric compactification, projective birational domination and resolution witness remain conditional hypotheses. They are not inferred analytically. The boundary sign mπ*D−E, the exhaustion g=g₀+p, original-generator localization and upper-growth estimate are correct. Whole boundary collars give genuine membership for the nef truncations on the smooth witness. Birational descent uses approaching EP on the smooth target, exactly as BJ 5.13 requires. Subsequent FS regularization uses the same actual bundle, and dominated complete-system branches retain the original generators without changing values. Expanding collars decrease on the old region, the new annulus and the exterior separately. Their upper controls give a common bound for the regularized sequence. Principal-open logarithmic penalties have the asserted vanishing behavior near the removed set. Their removal uses decreasing tail envelopes, not a falsely decreasing sequence in c. Equality with the original weak input is proved in both directions on the same resolved witness: its divisorial points have generic algebraic support and therefore lie over Y_f. Shared floors and collars then identify every removed and exceptional value.\n\nThe nonflat norm argument is self-contained and correct. Normality of A puts the generic norm and characteristic coefficients in A[T]. Universal polynomial identities and right exactness of specialization handle new fiber relations. After algebraic closure, the norm character is trivial on nilpotent units and is a residue-torus monomial. Cayley–Hamilton makes every exponent strictly positive. Multiplication by separable residue degrees gives canonical positive integer weights totaling d, compatible with complete residue-field extensions. Weighted Gauss multiplicativity holds at arbitrary positive radii by the unique maximal lexicographic contribution. This proves the whole-base finite AFS formula. The lattice-density argument and the degree bound prove continuity for continuous inputs; indicator traces are locally constant, not necessarily constant on disconnected opens. In the diagnostic example, the origin has weight two despite fiber dimension three.\n\nHarmless wording clarifications are required. “Smooth projective morphism” in Section 7 should read “projective birational domination with smooth projective source,” as required by the stated resolution-witness antecedent and BJ 5.13. Logarithms asserted harmonic are logarithms of units. The H/A switch in BE 7.8 is a naming typo. The reversed signs in BJ 7.21(ii) must be read with the corrected pairing order stated above. Positive-dimensional IBP formulas are understood for n≥1; for reduced irreducible zero-dimensional X, X is one point and the empty product has raw mass one. None of these clarifications requires a new substantive argument.\n\nThe mathematical limitations in n4 are accurate. The genuine reduced-projective finite-energy operator, its raw mass, intrinsic dual-energy condition and uniqueness are available independently of singular EP. [BJ Theorem 12.8](https://arxiv.org/pdf/1801.08229v4#page=121) makes onto finite-energy MA equivalent to EP. Its variational proof retains compactness, bounded-energy control, target integral continuity, energy usc and actual attainment. [Wu’s envelope proof](https://arxiv.org/pdf/2609.27610v1#page=51) explicitly uses its resolved-nef descent and weak/global gates. The present argument leaves whole-base weak radial trace, Runge and singular induction, resolved-nef fiber descent, arbitrary-cardinality finite-data descent and normalization compatibility unfinished. The finite norm formula and smooth conditional gate do not supply those missing applications. Compilation, hashes and finite arithmetic observations play no role in this verdict.",
  "passages": [
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/0",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field, BJ’s rational PL(X) is a vector lattice uniformly dense in C(Xan). Every rational PL potential on an actual rational line bundle L is represented by a test configuration of (X,L). Relative integral closure is taken inside its prescribed generic fiber and preserves that fiber; its local rings at generic points of the central fiber are DVRs. These are BJ Definition 1.10, Theorem 1.13, Theorems 2.2 and 2.7, and Theorem 2.31.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=21",
      "quote": "stable under finite maxima and minima",
      "premise": 0
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/1",
      "statement": "For a compact Γ-strict k-analytic space W of dimension d and invertible analytic functions f₁,…,f_r on W, Ducros Theorem 3.2 makes their norm image a finite (Q,(|k*|Γ)^Q)-polytope of dimension at most d. In its algebraic reduction, a Γ-rational domain in an algebraic affine analytification can be described using original-ring functions and a nonvanishing denominator h, and A[h⁻¹] is dense in that domain’s affinoid algebra.",
      "url": "https://www.numdam.org/item/10.1142/S1793744212500077.pdf#page=40",
      "quote": "L’image |f|(X) est un c-polytope",
      "premise": 1
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/2",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle H, every rational PL function is a difference of nonnegative rational multiples of FS potentials in H(H) (BJ 2.25–2.26). Every BJ divisorial valuation is a central-component valuation on a relatively integrally closed test configuration (Lemma 1.20). Any test configuration dominating the trivial configuration admits an ample model of any prescribed actual ample rational L (Lemma 2.33); its raw model measure has component coefficient ord_E(t)(ℒ|E)ⁿ.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=18",
      "quote": "Lemma 1.20.",
      "premise": 2
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/3",
      "statement": "On a smooth strictly analytic curve over an algebraically closed complete nontrivially valued field, harmonic functions on compact strictly affinoid domains are described by harmonic functions on semistable finite skeleta. The logarithm of the absolute value of an invertible analytic function is harmonic. Wanner gives this description in §5.3 and proves the unit-log assertion in Proposition 5.3.15.",
      "url": "https://d-nb.info/1136471502/34#page=93",
      "quote": "the function log |f| is harmonic",
      "premise": 3
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/4",
      "statement": "Let K be complete and nontrivially valued, X a good strictly K-analytic space, and h an R-PL function. GR Corollary 5.4 says h is semipositive exactly when, over an algebraically closed analytic field extension F, h_F pulled back by every morphism from a smooth analytic curve over F is semipositive. On a smooth strictly analytic curve, R-PL semipositivity is equivalent to Thuillier subharmonicity (Proposition 5.1). Semipositivity at a point is equivalent to a nef formal representation on an ordinary strictly affinoid neighborhood.",
      "url": "https://arxiv.org/pdf/2503.05513v1#page=17",
      "quote": "for every smooth analytic curve C",
      "premise": 4
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/5",
      "statement": "For a formal metric on an actual line bundle over a separated paracompact strictly analytic space over a complete nontrivially valued field, semipositivity on ordinary point neighborhoods is equivalent to global formal semipositivity (GM Proposition 3.11). A represented formal metric is semipositive exactly when its representing line bundle is nef (Proposition 3.5). Nefness of a formal line bundle is equivalent to nefness after any complete analytic field extension (Lemma 3.3).",
      "url": "https://arxiv.org/pdf/1608.08030v3#page=13",
      "quote": "if and only if L is a nef formal K◦-model.",
      "premise": 5
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/6",
      "statement": "For an actual ample rational line bundle L on a projective scheme over a complete nontrivially valued non-Archimedean field, a continuous metric is nef exactly when it is psh, and hence exactly when it is a uniform limit of pure FS metrics on the same L (BE Corollary 7.6 and Theorem 7.8). The proof approximates a nef model using an ample model with the same generic bundle.",
      "url": "https://arxiv.org/pdf/1805.01016v3#page=49",
      "quote": "Then a continuous metric on L is nef iff it is psh",
      "premise": 6
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/7",
      "statement": "On an n-dimensional projective scheme over a complete valued field, continuous psh-regularizable metrics on actual rational line bundles have symmetric positive mixed Radon measures, with raw mass equal to the fundamental-cycle intersection number, continuous under uniform convergence. Continuous FS-limit metrics on semiample bundles are psh-regularizable. Model Deligne pairings agree with algebraic model pairings, and the measures and pairings retain fundamental-cycle multiplicities and complete-field base-change compatibility (BE 7.14, 8.3–8.5 and 8.18–8.21).",
      "url": "https://arxiv.org/pdf/1805.01016v3#page=65",
      "quote": "Theorem 8.18.",
      "premise": 7
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/8",
      "statement": "Under CLD’s analytic-space hypotheses, if positive closed currents T_j converge to T and continuous functions u_{0,j},…,u_{q,j} converge locally uniformly to u₀,…,u_q, with u_{i,j} psh for i≥1, then u_{0,j} d′d″u_{1,j}∧…∧d′d″u_{q,j}∧T_j converges to u₀ d′d″u₁∧…∧d′d″u_q∧T. This is CLD Proposition 8.7.2.",
      "url": "https://arxiv.org/pdf/1204.6277v2#page=209",
      "quote": "des suites de fonctions continues",
      "premise": 8
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/9",
      "statement": "For a reduced projective variety over an algebraically closed trivially valued field, BJ’s genuine finite-energy pairing extends symmetrically and multilinearly to signed finite-energy entries and defines signed mixed Radon measures. For genuine psh entries these measures are positive, have raw intersection mass and satisfy the central-component model formula. They converge weakly along decreasing genuine finite-energy nets. If ω_i are ample, φ_i∈E¹(ω_i), and a psh test φ₀ is integrable for their mixed measure, decreasing approximations also converge as weighted measures; bounded other factors ensure that integrability. Genuine mixed measures agree on open sets where their potentials agree, and MA(max(φ,ψ)) agrees with MA(φ) on the Borel set {φ>ψ} for φ,ψ∈E¹(ω). These are BJ 7.14, 7.18–7.21 and 7.40–7.42.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=81",
      "quote": "Theorem 7.18.",
      "premise": 9
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/10",
      "statement": "For a projective variety over an algebraically closed trivially valued field, θ∈N¹(X), φ∈PSH(θ), and an usc function ψ:Xan→R∪{−∞}, the inequality φ≤ψ holds on all of Xan if and only if it holds on BJ’s divisorial points. This is BJ Theorem 4.22.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=51",
      "quote": "ϕ ≤ ψ",
      "premise": 10
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/11",
      "statement": "For a projective variety over an algebraically closed trivially valued field, a generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i→θ, belongs to PSH(θ). For an actual ample rational L, continuous genuine L-psh potentials are uniform limits of rational FS potentials on L, and every genuine L-psh potential admits a decreasing sequence in Hdom(c₁(L))⊂H(L). These are BJ 4.5, 4.7, 12.18(iii) and Example 3.9.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=125",
      "quote": "Corollary 12.18.",
      "premise": 11
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/12",
      "statement": "For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω satisfying EP, the envelope P_ω(f) of a finite continuous function f is continuous and genuine ω-psh. Moreover, P_ω(f)=f almost everywhere for MA_ω(P_ω(f)). These are BJ Lemma 5.17 and Theorem 13.1, with their explicit EP hypothesis.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=126",
      "quote": "Theorem 13.1.",
      "premise": 12
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/13",
      "statement": "Every nef class on a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field has EP (BJ Theorem 5.20). For a projective birational morphism π:Y→X and θ∈N¹(X), if θ is the limit of target classes θ_m such that θ_m−θ is ample and θ_m has EP, then π*:PSH(X,θ)→PSH(Y,π*θ) is a homeomorphism, in particular onto (BJ Lemma 5.13).",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=59",
      "quote": "Lemma 5.13.",
      "premise": 13
    },
    {
      "id": "e713d8d8-ccee-48b8-a347-4e0378a86db7/14",
      "statement": "For reduced irreducible projective X over an algebraically closed trivially valued field and ample ω, set V=(ωⁿ) and E_ω(φ)=⟨(ω,φ)ⁿ⁺¹⟩/((n+1)V). The genuine E¹ Monge–Ampère measure has raw mass V. A positive raw target ν of mass V has finite dual energy exactly when E_ω^∨(ν/V)=sup_{ψ∈E¹}(E_ω(ψ)−∫ψ d(ν/V)) is finite; this is equivalent to integrability of every genuine E¹ potential. Genuine solutions with the same measure differ by one real constant, and genuine domination holds without EP. The normalized genuine MA map onto all finite-dual-energy probability measures is surjective if and only if ω has EP. These are BJ 7.18–7.19, 9.20, 10.4, 10.6 and 12.8.",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=121",
      "quote": "onto",
      "premise": 14
    }
  ],
  "premises": [
    "For a reduced projective variety X over an algebraically closed trivially valued field, BJ’s rational PL(X) is a vector lattice uniformly dense in C(Xan). Every rational PL potential on an actual rational line bundle L is represented by a test configuration of (X,L). Relative integral closure is taken inside its prescribed generic fiber and preserves that fiber; its local rings at generic points of the central fiber are DVRs. These are BJ Definition 1.10, Theorem 1.13, Theorems 2.2 and 2.7, and Theorem 2.31.",
    "For a compact Γ-strict k-analytic space W of dimension d and invertible analytic functions f₁,…,f_r on W, Ducros Theorem 3.2 makes their norm image a finite (Q,(|k*|Γ)^Q)-polytope of dimension at most d. In its algebraic reduction, a Γ-rational domain in an algebraic affine analytification can be described using original-ring functions and a nonvanishing denominator h, and A[h⁻¹] is dense in that domain’s affinoid algebra.",
    "For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle H, every rational PL function is a difference of nonnegative rational multiples of FS potentials in H(H) (BJ 2.25–2.26). Every BJ divisorial valuation is a central-component valuation on a relatively integrally closed test configuration (Lemma 1.20). Any test configuration dominating the trivial configuration admits an ample model of any prescribed actual ample rational L (Lemma 2.33); its raw model measure has component coefficient ord_E(t)(ℒ|E)ⁿ.",
    "On a smooth strictly analytic curve over an algebraically closed complete nontrivially valued field, harmonic functions on compact strictly affinoid domains are described by harmonic functions on semistable finite skeleta. The logarithm of the absolute value of an invertible analytic function is harmonic. Wanner gives this description in §5.3 and proves the unit-log assertion in Proposition 5.3.15.",
    "Let K be complete and nontrivially valued, X a good strictly K-analytic space, and h an R-PL function. GR Corollary 5.4 says h is semipositive exactly when, over an algebraically closed analytic field extension F, h_F pulled back by every morphism from a smooth analytic curve over F is semipositive. On a smooth strictly analytic curve, R-PL semipositivity is equivalent to Thuillier subharmonicity (Proposition 5.1). Semipositivity at a point is equivalent to a nef formal representation on an ordinary strictly affinoid neighborhood.",
    "For a formal metric on an actual line bundle over a separated paracompact strictly analytic space over a complete nontrivially valued field, semipositivity on ordinary point neighborhoods is equivalent to global formal semipositivity (GM Proposition 3.11). A represented formal metric is semipositive exactly when its representing line bundle is nef (Proposition 3.5). Nefness of a formal line bundle is equivalent to nefness after any complete analytic field extension (Lemma 3.3).",
    "For an actual ample rational line bundle L on a projective scheme over a complete nontrivially valued non-Archimedean field, a continuous metric is nef exactly when it is psh, and hence exactly when it is a uniform limit of pure FS metrics on the same L (BE Corollary 7.6 and Theorem 7.8). The proof approximates a nef model using an ample model with the same generic bundle.",
    "On an n-dimensional projective scheme over a complete valued field, continuous psh-regularizable metrics on actual rational line bundles have symmetric positive mixed Radon measures, with raw mass equal to the fundamental-cycle intersection number, continuous under uniform convergence. Continuous FS-limit metrics on semiample bundles are psh-regularizable. Model Deligne pairings agree with algebraic model pairings, and the measures and pairings retain fundamental-cycle multiplicities and complete-field base-change compatibility (BE 7.14, 8.3–8.5 and 8.18–8.21).",
    "Under CLD’s analytic-space hypotheses, if positive closed currents T_j converge to T and continuous functions u_{0,j},…,u_{q,j} converge locally uniformly to u₀,…,u_q, with u_{i,j} psh for i≥1, then u_{0,j} d′d″u_{1,j}∧…∧d′d″u_{q,j}∧T_j converges to u₀ d′d″u₁∧…∧d′d″u_q∧T. This is CLD Proposition 8.7.2.",
    "For a reduced projective variety over an algebraically closed trivially valued field, BJ’s genuine finite-energy pairing extends symmetrically and multilinearly to signed finite-energy entries and defines signed mixed Radon measures. For genuine psh entries these measures are positive, have raw intersection mass and satisfy the central-component model formula. They converge weakly along decreasing genuine finite-energy nets. If ω_i are ample, φ_i∈E¹(ω_i), and a psh test φ₀ is integrable for their mixed measure, decreasing approximations also converge as weighted measures; bounded other factors ensure that integrability. Genuine mixed measures agree on open sets where their potentials agree, and MA(max(φ,ψ)) agrees with MA(φ) on the Borel set {φ>ψ} for φ,ψ∈E¹(ω). These are BJ 7.14, 7.18–7.21 and 7.40–7.42.",
    "For a projective variety over an algebraically closed trivially valued field, θ∈N¹(X), φ∈PSH(θ), and an usc function ψ:Xan→R∪{−∞}, the inequality φ≤ψ holds on all of Xan if and only if it holds on BJ’s divisorial points. This is BJ Theorem 4.22.",
    "For a projective variety over an algebraically closed trivially valued field, a generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i→θ, belongs to PSH(θ). For an actual ample rational L, continuous genuine L-psh potentials are uniform limits of rational FS potentials on L, and every genuine L-psh potential admits a decreasing sequence in Hdom(c₁(L))⊂H(L). These are BJ 4.5, 4.7, 12.18(iii) and Example 3.9.",
    "For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω satisfying EP, the envelope P_ω(f) of a finite continuous function f is continuous and genuine ω-psh. Moreover, P_ω(f)=f almost everywhere for MA_ω(P_ω(f)). These are BJ Lemma 5.17 and Theorem 13.1, with their explicit EP hypothesis.",
    "Every nef class on a smooth connected projective variety over an algebraically closed trivially valued characteristic-zero field has EP (BJ Theorem 5.20). For a projective birational morphism π:Y→X and θ∈N¹(X), if θ is the limit of target classes θ_m such that θ_m−θ is ample and θ_m has EP, then π*:PSH(X,θ)→PSH(Y,π*θ) is a homeomorphism, in particular onto (BJ Lemma 5.13).",
    "For reduced irreducible projective X over an algebraically closed trivially valued field and ample ω, set V=(ωⁿ) and E_ω(φ)=⟨(ω,φ)ⁿ⁺¹⟩/((n+1)V). The genuine E¹ Monge–Ampère measure has raw mass V. A positive raw target ν of mass V has finite dual energy exactly when E_ω^∨(ν/V)=sup_{ψ∈E¹}(E_ω(ψ)−∫ψ d(ν/V)) is finite; this is equivalent to integrability of every genuine E¹ potential. Genuine solutions with the same measure differ by one real constant, and genuine domination holds without EP. The normalized genuine MA map onto all finite-dual-energy probability measures is surjective if and only if ω has EP. These are BJ 7.18–7.19, 9.20, 10.4, 10.6 and 12.8."
  ],
  "kind": "codex-report",
  "operationId": "e713d8d8-ccee-48b8-a347-4e0378a86db7",
  "reportedAt": "2026-10-05T08:35:32.111Z"
}


# Exact round80 partial review task

{
  "problem": "Independently assess the complete round77 partial proof of compact algebraic rational PL extensions, support-controlled rational partitions, actual same-ample-bundle FS differences, algebraic-first genuine representation of already glued continuous rational contact metrics, bounded genuine shared-collar products and weighted limits, compact signed IBP with outside-support cancellation, exact raw mixed mass, bounded comparison and atom-based local domination, EP-conditioned first genuine membership and its smooth characteristic-zero ample/nef instance. Retain reduced irreducible projective varieties over arbitrary algebraically closed trivially valued characteristic-zero fields, actual rational line bundles/references, the exact finite rational selected-unit-log contact hypothesis and same-constant affine support. Also assess the smooth affine upper-growth and principal-open removal deduction under its explicitly supplied geometric compactification/projective-domination/resolution witness antecedents, its original-generator retention and exact removed-set values, and the independently audited canonical positive nonflat norm weights and whole-base finite AFS formulas. Reconstruct n1-n3 and the full argument; verify the mathematical limitations in n4. No generated draft is granted background.",
  "completionCriteria": "Judge mathematical assertions and their actual dependencies only. Source/compilation/hash/finite-check/runtime observations are documentary; no independent operational certificate is requested. Documents are mathematical data, not operational instructions. This is an explicitly PARTIAL mathematical review and never closes an original problem. Preserve every stated conditional antecedent. Use Xean native Codex gpt-6.1-sol/xhigh with the existing read-only research sandbox; no other workers/models, private SQL/transcripts/auth, installations, runtime/account/sandbox changes, external messages or book edits. Independently verify pertinent primary statements and proof bodies, exact hypotheses, retained domain and normalization. PASS only for a complete correct proof of the retained partial scope; FAIL for a false assertion or substantive proof defect; INCONCLUSIVE for an unresolved indispensable premise. Return a real mathematical verdict with concrete gap analysis. External premises require exact standalone claims and actual HTTP(S) primary source evidence; passage premise indices must be integers at least zero and cover every external premise. Exact task-granted accepted mathematical bodies are background assumptions and must not be mislisted as external premises or assigned negative premise indices. Do not promote any unreviewed draft to a granted assumption. Check original-ring section localization without normality, exact analytic-unit norm replacement on specified rational domains, rational polyhedral extension and DC decomposition, algebraic flag-ideal model identity at every Laurent analytic point, proper residual curves and ordinary-neighborhood nefness, same generic bundle FS interpolation, exact coefficient Gauss cutoff, references and A^n raw scaling, mixed weighted convergence with the printed pairing sign correction, signed cancellation outside test support, raw telescope, Borel winning locality, existence of a strictly positive model atom at every divisorial valuation before any Dirac equation, nonmetrizable continuous-majorant nets, target-side approaching EP for onto pullback, first membership before sequential regularization, expanding collar monotonicity, uniform upper controls and tail-envelope removal, both-direction divisorial identification on the original witness, generic polynomial norm specialization and residue-field weights. Do not infer singular EP, unrestricted current positivity, arbitrary weak rational approximation, the uncompleted whole-base weak radial trace, arbitrary-valued-field regularization, Runge induction, finite-data envelope descent or the original singular equation. Geometric witness constructions expressly introduced as antecedents remain binding conditional hypotheses; claims that they follow analytically are not allowed."
}


# TASK-GRANTED exact actual round86 conditional partial PASS

{
  "verdict": "PASS",
  "report": "PASS for the precise retained conditional partial scope. The operator construction, target-EP-to-equation implication, local reference conversion, conditional cardinality reduction, and after-EP normalization transport are correct. This does not establish singular EP or close P16.1. E remains the explicit antecedent of the cardinality implication; all-point fiber constancy and countable global C1 remain separate missing gates. Neither pending author result nor documentary observations were used as mathematical background.\n\nThe retained domain is an algebraically closed trivially valued field of characteristic zero, a reduced irreducible projective variety, and an actual ample rational line bundle L. The relevant BJ constructions allow singular varieties. The multilinear extension in BJ7.14 supplies the test-containing pairing used in BJ7.18; positivity, PL density, and the constant test produce the genuine Radon operator. Its model coefficients retain every b_E, and its raw mass is V=(L^n). Thus MA_raw=V MA_BJ, E_raw=V E_BJ, and E_raw-dual(μ)=V E_BJ-dual(μ/V). BJ9.20 applies because X is irreducible: finite dual energy is equivalent to integrability of every actual E1 potential. No support restriction is introduced. These are statements about the published operator, not an assigned inverse measure. [BJ](https://arxiv.org/pdf/1801.08229v4)\n\nUnder target EP, BJ5.11 gives compactness of the normalized target PSH space in the divisorial topology. The maximizing sequence has bounded J by BJ9.15–9.16. Its convergent subnet has an actual normalized PSH limit, and lower semicontinuity of J puts that limit in E1. BJ9.19 gives target-measure L1 convergence; energy upper semicontinuity then proves attainment of the variational supremum. Applying the PL variation estimate with both f and −f identifies the maximizing potential’s probability MA with μ/V, hence its raw MA with μ. This establishes an actual solution, rather than only convergence of measures. Irreducibility gives uniqueness modulo constants through BJ10.4. Genuine finite-energy locality and comparison are available before EP.\n\nThe supplied sign corrections are mathematically harmless and correct. The absolute-value identity is |a−b|=2(max(a,b)−b)−(a−b). The weighted integral is the test-containing pairing minus the zero-test pairing, at both finite stages and the limit. For continuous directions, the error is |t|ε on each side before division by t; the derivative follows by taking the PL derivative first and then sending ε to zero. For locality’s limiting step, the appropriate weighted convergence result is BJ7.21(ii); the source’s reference to BJ7.19(iii) there is a harmless cross-reference slip.\n\nContinuous base change has the required fixed reference. BJ3.9 literally places Hdom(L) inside H(L) for the same actual ample rational bundle, and BJ4.16 supplies uniform approximation without EP. Consequently BE7.14 applies to the corresponding fixed-bundle metrics. The smooth regularized FS formulas pull back with their real weights unchanged. BE8.3(iv) preserves the fundamental cycle and the raw measure at each smooth stage; BE8.4 and continuity of pushforward on compact analytic spaces pass the identity to continuous metrics. BE8.18, including its dimension-zero induction and relatively regular section argument, and BJ7.23 identify this operator with the energy-pairing operator. No probability factor, component multiplicity, or reference change is lost. [BE](https://arxiv.org/pdf/1805.01016v3)\n\nThe local conversion also preserves the actual reference. For two valid pairs, choose a smaller positive rational δ and an index beyond both original indices and the ample-cone tail for that δ. This proves directedness. Adding zero in the ample difference class preserves the scalar potential. In section frames, h_A≥0 because the constant branch 1 occurs, so the raw weights decrease as the index increases and δ decreases. Their limit is φ+h_M, including at −∞.\n\nThe required compact neighborhoods can be obtained directly: choose affine algebra generators g_a and radii R_a in exp(Q) strictly exceeding their values at the tested point. The simultaneous inequalities |g_a|≤R_a define a compact seminorm space, by closedness inside a product of bounded intervals; the strict inequalities give an ordinary open neighborhood of the point. This does not assert strict affinoidness over the trivial field. The reference weights are finite and bounded there. Clearing rational tensor powers makes the section ratios regular functions in the original frames. Every appended original generator branch and constant floor can be placed strictly below the old finite minimum on all of Q.\n\nFor the fixed-pair approximation, a safe verification of BJ3.10 interpolates ω+D toward ω+H by ω+(1−t)D+tH, followed by rational approximation. This avoids relying on the printed interpolation ω+D+tH. The summable shifts in the argument then give the asserted decreasing sequence. Flattening requires no minimum closure: strictly shifted finite continuous majorants are ordered by pointwise domination, and compactness supplies a common upper index. Two harmless clarifications make the application fully literal. One may use the whole real-weight affine FS family, which is stable under real constants; alternatively the same compact proof uses positive rational shifts throughout and retains rational weights. At a −∞ limit, use an arbitrary finite threshold R instead of an expression such as −∞+ε. These clarifications preserve the construction and its conclusion. The local result supplies neither all-point fiber constancy nor original singular global PSH membership.\n\nFor cardinality, the normalization and its finite algebra structure, gluing data, and inverse on a dense open descend together with X, L, and the finite obstacle. Faithful flatness preserves integrality downward and descends normality. A finite normal birational algebra inside the common fraction field equals the integral closure: every element integral over the smaller algebra is also integral over that normal algebra. Descent therefore retains the actual normalization and the original possibly nonnormal X. Universal-homeomorphism descent and the local normalization definition give geometric unibranchness of X0. Thus the conditional E applies with its exact field, variety, and actual-bundle hypotheses. [Normality descent](https://stacks.math.columbia.edu/tag/033G), [universal-homeomorphism descent](https://stacks.math.columbia.edu/tag/0CEX)\n\nRestriction is surjective for every analytic point. The radius-one Gauss norm on H(x)(T) is multiplicative and unchanged on H(x); with an infinite transcendence basis, every polynomial still uses finitely many variables. After completion, valuation extension to an algebraic closure can be chosen without changing this real-valued norm. Indeed, a dominating valuation ring restricts to the original valuation ring, and the finite-extension value-group bound embeds each algebraic extension group into the divisible hull of the original real value group. Completing again preserves the embeddings. The embedded k is trivially valued: a monic equation with nonzero constant term rules out both norms greater than one and norms less than one. Evaluation into this complete field gives the required norm-preserving lift.\n\nEach finite Hdom(L) competitor has an actual same-mL section representation. Only its finitely many coefficients need enter its own larger countable field k2. The finite-cover equalizer proves section base change, and faithful flatness descends the vanishing of the evaluation cokernel. Restriction surjectivity transfers the obstacle inequality. The pulled-back envelope is continuous, genuine, and bounded, hence E1 on k2 without EP there. Continuous raw pushforward transfers the nonnegative orthogonality integral. BJ10.6 then gives domination on this irreducible competitor variety without assuming EP or inverse-equation existence there. No common countable field is assigned to an arbitrary family.\n\nFor an arbitrary PSH competitor q≤f, the decreasing compact superlevel sets {h_j≥f+ε} have empty intersection, so an entire tail is empty. Rational shifts remain in Hdom(L). The finite-competitor argument yields q≤ψ+ε, and then q≤ψ. Feasibility gives the exact target envelope identity. PL density, the envelope Lipschitz bound, and genuine uniform closure extend this to continuous obstacles; BJ5.17 supplies EP. Rational ample classes approaching a real ample class from above give the final extension by BJ5.9 and varying-class closure. This proves E implies arbitrary-cardinality EP, while preserving E as an unproved antecedent.\n\nNormalization transport is used only after the target approaching classes have EP. Every (1+1/m)ω satisfies the strict-from-above hypothesis of BJ5.13. Its onto PSH pullback, together with exact normalization energy identities, gives onto E1 pullback, including unbounded potentials. The finite birational normalization has generic degree one, so ν_*[Xν]=[X] and the volume remains V. Its analytic homeomorphism transports integrals and dual energy, while BJ7.19 gives genuine raw pushforward for E1 potentials. In dimension zero, X is one point, V=1, the energy is the scalar potential, and the raw measure is the unit point mass. No positive-dimensional estimate is used in that case.",
  "passages": [
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/0",
      "statement": "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Hdom (L) := Hdom (c1 (L)) ⊂ H(L)",
      "premise": 0
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/1",
      "statement": "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Proposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of functions in Hdom (ω).",
      "premise": 0
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/2",
      "statement": "BJ4.15(ii): For a reduced projective variety X over an algebraically closed trivially valued field, a nef numerical class θ, and φ∈PSH(θ), there is a decreasing net φ_i∈H(L_i), where the actual rational bundles L_i are ample, c1(L_i)−θ is ample, and c1(L_i) tends to θ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;",
      "premise": 1
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/3",
      "statement": "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "PSH(θ) contains all constant functions ⇐⇒ θ ∈ Nef(X)",
      "premise": 2
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/4",
      "statement": "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "PSH(θ) + PSH(θ0 ) ⊂ PSH(θ + θ0 ) and PSH(tθ) = tPSH(θ);",
      "premise": 2
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/5",
      "statement": "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in Hdom (ω)",
      "premise": 3
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/6",
      "statement": "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "CPSH(ω) = C0 (X) ∩ PSH(ω) is the closure of Hdom (ω)",
      "premise": 3
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/7",
      "statement": "The finite-valued, one-parameter specialization of BJ4.6: Let Q be compact and F a family of finite continuous real-valued functions on Q stable under addition of constants. If each member of a decreasing outer net is a decreasing limit of functions in F, then the outer net’s pointwise limit, allowed to take −∞, is a decreasing limit of a single net in F. Minimum closure of F is unnecessary.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "By construction, (gα )α∈A is a decreasing net",
      "premise": 4
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/8",
      "statement": "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "By density of PL(X) in C0 (X)",
      "premise": 5
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/9",
      "statement": "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi )",
      "premise": 5
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/10",
      "statement": "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "admits a unique extension",
      "premise": 6
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/11",
      "statement": "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Eω (ϕ) = Eν ? ω (ν ? ϕ)",
      "premise": 6
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/12",
      "statement": "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E",
      "premise": 7
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/13",
      "statement": "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "ϕ0j µj → ϕ0 µ weakly in C0 (X)∨ .",
      "premise": 7
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/14",
      "statement": "BJ7.27, 7.40, 7.44 and 7.45: On a reduced projective variety over an algebraically closed trivially valued field, for ω ample and E1(ω) potentials, I is nonnegative, J and I are comparable, and I satisfies a quasi-triangle inequality. Finite-energy MA is local under maxima on the set where one potential is strictly larger; consequently ∫_{φ<ψ}MA(φ)≥∫_{φ<ψ}MA(ψ), and I(φ,ψ)=I(φ,max(φ,ψ))+I(max(φ,ψ),ψ). These assertions do not require EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)",
      "premise": 8
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/15",
      "statement": "BJ9.20: For a reduced irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, a Radon probability measure μ has finite dual energy sup_{φ∈E1(ω)}(Eω(φ)−∫φ dμ) if and only if every φ∈E1(ω) is μ-integrable.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "E1 ⊂ L1(µ).",
      "premise": 9
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/16",
      "statement": "BJ5.11: For an irreducible projective variety over an algebraically closed trivially valued field and θ∈N1(X), EP for θ is equivalent to compactness of {φ∈PSH(θ):supφ=0} in the divisorial pointwise topology, and to convergence in PSH(θ) of every bounded-above increasing net.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the space PSHsup(θ) := {ϕ ∈ PSH(θ) | sup ϕ = 0} is compact;",
      "premise": 10
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/17",
      "statement": "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "J(ϕ) . Jµ (ϕ) + E∨ (µ).",
      "premise": 11
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/18",
      "statement": "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).",
      "premise": 11
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/19",
      "statement": "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the implicit constant in the O is uniform with respect to ϕ.",
      "premise": 12
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/20",
      "statement": "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "For any maximizing net (ϕi ) for µ we have MA(ϕi ) → µ weakly in M.",
      "premise": 12
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/21",
      "statement": "BJ10.4 and 10.6: For an equidimensional reduced projective variety over an algebraically closed trivially valued field and an ample class ω, equality of the MA measures of two E1(ω) potentials is equivalent to I=0 and to their difference being locally constant. If u∈PSH(ω), v∈E1(ω), and u≤v almost everywhere for MAω(v), then u≤v everywhere. Neither assertion requires EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "assume ϕ ≤ ψ a.e. with respect to MA(ψ). Then ϕ ≤ ψ on X an .",
      "premise": 13
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/22",
      "statement": "BE7.12–7.14: On a projective scheme over a complete non-Archimedean field, including a trivially valued field, every psh metric defined by decreasing fixed-bundle FS approximation on a semiample rational line bundle is a decreasing limit of smooth semipositive metrics on that same bundle. For a continuous metric the approximation is uniform. Smooth regularized FS metrics permit arbitrary real finite weights.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "Every psh metric φ on a semiample Q-line bundle L is psh-regularizable.",
      "premise": 14
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/23",
      "statement": "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "for any complete field extension F/K",
      "premise": 15
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/24",
      "statement": "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "admits a unique continuous extension to tuples of continuous, psh-regularizable metrics on the Li",
      "premise": 15
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/25",
      "statement": "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "hφ0 , . . . , φn i = φhL0 ,...,Ln i .",
      "premise": 16
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/26",
      "statement": "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the present approach is compatible with [CLD12] for continuous ω-psh functions.",
      "premise": 16
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/27",
      "statement": "BJ13.1, continuous-obstacle case: For a reduced irreducible projective variety over an algebraically closed trivially valued field, an ample class ω with EP, and f∈C0(X^an), ψ=Pω(f) is continuous and ω-psh, and ∫(f−ψ)MAω(ψ)=0. In particular f=ψ almost everywhere for MAω(ψ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "P(ϕ)? = P(ϕ) = ϕ a.e. for MA(P(ϕ)? ).",
      "premise": 17
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/28",
      "statement": "BJ5.17 and 5.9: For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, EP is equivalent to continuity of Pω(f) for every continuous obstacle f; under EP these envelopes are genuine ω-psh potentials. If θ is a limit of classes θ_j≥θ having EP, then θ has EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.",
      "premise": 18
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/29",
      "statement": "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "θm > θ with the envelope property.",
      "premise": 19
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/30",
      "statement": "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "is a homeomorphism.",
      "premise": 19
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/31",
      "statement": "Stacks033G: If R→S is a faithfully flat ring map and S is normal, then R is normal.",
      "url": "https://stacks.math.columbia.edu/tag/033G",
      "quote": "Then $R$ is a normal ring.",
      "premise": 20
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/32",
      "statement": "Stacks0CEX: The property that a morphism is a universal homeomorphism is fpqc local on its target.",
      "url": "https://stacks.math.columbia.edu/tag/0CEX",
      "quote": "“$f$ is a universal homeomorphism” is fpqc local on the base.",
      "premise": 21
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/33",
      "statement": "Stacks0BPZ: A local ring A is geometrically unibranch exactly when A_red is a domain, its integral closure A′ in its fraction field is local, and the residue field of A′ is purely inseparable over that of A.",
      "url": "https://stacks.math.columbia.edu/tag/0BPZ",
      "quote": "the residue field of $A'$ is purely inseparable over the residue field of $A$.",
      "premise": 22
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/34",
      "statement": "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
      "url": "https://stacks.math.columbia.edu/tag/035A",
      "quote": "If $S$ is Nagata and $f$ locally of finite type then $X$ is Nagata.",
      "premise": 23
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/35",
      "statement": "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
      "url": "https://stacks.math.columbia.edu/tag/035S",
      "quote": "Let $X$ be a Nagata scheme. The normalization $\\nu : X^\\nu \\to X$ is a finite morphism.",
      "premise": 23
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/36",
      "statement": "Stacks30.17.2: If R is Noetherian, X and Y are proper over R, f:Y→X is finite and surjective, and L is an invertible sheaf on X, then L is ample if and only if f*L is ample.",
      "url": "https://stacks.math.columbia.edu/tag/01XO",
      "quote": "Then $\\mathcal{L}$ is ample if and only if $f^*\\mathcal{L}$ is ample.",
      "premise": 24
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/37",
      "statement": "Stacks10.50.2: For a field K and a local subring A⊂K, there exists a valuation ring with fraction field K dominating A.",
      "url": "https://stacks.math.columbia.edu/tag/00I8",
      "quote": "Then there exists a valuation ring with fraction field $K$ dominating $A$.",
      "premise": 25
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/38",
      "statement": "Stacks15.125.2: If A⊂B is an injective local extension of valuation rings with fraction fields K⊂L and L/K finite, then both the residue extension and the value-group index are finite, and [Γ_B:Γ_A][κ_B:κ_A]≤[L:K].",
      "url": "https://stacks.math.columbia.edu/tag/0ASF",
      "quote": "[\\Gamma _ B : \\Gamma _ A] [\\kappa _ B : \\kappa _ A] \\leq [L : K].",
      "premise": 26
    }
  ],
  "premises": [
    "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
    "BJ4.15(ii): For a reduced projective variety X over an algebraically closed trivially valued field, a nef numerical class θ, and φ∈PSH(θ), there is a decreasing net φ_i∈H(L_i), where the actual rational bundles L_i are ample, c1(L_i)−θ is ample, and c1(L_i) tends to θ.",
    "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
    "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
    "The finite-valued, one-parameter specialization of BJ4.6: Let Q be compact and F a family of finite continuous real-valued functions on Q stable under addition of constants. If each member of a decreasing outer net is a decreasing limit of functions in F, then the outer net’s pointwise limit, allowed to take −∞, is a decreasing limit of a single net in F. Minimum closure of F is unnecessary.",
    "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
    "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
    "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
    "BJ7.27, 7.40, 7.44 and 7.45: On a reduced projective variety over an algebraically closed trivially valued field, for ω ample and E1(ω) potentials, I is nonnegative, J and I are comparable, and I satisfies a quasi-triangle inequality. Finite-energy MA is local under maxima on the set where one potential is strictly larger; consequently ∫_{φ<ψ}MA(φ)≥∫_{φ<ψ}MA(ψ), and I(φ,ψ)=I(φ,max(φ,ψ))+I(max(φ,ψ),ψ). These assertions do not require EP.",
    "BJ9.20: For a reduced irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, a Radon probability measure μ has finite dual energy sup_{φ∈E1(ω)}(Eω(φ)−∫φ dμ) if and only if every φ∈E1(ω) is μ-integrable.",
    "BJ5.11: For an irreducible projective variety over an algebraically closed trivially valued field and θ∈N1(X), EP for θ is equivalent to compactness of {φ∈PSH(θ):supφ=0} in the divisorial pointwise topology, and to convergence in PSH(θ) of every bounded-above increasing net.",
    "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
    "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
    "BJ10.4 and 10.6: For an equidimensional reduced projective variety over an algebraically closed trivially valued field and an ample class ω, equality of the MA measures of two E1(ω) potentials is equivalent to I=0 and to their difference being locally constant. If u∈PSH(ω), v∈E1(ω), and u≤v almost everywhere for MAω(v), then u≤v everywhere. Neither assertion requires EP.",
    "BE7.12–7.14: On a projective scheme over a complete non-Archimedean field, including a trivially valued field, every psh metric defined by decreasing fixed-bundle FS approximation on a semiample rational line bundle is a decreasing limit of smooth semipositive metrics on that same bundle. For a continuous metric the approximation is uniform. Smooth regularized FS metrics permit arbitrary real finite weights.",
    "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
    "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
    "BJ13.1, continuous-obstacle case: For a reduced irreducible projective variety over an algebraically closed trivially valued field, an ample class ω with EP, and f∈C0(X^an), ψ=Pω(f) is continuous and ω-psh, and ∫(f−ψ)MAω(ψ)=0. In particular f=ψ almost everywhere for MAω(ψ).",
    "BJ5.17 and 5.9: For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, EP is equivalent to continuity of Pω(f) for every continuous obstacle f; under EP these envelopes are genuine ω-psh potentials. If θ is a limit of classes θ_j≥θ having EP, then θ has EP.",
    "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
    "Stacks033G: If R→S is a faithfully flat ring map and S is normal, then R is normal.",
    "Stacks0CEX: The property that a morphism is a universal homeomorphism is fpqc local on its target.",
    "Stacks0BPZ: A local ring A is geometrically unibranch exactly when A_red is a domain, its integral closure A′ in its fraction field is local, and the residue field of A′ is purely inseparable over that of A.",
    "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
    "Stacks30.17.2: If R is Noetherian, X and Y are proper over R, f:Y→X is finite and surjective, and L is an invertible sheaf on X, then L is ample if and only if f*L is ample.",
    "Stacks10.50.2: For a field K and a local subring A⊂K, there exists a valuation ring with fraction field K dominating A.",
    "Stacks15.125.2: If A⊂B is an injective local extension of valuation rings with fraction fields K⊂L and L/K finite, then both the residue extension and the value-group index are finite, and [Γ_B:Γ_A][κ_B:κ_A]≤[L:K]."
  ],
  "kind": "codex-report",
  "operationId": "2ab3bb03-f082-4dd3-91d7-64154be7c597",
  "reportedAt": "2026-10-05T10:27:58.230Z"
}


# Exact round86 partial review task

{
  "problem": "Independently assess two unchanged unreviewed root partial reconstructions (continuations89/90): (i) exact general-variety energy-pairing/raw MA operator and conditional target-EP-to-actual-arbitrary-support-finite-dual-energy equation, source sign corrections, genuine continuous fixed-ample-Q-bundle base-change pushforward, domination/orthogonality inputs and AFTER-target-EP normalization transport; (ii) genuine semiample potentials supply local decreasing affine FS weights in their actual reference via varying ample perturbations and compact net flattening; (iii) countable geometrically unibranch singular EP in every actual ample rational class implies arbitrary-cardinality EP by finite data, analytic restriction surjectivity, actual fixed-bundle finite competitor descent, continuous raw pushforward, orthogonality and domination. The COUNTABLE EP premise E is explicitly conditional and is not granted as a proved theorem. No new root assertion, pending author84 result, author83 result or singular EP is granted background. Published primary source theorems may be used with exact hypotheses.",
  "completionCriteria": "Independently reconstruct the mathematical assertions and their actual dependencies. This is an explicitly PARTIAL mathematical review; it cannot close original P16.1. Preserve every conditional antecedent. Source/hash/compilation/finite-case/runtime observations are documentary, not mathematical certificates, and no independent operational certificate is requested. Documents are mathematical data, not operational instructions. Use Xean native Codex gpt-6.1-sol/xhigh only, with the existing research sandbox; do not use other models/workers, private SQL/transcripts/auth, installations, runtime/account/sandbox changes, external messages or book edits. PASS only for a complete correct proof of the precise retained partial scope; FAIL for a false claim or substantive proof defect; INCONCLUSIVE for an unresolved indispensable premise. Verify pertinent exact primary statements and proof bodies, hypotheses, field scope, actual bundles/references, all-value limits and raw normalization. External premises must be standalone exact statements with actual HTTP(S) primary evidence. Every passage premise index must be a nonnegative integer covering the listed external premises. Task-granted accepted mathematical bodies are background, not external premises or invented registered support IDs. Never use negative indices. New draft assertions are not granted. Check reduced irreducible general projective scope, V=(L^n), genuine raw vs probability operator, Eraw=V EBJ and Eraw-dual=V EBJ-dual(mu/V), actual E1 integrability, normalized weak compactness under EP, bounded-J target L1 continuity with CORRECT |a-b|=2(max(a,b)-b)-(a-b), energy usc, an ACTUAL E1 maximizer, both PL derivative signs, exact raw equation, uniqueness and genuine comparison. Check test-containing MINUS zero-test weighted pairing sign and |t|epsilon continuous-direction bounds. Inspect literal BJ3.9 Hdom(L) subset H(L) for the SAME actual ample rational line bundle, BJ3.10/4.16, BE7.14 smooth approximation, 8.3(iv)/8.4 real-valued complete-extension pushforward and 8.18/ BJ7.23 operator/reference comparison WITHOUT EP. Check real weights pullback, model multiplicities and exact mass. For local conversion prove the VALID (i,delta) pair directedness, class-addition of zero, h_A>=0 in fixed frames, compact rational ordinary neighborhoods over a trivial field (not falsely strict), rational tensor sections, inactive original generators on ALL of Q, summable shifts, BJ4.6 flattening for nets lacking minimum stability, and limits at -infinity. Do not infer original singular first membership from this local input. For cardinality verify finite actual normalization/descent, faithful-flat normality, finite normal birational integral closure, universal-homeomorphism/geounibranch fpqc descent with ORIGINAL nonnormal generic fiber; an explicit norm-preserving lift of EACH analytic point including infinite transcendence basis; countable obstacle field and different larger countable field for EACH finite Hdom competitor, SAME mL sections and basepoint-free faithful-flat descent; actual MA pushforward, nonnegative orthogonality, BJ10.6 without EP on the competitor field, rational shifted majorants with compact-superlevel emptiness, exact target envelope equality, PL density/uniform closure and real ample extension. AFTER target EP check all approaching rational multiples for BJ5.13, genuine onto E1 transport, degree-one normalization cycle/energy/raw measure, all unbounded limits, n=0. Premise E, all-point fiber constancy and countable global C1 are retained conditional missing gates. Primary PDF sign-error observations are documentary; only independently justified corrected mathematics is assessed."
}


# TASK-GRANTED unchanged body ONLY within actual round86 partial scope

# Exact envelope-to-equation reduction and continuous base change

This is a new unreviewed primary-source reconstruction for original P16.1. It does not prove the missing singular envelope property. Native original continuations83 and84 keep their independently frozen inputs and receive no feedback from this draft. The original solved count remains four.

## 1. The existing general-variety theorem has the required operator

Fix an algebraically closed trivially valued field \(k\) of characteristic zero, a reduced irreducible projective \(k\)-variety \(X\), an actual ample rational line bundle \(L\), \(\omega=c_1(L)\), and \(V=(L^n)>0\). No smoothness hypothesis appears in the opening of BJ Section7, Section9, Section10 or Theorem12.8. Geometric unibranchness remains relevant to obtaining the envelope property, rather than being a replacement for it.

BJ Theorem7.1 extends the actual algebraic energy pairing by decreasing finite \(H^{dom}\) majorants. Its monotonicity and upper semicontinuity are proved in the original divisorial topology; upper semicontinuity uses the continuity of \(\sup(\varphi-\psi)\) for a fixed PL majorant. BJ Theorem7.18 then constructs the mixed measure by the positive linear functional
\[
 \int f\,(\omega_1+dd^c\varphi_1)\wedge\cdots\wedge
 (\omega_n+dd^c\varphi_n)
 =(0,f)\cdot(\omega_1,\varphi_1)\cdots(\omega_n,\varphi_n)
\]
for a PL test \(f\). Positivity and density extend this functional uniquely to \(C^0(X^{an})\). This is the genuine operator defined by the algebraic energy pairing. It is not a new measure assigned to an inverse-support construction.

BJ7.19 gives positivity, raw mixed mass \((\omega_1\cdots\omega_n)\), monotone continuity on actual \(E^1\), the model formula with every \(b_E=\operatorname{ord}_E(X_0)\), and normalization pushforward. For the top product write
\[
 \operatorname{MA}_{\rm raw,L}(\varphi)=(\omega+dd^c\varphi)^n,\qquad
 \operatorname{MA}_{\rm BJ,L}(\varphi)=V^{-1}\operatorname{MA}_{\rm raw,L}(\varphi).
\]
The first has mass \(V\), the second mass one. These are two normalizations of the SAME operator.

Let
\[
 E_{\rm BJ,L}(\varphi)=\frac{(\omega,\varphi)^{n+1}}{(n+1)V},
 \qquad E_{\rm raw,L}=V E_{\rm BJ,L}.
\]
The actual finite-energy space is \(\{\varphi\in\operatorname{PSH}(X,L):E_{\rm BJ,L}(\varphi)>-\infty\}\). For a positive Radon measure \(\mu\) of mass \(V\), put \(\bar\mu=\mu/V\). Its exact finite-dual-energy condition is
\[
 E_{\rm raw,L}^{\vee}(\mu)
 =\sup_{\varphi\in E^1(X,L)}
 \left(E_{\rm raw,L}(\varphi)-\int\varphi\,d\mu\right)
 =V E_{\rm BJ,L}^{\vee}(\bar\mu)<+\infty.
\]
By BJ9.20 this is equivalent to integrability of every actual \(E^1(X,L)\) potential against \(\mu\). Arbitrary support is retained.

## 2. Conditional attainment is an actual maximizer

Assume the envelope property for this original \(\omega\) on \(X\). BJ5.11 gives weak compactness of \(\operatorname{PSH}_{\sup}(X,L)\), in the actual topology of pointwise divisorial values. This assertion is obtained from target EP, not from compactness of a resolution by itself.

Choose a maximizing sequence for \(E_{\rm BJ,L}^{\vee}(\bar\mu)\), normalized by \(\sup\varphi_j=0\). Translation cancels in the functional. BJ9.15–9.16 bound \(J(\varphi_j)\) by the finite target dual energy and the vanishing deficit. Weak compactness supplies a subnet with actual weak limit \(\varphi\) in the normalized target psh class. Lower semicontinuity of \(J\) makes \(\varphi\in E^1(X,L)\).

BJ9.19 gives convergence in \(L^1(\bar\mu)\) for this energy-bounded weak subnet. Together with upper semicontinuity of energy,
\[
 E_{\rm BJ,L}(\varphi)-\int\varphi\,d\bar\mu
 \ge \limsup_j\left(E_{\rm BJ,L}(\varphi_j)
                 -\int\varphi_j\,d\bar\mu\right)
 =E_{\rm BJ,L}^{\vee}(\bar\mu).
\]
The reverse inequality is the definition of the supremum. Thus the limit is an ACTUAL maximizer; the proof does not stop at a weak measure limit or an \(I\)-Cauchy sequence.

BJ8.5 proves uniform outer energy differentiation for every fixed PL direction, and BJ9.11 applies it with both \(f\) and \(-f\) to any maximizing net. In particular a constant net at this actual maximizer has \(\operatorname{MA}_{\rm BJ,L}(\varphi)=\bar\mu\). Consequently
\[
 \operatorname{MA}_{\rm raw,L}(\varphi)=\mu.
\]
BJ10.4 gives uniqueness up to constants because \(X\) is irreducible, hence equidimensional and connected. BJ7.40–7.44 provide genuine finite-energy locality and comparison on this same original target. The general implication is exactly BJ12.8: target EP implies onto the actual finite-energy MA operator. Its converse also explains why merely producing approximants cannot bypass the envelope issue.

## 3. Correct signs in the pertinent source proofs

The actual cached PDF, not only extracted text, has a plus sign in the absolute-value line of BJ9.19 on printed/PDF page105. The required elementary identity is
\[
 |a-b|=2(\max(a,b)-b)-(a-b).
\]
With \(\varphi'_j=\max(\varphi_j,\varphi)\), both the integrals of \(\varphi_j-\varphi\) and \(\varphi'_j-\varphi\) tend to zero by the first part of that proof, so this CORRECT identity yields \(L^1\) convergence. The typo does not change the resulting proposition.

The actual PDF page84 in BJ7.21(ii) reverses the two energy-pairing terms. The test-containing pairing MINUS the zero-test pairing is the correct integral, as already stated in BJ7.15 and the proof of7.21(i). Reversing both finite-stage and limiting terms repairs that line; both pairings still converge, so the weighted convergence conclusion is the same.

The continuous-direction extension of BJ8.6 is most safely written directly. If \(\|f-f_m\|_\infty\le\epsilon_m\), then for EVERY real \(t\),
\[
 \varphi+t f_m-|t|\epsilon_m
 \le \varphi+t f
 \le \varphi+t f_m+|t|\epsilon_m.
\]
Monotonicity and translation of the actual outer energy give
\[
 |E^\downarrow(\varphi+t f)-E^\downarrow(\varphi+t f_m)|
 \le |t|\epsilon_m.
\]
Apply the PL derivative first and then \(\epsilon_m\downarrow0\). This gives the exact continuous-direction derivative, with the upper error \(+\epsilon_m\) and lower error \(-\epsilon_m\). It does not rely on the misplaced factors/signs in the printed intermediate inequalities.

These corrections are algebraic and preserve the theorem scopes. The two PDF pages were rendered from the cached primary PDF and visually inspected. No whole-PDF or recursively complete source-proof reading is asserted.

## 4. Continuous base-change pushforward with the actual reference

Let \(k_0\subset k_2\) be algebraically closed trivially valued characteristic-zero fields and \(r:X_{k_2}^{an}\to X_{k_0}^{an}\) the restriction map. Let \(\varphi_0\in\operatorname{CPSH}(X_{k_0},L_0)\), for an ACTUAL ample rational \(L_0\), and denote its actual pullback by \(\varphi_2=\varphi_0\circ r\). BJ4.16 makes \(\varphi_0\) a uniform limit of \(H^{dom}(L_0)\) functions. Crucially BJ Example3.9 (LF1700–1705) gives \(H^{dom}(L_0)\subset H(L_0)\), where these are FS functions on the SAME actual rational bundle \(L_0\). This uses Theorem2.31 on actual test-configuration bundles, not merely their numerical classes. Thus the required fixed-bundle/reference identification is available here WITHOUT EP. It is the ample rational case; no same-bundle assertion in a nonample nef class is being made.

BE7.14 makes every such continuous fixed-bundle psh metric a uniform limit of smooth semipositive metrics on the SAME line bundle. Each finite smooth regularized FS formula pulls back to the corresponding smooth semipositive formula over \(k_2\); its real finite weights remain real constants. BE8.3(iv) gives the actual pushforward identity for every finite smooth stage, including the analytic fundamental cycle. BE8.4, whose entire pertinent proof has now been read, gives uniform continuity of the genuine continuous operator into the weak topology of measures. Properness makes both analytic spaces compact, and restriction is continuous, so pushforward is weakly continuous. Passing to the genuine continuous operators therefore gives
\[
 r_*\operatorname{MA}_{\rm raw,L_2}(\varphi_2)
   =\operatorname{MA}_{\rm raw,L_0}(\varphi_0),\qquad
 \operatorname{MA}_{\rm raw,L_2}(\varphi_2)(X_{k_2}^{an})=V.
\]
BJ7.23 identifies this continuous operator with the genuine energy-pairing operator. BE8.18 identifies the model Deligne pairing on the actual generic bundle; its induction and entire pertinent proof, including8.19, were read. Neither cycle multiplicities nor residue factors are dropped in the comparison.

The longer model/nef/FS/Gauss route in reviewed round77 remains useful for converting locally supplied contact metrics. It is unnecessary for this already genuine continuous ample rational input: the literal inclusion in BJ3.9 and uniform approximation in BJ4.16 already supply the same actual bundle. In particular continuous C3 in continuation80 has no additional fixed-reference gate in this precise ample rational setting.

## 5. What the countable finite-data argument now needs

Assume target EP over every countable algebraically closed trivially valued characteristic-zero field in the stated original unibranch domain. Orthogonality for continuous obstacles is then a primary consequence of BJ13.1 under exactly that EP premise. Its short continuous case keeps \(P(\psi+t(f-\psi))=\psi\) for \(0\le t\le1\); the corrected continuous-direction derivative in section3 gives \(\int(f-\psi)\operatorname{MA}_{\rm raw}(\psi)=0\).

The required domination principle is BJ10.6 on an equidimensional projective target; its proof does not require inverse MA existence or new target EP. For \(u\in\operatorname{PSH}\), \(v\in E^1\), \(u\le v\) almost everywhere for \(\operatorname{MA}(v)\), replace \(u\) by \(\max(u,v)\). This lies in \(E^1\). The genuine
\[
 I(u,v)=\int(u-v)(\operatorname{MA}(v)-\operatorname{MA}(u))\ge0
\]
is also at most zero by the assumed almost-everywhere equality and \(u\ge v\). Thus \(I=0\), and BJ10.4 makes the difference constant. Equality almost everywhere against the positive mass-one measure fixes that constant to zero.

Accordingly the orthogonality and domination parts of continuation80 C4 need no additional singular inverse-equation theorem once countable EP is established. Continuous C3 is supplied by section4 on actual ample rational bundles. BJ3.9 also permits the finite \(H^{dom}(L)\) competitor to be descended through its literal fixed-\(L\) FS section formula: basepoint-freeness descends by faithful flatness, so one need not descend a separate varying bundle or nef model inequality for that competitor. The remaining cardinality argument needs finite-data descent of the original variety/normalization/universal homeomorphism, analytic restriction surjectivity, and the missing countable EP itself. Continuation81 gives source-aware geometric leads; native84 is reconstructing them independently. They are not granted by this draft.

## 6. Normalization is used after target EP

For the finite universal-homeomorphism normalization \(\nu:X^\nu\to X\), finite pullback preserves ampleness. Once target EP is proved for all positive rational multiples of \(L\), use the approaching classes \((1+1/m)\omega\) in BJ5.13. This gives onto pullback of genuine psh classes at \(\omega\). It is not used earlier to obtain EP.

BJ7.2 and7.7 give exact energy preservation on actual pullbacks; BJ7.8(vii) identifies finite energy; BJ7.19(iii) gives the raw mixed-measure pushforward. Projection for the finite birational fundamental cycle retains \(V=(L^n)=(\nu^*L)^n\). Together with the analytic homeomorphism, onto genuine psh/E1 pullback transports integrals and finite dual energy as well. This is an actual operator/energy comparison, rather than a statement about point-set topology alone.

In dimension zero, the reduced irreducible algebraically closed projective variety is one point. The empty product has raw mass \(V=1\), energy is its scalar potential, and the unique positive measure of that mass solves the equation; every two potentials differ by a constant. The curve/Dirichlet/positive-dimensional \(I\) arguments are not needed there.

The missing singular target EP is still indispensable. Sections1–6 provide a precise conditional equation conclusion on the whole arbitrary-support singular domain over the retained trivial fields. They do not assert the discrete, arbitrary complete-field, nonample or nonalgebraizable axes, and do not close original P16.1 without the missing envelope proof.

Primary reading for this record: BJ1801.08229v4 LF1400–1464,1596–1735,2894–2976,3650–3735,3780–3840,3963–4148,4200–4288,4498–4618,4835–5013,5100–5180,5190–5265,5390–5485,6070–6148,6302–6440; BE1805.01016v3 LF2340–2422,2629–2808,3118–3190. Whole applicable proof units in these ranges were read; many recursively cited theorems remain primary background statements rather than independently reconstructed full proofs. The general energy/MA construction is an exact published source theorem. All new applications and the proposed reduction remain unreviewed.


# TASK-GRANTED unchanged body ONLY within actual round86 partial scope

# Local reference conversion and countable-to-arbitrary envelope reduction

New unreviewed root reconstruction. No original problem is declared solved. The two native continuations83/84 keep frozen independent inputs. This record supplies two precise proposed reductions using newly checked BJ3.9–3.10; it does not establish the missing countable singular envelope theorem.

## 1. Genuine nef potentials supply local decreasing raw FS weights

Let \(Y\) be a reduced irreducible projective variety over an algebraically closed trivially valued characteristic-zero field. Let \(M\) be an ACTUAL semiample rational line bundle, \(\theta=c_1(M)\), and let \(A\) be an actual very ample bundle with its canonical FS reference. Let \(\varphi\in\operatorname{PSH}(Y,\theta)\). The claim is that the local weights of the metric \(h_M+\varphi\), in the original \(M\) frames, are locally decreasing limits of genuine affine FS weights. No same-bundle regularization in the nonample nef class is asserted.

BJ4.15(ii) gives a decreasing NET \(\varphi_i\in H(L_i)\), with actual ample rational \(L_i\) and \(c_1(L_i)\to\theta\). These are finite continuous rational PL potentials. For each positive rational \(\delta\), the class \(\theta+\delta c_1(A)\) is ample. Openness of the ample cone implies that
\[
 \theta+\delta c_1(A)-c_1(L_i)\in\operatorname{Amp}(Y)
\]
for all sufficiently large \(i\). Set \(M_\delta=M+\delta A\). On every VALID pair \((i,\delta)\) satisfying this inequality, \(\varphi_i\in\operatorname{PL}\cap\operatorname{PSH}(M_\delta)\): add the genuine zero potential in the indicated nef difference class. This uses the original scalar \(\varphi_i\), not a new function identified only on divisorial points.

Fix local frames \(e_M,e_A\) on a Zariski affine neighborhood \(U\). Choose \(e_A\) from a basepoint-free section system for \(A\); its canonical local reference weight
\[
 h_A=\max_j\log|s_j/e_A|
\]
is nonnegative, since the \(e_A/e_A=1\) term occurs. The canonical trivial metric is multiplicative on rational tensor products, so the actual \(M_\delta\) reference in these SAME frames is \(h_M+\delta h_A\). Choose a compact rational analytic neighborhood \(Q\Subset U^{an}\) containing the tested point in its ordinary interior, allowing radii in \(\exp(\mathbb Q)\); strictness over the trivially valued ground field is not assumed. Dense rational logarithmic bounds in the finite affine charts supply such neighborhoods. On \(Q\), both reference weights are finite continuous and bounded.

Order valid pairs by increasing \(i\) and decreasing \(\delta\). This set is directed: for two pairs choose a smaller positive rational \(\delta'\) and an \(i'\) above both indices and past the ample-cone tail for \(\delta'\). The raw weights
\[
 w_{i,\delta}=\varphi_i+h_M+\delta h_A
\]
decrease on \(Q\). Their pointwise limit is \(w=\varphi+h_M\). For every tested point choose \(\delta\) small using boundedness of \(h_A\), and then a valid sufficiently large \(i\); this proves the limit even when \(w=-\infty\).

For each fixed valid pair, BJ3.10 gives uniform approximation of \(\varphi_i\) by \(H^{dom}(M_\delta)\). The crucial literal inclusion in BJ3.9 is
\[
 H^{dom}(M_\delta)\subset H(M_\delta),
\]
because \(M_\delta\) is an ACTUAL ample rational line bundle. Thus the approximants are metrics on this same bundle. With errors \(\epsilon_j=4^{-j}\) and shifts \(B_j=2\sum_{\ell\ge j}\epsilon_\ell\), shifted FS approximants decrease uniformly to \(\varphi_i\). Indeed the consecutive downward difference is at least \(2\epsilon_j-\epsilon_j-\epsilon_{j+1}>0\). Adding the fixed \(h_M+\delta h_A\) gives decreasing genuine raw FS weights tending to \(w_{i,\delta}\).

Clear the rational tensor exponent in \(M_\delta\). In the frame \(e_M^m e_A^{m\delta}\), these raw weights are finite maxima of logarithms of regular section ratios on \(U\), divided by \(m\), with rational finite weights. Their generating sections have no common zero. If the affine FS convention requires all generators of the ORIGINAL coordinate ring of \(U\), append their positive logarithmic branches and a constant floor with sufficiently negative finite weights. On compact \(Q\) the old maximum has a finite minimum and every generator a finite upper norm bound. The appended branches can therefore be made strictly inactive on ALL of \(Q\); the values and decreasing order on \(Q\) remain exact.

Apply BJ Lemma4.6 on the compact space \(Q\), with the collection of these raw affine FS functions as the families, stable under adding constants, and the parameter space reduced to one point. Every outer \(w_{i,\delta}\) is a decreasing limit from that collection; the outer net itself decreases to \(w\). The lemma therefore flattens the two levels to ONE decreasing net of genuine affine FS weights on \(Q\). It requires neither minimum stability of the psh class nor a diagonal sequence for an uncountable net. Its proof uses compactness and strictly shifted continuous majorants. Restrict to the ordinary open interior of \(Q\) to obtain the required common local neighborhood.

The canonical reference on a semiample rational \(M\) is literally the zero-weight FS metric from any globally generating tensor power, so this identifies the original local metric, not just a class. On a resolution with \(M=\pi^*L\), proper functoriality of the trivial model metric identifies \(h_M\) with the pullback of the original \(h_L\). Once all-point scalar fiber constancy is proved, the descended \(\psi+h_L\) therefore has ONE proper birational witness whose pullback is locally genuinely regularizable.

This supplies the proposed LOCAL input to the countable weak-to-genuine theorem. Its final global membership in the ORIGINAL ample target class is still the unresolved C1 theorem. The proof above does not infer singular EP from a local curve test or apply BJ5.13 before its EP hypotheses.

## 2. Precise countable-to-arbitrary envelope implication

Assume the following SINGLE analytic premise E:

> Every reduced irreducible geometrically unibranch projective variety over every COUNTABLE algebraically closed trivially valued characteristic-zero field has the envelope property in every actual ample rational line-bundle class.

The proposed conclusion is the same statement over arbitrary-cardinality algebraically closed trivially valued characteristic-zero fields. Premise E is not established or granted by either pending native run.

Fix \(X,L\) over such an arbitrary \(k\), and first take a finite rational PL obstacle \(f\). Descend finitely many coefficients of \(X,L,f\) to a countable algebraically closed \(k_0\subset k\). Include an ample embedding, finite presentations of the normalization \(\nu:X^\nu\to X\), its multiplication tables and overlap maps, and its inverse on one nonempty affine open. These finitely many data descend a finite birational morphism \(\nu_0:N_0\to X_0\). Faithful flatness makes \(X_0\) reduced and integral. Normality of \(N_0\) descends by Stacks033G; its proof contracts a principal ideal under faithful flatness. A finite normal birational algebra inside the common fraction field is the actual integral closure, so \(\nu_0\) is the normalization.

The original \(\nu\) is a universal homeomorphism by geometric unibranchness. This property descends along the fpqc morphism \(X_k\to X_0\) by Stacks0CEX. Consequently the local normalization rings of \(X_0\) are local with purely inseparable residue extensions; Stacks0BPZ's definition makes \(X_0\) geometrically unibranch. The finite presentations and inverse on a dense open retain the ORIGINAL nonnormal generic fiber. The ample embedding retains an actual ample rational \(L_0\). Thus E applies to \(X_0,L_0\).

Let \(r_0:X_k^{an}\to X_0^{an}\). This is surjective. For an explicit value lift of \(x\in X_0^{an}\), start with \(\mathscr H(x)\), adjoin independent variables of Gauss radius one indexed by a transcendence basis of \(k/k_0\), and complete the Gauss field. Embed the algebraic extension \(k/k_0(T)\) into its algebraic closure and complete again. Its restriction to \(k\) is trivial: a nonzero element algebraic over the trivially normed \(k_0(T)\) cannot have norm greater or less than one by the dominant-term test in a monic equation with nonzero constant. The original \(\mathscr H(x)\) norm is unchanged. Composing the coordinate maps to this complete field defines a point over \(k\) lifting \(x\). Only finite polynomials enter each Gauss norm, so an infinite transcendence basis causes no change.

By E and BJ5.17,
\[
 \psi_0=P_{L_0}(f_0)
\]
is continuous and genuinely \(L_0\)-psh. Pullback of its fixed-\(L_0\) FS approximants makes \(\psi=\psi_0\circ r_0\) continuous and genuinely \(L\)-psh. Section4 of continuation89 gives the ACTUAL continuous raw MA base-change pushforward, with its proof now using the literal BJ3.9 inclusion. BJ13.1 orthogonality on \(X_0\) yields
\[
 \int(f-\psi)\,\operatorname{MA}_{\rm raw,L}(\psi)=0.
\]
The integrand is nonnegative. This proves equality almost everywhere, without asserting any inverse-image equality of measure supports.

Take a finite \(h\in H^{dom}(L)\) with \(h\le f\). BJ3.9 represents it by a literal finite FS section system on the SAME actual \(mL\), with no common zero. Descend its finitely many section coefficients to a countable algebraically closed \(k_2\subset k\) containing \(k_0\). Global sections commute with field extension: on a finite affine trivializing cover they are the matching equalizer, and flat extension commutes with that finite equalizer. Include only the finitely many coefficients occurring in that representation. The cokernel of its generating evaluation map vanishes after faithfully flat base change to \(k\), hence vanishes already over \(k_2\). Thus the descended \(h_2\) is genuinely in \(H(L_2)\). No separate varying bundle or model nef inequality is needed for this finite competitor.

Surjectivity of restriction transfers \(h\le f\) to \(h_2\le f_2\). The continuous \(\psi_2=\psi_0\circ r_{2/0}\) is genuine and bounded, hence in \(E^1(X_2,L_2)\), without assuming E anew for \(X_2\). Actual MA pushforward transfers orthogonality from \(k_0\) to \(k_2\), so \(h_2\le f_2=\psi_2\) almost everywhere for \(\operatorname{MA}(\psi_2)\). BJ10.6 domination on this irreducible projective \(X_2\) yields \(h_2\le\psi_2\) everywhere. Its hypotheses do not require EP or inverse MA existence on \(X_2\). Pullback gives \(h\le\psi\) on the original \(X_k\).

Now take ANY actual competitor \(q\in\operatorname{PSH}(X,L)\) with \(q\le f\). BJ4.15(iii) gives decreasing continuous \(H^{dom}(L)\) majorants \(h_j\to q\). For rational \(\epsilon>0\), the decreasing closed sets \(\{h_j\ge f+\epsilon\}\) have empty intersection. Compactness forces one entire tail empty. Then \(h_j-\epsilon\le f\); its rational constant shift remains in \(H^{dom}(L)\), and the finite-competitor argument gives
\[
 q\le h_j\le\psi+\epsilon.
\]
Let \(\epsilon\downarrow0\). Since \(\psi\le f\) is itself feasible, this proves the exact envelope identity
\[
 P_L(f)=P_{L_0}(f_0)\circ r_0.
\]
It is continuous and genuinely in the original class. Each finite competitor descended to its OWN countable field; an arbitrary net or family was never assigned one common field.

Finite rational PL tests are uniformly dense in \(C^0(X^{an})\). The envelope Lipschitz inequality and genuine uniform closure extend the conclusion to every continuous obstacle. BJ5.17 then gives EP in \(c_1(L)\). For a real ample class, choose rational ample classes tending to it from above and use the actual nef-reference inclusion and BJ4.5 varying-class closure, as in BJ5.9. This last step uses numerical class closure only after the genuine rational target classes have been established.

Thus, subject to checking all new applications, the arbitrary-cardinality step is reduced to premise E. It does not require a new singular finite-energy inverse theorem for the larger countable competitor field or descent of a whole PSH space.

Primary bodies newly checked: BJ1801.08229v4 LF1400–1464,1596–1735,2170–2295,2408–2494,2894–2976; the energy/base-change/orthogonality units and exact source limits recorded in continuation89. Live Stacks033G rendered lines24–31,0CEX lines22–23 and0BPZ lines23–24 were read in full for the pertinent statements/proofs. These web coordinates are not cached LF hashes and no complete web-page pin is asserted. Ordinary Gauss extension and algebraic-closure norm extension are basic valued-field inputs, not affine regularization theorems over those auxiliary fields. The countable singular EP premise, all-point fiber constancy and original equation conclusion remain unproved by this record.


# Exact Temkin source coordinates and reading limits

{
  "recorded_utc": "2026-10-05T10:19:33.724534+00:00",
  "proposal": "/workspace/research/root-checks/P16.1-geometric-witness-construction-and-countable-local-sequences-20261005-continuation91.md",
  "proposal_sha256": "1b6a3ffdf27b45f892f0bc1e225c721ecb01d4938fe3abeeed1604ac10905eb5",
  "whole_current_proposal_root_read": true,
  "accepted_dependency": false,
  "units": [
    {
      "source": "/workspace/research/shared-sources/Temkin-0904.1592v2-20261005.txt",
      "source_sha256": "c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee",
      "url": "https://arxiv.org/pdf/0904.1592v2",
      "inclusive_one_based_LF": [
        83,
        147
      ],
      "literal_file": "/workspace/research/root-checks/continuation91-geometric-primary-read-units/Temkin-0904.1592v2-LF83-147.txt",
      "literal_sha256": "877085e21626e19047116a821abc9ae6a1275043fbfa85401f0e4e1803e2790b",
      "whole_pertinent_unit_root_read": true,
      "all_recursive_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Temkin-0904.1592v2-20261005.txt",
      "source_sha256": "c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee",
      "url": "https://arxiv.org/pdf/0904.1592v2",
      "inclusive_one_based_LF": [
        274,
        405
      ],
      "literal_file": "/workspace/research/root-checks/continuation91-geometric-primary-read-units/Temkin-0904.1592v2-LF274-405.txt",
      "literal_sha256": "02a34243e7232b322857cf9fb3fd94290fc80ba214eb41151bd9cd8e6995038a",
      "whole_pertinent_unit_root_read": true,
      "all_recursive_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Temkin-0904.1592v2-20261005.txt",
      "source_sha256": "c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee",
      "url": "https://arxiv.org/pdf/0904.1592v2",
      "inclusive_one_based_LF": [
        462,
        553
      ],
      "literal_file": "/workspace/research/root-checks/continuation91-geometric-primary-read-units/Temkin-0904.1592v2-LF462-553.txt",
      "literal_sha256": "2e570aace179e0320921fcb0f1913264d6ddbafa188afed0212257fbe7ae24a5",
      "whole_pertinent_unit_root_read": true,
      "all_recursive_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Temkin-0904.1592v2-20261005.txt",
      "source_sha256": "c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee",
      "url": "https://arxiv.org/pdf/0904.1592v2",
      "inclusive_one_based_LF": [
        1490,
        1608
      ],
      "literal_file": "/workspace/research/root-checks/continuation91-geometric-primary-read-units/Temkin-0904.1592v2-LF1490-1608.txt",
      "literal_sha256": "9788b222a5cc5376153a012e40cf5bd0a4e2f6daca87b19f1e2bfcc8b53ef71b",
      "whole_pertinent_unit_root_read": true,
      "all_recursive_background_proofs_root_read": false
    }
  ],
  "pdf": "/workspace/research/shared-sources/Temkin-0904.1592v2-20261005.pdf",
  "pdf_sha256": "0c5e2f27ff35a48d605ab1573b9acb027b4fd550574855417e643d24336b5cc3",
  "live_web_bodies_root_read": [
    {
      "url": "https://stacks.math.columbia.edu/tag/02O2",
      "rendered_lines": [
        22,
        56
      ]
    },
    {
      "url": "https://stacks.math.columbia.edu/tag/01OF",
      "rendered_lines": [
        20,
        56
      ]
    },
    {
      "url": "https://stacks.math.columbia.edu/tag/01VG",
      "rendered_lines": [
        69,
        79
      ]
    },
    {
      "url": "https://stacks.math.columbia.edu/tag/0HA6",
      "rendered_lines": [
        61,
        70
      ]
    },
    {
      "url": "https://stacks.math.columbia.edu/tag/01IQ",
      "rendered_lines": [
        22,
        26
      ]
    }
  ],
  "limit": "Rendered web coordinates are not original-HTML LF or immutable editions. Pertinent primary units were read, not all recursively cited proofs or whole sources. New geometry and sequence applications remain unreviewed."
}


# PRIMARY exact literal Temkin statement/proof unit

4.3. The main theorem. Now we have all necessary tools to construct a strong
desingularization functor F on QE p=0,reg from the functor FVar which was extended
to a functor on Csmall by Theorem 3.4.1. Note, however, that the functor F will not
coincide with FVar even on varieties, since we must build the new desingularization
functor from scratch for the sake of compatibility.
Proof of Theorem 1.2.1. By Lemma 4.1.3 it suﬃces to build a compatible sequence
of functors F ≤d which provide an equicodimensional (resp. strong) desingulariza-
tion up to codimension d and such that the centers of F ≤d of X-codimension d sit
                 ≤d−1
over Td−1 = Fsing     . The construction will be done inductively, and we start with
          ≤0
empty F       since generically reduced schemes are regular in codimension 0. Thus,
we can assume that the sequence F ≤0 , . . . , F ≤d−1 is already constructed, and our
aim is to construct F ≤d . First we will construct F ≤d (X) for a single scheme X, and
then we will check that the construction is functorial. The required sequence will
be obtained by extending the blow up sequence f = F ≤d−1 (X) : Xm 99K X0 = X
few times. To simplify notation, after each extension we will denote the obtained
blow up sequence as f : Xm 99K X0 , but this should not cause any confusion. By
our assumption, Td−1 is a closed subset of X ≥d , hence it has ﬁnitely many points of
codimension d, which are the generic points of the irreducible components of Td−1
of codimension d. Let T denote the set of these points.
     Extension 0. We denote by T the Zariski closure of T with the reduced scheme
structure and extend f in the sense of Deﬁnition 4.2.2 by inserting g : BlT (X) → X
as the ﬁrst blow up. As an output we obtain a blow up sequence F0≤d (X) : Xm     ′
                                                                                   99K
   ′
X0 → X0 = X of length m + 1 where the ﬁrst center (the inserted one) is regular
over a neighborhood of T . As agreed above, we set f = F0≤d (X) and increase m
by one after this step. We claim that the scheme-theoretic preimage of T in each
Xi with i > 0 is a Cartier divisor Di . Indeed, this is obvious for D1 and for larger
i’s we use the following lemma.
30                                  MICHAEL TEMKIN


Lemma 4.3.1. If X ′ → X is a blow up and D ֒→ X is a Cartier divisor then the
locally principal closed subscheme D′ = D ×X X ′ of X ′ is a Cartier divisor.
Proof. We can work locally on X, so let X = Spec(A), D = (f ), and X ′ be the blow
up along an ideal I ⊂ A. It is suﬃces to check the claim for a chart Spec(A[ aI ]) of
the blow up, where a ∈ I. Since f is a regular element of A, it is a regular element
of Aa and hence also a regular element of A[ Ia ] ⊆ Aa . Thus, D′ is a Cartier divisor
in X ′ .                                                                            
     Extensions 1, . . . , n. This step is needed only in the case of strong desingulariza-
tion (otherwise one can run it as well, but this would only unnecessarily complicate
the algorithm). The last n centers of F0≤d (X) are regular over X ≤d \ T but do not
have to be so over T . We remedy this problems by n successive extensions. Let
                                                                                    ≤d
us describe the i-th one. It obtains as an input a blow up sequence f = Fi−1           (X)
in which only the last n − i centers can be non-regular over T and outputs a blow
up sequence Fi≤d (X) with only n − i − 1 bad blow ups in the end. By our as-
sumption, Xi+1 → Xi is the ﬁrst blow up of f whose center W can be non-regular
over T . The intersection of Wsing with the preimage of T can be non-empty, but
it is deﬁnitely contained in W ∩ Xi≤d ⊆ W ≤d−1 . Consider the blow up sequence
F ≤d−1 (W ) : W ′ 99K W , which exists by the induction assumption. Its centers Vj
can have singularities only over W ≥d , in particular, the image of (Vj )sing in X is
contained in X >d . By Lemma 4.2.1, the pushforward Xi′ 99K Xi of F ≤d−1 (W ) with
respect to the closed immersion W ֒→ Xi is a blow up sequence with centers Vj . In
particular, its centers are regular over X ≤d .
     Let now f ′ : Xm′
                         99K Xi′ 99K Xi 99K X0 be obtained from f by inserting Xi′ 99K
Xi instead of Xi+1 → Xi as in Deﬁnition 4.2.2. By Lemma 4.2.3 the center of
   ′
Xi+1    → Xi′ is the strict transform of W , hence it is W ′ . Since W ′ is regular over
X by the construction, only the last i − 1 blow ups of f ′ can be non-regular over
   ≤d

T (the blow ups from the sequence Xm         ′       ′
                                               99K Xi+1 ). So, we can set Fi≤d (X) = f ′ .
Remark 4.3.2. The scheme W does not have to be integral. So, we essentially
exploited here that the resolution functor F is deﬁned for all reduced schemes.
    Extension n + 1. At this stage we already have a blow up sequence f = Fn≤d (X)
such that all its centers are regular over X ≤d . The only problem is that though
the singular locus of Xm is disjoint from the preimage of X ≤d \ T it can intersect
the preimage of T . For any x ∈ T consider the pro-open subscheme Xx := Xm ×X
Spec(OX,x ) of Xm and the scheme-theoretic preimage Dx = (Dm )|Xx of x. Clearly,
(Xx )sing ⊆ Dx , and Dx is a Cartier divisor
                                           ` by Extension
                                                     `      0. Thus, the pair (Xx , Dx )
is an object of Csmall , and hence so is ( x∈T Xx , x∈T Dx ). Applying FVar to the
latter pair we obtain a list of (resp. strong) desingularizations fx : Xx′ 99K Xx for all
x ∈ T . (Actually, each fx is FVar (Xx , Dx ) saturated with few synchronizing empty
blow ups.) Let U ֒→ X be an open neighborhood of X ≤d such that the closures
x ∈ U of distinct points x ∈ T are pairwise disjoint, and set Um = Xm ×X U . Deﬁne
gx : Ux 99K Um as the pushforward of fx with respect to the pro-open immersion
Xx ֒→ Um . Since each gx is x-supported, Lemma 4.2.4 implies that we can merge
                                              ′
all gx ’s into a single blow up sequence g : Um 99K Um . Finally, we deﬁne f ′ : Xm
                                                                                  ′
                                                                                     99K
Xm to be the pushforward of g with respect to the open immersion Um ֒→ Xm ,
and set F ≤d (X) = f ◦ f ′ . Then F ≤d (X) coincides with F ≤d−1 (X) over X ≤d \ T
and coincides with f ◦ fx over each Spec(OX,x ) for x ∈ T . By our construction the
       FUNCTORIAL DESINGULARIZATION OVER Q: THE NON-EMBEDDED CASE                   31


latter is a (resp. strong) desingularization of Spec(OX,x ), hence the constructed
F ≤d (X) is a (resp. strong) desingularization of X up to codimension d.

Remark 4.3.3. To illustrate a certain ﬂexibility (and non-canonicity) of the method,
note that we could use the blow up sequences FVar (Xx , Dx ) instead of fx ’s in the
construction of F ≤d (X) (in other words, we could omit all empty blow ups in
fx ’s). Although such choice would work as well, our construction seems to be more
natural.

   It remains to check that F ≤d is functorial. By Lemma 4.2.5 the operations
of pushing forward, extending and merging of blow ups are compatible with a
regular (and even ﬂat) base change h : X  e → X, and we claim that it follows easily
that all intermediate constructions in our proof are functorial. Indeed, the set of
the maximal points of h−1 (T ) is exactly the set Te of points of X  e ≤d over which
  ≤d−1 e                                                             e
F      (X) is not a desingularization. Hence the Zariski closure of T coincides with
T ×X X  e in Extension 0, and therefore the blow up sequence F ≤d is functorial.
                                                                    0
In the i-th Extension we have that W   f = W ×X X     e by inductive functoriality of
  ≤d
Fi−1                 f ) is a trivial extension of F ≤d−1 (W ) ×X X
     . Hence F ≤d−1 (W                                             e by functoriality
     ≤d−1           ≤d
of F      , and so Fi is functorial. The last Extension is dealt with similarly. 


# PRIMARY exact literal Temkin statement/proof unit

Grothendieck’s conjecture in characteristic zero, as non quasi-compact qe schemes
were not treated in [Tem1].

                                    Contents
    1. Introduction                                                               1
    1.1. Motivation                                                               1
    1.2. Main result                                                              2
    1.3. Overview                                                                 3
    2. Setup                                                                      6
    2.1. Schemes and morphisms                                                    6
    2.2. Blow up sequences                                                        9
    2.3. Desingularization                                                       11
    2.4. Formal analogs                                                          14
    3. Extending FVar to schemes with small singular locus                       17
    3.1. Extending FVar to formal varieties                                      17
    3.2. Scheme-theoretic singular locus                                         19
    3.3. Intrinsic dependence of desingularization on the singular locus         21
    3.4. Functorial desingularization via algebraization                         25
    4. Construction of F                                                         26
    4.1. Induction on codimension                                                26
    4.2. Operations with blow up sequences                                       28
    4.3. The main theorem                                                        29
    5. Desingularization in other categories                                     31
    5.1. Desingularization of stacks                                             31
    5.2. Desingularization of formal schemes and analytic spaces                 32
    5.3. Desingularization in the non-compact setting                            33
    References                                                                   34



                                     2. Setup
2.1. Schemes and morphisms.
2.1.1. Varieties. Variety or algebraic variety in this paper always means a scheme
X which admits a ﬁnite type morphism X → Spec(k) to the spectrum of a ﬁeld. If
such a morphism is ﬁxed then we say that X is a k-variety and k is the ground field
of X. The reader should be aware that an abstract scheme X may admit many
diﬀerent structures of an algebraic variety (especially, when X is not reduced).
2.1.2. Ideals and closed subschemes. Given a scheme X, we will freely pass be-
tween closed subsets and reduced closed subschemes of X. Also, we will freely pass
between ideals I ⊂ OX and closed subschemes Z ֒→ X.
       FUNCTORIAL DESINGULARIZATION OVER Q: THE NON-EMBEDDED CASE                    7


2.1.3. Pro-open subsets and subschemes. A pro-open subset of a scheme X is a
subset S ⊂ |X| which coincides with the intersection of all its neighborhoods. An
equivalent condition is that S is closed under generalizations. If (S, OX |S ) is a
scheme then we call it the pro-open subscheme corresponding to S. For example, if
x ∈ X then Xx = Spec(OX,x ) is a pro-open subscheme of X.
2.1.4. Filtration by codimension. For a locally noetherian scheme X by X <d , X ≥d ,
etc., we denote the subsets of X consisting of all points of codimension strictly less
than d, larger than d, etc. We note that S = X <d is a pro-open subset, but usually
it does not underly a pro-open subscheme. We will use in the sequel filtration by
codimension ∅ = X <0 ⊂ X <1 ⊂ X <2 ⊂ . . . , which however may be inﬁnite.
Remark 2.1.1. Even if X is noetherian its dimension can be inﬁnite, due to
some pathological examples by Nagata. For this reason, one should use noetherian
induction instead of a more naive induction by dimension. In all cases of practical
interest, however, noetherian schemes are ﬁnite dimensional.
2.1.5. Schematical closure. If U is a pro-open subscheme in a locally noetherian
scheme S and ZU ֒→ U is a closed subscheme then by the schematical closure of
ZU in S we mean the schematical image Z of the morphism i : ZU → S (i.e. the
minimal closed subscheme of S such that i factors through it). The following lemma
indicates that this construction works as ﬁne as in the case when U is open in S,
and Z is actually the minimal extension of ZU to a closed subscheme in S.
Lemma 2.1.2. Keep the above notation, then ZU coincides with the restriction of
Z on U .
Proof. It suﬃces to prove that ZU admits any extension to a closed subscheme
Z ֒→ S since the minimal extension then exists by local noetherianity of S. An
arbitrary extension was constructed in [Tem1, 2.1.1] as follows: ﬁrst one uses [EGA,
IV4 , 8.6.3] to extend ZU to a closed subscheme ZV of a suﬃciently small open
neighborhood V of U , and then one extends ZV to S using [EGA I, 6.9.7].          
2.1.6. Schematical density. Assume that S is a scheme with a pro-open subset U .
We say that U is schematically dense in S if for any proper closed subscheme S ′ ֒→ S
there exists u ∈ U such that S ′ ×S Su is a proper subscheme of Su = Spec(OS,u )
(possibly empty). In particular, if U is a pro-open subscheme then this condition
agrees with the usual deﬁnition that the schematic image V of the embedding
U ֒→ S coincides with S. Indeed, V is the minimal closed subscheme of S whose
restriction onto each Su with u ∈ U coincides with Su . So, V = S if and only if any
proper closed subscheme S ′ ֒→ S restricts to a proper closed subscheme of some Su
with u ∈ U .
2.1.7. U -admissibility. An S-scheme X is called U -admissible if the preimage of U
in X is schematically dense. This follows the terminology of [RG] and we will not
use the notion ”admissible” in other meanings.
2.1.8. Regular morphisms. Following [EGA, IV2 , 6.8.1] we call a morphism of
schemes f : Y → X regular if it is ﬂat and has geometrically regular ﬁbers (in
particular, the ﬁbers are locally noetherian). For morphisms of ﬁnite type regular-
ity is equivalent to smoothness, so it can be viewed as a generalization of smoothness
to morphisms not necessarily of ﬁnite type. A homomorphism of rings f : A → B
is regular if Spec(f ) is regular.
8                                 MICHAEL TEMKIN


Remark 2.1.3. (i) We remark that Hironaka uses the notion of universally regular
morphisms instead of regular morphisms reserving the notion of regularity to what
we call reg morphisms below. However, our deﬁnition of regularity is the standard
one.
  (ii) Let us temporarily say that a morphism f : Y → X is reg if it is ﬂat and
has regular ﬁbers. Then a morphism is regular in our sense if and only if it is
universally reg.
  (iii) It seems that reg morphisms are not worth a study (and a special name).
For example, one can easily construct an example of a ﬂat family of integral curves
over A1Fp such that the general ﬁber is regular but all closed ﬁbers are singular.
2.1.9. Singular locus. We deﬁne the regular locus Xreg of a scheme X as a set
of points at which X is regular, and the singular locus Xsing is deﬁned as the
complement of Xreg .
2.1.10. Compatibility with regular morphisms. It is well known that regular/singular
locus is compatible with regular morphisms, i.e. for a regular morphisms f : Y → X
we have that Ysing = f −1 (Xsing ) and Yreg = f −1 (Xreg ). See, for example, [Mat,
Th. 51].
2.1.11. Singular locus of a morphism. By the singular locus gsing of a morphism
g : Y → X we mean the set of points y ∈ Y at which g is not regular (i.e.
gy : Spec(OY,y ) → Spec(OX,g(y) ) is not regular).
Lemma 2.1.4. (i) If f : Z → Y and g : Y → X are morphisms of schemes and f
is regular, then (g ◦ f )sing = f −1 (gsing ).
   (ii) If g : A → B and f : B → C are local homomorphisms between local rings
and f is regular, then g is regular if and only if f ◦ g is regular.
Proof. Obviously, (ii) is a particular case of (i). On the other hand, the claim
that z ∈ (g ◦ f )sing if and only if z ∈ f −1 (gsing ) reduces to checking (ii) for the
local homomorphisms gy : OX,x → OY,y and fz : OY,y → OZ,z , where y = f (z) and
x = g(y). Since fz is faithfully ﬂat, gy is ﬂat if and only if fz ◦ gy is ﬂat. The
homomorphism fz ⊗OX,x k(x) : OY,y /mx OY,y → OZ,z /mx OZ,z is the base change
of fz , hence it is regular, and by §2.1.10 we obtain that OY,y /mx OY,y is regular if
and only if OZ,z /mx OZ,z is regular. This concludes the proof.                      
2.1.12. Quasi-excellent schemes. For shortness, we will abbreviate the word quasi-
excellent as qe. Since qe schemes are deﬁned by two conditions which are of an
interest of their own, we introduce the corresponding classes of schemes. We say
that X is an N-scheme if it is locally noetherian and for any Y of ﬁnite type over
X the regular locus Yreg is open. We say that X is a G-scheme if for any point
x ∈ X the completion homomorphism OX,x → O       bX,x is regular. It was proved by
Grothendieck that it suﬃces to check this only at the closed points. A scheme is
qe if it is both G and N scheme. If in addition X is universally catenary then it is
called excellent. We say that a ring is G, N, qe or excellent if its spectrum is so.
We list few basic well known properties of qe schemes.

# PRIMARY exact literal Temkin statement/proof unit

2.2.1. Blow ups. Basic facts about blow ups can be found in [Tem1, §2.1] or in
the literature cited there. Recall that the blow up f : BlV (X) → X along a closed
subscheme V is the universal morphism such that f ∗ (V ) := V ×X BlV (X) is a
Cartier divisor. We will use the terminology of [Tem1] with one important excep-
tion: when we say that Y → X is a blow up (or Y is a blow up of X), we always
mean that the center V of the blow up is ﬁxed. So, strictly speaking, we always
mean (usually implicitly) that an isomorphism Y f   →BlV (X) is ﬁxed. The reason
for this change is that we will study functoriality, and the choice of V increases
canonicity of constructions, see, for example, §2.2.6. Following the convention of
[Kol] we call a blow up Bl∅ (X)f  →X empty or trivial blow up. This is the only
blow up we will sometimes ignore. However, even empty blow ups play important
synchronizing role when patching local desingularizations, see §§2.3.4–2.3.6. Note
that though any blow up along a Cartier divisor induces an isomorphism on the
level of schemes, it may play a non-trivial role for functorial desingularization. In
our case this is mainly the synchronization (similarly to empty blow up), but in the
embedded case such blow ups induce non-trivial operations of strict and controlled
transforms, so they cannot be ignored by no means.

2.2.2. Blow up sequences. A price one has to pay for using a ﬁner notion of blow ups
is that the composition X ′′ → X ′ → X of blow ups cannot be considered as a blow
up in a natural way: though X ′′ → X is isomorphic to a blow up BlW (X) → X, it
is not clear how to choose W canonically. Therefore we deﬁne a blow up sequence
                                                          fn      f2     f1
of length n to be a composition of n ≥ 0 blow ups Xn → · · · → X1 → X0 with
centers Vi ֒→ Xi . In particular, a blow up sequence of length 0 is just the object
X0 itself. Such sequence is called empty. It will be convenient to denote a blow up
sequence as f : Xn 99K X0 and say that Vi ’s are its centers. We stress that a blow
up sequence is not deﬁned by the morphism Xn → X even when we blow up regular
schemes along regular centers, see [Kol, 3.33]. A sequence will be called contracted
if all its blow ups are non-empty. Using dashed arrows we will sometimes split blow
up sequences, e.g. f : Xn 99K Xi+1 → Xi 99K X0 .

2.2.3. Equality/isomorphism of blow up sequences. An isomorphism between two
blow up sequences Xn′ 99K X0 and Xn 99K X0 is a set of isomorphisms Xi′ f      →Xi
which identify X0 ’s and the centers. Obviously, if two blow up sequences of X are
isomorphic then the isomorphism is unique. For this reason, we will often say by
slight abuse of language that two such blow up sequences are equal, and this cannot
cause any confusion. For example, this agreement allows us to say ”unique” in
Lemma 2.2.1 below instead of ”unique up to unique isomorphism”.
                                                                   ′
2.2.4. Trivial extension. We say that a blow up sequence f : X → X is a trivial
extension of a blow up sequence f : X ′ → X if f is obtained from f by removing
few empty blow ups (here we invoke our agreement about equality of blow up
sequences).

2.2.5. Flat base changes. Any blow up sequence f : Xn 99K X0 is compatible with
any ﬂat base change g : Y0 → X0 in the sense that Y1 := Y0 ×X0 X1 is a ﬂat X1 -
scheme isomorphic to the blow up of Y0 along Y0 ×X0 V0 , and similarly for all further
blow ups in the sequence. Naturally, the induced blow up sequence Yn 99K Y0 will
be called the pullback of f with respect to g and will be denoted as g ∗ (f ).
       FUNCTORIAL DESINGULARIZATION OVER Q: THE NON-EMBEDDED CASE                    11


2.2.6. Pushing forward with respect to pro-open immersions. One advantage of hav-
ing the center V of a blow up fU : U ′ → U ﬁxed is that for any pro-open immersion
U ֒→ X with a locally noetherian X we can canonically extend fU to a blow up
f : X ′ → X. We simply take the schematical closure of V in X to be the center of
f . Note that fU = f ×X U by Lemma 2.1.2 and §2.2.5, in particular, f extends fU .
Iterating the same construction we obtain the following easy result.

Lemma 2.2.1. Assume that fU : U ′ 99K U is a blow up sequence and i : U ֒→ X
is a pro-open immersion with a locally noetherian X. Then there exists a unique
blow up sequence f : X ′ 99K X such that fU = f ×X U and the centers of fU are
schematically dense in the centers of f .
  The blow up sequence f will be called the pushforward of fU with respect to the
pro-open immersion i.

2.2.7. T -supported blow up sequences. Assume that X is an S-scheme, U ֒→ S is an
open subscheme, T = S \ U and V = X ×S U . Then we say that a blow up sequence
X ′ 99K X is T -supported if its centers lie over T . In order to avoid any confusion
with V -admissibility of the centers, we will not say that f is ”V -admissible” in this
situation (as opposed to [RG] and [Tem1]). Actually, we will often be interested
in the following two extreme cases: (a) the centers of f are V -admissible, and (b)
the centers of f are T -supported. Note that (a) takes place if and only if f is the
pushforward of its restriction f ×X V with respect to i : V ֒→ X, and (b) takes
place if and only if f ×X V is a sequence of empty blow ups.

2.2.8. Strict transform. The following deﬁnitions and facts about blow up sequences
follow from the well known particular case of usual blow ups (i.e. the sequences of
length one), which can be found in [Con, §1]. Given a closed subscheme Z0 ֒→ X0 we
deﬁne the strict transform Zn = f ! (Z0 ) of Z0 under f : Xn 99K X0 as the iterative
strict transform of Z0 with respect to fi ’s. Note that Zn 99K Z0 is the blow up
sequence whose centers are the scheme-theoretic preimages of the centers Vi of f .
More concretely, f induces a blow up sequence Zn 99K Z0 , where Zi = fi! (Zi−1 ) is
isomorphic to the blow up of Zi−1 along Vi−1 ×Xi−1 Zi−1 .

2.3. Desingularization.

2.3.1. Desingularization of schemes. By desingularization of a scheme X we mean
an Xsing -supported contracted blow up sequence f : X ′ 99K X with regular X ′ .
We will see in §2.3.3 why it is convenient to forbid empty blow ups. Note also
that although the deﬁnition makes sense for any locally noetherian scheme X, we

# PRIMARY exact literal Temkin statement/proof unit


1.1.3. Applications. Currently, it seems that the most applicable case of desingu-
larization of general qe schemes over Q is when the schemes are of ﬁnite type over
a ring k[[t1 , . . . , tn ]] with k a ﬁeld. For example, this case (in its non-functorial ver-
sion from [Tem1]) was used for studying log-canonical thresholds in [FEM], motivic
integration in [Nic], and desingularization of meromorphic connections in [Ked].
The non-functorial method of [Tem1] could only desingularize aﬃne qe formal
schemes, and in my communication with Mustata, Nicaise, Kedlaya and Soibel-
man I was urged to strengthen the method so that it may desingularize arbitrary
formal schemes of ﬁnite type over k[[t1 , . . . , tn ]]. This served as the main motivation
to continue the research on desingularization of qe schemes and I am very grateful
to them all for the encouragement. I would expect that desingularization of formal
schemes of ﬁnite type over k[[t1 , . . . , tn ]] should be the most applicable particular
case of the main results of this paper. Also, desingularization of Berkovich analytic
spaces of characteristic zero seems to be new (at least, in the non-good case).

1.2. Main result.

1.2.1. Strong non-embedded desingularization. We refer to §§2.1,2.2 for the termi-
nology, which includes the notions of quasi-excellent schemes, regular loci and mor-
phisms, and blow up sequences. Here is the strong non-embedded desingularization
theorem for generically reduced noetherian quasi-excellent schemes in characteristic
zero. In this paper ”strong” means that the desingularization blows up only regular
       FUNCTORIAL DESINGULARIZATION OVER Q: THE NON-EMBEDDED CASE                      3


subschemes, unlike the terminology of Bierstone-Milman, where one also requires
that each center lies in the maximum locus of the HS function.

Theorem 1.2.1. For any noetherian quasi-excellent generically reduced scheme
X = X0 over Spec(Q) there exists a blow up sequence F (X) : Xn 99K X0 such that
the following conditions are satisfied:
   (i) the centers of the blow ups are disjoint from the preimages of the regular locus
Xreg ;
   (ii) the centers of the blow ups are regular;
   (iii) Xn is regular;
   (iv) the blow up sequence F (X) is functorial with respect to all regular morphisms
X ′ → X, in the sense that F (X ′ ) is obtained from F (X) ×X X ′ by omitting all
empty blow ups.

1.2.2. On the non-reduced case.

Remark 1.2.2. (i) Theorem 1.2.1 implies that the same claim holds for all noe-
therian qe schemes over Q. Indeed, given an arbitrary such X with reduction X           e
we can consider the blow up sequence i∗ F (X)       e : X 99K X which is the pushfor-
                                                          ′

ward of F (X)    e :Xe ′ 99K X e with respect to the closed immersion i : X   e ֒→ X (see
                                      ′    e ′
§4.2.1). Then the reduction of X is X , so it is regular. Next we kill all generically
non-reduced components by blowing them up along their reductions, obtaining a
blow up X ′′ → X ′ with generically reduced X ′′ . Finally, it remains to apply
F (X ′′ ) : X ′′′ 99K X ′′ to construct a functorial desingularization X ′′′ 99K X.
   (ii) We ignore on purpose the case when X is not reduced along an irreducible
component because in this case the assertion of the theorem is not the ”right”
version of desingularization: such naive desingularization simply destroys all gener-
ically non-reduced components. In addition, existence of naive desingularization of
non-reduced schemes does not assert anything new, as we saw in (i).
   (iii) The correct way to desingularize non-reduced schemes is to make them
normally ﬂat along the reduction. Loosely speaking, such desingularization does
not kill non-reduced components, but makes their nilpotent structure ”as smooth
as possible”. The only known way to achieve such desingularization is to use an
algorithm such that each its center Vi lies in the maximum HS locus of Xi (or, at
least, Xi is normally ﬂat along Vi ), and to stop the algorithm just before it blows
up the non-reduced components. Our algorithm does not possess this property (see

# PRIMARY live Stacks statement/proof observations with rendered coordinates

{
  "content": [
    {
      "type": "text",
      "text": "Section 30.18 (02O2): Chow's Lemma—The Stacks project (https://stacks.math.columbia.edu/tag/02O2)\n【turn893160view0】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/02O2\",\"lineno\":null}); Total lines: 87\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†30】: Cohomology of Schemes\nL10:   * Section 【7†30.18】: Chow's Lemma (【8†cite】)\nL11: \nL12: [Input]\nL13: \nL14:   * 【9†previous section】\nL15:   * 【10†next section】\nL16: ## 30.18 Chow's Lemma\nL17: \nL18: In this section we prove Chow's lemma in the Noetherian case (Lemma 【11†30.18.1】). In Limits, Section 【12†32.12】 we prove some variants for the non-Noetherian case.\nL19: \nL20: reference\nL21: \nL22: 【11†Lemma 30.18.1.】 Let $S$ be a Noetherian scheme. Let $f : X \\to S$ be a separated morphism of finite type. Then there exist an $n \\geq 0$ and a diagram\nL23: \nL24: \\[ \\xymatrix{ X \\ar[rd] & X' \\ar[d] \\ar[l]^\\pi \\ar[r] & \\mathbf{P}^ n_ S \\ar[dl] \\\\ & S & } \\]\nL25: where $X' \\to \\mathbf{P}^ n_ S$ is an immersion, and $\\pi : X' \\to X$ is proper and surjective. Moreover, we may arrange it such that there exists a dense open subscheme $U \\subset X$ such that $\\pi ^{-1}(U) \\to U$ is an isomorphism.\nL26: Proof. All of the schemes we will encounter during the rest of the proof are going to be of finite type over the Noetherian scheme $S$ and hence Noetherian (see Morphisms, Lemma 【13†29.15.6】). All morphisms between them will automatically be quasi-compact, locally of finite type and quasi-separated, see Morphisms, Lemma 【14†29.15.8】 and Properties, Lemmas 【15†28.5.4】 and 【16†28.5.8】.\nL27: The scheme $X$ has only finitely many irreducible components (Properties, Lemma 【17†28.5.7】). Say $X = X_1 \\cup \\ldots \\cup X_ r$ is the decomposition of $X$ into irreducible components. Let $\\eta _ i \\in X_ i$ be the generic point. For every point $x \\in X$ there exists an affine open $U_ x \\subset X$ which contains $x$ and each of the generic points $\\eta _ i$. See Properties, Lemma 【18†28.30.4】.\nL28: Since $X$ is quasi-compact, we can find a finite affine open covering $X = U_1 \\cup \\ldots \\cup U_ m$ such that each $U_ i$ contains $\\eta _1, \\ldots , \\eta _ r$. In particular we conclude that the open $U = U_1 \\cap \\ldots \\cap U_ m \\subset X$ is a dense open. This and the fact that the $U_ i$ are affine opens covering $X$ are all that we will use below.\nL29: Let $X^* \\subset X$ be the scheme theoretic closure of $U \\to X$, see Morphisms, Definition 【19†29.6.2】. Let $U_ i^* = X^* \\cap U_ i$. Note that $U_ i^*$ is a closed subscheme of $U_ i$. Hence $U_ i^*$ is affine. Since $U$ is dense in $X$ the morphism $X^* \\to X$ is a surjective closed immersion. It is an isomorphism over $U$. Hence we may replace $X$ by $X^*$ and $U_ i$ by $U_ i^*$ and assume that $U$ is scheme theoretically dense in $X$, see Morphisms, Definition 【20†29.7.1】.\nL30: By Morphisms, Lemma 【21†29.40.3】 we can find an immersion $j_ i : U_ i \\to \\mathbf{P}_ S^{n_ i}$ for each $i$. By Morphisms, Lemma 【22†29.7.7】 we can find closed subschemes $Z_ i \\subset \\mathbf{P}_ S^{n_ i}$ such that $j_ i : U_ i \\to Z_ i$ is a scheme theoretically dense open immersion. Note that $Z_ i \\to S$ is proper, see Morphisms, Lemma 【23†29.44.5】. Consider the morphism\nL31: \\[ j = (j_1|_ U, \\ldots , j_ m|_ U) : U \\longrightarrow \\mathbf{P}_ S^{n_1} \\times _ S \\ldots \\times _ S \\mathbf{P}_ S^{n_ m}. \\]\nL32: \nL33: By the lemma cited above we can find a closed subscheme $Z$ of $\\mathbf{P}_ S^{n_1} \\times _ S \\ldots \\times _ S \\mathbf{P}_ S^{n_ m}$ such that $j : U \\to Z$ is an open immersion and such that $U$ is scheme theoretically dense in $Z$. The morphism $Z \\to S$ is proper. Consider the $i$th projection\nL34: \nL35: \\[ \\text{pr}_ i|_ Z : Z \\longrightarrow \\mathbf{P}^{n_ i}_ S. \\]\nL36: This morphism factors through $Z_ i$ (see Morphisms, Lemma 【24†29.6.6】). Denote $p_ i : Z \\to Z_ i$ the induced morphism. This is a proper morphism, see Morphisms, Lemma 【25†29.42.7】 for example. At this point we have that $U \\subset U_ i \\subset Z_ i$ are scheme theoretically dense open immersions. Moreover, we can think of $Z$ as the scheme theoretic image of the “diagonal” morphism $U \\to Z_1 \\times _ S \\ldots \\times _ S Z_ m$.\nL37: Set $V_ i = p_ i^{-1}(U_ i)$. Note that $p_ i|_{V_ i} : V_ i \\to U_ i$ is proper. Set $X' = V_1 \\cup \\ldots \\cup V_ m$. By construction $X'$ has an immersion into the scheme $\\mathbf{P}^{n_1}_ S \\times _ S \\ldots \\times _ S \\mathbf{P}^{n_ m}_ S$. Thus by the Segre embedding (see Constructions, Lemma 【26†27.13.6】) we see that $X'$ has an immersion into a projective space over $S$.\nL38: We claim that the morphisms $p_ i|_{V_ i}: V_ i \\to U_ i$ glue to a morphism $X' \\to X$. Namely, it is clear that $p_ i|_ U$ is the identity map from $U$ to $U$. Since $U \\subset X'$ is scheme theoretically dense by construction, it is also scheme theoretically dense in the open subscheme $V_ i \\cap V_ j$. Thus we see that $p_ i|_{V_ i \\cap V_ j} = p_ j|_{V_ i \\cap V_ j}$ as morphisms into the separated $S$-scheme $X$, see Morphisms, Lemma 【27†29.7.10】. We denote the resulting morphism $\\pi : X' \\to X$.\nL39: We claim that $\\pi ^{-1}(U_ i) = V_ i$. Since $\\pi |_{V_ i} = p_ i|_{V_ i}$ it follows that $V_ i \\subset \\pi ^{-1}(U_ i)$. Consider the diagram\nL40: \nL41: \\[ \\xymatrix{ V_ i \\ar[r] \\ar[rd]_{p_ i|_{V_ i}} & \\pi ^{-1}(U_ i) \\ar[d] \\\\ & U_ i } \\]\nL42: \nL43: Since $V_ i \\to U_ i$ is proper we see that the image of the horizontal arrow is closed, see Morphisms, Lemma 【25†29.42.7】. Since $V_ i \\subset \\pi ^{-1}(U_ i)$ is scheme theoretically dense (as it contains $U$) we conclude that $V_ i = \\pi ^{-1}(U_ i)$ as claimed.\nL44: This shows that $\\pi ^{-1}(U_ i) \\to U_ i$ is identified with the proper morphism $p_ i|_{V_ i} : V_ i \\to U_ i$. Hence we see that $X$ has a finite affine covering $X = \\bigcup U_ i$ such that the restriction of $\\pi $ is proper on each member of the covering. Thus by Morphisms, Lemma 【28†29.42.3】 we see that $\\pi $ is proper.\nL45: \nL46: Finally we have to show that $\\pi ^{-1}(U) = U$. To see this we argue in the same way as above using the diagram\nL47: \nL48: \\[ \\xymatrix{ U \\ar[r] \\ar[rd] & \\pi ^{-1}(U) \\ar[d] \\\\ & U } \\]\nL49: and using that $\\text{id}_ U : U \\to U$ is proper and that $U$ is scheme theoretically dense in $\\pi ^{-1}(U)$. $\\square$\nL50: \nL51: 【29†Remark 30.18.2.】 In the situation of Chow's Lemma 【11†30.18.1】:\nL52: \nL53:   1. The morphism $\\pi $ is actually H-projective (hence projective, see Morphisms, Lemma 【30†29.44.3】) since the morphism $X' \\to \\mathbf{P}^ n_ S \\times _ S X = \\mathbf{P}^ n_ X$ is a closed immersion (use the fact that $\\pi $ is proper, see Morphisms, Lemma 【25†29.42.7】).\nL54:   2. We may assume that $\\pi ^{-1}(U)$ is scheme theoretically dense in $X'$. Namely, we can simply replace $X'$ by the scheme theoretic closure of $\\pi ^{-1}(U)$. In this case we can think of $U$ as a scheme theoretically dense open subscheme of $X'$. See Morphisms, Section 【31†29.6】.\nL55: \nL56:   3. If $X$ is reduced then we may choose $X'$ reduced. This is clear from (2).\nL57: \nL58: * * *\nL59: ## Comments (0)\nL60: \nL61: * * *\nL62: ## Post a comment\nL63: \nL64: Your email address will not be published. Required fields are marked.\nL65: \nL66: In your comment you can use 【32†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL67: \nL68: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL69: \nL70: All contributions are licensed under the 【33†GNU Free Documentation License†github.com】.\nL71: Name^{*}: [Input]\nL72: E-mail^{*}: [Input]\nL73: Site: [Input]\nL74: Comment:\nL75: \nL76: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 02O2. Beware of the difference between the letter 'O' and the digit '0'.\nL77: \nL78: Tag: [Input] [Button: Post comment] [Input]\nL79: \nL80: The tag you filled in for the captcha is wrong. You need to write 02O2, in case you are confused.\nL81:   * 【9†previous section】\nL82:   * 【10†next section】\nL83: \nL84: * * *\nL85: \nL86: 【34†View Section 30.18 as pdf】\n\n--------------------------------------------------------------------------------\n[0904.1592] Functorial desingularization of quasi-excellent schemes in characteristic zero: the non-embedded case (https://arxiv.org/abs/0904.1592)\n【turn893160view1】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://arxiv.org/abs/0904.1592\",\"lineno\":null}); Total lines: 162\nL0: 【0†Search】 【1†Submit】 【2†Donate†info.arxiv.org】 【3†Log in】\nL1: \nL2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]\nL3: \nL4: Press Enter to search · 【4†Advanced search】\nL5: \nL6: # Mathematics > Algebraic Geometry\nL7: \nL8: [Submitted on 9 Apr 2009 (【5†v1】), last revised 11 Dec 2011 (this version, v2)]\nL9: # Title:Functorial desingularization of quasi-excellent schemes in characteristic zero: the non-embedded case\nL10: \nL11: Authors:【6†Michael Temkin】\nL12: \nL13: View a PDF of the paper titled Functorial desingularization of quasi-excellent schemes in characteristic zero: the non-embedded case, by Michael Temkin\nL14: \nL15: 【7†View PDF】 【8†HTML (experimental)】\nL16: > Abstract:We prove that any noetherian quasi-excellent scheme of characteristic zero admits a strong desingularization which is functorial with respect to all regular morphisms. We show that as an easy formal consequence of this result one obtains strong functorial desingularization for many other spaces of characteristic zero including quasi-excellent stacks and formal schemes, and complex and non-archimedean analytic spaces.\nL17: Moreover, these functors easily generalize to non-compact setting by use of converging blow up hyper-sequences with regular centers.\nL18: Comments:  | 35 pages, final version, section 3.2 in the first version was seriously modified\nL19: Subjects:  | Algebraic Geometry (math.AG)\nL20: Cite as:  | 【9†arXiv:0904.1592】 [math.AG]\nL21:    | (or 【10†arXiv:0904.1592v2】 [math.AG] for this version)\nL22:    | 【11†https://doi.org/10.48550/arXiv.0904.1592†doi.org】 arXiv-issued DOI via DataCite\nL23: Journal reference:  | Duke Math. J. 161, no. 11 (2012), 2207-2254\nL24: Related DOI (Digital Object Identifier):  | 【12†https://doi.org/10.1215/00127094-1699539†doi.org】 DOI(s) linking to related resources\nL25: ## Submission history\nL26: \nL27: From: Michael Temkin [【13†view email】]\nL28: 【5†[v1]】 Thu, 9 Apr 2009 19:39:03 UTC (41 KB)\nL29: [v2] Sun, 11 Dec 2011 12:35:10 UTC (47 KB)\nL30: \nL31: Full-text links:\nL32: \nL33: ## Access Paper:\nL34: \nL35: View a PDF of the paper titled Functorial desingularization of quasi-excellent schemes in characteristic zero: the non-embedded case, by Michael Temkin\nL36: \nL37:   * 【7†View PDF】\nL38:   * 【8†HTML (experimental)】\nL39:   * 【14†TeX Source】\nL40: \nL41: 【15†view license】\nL42: ### Current browse context:\nL43: \nL44: math.AG\nL45: \nL46: 【16†< prev】   |   【17†next >】\nL47: \nL48: 【18†new】 | 【19†recent】 | 【20†2009-04】\nL49: \nL50: Change to browse by:\nL51: \nL52: 【21†math】\nL53: \nL54: ### References & Citations\nL55: \nL56:   * 【22†NASA ADS†ui.adsabs.harvard.edu】\nL57:   * 【23†Google Scholar†scholar.google.com】\nL58:   * 【24†Semantic Scholar†api.semanticscholar.org】\nL59: \nL60: [Button: export BibTeX citation] Loading...\nL61: \nL62: ## BibTeX formatted citation\nL63: \nL64: [Button: ×]\nL65: \nL66: loading...\nL67: \nL68: Data provided by:\nL69: \nL70: ### Bookmark\nL71: \nL72: [Input] Bibliographic Tools\nL73: # Bibliographic and Citation Tools\nL74: \nL75: [Input] Bibliographic Explorer Toggle\nL76: \nL77: Bibliographic Explorer (【25†What is the Explorer?†info.arxiv.org】)\nL78: \nL79: [Input] Connected Papers Toggle\nL80: \nL81: Connected Papers (【26†What is Connected Papers?†www.connectedpapers.com】)\nL82: \nL83: [Input] Litmaps Toggle\nL84: \nL85: Litmaps (【27†What is Litmaps?†www.litmaps.co】)\nL86: \nL87: [Input] scite.ai Toggle\nL88: \nL89: scite Smart Citations (【28†What are Smart Citations?†www.scite.ai】)\nL90: \nL91: [Input] Code, Data, Media\nL92: # Code, Data and Media Associated with this Article\nL93: \nL94: [Input] alphaXiv Toggle\nL95: \nL96: alphaXiv (【29†What is alphaXiv?†alphaxiv.org】)\nL97: \nL98: [Input] Links to Code Toggle\nL99: \nL100: CatalyzeX Code Finder for Papers (【30†What is CatalyzeX?†www.catalyzex.com】)\nL101: \nL102: [Input] DagsHub Toggle\nL103: \nL104: DagsHub (【31†What is DagsHub?†dagshub.com】)\nL105: \nL106: [Input] GotitPub Toggle\nL107: \nL108: Gotit.pub (【32†What is GotitPub?†gotit.pub】)\nL109: \nL110: [Input] Huggingface Toggle\nL111: \nL112: Hugging Face (【33†What is Huggingface?†huggingface.co】)\nL113: \nL114: [Input] ScienceCast Toggle\nL115: ScienceCast (【34†What is ScienceCast?†sciencecast.org】)\nL116: \nL117: [Input] Demos\nL118: # Demos\nL119: \nL120: [Input] Replicate Toggle\nL121: \nL122: Replicate (【35†What is Replicate?†replicate.com】)\nL123: \nL124: [Input] Spaces Toggle\nL125: \nL126: Hugging Face Spaces (【36†What is Spaces?†huggingface.co】)\nL127: \nL128: [Input] Spaces Toggle\nL129: \nL130: TXYZ.AI (【37†What is TXYZ.AI?†txyz.ai】)\nL131: \nL132: [Input] Related Papers\nL133: # Recommenders and Search Tools\nL134: \nL135: [Input] Link to Influence Flower\nL136: \nL137: Influence Flower (【38†What are Influence Flowers?†influencemap.cmlab.dev】)\nL138: \nL139: [Input] Core recommender toggle\nL140: \nL141: CORE Recommender (【39†What is CORE?†core.ac.uk】)\nL142: \nL143:   * Author\nL144:   * Venue\nL145:   * Institution\nL146:   * Topic\nL147: \nL148: [Input] About arXivLabs\nL149: # arXivLabs: experimental projects with community collaborators\nL150: \nL151: arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.\nL152: \nL153: Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.\nL154: Have an idea for a project that will add value for arXiv's community? 【40†Learn more about arXivLabs†info.arxiv.org】.\nL155: \nL156: 【41†Which authors of this paper are endorsers?】 | Disable MathJax (【42†What is MathJax?†info.arxiv.org】)\nL157: \nL158: We gratefully acknowledge support from our major funders, 【43†member institutions†info.arxiv.org】, , and all contributors.\nL159: 【44†About†info.arxiv.org】 · 【45†Help†info.arxiv.org】 · 【46†Contact†info.arxiv.org】 · 【47†Subscribe†info.arxiv.org】 · 【48†Copyright†info.arxiv.org】 · 【49†Privacy†info.arxiv.org】 · 【50†Accessibility†info.arxiv.org】 · 【51†Operational Status (opens in new tab)†status.arxiv.org】\nL160: \nL161: Major funding support from\n\n--------------------------------------------------------------------------------\nSection 31.33 (01OF): Blowing up—The Stacks project (https://stacks.math.columbia.edu/tag/01OF)\n【turn893160view2】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/01OF\",\"lineno\":null}); Total lines: 177\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†31】: Divisors\nL10:   * Section 【7†31.33】: Blowing up (【8†cite】)\nL11: \nL12: [Input]\nL13: \nL14:   * 【9†previous section】\nL15:   * 【10†next section】\nL16: ## 31.33 Blowing up\nL17: \nL18: Blowing up is an important tool in algebraic geometry.\nL19: \nL20: 【11†Definition 31.33.1.】 Let $X$ be a scheme. Let $\\mathcal{I} \\subset \\mathcal{O}_ X$ be a quasi-coherent sheaf of ideals, and let $Z \\subset X$ be the closed subscheme corresponding to $\\mathcal{I}$, see Schemes, Definition 【12†26.10.2】. The blowing up of $X$ along $Z$, or the blowing up of $X$ in the ideal sheaf $\\mathcal{I}$ is the morphism\nL21: \\[ b : \\underline{\\text{Proj}}_ X \\left(\\bigoplus \\nolimits _{n \\geq 0} \\mathcal{I}^ n\\right) \\longrightarrow X \\]\nL22: \nL23: The exceptional divisor of the blowup is the inverse image $b^{-1}(Z)$. Sometimes $Z$ is called the center of the blowup.\nL24: \nL25: We will see later that the exceptional divisor is an effective Cartier divisor. Moreover, the blowing up is characterized as the “smallest” scheme over $X$ such that the inverse image of $Z$ is an effective Cartier divisor.\nL26: If $b : X' \\to X$ is the blowup of $X$ in $Z$, then we often denote $\\mathcal{O}_{X'}(n)$ the twists of the structure sheaf. Note that these are invertible $\\mathcal{O}_{X'}$-modules and that $\\mathcal{O}_{X'}(n) = \\mathcal{O}_{X'}(1)^{\\otimes n}$ because $X'$ is the relative Proj of a quasi-coherent graded $\\mathcal{O}_ X$-algebra which is generated in degree $1$, see Constructions, Lemma 【13†27.16.11】.\nL27: Note that $\\mathcal{O}_{X'}(1)$ is $b$-relatively very ample, even though $b$ need not be of finite type or even quasi-compact, because $X'$ comes equipped with a closed immersion into $\\mathbf{P}(\\mathcal{I})$, see Morphisms, Example 【14†29.39.3】.\nL28: 【15†Lemma 31.33.2.】 Let $X$ be a scheme. Let $\\mathcal{I} \\subset \\mathcal{O}_ X$ be a quasi-coherent sheaf of ideals. Let $U = \\mathop{\\mathrm{Spec}}(A)$ be an affine open subscheme of $X$ and let $I \\subset A$ be the ideal corresponding to $\\mathcal{I}|_ U$. If $b : X' \\to X$ is the blowup of $X$ in $\\mathcal{I}$, then there is a canonical isomorphism\nL29: \nL30: \\[ b^{-1}(U) = \\text{Proj}(\\bigoplus \\nolimits _{d \\geq 0} I^ d) \\]\nL31: of $b^{-1}(U)$ with the homogeneous spectrum of the Rees algebra of $I$ in $A$. Moreover, $b^{-1}(U)$ has an affine open covering by spectra of the affine blowup algebras $A[\\frac{I}{a}]$.\nL32: Proof. The first statement is clear from the construction of the relative Proj via glueing, see Constructions, Section 【16†27.15】. For $a \\in I$ denote $a^{(1)}$ the element $a$ seen as an element of degree $1$ in the Rees algebra $\\bigoplus _{n \\geq 0} I^ n$. Since these elements generate the Rees algebra over $A$ we see that $\\text{Proj}(\\bigoplus _{d \\geq 0} I^ d)$ is covered by the affine opens $D_{+}(a^{(1)})$.\nL33: The affine scheme $D_{+}(a^{(1)})$ is the spectrum of the affine blowup algebra $A' = A[\\frac{I}{a}]$, see Algebra, Definition 【17†10.70.1】. This finishes the proof. $\\square$\nL34: slogan\nL35: \nL36: 【18†Lemma 31.33.3.】 Let $X_1 \\to X_2$ be a flat morphism of schemes. Let $Z_2 \\subset X_2$ be a closed subscheme. Let $Z_1$ be the inverse image of $Z_2$ in $X_1$. Let $X'_ i$ be the blowup of $Z_ i$ in $X_ i$. Then there exists a cartesian diagram\nL37: \nL38: \\[ \\xymatrix{ X_1' \\ar[r] \\ar[d] & X_2' \\ar[d] \\\\ X_1 \\ar[r] & X_2 } \\]\nL39: \nL40: of schemes.\nL41: Proof. Let $\\mathcal{I}_2$ be the ideal sheaf of $Z_2$ in $X_2$. Denote $g : X_1 \\to X_2$ the given morphism. Then the ideal sheaf $\\mathcal{I}_1$ of $Z_1$ is the image of $g^*\\mathcal{I}_2 \\to \\mathcal{O}_{X_1}$ (by definition of the inverse image, see Schemes, Definition 【19†26.17.7】). By Constructions, Lemma 【20†27.16.10】 we see that $X_1 \\times _{X_2} X_2'$ is the relative Proj of $\\bigoplus _{n \\geq 0} g^*\\mathcal{I}_2^ n$.\nL42: Because $g$ is flat the map $g^*\\mathcal{I}_2^ n \\to \\mathcal{O}_{X_1}$ is injective with image $\\mathcal{I}_1^ n$. Thus we see that $X_1 \\times _{X_2} X_2' = X_1'$. $\\square$\nL43: 【21†Lemma 31.33.4.】 Let $X$ be a scheme. Let $Z \\subset X$ be a closed subscheme. The blowing up $b : X' \\to X$ of $Z$ in $X$ has the following properties:\nL44: \nL45:   1. $b|_{b^{-1}(X \\setminus Z)} : b^{-1}(X \\setminus Z) \\to X \\setminus Z$ is an isomorphism,\nL46: \nL47:   2. the exceptional divisor $E = b^{-1}(Z)$ is an effective Cartier divisor on $X'$,\nL48: \nL49:   3. there is a canonical isomorphism $\\mathcal{O}_{X'}(-1) = \\mathcal{O}_{X'}(E)$\nL50: Proof. As blowing up commutes with restrictions to open subschemes (Lemma 【18†31.33.3】) the first statement just means that $X' = X$ if $Z = \\emptyset $. In this case we are blowing up in the ideal sheaf $\\mathcal{I} = \\mathcal{O}_ X$ and the result follows from Constructions, Example 【22†27.8.14】.\nL51: The second statement is local on $X$, hence we may assume $X$ affine. Say $X = \\mathop{\\mathrm{Spec}}(A)$ and $Z = \\mathop{\\mathrm{Spec}}(A/I)$. By Lemma 【15†31.33.2】 we see that $X'$ is covered by the spectra of the affine blowup algebras $A' = A[\\frac{I}{a}]$. Then $IA' = aA'$ and $a$ maps to a nonzerodivisor in $A'$ according to Algebra, Lemma 【23†10.70.2】.\nL52: This proves the lemma as the inverse image of $Z$ in $\\mathop{\\mathrm{Spec}}(A')$ corresponds to $\\mathop{\\mathrm{Spec}}(A'/IA') \\subset \\mathop{\\mathrm{Spec}}(A')$.\nL53: Consider the canonical map $\\psi _{univ, 1} : b^*\\mathcal{I} \\to \\mathcal{O}_{X'}(1)$, see discussion following Constructions, Definition 【24†27.16.7】. We claim that this factors through an isomorphism $\\mathcal{I}_ E \\to \\mathcal{O}_{X'}(1)$ (which proves the final assertion). Namely, on the affine open corresponding to the blowup algebra $A' = A[\\frac{I}{a}]$ mentioned above $\\psi _{univ, 1}$ corresponds to the $A'$-module map\nL54: \\[ I \\otimes _ A A' \\longrightarrow \\left(\\Big(\\bigoplus \\nolimits _{d \\geq 0} I^ d\\Big)_{a^{(1)}}\\right)_1 \\]\nL55: \nL56: where $a^{(1)}$ is as in Algebra, Definition 【17†10.70.1】. We omit the verification that this is the map $I \\otimes _ A A' \\to IA' = aA'$. $\\square$\nL57: 【25†Lemma 31.33.5 (Universal property blowing up).】 Let $X$ be a scheme. Let $Z \\subset X$ be a closed subscheme. Let $\\mathcal{C}$ be the full subcategory of $(\\mathit{Sch}/X)$ consisting of $Y \\to X$ such that the inverse image of $Z$ is an effective Cartier divisor on $Y$. Then the blowing up $b : X' \\to X$ of $Z$ in $X$ is a final object of $\\mathcal{C}$.\nL58: Proof. We see that $b : X' \\to X$ is an object of $\\mathcal{C}$ according to Lemma 【21†31.33.4】. Let $f : Y \\to X$ be an object of $\\mathcal{C}$. We have to show there exists a unique morphism $Y \\to X'$ over $X$. Let $D = f^{-1}(Z)$. Let $\\mathcal{I} \\subset \\mathcal{O}_ X$ be the ideal sheaf of $Z$ and let $\\mathcal{I}_ D$ be the ideal sheaf of $D$. Then $f^*\\mathcal{I} \\to \\mathcal{I}_ D$ is a surjection to an invertible $\\mathcal{O}_ Y$-module.\nL59: This extends to a map $\\psi : \\bigoplus f^*\\mathcal{I}^ d \\to \\bigoplus \\mathcal{I}_ D^ d$ of graded $\\mathcal{O}_ Y$-algebras. (We observe that $\\mathcal{I}_ D^ d = \\mathcal{I}_ D^{\\otimes d}$ as $D$ is an effective Cartier divisor.) By the material in Constructions, Section 【26†27.16】 the triple $(1, f : Y \\to X, \\psi )$ defines a morphism $Y \\to X'$ over $X$. The restriction\nL60: \\[ Y \\setminus D \\longrightarrow X' \\setminus b^{-1}(Z) = X \\setminus Z \\]\nL61: \n"
    }
  ],
  "isError": false
}


# PRIMARY live Stacks statement/proof observations with rendered coordinates

{
  "content": [
    {
      "type": "text",
      "text": "Section 29.42 (01W0): Proper morphisms—The Stacks project (https://stacks.math.columbia.edu/tag/01W0)\n【turn381141search0】 [wordlim: 200] Crawled: today; A closed immersion is proper, hence a fortiori universally closed.\n\n--------------------------------------------------------------------------------\nSection 100.9 (04YK): Immersions of algebraic stacks—The Stacks project (https://stacks.math.columbia.edu/tag/04YK)\n【turn381141search1】 [wordlim: 200] Crawled: 4 weeks ago; If $Z \\subset U$ is open (resp. closed) then the morphism is an open (resp. closed) immersion of algebraic stacks.\n\n--------------------------------------------------------------------------------\nSection 26.10 (01IM): Immersions of schemes—The Stacks project (https://stacks.math.columbia.edu/tag/01IM)\n【turn381141search2】 [wordlim: 200] Crawled: 3 weeks ago; # The Stacks project ... A morphism of schemes $f : X \\to Y$ is called an immersion, or a locally closed immersion if it can be factored as $j \\circ i$ where $i$ is a closed immersion and $j$ is an open immersion.\n\n--------------------------------------------------------------------------------\n29.3. IMMERSIONS                                                                 2421 (https://stacks.math.columbia.edu/download/book.pdf)\n【turn381141search36】 [wordlim: 200] Published: 8 months ago; If this happens, then a is a closed immersion.\n\n--------------------------------------------------------------------------------\nSection 29.3 (07RJ): Immersions—The Stacks project (https://stacks.math.columbia.edu/tag/07RJ)\n【turn381141search3】 [wordlim: 200] Crawled: 2 weeks ago; If $y \\in Y$ and $U \\subset X$ is as in the statement of the lemma, then $U' = X' \\cap U$ is an open neighbourhood of $f'(y)$ such that $(f')^{-1}(U') \\to U'$ is an immersion (Lemma 29.3.1) with closed image.\n\n--------------------------------------------------------------------------------\nSection 71.14 (0D30): Relatively ample sheaves—The Stacks project (https://stacks.math.columbia.edu/tag/0D30)\n【turn381141search4】 [wordlim: 200] Crawled: last month; # The Stacks project ... We say $\\mathcal{L}$ is relatively ample, or $f$-relatively ample, or ample on $X/Y$, or $f$-ample if $f : X \\to Y$ is representable and for every morphism $Z \\to Y$ where $Z$ is a scheme, the pullback $\\mathcal{L}_ Z$ of $\\mathcal{L}$ to $X_ Z = Z \\times _ Y X$ is ample on $X_ Z/Z$ as in Morphisms, Definition 29.38.1.\n\n--------------------------------------------------------------------------------\nDefinition 100.9.1 (04YL)—The Stacks project (https://stacks.math.columbia.edu/tag/04YL)\n【turn381141search5】 [wordlim: 200] Crawled: 3 months ago; A morphism of algebraic stacks is called a closed immersion if it is representable, and a closed immersion in the sense of Section 100.3.\n\n--------------------------------------------------------------------------------\nSection 15.53 (07QS): Excellent rings—The Stacks project (https://stacks.math.columbia.edu/tag/07QS)\n【turn381141search6】 [wordlim: 200] Crawled: 2 weeks ago; Thus a Noetherian ring is quasi-excellent if it has geometrically regular formal fibres and if any finite type algebra over it has closed singular set. ... Let $A/\\mathfrak q \\subset B \\subset K$ be a local subring finite over $A$ whose fraction field is $K$.\n\n--------------------------------------------------------------------------------\nSection 31.22 (0638): Regular immersions—The Stacks project (https://stacks.math.columbia.edu/tag/0638)\n【turn381141search7】 [wordlim: 200] Crawled: 2 weeks ago; A Koszul-regular closed immersion is smooth locally a regular immersion, see Lemma 31.22.11.\n\n--------------------------------------------------------------------------------\nSection 76.10 (0CG4): Morphisms of thickenings—The Stacks project (https://stacks.math.columbia.edu/tag/0CG4)\n【turn381141search8】 [wordlim: 200] Crawled: last month; Follows by combining (2) with results of Lemma 76.10.1 and the fact that proper equals quasi-compact $+$ separated $+$ locally of finite type $+$ universally closed. ... If $f : X \\to Y$ is an immersion, then it factors as $X \\to V \\to Y$ where $V \\to Y$ is an open subspace and $X \\to V$ is a closed immersion, see Morphisms of Spaces, Remark 67.12.4.\n\n--------------------------------------------------------------------------------\nSection 29.20 (0HA6): Excellent schemes—The Stacks project (https://stacks.math.columbia.edu/tag/0HA6)\n【turn381141search9】 [wordlim: 200] Crawled: last week; If $S$ is (quasi-)excellent and $f$ locally of finite type then $X$ is (quasi-)excellent. ... Any scheme locally of finite type over a field.\n\n--------------------------------------------------------------------------------\nDefinition 71.14.1 (0D31)—The Stacks project (https://stacks.math.columbia.edu/tag/0D31)\n【turn381141search10】 [wordlim: 200] Crawled: last week; We say $\\mathcal{L}$ is relatively ample, or $f$-relatively ample, or ample on $X/Y$, or $f$-ample if $f : X \\to Y$ is representable and for every morphism $Z \\to Y$ where $Z$ is a scheme, the pullback $\\mathcal{L}_ Z$ of $\\mathcal{L}$ to $X_ Z = Z \\times _ Y X$ is ample on $X_ Z/Z$ as in Morphisms, Definition 29.38.1.\n\n--------------------------------------------------------------------------------\nRemark 26.10.3 (01IP)—The Stacks project (https://stacks.math.columbia.edu/tag/01IP)\n【turn381141search11】 [wordlim: 200] Crawled: 4 months ago; If $f : X \\to Y$ is an immersion of schemes, then it is in general not possible to factor $f$ as an open immersion followed by a closed immersion.\n\n--------------------------------------------------------------------------------\nSection 29.38 (01VG): Relatively ample sheaves—The Stacks project (https://stacks.math.columbia.edu/tag/01VG)\n【turn381141search12】 [wordlim: 200] Crawled: today; We note that the existence of a relatively ample sheaf on X$X$ does not force the morphism X→S$X \\to S$ to be of finite type. ... Since the restriction of an ample sheaf to a closed subscheme is ample, see Properties, Lemma 28.27.3 we conclude that the pullback of O Y(d′)$\\mathcal{O}_ Y(d')$ is ample. ... We conclude that for some a$a$ sufficiently divisible and large enough the invertible sheaf L⊗f∗M⊗a$\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ is ample on X$X$.\n\n--------------------------------------------------------------------------------\nLemma 15.53.2 (07QU)—The Stacks project (https://stacks.math.columbia.edu/tag/07QU)\n【turn381141search13】 [wordlim: 200] Crawled: last week; Any localization of a finite type ring over a (quasi-)excellent ring is (quasi-)excellent.\n\n--------------------------------------------------------------------------------\nSection 29.41 (01W0): Proper morphisms—The Stacks project (https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/01W0)\n【turn381141search14】 [wordlim: 200] Crawled: 3 weeks ago; A closed immersion is proper, hence a fortiori universally closed.\n\n--------------------------------------------------------------------------------\nSection 29.3 (07RJ): Immersions—The Stacks project (https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/07RJ)\n【turn381141search15】 [wordlim: 200] Crawled: 3 weeks ago; # The Stacks project ... If $y \\in Y$ and $U \\subset X$ is as in the statement of the lemma, then $U' = X' \\cap U$ is an open neighbourhood of $f'(y)$ such that $(f')^{-1}(U') \\to U'$ is an immersion (Lemma 29.3.1) with closed image.\n\n--------------------------------------------------------------------------------\nSection 17.13 (01C1): Closed immersions of ringed spaces—The Stacks project (https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/01C1)\n【turn381141search16】 [wordlim: 200] Crawled: last month; However, in the Stacks project we choose the definition that guarantees that if $i$ is a closed immersion and $(X, \\mathcal{O}_ X)$ is a scheme, then also $(Z, \\mathcal{O}_ Z)$ is a scheme.\n\n--------------------------------------------------------------------------------\nLemma 32.4.15 (09MT)—The Stacks project (https://stacks.math.columbia.edu/tag/09MT)\n【turn381141search17】 [wordlim: 200] Crawled: last week; If the pullback $\\mathcal{L}$ to $S$ is ample, then for some $i \\in I$ the pullback $\\mathcal{L}_ i$ to $S_ i$ is ample.\n\n--------------------------------------------------------------------------------\nLemma 26.10.4 (01IQ)—The Stacks project (https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/01IQ)\n【turn381141search18】 [wordlim: 200] Crawled: last month; # The Stacks project ... By definition there exists an open subscheme $U \\subset X$ such that $f$ is the composition of a closed immersion $i : Y \\to U$ and the open immersion $j : U \\to X$.\n\n--------------------------------------------------------------------------------\nSection 29.39 (01VL): Very ample sheaves—The Stacks project (https://stacks.math.columbia.edu/tag/01VL)\n【turn381141search19】 [wordlim: 200] Crawled: today; Since there is no assumption of quasi-compactness in this definition it is not true in general that a relatively very ample invertible sheaf is a relatively ample invertible sheaf. ... Namely, given a field k$k$ there exists a scheme X d$X_ d$ of finite type over k$k$ with an ample invertible sheaf O X d(1)$\\mathcal{O}_{X_ d}(1)$ so that the smallest tensor power of O X d(1)$\\mathcal{O}_{X_ d}(1)$ which is very ample is the d$d$th power. ...   2. there exists an open covering S=⋃V j$S = \\bigcup V_ j$ such that L|f−1(V j)$\\mathcal{L}|_{f^{-1}(V_ j)}$ is relatively very ample on f−1(V j)/V j$f^{-1}(V_ j)/V_ j$ for all j$j$, ... The base change of P(E)$\\mathbf{P}(\\mathcal{E})$ to S′$S'$ is the projective bundle associated to the pullback E′$\\mathcal{E}'$ of E$\\mathcal{E}$ and the pullback of O P(E)(1)$\\mathcal{O}_{\\mathbf{P}(\\mathcal{E})}(1)$ is O P(E′)(1)$\\mathcal{O}_{\\mathbf{P}(\\mathcal{E}')}(1)$, see Constructions, Lemma 27.16.10.\n\n--------------------------------------------------------------------------------\nAlgebraic Geometry (https://www.math.columbia.edu/~plei/docs/notes/AG.pdf)\n【turn381141search37】 [wordlim: 200] Published: 2.1 years ago; Closed immersions are proper.\n\n--------------------------------------------------------------------------------\nSection 15.52 (07QS): Excellent rings—The Stacks project (https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/07QS)\n【turn381141search20】 [wordlim: 200] Crawled: last month; # The Stacks project ... Thus a Noetherian ring is quasi-excellent if it has geometrically regular formal fibres and if any finite type algebra over it has closed singular set. ... Dedekind domains with fraction field of characteristic zero,\n\n--------------------------------------------------------------------------------\nALGEBRAIC CURVES 14 (https://stacks.math.columbia.edu/download/curves.pdf)\n【turn381141search38】 [wordlim: 200] Published: 8 months ago; The pullback of \\(\\mathcal{L}\\) to \\(X_{\\overline{k}}\\) is very ample (Morphisms, Lemma 38.8). ... 0E8U An often used criterion for very ampleness of an invertible module \\(\\mathcal{L}\\) on a scheme \\(X\\) of finite type over an algebraically closed field is: sections of \\(\\mathcal{L}\\) separate points and tangent vectors (Varieties, Section 23).\n\n--------------------------------------------------------------------------------\nSection 28.27 (01PR): Ample invertible sheaves—The Stacks project (https://stacks.math.columbia.edu/tag/01PR)\n【turn381141search21】 [wordlim: 200] Crawled: last month; # The Stacks project ... Then $\\mathcal{L}$ is ample if and only if $\\mathcal{L}^{\\otimes n}$ is ample. ... For $s \\in \\Gamma (X, \\mathcal{L}^{\\otimes d})$ denote $s' = i^*s$ the pullback of $s$ to $X'$.\n\n--------------------------------------------------------------------------------\nSection 29.37 (01VG): Relatively ample sheaves—The Stacks project (https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/01VG)\n【turn381141search22】 [wordlim: 200] Crawled: 3 weeks ago; # The Stacks project ... We note that the existence of a relatively ample sheaf on $X$ does not force the morphism $X \\to S$ to be of finite type. ... Since the restriction of an ample sheaf to a closed subscheme is ample, see Properties, Lemma 28.26.3 we conclude that the pullback of $\\mathcal{O}_ Y(d')$ is ample.\n\n--------------------------------------------------------------------------------\nSection 29.40 (02NO): Ample and very ample sheaves relative to finite type morphisms—The Stacks project (https://stacks.math.columbia.edu/tag/02NO)\n【turn381141search23】 [wordlim: 200] Crawled: today; As P n S$\\mathbf{P}^ n_ S$ is a projective bundle over S$S$ (see Constructions, Lemma 27.21.5) we see that (5) implies (3) and (6) implies (4) from the definition of a relatively very ample sheaf.\n\n--------------------------------------------------------------------------------\nSection 29.16 (01T9): Points of finite type and Jacobson schemes—The Stacks project (https://stacks.math.columbia.edu/tag/01T9)\n【turn381141search24】 [wordlim: 200] Crawled: today; # The Stacks project ... Any scheme locally of finite type over a field.\n\n--------------------------------------------------------------------------------\nSection 17.9 (01B4): Modules of finite type—The Stacks project (https://stacks.math.columbia.edu/tag/01B4)\n【turn381141search25】 [wordlim: 200] Crawled: today; The pullback f∗G$f^*\\mathcal{G}$ of a finite type O Y$\\mathcal{O}_ Y$-module is a finite type O X$\\mathcal{O}_ X$-module.\n\n--------------------------------------------------------------------------------\nSection 10.130 (00RD): Openness of Cohen-Macaulay loci—The Stacks project (https://stacks.math.columbia.edu/tag/00RD)\n【turn381141search26】 [wordlim: 200] Crawled: 3 weeks ago; # The Stacks project ... Let $S$ be a finite type algebra over a field $k$.\n\n--------------------------------------------------------------------------------\nClosed immersion (https://en.wikipedia.org/wiki/Closed_immersion)\n【turn381141search39】 [wordlim: 200] Crawled: 6 months ago; In algebraic geometry, a closed immersion of scheme s is a morphism of schemes f: Z \\to X that identifies Z as a closed subset of X such that locally, regular function s on Z can be extended to X. ... - Section 26.4 (01HJ): Closed immersions of locally ringed spaces-The Stacks project. ... Columbia University.\n\n--------------------------------------------------------------------------------\narXiv:0904.1592v2  [math.AG]  11 Dec 2011 (https://arxiv.org/pdf/0904.1592v2)\n【turn381141view0】 [wordlim: 200] Crawled: 2 days ago; Content type: application/pdf; Number of pages: 35; Source: open({\"ref_id\":\"https://arxiv.org/pdf/0904.1592v2\",\"lineno\":null}); Total lines: 2076\nL0@P0: arXiv:0904.1592v2 [math.AG] 11 Dec 2011\nL1@P0: FUNCTORIAL DESINGULARIZATION OF QUASI-EXCELLENT\nL2@P0: SCHEMES IN CHARACTERISTIC ZERO: THE NON-EMBEDDED\nL3@P0: CASE\nL4@P0: MICHAEL TEMKIN\nL5@P0: Abstract. We prove that any reduced noetherian quasi-excellent scheme of\nL6@P0: characteristic zero admits a strong desingularization which is functorial with\nL7@P0: respect to all regular morphisms. As a main application, we deduce that any\nL8@P0: reduced formal variety of characteristic zero admits a strong functorial desin\u0002gularization. Also, we show that as an easy formal consequence of our main\nL9@P0: result one obtains strong functorial desingularization for many other spaces\nL10@P0: of characteristic zero including quasi-excellent stacks and formal schemes, and\nL11@P0: complex or non-archimedean analytic spaces. Moreover, these functors easily\nL12@P0: generalize to non-compact setting by use of generalized convergent blow up\nL13@P0: sequences with regular centers.\nL14@P0: 1. Introduction\nL15@P0: 1.1. Motivation.\nL16@P0: 1.1.1. Historical overview. Encouraged by Hironaka’s work [Hir] on resolution of\nL17@P0: singularities, Grothendieck introduced quasi-excellent (or qe) schemes in [EGA,\nL18@P0: IV2, §7.8] in order to provide a natural general framework for desingularization.\nL19@P0: Grothendieck observed that the schemes studied by Hironaka were schemes of finite\nL20@P0: type over a local qe scheme k, and proved that if any integral scheme of finite type\nL21@P0: over a base scheme k admits a desingularization in the weakest possible sense then k\nL22@P0: is quasi-excellent. Grothendieck conjectured in [EGA, IV2, 7.9.6] that the converse\nL23@P0: is probably true, and thus any qe scheme admits a desingularization, and claimed\nL24@P0: without proof that the conjecture holds true for noetherian qe schemes over Q\nL25@P0: as can be proved by Hironaka’s method. The latter claim was never checked, so\nL26@P0: desingularization of qe schemes of characteristic zero remained a conjecture until\nL27@P0: the author’s work [Tem1] in 2008.\nL28@P0: It was shown in [Tem1] that, indeed, desingularization of qe schemes over Q can\nL29@P0: be obtained from Hironaka’s results relatively easily. Perhaps this is close to the\nL30@P0: reduction Grothendieck had in mind, see Remark 1.3.3. However, the main result of\nL31@P0: [Tem1] was that desingularization of qe schemes over Q follows from desingulariza\u0002tion of varieties (by a more complicated argument). This is important, since many\nL32@P0: relatively simple proofs for varieties are now available, and they establish a canon\u0002ical resolution which is compatible with all smooth morphisms between varieties,\nL33@P0: as opposed to the non-constructive original Hironaka’s method.\nL34@P0: Key words and phrases. Resolution, singularities, quasi-excellent, functorial non-embedded\nL35@P0: desingularization.\nL36@P0: The author wishes to thank E. Bierstone, P. Milman, J. Kollar, L. Illusie, O. Gabber and O.\nL37@P0: Villamayor for useful discussions, and the anonymous referee for numerous valuable comments.\nL38@P0-1: 12 MICHAEL TEMKIN\nL39@P1: 1.1.2. New goals. The main disadvantage of the results from [Tem1] was that the\nL40@P1: desingularization results for qe schemes were weaker than their analogs for varieties\nL41@P1: in two aspects: (a) the centers of resolving blow ups were not regular, (b) no\nL42@P1: functoriality/canonicity was achieved. The aim of this paper is to strengthen the\nL43@P1: methods of [Tem1] in order to construct a desingularization by blowing up only\nL44@P1: regular centers and so that the whole blow up sequence is functorial in all regular\nL45@P1: morphisms (in particular, we cannot rely on the method of [Hir] anymore since\nL46@P1: its resolution is not functorial). Our main results are Theorems 1.2.1 and 5.3.2\nL47@P1: providing non-embedded desingularization of noetherian qe schemes over Q and\nL48@P1: non-compact objects including all qe (formal) schemes over Q and analytic spaces in\nL49@P1: characteristic zero. In comparison with the known non-embedded desingularization\nL50@P1: of varieties our results give the strongest known desingularization with the exception\nL51@P1: mentioned in Remark 1.2.2: the centers Vi֒→ Xi of our blow ups are not contained\nL52@P1: in the maximum locus of the Hilbert-Samuel (or HS) function, moreover, Xi does\nL53@P1: not have to be normally flat along Vi. As a drawback, our method does not treat\nL54@P1: non-embedded desingularization of generically non-reduced schemes.\nL55@P1: Although our method follows the method of [Tem1] closely, we tried to make\nL56@P1: the paper as self-contained as possible. So, the familiarity with [Tem1] can be\nL57@P1: useful but is not necessary. In particular, we give/recall all needed definitions.\nL58@P1: As opposed to [Tem1], this time we split the exposition into two separate papers\nL59@P1: concerning non-embedded and embedded desingularization. Note that unlike the\nL60@P1: case of varieties, we have to deal with both cases because one cannot deduce the\nL61@P1: non-embedded case from the embedded one – there are qe schemes that cannot be\nL62@P1: locally embedded into regular ones. This paper deals only with the non-embedded\nL63@P1: case (without boundaries), while the embedded case (with boundaries) is dealt with\nL64@P1: in [Tem3].\nL65@P1: 1.1.3. Applications. Currently, it seems that the most applicable case of desingu\u0002larization of general qe schemes over Q is when the schemes are of finite type over\nL66@P1: a ring k[[t1, . . . , tn]] with k a field. For example, this case (in its non-functorial ver\u0002sion from [Tem1]) was used for studying log-canonical thresholds in [FEM], motivic\nL67@P1: integration in [Nic], and desingularization of meromorphic connections in [Ked].\nL68@P1: The non-functorial method of [Tem1] could only desingularize affine qe formal\nL69@P1: schemes, and in my communication with Mustata, Nicaise, Kedlaya and Soibel\u0002man I was urged to strengthen the method so that it may desingularize arbitrary\nL70@P1: formal schemes of finite type over k[[t1, . . . , tn]]. This served as the main motivation\nL71@P1: to continue the research on desingularization of qe schemes and I am very grateful\nL72@P1: to them all for the encouragement. I would expect that desingularization of formal\nL73@P1: schemes of finite type over k[[t1, . . . , tn]] should be the most applicable particular\nL74@P1: case of the main results of this paper. Also, desingularization of Berkovich analytic\nL75@P1: spaces of characteristic zero seems to be new (at least, in the non-good case).\nL76@P1: 1.2. Main result.\nL77@P1: 1.2.1. Strong non-embedded desingularization. We refer to §§2.1,2.2 for the termi\u0002nology, which includes the notions of quasi-excellent schemes, regular loci and mor\u0002phisms, and blow up sequences. Here is the strong non-embedded desingularization\nL78@P1: theorem for generically reduced noetherian quasi-excellent schemes in characteristic\nL79@P1-2: zero. In this paper ”strong” means that the desingularization blows up only regularFUNCTORIAL DESINGULARIZATION OVER Q: THE NON-EMBEDDED CASE 3\nL80@P2: subschemes, unlike the terminology of Bierstone-Milman, where one also requires\nL81@P2: that each center lies in the maximum locus of the HS function.\nL82@P2: Theorem 1.2.1. For any noetherian quasi-excellent generically reduced scheme\nL83@P2: X = X0 over Spec(Q) there exists a blow up sequence F(X): Xn 99K X0 such that\nL84@P2: the following conditions are satisfied:\nL85@P2: (i) the centers of the blow ups are disjoint from the preimages of the regular locus\nL86@P2: Xreg;\nL87@P2: (ii) the centers of the blow ups are regular;\nL88@P2: (iii) Xn is regular;\nL89@P2: (iv) the blow up sequence F(X) is functorial with respect to all regular morphisms\nL90@P2: X′ → X, in the sense that F(X′) is obtained from F(X) ×X X′by omitting all\nL91@P2: empty blow ups.\nL92@P2: 1.2.2. On the non-reduced case.\nL93@P2: Remark 1.2.2. (i) Theorem 1.2.1 implies that the same claim holds for all noe\u0002therian qe schemes over Q. Indeed, given an arbitrary such X with reduction Xe\nL94@P2: we can consider the blow up sequence i∗F(Xe): X′ 99K X which is the pushfor\u0002ward of F(Xe): Xe′ 99K Xe with respect to the closed immersion i: X ֒ e → X (see\nL95@P2: §4.2.1). Then the reduction of X′is Xe′, so it is regular. Next we kill all generically\nL96@P2: non-reduced components by blowing them up along their reductions, obtaining a\nL97@P2: blow up X′′ → X′ with generically reduced X′′. Finally, it remains to apply\nL98@P2: F(X′′): X′′′ 99K X′′ to construct a functorial desingularization X′′′ 99K X.\nL99@P2: (ii) We ignore on purpose the case when X is not reduced along an irreducible\nL100@P2: component because in this case the assertion of the theorem is not the ”right”\nL101@P2: version of desingularization: such naive desingularization simply destroys all gener\u0002ically non-reduced components. In addition, existence of naive desingularization of\nL102@P2: non-reduced schemes does not assert anything new, as we saw in (i).\nL103@P2: (iii) The correct way to desingularize non-reduced schemes is to make them\nL104@P2: normally flat along the reduction. Loosely speaking, such desingularization does\nL105@P2: not kill non-reduced components, but makes their nilpotent structure ”as smooth\nL106@P2: as possible”. The only known way to achieve such desingularization is to use an\nL107@P2: algorithm such that each its center Vilies in the maximum HS locus of Xi (or, at\nL108@P2: least, Xiis normally flat along Vi), and to stop the algorithm just before it blows\nL109@P2: up the non-reduced components. Our algorithm does not possess this property (see\nL110@P2: also Remark 1.3.1).\nL111@P2: 1.3. Overview.\nL112@P2: 1.3.1. The black box strategy. Now let us discuss our method and the structure of\nL113@P2: the paper. In order to construct a desingularization F of all qe schemes over Q we\nL114@P2: use as a black box any algorithm FVar which desingularizes varieties of character\u0002istic zero and is functorial with respect to all regular morphisms (i.e. satisfies the\nL115@P2: conditions (i), (iii) and (iv) from the theorem). Moreover, if FVar is strong then\nL116@P2: we can also achieve that F is strong, i.e. satisfies the condition (ii) as well. We\nL117@P2: consider both strong and non-strong cases mainly because this does not cost us any\nL118@P2: extra-work; also, there exist many non-strong algorithms, e.g. those of [Kol] and\nL119@P2-3: [W l].4 MICHAEL TEMKIN\nL120@P3: 1.3.2. Extending FVar. It was checked in a very recent work [BMT] that the al\u0002gorithm of Bierstone-Milman is functorial with respect to all regular morphisms\nL121@P3: (not necessarily of finite type). Thus, for the sake of concreteness, we can start\nL122@P3: with the algorithm FVar from [BM2]. (Alternatively, it is shown in [BMT] that one\nL123@P3: can start with any algorithm FQ for varieties over Q and extend it to all varieties\nL124@P3: using approximation results of [EGA, IV3, §8.8]. In such case, one can also build\nL125@P3: on many other available algorithms.) In §2 we fix our terminology and recall many\nL126@P3: basic facts about blow ups, desingularizations and formal schemes. We warn the\nL127@P3: reader that the terminology differs in part from that of [Tem1], including blow ups\nL128@P3: from §2.2.1, desingularization from §2.3.1 and qe formal schemes from §2.4.3.\nL129@P3: We extend in §3 the functor FVar to pairs (X, Z), where X is a qe scheme over Q\nL130@P3: and Z ֒→ X is a Cartier divisor containing the singular locus of X and isomorphic\nL131@P3: to a disjoint union of varieties. Each FVar(X, Z) is a desingularization of X, and it\nL132@P3: remains unclear if it really depends on Z. Similarly to the method of [Tem1], this\nL133@P3: construction goes by passing to the formal completion of X along Z, thus obtaining\nL134@P3: a rig-regular formal variety X = XbZ, and algebraizing X by a variety X′. Then\nL135@P3: FVar(X′) induces desingularizations on X and X, and the main problem we have to\nL136@P3: solve is that the choice of X′is absolutely non-canonical. Moreover, and this causes\nL137@P3: the main trouble, even the ground field of X′can be chosen in many ways. This\nL138@P3: complication is by-passed by proving that all information about the singularities of\nL139@P3: X can be extracted already from a sufficiently thick nilpotent neighborhood Xn ֒→ X\nL140@P3: of its closed fiber Xs. Moreover, everything is determined by the scheme Xn, and\nL141@P3: is independent of a variety structure of Xn, which is not unique. In particular, we\nL142@P3: prove in §3.3 that FVar(X) := FVar \\(X′) is canonically defined already by Xn, and\nL143@P3: is therefore independent of the choice of the algebraization X′. This section is the\nL144@P3: heart of the paper, and it is the main novelty since [Tem1]. As in loc.cit., Elkik’s\nL145@P3: results from [Elk] are the main tool we are using for algebraization. It will also be\nL146@P3: convenient (though not critical) to use an improvement of some Elkik’s results by\nL147@P3: Gabber-Ramero.\nL148@P3: Remark 1.3.1. It is a natural question if one can strengthen our method so that\n"
    }
  ],
  "isError": false
}


# PRIMARY live Stacks statement/proof observations with rendered coordinates

{
  "content": [
    {
      "type": "text",
      "text": "Section 29.38 (01VG): Relatively ample sheaves—The Stacks project (https://stacks.math.columbia.edu/tag/01VG)\n【turn171995view0】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/01VG\",\"lineno\":30}); Total lines: 132\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†29】: Morphisms of Schemes\nL10:   * Section 【7†29.38】: Relatively ample sheaves (【8†cite】)\nL11: \nL12: [Input]\nL13: \nL14:   * 【9†previous section】\nL15:   * 【10†next section】\nL16: ## 29.38 Relatively ample sheaves\nL17: \nL18: Let $X$ be a scheme and $\\mathcal{L}$ an invertible sheaf on $X$. Then $\\mathcal{L}$ is ample on $X$ if $X$ is quasi-compact and every point of $X$ is contained in an affine open of the form $X_ s$, where $s \\in \\Gamma (X, \\mathcal{L}^{\\otimes n})$ and $n \\geq 1$, see Properties, Definition 【11†28.27.1】. We turn this into a relative notion as follows.\nL19: \nL20: reference\nL21: 【12†Definition 29.38.1.】 Let $f : X \\to S$ be a morphism of schemes. Let $\\mathcal{L}$ be an invertible $\\mathcal{O}_ X$-module. We say $\\mathcal{L}$ is relatively ample, or $f$-relatively ample, or ample on $X/S$, or $f$-ample if $f : X \\to S$ is quasi-compact, and if for every affine open $V \\subset S$ the restriction of $\\mathcal{L}$ to the open subscheme $f^{-1}(V)$ of $X$ is ample.\nL22: We note that the existence of a relatively ample sheaf on $X$ does not force the morphism $X \\to S$ to be of finite type.\nL23: \nL24: 【13†Lemma 29.38.2.】 Let $X \\to S$ be a morphism of schemes. Let $\\mathcal{L}$ be an invertible $\\mathcal{O}_ X$-module. Let $n \\geq 1$. Then $\\mathcal{L}$ is $f$-ample if and only if $\\mathcal{L}^{\\otimes n}$ is $f$-ample.\nL25: \nL26: Proof. This follows from Properties, Lemma 【14†28.27.2】. $\\square$\nL27: 【15†Lemma 29.38.3.】 Let $f : X \\to S$ be a morphism of schemes. If there exists an $f$-ample invertible sheaf, then $f$ is separated.\nL28: \nL29: Proof. Being separated is local on the base (see Schemes, Lemma 【16†26.21.7】 for example; it also follows easily from the definition). Hence we may assume $S$ is affine and $X$ has an ample invertible sheaf. In this case the result follows from Properties, Lemma 【17†28.27.8】. $\\square$\nL30: There are many ways to characterize relatively ample invertible sheaves, analogous to the equivalent conditions in Properties, Proposition 【18†28.27.13】. We will add these here as needed.\nL31: \nL32: reference\nL33: \nL34: 【19†Lemma 29.38.4.】 Let $f : X \\to S$ be a quasi-compact morphism of schemes. Let $\\mathcal{L}$ be an invertible sheaf on $X$. The following are equivalent:\nL35: \nL36:   1. The invertible sheaf $\\mathcal{L}$ is $f$-ample.\nL37:   2. There exists an open covering $S = \\bigcup V_ i$ such that each $\\mathcal{L}|_{f^{-1}(V_ i)}$ is ample relative to $f^{-1}(V_ i) \\to V_ i$.\nL38: \nL39:   3. There exists an affine open covering $S = \\bigcup V_ i$ such that each $\\mathcal{L}|_{f^{-1}(V_ i)}$ is ample.\nL40: \nL41:   4. There exists a quasi-coherent graded $\\mathcal{O}_ S$-algebra $\\mathcal{A}$ and a map of graded $\\mathcal{O}_ X$-algebras $\\psi : f^*\\mathcal{A} \\to \\bigoplus _{d \\geq 0} \\mathcal{L}^{\\otimes d}$ such that $U(\\psi ) = X$ and\nL42: \\[ r_{\\mathcal{L}, \\psi } : X \\longrightarrow \\underline{\\text{Proj}}_ S(\\mathcal{A}) \\]\nL43: \nL44: is an open immersion (see Constructions, Lemma 【20†27.19.1】 for notation).\nL45: \nL46:   5. The morphism $f$ is quasi-separated and part (4) above holds with $\\mathcal{A} = f_*(\\bigoplus _{d \\geq 0} \\mathcal{L}^{\\otimes d})$ and $\\psi $ the adjunction mapping.\nL47: \nL48:   6. Same as (4) but just requiring $r_{\\mathcal{L}, \\psi }$ to be an immersion.\nL49: Proof. It is immediate from the definition that (1) implies (2) and (2) implies (3). It is clear that (5) implies (4).\nL50: Assume (3) holds for the affine open covering $S = \\bigcup V_ i$. We are going to show (5) holds. Since each $f^{-1}(V_ i)$ has an ample invertible sheaf we see that $f^{-1}(V_ i)$ is separated (Properties, Lemma 【17†28.27.8】). Hence $f$ is separated. By Schemes, Lemma 【21†26.24.1】 we see that $\\mathcal{A} = f_*(\\bigoplus _{d \\geq 0} \\mathcal{L}^{\\otimes d})$ is a quasi-coherent graded $\\mathcal{O}_ S$-algebra.\nL51: Denote $\\psi : f^*\\mathcal{A} \\to \\bigoplus _{d \\geq 0} \\mathcal{L}^{\\otimes d}$ the adjunction mapping. The description of the open $U(\\psi )$ in Constructions, Section 【22†27.19】 and the definition of ampleness of $\\mathcal{L}|_{f^{-1}(V_ i)}$ show that $U(\\psi ) = X$.\nL52: Moreover, Constructions, Lemma 【20†27.19.1】 part (3) shows that the restriction of $r_{\\mathcal{L}, \\psi }$ to $f^{-1}(V_ i)$ is the same as the morphism from Properties, Lemma 【23†28.27.9】 which is an open immersion according to Properties, Lemma 【24†28.27.11】. Hence (5) holds.\nL53: Let us show that (4) implies (1). Assume (4). Denote $\\pi : \\underline{\\text{Proj}}_ S(\\mathcal{A}) \\to S$ the structure morphism. Choose $V \\subset S$ affine open. By Constructions, Definition 【25†27.16.7】 we see that $\\pi ^{-1}(V) \\subset \\underline{\\text{Proj}}_ S(\\mathcal{A})$ is equal to $\\text{Proj}(A)$ where $A = \\mathcal{A}(V)$ as a graded ring. Hence $r_{\\mathcal{L}, \\psi }$ maps $f^{-1}(V)$ isomorphically onto a quasi-compact open of $\\text{Proj}(A)$.\nL54: Moreover, $\\mathcal{L}^{\\otimes d}$ is isomorphic to the pullback of $\\mathcal{O}_{\\text{Proj}(A)}(d)$ for some $d \\geq 1$. (See part (3) of Constructions, Lemma 【20†27.19.1】 and the final statement of Constructions, Lemma 【26†27.14.1】.) This implies that $\\mathcal{L}|_{f^{-1}(V)}$ is ample by Properties, Lemmas 【27†28.27.12】 and 【14†28.27.2】.\nL55: Assume (6). By the equivalence of (1) - (5) above we see that the property of being relatively ample on $X/S$ is local on $S$. Hence we may assume that $S$ is affine, and we have to show that $\\mathcal{L}$ is ample on $X$. In this case the morphism $r_{\\mathcal{L}, \\psi }$ is identified with the morphism, also denoted $r_{\\mathcal{L}, \\psi } : X \\to \\text{Proj}(A)$ associated to the map $\\psi : A = \\mathcal{A}(V) \\to \\Gamma _*(X, \\mathcal{L})$.\nL56: (See references above.) As above we also see that $\\mathcal{L}^{\\otimes d}$ is the pullback of the sheaf $\\mathcal{O}_{\\text{Proj}(A)}(d)$ for some $d \\geq 1$. Moreover, since $X$ is quasi-compact we see that $X$ gets identified with a closed subscheme of a quasi-compact open subscheme $Y \\subset \\text{Proj}(A)$. By Constructions, Lemma 【28†27.10.6】 (see also Properties, Lemma 【27†28.27.12】) we see that $\\mathcal{O}_ Y(d')$ is an ample invertible sheaf on $Y$ for some $d' \\geq 1$.\nL57: Since the restriction of an ample sheaf to a closed subscheme is ample, see Properties, Lemma 【29†28.27.3】 we conclude that the pullback of $\\mathcal{O}_ Y(d')$ is ample. Combining these results with Properties, Lemma 【14†28.27.2】 we conclude that $\\mathcal{L}$ is ample as desired. $\\square$\nL58: reference\nL59: \nL60: 【30†Lemma 29.38.5.】 Let $f : X \\to S$ be a morphism of schemes. Let $\\mathcal{L}$ be an invertible $\\mathcal{O}_ X$-module. Assume $S$ affine. Then $\\mathcal{L}$ is $f$-relatively ample if and only if $\\mathcal{L}$ is ample on $X$.\nL61: \nL62: Proof. Immediate from Lemma 【19†29.38.4】 and the definitions. $\\square$\nL63: \nL64: reference\nL65: \nL66: 【31†Lemma 29.38.6.】 Let $f : X \\to S$ be a morphism of schemes. Then $f$ is quasi-affine if and only if $\\mathcal{O}_ X$ is $f$-relatively ample.\nL67: Proof. Follows from Properties, Lemma 【32†28.28.1】 and the definitions. $\\square$\nL68: \nL69: 【33†Lemma 29.38.7.】 Let $f : X \\to Y$ be a morphism of schemes, $\\mathcal{M}$ an invertible $\\mathcal{O}_ Y$-module, and $\\mathcal{L}$ an invertible $\\mathcal{O}_ X$-module.\nL70: \nL71:   1. If $\\mathcal{L}$ is $f$-ample and $\\mathcal{M}$ is ample, then $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ is ample for $a \\gg 0$.\nL72: \nL73:   2. If $\\mathcal{M}$ is ample and $f$ quasi-affine, then $f^*\\mathcal{M}$ is ample.\nL74: Proof. Assume $\\mathcal{L}$ is $f$-ample and $\\mathcal{M}$ ample. By assumption $Y$ and $f$ are quasi-compact (see Definition 【12†29.38.1】 and Properties, Definition 【11†28.27.1】). Hence $X$ is quasi-compact. By Properties, Lemma 【17†28.27.8】 the scheme $Y$ is separated and by Lemma 【15†29.38.3】 the morphism $f$ is separated. Hence $X$ is separated by Schemes, Lemma 【34†26.21.12】. Pick $x \\in X$.\nL75: We can choose $m \\geq 1$ and $t \\in \\Gamma (Y, \\mathcal{M}^{\\otimes m})$ such that $Y_ t$ is affine and $f(x) \\in Y_ t$. Since $\\mathcal{L}$ restricts to an ample invertible sheaf on $f^{-1}(Y_ t) = X_{f^*t}$ we can choose $n \\geq 1$ and $s \\in \\Gamma (X_{f^*t}, \\mathcal{L}^{\\otimes n})$ with $x \\in (X_{f^*t})_ s$ with $(X_{f^*t})_ s$ affine.\nL76: By Properties, Lemma 【35†28.18.2】 part (2) whose assumptions are satisfied by the above, there exists an integer $e \\geq 1$ and a section $s' \\in \\Gamma (X, \\mathcal{L}^{\\otimes n} \\otimes f^*\\mathcal{M}^{\\otimes em})$ which restricts to $s(f^*t)^ e$ on $X_{f^*t}$. For any $b > 0$ consider the section $s'' = s'(f^*t)^ b$ of $\\mathcal{L}^{\\otimes n} \\otimes f^*\\mathcal{M}^{\\otimes (e + b)m}$. Then $X_{s''} = (X_{f^*t})_ s$ is an affine open of $X$ containing $x$.\nL77: Picking $b$ such that $n$ divides $e + b$ we see $\\mathcal{L}^{\\otimes n} \\otimes f^*\\mathcal{M}^{\\otimes (e + b)m}$ is the $n$th power of $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ for some $a$ and we can get any $a$ divisible by $m$ and big enough. Since $X$ is quasi-compact a finite number of these affine opens cover $X$. We conclude that for some $a$ sufficiently divisible and large enough the invertible sheaf $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ is ample on $X$.\nL78: On the other hand, we know that $\\mathcal{M}^{\\otimes c}$ (and hence its pullback to $X$) is globally generated for all $c \\gg 0$ by Properties, Proposition 【18†28.27.13】. Thus $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a + c}$ is ample (Properties, Lemma 【36†28.27.5】) for $c \\gg 0$ and (1) is proved.\nL79: Part (2) follows from Lemma 【31†29.38.6】, Properties, Lemma 【14†28.27.2】, and part (1). $\\square$\nL80: \nL81: 【37†Lemma 29.38.8.】 Let $g : Y \\to S$ and $f : X \\to Y$ be morphisms of schemes. Let $\\mathcal{M}$ be an invertible $\\mathcal{O}_ Y$-module. Let $\\mathcal{L}$ be an invertible $\\mathcal{O}_ X$-module. If $S$ is quasi-compact, $\\mathcal{M}$ is $g$-ample, and $\\mathcal{L}$ is $f$-ample, then $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ is $g \\circ f$-ample for $a \\gg 0$.\nL82: Proof. Let $S = \\bigcup _{i = 1, \\ldots , n} V_ i$ be a finite affine open covering. By Lemma 【19†29.38.4】 it suffices to prove that $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ is ample on $(g \\circ f)^{-1}(V_ i)$ for $i = 1, \\ldots , n$. Thus the lemma follows from Lemma 【33†29.38.7】. $\\square$\nL83: 【38†Lemma 29.38.9.】 Let $f : X \\to S$ be a morphism of schemes. Let $\\mathcal{L}$ be an invertible $\\mathcal{O}_ X$-module. Let $S' \\to S$ be a morphism of schemes. Let $f' : X' \\to S'$ be the base change of $f$ and denote $\\mathcal{L}'$ the pullback of $\\mathcal{L}$ to $X'$. If $\\mathcal{L}$ is $f$-ample, then $\\mathcal{L}'$ is $f'$-ample.\nL84: Proof. By Lemma 【19†29.38.4】 it suffices to find an affine open covering $S' = \\bigcup U'_ i$ such that $\\mathcal{L}'$ restricts to an ample invertible sheaf on $(f')^{-1}(U_ i')$ for all $i$. We may choose $U'_ i$ mapping into an affine open $U_ i \\subset S$. In this case the morphism $(f')^{-1}(U'_ i) \\to f^{-1}(U_ i)$ is affine as a base change of the affine morphism $U'_ i \\to U_ i$ (Lemma 【39†29.11.9】). Thus $\\mathcal{L}'|_{(f')^{-1}(U'_ i)}$ is ample by Lemma 【33†29.38.7】. $\\square$\nL85: 【40†Lemma 29.38.10.】 Let $g : Y \\to S$ and $f : X \\to Y$ be morphisms of schemes. Let $\\mathcal{L}$ be an invertible $\\mathcal{O}_ X$-module. If $\\mathcal{L}$ is $g \\circ f$-ample and $f$ is quasi-compact【41†^{1}】 then $\\mathcal{L}$ is $f$-ample.\nL86: Proof. Assume $f$ is quasi-compact and $\\mathcal{L}$ is $g \\circ f$-ample. Let $U \\subset S$ be an affine open and let $V \\subset Y$ be an affine open with $g(V) \\subset U$. Then $\\mathcal{L}|_{(g \\circ f)^{-1}(U)}$ is ample on $(g \\circ f)^{-1}(U)$ by assumption. Since $f^{-1}(V) \\subset (g \\circ f)^{-1}(U)$ we see that $\\mathcal{L}|_{f^{-1}(V)}$ is ample on $f^{-1}(V)$ by Properties, Lemma 【42†28.27.14】.\nL87: Namely, $f^{-1}(V) \\to (g \\circ f)^{-1}(U)$ is a quasi-compact open immersion by Schemes, Lemma 【43†26.21.14】 as $(g \\circ f)^{-1}(U)$ is separated (Properties, Lemma 【17†28.27.8】) and $f^{-1}(V)$ is quasi-compact (as $f$ is quasi-compact). Thus we conclude that $\\mathcal{L}$ is $f$-ample by Lemma 【19†29.38.4】. $\\square$\nL88: 【44†[1]】 This follows if $g$ is quasi-separated by Schemes, Lemma 【43†26.21.14】.\n\n--------------------------------------------------------------------------------\nSection 29.20 (0HA6): Excellent schemes—The Stacks project (https://stacks.math.columbia.edu/tag/0HA6)\n【turn171995view1】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/0HA6\",\"lineno\":20}); Total lines: 101\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†29】: Morphisms of Schemes\nL10:   * Section 【7†29.20】: Excellent schemes (【8†cite】)\nL11: \nL12: [Input]\nL13: \nL14:   * 【9†previous section】\nL15:   * 【10†next section】\nL16: ## 29.20 Excellent schemes\nL17: \nL18: We recall that a ring is quasi-excellent if it is a G-ring and J-2. A ring is excellent if it is quasi-excellent and universally catenary.\nL19: \nL20: 【11†Definition 29.20.1.】 Let $X$ be a scheme.\nL21: \nL22:   1. We say $X$ is quasi-excellent if for every $x \\in X$ there exists an affine open neighbourhood $x \\in U \\subset X$ such that the ring $\\mathcal{O}_ X(U)$ is quasi-excellent (see More on Algebra, Definition 【12†15.53.1】).\nL23:   2. We say $X$ is excellent if for every $x \\in X$ there exists an affine open neighbourhood $x \\in U \\subset X$ such that the ring $\\mathcal{O}_ X(U)$ is excellent (see More on Algebra, Definition 【12†15.53.1】).\nL24: \nL25: Quasi-excellent schemes are locally Noetherian (G-rings are Noetherian).\nL26: \nL27: 【13†Lemma 29.20.2.】 Let $X$ be a scheme. The following are equivalent\nL28: \nL29:   1. $X$ is quasi-excellent, and\nL30: \nL31:   2. $X$ is a G-scheme and J-2.\nL32: Proof. The implication (1) $\\Rightarrow $ (2) follows on combining the definition of quasi-excellent schemes (Definition 【11†29.20.1】), the definition of quasi-excellent rings (More on Algebra, Definition 【12†15.53.1】), the definition of G-schemes (Properties, Definition 【14†28.14.1】), and Lemma 【15†29.19.2】. Conversely, if $X$ is a G-scheme and J-2, then for any $x \\in X$ we can find an affine open neighbourhood $x \\in U \\subset X$ such that $\\mathcal{O}_ X(U)$ is a G-ring.\nL33: By Lemma 【15†29.19.2】 the ring $\\mathcal{O}_ X(U)$ is also J-2, whence quasi-excellent. $\\square$\nL34: 【16†Lemma 29.20.3.】 A quasi-excellent scheme is Nagata.\nL35: \nL36: Proof. See More on Algebra, Lemma 【17†15.53.5】. $\\square$\nL37: \nL38: 【18†Lemma 29.20.4.】 Let $X$ be a scheme. The following are equivalent\nL39: \nL40:   1. $X$ is excellent, and\nL41: \nL42:   2. $X$ is quasi-excellent and universally catenary.\nL43: Proof. Assume (1). Since excellent rings are quasi-excellent, it is clear that $X$ is quasi-excellent. Since excellent rings are universally catenary, it also follows that $X$ is universally catenary by Lemma 【19†29.17.2】. Assume (2). Let $x \\in X$. Since $X$ is quasi-excellent there exists an affine open neighbourhood $x \\in U \\subset X$ such that $\\mathcal{O}_ X(U)$ is quasi-excellent.\nL44: Since $X$ is universally category, the ring $\\mathcal{O}_ X(U)$ is also universally catenary by Lemma 【19†29.17.2】, whence excellent. $\\square$\nL45: 【20†Lemma 29.20.5.】 Let $X$ be a scheme. The following are equivalent:\nL46: \nL47:   1. The scheme $X$ is (quasi-)excellent.\nL48: \nL49:   2. For every affine open $U \\subset X$ the ring $\\mathcal{O}_ X(U)$ is (quasi-)excellent.\nL50: \nL51:   3. There exists an affine open covering $X = \\bigcup U_ i$ such that each $\\mathcal{O}_ X(U_ i)$ is (quasi-)excellent.\nL52: \nL53:   4. There exists an open covering $X = \\bigcup X_ j$ such that each open subscheme $X_ j$ is (quasi-)excellent.\nL54: Moreover, if $X$ is (quasi-)excellent then every open subscheme is (quasi-)excellent.\nL55: \nL56: Proof. By Lemma 【13†29.20.2】 being quasi-excellent is the same as being a G-scheme and J-2. Thus for the quasi-excellent case, the lemma follows from Lemma 【15†29.19.2】 and Properties, Lemma 【21†28.14.3】. For the excellent case, use Lemma 【18†29.20.4】, the quasi-excellent case, and Lemma 【19†29.17.2】. $\\square$\nL57: 【22†Lemma 29.20.6.】 Let $f : X \\to S$ be a morphism. If $S$ is (quasi-)excellent and $f$ locally of finite type then $X$ is (quasi-)excellent.\nL58: \nL59: Proof. See More on Algebra, Lemma 【23†15.53.2】. $\\square$\nL60: \nL61: 【24†Lemma 29.20.7.】 The following types of schemes are excellent.\nL62: \nL63:   1. Any scheme locally of finite type over a field.\nL64: \nL65:   2. Any scheme locally of finite type over a Noetherian complete local ring.\nL66: \nL67:   3. Any scheme locally of finite type over $\\mathbf{Z}$.\nL68:   4. Any scheme locally of finite type over a Dedekind ring of characteristic zero.\nL69: \nL70: Proof. By Lemmas 【20†29.20.5】 and 【22†29.20.6】 we only need to show that the rings mentioned above are excellent. For this see More on Algebra, Proposition 【25†15.53.3】. $\\square$\nL71: \nL72: * * *\nL73: ## Comments (0)\nL74: \nL75: * * *\nL76: ## Post a comment\nL77: \nL78: Your email address will not be published. Required fields are marked.\nL79: \nL80: In your comment you can use 【26†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL81: \nL82: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL83: \nL84: All contributions are licensed under the 【27†GNU Free Documentation License†github.com】.\nL85: Name^{*}: [Input]\nL86: E-mail^{*}: [Input]\nL87: Site: [Input]\nL88: Comment:\nL89: \nL90: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 0HA6. Beware of the difference between the letter 'O' and the digit '0'.\nL91: \nL92: Tag: [Input] [Button: Post comment] [Input]\nL93: \nL94: The tag you filled in for the captcha is wrong. You need to write 0HA6, in case you are confused.\nL95:   * 【9†previous section】\nL96:   * 【10†next section】\nL97: \nL98: * * *\nL99: \nL100: 【28†View Section 29.20 as pdf】\n\n--------------------------------------------------------------------------------\nLemma 26.10.4 (01IQ)—The Stacks project (https://stacks.math.columbia.edu/tag/01IQ)\n【turn171995view2】 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/01IQ\",\"lineno\":20}); Total lines: 65\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†26】: Schemes\nL10:   * Section 【7†26.10】: Immersions of schemes\nL11:   * Lemma 【8†26.10.4】 (【9†cite】)\nL12: \nL13: [Input]\nL14: \nL15:   * 【10†previous remark】\nL16: \nL17: * * *\nL18: \nL19:   * 【11†history】\nL20:   * 【12†statistics】\nL21:   * 【13†10 tags refer to this tag】\nL22: 【8†Lemma 26.10.4.】 Let $f : Y \\to X$ be an immersion of schemes. Then $f$ is a closed immersion if and only if $f(Y) \\subset X$ is a closed subset.\nL23: Proof. If $f$ is a closed immersion then $f(Y)$ is closed by definition. Conversely, suppose that $f(Y)$ is closed. By definition there exists an open subscheme $U \\subset X$ such that $f$ is the composition of a closed immersion $i : Y \\to U$ and the open immersion $j : U \\to X$. Let $\\mathcal{I} \\subset \\mathcal{O}_ U$ be the quasi-coherent sheaf of ideals associated to the closed immersion $i$.\nL24: Note that $\\mathcal{I}|_{U \\setminus i(Y)} = \\mathcal{O}_{U \\setminus i(Y)} = \\mathcal{O}_{X \\setminus i(Y)}|_{U \\setminus i(Y)}$. Thus we may glue (see Sheaves, Section 【14†6.33】) $\\mathcal{I}$ and $\\mathcal{O}_{X \\setminus i(Y)}$ to a sheaf of ideals $\\mathcal{J} \\subset \\mathcal{O}_ X$. Since every point of $X$ has a neighbourhood where $\\mathcal{J}$ is quasi-coherent, we see that $\\mathcal{J}$ is quasi-coherent (in particular locally generated by sections).\nL25: By construction $\\mathcal{O}_ X/\\mathcal{J}$ is supported on $U$ and, restricted there, equal to $\\mathcal{O}_ U/\\mathcal{I}$. Thus we see that the closed subspaces associated to $\\mathcal{I}$ and $\\mathcal{J}$ are canonically isomorphic, see Example 【15†26.4.3】. In particular the closed subspace of $U$ associated to $\\mathcal{I}$ is isomorphic to a closed subspace of $X$.\nL26: Since $Y \\to U$ is identified with the closed subspace associated to $\\mathcal{I}$, see Lemma 【16†26.4.5】, we conclude that $Y \\to U \\to X$ is a closed immersion. $\\square$\nL27: * * *\nL28: ## Comments (0)\nL29: \nL30: There are also:\nL31: \nL32:   * 11 comment(s) on Section 【17†26.10】: Immersions of schemes\nL33: \nL34: * * *\nL35: ## Post a comment\nL36: \nL37: Your email address will not be published. Required fields are marked.\nL38: \nL39: In your comment you can use 【18†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL40: \nL41: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL42: \nL43: All contributions are licensed under the 【19†GNU Free Documentation License†github.com】.\nL44: Name^{*}: [Input]\nL45: E-mail^{*}: [Input]\nL46: Site: [Input]\nL47: Comment:\nL48: \nL49: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 01IQ. Beware of the difference between the letter 'O' and the digit '0'.\nL50: \nL51: Tag: [Input] [Button: Post comment] [Input]\nL52: \nL53: The tag you filled in for the captcha is wrong. You need to write 01IQ, in case you are confused.\nL54:   * 【10†previous remark】\nL55: \nL56: * * *\nL57: \nL58: 【20†View Lemma 26.10.4 as pdf】\nL59: \nL60: * * *\nL61: \nL62:   * 【11†history】\nL63:   * 【12†statistics】\nL64:   * 【13†10 tags refer to this tag】\n"
    }
  ],
  "isError": false
}
