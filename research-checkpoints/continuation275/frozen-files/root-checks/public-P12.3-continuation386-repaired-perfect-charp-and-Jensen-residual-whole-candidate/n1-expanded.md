## 1. Objects, raw envelopes, and the exact regularity question

Replace an excellent local ring by its reduction. Fix a proper maximal-primary ideal \(\mathfrak a\). The compact Hausdorff link is \(X=\{v:v(\mathfrak a)=1\}\), with every prime support below the maximal ideal retained. The independent geometric core is G331's actual negative effective finite REAL Cartier presentations on actual primary blowups, with degree nonnegative on every contracted proper integral curve. Its continuous uniform closure is \(C\); its actual decreasing-\(C\)-net completion, with bottom, is \(D\). The comparison with ideal profiles is a qualified G331 theorem, not our definition of positivity. No envelope theorem, arbitrary-model cofinality, singular resolution, or radial/CLD comparison is imported.

For finite continuous \(f\), put
\[
p(f)=\sup\{h\in D:h\le f\}.
\]
A sufficiently negative primary constant is a competitor. All competitors are nonpositive, so the supremum is finite and bounded. If \(h_i\downarrow h\le f\) is an actual representation, the open sets \(\{h_i<f+\epsilon\}\) cover \(X\). Directedness and compactness give one term satisfying this everywhere. Then \(h_i-\epsilon\in C\), is below \(f\), and is above \(h-\epsilon\). Consequently the raw \(C\) and \(D\) suprema agree. In particular \(p(f)\) is lower semicontinuous. Subtracting \(\epsilon\), never adding an unrestricted positive constant, proves
\[
\|p(f)-p(g)\|_\infty\le\|f-g\|_\infty.
\]
Positive homogeneity follows by scaling the cone.

If \(p(f)\) is continuous, choose finitely many continuous competitors approaching it at every point; their maximum approximates it uniformly from below. Thus \(p(f)\in C\). Conversely membership in \(C\) implies continuity. If \(p(f)\in D\), it is upper semicontinuous and hence continuous. A greatest \(D\) minorant is exactly the raw supremum. Any maximal minorant is greatest, since its maximum with any other minorant remains in \(D\). Finally, if the upper regularization \(p(f)^*\) belongs to \(D\), then \(p(f)^*\le f\) by continuity of \(f\), so it is a competitor and equals \(p(f)\). These conditions are equivalent. Merely regularizing the raw supremum is not positivity recognition.

There is an intrinsic all-support factorial formula. Define
\[
J_k(f)=\{r\in R:v(r)\ge-kf(v)\text{ for every }v\in X\}.
\]
These are ideals. If \(-f\le M\), then \(\mathfrak a^{\lceil kM\rceil}\subset J_k\), so each is unit or proper primary. An element integral over \(J_k\) satisfies the same inequalities: first kill the support and use the least-valued-term test on its monic equation in the valued quotient field. They are integrally closed and \(J_kJ_l\subset J_{k+l}\). Rational profiles \(-v(I)/k\le f\) have \(I\subset J_k\). The granted rational-profile density, negative rational shifts and the preceding compact argument therefore give
\[
p(f)=\sup_k[-v(J_k(f))/k]
     =\sup_n[-v(J_{n!}(f))/n!].
\]
The factorial profiles increase. No increasing closure of \(D\) is asserted.

We need actual decreasing closure, rather than flattening nested representations. On a normal branch G331 gives the zero dichotomy. Suppose \(u_i\in D\) decreases to \(u\). If every term is zero the assertion is direct. Otherwise restrict to a tail with \(u_i\le-c<0\). For a finite continuous \(F>u\), compactness of strict tests selects \(u_i<F\) everywhere and then a term \(g\in C\) of its representation with \(u_i\le g<F\) and \(g<-c/2\). A sufficiently small positive \(b\) makes \(q=(1-b)g\) strictly above \(u\) and still below \(F\). All-bottom points cause no subtraction of infinities. Apply this insertion to the minimum of two continuous majorants. These majorants are downward directed. Upper semicontinuity of \(u\), normality of the compact Hausdorff space and a Urysohn cutoff produce, for each point and finite \(t>u(v)\), a continuous \(F>u\) with \(F(v)<t\). Insertion shows that the infimum of this ONE decreasing \(C\)-net is \(u\). For a reduced ring pull back to its finitely many normal centres, apply the branch argument and descend by G331's full-fibre \(D\) theorem. This proves closure under decreasing nets of \(D\) with no assumed increasing or arbitrary-infimum closure.

Say CE holds if every finite continuous obstacle has its raw envelope in \(C\). Under CE, for any bounded-above extended upper semicontinuous \(\phi\), take all finite continuous nonpositive majorants of \(\min(\phi,0)\), directed by minima. Their infimum is that function by Urysohn cutoffs. Their envelopes give ONE decreasing \(C\)-net. Its infimum is the greatest \(D\) minorant of \(\phi\). The preceding closure theorem also proves commutation with decreasing obstacle nets having specified upper semicontinuous limits. These assertions include poles and bottom; bounded obstacles give bounded minorants. They supply no increasing-limit shortcut through energy.

For another primary gauge \(\mathfrak b\), let \(d(v)=v(\mathfrak b)>0\) and \(T(v)=v/d(v)\). Both \(d\) and its inverse are bounded continuous. Homogeneous potentials and obstacles transform by \(u_{\mathfrak b}(T(v))=u_{\mathfrak a}(v)/d(v)\). Order, uniform convergence and actual decreasing representations are preserved. Thus
\[
p_{\mathfrak b}(f_{\mathfrak b})(T(v))=p_{\mathfrak a}(f_{\mathfrak a})(v)/d(v),
\]
with the exact three-gauge cocycle. No constant-translation identity is needed.

Artifacts: whole-proof.md, P12.3-independent-paper.tex, source-ledger.md, coverage.md, scope-and-verdict.json, native-notes.json and reports. Rerun: python reader.py m --retain; python reader.py p --retain; python reader.py b --retain; python identity_audit.py; python bounded_diagnostics.py; python build_delivery.py; python final_audit.py. The paper is intentionally uncompiled; ROOT retains compilation and publication. Execution and hashes do not certify the mathematics.
