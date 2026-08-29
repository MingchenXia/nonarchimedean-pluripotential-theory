# Revised3 dependency-binding audit for the componentwise arbitrary-valued packet

Date: 29 August 2026  
Status: pre-gate preparation only; not submitted to Rethlas and not integrated
into the live manuscript

## Disposition

The componentwise statement and proof retain their independent conditional
mathematical audit result: **0 intrinsic critical errors and 0 intrinsic
mathematical gaps**.  The replacement revised3 normal-curve theorem has the
same proposition label and the same classification statement used by the
componentwise proof, and its exact bytes passed an independent hostile audit
with 0/0.

The full revised3-bound dependency closure has now been materialized and
compiled.  It is eligible for production submission **only if** the separate
production verification of the exact revised3 normal-curve statement and
proof returns final verdict `correct`, with zero critical errors and zero
gaps.  Until then this packet remains quarantined.

## Exact ordered inputs

The dependency-closed statement and proof use the same order.

1. Nontrivially valued rigid-point zero atom:
   - statement SHA-256
     `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`;
   - proof SHA-256
     `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`.
2. Trivially valued Gauss--Shilov rigid-point zero atom:
   - statement SHA-256
     `ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a`;
   - proof SHA-256
     `789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66`.
3. Third-revision arbitrary-valued normal-curve core:
   - statement SHA-256
     `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`;
   - proof SHA-256
     `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`.
4. Principal componentwise packet:
   - statement SHA-256
     `91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0`;
   - proof SHA-256
     `098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1`.

The first packet has an exact production verdict `correct`.  The second was
itself verified in dependency-closed form after the first.  Its proof invokes
the first lemma.  The componentwise proof invokes the second and third
packets.  The third proof introduces no further manuscript theorem
dependency.  This is therefore the complete new-theorem dependency order.

## Exact materialized bytes

Materialization uses the production submission helper's exact rule: remove
terminal newline characters from each ordered input, join successive inputs
with two newline characters, and append one final newline character.

- Materialized statement:
  `p213_componentwise_arbitrary_valuation_statement_materialized_revised3_20260829.tex`
  - length: 11920 bytes;
  - SHA-256:
    `d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6`.
- Materialized proof:
  `p213_componentwise_arbitrary_valuation_proof_materialized_revised3_20260829.tex`
  - length: 54321 bytes;
  - SHA-256:
    `cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.

As a control on the algorithm, applying the same rule only to the first two
packets reproduces exactly the previously verified Gauss--Shilov
dependency-closed hashes
`ec185858edcc896d5bef402c1581885cd37fb7e9fcdaebad8e3a558a5d9ea02e`
and
`e7880752ee94b982fa1b77a5a5b09449fe97832719d50868f4ecee2f4ea6e1d5`.

## Compile and reference audit

The fresh harness
`p213_componentwise_arbitrary_valuation_compile_materialized_revised3_20260829.tex`
has SHA-256
`34f230b9369d4adb337a51984500a4ebe98331fea2387bae5aae11093266b271`.
It imports the materialized statement followed by the materialized proof and
uses both `NonArchimedean.bib` and `ComplexGeometry.bib`; the latter supplies
the `stacks-project` entry used by the local DVR argument.

A forced clean `latexmk` build produced a 24-page, 401739-byte PDF with
SHA-256
`9ef38e568d572dea9fffac0ae326e9e88646128017285a223b052a617b89fcb3`.
The final log has no TeX error, package warning, undefined citation, undefined
reference, duplicate label, overfull box, or underfull box.  An independent
label scan across all eight source inputs likewise found no duplicate label.

The earlier harness with SHA-256
`3e7ac35df61c6faf2fde3c3505a89e428c2a8c6fb68e12452a72a4a9db3de9db`
must not be used for production: it imports the rejected first-revision
normal-curve statement.  The materialized pair recorded here is the only
prepared revised3 binding.

## Remaining safe gate

Before submission, rehash all eight inputs and require exact equality with
the values above.  Verify that the revised3 production receipt records the
same statement and proof hashes and a final `correct` 0/0 verdict.  Submit the
componentwise principal files with the first three statement dependencies and
first three proof dependencies in the displayed order.  The resulting request
must contain statement digest
`d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6`
and proof digest
`cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.

Archive the exact request, response, sanitized headers, checked-item record,
service verification, and proof-digest receipt.  Live integration and any
open-problem inventory change remain forbidden unless that dependency-closed
componentwise production verdict is final `correct` with 0/0.

