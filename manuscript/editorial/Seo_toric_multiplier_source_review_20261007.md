# Toric analytic multiplier ideals: affine pairs, Newton bodies and source boundaries

Date: 7 October 2026. Baseline `work` commit
`d7e68b2e567e38480d6be3b1d16f16d74b3123a4`; observed `main`
`00957114db21b627e97369563032ceda9cea09c7`.

Hoseob Seo's *Analytic multiplier ideals of toric plurisubharmonic functions
on a toric complex space*, arXiv:2610.08741v1, submitted 6 October 2026
at 17:40:00 UTC, was read completely: 33 physical pages in 17 individually
displayed sheets. Eight dependency PDFs were read in selected scopes:
45 further physical pages in 24 displayed sheets. All **78 distinct
source/page pairs in 41 sheets** have complete selected-text reading,
matching image inspection and sequential notes. There is no identity-based
reuse in this source checkpoint. Four PDFs are complete readings, including
the two short errata files; five are partial readings. This is a scoped
source audit, not a certificate for the entire recursive proof chain.

The main affine-pair criterion is suitable for a connection to Chapters 51
and 55. Its character lattice, adapted volume, weight normalization,
fractional-module scope and non-full-dimensional cone must remain explicit.
An open logarithmic neighbourhood cannot literally equal the closed
translated cone printed in the main proof. Cofinal neighbourhood inclusions
provide the required local-integrability comparison. The archived Blickle
antecedent also has a literal shift-sign inconsistency; its uninspected
journal edition is not accused of that error. These source qualifications
do not supply an original theorem or an independently certified repair.

The source-only checkpoint preserves the 4,495-page book, 425 active
inputs, 108 protected inputs, 108 previous frozen manifests and 184 frozen
exports. The canonical problem inventory and open historical native
catalogue/editor are unchanged. There is no original-result promotion,
model call, new receipt, solved status, BJ22 Theorem 6.21 repair, critical
division proof, or general envelope closure claim.

## Exact files and actual reading

Physical pages, rather than publisher page ranges or extraction line
numbers, control this table. Matching images settle closure bars and
rounding signs. The actual notes and file hashes are included in the
companion manifest.

| Exact controlling file | Physical pages actually read | PDF SHA-256 |
| --- | --- | --- |
| Seo 2610.08741v1, 6 October 2026 | 1--33, complete | `8015b8373fd823459692c3e2c94020384cbcd6c3b607a6728f8080c57484be01` |
| Guenancia 1011.3162v2, 12 May 2011 | 3--11 of 24 | `1816e70d4fdec46864f1ee821d6d4f83ce26bc43678844adf744b9595adda9f5` |
| Blickle math/0310487v1, 31 October 2003 | 1--8, complete | `56a642806a7fc1828ffd163f0ea50b1f6260067567480bb76161cb9d8365a3aa` |
| Fujino--Schwede--Takagi, author-hosted `supplements_revised2.pdf` | 10--13 of 46 | `bde1ba1e6fa31940405e5548850aab62e985ca369e06ee839fa1cdcafc6b48f4` |
| Li 2201.13069v1, 31 January 2022 | 2--5 of 9 | `4ec4a4e8abdc50d5359dc8471c894ca59784e3e2fc50f71e3ba4b5f5ea27db20` |
| Guan--Zhou, official Annals 182 (2015), 605--616 | 1--2 of 12 | `f1b155ff1615d60eaeb3d2c7347f301efd6a869aa0eddd2ae3da59b361919b28` |
| Rockafellar--Wets, author-distributed *Variational Analysis*, cover identifies third printing 2009 | 1--2, 94--97, 99--100, 482--486, 501--502 of 743 | `24fb23c38a92f34b8c89d2b6dbecb148071462866441f82d7a70541385608fa4` |
| Rockafellar--Wets, March 2009 second-printing errata | 1--2, complete | `eba2e23612531a67ea7f6cdfaa6808b4b880ae875fc264986729d2d887f5231f` |
| Rockafellar--Wets, December 2013 third-printing errata | 1, complete | `83152b03d694c59be4a050f629f1ced83e05dbf9209c5b9c6e6fe2af71bbf920` |

The 46-page Fujino author revision is not the 47-page journal layout.
Guenancia's 2011 v2 is not silently treated as the later Math. Z. 271
edition. Blickle's publisher PDF endpoint redirected to subscription
metadata; no published theorem locator was cleared from that response.
The first Annals filename attempt returned 404; the separately discovered
official `-p.pdf` endpoint supplied the inspected published file. The
initial network-restricted Seo acquisition and this 404 remain frozen
diagnostics, not successful acquisitions or automatic-approval rejections.

## Main result and proof ingredients

**T01 — Ambient signature.** Seo Theorem 6.1, physical pp.28--29,
concerns the normal affine toric analytic space associated to a strongly
convex rational polyhedral cone `sigma` in a lattice `N`, with actual
dual character lattice `M`. An invariant rational Weil divisor `D`
satisfies `K_X+D` Q-Cartier. The weight is a compact-torus-invariant psh
function in the local ambient-extension sense, not identically minus
infinity. The cone need not span `N_R`, and `D` need not be effective.
The analytic space is complex; the algebraic toric resolution argument
in Blickle is not an analytic positive-characteristic extension.

**T02 — Adapted volume and factor two.** Definition 3.1, p.8,
uses meromorphic germs `f` with `|f|^2 exp(-2 phi)` integrable against
the volume of a local pluricanonical generator after an integer index
clears `K_X+D`. Analytic ideal weights are
`phi_a=(1/2) log(sum |f_j|^2)+O(1)`, p.7. The book's squared-norm
weight `psi` therefore equals `2 phi`. Bounded positive changes of the
adapted volume leave the integrability module unchanged. Li Definition
2.2 / Remark 2.3, physical p.3, are the checked antecedent. Broader
real-divisor wording does not produce an integer generator without an
additional Cartier construction.

**T03 — Canonical shift.** Section 2 and the proof of Theorem 6.1
use `K_X=-sum D_rho`, primitive ray vectors `v_rho` and
`<u_D,v_rho>=1-a_rho`. Equivalently,
`q(K_X+D)=div chi^(-q u_D)`. On the dense torus the adapted radial
measure contributes `|chi^(u_D)|^2`; the interior criterion is
`m+u_D in int P(phi)`. The convention must be fixed before comparing
an antecedent's sign. A multiple `q u_D` must belong to the actual `M`,
not merely have integer coordinates in an ambient covering lattice.

**T04 — Fractional and holomorphic modules.** Proposition 3.3,
pp.10--11, shows that effective `D` and a locally upper-bounded weight
give holomorphic germs: an integer pole along a prime divisor makes
the one-variable adapted-volume integral diverge. Negative `D` can
permit poles. The exact smooth test `D=-[0]`, `phi=0`, permits `1/z`
and gives `O([0])`. Thus the general result is a coherent fractional
module, not always an ideal contained in `O_X`.

**T05 — Birational transformation.** Lemma 3.4 and Proposition
3.5, pp.11--12, write
`A=K_Y-q^(-1) mu^*(q(K_X+D))`. The pullback adapted density has
normal-crossing powers `|z_i|^(2a_i)` and a bounded smooth unit.
Rounding `A` leaves the effective remainder `ceil(A)-A`, giving
`mu_*(O_Y(ceil A) tensor I(Y,0;phi o mu+phi_(ceil A-A)))`.
The finite covering of each compact fibre precedes shrinking the base
neighbourhood. Proper direct images, meromorphic descent and smooth
Nadel coherence remain attributed foundational inputs. Li Proposition
2.4, p.3, gives the matching discrepancy convention.

**T06 — Algebraic analytic singularities.** Theorem 3.2,
pp.8--10, identifies the analytic module with analytification of the
algebraic pair multiplier module. On a common log resolution the
integer poles are absorbed by `ceil(a_i-c b_i)`, leaving powers in
`(-1,0]`. The meromorphic square-integrable remainder is holomorphic.
This input concerns a nonzero algebraic ideal and positive real `c`;
compatibility of proper pushforward with analytification is imported.

**T07 — Local denominator clearing.** Lemma 3.6, Proposition 3.7
and Corollary 3.8, p.13, use Cartier twisting and a holomorphic
denominator to reduce locally to effective boundary and smooth
coherence after resolution. The construction permits a denominator
vanishing along all relevant negative components; it does not require
the original boundary to be effective. Cartan A and Grauert are
explicit external foundations, not independently proved in this audit.

**T08 — Strong openness with fixed boundary.** Corollary 3.9,
pp.14--15, scales only the psh weight, retaining `D`. On a resolution,
the nonpositive normalized fractional-divisor weight gives the stated
sandwich between the two perturbations. Smooth strong openness and
a finite compact-fibre cover provide a common small epsilon. The
checked published Guan--Zhou Theorem 1.1 is on printed p.606 / physical
p.2 and uses `exp(-phi)`; apply it to `2 phi`. Its complete 12-page
proof is not claimed read here. The conjecture language in Guenancia's
2011 text is historical and must not become a current open status.

**T09 — Convex logarithmic weight.** Lemma 5.1, pp.20--21,
identifies a toric psh weight with a finite convex function `g` on
`N_R`, increasing in cone directions. Conversely a finite convex
cone-monotone function is bounded above on local monomial polydisks
and extends psh across the normal boundary. The normal removable
extension theorem is the imported input; local boundedness uses
Minkowski--Weyl geometry and compact transverse parameters.

**T10 — Newton body, closure and interior.** Definition 5.2,
pp.21--22, defines
`P(phi)=dom((g+indicator(-sigma))^*)` by a finite supremum.
It need not be closed. Lemma 4.4 and Proposition 5.3 identify its
closure by recession half-spaces and its ordinary interior by strict
inequalities in every nonzero direction in `-sigma`. The closure bar
visible in the source image is retained. Uniformity follows from
lower semicontinuity on the compact unit-direction section; a
pointwise strict inequality is not passed through an unproved
integral limit.

**T11 — Convex primary-source substitute.** Seo cites
Rockafellar's 1970 *Convex Analysis* Theorems 13.3 and 16.4. That
controlling edition was not read here. Instead the author-distributed
Rockafellar--Wets third-printing copy supplies checked Theorems 3.21
(printed p.88), 3.26(a) (pp.91--92), 11.1 (p.474), 11.5
(pp.477--478) and 11.23(a) (pp.493--494). These give the convex
recession formula, linear lower growth, biconjugacy, support of the
conjugate domain and conjugation of a sum. Finite `g` supplies the
domain-interior qualification even for a lower-dimensional cone.
The alternate locators do not authenticate the unread 1970 locators.
Both read author errata lists leave these selected locators unchanged.

**T12 — Exponential integrability.** Theorem 4.6, pp.18--19,
assumes the cone full-dimensional in the integration vector space.
Strict recession positivity of `g-<m,->+indicator(-sigma)` gives a
uniform bound `gamma |x|+beta` with `gamma>0`, so exponential tails
are integrable. Necessity uses a positive-volume half-tube along a
failed direction, rather than an isolated measure-zero ray. Remark
4.7 supplies uniformity over compact transverse parameters. The
smooth orthant antecedent is Guenancia v2 Proposition 1.9,
pp.5--6, with its full selected proof; Theorem 1.13 and the Parseval
argument are on pp.7--8.

**T13 — Finite monomial generation.** Section 5.3,
pp.23--26, first Fourier-projects global Stein sections. Coherence
gives continuity in the global quotient; a projected section is a
single character on the dense torus. Finite jet quotients and
Krull intersection force each germ into the monomial-generated
ideal. Cartan A and Noetherianity yield finite generation. Extension
from a closed-orbit neighbourhood uses invariant monomial sections
and torus translates. The proof does not average a germ while its
base point moves. A compact-torus-invariant coherent module is
promoted to full-torus invariance by holomorphic one-parameter
families and the identity theorem in the Fréchet quotient.

**T14 — Fractional finite generation.** Corollary 5.8, p.25,
uses the coherent nonzero invariant colon module `(O:F)` to obtain
a global character denominator. Multiplication by that character
reduces to the finite monomial ideal case. This supplies finitely
many global meromorphic character generators; their exponents need
not lie in the holomorphic semigroup.

**T15 — Non-full cone.** In Theorem 6.1 the saturated lattice
`N_sigma=N intersect span_R sigma` is split from its complement.
The space is a smaller affine toric space times a torus, and the
unique closed orbit is `{z_0} times T`, rather than necessarily a
single fixed point. Integration on the cone uses its own span;
the transverse logarithms lie in compact annuli. Changing `u_D`
by an element annihilating `sigma` does not change body membership.
The zero-cone case is the dense torus with locally bounded weights
and ordinary module `O_X`.

**T16 — Neighbourhood equality qualification.** The main proof,
pp.28--29, prints an exact equality between the logarithm of an
open monomial neighbourhood and a closed translated cone times an
open transverse set. That equality is literally false, already for
one disk. The elementary local comparison uses the cofinal sets
`S_L={<m_j,x><-L}` in the full cone span. If all
`<m_j,b>>L`, then `-b-sigma subset S_L`; if
`L>max_j <m_j,b_0>`, then `S_L subset -b_0-sigma`.
Retain compact transverse annuli and use recession/translation
invariance. These inclusions are explanatory source qualifications,
not a new repair theorem or independent-model receipt. No
counterexample to the main criterion was found in this audit.

**T17 — Negative ideal weight.** Proposition 5.10, p.27,
requires positive **rational** `c` for the pair reduction of
`phi-c phi_a`, where an invariant coherent nonzero ideal has
finite character generators `chi^(a_j)`. The integrability module
is the finite intersection for boundaries
`D-c div chi^(a_j)`, because the sum-of-squares weight is comparable
to the finite sum of individual powers. Corollary 6.3, p.30,
requires `m+u_D+c a_j` in the interior for every `j`.
The resulting weight need not itself be psh. Do not extend the
Q-Cartier proof to irrational `c` by notation alone.

**T18 — Non-lc qualification.** Seo Definition 3.11 and
Propositions 3.12--3.13, pp.15--16, correspond to the checked
Fujino--Schwede--Takagi author-revision Definition 7.1 / Lemma
7.2 (pp.10--11) and Lemma 7.5 with its proof (p.12).
The log-canonicity test and small-negative-ideal-power description
retain effective `D`. Maximal non-lc rounding moves negative
integer discrepancies off their ordinary multiplier boundary.
The smooth example `D=[0]` has ordinary multiplier ideal `(z)`
but maximal non-lc ideal `O`. Closed Newton membership for the
latter must not replace the strict multiplier interior.

**T19 — Bounded perturbation.** Remark 6.4, pp.30--31,
calls a toric psh weight plus a locally bounded measurable function
toric quasi-psh. State that class explicitly: it is broader than
the book's usual psh-plus-smooth convention. A bounded perturbation
does not change the integrability module or the finite-supremum
Newton domain on the relevant relatively compact logarithmic cone
set. No new definition of quasi-psh is forced into earlier chapters.

**T20 — Ancillary boundary.** Remark 3.10's comparison with
Nadel--Ohsawa/Grauert--Riemenschneider ideals and its lci identification
is not independently cleared. The selected Li passage introduces a
different divisor measure; its subsequent proof was not read to
completion. Cartan A, Krull intersection, smooth Nadel coherence,
Grauert, normal extension and resolution remain explicitly imported.
No claim of fully checked recursive foundations is made.

## Exact diagnostics and historical-source qualifications

The companion diagnostics use integer/rational arithmetic and signs of
`A sqrt(2)+B` by comparison of integer squares. No floating threshold
is credited as a certificate. Two bounded grids each check 1,681
points; unbounded semigroup cases are also recorded explicitly.

**E01 — Seo Example 6.2.** On `z_1 z_2=z_3^2`, put
`z_1=s^2`, `z_2=t^2`, `z_3=st`, so
`M={(a,b) in Z^2:a+b even}`. For `D=(1/2)E`, the shift
is `(1/2,1)` and its actual Q-Cartier clearing index is **4**.
The weight has logarithmic function
`max(2 sqrt(2)x_1,4x_2)` and Newton body
`conv((2 sqrt(2),0),(0,4))+R_+^2`.
The strict translated inequality yields
`I_D=(z_1,z_3,z_2^2)`, whereas `D=0` yields
`I_0=(z_1,z_2,z_3)`. Every generator and semigroup difference is
checked in the even-sum lattice. An ambient `Z^2` calculation would
admit nonexistent characters and miss the clearing index.

**E02 — Module and cone boundaries.** Smooth effective and negative
one-dimensional boundaries distinguish holomorphic and fractional
modules. A ray in `R^2` gives `C times C*`, with arbitrary transverse
character exponents and arbitrary perpendicular shift; the closed
orbit is one-dimensional. The zero cone gives the torus case.
The ordinary/maximal non-lc example fixes strict versus closed
thresholds without an unproved limiting argument.

**E03 — Literal logarithmic equality.** An open disk has logarithm
`(-infinity,-1)` after a chosen radius, whereas a closed translated
ray includes its endpoint. A rational-generator example checks both
cofinal inclusion directions exactly. This diagnoses the printed
equality rather than the main theorem statement.

**E04 — Blickle archived v1 sign.** Physical p.2 defines
`div x^u=r(K_X+Delta)`, `w=u/r`, but then uses `m+w`.
For `X=C`, `Delta=0`, `a=(z)` and `c=1`, the actual multiplier
ideal contains `z` by direct integration, whereas that literal
shift is `-1` and excludes it. The proof on p.5 repeats the conflict;
the p.7 corollary instead writes `K+Delta=-div x^w`, consistent
with the positive shift. The module proof also prints an opposite
canonical-divisor sign in an intermediate inequality. Record only
these inspected **2003 v1** statements. The subscription journal
edition is not declared wrong or repaired by inference.

**E05 — Guenancia archived v2 proof text.** The finite-monomial
lemma on p.7 selects inequalities between adjacent terms along a
subsequence; that does not establish a decreasing subsequence of
the selected coordinates. Standard polynomial Noetherianity supplies
the finite-generation fact. The p.8 substitution `t=-log r` prints
`log(radius)` instead of `-log(radius)` as its endpoint; a unit
polydisk avoids that normalization typo. The p.10 valuative proof
mentions isolated singularities beyond its displayed signature.
These diagnostics are not counterexamples to the smooth toric
multiplier criterion, and no unchecked valuative or adjoint statement
is imported from them.

**E06 — Versions and outstanding source gates.** Strong openness
is proved by the inspected 2015 theorem, despite the older conjecture
language. The unread 1970 convex locators have checked alternative
primary anchors, rather than retrospective clearance. Author
revision, preprint and journal numbering remain separate. No
historical speculative question in Blickle's final section is added
to the current open-problem inventory without a present literature
status check.

## Integration and continuation

The proposed integration should explain the adapted pair module and
actual character lattice beside Chapter 51's smooth multiplier ideals,
then connect the logarithmic Newton domain and recession inequalities
to Chapter 55's convex dictionaries. A scoped appendix can retain
finite generation, non-full cones, negative ideal weights and the
worked singular example. Imported theorem attribution and the literal
source qualifications must be visible; proof-audit records stay
editorial. Compile and read every changed final page before publication.

The newly discovered arXiv:2610.07826v1 (variation of singular
Kähler--Einstein metrics and invariance of plurigenera) and
2610.07528v1 (finite pullbacks, Segre and generic Lê numbers) remain
metadata-only candidates. Their PDF proofs have not been acquired or
read, and neither is certified suitable for integration. Fang
2610.06719v1 was already audited in the preceding research cycle and
is not counted again as a new reading. Continue source-checked cloud
research and inspect incoming author progress at GitHub checkpoints.
