# Proposal excerpt read for this bounded check

Snapshot taken 1 September 2026. The source was a mutable authored draft;
the hash below identifies the bytes read, not a frozen or audited full proof.

Source: /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_ordinary_open_outer_collar_research_20260831/RESEARCH_NOTE.md

Full draft bytes: 28882. SHA-256: 2ff98181aa3bedb0fda36a0495a7336a3ca55836c02e4b43fc3ed0dddd873c0a.

Only the following Section 10 example is the subject of this diagnostic.
The remaining outer-collar proof was not independently audited here.

## 10. Why independence cannot simply be dropped

There is an elementary all-source topological obstruction at dependent weights. Take K=C((pi)). Blow up P^1_R at one closed special-fibre point, obtaining the regular strictly semistable curve model with a node xy=pi. Take its product with P^1_R. The selected two vertical components meet in the proper curve C=P^1_k; their tube is an annulus factor times the good-reduction analytic curve.

At the monomial point above eta_C with alpha_x=alpha_y=ell/2, the Gauss rule gives
\[
                        |y^2-\pi|=|\pi|.
\]
Hence
\[
                    W=\{|y^2-\pi|>|\pi|/2\}\cap X_C
                                                        \tag{10.1}
\]
is an ordinary neighbourhood of that point.

Every normal box about (ell/2,ell/2), and every shallow residual interval in a chosen p-tube, has actual source points with y=sqrt(pi), x=sqrt(pi), after viewing points over the finite extension as ordinary Berkovich points over K. A Gauss point of any prescribed shallow w-radius supplies the residual factor. These points have the required normal and residual radii but lie outside W. They are not Gauss points for the normal moment, which is precisely why checking only a skeleton would miss them.

Thus no whole inverse-image normal-box collar lies in W at these weights. Nor can a finite exceptional set repair the cofinite outer-collar statement: choose p outside that set. This is a counterexample to dropping (1.1) from (1.2), not a counterexample to closed-current rigidity. The example introduces no pullback of an unknown current.
