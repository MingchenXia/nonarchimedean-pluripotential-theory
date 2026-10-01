# Chapter 45 completion audit

Date: 1 October 2026

Base commit: `6cf010df8b11ef988044679b1576a55efc699a52`.

Scope: `parts/part4/ch45_envelope_consequences.tex`, following the sequential
chapter-quality programme. This completes the proof/example, external-source,
and whole-chapter rendered review left open by the three 30 September
checkpoints. Chapter 46 is next; Chapter 72 research remains paused.

## Mathematical and expository review

The chapter was read continuously and its assertions, proofs, definitions,
examples, warnings, dictionary, and provenance note reviewed. All 29 formal
assertions have an immediately following proof: eight theorems, nine
propositions, three lemmas, and nine corollaries. The thirtieth proof block
supplies the assembly proof of the theorem stated in Chapter 37. All 65
reusable environments have semantic labels, including the two important
boxes and three warning boxes; this count is not a count of numbered theorems.

The assembly and its dependencies retain integral projective varieties over
an algebraically closed trivially valued field, arbitrary real numerical
classes, arbitrary characteristic, and unibranchness where reflection needs
it. The direct inputs from Chapters 34 and 40--44 were checked at their
statement/proof interfaces. The sufficiency direction remains attributed to
the supplied unpublished manuscript, and the published ample-class converse
remains separate. No research atom or independent-verifier status changes.

The substantive revisions are:

- Generic degree is defined without normality. Normality belongs to the
  normal-target descent theorems and their openness, flattening, and carrier
  arguments. The discussion now treats the two passages from smooth to
  normal to unibranch and restricts the nonnormal-target obstruction to a
  nonnormal target.
- Characteristic-zero subintegrality follows from the residue extensions of
  a finite universal homeomorphism being purely inseparable and hence
  trivial. It does not require a normal source, although the particular
  reflection corollary invoked in the assembly has that hypothesis.
- Compactness bounds each individual psh function; it does not bound an
  arbitrary family uniformly. The endpoint discussion now explains why
  divisorial comparison requires psh membership before it can be applied
  to a raw supremum.
- The increasing-net proof invokes divisorial nonnegligibility directly and
  records that this trace equality needs neither directedness nor the
  envelope property. Raw obstacle identities are separated from the
  envelope theorem's guarantee that their outputs are psh.
- A decreasing sequence uses the usual order on the natural numbers. The
  divisibility order is a directed order, with the factorial chain providing
  a cofinal sequential reduction on the positive integers.
- Two one-section functions on the projective line already have no common
  psh lower bound in degree one: domination forces two initial slopes at
  most minus one, contradicting the degree budget. This replaces the
  uncountable-field example and works over every algebraically closed field.
- The converse explicitly transfers the envelope property to positive
  scalar multiples of the ample class before invoking birational reflection.
  Projectivity is retained in the substantive implications of the
  four-way characterization.
- The smooth-curve criterion explicitly requires upper semicontinuity, a
  finite trivial-valuation value, and endpoint values equal to ray limits.
  The centre formula excludes the zero parameter, and normalization endpoint
  notation is in the correct analytic space.
- The explicit cusp-envelope candidate and maximality argument establish
  existence directly on the normalization; psh reflection transports the
  greatest competitor. The low-slope parameter range is nonnegative.
  A least upper bound need not belong to the original family.
- The historical comparison removes two restrictions relative to the
  addendum, since that addendum already covers all real classes. The source
  note now gives the exact arbitrary-class obstacle locators in the addendum.

The node, cusp, pole, nonattainment, and exponential-envelope calculations
were rederived. An auxiliary arithmetic check passed 2,519 comparisons:
exact rational cusp-envelope values for slopes 0, 1, 3, 4, 5, and 10 and three
positive transition lengths; the cusp-semigroup presentation for every
integer from 2 through 101; and the exponential contact/minimum calculation
at and around the transition at log 2. These checks supplement the convexity,
maximality, endpoint, and degree-budget arguments; they do not replace them.

## Direct source interfaces

The following primary versions were consulted, including the rendered source
pages containing the envelope and obstacle results:

| Source | Interfaces checked |
| --- | --- |
| Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, Ann. Fac. Sci. Toulouse 31 (2022), 647--836, [published PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf) | Example 4.13; Corollary 4.17; Theorem 4.22; Theorem 5.6; Lemma 5.9; Theorems 5.11 and 5.12; Lemma 5.13; Remark 5.15; Lemma 5.17, Corollary 5.18 and Lemma 5.19; Theorem 5.20. |
| Boucksom--Jonsson, *Addendum*, Ann. Fac. Sci. Toulouse 33 (2024), 405--417, [published PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1775.pdf), bibliography key `BJ22b` | Theorem A; Lemma 1.2; Lemma 1.3; Corollary 1.4. The arbitrary-class obstacle calculus is a published input; smoothness and the characteristic-zero-or-dimension-at-most-two alternative remain in Theorem A. |
| [Stacks Project Tag 035S](https://stacks.math.columbia.edu/tag/035S), Lemma 29.55.11 | Finiteness of normalization for a Nagata scheme; applied to a variety over a field. |

Downloaded source SHA-256 values:

- Published 2022 paper:
  `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.
- Published 2024 addendum:
  `cb792f775cbbc2fa7554af6a7e6712e59b10c95b7c2245215f640748abe3647f`.
- Stacks HTML snapshot:
  `bde1726812d3ba4de42e4e31ef36d984b91ea5276ac35ca490a1f1c50f8a3fcc`.

The source downloads are local reference material, not replacements for the
repository's frozen supplied sources or dated release records. This is a
direct chapter and primary-source audit, not an independent-agent or
exact-current model-verifier verdict.

## Mechanical and rendered verification

The scoped house review checked hypothesis signatures, notation, proof
structure, obstacle domains, semantic labels, attribution, and the book's
math-delimiter convention. A limited mechanical scan, run before and after
rendered review, found no unlabelled reusable environments, proofless formal
assertions, legacy inline delimiters, double-dollar displays, or unresolved
TODO/FIXME/TBD markers. Descriptive titles and the established label
namespaces were retained. The legacy standalone Mingchen writing-audit
executable was not present in the repository or available skill environment;
this review does not reproduce or assert its historical warning counts.

From `manuscript/`, the reference checker, its regression suite, and the
open-problem inventory checker passed:

```text
python3 editorial/tools/refcheck.py
python3 -m unittest discover -s editorial/tools -p test_refcheck.py
python3 editorial/tools/check_open_problem_inventory.py
```

The final reference closure has 425 inputs and 12,028 labels, with zero
missing inputs, duplicate labels, dangling references, or structural defects.
All six regression tests pass. The inventory remains 42 active atoms in 12
Chapter 72 environments, with tiers T1=0, T2=3, T3=7, T4=15, T5=17.
`git diff --check` passes. The scoped scan and reference check were repeated
after rendered review.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds. Missing font dependencies were restored in a workspace-local
TeX tree from the frozen TeX Live 2025 archive. The final PDF has 4,106 pages
and 19,202,090 bytes. SHA-256:
`eae448686e661c97d70f422c28b14dfbf859dfd4cd60653c39d1b50f93e6c677`.
The final chapter source SHA-256 is
`e945955113b55ec7989217126946c43d2a32702067633b565213b10d4a9d1c70`.

The final log has zero unresolved references or citations, missing glyphs,
rerun requests, emergency stops, or fatal errors. Chapter 45 has zero overfull
boxes and zero LaTeX/package warnings. The complete book has 24 overfull
boxes outside Chapter 45 and 13 duplicate PDF destinations in Chapter 70.
Earlier checkpoints recorded two overfull boxes under their build setup;
this restored font environment is not a byte-identical reproduction of those
snapshots, and no claim of a globally clean layout is made.

All fifty Chapter 45 pages, physical 2595--2644 (printed 2525--2574), were
scanned, together with the Chapter 44 closing page 2593, its blank verso 2594,
and the Chapter 46 opening at 2645. The altered mathematical passages were
also inspected at full resolution; late changes on physical pages 2599,
2629, and 2641 were re-rendered from the final PDF. No chapter clipping,
overlap, bad glyph, formula overflow, or hierarchy defect was found.

The generated full book and chapter excerpt are local review artifacts.
The frozen release artifacts and dated checksum ledgers are unchanged.
