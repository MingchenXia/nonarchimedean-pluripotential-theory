# P21.3 calibrated-chart rigidity: bounded research and obstruction note

Date: 2026-08-31. Author/reviewer: p213_skeletal_hostile. Status: research, not independently or production verified. No live edits or production calls.

## Outcome

I did not prove the scalar-rigidity target in TARGET.tex and did not construct a noncanonical positive closed analytic current. P21.3 remains open. This note identifies exactly what the available reduction proves, tests the requested branching/finite-map/absolute-continuity routes, and isolates the remaining analytic interface.

The two diagnostics proved below are counterexamples to auxiliary proof shortcuts, NOT counterexamples to rigidity or Bedford--Taylor independence:

1. Even on a smooth analytic surface, there need not be one Radon measure dominating every coefficient measure of the canonical integration current.
2. A finite étale map of smooth analytic surfaces need not be an ordinary-topology covering of its analytic degree at a Gauss point.

The algebraic residual-curve functional lemma is affirmative and complete. It removes a possible Picard-group obstruction but does not supply the higher-dimensional analytic realization of that functional.

## 1. Exact live residual and relation to this subtask

The live Ch72 file has SHA-256 6e671da09d50cc7becd553d319a0cbce0fe6c3622ac77a491550411a32c69b8c. Its problem at lines 3150--3168 asks, for every complete field and every good separated strict boundaryless pure \(n\)-dimensional analytic \(X\), \(n\geq2\), whether every positive \(\mathrm d'\)- and \(\mathrm d''\)-closed current of bidegree \((p,p)\), \(0\leq p\leq n-1\), satisfies
\[
 \mathrm d'\mathrm d''[U]=\mathrm d'\mathrm d''[V]
 \quad\Longrightarrow\quad
 \mathrm d'\mathrm d''((U-V)T|_W)=0
\]
for every ordinary open \(W\) and every continuous psh pair on \(W\).

The curve results and genuine-polycylinder-basis/fixed-domain results are already excluded by lines 3088--3127 and 3171--3181. A polycylinder cover cannot silently be treated as a basis. The discontinuous-potential predicate is explicitly outside the counted continuous-pair atom (lines 3311--3322).

If \(T=c\delta_X\), the implication follows immediately on every \(W\), since \((U-V)\delta_X=[U-V]\). Thus the proposed scalar theorem would be useful, but only for its displayed \(p=0\), nontrivial-valuation, quasi-smooth scope. No atom should be retired on that basis.

An actual counterexample to the full residual would require an actual analytic current, both actual continuous psh functions, equality of their analytic Hessian currents before pushforward, and a compactly supported test form of bidegree \((n-p-1,n-p-1)\) detecting a nonzero \(\mathrm d'\mathrm d''((U-V)T)\). A continuous Hessian-zero function alone is not a supplied psh-pair construction.

## 2. Existing candidate input: what absolute continuity really gives

The earlier expanded independent audit and the frozen source-representation packet are inputs as research data, not production-approved dependencies. The latest typeset packet itself is explicitly paused and not finally independently audited; its recorded latest cross-proof PDF is stale. No new verdict on those complete files is claimed here.

Taking the source-representation assertion as input, fix a chart and subdivide compatibly with both calibrations. In the interior of an \(n\)-cell, let
\[
 \kappa_F=b_C\,\mathrm dt,\qquad
 \mu_F=a_C\,\mathrm dt,\qquad b_C\geq0,\quad a_C>0.
\]
For a positive chart-tropical top form, its coefficient measure for \(T\) is absolutely continuous with respect to its canonical coefficient measure. On the region where the top form is nonzero, the ratio is \(b_C/a_C\). Both coefficient measures give zero mass to the lower-dimensional cell boundaries in this representation.

This is genuinely chartwise absolute continuity and constant density on a cell. Refinement compatibility identifies source densities on cells where both moments have full rank. A direction collapsed by the old chart is not compared merely by that rank condition. Closedness of the enlarged chart can create additional relations, but the creation of sufficiently many relations is the missing assertion.

In particular, this does not provide an ordinary-continuous function \(h\) with \(T=[h]\). It does not give one locally constant scalar across all cells, source sheets or charts. Nor does it provide a single Radon reference measure to which a global Radon--Nikodym theorem can be applied. The next diagnostic rules out the last conclusion as a general principle.

## 3. A smooth twofold with no common dominating Radon measure

Take \(K=\mathbf C((\pi))\), with \(|\pi|=e^{-1}\), and
\[
 X=(\mathbf A^1_K\times\mathbf G_{m,K})^{\mathrm{an}},
\]
with coordinates \(x,z\). This is a connected smooth, good, separated, strict, boundaryless twofold. Let
\[
 Q=\{|x|\leq1,\ e^{-1}\leq|z|\leq e\}.
\]
It is a compact affinoid domain.

For every \(a\in\mathbf C\), viewed as a constant in \(K\), put
\[
 Q_a=\{e^{-2}\leq|x-a|\leq e^{-1},\
                     e^{-1}\leq|z|\leq e\}.
\]
These compact sets lie in \(Q\). They are pairwise disjoint: for \(a\ne b\), \(|a-b|=1\), while both \(|x-a|\) and \(|x-b|\) would be less than one on their intersection, contradicting the ultrametric inequality.

Choose one nonnegative, nonzero smooth function
\[
 \chi\in C_c^\infty((1,2)\times(-1,1)).
\]
On the open product annulus with coordinates
\[
 u=-\log|x-a|,\qquad v=-\log|z|,
\]
define
\[
 \omega_a=\chi(u,v)\,
   \mathrm d'u\wedge\mathrm d''u\wedge
   \mathrm d'v\wedge\mathrm d''v.
\]
Its support is compactly contained in that annulus: tropicalization inverse images of compact coordinate rectangles are compact polyannuli. Extension by zero therefore gives a smooth positive compactly supported top form on \(X\), supported in \(Q_a\). Standard torus-coordinate integration gives
\[
 \int_X\omega_a=\int_{\mathbf R^2}\chi(u,v)\,\mathrm du\,\mathrm dv>0.
\]
There is no lattice factor because \(x-a,z\) are the actual two torus coordinates.

Let \(\mu_a\) be its positive canonical coefficient measure, so that
\[
 \int \rho\,\mathrm d\mu_a=\langle\delta_X,\rho\omega_a\rangle.
\]
It is a positive Radon measure supported on \(Q_a\), of positive total mass.

Suppose a positive Radon measure \(\sigma\) on \(X\) dominated all these coefficient measures in the sense \(\mu_a\ll\sigma\). Then \(\sigma(Q_a)>0\) for every \(a\). But \(\sigma(Q)<\infty\), and a finite measure cannot give positive mass to uncountably many disjoint measurable subsets. Indeed, for each positive integer \(m\), only finitely many of the disjoint sets can have measure at least \(1/m\); all positive-mass sets belong to the union of these finite collections. This contradiction proves the claim.

The example already uses \(T=\delta_X\), which is scalar and Bedford--Taylor. It says nothing negative about scalar rigidity. It shows that full support of a current and positivity of its individual coefficient measures do not turn that current into one ordinary Radon density. The statement proved here is on the displayed whole surface; no stronger assertion about every sufficiently small ordinary neighborhood is needed or claimed.

## 4. Finite étale maps do not supply ordinary-open sheets

Again over \(K=\mathbf C((\pi))\), let \(m\geq2\) and consider
\[
 \pi:(\mathbf G_m^2)^{\mathrm{an}}\longrightarrow
            (\mathbf G_m^2)^{\mathrm{an}},
 \qquad (x,z)\longmapsto(y=x^m,z).
\]
This is finite étale of degree \(m\).

Let \(\eta\) be the unit two-variable Gauss point downstairs. Its completed residue field has residue field \(\mathbf C(\bar y,\bar z)\). The polynomial
\[
                     X^m-y
\]
has irreducible reduction over that residue field: viewed over \(\mathbf C(\bar z)(\bar y)\), it is Eisenstein at \(\bar y=0\). Thus it is irreducible over \(\mathcal H(\eta)\): all its roots have norm one, so any monic factor would have integral coefficients and would reduce to a nontrivial monic factor of the same degree. The analytic fibre is the spectrum of the finite field
\(\mathcal H(\eta)[X]/(X^m-y)\), hence consists of one point, since a complete non-Archimedean absolute value extends uniquely to a finite field extension.

That point is the unit Gauss point in coordinates \(x,z\). Its residue extension has degree \(m\), although the set-theoretic fibre has one point. Therefore there cannot be \(m\) disjoint ordinary source neighborhoods over one neighborhood of \(\eta\), each mapping isomorphically onto that neighborhood.

This is a direct counterexample to replacing finite étale degree by a count of ordinary-open sheets. It is not a counterexample to a correctly stated degree-weighted pushforward formula. For the tropical coordinates the linear map is \((u,v)\mapsto(mu,v)\); the pullback of a top form contributes \(m^2\), while the coordinate change in its integral contributes \(m^{-1}\), giving the expected degree \(m\).

Consequently even a proof of scalar rigidity downstairs would only begin a finite-map argument. One would still need a valid local source-disintegration or refinement-separation theorem; a positive sum of source contributions cannot be split by declaring a covering that does not exist.

## 5. Tropical branching: the explicit cross does not lift

The previous cross packet studies
\[
 ((\mathbf P^1\setminus\{0,1,a,\infty\})\times\mathbf G_m)^{\mathrm{an}},
 \quad f=x/(x-1),\quad g=x-a,\quad h=x.
\]
For the coarse chart using \(f,g,z\), weights \((A,A,B,B)\) are balanced on its four halfplanes. Adjoining \(h\) changes transverse directions to
\[
 (1,0,1),\quad(-1,0,0),\quad(0,1,0),\quad(0,-1,-1).
\]
The corresponding weighted sum is \((0,0,A-B)\). Positivity/order zero and lower-face noncharging prevent an unrecorded line-supported distribution from correcting this defect. The explicit compactly supported derivative test in the frozen proof gives
\[
 \langle G_*T,\mathrm d'\beta\rangle
       =(A-B)\int\kappa.
\]
Thus an actual positive closed lift forces \(A=B\). The properness and source-scope qualifications in that packet must be retained.

This remains one concrete obstruction to a counterexample, not a universal refinement theorem. Finite balancing on a chosen target fan is insufficient; an attempted noncanonical family must survive every ordinary restriction and every common analytic refinement, with source sheets distinguished.

## 6. The positive divisor-functional step is complete

Here is the algebraic statement needed in a residual-curve route. Let \(C\) be a regular integral proper curve over a field \(k\). Let
\[
 \lambda:\operatorname{Div}(C)\longrightarrow\mathbf R
\]
be a group homomorphism, finite-valued, nonnegative on effective divisors, and zero on every principal divisor. Then
\[
                         \lambda=c\,\deg_k,\qquad c\geq0.
\]

Proof. Choose a closed point \(q\), and choose \(N\) so large that \(H=Nq\) satisfies \(\deg_kH+\chi(C,\mathcal O_C)>0\). If \(A\) is any integral divisor of degree zero, then for every integer \(n\),
\[
 \chi(C,\mathcal O_C(H+nA))
            =\deg_kH+\chi(C,\mathcal O_C)>0.
\]
Since a proper curve has no coherent cohomology above degree one, this implies a nonzero global section. Regularity and integrality give an effective divisor \(D_n\) linearly equivalent to \(H+nA\). Hence
\[
 0\leq\lambda(D_n)=\lambda(H)+n\lambda(A)\qquad(n\in\mathbb Z).
\]
Both signs of \(n\) force \(\lambda(A)=0\). For any closed point \(p\), apply this to
\[
              (\deg_kq)p-(\deg_kp)q.
\]
It follows that \(\lambda(p)/\deg_kp=\lambda(q)/\deg_kq=c\). This proves the formula on all divisors. Positivity gives \(c\geq0\).

No algebraic closedness, geometric connectedness, torsion assertion for \(\operatorname{Pic}^0\), or continuity of \(\lambda\) is needed. Positivity across all effective representatives is the decisive constraint.

This argument is the established residual-curve mechanism, not a novelty claim. The precise Euler-characteristic degree interface is recorded in SOURCE_INTERFACE.md.

## 7. Exact missing higher-dimensional interface

The algebraic lemma would compare analytic calibration ratios along a residual curve if one could prove all of the following in the required analytic scope:

- The relevant transverse source branches at a codimension-one skeletal face are identified with closed points of a proper regular residual curve, with the correct residue and lattice factors.
- Every residual rational function can be lifted to an analytic unit on a suitable ordinary source neighborhood, allowing extra charts as necessary. Closedness against those charts yields its entire principal-divisor relation.
- The weights assigned to a residual point are independent of all choices of lift, slice, chart and refinement. They represent the required individual source calibrations, not merely sums over several sheets.
- All source cells and sheets on the connected analytic space can be linked through these comparisons, or any omitted set has a separately justified noncharging/removal argument.

These are requirements for a proof, not proved facts in this packet. Taking a slice of an arbitrary positive current is not available by default. A generically finite or étale projection does not resolve the sheet issue, as Section 4 shows. Reconstructing a current from compatible charts does not establish uniqueness of the compatible family.

A conditional graph-propagation observation is elementary: if every two neighboring source cells in an appropriate incidence graph have equal canonical ratios, and that graph is connected and accounts for every chart cell, then all ratios coincide. The unproved part is precisely the analytic construction and connectivity/accounting of that graph, not the graph-theoretic deduction.

## 8. Rejected shortcuts and current status

| Proposed shortcut | Why it does not complete the target |
| --- | --- |
| Constant density on each top cell | Gives no relation across invisible branches or different source sheets. |
| One dominating Radon measure | Fails on the explicit smooth twofold in Section 3. |
| Finite étale map gives separate ordinary sheets | Fails at the explicit Gauss fibre in Section 4. |
| One balanced tropical fan gives an analytic current | The extra-unit cross refinement kills the standard unequal weights. |
| CLD reconstruction implies canonical uniqueness | Uniqueness there is for a prescribed compatible family. |
| Positive functional on residual divisors may retain a Picard-zero component | Section 6 rules that out; the analytic realization of the functional remains missing. |
| Smooth/quasi-smooth implies an ordinary polycylinder basis | Not assumed and not established. |
| A \(p=0\) result would retire P21.3 | Positive bidegrees and other ambient/valuation regimes remain. |

No actual noncanonical compatible family was constructed, and no proof of the required residual analytic interface was obtained. The mathematically honest endpoint is the open TARGET.tex plus the complete shortcut diagnostics and algebraic sublemma above. No live status, inventory count, or production record should change.
