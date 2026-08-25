# Integration blueprint: verified real toric current products

Date: 25 August 2026.

This blueprint records the natural live placement and all currently located
scope/ledger text affected by the production-verified P20.1 packet. It does
not itself edit a live chapter. The controlling receipt is
`rethlas_receipts_20260825/real_toric_numerical_dimension_round3_production_receipt.md`.

## 1. Mathematical result to integrate

For a maximal-compact-torus-invariant closed positive `(1,1)`-current \(T\)
in any pseudoeffective real class on a smooth projective toric variety, and
for an invariant Kähler form \(\omega\) with moment polytope \(Q\), set

\[
 \Delta(T)=\overline{\operatorname{dom}F_T^*}.
\]

With lattice-normalized mixed volume,

\[
 \int_X\langle T^k\rangle_{\mathrm{Cao}}\wedge\omega^{n-k}
 =\int_X\langle T^k\rangle_{\mathrm{np}}\wedge\omega^{n-k}
 =n!V(\Delta(T)[k],Q[n-k])
\]

for \(0\leq k\leq n\), with both degree-zero products equal to \(1\).
Therefore

\[
 \nu_{\mathrm{Cao}}(T)=\nu_{\mathrm{np}}(T)=\dim\Delta(T).
\]

The class-level formula is false and must not be inferred. On
\(\mathbf P^1\), \(T=\lambda[0]\) has current-level dimension zero while its
positive class has numerical dimension one; this remains a counterexample
for irrational \(\lambda\).

## 2. Natural chapter placement

The principal statement and full proof belong in
`parts/part5/ch55_okounkov_dh.tex`, immediately after
`thm:ok-toric-zero-mass` and before
`prop:ok-i-invariant-obstruction`. That location already develops Cao
dimension, toric Newton bodies, and the rational section-counting proof.

Integration should:

1. replace the present `rem:ok-toric-scope` by a transition explaining that
   the preceding theorem is the integral/rational algebraic proof and that
   the next theorem is the real-class analytic extension;
2. insert an **unnamed** theorem (no optional conventional name), with a new
   `thm:` label, carrying the exact verified statement, including the
   \(k=0\) convention;
3. adapt the complete frozen proof into book prose without changing its
   logical chain: one gentle quasi-equisingular approximation, Cao's
   polynomial identity after adding \(s\omega\), equality with the
   non-pluripolar mass in the Kähler perturbation, the local toric
   complex/real Monge--Ampère formula, the identity
   \(\Delta(T+s\omega)=\Delta(T)+sQ\), coefficient comparison, and the
   mixed-volume dimension criterion;
4. retain the old rational proof as a second, algebraic proof and a useful
   bridge to section growth; do not present it as proving the real-class
   extension;
5. include the Fubini--Study closure warning, the \(\mathbf P^1\)
   class/current counterexample, the genuinely irrational
   \(\mathbf P^1\times\mathbf P^1\) segment example, and the purely
   divisorial and smooth-Kähler boundary cases;
6. use `\Cref`/`\cref` for internal references and preserve every existing
   `\eqref`; use `\mathrm d`, `\mathrm i`, and `\mathrm e` in accordance
   with the book conventions.

Chapter 69 should not duplicate the long analytic proof. Keep
`thm:verified-toric-dimension` as the independently verified
integral/rational algebraic theorem, but revise
`rem:verified-toric-rationality` to say that the *proof just given* is
rational while the general current-level real-class theorem is proved in
Chapter 55. Cross-reference the new theorem. This preserves both existing
receipts rather than silently changing their historical proof objects.

## 3. Definitions and firewalls that must accompany the theorem

- **Current versus class:** define
  \(\nu_{\mathrm{Cao}}(T)\) and \(\nu_{\mathrm{np}}(T)\) as the largest
  \(k\) with nonzero current-level product class. Never write the result as
  \(\nu(\{T\})=\dim\Delta(T)\).
- **Real versus transcendental:** on a smooth projective toric variety,
  \(H^{1,1}(X,\mathbf R)=N^1(X)_{\mathbf R}\). Say “irrational real divisor
  class”, not “genuinely transcendental toric class”.
- **Closed Newton body:** use
  \(\overline{\operatorname{dom}F_T^*}\), equivalently the closure of the
  subgradient image. An unclosed gradient image is wrong even for the
  Fubini--Study function \(\log(1+\mathrm e^x)\).
- **Multiplier-ideal conventions:** record
  \(\mathcal I_{\mathrm C}(a\varphi)=
    \mathcal I_{\mathrm B}(2a\varphi)\), and use
  \(\lambda=2m\), \(\lambda'=2m(1+\delta)\). Do not claim the written
  definitions are identical.
- **Degree zero:** explicitly state
  \(\langle T^0\rangle_{\mathrm{Cao}}=
    \langle T^0\rangle_{\mathrm{np}}=1\).
- **Normalization:** retain
  \(\mathrm d^c=(2\pi\mathrm i)^{-1}(\partial-\bar\partial)\), norm
  weights, lattice covolume one, and
  \(\int_X\omega^n=n!\operatorname{vol}_M(Q)\).
- **Novelty:** the targeted literature search found no source stating the
  exact real-class Cao/non-pluripolar mixed formula, but that is not a
  priority proof. Describe it as a dated, Rethlas-verified book derivation
  unless a separate priority review is completed.

## 4. Primary-source map

Convert the packet's hash attestations into normal citations while retaining
the exact scopes.

- Cao, Definitions 2--4: quasi-equisingular approximation and the
  arbitrary-current Cao product. Cao Proposition 4.4 remains relevant only
  to the older rational line-bundle proof.
- *Singularities in Global Pluripotential Theory*, Definitions 1.6.1 and
  1.6.5, Theorems 1.6.2, 6.2.1, and 7.1.1, and Example 7.4.1: gentle
  regularization, mass continuity, and toric \(\mathcal I\)-goodness.
- Coman--Guedj--Sahin--Zeriahi, Lemmas 2.1--2.2: convex conjugates and the
  **local** torus complex/real Monge--Ampère identity. Do not enlarge their
  global ample-class theorem to the present real-class setting.
- Boucksom--Eyssidieux--Guedj--Zeriahi, Propositions 1.4 and 1.6: locality,
  multilinearity, global non-pluripolar products, and noncharging of
  pluripolar sets.

The receipt records the four exact archived PDF hashes.

## 5. Live source text to change

The following locations were located on the 25 August pre-integration tree.
Line numbers are navigation aids and must be refreshed before editing.

| File | Current location | Required change |
|---|---:|---|
| `parts/part5/ch55_okounkov_dh.tex` | 1524--1531 | replace the “Exact scope” remark by the general theorem transition and insert the full verified theorem/proof before the no-go proposition |
| `parts/part6/ch69_verified_extensions.tex` | 645--652 | revise the rationality-boundary remark: the local proof is rational, but the general current-level real theorem now exists in Chapter 55 |
| `parts/part6/ch69_verified_extensions.tex` | 871--884 | remove the irrational-real toric item from the boundary ledger |
| `parts/part6/ch72_major_open_problems.tex` | 1946--1969 | remove the `problem` environment `prob:frontier-real-toric`; replace it, if historical continuity is desired, by a short resolved-note cross-reference outside any `problem` environment |
| `frontmatter/part6_intro.tex` | 86--91 | retain the historical rational receipts but add the new real-class analytic theorem/receipt and remove the statement that Part VI excludes irrational real toric classes |

No other live occurrence of `prob:frontier-real-toric` was located. Run a
fresh reference scan before deleting its label.

## 6. Editorial ledgers to update

These are mutable status records and presently describe P20.1 as open or
the toric result as rational-only.

| File | Current location / token | Required change |
|---|---|---|
| `editorial/major_open_problem_program.md` | active-count paragraph near lines 48--51; `OP-20` near 361--375 | retire OP-20, record the class-level disproof and current-level solution, and decrement the counts |
| `editorial/open_problem_atomic_inventory_20260824.md` | P20.1 near 287--293; T1 queue near 316 | remove P20.1 and remove it from the queue; T1 loses one atom |
| `editorial/chapter_status.md` | Chapter 69 row; Chapters 70--72 row; count statements near 113 and 136 | add the new receipt and change rational-only/open counts |
| `editorial/mathematical_revision_log.tex` | toric scope near 66--78 and retained-results list near 128--136 | append a dated correction; do not rewrite the historical truth of older receipt scopes |
| `editorial/rethlas_verified_results.md` | Chapter 55/69 toric entries near 300--340 | add a separate real-class theorem entry and explain that it supersedes only the old frontier, not the older packets' scopes |
| `editorial/part6_postexpansion_audit_20260824.md` | frontier counts near 18--19 and 232 | add a dated delta or refresh counts after integration |
| `editorial/rethlas_r3_report.md` | count statements near 72 and 1568 | add a dated post-report delta rather than falsifying the historical R3 snapshot |

If P20.1 is the only environment retired between recounts, the literal delta
is:

- Chapter 72: \(20\to19\) problem environments;
- book-wide including Chapter 71: \(21\to20\) problem environments;
- active atoms: \(63\to62\);
- T1 queue: \(3\to2\), with `P21.1` then `P01.1`.

Other agents may resolve additional atoms before integration, so recompute
the absolute totals from the then-current tree; the invariant contribution
of this result is exactly minus one environment and minus one atom.

## 7. Frozen historical artifacts not to rewrite

The following contain rational-only firewalls that were true of their exact
submitted objects. They are audit evidence, not stale mutable prose, and
must remain byte-for-byte unchanged:

- `editorial/rethlas_packets_20260824/ch55_toric_zero_mass_*`;
- `editorial/rethlas_packets_20260824/ch69_verified_toric_dimension_*`;
- `editorial/rethlas_receipts_20260824/ch55_toric_zero_mass_cao_attested_receipt.md`;
- `editorial/rethlas_receipts_20260824/ch69_verified_toric_dimension_exact_current_receipt.md`;
- all `real_toric_numerical_dimension_failed_gate_round1_*` files;
- all `real_toric_numerical_dimension_round2_timeout_*` files;
- all frozen round-3 packet and receipt artifacts.

New mutable ledgers should say that the old packets remain correct in their
restricted scope and that the independently verified analytic theorem now
removes the irrational current-level frontier.

## 8. Post-integration gates

1. Extract the exact live theorem and proof and compare the mathematical
   content against the frozen round-3 files. Any substantive change needs a
   new Rethlas run.
2. Check that all new internal references use `\Cref`/`\cref`, every
   displayed-equation reference uses `\eqref`, and no optional conventional
   theorem/lemma name was introduced.
3. Run the chapter-focused build for Chapters 55, 69, and 72, then the full
   book build; reject undefined references/citations, duplicate labels,
   overfull boxes, and index failures.
4. Recount literal `problem` environments and active atoms after all
   concurrent integrations.
5. Verify that no open-problem list or frontmatter sentence still calls the
   irrational current-level case open, and that no prose asserts the false
   class-level identity.
6. Record the live-file hashes and byte-exact extracts in a separate
   post-integration manifest. The present production receipt alone does not
   certify those future bytes.
