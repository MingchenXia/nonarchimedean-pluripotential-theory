# Independent mathematical review of precise conditional partial scope


# UNCHANGED unreviewed new deduction; no grant

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


# UNCHANGED unreviewed new deduction; no grant

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


# Exact original P16.1 and unchanged full family

{
  "problem": "Original P16.1:\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nComplete unchanged mathematical family:\n\n10     The general non-Archimedean Monge–Ampère equation\nActive items: P16.1, P16.2, P16.3, P16.4, P16.5, P16.6, P16.7. Status: Open in the\nresidual scope.\n\n10.1    Atomic targets\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nP16.2 (T5): Proper nonprojective algebraizable equation theories\nConstruct an appropriate replacement positivity datum and the associated psh, ﬁnite-energy,\ncomparison and equation theory on proper nonprojective algebraizable spaces. A proper\nalgebraic scheme with an ample line bundle is already projective, so retaining that datum\nwhile dropping projectivity is not a new case.\n\nP16.3 (T5): Finite-energy equations in positive residue characteristic\nConstruct the required ﬁnite-energy operator and prove existence and uniqueness when the\noriginal residue-characteristic restriction is removed. Replace the resolution, model-regularity\nand envelope inputs wherever they are used rather than merely changing the standing ﬁeld\nhypothesis.\n\nP16.4 (T4): Finite-energy equations over arbitrary complete valued ﬁelds\nExtend the operator and existence theorem to nondiscrete valuations and arbitrary complete\nnon-Archimedean ﬁelds outside the established invariant-toric, skeleton-supported endpoint.\nA deﬁnition of the ﬁnite-energy space alone does not establish the operator or the equation.\n\nP16.5 (T5): Finite-energy equations for nonample positivity classes\nExtend the equation theory to big or pseudoeﬀective nonample classes, specifying the psh cone,\nreference singularity type, energy and total mass. At zero volume, the existing probability\nnormalization must be replaced rather than retained unchanged.\n\nP16.6 (T4): Arbitrary-support ﬁnite-energy measures\nProve the operator and existence-and-uniqueness theorem for arbitrary ﬁnite-energy measure\nsupport beyond the known toric skeletal regime. Measures must satisfy the correct mass and\nenergy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine\nMonge–Ampère measure by another inverse measure construction.\n\nP16.7 (T5): Finite-energy equations on nonalgebraizable analytic spaces\nConstruct the ﬁnite-energy operator and its existence-and-uniqueness theory on genuinely\nnonalgebraizable analytic spaces, with an explicit positivity datum and the necessary com-\npactness, envelope and comparison replacements.\n\n\n\n\n                                              73\n\n10.2    What constitutes a solution\nFor each axis, state the retained hypotheses and construct the ﬁnite-energy operator together\nwith the corresponding existence-and-uniqueness theorem. Specify the measure mass and\nﬁnite-energy condition, uniqueness modulo constants and the replacement inputs for com-\npactness, envelopes, energy diﬀerentiation and comparison. An endpoint solving a special\ntoric measure class does not remove a general axis.\n\n10.3    Full statement and detailed state of the art\nProblem 10.1. Extend the ﬁnite-energy existence and uniqueness theory for the NA Monge–\nAmpère equation beyond the currently proved combinations of smoothness, projectivity,\nresidue characteristic, valuation, positivity class, support, and algebraizability hypotheses.\n\n    This is not one yes-or-no assertion. Positive characteristic, singular or unibranch varieties,\nnondiscrete valuations, big classes, arbitrary support, and nonalgebraizable analytic spaces\nrequire diﬀerent inputs. The known variational proofs use compactness, envelope regularity,\ndiﬀerentiability of energy, and a comparison principle; deleting a geometric hypothesis is valid\nonly after replacing every place where it enters. The relevant positive results and their distinct\ndomains are surveyed in Book Chapter 28, Book Chapter 29.\n    The projectivity axis has one logical constraint. A proper algebraic K-scheme endowed\nwith an ample line bundle is already projective over K [Stacksb, Tag 0B5N]. Thus P16.2\ncannot mean that one retains the BFJ line-bundle polarization L while simply deleting the\nword “projective.” A nonprojective proper algebraizable extension must ﬁrst replace that\npositivity datum—and then construct the corresponding psh, ﬁnite-energy, and comparison\ntheory—rather than merely rerun the original argument. No canonical replacement with the\nrequired equation theory is asserted here.\n    One exact source-stated axis is especially clean. Pille–Schneider observes that the ﬁnite-\nenergy space can be deﬁned over an arbitrary non-Archimedean ﬁeld, but that the extension of\nthe Monge–Ampère operator is not known there in general; the discretely valued characteristic-\nzero and trivially valued cases are the established endpoints [PS23, Remark 4.4]. This should\nbe solved before bundling all remaining axes into a single theorem.\n\nProposition 10.1 (Arbitrary-ﬁeld invariant toric skeletal endpoint). Let K be a complete\nnontrivially valued non-Archimedean ﬁeld, XΣ a proper toric K-variety, and L an ample toric\nline bundle. If µ is a positive Radon measure on XΣan , is supported on the canonical skeleton\nNΣ , gives zero mass to NΣ \\NR , and has total mass degL (XΣ ), then there is a toric continuous\nsingular psh metric on L whose Monge–Ampère measure is µ. It is unique up to multiplication\nof the metric by a positive constant.\n\n    Thus nondiscreteness and the arbitrary complete ground ﬁeld cause no obstruction in\nthis invariant toric, skeleton-supported range. Here “continuous singular” has the source’s\nextended-valued meaning: local weights are continuous into R ∪ {−∞}, as in [BGGJK25,\n§5.3.1]. It does not imply ﬁnite real-valued weights or ﬁnite energy. This is not an arbitrary-\nﬁeld ﬁnite-energy theorem in the BFJ sense: the result permits a singular potential, requires\ntorus invariance and skeletal support, and does not construct the general extended Monge–\nAmpère operator. In particular, P16.4 and P16.6 retain the respectively nonskeletal and\nnoninvariant ﬁnite-energy residual scopes.\n    There is also a distinct, nonproper algebraic endpoint. Let n > d ≥ 1, let X be a smooth\nprojective Fano complex variety of dimension n, and let D be a reduced simple-normal-crossing\nanticanonical divisor whose dual complex is the standard (d−1)-simplex. For the aﬃne Calabi–\nYau complement X = X \\ D, Wang’s Theorem A constructs a continuous non-Archimedean\npsh function on X an , over the trivially valued ﬁeld C, whose local Monge–Ampère measure\n\n                                               74\n\nis the canonical Lebesgue measure on the essential skeleton [Wan25]. The source is a version-\none preprint and uses a local CLD/tropical–convex construction. In particular, it neither\nconstructs the BFJ ﬁnite-energy operator nor treats arbitrary measures or arbitrary aﬃne\nvarieties. Since X is aﬃne and hence not proper, this endpoint does not answer P16.2; it\nonly records a special nonprojective algebraic solution after the properness requirement is\nalso dropped.\n    There is a separate ﬁnite-atomic inverse statement which must not be called a ﬁnite-energy\nMonge–Ampère theorem. Under its standing assumptions that K is maximally complete and\n|K × | = R>0 , Fang ﬁxes an irreducible projective K-variety with an ample line bundle and a\nﬁnite set of graded birational points on its aﬃne cone. For every probability vector on that\nﬁnite set, the source constructs a Shilov-ﬁnite, possibly singular metric having the prescribed\nequidistribution measure [Fan25, Proposition 4.8]. The source itself says that comparing this\nBanach-algebra measure with the genuine Monge–Ampère measure requires the separate con-\ntinuity property of an envelope metric. Thus it supplies neither a continuous semipositive\nsolution nor the BFJ ﬁnite-energy operator for the prescribed atomic measure, and does not\nnarrow P16.6.\n    There is also a resolved negative regularity chronology. The ﬁrst skeletal-factorization\nquestion of Gubler–Jell–Künnemann–Martin already fails on their toric surface [GJKM19,\nAppendix A]. Boucksom–Jonsson then construct a ﬁnite atomic Monge–Ampère measure sup-\nported on a dual complex whose solution is invariant under no retraction attached to any\nSNC model; they also construct a divisorial Green function that is not Q-PL [BJ24b, Theo-\nrems A and B]. Hence support on a dual complex does not imply factorization through some\nreﬁned skeleton. This is a theorem-level obstruction to a proof strategy, not an open regularity\nexpectation.\n    The Rethlas programme treats each axis separately and ﬁrst searches the post-2020 liter-\nature for an existing theorem. Alterations and universal homeomorphisms can address some\nalgebraic descent questions, but they do not by themselves supply multiplier ideals or dif-\nferentiability in positive characteristic. The unrestricted formulation is open; several strictly\ndelimited axes are already known.\n\n\n\n\n                                               75\n\n",
  "completionCriteria": "Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted."
}


# Primary exact coordinates and explicit reading limits

{
  "recorded_utc": "2026-10-05T10:02:16.290177+00:00",
  "proposals": [
    {
      "path": "/workspace/research/root-checks/P16.1-envelope-to-raw-equation-and-continuous-base-change-20261005-continuation89.md",
      "sha256": "49f9dde261db15a4df3e8baca0fb0afa4ffab070e8f64a89bd2b531c716943a9",
      "bytes": 13078,
      "whole_current_saved_proposal_root_read": true,
      "accepted_dependency": false
    },
    {
      "path": "/workspace/research/root-checks/P16.1-local-reference-converse-and-countable-to-arbitrary-EP-20261005-continuation90.md",
      "sha256": "6c30c2e4c8b93394864fb5b373b2565436b20e0cd140794337541513f7bccec7",
      "bytes": 12725,
      "whole_current_saved_proposal_root_read": true,
      "accepted_dependency": false
    }
  ],
  "units": [
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        1400,
        1464
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF1400-1464.txt",
      "literal_sha256": "8c3cde058ac956453efe16c92a188c5b0161a78f42890ef7e8069684ef757655",
      "bytes": 4856,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        1596,
        1735
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF1596-1735.txt",
      "literal_sha256": "f341320b03c63a0680b824b8ad5b0f8779a89cec36253de22d6af3b449ebc68d",
      "bytes": 10582,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2170,
        2295
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF2170-2295.txt",
      "literal_sha256": "051771d04bbe91b94832d09ee665620765f199dab2c009fa7709c1d014298993",
      "bytes": 9464,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2408,
        2494
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF2408-2494.txt",
      "literal_sha256": "57b9daeca55045edc34a0cad20fb9a4b992c6d96ed18c3708d387e41887bf737",
      "bytes": 6398,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2894,
        2976
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF2894-2976.txt",
      "literal_sha256": "9e9789c16e6e0105ad20368fdf05e44daabb8ecbe2cb583d8790c7662ddb1ebd",
      "bytes": 6518,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        3650,
        3735
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF3650-3735.txt",
      "literal_sha256": "004fe0971ff0d1553646bae690a7aabffed0cba7a373b8e77282c2c117a884eb",
      "bytes": 6749,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        3780,
        3840
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF3780-3840.txt",
      "literal_sha256": "061b6514a883ec8005e646d9f6bcf90b8a73b47cba970ee09ed2d7aa26ad2b7d",
      "bytes": 4561,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        3963,
        4148
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF3963-4148.txt",
      "literal_sha256": "acce77b77dfa912f7518c2b95c1ac40b0377a1a087dacd14cd07a9165aba6540",
      "bytes": 12884,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        4200,
        4288
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF4200-4288.txt",
      "literal_sha256": "5242bbea26d88e8cfb1ba396546aca6a1e9909e967cf2bec234f19b41592fa41",
      "bytes": 5525,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        4498,
        4618
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF4498-4618.txt",
      "literal_sha256": "de2e99b0274d72fe53388340cacdab4b8ec59b4d2c909382ce756af9c652eca8",
      "bytes": 9031,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        4835,
        5013
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF4835-5013.txt",
      "literal_sha256": "e5e68be0edf91417124c40346ef383153c38fcc71bfcdabd1a0bc746547a8ac0",
      "bytes": 11024,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        5100,
        5180
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF5100-5180.txt",
      "literal_sha256": "d41a06f1b36ae5f53b3db51829d1c7235b3f735371d4afa8c27ac97855f2f0d1",
      "bytes": 5323,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        5190,
        5265
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF5190-5265.txt",
      "literal_sha256": "43bb31eedb125c98cfd927ac80af113538e5a25fd1746c798fe90e0090efc43e",
      "bytes": 4902,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        5390,
        5485
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF5390-5485.txt",
      "literal_sha256": "7793b21000d502302e30c2dcf59827f04b0f913d26f8679ef52719daec5b21b3",
      "bytes": 5771,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        6070,
        6148
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF6070-6148.txt",
      "literal_sha256": "f9a75c9afb9ee98f353a9a27b0dee86b0299563980fbf37fa43831ec9cb254b9",
      "bytes": 5300,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        6302,
        6440
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BJ-1801.08229v4-LF6302-6440.txt",
      "literal_sha256": "48beafb24742b0db0d5295b4fee1781284c633159a441f642b64a505644944a6",
      "bytes": 8396,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "url": "https://arxiv.org/abs/1805.01016v3",
      "inclusive_one_based_LF": [
        2340,
        2422
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BE-1805.01016v3-LF2340-2422.txt",
      "literal_sha256": "97d1a4a90cf6807b465e649a79f8b68062962404069f7e5311bbad868c2ee0fb",
      "bytes": 6107,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "url": "https://arxiv.org/abs/1805.01016v3",
      "inclusive_one_based_LF": [
        2629,
        2808
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BE-1805.01016v3-LF2629-2808.txt",
      "literal_sha256": "20ea338f1b262a5e6974219c6142d79303184cc009ece817a5451680d9c94b37",
      "bytes": 13253,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "url": "https://arxiv.org/abs/1805.01016v3",
      "inclusive_one_based_LF": [
        3118,
        3190
      ],
      "literal_file": "/workspace/research/root-checks/continuation89-envelope-primary-read-units/BE-1805.01016v3-LF3118-3190.txt",
      "literal_sha256": "a36f2d7e5d8381a4766d4f77c8e34ab1a942de2f58526dad278606aa5175e333",
      "bytes": 5480,
      "whole_applicable_statement_and_proof_unit_root_read": true,
      "all_recursively_cited_background_proofs_root_read": false
    }
  ],
  "visual_primary_page_checks": [
    {
      "image": "/workspace/research/root-checks/continuation89-primary-page-checks/BJ-Proposition9.19-PDFpage105.png",
      "image_sha256": "635e16803970bd0c9af54ce97ffb25887471415a1b05a3d5a001787b2756c5dd",
      "primary_pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
      "primary_pdf_sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
      "one_based_pdf_page": 105,
      "root_visually_read": true
    },
    {
      "image": "/workspace/research/root-checks/continuation89-primary-page-checks/BJ-Proposition7.21-PDFpage84.png",
      "image_sha256": "428b24fcd08231d7f048130e5dde04c2c46392af773cac23ae259cf426b871ba",
      "primary_pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
      "primary_pdf_sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
      "one_based_pdf_page": 84,
      "root_visually_read": true
    }
  ],
  "live_web_bodies_root_read": [
    {
      "url": "https://stacks.math.columbia.edu/tag/033G",
      "rendered_lines": [
        24,
        31
      ]
    },
    {
      "url": "https://stacks.math.columbia.edu/tag/0CEX",
      "rendered_lines": [
        22,
        23
      ]
    },
    {
      "url": "https://stacks.math.columbia.edu/tag/0BPZ",
      "rendered_lines": [
        23,
        24
      ]
    }
  ],
  "reading_limits": "Web coordinates are rendered tool lines, not cached LF/hash pins. The two selected PDF pages were visually read; no whole-PDF reading is claimed. Whole applicable primary proof units were read, not all recursive background proofs. New applications remain unreviewed."
}


# PRIMARY exact literal unit

a test configuration X 00 dominating X and X 0 via µ : X 00 → X , µ0 : X 00 → X 0 , such that
L00 := µ? L = µ0? L0 . Since X and X 0 are integrally closed, Lemma 1.12 yields µ? OX 00 = OX ,
µ0? OX 00 = OX 0 , and the projection formula shows that
                           H0 (X , mL) = H0 X 00 , mL00 = H0 (X 0 , mL0 ).
                                                          

The proof is complete.                                                                             
2.7. Fubini–Study functions and test configurations. Let L be a Q-line bundle on X.
For any test configuration (X , L) for (X, L), we can choose a test configuration X 0 with two
morphisms µ : X 0 → X , ρ : X 0 → Xtriv . Then
                                D := µ? L − ρ? Ltriv ∈ VCar(X )Q ,
and mapping L to D yields a 1–1 correspondence between the set of equivalence classes
of test configurations for (X, L) and the Q-vector space limX VCar(X )Q , which in turn is
                                                         −→
isomorphic to PL(X), by Theorem 2.7. We write ϕL for the element of PL(X) associated to
30                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

L. The restriction of ϕL to X div coincides with the function associated to the equivalence
class of (X , L) in [BHJ17, §6].
Theorem 2.31. For any Q-line bundle L on X, the map L 7→ ϕL sets up a 1–1 correspon-
dence between:
    (i) the set of equivalence classes of test configurations for L and PL(X);
   (ii) the set of equivalence classes of semiample test configurations for L and H(L).
   Note that the sets in (ii) are nonempty only if L is semiample. Combined with Proposi-
tion 2.30, we infer:
Corollary 2.32. If L is an ample Q-line bundle, then L 7→ ϕL defines a 1–1 correspondence
between the set of ample, integrally closed test configurations for L and H(L).
     The set H(L) thus corresponds to HNA (L) in the notation of [BHJ17, Definition 6.2].
Proof of Theorem 2.31. By construction, the map L 7→ ϕL is the composition of D 7→ ϕD
with the canonical bijection between equivalence classes of test configurations for L and
limX VCar(X )Q . Thus (i) is a direct consequence of Theorem 2.7.
−→
   To prove (ii), let (X , L) be a semiample test configuration for (X, L). After replacing L
with a multiple and pulling-back to a higher test configuration, we may assume without loss
that L is a globally generated line bundle, and that X dominates the trivial test configuration
via µ : X → Xtriv . Set D := L − µ? Ltriv ∈ VCar(X ), so that ϕL = ϕD . Since L is globally
generated, OX (D) is µ-globally generated, and the flag ideal a := µ? OX (D) thus satisfies
a·OX = OX (D), and hence ϕa = ϕD = ϕL . Denote by a0 ⊂ a the flag ideal locally generated
by
                                H0 (Xtriv , Ltriv ⊗ a) ≃ H0 (X , L).
Since L is globally generated, we have a0 · OX = OX (D) = a · OX ; hence ϕa0 = ϕL . By
construction, L ⊗ a0 is globally generated, and Proposition 2.25 thus yields, as desired,
ϕL ∈ H(L).
   Conversely pick ϕ ∈ H(L). After replacing L with a multiple, Proposition 2.25 yields
ϕ = ϕa for a flag ideal a on Xtriv such that Ltriv ⊗ a is globally generated. Denoting by
µ : X → Xtriv the blowup along a, we have a · OX = OX (D) for a vertical Cartier divisor D
such that L := µ? Ltriv + D is globally generated, and ϕL = ϕD = ϕa = ϕ.                      
     The next result will be needed in §3.1.
Lemma 2.33. If L is an ample Q-line bundle on X and X any test configuration for X
that dominates Xtriv , then L admits an ample test configuration L determined on X .
Proof. By Lemma 1.8, we can find D ∈ VCar(X )Q that is relatively ample over Xtriv .
Denoting by LX the pullback of L to X , it follows that L := LX + εD is ample for ε ∈ Q>0
small enough, and we are done.                                                         
2.8. Geometric interpretation of the scaling action. As noted in §2.1, the spaces
PL(X) and PL+ (X) admit a natural scaling action by Q>0 . We now give a geometric
interpretation of the scaling action of Z>0 in terms of base change.
   Using flag ideals, this is easy: any function ϕ ∈ PL+ (X) can be written ϕ = m−1 ϕa for
some m ∈ Z>0 and some flag ideal a on Xtriv = X × A1 . It then follows from the discussion
after (2.5) that if d ∈ Z>0 , then d · ϕ = m−1 ϕa(d) , where a(d) is the pullback of a under the
map Xtriv → Xtriv given by $ 7→ $d .
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                           31

  Following [BHJ17, §6.3], we can give a smilar interpretation of the scaling action when
the functions are associated to test configurations.
  Let L be a Q-line bundle on X. For any test configuration (X , L) for (X, L) and d ∈ Z>0 ,

# PRIMARY exact literal unit

curve C ⊂ X0 , which we accomplish by way of a standard degeneration argument: denote
34                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

by Ct the image of C under t ∈ Gm , and note that α · C = α · Ct , by Gm -invariance of α.
By properness of the components of the Chow scheme of X0 , C0 := limt→0 Ct exists as an
effective 1-cycle. It is Gm -invariant, and hence a positive linear combination of Gm -invariant
irreducible curves. Thus
                                 α · C = lim α · Ct = α · C0 ≥ 0,
                                         t→0
and we are done.                                                                              
   If a test configuration X dominates Xtriv = X × A1 , then each class θ ∈ N1 (X) pulls back
to a class θX ∈ N1 (X /A1 ) via the composition
                                   X → Xtriv = X × A1 → X.
In line with [Zha95, Gub98, CL06, BFJ16], we introduce:
Definition 3.2. We say that a function ϕ ∈ PLR is θ-plurisubharmonic ( θ-psh for short)
if it is determined by a divisor D ∈ VCar(X )R on a test configuration X dominating Xtriv
such that θX + D ∈ Nef(X /A1 ).
   We sometimes also say that the pair (θ, ϕ) ∈ N1 (X) × PLR is psh. Here θX + D denotes,
slightly abusively, the sum of θX and of the image of D in N1 (X /A1 ).
   This definition is independent of the choice of X . Indeed, for any morphism of test
configurations µ : X 0 → X , we have
                                   θX 0 + µ? D = µ? (θX + D) ,
which is thus nef iff θX +D is nef. Restricting to X1 ≃ X further shows that a θ-psh function
in PLR can only exist when θ ∈ Nef(X).
   We will use the notation
                              PLR ∩ PSH(θ)     and    PL ∩ PSH(θ)
for the sets of θ-psh functions in PLR and PL, respectively. At this point, the notation is
purely formal, but it will be justified in §4, by defining the set PSH(θ).
   When θ = c1 (L) ∈ N1 (X) is the numerical class of L ∈ Pic(X)Q on X, we simply speak
of L-psh functions. By Theorem 2.31, we have:
Example 3.3. For any Q-line bundle L on X, L 7→ ϕL sets up a 1–1 correspondence
between the set of semipositive non-Archimedean metrics in the sense of [BHJ17, Defini-
tion 6.4], i.e. equivalence classes of nef test configurations L for L, and PL ∩ PSH(L). By
Theorem 2.31 (ii), we thus have H(L) ⊂ PL ∩ PSH(L), the inclusion being strict in general.
Remark 3.4. Following [BFJ16, BFJ15] we could define a closed (1, 1)-form on X an to be
an element η ∈ limX N1 (X /A1 ), and declare a function ϕ ∈ PLR to be η-psh if it is of the
                −→
form ϕ = ϕD , with D ∈ VCar(X )R such that η + D is nef. In this paper we only consider
the case when η ∈ N1 (Xtriv /A1 ) is determined by the pullback of a class θ ∈ N1 (X).
     As a direct consequence of the fact that Nef(X /A1 ) ⊂ N1 (X /A1 ) is closed, we have:
Lemma 3.5. Let θi → θ be a convergent sequence in N1 (X). Pick ϕ, ψ ∈ PLR , and assume
that ϕ + ci ψ is θi -psh for a sequence ci → 0. Then ϕ is θ-psh.
Proposition 3.6. Pick θ, θ0 ∈ N1 (X), and assume that ϕ, ϕ0 ∈ PLR are θ-psh and θ0 -psh,
respectively. Then:
    (i) ϕ + ϕ0 is (θ + θ0 )-psh, and tϕ is tθ-psh for all t ∈ R>0 ;
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        35

    (ii) for each c ∈ R and t ∈ Q>0 , ϕ + c and t · ϕ are θ-psh;
   (iii) if θ = θ0 and ϕ, ϕ0 ∈ PL, then max{ϕ, ϕ0 } ∈ PL is θ-psh;
   (iv) ϕ is decreasing with respect to the partial order on X an , and hence satisfies (1.4)
         (see Lemma 1.4);
    (v) for any morphism f : Y → X from a projective variety, f ? ϕ is f ? θ-psh;
   (vi) if we further assume that f : Y → X is surjective, then
                   ϕ θ-psh ⇐⇒ ϕ|Xαan θ|Xα -psh for all α ⇐⇒ f ? ϕ f ? θ-psh.
  In particular, (i) shows that PLR ∩ PSH(θ) is a convex subset of PLR .
Lemma 3.7. For any θ ∈ N1 (X) and ϕ ∈ PLR ∩ PSH(θ), there exists a sequence ϕm ∈
H(Lm ) with Lm ∈ Pic(X)Q such that ϕm → ϕ uniformly on X an and c1 (Lm ) → θ.
Proof. Pick a test configuration X dominating Xtriv and D ∈ VCar(X )R such that ϕ = ϕD .
By openness of the (relatively) ample cone of N1 (X /A1 ), we can find a sequence of Q-
line bundles Lm on X and Dm ∈ VCar(X )Q such that c1 (Lm ) → θ in N1 (X), Dm → D
in VCar(X )R , and c1 (Lm )X + Dm ∈ N1 (X /A1 ) is ample for all i. In particular, Lm :=
(Lm )X +Dm is a semiample test configuration for L, and hence ϕm := ϕLm = ϕDm ∈ H(Lm ).
Furthermore, Dm → D implies ϕm → ϕ uniformly.                                          
Proof of Proposition 3.6. Pick a test configuration X dominating Xtriv and D, D0 ∈ VCar(X )R
that determine ϕ, ϕ0 . By assumption, θX + D and θX   0 + D 0 are nef. Thus

       (θ + θ0 )X + D + D0 = (θX + D) + θX   0
                                               + D0
                                                    
                                                        and (tθ)X + tD = t (θX + D)
are nef as well, proving (i).
   For each c ∈ R we have ϕ + c = ϕD+cX0 . Since X0 = π ? (0) vanishes in N1 (X /A1 ),
θX + D + cX0 is nef, and ϕ + c is thus θ-psh. To prove the remaining part of (ii), it suffices to
prove that if d ∈ Z>0 , then ϕ is θ-psh iff d · ϕ is θ-psh. In view of Lemma 2.34, this follows
from the fact that θX + D ∈ N1 (X /A1 ) is nef iff its pullback under the base change of X
with respect to $ 7→ $d is nef.
   Assume now θ = θ0 and D, D0 ∈ VCar(X )Q . By openness of Amp(X), we can find an
Q-line bundle L on X such that c1 (L) − θ is ample and arbitrarily small. Then ϕ, ϕ0 are
L-psh, and it will be enough to show that max{ϕ, ϕ0 } is L-psh as well, by Lemma 3.5. After
perhaps passing to a higher test configuration, we may assume that X supports an ample
test configuration L for L (Lemma 2.33). For each ε ∈ Q>0 , the Q-line bundle LX + D + εL
is ample, and hence semiample. Thus ϕ + εϕL is Fubini–Study for (1 + ε)L, and similarly
for ϕ0 + εϕL . By Proposition 2.19, it follows that
                        max{ϕ + εϕL , ϕ0 + εϕL } = max{ϕ, ϕ0 } + εϕL
is Fubini–Study for (1 + ε)L, and hence (1 + ε)L-psh. Using Lemma 3.5 we conclude, as
desired, that max{ϕ, ϕ0 } is L-psh. This proves (iii).
    By Proposition 2.19, any Fubini–Study function is decreasing, and (iv) thus follows from
Lemma 3.7.
    To prove (v), note that the Gm -equivariant rational map Y × Gm 99K X induced by f
admits a Gm -equivariant resolution of indeterminacies, which is thus a test configuration Y
for Y dominating Ytriv . Also denoting by f : Y → X the corresponding morphism, we have
f ? ϕ = ϕf ? D , and the result thus follows from the fact that θY + f ? D = f ? (θX + D) is nef,
as the pullback of a nef class. If f : Y → X is surjective, then f : Y → X is surjective as
well, and (vi) follows.                                                                        
36                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

   Given a test configuration π : X → A1 , we denote by Amp(X /A1 ) ⊂ Nef(X /A1 ) the set
of π-ample classes α ∈ N1 (X /A1 ), that is, classes whose restriction to X0 is ample.
Definition 3.8. For any ω ∈ Amp(X), we denote by Hdom (ω) ⊂ PL ∩ PSH(ω) the set of ω-
psh PL functions of the form ϕD with D ∈ VCar(X )Q for a test configuration X dominating
Xtriv and ωX + D ∈ Amp(X /A1 ).
   After pulling back by the (finite) integral closure morphism Xe → X , one may always
arrange that X is integrally closed in this definition.
Example 3.9. If ω = c1 (L) for an ample Q-line bundle, then H(L) is in 1–1 correspon-
dence with the set of ample, integrally closed test configurations (X , L) for (X, L) (see Corol-
lary 2.32), and
                              Hdom (L) := Hdom (c1 (L)) ⊂ H(L)
corresponds to the subset such that X dominates Xtriv .
     As in Corollary 2.26, we have
                                     Q+ Hdom (ω) = PL+ (X)                                 (3.2)
for any ω ∈ Amp(X), so that Hdom (ω) spans the Q-vector space PL(X).
Proposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of
functions in Hdom (ω).
Lemma 3.11. For any ω ∈ Amp(X), the set of test configurations X dominating Xtriv such
that there exists H ∈ VCar(X )Q with ωX + H ∈ Amp(X /A1 ) is cofinal in the set of all test
configurations.
Proof. By Lemma 1.8, any test configuration for X is dominated by a test configuration X
with a morphism µ : X → Xtriv such that VCar(X )Q contains a µ-ample divisor A. Since
ωXtriv ∈ N1 (Xtriv /A1 ) is ample, ωX + εA = µ? ωXtriv + εA ∈ N1 (X /A1 ) is ample for ε ∈ Q>0
small enough, and setting H := εA yields the result.                                        
Proof of Proposition 3.10. Pick any ϕ ∈ PLR ∩ PSH(ω), and write ϕ = ϕD for some D ∈
VCar(X )R , where X is an integrally closed test configuration. Thus ωX + D ∈ N1 (X /A1 ) is
nef. By Lemma 3.11 we may assume that there exists P    H ∈ VCar(X )PR such that ωX + H is
ample. Pick a basis (Ci ) for VCar(X )Q and write D = i ci Ci , H = i c0i Ci with ci , c0i ∈ R.
                                  1                                                          1
For m  1, the class ωX + D + m     H ∈ N1 (X /A1 ) is ample, and we can pick εm,i ∈ (0, m     )
                    P          0
                              ci
such that if Dm := i (ci + m + εm,i )Ci , then Dm ∈ VCar(X )Q and ωX + Dm is ample. It
                                                     1
follows that ϕDm ∈ Hdom (ω), and that ϕDm − ϕ = m
                                                             P
                                                       ϕH + i εm,i ϕCi tends to 0 uniformly
on X an .                                                                                     
3.2. The energy pairing. Recall that every test configuration π : X → A1 admits a canon-
ical compactification π : X̄ → P1 . If X dominates Xtriv , then any θ ∈ N1 (X) pulls back to a
class θX̄ ∈ N1 (X̄ ), whose image in N1 (X /A1 ) coincides with θX considered above.
   Pick an (n + 1)-tuple of pairs (θi , ϕi ) ∈ N1 (X) × PLR , i = 0, . . . , n, and choose a test
configuration X dominating Xtriv and divisors Di ∈ VCar(X )R that determined the ϕi .
Following [BHJ17, Definition 6.11], we introduce:

# PRIMARY exact literal unit

to an arbitrary numerical class θ ∈ N1 (X). We also study pluripolar sets, i.e. loci where
θ-psh functions take the value −∞.
               GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        45

  4.1. The class of θ-psh functions. Recall that:
       • a function ϕ ∈ X an → R ∪ {−∞} is called generically finite if ϕ|Xαan 6≡ −∞ for all α
         (see Definition 1.3);
                                gf
       • for any L ∈ Pic(X)Q , HR  (L) denotes the set of generically finite (continuous) func-
                    an
         tions ϕ : X → R ∪ {−∞} of the form
                                    ϕ = m−1 max{log |si | + λi }
                                                i
           where (si ) is a finite set of sections of mL with m sufficiently divisible, λi ∈ R (see
           Definition 2.18). This set is non-empty iff L is effective.
  Given any numerical class θ ∈ N1 (X), we are seeking to define a class PSH(θ) of θ-
  plurisubharmonic functions (θ-psh functions for short) ϕ : X an → R ∪ {−∞}. By analogy
  with the complex analytic setting, these functions should be usc and generically finite, and
  the following properties should hold:
                                                gf
 (PSH1) for any L ∈ Pic(X)Q , we have HR           (L) ⊂ PSH(L) := PSH(c1 (L));
 (PSH2) if a generically finite function ϕ : X an → R ∪ {−∞} arises as the pointwise limit of
           a decreasing net (ϕi ) with ϕi ∈ PSH(θi ) and limi θi = θ, then ϕ ∈ PSH(θ).
  Note that (PSH2) implies the following two properties:
(PSH2a) for any function ϕ : X an → R ∪ {−∞}, the set of θ ∈ N1 (X) such that ϕ ∈ PSH(θ)
           is closed (possibly empty);
(PSH2b) for any θ ∈ N1 (X), the set PSH(θ) is closed under decreasing limits (provided the
           limit function is generically finite).
  Taking (PSH1) and (PSH2) as minimal requirements directly leads to the following defini-
  tion:
  Definition 4.1. For any θ ∈ N1 (X), we define a θ-psh function ϕ : X an → R ∪ {−∞} as a
  generically finite, usc function that can be written as the pointwise limit of a decreasing net
         gf
  ϕi ∈ HR   (Li ) with Li ∈ Pic(X)Q such that limi c1 (Li ) = θ in N1 (X).
    We denote by PSH(θ) the set of θ-psh functions, and by
                        CPSH(θ) := C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) ⊂ PSH(θ)
  the subsets of continuous and bounded θ-psh functions, respectively. When needed, we also
  write PSH(X, θ) = PSH(θ) etc. Using the notation in the definition, we have:
                 gf
        • since HR  (Li ) is non-empty, Li is necessarily effective, by (2.11), and hence
                                   PSH(θ) 6= ∅ =⇒ θ ∈ Psef(X);                                (4.1)
        • if ϕ is bounded, then ϕi is finite valued, i.e. ϕi ∈ H(Li ); this implies that Li is
          semiample, by (2.12), and hence
                                    E ∞ (θ) 6= ∅ =⇒ θ ∈ Nef(X);                               (4.2)
        • if ϕ ∈ CPSH(θ) is further continuous, then ϕi → ϕ uniformly on X an , by Dini’s
          lemma.
  Remark 4.2. In the complex analytic case, psh functions and metrics are defined in a
  different way, which is local in nature. However, when X is smooth, well-known arguments
  due to Demailly [Dem92] and relying on the Ohsawa–Takegoshi extension theorem show that
  any psh metric on a (necessarily pseudoeffective) line bundle L can be approximated from
  above by metrics attached to sections of mL + A, where A is a fixed ample line bundle and
46                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

m is large (compare for instance [Bou04, Theorem 5.4] or [GZ05, Appendix]). As a result,
any such metric satisfies the analogue of Definition 4.1.
Lemma 4.3. For functions in PL(X)R , Definition 4.1 is consistent with Definition 3.2.
In other words, given θ ∈ N1 (X), a test configuration X that dominates Xtriv and D ∈
VCar(X )R , we have
                        ϕD ∈ PSH(θ) ⇐⇒ θX + D ∈ Nef(X /A1 ).
  Indeed, this follows from Lemma 3.5, Lemma 3.7 and Corollary 3.22. For any θ ∈ N1 (X),
we get, in particular,
                   PSH(θ) contains all constant functions ⇐⇒ θ ∈ Nef(X),                       (4.3)
which provides a converse to (4.2).
Remark 4.4. If L is a Q-line bundle, then functions in PSH(L) = PSH(c1 (L)) can be
interpreted as psh metrics on L, using the trivial metric. By (4.3), any nef line bundle L
admits a bounded (continuous) psh metric, to wit the trivial metric. This is in stark contrast
with the complex analytic case, where a nef and big line bundle may not admit any bounded
psh metric (see [BEGZ10, Example 5.4], based on [DPS94, Example 1.7]).
Theorem 4.5. Properties (PSH1) and (PSH2) above are satisfied.
  As a consequence, Definition 4.1 is indeed the minimal one for which (PSH1) and (PSH2)
are satisfied.
Lemma 4.6. Let K be a compact topological space, and assume we are given:
      • a set S and, for each s ∈ S, a family Fs of continuous functions f : K → R ∪ {−∞},
         stable under addition of a constant;
      • a map ρ : S → T to a metrizable topological space T .
For each t ∈ T , denote by Fet the set of all (usc) functions g : K → R ∪ {−∞} that can
be written as the pointwise limit of a decreasing net (fi ) with fi ∈ Fsi for a net (si ) of S
                                          ≈
such that limi ρ(si ) = t in T . Then Ft = Fet for any t ∈ T . In other words, if a function
g : K → R ∪ {−∞} can be written as the pointwise limit of a decreasing net (gi )i∈I with
gi ∈ Feti for a net (ti ) of T such that limi ti = t, then g ∈ Fet .
Proof. Pick a metric d on T inducing the given topology. For each i ∈ I, gi is the pointwise
limit of a decreasing net (fi,j )j∈Ji with fi,j ∈ Fsi,j for a net (si,j )j∈Ji in S such that ti,j :=
ρ(si,j ) satisfies limj ti,j = ti . Denote by A the set of triples α = (i, j, ε) with i ∈ I, j ∈ Ji
and ε ∈ R>0 , and define a partial preorder on A by setting
                                                 i ≥ i0
                                                
                                  0 0 0
                    (i, j, ε) ≥ (i , j , ε ) ⇐⇒   fi,j + ε ≤ fi0 ,j 0 + ε0 on K                 (4.4)
                                                  d(ti,j , ti ) + ε ≤ d(ti0 ,j 0 , ti0 ) + ε0 ,
                                                

We claim that A is directed. To see this, pick α1 = (i1 , j1 , ε1 ), α2 = (i2 , j2 , ε2 ) in A. Since
I is directed, we can choose i3 ∈ I with i3 ≥ i1 , i2 . Pick also ε3 > 0 with ε3 < min{ε1 , ε2 }.
Since (gi )i is decreasing, we have gi3 ≤ min{gi1 , gi2 } ≤ min{fi1 ,j1 , fi2 ,j2 }, and hence
                              gi3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }                     (4.5)
pointwise on K. For each j ∈ Ji3 , define hj : K → R by
                   hj := exp (fi3 ,j + ε3 ) − exp (min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }) .
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                      47

Then (hj ) is a decreasing net of continuous functions such that limj hj < 0 pointwise on K,
by (4.5). The compact space K can thus be written as the increasing union of the open sets
{hj < 0}, and hence K = {hj3 < 0} for some j3 ∈ Ji3 , i.e.
                            fi3 ,j3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 } on K.
Since limj ti3 ,j = ti3 and ε3 < min{ε1 , ε2 }, we can further arrange, after increasing j3 if
needed, that
          d(ti3 ,j3 , ti3 ) + ε3 < min{ε1 , ε2 } ≤ min {d(ti1 ,j1 , ti1 ) + ε1 , d(ti2 ,j2 , ti2 ) + ε2 } .
Thus α3 := (i3 , j3 , ε3 ) ∈ A satisfies α3 ≥ α1 , α2 , which proves, as desired, that A is directed.
  Now, for each α = (i, j, ε) ∈ A, set
                  sα := si,j ∈ S,       tα = ρ(sα ) ∈ T,        and gα := fi,j + ε ∈ Fsα ,
where the last containment holds because Fsα is assumed to be stable under addition of a
constant. By construction, (gα )α∈A is a decreasing net, and it will suffice to show limα gα = g
pointwise on K and limα tα = t. Pick δ > 0 and x ∈ K. Since limi gi (x) = g(x) and
limi ti = t, we can find i0 ∈ I such that gi0 (x) < g(x) + δ and d(ti , t) < δ for all i ≥ i0 .
Using limj fi0 ,j (x) = gi0 (x) and limj ti0 ,j = ti0 , we next pick j0 ∈ Ji0 and 0 < ε0  1 such
that fi0 ,j0 (x) + ε0 < g(x) + δ and d(ti0 ,j0 , ti0 ) + ε0 < δ. Set α0 := (i0 , j0 , ε0 ) ∈ A. For each
α = (i, j, ε) ∈ A such that α ≥ α0 , we then have, by (4.4),
                           gα (x) = fi,j (x) + ε ≤ fi0 ,j0 (x) + ε0 < g(x) + δ,

                    d(tα , ti ) = d(ti,j , ti ) ≤ d(ti,j , ti ) + ε ≤ d(ti0 ,j0 , ti0 ) + ε0 < δ,
as well as i ≥ i0 , which implies d(ti , t) < δ and hence d(tα , t) < 2δ. This shows, as desired,
limα gα (x) = g(x) and limα tα = t, which concludes the proof.                                 

Proof of Theorem 4.5. That (PSH1) holds is clear from Definition 4.1. As for (PSH2), it
                                                                             gf
corresponds to the special case of Lemma 4.6 in which K := X an , FL := HR      (L) for L ∈ S :=

# PRIMARY exact literal unit

the complex analytic case, this holds in fact on any connected variety, see Corollary 4.24
below.
Remark 4.14. Any ϕ ∈ PL(X)R is η-psh with respect to some closed (1, 1)-form η, in the
sense of Remark 3.4. However, ϕ is in general not θ-psh for any θ ∈ N1 (X), since such
functions must be decreasing in the partial ordering on X an (see Proposition 4.12 ). As a
result, several potential definitions of quasi-psh functions coexist in our context.
4.3. The regularization theorem. Many properties of θ-psh functions are obtained by
regularization, that is, approximation by nicer θ-psh functions. In our present approach,
regularization of θ-psh functions is built into their definition. One can, however, improve
the properties of the approximants as follows:
Theorem 4.15. Pick θ ∈ N1 (X) and ϕ ∈ PSH(θ). Then:
                                                                   gf
     (i) ϕ can be written as the limit of a decreasing net ϕi ∈ HQ    (Li ) with Li ∈ Pic(X)Q
         such that c1 (Li ) − θ is ample and limi c1 (Li ) = θ;
    (ii) if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;
   (iii) if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in
         Hdom (ω) (see Definition 3.8).
50                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

   We shall later prove that these results actually hold with (countable) sequences instead
of nets, see Corollary 12.18.
   As already indicated by (iii), the class of θ-psh functions has particularly good properties
when θ ∈ Amp(X) is ample. In this case, we typically write ω instead of θ.
Corollary 4.16. For any ω ∈ Amp(X), the space CPSH(ω) = C0 (X) ∩ PSH(ω) is the
closure of Hdom (ω) ⊂ C0 (X) in the topology of uniform convergence.
Proof. By Theorem 4.7, CPSH(ω) is closed in the topology of uniform convergence. By
Theorem 4.15 and Dini’s lemma, any ϕ ∈ CPSH(ω) is the uniform limit of a net in Hdom (ω),
and the result follows.                                                                
Corollary 4.17. For any θ ∈ N1 (X) and any ϕ ∈ PSH(θ) we have ϕ > −∞ on X lin .
Proof. Pick an ample line ` bundle L such that c1 (L) − θ is nef. Then ϕ ∈ PSH(L). Using
Theorem 4.7 and X lin = α Xαlin , we may assume X is irreducible. Now pick v ∈ X lin . Then
TL (v) < ∞, and we claim that ϕ(v) ≥ ϕ(vtriv ) − TL (v). Indeed, TL (v) is the supremum of
m−1 v(s) over m ∈ Z>0 and s ∈ H0 (X, mL) \ {0}. Equivalently, ψ := m−1 log |s| satisfies
ψ(v) ≥ ψ(vtriv ) − TL (v). Adding constants and taking finite maxima shows that this also
holds for all ψ ∈ H(L), and then for all ϕ ∈ PSH(L), by Theorem 4.15.                     
     As another consequence, we get:
Corollary 4.18. Assume that X is irreducible, and let L be an ample Q-line bundle. Then
PSH(L) is the smallest class of functions ϕ : X an → R ∪ {−∞}, not identically −∞, that
contains all functions of the form m−1 log |s| with m ∈ Z>0 and s ∈ H0 (X, mL) \ {0}, and
is stable under addition of a real constant, finite maxima, and decreasing limits.
                                                                                gf
Proof of Theorem 4.15. By definition, ϕ is the limit of a decreasing net ϕi ∈ HR   (Li ) with
c1 (Li ) → θ. Using (2.8) it is straightforward to see that each ϕi can further be written
                                         gf
as a decreasing limit of functions in HQ    (Li ). By Lemma 4.6, we may thus assume that
        gf
ϕi ∈ HQ    (Li ). We can also arrange that c1 (Li ) − θ ∈ Amp(X). Indeed, given any ample
line bundle A, we can find εi ∈ Q>0 such that limi εi = 0 and Li − θ + εi A is ample. By
                                    gf          gf
Proposition 2.19, we have ϕi ∈ HQ      (Li ) ⊂ HQ  (Li + εi A), and replacing Li with Li + εi A
yields the claim. This proves (i).
   Assume next that θ is nef. In the notation of (i), it follows that each Li is ample. Further,
each ϕi is the decreasing limit of max{ϕi , −m} ∈ H(Li ), and Lemma 4.6 yields (ii).
   Finally assume that ω := θ is ample. Replacing ϕ with ϕ − sup ϕ, we may assume
ϕ ≤ 0. By Proposition 3.10, any function in PL ∩ PSH(ω) is a decreasing limit of functions
in Hdom (ω). Relying again on Lemma 4.6, it will thus be enough to show that ϕ is the
decreasing limit of functions in PL ∩ PSH(ω). Use the notation of (ii), and pick t ∈ Q>1 .
For all i large enough we then have tω − c1 (Li ) ∈ Amp(X) for i large enough, and hence
H(Li ) ⊂ PL ∩ PSH(tω). It follows that t−1 ϕ is the decreasing limit of a net in PL ∩ PSH(ω).
Since ϕ ≤ 0, we have t−1 ϕ & ϕ as t & 1, and another application of Lemma 4.6 shows that
ϕ is also the decreasing limit of functions in PL ∩ PSH(ω). This proves (iii).                
Remark 4.19. Assume that char k = 0 and that X is smooth and connected. Consider
the field of Laurent series K = k((t)), and denote by XKan the Berkovich analytification of
                                                               an → X an . The base change
the base change XK ; this comes with a natural projection π : XK
ωK of any ω ∈ Amp(X) defines a closed (1, 1)-form on XK   an with ample de Rham class, in

the sense of [BFJ16]. Using Theorem 4.15 (iii) and Theorem A.4 in the Appendix, one can
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                       51

show that a function ϕ : X an → R ∪ {−∞} is ω-psh in the present sense iff π ? ϕ is ωK -psh
on XKan in the sense of [BFJ16].


                                        θ ∈ N1 (X) for the moment. By Corollary 4.17 ,
4.4. The topology of PSH(θ). Let us fix `
any ϕ ∈ PSH(θ) is finite-valued on X = α Xαdiv .
                                    div


Definition 4.20. We endow PSH(θ) with the topology of pointwise convergence on X div .
  As we shall later see in Theorem   11.4, this topology coincides with the topology of point-
                       lin        lin
                            `
wise convergence on X = α Xα . In view of (4.6), we have:
Example 4.21. The map ϕ 7→ sup ϕ = maxα ϕ(vtriv,α ) is continuous on PSH(θ).
Theorem 4.22. For any ϕ ∈ PSH(θ) and any usc function ψ : X an → R ∪ {−∞}, we have

# PRIMARY exact literal unit

5.3. Envelopes. For ample classes, the envelope property admits a useful reformulation.
We continue to assume that X is irreducible unless stated otherwise. Fix a class ω ∈
Amp(X).
Definition 5.16. The ω-psh envelope of a function ϕ : X an → R ∪ {±∞} is the function
Pω (ϕ) : X an → R ∪ {±∞} defined as the pointwise supremum
                           Pω (ϕ) := sup {ψ ∈ PSH(ω) | ψ ≤ ϕ} .
  Thus Pω (ϕ) ≡ −∞ iff there is no ψ ∈ PSH(ω) with ψ ≤ ϕ. Despite the name, Pω (ϕ) is
not always ω-psh (and indeed not even usc in general). However, it is clear that
     • ϕ 7→ Pω (ϕ) is increasing;
     • Pω (ϕ + c) = Pω (ϕ) + c for all c ∈ R.
60                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

These properties formally imply the Lipschitz estimate
                               sup Pω (ϕ) − Pω (ϕ0 ) ≤ sup |ϕ − ϕ0 |.                     (5.1)
when ϕ, ϕ0 are bounded.
Lemma 5.17. For any ω ∈ Amp(X), the following statements are equivalent:
   (i) ω has the envelope property;
  (ii) for any function ϕ : X an → R ∪ {±∞}, we have
                      Pω (ϕ) ≡ −∞, Pω (ϕ)? ≡ +∞, or Pω (ϕ)? ∈ PSH(ω).
     (iii) for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.
     We refer to the property in (iii) as continuity of envelopes.
Proof. First assume (i). Pick any ϕ : X an → R ∪ {±∞}, and suppose that the set F :=
{ψ ∈ PSH(θ) | ψ ≤ ϕ} is nonempty, so that Pω (ϕ) 6≡ −∞. If the functions in F are uniformly
bounded above, then Pω (ϕ)? ∈ PSH(ω), by (i). If not, then, by the definition of the
Alexander–Taylor capacity we have
             Pω (ϕ)(v) = sup {ψ(v) | ψ ∈ F} ≥ sup {sup ψ | ψ ∈ F} − Tω (v) = +∞
for all v ∈ X div , and hence Pω (ϕ)? ≡ +∞, by density of X div . This proves (i)⇒(ii).
   Next we prove (ii)⇒(iii), so pick ϕ ∈ C0 (X). Then Pω (ϕ)? ∈ PSH(ω) is a competitor in
the definition of Pω (ϕ), and hence Pω (ϕ)? ≤ Pω (ϕ). We conclude that Pω (ϕ)? = Pω (ϕ) is
usc. We claim that Pω (ϕ) is also lsc, and hence continuous. To prove the claim, it suffices to
show that Pω (ϕ) is a supremum of continuous functions, and for this it suffices to prove that
for any ψ ∈ PSH(ω) with ψ ≤ ϕ and any ε > 0, there exists ψ 0 ∈ C0 (X) with ψ ≤ ψ 0 ≤ ϕ+ε.
Pick a decreasing net ψi ∈ Hdom (ω) converging pointwise to ψ. For each v ∈ X an , the set
{ψi < ϕ + ε} is an open neighborhood of v for i large enough, by lower semicontinuity of
ϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for all i large enough, so we can
take ψ 0 = ψi .
   Finally, we prove (iii)⇒(i), following [BE20, Lemma 7.30]. Let (ϕi ) be a bounded-above
family in PSH(ω), and set ϕ := sup?i ϕi . Since ϕ is usc and X an is compact, we can find
a decreasing net of continuous functions (ψj ) such that ψj → ϕ. For each i, j, we have
ϕi ≤ ψj , and hence ϕi ≤ Pω (ψj ), which in turn yields ϕ ≤ Pω (ψj ) ≤ ψj . We have thus
written ϕ as the limit of the decreasing net of ω-psh functions Pω (ψj ), which shows that ϕ
is ω-psh.                                                                                    
Corollary 5.18. Assume that ω ∈ Amp(X) has the envelope property, and consider a usc
function ϕ : X an → R ∪ {−∞}. Then:
    (i) Pω (ϕ) is ω-psh, or Pω (ϕ) ≡ −∞;
   (ii) if ϕ is the limit of a decreasing net (ϕj ) of bounded-above, usc functions, then
        Pω (ϕj ) & Pω (ϕ).
Proof. By Lemma 5.17, either ψ := Pω (ϕ)? is ω-psh, or Pω (ϕ) ≡ −∞. Since Pω (ϕ) ≤ ϕ and
ϕ is usc, we also have ψ ≤ ϕ. If ψ is ω-psh, then ψ ≤ Pω (ϕ), which proves (i).
  To see (ii), note that ρ := limj Pω (ϕj ) satisfies either ρ ∈ PSH(ω) or ρ ≡ −∞, by
Theorem 4.7. Furthermore, Pω (ϕj ) ≤ ϕj yields in the limit ρ ≤ ϕ, and hence ρ ≤ Pω (ϕ) (by
definition of Pω (ϕ) if ρ ∈ PSH(ω), and trivially if ρ ≡ −∞). Thus limj Pω (ϕj ) = ρ = Pω (ϕ).
On the other hand, Pω (ϕj ) ≥ Pω (ϕ) implies ρ ≥ Pω (ϕ), which completes the proof of (ii). 
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      61

  For any function ϕ : X an → R ∪ {±∞}, we also introduce the pointwise envelope
                           Qω (ϕ) := sup {ψ ∈ CPSH(ω) | ψ ≤ ϕ} ;
this is lsc and bounded below if ϕ is bounded below, and ≡ −∞ otherwise. Since each
ψ ∈ CPSH(ω) is the uniform limit of functions in Hdom (ω) (see Theorem 4.7), one easily
checks that
                            Qω (ϕ) = sup{ψ ∈ Hdom (ω) | ψ ≤ ϕ}.
Lemma 5.19. Suppose ϕ : X an → R ∪ {+∞} is bounded below, with lsc regularization
ϕ? : X an → R ∪ {+∞}. Then:
     (i) Qω (ϕ) = Pω (ϕ? );
    (ii) Qω (ϕ) ∈ C0 (X) ⇐⇒ Qω (ϕ) ∈ PSH(ω);
   (iii) if ϕ is the pointwise limit of an increasing net (ϕj ) of bounded-below, lsc functions
         (and hence ϕ is lsc), then Pω (ϕj ) % Pω (ϕ).
Proof. A function ψ ∈ CPSH(ω) satisfies ψ ≤ ϕ iff ψ ≤ ϕ? . Thus Qω (ϕ) = Qω (ϕ? ), and we
may therefore assume wlog that ϕ is lsc. Trivially, Pω (ϕ) ≥ Qω (ϕ). Pick ψ ∈ PSH(ω) such
that ψ ≤ ϕ, and let (ψi ) be a decreasing net in CPSH(ω) converging pointwise to ψ. For
each ε > 0 and v ∈ X an , we can find i such that {ψi < ϕ + ε} is an open neighborhood of
v, by lower semicontinuity of ϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for
all i large enough. Thus ψ ≤ ψi ≤ Qω (ϕ + ε) = Qω (ϕ) + ε, which proves (i).
   As noted above, Qω (ϕ) is lsc and bounded below. If Qω (ϕ) is ω-psh, then it is in particular
usc, and hence Qω (ϕ) ∈ C0 (X). Assume, conversely, that Qω (ϕ) ∈ C0 (X). Since CPSH(ω)
is stable under finite maxima, Qω (ϕ) is the pointwise limit of an increasing net (ψi ) in
CPSH(ω). By Dini’s lemma, ψi → Qω (ϕ) uniformly on X an , and hence Qω (ϕ) ∈ PSH(ω),
by Theorem 4.7. This proves (ii).
   Consider finally a net (ϕj ) as in (iii). We trivially have limj Pω (ϕj ) = supj Pω (ϕj ) ≤
Pω (ϕ). Pick ε > 0 and ψ ∈ CPSH(ω) such that ψ ≤ ϕ. As above, for all j large enough
we have ψ ≤ ϕj + ε, and hence ψ ≤ Pω (ϕj ) + ε. Thus Pω (ϕ) ≤ supj Pω (ϕj ), and we are
done.                                                                                         


# PRIMARY exact literal unit

   In this section, X denotes a projective variety of dimension n, with irreducible components
Xα . We extend the energy pairing to arbitrary psh functions, and use this to define functions
of finite energy, and the mixed Monge–Ampère operator thereon.
7.1. Extending the energy pairing. In §3.2, the energy pairing
                                  (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ∈ R
was defined for pairs (θi , ϕi ) ∈ N1 (X) × PLR . When the ϕi are θi -psh, this is an increasing
function of the ϕi , by Lemma 3.15. On the other hand, any ω-psh function with ω ∈
Amp(X) can be written as a decreasing limit of functions in Hdom (ω) ⊂ PL ∩ PSH(ω) (see
Theorem 4.15). This allows to extend the energy pairing by monotonicity, as follows.
                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                                       75

Theorem 7.1. For each (n + 1)-tuple ω0 , . . . , ωn ∈ Amp(X), the energy pairing
                           (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )
admits a unique extension to a map ni=0 PSH(ωi ) → R ∪ {−∞} that is
                                          Q

     • upper semicontinuous;
     • increasing in each variable.
Furthermore, this map is continuous along decreasing nets, and satisfies
                  (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =             inf             (ω0 , ψ0 ) · . . . · (ωn , ψn )              (7.1)
                                                       ψi ∈Hdom (ωi ), ψi ≥ϕi
                  Q
for all (ϕi ) ∈       i PSH(ωi ).

Proof. Any map that is both usc and increasing is automatically continuous along decreasing
nets. Since all functions in PSH(ωi ) are limits of decreasing nets in Hdom (ωi ) ⊂ PL(X) ∩
PSH(ωi ), uniqueness is clear. To prove existence, it suffices to show that (7.1) has the
required properties.
  Monotonicity is obvious. To prove upper semicontinuity, suppose that ϕi ∈ PSH(ωi ),
0 ≤ i ≤ n, and t ∈ R satisfy
                                (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) < t,
By definition, we can choose ψi ∈ Hdom (ωi ) and 0 < ε  1 such that ϕi ≤ ψi and
                                        (ω0 , ψ0 ) · . . . · (ωn , ψn ) < t − ε.
Set                                          X
                                     C :=     (ω0 · . . . · ωbi · . . . · ωn ) > 0.
                                               i
By Proposition 4.28, ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi ), and we can thus find an
open neighborhood Ui of ϕi in PSH(ωi ) such that ϕ0i ≤ ψi + εC −1 for all ϕ0i ∈ Ui . By
monotonicity of the energy pairing and Proposition 3.14, this gives
                   (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n ) ≤ (ω0 , ψ0 + εC −1 ) · . . . · (ωn , ψn + εC −1 )
                                = (ω0 , ψ0 ) · . . . · (ωn , ψn ) + ε < t
         0
for all ϕi ∈ Ui , which proves upper semicontinuity.                                                                             
Proposition 7.2. The energy pairing (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is symmetric and R>0 -linear
with respect to each variable (ωi , ϕi ) with ωi ∈ Amp(X) and ϕi ∈ PSH(ωi ). Furthermore,

                                                                                    n
                                                                                    X
 (ω0 , ϕ0 + c0 ) · . . . · (ωn , ϕn + cn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) +            ci (ω0 · . . . · ωbi · . . . · ωn )X (7.2)
                                                                                    i=0
for all ci ∈ R,
                         (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ) = t(ω0 , ϕ0 ) · . . . · (ωn , ϕn )                          (7.3)
for all t ∈ R>0 ,
                                                          X
                   (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =              (ω0 , ϕ0 )|Xα · . . . · (ωn , ϕn )|Xα ,                    (7.4)
                                                       dim Xα =n
and
                 (ν ? ω0 , ν ? ϕ0 ) · . . . · (ν ? ωn , ν ? ϕn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn )                           (7.5)
with ν : X ν → X the normalization morphism.
76                                 SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. Using approximation by decreasing nets in Hdom (ωi ), everything is clear from Propo-
sition 3.14, except that this only provides a proof of (7.3) for t ∈ Q>0 . To get the general
case, we may replace ϕi with ϕi − sup ϕi and assume ϕi ≤ 0 for all i. Write a given t ∈ R>0
as the limit of an increasing sequence tm ∈ Q>0 . For each i, (tm · ϕi )m is a decreasing
sequence in PSH(ωi ) that converges to t · ϕi , and hence
                    lim (ω0 , tm · ϕ0 ) · . . . · (ωn , tm · ϕn ) = (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ).
                   m→∞
The result follows.                                                                                                           
     We also record the following useful monotonicity property with respect to ωi .
Proposition 7.3. For i = 0, . . . , n, pick ωi , ωi0 ∈ Amp(X) such that ωi0 ≥ ωi , and ϕi ∈
PSH(ωi ) ⊂ PSH(ωi0 ). Then
   (i) if ϕi ≤ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≤ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≤ 0;
  (ii) if ϕi ≥ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≥ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≥ 0.
Proof. By monotone approximation, we may assume ϕi ∈ PL ∩ PSH(ωi ). By assumption,
θi := ωi0 − ωi is nef. The result thus follows by expanding out
                 (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) = ((ω0 , ϕ0 ) + (θ0 , 0)) · . . . · ((ωn , ϕn ) + (θn , 0))
and applying Corollary 3.16.                                                                                                  
  For any θ ∈ N1 (X), recall that CPSH(θ) = C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) respectively denote
the sets of continuous and bounded θ-psh functions. We conclude this section with a general
continuity result for the energy pairing involving such functions. It is an analogue of the
Chern–Levine–Nirenberg inequality in the complex case.
Theorem 7.4. For all ω0 , . . . , ωn ∈ Amp(X), the energy pairing
                                      (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )
is finite-valued and continuous on PSH(ω0 )× ni=1 CPSH(ωi ) with its natural topology (point-
                                                              Q

# PRIMARY exact literal unit

                                    (ϕ0j , ϕ1j , . . . , ϕnj ) → (ϕ0 , ϕ1 , . . . , ϕn )
                   Qn
in PSH(ω0 ) × i=1 CPSH(ωi ), so that ϕ0j → ϕ0 in PSH(ω0 ) (i.e. pointwise on X div ) and
ϕij → ϕi uniformly for i ≥ 1. Write
  (ω0 , ϕ0j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0 ) · . . . · (ωn , ϕn )
            = [(ω0 , ϕ0j ) · (ω1 , ϕ1j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0j ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn )]
                         + [(ω0 , ϕ0j ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn )] .
By (7.6), the first term tends to 0 as j → ∞, while the previous step of the proof shows
that the second term tends to 0 as well, so we are done.                              
7.2. Functions of finite energy.
Definition 7.6. For each ω ∈ Amp(X), we define the Monge–Ampère energy functional
                                            Eω : PSH(ω) → R ∪ {−∞}
by setting, for ϕ ∈ PSH(ω),
                                             (ω, ϕ)n+1
                                               Eω (ϕ) :=  .                                                            (7.9)
                                            (n + 1)(ω n )
We say that ϕ has finite energy if Eω (ϕ) > −∞.
  We denote by
                                       E 1 (ω) ⊂ PSH(ω)
the set of ω-psh functions of finite energy.
78                                SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proposition 7.7. For each ω ∈ Amp(X), the functional Eω : PSH(ω) → R∪{−∞} satisfies:
    (i) Eω is increasing, concave, usc, and continuous along decreasing nets;
   (ii) Eω (ϕ + c) = Eω (ϕ) + c for ϕ ∈ PSH(ω) and c ∈ R;
  (iii) for each ϕ ∈ PSH(ω) and t ∈ R>0 we have Eω (t·ϕ) = t Eω (ϕ) and Etω (tϕ) = t Eω (ϕ);
  (iv) for each ϕ ∈ PSH(ω) we have
                                   X
                          Eω (ϕ) =    cα Eω|Xα (ϕ|Xαan ) = Eν ? ω (ν ? ϕ)             (7.10)
                                                       α
           with cα    := (ω n )   Xα   /(ω n )   X and ν : X
                                                               ν → X the normalization morphism.
                                                                      P
     Note that cα > 0 iff Xα is top-dimensional, and                      α cα = 1.

Proof. Concavity follows from Theorem 3.25, by monotone approximation. The rest of (i)–
(ii) and the first half of (iii) are consequences of Proposition 7.2. Pick ϕ ∈ PSH(ω). For any
t ∈ R>0 , tϕ ∈ PSH(tω) satisfies
                                              (tω, tϕ)n+1        (ω, ϕ)n+1
                           Etω (tϕ) =                       = t               = t Eω (ϕ),
                                            (n + 1)((tω)n )     (n + 1)(ω n )
which concludes the proof of (iii). Finally, (iv) is a consequence of (7.4).                       
Theorem 7.8. Given ample classes ω, ω 0 , ω0 , . . . , ωn ∈ Amp(X), we have:
    (i) E 1 (ω) is a convex subset of PSH(ω), and contains all bounded ω-psh functions;
   (ii) E 1 (ω) is stable under addition of a constant and the scaling action of R>0 ;
  (iii) if ϕ ∈ E 1 (ω), then any ψ ∈ PSH(ω) such that ψ ≥ ϕ is also in E 1 (ω);
  (iv) if ω ≤ ω 0 then E 1 (ω) ⊂ E 1 (ω 0 );
   (v) E 1 (tω) = t E 1 (ω) for all t ∈ R>0 , and
                                             E 1 (ω) + E 1 (ω 0 ) ⊂ E 1 (ω + ω 0 );
      (vi) if ϕi ∈ E 1 (ωi ), i = 0, . . . , n, then (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is finite;
     (vii) if ϕ ∈ PSH(ω) then
                    ϕ ∈ E 1 (ω) ⇐⇒ ν ? ϕ ∈ E 1 (ν ? ω)
                    ⇐⇒ ϕ|Xαan ∈ E 1 (ω|Xα ) for all top-dimensional components Xα .
Lemma 7.9. Pick ω, ω 0 ∈ Amp(X) and t ≥ 1 such that ω ≤ ω 0 ≤ tω. For all nonpositive
ϕ ∈ PSH(ω) ⊂ PSH(ω 0 ) we have
                                   0 ≥ (ω, ϕ)n+1 ≥ (ω 0 , ϕ)n+1 ≥ tn (ω, ϕ)n+1 .
Proof. By Proposition 7.3 we have
                      0 ≥ (ω, ϕ)n+1 ≥ (ω 0 , ϕ)n+1 ≥ (tω, ϕ)n+1 = tn+1 (ω, t−1 ϕ)n+1 .
Since ϕ ∈ PSH(ω) and t−1 ∈ [0, 1], concavity of the energy yields (ω, t−1 ϕ)n+1 ≥ t−1 (ω, ϕ)n+1 ,
and the result follows.                                                                      
Lemma 7.10. Pick r ≥ 1, ω0 , . . . , ωr ∈ Amp(X), 0 ≥ ϕi ∈ PSH(ωi ) for i = 0, . . . , r.

# PRIMARY exact literal unit

pointwise, and
                     ˆ                   ˆ                                
                                                            0
                          f µ = inf            g µ | g ∈ C (X), g ≥ f          ∈ R ∪ {−∞}.        (7.13)

   We will sometimes need to rely on the following monotone convergence theorem for (pos-
sibly uncountable) nets of usc functions, a simple consequence of (7.13) and Dini’s lemma
(see for instance [Fol99, Proposition 7.12]).
Lemma 7.17. If µ is a Radon measure on X an and (fj )j a decreasing
                                                             ´      ´net of usc functions
    an
on X , converging pointwise to a (usc) function f , then limj fj µ = f µ.
  More generally, continuous linear forms in C0 (X)∨ correspond to signed Radon mea-
sures on X an . Any such measure can be written as a difference of Radon measures, and
Lemma 7.17 thus applies as well when µ is a signed measure.
  With these preliminaries in hand, we now generalize the construction of mixed Monge–
Ampère measures, introduced in §3.2 in the PL case.
Theorem 7.18. For each n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , i = 1, . . . , n, there exists a unique
signed measure
                                                      ^
             (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ) = (θi + ddc ϕi ) ∈ C0 (X)∨              (7.14)
                                                                    i
such that             ˆ             ^
                                ϕ    (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )    (7.15)
                         X an        i
for all ϕ ∈ PL(X)R . If further θi ∈ Nef(X) and ϕi ∈ PSH(θi ) for i = 1, . . . , n, then (7.14)
is a positive measure.
  While the notation mimics the one for mixed Monge–Ampère measures in the complex
analytic case, we will not define the individual factors θi + ddc ϕi . At least if the ϕi are
continuous, this could, however, be done using the approach in [CLD12] (cf. Remark 7.23
below).
Proof. By density of PL(X) in C0 (X) (see Theorem 2.2), the prescription (7.15) uniquely
determines the measure (7.14). To show existence, we may assume, by multilinearity, that
θi ∈ Nef(X) and ϕi ∈ E~1 ∩ PSH(θi ) for i = 1, . . . , n. Since any ϕ ∈ PL(X)R can be written
as a difference of functions in PLR ∩ PSH(ω) for some ω ∈ Amp(X) (see (3.2)), Lemma 7.15
shows that ϕ 7→ (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ) is a positive linear form on PL(X)R . By density
of PL(X)R in C0 (X), it thus uniquely extends to a positive linear form on C0 (X), and we
are done.                                                                                              
82                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proposition 7.19. Mixed Monge–Ampère measures satisfy the following properties:
   (i) the signed measure i (θi + ddc ϕi ) is a symmetric and multilinear function of the
                              V

       n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , of total mass
                             ˆ     ^
                                     (θi + ddc ϕi ) = (θ1 · . . . · θn )X ;
                                       X an i

     (ii) assume (θi , ϕi ) ∈ N1 (X) × PLR , and pick an integrally closed test configuration X
          dominating Xtriv and Di ∈ VCar(X )R such that ϕi = ϕDi ; then
                                   ^                   X
                                      (θi + ddc ϕi ) =   cE δvE ,
                                           i                          E

          where E ranges over the irreducible components of X0 and
                         cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E ;
     (iii) for all (θi , ϕi ) ∈ N1 (X) × E~1 and t ∈ R>0 we have
                                 ^                           ^
                                    (θi + ddc (t · ϕi )) = t? (θi + ddc ϕi ),                    (7.16)
                                   i                                   i
                        ^                              X        ^
                             (θi + ddc ϕi ) =                          θi |Xα + ddc ϕi |Xαan ,
                                                                                            
                                                                                                 (7.17)
                         i                          dim Xα =n i
                              ^                              ^
                                       (θi + ddc ϕi ) = ν?          (ν ? θi + ddc ν ? ϕi ) ,     (7.18)
                               i                                i
          with ν : X ν → X the normalization;
     (iv) for any ω ∈ Amp(X), the map E 1 (ω)n 3 (ϕ1 , . . . , ϕn ) 7→ i (θi +ddc ϕi ) is continuous
                                                                      V
          along decreasing nets;
      (v) for all (θi , ϕi ) ∈ N1 (X) × E~1 and ϕ ∈ E~1 , ϕ is integrable against i (θi + ddc ϕi ),
                                                                                   V
          and (7.15) holds.
  When ϕi = 0 for some i, we drop the term ddc ϕi from the notation. As a special case of
Proposition 7.19 (ii), we then have
                                          X
                        θ1 ∧ · · · ∧ θn =   (θ1 · . . . · θn )Xα δvtriv,α .        (7.19)
                                                    dim Xα =n

Proof of Proposition 7.19. Points (i) and (iii) follow from Proposition 7.2, while (ii) is a
reformulation of (3.5). By density of PL(X) in C0 (X), (iv) is equivalent to the fact that,
for each ϕ ∈ PL(X),
                                 ˆ  ^
            (ϕ1 , . . . , ϕn ) 7→ ϕ   (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )
                                                i

is continuous along decreasing nets in E 1 (ω)n+1 . Now ϕ can be written as a difference of
functions in PL ∩ PSH(ω 0 ) for some ω 0 ∈ Amp(X), and the desired continuity is thus a
consequence of Theorem 7.14. To prove (v), we may assume θi ∈ Amp(X) and ϕi ∈ E 1 (θi ),
by multilinearity. Any ϕ ∈ E 1 (ω) with ω ∈ Amp(X) can be written as the pointwise limit
of a decreasing net in PL ∩ PSH(ω), and (7.15) thus holds for ϕ, by monotone convergence
and the continuity of the energy pairing along decreasing limits.                        
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                 83

Example 7.20. Assume X is a smooth curve and pick ω ∈ Amp(X). By Example 4.13,
any ϕ ∈ PSH(ω) determines a positive Radon measure (deg ω)δvtriv + ∆ϕ, with
              X d                                                     d2
                                                                                     
                                             d
        ∆ϕ =              ϕ(t ordp )δvtriv −       ϕ(t ordp )δvp,triv + 2 ϕ(t ordp )
                    dt 0+                    dt +∞                     dt
                 p∈X(k)

the tree Laplacian (see [FJ04, §7]). As we saw in Example 3.19, we have ω + ddc ϕ =
(deg ω)δvtriv + ∆ϕ for any ϕ ∈ PLR ∩ PSH(ω), and this remains true for any ϕ ∈ E 1 (ω),
by monotone approximation. For such functions, ω + ddc ϕ further puts no mass on the
endpoints vp,triv , which means that the convex function t 7→ ϕ(t ordp ) has sublinear growth
(see respectively Corollary 7.49 and Theorem 11.11).
Proposition 7.21. Pick ωi ∈ Amp(X) and ϕi ∈ E 1 (ωi ), i = 1, . . . , n, and choose also
ω0 ∈ Amp(X) and ϕ0 ∈ PSH(ω0 ). Then:
    (i) ϕ0 is integrable with respect to µ := i (ωi + ddc ϕi ) iff (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) > −∞,
                                             V
        and this holds as soon as ϕi is bounded for i = 1, . . . , n;
   (ii) assume ϕ0 ∈ L1 (µ). Pick for i = 0, . . . ,Vn a decreasing net (ϕij )j in PSH(ωi ) that
        converges pointwise to ϕi , and set µj := i (ωi + ddc ϕij ). Then ϕ0j ∈ L1 (µj ) for all
        j, and ϕ0j µj → ϕ0 µ weakly in C0 (X)∨ .
Lemma 7.22. Let K be a compact topological space with a weakly convergent net of positive
Radon measures µj → µ. Assume also given an increasing net of lsc             ´ fj : K →
                                                                     ´ functions
R ∪ {+∞} such that fj ∈ L1 (µj ) for all j, f := limj fj ∈ L1 (µ) and fj µj → f µ. Then
fj µj → f µ weakly in C0 (K)∨ .
Proof. Being lsc, each fj is bounded below, and the increasing net (fj ) is thus ultimately
bounded below. Since ´µj → µ, we may therefore assume, after adding a constant, that
fj ≥ 0 for all j. Since fj µj converges, the positive measures σj := fj µj stay in a fixed
weakly compact subset of C0 (X)∨ , and it suffices
                                              ´ to show
                                                      ´    that any
                                                                 ´ limit ´point σ∞ of σj
must coincide with σ := f µ. By assumption, σj → σ, hence σ∞ = σ, and it will
thus be enough to show that σ∞ ≥ σ. To this end, pick 0 ≤ g ∈ C0 (K). For all j ≥ k we
have fj ≥ fk , and hence       ˆ       ˆ           ˆ
                                      g σj =    gfj µj ≥      gfk µj .
                                                                                    ´            ´
By lower semicontinuity of gfk and the weak convergence µj → µ, we infer                g σ∞ ≥       gfk µ.
Using monotone convergence, this now yields in turn,
                                ˆ         ˆ         ˆ
                                   g σ∞ ≥ gf µ = g σ,

which concludes the proof.                                                                               
Proof of Proposition 7.21. Set c := (ω0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) ∈ R, and pick a decreasing
net (ϕ0j ) in PL ∩ PSH(ω0 ) such that ϕ0j → ϕ0 pointwise. By construction of µ, we have for
each j                         ˆ
                                  ϕ0j µ = (ω0 , ϕ0j ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − c.
                         ´           ´
By Lemma 7.17, ϕ0j µ → ϕ0 µ. By Theorem 7.1, we have on the other hand (ω0 , ϕ0j ) ·
(ω1 , ϕ1 ) · . . . · (ωn , ϕn ) → (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ). Thus
                                ˆ
                                   ϕ0 µ = (ω0 , ϕ0 ) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − c,
84                            SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

and (i) follows.
  We turn to (ii). By Proposition 7.19 (iv), we have µj → µ. Further,
            ˆ
              ϕ0j µj = (ω0 , 0) · (ω1 , ϕ1j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0j ) · . . . · (ωn , ϕnj )

is finite for each j, and converges to
                ˆ
                  ϕ0 µ = (θ0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ0 ) · . . . · (ωn , ϕn ).

The result is now a consequence of Lemma 7.22.                                                                
Remark 7.23. For continuous ω-psh functions, mixed Monge–Ampère measures can also be
defined using the general theory developed by Chambert-Loir and Ducros [CLD12]. By base
change invariance of their theory, it follows from Proposition 7.19 (ii) and [BE20, Theorem
8.18] that the present approach is compatible with [CLD12] for continuous ω-psh functions.
7.4. The Monge–Ampère operator and energy functionals. In this section we fix
ω ∈ Amp(X). We denote by V := (ω n ) its volume, and write E 1 := E 1 (ω) and E := Eω .
Definition 7.24. The Monge–Ampère operator takes ϕ ∈ E 1 to the Radon probability
measure
                      MA(ϕ) = MAω (ϕ) := V −1 (ω + ddc ϕ)n
on X an .
Definition 7.25. For any two ϕ, ψ ∈ E 1 we set
                                                                      ˆ
                         Jψ (ϕ) = Jω,ψ (ϕ) = E(ψ) − E(ϕ) +                (ϕ − ψ) MA(ψ)

and
                                                      ˆ
                           I(ϕ, ψ) = Iω (ϕ, ψ) =          (ϕ − ψ) (MA(ψ) − MA(ϕ))
                                                   = Jψ (ϕ) + Jϕ (ψ).

 Note that Jψ (ϕ) and I(ϕ, ψ) are both invariant under translation of ϕ, ψ by constants.
When ψ = 0 we simply write
                                      ˆ             ˆ
                     I(ϕ) := I(ϕ, 0) = ϕ MA(0) − ϕ MA(ϕ)

# PRIMARY exact literal unit

                               1                       n
                             n+1 I(ϕ, ψ) ≤ Jψ (ϕ) ≤ n+1 I(ϕ, ψ);                       (7.28)
                          V −1 dω (ϕ, ψ) ≈ I(ϕ, ψ) ≈ Jψ (ϕ) ≈ Jϕ (ψ);                  (7.29)
                              I(ϕ1 , ϕ2 ) . I(ϕ1 , ϕ3 ) + I(ϕ3 , ϕ2 ).                 (7.30)
Proof. As in Lemma 3.26, (7.22), (7.24), (7.25) and (7.27) follow from straightforward com-
putations based on the multilinearity and symmetry of the energy pairing on E 1 , while (7.26)
follows from (7.4). Equation (7.23) follows from (3.16) by monotone approximation. Equa-
tions (7.25) and (7.27) imply (7.28) and (7.29), and (7.30) is now a consequence of Theo-
rem 3.31 and monotone approximation.                                                        
  Taking into account (7.24), we can write (7.28) as
                        E(ψ) + E0 (ψ)(ϕ − ψ) − E(ϕ) ≥ n+1
                                                       1
                                                          I(ϕ, ψ),                     (7.31)
which can be seen as a strict concavity property of E with respect to I. Indeed, it yields the
following uniform concavity estimate:
Theorem 7.28. For any two ϕ, ψ ∈ E 1 and t ∈ [0, 1] we have
                E((1 − t)ϕ + tψ) − ((1 − t) E(ϕ) + t E(ψ)) & t(1 − t) I(ϕ, ψ).
  The proof relies on the following elementary estimate, which is certainly well-known.
Lemma 7.29. For all a, b ∈ R≥0 and t ∈ [0, 1] we have (1 − t)a + tb ≥ t(1 − t)(a + b).
86                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. By homogeneity we may assume a + b = 1. Write t = 21 + x and a = 12 + y with
x, y ∈ [− 12 , 21 ], where we may assume x ≥ 0, by symmetry. Then
              1      1        1      1     1                    1    1       1
(1−t)a+tb = ( −x)( +y)+( +x)( −y) = −2xy, t(1−t)(a+b) = ( +x)( −x) = −x2 ,
              2      2        2      2     2                    2    2       4
and hence
                                       1            1 1           1
      (1 − t)a + tb − t(1 − t)(a + b) = − 2xy + x2 ≥ − x + x2 = ( − x)2 ≥ 0.
                                       4            4 2           2
                                                                               

Proof of Theorem 7.28. Set ϕt := (1 − t)ϕ + tψ. By (7.31), we have
                              ˆ
                      E(ϕt ) + (ϕ − ϕt ) MA(ϕt ) − E(ϕ) & I(ϕ, ϕt )

and                                    ˆ
                            E(ϕt ) +       (ψ − ϕt ) MA(ϕt ) − E(ψ) & I(ϕt , ψ),

Since (1 − t)(ϕ − ϕt ) + t(ψ − ϕt ) = 0, this yields
                    E(ϕt ) − ((1 − t) E(ϕ) + t E(ψ)) & (1 − t) I(ϕ, ϕt ) + t I(ψ, ϕt )

                           ≥ t(1 − t) (I(ϕ, ϕt ) + I(ϕt , ψ)) & t(1 − t) I(ϕ, ψ),
by Lemma 7.29 and (7.30).                                                                                             

  For later use, we record the following crucial consequence of Corollary 3.34 (compare [BBGZ13,
Lemma 3.13]).
Lemma 7.30. For all ϕ, ϕ0 , ψ, ψ 0 ∈ E 1 we have
  ˆ
                                                        1                                  1
    (ϕ − ϕ0 ) MA(ψ) − MA(ψ 0 ) . I(ϕ, ϕ0 )αn I(ψ, ψ 0 ) 2 max{J(ϕ), J(ϕ0 ), J(ψ), J(ψ 0 )} 2 −αn
                               


with αn := 2−n .
Proof. After regularization, we may assume ϕ, ϕ0 , ψ, ψ 0 ∈ PLR ∩ PSH(ω). Note that
    ˆ
  V (ϕ − ϕ0 ) MA(ψ) − MA(ψ 0 ) = (0, ϕ − ϕ0 ) · (ω, ψ)n − (0, ϕ − ϕ0 ) · (ω, ψ 0 )n
                                 

                                                    n−1
                                                    X
                                                =         (0, ϕ − ϕ0 ) · (0, ψ − ψ 0 ) · (ω, ψ)j · (ω, ψ 0 )n−1−j .
                                                    j=1

By the Cauchy–Schwarz inequality (3.17) we infer

     (0, ϕ − ϕ0 ) · (ω, ψ)n − (ϕ − ϕ0 ) · (ω, ψ 0 )n
                     . max kϕ − ϕ0 k(ω,ψ)j ·(ω,ψ0 )n−1−j kψ − ψ 0 k(ω,ψ)j ·(ω,ψ0 )n−1−j
                                                                                        
                        j
                                                                                         
                                                                                                  1
                                                  ≤ max kϕ − ϕ k(ω,ψ)j ·(ω,ψ0 )n−1−j dω (ψ, ψ 0 ) 2
                                                                     0
                                                                 j

and Corollary 3.34 together with (7.29) yield the desired estimate.                                                   
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      87

Corollary 7.31. For all ϕ, ϕ0 , ψ ∈ E 1 we have
                  | Jψ (ϕ) − Jψ (ϕ0 )| . I(ϕ, ϕ0 )αn max{J(ϕ), J(ϕ0 ), J(ψ)}1−αn
with αn = 2−n .
Proof. Set M := max{J(ϕ), J(ϕ0 ), J(ψ)}. We have
                                 ˆ                          ˆ
Jψ (ϕ) − Jψ (ϕ ) = E(ϕ ) − E(ϕ) + (ϕ − ϕ ) MA(ψ) = Jϕ0 (ϕ) + (ϕ − ϕ0 )(MA(ψ) − MA(ϕ0 )),
              0       0                  0



# PRIMARY exact literal unit

Proof. By multilinearity, we can assume wlog θi ≥ ω for all i, and hence E 1 (ω) ⊂ E 1 (θi ).
                                                                                    i ≥ p. The
We proceed by induction on p = 0, . . . , n such that ϕij = ϕi is a constant net forQ
case p = 0 is trivial, so assume p ≥ 1. By monotonicity of the energy pairing on i PSH(θi )
(see Theorem 7.1), j 7→ (θ0 , ϕ0j ) · . . . · (θn , ϕnj ) is increasing, and
                         lim(θ0 , ϕ0j ) · . . . · (θn , ϕnj ) ≤ (θ0 , ϕ0 ) · . . . · (θn , ϕn ).
                           j

Conversely, pick j ≥ l. Then ϕ0j ≥ ϕ0l , and hence
                    (θ0 , ϕ0j ) · . . . · (θn , ϕnj ) ≥ (θ0 , ϕ0l ) · (θ1 , ϕ1j ) · . . . · (θn , ϕnj ).
Using the inductive assumption, we infer
                   lim(θ0 , ϕ0j ) · . . . · (θn , ϕnj ) ≥ (θ0 , ϕ0l ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )
                     j
                 GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                       91
                                                         ˆ
          = (θ0 , 0) · (θ1 , ϕ1 ) · . . . · (θ, ϕn ) +       ϕ0l (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ).

Since Jθ0 (ϕ0l ) = sup ϕ0l − Eθ0 (ϕ0l ) is ultimately bounded, Lemma 7.37 next shows that
      ˆ                                               ˆ
  lim ϕ0l (θ1 + dd ϕ1 ) ∧ · · · ∧ (θn + dd ϕn ) = ϕ0 (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ).
                      c                        c
   l

Thus
                      lim(θ0 , ϕ0j ) · . . . · (θn , ϕnj ) ≥ (θ0 , 0) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )
                       j
             ˆ
         +       ϕ0 (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ) = (θ0 , ϕ0 ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ),
and we are done.                                                                                                  
Remark 7.39. Lemma 7.37 and Theorem 7.38 remain valid when X is reducible, by (7.17)
and (7.4), respectively.
7.6. Locality and the comparison principle. The next result and its consequences play a
crucial role in analyzing deep properties of ω-psh functions and the Monge-Ampère operator.
Theorem 7.40. If ω ∈ Amp(X), then
                                1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)                                     (7.32)
for all ϕ, ϕ0 ∈ E 1 (ω).
  A first consequence is the fact that the mixed Monge–Ampère operator is local in nature,
something that is not an immediate consequence of our definition in §7.3.
Corollary 7.41. Let G ⊂ X an be open set. If ωi ∈ Amp(X) and ϕi , ψi ∈ E 1 (ωi ), 1 ≤ i ≤ n,
are such that ϕi = ψi on G, then
       (ω1 + ddc ϕ1 ) ∧ · · · ∧ (ωn + ddc ϕn ) = (ω1 + ddc ψ1 ) ∧ · · · ∧ (ωn + ddc ψn ) on G.
In particular, if ω ∈ Amp(X) and ϕ, ϕ0 ∈ E 1 (ω) are such that ϕ = ϕ0 on G, then MA(ϕ) =
MA(ϕ0 ) on G.
Proof. By multilinearity, it suffices to prove the final statement. As in [BFJ15, Corollary 5.2],
given ε > 0 we apply Theorem 7.40 to ϕ+ε and ϕ0 . This gives MA(max{ϕ+ε, ϕ0 }) = MA(ϕ)
on G ⊆ {ϕ+ε > ϕ0 }. Letting ε → 0 gives MA(max{ϕ, ϕ0 }) = MA(ϕ) on G, since the Monge–
Ampère operator is continuous under decreasing limits. Exchanging the roles of ϕ and ϕ0
completes the proof.                                                                           
Remark 7.42. As mentioned in Remark 7.23, when all the functions involved are continu-
ous, the mixed Monge–Ampère measure coincides with the one in [CLD12]. Since the latter
is local in nature, Theorem 7.40 and Corollary 7.41 follow in this case. However, for appli-
cations it is important to consider functions ϕ, ϕ0 that are not continuous, and in this case
the Borel set {ϕ > ϕ0 } can be quite complicated. By definition, it is an open subset in the
plurifine topology, see [BT87].
Lemma 7.43. Let ϕ, ϕ0 ∈ PL(X), and pick an integrally closed test configuration X such
that ϕ, ϕ0 and ϕ00 := max{ϕ, ϕ0 } are associated to elements D, D0 , D00 of VCar(X )Q . Pick
an irreducible component E of X0 , and assume that ϕ(vE ) > ϕ0 (vE ). Then ϕ(vF ) ≥ ϕ0 (vF )
for any irreducible component F of X0 that intersects E.
92                          SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. First, ϕD00 −D = ϕD00 − ϕD ≥ 0 implies D00 − D ≥ 0, by Lemma 2.8, and similarly
D00 − D0 ≥ 0. Furthermore, 0 < ϕ00 (vE ) − ϕ0 (vE ) = σ(vE )(D00 − D0 ), and E is thus in the
support of D00 − D0 . Now pick any k × -invariant divisorial valuation w on X with center
ξ ∈ E ∩ F , normalized by w(X0 ) = 1; denote by v ∈ X div its restriction to k(X) ,→ k(X ), so
that w = σ(v) (see §1.3). Then w(D00 − D0 ) = ϕ00 (v) − ϕ0 (v) > 0, and hence ϕ00 (v) = ϕ(v).
This means that D00 = D at ξ; hence 0 = σ(vF )(D00 − D) = ϕ00 (vF ) − ϕ(vF ), which proves
the result.                                                                                 
Proof of Theorem 7.40. First assume that ϕ, ψ ∈ PL ∩ PSH(ω). As in Lemma 7.43, pick
an integrally closed test configuration X dominating the trivial one, such that ϕ = ϕD ,
ϕ0 = ϕD0 and max{ϕ, ϕ0 } = ϕD00 with D, D0 , D00 ∈ VCar(X )Q . As in Proposition 7.19 (ii)
we have                                  X
                         MA(ϕD ) = V −1     bE ((ωX + D)|E )n δvE ,
                                                   E
and a similar formula holds for MA(ϕ ). We thus need to show that ((ωX + D)|E )n =
                                             D00
((ωX + D00 ])|E )n for any E with ϕD (vE ) > ϕD0 (vE ). Now Lemma 7.43 yields ϕD (vF ) =
max{ϕ(vF ), ϕ0 (vF )} = ϕD00 (vF ) for all components F of X0 that intersect E. This implies
that D and D00 coincide in a neighborhood of E. Hence D|E = D00 |E , which implies the
result.
   Now consider the general case. Set
                             f := max{ϕ − ϕ0 , 0} = max{ϕ, ϕ0 } − ϕ0 .
Then {ϕ > ϕ0 } = {f > 0}, and it thus suffices to prove that
                                  f MA(max{ϕ, ϕ0 }) = f MA(ϕ).                                   (7.33)
Indeed, multiplying by f −1 on {f > 0} will then yield the result.             Let (ϕj )j and (ϕ0j )j be
decreasing nets in PL ∩ PSH(ω) converging to ϕ and ϕ0 , respectively, and set
                            fj := max{ϕj − ϕ0j , 0} = max{ϕj , ϕ0j } − ϕ0j .
By the first part of the proof we have fj MA(max{ϕj , ϕ0j }) = fj MA(ϕj ), and (7.33) is now
a consequence of Proposition 7.19 (iii), since max{ϕj , ϕ0j } ∈ E 1 (ω) decreases to max{ϕ, ϕ0 }.
                                                                                               
     Using Theorem 7.40 we obtain the very useful comparison principle.
Theorem 7.44. If ω ∈ Amp(X) and ϕ, ψ ∈ E 1 (ω), then
                          ˆ                 ˆ
                              MA(ϕ) ≥           MA(ψ).
                                  {ϕ<ψ}                {ϕ<ψ}

Proof. We follow [GZ07, Theorem 1.5]. For any ε > 0 we have
      ˆ                         ˆ                                          ˆ
  1 = MA(max{ϕ, ψ − ε}) ≥             MA(max{ϕ, ψ − ε}) +                          MA(max{ϕ, ψ − ε})
                                    {ϕ<ψ−ε}                              {ϕ>ψ−ε}
                    ˆ                    ˆ                       ˆ                     ˆ
              =             MA(ψ) +             MA(ϕ) = 1 +              MA(ψ) −              MA(ϕ),
                  {ϕ<ψ−ε}             {ϕ>ψ−ε}                  {ϕ<ψ−ε}              {ϕ≤ψ−ε}

where the second equality follows from Theorem 7.40 and from MA(ϕ − ε) = MA(ϕ). We
complete the proof by letting ε → 0.                                             
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                          93

  Another simple consequence of Theorem 7.40 is the following formula for the I-functional.
Proposition 7.45. If ω ∈ Amp(X), and ϕ, ψ ∈ E 1 (ω), then max{ϕ, ψ} ∈ E 1 (ω), and
                          I(ϕ, ψ) = I (ϕ, max{ϕ, ψ}) + I (max{ϕ, ψ}, ψ) .                   (7.34)
Proof. The first assertion follows from Theorem 7.8 (iii). For the second, note that
                 ˆ
       I(ϕ, ψ) = (ϕ − ψ)(MA(ϕ) − MA(ψ))
                   ˆ                                 ˆ
               =       (ϕ − ψ)(MA(ϕ) − MA(ψ)) +            (ϕ − ψ)(MA(ϕ) − MA(ψ))
                  {ϕ>ψ}                                    {ψ>ϕ}
                  ˆ
              =        (max{ϕ, ψ} − ψ)(MA(max{ϕ, ψ}) − MA(ψ))
                  ˆ
              +       (max{ϕ, ψ} − ϕ)(MA(max{ϕ, ψ}) − MA(ϕ))
              = I (ϕ, max{ϕ, ψ}) + I (max{ϕ, ψ}, ψ) ,

# PRIMARY exact literal unit

                                                                          an ). By Proposition 8.3 (v),

we have
          E(ϕi ) = E↓ (ϕi ) & E↓ (ϕ)   and       E(ϕi |Xαan ) = E↓ (ϕi |Xαan ) & E↓ (ϕ|Xαan ),
and the first point follows. In the lsc case, the proof is similar, using an increasing net
instead.                                                                                 
8.3. Uniform differentiability of the energy. Building on [BGM20] we prove the fol-
lowing uniform differentiability result, which is crucial for what follows.
Theorem 8.5. Pick f ∈ PL(X)R . For any ϕ ∈ E 1 , we then have
                                          ˆ
                      ↓
                    E (ϕ + εf ) = E(ϕ) + ε f MA(ϕ) + O(ε2 )

as ε → 0, where the implicit constant in the O is uniform with respect to ϕ.
   If ϕ ∈ CPSH(ω) (and for any ϕ ∈ E 1 , if the envelope property holds), the left-hand side
satisfies
                       E↓ (ϕ + εf ) = E(ϕ + εf ) = E(P(ϕ + εf )),
by (8.7).
98                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Corollary 8.6. For any ϕ ∈ E 1 and f ∈ C0 (X) we have
                                               ˆ
                           d       ↓
                                 E (ϕ + tf ) = f MA(ϕ).
                          dt t=0

  Again, one can replace E↓ with E = E ◦ P if ϕ ∈ CPSH(ω), or if the envelope property
holds.
  For any ω ∈ Amp(X) we set Vω := (ω n ).
Lemma 8.7. Pick ω, ω 0 ∈ Amp(X), ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ), and set f := ψ1 − ψ2 . For
any ϕ ∈ CPSH(ω) we then have
                               ˆ
                            −1
                                                           n
                                 f ω + ω 0 + ddc (ϕ + ψ1 )    ≤ Vω−1 Vω+ω0 − 1 sup |f |.
                                                                              
    Eω (ϕ + f ) − Eω (ϕ) − Vω

Proof. We may assume ω = c1 (L), ω 0 = c1 (L0 ) for ample line bundles L, L0 on X, Indeed, by
homogeneity, we then obtain the case when L, L0 are ample Q-line bundles, and the general
case by a simple perturbation argument based on Proposition 8.1 (iii).
   Consider first any continuous function ρ ∈ C0 (X). For each m ∈ N, ρ defines a sup-norm
k · kmρ on H0 (X, mL), defined by
                                   kskmρ = sup |s|e−mρ .
                                             X an

This norm induces a norm det k · kmρ on the determinant line det H0 (X, mL). Comparing
with the trivial norm, we can and will think of det k · kmρ as a number. It now follows
from [CMac15] (see [BE20, Theorem 9.5]) that the volume
                                                1
                        volL (ρ) := − lim             log det k · kmρ
                                      m→∞ mh0 (mL)

exists in R. We claim that volL (ρ) = EL (ρ). Using [BE20, (9.7)] and (8.3), it is enough
to prove this when X is irreducible. When ρ ∈ CPSH(L), the equality holds by [BE20,
Theorem A] (or [BoJ18b, Lemma 4.5]). In the general case, this yields
                  EL (ρ) = sup {EL (ψ) | ψ ∈ CPSH(L), ψ ≤ ρ} ≤ volL (ρ),
by monotonicity of volL . On the other hand, Theorem 5.1.1 of [Reb21] (which is valid for
arbitrary non-Archimedean fields; see also [BoJ18b, Theorem 4.13] for the trivially valued
case) shows that
                                                           |s|
                           ρm := m−1 log       sup
                                             0
                                          s∈H (X,mL)\{0} ksk mρ

satisfies ρm ∈ PLR ∩ PSH(ω), ρm ≤ ρ and EL (ρm ) → volL (ρ); the claim follows.
   In particular, EL (ϕ + f ) = volL (ϕ + f ) and EL (ϕ) = volL (ϕ). The desired estimate is
now a consequence of Lemma 8.8 below, itself a reformulation of [BGM20, Lemma 3.2]. 
Lemma 8.8. Let L and L0 be ample line bundles on X, and set ω = c1 (L), ω 0 = c1 (L0 ).
Consider functions ϕ ∈ CPSH(ω), and ψ1 , ψ2 ∈ CPSH(ω 0 ). Set f := ψ1 − ψ2 ∈ C0 and
C := Vω+ω0 − Vω > 0. Then
               ˆ
    C inf
        an
           f≤      f (ω + ω 0 + ddc (ϕ + ψ1 ))n − Vω (volL (ϕ + f ) − volL (ϕ)) ≤ C sup f.
       X        X an                                                              X an
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      99

Proof. This is a reformulation in our context of [BGM20, Lemma 3.2] in the special case
of a trivially valued field k. The fact that k is trivially valued means that we can view ϕ,
ψ1 , ψ2 as continuous psh metrics on the Berkovich analytifications of the line bundles L and
L0 , respectively. The difference volL (ϕ + f ) − volL (ϕ) can be viewed as the relative volume
of the metrics ϕ + f and ϕ on L. Note that our current normalization of the volume differs
from the one in loc.cit. by a factor Vω = (Ln ).                                              
Proof of Theorem 8.5. We argue along the lines of the proof of [BGM20, Theorem 3.1].
Write ϕ ∈ E 1 as the limit of a decreasing net (ϕi ) in CPSH(ω). Then E(ϕi +εf ) → E↓ (ϕ+εf )
(by Proposition 8.3 (v)), E(ϕi ) → E(ϕ) (by continuity of E along decreasing nets in PSH(ω)),
and MA(ϕi ) → MA(ϕ) weakly (by Proposition 7.19).
  It is therefore enough to prove the result for ϕ ∈ CPSH(ω). Since f ∈ PL(X)R , we can
choose ω 0 ∈ Amp(X) and ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ) such that f = ψ1 − ψ2 . By Lemma 8.7
we have, for any ε > 0,
                                   ˆ
                                −1
                                                                    n
   Eω (ϕ + εf ) − Eω (ϕ) − εVω       f ω + ddc ϕ + ε(ω 0 + ddc ψ1 )

                                                                ≤ ε Vω−1 Vω+εω0 − 1 sup |f |.
                                                                                   

Now Vω−1 Vω+εω0 − 1 = O(ε), while
                                              n  
                               n             X  n j
Vω−1         c          0          c       −1
       ω + dd ϕ + ε(ω + dd ψ1 ) = MAω (ϕ)+Vω       ε (ω+ddc ϕ)n−j ∧(ω 0 +ddc ψ1 )j ,
                                                 j
                                                          j=1

where (ω + ddc ϕ)n−j ∧ (ω 0 + ddc ψ1 )j is a Radon measure of mass (ω n−j · ω 0j ). The result
follows.                                                                                    
Proof of Corollary 8.6. For f ∈ PL(X)R the result follows directly from Theorem 8.5. For
an arbitrary f ∈ C0 (X) we argue as in the proof of [BGM20, Theorem 3.1]. By Theorem 2.2,
we can pick a sequence (fm ) in PL(X)R such that εm := sup |f − fm | → 0. For each t > 0,
we have fm − tεm ≤ f ≤ fm + tεm ; Proposition 8.3 (i) thus yields
                  E↓ (ϕ + tfm ) − tεm ≤ E↓ (ϕ + tf ) ≤ E↓ (ϕ + tfm ) + tεm ,
and hence          ˆ                                                 
                     fm MA(ϕ) − εm ≤ lim inf t−1 E↓ (ϕ + tf ) − E↓ (ϕ)
                                           t→0+
                                                     ˆ
                             −1    ↓             ↓
                 ≤ lim sup t      E (ϕ + tf ) − E (ϕ) ≤ fm MA(ϕ) − εm ,
                       t→0+
by Theorem 8.5 applied to fm . Letting m → ∞, we get
                                                    ˆ
                            −1    ↓             ↓
                      lim t      E (ϕ + tf ) − E (ϕ) = f MA(ϕ),
                            t→0+

and replacing f with −f concludes the proof.                                                 

                                       9. Measures of finite energy
   Denote as above by X a projective variety of dimension n, and fix an ample class ω ∈
Amp(X). We define the Monge–Ampère energy of a probability measure on X an , and begin
a study of the space of measures of finite energy.
100                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

9.1. The energy of a measure. Denote by M = M(X) the space of Radon probability
measures on X an . It is a compact convex subset of the dual C0 (X)∨ for the weak topology.
Fix a class ω ∈ Amp(X).
Definition 9.1. The energy of a Radon probability measure µ ∈ M is defined by
                                                 ˆ     
                  E∨ (µ) := E∨
                             ω (µ) := sup  E(ϕ) −   ϕ µ   ∈ [0, +∞].                       (9.1)
                                                  ϕ∈E 1

We say that µ has finite energy if E∨ (µ) < +∞, and denote by M1 ⊂ M the set of such
measures.
   Here we write E 1 = E 1 (ω) for simplicity. As we shall see, measures in M1 = M1 (ω) have
a prescribed mass on each Xαan , determined by ω (see Corollary 9.13). However, when X is
irreducible, M1 turns out to be independent of ω ∈ Amp(X) cf. Theorem 9.24 below.
   By definition, measures of finite energy integrate all functions in E 1 . Combined with
Corollary 7.48, this implies:
Lemma 9.2. Measures in M1 put no mass on pluripolar sets.
  We will later study the dependence Amp(X) 3 ω → E∨    ω (µ) for a fixed measure µ ∈ M.
Already now, we note that Proposition 7.7 (iii) implies
Lemma 9.3. For ω ∈ Amp(X), t ∈ R>0 and µ ∈ M, we have E∨           ∨
                                                       tω (µ) = t Eω (µ).

Proposition 9.4. The energy functional E∨ : M → [0, +∞] satisfies:
      (i) for each µ ∈ M we have
                                                                ˆ   
                                     ∨
                                 E (µ) =          sup      E(ϕ) − ϕ µ ;                    (9.2)
                                            ϕ∈Hdom (ω)

      (ii) E∨ is convex, lsc, and homogeneous with respect to the scaling action of R>0 , i.e.
                                            E∨ (t? µ) = t E∨ (µ)
          for all µ ∈ M and t ∈ R>0 ;
Proof. Denote by S ∈ [0, +∞] the right-hand side of (9.2). Trivially, E∨ (µ) ≥ S. Conversely
pick ϕ ∈ E 1 , and choose a decreasing net (ϕj ) in Hdom (ω) such that ϕj → ϕ. Then
E(ϕ) ≤ E(ϕj ), and hence
                 ˆ                 ˆ       ˆ                        ˆ
         E(ϕ) − ϕ µ ≤ E(ϕj ) − ϕj µ + (ϕj − ϕ)µ ≤ S + (ϕj − ϕ)µ.
                    ´            ´
By Lemma 7.17,          ϕj µ →       ϕ µ; hence
                                                   ˆ   
                                     ∨        ∨
                                 E (µ) = sup E (ϕ) − ϕ µ ≤ S,
                                            ϕ∈E 1


# PRIMARY exact literal unit

                                           c∈R
                                                          ´
Similarly, if µ ∈ C0 (X)∨ and ϕ ∈ C0 (X) satisfy ϕ ≥ 0 and ϕ µ < 0, then E(tϕ) ≥ 0 for
t ≥ 0 yields                              ˆ       
                              ∨
                             E (µ) ≥ sup −t ϕ µ = +∞.
                                           t≥0
       ∨
Thus E     ≡ +∞ on C0 (X)∨ \ M1 . As E is concave, Legendre duality now yields (9.7).
                                                                                            
  The next duality statement will be used in the proof of Theorem 9.11.
Proposition 9.9. For any usc function ϕ : X an → R ∪ {−∞}, we have
                                                 ˆ    
                          E↓ (ϕ) = inf E∨ (µ) + ϕ µ .                                   (9.8)
                                           µ∈M

Proof. Write ϕ as the limit of a decreasing net (ϕi ) in C0 (X). On the one hand, for each
µ ∈ M we have                                           ˆ
                             E↓ (ϕ) ≤ E(ϕi ) ≤ E∨ (µ) + ϕi µ,
                                      ´
by (9.7), and hence E↓ (ϕ) ≤ E∨ (µ) + ϕ µ, by Lemma 7.17. On the other hand,
                               ˆ                    ˆ      
                        ∨                        ∨
                 inf E (µ) + ϕ µ ≤ inf E (µ) + ϕi µ = E(ϕi ),
                    µ                            µ

where the right-hand side converges to E↓ (ϕ), by Proposition 8.3 (v). This proves (9.8).   
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     103

9.3. Maximizing nets. With a view towards solving the Monge–Ampère equation MA(ϕ) =
µ, we introduce the following notion.
Definition 9.10. Given a measure µ of finite energy, we ´shall say that a net (ϕi ) in E 1 is
maximizing for µ if it computes E∨ (µ) = supϕ∈E 1 E(ϕ) − ϕ µ in the sense that
                                         ˆ
                                E(ϕi ) − ϕi µ → E∨ (µ).

  As a key consequence of the uniform differentiability property of Theorem 8.5, we prove:
Theorem 9.11. Let µ be a measure of finite energy. For any maximizing net (ϕi ) for µ we
have MA(ϕi ) → µ weakly in M.
                             ´              ´
Proof. It is enough to ´show f MA(ϕi ) → f µ for any f ∈ PL(X), by Theorem 2.2. Set
δi := E∨ (µ) − E(ϕi ) + ϕi µ, so that δi → 0. For any ε > 0, (9.8) shows that
                               ˆ                                ˆ
                 ↓                              ∨
                E (ϕi + εf ) − (ϕi + εf ) µ ≤ E (µ) = E(ϕi ) − ϕi µ + δi .

By Theorem 8.5, we infer
                                ˆ                      ˆ
                            ε        f MA(ϕi ) ≤ ε         f µ + δi + Cε2

                              ´ of i and ε. Dividing by ε, letting i → ∞, and then ε → 0,
for a constant C´ > 0 independent
we get lim supi f MA(ϕi ) ≤ f µ, and replacing f with −f yields the result.            
  This yields a variational characterization of solutions to Monge–Ampère equations:
Corollary 9.12.´ Pick ϕ ∈ E 1 and µ ∈ M1 . Then MA(ϕ) = µ iff ϕ computes E∨ (µ) =
supψ∈E 1 E(ψ) − ψ µ . In particular, E∨ (µ) = 0 iff µ = MA(0).
                                  ´
Proof. If MA(ϕ) = µ then E(ϕ) − ϕ µ = E∨ (µ) by (9.3). If the converse holds then the
constant net ϕi = ϕ is maximizing, and hence MA(ϕ) = µ, by Theorem 9.11.           
  As another consequence, we prove that measures of finite energy have a prescribed mass
on the irreducible components of X an .
Corollary 9.13. Pick µ ∈ M1 . Then µ(Xα ) = (ω n )Xα /(ω n )X for all α, and µ(Z) = 0 for
all Zariski closed subsets Z ⊂ X with dim Z < n.
Proof. Set cα := (ω n )Xα /(ω n )X (which vanishes if dim Xα < n). Pick a maximizing net (ϕi )
for µ. By Theorem 9.11, µi := MA(ϕi ) converges weakly to µ. By Corollary 7.49 (ii), we
have µi (Xα ) = cα for all i and α, and hence
                                    µ(Xα ) ≥ lim sup µi (Xα ) = cα .
                                                   i
As in the proof of Corollary 7.49, when α 6= α0 µ further puts no mass on the pluripolar set
Xαan ∩ Xαan0 , by Lemma 9.2. Thus
                                        X             X
                            1 = µ(X) =      µ(Xα ) ≥      cα = 1,
                                               α                α
which forces µ(Xα ) = cα for all α. Finally let Z ⊂ X be a Zariski closed subset with
dim Z < n, and pick an irreducible component Y of Z. If Y is not a component of X
then Y an is pluripolar, and hence µ(Y ) = 0, by Lemma 9.2. If Y = Xα for some α then
µ(Y ) = cα , which vanishes as well since dim Xα < n. Since this holds for all components of
Z, we get, as desired, µ(Z) = 0.                                                          
104                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Definition 9.14. For any µ ∈ M1 we define a functional Jµ : E 1 → [0, +∞) by

# PRIMARY exact literal unit

                                         Jµ (0) = E∨ (µ),                                (9.10)
and that a net (ϕi ) in E 1 is maximizing for µ iff Jµ (ϕi ) → 0.
Lemma 9.15. For all ϕ, ϕ0 ∈ E 1 we have
                               I(ϕ, ϕ0 ) ≈ inf (Jµ (ϕ) + Jµ (ϕ0 )).
                                          µ∈M1

In particular, we have for all ϕ ∈ E 1 and µ ∈ M1
                                     J(ϕ) . Jµ (ϕ) + E∨ (µ).                             (9.11)
Proof. On the one hand, inf µ (Jµ (ϕ) + Jµ (ϕ0 )) ≤ Jϕ (ϕ0 ) ≈ I(ϕ, ϕ0 ), thanks to (7.28). Con-
versely, set τ := 12 (ϕ + ϕ0 ). By strict concavity of E (Theorem 7.28),
                            ˆ                               ˆ
           ∨                          1             0     1
          E (µ) ≥ E(τ ) − τ µ ≥ (E(ϕ) + E(ϕ )) −              (ϕ + ϕ0 ) µ + Cn−1 I(ϕ, ϕ0 ),
                                      2                   2
and hence
                                inf (Jµ (ϕ) + Jµ (ϕ0 )) & I(ϕ, ϕ0 ).
                                 µ

In particular, J(ϕ) ≈ I(ϕ, 0) . Jµ (ϕ) + Jµ (0) = Jµ (ϕ) + E∨ (µ), which proves the final
point.                                                                                 
Corollary 9.16. Pick µ ∈ M1 , and choose a maximizing net (ϕi ) for µ. Then J(ϕi ) .
E∨ (µ) + o(1) for all i large enough.
Lemma 9.17. For each C > 0 we have
                         ˆ
                                                     1
                            ϕ (µ − MA(ψ)) . C Jµ (ψ) 2

for all ϕ, ψ ∈ {J ≤ C} ⊂ E 1 and µ ∈ M1C .
Proof. By monotone approximation, we may assume ϕ ∈ PLR . Pick a maximizing sequence
(ψi ) for µ. By Corollary 9.16, J(ψi ) . C + o(1) for all i large enough. By Lemma 7.30, we
infer
           ˆ
                                                          1                        1
             ϕ(MA(ψi ) − MA(ψ)) . (C + o(1)) I(ψi , ψ) 2 . C max{Jµ (ψi ), Jµ (ψ)} 2 ,

where the right-hand inequality
                            ´   follows from
                                          ´ Lemma 9.15. By Theorem 9.11, we have
MA(ϕi ) → µ weakly; hence ϕ MA(ψi ) → ϕ µ, while Jµ (ψi ) → 0, so we are done.         
                                                                    ´
Corollary 9.18. Pick µ ∈ M1 . If (ϕi ) is maximizing for µ then limi ϕi (MA(ϕi ) − µ) = 0
and limi E∨ (MA(ϕi )) = E∨ (µ).
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            105

Proof. By Corollary 9.16, J(ϕi ) is bounded for i large enough. By Lemma 9.17, it follows
that                         ˆ         ˆ
                                                                1
                        ci := ϕi µ − ϕi MA(ϕi ) = O(Jµ (ϕi ) 2 )
tends to 0, and hence
                                       ˆ                           ˆ
             ∨
            E (MA(ϕi )) = E(ϕi ) −         ϕi MA(ϕi ) = E(ϕi ) −       ϕi µ + ci → E∨ (µ),

completing the proof.                                                                               
  As another useful consequence, we get:
Proposition 9.19. Let ϕi → ϕ be a convergent net in PSH(ω), and assume that J(ϕi ) is
eventually bounded. For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).
                                    ´
Proof. We first claim that ψ 7→ ψ µ is continuous on {J ≤ C} ⊂ PSH(ω) for ´any C > 0.
To see this, pick a maximizing net (ρj )j for µ in PL ∩ PSH(ω). For each          ´ j, ϕ 7→ ϕ MA(ρ ´ j)
is continuous on PSH(ω), by Proposition 7.19 (ii). By Lemma 9.17, ψ MA(ρj ) → ψ µ
uniformly for ψ ∈ {J ≤ C} ⊂ PSH(ω), and the claim follows since continuity is preserved
under uniform convergence.
   The functional J is lsc, so J(ϕ) ≤ lim inf J(ϕi ) < ∞. Set ϕ0i := max{ϕi , ϕ}, so that
|ϕi − ϕ| = 2(ϕ0i − ϕ) + (ϕi − ϕ). Then ϕ0i → ϕ pointwise on X div , i.e. ϕ0i → ϕ in PSH(ω).
By (7.34) we further have I(ϕ0i , ϕ) ≤ I(ϕi , ϕ), and J(ϕ0i ) ≈ I(ϕ0i , 0) is thus eventually
                                                                                        ´      bounded,
                                                                                                  ´
by
´ 0 the quasi-triangle
          ´            inequality
                            ´      for I. The  first part of  the proof    thus  yields   ϕi µ → ϕ µ,
  ϕi µ → ϕ µ, and hence |ϕi − ϕ|µ → 0, which concludes the proof.                                    
9.4. Dependence on the ample class. In this section, X is assumed to be irreducible.
As in [BBGZ13, Proposition 3.4] we then have the following useful characterization of mea-
sures of finite energy.

# PRIMARY exact literal unit


and (9.13) follows.                                                                                
Proof of Lemma 9.26. Pick C > |ρ0 (0)|, and choose η ∈ (0, ε] such that |ρ0 (δ)| ≤ C for
δ ∈ [0, η], and hence 0 ≤ ρ(δ) ≤ Cδ for δ ∈ [0, η]. For all x, y ∈ Z we thus have
                            d(x, y) ≤ η =⇒ |f (x) − f (y)| ≤ Cd(x, y).
Now pick x, y ∈ Z at arbitrary distance, and choose a geodesic γ : [0, 1] → Z connecting x
to y. By compactness of [0, 1], we can find a chain 0 = t0 < t1 < · · · < tN = 1 in [0, 1]
          the xi := γ(ti ) satisfy d(xi , xi+1 ) ≤ η for i < N . Since γ is a geodesic, we have
such that P
d(x, y) = i<N d(xi , xi+1 ). Now (9.14) yields |f (xi ) − f (xi+1 )| ≤ Cd(xi , xi+1 ) for all i < N ,
and hence                               X
                     |f (x) − f (y)| ≤       |f (xi ) − f (xi+1 )| ≤ Cd(x, y).
                                         i<N
108                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

This holds for any C > |ρ0 (0)|, and the result follows.                                       

                            10. The strong topology on M1
   As in §9, we denote by X a projective variety of dimension n, and fix ω ∈ Amp(X). The
set M1 ⊂ M of measures of finite energy comes equipped with the weak topology of Radon
probability measures. Here we introduce and study a stronger topology on M1 .
10.1. A quasimetric on M1 . Recall from Definition 9.14 that
                                                 ˆ
                                  ∨
                        Jµ (ϕ) = E (µ) − E(ϕ) + ϕ µ ≥ 0

for all µ ∈ M1 and ϕ ∈ E 1 . Dualizing Lemma 9.15 we introduce:
Definition 10.1. For any two µ, µ0 ∈ M1 we set
                               I∨ (µ, µ0 ) := inf (Jµ (ϕ) + Jµ0 (ϕ)).
                                            ϕ∈E 1

Theorem 10.2. The functional I∨ is a quasi-metric on M1 . Furthermore,
                                     I∨ (µ, MA(0)) ≈ E∨ (µ)                                (10.1)
and
                                     I∨ (µ, MA(ϕ)) ≈ Jµ (ϕ)                                (10.2)
for all µ ∈ M1 and ϕ ∈ E 1 .
  Theorem 10.2 will be proved below, together with the following crucial estimates.
Theorem 10.3. For all ϕ, ϕ0 ∈ E 1 (ω) and µ, µ0 ∈ M1 we have
    ˆ
                                                 1                                     1
      (ϕ − ϕ0 ) µ − µ0 . I(ϕ, ϕ0 )αn I∨ (µ, µ0 ) 2 max{J(ϕ), J(ϕ0 ), E∨ (µ), E∨ (µ0 )} 2 −αn
                      


with αn := 2−n . In particular,
                   ˆ            ˆ
                                               1
              0 ≤ ϕ MA(0) − ϕ µ . max{1, J(ϕ)} 2 max{1, E∨ (µ)}1−αn .

  This last estimate should be compared with the trivial bound
                             ˆ           ˆ
                        0 ≤ ϕ MA(0) − ϕ µ ≤ J(ϕ) + E∨ (µ),

which holds by definition of E∨ .
  As an important consequence of Theorem 10.3, we have:
Corollary 10.4. Assume that X is equidimensional. If ϕ, ψ ∈ E 1 , then the following
properties are equivalent:
     (i) MA(ϕ) = MA(ψ);
    (ii) I(ϕ, ψ) = 0;
   (iii) ϕ − ψ is locally constant.
                                                                                        
Proof. The implications (iii)⇒(i)⇒(ii) are clear. If I(ϕ, ψ) = 0, then I ϕ|Xαan , ψ|Xαan = 0
for each irreducible component Xα of X, by (7.26). In order to prove that ϕ − ψ is locally
constant, we may thus assume that X is irreducible. After adding constant, assume sup ϕ =
sup ψ. Then ϕ(v) = ψ(v) for every v ∈ X div , as a consequence of Theorem 10.3 with µ = δv
and µ0 = δvtriv , since δv ∈ M1 by Proposition 11.1. By Theorem 4.22, we infer ϕ = ψ on
X an , which proves (ii)⇒(iii).                                                           
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD             109

  Corollary 10.4 in turn implies the following useful results.
Corollary 10.5. Assume that X is equidimensional. If ϕ, ψ ∈ E 1 satisfy ϕ ≥ ψ and
E(ϕ) = E(ψ), then ϕ = ψ.
Proof. By (7.4), we may assume that X is connected. From (7.22) and the assumptions, it
follows that           ˆ                  ˆ
                              (ϕ − ψ) MA(ϕ) =          (ϕ − ψ) MA(ψ) = 0.
                ´
Thus I(ϕ, ψ) = (ϕ − ψ)(MA(ψ) − MA(ϕ)) = 0, and hence ψ = ϕ + c for a constant c, by
Corollary 10.4. But then E(ϕ) = E(ψ) = 0 gives c = 0 and we are done.             
Corollary 10.6 (Domination principle). Assume that X is equidimensional. Let ϕ ∈
PSH(ω), ψ ∈ E 1 , and assume ϕ ≤ ψ a.e. with respect to MA(ψ). Then ϕ ≤ ψ on X an .
Proof. Arguing on each connected component, we may assume that X is connected. After
replacing ϕ with max{ϕ, ψ}, we may assume ϕ ≥ ψ, and hence ϕ ∈ E 1 . The assumption
then becomes ϕ = ψ a.e for MA(ψ), and we need to show ϕ = ψ. Note that
                      ˆ                            ˆ
             I(ϕ, ψ) = (ϕ − ψ)(MA(ψ) − MA(ϕ)) = (ψ − ϕ) MA(ϕ) ≤ 0.

By Corollary 10.4, we infer ϕ = ψ + c with c ∈ R, and ϕ = ψ a.e. for MA(ψ) implies
c = 0.                                                                          

10.2. Proof of Theorems 10.2 and 10.3.
Lemma 10.7. If ψ, ψ 0 ∈ E 1 and µ = MA(ψ), µ0 = MA(ψ 0 ), then
                                         I(ψ, ψ 0 ) ≈ I∨ (µ, µ0 ).
Proof. By (9.9) we have
                                 I∨ (µ, µ0 ) = inf (Jψ (ϕ) + Jψ0 (ϕ)).
                                              ϕ∈E 1


# PRIMARY exact literal unit

Proposition 12.6. Let (ϕi ) be a net in E 1 and ϕ ∈ E 1 such that ϕi ≤ ϕ for all i. Then
ϕi → ϕ strongly iff E(ϕi ) → E(ϕ).
Proof. The ‘only if’ part follows directly from the definition of strong convergence. Con-
versely, assume E(ϕi ) → E(ϕ). Since ϕi ≤ ϕ,
                                                  ˆ
            I(ϕi , ϕ) ≈ Jϕ (ϕi ) = E(ϕ) − E(ϕi ) + (ϕi − ϕ) MA(ϕ) ≤ E(ϕ) − E(ϕi )

tends to 0, and hence ϕ0i := ϕi − sup ϕi converges strongly to ϕ0 := ϕ − sup ϕ, by Theo-
rem 12.4. In particular, E(ϕ0i ) = E(ϕi ) − sup ϕi converges to E(ϕ0 ) = E(ϕ) − sup ϕ, hence
sup ϕi → sup ϕ, and we conclude, as desired, ϕi → ϕ strongly.                             
12.2. Strong continuity and surjectivity of the Monge–Ampère operator. We de-
fine the strong topology on E 1 /R ≃ Esup
                                        1 as the one induced by the strong topology on E 1 .

It is defined by the quasi-metric (ϕ, ϕ0 ) 7→ I(ϕ, ϕ0 ), by Theorem 12.4.
   As a direct consequence of Lemma 10.7, we have:
Proposition 12.7. The Monge–Ampère operator MA : E 1 → M1 induces a bi-Lipschitz
embedding
                            (E 1 /R, I) ,→ (M1 , I∨ ).
   Recall from Theorem 5.11 that the envelope property for ω ∈ Amp(X) (which holds if X
is smooth and k has characteristic zero, cf. Theorem 5.20) is equivalent to the compactness
of PSH(ω)/R. In a similar vein we have:
Theorem 12.8. For any ω ∈ Amp(X), the following are equivalent:
    (i) the envelope property holds for ω;
   (ii) the Monge–Ampère operator MAω : E 1 (ω) → M1 is onto;
  (iii) the Monge–Ampère operator induces a bi-Lipschitz isomorphism
                                  (E 1 (ω)/R, Iω ) ≃ (M1 , I∨
                                                            ω );
122                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

      (iv) (E 1 (ω)/R, Iω ) is complete;
       (v) (E 1 (ω), Iω ) is complete.
  In particular, E 1 (ω) can only be complete if X is unibranch, cf. Theorem 5.12.
Proof. Assume (i). By Corollary 9.12, (ii) holds iff the supremum defining
                                                      ˆ     
                              ∨
                             E (µ) = sup E(ϕ) − ϕ µ
                                             ϕ∈E 1

is achieved for any µ ∈ M1 . Thus choose a maximizing sequence (ϕi ) for µ in Esup     1 . By

Corollary 5.21, PSHsup is weakly compact, and we may thus assume, after passing to a
subnet, that (ϕi ) converges weakly to ϕ ∈ PSHsup . Since Jµ (ϕi ) → 0, (9.11) shows that J(ϕi )
is eventually bounded, and hence that ´ϕ ∈ E 1 (ω),
                                                 ´ since J is weakly lsc. By Proposition 9.19,
the weak convergence ϕi → ϕ implies ϕi µ → ϕ µ, and hence
                             ˆ                        ˆ       
                     E(ϕ) − ϕ µ ≥ lim sup E(ϕi ) − ϕi µ = E∨ (µ),
                                             i
since E is weakly usc. This proves (i)⇒(ii). Proposition 12.7 gives (ii)⇔(iii), and (iii)⇒(iv)
follows from the completeness of (M1 , I∨    ω ) (Theorem 10.14).
   Assume (iv), and pick a Cauchy sequence (ϕi ) in (E 1 (ω), Iω ). Then (ϕi −sup ϕi ) is Cauchy
     1 (ω) ≃ E 1 (ω)/R, and hence strongly convergent in E 1 (ω). Now (sup ϕ ) is Cauchy as
in Esup                                                                            i
well, and hence convergent in R, so we conclude that (ϕi ) is strongly convergent, proving
(iv)⇒(v).
   Finally we prove (v)⇒(i). Assume that E 1 (ω) is complete. By Theorem 5.11, (i) is
equivalent to the fact that any bounded, increasing net (ϕi ) in PSH(ω) converges weakly in
PSH(ω). Since the increasing net (sup ϕi ) converges in R, it will be enough to show that
(ϕi ) is Cauchy in E 1 (ω)/R, i.e. that
                                                                 ˆ
              Iω (ϕi , ϕj ) ≈ Jω,ϕi (ϕj ) = Eω (ϕi ) − Eω (ϕj ) + (ϕj − ϕi ) MAω (ϕi )

tends to 0 as i, j → ∞, where by symmetry of Iω we may assume i ≤ j. The increasing net
(Eω (ϕi )) converges in R. Given ε > 0, choose i0 such that 0 ≤ Eω (ϕj ) − Eω (ϕi ) ≤ ε for
j ≥ i ≥ i0 . As ϕi ≤ ϕj , (7.22) yields
                   ˆ
              0 ≤ (ϕj − ϕi ) MAω (ϕi ) ≤ (n + 1) (Eω (ϕj ) − Eω (ϕi )) ≤ (n + 1)ε.

Thus                                               ˆ
                           Eω (ϕi ) − Eω (ϕj ) +       (ϕj − ϕi ) MAω (ϕi ) ≤ nε,
which proves, as desired, that (ϕi ) is Cauchy in E 1 (ω)/R.                                  
   As a direct consequence of Theorem 12.8 and Theorem 5.20, we have the following result,
cf. Theorem A.
Theorem 12.9. Suppose that X is smooth, that char k = 0 or dim X ≤ 2, and fix ω ∈
Amp(X). Then the Monge–Ampère equation MA(ϕ) = µ admits a solution ϕ ∈ E 1 (ω),
unique up to translation, for every µ ∈ M1 .
Example 12.10. Assume the envelope property for ω ∈ Amp(X). For each v ∈ X lin , there
exists a unique ϕv ∈ E 1 (ω) such that MA(ϕv ) = δv and ϕv (v) = 0, which we call the Green’s

# PRIMARY exact literal unit

                13. Capacities, pluripolar sets, and negligible sets
  Assuming the envelope property, we make a more detailed study of pluripotential theory,
adapting to our setting classical arguments from the complex analytic case. In particular,
we prove the fundamental result that negligible sets are the same as pluripolar sets.
  In what follows, X is of dimension n and irreducible. We fix an ample class ω ∈ Amp(X),
and we assume that the envelope property holds for ω, see §5.2. As before, we write
V = Vω = (ω n ) and MA(ϕ) := V −1 (ω + ddc ϕ)n for ϕ ∈ E 1 = E 1 (ω).
13.1. Envelopes of lsc functions. Consider an arbitrary function ϕ : X an → R ∪ {+∞},
and assume that ϕ is bounded below. By Lemma 5.17, the usc regularization
                              P(ϕ)? = sup? {ψ ∈ PSH | ψ ≤ ϕ}
of the ω-psh envelope P(ϕ) is either ω-psh and bounded, or satisfies P(ϕ)? ≡ +∞.
Theorem 13.1. Pick any lsc function ϕ : X an → R ∪ {+∞}, and assume P(ϕ)? 6≡ +∞.
Then
                     P(ϕ)? = P(ϕ) = ϕ a.e. for MA(P(ϕ)? ).
  In particular, the orthogonality property
                             ˆ
                                   (ϕ − P(ϕ)? ) MA(P(ϕ)? ) = 0                           (13.1)
                                X an
holds (compare [BFJ15, BGM20]).
Lemma 13.2. If N ⊂ X an is a negligible Borel set (see Definition 5.1), then µ(N ) = 0 for
all measures of finite energy µ ∈ M1 .
   This strengthens in particular Lemma 9.2, since pluripolar sets are negligible (Proposi-
tion 5.3),
Proof. By Choquet’s lemma (see Corollary 12.22), there exists an increasing, uniformly
bounded sequence (ϕm )∞                                          ?
                           1 in PSH(ω) such that N ⊂ {ϕ < ϕ }, where ϕ := limm ϕm
pointwise. Recall that ϕ? ∈ PSH(ω), thanks to the standing assumption that the envelope
property holds. On X div we have ϕ? = ϕ, by Theorem´5.6. Thus ´ϕm → ϕ? weakly in E 1 (and
in fact strongly as well, by Theorem 12.5), and hence ϕm µ → ϕ? µ,  ´ by Proposition
                                                                              ´      9.19.
On
´ ?  the other hand, the   monotone convergence  theorem shows that   ϕ m µ →   ϕ µ. Thus
  (ϕ − ϕ)µ = 0, which implies µ(N ) = 0.                                                
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     127

Proof of Theorem 13.1. Set ψ := P(ϕ)? and µ := MA(ψ). Assume first ϕ ∈ C0 (X), so that
ψ = P(ϕ) is continuous and ω-psh. Arguing as in the proof of [BGM20, Lemma 3.5], set
f := ϕ − ψ ≥ 0, and observe that for t ∈ [0, 1],
                                ϕt := ψ + tf = (1 − t) P(ϕ) + tϕ
satisfies P(ϕ) ≤ ϕt ≤ ϕ, and hence P(ϕt ) = P(ϕ). Thus E(ψ + tf ) = E(P(ϕ)) for t ∈ [0, 1],
and Corollary 8.6 yields
                         ˆ
                                             d
                           (ϕ − ψ) MA(ψ) =          E(ψ + tf ) = 0,
                                             dt t=0
and hence ϕ = ψ µ-a.e.
   Now consider the general case. Since the Borel set {ψ > P(ϕ)} is negligible, Lemma 13.2
shows that ψ = P(ϕ) µ-a.e. In particular, ψ ≤ ϕ µ-a.e., and it thus remains to show that µ
puts no mass on the open set U := {ψ < ϕ}.
   Since ϕ is lsc and X an is compact, there exists an increasing net (ϕj ) in C0 (X) that con-
verges pointwise to ϕ. By Lemma 5.19, the increasing net ψj := P(ϕj ) converges pointwise
to P(ϕ). By Theorem 5.6, we thus have ψj → ψ on X div , and Theorem 12.5 implies that
µj := MA(ψj ) converges weakly to µ. By the first part of the proof, µj puts no mass on the
open set Uj := {ψj < ϕj }, and we want to take the limit and deduce that µ(U ) = 0; this
will conclude the proof. To do so, suppose µ(U ) > 0, and pick a point v ∈ U ∩ supp µ. Thus
ψ(v) < ϕ(v), so there exists j0 such that ψ(v) < ϕj (v) for j ≥ j0 . Set V := {ψ < ϕj0 }.
Then V is open, v ∈ V and V ⊂ Uj for j ≥ j0 . Since v ∈ supp µ, we have µ(V ) > 0. As
µj → µ weakly, we must have µj (V ) > 0 for j  0, which contradicts µj (Uj ) = 0.           

13.2. The Bedford–Taylor capacity, reprise. Recall from §7.7 that we have set, for each
Borel set E ⊂ X an ,
                                     ˆ                               
            Cap(E) = Capω (E) := sup    MA(ψ) | ψ ∈ PSH, −1 ≤ ψ ≤ 0 .
                                             E

Note that 0 ≤ Cap(E) ≤ 1 for all Borel sets E ⊂ X an , and that Cap(X) = 1.
Proposition 13.3. The function Cap is a precapacity, i.e. it satisfies:
                                E ⊂ E 0 =⇒ Cap(E) ≤ Cap(E 0 )                           (13.2)
for all Borel subsets E, E 0 , and
                                                !
                                       [
                                 Cap       Em       = sup Cap(Em )                      (13.3)
                                       m               m

for any increasing sequence (Em ) of Borel subsets.
   It is further subadditive, i.e.
                                      [    X
                                  Cap    Em ≤       Cap(Em )                            (13.4)
                                                      j

for any sequence (Em ) of Borel subsets, and inner regular, i.e.
                          Cap(E) = sup {Cap(K) | K ⊂ E compact}                         (13.5)
for any Borel subset E.
128                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. The first three properties follow immediately from the definition of the capacity as
the supremum of the Borel measures MA(ψ), and the last one likewise follows from the fact
that these Borel measures are Radon measures, and hence inner regular on all Borel sets. 

  We define the outer capacity of any subset E ⊂ X an as

                           Cap? (E) := inf {Cap(U ) | U ⊃ E open} .

Trivially, Cap? (U ) = Cap(U ) for any open U ⊂ X an , and Cap? is outer regular, i.e.

                                Cap? (E) =      inf       Cap? (U )                      (13.6)
                                             U open ⊃ E

for all E. Proposition 13.3 immediately yields:

Proposition 13.4. The function Cap? is monotone and subadditive, i.e. the analogues
of (13.2) and (13.4) hold for arbitrary subsets of X an .

   As we shall see, Cap? also satisfies the continuity condition (13.3), but this is much more
involved, see Theorem 13.29 below.

Example 13.5. Every nonempty open subset U ⊂ X an has Cap(U ) > 0. Indeed, U must
contain a divisorial valuation v, by density of X div . For 0 < ε  1, ψ := εϕv − 1 is a
candidate in (7.35), and hence
                                   ˆ               ˆ
                                                 n
                        Cap(U ) ≥     MA(ψ) ≥ ε        MA(ϕv ) ≥ εn .             (13.7)
                                      U               U

  By Proposition 9.6 and Lemma 13.2, we have, on the other hand:

Example 13.6. Every negligible Borel set N ⊂ X an satisfies Cap(N ) = 0.

  As we shall see below, this holds in fact for Cap? as well, see Lemma 13.19.
  To conclude this section, we consider the dependence of Cap = Capω on ω ∈ Amp(X).

Theorem 13.7. For any ample classes ω, ω 0 ∈ Amp(X) there exists a constant C =
C(ω, ω 0 ) ≥ 1 such that C −1 Capω ≤ Capω0 ≤ C Capω .

  This is a direct consequence of the following more precise result.

Lemma 13.8. Let ω, ω 0 ∈ Amp(X). Then:
       (i) if ω ≤ ω 0 , then Vω Capω ≤ Vω0 Capω0 ;
      (ii) if t ≥ 1, then t−n Capω ≤ Captω ≤ Capω ;

Proof. If ω ≤ ω 0 , then PSH(ω) ⊂ PSH(ω 0 ) and

                  Vω MAω (ψ) = (ω + ddc ψ)n ≤ (ω 0 + ddc ψ)n = Vω0 MAω0 (ψ)

for any ψ ∈ PSH(ω) with −1 ≤ ψ ≤ 0. This proves (i).
   The first inequality in (ii) follows from (i). For the second, suppose ϕ ∈ PSH(ω) and
−1 ≤ ψ ≤ 0. Then t−1 ψ ∈ PSH(ω), −1 ≤ t−1 ϕ ≤ 0, and the Radon measures MAω (t−1 ψ)
and MAtω (ψ) coincide. Thus Captω ≤ Capω .                                             
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     129

# PRIMARY exact literal unit

psh iff L is nef.
Proof of Theorem 7.8. By Theorem 5.14, pure Fubini–Study metrics on L coincide with
model metrics associated to Q-models L of L that are semiample, and hence nef. Since K
is nontrivially valued, Corollary 7.6 implies that every continuous psh metric is a uniform
limit of pure Fubini–Study metrics, and hence is nef.
   To prove the converse, let L be a nef Q-model of L, determined on a model X of X.
Using again Theorem 5.14, it will be enough to show that φL is a uniform limit of model
metrics associated to semiample Q-models. Since L is ample, it admits an ample Q-model
A on some projective model X ′ dominating X (cf. [GM19, Lemma 4.12]). The pull-back
L′ of L to X ′ is nef. For each ε ∈ (0, 1) ∩ Q, Lε := (1 − ε)L′ + εH is thus ample on Xs ,
and hence on X , by [EGA, IV.9.6.4]. In particular, Lε is a semiample model of L. Since
φL = φL′ (Lemma 5.10), φLε − φL = ε(φH − φL ) converges to 0 uniformly as ε > 0, and we
are done.                                                                                 
Remark 7.10. We expect Theorem 7.8 and Corollary 7.9 to hold when L is merely semi-
ample. For this, it would be enough to show that any nef model metric on L descends to the
Stein factorization A as in Lemma 5.5; this would for instance follow from a relative version
of the local Hodge index theorem proved in [YZ16, Theorem 2.1].
7.3. Psh-regularizable metrics. The curvature form of a smooth metric φ on a line bun-
dle L is a closed (1, 1)-form, which we denote by ddc φ (see [CLD12, §6.4.1] for the non-
Archimedean case). For each trivializing section τ of L over an open U ⊂ X, the function
log |τ |φ is smooth, and ddc φ = −ddc log |τ |φ on U an . Again, this makes sense for Q-line
bundles as well.
Definition 7.11. A smooth metric φ on a Q-line bundle L is semipositive if its curvature
form ddc φ is semipositive (see [CLD12, §5.4] for the non-Archimedean case).
Example 7.12. Let L be a line bundle, s1 , . . . sr ∈ H0 (L) be sections without common zeroes,
λ1 , . . . , λr ∈ R, and maxε : Rr → R a regularized max function. Then
                          φ := maxε {log |s1 | + λ1 , . . . , log |sr | + λr }
50                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

is a smooth semipositive metric on L, see [CLD12, 6.3.2].
Definition 7.13. A (possibly singular) metric φ on a line bundle L is psh-regularizable if
φ can be written as the limit of a decreasing net φi of smooth semipositive metrics.
     If φ is continuous then φi → φ uniformly, by Dini’s lemma.
Theorem 7.14. Every psh metric φ on a semiample Q-line bundle L is psh-regularizable.
Proof. By Lemma 7.4, it is enough to prove the result when φ is a Fubini–Study metric.
After replacing L with a multiple, there exists a basis (s1 , . . . , sN ) of H0 (L) without common
zeroes and constants λi ∈ R such that φ = max {log |s1 | + λ1 . . . , log |sN | + λN }, and φ is
thus the uniform limit as ε → 0 of the smooth semipositive metrics
                           φε = maxε {log |s1 | + λ1 . . . , log |sN | + λN }
as in Example 7.12.                                                                             
7.4. The Fubini–Study operator. The following discussion is closely related to the point
of view developed by Chen and Moriwaki in [CMor18, §3.2].
Definition 7.15. Let L be a globally generated line bundle. We say that a subspace V ⊂
H0 (L) is basepoint free if sections in V generate L at all points. To each norm k · k on V ,
we then associate the metric FS(k · k) on L defined at each x ∈ X an as the quotient norm
                                                              |s(x)|
                                FS(k · k)(x) := log sup              .
                                                      s∈V \{0} ksk

     Recall that log |s| denotes the singular metric attached to s ∈ H0 (L), cf. Example 5.1.
Theorem 7.16. For any norm k · k on a basepoint free subspace V ⊂ H0 (L), the metric
FS(k · k) is continuous and psh.
Lemma 7.17. Let s1 , . . . , sr be finitely many sections of L without common zeroes, and
λ1 , . . . , λr ∈ R. Let V ⊂ H0 (L) be the basepoint free subspace generated by the si . Let k · kλ
be the norm on K r which is diagonal in the canonical basis (ei ) and such that kei kλ = e−λi ,
and denote by k·k the induced quotient norm on V with respect to the surjective map K r → V
that sends (ei ) to (si ). Then:
                              P
       (i) FS(k · k) = 21 log i |si |2 e2λi when K is Archimedean;
     (ii) FS(k · k) = maxi (log |si | + λi ) when K is non-Archimedean.
                                                                                P
Proof. For each s ∈ V , we have ksk = inf {kakλ | a ∈ K r , s = i ai si }. Using this, one
immediately checks that                                           P
                                                                 | i ai si |
                                     FS(k · k) = log sup
                                                     a∈K r \{0}    kakλ
                    an
pointwise on X . In the Archimedean case, the Cauchy–Schwarz inequality yields
                                        P
                                       | i ai si |2 X |si |2        X
                              sup                  =              =      |si |2 e2λi .
                            a∈K r \{0}   kak2λ         i
                                                          ke i k2
                                                                λ     i
In the non-Archimedean case, Lemma 1.16 yields
                               P
                              | i ai si |        |si |
                       sup                = max        = max |si |eλi .
                        r
                     a∈K \{0}   kakλ         i  ke k
                                                  i λ     i
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                51


# PRIMARY exact literal unit

                ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα             (8.1)
                                       α
                          an
on the topological space X , the mixed Monge–Ampère measure     of the φi , with δX =
P
  α m  δ
      α Xα denoting the analytic fundamental class of X (see [CLD12,  §3.7] for the non-
Archimedean case).
Remark 8.1. When K = R, we define ddc φ1 ∧ . . . ∧ ddc φn ∧ δX as the image of the
corresponding measure on X(C) = XCan by the projection map XCan → X an .
Example 8.2. Assume that n = 0, i.e. X = Spec A with A a finite K-algebra. The pre-
vious construction produces a positive measure δX on Q    the finite set X an , which is described
as follows. We have a product decomposition A = i Ai into local finite K-algebras Ai
corresponding to the connected components of X. The (reduced) irreducible components of
X are given by Xi = Spec Ki , where the residue field Ki of Ai is a finite extension of K,
and the uniquePextension of the absolute value of K to Ki defines a point xi ∈ X an . The
current δX = i mi δXi is a measure on X an , and the requirement that δXi has total mass
deg π⋆ [Xi ] = [Ki : K] yields δXi = [Ki : K]δxi . As mi [Ki : K] = dimK Ai , we conclude that
                                           X
                                     δX =     (dimK Ai )δxi .
                                                 i

Proposition 8.3. For each tuple φ1 , . . . , φn of smooth metrics on Q-line bundles L1 , . . . , Ln ,
the mixed Monge–Ampère measure ddc φ1 ∧ . . . ∧ ddc φn ∧ δX satisfies the following properties:
    (i) it is a symmetric, multilinear function of the φi , and a positive Radon measure if
        the φi are semipositive, i.e. ddc φi ≥ 0;
56                         SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON
           R
      (ii) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX = (L1 · . . . · Ln );
     (iii) if L0 = L1 = OX (and hence φ0 , φ1 are smooth functions on X an ), then
      Z                                              Z
          φ0 dd φ1 ∧ dd φ2 ∧ . . . ∧ dd φn ∧ δX = φ1 ddc φ0 ∧ ddc φ2 ∧ . . . ∧ ddc φn ∧ δX .
               c        c              c
                                                                                               (8.2)

     (iv) for any complete field extension F/K, we have
                 p⋆ (ddc φ1,F ∧ . . . ∧ ddc φn,F ∧ δXF ) = ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
         where φi,F is the pullback of φi to Li,F and p : XFan → X an is the canonical projection.
Proof. (i) is straightforward. (ii) is classical in the Archimedean case, and proved in [CLD12,
Proposition 6.4.3] in the non-Archimedean case. (iii) is a consequence of the Stokes formula
(see [CLD12, Théorème 3.12.2] in the non-Archimedean case). In the Archimedean case, (iv)
is nontrivial only when K = R, F = C, in which case it holds by definition (see Remark 8.1).
In the non-Archimedean case, it is implicit in [CLD12], and can be checked as follows. Pick
a smooth, compactly supported function f on X an , and consider the smooth, compactly
supported (n, n)-form α := f ddc φ1 ∧ . . . ∧ ddc φn . According to [Gub16, Proposition 5.13],
there exists a Zariski open subset U ⊂ X with a closed embedding U ֒→ Grm,K and a
compactly supported smooth (n, n)-superform on Rr such that α is obtained by pulling-
back η by the tropicalization map Trop : U an → Rr , and
                             Z                                  Z
                                      c              c
                                f dd φ1 ∧ · · · ∧ dd φn ∧ δX =     α
                                                                          X
is defined as the integral of η on the tropical cycle Trop(U ). Unravelling the definitions, it
is clear that the pull-back αF of α to XFan is simply the pull-back of η by the tropicalization
map TropF : UFan → Rr . The construction of the tropical cycle of an algebraic variety being
invariant under ground field extension,
                                  R       Rwe have TropF (UF ) = Trop(U ) as tropical cycles,
and we conclude as desired that X α = XF αF .                                                 
   Recall from §7.3 that a continuous metric on a Q-line bundle L is psh-regularizable iff it is
a uniform limit of smooth semipositive metrics on L. If L is semiample, then any continuous
psh metric (in the sense of Definition 7.2, i.e. a uniform limit of Fubini–Study metrics) is
psh-regularizable, by Theorem 7.14.
Theorem 8.4. Let L1 , . . . , Ln be Q-line bundles on X. The measure-valued operator
                             (φ1 , . . . , φn ) 7→ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
defined so far on smooth metrics, admits a unique continuous extension to tuples of contin-
uous, psh-regularizable metrics on the Li , with respect to uniform convergence for tuples of
metrics, and the weak topology on Radon measures.
     As a direct consequence of Proposition 8.3, we get:
Proposition 8.5. For each tuple of continuous, psh-regularizable metrics (φi ),
                                            X
             ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα
                                                     α

is a positive Radon measure on X an , of total mass (L1 · . . . · Ln ). It is further symmetric
and multiadditive as a function of the φi .
                    NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                          57

   Theorem 8.4 follows from the classical Bedford–Taylor theory [BT76] in the Archimedean
case, and from its analogue in the non-Archimedean case [CLD12, Corollaire 5.6.5]. In the
present global setting, one can however provide a simple direct argument, based on the
following global version of the classical Chern–Levine–Nirenberg inequality that will be put
to use again a bit later.
Lemma 8.6. Let L0 , . . . , Ln be line bundles on X, and suppose given a pair of smooth,
semipositive metrics φi , φ′i on each Li . Then
       Z                                            Z
          (φ0 − φ′0 ) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX − (φ0 − φ′0 ) ddc φ′1 ∧ . . . ∧ ddc φ′n ∧ δX

                                                  n
                                                  X
                                           ≤C           sup |φi − φ′i |
                                                  i=1

with C := 2 max1≤i≤n (L0 · L1 · . . . · Lbi · . . . · Ln ).
Proof. For brevity of notation, set T := ddc φ2 ∧ . . . ∧ ddc φn ∧ δX . By (8.2),
       Z                         Z                          Z
         (φ0 − φ′0 ) ddc φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T = (φ0 − φ′0 ) ddc (φ1 − φ′1 ) ∧ T
          Z                                       Z                              Z
      =       (φ1 − φ′1 ) ddc (φ0 − φ′0 ) ∧ T =       (φ1 − φ′1 ) ddc φ0 ∧ T +       (φ1 − φ′1 ) ddc φ′0 ∧ T.

Since ddc φ0 ∧ T and ddc φ′0 ∧ T are both positive measures of mass (L0 · L2 · . . . · Ln ), we infer
     Z                          Z
       (φ0 − φ0 ) dd φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T ≤ 2(L0 · L2 · . . . · Ln ) sup |φ1 − φ′1 |.
                ′   c


We conclude by symmetry and multilinearity.                                                                     
Proof of Theorem 8.4. Assume first that K is non-Archimedean, and pick f ∈ PLR (X an ).
By Lemma 5.17, we can find a pair of Fubini–Study metrics on an ample line bundle L0 such
that f = φ0 − φ′0 . By Theorem 7.14, φ0 and φ′0 are uniform limits of smooth, semipositive
metrics on L0 . Lemma 8.6 thus shows that
                                             Z
                        (φ1 , . . . , φn ) 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

is Lipschitz continuous with respect to the supnorm on tuples of smooth, semipositive met-
rics (with Lipschitz constant depending on f ), and hence extends continuously to tuples of
continuous, psh-regularizable metrics. For eachR tuple of continuous, psh-regularizable met-
rics (φi ), the linear form on PLR (X an ) f 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is positive, hence
continuous, and it thus extends to a positive linear form on C0 (X), by density of PLR (X an ).
   In the Archimedean case, the argument is similar, arguing with a smooth function f
instead. It is in fact even simpler, since f can directly be written as a difference of smooth
psh metrics on some ample line bundle.                                                         
   In order to exploit the multilinearity of the previous construction, it is convenient to
introduce the following terminology.
Definition 8.7. We say that a continuous metric φ on a line bundle L is dpsh if it can be
written as a difference of continuous, psh-regularizable metrics.
58                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

     A dpsh metric is thus the same as an approachable metric in the sense of [CLD12, §6.3].
Lemma 8.8. Every line bundle L admits a smooth, dpsh metric.
Proof. By Theorem 7.14, any ample line bundle admits a smooth, semipositive metric, and
the result follows since L can be written as a difference of ample line bundles.      
Example 8.9. If K is Archimedean, every smooth metric is dpsh.
   While this is probably true in the non-Archimedean case as well, it is less obvious, since
strictly positive (1, 1)-forms do not exist globally in this context.
Example 8.10. If K is non-Archimedean, every R-PL metric is dpsh, by Lemma 5.17.
   The operator (φ1 , . . . , φn ) 7→ ddc φ1 ∧. . .∧ddc φn ∧δX , being symmetric and multiadditive on
tuples of continuous, psh-regularizable metrics, extends to a symmetric, multilinear operator
on continuous dpsh metrics, with values in signed Radon measure. Note that Proposition 8.3
still holds for such metrics.
Example 8.11. If K is non-Archimedean and φ1 , . . . φn are R-PL metrics, then ddc φ1 ∧. . .∧
ddc φn ∧ δX has finite support. By ground field invariance, we may indeed assume that K is
algebraically closed, and that its value group is large enough to ensure that the φi become pure
after base change. By Proposition 5.16, φ1 , . . . , φn are then induced by Q-models L1 , . . . , Ln
of L1 , . . . , Ln determined on a projective model X of X. By linearity with respect to the
fundamental class [X], we may further assume that X is (geometrically) irreducible, which
allows us to assume that Xs is reduced, by Theorem 4.20. Each irreducible component Y of
Xs then determines a unique Shilov point xY ∈ Γ(X ), and
                                                       X
                        ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =  (L1 |Y · . . . · Ln |Y )δxY ,         (8.3)
                                                    Y
by [CLD12, Proposition 6.9.2] (compare [Gub07, Proposition 3.11]).
8.2. A Poincaré–Lelong formula. We start with the following integrability result.
Theorem 8.12. Let φ1 , . . . , φn be continuous, psh-regularizable metrics on line bundles
L1 , . . . , Ln , and let s ∈ H0 (X, L) be a regular section of a line bundle L, equiped with any
continuous metric φ. Then log |s|φ is integrable with respect to ddc φ1 ∧ . . . ∧ ddc φn ∧ δX , and
                                  Z
                                     log |s|φ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

depends continuously on the φi with respect to uniform convergence.
Lemma 8.13. We can find two ample line bundles A, A′ , a decreasing sequence (ψj ) of
smooth, semipositive metrics on A, and a smooth, semipositive metric ψ ′ on A′ such that
L = A − A′ and ψj − ψ ′ → log |s| pointwise.
Proof. Pick a very ample line bundle A′ such that A := L + A′ is also very ample. Let (sα )
and (s′β ) be bases of H0 (A) and H0 (A′ ), respectively, and set
                                                                                   
                           X                    X                           X
             ψj := 21 log    |s · s′β |2 + e−j   |sα |2  , ψ ′ := 21 log   |s′β |2  .
                            β                  α                             β
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                        59

These metrics are smooth and semipositive (both in the Archimedean and non-Archimedean
cases), and
                                                                
                                                   X
                           log |s| + ψ ′ = 21 log   |s · s′β |2 
                                                          β

is the decreasing limit of ψj .                                                                            

Proof of Theorem 8.12. Given any other metric φ′ on L, log |s|φ − log |s|φ′ = φ′ − φ is a con-

# PRIMARY exact literal unit

to φ0 , φ1 , and hence with respect to any permutation of φ0 , . . . , φn , being already symmetric
with respect to φ1 , . . . , φn by induction. Finally, the pairing satisfies by construction the
restriction formula, and we are done.                                                             
8.4. The non-Archimedean case. We assume in this section that K is non-Archimedean,
possibly trivially valued. By the change of metric formula (8.9), the Deligne pairing is
basically determined by its values on model metrics, which are described by the following
result.
Theorem 8.18. Let L0 , . . . , Ln be line bundles on a projective K-scheme X of dimension
n. Let L0 , . . . , Ln be models of L0 , . . . , Ln , determined on a projective model X of X, and
denote by φ0 , . . . , φn the corresponding model metrics. Then
                                         hφ0 , . . . , φn i = φhL0 ,...,Ln i .                        (8.15)
  Here hL0 , . . . , Ln i is the Deligne pairing with respect to the flat projective morphism X →
Spec K ◦ , cf. Appendix A. Since Deligne pairings commute with base change, hL0 , . . . , Ln i is
a model of hL0 , . . . , Ln i, and φhL0 ,...,Ln i denotes the corresponding model metric.
Proof. We argue by induction on n. Assume first n = 0, and hence X = Spec A with A finite
free over K ◦ . As recalled in Lemma A.19, any line bundle on X is trivial in a neighborhood
of the special fiber of X , and hence trivial on X . A trivializing section s ∈ H0 (L0 ) induces
a trivializing section hsi = NX /K ◦ (s) of hL0 i = NX /K ◦ (L0 ), as well as a trivializing section
s ∈ H0 (X, L0 ), such that |s|φ0 = 1 on X an . By (8.11), we infer
                                                Z
                                log |hsi|hφ0 i = log |s|φ0 δX = 0,

which is equivalent to hφ0 i = φhL0 i .
   Let now L0 , . . . , Ln be line bundle on a projective K-scheme X of dimension n, and
L0 , . . . , Ln be models of L0 , . . . , Ln determined on a projective model X of X. Since any
line bundle on X can be written as a difference of ample line bundles, we may assume that
L0 is ample, by linearity. After passing to a large enough multiple, we assume that there
exists a relatively regular section s ∈ H0 (L0 ), by Proposition A.15. Denote by Z its divisor,
with generic fiber Z. By the restriction property of Deligne pairings on models, s induces
an isomorphism
                                   hL0 , · · · , Ln i = hL1 |Z , . . . , Ln |Z i
of models of hL0 , . . . , Ln i = hL1 |Z , . . . , Ln |Z i. By induction, we get
                        φhL0 ,··· ,Ln i = φhL1 |Z ,...,Ln |Z i = hφ1 |Z , . . . , φn |Z i
                                           Z
                     = hφ0 , . . . , φn i + log |s|φ0 ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
66                       SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

using the restriction property of Theorem 8.16. It remains to show that the right-hand
integral vanishes, which follows from the fact that ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is supported on
Γ(X ) (cf. Example 8.11) together with Lemma 8.19 below.                                       
Lemma 8.19. If s is a relatively regular section of a line bundle L on a model X , then
|s|φL = 1 on Γ(X ).
Proof. Since s doesn’t vanish at the associated points of Xs , s is nonzero on the reduction
ξ := redX (x) of any Shilov point x ∈ X an defined by X . In other words, s defines a
trivializing section of L on an open neighborhood U of ξ, and we infer |s|φL ≡ 1 on U i , by
definition of the model metric φL .                                                        
   Using Theorem 8.18, we relate Deligne pairings and Gubler’s intersection theory on mod-
els [Gub98].
Definition 8.20. If D is a vertical Cartier divisor and L1 , . . . , Ln are line bundles on a
projective model X of X, we define their intersection number as the real number
                             (D · L1 · . . . · Ln ) := φhOX (D),L1 ,...,Lni .
   Here the right-hand side is a model function on Spec K, identified with its value on the
unique point of Spec K. Equivalently, (D · L1 . . . · Ln ) = vK (f ) for any choice of generator
f of the free K ◦ -module
                                       hO(D), L1 , . . . , Ln i ֒→ K.
In particular, (D · L1 . . . · Ln ) belongs to the (additive) value group ΓK ⊂ R.
   As a special case of Theorem 8.18, we have
                                            Z
                     (D · L1 . . . · Ln ) = φD ddc φL1 ∧ . . . ∧ ddc φLn ∧ δX .           (8.16)

On the other hand, in [Gub98, §3] Gubler associates to every vertical Cartier divisor D on
X an n-dimensional cycle cyc(D) with coefficients in ΓK on the finite type K̃-scheme Xs ,
such that the following holds:
     (i) if µ : X ′ → X is a morphism of projective models, then cyc(D) = µ⋆ cyc(µ⋆ D);
    (ii) if F/K is a non-Archimedean extension and DF is the pull-back of D to the base
         change of X to F ◦ , then cyc(DF ) = cyc(D)Fe ;
   (iii) if Xs is reduced, every irreducible component Y of Xs determines a unique Shilov
         point xY ∈ Γ(X ), and
                                             X
                                   cyc(D) =      φD (xY )[Y ].
                                                  Y
Corollary 8.21. Let L1 , . . . , Ln be line bundles on a model X of X, and D be a vertical
Cartier divisor on X . Then

# Live primary Stacks statements/proofs and definition

{
  "content": [
    {
      "type": "text",
      "text": "Lemma 10.164.3 (033G)—The Stacks project (https://stacks.math.columbia.edu/tag/033G)\n【turn974364view0】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/033G\",\"lineno\":null}); Total lines: 67\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†1】: Preliminaries\nL9:   * Chapter 【6†10】: Commutative Algebra\nL10:   * Section 【7†10.164】: Descending properties\nL11:   * Lemma 【8†10.164.3】 (【9†cite】)\nL12: \nL13: [Input]\nL14: \nL15:   * 【10†previous lemma】\nL16:   * 【11†next lemma】\nL17: \nL18: * * *\nL19: \nL20:   * 【12†history】\nL21:   * 【13†statistics】\nL22:   * 【14†8 tags refer to this tag】\nL23: \nL24: 【8†Lemma 10.164.3.】 Let $R \\to S$ be a ring map. Assume that\nL25:   1. $R \\to S$ is faithfully flat, and\nL26: \nL27:   2. $S$ is a normal ring.\nL28: \nL29: Then $R$ is a normal ring.\nL30: Proof. Since $S$ is reduced it follows that $R$ is reduced. Let $\\mathfrak p$ be a prime of $R$. We have to show that $R_{\\mathfrak p}$ is a normal domain. Since $S_{\\mathfrak p}$ is faithfully over $R_{\\mathfrak p}$ too we may assume that $R$ is local with maximal ideal $\\mathfrak m$. Let $\\mathfrak q$ be a prime of $S$ lying over $\\mathfrak m$. Then we see that $R \\to S_{\\mathfrak q}$ is faithfully flat (Lemma 【15†10.39.17】). Hence we may assume $S$ is local as well. In particular $S$ is a normal domain.\nL31: Since $R \\to S$ is faithfully flat and $S$ is a normal domain we see that $R$ is a domain. Next, suppose that $a/b$ is integral over $R$ with $a, b \\in R$. Then $a/b \\in S$ as $S$ is normal. Hence $a \\in bS$. This means that $a : R \\to R/bR$ becomes the zero map after base change to $S$. By faithful flatness we see that $a \\in bR$, so $a/b \\in R$. Hence $R$ is normal. $\\square$\nL32: * * *\nL33: ## Comments (0)\nL34: \nL35: * * *\nL36: ## Post a comment\nL37: \nL38: Your email address will not be published. Required fields are marked.\nL39: \nL40: In your comment you can use 【16†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL41: \nL42: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL43: \nL44: All contributions are licensed under the 【17†GNU Free Documentation License†github.com】.\nL45: Name^{*}: [Input]\nL46: E-mail^{*}: [Input]\nL47: Site: [Input]\nL48: Comment:\nL49: \nL50: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 033G. Beware of the difference between the letter 'O' and the digit '0'.\nL51: \nL52: Tag: [Input] [Button: Post comment] [Input]\nL53: \nL54: The tag you filled in for the captcha is wrong. You need to write 033G, in case you are confused.\nL55:   * 【10†previous lemma】\nL56:   * 【11†next lemma】\nL57: \nL58: * * *\nL59: \nL60: 【18†View Lemma 10.164.3 as pdf】\nL61: \nL62: * * *\nL63: \nL64:   * 【12†history】\nL65:   * 【13†statistics】\nL66:   * 【14†8 tags refer to this tag】\n\n--------------------------------------------------------------------------------\nLemma 35.23.11 (0CEX)—The Stacks project (https://stacks.math.columbia.edu/tag/0CEX)\n【turn974364view1】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/0CEX\",\"lineno\":null}); Total lines: 63\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†35】: Descent\nL10:   * Section 【7†35.23】: Properties of morphisms local in the fpqc topology on the target\nL11:   * Lemma 【8†35.23.11】 (【9†cite】)\nL12: \nL13: [Input]\nL14: \nL15:   * 【10†previous lemma】\nL16:   * 【11†next lemma】\nL17: \nL18: * * *\nL19: \nL20:   * 【12†history】\nL21:   * 【13†statistics】\nL22: 【8†Lemma 35.23.11.】 The property $\\mathcal{P}(f) =$“$f$ is a universal homeomorphism” is fpqc local on the base.\nL23: Proof. This can be proved in exactly the same manner as Lemma 【14†35.23.3】. Alternatively, one can use that a map of topological spaces is a homeomorphism if and only if it is injective, surjective, and open. Thus a universal homeomorphism is the same thing as a surjective, universally injective, and universally open morphism. Thus the lemma follows from Lemmas 【15†35.23.7】, 【10†35.23.10】, and 【16†35.23.4】. $\\square$\nL24: \nL25: * * *\nL26: ## Comments (0)\nL27: \nL28: There are also:\nL29: \nL30:   * 2 comment(s) on Section 【17†35.23】: Properties of morphisms local in the fpqc topology on the target\nL31: \nL32: * * *\nL33: ## Post a comment\nL34: \nL35: Your email address will not be published. Required fields are marked.\nL36: \nL37: In your comment you can use 【18†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL38: \nL39: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL40: \nL41: All contributions are licensed under the 【19†GNU Free Documentation License†github.com】.\nL42: Name^{*}: [Input]\nL43: E-mail^{*}: [Input]\nL44: Site: [Input]\nL45: Comment:\nL46: \nL47: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 0CEX. Beware of the difference between the letter 'O' and the digit '0'.\nL48: \nL49: Tag: [Input] [Button: Post comment] [Input]\nL50: \nL51: The tag you filled in for the captcha is wrong. You need to write 0CEX, in case you are confused.\nL52:   * 【10†previous lemma】\nL53:   * 【11†next lemma】\nL54: \nL55: * * *\nL56: \nL57: 【20†View Lemma 35.23.11 as pdf】\nL58: \nL59: * * *\nL60: \nL61:   * 【12†history】\nL62:   * 【13†statistics】\n\n--------------------------------------------------------------------------------\nDefinition 15.108.1 (0BPZ)—The Stacks project (https://stacks.math.columbia.edu/tag/0BPZ)\n【turn974364view2】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/0BPZ\",\"lineno\":null}); Total lines: 64\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†1】: Preliminaries\nL9:   * Chapter 【6†15】: More on Algebra\nL10:   * Section 【7†15.108】: Local irreducibility\nL11:   * Definition 【8†15.108.1】 (【9†cite】)\nL12: \nL13: [Input]\nL14: \nL15:   * 【10†next lemma】\nL16: \nL17: * * *\nL18: \nL19:   * 【11†history】\nL20:   * 【12†statistics】\nL21:   * 【13†2 tags refer to this tag】\nL22: \nL23: [Chapter 0 (23.2.1), 【14†EGA4】]\nL24: 【8†Definition 15.108.1.】 Let $A$ be a local ring. We say $A$ is unibranch if the reduction $A_{red}$ is a domain and if the integral closure $A'$ of $A_{red}$ in its field of fractions is local. We say $A$ is geometrically unibranch if $A$ is unibranch and moreover the residue field of $A'$ is purely inseparable over the residue field of $A$.\nL25: \nL26: * * *\nL27: ## Comments (0)\nL28: \nL29: There are also:\nL30: \nL31:   * 2 comment(s) on Section 【15†15.108】: Local irreducibility\nL32: \nL33: * * *\nL34: ## Post a comment\nL35: \nL36: Your email address will not be published. Required fields are marked.\nL37: \nL38: In your comment you can use 【16†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL39: \nL40: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL41: \nL42: All contributions are licensed under the 【17†GNU Free Documentation License†github.com】.\nL43: Name^{*}: [Input]\nL44: E-mail^{*}: [Input]\nL45: Site: [Input]\nL46: Comment:\nL47: \nL48: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 0BPZ. Beware of the difference between the letter 'O' and the digit '0'.\nL49: \nL50: Tag: [Input] [Button: Post comment] [Input]\nL51: \nL52: The tag you filled in for the captcha is wrong. You need to write 0BPZ, in case you are confused.\nL53: \nL54:   * 【10†next lemma】\nL55: * * *\nL56: \nL57: 【18†View Definition 15.108.1 as pdf】\nL58: \nL59: * * *\nL60: \nL61:   * 【11†history】\nL62:   * 【12†statistics】\nL63:   * 【13†2 tags refer to this tag】\n"
    }
  ],
  "isError": false
}
