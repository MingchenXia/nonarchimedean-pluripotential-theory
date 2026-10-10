# Original maximal-ray and holomorphic-extension dependencies

Date: 9 October 2026. Scope: an actual complete reading of the published
BBJ21 author offprint and a selected reading of the original Finski
metric-structure paper. This is a source checkpoint; the active
4,667-page book and the open LaTeX catalogue are unchanged.

## Controlling primary sources and actual scope

| Source | Edition and digest | Actual reading |
| --- | --- | --- |
| Berman–Boucksom–Jonsson, *A variational approach to the Yau–Tian–Donaldson conjecture* | JAMS 34 (2021), 605–652; DOI 10.1090/jams/964; author offprint SHA256 `36c3741fa0c0185099698862a29e301e139c07b56d63519369d77eb06ca4be11` | All 48 physical pages, printed 605–652, in 24 ordered individual two-page displays; complete selected text, appendices and references read. |
| Finski, *On the metric structure of section ring* | arXiv:2209.03853v2, 29 September 2022; SHA256 `51f72c62959037a8a2d7e0036c15af1182cb98a1623b88f1e217b3a7b82d87e3` | Physical 1–14 and 47–50: 18 of 50 pages in nine ordered individual displays. Physical 15–46 remain unread in this round. |

The combined checkpoint has 66 actual source/page pairs and 33 matching
views. Render preparation, acquisition, exact calculations and export
add no reading credit. The preparation manifest retains its original
false reading flags; a separate actual record pins each chronological
note, receipt, complete text and individually displayed image. Reading
the complete BBJ21 PDF does not certify every paper in its bibliography.
The Finski selection is explicitly partial even though the particular
Corollary 2.12 proof and its preceding hypotheses were read.

The BBJ21 offprint is distinct from the earlier forty-page arXiv v3
used in the Chapter 60 audit. No receipt for that version has been
reused to claim this published reading. The Finski v2 is also not
silently identified with a later 54-page author-site description or
the published 83-page semiclassical extension paper.

Acquisition helper v1 failed before directory creation or network access
because optional `requests` was unavailable. Its bytes and zero-credit
failure record are retained. Fresh v2 used the standard library and
acquired both pinned PDFs; no package installation or local execution
environment was needed. The separate metadata searches, including a
failed web-tool offprint request, are discovery records only.

## BBJ21: hypotheses, normalization and proof interfaces

The underlying projective variety is a smooth complex manifold, and L
is ample, possibly rational after denominators are cleared. The current
theta is quasi-positive and klt for the definitions and integrability
results; semipositivity is an additional assumption where Ding
convexity and the existence implications require it. Neither a singular
base nor an arbitrary non-Archimedean field is covered merely by quoting
this source. Its sequence-based regularization is an actual imported
input in this complex projective setup, not a consequence of a general
directed-model definition.

The source uses probability MA = omega_u^n/V, E(0)=0 and E(u+c)=E(u)+c.
Its L functional has the factor -1/2 in the logarithm of the integral
of exp(-2u). Psh lifts use t=-log|tau|. These conventions differ from
an unnormalized complex intersection measure and from formulas for
logarithms of squared norms. All translations must preserve the factors.

Theorem 6.2 constructs a **canonical psh extension** of the divisorial
NA values of a linear-growth ray. The dyadic decrease of multiplier-ideal
approximants includes the fixed m0 shift and the normalization phi_m<=0.
Horizontal cosupport is possible for a general psh ray: those ideal
metrics need not all be ample test-configuration metrics. The E1 case
in Theorem 6.4 supplies the stronger vertical cosupport and the energy
lower bound. This is a canonical extension assertion; it does not
identify arbitrary pointwise raw FS suprema with their usc extensions.

The proof of Theorem 6.6 retains three separate inputs:

1. The model/base case is imported from Berman16 Proposition 2.7.
2. Decreasing complex and NA data give finite energy of the limiting ray
   and its prescribed energy slope, with endpoint continuity using the
   earlier finite-energy topology results.
3. Order gives U_NA<=phi, Theorem 6.4 gives E(U_NA)>=E(phi), and ordered
   strictness from Lemma 6.3 identifies U_NA=phi. Maximality then compares
   each competitor with every approximating model ray.

Energy continuity alone does not perform step 3. Lemma 6.3 imports
finite-energy MA uniqueness/duality from the original NA sources.
Theorem 6.4 gives an inequality for an arbitrary finite-energy ray;
equality of slopes is the maximality condition in Corollary 6.7.
Example 6.10 describes a nonconstant finite-energy geodesic with zero
NA metric using cited polar-set and Darvas constructions. It therefore
does not license an equality theorem for all rays, and those cited
constructions are not independently proved by reading the example.

The stability contradiction in Theorem 5.1 is based at zero. It has
E(U_t)=ct, c<0, L(U_NA)<=c, E(phi_m)>=c and
L(phi_m)>=(1-epsilon)E(phi_m), with 0<epsilon<1. Passing to the limit
would give c>=(1-epsilon)c, which fails for negative c. The existing
Chapter 68 proof architecture keeps these signs and never assumes
equality of energy for all rays.

## Concrete printed defects and additional proof steps

The following distinctions are essential: a false literal lemma, a local
typographical error and an additional step in a cited proof are not the
same conclusion. No intended main BBJ21 theorem is declared disproved.

| Location | Observation | Consequence retained |
| --- | --- | --- |
| Proposition 1.5 proof, printed 613 | The finite/nonfinite case words are interchanged. U=0 diagnoses the literal wording. | The intended all-or-none finite-energy alternative survives the case-label correction. |
| Lemma 1.6, printed 613 | The energy fibre formula omits 1/(n+1) under the source's ordinary wedge and E conventions. For a spatially constant U=f(t), the integrated (n+1)-fold wedge equals (n+1)V dd^c f whereas E(U)=f. | Use 1/((n+1)V). The positive factor does not change convexity or the zero-curvature characterization of geodesics. |
| Theorem 2.16 proof, printed 621 | It takes T_j=d1(u_j,0) while calling a segment from an arbitrary u to u_j unit speed on [0,T_j]. Direct application of the stated sup-normalization lemma is also immediate only from zero, and subtracting F(u) requires finiteness. | The origin-zero case used in the stability contradiction is separate. General-origin bookkeeping requires d1(u_j,u), normalization and a finite base value; no full general repair is claimed here. |
| Theorem 5.4 proof, printed 629–630 | The application of B.7 writes a logarithmic numerator and an exponent without consistently retaining the scalar s and the twisted denominator V=U+psi. For s<0, s log|tau| is not quasi-psh and is outside the stated analytic-numerator theorem. The high-discrepancy estimate changes the location of the constant C in its epsilon factor. | A signed-log reduction and explicit consistent margin are additional proof steps. Simultaneously adding M log|tau| to numerator and denominator preserves integrability, but the valuative condition acquires epsilon M w(tau); that term must be controlled. No citation alone supplies the extension. |
| Lemma 6.1 proof, printed 633 | The nonzero-ideal assumption prevents the limit from being identically minus infinity; the zero ideal would give the excluded metric. | Multiplier ideals in the intended application are nonzero. |
| Theorem 6.6 proof, printed 635 | The last competitor paragraph prints U_NA where the needed inequality is V_NA<=phi_j. | The competitor premise supplies the needed V inequality. |
| Theorem 6.12 proof, printed 636 | It says Lemma 6.11 proves (ii)=>(iii), whereas the immediate implication is (iii)=>(ii). The following contradiction proves (ii)=>(i). | Correct the arrow when explaining the equivalence; do not reinterpret strict positivity as a uniform estimate without the other argument. |
| Definition 7.2, printed 637 | Earlier X_div conventions include the trivial valuation, with A=S=0. | Ratios A/S require nontrivial valuations; B.9 explicitly excludes the trivial valuation. Its role in canonical metric maxima is separate. |
| Theorem 7.5 proof, printed 639 | Ding semistability of (X,sL) yields s<=delta_theta, but the paragraph prints s<=s_theta. | The intended minimum bound needs the delta conclusion; the final statement already includes both thresholds. |
| Lemma A.1 proof, printed 639–640 | A wedge power has the wrong degree, the averaging formula requires a separate n=1 case, and the exponents are inconsistent across the page break. | These proof lines require correction; the stated estimate has separate original energy-estimate dependencies. |
| Lemma A.2, printed 640 | The statement with M depending only on I(u0), I(v0) and I(f_j) is false for arbitrary constants. | See the direct calculation below. The intended Corollary A.3 is not declared false. |
| Theorem B.5 proof, printed 646 | The analytic case prints c_V-c_U>-1. The actual L2 condition is c_V-c_U<1. The Holder step also requires k>=2. | The preceding nonnegative-coefficient uniform-margin inequality implies the correct condition. The final general step uses the stronger already established center-meeting condition (iv). |
| Theorem B.7 proof, printed 647 | Invariance of the point and hypersurface does not make arbitrary coordinate monomial valuations invariant. | Choose equivariant local coordinates by circle linearization; preserve the proper invariant-component and equivariant-modification inputs. |

For the literal Lemma A.2, take dimension two, u0=c!=0,
v0=f1=f2=0. Every I appearing in M is zero, while

    |integral (u0-v0) omega_f1 wedge omega_f2| = |c| V > 0.

The printed right side is zero. Its proof additionally bounds the
absolute mean difference by I(u0,v0), which fails for the same constants.
For example c=3/2 and V=7/3 give left side 7/2 versus zero. A replacement
estimate must control constants through a normalization or a d1/mean
term. One cannot cite the printed version unchanged. A possible repair
route combines the preceding mixed-energy estimate with Darvas's
absolute-integral comparison and d1 distances from zero; that route is
not promoted to a new lemma or independent verification receipt here.

The compactness theorem's origin-zero application and Corollary A.3
require the underlying mean-control statement. The present checkpoint
records this dependency honestly rather than declaring the main
variational theorem false or silently certifying a complete corrected
proof. A search of current book TeX found no direct citation of BBJ21
Lemma A.2 or Corollary A.3. General compactness imports are still
subject to this original-proof audit.

Appendix B is complex analytic. The Siu decomposition used in B.6
subtracts generic **classical complex** divisorial Lelong terms on a
modification. It is not the disputed homogeneous NA Theorem 6.21 in
BJ22. Conversely, this difference is not a certificate of independence
of every original NA input used by BBJ21.

## Finski: the exact extension result used by the book

Corollary 2.12 is on physical page 12 of arXiv v2. Under the preceding
smooth projective/ample/closed-submanifold setup and a continuous psh
metric h on L, it says that the restriction quotient [Hilb^X(h)] is
equivalent to Hilb^Y(h). Here equivalence means
d_infinity(N_k,N'_k)/k tends to zero. Restriction is eventually
surjective; the statement is not for every small degree.

Its actual proof has two directions. Restriction of sup norms and
Bernstein–Markov comparison give the lower bound. Theorem 2.5 gives
a fixed-constant L2 extension estimate with positive smooth volume
measures, and another Bernstein–Markov comparison gives the upper
bound. Theorem 2.5 fixes a positive reference metric and a twist p0
before varying k. Comparing the continuous metric with the reference
on this **fixed** twist costs a constant, not exp(Ck).

Theorem 2.6 is different: for smooth strictly positive h it gives the
sharper quotient ratio with k^{(n-m)/2}, using the original semiclassical
theorem [27]. Neither result extends automatically to singular bases,
arbitrary finite-energy metrics, nonclosed submanifolds or merely big L.
The later published submultiplicative proof's use of Corollary 2.12
therefore retains these exact holomorphic hypotheses.

Three local formulation issues also matter when copying formulas:

* Formula (2.20)'s admissible weights must be their actual psh
  representatives. A USC function equal to 1 at a single point and 0
  elsewhere has zero distributional dd^c, but its smooth-volume integral
  of exp(p psi) is V while its supremum is exp(p). It violates the
  advertised estimate for any epsilon<1 as p tends to infinity. The
  intended section-log weights and standard psh theorem are unaffected.
* In (2.33), rho_k is the section-length evaluation operator norm.
  Lemma 2.14 gives the squared metric ratio rho_k^{-2}, not rho_k.
  Scaling a one-dimensional norm by a=3 gives rho=1/3 and metric ratio
  9. The intended uniform logarithmic convergence survives the inverse
  and factor two.
* Lemma 2.17 needs a nonzero section and a point-extension constant
  uniform across x. The proof of (2.36) should choose a positive smooth
  measure; a measure bounded only from above need not satisfy the
  reverse Bernstein–Markov inequality. These steps are not supplied by
  allowing the zero section or an arbitrary zero measure.

The residue-measure coefficient in (2.6) must be retained or absorbed
in the fixed extension constant when (2.12) replaces that measure.
The exact neat-analytic distance-weight construction is another cited
input. These matters do not refute the intended Corollary 2.12.

The Finski MA measure has total mass c1(L)^n/n!, not one. Tensor products
also remain typed: Hermitian for Hilbert norms, projective for L1,
injective for sup norms. Multiplicatively generated norms require the
single sublinear error for all factor counts r, not only a two-factor
estimate. The introduction explicitly warns that a FS limit alone
does not determine an arbitrary graded Hermitian norm class.

## Original dependencies still to audit

The complete BBJ21 bibliography identifies exact old references:

* BoJ18a: arXiv:1801.08229v1, *Singular semipositive metrics on line
  bundles on varieties over trivially valued fields*.
* BoJ18b: arXiv:1805.11160v1, *A non-Archimedean approach to K-stability*.
* Berman16: Inventiones 203 (2016), 973–1025,
  DOI 10.1007/s00222-015-0607-7, especially Proposition 2.7.
* BFJ15 and BFJ16: the separate MA solution and singular semipositive
  metric papers, with their original field and projectivity assumptions.

The Finski original bibliography identifies [27] as arXiv:2109.06851,
[28] as arXiv:2201.04102 and [29] as arXiv:2207.02761. Its [5] is
BBWN's Acta Math. 207 (2011) paper, and [23] is Demailly's 2016
nonreduced extension chapter. Its [43] explicitly includes Ohsawa's
2001 erratum. These are exact next-stage references, not newly read
proofs. The NA comparison [10]=arXiv:2107.11221 is a different paper
from both of BBJ21's original BoJ18 references.

No verified additional BBJ21 corrigendum was established by the limited
metadata search. An aggregate search snippet mentioning a Theorem 5.6
gap did not authenticate its source and is not evidence of a BBJ21 gap.
That limitation is separate from the actual primary-page observations
above. Previously read big-polarization arXiv v1 metadata also does not
become a new revision or a new full-paper reading.

## Book integration decision and status

The existing Chapter 60 description of the limiting energy identification
is compatible with the published Theorems 6.4/6.6. Its locator still
explicitly cites the earlier arXiv v3; a future scoped edit can add the
published-version anchor without erasing that historical audit.
Chapter 68 keeps the origin-zero stability contradiction and identifies
the deep compactness/singularity imports. It should retain the additional
proof obligations above. Chapter 65's fixed-r Parseval explanation
retains its holomorphic extension input; the newly read Corollary 2.12
now supplies a precise original source for that input.

No formal theorem block, semantic label, bibliography, active PDF or
native-editor source is changed by this checkpoint. No original general
result or independent model receipt is claimed. The thirteen exact
diagnostic families are elementary calibrations, not substitutes for
the original pluripotential and extension proofs.

The canonical catalogue remains 42 atoms in twelve formal problems,
with tier counts (0,3,7,15,17). General BJ22 critical homogeneous Siu
and general envelopes stay OPEN; LPWZ density stays UNVERIFIED. The
user's warning about the proof of BJ22 Theorem 6.21 remains binding.
The native open catalogue remains in the same editor. The last complete
ordered whole-book reading remains 4 October; later book/source reads
are scoped. Next pursue the exact original NA/model and semiclassical
inputs, then integrate only cleared explanations in a staged book build
with actual rendered reading. Continue in the cloud, integrate incoming
author progress and publish checked units regularly. Xean is suspended.
