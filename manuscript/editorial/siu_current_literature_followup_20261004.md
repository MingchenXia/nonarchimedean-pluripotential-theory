# Current Siu-related literature: bounded follow-up

Date: 4 October 2026, lookups at 21:39--21:41 UTC. This follows
the [repair-route dossier](bj22_siu_repair_routes_dossier_20261004.md).
The checks below concern exact versions and selected proof interfaces;
they are not an exhaustive erratum or current-literature search.

## Current-version and retrieval checks

The actual arXiv abstract page for
[2602.10800](https://arxiv.org/abs/2602.10800) lists v1 of 11 February
and v2 of 19 May 2026, with v2 current at this lookup.
Its title is *From complex to non-Archimedean geometry: an approach to
the YTD conjecture*, by Boucksom and Jonsson. The cached v2 introduction
was freshly read at lines 1--100, and its psh/envelope overview at
628--665. It treats the polarized smooth projective complex setting
and summarizes deep envelope results; these selected passages supply
no independent arbitrary-normal critical Siu proof. No fresh whole-paper
reading or later-publication clearance is asserted.

The actual arXiv page for
[2609.27610](https://arxiv.org/abs/2609.27610) lists only v1 of
23 September 2026 at this lookup. Wu's *On the local theory of
non-archimedean psh functions* is thus still the version inspected in
the [earlier scouting audit](recent_arxiv_scouting_audit_20261004.md).
Its abstract advertises a normal-variety envelope result; actual Theorem
7.1 has the geometrically-unibranch projective and equicharacteristic-zero
discretely/trivially-valued hypotheses recorded below.

Three arXiv search pages returned no results for the actual submitted
queries: `Siu Jonsson` in all fields; and the title-field queries
`Mixed differential calculus and Monge-Ampère equations on tropical varieties`
and `On solutions to tropical Monge–Ampère equations`.
The latter are the APW26a/b titles cited by Wu. These bounded negative
searches do not prove that a correction or a dependency manuscript does
not exist elsewhere, under another title, or on an author page.
The attempted Jonsson university homepage request failed with a proxy
403 tunnel response; no homepage or erratum-list reading is inferred
from it. Response bodies, dates, URLs, hashes and failures are preserved
in the ignored source cache and companion manifest.

## The main Wu proof route, separately from Appendix A

The earlier audit's Appendix A concerns do not alone describe every
dependency of the envelope theorem. This follow-up traced the actual
main route:

1. Theorem 7.1, actual pages 51--52, pulls a bounded-above family to
   a smooth resolution, uses independently known smooth envelopes,
   descends an usc function by Proposition 2.24, and invokes weak/global
   comparison Theorem 6.5. The first proof stage assumes a countable
   dense subfield; the second uses field descent and orthogonality.
2. Theorem 6.5, page 38, depends on local weak/regular comparison
   Theorem 6.3 and the upper logarithmic-growth and extension machinery.
3. Theorem 6.3's singular-stratum induction, pages 50--51, uses
   Proposition 6.14. Its norm/Runge proof invokes Lemmas 6.7--6.8.
4. Lemma 6.7 uses strict supports of Lemma 6.6. Its construction also
   invokes Lemma 3.4(3)'s rational-PL approximation. These cite APW26b,
   not merely the source's separate Appendix A comparison.

Thus the unacquired APW dependence also appears in the main theorem's
route. It is a precisely identified source gap in this audit, not a
proof that the underlying claims or Theorem 7.1 are false.

## Actual printed diagnostics and a constructive local replacement

Actual page 38 prints `chi_k(t') > l(t)` in Lemma 6.6. Together with
`chi_k(t)=l(t)`, this is contradictory when two contact points are
exchanged. The subsequent proof on page 39 uses `chi_k-l`, making the
intended supporting comparison `chi_k(t') > l_t(t')` visible.
The [explicit log-sum-exp dossier](extended_tropical_logsumexp_dossier_20261004.md)
gives a complete candidate calculation for that corrected local
ingredient: finite continuous values at all extended-coordinate faces,
strict touching supports, a uniform positive gap outside any contact
neighbourhood, and global decreasing rational-PL majorants. It uses
the classical entropy identity and carefully distinguishes local finite
affine supports from globally extended supports. It does not import
APW26b as an unread oracle or certify the later singular descent proof.
The explicit pullback also has affine FS approximants retaining the
coordinate-ring generators themselves. Its two-sided bound satisfies
both printed growth directions for this special function; this closes
that particular interface without changing either definition or
settling the growth comparison for arbitrary functions.

Actual page 12's Lemma 2.25 proof prints `-m phi` after normalizing
`phi<=0`; this is increasing and has the opposite sign from BJ22
Corollary 4.24's decreasing `m phi`. The source's constant-function
conclusion has a known correctly signed antecedent; this printed line
cannot itself justify decreasing closure.

Actual pages 47--48 use `delta/(2(gamma-1))` while declaring only
`gamma` a positive integer. The case `gamma=1` needs a separate
handling; the other-fibre sum is empty then, but the displayed bound
is undefined as written. The same gluing paragraph switches from a
`3g-1` contact set to a `Cg-delta` majorant without giving the stated
contact-set containment for the newly chosen constants. These are
additional normalization and scope checks still required in that
proof reconstruction. They are not counterexamples to the main theorem.

## Fresh reading scope and book decision

This follow-up freshly read the Wu extracted text at lines
480--850, 840--887, 1800--2148, 2300--2620 and 2655--2737,
with the output-truncated middle range recovered at 2480--2590.
Ten selected actual pages were viewed: 12, 14, 38--40, 47--48,
51--52 and 55. The bibliography's APW titles were additionally
read in extracted lines 2829--2833; earlier actual views of page 54
remain the dated scouting record. This is a targeted rereading, not
a new whole-paper audit, and does not clear every cited antecedent.

Keep Wu's general envelope claim outside the active manuscript until
the required corrected definitions, source dependencies, and complete
descent argument have been independently checked. The explicit local
construction is retained as a worked research candidate, not as a
new general theorem. All 425 active book inputs, the 86-page catalogue,
historical receipts and 42 open-problem statuses remain unchanged.
The critical `(SD)_k` input is still unresolved.
