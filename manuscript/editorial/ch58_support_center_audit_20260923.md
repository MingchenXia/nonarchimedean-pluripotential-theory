# Chapter 58: support, center and local recovery

Audit date: 23 September 2026.

## Scope and mathematical changes

The section retains its original setting: a compact reduced irreducible
complex space. The cited strong Noetherian property is a sheaf-theoretic
input, not an inference from Noetherianity of one stalk. The revised
argument explains both uses of compactness: local stationarity of an
increasing sequence gives global stationarity by a finite cover; if
an arbitrary sum were not a finite sum, successively adding an ideal
would contradict that stationarity. Thus the support and center sums
are finite, and their infinite/positive values and properness are justified.

The original source defines primality by testing products of global
coherent ideals. This convention was not specified in the chapter,
and must not be mistaken for primality in every analytic local ring.
The revised section explicitly defines global primality and proves its
equivalence to the radical ideal of a nonempty irreducible analytic
subspace. The proof records the common radical-power exponent on a
compact space and the finite irreducible-component argument. Coherence
of analytic radicals and the analytic Nullstellensatz remain the usual
complex-analytic inputs to that argument.

The new nodal cubic example makes the distinction explicit. The curve
y^2 z=x^2(x+z) is globally irreducible, since x^2(x+1) is not a square
in C(x), while at [0:0:1] its analytic equation factors as
(y-x sqrt(1+x))(y+x sqrt(1+x)). Each factor is nonzero in the quotient
local ring, but their product vanishes. Its zero ideal is globally
prime and is both the support and center ideal of the trivial
character, although that stalk is not prime. The example concerns
global analytic subspaces and does not impose local irreducibility.

The support decomposition now specifies reduced nonempty subspaces
and the embedding of each full-support stratum. It uses the canonical
inverse-image ideal under O_X -> O_Y. The proof checks zero and unit
values, independence of lifts, and the product law after adjoining
the infinite-valued support ideal. Both directions of the stratum
identification are written out. The point criteria use maximality of
the point ideal and radicality, with no unstated local-primality claim.

## Finite-level local recovery

For a character centered at p, write c=v(m_p) in (0,infinity].
The ideal a_k(f) is constructed from the class of a germ f modulo
m^k, in the coherent quotient O_X/m_p^k supported at p; f itself
need not extend globally. The proof retains the already corrected
increasing direction of the values v(a_k(f)).

The exact ideal sandwich

    a_(2k)(fg) subset a_k(f) a_k(g) subset a_k(fg)

replaces the less explicit two-index argument. Its valuations give
multiplicativity of the increasing limit without subtracting infinite
values. The sum inequality and positivity on the maximal ideal are
checked separately. Adjoining m_p^k to a_l(f), l>=k, then gives the
new exact identity

    v(a_k(f)) = min(w(f), k c).

Finite stalk generators prove recovery of every global coherent ideal,
and the same formula verifies the reverse composite. The zero stalk
uses the single generator zero, and c=infinity is included explicitly.
Thus the proof does not discard point-supported semivaluations or
silently assume finiteness of every germ value.

The second local mathematical pass checked both directions of the
global-prime equivalence, empty/unit cases, the nodal factorization,
both support-stratum maps, finite generators, the two multiplicative
inequalities, and the extended-real limits. It replaced the potentially
ambiguous phrase 'k-jet' by the precise quotient modulo m^k and kept
the short support/center definition together on one page.

## Primary-source version and locators

The source read is Mesquita-Piccione's
[final author version, arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
dated 18 September 2025. The fresh official HTML agrees with the
repository's already archived PDF at the checked passages. The PDF
was copied read-only to a temporary working location for rendering;
the archived source was not modified.

Exact locators are page 6, Notations and Conventions (global prime
ideals); page 11, the compact analytic setting and Lemma 2.1.1
(support and center ideals); and page 12, Definition 2.1.2,
Remark 2.1.3, Example 2.1.4 and Remark 2.1.5 (strata, point
criteria, local recovery and the strong Noetherian input).
All three pages were rendered and inspected.

The publisher's full text was unavailable in this check. Accordingly,
the revised section cites the new, explicitly versioned MPTropicalV2
entry; it does not claim to have verified these locators in the
published typesetting. The existing MP24 publication entry and all
other bibliography entries retain their exact bytes. The new entry
preserves the compound surname and its MP label.

## Validation and preservation

- Final full build after the second pass: 3,943 pages, 18,747,272 bytes.
- Reference/structure audit: 389 TeX inputs, 11,572 unique labels;
  no missing inputs, duplicate labels, dangling references or
  structural errors.
- No unresolved references or citations and no horizontal or vertical
  overflow in the final log. Existing underfull-box and class-name
  warnings remain outside this unit.
- Strict style audit of the complete support/center section:
  zero errors and zero warnings.
- Research inventory remains 46 active atoms in 14 environments,
  tiers `(0,5,8,16,17)`.
- Final physical pages 3297--3301 (printed 3229--3233) and the new
  bibliography entry on physical page 3940 (printed 3872) were
  rendered and visually inspected. The definition now stays together.
- `git diff --check` passes. Chapter 58 content outside this section
  and every pre-existing bibliography entry were compared byte for
  byte with the preceding committed source and are unchanged.

SHA-256 records:

| File | SHA-256 |
| --- | --- |
| Chapter 58 before revision | `99a3a0b8553cd65e9d84dea62545ead060630e8d8fe6135fdb9f36931c13f6ba` |
| Final Chapter 58 | `ce96af45cce2ba055fc996aa1bd92810e4a8e90b4ace3dcbdfed7db47c002c26` |
| Bibliography before addition | `86e76850bdc4d667b9411919cbe5e7220f380a0a7fcee047ea651e8a4cc4cb8b` |
| Final bibliography | `4ae3370eca199278ec8f2b43fbe677afc9789ddeeaef2da5156fc183bf8f860c` |
| Final local book.pdf | `d8108b550591643a1e91c3bbfe4c47121c0cf3f762a2eb43296f8eafb6ec415a` |
| MP final author PDF v2 | `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23` |

Other chapters, supplied author sources, frozen statements and proofs,
production verifier records, research classifications and dated release
artifacts are preserved. The live generated PDF remains ignored.
These are local mathematical, source, style, build and visual checks;
no independent-agent or production verification, research-atom closure
or whole-book completion is claimed.

The next bounded unit checks the proper bimeromorphic transport in
Chapter 58: the lifted character's nonnegativity and independence of
twists, the zero ideal, and the common-resolution argument. The
following algebraic recovery theorem and topology claims remain
separate checks. An eventual bibliography pass should also examine
the pre-existing duplicate Nakayama and Odaka entries visible on
printed page 3872, while preserving frozen citation keys.
