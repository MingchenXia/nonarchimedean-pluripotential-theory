# Positive weights: analytic estimates and source conventions

Date: 8 October 2026. Source checkpoint before book integration.
Preservation baseline: `b2464f53a8af822005cdbec414b63463207e85cc`.

Simon Jubert and Chung-Ming Pan, *Extremal Sasaki manifolds and weighted
K-stability*, [arXiv:2610.10216v1](https://arxiv.org/abs/2610.10216v1),
submitted 7 October 2026, has been read in full: all thirty physical pages,
complete selected text and fifteen individually displayed matching images,
with sequential notes. Two primary dependencies have fourteen selected
pages in eight individually displayed images. The combined scope is
**44 distinct exact-source/page pairs in 23 images**, one complete reading
and two partial readings. Search results, acquisition, prepared views and
references to other papers receive no proof-reading credit.

The directly checked smooth analytic estimates remove log-concavity from
the specified PDE systems. Several introductory and geometric formulations
must not be copied as printed. This review separates those issues from the
analytic estimates: it does not claim that every statement of the paper
has been independently verified or that its main estimate is disproved.

| Exact controlling file | Actually read physical pages | PDF SHA-256 |
| --- | --- | --- |
| Jubert–Pan, 2610.10216v1, thirty-page PDF | All 1–30 | `f0e067da80dce5007e29f926c2e328703eb09be3fbd9b1232c2fe28cb21abfcb` |
| Apostolov–Jubert–Lahdili, published Geometry & Topology 27(8), 3229–3302, DOI 10.2140/gt.2023.27.3229; publisher PDF has 77 physical pages including additional material | 2–3, 6, 13–15, 61; seven pages | `d22c49681931ebbd582cb2cda48a5a0178f9c07b782ae34d6ae10cdf2bc690bd` |
| Lahdili, 1808.07811v4, revised 27 April 2019, forty-seven-page preprint PDF | 1–2, 7, 11–12, 19–20; seven pages | `48e769d2e01bb748d4477df7b1b697b95464828c1c3663cf7221c08ef47abb56` |

## Safe analytic scope

**PW01 — Local units.** Jubert–Pan use d^c=i(bar partial−partial),
dd^c=2i partial bar partial, and Ric=−dd^c log omega^n. Relative to the
book's dd^c these are multiplied by 4pi; the source Ricci form is twice
the usual Ricci form. Preserve the entire set of operators, moment maps,
potential units and Fano class together. Write a separate prescribed
function h for the second PDE, so geometric weights are not silently
identified with an inconsistently normalized right-hand side.

**PW02 — Precise Theorem 2.1.** Physical 9–17 contains the statement and
complete smooth proof. For n>=2, positive smooth v and a bounded smooth
prescribed h, the system v(m_phi)omega_phi^n=e^F omega^n,
Delta_phi,v F=−h(m_phi)+tr_phi,v Ric(omega) gives reverse trace in
L^(2p+2) and forward trace in L^((2p+2)/(n−1)), p>=1.
Constants depend on bounded phi and F, the fixed background and torus
basis, positive min(v), sup(v), derivatives of log v through order two,
sup|h| and normalized moment/Ricci coordinates. The overview's
solution-independent constant omits this dependence. The second exponent
has no literal n=1 interpretation; no artificial endpoint is assigned.

The key cancellation, Claim 2.2 and equations (2.3)–(2.4) on physical
10–11, converts the weighted Hessian term into background torus-metric
data and cancels the derivative of reverse trace against the weighted
drift. No sign of Hessian(log v) is needed. The auxiliary functions and
the two integrations by parts retain derivatives of v. Choosing
a=(p^2+1)/(2p) absorbs the gradient term; a sufficiently large b and
Hölder close the trace moments. These are attributed source arguments,
not a newly proved book theorem.

**PW03 — Twisted estimate.** Theorem 2.3 and its complete proof on
physical 17–20 replace F by F+f in the second equation, introduce a fixed
closed torus-invariant beta with a chosen moment map, and assume
beta+dd^c f>=0. Retain the proof's sup(phi)=sup(f)=0 normalization and
bounded phi,F+f. Its conclusion is
integral e^((k−1)f)(forward trace)^k omega^n<=Ck for k>=1.
The extra hypothesis integral e^(−p0 f)omega^n<=M, p0>1, gives an
unweighted L^q estimate only for 1<q<p0. F itself need not be bounded;
the proof retains reciprocal-trace remainders. Total weighted mass is
bounded by sup(v) times the fixed ordinary volume, closing the lower
moments without an illicit bound on F. The continuity theorem cited from
DJL26 is not recursively reread here.

**PW04 — Smooth soliton estimate.** Theorem 3.1 on physical 20–22 has a
direct maximum-principle proof for a smooth Fano manifold in the source
class 4pi c1(X), positive smooth v and bounded phi in
v(m_phi)omega_phi^n=e^(−phi+h_omega)omega^n. Its forward pointwise trace
bound follows from reverse trace and the volume equation. Proposition
3.2 additionally imports finite-energy regularization from Han–Li;
Remark 3.3's log-Fano extension is left to readers. Neither singular
regularity nor a log-Fano correspondence is certified by this checkpoint.

## Printed formulas and hypotheses excluded from import

**PW05 — Geometric scalar versus PDE h.** The source defines
Scal_v=v tr_phi,v Ric_v on physical 6 and Scal_v=w on 7. Its volume
equation implies Ric_v=Ric(omega)−dd^c F; consequently the second
equation has prescribed h=w/v. Physical 9 instead prints −w and calls
the system equivalent. Positivity of v allows reparametrization for the
analytic estimate, but the book must display h separately. This does not
authorize transporting every variational consequence without checking.

**PW06 — Mabuchi variation.** Physical 8 prints an extra factor v in
integral f(w−Scal_v)v omega_phi^n, while its condition (1.4) has no v.
Published AJL Definition 1.1 and Remark 1.2, physical 14/printed 3241,
give the variation with omega^[n] and no extra v, and the matching
constant-invariance condition. Lahdili v4 Definition 5, physical 11,
equation (14), agrees after including its slope constant in w. The
printed JP formula is not imported. A formal zero-mean diagnostic on
[0,1] has integral(x−1/2)=0 but integral(1+x)(x−1/2)=1/12;
an unweighted mean condition alone does not remove that extra factor.
This diagnostic is not advertised as a new geometric counterexample.

**PW07 — Automorphism quotient.** JP Theorem B uses T_C for an arbitrary
compact reduced torus. Published AJL Theorem 1, physical 6/printed 3233,
requires maximal T; its immediate discussion and Remark 7.7 on physical
61/printed 3288 replace T_C by the connected centralizer for nonmaximal T.
AJL Proposition 1.4/Theorem 1.5 on physical 15 give the same distinction.
The trivial-torus CP^1 automorphism orbit illustrates the obstruction:
in the usual reference units, J=t coth(t)−1 tends to infinity, while
the Mabuchi energy is constant along the cscK orbit. This is a direct
worked source-hypothesis diagnostic, without a new theorem or independent
model receipt. Theorem B is not imported as printed.

**PW08 — Weighted Futaki correction.** JP physical 23 prints 8pi times
ordinary Vol(X,alpha). Published AJL physical 6 and Lahdili v4 Definition
11/Remark 6 on physical 19 use
8pi integral_X v(m_omega)omega^[n]. Both sources use divided powers.
The missing v is independent of harmless overall normalization. For a
constant weight v=a, the trivial-product calculation in the original
formula cancels; replacing its correction by ordinary volume leaves
8pi(1−a)Vol in complex dimension one. This is a direct normalization
check, not a new invariant theorem. JP Corollary C and its printed
stability definition are not treated as a verified algebraic equivalence.

**PW09 — Geometric applications.** Section 4's Sasaki construction fixes
a regular free circle reference chi and smooth quotient X_chi. The
candidate Reeb can be irregular inside the specified deformation family.
The weights ell^(−n−1),ell^(−n−3) are positive on the fixed polytope;
log v has positive semidefinite Hessian and is not log-concave for a
nonconstant ell. The reduction is attributed to AC21/ACL21, whose full
proofs are not reread. The cone comparison also requires vanishing contact
Futaki in its constant-scalar setting and distinguishes normal central
fibers. Do not infer a theorem for every irregular Sasaki manifold.

JP Section 4.4 initially allows a general Kähler class, while its
Corollary C requires polarization. Its identification of cKEM with
weighted extremal also requires controlling the extremal affine factor:
Lahdili v4 physical 1–2 places the cKEM reduction in the weighted cscK
equation. Corollaries 4.7–4.8 are excluded from verified theorem import,
pending consistent definitions and complete dependent proofs.

## Evidence and status

Five exact diagnostic groups pass: gradient/Holder parameters,
determinant trace comparison in dimensions two through four,
reciprocal-affine log-convexity, variational/Futaki normalization and
the CP^1 orbit integral. The first diagnostic helper failed because a
Laurent expression was passed to a polynomial constructor; the unchanged
failure is preserved and a separately numbered v2 clears positive
denominators. This was not a failed mathematical inequality.

The companion sequential notes and manifest preserve exact PDF, full
selected-text, image and note hashes. The review does not claim a fresh
ordered whole-book reread, an exhaustive literature search, an independent
gpt-6.1-sol xhigh receipt, original theorem promotion, or a solution of a
canonical open problem. The **42 atoms in twelve problem environments**,
the general BJ22 critical homogeneous Siu-division/envelope input **OPEN**,
and the LPWZ density candidate **UNVERIFIED** retain their statuses.
