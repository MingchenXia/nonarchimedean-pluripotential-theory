# Chapter 59 projective comparison and nonalgebraic examples

Date: 23 September 2026.
Baseline: `2de7848c5632c15aa4dd16006838292044889ab0`.
Scope: the projective comparison immediately before Section 59.5,
Section 59.6 and the source note; two bibliography entries appended.

## Mathematical checks

The projective paragraph now uses the already proved proper algebraic
recovery theorem in Chapter 58 and distinguishes complex analytification
from Berkovich analytification with the trivial absolute value. On each
algebraic snc test configuration, the components of every intersection,
central multiplicities, normalized vertex coordinates, ideal evaluations,
and divisor pullback matrices agree after complex analytification. This
identifies its retraction and transition maps with BJ22 Theorem A.1.
Finite flag coefficients algebraize by GAGA; their blowups and the formula
D_f = sum b_i f(e_i) E_i identify the PL correspondence with Lemma A.2.
The paragraph does not assume that an arbitrary analytic C-star action
algebraizes, or claim a new cofinality theorem for analytic models.

The approximation paragraph distinguishes uniform sequences for one
continuous function, the net of retractions indexed by models, and rational
approximation within a fixed finite face. No countable cofinal system is
inferred from the first or third assertion.

The torus example now supplies the elementary genericity argument. For
each nonzero integral alternating form E on a real torus of dimension
2g, g >= 2, the type-(1,1) equation cuts out a proper closed real-analytic
locus in either component of the complex-structure space. A four-vector
construction proves properness in both orientation components; Baire and
Lefschetz (1,1) give NS = 0. A translation-invariant Hermitian form gives
a Kahler metric. A nonzero effective divisor would have positive Kahler
degree, contradicting its zero cohomology class. Normality then excludes
nonconstant meromorphic functions. Point ideals distinguish the exceptional
valuations despite this constant global field. Blowing up (p,0) in the
product gives two central components, each of multiplicity one, with
connected intersection P^(g-1); the dual interval has the stated endpoints.
The dimension restriction is retained: a point blowup of a curve would not
produce the asserted exceptional divisor over X.

The K3 example cites existence with Pic = NS = 0 and the Kahler input
separately. Two point blowups have chart x=ab, y=ab^2, exceptional boundary
E'=(a=0), F=(b=0), and K_Y/X=E'+2F. The exponent transformation is injective.
For a single zero weight, the coefficient is a germ on the boundary curve,
not its value at the intersection point. The two positive boundary rays and
the zero character are stated separately, avoiding a convention of 0 times
infinity on the zero germ. For every s,t >= 0 the global ideals I_p and
the finite-colength ideal with stalk (y)+(x,y)^2 have values s+t and s+2t.
Their difference recovers t and then s, proving separation including the
boundary. The earlier log-smooth discrepancy formula gives 2s+3t.

## Exact sources and bibliography

- Boucksom--Jonsson, published
  [Appendix A](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf):
  the boundary and normalization conventions on pp. 826--827,
  Theorem A.1 and Lemma A.2 on p. 828. Printed pp. 827--828 were rendered
  and inspected; p. 826 was read as text. PDF SHA-256:
  `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.
- Huybrechts, *Lectures on K3 surfaces*: the published
  [Chapter 17, Section 1.1](https://www.cambridge.org/core/books/abs/lectures-on-k3-surfaces/picard-group/0FFE84C56E2FA804CCAB4B5BEAD80B0E)
  preview states Pic=NS, the integral (1,1) description and attainment
  of all possible Picard numbers. This is the locator cited in the book.
  The author's downloadable draft was read for context only; its page
  numbers are not attributed to the published edition. The
  [author's publication list](https://www.math.uni-bonn.de/people/huybrech/Publbooks.html)
  and publisher chapter metadata verify author, title, series 158,
  publisher, year and book DOI. MathSciNet access was unavailable and the
  publisher frontmatter download failed; no unverified MR number, ISBN
  or page total was added. No source PDF is redistributed.
- Siu, *Every K3 surface is Kahler*: printed p. 139 was inspected in the
  [author-hosted published scan](https://people.math.harvard.edu/~siu/siu_reprints/siu_k3_kaehler_invent1983.pdf).
  The [publisher record](https://doi.org/10.1007/BF01393829) verifies the
  journal, volume 73, year 1983, pages 139--150 and DOI. PDF SHA-256:
  `b84ef0cfa49701008f42b513b990ef2f22387d413713588d748b023ffc970983`.
- The source-note map was checked against the existing exact
  [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2), whose PDF hash is
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  It no longer calls these version-specific locators simply "MP24".
  The earlier Bingener, Xia and Jonsson--Mustata source reconstructions
  retain their recorded scopes. The discrepancy convention is unchanged.
  The current MPWN arXiv record still lists v1 without a journal reference;
  Xia's site describes *Stein spaces* as personal notes. These observations
  explain the retained preprint/notes citations, not a claim that no other
  publication exists.

## Second pass, rendering and preservation

After the first successful full build and inspection of the comparison
and example pages, the complete second mathematical and source pass
rechecked the two orientation components, closed exceptional loci,
generic coefficient germs at zero weights, coherent extension of the
finite-colength ideal, the recovery of both weights, and the relative
canonical coefficients. It made the zero cases and ideal calculation
explicit. The second rendered pass kept the blowup-coordinate paragraph
and its display together. A redundant source-note recap created a short
isolated final page; it was removed, followed by another complete build.

Final build: **3,965 pages, 18,870,444 bytes**. Reference check:
390 TeX inputs, 11,599 unique labels, no missing inputs, duplicate labels
or dangling references. The final log has no undefined references/citations,
rerun request or horizontal/vertical overflow; existing underfull/class
warnings remain. Strict changed-block style audit: zero errors/warnings;
with bibliography: zero errors and three reviewed source-version warnings.
Whole-chapter audit: 102 legacy errors (101 inline delimiters and one
MP24 compound-surname bibliography label) and six warnings (three
source-version warnings, the chapter-label prefix and two optional
definition titles). This is not a clean whole-chapter style claim.
Inventory: 45 active atoms, 14 environments, tiers (0,5,8,15,17).
`git diff --check` passes.

Final changed pages and their boundaries, physical 3329--3337, plus the
new bibliography entries on physical pages 3961 and 3963, were rendered
and inspected after the final complete build.
Final chapter SHA-256: `33c8d7ad029e5c7be18291eff1637b384a9b73c98948d9c7c54772e549cadd6a`.
Final bibliography SHA-256: `d7fe599d8cac4e6de1b8edee632536bf2b44a38b1154c0f316bb3c67353059a0`.
Final live PDF SHA-256: `4520099e5b47796dd201f016ec841febd4cc82e74514ea34d4875a17f1909a71`.

The chapter text before the comparison and all of Section 59.5 retain
their exact baseline bytes. The old bibliography is an unchanged prefix
of the new file. The P12.1 proof retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`;
its supplied source, retirement and provenance are unchanged. Chapters 58,
60 and 61, supplied CURVE_PSH.tex, frozen packets, verifier records and
dated releases are untouched. This unit supplies checked exposition and
worked applications; it closes no research atom and claims no new
independent-agent or production-verifier pass.
