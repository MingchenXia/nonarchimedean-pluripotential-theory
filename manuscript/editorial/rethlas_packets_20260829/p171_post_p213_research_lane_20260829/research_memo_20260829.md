# Post-P21.3 research lane: ranking and P17.1 source-level attempt

Date: 29 August 2026

Status: **quarantined research memo; no live integration; no retirement**.

This memo assumes only for queue-order purposes that the one-dimensional
P21.3 packet passes its remaining production and editorial gates. It does
not itself alter the status of P21.3. It records a source-level attempt on
the next candidate and fails closed wherever a complete argument is not
available.

## Frozen inputs read

The ranking below was made from the complete live Chapter 72 and the complete
atomic inventory, not from their headings alone.

| input | SHA-256 |
|---|---|
| manuscript/parts/part6/ch72_major_open_problems.tex | 97684f7b96b4ca3bf9b8e6aa3a211b36f4401ee052b2d6e4336ceeac204dd712 |
| manuscript/editorial/open_problem_atomic_inventory_20260824.md | 76db1b15d470c380c21468cf4f8d6bab71f20ccad59b2eb147c39045462cfa2b |

The relevant live anchors are Chapter 72, lines 2098--2147, and the inventory,
lines 386--390. The other remaining T2 atoms were compared against their
full residual scopes, including every narrowing addendum.

## Ranking of the three most tractable remaining atoms

The ranking measures how bounded the next exact proof or counterexample
packet appears to be. It is not a probability that the answer is positive.

### 1. P17.1: Banach-base fibrewise mixed Monge--Ampère continuity

This is first because Pille--Schneider already reduces the problem to FS
metrics and DFS tests, and because one genuinely analytic part of the
finite-level bridge has now been verified. The remaining issue is algebraic
and metric: construct the correctly oriented relative Chow/resultant line and
identify its fibrewise norm without assuming the desired continuity.

The route is finite and modular. The new elementary reduction archived with
this memo also shows that arbitrary basepoint-free FS systems can be replaced,
by multilinearity, with systems defining closed immersions. That removes one
unnecessary generalization from the critical path, subject to exact-byte
verification of the reduction.

### 2. P07.1: first-stage collapse of the CLD psh hierarchy

Finite ambient-induced real-affine stars and the two nonambient interval
endpoints are already settled. The next natural test is the infinite-valence
star occurring in the trivially valued projective line. CLD's definitions are
explicit enough to make this a concrete order-theoretic target.

It ranks below P17.1 because the center of the infinite star couples all
branches: a neighborhood contains all but finitely many full branches, while
ordinary smooth functions have a finite-slope/harmonicity constraint there.
The existing finite-star proof does not pass to this topology by a formal
exhaustion. No complete proof or separating transfinite counterexample was
found in this pass.

### 3. P03.1: normal or analytically unibranch local-envelope classification

The verified nodal counterexample shows exactly why reducible branch jumps
break the unconditional statement. Normality or analytic unibranchness is
therefore a natural firewall, and the global unibranch envelope theorem gives
a plausible positive model.

It ranks below P07.1 because the desired result is local with a relative
boundary, whereas the available positive theorem is global. One still needs
either a local-to-global construction preserving the obstacle and the
upper-semicontinuous regularization, or a normal/unibranch counterexample.
The nodal construction does not survive normalization and supplies neither.

P06.1 and P06.2 rank below these three. Their residual scopes begin precisely
where altered local uniformization or proper full-rank moment factorization no
longer supplies a recognition theorem: non-quasi-smooth points of dimension at
least two for P06.1, and arbitrary continuous zero-current functions without a
moment factor for P06.2.

## Exact P17.1 target

The literal source is Pille--Schneider, Question 4.9. If \(A\) is an
integral Banach ring, \(X/A\) is flat and projective in the source's
\(n\)-dimensional setting, \(L_1,\ldots,L_n\) are semiample, and
\(\phi_i\in\operatorname{CPSH}(L_i)\), the question is whether
\[
 x\longmapsto
 \int_{X_{\mathcal H(x)}^{\mathrm{an}}}
 \psi_x\,
 \operatorname{MA}\bigl((\phi_1)_x,\ldots,(\phi_n)_x\bigr)
\]
is continuous on \(\mathcal M(A)\) for every
\(\psi\in C^0(X^{\mathrm{an}})\).

Nothing below adds reducedness, geometric reducedness, purity, Noetherianity,
or a value-group restriction. Any positive proof must retain the generic
lengths in the top-dimensional fundamental cycles of the fibres.

## Primary-source ledger

### Pille--Schneider

Frozen file used:

- Léonard Pille--Schneider, *Global pluripotential theory on hybrid
  spaces*, Journal de l'École polytechnique — Mathématiques 10 (2023),
  601--658, DOI 10.5802/jep.228;
- official PDF:
  https://jep.centre-mersenne.org/item/10.5802/jep.228.pdf;
- local audit copy: /private/tmp/PS23Hybrid.pdf;
- SHA-256:
  68d1bf470a78d4021e126ec1d491ad002cb64a1689d06beec3dd3fc9f9dee71e.

Exact usable anchors:

1. Definition 2.13 gives global tropical FS metrics.
2. Definition 2.15 gives DFS metrics and DFS functions.
3. Theorem 2.16 proves that \(\operatorname{DFS}(X)\) is dense in
   \(C^0(X^{\mathrm{an}})\).
4. Definition 4.8 defines the fibrewise mixed Monge--Ampère family.
5. Question 4.9 is the literal open question.
6. The paragraph immediately following Question 4.9 and Lemma 4.10 reduce
   it to DFS tests and FS metrics by density and a
   Chern--Levine--Nirenberg estimate.
7. Theorem 4.11 proves only the stated hybrid special case.

The source itself says that the general answer is unclear without further
assumptions on \(A\). Thus no result in that paper may be cited as solving
P17.1.

### Chen--Moriwaki

Frozen file used:

- Huayi Chen and Atsushi Moriwaki, *Arithmetic intersection theory over
  adelic curves*, arXiv 2103.15646v1, 29 March 2021;
- PDF: https://arxiv.org/pdf/2103.15646v1;
- local audit copy: /private/tmp/ChenMoriwaki2103.15646.pdf;
- SHA-256:
  89828d2fe257736d0a51d8152d47b29ba0da207b61f6e04137fd9f28f89d5b1f.

A later author-hosted 153-page revision was also frozen:

- PDF:
  https://webusers.imj-prg.fr/~huayi.chen/Recherche/Intersection_Adelic_Curves.pdf;
- local audit copy: /private/tmp/ChenMoriwakiIntersectionAccepted.pdf;
- SHA-256:
  4978bf5a6b0b09dbb43a273fe0eba1e2368ce60b9f78730e567f59d605be0b44.

Exact usable anchors in this frozen version:

1. Section 1.6 assumes closed immersions
   \(f_i:X\to\mathbf P(E_i)\).
2. Definition 1.6.3 extends the resultant from integral \(X\) to the
   top-dimensional fundamental cycle of an arbitrary projective scheme,
   with generic lengths as exponents.
3. Example 1.6.4 is the dimension-zero norm/resultant orientation check.
4. Definition 1.6.7 fixes the scalar by evaluation at a properly
   intersecting tuple; Remark 1.6.8 gives field base change.
5. Theorem 3.8.7 gives the local-height/resultant formula for a nontrivial
   complete valued field and closed immersions.
6. Proposition 3.9.3 gives the corresponding formula over a trivially
   valued field by scalar extension.

There is material version drift, but not a mathematical contradiction.
In arXiv 2103.15646v1, the broad closed-immersion local-height/resultant
formula is Theorem 3.8.7 and the trivial-valuation formula is Proposition
3.9.3. In that version, Proposition 3.9.7 is instead a special comparison
for a regular projective curve when either \(X=\mathbf P^1\) and
\(L=\mathcal O(1)\), or the generating normed vector space has dimension
two.

In the later author-hosted revision, a new reminder-on-norms section shifts
the numbering: the broad formula is Theorem 3.9.7 and the trivial-valuation
formula is Proposition 3.10.3. Thus the older editorial source map
manuscript/editorial/rethlas_packets_20260828/p171_resultant_deligne_bridge_source_map_20260828.md
is compatible with the author-hosted revision when it cites Theorem 3.9.7,
but it must freeze or state that edition. A citation to “3.9.7” without an
edition is ambiguous enough to point to a different proposition in arXiv
v1.

### D'Andrea--Krick--Sombra

Frozen file used:

- Carlos D'Andrea, Teresa Krick, and Martín Sombra, *Heights of varieties
  in multiprojective spaces and arithmetic Nullstellensätze*, arXiv
  1103.4561v2;
- PDF: https://arxiv.org/pdf/1103.4561v2;
- local audit copy: /private/tmp/DAndreaKrickSombra1103.4561.pdf;
- SHA-256:
  17b312a97917369a3435c693c5994f2ff4281a452868fc89049570653d466726.

Section 1.3 is the relevant cycle-resultant source. Lemma 2.32,
Definition 2.33, and equations (2.34)--(2.35) give the fixed-type
Mahler/Philippon coefficient bounds used in the already verified analytic
lemma. They do not construct a relative resultant line over a Banach base.

### Ducrot

Frozen file used:

- François Ducrot, *Structures du cube et fibrés d'intersection*,
  arXiv alg-geom/9712010v1;
- PDF: https://arxiv.org/pdf/alg-geom/9712010v1;
- local audit copy: /private/tmp/Ducrot9712010.pdf;
- SHA-256:
  8c4c32a1a29936235557040111c7bb4236fe30de2b0cca0655800ea9f10389d0.

The relevant scope is a projective flat family of relative dimension \(n\)
over a locally Noetherian base. Proposition 6.1.1 constructs the
multi-additive symmetric intersection line and records base change,
dimension-zero norm, and Cartier restriction. Corollary 6.1.2 iterates
restriction along a relative regular sequence. Lemma 6.3.1 computes the
resultant line, Lemmas 6.3.2--6.3.3 provide the depth/gluing mechanism,
Definition 6.3.4 defines the resultant section, Lemma 6.3.5 identifies its
incidence divisor only at fibre-local depth at most one, and Lemma 6.3.6
gives symmetry.

This is a powerful template. It is not by itself a theorem over an arbitrary
integral Banach ring, and it does not automatically identify every finite
basepoint-free subsystem with the fieldwise cycle resultant used by
Chen--Moriwaki.

## Prior P17.1 packets and their exact status

The first full candidate was rejected:

- rejection memo SHA-256:
  1ea5ec91c8f3b29ce644316351aa15bfbf57c6073af2f3317ddd213db3c97362;
- verifier verdict: wrong;
- decisive error: the resultant was put in the dual Deligne line.

The dimension-zero check fixes the orientation. The universal norm is a
section of the positive Deligne line tensored with the polynomial
coefficient line. If \(e'=ue\) is a new local frame of the positive line,
the scalar polynomial satisfies
\[
                              R_{e'}=u^{-1}R_e.
\]
This is exactly the transformation law required by an additive metric.
The opposite rule in candidate 1 invalidated all later metric patching.

One analytic input survived, was repaired, and passed independent
production verification:

- exact blueprint:
  manuscript/editorial/rethlas_packets_20260828/p171_weighted_philippon_gauss_continuity_blueprint_verified_20260828.md;
- SHA-256:
  58c2c4bbae0335b313e615655a014738bee0d9372ca648c4f111f063360c784b;
- production run:
  20260828T114547Z_2c38e89bc058;
- verdict:
  correct, with zero critical errors and zero gaps.

That result proves continuity of the line-valued weighted
Philippon--Gauss coefficient norm, including the Archimedean character
topology, powered absolute values, the boundary \(\rho\to0\), and the
correct frame law. It does not prove that the relevant fibrewise
Monge--Ampère integral equals that coefficient norm.

The staged relative-resultant candidate has hashes

- statement:
  beba5a7c1c1e938ab774aac5fbe0d44a294da9efa022b340169b55a161effc45;
- proof:
  cbb2391527ed48fde34cb95e005b21ae52961b1caa1b41b8a98736f14ffe9f9c.

It is confined to a locally Noetherian base, relatively ample finite locally
free quotient systems, and depth-at-most-one incidence. It has pre-production
audits but no production Rethlas verdict and cannot be used as a theorem.

## New finite-level reduction isolated in this pass

The two TeX files beside this memo give a complete elementary candidate
proof of the following reduction.

Fix one projective embedding
\(\iota:X\hookrightarrow\mathbf P^r_A\), let \(H=\iota^*\mathcal O(1)\),
and let \(\eta\) be its coordinate max metric. If
\[
                  \phi=\frac1m\max_j(\log|s_j|+a_j)
\]
is any tropical FS metric on a semiample line bundle \(L\), then the
products \(s_jt^\alpha\), \(|\alpha|=m\), define the Segre product of the
map given by the \(s_j\) with the \(m\)-th Veronese of \(\iota\). This is
a closed immersion and
\[
 \phi+\eta
 =\frac1m\max_{j,|\alpha|=m}
   \bigl(\log|s_jt^\alpha|+a_j\bigr),\qquad
 \phi=(\phi+\eta)-\eta.
\]
Multilinearity therefore expands every FS/DFS finite-level integral into a
finite signed sum in which every metric is induced by a closed immersion.

This observation removes the need to prove a relative resultant theorem for
arbitrary basepoint-free subsystems merely in order to solve P17.1. It does
**not** remove the need for a relative closed-immersion Chow form and its
metric comparison.

The statement and proof are quarantined and have not received an exact-byte
Rethlas verdict. They must not enter the live book before such a verdict.

## Sharp firewall against an overstrong intermediate statement

Let
\[
 X=\mathbf P^1\times\mathbf P^1,\qquad
 L_0=L_1=L_2=\operatorname{pr}_1^*\mathcal O_{\mathbf P^1}(1).
\]
In the product of the three coefficient projective lines, the three
universal sections have a common zero exactly on the small diagonal. That
locus has codimension two, not one. Moreover,
\[
             (L_jL_k\cdot[X])=0\qquad(j\ne k),
\]
so every resultant block degree is zero and the line-valued resultant is a
unit.

Thus the assertion “the resultant vanishes exactly when the universal
sections have any common zero” is false for general semiample systems.
Ducrot's depth-at-most-one statement, or the equivalent essential-cycle
condition, is load-bearing. This is a counterexample to an intermediate
lemma only; it is not a counterexample to P17.1. In this example the
relevant positive mixed measure has total mass zero and hence is zero.

## Attempted completion and exact point of failure

The most economical positive route now has the following form.

1. Use Pille--Schneider's DFS/FS density and CLN estimate to reduce to a
   DFS test and tropical FS metrics.
2. Use the closed-immersion reduction above and multilinearity.
3. For each resulting closed-immersion tuple, construct a positive relative
   Chow/resultant line and section over the algebraic base underlying \(A\).
4. Identify each field fibre with the Chen--Moriwaki fundamental-cycle
   resultant, with the dimension-zero orientation fixed as above.
5. Use Chen--Moriwaki's local-height formula and the verified weighted
   Philippon--Gauss lemma to obtain a continuous finite-level weight on
   \(\mathcal M(A)\).
6. Apply the fieldwise Deligne change-of-metric formula and then the uniform
   density/CLN argument.

Steps 1, 2 at the level of the displayed candidate proof, and the analytic
continuity part of Step 5 are available. A complete proof of Steps 3--5 in
the literal source scope is not available in the audited packets. No
counterexample satisfying flatness, global continuity of the metrics, and
psh positivity was found.

The exact unresolved dependencies are:

### D1. Relative closed-immersion Chow section over an arbitrary base

For a flat projective finitely presented \(X\to\operatorname{Spec}A\) and
closed immersions \(X\to\mathbf P(E_i)\) defined by finite free systems,
construct canonically the positive intersection line and a line-valued
mixed Chow section. Prove regularity, symmetry, the dimension-zero norm
orientation, and arbitrary base change.

Ducrot proves the locally Noetherian intersection-line/resultant package in
his stated setup. Passing to a finitely generated approximation of \(A\)
is plausible, but independence of the approximation and base-change
naturality of the section must be proved, not inferred from the
corresponding facts for the line alone.

### D2. Fibrewise fundamental-cycle identification

Prove that the fibre of the relative section in D1 is the
Chen--Moriwaki/D'Andrea--Krick--Sombra resultant of
\([X_x]_n\), with generic lengths, and fix its scalar functorially.
Nonessential components and zero block degrees must yield the canonical unit
rather than a false incidence divisor.

### D3. Exact metric comparison in the required fieldwise scope

Translate Chen--Moriwaki Theorem 3.8.7 and Proposition 3.9.3 in arXiv v1
(Theorem 3.9.7 and Proposition 3.10.3 in the author-hosted revision) from
their normalized properly intersecting sections to the unnormalized
line-valued relative section. Track:

- the positive-line frame sign;
- real diagonal weights;
- powered Archimedean absolute values;
- trivial valuations;
- nonreduced fundamental-cycle multiplicities;
- degree-zero/nonessential blocks;
- the exact harmonic correction in the Philippon norm.

The verified weighted Philippon--Gauss lemma proves continuity once this
identity is established; it does not establish the identity.

### D4. Line-power and finite-level normalization

Specify the canonical multi-additive identification between the resultant
line and the required Deligne/intersection line with no unspecified power
\(q_\ell\). Show that the normalization used after synchronized tensor
powers has the correct frame transformation and converges uniformly to the
tropical max metric. Every exponent and sign must pass the
relative-dimension-zero test.

Once D1--D4 are proved, the last passage is not an additional open
dependency: Pille--Schneider explicitly supplies the density/CLN reduction,
and flatness keeps the relevant intersection masses fibre-independent.

## Outcome

P17.1 remains open. This pass produced:

1. an exact three-item tractability ranking;
2. a corrected primary-source map, including the Chen--Moriwaki
   edition-dependent 3.9.7 warning;
3. a complete quarantined candidate proof reducing arbitrary finite-level
   FS/DFS data to closed-immersion systems;
4. a sharp \(\mathbf P^1\times\mathbf P^1\) firewall against an overstrong
   incidence claim;
5. the explicit four-dependency ledger D1--D4.

No affirmative answer to P17.1 and no counterexample to P17.1 is claimed.
No live manuscript, bibliography, inventory, provenance file, or verified
results ledger was edited.
