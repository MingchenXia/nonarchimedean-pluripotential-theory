# Production Rethlas receipt: arbitrary-valued componentwise analytic curves

Date: 29 August 2026

This receipt records the controlling dependency-closed verification.  It is
not a novelty or priority claim.

## Exact principal packet

- statement SHA-256:
  `91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0`;
- proof SHA-256:
  `098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1`;
- independent hostile-audit SHA-256:
  `35af811f8d73fadc2a484f9f90f1ef0825470ad3223eab69195ba5b9269e6fa2`;
- revised3-binding audit SHA-256:
  `4a347171150e52a88223415cc8cfff1bb38baeabeb6eb0ce84be29ba5be595c7`.

The independent mathematical audit passed with zero critical errors and zero
intrinsic proof gaps.  The binding audit rechecked the complete dependency
order, all labels, and the materialization rule.  Its 24-page exact harness
compiled without errors, unresolved references or citations, duplicate
labels, or overfull boxes.

## Exact dependencies and materialization

The production request prepended statement and proof dependencies in the
same order:

1. nontrivially valued normal rigid-point zero atom,
   `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`
   and
   `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`;
2. trivially valued Gauss--Shilov rigid-point zero atom,
   `ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a`
   and
   `789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66`;
3. arbitrary-valued normal-curve third revision,
   `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`
   and
   `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`.

The decoded request fields are byte-identical to the prepared materialized
files.  Their sizes and SHA-256 values are

```text
statement: 11920 bytes  d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6
proof:     54321 bytes  cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f
```

All 23 labels in the dependency closure are unique, and every cross-packet
reference points backward to an included exact dependency.

## Controlling production result

The production service used `gpt-5.6-sol` at `xhigh` scrutiny.  The archive
`p213_componentwise_arbitrary_valuation_revised3_run_20260829_8107` records
HTTP status 200, final verdict `correct`, checked item
`pi_1ca3e6d14c7e8596372d863d`, zero critical errors, and zero gaps.  The
returned proof digest is exactly the materialized proof hash above.  The
service returned no run identifier, and none is inferred.

The request, response, and sanitized-header archives have SHA-256 values

```text
6920d2582649e1fcedcc3a729242e1ca02fded05502cc878a36f4e8652929365
87507beab77d5917edc8cd8d1abcf466965222a2c973e6cded58beabd2057a8a
0733b7bff2ffbe09bba821804d7b4bcbf50842031743a096f5db79c9dc5cdde6
```

## Mathematical scope

The principal packet treats every good, separated, strict, boundaryless,
purely one-dimensional analytic space over a complete non-Archimedean field,
possibly trivially valued.  It permits reducible and nonreduced spaces and
imposes no smoothness hypothesis on the normalizations of the reduced
components.  It identifies the ordinary CLD calculus and current topology
under nilreduction while retaining the generic multiplicities in the
fundamental integration current; classifies every positive closed ordinary
CLD current of bidegree `(0,0)` as the unique locally finite nonnegative sum
of normalized component currents; and proves Bedford--Taylor independence
for continuous psh pairs.  It does not assert the possibly discontinuous-pair
predicate of CLD Definition 8.6.2 in the reducible or nonreduced setting.
