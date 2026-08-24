# Part I post-expansion mathematical and primary-source audit (23--24 August 2026)

## Scope, method, and source firewall

This audit covers frontmatter/part1_intro.tex and Chapters 1--8 after the
post-expansion rewrite. It is an independent mathematical-correctness,
normalization, example, and primary-source audit. It introduces no new
mathematical result. Every change below either repairs a computation, narrows
a statement to the hypotheses supported by its proof and source, or makes an
imported theorem visibly external. Two independent chapter-block reviews
were reconciled with a final line-by-line normalization pass.

The author's Deligne-pairing paper arXiv:1710.09731 is excluded completely.
No statement, proof, citation, or indirect dependency in the audited files
uses it. The bibliography and all files outside the stated scope were left
untouched.

The Part I introduction was reviewed and required no textual change. All
eight chapter files were revised.

## Corrections integrated

### Chapter 1: the four entrances

- The Gauss seminorm at an arbitrary positive real radius is now proved
  multiplicative by passing to the associated graded ring for the real
  weight. The former instruction to rescale the radius into the value group
  was invalid when the radius is not rational over that group.
- An unsupported claim that a displayed ideal potential necessarily had
  infinite energy was removed. Energy is not defined at this stage of the
  book and its finiteness depends on later hypotheses.
- The two-break toric Fubini--Study weight is always described as a
  continuous semipositive real-weight metric. It is called a rational model
  metric only when its break parameter belongs to
  $v(K^\times)\otimes_{\mathbf Z}\mathbf Q$.
- The preview comparison between CLD Chern products and Chambert--Loir
  measures is restricted to a discretely valued field, a proper normal
  pure-dimensional generic fibre, and one common proper flat normal model.
  If the model line bundles extend $L_i^{\otimes m_i}$, the proof now uses
  the rational first Chern classes
  $m_i^{-1}c_1(\mathfrak L_i)$ and includes the indispensable factor
  $(m_1\cdots m_n)^{-1}$ both in the atomic measure and in the inductive CLD
  computation. The two deep CLD inputs are explicitly attributed to CLD,
  Theorem 18.5.5 and Proposition 18.5.8.

The sign convention remains

\[
                  \varphi_D=-\log|f_D|=v(f_D),
\]

so an effective vertical divisor gives a nonnegative potential and twisting
the norm by $\mathrm e^{-\varphi_D}$ makes the norm smaller.

### Chapter 2: valuations and semivaluations

- Every additive valuation and semivaluation now satisfies
  $v(0)=+\infty$, with the corresponding multiplicative convention
  $|0|=0$. Boundary faces of monomial cones are treated as semivaluations
  with nonzero support, not as valuations of the function field.
- The quasimonomial construction is based at a regular codimension-$r$
  point, uses a full regular system of parameters, and is defined through
  the associated graded expansion (or, in the equicharacteristic complete
  case, a coefficient field). The former description did not cover the
  stated generality.
- The terminology now separates a divisorial valuation up to arbitrary
  positive real rescaling from the rationally scaled divisorial points used
  in the rational model subspace. The unsupported converse characterization
  of all rank-one Abhyankar valuations was deleted.
- The irrational monomial example is identified as a point of a normalized
  slice of a monomial cone, not as an interior point of a one-dimensional
  rational skeleton edge.
- The valuation gallery distinguishes real-valued Berkovich points from a
  lexicographically ordered rank-two valuation. The latter is not a point,
  nor a limit of points, in the real-valued Berkovich topology. The
  irrational monomial valuation remains approximable by rational
  quasimonomial ones.
- The linear-growth discussion for semivaluations now keeps supports and
  local frames visible instead of evaluating rational functions outside
  their domains.

### Chapter 3: models

- Over a densely valued field, special-fibre components of formal models are
  handled through reduction tubes and Shilov boundary points. The formula
  $b_E^{-1}\operatorname{ord}_E$ is used only in the discrete normal
  algebraic-model setting where $b_E$ and a uniformizer exist.
- An admissible ideal is required to be coherent and open. The ideal
  $K^{\circ\circ}$ is no longer offered as a coherent example in a dense
  value group.
- Two nonnormal-model examples were repaired without an implicit square-root
  or characteristic assumption: nonnormality is detected by the
  two-dimensional embedding dimension of the relevant height-one local
  ring, hence by failure to be a DVR.
- A line bundle on the generic fibre is extended itself after taking a
  difference of sufficiently positive extensions. Rational model metrics
  are now explained as rational weights or tensor-power normalizations, not
  as evidence that only a tensor power of the generic line bundle extends.
- The flattening statement is imported with the noetherian hypotheses of
  Stacks Project, Tag 0815. The model-availability ledger no longer hides
  the distinction between resolution over a field, relative resolution over
  a DVR, and alterations.
- A Kodaira fibre of type $I_n$ is used as an SNC polygon only for $n\geq2$.
  For $I_1$, the manuscript records the blowup needed to obtain an SNC model
  and the multiplicity-two exceptional component.
- The special-fibre total-mass calculation is stated on a normal model,
  matching the normalized component valuation used in its proof. A false
  converse about nefness descending from a pullback was removed.
- Normalization is performed only under an explicit finiteness hypothesis;
  the text distinguishes normalization of a model with fixed normal generic
  fibre from replacement of a nonnormal generic fibre by its normalization.

### Chapter 4: Berkovich spectra and analytification

- The trivially valued affine-line introduction now describes the genuine
  rescaling rays used later and does not claim a classification of every
  point before the relevant hypotheses are imposed.
- Banach algebras with arbitrary real polyradii are called generalized
  $K$-affinoid algebras; they are not silently treated as strictly
  $K$-affinoid.
- Compactness of the analytification of a proper scheme is imported with the
  exact scope of Berkovich, Theorem 3.4.8, rather than justified by an
  abbreviated argument that did not prove properness of the analytic map.
- The four Berkovich affine-line types, completed residue fields, reduction
  fibres, and the standard annulus were checked against the conventions
  $v=-\log|\cdot|$ and $|\cdot|=\mathrm e^{-v}$. No numerical change was
  required in those computations.

### Chapter 5: skeleta and retractions

- On a stratum with component multiplicities $b_j$, the integral-affine
  constants are $g_J^{-1}\mathbf Z$, where
  $g_J=\gcd(b_j:j\in J)$, and the slope lattice is
  $\mathbf Z^J/\mathbf Z(b_j/g_J)_{j\in J}$. The proof now derives this
  lattice rather than using the reduced-fibre formula in the nonreduced
  case.
- Continuity of the retraction is proved by gluing on a finite closed cover;
  the former assertion that the relevant reduction tubes formed an open
  cover was false.
- Blowing up a node with endpoint multiplicities $b,b'$ inserts the weighted
  mediant $(bt+b't')/(b+b')$. Iterated blowups give the Farey points; the
  text no longer calls the sequence dyadic. The first new points are
  $1/2$, then $1/3$ and $2/3$.
- In the two-dimensional triangle, barycentric refinement is produced by
  blowing up the deepest stratum first and then the strict transforms of the
  one-dimensional strata. The former order did not give the claimed fan.
- Relative resolution is now isolated as an explicit external hypothesis
  (R). Hironaka's field-form theorem is not presented as a proof over
  $k[[t]]$. Refinement to irreducible strata uses the precise cofinality
  result BFJ, Theorem 3.15, rather than an unsupported termination argument.
- The inverse-limit embedding uses BFJ, Corollary 3.2, for separation by
  model functions and the topology. On a fixed model the map
  $D\mapsto\varphi_D$ is injective, and
  $\varphi_{D+c\mathcal X_s}=\varphi_D+c$; fibre multiples become invisible
  only after an explicitly declared quotient by constant functions. On a
  one-dimensional cell this quotient is by the actual subgroup of
  integral-affine constants, not automatically by $\mathbf Z$.
- The image of a model retraction consists of the rational model functions
  that factor through that retraction. Piecewise-affine functions whose
  bends require a refinement are not assigned to the lower model.
- The strong deformation retraction is transparently imported from
  Berkovich, Theorem 8.1; local contractibility is kept as a separate
  consequence with its own scope.

### Chapter 6: model metrics and Chambert--Loir measures

- The standing geometric-connectedness hypothesis is now visible where it
  is used to identify global units and constants.
- For two rational model metrics on the same line bundle, the proof chooses
  a common tensor power $M$, writes the vertical Cartier divisor as $D_M$,
  and uses the rational divisor $D=M^{-1}D_M$. Thus

  \[
       \|\cdot\|_2=\|\cdot\|_1\mathrm e^{-\varphi_D},
       \qquad
       \varphi_D=M^{-1}v(f_{D_M}).
  \]

  The former formula omitted $M^{-1}$. Also, only a scalar $h\in K^\times$
  gives a purely vertical principal divisor and a constant model function;
  a general $h\in K(X)^\times$ has a horizontal part.
- The tensor-product formula for weighted Fubini--Study metrics now averages
  the two weights with coefficients $m/(m+m')$ and $m'/(m+m')$. A real
  corner is an integral model metric only when its break lies in the value
  group, a rational model metric when it lies in the rationalized value
  group, and otherwise only a real-weight semipositive Fubini--Study metric.
- The formal/algebraic/PL comparison is imported with the precise results of
  Gubler--Martin, Theorems 1.1--1.2, Propositions 2.10 and 2.15, and Theorem
  2.17. The closedness theorem is imported as Gubler--Martin, Theorems 1.3
  and 5.5, with the base-ideal construction attributed to Proposition 5.1.
  The manuscript no longer asserts that the set of model data is countable.
- If $\mathcal L_i|_X\simeq L_i^{\otimes m_i}$, the mixed
  Chambert--Loir measure is now

  \[
    \frac1{m_1\cdots m_n}
    \sum_Y b_Y
      \bigl(c_1(\mathcal L_1|_Y)\cdots
            c_1(\mathcal L_n|_Y)\bigr)\,\delta_{x_Y}.
  \]

  Its model-independence proof follows the unique strict transform of each
  old component, preserves its multiplicity and normalized divisorial point,
  and kills exceptional components by the projection formula. The total
  mass is exactly $(L_1\cdots L_n)$, with no probability normalization. The
  vertical-intersection identity contains the same denominator, so the
  factors $b_Y$ cancel precisely against
  $\varphi_D(x_Y)=a_Y/b_Y$.
- The continuous extension is restricted to a discretely valued field and
  an integral projective pure-dimensional scheme. The imported input is
  Chambert--Loir, Proposition 2.7 and Sections 2.3--2.4. The displayed
  Cauchy estimate is explicitly described as the form extracted from that
  proof; the previous attempted replacement by positivity of a lower-degree
  signed object was invalid.

### Chapter 7: compactness, limits, capacity, and pushforwards

- The binary-expansion example now includes the endpoint $t=1$.
- In the pointwise-versus-uniform convergence example, the finite sets
  genuinely exhaust a fixed countable dense subset. An impossible claim of
  producing a neighbourhood basis at every point without generating the
  topology was removed.
- The capacity counterexample uses the finite space $\{0,1\}$ and
  $\operatorname{Cap}(A)=|A|^2$, so every assertion is directly checked.
- The concavity example uses $\sqrt{x}$, not the convex function
  $-\sqrt{x}$.
- Pushforward and tail formulas for a concave transform $G$ that equals
  $-\infty$ on a null set now use a finite Borel representative
  $\widetilde G$. The proof states why the pushforward and moments are
  independent of the chosen values on the null set; expressions such as
  $\chi(-\infty)$ are no longer formed.

### Chapter 8: worked examples

- Two successive blowups of the standard projective-line model produce a
  two-legged path with the original Gauss point at its centre, not a tripod.
  The symmetric model weights are $-\tfrac12$ times the two hat functions,
  consistent with $\|\cdot\|=\|\cdot\|_0\mathrm e^{-\varphi}$.
- A point of the apartment arising from an integral model requires its
  parameter in $v(K^\times)$; rational model points use
  $v(K^\times)\otimes\mathbf Q$. For a two-variable monomial valuation,
  being divisorial up to real scaling is equivalent to a rational slope,
  whereas being a rationally normalized divisorial point additionally fixes
  a rational scale.
- For $\min\{2w_1,3w_2,c\}$, equality with the untruncated function holds
  on $\min\{2w_1,3w_2\}\leq c$; the function is constant only when both
  monomial values are at least $c$. The resulting sequence decreases to the
  untruncated potential with the stated sign.
- The trivially valued curve space is not called a locally finite tree.
  The worked piecewise-affine functions are instead described as having
  nonzero slope on only finitely many rays.
- The toric Chambert--Loir/real Monge--Ampere comparison is restricted to
  the complete discretely valued toric model setting of
  Burgos Gil--Philippon--Sombra, Theorem 5.70. The manuscript displays the
  reflection dictated by its sign convention and the factor $n!$.
- The Hirzebruch tropical curve has four unbounded edges. On
  $\mathbf P(1,1,2)$, $\mathcal O(1)$ is the ample rank-one reflexive
  $\mathbf Q$-Cartier sheaf, while $\mathcal O(2)$ is Cartier.
- In the three-vertex chain, the text now says “a symmetric” solution: all
  triples $(0,a,0)$ with $-1<a<0$ yield three positive atoms. The example
  no longer claims uniqueness that its equations do not imply.
- The slope-formula, toric, weighted-projective, base-change, and atomic
  chain examples were recalculated atom by atom. Every displayed
  Chambert--Loir measure now has the generic intersection number as total
  mass, and every displayed graph Laplacian has total mass zero.
- An unverified assertion that Thuillier's text contained a typo was removed;
  only the manuscript's explicit comparison of sign and length conventions
  remains.

## Primary-source checks completed

- The toric comparison in Chapter 8 matches the published Theorem 5.70 of
  Burgos Gil--Philippon--Sombra (Theorem 4.7.4 in the arXiv version): the
  field is complete with nontrivial discrete valuation, the fan is complete,
  the toric metric is a semipositive model metric, and the tropical
  pushforward is $n!$ times the real Monge--Ampere measure.
- Gubler--Martin's closedness statement in Chapter 6 has the scope of their
  Theorem 1.3 and is supplied by Theorem 5.5; convergence on divisorial
  points is the relevant pointwise hypothesis. The algebraic/formal/PL
  comparisons and density statements use the exact numbered results listed
  above.
- Chambert--Loir's continuous extension is Proposition 2.7, based on the
  local-height recursion in Sections 2.3--2.4. It is not presented as an
  elementary positivity argument.
- The CLD/model-core comparison records the precise normalization factors
  and names the two CLD results used in its proof.
- Berkovich properness and the strong deformation retraction are imported
  rather than reproved in greater scope. BFJ's cofinality and separation
  results are likewise named at their exact uses.
- Stacks Project tags are used only where their noetherian and finiteness
  hypotheses are visible. No new bibliography entry was added.

## Remaining provenance risks (reported, not filled speculatively)

These are not detected contradictions in the revised mathematics. They are
places where the present bibliography or prose does not yet give the exact
primary-source pointer demanded by a fully exhaustive provenance standard.

1. The explicit type-IV Puiseux example in Chapter 4 uses
   Newton--Puiseux and algebraic closedness of the completed algebraic
   closure without a precise primary theorem citation.
2. Chapter 4 gives correct standard statements on base-change surjectivity,
   the fibre
   $\mathcal M(\mathcal H(x)\widehat\otimes_K L)$, and proper GAGA, but
   presently points only to Berkovich's general Section 3.4 rather than to a
   separate exact theorem number for each assertion.
3. The jump from the explicit affine-line disc order to the global
   topological-tree statement would benefit from an exact primary theorem
   citation.
4. Relative resolution and principalization for models finite type over
   $k[[t]]$ are not consequences of Hironaka's field-form theorem alone.
   Chapter 5 now marks the required relative statement as external
   hypothesis (R), but Chapters 3 and 5 still need a precise source if this
   input is to be quoted rather than assumed. No source was invented.
5. The displayed Chambert--Loir Cauchy bound is a faithful reformulation of
   the proof of Proposition 2.7, not the verbatim statement of that
   proposition. A future source note could point to the exact page or
   equation in the edition used.
6. The removal of base change in the curve slope formula and the brief
   Alexandrov total-mass argument in Chapter 8 have complete arguments in
   the manuscript, but would benefit from more precise primary pointers.

None of these items authorizes enlargement of a theorem's scope. Until a
precise source is supplied, the manuscript's visible hypotheses and proofs
are the authority.

## Formal and build verification

The final audited files were checked after all corrections.

- Formal-statement parser: 171 theorem, lemma, proposition, or corollary
  environments; zero unclosed statements, zero statements without an
  immediately following proof, and zero empty or unclosed proofs.
- Reference style: zero raw \ref or \autoref; equations are referenced with
  \eqref, while objects use \cref or \Cref.
- Structural scan: zero exercise environments, zero duplicate labels inside
  the audited files, and zero occurrence of arXiv:1710.09731 or a Deligne
  pairing dependency.
- Citation-key scan: 69 distinct keys used, 499 keys available in the two
  bibliography files, zero missing keys.
- Notation scan: differentials use the upright macro \rd, and the
  exponential and imaginary constants use \rme and \rmi where they occur.
- Targeted pdflatex build with only the Part I introduction and Chapters
  1--8 included: exit status 0; 348-page PDF; zero LaTeX, package, or fatal
  errors, zero overfull boxes, zero multiply defined labels, and zero
  undefined-reference warnings. The isolated build has no generated bbl,
  so it reports undefined-citation warning lines; the independent
  citation-key scan above confirms that every cited key exists. Hyperlink
  destination warnings for excluded chapters are an expected consequence
  of includeonly with the full-book auxiliary files.
- chktex: zero syntax errors. Its 1,933 warnings are overwhelmingly the
  project's deliberate mathematical and house-style conventions (author
  name dashes, cleveref spacing, table rules, and interval punctuation), so
  they are recorded rather than mechanically applied.

The targeted PDF is
/tmp/nappt_part1_postexpansion/part1_postexpansion_check.pdf.

## Final file fingerprints

SHA-256 after the audit:

    aeb10a9d78a3c7adc3ef818b4067ab8d67a1ae3d46f0d2a967a7357bf45b7ec0  frontmatter/part1_intro.tex
    f8f43607b2e118f4c3bd1ff8083617b83a57046c422b665c35030c820b32ec7a  parts/part1/ch01_four_entrances.tex
    3dfa283f26f7fa5beb2dd4b039532dfd41c0b2cc959d09c644830448aa729c91  parts/part1/ch02_valuations.tex
    2799b58ebe72927e7769079adc521db34c5507cef6fe7354f1bf894d3a42530d  parts/part1/ch03_models.tex
    11eb330d5dd0310d520e81cc6701aa6b706310bb3f92195f670f2a27acbe3b1c  parts/part1/ch04_berkovich.tex
    76c47909486f66289199e54369ecb5ba0c8bc4018efa205f534d1e44e25d318d  parts/part1/ch05_skeleta.tex
    d4c1f705df147735fe6db950ad7ce164f3c5913590b0f0c8199bbc55f15c7f02  parts/part1/ch06_metrics.tex
    8674f1986bb73433cae12880ff169b49102f3d74eb7787cbc911d84053ef6b0b  parts/part1/ch07_tools.tex
    c13bc57da126068095e6799de881ee9ded35e29179d147fd1950fc91e40a2e9f  parts/part1/ch08_examples.tex
