# P21.3 arbitrary-valued componentwise curves: live integration receipt

**Date:** 29 August 2026

**Model and scrutiny:** `gpt-5.6-sol`, `xhigh`

**Controlling item:** `pi_1ca3e6d14c7e8596372d863d`

**Verdict:** `correct`; **critical errors:** `0`; **gaps:** `0`

This receipt controls the dependency-closed integration of the reducible and
nonreduced curve theorem.  It is not a novelty or priority claim.

## Principal packet and dependency closure

The live principal statement and proof have SHA-256 values

```text
91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0
098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1
```

The production request prepended, in order, the nontrivially valued rigid
zero-atom pair, the trivially valued Gauss--Shilov zero-atom pair, and the
arbitrary-valued normal-curve pair.  Their statement/proof digests are

```text
469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac
661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2
ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a
789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66
339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7
d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660
```

The exact materialized statement and proof are 11,920 and 54,321 bytes, with
SHA-256 values

```text
d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6
cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f
```

The archived request decodes to these exact bytes, and the returned proof
digest is the materialized proof digest.  The request, response, and
sanitized headers have SHA-256 values

```text
6920d2582649e1fcedcc3a729242e1ca02fded05502cc878a36f4e8652929365
87507beab77d5917edc8cd8d1abcf466965222a2c973e6cded58beabd2057a8a
0733b7bff2ffbe09bba821804d7b4bcbf50842031743a096f5db79c9dc5cdde6
```

The controlling packet receipt has SHA-256
`8cfc406127987d4347a3ec765f015b3ba30645723f884002aa5cd27c29655810`.
Its independent receipt audit has SHA-256
`591f56135349eed40e016db205ff62e84c6b731f8630dd5efc2de0b92cde2545`.
Independent mathematical, source, binding, response, and post-integration
audits all passed.

## Mathematical scope and retired residual

Let (K) be a complete non-Archimedean field, possibly trivially valued, and
let (X) be a good separated strict boundaryless pure one-dimensional
(K)-analytic space, with arbitrary reducible and nonreduced structure.  If
((X_i)_i) are the irreducible components of (X_{\mathrm{red}}), every
positive closed ordinary CLD current of bidegree ((0,0)) has a unique locally
finite representation

```text
T = sum_i c_i delta_{X_i},  c_i >= 0.
```

Nilreduction preserves the ordinary CLD calculus, psh sheaf, and current
topology, while the fundamental integration current retains generic
component multiplicities.  The theorem proves Bedford--Taylor independence
for continuous psh pairs.  It does not claim the possibly discontinuous-pair
predicate of CLD Definition 8.6.2 on a reducible or nonreduced space.

Together with the normal-curve theorem, this retires every one-dimensional
case lying inside P21.3's ambient hypotheses.  P21.3 remains exactly one T2
atom, now restricted to analytic dimension at least two.  The book-wide
inventory remains 15 problem environments and 54 active atoms, with tier
counts `0/6/14/17/17`.

## Integration and whole-book gate

Chapter 16 inputs the principal statement and proof without mathematical-text
transformation, after their exact dependencies.  The post-integration audit
found 145 unique live TeX inputs, no duplicate source labels, and each of the
60 new packet labels exactly once in the compiled auxiliary files.  It also
confirmed the scope and counts in Chapter 72, Appendix L, the inventory, and
the verification ledger.

- Final PDF: 3,282 pages, 15,765,463 bytes, SHA-256
  `ee3ef27eebb5449b703e25e91d48b804598049a3f47244117cdd823e9a3497d0`.
- Final log SHA-256:
  `3619f042f18a1a73734c5dff76378fc480469affb2e96d50b17927195823ecb8`.
- No TeX error, undefined reference or citation, duplicate label or
  destination, rerun request, or overfull box; only the harmless historical
  class-path warning and 992 underfull-box notices remain.
- Final rendered inspection passed on the theorem, example, scope-firewall,
  residual-problem, and provenance pages listed in the companion normal-curve
  integration receipt.

