# Chapters 61--62: domination and normalized model formulas — 22 September 2026

## Mathematical correction

The domination proof in Chapter 61 formerly inferred the pointwise
inclusion K subset {phi + epsilon > psi} from phi >= psi on K.
That inference fails where both potentials equal minus infinity.
The corrected argument uses the finite-energy integrability lemma:
the exceptional set has zero MA(phi) measure, which is all locality
and equality of the two probability measures require. Evaluation
at a finite point then identifies the additive constant. The
regularity proof specifies convergence of its decreasing net and
applies domination to phi_i - epsilon with phi as reference.

The former Chapter 62 invariance proof treated positive products
as multilinear intersections for every big class. It used
F dot <B^n> = V and a binomial formula under B -> B + cF.
The new surface example disproves these steps under the chapter's
literal global-bigness definition.

On the blowup of P1 x P1 at (p,0), use the basis (H,F,E) with
H.F = 1, E.E = -1, and all other basis pairings zero.
For B_c = H + cF - E/2 and 0 < c < 1/2, the Zariski decomposition is

    P_c = (1/2+c)H + cF - cE,
    N_c = (1/2-c)(H-E).

P_c has intersections c, 0, 1/2 with the three extremal curves
E, H-E, F-E; the negative support has square -1 and P_c.N_c = 0.
Thus <B_c> = P_c, <B_c^2> = c+c^2, and B_c is big.
The central fiber is reduced, and K_relative = -2H+E. The raw
intersection definitions give

    M(B_c) = c^2,       J(B_c) = c/2-c^2/2.

At c = 1/10 these are 1/100 and 9/200.
At c = 3/2, B_c is Kähler, the volume is 11/4, and the
ordinary-intersection values are M = 1/4, J = 1/8.
The divisors differ only by 7F/5. Also F.<B_(1/10)> = 3/5,
whereas V = 1. An exact rational-arithmetic check independently
reproduced all these intersections and values. The negative part
is horizontal; it changes under addition of the base class.

## Resulting scope

The raw DF, M and J formulas and the original all-big-model stability
definition remain in the manuscript. A separate normalized model
inequality tests those formulas on f_D >= 1.

For that normalized range, the imported positive-product identities
identify M and J with the potential functionals. Pullback invariance
and translation between two normalized representatives follow from
these identities, without an unrestricted pullback or binomial rule
for positive products. The former blanket assertion about all three
raw intersection expressions was removed.

Every PL obstacle f can be translated into this range. Indeed,
f_D >= 1 implies D - X_0 effective, and A + X_0 is the pullback
of a Kähler class from X x P1. Therefore A+D is big. This proves
the equivalence of the normalized model inequality with the PL-envelope
inequality, with the same positive constant.

The full finite-energy and divisorial-measure equivalences are stated
with this normalized condition. The raw all-big-model condition
implies them by restriction. The cscK existence implication survives.
Chapter 68, the model-to-ray formulas and the provenance appendix
now use the same scope.

No converse from the normalized inequality to the literal raw
all-big-model condition is claimed. The example disproves a proposed
invariance argument; it does not by itself disprove equivalence of
the two stability notions. A comparison sufficient for that converse
remains an explicit unresolved source-audit item.

## Primary-source check

[MPWN25, arXiv v1](https://arxiv.org/html/2509.09442v1),
Definitions 1.1.1--1.1.2, use global bigness and the raw intersection
expressions. Theorem 9.1.1 and Proposition 9.1.5 explicitly assume
f_D >= 1. Lemma 9.1.4 requires an effective vertical divisor to
promote relative nefness to global nefness. Corollary 9.1.6 asserts
the all-big-model equivalence; the missing comparison is not supplied
by adding a base class. The arXiv record still listed only v1 when
checked for this audit.

For context, [Li, arXiv:2102.09457v1](https://arxiv.org/pdf/2102.09457),
Definition 2.1, page 4, imposes an additional equality of stable and
relative base ideals in the definition of a big model. It is therefore
not a theorem about every globally big compactified class. This
preprint comparison is recorded here only; it is not substituted for
a checked published theorem or added as a new proof input.

## Validation and preservation

The reconstructed domination and regularity proofs, the complete
new normalization section and the provenance addition pass the
strict writing audit with zero errors and zero warnings.
A second mathematical reading checked the null set, normalization
quantifiers, Zariski decomposition, both directions of the normalized
inequality, all affected consumers and the remaining unproved converse.

The complete source closure has 389 TeX files and 11,506 labels.
There are no missing inputs, duplicate labels, dangling references
or structural defects. The full build has 3,921 pages and
18,608,364 bytes, no unresolved references or citations, and no
horizontal or vertical overflow. The diff is whitespace-clean.
Physical pages 3345--3358, 3489--3490, 3492--3493 and 3872 were
rendered and inspected. The fraction table was enlarged and its
row spacing corrected after the first visual pass.

PDF SHA-256: `0fe5125598e9033a2c7e2d23d5b27efaaaa0482ccd1d39d1e499c3a0bf03b62d`

Chapter 61 SHA-256: `d184a2c92848b2d6b3130eec542923c7c338a7128ea504afb44b3b5fa588fa62`

Chapter 62 SHA-256: `5b2a380695cf5a1898baee959a13683d5a0cb748ce308cd955bbad4b9078f49d`

Chapter 68 SHA-256: `e03008e0bb3bffd991dbe3cc61a842a667839a6481394e8cce522da9fd6d8847`

The factor-n verification block is byte-identical, with SHA-256
`204ca71038019e4ca4b24aba3b89e54965ef8586fe433a511619e4a54933ee25`.
Its surrounding scope now explicitly requires f_D >= 1.
The checked Chapter 61 dual-complex proof retains SHA-256
`f82585d8a420d3214a008a583a14f0487bd657372b4f8656acae3c027ac487de`.
The supplied CURVE_PSH.tex is still byte-identical to the author's
download, and Chapter 71 and dated release artifacts are unchanged.
The editorial inventory remains 46 active atoms in 14 formal
environments, with tiers (0,5,8,16,17).
This is a source-scope repair and a direct intersection calculation;
no new research gate or independent-agent verification is claimed.
