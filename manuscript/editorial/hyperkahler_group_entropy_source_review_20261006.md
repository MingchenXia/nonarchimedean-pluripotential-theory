# Positive entropy in hyper-Kähler families: exact-source audit

Recorded 6 October 2026. Baseline: `090df44d059d3aaff4753f4610338b84a3244fd3`.
This checkpoint changes no active TeX, bibliography, canonical problem status,
original-result verification tier or general Siu/envelope closure.

## Decision

The new preprint supplies a relevant **source-attested dense existence
statement** for positive-entropy birational maps in polarized hyper-Kähler
families. It does not supply a chosen relative automorphism, constant
dynamical degree, uniform eigenpotentials or convergence of invariant
measures. A later exposition can connect it to Chapter 66's K3 discussion
while preserving this distinction.

The complete proof of the dense existence statement is **not independently
certified here**. The main argument uses recent reflective-lattice and
common-group results, whose selected inputs have been read, but the
homogeneous-dynamics input requires the exact published edition and its
measure-theoretic dependencies. Several literal scope and notation issues
are recorded below. They do not establish a counterexample to the main
theorem. No replacement proof or independent research-result receipt is
claimed.

## Editions and actual reading

Read the complete selected text and actually displayed **91 physical pages
in 46 sheets** across nine PDFs. These are page counts of the acquired
layouts, not a claim to have read every cited publication in full.

| Source | Acquired layout | Physical pages actually read | Scope |
| --- | --- | --- | --- |
| F. A. Denisi, K. Oguiso, C. Onorati, F. Rizzo, S. Viktorova, *Algebraic entropy of birational automorphism groups in families of hyper-Kähler manifolds* | `2610.05173v1`, 8 pages; submitted 4 October 2026, 12:31:16 UTC | 1–8 | Entire v1, including references |
| E. Amerik, A. Soldatenkov, M. Verbitsky, *Reflective lattices and hyperkähler manifolds* | `2605.28593v1`, 14 actual pages; submitted 27 May 2026, 15:12:07 UTC; internal version 1.0, 26 May | 1–14 | Entire v1; arXiv's thirteen-page comment is not its actual PDF page count |
| F. A. Denisi, C. Onorati, F. Rizzo, S. Viktorova, *Birational automorphism groups in families of hyper-Kähler manifolds* | `2601.16090v1`, 20 pages; submitted 22 January 2026, 16:41:36 UTC | 1–20 | Entire v1 |
| K. Oguiso, *Automorphisms of hyperkähler manifolds in the view of topological entropy* | `math/0407476v5`, 13 pages; submitted 25 April 2005, 03:57:45 UTC | 1–10 | Theorem 2.1 and its complete displayed proof, with surrounding material; pages 11–13 unread |
| E. Markman, *A survey of Torelli and monodromy results for holomorphic-symplectic varieties* | `1101.4606v3`, 46 pages; submitted 18 December 2011, 16:54:24 UTC | 22–27 | Theorem 6.18, Lemmas 6.22–6.23 and surrounding cone/monodromy discussion; not the Springer chapter's pagination |
| D. Huybrechts, *Finiteness of polarized K3 surfaces and hyperkähler manifolds* | Publisher PDF, AHL 1 (2018), printed 227–246, DOI `10.5802/ahl.6`, 20 actual pages | 1–6, printed 227–232 | Introduction and Remark 1.1 lattice finiteness inputs; remaining pages unread |
| V. V. Nikulin, *Reflection groups in hyperbolic spaces and the denominator formula for Lorentzian Kac–Moody Lie algebras* | `alg-geom/9503003v6`, 30 actual pages; submitted 14 October 1995, 18:25:43 UTC | 1–8 | Definition 1.1.2, Theorem 1.1.3 and its displayed geometric argument; remaining pages unread |
| E. Amerik, M. Verbitsky, *Collections of parabolic orbits in homogeneous spaces, homogeneous dynamics and hyperkähler geometry* | Author-hosted version 0.9, 13 April 2016, 13 pages | 1–13 | Entire old author copy; distinct from the 2020 IMRN publication entitled *Collections of orbits of hyperplane type…* |
| K. Oguiso, *Picard numbers in a family of hyperkähler manifolds—A supplement to the article of R. Borcherds, L. Katzarkov, T. Pantev, N. I. Shepherd-Barron* | `math/0011258v1`, 12 pages; submitted 30 November 2000, 07:19:48 UTC | 1–6 | Main Theorem and its complete local period/Rouché proof; remaining pages unread; not a reading of the combined 2003 JAG article |

Huybrechts' acquired first page explicitly prints **227–246**, matching its
twenty physical pages. The publisher landing page returned different end-page
metadata; the controlling copy and Remark 1.1 locator are specified here
without declaring the layouts equivalent. Nikulin's published MathNet PDF
download returned HTTP 503; web-extracted published text was only a locator
aid, not actual page-image reading. The arXiv v6 copy is separately pinned.
Oguiso's 2003 article combines material associated with `math/0011258` and
`math/0104049`; looking up the latter's metadata does not constitute reading it.

PDF SHA-256 pins, in the table's order:

- `9b613baffa0f9f7177a27f8c1ead56a6974ca20a8b44786a6f941856bc672402`.
- `f23b625f033f7c04768cadbd2c691aeb723d30790d64ce066fe7fca974a87259`.
- `d74c8f5c32906f050b7614932621eed67b7cb0a7f405874662ba2542e253feb4`.
- `893f3d77372d157ae319fabf4f6c87a40e29befbb7acca7ccbd97db205c5d4a8`.
- `55d67f2588729b1aecdb6cf3d5d9eaaba50a336cbfbf918caf9ea58c2eec76a6`.
- `6e5476531202b7d67f92f35e5f5c75242bea9ad56d97266ecd4f9f5d805954a9`.
- `9cf58081ae4506be301b29bdb38746bfb09dc15c63b197566f77975154464e47`.
- `3efdbb138f8e778c7e6fcf72a03ed7044d69135d6cecd5f578213281bea33031`.
- `d5322c83ec69145836efd4e6b2474f33477de9f13094a7ddb9f092b13635d5a2`.

Acquisition URLs and bytes are embedded in the companion manifest. Historical
acquisition flags remain false: completed selected reading is recorded
separately, with every displayed image and corresponding text hash.

## What the new statement says

**HG01 — Entropy convention.** Definition in the introduction, physical 1:
`h(g)=log lambda_1(g)` is algebraic entropy **at H2 level**. A birational
hyper-Kähler map is an isomorphism in codimension one, making its H2 action
functorial under powers; the first dynamical degree is the spectral radius
on H^(1,1). This is not a definition of the full topological entropy in every
even dimension. For a regular K3 automorphism the familiar degree/entropy
interpretation applies.

**HG02 — Family hypotheses and quantifiers.** Theorem 1.1, physical 1,
assumes a non-isotrivial **polarized** hyper-Kähler family over a small
complex disk and `b2>=6`. It asserts Euclidean density of parameters t
for which **some** birational self-map of X_t has positive h. The map can
depend on t. Corollary 1.3, physical 2, extends the stated existence to
families of projective hyper-Kähler manifolds over an irreducible complex
analytic base; its local-disk reduction is on physical 6–7. Neither result
removes projectivity or asserts the analogous statement for arbitrary strict
Calabi–Yau manifolds. Remarks 1.2 and 1.4 discuss these limitations.
Remark 1.5 concerns a **Zariski-dense** generic orbit via a further external
result; it is not Euclidean orbit density or measure equidistribution, and
that external orbit theorem has not been audited here.

## Groups, chambers and lattice finiteness

**HG03 — Common subgroup, finite index and finite exceptions.** DORV
Theorem 1.1, physical 2, and its proof, physical 10–13, give a common
subgroup G0 for fibers outside a finite exceptional set F. The uniform
finite-index assertion concerns the very general birational group. It is not
a global relative automorphism. In the positive-entropy very-general case
of the new paper's proof, physical 6, passing from a given g to G0 requires
taking a positive power: a finite-index subgroup contains g^m for some m,
and `lambda_1(g^m)=lambda_1(g)^m>1`. The chosen element need not itself
belong to G0. The finite exceptional set is retained.

**HG04 — The actual cone stabilizer.** The new paper's preliminary
discussion, physical 3, identifies its birational monodromy with the full
moving-cone stabilizer inside O(Pic). Markman's precise statements are
Theorem 6.18 and Lemma 6.23, selected physical 22–25: write
`rho:Mon_Hdg -> O(NS)` and `Gamma=im(rho)`. Gamma has finite index
in `O^+(NS)`; `ker(rho)` lies in the birational monodromy subgroup; and
`Gamma_Bir=Mon_Bir/ker(rho)` is the relevant image stabilizing the
fundamental exceptional chamber. The semidirect product is
`Gamma=W_Exc semidirect Gamma_Bir`. Full ambient O(NS) stabilizer
equality must not be substituted for this image statement. Finite kernels
and finite indices must be retained when passing between geometric groups,
their H2 representations and their Picard representations. This is also
needed for ASV's informal isomorphism wording on physical 5.

**HG05 — Fixed deformation type, scale and positive Picard direction.**
The new paper's Proposition 2.5, physical 4, uses a fixed deformation type
through a uniform negative square bound; DORV Proposition 2.6, physical 7,
likewise uses that bound in its proof. These are not uniform finiteness
claims over all unknown deformation types. Nikulin's Theorem 1.1.3,
selected physical 5–7, gives parabolic reflective lattice finiteness **up
to similarity and isomorphism** for fixed rank at least three. A negative
root bound is a separate input for bounding the possible scales.
Huybrechts' Remark 1.1, printed 231, supplies the stated embedding/vector
orbit finiteness inputs, themselves citing lattice theory.

The full Picard lattice contains the positive polarization h; it cannot
be treated as a sublattice of h-perp, as in the new paper's physical 4
wording. Its negative definite part `Pic intersect h-perp` can be.
Similarly, ASV physical 11's identification of a very general NS with its
negative lattice M_i omits the h direction. The full NS is the appropriate
primitive saturation of `Zh direct-sum M_i` in Lambda. ASV physical 4
prints signature `(2,b2-k)` for L-perp when L has signature `(1,k)`;
the dimension-consistent signature is `(2,b2-3-k)`.

## Period divisors and dense intersection

**HG06 — Dimension comparison and local analytic avoidance.** In the
new paper's proof on physical 6, the phrase excluding Z_j of dimension
smaller than `dim(Z_j)` is tautological. The immediately following
definition of J and ASV's minimal-stratum argument indicate the intended
comparison with `dim(Z_i)`. When restricting to a nonconstant period disk,
noncontainment in a finite union of analytic strata must hold on every
open subdisk, by analytic continuation; each proper preimage is discrete.
Mere ambient density or one point outside a bad union is not sufficient.
This is a scoped reading of the stated strategy, not an independently
certified replacement proof.

**HG07 — Strong density and critical parameters.** ASV Definition 2.8
and Theorem 2.10, physical 9–10, require dense intersection with every
nonconstant holomorphic disk, a stronger property than ambient density.
Theorem 2.10 explicitly obtains a needed orbit-density step from the proof
of the external Amerik–Verbitsky theorem, rather than simply restating its
printed conclusion. Proposition 2.11, physical 11, uses `f'(0)!=0`
without separately stating an unramified parametrization. A nonconstant
map can have `f'(0)=0`, for example z squared. One can restrict the
local transversality strategy to noncritical points on each open subdisk;
the printed assertion at an arbitrary center needs that explanation.
Lemma 2.12's Rouché argument retains a nonidentically-zero restricted
defining function. Oguiso's earlier Main Theorem, selected physical 2–5,
has a full local period/Rouché argument for dense countable Picard jumps;
it does not by itself give the new prescribed lattice-divisor collection.

**HG08 — Integrality versus an isotropic pairing-one partner.** The
construction in ASV section 2.3 **immediately preceding** Proposition 2.6,
physical 8, enlarges a lattice by e/m and then infers an isotropic f with
`(e/m,f)=1`. Mere integrality and divisibility one do not imply this: in
the odd unimodular lattice with Gram matrix `[[0,1],[1,1]]`, e has square
zero, but every vector pairing one with e has square `2k+1`. Evenness or
another application-specific argument is needed. This is a diagnostic of
the general lattice inference, not a counterexample to the actual
Beauville–Bogomolov application. The frozen diagnostic v1 named this
location as part of the proof of Proposition 2.6; v2 corrects the locator
without altering the algebraic check.

**HG09 — The new construction avoids that parity demand.** Proposition
2.9, physical 4–5 of the new paper, takes an arbitrary f pairing one with
e/m, with square b, and uses
`u_a=(1+2dab)e/m-4da f`. Its square is exactly `-8da`, and its two
coefficients are coprime. No isotropic f is required. The subsequent
saturation-index and small-negative-square avoidance use separate lattice
inputs and the fixed deformation bound. The elementary calculation is
checked symbolically and on 2100 integer triples; those checks certify
neither the global embeddings nor strong density of the resulting divisors.

**HG10 — The example's exceptional parameters.** Example 1.6, physical
2, says all members of the cited fourfold family have positive-entropy
birational maps. DORV Example 1.4(1), physical 3, explicitly restricts its
infinite-group conclusion to the complement of a finite F. The generic
rank-two infinite group and common-group power argument give positivity
on the restricted family. The cited density statement and rank-two remark
alone do not remove F. Interpret the family as already restricted, or
supply a separate argument for those parameters before asserting the
unrestricted all-members version. No actual exceptional fiber counterexample
has been produced here.

## Literal scope checks in the dependencies

**HG11 — Isotropic polarization surrogate in a displayed proof.** DORV
Lemma 2.1, physical 5, allows a primitive ell without a positive-square
hypothesis. Its proof forms `b=ell^2 a-(ell,a)ell` and equates the
orthogonal complements of the spans of `(ell,a)` and `(ell,b)`. This
equality needs `ell^2!=0`: in U take ell=e, a=f with `(e,f)=1`.
Then b=-e, and the two orthogonal complements differ. The actual polarized
application has `ell^2>0`; this check neither refutes the lemma nor that
application. Cohomology in a general family forms a locally constant
local system; the disk marking supplies the constant system used later.

**HG12 — Moving-cone component.** DORV Lemma 2.7, physical 7, must
also require membership in the positive-cone component containing ample
classes. On a Picard-rank-one projective K3 there are no prime exceptional
divisors, so h=-H for an ample H has positive square and satisfies the
printed exceptional inequalities vacuously, while lying in the other
component. The polarized proof uses the intended component.

**HG13 — Discriminant action and local Hilbert argument.** DORV Lemma
3.2, physical 12, writes an action map to `Hom(D,D)` and uses its kernel
as the subgroup acting trivially. The correct composition group is
`Aut(D)`, with identity action as its neutral element. It is finite, as
needed for the index argument. In the finite-exception proof on physical
13, an infinite set of points on an unrestricted noncompact disk need
not accumulate inside it. A relatively compact smaller disk, proper
relative Hilbert schemes and local finiteness of their components are
retained when using the bounded-degree argument. The externally cited
effectivity, Riemann–Roch, prime-exceptional bounds and finite-generation
inputs have not all been independently read here; the whole common-group
proof is not declared closed.

**HG14 — Rank-two polarity.** DORV physical 17 says that Bir is finite
when a rank-two lattice contains neither an isotropic vector nor a prime
exceptional class. Its following construction and conclusion use the
opposite polarity, namely an infinite group. Do not copy that isolated
sentence as a criterion. The new paper's rank-two zero-entropy obstruction
can instead be traced to Oguiso Theorem 2.1's infinite-group hypothesis and
rank bound, with the finite representation kernel retained.

**HG15 — Infinite versus arbitrary zero-entropy groups.** Oguiso
Theorem 2.1, selected physical 4–8, assumes an **infinite** subgroup of
isometries of a hyperbolic lattice, all of spectral radius one. It gives a
fixed primitive isotropic direction and a finite-index free abelian
subgroup of rank at most r-2. The complete displayed proof was read.
The earlier Theorem 1.3, physical 2, states a rho-2 bound without that
infinite qualifier; the trivial group on a Picard-rank-one projective K3
has rank zero, exceeding -1. This literal scope problem does not affect
the infinite-group Theorem 2.1 used by the new paper.

**HG16 — The old homogeneous-dynamics copy is not the published proof.**
The acquired 2016 author copy calls the stabilizer of a negative,
nonisotropic vector a maximal parabolic subgroup, physical 2, 4–6 and 11.
Such an orthogonal stabilizer is reductive, of type SO(p,q-1); it is not
a parabolic subgroup in the Borel-containing sense the same copy defines
on physical 4. This copy cannot silently discharge the 2020 published
theorem's hypotheses. Its argument also cites measure classification and
non-divergence results that have not been read here. The changed published
title, *orbits of hyperplane type*, makes edition control material rather
than cosmetic. The published PDF lookup was inaccessible; its proof
remains an external gate. This diagnostic is restricted to the actual
2016 copy and is not an assertion that the later publication or the new
density theorem is false.

**HG17 — Picard-jump edition control.** The selected `math/0011258v1`
Main Theorem and local proof are an exact source for the earlier dense
Picard-jump mechanism. They are not byte- or locator-equivalent to
*Local families of K3 surfaces and applications*, JAG 12(3), 405–433
(2003). Its publication metadata was checked, but the combined published
proof was not read. The 2016 author PDF and either old Oguiso
preprint must not be cited as though their published layouts were inspected.

## Connection to the book and unresolved work

**HG18 — Dense existence does not select hybrid data.** Chapter 66's
K3 hybrid route uses one specified relative automorphism, compatible
eigenclasses and positive mass normalization, family-uniform potential
tails and a justified mixed-curvature continuity input. The new theorem's
`for dense t, there exists g_t` does not give any of these compatibility
data. A map on each of a dense set of fibers is not a morphism of the
relative space, and its dynamical degree can vary. In higher dimensions
the existence theorem is birational, whereas the K3 discussion starts
with regular automorphisms. No invariant-measure convergence or canonical
open-problem closure follows from the density statement alone.

The next admissible book change is a short attributed account of the
source-attested statement and this interface, with the exact-v1 boundaries
linked in Appendix L. An unconditional reconstruction of its period-density
proof awaits the controlling published homogeneous-dynamics source and
remaining dependencies. No new canonical problem, priority or verification
tier is introduced.

## Preservation and validation

The companion manifest embeds all acquisitions, frozen reading manifests
and six literal diagnostics, and pins every one of the 5130 baseline
tracked files. The 5128 files other than README and the continuation
programme remain byte-identical. All 425 active source-closure entries, both bibliographies,
the 108 protected inputs, generated book/index files, 90 prior frozen
manifests and 157 frozen exports remain byte-identical. The current book
remains the validated **4438-page** Hessian-comparison build; this
source-only checkpoint does not compile a new book. The native catalogue
source, PDF and open editor are unchanged. General BJ22 Theorem 6.21
Siu/envelope closure remains conditional, and no theorem counterexample
or new original-result receipt is claimed.
