# Independent hostile audit of the P14.2 exact-live adaptation

## Binary verdict

`PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET`

The verdict is limited to the exact artifacts pinned in this dossier.  It does
not authorize or record live integration, inventory mutation, production
submission, retirement, or Git activity.

## Frozen identities

The audit independently rehashed and bound the following inputs.

- Frozen exact-live adaptation dossier: its `SHA256SUMS` has SHA-256
  `56e2084c2264dad4bb83f0d2bdd4e3348933002a6c9d9a6821ab02ae1686cdff`.
- Canonical original statement, proof, and example: respectively
  `488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949`,
  `bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21`,
  and `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f`.
- Stable independent re-audit dossier: its `SHA256SUMS` has SHA-256
  `d8efb5f13b8a34409744243dcf1aed3223f5812b2c5d13204741202e1f356a7c`;
  its own read-only checker reports `PASS_STABLE_P142_INDEPENDENT_REAUDIT`.
- Live Chapter 71 preimage:
  `27e6050d1fc1a21c48e2e03d513a87fb6f3bc249e32f648aef590f1fe674c930`.
  It remained unchanged throughout this audit.

## Exact adaptation audit

The adapted hashes are

- statement: `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2`;
- proof: `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac`;
- example: `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f`.

The example is byte-for-byte identical to the canonical example.  For the
statement and proof, a token-preserving inverse normalization was applied:

1. `X^{\bethan}` was changed back to the canonical `X^\beth`;
2. tags `71.33a`--`71.33j` were removed;
3. `\[...\]`, `equation`, and `align` display wrappers were erased;
4. align-only ampersands and row breaks, and only the punctuation immediately
   introduced when an align row became a stand-alone display, were erased;
5. whitespace was normalized.

After this transformation, adapted and canonical statement token streams are
identical, and adapted and canonical proof token streams are identical.  Thus
there is no omitted or added mathematical assertion, proof sentence, displayed
formula, hypothesis, caveat, or example text.  The ten live-style tags occur
exactly once and have the intended mapping: dense formula (a), raw transform
(b), mesh (c), finite ideal values (d), upper approximants (e), decreasing
sequence (f), exact limit (g), grid sandwich (h), usc infimum (i), and double
infimum (j).

## Mathematical audit

### Monotone-parameter lemma

For a fixed `N`, the grid covers `[c-N,c)` by `N^2` half-open intervals of
length `1/N`.  Nonnegativity controls all parameters below `c-N`.  On a grid
interval, parameter monotonicity gives

`tau-a_tau <= tau-a_left <= left-a_left+1/N`.

The finite floor makes the sampled maximum finite even when every sampled value
is minus infinity.  Hence `G_N <= F_N <= G_N+1/N`, including extended values.
The identity `F=inf_N(G_N+1/N)` follows because `F_N=max(c-N,F)` tends to `F`,
also at `F=-infinity`.  An arbitrary infimum of upper-semicontinuous functions
is upper semicontinuous since its strict sublevel set is the union of theirs.

For density, a point `s` is chosen strictly to the left of `tau`.  Then
`a_s<=a_tau`, so every finite full-supremum term is approached from below.
Minus-infinity terms impose no condition, and if all terms are minus infinity
both suprema are minus infinity.  No parameter regularity or metrizability is
silently used.

### Extended Fekete argument

Subadditivity of multiplier ideals and reversal of ideal inclusion under a
semivaluation make
`b_m=v(I(m Gamma_tau))` a nonnegative superadditive sequence in
`[0,+infinity]`.  If `b_q=+infinity`, then superadditivity applied to
`m=q+r` makes every `b_m` with `m>=q` infinite.  Otherwise division of
`m=kq+r` gives `liminf b_m/m >= b_q/q` for every `q`.  Comparison with the
defining supremum proves existence of the limit, including the case in which
all terms are finite but their normalized supremum is infinite.  No illegal
`infinity-infinity` or `0 times infinity` expression occurs.

### Topology and finite approximants

The MP tropical spectrum is equipped with pointwise convergence of ideal
evaluations into compact ordered `[0,+infinity]`.  Each evaluation is therefore
continuous.  Positive scaling, order reversal followed by finite translation,
finite minima and maxima, and truncation by the real floor are continuous in
the relevant order topologies.  The floor also gives a uniformly bounded real
function.  Supremizing the nonnegative normalized ideal evaluations is lower
semicontinuous, so the monotone-parameter lemma applies at every semivaluation,
including points with nonzero support and infinite ideal values.

The `M`-limit commutes with the finite sampled maximum.  This remains true when
the limiting terms are minus infinity: for a fixed real threshold each of the
finitely many decreasing terms is eventually below it, and one maximum of the
finitely many indices works.  Exhausting the positive integer quadrant by
finite squares proves the stated decreasing sequential limit without extracting
a sequence from an arbitrary topological net.

### Pseudoeffective inverse-system scope

Every Kähler perturbation of the unperturbed pseudoeffective class is big, and
the DXZ component is an I-model test curve with finite terminal parameter and
nontrivial interior levels.  Formula (28) and Definition 3.3 of DXZ give the
transition and the inverse system.  DX22 Proposition 2.18(ii), in the setting of
an arbitrary compact Kähler manifold with pseudoeffective background, says the
I-model envelope has exactly the same multiplier ideals for every positive real
coefficient, hence in particular for every positive integer used here.

Passing to a perturbation comparable with two chosen components therefore
identifies their coherent multiplier ideals level by level, and the terminal
parameter is common.  An equality of coherent ideals can be evaluated at every
MP semivaluation, not just a divisorial valuation.  The raw transform and every
finite approximant are consequently component-independent.  The argument never
chooses a positive-mass object in the unperturbed class, so pseudoeffective
zero-volume classes are genuinely included.  It makes none of the stronger MP
positivity, Monge--Ampère, energy, or P-equivalence assertions explicitly
disclaimed in the candidate.

### Example

Locally `psi=lambda log|z|^2+O(1)`.  A germ of order `q` is integrable against
`exp(-m psi)` exactly when `q-m lambda>-1`, equivalently
`q>=floor(m lambda)`.  Thus the multiplier ideal and both displayed transforms
are correct.  At `v(m_p)=+infinity`, every positive ideal power has infinite
value, while the finitely many exponent-zero cases are the unit ideal of value
zero; the proof does not form `0 times infinity`.

## Primary-source interfaces

The four original PDFs and their extracted snapshots were independently
rehashed.  The PDF hashes are MP24 `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`,
DXZ23 `7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c`,
DX22 `e30979bca8e63f3f3cebb9174e02042e76aaa3dda2e5e7fce1ac5afcc9bfc306`,
and DEL00 `59219defe8729b2cd8db7e05cabec3736832e3bfd5aad4ac1b58390c801337a2`.

- DEL00 Theorem 2.6(ii) supplies analytic multiplier-ideal subadditivity.
  Quasi-psh weights reduce locally to its psh statement after adding a smooth,
  hence locally bounded, summand.
- MP24 Definition 1.3.1 defines semivaluations on all locally finite-type ideal
  sheaves and equips their spectrum with pointwise convergence.
- DX22 Section 2.4 explicitly assumes a compact Kähler manifold and a
  pseudoeffective class; Proposition 2.18(ii) supplies I-equivalence of the
  envelope and its input.
- DXZ23 Section 2.2 supplies the test-curve properties; formula (28) supplies
  the transition; Definition 3.3 supplies the pseudoeffective projective limit.

The bibliography keys DEL00, MP24, DX22, and DXZ23 occur in the live bibliography
and resolve in both complete builds.

## Exact throwaway integration and collision audit

The exact concatenation `statement -> proof -> example` was inserted after the
existing perturbation-independence proof and its source paragraph, and before
the existing divisorial-inversion paragraph.  The preimage is byte-identical to
the pinned live Chapter 71.  The postimage has SHA-256
`07eff0ccc90ae68a1a706c928e1fac006f7546574d28a0f01e33e4367fc60a33`.

All fourteen imported base labels occur zero times in the live preimage and
exactly once in the postimage.  Each tag 71.33a--j occurs zero times in the live
preimage and exactly once in the postimage.  The later pre-existing numbering
resumes at 71.36.  No bibliography-key, label, tag, or Hyperref destination
collision was found.

## Full-book and visual gates

After a documented sparse-copy harness omission was repaired only in the
throwaway tree, two separate forced full-book `latexmk` commands completed with
exit code zero.  Each produced 3516 pages.  The final book auxiliary file, Ch71
auxiliary file, and BibTeX log are byte-identical across the two runs.  Both
successful TeX logs contain zero errors, undefined references, undefined
citations, multiply defined labels, duplicate destinations, missing draft
includes, or rerun-required warnings.

The imported labels resolve on printed pages 3184--3188.  Physical PDF pages
3252--3256 were rendered and inspected.  The insertion order, all displays,
tags, references, citations, extended-value symbols, and transition to the
pre-existing divisorial theorem are legible and unclipped.  See
`VISUAL_AUDIT.md` and `visual_evidence/`.

## Final conclusion

No mathematical, source-interface, exact-adaptation, collision, compilation,
or visual blocker remains for constructing a separate source-closed production
packet from these exact frozen inputs.
