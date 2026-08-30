# Current-source build: P06.2 arbitrary-field strict-polydisc traces

Date: 30 August 2026 (Asia/Shanghai).

This record supersedes `current_source_build_p071_infinite_star_20260830.md`
as the controlling current-source build. It does not rewrite or replace any
earlier dated release archive.

## Mathematical gate

The arbitrary-field strict-polydisc packet passed two independent exact-byte
hostile audits and production Rethlas run
`20260830T015556Z_7510083fecda`, using `gpt-5.6-sol` at `xhigh`. The final
verdict was `correct`, with zero critical errors, zero gaps, and eight
reference checks without an issue. The direct endpoint assigned no item
identifier. The exact statement/proof SHA-256 values are

- `7510083fecda2d561c4ce2a1b35d08377268ef48adda2b242172428dbd39caec`;
- `77a013d4e655d288d8803c9650df5446bed570de2644591edddfc116c323eab2`.

The controlling production receipt has SHA-256 value
`53526abfe80ea1ab7b02e48e9f5a06258befa522d81c36b28dc6f48dc8e86142`.
The release-candidate `SHA256SUMS` manifest was rechecked after integration;
all eight archived files matched.

The unconditional theorem is deliberately confined to the part that descends
over every complete nontrivially valued ground field: a continuous
zero-current function is constant on all ground-field rational points, on all
ground-field-centred Gauss skeleta, and on the closure of their union. Full
constancy follows if the zero-current equation is known after one complete
algebraically closed extension. On the open polydisc this scalar-extension
hypothesis is automatic when both signs of the function are CLD-psh in the
approximation sense. No automatic scalar-extension stability for arbitrary
continuous Hessian currents, non-rational rigid points, or arbitrary analytic
germs is asserted.

## Converged whole-book build

Starting from base commit
`85ec96412ea6c00fd1056bc0f744768e5c736135`, the integrated source was built
with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
```

The build converged. The final log scan found:

- LaTeX errors, fatal errors, and undefined control sequences: 0;
- undefined references and citations: 0;
- multiply defined labels and duplicate destinations: 0;
- overfull horizontal or vertical boxes: 0.

## Current PDF

- pages: 3,368;
- bytes: 16,158,406;
- SHA-256: `a0e051390248f0055f7aee0150159501668ff6510b2f7bb81cf54800192c5ada`.

The synchronized artifact is
`output/pdf/Non-Archimedean_Pluripotential_Theory.pdf`; its hash equals the
final `manuscript/book.pdf` hash.

## Rendered audit

Physical PDF pages 1026--1029, containing Propositions 18.8.9 and 18.8.10 and
their complete proofs, were rendered and inspected at high resolution.
Physical pages 3169--3170, containing the revised P06.2 status and production
provenance in Chapter 72, and physical page 3336, containing the Appendix L
provenance record, were also inspected. No clipping, overlap, malformed
display, broken link text, hash overflow, or margin intrusion was found.

## Inventory consequence

The theorem narrows but does not retire P06.2. The active inventory therefore
remains 53 atomic questions in 14 formal problem environments, with tier
distribution `(0,5,14,17,17)`. The next residual target is descent to rigid
points with nontrivial residue extension; in dimension one this reduces to a
finite continuous-multiplier trace lemma through ramified, inseparable, and
endpoint fibres.

No novelty or priority claim is made.
