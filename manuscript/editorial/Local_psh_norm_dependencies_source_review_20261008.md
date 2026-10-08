# Finite-flat norm metrics: exact hypotheses and remaining local interfaces

Date: 8 October 2026. This is a source-only continuation after the verified
4,651-page Wu integration, not another whole-book pass or a new theorem
promotion. The controlling source is the published Boucksom–Eriksson,
*Spaces of norms, determinant of cohomology and Fekete points in
non-Archimedean geometry*, Advances in Mathematics 378 (2021), 107501,
DOI 10.1016/j.aim.2020.107501. The exact cached Chalmers PDF has SHA256
f9b8d54cfb2733486f35d450f5f763acf81a51816368ccd2c24c0663845d84f9:
125 physical pages, including its cover, versus 124 article pages.

Twenty-nine disjoint physical pages were freshly read with complete selected
text and fifteen individually displayed matching images, with sequential
notes/receipts. The first batch is 1–2, 78–88 and 119–123 (18 pages/nine
views). The second is 22–23, 52–54, 62–64 and 69–71 (eleven pages/six views).
This is a partial source reading; the other 96 pages are not claimed read
in this checkpoint. Existing earlier source readings receive no reuse or
fresh credit here. Preparation flags remain false. The first preparation
helper counted historical editorial TeX drafts in the core-input census and
failed before making any images or record. Its empty directories and failed
helper are frozen. V2 uses the already verified 425-root core inventory.

The local-psh main source remains Wu arXiv:2609.27610v1. This follow-up
narrows its norm-metric dependency; it does not certify its general
weak/global comparison or envelope theorem.

## Fibre multiplicities and the sign of the norm weight

For a finite flat map (f:Y	o X) of constant degree (d), the scheme
fibre over an analytic point (x) has finite algebra

[
 A_x=prod_y A_y,qquad n_y=dim_{H(x)}A_y
      =operatorname{length}(A_y)[H(y):H(x)],qquad sum_y n_y=d.
]

Example 8.2 (physical 71/article 70), Theorem 8.16's zero-dimensional proof
(physical 81–82/article 80–81), and Appendix (A.8) (physical 120/article 119)
retain both nilpotent length and residue-field degree. The analytic fibre
measure is (sum_y n_ydelta_y), not counting measure on its points.
The intrinsic multiplicity is Artinian composition length; notation such as
(dim_{K'}A) should not assume an unproved compatible residue coefficient
field over an imperfect base.

The norm line is
[
 N_f(L)=det f_*Lotimes(det f_*mathcal O_Y)^{-1}.
]

Lemma A.19 identifies this determinant line with the classical cocycle norm;
A.20 supplies its additive structure and base-change compatibility. For a
local trivializing section (s), (8.17) defines the metric by
[
 log|N_f(s)|_{N_f(phi)}(x)
       =sum_{f(y)=x}n_ylog|s(y)|_phi.
]

Thus the additive potential is **minus** the logarithmic section norm. For
real functions, the weighted trace satisfies
[
 N_f(f^*g)=dg,qquad
 |N_f(u)-N_f(v)|_inftyleq d|u-v|_infty.
]

These elementary identities are distinct from psh preservation. A concrete
diagnostic over (K=mathbf F_2((t))) uses
(A=K[z]/((z^2-t)^2)), of rank four, length two and residue degree two.
The determinant norm of (z) is (t^2), while (v(z)=1/2), so the
weighted logarithmic identity has coefficient four. The nonzero element
(epsilon=z^2-t) squares to zero. There is no compatible (K)-embedding
of (K(sqrt t)) into (A): writing a candidate in the basis
(1,z,z^2,z^3), its square's (epsilon)-coefficient forces the remaining
constant to be a square root of (t) in (K), impossible by its odd
(t)-adic valuation. This diagnoses coefficient-field notation, not the
intrinsic length or determinant formula, and is not a geometrically reduced
example within Proposition 8.22.

## The precise continuous global norm theorem

Proposition 8.22, physical 86–87/article 85–86, assumes:

- a finite flat morphism of **projective geometrically reduced** (K)-schemes;
- an **ample rational** line bundle on the source;
- a **continuous psh** metric in the paper's global metric class.

Its conclusion is that the norm metric is continuous psh. In the
nontrivially valued case, its proof passes through Theorem 7.8's uniform
nef-model approximation, compatible finite flat models and norm nefness
via singular-curve Riemann–Roch. The norm's degree-Lipschitz bound passes
the limit. The model trivialization argument is on a **reduction tube**,
as is Lemma 8.19, not the entire generic algebraic open.

Proposition 5.13's graph closure and Raynaud–Gruson step allow replacing
the target model by a blowup and the source by its proper transform. That
is sufficient when the norm proof chooses both compatible models. The
printed proof does not establish flatness over every arbitrarily fixed
original target model. Relative ampleness, flattening and singular-curve
Riemann–Roch are attributed classical inputs, not recursively certified.

Theorem 7.8 assumes nontrivial valuation, ample rational polarization and
continuity. Remark 7.10 explicitly leaves its merely semiample extension
as an expectation. Theorem 7.31 permits arbitrary complete field extension
for a **continuous** metric on a **semiample** line bundle over a
**geometrically reduced projective** scheme; its proof uses the prior
Theorem 6.6 sublinear supnorm/base-change estimate, not newly reread here.
Lemma 1.26 chooses a suitable nontrivial extension for at most countably
many finite-dimensional norms over a trivially valued field. It is not a
countable-dense-subfield assertion for arbitrary fields.

These results explain the intended norm interface over arbitrary complete
fields in the correct continuous global scope. They do not provide Wu's
missing affine regularization over a nondiscrete completed residue field,
nor turn a lower coercive bound into an upper majorant. In characteristic
zero, reduced finite-type schemes are geometrically reduced, but the
metric class, projectivity, polarization and continuity still require proof
at the precise application. In positive characteristic, reducedness alone
does not meet the cited theorem's hypothesis.

## Maximum iteration and approximation details

In the intended ample base-polarization application of Proposition 8.24,
a continuous psh metric (psi) on (f^*L) can be averaged and maxed with
its original value. Use
(N_f(f^*L)simeq L^{otimes d}), rather than mistyping the source bundle
as (N_f(L)). The multiplicity-weighted iteration in Lemma 8.25 has
error at most ((1-1/d)^kM_0) for (d>1). A fibre maximum has positive
integer weight at least one, explaining the contraction. The degree-one
case is the identity. The construction is on compact continuous global
data; its final descended-psh inference is not proof of arbitrary local
USC or weak-psh descent.

The converse proof in Corollary 7.6 needs a fast subsequence before shifting
an arbitrary uniformly convergent sequence by constants tending to zero.
On two reduced projective points, the FS metrics
[
 phi_i=igl((-1)^i/i,-(-1)^i/iigr)longrightarrow(0,0)
]
would require (c_i-c_{i+1}geq1/i+1/(i+1)) to make the entire shifted
sequence decreasing. The required differences have divergent sum. A
subsequence with uniform error at most (2^{-k}), shifted by
(c_k=3,2^{-k}), does decrease to the same limit. This corrects that
particular proof step; it does not refute uniform-closure membership or
establish a replacement general envelope theorem.

Five exact rational/symbolic diagnostic families check the nilpotent
determinant, fibre rank/uniform estimate, weighted contraction, divergent
shift requirement and fast-subsequence repair. They are elementary tests,
not original general theorem promotions or independent-model receipts.

## Local printed slips and retained dependencies

The contemporaneous notes retain these local issues without extending them
to a rejection of the intended norm theorem:

| Physical page | Printed issue | Intended local reading |
| --- | --- | --- |
| 79 | repeated (L_2|_{Z_0cap Z_1}) in one proof pairing | list (L_2,ldots,L_n), as in the lemma statement |
| 81 | one prose curvature sign is plus | minus, as in (f=log|s|_phi) and the following display |
| 119 | finite-flat (lambda(L)) printed as (det f_*mathcal O) | (det f_*L), as in Lemma A.17 and the norm ratio |
| 87–88 | wrong base/source polarization and fibre variables | base (L), source (f^*L), and correctly typed fibre maximum |
| 53 | cover variables swapped; flattening changes target model | cover the model carrying (L), permit the target blowup |
| 63 | ample model (A) becomes undefined (H); model primes inconsistent | perturb by the chosen (A) on the dominating model |
| 69 | first proof direction in Lemma 7.29 repeats continuity hypothesis | assume the stated USC-upper-envelope-is-psh property for that direction |

The corrected first direction of Lemma 7.29 uses the assumed psh upper
envelope, a decreasing FS presentation and compact Dini buffers. It does
not establish the property unconditionally. Source-era Conjecture 7.30
remains visibly a conjecture. Complete prior logarithmic-integrability,
supnorm/base-change, reduced-fibre and higher-dimensional Ducrot proofs
are not recursively certified by this partial reading. Their exact scopes
remain listed in the manifest.

## Recent-paper and APW discovery

The frozen exact-title APW query in the preceding Wu checkpoint returned
no matches. This checkpoint's broader surname query is deliberately filtered
against the exact named authors; it contains unrelated homonyms and no
identified version of the two required preprints. The bounded query is
metadata evidence, not proof that the dependencies are unavailable.

Two recent arXiv searches are retained. The broader title search locates
the exact already-reviewed Wu version, October hybrid dynamics and harmonic
quiver papers, Lin's toric restriction paper and other related directions.
It also identifies arXiv:2606.19160v1, *Non-archimedean Green currents for
the zero-locus of a regular section*, as a candidate for primary review.
Its metadata/abstract supplies zero proof-reading credit. No result from
that unread source is integrated here. Existing audited papers are not
credited again merely because they appear in a new query.

The book remains at 4,651 pages. All 425 core TeX roots, two bibliographies,
active PDF and native catalogue/editor are unchanged at this source-only
checkpoint. The 42 atoms/twelve formal problems keep their statuses:
general BJ22 critical homogeneous Siu/envelopes OPEN, LPWZ density
UNVERIFIED. The warning about BJ22 Theorem 6.21 remains binding. The last
complete ordered whole-book pass is 4 October. This audit and its uploaded
authored records add no reading credit beyond the actual 29 pages above.
