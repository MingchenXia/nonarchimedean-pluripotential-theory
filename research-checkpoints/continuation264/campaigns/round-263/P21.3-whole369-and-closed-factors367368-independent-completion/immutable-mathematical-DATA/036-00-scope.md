# A direct removability route for P21.3

Research draft, 8 October 2026. P21.3 is unresolved in this deliverable. The results below are proved partial progress, with their additional hypotheses displayed. No independent correctness verdict is claimed.

## The unchanged target

Let \(K\) be any complete non-Archimedean field, with trivial or nontrivial valuation. Let \(X\) be a good separated strict boundaryless pure \(n\)-dimensional \(K\)-analytic space, \(n\geq2\). For every ordinary open \(W\subseteq X\), every positive ordinary CLD current \(T\) of bidegree \((p,p)\), \(0\leq p\leq n-1\), satisfying both \(\mathrm d'T=0\) and \(\mathrm d''T=0\), and every separately admissible finite continuous psh pair \(U,V\) on \(W\), the target asks whether
\[
 D[U]=D[V]\quad\Longrightarrow\quad D(UT|_W)=D(VT|_W),\qquad D=\mathrm d'\mathrm d''.
\]
Here \([f]=f\delta_X\) uses the original canonical integration current. Its generic Artinian component lengths are retained. We do not replace \(X\) by its reduction, normalize its components, change its field, or replace its currents by tropical pushforwards.

Write \(h=U-V\), \(q=n-p\), and \(r=q-1\). The required equation is \(D(hT|_W)=0\). The testing degree for this equation is \((r,r)\); the testing degree for \(T\) is \((q,q)\). This distinction is used throughout, including \(r=0\) when \(p=n-1\).

The dossier's descriptions of previous positive ranges are context, not incoming mathematical premises. No previous manuscript or review result is used as a theorem. Our only published mathematical inputs are the explicitly checked ordinary CLD calculus below. In particular the proofs do not use generated-psh recognition of either sign of \(h\), a conversion from continuous Psh to CPsh, any current density theorem, a strong-current lift, or scalar descent.

## The new results and their scope

We prove a quantitative cutoff bound for a possible multiplier defect supported on a closed ordinary locus. It controls the ordinary product using the original current's positive coefficient measures. Cutoffs and their decompositions are actual CLD forms on one fixed ordinary open. The bound yields removability when its weighted errors vanish, and a necessary blowup condition for a nonzero defect when the difference has a smooth harmonic trace along the locus.

We also prove a geometric consequence using CLD's analytic dimension support principle. Suppose \(Z\subset W\) is closed and locally is a closed analytic locus of dimension less than \(n-p-1\), and \(h\) is ordinary CLD-smooth with zero smooth Hessian on \(W\setminus Z\). Then \(D(hT)=0\) for every allowed \(T\). This conclusion retains singularities, nilpotents and both valuation regimes. It has an extra hypothesis on the nonsmooth locus and on the smooth Hessian off that locus. We do not deduce that hypothesis from canonical Hessian equality.

These results concern a specified open carrying the pair. Applying them to all ordinary opens requires the additional hypotheses on each such open, or suitable ordinary local hypotheses there. No cover is turned into a basis. When \(p=n-1\), the analytic dimension bound is \(\dim Z<0\), so it removes no nonempty locus. The cutoff theorem still makes sense in that degree, but its vanishing condition is not established for arbitrary currents and pairs.

The exact universal residual is unchanged: prove annihilation for arbitrary admissible pairs and arbitrary positive doubly closed ordinary currents on every ordinary open, including gluing loci for which neither off-locus regularity nor the cutoff bound is known, or construct an admissible analytic counterexample with an actual compact detecting test.
