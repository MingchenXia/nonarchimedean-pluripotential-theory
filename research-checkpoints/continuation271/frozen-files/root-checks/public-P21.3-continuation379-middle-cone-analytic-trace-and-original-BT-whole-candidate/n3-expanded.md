# Complete scalar and smooth-form factor transfer

Use n1's signed coefficient measures and ordinary scalar products. Let \(\mathcal F(O)\subset C(O,\mathbb R)\) be any prescribed restriction-compatible class of finite functions. A positive doubly closed current \(T\) is BT for \(\mathcal F\) if, on every ordinary \(O\), all \(u,v\in\mathcal F(O)\) with \(D[u]=D[v]\) have \(D((u-v)T)=0\). Initial BT is an explicit hypothesis in the transfer statements below. The original individually continuous psh class can be used without replacing it by generated CPsh.

For a smooth form \(\beta\) and a complementary compact test \(\omega\), \(\beta\wedge\omega\) has the complementary diagonal type for \(T\). Since \(T\) has even total degree, n1 gives
\[
 \langle\beta\wedge(hT),\omega\rangle
 =\int h\,d\mu_{T,\beta\wedge\omega}.                                    \tag{6}
\]
If \(\beta\wedge T=0\), evaluate that zero current on \(f\omega\) for all smooth scalars \(f\). Measure uniqueness makes the measure in (6) zero, proving \(\beta\wedge(hT)=0\). For a smooth scalar \(a\), uniqueness gives \(\mu_{T,a\theta}=a\mu_{T,\theta}\), hence \(a(hT)=(ah)T\). For positive \(C=\gamma\wedge T\), its coefficient measure agrees with \(\mu_{T,\gamma\wedge\omega}\) on every smooth scalar, so
\[
 hC=\gamma\wedge(hT).                                                     \tag{7}
\]
For continuous \(a\geq0\), the same uniqueness applied to the ordinary positive \(aT\) gives \(h(aT)=(ha)T\). These statements use the measures of positive \(T\); they invent no continuous wedge on an arbitrary signed current.

For any current \(S\) and smooth \(\beta\) of total degree \(b\), signed transposition and total-degree exterior commutation proves
\[
 d(\beta\wedge S)=d\beta\wedge S+(-1)^b\beta\wedge dS,\qquad d=d',d''.
\]
Indeed move \(\beta\) past total-degree-\(m\) \(S\) with \((-1)^{bm}\), transpose the differential with \((-1)^{m+b+1}\), and expand \(d(\beta\wedge\omega)\) on each compact test. The two resulting signs are exactly the displayed terms. This is also the correctly indexed argument of CLD 7.7.7. No closedness of \(S\) is assumed. For smooth \((k,k)\)-form \(\gamma\), applying both rules gives
\[
 D(\gamma\wedge S)=D\gamma\wedge S-d''\gamma\wedge d'S
                  +d'\gamma\wedge d''S+\gamma\wedge DS.                  \tag{8}
\]

Suppose \(T\) and \(C=\gamma\wedge T\) are doubly closed. First-order Leibniz gives \(d'\gamma\wedge T=d''\gamma\wedge T=0\). Differentiating the second gives \(D\gamma\wedge T=0\). Put \(S=hT\). The measure argument inherits all three annihilators for \(S\). Differentiate the first by \(d''\) and the second by \(d'\), remembering that both differentiated form factors have odd total degree:
\[
 0=-D\gamma\wedge S-d'\gamma\wedge d''S,
 \qquad0=D\gamma\wedge S-d''\gamma\wedge d'S.
\]
Thus both cross terms in (8), as well as its \(D\gamma\) term, vanish. We obtain
\[
 D(\gamma\wedge(hT))=\gamma\wedge D(hT).                                  \tag{9}
\]
This calculation keeps \(S=hT\) potentially nonclosed. For a scalar factor it reads \(D((ah)T)=aD(hT)\) under closedness of \(aT\).

Consequently, for an initial BT current \(T\), an actual smooth-factor product \(C=\gamma\wedge T\) is BT if and only if it is positive and doubly closed. Necessity is in the definition. For sufficiency restrict to arbitrary ordinary \(O\), take an admissible pair there, put \(h=u-v\), and apply initial \(D(hT)=0\), (7), and (9). The form \(\gamma\) itself need be neither positive nor closed. Its actual product must be positive, and closedness is precisely \(d'\gamma\wedge T=d''\gamma\wedge T=0\). The degree range is \(p+k\leq n\); original nontrivial P21.3 tests require \(p+k\leq n-1\), while degree \(n\) has no Hessian tests. In particular a smooth \(a\geq0\) is allowable exactly when \(aT\) is doubly closed.

The fixed-current scalar-net theorem is equally exact. If locally smooth \(a_i\geq0\) converge locally uniformly to continuous \(a\), and EACH \(a_iT\) is doubly closed for the FIXED initial BT \(T\), then \(aT\) is positive and closed by n1's coefficient-measure convergence and transposition. For any admissible \(h\) on any ordinary subopen and compact detecting \(\omega\),
\[
 \langle D((a_i-a)hT),\omega\rangle
 =\int(a_i-a)h\,d\mu_{T,D\omega}\longrightarrow0.
\]
The measure is finite and \(h\) bounded on its compact support. Each earlier identity is zero, giving BT in the limit; ordinary locality completes the every-open statement. Unrestricted smooth approximation supplies none of the required closedness equations.

For the form-net version, assume EACH smooth \(\gamma_i\wedge T\) positive and doubly closed, and convergence in coefficients on compact supports in a FIXED finite family of common moment charts to a SMOOTH \(\gamma\). Localize a test and expand the factors in the finite exterior monomial bases. Each monomial times the localized test has a fixed finite signed coefficient measure of \(T\). Uniform coefficient convergence proves weak convergence of the products. Apply the same argument to \(d'\omega,d''\omega\) to get closedness, and pass on positive tests to get positivity. For BT use \(D\omega\) and multiply converging coefficients by the fixed bounded \(h\), then use (7). This produces no nonsmooth wedge, changing-chart convergence theorem, or density of arbitrary currents.

The complete source-scope diagnostic is analytic. On \(X=(\mathbb G_{m,\mathbb Q_\ell}^2)^{\rm an}\), let \(s_i=-\log|T_i|\) and \(a=2+s_1^2>0\). This is good separated strict boundaryless pure dimension two. Its \(\delta_X\) is positive, doubly closed, and tautologically BT. However
\[
 D(a\delta_X)=[2d's_1\wedge d''s_1].
\]
For nonzero \(\zeta\geq0\) smooth compact on \(\mathbb R^2\), the actual test \(\omega=\zeta(s)d's_2\wedge d''s_2\) has compact support in a closed analytic polyannulus. The identity moment has finite-flat degree one; CLD 14.3.1--5, 14.5.2--3 and 5.8.4 gives its standard calibration, with the paired positive orientation. Therefore
\[
 \langle D(a\delta_X),\omega\rangle=2\int_{\mathbb R^2}\zeta(s)\,ds_1ds_2>0.
\]
Thus \(a\delta_X\) is ineligible as a P21.3 current. This diagnoses the absent closedness premise of literal CLD 8.6.7; it is not an original counterexample. Conversely \(S=(d's_1\wedge d''s_1)\wedge\delta_X\) is positive closed BT, and both \(d'a\wedge S,d''a\wedge S\) vanish by repeated generators, so \(aS\) is closed BT. Nonconstant relative weights are allowed.

The entire scalar367 and relative368 statements are proved after replacing their unsupported strong-cone step by n1's middle-cone construction. Their submitted proofs require that correction. The repaired whole372 transfer chain retains initial BT, actual product positivity and double closedness, every approximant's equations, and the smooth form limit. Artifacts: P21.3-review-paper.tex, P21.3-proof-companion.md, and independent-whole372-verdict.json. Rerun python audit.py and python build_review.py. No supplied program is executed or imported.
