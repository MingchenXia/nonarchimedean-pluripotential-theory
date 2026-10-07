# Conifold contractions: non-closed mass, local Kähler estimates and metric completion

Date: 7 October 2026. Baseline `2747f02872cc19954d627f974a3070c81695588a`;
publication branch `work`; `main` at baseline is
`00957114db21b627e97369563032ceda9cea09c7`.

The new source is Riley Guyett and Ryan Mc Gowan, *Monge–Ampère
degenerations and conifold contractions in Fujiki class C*, exact
arXiv:2610.00942v1, submitted 1 October 2026, 02:19:41 UTC.
All 28 actual pages were read as full selected text with matching images
in fourteen sheets. Five exact dependency files contribute seventy
fresh page pairs in thirty-six sheets and fifteen previously read
Guedj–Lu v1 page pairs in eight reused sheets. The cumulative audit has
113 distinct exact-source/page pairs in 58 sheets; 98 pairs in 50 sheets
are fresh. Two repeated main-paper sheets add no distinct pages.

Twenty-four scoped records and twelve exact elementary checks keep
general Hermitian subsequences, closed-background full-family convergence
and the nodal threefold metric theorem separate. No main-theorem
counterexample, complete external proof-chain certificate, original
result, independent model call, production receipt or canonical problem
solution is claimed. A mistaken initial torsion-formula reading is
explicitly corrected below before any book integration.

## Exact primary files and actual reading

New files are cached under
`source_material/Guyett_McGowan_conifold_sources_20261007/`.
The GL3 v1 file is reused from
`source_material/Hermitian_regularity_dependencies_20261006/`.

| Exact source | Actual returned layout and pages read | PDF SHA-256 |
| --- | --- | --- |
| Guyett–Mc Gowan 2610.00942v1 | 28 pages; all 1–28 | `91483d2ab62b8678302732889f9a8b18af02352073dc94b6582718d7e9ca532a` |
| Junsheng Zhang, Crelle 826 (2025), 271–302, DOI 10.1515/crelle-2025-0044 | 32 pages; actual 1–4, 19–24, ten pages | `fea1f755c8d02f7ec6c19837fefee42281dfc23ba128c88b7e32044212828027` |
| Boucksom–Guedj–Lu, published online 16 June 2025, DOI 10.1007/s42543-025-00105-2 | 43 pages; actual 1–5, 13–18, 35–41, eighteen pages | `a0d2ae63b9c412646e8c9785b3e3fa215a66e96e2de810b819f4a36ae25e688a` |
| Guedj–Lu, Algebraic Geometry 9(6) (2022), 688–713, DOI 10.14231/AG-2022-021 | 26 pages; actual 1–4, 10–17, twelve pages | `fca21ff19b3a6c1f384b73333a8367ff1e53111d3db669365ba27f1e14e963fa` |
| Jian Song, 1201.4358v1, 20 January 2012, 18:22:06 UTC | 21 pages; all 1–21 | `910f047de56a0a415737845200c09f9e07cfd1f2939f8ca230c7eb8fcaaee1f8` |
| Guedj–Lu, 2107.01938v1, 5 July 2021, 11:12:56 UTC | 34 pages; fresh 4–7, 30–34; reused 1–3, 8–13, 17–18, 26–29; cumulative 24 pages | `bd6b9594f5c32a9bc984b7b7f462f9c30492d928bd44330c64030a94c7f70f93` |

Zhang actual page 1 is printed 271; GL2 actual page 1 is printed 688.
Only the main paper and Song's exact v1 are fully read. The other four
files are partial selections. BGL's earlier arXiv reading is not counted
as a reading of the 2025 published edition. GL3's fifteen reused pages
are not counted again as fresh. The Song 2015 publisher endpoint returned
a non-PDF cookie page; GL3's 2023 publisher endpoint returned HTTP 405.
Neither journal edition is declared read. The initial incorrect GL2 URL
and its corrected successful publisher URL remain separately recorded.

The main-reading record has SHA-256
`62fe81edef0047a2efa6f6768a9d428f0b519d6871c247caf0e9702d0984c5ad`;
the dependency-reading record has SHA-256
`b843a1d4bc626d878a6676cfdb28b8ff470637c59da0b90c3a7dc948781ce00b`.
The prior exact GL3 selected-reading record remains byte-identical with
SHA-256 `51d2995b1fb6cd0e79f929a2d73f08b770b706457667b60965cc372edd12c803`.

## Reading correction

The frozen main sheet-six note initially called the first actual-page-11
absolute-value estimate too strong. Redisplaying the complete actual
9–12 images shows **absolute values on both sides** of the controlling
inequality. At the maximum point the cross term has form `B−2Q`, where
`Q = sum_i λ_i^{-1}|sum_j T_ijj|² ≥ 0`. Thus
`|B−2Q| ≤ |B|+2Q ≤ |B|+CR`; the next Young inequality also bounds `|B|`.
There is no potentially negative right-hand side. The initial reading
is withdrawn as a final assessment; this is our reading correction,
not a defect or repair of the source's torsion argument.

The immutable addendum has SHA-256
`d1fa5647814c10546a629762f0942713cf64f3fae79987f5e32a5647bf52fdb0`.
It retains the initial note and pins both repeated images. Those repeats
add zero source/page pairs. Subsequent exposition must use this corrected
assessment, not the earlier note or a text extraction that drops bars.

## Scoped records

**GS01 — Version and provenance.** The main theorem locators belong to
the exact October v1. Zhang, BGL and GL2 use the acquired published
editions. Song and GL3 use only their exact arXiv versions. Acquisitions,
actual PDF counts, extraction hashes and actual selected readings are
different records; a search result or PDF metadata does not count as
reading its proof. Failed publisher requests remain visible.

**GS02 — Global geometry.** Main actual 1–6 assumes a normal irreducible
projective Q-Gorenstein variety Y with torsion canonical class, a smooth
small crepant resolution π:X→Y, and exceptional locus E. X belongs to
Fujiki class C but need not be Kähler. The smooth positive volume Ω on X
has total mass one and vanishing Chern–Ricci form. The resolution here
is a fixed complex space; shrinking a class is not a degeneration of
complex structures over a punctured disc.

**GS03 — Two background regimes.** Main Theorem 1.1 permits a smooth
Hermitian form ωY, whose pullback θ is semipositive and positive off E.
The regularizations θ+εη use an arbitrary Hermitian η. Metrics solving
`(θ+εη+i∂∂bar φε)^n=cεΩ`, with supremum-zero potentials, are
Chern–Ricci-flat; non-closedness prevents inferring Riemannian
Ricci-flatness. The GH theorem later imposes closed Kähler ωY and a
locally Kähler η near E. These are additional hypotheses.

**GS04 — Smooth existence and normalization.** The positive-ε equations
use Tosatti–Weinkove's smooth Hermitian theorem. Its complete original
proof is not acquired/read here. The right-hand side needs an unknown
positive normalizing scalar in the non-closed setting. It cannot
generally be replaced by `∫(θ+εη)^n`; the torus diagnostic GC01 shows
explicit smooth-potential mass variation.

**GS05 — Exact mass bounds.** GL2 Proposition 3.2, actual 13/printed 700,
gives monotonicity of lower mass and mixed upper mass under ordered
semipositive backgrounds. Its lower estimate uses an envelope contact
argument. Corollary 3.8, actual 17/printed 704, gives finite upper and
positive lower mass for Hermitian forms on class-C manifolds. The
degenerate θ is separately compared with `aπ*κY`, a closed semipositive
big form, to obtain `v−(θ)≥a^n∫(π*κY)^n>0`. Positive `∫θ^n`
alone would not be sufficient for an arbitrary non-closed background;
GL2 Example 3.5 is an explicit collapsing semipositive example.

**GS06 — Barrier input.** Main actual 5–6 compares θ to a closed nef
big pullback and imports Collins–Tosatti's identification of its null
locus with E. This supplies an analytic-singularity barrier ρ, smooth
off E, with `θ+i∂∂barρ≥δη`. Collins–Tosatti, its general null-locus
proof and the regularization/barrier construction remain external
inputs. The argument is not licensed by a bare Fujiki assumption alone.

**GS07 — Uniform bounded potentials.** Main actual 7–8 uses GL3
Theorem A, exact v1 actual 2, with `m>n`, the normalized psh Lm bound
`Am(Ω)`, positive `v−` and an upper bound on `cε/v−(θ+εη)`.
Normalized potentials for all ε lie in one reference psh family,
allowing uniform Skoda/Lm control. Supremum normalization and positive
lower mass must remain in the statement. The selected GL3 proof pages
and inherited earlier notes do not certify all external integrability
inputs or the unread 2023 publisher layout.

**GS08 — Torsion-sensitive second order estimate.** Main actual 8–12
uses lowered coordinate torsion components controlled on a finite
cover, a singular barrier and `H=log S−γ(u)`, with
`u=φε−ρ+C+2>1`, `γ=Au+log u`. These are not an intrinsic torsion norm
bound for the degenerating metric. Chern–Ricci vanishing, background
commutator bounds, Guan–Li coordinates and weighted Young inequalities
give the trace estimate. The absolute-value step is valid under the
corrected reading above; no torsion counterexample is recorded.

**GS09 — Trace contradiction and regularity.** Main actual 11–12 has
`γ'=A+1/u` and `−γ''=1/u²`. If maximum H diverges then S/u diverges;
the differential inequality bounds R, whereas fixed positive determinant
and `S≤nDR^{n−1}` bound S, a contradiction. On compact subsets off E,
both upper/lower ellipticity follow. Evans–Krylov–Trudinger and Schauder
are imported, not fully audited here. GL3 actual 30 supplies the
continuation of its own corresponding two-case trace estimate.

**GS10 — Scalar limit independent of η.** Main actual 13 uses a
maximum comparison for two ε values to show cε increases with ε,
and compact pointwise equivalence of two Hermitian perturbations to
give `c^(1)_(ε/M)≤c^(2)_ε≤c^(1)_(Mε)`. The positive decreasing-to-zero
limit c0 is independent of η. This scalar uniqueness does not imply
uniqueness of the limiting potential for a non-closed θ.

**GS11 — What compactness proves.** Main actual 12–14 extracts bounded
normalized potentials in L1 and C∞ locally off E. The general
non-closed assertion is subsequential. Smooth off-E equations extend
globally as non-pluripolar measure identities because E is analytic and
both the non-pluripolar product and Ω assign it zero mass. BGL Theorem
2.2, actual 16–17, supplies the relevant product under bounded mass;
ordinary arbitrary-L1 continuity of MA is not asserted.

**GS12 — Closed-background upgrade.** If ωY is Kähler, θ is closed,
Stokes fixes `c0=∫Xθ^n`. Bounded potentials descend through connected
compact fibers to normal Y using local Kähler potentials. The density
of ΩY=π*Ω has the required klt integrability, and EGZ uniqueness gives
the full-family limit. The complete EGZ proof and descent theorem
remain external inputs. Main actual 2's Corollary 1.1 literally writes
Ω on X in an equation on Y; actual 14 correctly uses ΩY. This is an
ambient-volume notation qualification, not a theorem counterexample.

**GS13 — General closed big approximation.** Main Theorem 3.1, actual
14–15, abstracts the convergence when θ is closed semipositive big,
an analytic barrier is given, and the required upper mass is finite.
An arbitrary smooth positive Ω adds a bounded Ricci contribution to
the trace calculation; `SR≥n²` controls its inverse-S error. No
unconditional statement for every big non-closed background or general
smooth ample-locus solution is substituted.

**GS14 — Threefold nodal model.** Main actual 15–17 requires dimension
three and ordinary double points with small-resolution neighborhood
`O_P1(−1)⊕O_P1(−1)`. A cutoff construction makes η Kähler on a
neighborhood of E, without making it globally Kähler. In the GH
regime θ is also closed, so local approximating metrics are genuinely
Ricci-flat Kähler. This is where the Song Bochner/slicing inputs apply.

**GS15 — Rough bound and its limit.** Main actual 16–18 uses the flat
four-coordinate contraction map to get a Chern–Lu lower metric bound.
The local determinant comparison gives
`C^{-1}ωE≤ωtildeε≤Ce^{-ρ}ωE`. GC03 checks the reference determinant
at `z=0,ξ=(r,0)`. The rough upper bound has logarithmically divergent
radial length; it does not itself prove completion or GH convergence.

**GS16 — Exceptional curve diameter.** Main actual 18–19 bounds
`ωtildeε|C≤C0ωFS` via a wedge ratio and has
`Area(C)=ε∫Cη`. Lemma 4.1 proves the conformal-sphere diameter estimate
`diam(C)≤Cε^{1/3}` by a Fubini strip of width A^{1/3}, horizontal
Cauchy–Schwarz and the pointwise vertical bound, followed by a finite
coordinate chain. Song v1 Proposition 4.3, actual 17, cites an external
lemma for this step; the new source writes that elementary argument.

**GS17 — Partial trace, not a full inverse.** Main actual 19–20 and
Song v1 Proposition 4.1, actual 10–13, use the two-dimensional leaf
trace relative to `τ=i∂∂bar e^{ρ1}` on a finite-chart ruling. τ is
degenerate as an ambient threefold form. Leaf-preserving coordinates
and a Schur complement leave its leaf matrix constant; Ricci-flat
Kähler symmetry plus weighted Cauchy give `ΔlogH≥0`. Singular
maximum-principle/collar bounds yield `H≤Ce^{−ρ1}`. The infinity
ruling needs another chart or a unitary rotation.

**GS18 — Vector and chart dependence.** The auxiliary
`V1=ξ1∂ξ1` transforms to
`ν1∂ν1+ν2∂ν2−w∂w`, so is not tangent to a general Lw.
At w=0 it equals the fiber radial field V. Bochner plus the partial
trace controls `|V1|²H`; a compact U(2) change of fiber coordinates
allows w=0 at the chosen point with uniform constants. GC08/GC09
check the leaf shear and vector transformation; no general-leaf
tangency is inferred.

**GS19 — Intrinsic source no-neck.** Main Proposition 4.2, actual
20–21, obtains `|W|²≤Ce^{−ρ/2}` with `W=e^{−ρ/2}V`.
For `R=e^{ρ/2}` the length is bounded by
`C∫_0^δR^{−1/2}dR≤Cδ^{1/2}`. Two radial paths and a path on C
remain inside Uδ, giving the **intrinsic** diameter bound
`Cδ^{1/2}+Cε^{1/3}`. The δ and ε quantifiers are separate;
GC04 shows why the stronger radial estimate is essential.

**GS20 — Exact Zhang theorem.** Main Proposition 4.3 imports Zhang's
published Theorem 1.4, actual 3/printed 273. It requires an isolated
log-terminal algebraic germ, K-polystable cone C equal to K-semistable
cone W as Fano cones, a smooth link, bounded KE potential and
non-positive Ricci curvature. The cone-germ remark gives the assumptions
and a biholomorphic identification for a germ itself isomorphic to a
CY cone. The conifold cone has potential proportional
`(sum|zi|²)^{2/3}` and smooth link S²×S³. Zhang's separate Theorem
1.1 requires a quadratic curvature bound in the GH-limit setting;
smooth link alone is insufficient, as Corollary 1.3 illustrates.

**GS21 — Target no-neck and completion.** Main actual 21–23 transfers
the conical metric equivalence to punctured target neighborhoods.
Paths down to a radius s, across the compact connected link and back
give limiting cone distance at most r1+r2. This bounds the **extrinsic**
diameter measured by the ambient regular-locus distance. Total
boundedness adds one completion point per node; regular-core estimates
separate nodes and identify the completion topologically with Y.
Zhang Section 7, actual 19–24, uses earlier construction, weighted
invertibility and external compactness/algebraic tangent-cone results;
those full chains are not certified by this selection. Its positive-Ricci
discussion is a proposed program, not an established extension.

**GS22 — Two-sided distance comparison.** Main Proposition 5.1,
actual 23–26, assumes a compact completion homeomorphic to Y,
smooth metric convergence on a fixed regular core, small target
extrinsic diameters and small source intrinsic diameters. A graph
correspondence for π cuts first-entry/last-exit excursions into finitely
many singular neighborhoods and compares retained core lengths. The
bounded number of excursions controls distortion. The curve collapse
alone does not supply the target input; regular-locus smooth convergence
alone does not supply either diameter input. Closed-background
uniqueness then gives GH convergence of the full family.

**GS23 — Literal presentation and historical boundaries.** Main Figure
1, actual 25, has labels Y on the left and X on the right with inverse
arrow, while the caption reverses those sides. This does not affect
the graph proof. Song's exact v1 has reversed introductory class labels
although `ωt=θ+tω0` and the exceptional area formula control the
intended contraction. Its ansatz U0 interval, rank-three typo in a
rank-two flop paragraph, extra outer derivative in the displayed ODE,
first logarithmic-gradient symbol and radial endpoint have their
separate auxiliary scopes. GC10/GC11 check the ODE and endpoint
formula issues. No assertion about the unread 2015 edition follows.
Song's historical Conjecture 5.1 includes a uniform curvature rate and
rescaled limit; Zhang's germ asymptotic does not establish either
approximation-family claim here. Their present open status has not
been exhaustively audited, so they are not assigned new open-problem
atoms. GL2's literal arbitrary-proper-map Lemma 3.6 is used here only
for degree-one modifications, where the mass change of variables
applies; arbitrary proper maps are not imported.

**GS24 — Integration boundary.** A short attributed Chapter 66 account
can connect bounded MA potentials to metric geometry, while keeping
ε on a fixed resolution distinct from the hybrid punctured-disc
parameter t. It may explain the two diameter inputs and exact nodal
threefold regime. It cannot prove a new hybrid metric limit, smoothability
of every small resolution, non-closed potential uniqueness, a general
Hermitian GH theorem, a family curvature bound, or general BJ22
homogeneous Siu/envelope closure. Canonical Chapter 72 statuses and
the native open-problem catalogue remain unchanged.

## Exact elementary checks and preservation

GC01–GC12 check non-closed mass variation, positive trace algebra,
conifold determinant ratios, radial integrability, the A^{1/3} balance,
barrier derivatives/Young signs, the correctly barred torsion triangle
estimate, the leaf Schur complement, vector/chart dependence, the
Song ansatz ODE, its radial endpoint and punctured-cone paths.
All twelve checks pass. Their immutable record has SHA-256
`377614b1933d26a83cb8677039ef2d6f47dde1ce77a7845299f2ccdcb4b166a3`.
They are formula diagnostics, not certification of any main theorem.

This source-only checkpoint preserves all 425 active TeX inputs,
108 protected inputs, both bibliographies, the generated 4,458-page
book and index, 96 prior frozen manifests and 166 prior exports.
The native catalogue source/PDF and editor remain unchanged. No
original theorem, model invocation, Rethlas receipt, Xean run,
canonical-status change or BJ22 closure repair is added. Publication
uses an ordinary push to work after explicitly fetching both branch
references; the existing draft PR is updated with the scoped record.
