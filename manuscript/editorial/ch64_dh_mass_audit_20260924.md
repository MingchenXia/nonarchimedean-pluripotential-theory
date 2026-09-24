# Chapter 64: DH mass and endpoint atoms — 24 September 2026

## Scope and correction

Baseline: `a3368bf4ef5179042522dade93a71ea89308a5ea`. The clean main
branch was synchronized with the designated origin before this unit.
All drafting and both full build rounds used a temporary baseline export.
The initial fetch approval timed out; its authorized retry succeeded.
No concurrent live source edit, build or Git mutation was found.

The two claims that total DH mass equals V precisely when the terminal
level has full mass were false. The defining reference is the initial
level. Both occurrences are corrected, with an explicit counterexample.
The former moment theorem also omitted the I-model assumption needed to
identify multiplier-ideal volume with non-pluripolar mass. The corrected
hypotheses are stated at the section opening and in the theorem, and the
reason for this restriction is explicit. The existing Chapter 55 warning
on multiplier-ideal volume applies to the omitted generality.

For a bounded positive-mass I-model test curve on a connected smooth
projective complex manifold of positive dimension, let m be the initial
mass and c the cutoff. The partial-body theorem gives a bounded transform
G on a reference body of Euclidean volume m/n!. Its superlevel identity
proves DH([tau,c]) = M(tau). Finite-measure continuity from above gives
the endpoint atom lim_(tau up c) M(tau). No identification with the raw
analytic endpoint mass is used in this general statement.

The Minkowski inclusion and Brunn--Minkowski give concavity of M^(1/n)
on the interior. Thus M is locally Lipschitz there. Differences of tails
identify the density -M' on compact subintervals; exhaustion proves that
only c can carry an atom. Boundedness of G justifies ordinary signed
Fubini for every integer moment, including odd powers and negative cutoffs.
The first moment is the existing unnormalized relative energy identity.
Replacing m by V when m < V creates a negative constant integrand on a
lower half-line and is invalid.

## Explicit example and arithmetic

The hyperplane curve on P1 from Chapter 52 has mass 1-sigma and partial
body [sigma,1]. Freeze its initial level at a and cut off at b, where
0 <= a <= b <= 1 and a < 1. Concavity follows by composing a decreasing
concave curve with max(a,tau); the closed endpoint is inherited from the
original curve. The transform is min(x,b) on [a,1]. Its DH measure is
Lebesgue measure on (a,b) plus (1-b) delta_b. The initial mass is 1-a,
the analytic endpoint mass in this example is 1-b, and the first moment
is b-(a^2+b^2)/2. The text checks (a,b)=(0,1), (1/4,3/4) and a=b.

Exact Fraction arithmetic uses 65 pairs of tenth-integer cutoffs, with
translations -3, -1, 0, 1/3 and 2, and moment orders 1 through 6. All
1,950 comparisons agree among direct integration of the pushed measure,
the layer-cake formula and the binomial translation formula. The zeroth
mass and unshifted first moment are checked for every pair. These are
checks of the example, not substitutes for the general proof.

## Primary sources and proof limits

The published [Xia article](https://msp.org/gt/2025/29-3/gt-v29-n3-p04-p.pdf),
Geometry & Topology 29 (2025), 1283--1344, was downloaded, extracted and
visually inspected on physical pages 46, 49 and 50, corresponding to
printed pages 1326, 1329 and 1330. Definition 7.1 specifies the full
initial potential and distinguishes I-model curves. Definition 7.6 and
(7-8) define a bare Lebesgue pushforward, of mass vol(Delta). Lemma 7.7
and Definition 7.8 use I-model curves with full initial volume and the
intersection of interior bodies at the endpoint. The book's analytic
measure, equation (55.21), is n! times this source convention. This
factor is now explicit beside the citation. The relative initial-body
extension used here is the existing book Theorem 55.3.1, rather than an
assertion that the published Lemma 7.7 covers relative initial mass.
The existing bibliography key Xia21 already resolves to the publication.

Published source PDF SHA-256:
`b8568896bbf7cdad2dedfc97a8048d3caa75bc800d67f04bfcbadd3705a2a5f9`.

The mass-volume identification, partial-body construction and relative
ray-energy correspondence remain cited inputs with their stated scopes.
This is a two-pass local correction and consequence audit, not a new
independent-agent or production-verifier receipt. No frontier research
atom changes status in this unit.

## Final verification and preservation

The second pass rechecked the I-model restriction, reference volume,
bounded support, half-open interval subtraction, endpoint limits,
Brunn--Minkowski argument, signed Fubini and all degenerate curve cases.
It made the closed-endpoint check explicit, split two overflowing displays
and improved the first-moment layout. Both full-book build rounds completed.
The final PDF has 4,003 pages and 19,061,958 bytes, with no
unresolved reference/citation, multiply defined label, rerun request or
horizontal/vertical overflow. The source closure contains 390 inputs and
11,700 unique labels. The inventory retains 45 active atoms across 14
environments, with tier counts (0,5,8,15,17). The scoped house audit passes
strict mode with zero errors and zero warnings.

Physical pages 3464--3467 and 3469 were rendered and inspected in both
passes; final page 3470 was also inspected for the source-note continuation.
Earlier Chapter 64 sections and the entire algebraic-DH/finite-energy
comparison block retain their exact baseline bytes. All other tracked
sources were compared against the 4,140-file baseline before updating
progress records. Chapters 60--63, P12.1 integration and provenance, both
author originals, bibliography, frozen packets, verifier receipts and
dated release artifacts remain unchanged. Only Chapter 64 and four
current progress/audit records are included in this revision unit. The
checked current book.pdf replaces the ignored local artifact; generated
build files are not committed.

Final PDF SHA-256:
`858f1c9bf473f4059b0fa2fd4742af299fc201da925f3f4d5512904e684123df`.
Final Chapter 64 SHA-256:
`356aa36cc157e181ce34128c96068b30d3b07c54e1051c3da746e21161b98f32`.
