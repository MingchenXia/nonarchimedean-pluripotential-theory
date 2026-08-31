# Exact source excerpts (line-numbered; not replacement text)

## BEFORE: manuscript/parts/part2/ch16_bedford_taylor.tex
Commit 10897afc0b7379ee169f46ecb77184ac7580f177; SHA256 5330c13d296dc772c923b097d5819929c0bde5530509c60349fcd331ba187683

```tex
1540: The Bedford--Taylor property is local.  The integration current $\delta_X$
1541: has it.  It is preserved by wedging with a smooth positive closed form, by
1542: weak limits of positive closed Bedford--Taylor currents, and by
1543: \[
1544:                      T\longmapsto\dprimeddprime(uT)
1545: \]
1546: for continuous psh $u$.
1547: \end{proposition}
1548: \begin{proof}
1549: Locality is the sheaf property.  For $\delta_X$,
1550: $\dprimeddprime(u\delta_X)=\dprimeddprime[u]$.  Smooth closed factors commute
1551: with $\dprimeddprime$ by the Leibniz rule, and the resulting current stays
1552: positive by \Cref{prop:current-positivity-calculus}.  For a weakly convergent net,
1553: \Cref{lem:continuous-times-positive-current} permits passage to the
1554: limit in the defining equality.  For the last assertion, the functions for
1555: which the claimed current is Bedford--Taylor form a sheaf containing the
1556: smooth psh functions and stable under uniform limits.  The defining closure
1557: property of $\operatorname{CPsh}$ gives the result without a direct smooth
1558: regularization.  These assertions are
1559: \cite[Definition~8.6.2 and Propositions~8.6.3, 8.6.5--8.6.8]{CLD25}.
1560: \end{proof}
1561: 
1562: \begin{proof}[Second proof, item by item]
1563: \emph{Locality.}  Let $(U_i)$ cover $X$ with $T|_{U_i}$ Bedford--Taylor.  If
1564: $u,v$ are continuous psh on an open $V$ with
1565: $\dprimeddprime u=\dprimeddprime v$, then
1566: $\dprimeddprime(uT)=\dprimeddprime(vT)$ holds on each $U_i\cap V$, hence on
1567: $V$ because currents form a sheaf (\Cref{chap:cld-currents}).  Conversely
1568: the restriction of a Bedford--Taylor current is Bedford--Taylor, since the
1569: defining condition quantifies over all opens.  Thus the Bedford--Taylor
1570: currents form a subsheaf of the sheaf of positive closed currents.
1571: 
1572: \emph{The current $\delta_X$.}  For a continuous $u$ one has
1573: $u\delta_X=[u]$ by definition of the integration current, so
1574: $\dprimeddprime(u\delta_X)=\dprimeddprime[u]$, which depends only on
1575: $\dprimeddprime[u]$ tautologically.
1576: 
1577: \emph{Smooth positive closed factors.}  Let $\gamma$ be smooth, positive and
1578: closed, and let $u,v$ be continuous psh with
1579: $\dprimeddprime u=\dprimeddprime v$.  By
1580: \Cref{prop:ch16-smooth-factor},
1581: $\dprimeddprime(u(T\wedge\gamma))=\dprimeddprime(uT)\wedge\gamma$ and
1582: likewise for $v$; the two right-hand sides agree because $T$ is
1583: Bedford--Taylor.  Positivity of $T\wedge\gamma$ is
1584: \Cref{prop:current-positivity-calculus}\,(2), and it is closed because
1585: $\dprime(T\wedge\gamma)=\dprime T\wedge\gamma\pm T\wedge\dprime\gamma=0$.
1586: 
1587: \emph{Weak limits.}  Let $T_k\to T$ weakly with each $T_k$ Bedford--Taylor.
1588: The limit is positive and closed by
1589: \Cref{prop:current-positivity-calculus} and weak continuity of the
1590: differential.  For continuous psh $u$,
1591: \Cref{lem:continuous-times-positive-current} gives $uT_k\to uT$, hence
1592: $\dprimeddprime(uT_k)\to\dprimeddprime(uT)$; the same for $v$.  Passing to
1593: the limit in $\dprimeddprime(uT_k)=\dprimeddprime(vT_k)$ gives the required
1594: equality.
1595: 
1596: \emph{Iteration.}  Fix a Bedford--Taylor current $T$ and let
1597: \[
1598:  \mathscr P(U)=\bigl\{f\in C(U):\ \dprimeddprime(fT|_U)
1599:    \text{ is a Bedford--Taylor current}\bigr\}.
1600: \]
1601: This is a sheaf, by locality just proved.  If $f$ is smooth psh, then
1602: $\dprimeddprime(fT)=\dprimeddprime f\wedge T$ by
1603: \Cref{cor:ch16-smooth-case}, and $\dprimeddprime f$ is a smooth form that is
1604: positive and closed, the latter because
1605: $\dprime\dprimeddprime f=\ddprime\dprimeddprime f=0$; the preceding item
1606: therefore applies and $\dprimeddprime f\wedge T$ is Bedford--Taylor.
1607: Stability of $\mathscr P$ under local uniform limits is
1608: the weak-limit item together with
1609: \Cref{lem:continuous-times-positive-current}.  Now apply
1610: \Cref{lem:ch16-cpsh-induction}.
1611: \end{proof}
1612: 
1613: \begin{corollary}
1614: \label{cor:ch16-bt-times-function}
1615: Let $T$ be a Bedford--Taylor current and let $f$ be a nonnegative locally
1616: constant function.  Then $fT$ is Bedford--Taylor.
1617: \end{corollary}
1618: 
1619: \begin{proof}
1620: Locality (\Cref{prop:bt-current-stability}) reduces to the case of a
1621: constant $f=c\geq0$, where $cT$ is positive and closed and
1622: $\dprimeddprime(u\,cT)=c\,\dprimeddprime(uT)$ by linearity.
1623: \end{proof}
1624: 
1625: CLD state the stronger \cite[Corollary~8.6.7]{CLD25}, for an arbitrary
1626: continuous nonnegative $f$ such that $fT$ is again positive and closed; the
1627: extra input there is a local smooth approximation of $f$ combined with
1628: \Cref{prop:bt-current-stability}.  Only the locally constant case is used
1629: below, so we do not reproduce that argument.
1630: 
1631: \subsection{Dimension one}
1632: \label{sec:ch16-bt-curves}
1633: 
```

```tex
2358: \Cref{sec:ch16-comparison} proves the comparison principle in the case where
2359: it is a theorem---on a tropical chart, where convexity is available---and
2360: records exactly what that case does and does not give.
2361: 
2362: \subsection{A variant adapted to harmonic charts}
2363: \label{sec:ch16-harmonic-continuity}
2364: 
2365: The next statement will be needed in \Cref{sec:ch16-harmonic-charts}, where
2366: the potentials are pullbacks of convex functions under a harmonic chart and
2367: are therefore \emph{not} psh in general: only their products with a positive
2368: closed current are positive.
2369: 
2370: \begin{proposition}
2371: \label{prop:ch16-harmonic-continuity}
2372: Let $(T_a)$ be a weakly convergent net of positive closed currents with
2373: limit $T$, let $f:X\to\mathbf R^m$ be a harmonic chart, and let
2374: $v_i^a\to v_i$ locally uniformly with all $v_i^a,v_i$ continuous convex on
2375: $\mathbf R^m$.  Put $u_i^a=f^*v_i^a$ and $u_i=f^*v_i$.  Then
2376: \[
2377:  u_0^a\,\dprimeddprime u_1^a\wedge\cdots\wedge\dprimeddprime u_q^a\wedge T_a
2378:  \longrightarrow
2379:  u_0\,\dprimeddprime u_1\wedge\cdots\wedge\dprimeddprime u_q\wedge T .
2380: \]
2381: \end{proposition}
2382: 
2383: \begin{proof}
2384: The proof of \Cref{thm:cld-bt-continuity} is repeated verbatim, with a
2385: single change at step (3): positivity and closedness of
2386: $\dprimeddprime(u_1^aS_a)$ are no longer supplied by
2387: \Cref{thm:one-bt-factor}, whose hypothesis is that $u_1^a$ be psh, but by
2388: \Cref{cor:ch16-harmonic-convex-positive}, whose hypothesis is that $u_1^a$
2389: be the pullback of a convex function by a harmonic chart.  All other steps
2390: use only continuity of the potentials and positivity of the currents.  This
2391: is \cite[Proposition~8.7.3]{CLD25}; the reader should note the forward
2392: reference, which is not circular, since
2393: \Cref{cor:ch16-harmonic-convex-positive} is proved from
2394: \Cref{thm:bt-harmonic-compatibility} and
2395: \Cref{thm:cld-bt-continuity}, neither of which uses the present statement.
2396: \end{proof}
2397: 
2398: \section{Chern--Levine--Nirenberg estimates}
2399: \label{sec:ch16-cln}
2400: 
```

```tex
3725: 
3726: \begin{theorem}
3727: \label{thm:bt-harmonic-compatibility}
3728: Let $T$ be a skeletal Bedford--Taylor current and let $\alpha$ be a $G$-form
3729: locally tropicalized by harmonic coordinates.  Then
3730: \[
3731:  \dprime(T\wedge\alpha)=T\wedge\dprime\alpha,
3732:  \qquad
3733:  \ddprime(T\wedge\alpha)=T\wedge\ddprime\alpha.
3734: \]
3735: Consequently, if $T$ is locally a difference of skeletal Bedford--Taylor
3736: currents and $u_1,\ldots,u_q$ are $G$-smooth functions locally tropicalized
3737: by harmonic coordinates, their recursive Bedford--Taylor product equals the
3738: direct product with the $G$-form
3739: $\bigwedge_i\dprimeddprime u_i$.
3740: \end{theorem}
3741: \begin{proof}
3742: Work in a common harmonic tropical chart and subdivide so that the skeletal
3743: support of $T$ is a calibrated weighted complex $C$.  By the definition of
3744: the differential of a current, the difference
3745: $\dprime(T\wedge\alpha)-T\wedge\dprime\alpha$, evaluated on a test form, is
3746: the sum of the boundary terms obtained by applying Stokes on the facets of
3747: $C$.  At a codimension-one face $\tau$, this term is contraction with
3748: \[
3749:              \sum_{\sigma\supset\tau}
3750:                     m_\sigma u_{\sigma/\tau}.
3751: \]
3752: The Bedford--Taylor property of the skeletal current supplies the weighted
3753: balancing relation, while harmonicity says that every harmonic coordinate
3754: has zero total normal slope.  Hence the displayed class vanishes after
3755: pairing with every coefficient of $\alpha$.  There is no residual boundary
3756: current, which proves the $\dprime$ identity.  Applying the involution $J$
3757: gives the $\ddprime$ identity.
3758: 
3759: For the consequence, start with $T$ and define the recursive product one
3760: factor at a time.  The two identities just proved allow each differential
3761: to pass through $T$ and through the previously inserted closed factors.
3762: Thus inserting $u_i$ by the Bedford--Taylor recursion has the same effect as
3763: wedging with the harmonic-chart form $\dprimeddprime u_i$.  Induction on $q$
3764: gives the stated direct product.  Differences are handled by linearity.
3765: This calibrated Stokes computation is
3766: \cite[Proposition~8.11.1 and Corollary~8.11.2]{CLD25}.
3767: \end{proof}
3768: 
3769: The heart of that proof is a single identity, which we isolate because
3770: \Cref{sec:ch16-harmonic-ambiguity} shows that it can fail when the
3771: hypotheses are weakened.
3772: 
3773: \begin{lemma}
3774: \label{lem:ch16-normal-slope-vanishes}
3775: Let $T$ be a skeletal Bedford--Taylor current of type $(p,p)$, let $v$ be a
3776: harmonic parlinear function on $X$, and fix a cellular decomposition
3777: $\mathscr C$ of a compact skeletal neighbourhood $\Sigma\subseteq P^T_f$ on
3778: which $v$ is affine on each cell.  Let $D\in\mathscr C_{p-1}$, and for each
3779: $p$-cell $C\supseteq D$ let $e_C$ be the primitive vector pointing from $D$
3780: into $C$ and normalized so that the canonical calibration of $C$ is
3781: $[\,e_C\wedge\mu_D,\varepsilon_C]$.  Then
3782: \begin{equation}
3783: \label{eq:ch16-normal-slope-sum}
3784:  \sum_{C\supseteq D}\partial_{e_C}\bigl(v|_C\bigr)=0 .
3785: \end{equation}
3786: \end{lemma}
3787: 
3788: \begin{proof}
3789: Harmonicity of $v$ and the Bedford--Taylor property give
3790: $\dprimeddprime(vT)=\dprimeddprime[v]\wedge T=0$ on the interior of the
3791: chart domain.  Since $v$ is parlinear, $\dprimeddprime v=0$ as a $G$-form,
3792: so \eqref{eq:ch16-skeletal-defect} reduces to
3793: \[
3794:  0=\bigl\langle\dprimeddprime(vT),\rho\omega\bigr\rangle
3795:  =-\int^\partial_\Sigma\ddprime v\wedge\rho\omega
3796: \]
3797: for every $f$-tropical symmetric $\omega$ of type $(p-1,p-1)$ and every
3798: smooth $\rho$ with $\rho\omega$ compactly supported in the chart interior.
3799: Fix $x$ in the relative interior of $D$ and choose $\omega=f^*q^*\gamma$,
3800: where $q$ is a torus morphism for which $(q\circ f)_{\mathrm{trop}}$ is a
3801: piecewise immersion of a neighbourhood of $x$ in $D$ into $\mathbf R^{p-1}$,
3802: and take $\rho$ supported so as to meet no $p$-cell other than those
3803: containing $D$.  The computation of
3804: \Cref{thm:ch16-skeletal-product}, performed with $a_C=\partial_{e_C}(v|_C)$,
3805: turns the displayed vanishing into
3806: \[
3807:  \int_D\Bigl(\sum_{C\supseteq D}\partial_{e_C}(v|_C)\Bigr)
3808:    \rho\,\langle f^*q^*\gamma,\mu_D\rangle=0 .
3809: \]
3810: As $\rho$ and $\gamma$ are arbitrary and $q_*f_*\mu_D\neq0$, the bracket
3811: vanishes, which is \eqref{eq:ch16-normal-slope-sum}.
3812: \end{proof}
3813: 
3814: \begin{proof}[Completion of the proof of
3815: \Cref{thm:bt-harmonic-compatibility}]
3816: With $\alpha=u^*\beta$ for a harmonic parlinear $u:W\to\mathbf R^d$, Stokes
3817: on the cells of $\mathscr C$ gives
3818: \[
3819:  \int_{P^T_f}\dprime(\rho\alpha)
3820:  =\sum_{D\in\mathscr C_{p-1}}\int_D
3821:    \Bigl(\sum_{C\in\mathscr C_D}\langle(\rho u^*\beta)_C,\mu_C\rangle\Bigr),
3822: \]
3823: where $\mathscr C_D$ is the set of $p$-cells $C\supseteq D$ on which
3824: $u|_C$ is injective; cells on which $u|_C$ is not injective contribute zero
3825: because $u^*\beta$ vanishes there.  Contracting and pushing forward through
3826: $u$ turns the inner sum into
3827: $\rho\circ u_D^{-1}\bigl\langle\beta,\sum_{C\in\mathscr C_D}u_*\mu_C
3828: \bigr\rangle$, so it suffices to prove
3829: $\sum_{C\in\mathscr C_D}u_*\mu_C=0$.  Since $\mu_C=e_C\wedge\mu_D$, one has
3830: $u_*\mu_C=u_*(e_C)\wedge u_*(\mu_D)$ with $u_*(\mu_D)$ independent of $C$;
3831: and the coordinates of $u_*(e_C)$ are the numbers
3832: $\partial_{e_C}(v|_C)$ as $v$ runs through the components of $u$.  By
3833: \Cref{lem:ch16-normal-slope-vanishes} each coordinate of
3834: $\sum_{C\supseteq D}u_*(e_C)$ vanishes, whence
3835: $\sum_{C\in\mathscr C_D}u_*\mu_C=0$.
3836: \end{proof}
3837: 
3838: \begin{corollary}
3839: \label{cor:ch16-harmonic-convex-positive}
3840: Let $f:U\to\mathbf R^r$ be a harmonic chart and let $F$ be continuous convex.
3841: Then $u=F\circ f$ is locally a difference of psh functions and
3842: $\dprimeddprime u\wedge T$ is positive for every positive closed $T$ for
3843: which the product is defined.
3844: \end{corollary}
3845: \begin{proof}
3846: On every relatively compact convex subset of the tropical target, choose
3847: smooth convex functions $F_j$ converging uniformly to $F$.  The Hessian of
3848: $F_j$ is positive semidefinite, so
3849: $\dprimeddprime(F_j\circ f)$ is a positive harmonic-chart form.  By the
3850: first part of \Cref{thm:bt-harmonic-compatibility}, its wedge with the
3851: positive closed current $T$ is positive.  Bedford--Taylor continuity passes
3852: to the uniform limit and gives positivity of
3853: $\dprimeddprime(F\circ f)\wedge T$.
3854: 
3855: The same local regularization writes $F\circ f$ as a locally approachable
3856: psh function; in particular it is a difference of psh functions, trivially
3857: by subtracting the psh constant zero.  If one works with a signed harmonic
3858: chart presentation, decompose it into the difference of the two convex
3859: presentations supplied by the chart.  This is
3860: \cite[Corollary~8.11.3]{CLD25}.  The conclusion concerns convex functions in
3861: harmonic charts and does not identify arbitrary classically psh functions
3862: with the CLD approximation sheaf.
3863: \end{proof}
3864: 
3865: \section{Harmonic ambiguity}
3866: \label{sec:ch16-harmonic-ambiguity}
3867: 
3868: \Cref{def:ch16-bt-current} isolated the property that makes
```

## AFTER: manuscript/parts/part2/ch16_bedford_taylor.tex
SHA256 41333978fbce28644d1f63aac6431f763dd3f3cc1dd792faf1b20b43ab3a9e83

```tex
1612: 
1613: \begin{corollary}
1614: \label{cor:ch16-bt-times-function}
1615: Let $T$ be a Bedford--Taylor current and let $f$ be a nonnegative locally
1616: constant function.  Then $fT$ is Bedford--Taylor.
1617: \end{corollary}
1618: 
1619: \begin{proof}
1620: Locality (\Cref{prop:bt-current-stability}) reduces to the case of a
1621: constant $f=c\geq0$, where $cT$ is positive and closed and
1622: $\dprimeddprime(u\,cT)=c\,\dprimeddprime(uT)$ by linearity.
1623: \end{proof}
1624: 
1625: The arbitrary continuous multiplier in the printed statement of
1626: \cite[Corollary~8.6.7]{CLD25} requires care: multiplying by a nonnegative
1627: function preserves positivity but does not automatically preserve
1628: closedness.  Even for smooth $f$, the Leibniz rule gives
1629: $\dprime(fT)=\dprime f\wedge T$ when $T$ is closed.  Smooth approximation
1630: of $f$ therefore does not supply a sequence of closed Bedford--Taylor
1631: currents to which \Cref{prop:bt-current-stability} applies.  We use only
1632: the locally constant assertion proved above; no assertion for arbitrary
1633: continuous multipliers is needed below.
1634: 
1635: \subsection{Dimension one}
1636: \label{sec:ch16-bt-curves}
1637: 
1638: In analytic dimension one the ambiguity can be removed throughout the normal
1639: category over an arbitrary complete non-Archimedean ground field, including a
```

```tex
2365: 
2366: \subsection{A variant adapted to harmonic charts}
2367: \label{sec:ch16-harmonic-continuity}
2368: 
2369: For a harmonic chart, convexity on the target must be distinguished from
2370: membership in the ordinary CLD sheaf $\operatorname{CPsh}_X$.  The following
2371: version of the continuity statement retains that membership explicitly.
2372: It will apply whenever a separate analytic argument establishes pshness of
2373: the pullbacks; the formal-metric argument in
2374: \Cref{thm:ch19-canonical-positivity} is one such instance.
2375: 
2376: \begin{proposition}
2377: \label{prop:ch16-harmonic-continuity}
2378: Let $(T_a)$ be a weakly convergent net of positive closed currents with
2379: limit $T$, let $f:X\to\mathbf R^m$ be a harmonic chart, and let
2380: $v_i^a\to v_i$ locally uniformly with all $v_i^a,v_i$ continuous convex on
2381: $\mathbf R^m$.  Put $u_i^a=f^*v_i^a$ and $u_i=f^*v_i$.  Assume, for
2382: $1\leq i\leq q$, that $u_i^a$ and $u_i$ belong to the ordinary sheaf
2383: $\operatorname{CPsh}_X$.  Then
2384: \[
2385:  u_0^a\,\dprimeddprime u_1^a\wedge\cdots\wedge\dprimeddprime u_q^a\wedge T_a
2386:  \longrightarrow
2387:  u_0\,\dprimeddprime u_1\wedge\cdots\wedge\dprimeddprime u_q\wedge T .
2388: \]
2389: \end{proposition}
2390: 
2391: \begin{proof}
2392: The image under the continuous map $f$ of a compact subset of $X$ is compact.
2393: Thus local uniform convergence on the target implies local uniform
2394: convergence of every $u_i^a$ to $u_i$.  The stated psh hypotheses now allow
2395: direct application of \Cref{thm:cld-bt-continuity}.
2396: \end{proof}
2397: 
2398: The more general formulation of \cite[Proposition~8.7.3]{CLD25} invokes
2399: \cite[Corollary~8.11.3]{CLD25} to obtain positivity at each recursive
2400: step.  In the proof available here, harmonic-chart compatibility requires
2401: a skeletal Bedford--Taylor current
2402: (\Cref{thm:bt-harmonic-compatibility}); positivity and closedness alone
2403: are not those hypotheses.  Accordingly we do not remove the explicit
2404: $\operatorname{CPsh}_X$ assumption by that argument.
2405: 
2406: \section{Chern--Levine--Nirenberg estimates}
2407: \label{sec:ch16-cln}
```

```tex
3844: \end{proof}
3845: 
3846: \begin{corollary}
3847: \label{cor:ch16-harmonic-convex-positive}
3848: Let $f:U\to\mathbf R^r$ be a harmonic chart, let $F$ be a continuous
3849: convex function on $\mathbf R^r$, and let $T$ be a skeletal Bedford--Taylor
3850: current on $U$.  Then the current
3851: $\dprimeddprime\bigl((F\circ f)T\bigr)$ is positive and closed.
3852: \end{corollary}
3853: \begin{proof}
3854: Convolution with nonnegative smooth approximate identities gives smooth
3855: convex functions $F_j$ converging to $F$ locally uniformly.  Put
3856: $u_j=F_j\circ f$.  The positive semidefinite Hessian of $F_j$ makes
3857: $\dprimeddprime u_j$ a positive harmonic-chart $G$-form.  Applying
3858: \Cref{thm:bt-harmonic-compatibility} first to $u_j$ and then to
3859: $\ddprime u_j$ gives
3860: \[
3861:  \dprimeddprime(u_jT)=T\wedge\dprimeddprime u_j\geq0.
3862: \]
3863: These currents are closed, since they are $\dprimeddprime$-exact.
3864: Continuity of $f$ gives $u_j\to F\circ f$ locally uniformly.  By
3865: \Cref{lem:continuous-times-positive-current}, $u_jT\to(F\circ f)T$;
3866: continuity of the current differentials and closedness of the positive cone
3867: give the asserted positive closed limit.
3868: \end{proof}
3869: 
3870: This argument retains the hypotheses of
3871: \cite[Proposition~8.11.1]{CLD25}.  It does not justify the assertion for
3872: arbitrary positive closed currents printed in
3873: \cite[Corollary~8.11.3]{CLD25}.  Nor does it show that $F\circ f$ is
3874: locally approachable in the ordinary CLD sense: $F_j\circ f$ is
3875: $G$-smooth, and need not be ordinary smooth.  In the analytic setting,
3876: strictly parlinear harmonic coordinates over a nontrivially valued field
3877: admit a separate psh argument using residual line bundles
3878: \cite[Corollary~18.8.9]{CLD25}; its application to canonical metrics is
3879: spelled out in \Cref{thm:ch19-canonical-positivity}.
3880: 
3881: \section{Harmonic ambiguity}
3882: \label{sec:ch16-harmonic-ambiguity}
```

## BEFORE: manuscript/parts/part2/ch19_cld_examples.tex
Commit 10897afc0b7379ee169f46ecb77184ac7580f177; SHA256 dbd90da1e3ff05f3aba9753faecc6789d03a44ba46cbf1cd0846aed0e334e52a

```tex
2596: \begin{theorem}
2597: \label{thm:ch19-canonical-positivity}
2598: Assume the absolute value of \(K\) is nontrivial and keep the notation
2599: above.  The following are equivalent:
2600: \begin{enumerate}
2601: \item\label{itm:ch19-pos:psh} the cubical metric of \(L\) is psh;
2602: \item\label{itm:ch19-pos:current} \(c_1(\overline L)\geq0\);
2603: \item\label{itm:ch19-pos:data} the quadratic form \(q_L\) is positive
2604:  semidefinite and the residual line bundle \(\mathcal M_s\) is nef on the
2605:  abelian variety \(\mathcal B_s\);
2606: \item\label{itm:ch19-pos:nef} \(L\) is nef.
2607: \end{enumerate}
2608: Moreover \(c_1(\overline L)=0\) if and only if \(L\) is translation
2609: invariant, if and only if \(q_L=0\) and \(\mathcal M_s\) is numerically
2610: trivial; and \(L\) is ample if and only if \(\mathcal M_s\) is ample and
2611: \(q_L\) is positive definite.
2612: \end{theorem}
2613: 
2614: \begin{proof}
2615: This is \cite[Proposition~19.3.1, Corollary~19.3.2 and
2616: Theorem~B.6.4]{CLD25}.  The implication
2617: \cref{itm:ch19-pos:psh}$\Rightarrow$\cref{itm:ch19-pos:current} is
2618: \Cref{prop:cld-psh-positive-current}.  For
2619: \cref{itm:ch19-pos:data}$\Rightarrow$\cref{itm:ch19-pos:psh}: nefness of
2620: $\mathcal M_s$ makes $q^*\overline M$ psh by
2621: \Cref{thm:gk-formal-positivity-comparison}; the function $\tau$ is harmonic
2622: and piecewise linear and $q_L$ is convex, so $\tau^*(\tfrac12q_L)$ is psh by
2623: \Cref{cor:ch16-harmonic-convex-positive}; and $p^*\overline L$ is the
2624: product of these two psh metrics by
2625: \eqref{eq:ch19-canonical-weight}.  Since $p$ has local sections,
2626: $\overline L$ is psh.
2627: 
2628: For \cref{itm:ch19-pos:current}$\Rightarrow$\cref{itm:ch19-pos:data}, two
2629: separate arguments are needed.  Over a rigid point $b\in B$ the residual
2630: bundle of $M$ is trivial, so on a neighbourhood $U$ of $b$ the metrized
2631: bundle $q^*\overline M$ is trivial and $E$ is trivialized, whence
2632: $c_1(p^*\overline L)=\tau^*(\tfrac12\dprimeddprime q_L)$ there; positivity
2633: of a form pulled back by a surjection onto $N_{\mathbf R}$ forces
2634: $\dprimeddprime q_L\geq0$, that is, $q_L$ positive semidefinite.  For the
2635: residual nefness, let $\omega$ be the standard invariant $(1,1)$-form on
2636: $N_{\mathbf R}$; then $\tau^*\omega^r$ kills the second term of
2637: \eqref{eq:ch19-canonical-curvature} for dimension reasons, so
2638: $c_1(q^*\overline M)\wedge\tau^*\omega^r\geq0$, and the fibre-integration
2639: projection formula \Cref{thm:cld-fibre-projection} converts this into
2640: $\langle c_1(\overline M),\alpha\rangle\geq0$ for every positive smooth
2641: $\alpha$ on $B$, hence $c_1(\overline M)\geq0$ and $\mathcal M_s$ is nef by
2642: \Cref{thm:gk-formal-positivity-comparison}.
2643: 
2644: Equivalence with \cref{itm:ch19-pos:nef} in the algebraic case: if $L$ is nef,
2645: split $L^2=L_+\otimes L_-$ with $L_+$ symmetric and $L_-$ antisymmetric, so
2646: $c_1(\overline{L_-})=0$; for an ample symmetric $N$ the bundle
2647: $L_+^{t}\otimes N$ is ample for all $t\geq0$ by Nakai--Moishezon and its
2648: cubical metric is psh, whence $tc_1(\overline{L_+})+c_1(\overline N)\geq0$
2649: and, dividing by $t\to\infty$, $c_1(\overline{L_+})\geq0$.  Conversely if
2650: the metric is psh then for every irreducible curve $C\subset A$ one has
2651: $(L\cdot C)=\int_{C^{\An}}c_1(\overline L|_{C^{\An}})\geq0$ by
2652: \Cref{prop:ch16-degree-formula}, so $L$ is nef.  The statements about
2653: triviality and ampleness are the cited corollary and theorem.
2654: \end{proof}
2655: 
2656: \subsection{Ordinary delta-metricity}
2657: \label{sec:ch19-canonical-delta-metricity}
2658: 
2659: We can now decide exactly when the quadratic factor in
2660: \eqref{eq:ch19-canonical-weight} belongs to the ordinary
2661: Gubler--K\"unnemann delta-form category.  The point is not merely that the
2662: coordinates of \(\tau\) fail to be smooth.  One must recover their first
```

## AFTER: manuscript/parts/part2/ch19_cld_examples.tex
SHA256 4d59d219eec46bea029d6d131e6f55c110a7fbf4c3f30be9dcf4147a4c5a6652

```tex
2596: \begin{theorem}
2597: \label{thm:ch19-canonical-positivity}
2598: Assume the absolute value of \(K\) is nontrivial and keep the notation
2599: above.  The following are equivalent:
2600: \begin{enumerate}
2601: \item\label{itm:ch19-pos:psh} the cubical metric of \(L\) is psh;
2602: \item\label{itm:ch19-pos:current} \(c_1(\overline L)\geq0\);
2603: \item\label{itm:ch19-pos:data} the quadratic form \(q_L\) is positive
2604:  semidefinite and the residual line bundle \(\mathcal M_s\) is nef on the
2605:  abelian variety \(\mathcal B_s\);
2606: \item\label{itm:ch19-pos:nef} \(L\) is nef.
2607: \end{enumerate}
2608: Moreover \(c_1(\overline L)=0\) if and only if \(L\) is translation
2609: invariant, if and only if \(q_L=0\) and \(\mathcal M_s\) is numerically
2610: trivial; and \(L\) is ample if and only if \(\mathcal M_s\) is ample and
2611: \(q_L\) is positive definite.
2612: \end{theorem}
2613: 
2614: \begin{proof}
2615: This is \cite[Proposition~19.3.1, Corollary~19.3.2 and
2616: Theorem~B.6.4]{CLD25}.  The implication
2617: \cref{itm:ch19-pos:psh}$\Rightarrow$\cref{itm:ch19-pos:current} is
2618: \Cref{prop:cld-psh-positive-current}.  For
2619: \cref{itm:ch19-pos:data}$\Rightarrow$\cref{itm:ch19-pos:psh}: nefness of
2620: $\mathcal M_s$ makes $q^*\overline M$ psh by
2621: \Cref{thm:ch17-psh-residual-nef}, since its residual bundles are pullbacks
2622: of the nef bundle $\mathcal M_s$.  We justify separately that
2623: $\tau^*(\tfrac12q_L)$ is psh; harmonicity by itself is not an ordinary
2624: smooth-approximation argument.
2625: 
2626: Choose a lattice basis and write $h_1,\ldots,h_r$ for the coordinates of
2627: $\tau$.  By \Cref{prop:ch19-tau-coordinates}, each $h_j$ is an integral
2628: parlinear function with $\dprimeddprime[h_j]=0$.  The trivial line bundles
2629: with weights $h_j$ and $-h_j$ therefore both have zero first Chern current.
2630: Applying \Cref{thm:ch17-psh-residual-nef} to these two metrics shows that
2631: both $h_j$ and $-h_j$ are continuous psh.  Consequently every real affine
2632: function of $(h_1,\ldots,h_r)$ is psh, by the convex-cone property of the
2633: CLD sheaf and the inclusion of constants.
2634: 
2635: Put $F=\tfrac12q_L$.  Its Hessian $H$ is a constant positive semidefinite
2636: matrix.  For $a\in\mathbf R^r$ let
2637: $\ell_a(t)=F(a)+\nabla F(a)\cdot(t-a)$.  Then
2638: \[
2639:  0\leq F(t)-\ell_a(t)
2640:        =\tfrac12(t-a)^{\mathsf T}H(t-a)
2641:        \leq\tfrac12\|H\|\,\|t-a\|^2.
2642: \]
2643: On a fixed compact subset of $\mathbf R^r$, choose a finite
2644: $\varepsilon$-net $(a_j)$.  The convex function $\max_j\ell_{a_j}$ differs
2645: from $F$ there by at most $\tfrac12\|H\|\varepsilon^2$.  Its pullback by
2646: $\tau$ is a finite maximum of continuous psh functions, hence psh.
2647: As $\varepsilon\downarrow0$, these pullbacks converge uniformly on each
2648: fixed compact analytic neighbourhood under consideration.  Stability under
2649: local uniform limits gives $F\circ\tau$ psh.  If $r=0$, this assertion
2650: just says that a constant is psh.  This is the quadratic instance of the
2651: analytic result \cite[Corollary~18.8.9]{CLD25}; it does not use the
2652: general harmonic-chart assertion discussed in
2653: \Cref{cor:ch16-harmonic-convex-positive}.
2654: 
2655: The quadratic function $f$ in the metric decomposition differs from $F$
2656: by a real affine function, whose pullback is psh by the preceding
2657: argument.  Thus $f\circ\tau$ is psh as well.  Now $p^*\overline L$ is the
2658: product of these two psh metrics by
2659: \eqref{eq:ch19-canonical-weight}.  Since $p$ has local sections,
2660: $\overline L$ is psh.
2661: 
2662: For \cref{itm:ch19-pos:current}$\Rightarrow$\cref{itm:ch19-pos:data}, two
2663: separate arguments are needed.  Over a rigid point $b\in B$ the residual
2664: bundle of $M$ is trivial, so on a neighbourhood $U$ of $b$ the metrized
2665: bundle $q^*\overline M$ is trivial and $E$ is trivialized, whence
2666: $c_1(p^*\overline L)=\tau^*(\tfrac12\dprimeddprime q_L)$ there; positivity
2667: of a form pulled back by a surjection onto $N_{\mathbf R}$ forces
2668: $\dprimeddprime q_L\geq0$, that is, $q_L$ positive semidefinite.  For the
2669: residual nefness, let $\omega$ be the standard invariant $(1,1)$-form on
2670: $N_{\mathbf R}$; then $\tau^*\omega^r$ kills the second term of
2671: \eqref{eq:ch19-canonical-curvature} for dimension reasons, so
2672: $c_1(q^*\overline M)\wedge\tau^*\omega^r\geq0$, and the fibre-integration
2673: projection formula \Cref{thm:cld-fibre-projection} converts this into
2674: $\langle c_1(\overline M),\alpha\rangle\geq0$ for every positive smooth
2675: $\alpha$ on $B$, hence $c_1(\overline M)\geq0$ and $\mathcal M_s$ is nef by
2676: \Cref{thm:ch17-psh-residual-nef}.
2677: 
2678: Equivalence with \cref{itm:ch19-pos:nef} in the algebraic case: if $L$ is nef,
2679: split $L^2=L_+\otimes L_-$ with $L_+$ symmetric and $L_-$ antisymmetric, so
2680: $c_1(\overline{L_-})=0$; for an ample symmetric $N$ the bundle
2681: $L_+^{t}\otimes N$ is ample for all $t\geq0$ by Nakai--Moishezon and its
2682: cubical metric is psh, whence $tc_1(\overline{L_+})+c_1(\overline N)\geq0$
2683: and, dividing by $t\to\infty$, $c_1(\overline{L_+})\geq0$.  Conversely if
2684: the metric is psh then for every irreducible curve $C\subset A$ one has
2685: $(L\cdot C)=\int_{C^{\An}}c_1(\overline L|_{C^{\An}})\geq0$ by
2686: \Cref{prop:ch16-degree-formula}, so $L$ is nef.  The statements about
2687: triviality and ampleness are the cited corollary and theorem.
2688: \end{proof}
2689: 
2690: \subsection{Ordinary delta-metricity}
2691: \label{sec:ch19-canonical-delta-metricity}
2692: 
2693: We can now decide exactly when the quadratic factor in
2694: \eqref{eq:ch19-canonical-weight} belongs to the ordinary
2695: Gubler--K\"unnemann delta-form category.  The point is not merely that the
2696: coordinates of \(\tau\) fail to be smooth.  One must recover their first
```

