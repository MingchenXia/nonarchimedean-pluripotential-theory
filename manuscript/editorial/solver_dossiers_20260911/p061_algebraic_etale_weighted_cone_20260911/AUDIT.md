# P06.1 algebraic-etale weighted-cone audit

## Result

The packet turns a separated finite-type algebraic etale morphism over a
relative positive-weighted cone into the exact strict analytic
standard-etale chart required by the live weighted-cone tube theorem.  At a
source point over the zero section of a smooth algebraic base, every
classically pluriharmonic germ is therefore locally real-PL and
Gubler--Jell--Rabinoff harmonic.

## Structural checks

1. Stacks Tag 025C is used only after fixing the affine relative-cone target.
2. A principal open is chosen inside the image of the supplied open
   immersion; multiplying its defining polynomial by the derivative retains
   both localizations.
3. The target affinoid is a genuine relative weighted cone over a strict
   quasi-smooth affinoid neighbourhood in the smooth base.
4. Strict bounds on the algebraic standard-etale coordinate and its inverse
   put the chosen point in the ordinary interior of the constructed source
   affinoid.
5. The live `thm:p061-standard-etale-weighted-cone-tube` applies only after
   these three localization firewalls have been verified.

## Scope

The theorem covers only points mapping to the displayed zero section.  It
does not infer a chart for a general analytic etale morphism, a genuinely
log-etale morphism, a point away from the zero section, or an arbitrary
singular germ.  P06.1 remains active and the Chapter 72 atom count is
unchanged.

## Independent hostile review

GPT-6 Astra reviewed the exact live theorem, proof, source record, and
manuscript integration.  Its final verdict was PASS.  The review independently
checked Stacks Tag 025C and confirmed the open-immersion-only use, the
principal-open numerator step, the target and source interior arguments, the
derivative inverse, the quasi-smooth central-fibre input, and all stated scope
firewalls.  Its one clarification request---write the principal-open generator
as `P/(G')^N` before replacing it by its numerator---is incorporated in the
final proof.  A final reread after that repair again returned PASS.

## Mechanical verification

- Full `latexmk` build: PASS, 3638 pages.
- Undefined references: none.
- Undefined citations: none.
- Multiply defined labels: none; the new theorem label is unique.
- Open-problem inventory checker: PASS, 48 active atomic questions in 14
  formal Chapter 72 problem environments, tier counts `(0,5,9,17,17)`.
- `git diff --check`: PASS.
