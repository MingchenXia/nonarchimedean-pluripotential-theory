# P05.1 universal one-vertex literal nonregularity: integration audit — 26 September 2026

## Supplied source and integration decision

The author-supplied three-page PDF is the explicitly withdrawn draft
*Orthogonality on one-dimensional balanced fans*.  The repository copy is
byte-identical to the supplied file: 252,482 bytes, SHA-256
`0ad51074108eb2202d4b624637c035610d275c67fd8456dab59282d543d5f5fb`.
Its retained positive theorem is not cited or restored.  The relevant datum
is the coefficient conflict stated in its withdrawal notice: the literal
piecewise-affine class has integral slopes, whereas the proposed envelope can
have fractional slope.

Chapter 72 now turns that warning into a separate book-local theorem.  Let
`X` be any one-vertex balanced rational fan, let the literal reference be
raywise affine with positive integral slopes `g_i`, choose a ray `j`, and fix
an integer `N>=2`.  A bounded literal obstacle supported on that ray has the
explicit envelope

```text
gamma(t u_j)-t/N   for 0<=t<=N,
gamma(t u_j)-1     for t>=N,
gamma              on every other ray.
```

Every literal integral-slope convex piecewise-affine approximant is separated
from this envelope by at least `(N-1)/(2N)` in the uniform norm.  Bounded
reference shift transfers the failure from the raywise-affine tail reference
to every positive-at-infinity literal reference on a finite rational
subdivision.  Thus no one-vertex pair in this literal category has regularity,
and none lies in the domain of the source's literal orthogonality definition,
which assumes regularity.

## Mathematical audit

The envelope computation has four independent checks.

1. Its raywise slopes are nondecreasing, and every initial slope at the
   unique vertex is positive.  Every nonnegative balancing relation therefore
   has nonnegative Jensen defect.
2. The candidate lies below the obstacle.  On the only nontrivial interval
   this is `-t/N <= N-1-t`, equivalent to `t<=N`.
3. Any competitor is bounded on the distinguished segment by the chord
   joining its endpoint bounds at `0` and `N u_j`; that chord is the candidate
   envelope.  Off the segment the obstacle itself gives the bound.
4. For a literal approximant, the left derivative at `t=1` is an integer.
   The exhaustive alternatives `m<=g_j-1` and `m>=g_j` force an error jump of
   magnitude at least `(N-1)/N`, hence a uniform error of at least half that
   amount.

The theorem does not contradict the real-piecewise-affine regularity and
orthogonality results, does not define a Monge--Ampere measure for the
nonregularizable envelope, and does not classify literal regularity on a
general finite graph or in higher dimension.  P05.1 and P05.2 therefore
remain active; the inventory stays at 42 atoms in 12 formal environments,
with tiers `(0,3,7,15,17)`.

## Source and verification boundary

The BMPS source locators are Definition 2.28, Theorem 6.4, Definition 6.5,
and Definition 6.9 of arXiv:2603.08664v1.  The official arXiv record was
rechecked on 26 September 2026 and still lists the submission of 9 March 2026
without a published-version link.  The fractional-envelope formula and the
quantitative separation estimate are proved directly in the book packet.

No model-verifier result is claimed for this theorem.  Earlier archived
gpt-6-astra receipts concern different frozen packets and do not certify this
integration.

## Release gates

- Scoped Mingchen-writing audit: zero errors and one reviewed BMPS26
  arXiv-only warning.
- Minimal packet: two pages, 133,909 bytes, clean final log; both pages were
  rendered and inspected.
- Reference graph: 415 build-closure files and 11,864 unique labels; zero
  missing inputs, duplicate labels, dangling references, or structural
  errors.  All six checker tests pass.
- Inventory: 42 active atoms in 12 environments, tiers
  `(0,3,7,15,17)`.
- Full book: 4,090 pages, 19,465,527 bytes, SHA-256
  `1aced01d8f8c57975d09a6ed9d1b8510a44d651c42a3f773213faf969f413717`.
- Full-book log: no unresolved reference or citation, rerun request, missing
  input, horizontal or vertical overflow, or fatal error.  The 13 inherited
  Chapter 70 duplicate destinations are unchanged.
- Visual audit: physical book pages 3797--3800, corresponding to printed
  pages 3729--3732, were rendered after the final build and inspected.  The
  theorem, both proofs, the coefficient-category transition, and the next
  one-vertex result have no clipping, collision, or malformed display.
