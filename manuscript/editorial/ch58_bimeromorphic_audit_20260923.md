# Chapter 58: bimeromorphic transport of full-support characters

Audit date: 23 September 2026.

## Scope

This unit replaces only the bimeromorphic proposition and its proof in
Chapter 58, adding two supporting lemmas and a nodal-curve example.
The original conclusion for proper bimeromorphic maps of reduced
irreducible compact complex spaces is preserved, including nonnormal
spaces. The support/center section, subsequent algebraic recovery,
multiplier-ideal bridge and all other chapter text are unchanged.

This is a checked reconstruction of an existing sourced proposition.
It is not a new research theorem, an independent-agent verification,
a production verifier gate, or a closure of a research atom.

## Mathematical repair

The former proof used relative generation to descend a sheaf directly
as an ideal of the base, without treating a nonnormal base. It then
asserted choice independence and the character laws without proving
nonnegativity or explaining why equal pullbacks have equal values.
It also declared every value finite, including the zero ideal, and
applied the relatively ample special case to both arrows in a common
resolution without establishing its hypotheses for the second arrow.

The finite case is now proved directly. For A=O_X inside B=q_*O_Y,
the conductor c=Ann_A(B/A) is a nonzero coherent ideal of both rings.
For a coherent ideal j on Y, the product a_j=c q_*j is an ideal of A.
For nonzero j, set w(j)=v(a_j)-v(c), and set w(0)=infinity. The proof
checks nonnegativity from a_j subset c, addition from the sum identity,
multiplication from a_j a_l=c a_(jl), the unit, and both inverse maps.
Finite cancellation proves uniqueness and independence of the common
coherent ideal. No claim about prime analytic stalks is needed.

For a projective modification of normal spaces, pullback inclusion
of two nonzero ideals implies the reverse inequality for every
full-support character. To prove this, principalize the denominator
ideal by a normalized blowup and apply the precise direct-image
description of its integral closure. Invariance under integral closure
is rederived from the finite Rees algebra and

    (bar b)^(N+1) = b (bar b)^N.

The exponent is uniform on the compact space. Cancellation uses only
finite values of nonzero global coherent ideals. The integral equation
uses coefficients a_i in b^i; it does not reproduce the coefficient
condition printed in the source's Definition 2.2.1. The source's
Lemma 2.2.4 uses integral closures of powers in its own cancellation
argument; these bars were checked visually rather than inferred from
the plain-text extraction.

The normal relatively ample case then uses L=O(E) subset O, after
taking a relatively generated power, and k=f_*L. Normality gives
f_*O=O, so relative generation produces genuine base ideals a with
f^*a=j L^m. The reflection lemma proves that v(a)-m v(k) is nonnegative.
Multiplying numerators by powers of k proves independence of m and a.
Products and sums are represented explicitly, including the common
exponent in the sum calculation. Zero and unit ideals are handled
separately. Uniqueness also proves independence of L.

For the general normal case, domination first proves surjectivity
for every proper bimeromorphic map. Apply that already established
surjectivity statement to the second arrow; injectivity of the
composite then proves injectivity of the original map. No relatively
ample divisor for the second arrow is presumed. An ample negative
exceptional combination has suitably chosen weights, rather than
an asserted unweighted exceptional sum. The finite normalization
square finally recovers the full original nonnormal scope.

## Counterexample and exceptional cases

On the normalization of the previously defined nodal cubic, the ideal
O(-p_+) does not descend to an ideal on the curve: a pair of analytic
germs at the node must have equal constant terms, so being a unit at
p_- forces a unit at p_+. A finite map has relatively ample trivial
line bundle and relatively generated coherent sheaves; hence this
is a counterexample to the former descent shortcut itself.

The conductor is O(-p_+-p_-), and its product with O(-p_+) is
O(-2p_+-p_-). This does descend, via pairs in (u^2) and (t).
The two point characters upstairs also have the same image at the
node, demonstrating why bijectivity cannot extend to all support
strata. No homeomorphism assertion is added.

The second local pass checked nonzero pullbacks, zero and unit ideals,
finiteness of every subtraction, both conductor inverse identities,
the direction of ideal/value inequalities, uniformity of the reduction
and twisting exponents, the sum representation, independence of all
choices, the order of the resolution argument, the normalization
square and the two branch calculation. It added explicit preservation
of full support in the finite lemma and made the compact-base choice
and coherent-ideal qualification explicit. The final layout pass removed
repeated conventions and explanations so that the adjoining theorem
statement and its formula remain together, without changing that theorem.

## Sources and limits of source inspection

- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
  18 September 2025: Proposition 2.1.6, pp. 12--14, for the original
  theorem and geometric domination input; Proposition 2.2.2,
  Corollary 2.2.3 and Lemma 2.2.4, p. 14, for normalized blowups and
  integral closure. Section 2.2's explicit normality restriction is
  retained at every use. The archived PDF was read without modification;
  pp. 13--14 were rendered and inspected, and the official HTML was
  checked again. PDF SHA-256:
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  The exact-version bibliography entry MPTropicalV2 is used. The
  publisher's full typesetting was not available in this audit.
- Grauert--Remmert, *Coherent Analytic Sheaves*, existing CAS entry:
  [Chapter 3, Section 1](https://link.springer.com/chapter/10.1007/978-3-642-69582-7_3)
  for preservation of coherence under finite maps, and
  [Chapter 8](https://link.springer.com/chapter/10.1007/978-3-642-69582-7_8)
  for normalization. The official chapter descriptions and publisher
  preview text at pp. 61--62 and 152--153 were checked. These verify
  the cited interfaces and chapter locations, not a fresh audit of
  the complete proofs behind the subscription preview.
- [Stacks Project, Tag 00H3](https://stacks.math.columbia.edu/tag/00H3)
  was checked directly for the passage from ideal integral dependence
  to integral dependence of a degree-one Rees element.

Analytic normalization, the finite/direct-image theorems, relative
generation, normalized blowups, and Hironaka domination remain named
geometric inputs. They have not been relabelled as newly proved here.
The character computations and all subsequent formal reductions are
written out. No claim of independent or production verification is made.

## Validation and preservation

The final full build passes: 3,945 pages, 18,759,784 bytes, 389 TeX inputs
and 11,575 unique labels. Reference checking reports no missing inputs,
duplicate labels or dangling references. The final log has no unresolved
references or citations and no horizontal or vertical overflow. Existing
underfull-box and document-class warnings outside this unit remain.
The strict house-style audit of the complete changed block returns
zero errors and zero warnings. `git diff --check` passes.

Both build stages were inspected at the revised pages. Final physical
pages 3301--3305 (printed 3233--3237) were rendered and visually checked,
including the adjoining section transition. Source and PDF checks are
separate from the mathematical/source re-reading above.

The checked inventory remains 46 active atoms in 14 environments,
with tiers `(0,5,8,16,17)`. Author sources, the supplied CURVE_PSH.tex,
frozen proof packets, verifier receipts and dated release artifacts
are unchanged. The chapter's prefix and suffix outside this unit were
compared byte for byte with the preceding commit. The bibliography
also remains byte-identical. The generated live PDF is ignored and
is not included in the Git commit.

SHA-256:

- Chapter 58: `676425d8bb189b2027f0cccea43f441c6e004f090db1618fbd1de0d39fdeca6e`.
- Existing bibliography: `4ae3370eca199278ec8f2b43fbe677afc9789ddeeaef2da5156fc183bf8f860c`.
- Generated live PDF: `560a3774d03eee826ea44de5a5e39841142eb6df6d55a43bf6f099a05245a079`.
- Supplied and restored CURVE_PSH.tex: `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

The next bounded unit is Chapter 58's proper algebraic recovery:
verify the algebraic ideal-semiring comparison, the use of GAGA,
the centering argument and equality of topologies. Keep that check
separate from any extension to nonproper analytic spaces.
