# Pointwise minima and nonpluripolar mass: known-formula audit

Date: 5 October 2026. Baseline work commit:
`768013b67c97cace72bd82202a5a898505b85b3b`.

Admission scope: ordinary import and **explicit direct formal consequence
of a named-source formula**, as distinguished by the opening paragraph of
`rethlas_verification_protocol.md`. No priority or new production-verifier
receipt is claimed. This is a new source comparison and integration, not
an alteration of the frozen relative-truncation research draft.

## 1. What the literature comparison establishes

Błocki, *Equilibrium measure of a product subset of C^n*, Proceedings of
the American Mathematical Society 128(12) (2000), 3595–3599, proves a
formula for powers of the maximum of two locally bounded psh functions
in Theorem 4, printed pages 3596–3597. The author-hosted file has the
published journal masthead, pagination and copyright. It was acquired
from https://gamma.im.uj.edu.pl/~blocki/publ/eqpr.pdf, read in full
(252 extracted Python splitlines), and all five actual pages were viewed.
The theorem does not assume a psh minimum or continuity of the two
potentials: local boundedness is its stated regularity hypothesis.

PDF: 5 pages, 130,352 bytes, SHA-256
`80995141cf3245d2fcb8192918ae4d03bcf5a81cb9825309c958216b0a52907c`.
The AMS web/DOI metadata openings were inaccessible through the web tool;
no additional DOI was admitted on that basis. The inspected published
masthead and author publication page control the bibliography entry.

Alesker, *Valuations on convex functions and convex sets and
Monge–Ampere operators*, explicitly arXiv:1703.08778v2, 2 April 2017,
Section 3.1, actual page 11, attributes the valuation property on
continuous psh functions to that Błocki paper. Its reference [8], actual
page 18, independently identifies the paper. Theorem 2.3 in Alesker is
stated for real convex functions, and is not cited as a complex theorem.
Selected ranges 1–140, 186–270, 401–470 and 700–756 were read; actual
pages 1, 3, 6, 10, 11 and 18 were viewed. No full reading of that
19-page paper or identity with its later published file is claimed.

PDF: 19 pages, 176,907 bytes, SHA-256
`051967d6dc021e22dcce52f8c49537ca23d259d85d9ce842c8d38325f2ed3cf8`.

This primary evidence identifies the bounded valuation identity as
known. The singular passage below is a direct use of the defining
nonpluripolar truncation and locality, with its hypotheses written out.
The earlier web searches alone are not evidence of priority, novelty,
or the absence of a more explicit formulation elsewhere.

## 2. Exact scope and bounded calculation

Let X be a compact connected complex Kähler manifold of dimension
n >= 1, and let theta be a smooth closed real (1,1)-form. Let A and B
be theta-psh potentials, with the **pointwise** minimum C=min(A,B)
also theta-psh; b=max(A,B) is theta-psh. The known-formula consequence is

    MA_theta(A) + MA_theta(B) = MA_theta(C) + MA_theta(b).

All products here are nonpluripolar. Existence of these potentials
implies that the class is pseudoeffective. A big class, positive mass,
full mass, p-energy, projectivity, analytic singularities or small
unbounded locus is not an added hypothesis of the equality. Compact
Kähler is retained for the global well-defined finite products. The
local derivation is on complex coordinate charts, and supplies no
non-Archimedean analogue, line-extension theorem, or statement in a
different characteristic category.

For locally bounded psh u,v,c=min(u,v),w=max(u,v), write
U=ddc u, V=ddc v, C0=ddc c, W=ddc w. The degree-two case of Błocki's
Theorem 4 is exactly

    W^2 = W (U+V) - UV.

Since c+w=u+v, one has C0+W=U+V. Hence C0 W=UV. The two pairs have
the same first power sum and product. Their power sums satisfy the
same Newton recurrence

    S_j=(U+V) S_(j-1) - UV S_(j-2),  S_0=2, S_1=U+V,

so C0^j+W^j=U^j+V^j through degree n. In dimension one the identity
is just the linear current equality. Every mixed product in this
argument is a bounded Bedford–Taylor product. Wedging an equality
of the closed mixed currents with ddc f for bounded psh f means
applying the linear recursive operation ddc(f T). Thus no undefined
product of arbitrary distributions or unbounded-potential current
is being used to multiply the degree-two identity.

## 3. Singular passage and measurability audit

On a relatively compact chart choose a smooth local potential rho of
theta. The local psh functions u=A+rho, v=B+rho, c=C+rho and w=b+rho
have the same pointwise minimum/maximum relations. For integer k >= 1
set u_k=max(u,-k), v_k=max(v,-k). Their minimum is

    min(u_k,v_k)=max(c,-k),

which is psh because c is psh; their maximum is max(w,-k). All are
locally bounded. Apply the bounded formula to these four cutoffs.
On the plurifine open set {c>-k}, all four cutoffs agree with their
original potentials. BEGZ's nonpluripolar construction and plurifine
locality transfer the identity to that set. Its increasing union is
{c>-infinity}. Each of the four original measures gives the
complementary pluripolar set zero mass, including the measure of w
even if w is finite at some poles of c. Ordinary countable continuity
of measures therefore proves the equality on the whole chart.
The identities agree on overlaps and give the global equality.

This does not claim convergence of the complete cutoff measures.
There is no subtraction of infinite potential values, no uncountable
intersection of contact sets, no derivative of an energy functional,
and no general Siu decomposition or envelope repair in this argument.

The BEGZ dependency is the previously cached arXiv:0812.3674v2,
9 September 2010, 54 pages, SHA-256
`43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd`.
Definition 1.1, Proposition 1.4's locality item, and Proposition 1.6
were already selected and actually inspected for the frozen research
draft. That record is reused without overwriting it or claiming a
new full reading. The capacity definition, equation (4.3), was newly
checked at Python splitlines 1936–2006 and actual page 40. For theta
Kähler, its V_theta=0 formula is exactly the capacity used in the
new section. No identity with an uninspected published BEGZ file is
asserted by this checkpoint.

If A or B is identically minus infinity, handle it separately with
mass zero for that potential and its minimum. The maximum is the
other potential and the mass identity is tautological. A current of
an identically minus-infinity function is never defined. If both A
and B are nontrivial psh functions on a connected manifold, their
minimum cannot be identically minus infinity: their two polar sets
do not cover X.

## 4. Relation to the frozen research draft and complete lines

The earlier research proof using max(h,b-k) remains byte-for-byte
preserved, with no production review or promotion retroactively
ascribed to it. General singularity-type invariance would also allow
its cutoff masses to be m(b), rather than only the class volume.
The known local formula gives a more direct equality of measures,
so the book uses that explicit known-formula route.

For a sublinear complex Kähler subgeodesic line, the controlling
published Darvas–McCleerey Proposition 3.3 and Lemma 3.4 give

    A_tau = sup_(sigma >= tau) psi_sigma,
    B_tau = sup_(sigma <= tau) psi_sigma,
    max(A_tau,B_tau)=u_0.

Pointwise concavity gives min(A_tau,B_tau)=psi_tau. If both tails
were above psi_tau at a point, choose a finite larger value on
each side of tau; the concavity inequality at their convex
combination contradicts the assumed value, including when it is
minus infinity. These are raw pointwise identities from the source,
not envelopes silently regularized in the proof. The source ensures
that each tail is psh or identically minus infinity.

The direct known-formula consequence therefore gives

    m(A_tau)+m(B_tau)=m(psi_tau)+m(u_0)

for every tau. Full mass of u_0 gives the +V expression asked about
on actual published page 16 after equation (20). This is presented
as an application of the known formula, with no priority claim or
new original theorem heading. It is not an active catalogue atom.
For a collapsed vertical line u_t=a+ct, the three duals equal a at
tau=c, giving 2V=V+V. Omitting the all-time dual term is still
incorrect at that slope. The local theta-class calculation does
not extend the source's line correspondence to merely big classes.

The 25-page published Darvas–McCleerey source and its full reading
are reused from the preceding integration; no fresh complete reading
or identification with its selected arXiv version is recorded here.

## 5. General rooftops and version numbers

Darvas–Di Nezza–Lu, *The metric geometry of singularity types*,
explicitly arXiv:1909.00839v1, 2 September 2019, gives the general
volume-diamond inequality in Theorem 1.2 and Theorem 5.4. Theorem 1.3
in that version concerns multiplier ideals. Its Remark 5.5 supplies
the curve equality and a strict projective-plane example. Selected
text was read, and actual pages 1, 5, 19, 20, 21 and 22 were viewed.
The author publication page verifies J. Reine Angew. Math. 771 (2021),
137–170; the publisher PDF request returned HTTP 202 with an empty
HTML response. No published PDF was acquired and no numbered
preprint locator is identified with a published locator.

PDF: 27 pages, 369,429 bytes, SHA-256
`68ac421684f6c46705e4e875887b0cd40f997fbcfad29efd11a55415570b0a36`.
The new active citation to DDNLmetric is unnumbered. Appendix L
identifies the preprint anchors separately. The old bibliography
entry's metadata is unchanged.

For the source's two isolated-pole potentials on P2, both masses
are zero, their rooftop is nontrivial and has mass zero, and their
maximum is bounded and has mass one in the unit-volume convention.
Their minimum is not psh. At z1=a != 0 and Re(z2)=1/2, the minimum
switches between log(|a|^2+|z2|^2) and log(|a|^2+|z2-1|^2).
The normal derivative jumps down across that interface, producing
a negative singular Laplacian measure on the complex slice.
Subtracting a smooth rho cannot cancel that negative interface
measure. This explains why the strict rooftop example is consistent
with the pointwise-minimum identity.

## 6. The 2025 capacity comparison

Dang–Do–Pham, *Singularities vs non-pluripolar Monge–Ampère masses*,
explicitly arXiv:2503.07534v1, submitted 10 March 2025, is the
controlling source for the new capacity comparison. All 555
extracted Python splitlines, including references, were read;
actual pages 1–7 were inspected.

PDF: 9 pages, 149,607 bytes, SHA-256
`51e158d9efeb4e52a9564cb3fae2b52e2a092d7913eca76fd77349afe8de1f8a`.
The primary publisher page confirms Mathematische Zeitschrift 311,
article 47 (2025), published 4 September 2025, DOI
10.1007/s00209-025-03844-1. Its PDF request redirected to an HTML
article page with HTTP 200, not a PDF. No published full text was
read or equated with the preprint.

Theorem 1.2 compares mixed nonpluripolar masses of n potentials in
pseudoeffective classes under the quantitative capacity tail condition
k^n Cap_omega({varphi_j < chi_j + a h - k}) -> 0, with a common
h in E(X,omega) and a >= 0. The inequality direction, mixed-product
degree and common perturbation are retained. The book distinguishes
this singularity comparison from ordinary convergence in capacity.

The capacity displayed on actual preprint page 2 integrates over X,
without the tested set. Read literally it is independent of E and
cannot be a capacity. The new section uses the standard integral over
E, independently attested by BEGZ equation (4.3), and does not import
that literal display. The proof on page 5 invokes locality on a
nonstrict contact set; its required inequality follows from the
paper's Lemma 2.2, rather than locality on a non-open set. Neither
that literal justification nor an equality on a nonstrict set is
used as a proof input here. The a=0 case in the comparison proof
can take h=0 and a positive auxiliary coefficient, avoiding the
printed divisions by a; the theorem's a=0 signature is retained.

## 7. Zero-reference-mass diagnostic, outside active TeX

The preprint's Theorem 1.1 states its comparison for an arbitrary
reference phi in a big class, without requiring m(phi)>0. Its
Proposition 2.5 proof explicitly describes only an arbitrary reference
of **positive** mass. The unrestricted zero-mass statement and the
same unrestricted implication in Corollary 3.3 are excluded from the
book. The following diagnostic tests exactly that omitted boundary;
it is not a claim about the unacquired published theorem.

On P2 let omega be the unit Fubini–Study form, with homogeneous
coordinates [Z0:Z1:Z2], and put

    phi = log((|Z1|^2+|Z2|^2)/(|Z0|^2+|Z1|^2+|Z2|^2)),
    psi = log(|Z1|^2/(|Z0|^2+|Z1|^2+|Z2|^2)).

Both are omega-psh and psi <= phi. Away from p=[1:0:0], the
curvature of phi is the pullback of the Fubini–Study form on P1
by [Z1:Z2], hence has rank one and square zero. Its pole at p is
pluripolar, so its nonpluripolar mass is zero. The curvature of psi
is the divisor [Z1=0], whose nonpluripolar top measure is zero.
Thus both belong to the set E(X,omega,phi) if relative full mass
is defined merely by singularity order and equal zero masses.

At a generic point of D={Z1=0} away from p, phi is smooth, whereas
psi has a logarithmic pole. The bound |phi-psi| <= -a h, for a>0,
would force a positive divisorial Lelong number for h. A Kähler
full-mass h has zero Lelong numbers, so no h in E(X,omega) can
satisfy it. Equivalently, for any coefficient b>0, a psh envelope
below b(psi-phi) cannot have full mass: it must have a positive
generic Lelong number along D, or be identically minus infinity.
All potential differences are considered away from their poles;
the contradiction uses an ordinary punctured neighborhood of a
generic point of D. It does not subtract two minus-infinity values.

The same pair appears as an ordered isolated-pole/divisor pair in
the source-checked projective examples above. This diagnoses a
literal initial-version boundary, without rejecting its capacity
comparison or the positive-reference-mass results. It has no
independent production-model review, no VERIFIED receipt, no
active original counterexample heading and no effect on any of
the book's 42 problem statuses.

## 8. Preservation and validation boundary

The new section, provenance entry and three bibliography additions
are checked by the matching source, build and PDF-navigation record.
All existing formal theorem/lemma/problem/example/remark/proof blocks
in the changed TeX inputs are retained byte for byte. The catalogue
source/PDF, 108 protected inputs, all 42 complete status rows, the
frozen relative-truncation draft and earlier exported releases are
preserved. The general BJ22 closure and Siu boundaries, and the
quantization assumptions A2–A4, are unchanged.

Primary PDF inspections are recorded in the two contact-sheet
manifests and the additional BEGZ capacity-page record. Only actually
successful views count. Known-formula admission is not described
as an independent model verification of the earlier candidate.

The final cloud build has 4,294 pages, 313 cited bibliography entries,
21,563 named PDF destinations, 46,473 internal links and 2,475 outline
entries. It has no TeX errors, unresolved references, missing glyphs,
package/PDF warnings, rerun requests or overfull boxes; the 954 underfull
boxes are the same count as the preceding release. Bibliography and
index processing report no warnings or rejected entries. All numerical
index destinations and outline/internal-link targets were checked.
Sixteen actual pages of this final PDF were inspected, including both
new TOC entries, the complete new section, its boundaries, the provenance
entry and all three new references. The review extract contains those
same pages. This is a targeted release review, not another full-book
rereading. The source export is checked member by member against current
workspace bytes; a separate isolated archive compilation is not claimed.
