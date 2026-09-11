# BFJ zero-approximation source audit

Checked 11 September 2026 against Boucksom--Favre--Jonsson,
*Valuations and plurisubharmonic singularities*, arXiv:math/0702487v2,
Propositions 3.11, 3.13, and 3.14.  The primary PDF was downloaded from
<https://arxiv.org/pdf/math/0702487> and has SHA-256
`ed10edf37ef2a9e8feab63e03fba83f283325ea7e0b6568b3eb5af12777dcf3a`.

## Finding

The previous Chapter 70 wording strengthened BFJ Proposition 3.13 to say
that every approximating ideal is `m`-primary.  This is false for the zero
formal psh function under the standard convention that a primary ideal is
proper.

BFJ use

```text
a_k = L^2(2^k g) + m^(4^k),    c_k = 2^(-k).
```

For `g = 0`, Definition 3.6 gives `1 in L^2(0)`, hence `L^2(0) = R` and
`a_k = R`; the approximating function is exactly zero.  No sequence of
strictly negative `m`-primary ideal functions can decrease pointwise to zero.

For `g` not identically zero, BFJ Proposition 3.14 gives `max_V g < 0`.
Theorem 3.9 then forces `L^2(2^k g)` to be proper for all sufficiently large
`k`: at any fixed quasimonomial valuation, the upper estimate
`Z(L^2(2^k g)) <= 2^k Z(g) + A` is strictly negative for large `k`, which is
incompatible with the unit ideal.  Since the ambient ring is local, adding
`m^(4^k)` then makes the proper ideal `m`-primary.

## Correction

Chapter 70 now says that the approximating ideals are either the unit ideal
or `m`-primary.  In the nonzero case, after discarding finitely many terms,
they are all `m`-primary; in the zero case, the unit ideal gives the constant
zero approximation.  The same qualification is propagated to the chapter's
comparison ledger.  No P12 atom or inventory count changes.

This correction preserves the exact BFJ monotonicity and convergence claim;
it removes only the unsupported proper-primary strengthening at the zero
boundary.
