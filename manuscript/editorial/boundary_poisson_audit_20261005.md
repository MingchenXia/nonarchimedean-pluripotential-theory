# Boundary singularities and homogeneous nonuniqueness

This known-result checkpoint follows `90d5965`. Chapter 68.12 and
provenance L.42 explain Xieping Wang's explicit unit-ball family from
arXiv:2609.15572v1. No original theorem or production-model receipt is
claimed. The research-only entropy class-perturbation candidate stays OPEN.

## Primary source and reading scope

The official arXiv history, inspected on 5 October 2026, lists v1 submitted
14 September 2026. The acquired PDF has an internal date of 15 September;
these two dates are distinguished. It has fourteen actual pages, all read
as extracted text and all actually displayed in seven sheets. The source is
cached in `source_material/pluricomplex_Poisson_20261005/`, with an unchanged
historical acquisition record and a fresh complete-reading record.

PDF: 364749 bytes, SHA-256
`c148f9dcf659b91d11138f3222dcfafca7bfbce5a15eabe1707be93fafdf6545`.
Extracted text: 50595 bytes, 783 Python splitlines, SHA-256
`1c94c045dfbb014dd19b99297f207391a389e6abf3d145eb06e2da67feec2d6c`.

Controlling primary anchors:

| Statement or input | Actual page in v1 |
| --- | --- |
| Boundary equation (1.2), comparability and approach region | 2 |
| Explicit nonunique ball family, Theorem 1.2 | 3 |
| Cayley map and complex Hessian identity, Lemma 3.1 | 8–9 |
| Convex envelope (3.1), coefficients and Lemma 3.2 bounds | 9–10 |
| Smooth unique maximum, Lemma 3.3 | 10–11 |
| Axis and large-height asymptotics, Lemma 3.4 | 11–12 |
| Theorem 3.5, continuous psh extension, noncharging and distinctness | 12–13 |

The general-domain Theorem 1.1 and its Section 2 proof were also read.
Their prior Huang–Wang and Wang geodesic-regularity papers have not been
independently acquired for this checkpoint. The general-domain theorem is
not admitted here; the admitted explicit family needs only Section 3,
elementary calculus and the book's existing locally bounded
Bedford–Taylor/removable-singularity foundations.

## Exact signature and boundary conditions

The ambient space is the unit ball in C^N with N=m+1>=2. The functions are
continuous and plurisubharmonic inside the ball, locally bounded there,
and have ordinary Bedford–Taylor top measure zero. They extend with value
zero at every boundary point other than p=(1,0,...,0). Growth at p is
comparable to minus the reciprocal Euclidean distance within each fixed
nontangential approach region. The comparison constants may depend on
its aperture; exact leading coefficients along all curves are not specified.

For P=-(1-|w|^2)/|1-w_1|^2, the inequalities P<=u_lambda<=e^(-lambda)P
are correctly ordered because P is negative. They give zero boundary
values away from p and the required nontangential comparison. This does
not contradict an envelope definition with a prescribed normalization,
nor a rigidity result requiring harmonicity on every geodesic leaf.
There is no planar harmonic counterexample.

## Cayley coordinate correction

The PDF's page 8 fixes p=e_1 but writes C(z,zeta) with its scalar
(zeta-i)/(zeta+i) component last. That ordering sends its distinguished
point to e_N, so the claimed identity with the e_1-kernel has a coordinate
mismatch. The book permutes the components and places the scalar first.
Directly,

1-|C|^2=4(Im(zeta)-|z|^2)/|zeta+i|^2,
|1-C_1|^2=4/|zeta+i|^2,

which proves P composed with C=|z|^2-Im(zeta). No property of the
constructed family changes under this unitary coordinate permutation.

## Convexity, rank and the analytic axis

For y>exp(x), every member c_lambda(t)(exp(t)(1+x-t)-y) is negative
and affine in (x,y) with positive x-slope. Its finite supremum is convex
and increasing in x. The tangent inequality and the test t=x give the
two-sided envelope bound. The source's scalar stationarity function F
has opposite infinite limits, and every zero has derivative below -1.
It therefore has exactly one zero, a strict smooth maximum. Here
0<lambda<1 and 0<kappa<=lambda/4 are retained.

At that maximum E''=exp(t)cF'<0. Affinity in (x,y) and implicit
differentiation give Hess_R f=-b b^T/E'', where
b=(exp(t)(c+c'),-c')^T. This outer-product reformulation is explicitly
identified as a direct formal differentiation of the known construction.
Its rank is one since c+c'=c(1-kappa)>0. The stationarity and both mixed
derivative identities were additionally checked symbolically; this is a
diagnostic, not an independent mathematical verifier.

The complex determinant formula has exponent m-1 and the factor 1/(4r^2).
It applies for r=|z|>0 and forces zero top measure off the axis. The
source's locally uniform x->-infinity asymptotic gives continuity on the
axis with value -Im(zeta). The locally bounded removable psh extension
and ordinary Bedford–Taylor noncharging of the analytic axis exclude
hidden mass there. An off-axis determinant calculation alone would
not suffice. No non-pluripolar replacement of a polar residual measure
is being made: these functions are locally bounded inside the domain.

## Distinctness, normalization and exclusions

All v_lambda agree with rho=-Im(zeta) on the axis. For each fixed z!=0,
v_lambda(z,iy)/rho(z,iy)->exp(-lambda) as y->infinity. A proportionality
constant must therefore be one on the axis, while different lambda give
different limits. Pairwise nonproportionality is the identified direct
formal consequence. All ball solutions agree with P on one disk; the
example does not impose harmonicity on every prescribed leaf.

The source's numerical ddc coefficient is immaterial for positivity and
a homogeneous zero top measure. The book keeps ddc=i/(2pi) partial
barpartial. No positive pole mass, boundary Dirac measure, finite global
Cegrell energy, probability normalization or compact class is asserted.
There is no deduction about boundary concentration of Gibbs maximizers.
The preceding BB critical theorem retains no boundary blow-up, its
selected variational family and its F limit.

The general non-Archimedean Siu/closure problem, A2–A4 and spectral
questions are untouched. The forty-two complete canonical problem
statuses, native catalogue, prior primary-reading receipts, frozen
manifests and separate toric research candidate retain their bytes.

The first build passed TeX and navigation gates. Its scoped page review
found a presentation issue: the new Monge–Ampère index term used a new
sort/display key, splitting an existing accented entry. The added term
was changed to that existing key, with no mathematical change. This
second build produced one 10.55237pt vertical overfull box in the
balanced final index page. The redundant new Monge–Ampère pointer
was therefore removed; the dedicated pluricomplex Poisson kernel
entry retains access to the section. The first PDF and its 24
actually displayed pages remain historical diagnostics, and the
second build is a failed presentation diagnostic. The third build
reduced the balanced-index vertical overfull box to 0.55237pt. The
dedicated Poisson kernel term was then made a direct page entry,
removing an unnecessary subentry line. The fourth build retained
the 0.55237pt vertical overfull box. A fifth full build with zero
index-scoped multicolumn separation did not remove it.

Fresh isolated index probes then reproduced the same 0.55237pt
box with the ordinary layout. The natural-column-height variant
(`raggedcolumns`) passed with the same nine index pages, while a
reduced line-leading probe did not solve it. The first probe
launch lacked the class search path and produced no PDF; that
failed record is retained separately. The successful second probe
uses the book's preamble, current index and explicit style path.
No probe is a final-book build or full-book reading.

The final repair uses a one-use environment hook in `book.tex`
to select natural column heights only in the index. Font sizes,
the class and other environments are unchanged. The final release
uses a fresh sixth full build and fresh matching page review.
Three active inputs change: Chapter 68, provenance L and this
index hook.

The sixth full build is the final 4,334-page release: SHA-256
`99ae882e7f9f0c9545d74005a4c1a83d3a4759ce50ebe9de52d360fb03c6e5da`.
TeX, bibliography, references, index and PDF navigation checks pass;
there are zero overfull boxes. All twelve matching review sheets
were actually displayed, covering twenty-four physical pages:
1, 60, 61, 67, 68, 3597–3602, 4098–4101, 4309, 4313–4315,
4317, 4319 and 4332–4334. The section, surrounding transitions,
provenance, corrected index columns and bibliography display cleanly.
This is a scoped review, not another whole-book reading. The review
PDF has twenty-four pages and SHA-256
`95cc9f02df3f398c18d3a6caefa53f46289d205a8e5c97c74218775d62bf85f4`.

The final gates retain 425 active inputs, 12,728 unique labels,
632 bibliography keys and 337 cited keys. All 108 protected inputs,
forty prior frozen manifests and forty-two complete canonical problem
status rows retain their bytes. The source closure changes exactly
the three inputs identified above. No independent production-model
call, fresh native-catalogue compilation or isolated export compilation
is claimed. Normal work-branch publication continues under the user's
standing GitHub authorization, with platform permission checks retained.
