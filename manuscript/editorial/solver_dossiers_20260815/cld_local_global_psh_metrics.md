# Dossier: Local CLD-psh metrics vs global psh approximation (CLD Remark 17.8.10)

**Date:** 15 August 2026. **Packet:** `/home/claude/work/refs/cld_local_global_psh_metrics.md`.
**Primary source:** `/home/claude/work/refs/cld25.txt` = Chambert-Loir–Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, 2025 revision (French), cited below as **CLD25** with line numbers of the local text file. Secondary local sources: `gjkm19.txt` (Gubler–Jell–Künnemann–Martin, Ann. Inst. Fourier 69 (2019) 2331–2376, incl. Burgos Gil–Sombra appendix), `ch72_major_open_problems.tex` (lines 1422–1436). Web status audit: arXiv:1204.6277 fetch returned no version metadata (failure noted; all quotations below are from cld25.txt); Gubler–Rabinoff, *On semipositive piecewise linear functions in non-archimedean analytic geometry*, arXiv:2503.05513 (= [83] of CLD25), checked at abstract/HTML-summary level only — every use below is flagged **[GR25, abstract-level]**.

Throughout \(k\) is a field complete with respect to a nontrivial non-archimedean absolute value (the strictness/formal-model theory of CLD25 §17.7 and App. B assumes nontriviality: lines 25277, 29543). "Rigid point" = point \(x\) with \([\mathscr H(x):k]<\infty\).

---

## 0. Formalization and the three global cones

### 0.1 Local psh (the hypothesis of Question A)

* **CLD25 Def. 8.1.1** (line 9723): \(\mathrm{Psh}_X\) is the *smallest* subsheaf of \(\mathbf R\cup\{-\infty\}\)-valued functions containing the smooth \(u\) with \(d'd''u\ge 0\) and stable under decreasing limits. Transfinite hierarchy \(\mathrm{Psh}_{X,\alpha}\) (Lemme 8.1.4, line 9757): \(\mathrm{Psh}_{X,0}\) = smooth psh, \(\mathrm{Psh}_{X,\alpha+1}\) = local decreasing limits from level \(\alpha\).
* **Rem. 8.1.6** (line 9785): CLD *do not know* whether the hierarchy is stationary; all known examples lie in \(\mathrm{Psh}_{X,1}\) ("localement approchable", Def. 8.1.13, line 9879).
* **Def. 8.1.7 / Prop. 8.1.11** (lines 9791, 9829): \(\mathrm{CPsh}_X=\mathrm C_X\cap \mathrm{Psh}_X\), level-by-level; at level 1, uniform and decreasing local approximation coincide (Dini + Lemme 8.1.10).
* **Prop. 8.3.1** (line 9996): psh \(\Rightarrow d'd''[u]\ge0\); for *smooth* \(u\) the converse holds. For general continuous \(u\) the converse (positive current \(\Rightarrow\) CLD-psh) is **not** stated in CLD25. Hence three *local* conditions, with proven inclusions only
  \(\;\mathrm{CPsh}_{X,1}\subseteq \mathrm{CPsh}_X \subseteq \{u\in \mathrm C: d'd''[u]\ge 0\}.\)
* **Def. 17.8.1** (line 25461): a continuous metric on a line bundle \(L\) (locally trivial for the usual topology) is *psh* iff \(\log\lVert s\rVert^{-1}\) is psh for every local invertible section. This — the sheaf-theoretic Def. 8.1.1 cone, **not** the positive-current cone — is the hypothesis of Question A, per the packet.

### 0.2 Global psh (the target of Question A)

* **CLD25 17.8.5** (line 25535): \(\lVert\cdot\rVert\) is **globalement psh** iff there are *smooth psh* metrics \(\lVert\cdot\rVert_n\) on \(L\) with \(\log(\lVert\cdot\rVert/\lVert\cdot\rVert_n)\to0\) uniformly on \(X\); **globalement dpsh** iff \(\overline L\simeq \overline L_1\otimes\overline L_2^{-1}\) (isometry) with \(\overline L_i\) globally psh.
* Trivial but load-bearing facts (proofs immediate from §8.1):
  * (G1) *global \(\Rightarrow\) local*: a globally psh metric has CLD-psh weights (uniform limits, Prop. 8.1.9/8.1.11) — so Question A asks for the converse;
  * (G2) *level bound*: globally psh \(\Rightarrow\) all weights lie in \(\mathrm{CPsh}_{X,1}\). **Hence Question A implies the level-collapse statement "continuous psh metric weights have level \(\le1\)"; conversely any continuous psh metric on a projective \(X\) with weight of level \(\ge2\) (if one exists) refutes A.** Interface with the separate packet `cld_psh_early_collapse.md` noted; not pursued here.
  * (G3) the globally psh cone is closed under uniform limits of metrics and under \(m\)-th tensor roots (\(u\) smooth psh \(\Leftrightarrow\) \(mu\) smooth psh on \(L^{\otimes m}\)).

### 0.3 The other two global cones; a discrepancy in ch71

* **FS cone**: metrics \(u=\frac1m\max_j(\log|s_j|+\lambda_j)\), \(s_j\in H^0(X,L^{\otimes m})\) finite base-point-free family, \(\lambda_j\in\mathbf R\); **FS-closure** = uniform limits of these.
* **Zhang cone**: nef-model (= semipositive formal) metrics; **Zhang-closure** = uniform limits (Zhang [142 of CLD25]; the definitional framework of gjkm19.txt lines 115–125).
* `ch72_major_open_problems.tex` (line 1426) phrases Problem `frontier-cld-global-metric` as "globally psh in the *Fubini–Study or nef-model* sense". **This is not CLD 17.8.5** and per the packet must not be substituted for it. Status of comparisons proved in this dossier: FS-closure \(\subseteq\) 17.8.5-cone (Prop. A1 below); FS-closure \(\subseteq\) Zhang-closure (an FS metric is a semiample model metric after scaling when \(\lambda_j\in\log|k^\times|\mathbf Q\), and a uniform limit of such in general); **no** inclusion between the 17.8.5-cone and the Zhang-closure is proven in either direction in general — even "smooth psh \(\Rightarrow\) Zhang-semipositive" is not in the literature examined (it is a second local-to-global problem of the same type). On common loci they agree (§1).

### 0.4 Parlinear ("paralinéaire") metrics (the hypothesis of Question B)

* CLD25 Def. 17.2.3 (line 24069) with the function classes of 12.5.2 (line 17526): *paralinéaire* (\(\mathbf R\)-pl), *entière* (locally \(\log|g|+c\)), *stricte* (\(\lambda\log|g|,\lambda\in\mathbf Q\)), *strictement entière* (locally \(\log|g|\)).
* **Prop. 17.7.5** (line 25277; \(k\) nontrivially valued, \(X\) strict paracompact): *formal metrics = paralinear strictly entire metrics.* Formal metric of a model \((\mathfrak X,\mathfrak L)\): 17.7.2 (line 25249).
* Textual observation: **Cor. 17.8.9** (line 25605) is *stated* for "métrique paralinéaire" but its printed proof starts "Soit \((\mathfrak X,\mathfrak L)\) un modèle formel … induisant la métrique **formelle** donnée" — i.e. it treats the strictly entire case; the reduction of \(\mathbf R\)-pl/entire to formal is left implicit (presumably via 12.5.2-approximation, but dpsh-ness is not obviously closed under uniform limits with uncontrolled decompositions). Also the proof's conclusion uses the locution "globalement psh-approchable et tropicalement psh-approchable" (line 25613), terminology defined nowhere in the 2025 text — a drift from an earlier draft; and 17.8.7 (line 25593) contains the typo "par alors". These indicate §17.8 is freshly rewritten; both Questions A and B are exactly Rem. 17.8.10 (line 25618).

---

## 1. Map of the known common loci (all CLD25-internal unless flagged)

| Locus | Local psh status | Global status | Source |
|---|---|---|---|
| Semiample formal metric (\(\mathfrak L\) with \(p:\mathfrak X\to\widehat{\mathbf P}^N_{k^\circ}\), \(p^*O(1)\simeq\mathfrak L^{\otimes d}\)) | tropically convex, psh | **globally psh** | Cor. 17.8.7 (l. 25591) via Prop. 17.8.6 |
| Weil/FS metric on \(O(1)\), \(\mathbf P^n\) | tropically convex | globally psh, with explicit smoothings \(M_\eta(\log|x_0|,\dots,\log|x_n|)\) and quantitative tropicalization control | Prop. 17.8.6 (l. 25541), Demailly [45, lemme 5.18] |
| pl-entire metric, \(X\) boundaryless | **psh near \(x\) \(\Leftrightarrow\) \(c_1\ge0\) near \(x\) \(\Leftrightarrow\) residual bundle \(\widetilde L_x\) nef** — the three local notions collapse | not addressed by CLD25 beyond the semiample case | **Cor. 18.8.8** (l. 27970); formal-model version Ex. 18.8.10 b) (l. 28034): positivity \(\Leftrightarrow\) nef on each proper component of \(\mathfrak X_s\) |
| Nef-residual pl (strictly entire) metric | psh near each such point | globally psh **unknown** (nef vs semiample gap; §3.4) | Prop. 17.8.4 (l. 25509) is local only |
| Projective algebraic \(X\), arbitrary pl metric | tropically d-convex (l. 25480) | **globally dpsh** (difference of two ample formal = semiample metrics) | Cor. 17.8.9 (l. 25605) |
| Cubist metrics on abelian varieties w/ formal abelian model | psh \(\Leftrightarrow\) \(\mathcal L_s\) nef | globally psh not addressed | 19.1.8/19.1.9 (l. 28428) |
| Curves | Thuillier's theory; envelope \(P(\lVert\cdot\rVert)\) continuous semipositive for \(L\) ample, **any** complete \(k\) | Zhang-closure well-understood | gjkm19 Thm 1.1 (file l. 205); retraction formula Prop. 1.2 fails in dim \(\ge2\) (Burgos–Sombra appendix) |

Necessary numerical condition (compatibility with the numerical class): if \(L\) carries any continuous metric with \(c_1\ge0\) then \(\deg_C L\ge0\) for every compact analytic curve \(C\subseteq X\) (restriction + CLD25 ch. 18 degree theory, 18.3.11/18.4.7). All approximants below are genuine metrics on \(L\) (transition-function compatible); no cocycle is altered.

---

## 2. Question A — attack map

Mechanisms attempted: (i) Richberg gluing in the CLD smooth category; (ii) envelope/quantization; (iii) skeletal reduction. Verdicts: (i) fails at two recorded points, one of them structural; (ii) yields a sharp conditional reduction with one clean open link; (iii) killed by the Burgos–Sombra example.

### 2.1 Proposition A1 (proved). FS-closure \(\subseteq\) globally psh (17.8.5)

**Statement.** Let \(X\) be a paracompact \(k\)-analytic space, \(L\) a line bundle, \(\lVert\cdot\rVert\) a continuous metric which is a uniform limit of FS metrics \(u_m=\frac1{m}\max_{j\in J_m}(\log|s_j|+\lambda_j)\) with \((s_j)_{j\in J_m}\subset H^0(X,L^{\otimes m})\) finite and base-point-free, \(\lambda_j\in\mathbf R\). Then \(\lVert\cdot\rVert\) is globally psh in the sense of CLD 17.8.5 (and its weights lie in \(\mathrm{CPsh}_{X,1}\)).

**Proof.** Fix \(m\), write \(N+1=\#J_m\). For \(\eta>0\) let \(M_\eta:\mathbf R^{N+1}\to\mathbf R\) be Demailly's regularized maximum ([45, lemme 5.18], quoted with properties a)–d) at CLD25 l. 25552). Define a metric on \(L^{\otimes m}\) by the weight (for any local invertible section \(t\) of \(L^{\otimes m}\))
\[ v_\eta:=\log\lVert t\rVert_\eta^{-1}=M_\eta\big(\log|s_0/t|+\lambda_0,\dots,\log|s_N/t|+\lambda_N\big). \]
Property d) of \(M_\eta\) makes this frame-independent, hence a metric. *Smoothness*: at \(x\), let \(J(x)=\{j: s_j(x)\ne0\}\ne\emptyset\) (base-point-freeness); by continuity there is a neighborhood \(U\ni x\) on which, for \(j\notin J(x)\), \(\log|s_j/t|+\lambda_j+\eta\le\max_{i\in J(x)}(\log|s_i/t|+\lambda_i)-\eta\); property c) then gives \(v_\eta=M_\eta\big((\log|s_j/t|+\lambda_j)_{j\in J(x)}\big)\) on \(U\), a smooth function of the moment \((s_j/t)_{j\in J(x)}\) of invertible functions — smooth. *Psh*: each \(\log|s_j/t|+\lambda_j\) is smooth harmonic (\(d'd''\log|f|=0\)) hence psh, \(M_\eta\) is smooth, convex, increasing in each variable, so Prop. 8.2.1 (l. 9888, level-preserving, case \(\alpha=0\)) gives \(v_\eta\) smooth psh. *Estimate*: property b) gives \(0\le v_\eta-\max_j(\cdot)\le\eta\), so \(\frac1m v_\eta\) (a smooth psh weight of a metric on \(L\), by (G3)) is within \(\eta/m\) of \(u_m\). Diagonalize using (G3)-closure under uniform limits. \(\square\)

*Remarks.* (a) This transplants CLD's own proof of 17.8.6 from \(\mathbf P^n\) to arbitrary section families and real weights; nothing new is used. (b) Consequently 17.8.7 extends: any metric in the FS-closure — in particular any uniform limit of semiample formal metrics and of their real rescalings — is globally psh. (c) Combined with quantization theorems (§2.3), this is the *only* currently available bridge into the 17.8.5-cone.

### 2.2 Route (i): Richberg gluing — two recorded failure points

Inventory of the complex Richberg toolkit in the CLD calculus:

1. **Regularized max: EXISTS.** \(M_\eta\) composed with smooth psh is smooth psh, level-preserving (Prop. 8.2.1); max/min of pl stay pl (Lemme 12.5.3, l. 17541).
2. **Smooth partitions of unity: EXIST** (paracompact case; CLD25 App. A.2, l. 29106–29126, and l. 7120) — but, as in complex analysis, they do not preserve psh-ness; they play no role in Richberg proper.
3. **Local smooth psh approximants: OPEN.** First failure point. The complex proof starts from convolution: every psh function is locally a decreasing limit of smooth psh. The CLD substitute would be: *every continuous CLD-psh function lies in \(\mathrm{CPsh}_{X,1}\)*. This is precisely the (open) level-collapse of Rem. 8.1.6. **FIRST GENUINELY UNSUPPORTED IMPLICATION of route (i):** "\(u\in\mathrm{CPsh}_X \Rightarrow u\in \mathrm{CPsh}_{X,1}\)". No proof; no counterexample; CLD state all known examples are level 1.
4. **Strict positivity reserves: STRUCTURALLY ABSENT.** Second failure point, independent of the first.

**Lemma A (rigid-point flatness; proved).** Let \(X\) be a \(k\)-analytic space, good at a rigid point \(x\) (\([\mathscr H(x):k]<\infty\)). Every CLD-smooth function is constant on a neighborhood of \(x\); every smooth \((p,q)\)-form with \(p+q\ge1\) vanishes identically on a neighborhood of \(x\).

*Proof.* Smooth functions are locally \(\varphi\circ(\log|f_1|,\dots,\log|f_n|)\) with \(f_i\) invertible near \(x\) (CLD25 ch. 3, 3.1.7 framework), so it suffices to show \(|f|\) is locally constant at \(x\) for \(f\in\mathcal O_{X,x}^\times\). Let \(k'=\mathscr H(x)\), a finite extension with its unique extended absolute value. The base-change \(\pi:X_{k'}\to X\) (on an affinoid neighborhood) is finite and flat, hence open [Berkovich, *Étale cohomology*, = CLD25 bib. [9], 3.2.7: quasi-finite flat morphisms are open — **recalled, standard**]. The point \(x\) lifts to a \(k'\)-rational point \(y\); with \(a:=f(y)\in k'^\times\), the open set \(W=\{|f_{k'}-a|<|a|\}\) contains \(y\) and \(|f_{k'}|\equiv|a|\) on \(W\) (ultrametric). Then \(\pi(W)\) is an open neighborhood of \(x\) on which \(|f|\equiv|a|\). Forms: locally pulled back along the tropicalization moment, which is constant near \(x\). \(\square\)

**Consequences.** On a strict space of dimension \(\ge1\) over nontrivially valued \(k\), rigid points are dense; hence: *no smooth strictly positive \((1,1)\)-form exists* (no CLD analogue of a Kähler reference form \(\omega\)); the curvature of any smooth psh \(v\) is, at each point, degenerate transverse to the local moment of \(v\). The complex Richberg seam-forcing step — replace \(v_j\) by \(v_j-\delta\chi_j\) with \(\chi_j\) a cutoff vanishing on \(W_j\) and \(\ge c>0\) near \(\partial U_j\), psh-ness preserved because \(d'd''v_j\ge\varepsilon\omega\gg\delta\,|d'd''\chi_j|\) — has **no CLD substitute**: there is no \(\omega\), and no pointwise form-inequality between \(d'd''v_j\) and \(d'd''\chi_j\) can be extracted from \(C^0\)-approximation data. Recorded failure: the implication "\(v_j\) smooth psh close to \(u\), \(\chi_j\) smooth cutoff \(\Rightarrow\) \(v_j-\delta\chi_j\) psh for small \(\delta\)" is false in general and unfixable uniformly.

**Restricted locus where Richberg-type gluing does work.** If all local approximants and cutoffs are tropicalized by a *common* moment family near the seams — e.g. weights of the form (pullback along a fixed pl G-smooth \(\tau:X\to\mathbf R^n\) or a fixed skeleton) — then patching happens in \(\mathbf R^n\) where classical convex gluing applies, and Cor. 18.8.9 (l. 27980: \(\tau^*u\) psh for \(\tau\) strictly pl harmonic, \(u\) convex continuous) converts the result back. This is exactly the mechanism of 17.8.6 (single global family \(\log|x_i|\)) and of the abelian case §19.2 (l. 28810). **Warning (route (iii) killed):** one cannot reduce a general metric to its skeletal retraction: the Burgos Gil–Sombra appendix to gjkm19 exhibits a toric surface and a semipositive metric whose retraction to a skeleton is *not* semipositive (gjkm19, ll. 51–58 of abstract and Appendix). So the restricted locus is genuinely restrictive.

### 2.3 Route (ii): envelopes/quantization — conditional reduction

Let \(X=Y^{\mathrm{an}}\), \(Y\) projective, \(L\) ample, \(\varphi\) a continuous metric with CLD-psh weights. Define the Zhang envelope \(P(\varphi)\) (gjkm19, (1.2), file l. 162) and level-\(m\) FS envelopes \(P_m(\varphi)=\frac1m\sup\{\text{FS weights from }H^0(X,L^{\otimes m})\text{-families}\le m\varphi\}\).

Known bricks (with exact hypotheses; all in the *Zhang* cone):
* **(H1) Continuity of the envelope** \(P(\varphi)\): curves, any complete \(k\), \(L\) ample (gjkm19 Thm 1.1); \(k\) discretely valued, residue char 0, \(X\) smooth [BFJ, JAMS 28 (2015), JAG 25 (2016) = CLD25 bib. [33],[34] — **recalled**, cited but not contained in local refs]; equichar \(p>0\), \(X\) smooth of geometric origin from a \(d\)-dim family over perfect \(k_0\), assuming resolution in dim \(d+n\) (gjkm19 Thm 1.4; unconditional for such surfaces, via Cossart–Piltant).
* **(Q) Quantization** \(P_m(\varphi)\to P(\varphi)\) uniformly (\(L\) ample): via orthogonality + multiplier/test ideals under the same hypotheses (gjkm19 §§7–9; [BFJ]; Boucksom–Eriksson, Adv. Math. 378 (2021) = CLD25 bib. [30] — **recalled** for the general density-of-FS statement; curves via Thuillier).
* **(A1)** (proved above): uniform FS limits are globally psh.

**Conditional Reduction A3.** Assume (H1) and (Q) hold for \((k,X,L)\). Then: *Question A holds for \((X,L)\) iff every continuous metric \(\varphi\) with CLD-psh weights satisfies \(\varphi=P(\varphi)\).* Indeed \(\Leftarrow\): \(\varphi=P(\varphi)=\lim P_m(\varphi)\) uniformly, each \(P_m\) an FS envelope, and sup's of FS families are again uniform FS limits; apply A1. \(\Rightarrow\): globally psh \(\Rightarrow\) weights level \(\le1\) and, on the semiample/FS side of every known comparison, \(\varphi\le P(\varphi)\) forces equality since \(P(\varphi)\le\varphi\) always. (The forward direction as stated uses that smooth psh metrics on ample \(L\) are dominated by their envelopes, i.e. smooth psh \(\Rightarrow\) Zhang — see the caveat in §0.3; strictly, A3 is the equivalence *modulo* that comparison, which is exactly the same open link.)

**The single open link (H2):** "\(\varphi\) continuous, weights CLD-psh \(\Rightarrow\varphi\le P(\varphi)\)", i.e. the CLD-local cone does not exceed the Zhang cone. **Status:** TRUE on the pl-entire locus — this is Cor. 18.8.8: CLD-psh pl-entire \(\Rightarrow\) nef residual bundles \(\Rightarrow\) (Ex. 18.8.10 b)) nef formal model \(\Rightarrow\) Zhang-semipositive \(\Rightarrow\) \(\varphi=P(\varphi)\). OPEN beyond pl. The natural tool — a domination/maximum principle for CLD-psh functions — is explicitly lacking: CLD25 0.3.5 (l. 658–664): "*Nous ne savons pas si un tel principe vaut pour les fonctions psh de ce texte*"; [GR25, abstract-level] Thm 1.7 proves a maximum principle for *piecewise-smooth* CLD-psh functions only. **FIRST GENUINELY UNSUPPORTED IMPLICATION of route (ii): (H2) beyond the pl locus.**

### 2.4 The nef/semiample sub-gap (recorded failed attempt)

Even for a *nef formal* metric on ample \(L\) (locally psh by 17.8.4/18.8.8), CLD-internal global psh-ness is unproven: the ε-perturbation of Prop. 17.8.4's proof (l. 25514–25533) works locally because the ample twist \(M'\) is realized on the *trivial* bundle \(\mathcal O_U\) (weight \(h\) a function); globally, dividing the semiample metric of \(\mathfrak L^{\otimes n}\otimes\mathfrak A\) by any metric on \(\mathfrak A\)'s generic fibre subtracts a curvature term with no pointwise domination available (only \(C^0\) data). Failure recorded: "\(C^0\)-closeness of metrics \(\Rightarrow\) form-level curvature comparison" is unsupported. The nef case therefore also routes through (Q) (Zhang-type section lifting), i.e. is conditional on quantization — *not* CLD-internal. On toric models and on curves it is classical.

### 2.5 Question A: self-adversarial audit

* **\(k\) not algebraically closed:** A1, Lemma A, 18.8.8, gjkm19 Thm 1.1 hold; [BFJ] bricks assume discretely valued, residue char 0 (their descent to non-closed \(k\) is standard but recalled).
* **Positive residue characteristic:** (H1),(Q) known only in the gjkm19 geometric-origin+resolution regime; A's conditional route inherits this. Nothing in §2.1–2.2 is characteristic-sensitive.
* **Non-smooth \(X\):** 17.8.9 and A1 need no smoothness; (H1)/(Q) do. Cor. 18.8.8 needs \(X\) boundaryless (proper \(\Rightarrow\) OK).
* **Numerically trivial or torsion \(L\):** any psh metric has \(c_1\) positive of total intersection mass 0; on the Tate curve the cubist metric of a degree-0 bundle has weight affine (real slope) along the skeleton — *smooth* (real slopes are CLD-smooth: \(\varphi(t)=at+c\), \(a\in\mathbf R\)) and harmonic, hence globally psh trivially. A holds here. Torsion \(L\): reduce by finite pullback (8.1.5) + descent of uniform approximants — unchecked in detail, flagged.
* **Irrational slopes:** \(\mathbf R\)-pl metrics are not covered by the residual-bundle calculus (17.3 needs *entire*); but they are CLD-smooth-approximable along fixed skeleta and lie in the FS-closure when their \(\mathbf Q\)-approximations do; the collapse 18.8.8 for them is obtained only by \(\mathbf Q\)-perturbation, gap flagged.
* **Trivially valued \(k\):** outside packet scope; note 17.7.5 fails there.

### 2.6 Question A: boundary examples

* **\(\mathbf P^1\):** local CLD-psh = subharmonicity-type conditions on the tree; expected equal to Thuillier's cone, but the comparison CLD\(\leftrightarrow\)Thuillier is *not* in the examined sources ([GR25, abstract-level] builds on curves/Thuillier for *their* notion; CLD 0.3.5 stresses the notions differ). Granting it, A on curves follows from gjkm19 Thm 1.1 + curve quantization + A1. Even \(\mathbf P^1\) thus assembles only from external bricks; no CLD-internal proof exists. Disposition for curves: expected YES, modulo the flagged comparison.
* **Tate elliptic curve:** cubist metrics globally psh (§2.5); nef-model metrics on degree-\(d>0\) bundles: FS-quantization concrete via theta functions; A expected YES.
* **Toric surfaces:** the Burgos Gil–Sombra appendix (gjkm19) blocks skeletal reduction (§2.2); on the other hand toric metrics invariant under the torus skeleton with convex support functions lie in the FS-closure (classical toric semiampleness), where A holds by A1.

### 2.7 Question A: disposition

**OPEN-AFTER-ATTEMPT** in general, with: **CANDIDATE-PROPOSITION A1** (proved: FS-closure \(\subseteq\) globally psh; includes real-weight FS and semiample formal limits); **CANDIDATE-PROPOSITION A2** (= CLD 18.8.8 read as a collapse: on the pl-entire locus of a boundaryless space, local CLD-psh = positive current = nef-residual, and (H2) holds there); **CONDITIONAL-REDUCTION A3** (for ample \(L\) under (H1)+(Q): A \(\Leftrightarrow\) (H2), the CLD-vs-Zhang cone comparison, itself open beyond pl); Richberg route: two recorded failure points ((O1) level collapse open — Rem. 8.1.6; (O2) Lemma A: no strict positivity reserves), workable only on common-tropicalization loci.

---

## 3. Question B — extension of 17.8.9 to formal models with projective special fibre

Setting: \(k\) nontrivially valued (discretely valued where stated), \(X\) proper strict \(k\)-analytic, admitting a formal model \(\mathfrak X_0\) (flat, tfp, B.1.1 l. 29544) with \(\mathfrak X_{0,s}\) projective over \(\tilde k\). Question (Rem. 17.8.10, l. 25621, after Scholze [121]): is every parlinear metric on every line bundle \(L\) on \(X\) globally dpsh?

### 3.1 Dissection of the proof of Cor. 17.8.9 (l. 25607–25615)

1. **(P1)** "\(X\) possède un modèle formel qui est projectif; on peut supposer \(\mathfrak X\) projectif sur \(k^\circ\)" — uses algebraicity of \(X\) (closure in \(\mathbf P^N_{k^\circ}\)) + Raynaud domination (App. B.1.3, l. 29557).
2. **(P2)** GFGA ([1] Abbes, th. 2.13.8) algebraizes \(\mathfrak L\) on the projective \(\mathfrak X\).
3. **(P3)** On projective \(\mathfrak X/k^\circ\): \(\mathfrak L\simeq\mathfrak L_1\otimes\mathfrak L_2^{-1}\) with \(\mathfrak L_i\) ample. (Micro-flag: for non-noetherian \(k^\circ\) this needs noetherian approximation — standard, unremarked in CLD25.)
4. **(P4)** Ample \(\Rightarrow\) semiample \(\Rightarrow\) Cor. 17.8.7 \(\Rightarrow\) each \(\overline L_i\) globally psh; isometry \(\overline L\simeq\overline L_1\otimes\overline L_2^{-1}\).

### 3.2 What survives (proved lemmas)

**Lemma B1 (cofinality; proved).** If one formal model \(\mathfrak X_0\) has projective special fibre, then formal models with projective special fibre are cofinal among all formal models of \(X\); consequently every strictly entire pl metric on any \(L\) is induced by a model \((\mathfrak X,\mathfrak L)\) with \(\mathfrak X_s\) projective.
*Proof.* Any model \(\mathfrak X_1\) is dominated by an admissible blow-up \(\mathfrak X_2\to\mathfrak X_0\) (Raynaud; B.1.3/B.1.4 machinery, l. 29557 ff., and [19, 8.2, 8.4] as cited there). An admissible blow-up is the completed \(\operatorname{Proj}\) of the Rees algebra of a coherent open ideal, hence a projective morphism; \(\operatorname{Proj}\) commutes with the base change \(\otimes\tilde k\), so \(\mathfrak X_{2,s}\to\mathfrak X_{0,s}\) is projective and \(\mathfrak X_{2,s}\) is projective over \(\tilde k\). Metrics: pull back \((\mathfrak X_1,\mathfrak L_1)\); local freeness after a further admissible blow-up by Thm B.1.8 b) (l. 29655), which preserves projectivity of the special fibre by the same argument. \(\square\)
So **(P1) survives in the weakened form** "may assume \(\mathfrak X_s\) projective". **(P2) is not available and not needed** if one works with \(\mathfrak L\) directly on \(\mathfrak X\).

**Lemma B2 (polarized case; proved for \(k\) discretely valued).** Let \(k\) be discretely valued, \(\mathfrak X\) a formal model with \(\mathfrak X_s\) projective, and suppose \(\mathfrak X\) carries a line bundle \(\mathfrak A\) with \(\mathfrak A_s\) ample (**hypothesis (B-H1)**). Then for every line bundle \(\mathfrak L\) on \(\mathfrak X\) the formal metric of \(\mathfrak L_\eta\) is globally dpsh.
*Proof.* Choose \(n\) with \((\mathfrak A^{\otimes n}\otimes\mathfrak L)_s\) globally generated, ample, and \(H^1(\mathfrak X_s,(\mathfrak A^{\otimes n}\otimes\mathfrak L)_s)=0\) (Serre on the projective \(\mathfrak X_s\)); same for \(\mathfrak A^{\otimes n}\). Write \(\mathfrak M\) for either bundle. Since \(\mathfrak X\) is \(\pi\)-adically flat, \(\pi^m\mathcal O/\pi^{m+1}\mathcal O\simeq\mathcal O_{\mathfrak X_s}\), so the obstruction to lifting a section through \(\mathfrak X_{m}\to\mathfrak X_{m+1}\) lies in \(H^1(\mathfrak X_s,\mathfrak M_s)=0\); by completeness \(H^0(\mathfrak X,\mathfrak M)\to H^0(\mathfrak X_s,\mathfrak M_s)\) is onto. Finitely many lifted sections generate mod \(\pi\), hence generate (coherent cokernel with zero reduction vanishes), defining \(p:\mathfrak X\to\widehat{\mathbf P}^N_{k^\circ}\) with \(p^*O(1)\simeq\mathfrak M\): \(\mathfrak M\) is semiample, so its formal metric is globally psh (Cor. 17.8.7). Then \(\overline{\mathfrak L_\eta}=\overline{(\mathfrak A^n\mathfrak L)_\eta}\otimes\overline{(\mathfrak A^n)_\eta}^{-1}\) is an isometry of the given formal metric with a difference of globally psh metrics. \(\square\)

### 3.3 The genuine obstruction

**Proposition B3 (collapse of the polarized case; proved modulo recalled algebraization).** For \(k\) discretely valued, (B-H1) on some model implies \(X\) is the analytification of a projective \(k\)-variety. Indeed \((\mathfrak X,\mathfrak A)\) with \(\mathfrak A_s\) ample algebraizes to a projective scheme over \(k^\circ\) [EGA III 5.4.5, Grothendieck existence over the complete noetherian \(k^\circ\) — **recalled**, not in local refs]. Hence Lemma B2 adds nothing beyond 17.8.9: **within the known proof architecture, Question B's hypothesis is either upgraded to (B-H1) — which forces algebraicity — or the ample-decomposition step (P3) has no substitute.**

**FIRST GENUINELY UNSUPPORTED IMPLICATION for B:** "\(\mathfrak X_s\) projective \(\Rightarrow\) some admissible blow-up \(\mathfrak X'\) carries \(\mathfrak A'\) with \(\mathfrak A'_s\) ample". This is a *lifting* problem: an ample class on \(\mathfrak X_s\) must lift through the thickenings \(\mathfrak X_m\); the step-\(m\) obstruction lies in \(H^2(\mathfrak X_s,\mathcal O_{\mathfrak X_s})\otimes(\pi^m)/(\pi^{m+1})\). This is exactly the Kähler-type phenomenon behind Scholze's analogy ([121]) and CLD's own Perspective 0.4.1 (l. 674: "Qu'est-ce qu'une forme de Kähler dans notre contexte…"). For \(\mathfrak X_s\) a projective K3 or abelian surface, \(h^{0,2}\ne0\) and generic formal deformations kill every polarization.

### 3.4 COUNTEREXAMPLE-CANDIDATE B4

Take \(k=\mathbf C((t))\), \(S\) a complex projective K3, \(\mathfrak X_0\) a formal deformation of \(S\) over \(k^\circ=\mathbf C[[t]]\) whose Kodaira–Spencer direction kills all of \(\mathrm{NS}(S)\) (possible since the period map is submersive and \(h^{0,2}(S)=1\)); \(X:=\mathfrak X_{0,\eta}\), a proper strict connected \(k\)-analytic space with a formal model with projective special fibre. Let \(u\) be any nonconstant pl function on \(X\) (e.g. the metric quotient of a vertical admissible blow-up: exists by B.1.3 + 12.5 density, l. 25311–25324), and \(\overline{\mathcal O}_u\) the parlinear metric \(e^{-u}|\cdot|\) on \(\mathcal O_X\).
*Claim:* \(\overline{\mathcal O}_u\) is **not** globally dpsh, refuting B. *Argument:* a dpsh presentation needs \(L_1\simeq L_2\in\operatorname{Pic}(X)\) with globally psh metrics and \(u=\varphi_1-\varphi_2+c\).
(c1) **[gap — plausibility only]** \(\operatorname{Pic}(X)\) is generated by generic fibres of vertical classes, hence trivial: line bundles on \(X\) extend to models (B.1.8); on a model \(\mathfrak X'\to\mathfrak X_0\), twisting by exceptional vertical divisors reduces the special-fibre class to a pullback from \(S\), which does not lift by the Noether–Lefschetz choice; the required descent of this argument through admissible blow-ups (behavior of \(H^2(\mathcal O)\)-obstructions under \(p_{m*}\)) is *not verified here*; the existence of such non-algebraic proper rigid K3-type spaces is folklore-standard but no verifiable citation is in the local refs.
(c2) **[gap — abstract-level citation]** Smooth psh functions on the proper connected \(X\) are constant: by [GR25, abstract-level] Thm 1.7 (maximum principle for piecewise-smooth CLD-psh: local max \(\Rightarrow\) locally constant; \(\partial X=\emptyset\)), the set where a smooth psh \(v\) attains \(\max v\) is open and closed. Then globally psh metrics on \(\mathcal O_X\) are uniform limits of \(e^{-v_n}|\cdot|\), \(v_n\) smooth psh \(=\) constants, so are the metrics \(e^{-c}|\cdot|\); with \(\operatorname{Pic}(X)=0\) and \(|\mathcal O(X)^\times|\) constant (Kiehl finiteness, unique extension of the absolute value), every dpsh function is constant — contradiction with \(u\) nonconstant. \(\square\) (modulo (c1),(c2))

### 3.5 Question B: audit and non-discrete caveats

* **Non-discretely valued \(k\):** Lemma B1 holds verbatim. Lemma B2's grading argument and Prop. B3's algebraization need adaptation (graded pieces \(\ne\mathcal O_{\mathfrak X_s}\); Grothendieck existence over general \(k^\circ\): Fujiwara–Kato *Foundations of Rigid Geometry* — **recalled**, unverified); statements above are asserted only for discretely valued \(k\); general rank-1 case: OPEN-technical.
* **General parlinear vs formal metrics:** as in §0.4, the printed 17.8.9 covers the strictly entire case; the same restriction is inherited by Lemma B2 and by B4 (where \(u\) pl strictly entire suffices).
* **Non-smooth \(\mathfrak X_s\), positive residue characteristic:** Lemmas B1–B2 are insensitive (only projectivity of \(\mathfrak X_s\) is used); B4's deformation input is residue-char-0 for convenience; K3s over \(\mathbf F_p[[t]]\)-type bases would need care (not attempted).
* **Curves:** every proper strict analytic curve with a formal model with projective special fibre *is* algebraic (1-dimensional proper rigid spaces are projective — recalled, standard), so B is TRUE for curves via 17.8.9 itself: the question is genuinely \(\ge2\)-dimensional.
* **Consistency check on the algebraic side:** on projective \(X\), B4's mechanism cannot run: \(u\) pl is dpsh via two metrics on the *same ample* \(A\) (17.8.9 with vertical twists), matching the fact that \(\operatorname{Pic}\) is large. The dichotomy is exactly (B-H1).

### 3.6 Question B: disposition

**COUNTEREXAMPLE-CANDIDATE** (B4; gaps (c1),(c2) explicitly recorded) **+ CONDITIONAL-REDUCTION** (Lemmas B1–B2, Prop. B3: for discretely valued \(k\), the 17.8.9-architecture extends *iff* a polarization lifts to some model, which forces \(X\) algebraic-projective; the obstruction is the \(H^2(\mathfrak X_s,\mathcal O)\)-lifting class — the precise non-archimedean "Kähler" gap Scholze's analogy predicts). B as literally asked is **expected FALSE**; the corrected question is: *which* positivity datum on \(X\) (a "non-archimedean Kähler structure") replaces the ample decomposition — beyond scope.

---

## 4. Dispositions (summary)

| Sub-question | Disposition |
|---|---|
| A, general \(L\), general continuous CLD-psh metric | **OPEN-AFTER-ATTEMPT** (routes (i)–(iii) mapped; first unsupported implications recorded: level collapse \(\mathrm{CPsh}=\mathrm{CPsh}_1\); (H2) CLD\(\subseteq\)Zhang beyond pl; no strict positivity reserves — Lemma A) |
| A, FS-closure (incl. semiample formal limits, real weights) | **CANDIDATE-PROPOSITION A1** (proved) |
| A, pl-entire locus: collapse of local notions | **LITERATURE-RESOLVED** internally to CLD25 (Cor. 18.8.8 + Ex. 18.8.10) |
| A, \(L\) ample under (H1)+(Q) | **CONDITIONAL-REDUCTION A3** to (H2) |
| A, curves / Tate curve / toric-invariant | expected YES; modulo flagged CLD\(\leftrightarrow\)Thuillier comparison (curves) — **CONDITIONAL** |
| B, polarized model, \(k\) discrete | **CANDIDATE-PROPOSITION** (Lemma B2, proved) — but collapses to the algebraic case (Prop. B3) |
| B, as stated (projective special fibre only) | **COUNTEREXAMPLE-CANDIDATE B4** (gaps (c1),(c2)) + obstruction isolated (\(H^2(\mathcal O)\)-lifting) |

Integrity notes: [GR25] used at abstract level only; [BFJ], [BE21], EGA III 5.4.5, Fujiwara–Kato, Berkovich 3.2.7 are recalled from memory and so flagged at each use; no priority claims; the textual anomalies in CLD25 §17.8 (17.8.9 statement/proof mismatch, "psh-approchable" drift) are observations about the source, not criticisms relied upon.

---

## Proposed ledger lines

* **[CANDIDATE-PROPOSITION]** (A1) On any paracompact \(k\)-analytic space, every continuous metric in the Fubini–Study closure — uniform limits of \(\frac1m\max_j(\log|s_j|+\lambda_j)\) over finite base-point-free families \(s_j\in H^0(X,L^{\otimes m})\), \(\lambda_j\in\mathbf R\) — is globally psh in the sense of CLD 17.8.5, with smooth psh approximants given by Demailly's regularized maximum via CLD Prop. 8.2.1; in particular Cor. 17.8.7 extends to all real-weight semiample-formal limits. (Complete proof in dossier §2.1.)
* **[CANDIDATE-PROPOSITION]** (G2) A globally psh metric in the sense of 17.8.5 has weights in \(\mathrm{CPsh}_{X,1}\); hence CLD's Question A implies the level-1 collapse for continuous psh metric weights, and a single continuous psh metric of hierarchy level \(\ge2\) on a projective variety would refute A. (Proof in §0.2.)
* **[CANDIDATE-LEMMA]** (Lemma A) CLD-smooth functions are locally constant near rigid points (good locus); hence no strictly positive smooth \((1,1)\)-forms exist on strict spaces of positive dimension and the Richberg strict-positivity-reserve mechanism has no CLD analogue; the CLD calculus does possess the other two Richberg ingredients (regularized max via 8.2.1; smooth partitions of unity via App. A.2). (Proof in §2.2, modulo the recalled openness of finite flat base-change maps.)
* **[CONDITIONAL-REDUCTION]** (A3) For \(L\) ample and \((k,X)\) within the known envelope regimes (curves/any \(k\); discretely valued residue char 0, \(X\) smooth; equichar \(p\) geometric origin + resolution), Question A is equivalent to the cone comparison (H2): every continuous CLD-psh metric equals its Zhang envelope; (H2) holds on the pl-entire locus by CLD Cor. 18.8.8, and is open beyond it — the missing tool being a domination/maximum principle for CLD-psh functions (CLD 0.3.5).
* **[CANDIDATE-LEMMA]** (B1) If a proper strict \(X\) admits one formal model with projective special fibre, such models are cofinal (admissible blow-ups are projective on special fibres), so every strictly entire pl metric is induced by a model with projective special fibre. (Proof in §3.2.)
* **[CONDITIONAL-REDUCTION]** (B2/B3) For discretely valued \(k\): if some model carries a line bundle with ample special-fibre restriction, every formal metric on \(X\) is globally dpsh (proved by section-lifting through thickenings); but this hypothesis algebraizes \(X\) (Grothendieck existence, recalled), so the extension of 17.8.9 asked in Rem. 17.8.10 is exactly obstructed by the lifting of a polarization, with obstruction classes in \(H^2(\mathfrak X_s,\mathcal O_{\mathfrak X_s})\).
* **[COUNTEREXAMPLE-CANDIDATE]** (B4) For \(X\) the generic fibre of a polarization-killing formal deformation of a projective K3 over \(\mathbf C[[t]]\): granting (c1) triviality of \(\operatorname{Pic}(X)\) modulo vertical classes and (c2) the Gubler–Rabinoff (arXiv:2503.05513) maximum principle for piecewise-smooth CLD-psh functions, any nonconstant pl function yields a parlinear metric on \(\mathcal O_X\) that is not globally dpsh — refuting the extension of Cor. 17.8.9 to formal models with projective special fibre.
* **[CANDIDATE-OBSERVATION]** The phrasing of ch71 Problem `frontier-cld-global-metric` ("globally psh in the Fubini–Study or nef-model sense") is not known to define the same cone as CLD 17.8.5: proved inclusions are FS-closure \(\subseteq\) 17.8.5-cone and FS-closure \(\subseteq\) Zhang-closure; the comparison between the 17.8.5-cone and the Zhang-closure is open in both directions (even for smooth psh metrics).
