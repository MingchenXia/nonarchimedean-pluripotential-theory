# P18.1 solver dossier: continuity of the Favre--Pille-Schneider hybrid extension

Date of audit: 2026-08-25 (Asia/Shanghai).

Status: **historical base-scalar counterexample, production Rethlas
final/correct and integrated; superseded in scope by the verified normalized
counterexample**.

**Controlling 25 August addendum.**  The later fibre-dependent log-sum-exp
construction has zero supremum relative to the Fubini--Study model metric on
every complex fibre and on the non-Archimedean fibre, yet remains hybrid
discontinuous.  It passed production run
`20260825T035945Z_070e264c3ef1`, item
`pi_db89dd432acabcf33a3f2272`, final `correct`, with zero critical errors and
zero gaps, and is now integrated in Chapter 66.  The exact adapted live bytes
then passed run `20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`, with the same clean verdict.  It retires the former
normalized residual from Chapter 72.  Statements below saying that the
normalized problem remains open are preserved only as the earlier
base-scalar audit stage and are superseded by this addendum.

The user explicitly authorized submission of the frozen theorem and proof to
the local production Rethlas service.  The exact submitted bytes, digests, and
service artifacts are preserved in the receipt named in Section 9.

## 1. Verdict

Endpoint continuity does **not** force continuity of the canonical glued hybrid
metric.  The failure already occurs for the smooth trivial polarized
degeneration
\[
 \mathbf P^1_{\mathbf C}\times\mathbb D^*\longrightarrow\mathbb D^*.
\]
The metric on the punctured total space can be smooth and semipositive, can
extend as a finite psh metric to the product model, and can have the continuous
Fubini--Study model metric as its associated non-Archimedean metric, while its
canonical hybrid psh extension is discontinuous.

This is not an arbitrary set-theoretic gluing example.  The metric satisfies the
actual logarithmic-growth and positivity hypotheses of
Pille-Schneider's Theorem 3.13, and the discontinuous glued object is precisely
the canonical hybrid psh metric produced by that theorem.

The same construction separately refutes the reverse implication in Favre's
literal Question 1: all three intrinsic conditions listed there hold, but the
potential is not uniform.  This second conclusion is checked directly and does
not assume that Favre's formulation is equivalent to Pille-Schneider's metric
formulation.

The counterexample is a base-scalar defect.  It disappears after quotienting
metrics by arbitrary functions pulled back from the base, or after imposing a
normalization that controls that scalar part.  Thus it settles the literal
questions, but it does not settle a strengthened, normalized version.

## 2. Exact live statement and stale scope

The live problem is
`manuscript/parts/part6/ch72_major_open_problems.tex`, lines 1874--1880:

> Let \((X,L)\to\mathbb D^*\) be a polarized projective degeneration.
> Let \(\phi\) be a continuous semipositive metric with logarithmic
> growth and assume that \(\phi^{\mathrm{NA}}\) is continuous.  Is
> \(\phi^{\mathrm{hyb}}\) continuous?

The following live assertions become stale if the counterexample is accepted:

* `manuscript/parts/part6/ch72_major_open_problems.tex`, lines 1872--1893:
  the problem and the sentence that it remains open;
* `manuscript/parts/part6/ch66_hybrid_spaces.tex`, lines 451--464:
  the prose calling general continuity the missing regularity and an open
  upgrade;
* `manuscript/parts/part6/ch66_hybrid_spaces.tex`, lines 1288--1293 and
  1328--1333: the recap/source note listing Favre's question as open;
* `output/open_problem_packets/reference_pack_unavailable_sources.txt`,
  line 30;
* `manuscript/editorial/part6_postexpansion_audit_20260824.md`, line 182;
* `manuscript/editorial/major_open_problem_program.md` near line 337;
* `manuscript/editorial/open_problem_atomic_inventory_20260824.md` near
  line 264;
* `manuscript/editorial/solver_dossiers_20260815/post2025_ytd_residuals.md`
  near line 363.

This dossier makes no edits to any of those files.

## 3. Authenticated primary-source audit

### Pille-Schneider

Local primary source:
`tmp/pdfs/ps23_hybrid.pdf`,
SHA-256
`55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7`.
The extracted text
`tmp/pdfs/ps23_hybrid.txt` has SHA-256
`dc7672bad7443db5a757a3fd3d34897c9ee89dbb6f749d33bd26e58e74391326`.
It is arXiv:2209.04879v2 and the published paper is
*J. Éc. polytech. Math.* 10 (2023), 601--658.

The dependencies used here are:

* Proposition 2.25, printed pages 20--21: the hybrid-circle
  correspondence sends a subharmonic function \(u\) to the psh hybrid
  function \(u(t)/\log_r|t|\), with central value determined by the
  Lelong number; the paragraph following it records the expected
  continuity statement.
* Definition 3.9, printed page 28: logarithmic growth is equivalent to
  extension as a psh metric on a normal model.
* Theorem 3.10, printed page 28: generic vertical Lelong numbers define
  the associated non-Archimedean psh metric.
* Theorem 3.13, printed page 29: the complex metric and its associated
  non-Archimedean metric glue to a canonical hybrid psh metric.
* Proposition 3.16 and Lemma 3.17, printed pages 30--31: continuity, if
  independently known, identifies the central restriction and yields a
  continuous hybrid psh metric.
* Question 3.18, printed page 31: the precise metric question refuted
  below.  The following paragraph asks for a normalized Bergman error
  uniform in \(t\).
* Theorem 4.11 and Theorem 5.1 are not used in the proof: the former
  assumes a continuous hybrid metric, and the latter concerns the
  special canonically polarized family.

### Favre

Local primary source:
`tmp/pdfs/Favre20_arxiv1611.08490_primary.pdf`,
SHA-256
`137ddb0245b4f09ff8b7a4a2880bd3846f146cd013f2ce9563d7f90f45ea1a5f`.
It is arXiv:1611.08490v2.

The dependencies used here are:

* Definition 4.1, printed pages 25--26: a uniform function admits
  model approximants with error
  \(\epsilon_n\log|t|^{-1}\).
* The remark immediately after Definition 4.1, printed page 26:
  uniformity implies that the normalized punctured function extends
  continuously to the hybrid space.
* Question 1, printed page 33: the three proposed intrinsic conditions
  are continuity near the punctured \(\overline X_r\), realization of
  the curvature by a positive current on a model neighborhood, and
  continuous extension of the generic-Lelong function.

Visual inspection of printed page 33 confirms that Favre's first bullet
uses the punctured space \(\overline X_r\), not the model
\(\overline{\mathcal X}_r\).  The construction below is nevertheless
stronger: its positive current extends across the central fibre.

A targeted public-source search through the audit date found the original
question and special positive cases, but no published proof, disproof, or
counterexample to the exact question.  This is only a search report; priority
and novelty remain unconfirmed.

## 4. The scalar construction

Put
\[
 s_j=2^j,\qquad
 \rho_j=\exp(-s_j),\qquad
 c_j=4^{-j},\qquad
 \epsilon_j=\exp(-s_j/c_j)=\exp(-8^j).
\]
For \(t\in\mathbb D\), define
\[
 q_j(t)=\frac{c_j}{2}
   \log\frac{|t-\rho_j|^2+\epsilon_j^2}{5},
 \qquad
 u(t)=\sum_{j\geq1}q_j(t).
\tag{1}
\]

### 4.1 Positivity, convergence, and the value at the origin

Each \(q_j\) is smooth and subharmonic.  The denominator \(5\) ensures
\(q_j\leq0\) on \(\mathbb D\).  On each compact subset of
\(\mathbb D^*\), the series and all of its derivatives converge normally:
for large \(j\), both \(\rho_j\) and \(\epsilon_j\) stay a fixed positive
distance from the compact set, the derivatives of the logarithm are
uniformly bounded, and \(\sum c_j<\infty\).  Thus
\(u\in C^\infty(\mathbb D^*)\) is subharmonic.

At zero,
\[
 q_j(0)
 =-c_js_j-\frac{c_j}{2}\log5
  +\frac{c_j}{2}\log\!\left(1+
             \frac{\epsilon_j^2}{\rho_j^2}\right)
 =-2^{-j}+O(4^{-j}).
\tag{2}
\]
Consequently \(u(0):=\sum_jq_j(0)>-\infty\).  Since the partial sums
decrease and are subharmonic on \(\mathbb D\), their nontrivial decreasing
limit is subharmonic on \(\mathbb D\).  This gives the psh extension used
below.

The circular means of \(u\) satisfy
\[
                  u(0)\leq M_u(r)\leq0 .
\]
Dividing by \(\log r\to-\infty\) gives
\[
                         \nu_0(u)=0.
\tag{3}
\]

### 4.2 Uniform logarithmic lower bound

Let
\[
 B_j=\{\,|t-\rho_j|<\rho_j/2\,\}.
\]
Since \(\rho_{j+1}=\rho_j^2\) and \(\rho_1<1/3\), the disks \(B_j\) are
pairwise disjoint.  If \(t\notin B_j\), then
\[
 q_j(t)\geq
 \frac{c_j}{2}\log\frac{\rho_j^2}{20}
 =-c_js_j-\frac{c_j}{2}\log20.
\tag{4}
\]
If \(t\) belongs to none of the \(B_j\), summation of (4) gives
\(u(t)\geq-C\).  If \(t\in B_m\), then
\[
 q_m(t)\geq
 \frac{c_m}{2}\log\frac{\epsilon_m^2}{5}
 =-s_m-\frac{c_m}{2}\log5,
\tag{5}
\]
while (4) applies to every \(j\ne m\).  Since
\(-\log|t|=s_m+O(1)\) on \(B_m\), (4)--(5), together with \(u\leq0\),
yield
\[
       -\log|t|^{-1}-C\leq u(t)\leq0
       \quad (0<|t|<1)
\tag{6}
\]
after enlarging \(C\).  Hence \(u\) has logarithmic growth in both the
source definition and the symmetric convention used in the live chapter.

### 4.3 Two incompatible hybrid limits

At the centre of the \(m\)-th well,
\[
 q_m(\rho_m)=-s_m-\frac{c_m}{2}\log5.
\]
Since \(\rho_m\notin B_j\) for \(j\ne m\), (4) gives
\[
                       u(\rho_m)=-s_m+O(1).
\tag{7}
\]
On the other hand, \(-\rho_m\) belongs to none of the \(B_j\), and hence
\[
                       -C\leq u(-\rho_m)\leq0.
\tag{8}
\]
For every fixed hybrid radius \(r_0\in(0,1)\), equations (7)--(8) imply
\[
\begin{aligned}
 \frac{\log r_0}{\log|\rho_m|}\,u(\rho_m)&\longrightarrow\log r_0,\\
 \frac{\log r_0}{\log|-\rho_m|}\,u(-\rho_m)&\longrightarrow0.
\end{aligned}
\tag{9}
\]
The two limits are distinct.

## 5. Lift to a genuine polarized degeneration

Let
\[
 \mathcal X=\mathbf P^1_{\mathbf C}\times\mathbb D,\qquad
 X=\mathcal X|_{\mathbb D^*},\qquad
 \mathcal L=\operatorname{pr}_1^*\mathcal O_{\mathbf P^1}(1),
\]
and let \(\phi_{\mathrm{FS}}\) be the product Fubini--Study model metric.
Set
\[
                    \phi=\phi_{\mathrm{FS}}+u\circ\pi .
\tag{10}
\]
Then \(\phi\) is smooth on \(X\), and
\[
 \mathrm d\mathrm d^c\phi
  =\operatorname{pr}_1^*\omega_{\mathrm{FS}}
    +\pi^*\mathrm d\mathrm d^c u\geq0.
\tag{11}
\]
It extends as a finite psh metric on \(\mathcal L\) over all of
\(\mathcal X\).  In particular it has logarithmic growth by
Pille-Schneider's Definition 3.9; equation (6) also checks the live
two-sided convention directly.

For a vertical prime divisor \(E\) on any model dominating
\(\mathcal X\), write at its generic point
\[
                     t=\zeta^{b_E}h,
\]
where \(\zeta=0\) defines \(E\) and \(h\) is a unit.  Pullback of a
one-variable subharmonic function multiplies its generic Lelong number by
\(b_E\).  Equation (3) therefore gives
\[
                     \nu_E(u\circ\pi)=b_E\nu_0(u)=0.
\tag{12}
\]
Pille-Schneider's Theorem 3.10 now identifies the associated
non-Archimedean metric with the product Fubini--Study model metric:
\[
                     \phi^{\mathrm{NA}}
                     =\phi_{\mathrm{FS}}^{\mathrm{NA}}.
\tag{13}
\]
This endpoint is continuous.

By Pille-Schneider's Theorem 3.13, (10) and (13) glue to the canonical
hybrid psh metric \(\phi^{\mathrm{hyb}}\).  Fix
\(p\in\mathbf P^1(\mathbf C)\), and let \(p_K\) be the corresponding
\(\mathbf C((t))\)-point.  Functoriality of the hybrid analytification of
the constant section shows that
\[
 (p,\rho_m)\longrightarrow p_K,\qquad
 (p,-\rho_m)\longrightarrow p_K.
\tag{14}
\]
The product Fubini--Study hybrid metric is continuous.  Its difference
from the metric in (10), on a complex fibre, is the normalized scalar
\[
             \lambda(t)u(t)
             =\frac{\log r_0}{\log|t|}\,u(t),
\tag{15}
\]
whereas its central non-Archimedean difference is zero by (13).
Equations (9), (14), and (15) give two different limits at the same
central point.  Hence \(\phi^{\mathrm{hyb}}\) is not continuous.

This verifies every hypothesis of the live problem and gives a negative
answer.

## 6. Favre's literal Question 1, checked separately

Take Favre's potential to be \(\varphi=u\circ\pi\) relative to the
product Fubini--Study metric, and put
\[
 T=\operatorname{pr}_1^*\omega_{\mathrm{FS}}
     +\pi^*\mathrm d\mathrm d^c u.
\]
Then:

1. \(\varphi\) is smooth, hence continuous, on a neighborhood of every
   punctured \(\overline X_r\);
2. \(T\) is a positive closed \((1,1)\)-current on the whole product
   model and restricts to
   \(\omega_{\mathrm{FS}}+\mathrm d\mathrm d^c\varphi\);
3. (12) gives \(g_T\equiv0\), which extends continuously to the
   non-Archimedean analytification.

If \(\varphi\) were uniform, the remark following Favre's Definition 4.1
would make the normalized punctured function extend continuously to the
hybrid space.  But the two sequences in (9) and (14) converge to the same
hybrid point and have distinct normalized limits.  Thus \(\varphi\) is
not uniform.  No equivalence with Pille-Schneider's question was used.

## 7. Boundary tests and scope restrictions

* **Relative dimension.**  The construction works with any fixed
  polarized projective variety in place of \(\mathbf P^1\).  It even
  works in relative dimension zero if points are admitted as polarized
  fibres.
* **Geometry of the degeneration.**  The total space and central fibre
  are smooth, the degeneration is trivial, semistable, and toroidal.
  Singular central fibres and monodromy play no role.
* **Fibrewise geometry.**  On each fibre the perturbation is a constant,
  so the fibrewise curvature remains exactly Fubini--Study and the
  fibrewise oscillation of the perturbation is zero.  An oscillation
  estimate alone cannot repair the literal statement unless it also
  fixes the base-scalar normalization.
* **Why divisorial data miss the defect.**  Generic vertical Lelong
  numbers record the asymptotic slope averaged at the origin.  The
  wells have summable masses and zero Lelong number, but depth comparable
  to \(|\log|t||\) on extremely small moving sets.
* **Radial scalar functions.**  A radial subharmonic scalar has a convex
  logarithmic profile; its normalized slope has a limit.  The present
  non-radial concentration is essential to this construction.
* **Locally bounded model extension.**  If the difference from a model
  metric is locally bounded near the central fibre, then multiplication
  by \(\lambda(t)=\log r_0/\log|t|\) sends that difference uniformly to
  zero.  Together with continuity on the punctured space, this gives
  continuity at the central fibre.  Our extension is finite everywhere
  but not locally bounded below.
* **No contradiction with known positive results.**  Uniform/model
  metrics have a common uniform approximation; the canonically
  polarized and abelian cases have additional estimates.  Theorem 3.13
  only asserts psh gluing, and Theorem 4.11 assumes continuity.

## 8. Honest repaired statements

A sufficient hypothesis is the existence, for every \(\varepsilon>0\),
of a continuous hybrid Fubini--Study or model metric
\(\Psi_\varepsilon\) such that, for all sufficiently small \(t\),
\[
 \sup_{X_t}
 \frac{|\phi_t-\psi_{\varepsilon,t}|}{\log_{r_0}|t|}
 \leq\varepsilon,
 \qquad
 \|\phi^{\mathrm{NA}}-\psi_\varepsilon^{\mathrm{NA}}\|_\infty
 \leq\varepsilon.
\tag{16}
\]
Then the glued metric is a uniform limit of continuous hybrid metrics
and is continuous.  This is essentially the uniformity missing from the
literal endpoint hypotheses.

A weaker positive subclass is obtained by assuming that
\(\phi-\phi_{\mathcal L}\) is locally bounded near the central fibre for
some continuous model metric \(\phi_{\mathcal L}\).  The exact remaining
research problem is therefore a normalized version excluding
uncontrolled base scalars and still weaker than (16).  Nothing in this
dossier proves such a normalized theorem.

## 9. Frozen local packet

The exact theorem and its source-aware proof are frozen locally as:

* `manuscript/editorial/rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_statement_exact_20260825.tex`;
* `manuscript/editorial/rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_source_aware_proof_exact_20260825.tex`;
* `manuscript/editorial/rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_manifest_20260825.md`.

The exact packet was submitted, with the user's explicit authorization, to
production Rethlas at `127.0.0.1:8107`, using `gpt-5.6-sol` at `xhigh`.
Run `20260825T030402Z_13e01361eeff`, proof item
`pi_e8a9764e8fb295f8ff4cefbb`, returned `final/correct`, with zero
critical errors, zero gaps, and no expanded-proof request.  The returned proof
digest is exactly
`c52e050011f568bc928e39f43cca784839c4820112505efbe55141eaf187e823`.
The controlling receipt is
`manuscript/editorial/rethlas_receipts_20260825/p18_favre_hybrid_extension_counterexample_production_receipt.md`.
