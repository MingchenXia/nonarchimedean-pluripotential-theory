## 11. A new analytic mechanism: canonical Jensen measures

This section is a new residual attempt, proved here from the qualified geometric \(C\), not an additional order definition of psh. Let \(M_{\le1}(X)\) be the weakly compact space of positive Radon measures of mass at most one. Define the canonical Jensen set
\[
\mathcal J_x=\{\mu\in M_{\le1}(X):h(x)\le\int h\,d\mu\text{ for every }h\in C\}.
\]
It is nonempty (\(\delta_x\) belongs), compact and convex. Its graph is closed, since every defining function \(h\) is continuous. All ingredients are the already independently geometric cone; no replacement cone is introduced.

We prove an exact dual formula for EVERY finite continuous obstacle:
\[
p(f)(x)=\min_{\mu\in\mathcal J_x}\int f\,d\mu.
\]
One inequality follows immediately by testing a competitor \(h\le f\). For the reverse, in the Banach space \(C(X)\times\mathbb R\) consider the convex cone
\[
W=\{(g,t):\exists h\in C,\ h\le g,\ t\le h(x)\}.
\]
For \(t>p(f)(x)\), \((f,t)\) is outside its closure: if \((g_i,t_i)\to(f,t)\) in norm, nonexpansivity gives \(t_i\le p(g_i)(x)\le p(f)(x)+\|g_i-f\|\), a contradiction. Hahn--Banach separation from the closed convex cone gives a nonzero functional \(L(g,t)=\mu(g)-\alpha t\), nonnegative on \(W\), strictly negative at \((f,t)\). Since \((r,-s)\in W\) for \(r\ge0,s\ge0\), \(\mu\) is positive and \(\alpha\ge0\). If \(\alpha=0\), the pairs \((-a,-a)\in W\) force \(\mu(X)=0\), contradicting nonzero separation. Divide by \(\alpha>0\). The pairs \((h,h(x))\) give exactly the Jensen inequalities, and \(h=-1\) gives mass at most one. Separation says \(\int f,d\mu<t\). Let \(t\downarrow p(f)(x)\). Compactness attains the infimum. The positive-functional/Radon correspondence, Banach separation and weak compactness of the unit positive dual ball are explicit ordinary functional foundations; the dual argument itself is new.

There is an exact topological criterion. CE holds iff the correspondence \(x\mapsto\mathcal J_x\) is lower hemicontinuous in the weak measure topology; its upper hemicontinuity already follows from closed graph and compact ambient measure space. Lower hemicontinuity makes the minimum of each continuous linear test upper semicontinuous; closed graph gives lower semicontinuity, so the dual formula proves CE.

Conversely suppose all \(p(f)\) are continuous, but lower hemicontinuity fails at \(x_0\) for some \(\mu_0\in\mathcal J_{x_0}\). A weak neighbourhood can be specified by finitely many continuous functions \(f_1,\ldots,f_r\) and an Euclidean ball of radius \(\epsilon\) about their integrals at \(\mu_0\). There is a net \(x_i\to x_0\) such that the compact convex projections of \(\mathcal J_{x_i}\) avoid that ball. Closest-point separation gives unit vectors \(a_i\) satisfying
\[
a_i\cdot\left(\left(\int f_jd\mu\right)_j-
\left(\int f_jd\mu_0\right)_j\right)\ge\epsilon
\quad(\mu\in\mathcal J_{x_i}).
\]
A subnet has \(a_i\to a\). All projected vectors are uniformly bounded, so the same inequality with \(a\) holds with \(\epsilon/2\) eventually. For \(f=\sum a_j f_j\), the dual formula gives \(p(f)(x_i)\ge\int f d\mu_0+\epsilon/2\), whereas \(p(f)(x_0)\le\int f d\mu_0\). This contradicts continuity. This proves necessity, retaining nonmetrizable links and actual nets.

The criterion provides a genuine geometric/analytic direction for the residual: prove weak lower hemicontinuity of THESE canonical measures, or find its failure at a normal germ. The matrix, trace and finite-cover arguments above prove it indirectly in their sectors; the criterion does not assert it universally.

There is a useful normal obstruction reduction. G331's actual divisorial inequality says \(g(\nu)\ge A_\nu g(v)\) for all \(g\in C\) and all \(v\), with fixed \(A_\nu>0\). If a continuous obstacle is negative somewhere, divisorial density supplies \(\nu\) with \(f(\nu)<0\). Every competitor then satisfies
\[
g(v)\le f(\nu)/A_\nu<0\quad\text{for ALL }v.
\]
Consequently on a normal branch the raw envelope is either zero (precisely when \(f\ge0\)) or uniformly strictly negative. This extends to the raw supremum without recognizing it in \(D\). A genuine normal continuous-obstacle counterexample cannot consist of a mixed-zero discontinuity. It would have to fail upper semicontinuity while remaining bounded and uniformly negative. The double-plane obstruction and the increasing energy spikes therefore cannot furnish it.

We tested the correction mechanism and the Jensen route, not merely restated the residual. Primary truncations reverse the needed subadditivity correction. The quadratic example has a good cover in every perfect positive characteristic. The dual proof reduces the residual to lower hemicontinuity but does not derive it from the available valuations, intersection/energy bounds, or conductor rules. No normal counterexample satisfying the continuous signed primary/model-obstacle condition was obtained. In particular arbitrary excellent normal dimension at least three, general nonisolated perfect-characteristic algebraic germs, the characteristic-zero infinite-\(Q\) locus, mixed/imperfect/nonalgebraic/nonclosed scope remain unresolved. The original's 'when possible/appropriate regularity' is not redefined as this criterion; its entire completion criteria still require the actual existence/positivity theory. Original candidate=false.

Artifacts: whole-proof.md, P12.3-independent-paper.tex, source-ledger.md, coverage.md, scope-and-verdict.json, native-notes.json and reports. Rerun: python reader.py m --retain; python reader.py p --retain; python reader.py b --retain; python identity_audit.py; python bounded_diagnostics.py; python build_delivery.py; python final_audit.py. The paper is intentionally uncompiled; ROOT retains compilation and publication. Execution and hashes do not certify the mathematics.
