# Chapter 61: model measures and sequential selection — 22 September 2026

## Repair

The proof of simultaneous strong and entropy approximation formerly
selected models using only two numerical energy conditions. It did
not establish weak convergence of the selected sequence; convergence
of the full model net does not supply a countable cofinal model family.

The revised proof first establishes convergence of the full net.
PL tests factor through every sufficiently fine model, so their
integrals are eventually equal to those against the original measure.
Uniform density and probability mass give weak convergence.
Retraction compatibility and the psh majorant property make the
composed potentials decrease. Model dominants identify their limit
with the original psh potential.

The composed potentials are continuous on the whole compact
analytification by continuity on the finite dual complex. They are
uniformly bounded above. The Radon version of monotone convergence
for decreasing usc nets, already proved in Chapter 7, therefore
applies. The variational inequalities first prove finite energy of
every retracted measure. Interchanging two suprema then proves
convergence of dual energies. The continuous nonnegative discrepancy
representatives use the increasing-net version of the same Radon
argument, including infinite entropy.

Only after full-net strong convergence is established does the proof
select nested models. At step j it requires quasi-distance less
than 1/j and entropy within 1/j of the finite target, or greater
than j for an infinite target. Each condition holds on a tail;
directedness gives a model satisfying both and dominating the previous
choice. The quasi-metric bound proves strong convergence of the
selected sequence without a countable cofinal family.

## Sources and dependencies

This reconstructs Lemmas 7.2.1--7.2.2 and Corollary 7.2.3 of
[MPWN25, arXiv v1](https://arxiv.org/html/2509.09442v1).
It retains the theorem's scope and makes the selection and integration
steps explicit. The internal inputs are Chapter 59 retraction
compatibility and reduced discrepancy, Chapter 61 convex restriction
and strong quasi-metrics, and Chapter 7's semicontinuous Radon
integration results. The already verified convex-restriction
statement and proof are untouched.

## Validation

The actual final proof passes the strict writing audit with zero
errors and zero warnings. A second reading checked the retraction
composition, model factorization, continuity of the integrands,
the order of the two suprema, finite energy before its use, and
the finite/infinite entropy alternatives.

The source check has 389 TeX files and 11,500 labels, with no
missing input, duplicate label, dangling reference or structural
defect. After correcting an undefined temporary notation, the
full build passes with 3,919 pages and 18,597,461 bytes, no
unresolved reference or citation and no horizontal or vertical
overflow. Physical pages 3342--3344 were rendered and inspected.
The source diff is whitespace-clean.

PDF SHA-256: `f41cadc3e055abd67c0ace4e963f61907f1947503581fc1f3838fdf738d0d512`

Chapter 61 SHA-256: `74133504d5e24c5a2425f6dc42d4e1ba0ecd870b6caf20c3251edfdd05abd074`

Preserved convex-restriction block SHA-256:
`f82585d8a420d3214a008a583a14f0487bd657372b4f8656acae3c027ac487de`

The inventory remains 46 active atoms in 14 formal environments,
tiers (0,5,8,16,17). The supplied CURVE_PSH.tex, Chapter 71,
frozen research inputs and dated release artifacts are unchanged.
No research gate or new research result is claimed.
