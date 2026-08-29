# Independent exact-byte audit: P17.1 finite-level reduction, revised3

Date: 29 August 2026

Verdict: **PASS**.

- Critical mathematical errors: **0**.
- Verification or source-locator gaps: **0**.
- Hash, scope, algebra/sign, edition-concordance, compile, and layout defects:
  **0**.

The packet remains quarantined.  This audit neither submits it to production
nor authorizes live-manuscript integration.

## Frozen artifacts audited

~~~text
11b559989d5d79737c1b2e37e819ec4dc11fbc0baf704a1dd8f3c4427f6ee4ae  p171_closed_immersion_reduction_statement_revised3_20260829.tex
5c5b7561549f4feecadd5677dd54f14f98a02cecf76502e251fdb2ef9219697d  p171_closed_immersion_reduction_proof_revised3_20260829.tex
a36e2cf83a8cf89c1f4dfadcec2bf1d9521bdaa9639f91273c7c9d7b7c4e179f  p171_closed_immersion_reduction_compile_revised3_20260829.tex
0e6bf326b0f25de682d95e96189e4fdeb8b607219d8711faf7c483806276d6c1  p171_closed_immersion_reduction_compile_revised3_20260829.pdf
9409c9cfb44f9195d47b67ced32ffeaf50fd7c1902b96422de0e665616a77a5b  p171_chen_moriwaki_edition_map_frozen_revised3_20260829.md
4f735ee3da8875d5213db57c1528252ace0c9dc8bf3c8830bdaa29c8b34fc1af  p171_closed_immersion_reduction_repair_ledger_revised3_20260829.md
~~~

All six hashes were recomputed independently and match the frozen manifest.

## Exact repair and provenance check

The revised2-to-revised3 comparison contains no additional mathematical
change.  Apart from revision identifiers and corresponding harness filenames,
the only substantive replacement is the source locator

> paragraph following Definition 8.7

by

> paragraph following Example 8.10.

The latter is exact: Lemma 8.8 and Examples 8.9--8.10 intervene after
Definition 8.7, and the required symmetric multilinear extension to
continuous dpsh metrics is stated in the paragraph immediately following
Example 8.10.  Revised2 therefore remains rejected provenance, while revised3
closes its sole verification gap.

## Mathematical and source audit

The source hypotheses agree with Pille--Schneider: the base is an integral
Banach ring, and the morphism is an \(n\)-dimensional projective scheme over
that base, with flatness imposed exactly where the fibrewise measure statement
is made.  The tropical Fubini--Study and dpsh terminology used by the packet
matches the cited definitions.  No unproved purity, reducedness, or
equidimensionality hypothesis is silently inserted.

The all-complete-valued-field multilinearity is supported by
Boucksom--Eriksson Proposition 8.5, Definition 8.7, and the paragraph following
Example 8.10.  The Deligne-pairing change-of-metric step is supported by
Theorem 8.16 and formula (8.9).  Pille--Schneider Proposition 4.2 is correctly
treated as a non-Archimedean-only input and is not used as the all-field
anchor.

The Segre--Veronese construction gives the asserted closed immersion, and the
pullback metric has the stated maximum identity.  Polarization yields the
correct \(2^n\) signed Monge--Ampere terms.  Iterating the change-of-metric
formula yields the correct \(2^{n+1}\) signed Deligne-pairing weights, with no
sign or normalization mismatch.  The construction is finite and uniform under
base change in precisely the stated sense.

All 12 entries of the two-edition Chen--Moriwaki concordance were checked, as
was the firewall explaining that version-1 Proposition 3.9.7 is only the
special regular-curve comparison and is not a general relative identity.

## Scope audit

The packet proves only a finite signed closed-immersion expansion.  It does
not construct a relative resultant or Chow form, identify the fibrewise
expression with such an object, prove continuous assembly over the Banach
base, solve Pille--Schneider Question 4.9, or retire P17.1.  Its scope warning
is therefore accurate and fail-closed.

## Independent compile and rendering check

The exact harness was compiled independently.  The rebuilt PDF has SHA-256

~~~text
ab3c953fe6127b7b2040f92381d9331ba4ba68b193ab33f02aef28dbc5b74070
~~~

The final log has zero warnings and zero errors.  The output has three A4
pages and empty Author metadata.  Extracted text and all three independently
rendered pages agree with the frozen PDF; no clipping, overflow, or visual
defect was found.

## Gate

The exact revised3 statement/proof pair is eligible for a production
gpt-5.6-sol/xhigh Rethlas submission solely as a quarantined finite-level
reduction.  It remains ineligible for live integration unless the separately
archived production response is `final/correct`, binds to the exact proof
digest above, and has empty critical-error and gap arrays.
