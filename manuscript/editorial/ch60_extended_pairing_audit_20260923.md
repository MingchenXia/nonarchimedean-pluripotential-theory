# Chapter 60: extended pairings and finite-energy measures

Date: 23 September 2026.
Baseline: `ab6a6578dd34e507e6c0459b89562f3bfd56d382`.
Scope: the extended-pairing definition through the finite-energy measure
construction in Section 60.4 of `parts/part5/ch60_mp_psh.tex`.
All earlier text and the entire text from the radial-limit section onward
retain their baseline bytes. This unit supplies proofs of established
finite-energy assertions; no research atom is retired.

## Mathematics and dependencies

The majorant infimum is nonempty by the already proved approximation by H.
Agreement with real model intersection numbers is proved before their use
in the extension. Monotonicity is immediate from the majorant sets.
For upper semicontinuity, choose a tuple of model majorants whose pairing
is strictly below a proposed real upper bound. A small rational translation
in every slot preserves that strict bound: its exact increment is epsilon
times the sum of the mixed background volumes. Obstacle-supremum continuity
then gives an open neighborhood dominated by those translated models.
The proof includes an original pairing equal to minus infinity.

Monotonicity and upper semicontinuity prove continuity along decreasing
nets. Finite product directed sets accommodate independent approximations
in the different slots. The real translation identity follows from model
approximation, one-fibre testing and the vanishing of terms with two fibre
factors. Its right side is a finite translation even when the pairing is
minus infinity; it does not subtract two infinite pairings.

The extension agrees with the earlier energy on real model psh functions.
Testing the zero-potential measure proves that the first term of J is the
finite value at the trivial valuation. Translation, J>=0, upper
semicontinuity of E and lower semicontinuity of J follow. Dimension zero
is stated separately.

`prop:mp-mixed-energy-finite` proves an explicit lower bound. Put m=n+1,
beta=sum_i alpha_i, and choose an integer T>=1 such that T alpha_i-beta
is nef for every i. This choice depends only on the fixed Kähler classes.
For nonpositive model potentials:

1. Replacing each background alpha_i by beta decreases the mixed pairing,
   as the change has a nef zero-potential factor and nonpositive remaining
   potentials.
2. Every degree-m mixed monomial in B_i=(beta,phi_i) is nonpositive.
   Expansion gives product_i B_i >= (sum_i B_i)^m/m!. Concavity bounds
   the latter below by m^(m-1)/m! times sum_i (beta,phi_i)^m.
3. The zero-potential telescoping identity, testing against a nonpositive
   potential, and nef background comparison give
   (beta,u)^m >= (T alpha_i,u)^m >= T^n (alpha_i,u)^m.

The resulting constant is m^(m-1)T^n/m!, independent of the representing
model and potentials. It is the constant from this calculation, not the
literal t^(n^2) bound of the cited source. The argument is an application
of the established model intersection calculus and concavity, not a claim
of a new research theorem.

For general nonpositive potentials, their decreasing model approximants
are eventually <=epsilon because their suprema are their values at the
trivial valuation. Apply the model inequality after subtracting this fixed
epsilon, and pass along the product directed set. If any diagonal energy
is minus infinity the lower bound is vacuous. Otherwise the finite lower
bound establishes finiteness of the shifted mixed pairing, and the real
translation identity permits epsilon to tend to zero. Translating finite
suprema then proves mixed finiteness for arbitrary finite-energy inputs.
No varying normalization is assumed to preserve monotonicity.

The twisted and PL test pairings now cite this proved finiteness before
taking differences. The PL construction explicitly permits a further
smooth domination carrying a relatively Kähler vertical divisor, and
chooses one integer N for all central components. Its independence of the
auxiliary divisor, N and approximation is proved by a common model limit.
The positive, norm-bounded PL test functional extends to C0 and Riesz
representation gives the unique Radon probability measure. The preserved
uniform-density estimate proves weak convergence for decreasing model nets.

The new P1 example has u_j=-min{v(I_p),j}, MA(u_j)=delta_(j ord_p) and
E(u_j)=-j/2. Its limit has infinite negative energy, although its model
measures converge to the supported endpoint mass. The ideal-coordinate
proof includes order zero, positive order, and the zero ideal. This example
does not extend the finite-energy construction to all psh functions.

## Sources

The exact Mesquita-Piccione source remains the
[18 September 2025 author version](https://arxiv.org/html/2409.06221v2).
Section 4.4 was read, and printed pages 42–43 were rendered and inspected:
Lemma 4.4.1, Proposition 4.4.4, Definition 4.4.6 and Remark 4.4.8 support
the corresponding assertions. The book proves the lower bound on models
and passes by nets, rather than silently assuming sequential approximation.
PDF SHA-256:
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.

The published [Boucksom–Jonsson article](https://afst.centre-mersenne.org/articles/10.5802/afst.1705/)
was checked at Theorem 7.1, pp. 747–748, Lemma 7.9, p. 752, and Corollary
7.11, p. 753. These are cited as algebraic arguments that are reconstructed
on the analytic models, not as statements directly covering transcendental
Kähler classes. Printed pages 752–753 were rendered and inspected; the
theorem on pp. 747–748 was checked in the published PDF text. The publisher
record agrees with the existing BJ22 entry. No bibliography entry changed.
PDF SHA-256:
`50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.

## Two passes and validation

The first full build produced 3,977 pages (18,930,954 bytes). Physical
pages 3360–3365 were rendered and inspected; one 5.04pt horizontal overflow
in the new curve example was found. The second full mathematical, source,
notation and prose pass checked the signs in both background comparisons,
the m! expansion coefficient, all finite/infinite limit cases, the product
directed set, zero-dimensional conventions and test-pairing independence.
It added the published comparison locators, clarified the choice of T and
the common psh background, expanded the endpoint coordinate calculation,
and displayed the example's defining formula to remove the overflow.
The final full build and review of physical pages 3360–3366 followed.
This was a scoped page review, not an all-page visual audit.

- Full build: PASS, **3,979 pages, 18,933,419 bytes**.
- Reference/input audit: **390 TeX files, 11,630 unique labels**; no missing
  input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply-defined label,
  rerun request or horizontal/vertical overflow. Existing class/underfull
  warnings remain.
- Scoped strict house audit: zero errors and one reviewed exact-author-version
  arXiv warning; strict mode returns 1, not a warning-free strict pass.
- Inventory: PASS, **45 active atoms / 14 formal environments**, tiers
  **(0,5,8,15,17)**.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`3ebe68c0d58fcb7a712230a7379c8c48804137b017ddf834b396888a139ac3e3`.
Final live PDF SHA-256:
`f9ebb9f354bca65d65d3eee7d5cbd3db7e129b735be3d9f9d8a7490085b0357e`.

The P12.1 fragment retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
P12.2–P12.6, supplied sources, bibliography, historical records, frozen
packets, verifier receipts and dated releases are unchanged. No new
independent-agent or production-verifier pass is claimed. The PDF remains
the ignored live build product. The overall audit continues with the
radial-limit construction and the exact complex-ray source inputs.
