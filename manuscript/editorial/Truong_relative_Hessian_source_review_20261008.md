# Relative Hessian boundary and mass audit, 8 October 2026

The controlling source is Truong Dinh Dat, *Relative Finite Energy Classes for Complex Hessian Equations with Prescribed Singularities*, arXiv:2609.12032v1, posted 10 September 2026 at 16:48:01 UTC. The exact 26-page PDF has SHA256 `9b7d92cf183b7e378f44cb57859eb766c23388f217496914d6135496562cf534`; its full extracted text has SHA256 `c19f4158dc0cec14359b1dad18286815b9e4d915efc181b17ed4c9e9fb6d0569`. Every physical page, including the complete bibliography, was read in order through complete selected text and thirteen individually displayed matching images, with thirteen sequential notes and receipts. The actual-reading ledger has SHA256 `b6cf6d16b2e984264ea7dd2e3d56485393ad8aad38d373500e07be79d4ef5ea6`. Preparation flags remain false and provide zero reading credit.

The extractor's font-type mismatch warning remains recorded. All displayed image/text pairs were readable; no content loss was detected in this inspection. An earlier truncated display of view 08 was not credited: its image was displayed again before its receipt. This is not an automated font-integrity certificate or an independent model receipt. No later or journal edition was read, and no external bibliography proof was recursively certified.

## Literal definitions and smooth comparison

Definitions 2.4–2.5 on physical pages 7–8 impose a bounded difference below the reference and finite global Hessian mass on each basic approximant, followed by a decreasing sequence with uniformly bounded absolute signed energy. They impose **no boundary trace**. Sections 3–5 assume a negative reference with analytic singularities. Smooth references are allowed. Section 6 on page 20 instead writes a class defined by an upper bound and finite signed energy; equivalence of these two definitions is not established.

Use precisely the source's normalization, $d^c=i(\bar\partial-\partial)/(2\pi)$, $dd^c=i\partial\bar\partial/\pi$. On the unit disk, write $s=|z|^2$, $\beta=dd^cs$, and $\psi=s-2$. Then $\int\beta=2$. The smooth negative functions

\[
u=-3,\qquad v=\psi-1=s-3,\qquad w=\psi-2=s-4
\]

are all in the written basic class. Their reference differences lie respectively in $[-2,-1]$, $\{-1\}$, and $\{-2\}$. Their Hessian measures are $0,\beta,\beta$, and their signed relative energies are $-3/2,-2,-4$. The strictly decreasing sequences $u+1/j,v+1/j,w+1/j$ also lie in the basic class and have uniformly bounded energies, so class membership does not rely on allowing a stationary sequence.

On $\{u<v\}=D\setminus\{0\}$, the claimed comparison inequality is $2\leq0$. This contradicts the literal introductory Theorem 1.3 and Theorem 5.1. Corollary 5.2's domination premise is vacuous for $H(u)=0$, but $u<v$ off the origin. Corollary 5.3's injectivity fails because $v\ne w$ have the same nonzero Hessian. Its proof infers zero measure from equality of two integrals, although their equal value may be positive. The same pair gives a literal Theorem 7.2 stability counterexample: take every $u_j=w$, target $u=v$, and every $\mu_j=\mu=\beta$. Uniform energy and identical measures hold while $u_j-u=-1$. Since $\beta=(2/\pi)dV$ is an $L^\infty$ density, Theorem 7.3's unnormalized uniqueness is false too. No claim is made that this density satisfies Theorem 6.1's separate measure hypothesis.

The traces here are $u=-3,v=-2,w=-3,\psi=-1$. The missing boundary hypothesis is concrete. These computations do not contradict a correctly normalized Dirichlet comparison or uniqueness theorem. Even an ordering assertion for the signed energy requires its own boundary premises: $u\leq v$ but $E(u)>E(v)$.

## Global integration by parts

On the unit ball in $\mathbf C^2$, set $m=n=2$, $\psi=|z|^2-2$, $u=\psi-1$, $v=\psi-2$, and $w_1=\psi$. All products are ordinary smooth products and all functions have finite mass and energy. Since $u-v=1$, Theorem 3.11's printed left integral is $\int\beta^2=4$; its right integral contains $dd^c1=0$ and is zero. The discarded Stokes boundary term supplies the difference. Physical page 13 explicitly asserts vanishing relative boundary values that are absent from the definitions. This diagnosis does not dispute compactly supported local integration by parts.

## Finite relative energy does not bound global mass

An additional test keeps a common relative boundary trace. On the same disk and with the same strictly subharmonic reference, let $\alpha=3/4$ and

\[
h_\epsilon$s$=-$1-s+\epsilon$^\alpha+\epsilon^\alpha,
\qquad u_\epsilon=\psi+h_\epsilon,
\qquad \epsilon_j=1/j.
\]

The functions are smooth up to the boundary for positive epsilon, satisfy $-1\leq h_\epsilon\leq0$ and $h_\epsilon(1)=0$, and decrease with decreasing epsilon. Positivity of $h_\epsilon'$ and $h_\epsilon''$ proves subharmonicity. Radial integration gives

\[
\int_D H_1$u_\epsilon$=2+\frac32\epsilon^{-1/4},
\qquad
E_\psi$u_\epsilon$=2\int_0^1h_\epsilon$s$\,ds
-\alpha^2\int_0^1s$1-s+\epsilon$^{2\alpha-2}\,ds.
\]

The absolute reference term is at most 2 and the gradient term at most $3/4$. Hence the absolute signed energies are uniformly at most $11/4$, with exact limit $-53/28$, although the total masses tend to infinity. The limit $u=\psi-(1-|z|^2)^{3/4}$ is smooth inside the disk, has locally finite Hessian and infinite total mass, and belongs to Definition 2.5 via these approximants. Every integer canonical truncation $\max(u,\psi-k)$, $k\geq1$, equals $u$, which is not in the basic finite-global-mass class. Thus Lemma 3.6's canonical membership claim fails under its literal definitions **even with a common boundary trace**. The example also disproves the energy-to-global-mass inference used in the product construction. It does not refute local one-factor distributional continuity.

The exact diagnostic ledger has SHA256 `7ec956bea0aefbc0d70b55c17cf46bff4aee5d88ed1ec7a2ed4b2820ba605de8`. The first helper failed a SymPy direct boundary-limit assertion because it returned an unresolved complex fractional-power branch. The failed helper and its record are frozen. Version 2 substitutes $s=1-\epsilon$, $\epsilon>0$, before the one-sided limit and returns positive infinity; all identities and finite sample checks pass. These are reproducible elementary calculations, not a certificate of general Hessian theory.

## Measure hypotheses and remaining proof gates

For any smooth reference with finite positive Hessian mass $M$, the test $\phi=\psi-C$, $C>0$, has signed energy $-CM$. Theorem 6.1(ii) would require $C\mu(\Omega)\leq A(CM)^{m/(m+1)}$ for **every** $C>0$, forcing $\mu(\Omega)=0$. On the chosen disk $M=2$. Thus that unnormalized hypothesis cannot support nonzero data in this smooth case. Section 6 also allows positive signed energy, making the fractional power of $-E$ undefined over the reals already for $m=1$. No general repaired existence theorem is inferred from this scaling calculation.

Separate unresolved proof obligations include defining mixed products at the poles of a relatively bounded reference, controlling weighted tails and changing test coefficients, deriving restricted-measure limits on moving sublevel sets, transferring the assumption on $\mu$ to its smooth approximations, and applying decreasing continuity to mere $L^1_{\rm loc}$ subsequences. Uniform mass plus Lebesgue $L^1$ convergence does not by itself justify testing varying measures by unbounded coefficients. Class membership alone also does not give the uniformly bounded difference asserted in Theorem 7.4. These are proof qualifications, distinct from the explicit statement counterexamples above.

## Integration and preservation

The useful addition is a local boundary/normalization warning adjacent to Chapter 51's existing family-normalization discussion, with the worked smooth and radial tests in new L.94. It will preserve the compact manifold setting of the preceding mass theorem, specify the local-domain normalization separately, and import **none** of this preprint's general theorems. The diagnostic calculations add no original general theorem or independent gpt-6.1-sol xhigh receipt.

At this source checkpoint the active validated book remains the 4,636-page edition, SHA256 `4178a551f52b71e59f1f8bfd87b7ecf8c339970f3d823a1abadd8fae7f592f70`. All 425 active TeX inputs, both bibliographies and the native catalogue source/PDF are preserved. The last complete ordered book pass remains 4 October. The 42 canonical atoms and twelve formal problems retain their statuses: general BJ22 critical homogeneous Siu division/envelopes OPEN, LPWZ density UNVERIFIED. Complete source PDF/text/images stay in the cloud; authored audit notes, receipts, records and helpers are authorized for GitHub upload. Export and upload add zero reading credit.
