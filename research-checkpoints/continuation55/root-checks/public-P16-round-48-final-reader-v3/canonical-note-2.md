ID: n2

SUMMARY:
Source-established arbitrary-support theorem over algebraically closed trivially valued characteristic-zero fields: smooth integral projective X, ample L, arbitrary dimension, genuine finite-energy MA, raw mass (L^n), finite dual energy and uniqueness modulo constants. Partial for original P16.6.

DETAILED SUMMARY:
Boucksom–Jonsson 1801.08229v4 constructs the approximation-independent genuine finite-energy operator and solves the equation for every positive Radon target of raw mass V=(L^n) and finite dual energy. No skeletal-support or toric-invariance hypothesis occurs. The proof supplies compactness, envelopes, finite-energy differentiation, continuity of integration, comparison and injectivity. This established trivial-field result does not automatically transfer to discrete or arbitrary fields.

SUPPORT:
["n1"]

TEXT:
Retain k algebraically closed, trivially valued and of characteristic zero; X/k smooth, connected, integral and projective, dimension n≥1 arbitrary; L ample; and the canonical trivial-field reference metric. Let V=(L^n)>0. Normalize intersection energy by E(0)=0 and E(u+c)=E(u)+c, and define E1={u psh:E(u)>−infinity}.

The exact target condition is positivity and Radon regularity, mu(Xan)=V, and raw dual energy sup_{a in model/FS tests}{V E(a)−integral a dmu}<infinity. For the entire probability nu=mu/V, this equals V Q(nu), where Q(nu)=sup_a{E(a)−integral a dnu}. No restriction of a target is renormalized. Constants make the raw supremum infinite at incorrect mass.

This theorem is already established in 1801.08229v4. Theorem 7.1 extends the genuine intersection pairing by majorants, uniquely and continuously along decreasing nets. Theorem 7.8 makes mixed pairings finite on E1. Theorem 7.18 tests this pairing against PL functions: positivity, mass V on constants, PL density and Riesz give a unique positive Radon MA measure. Proposition 7.19 verifies the model intersection formula and decreasing continuity. Therefore every decreasing model approximation gives the same genuine raw operator M(u), of mass V. No inverse measure construction is substituted.

Theorem 5.20 supplies the envelope property under the retained hypotheses; Corollary 5.21 gives compact normalized PSH; Lemma 5.17 gives continuous envelopes. Theorem 8.5/Corollary 8.6 gives differentiation through the envelope, with derivative integral f d(M(u)/V). Theorem 9.20 identifies finite Q with integrability of every E1 potential. Proposition 9.19 proves L1(nu) continuity on bounded-energy sets.

The printed proof of Theorem 12.8 normalizes a maximizing sequence for E−integral against nu, bounds its energy by (9.11), extracts a psh subnet using compactness, and uses Proposition 9.19 and energy upper semicontinuity to prove actual attainment. Corollary 9.12 identifies its maximizer with the genuine MA solution. Conversely, concavity and integrability against its own MA give Q(M(u)/V)=E(u)−integral u d(M(u)/V)<infinity. Thus the range is exactly the stated raw-mass-V finite-dual-energy measures. Theorems 7.40 and 7.44 give locality and comparison; Proposition 12.7 gives injectivity modulo constants; Theorem 12.9 concludes existence and uniqueness.

There is no support restriction, torus action or dimension-one assumption. The application is written in P16.6-argument.md and standalone P16.6-paper.tex/P16.6-paper.pdf; rerun `python3 build_artifacts.py`. This is a source-established mathematical theorem, not a finite computation. It remains partial for original P16.6 because its trivial-field hypotheses are not transported to other fields by unproved base change or measure completeness.

Artifacts: /workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo
