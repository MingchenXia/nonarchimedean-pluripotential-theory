# Projective nonuniqueness and the zero-boundary mean-field equation

This checkpoint continues `6237e78` on the cloud-only `work` branch.
The preceding big-class release, all earlier frozen records and the open
native LaTeX catalogue remain immutable. The new Chapter 68 subsections
and Appendix L.38 admit identified known material, not a new general
result or an independent production-verifier receipt.

## Primary reading and admission

Lu–Phung, *On uniqueness of solutions to complex Monge–Ampère mean field
equations*, [arXiv:2501.18281v1](https://arxiv.org/abs/2501.18281v1),
submitted 30 January 2025, manuscript dated 31 January, was read in full,
including references. Its 833-line Python `splitlines` extraction was read
in ranges 1–270, 271–535 and 536–833. All 15 actual PDF pages were
displayed and inspected. The 222,975-byte PDF has SHA-256
`57371de09ad8ab4599f8998661f7307ab413bfd7a7de65d7b3d9cd1aa56aecdf`.
Locators belong to this arXiv file. No byte identity with a later journal
publication is claimed. Acquisition metadata remains its historical
snapshot; mutable progress records the subsequent complete reading.

The imported inputs are Example 3.5, Theorem 1.2, Lemmas 2.2–2.3 and
Theorems 2.5–2.6, on actual pages 2, 3–6 and 12. They concern a known
smooth projective family and bounded zero-boundary solutions on bounded
hyperconvex domains. Compact Hermitian results and the source's compact
stability proof are not imported here.

### Projective family

The book uses the hyperplane-class form
`omega_H=ddc_b log(1+|z|^2)` on `P^n`, of volume one. Its globally defined
positive homogeneous ratio gives
`a_e=log((|z|^2+e)/(1+|z|^2))` and
`u_e=a_e-log(e)/(n+1)`, for every `e>0` and `n>=1`.
The current is a projective-automorphism pullback of the Fubini–Study
form. The Hessian eigenvalues are `(r+e)^(-1)` in the `n-1` tangential
directions and `e(r+e)^(-2)` radially. Thus its determinant is
`e(r+e)^(-n-1)`, and
`MA(u_e)=e exp(-(n+1)a_e) omega_H^n
         =exp(-(n+1)u_e) omega_H^n`.
The difference of values at the distinguished origin and a point at
infinity is `log(e)`, so the potentials are distinct even modulo
additive constants. They lie in an automorphism orbit. The example
concerns uniqueness of actual potentials and does not refute uniqueness
modulo automorphisms, a small-parameter result, or a strictly subcritical
existence criterion. The displayed `n+1` belongs to this fixed class.
No universal critical parameter is asserted.

The source uses `ddc_s=i partial partialbar/pi=2 ddc_b`; its unscaled
projective form is twice the book's hyperplane-class form. Dividing both
the source form and its currents by two gives the displayed family and
scales both top-degree measures by `2^(-n)`. This combined class change
keeps the potential and the parameter `n+1`. It is separate from the
local fixed-current conversion below.

### Local bounded solutions

The local equation has Euclidean volume, a nonnegative `L^p` probability
density with `p>1`, a bounded hyperconvex domain in `C^n`, `n>=1`, bounded
negative psh potentials, zero boundary values and ordinary Bedford–Taylor
mass one. The small-parameter statement does not require a smooth
boundary or a strictly positive density.

The criterion from Lemma 2.3 is `gamma ||u||_infinity<n` for each of two
solutions. A maximal bounded solution for the ordered unnormalized
constant, a bounded auxiliary density and the mixed inequality produce
`||w-v|| <= (gamma/n)||v|| ||w-v||`. The coefficient is strictly below
one. If `w=v`, then `u<=v`; the ordering of logarithmic normalizing
constants and unit mass force the densities to agree. Ordinary bounded
Dirichlet uniqueness yields `u=v`, even when the density vanishes.
The chapter supplies this final mass argument rather than silently
assuming that the maximal solution must be distinct.

For the convex local class `T0` of bounded zero-boundary psh potentials
with ordinary mass at most one, assume a uniform bound
`integral exp(-beta h) f <= A`, `A>=1`. The actual formula on source page
6 in the first estimate of Theorem 2.6 writes the denominator at `beta/2`
instead of the equation's parameter `gamma`. This replacement is not
used. Keep `Z_gamma>=1` and, since `gamma<=beta/2` and `u<=0`, calculate

`integral exp(-beta h/2) MA(u)
 <= integral exp(-beta(h+u)/2) f <= A`.

The last inequality uses `(h+u)/2 in T0`, since `u` has mass one.
The imported Theorem 2.5 then gives
`||u||<=2 n A^(1/n)/beta`; the criterion applies for
`0<gamma<beta/(2 A^(1/n))`. This is the source's sufficient range,
with the intermediate denominator estimate written correctly. It is an
identified direct formal calculation, with no original-result or
theorem-counterexample claim. The source's proof of Theorem 1.2 on page 6
obtains the exponential bound by the local mass-one volume estimate and
Hölder; the resulting constants depend on dimension, `p`, the density
norm and the domain diameter. No sharp threshold or all-parameter radial
symmetry conclusion is imported.

For the fixed-current local conversion take `u_s=u_b/2`,
`gamma_s=2 gamma_b` and `beta_s=2 beta_b`. Currents, exponential weights
and mass-one classes coincide. The product `gamma ||u||` is invariant;
both the a priori potential bound and the parameter range scale
consistently. This is not a local singular-klt extension or an
identification with non-pluripolar products that discard pole mass.

### Excluded compact stability proof

On actual page 9 of the acquired Lu–Phung file, the first step of Theorem
3.2 selects one of two sets by `omega^n`-volume at most one half. Its next
auxiliary equation uses `2 1_E f omega^n+b omega^n` and needs
`integral_E f omega^n<=1/2` to ensure `b>=0`. The two measures are
different for a general density. This compact proof is excluded from
the present import; the active book's preceding big-class stability
uses its separately audited extrapolated-envelope argument and checked
DDL contact inputs. No counterexample to the compact stability theorem
is claimed. The local criterion and projective calculation do not use
this step.

## Uniform-estimate follow-up: complete reading, no import

Dang–Zhang–Zhou, *Uniform estimates for complex Monge–Ampère equations:
Big cohomology classes*, [arXiv:2608.19600v1](https://arxiv.org/abs/2608.19600v1),
submitted 20 August 2026, manuscript dated 21 August, was separately read
in full, including references: Python `splitlines` ranges 1–230,
231–465, 466–730, 731–985 and 986–1308. All 22 actual pages were
displayed and inspected. Its 281,592-byte PDF has SHA-256
`f3d33679ea3eba2c8ca19ae0076fe0262216fc17d1d0ef82b6c89978431349e8`.
The paper remains research-only in this checkpoint. In particular:

- On actual page 6, division by the ambient big-class volume gives a
  probability measure only for full-mass potentials. The assertion for
  every psh potential is not used. An arbitrary obstacle being finite on
  a non-pluripolar set does not by itself supply a psh minorant.
- Condition (K) on page 9 must be interpreted as a high-value growth
  condition. The literal identity with `h>1` down to zero conflicts with
  the displayed Young-function limit `w(t)/t -> 0`. Low-value modification
  and density rescaling must be explicit. Orlicz membership supplies
  `integral w(epsilon f)<infinity`, not necessarily `integral w(f)` as
  used in the auxiliary normalizer on pages 14–15.
- Lemma 3.2 on pages 10–11 uses a finite `r`-moment and asserts that its
  envelope has minimal singularities before a bound for the original
  relative potential is established. Its cutoff at `C_Lambda`, contact
  set and the domain of the concave composition require a separate
  truncation audit. The general full-mass lemma is not imported.
- The relative equation in Theorem 3.12 on page 17 uses ambient volume
  in the operator, while a positive-mass model type may have smaller
  total mass. If that mass is `M_phi`, the displayed ambient-normalized
  left-hand side integrates to `M_phi/V`, rather than one. No relative
  solvability statement with those unreconciled units is copied.
- The proof of Theorem 4.1 on page 17 initially writes the measure of
  an arbitrary finite-energy potential as a smooth-volume density; an
  approximation step is needed for a general measure. The statement of
  Theorem 4.2 and its proof on pages 18–20 need tracked dependence on the
  entropy bound, Orlicz normalization and arbitrary exponent `N`. No
  unverified uniformity or improved energy theorem is admitted.

These are specific proof and normalization checks, not a claim that the
paper's principal known Orlicz estimate or every theorem is false.
BEGZ's already acquired version 2 Remark 4.6 points to an Orlicz
extension, but this checkpoint makes no new claim about which weight
classes have been independently cleared from that brief remark alone.
The explicit minimal-singularity hypothesis in the preceding logarithmic
continuity subsection remains intact. The 37 new actual primary page
views are recorded in the follow-up contact-sheet manifest, with 15
admitted-source pages and 22 research-only pages.

## Preserved boundaries

All 42 complete problem statuses, the native 86-page catalogue, earlier
formal theorem/proof blocks and the general Siu/envelope/quantization
scope remain unchanged. In particular Boucksom–Jonsson Theorem 6.21's
proof issue is not a theorem counterexample or a repaired general Siu
decomposition. The singular local Guedj–Trusiani comparison remains
pending. No initial spectral pushforward or minimizing-direction
convergence follows from these local estimates.

## Final cloud verification

The final build has 4,315 physical pages, 12,680 unique labels and 327
cited references. All 425 active TeX inputs are present. The 108 protected
inputs, 46 old formal environments/proofs in the two edited sources,
all 42 complete problem statuses, prior frozen releases and both native
catalogue files retain their prior bytes. The six new equation tags are
68.23s–68.23x. Bibliography, index and PDF navigation checks pass with
zero invalid destinations. There are no TeX errors, unresolved references,
missing glyphs, package/PDF warnings, rerun requests or overfull boxes;
954 underfull boxes remain.

Three intermediate index builds had a 0.55237pt overfull final column.
Removing the two optional new index subentries restores the existing
743-entry index without changing mathematical text or existing entries.
Twenty pages of the matching final PDF were displayed and inspected,
including the new main/provenance content, its transitions, contents,
index endpoints, new bibliography entry and final page. The review PDF
contains exactly those pages. This is a scoped release review, not a
fresh whole-book rereading. The complete active source closure and all
archive members are byte checked; no isolated archive compilation is
claimed. Artifact hashes are recorded in the matching integration manifest
and artifact record.

The next research dependency reading has also progressed, without another
book import: Di Nezza–Trapani–Trusiani's published SIGMA 20 (2024), 039
text (1,217 extracted lines) and Guedj–Lu arXiv:2502.02313v2 (807 lines)
were read in full, including references; all 19 and 14 actual pages were
inspected. These 33 research-only views are separate from the 37 Lu–Phung
and uniform-estimate views above. Berman–Berndtsson's published local
mean-field section has only been read selectively (lines 2,236–2,370),
with no complete reading or actual-page review claimed. Continue checking
relative normalized entropy/energy, the primary condition (K), and current
literature on the sources' dated questions before admitting further material.
