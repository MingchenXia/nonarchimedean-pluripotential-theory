# P06.1 standard-etale weighted-cone tube audit

## Result and scope

The packet proves local real-PL regularity, hence Gubler--Jell--Rabinoff
harmonicity, for classically pluriharmonic germs at central-fibre points of a
displayed strict standard-etale Tate presentation over a relative
positive-weighted cone.  The central standard-etale fibre must already have
the local pluriharmonic real-PL property; a quasi-smooth original base is a
sufficient condition.

The proof combines quotient-Gauss-norm contraction of the cone variables,
the existing contractive standard-etale Newton lemma, and the previously
verified relative weighted-cone descent theorem.  The explicit example uses

`T^2-T-x=0,  (2T-1)U-1=0`

over the cubic cone `x^3+y^3+z^3=0`; the first equation is not homogeneous for
strictly positive weights on `T` and `x`.

## Firewalls

- Only central-fibre points in the displayed strict affinoid presentation are
  covered.
- No standard-etale presentation or uniformization is asserted for an
  arbitrary singular germ.
- The example does not claim that the germ has no alternative weighted
  presentation or that it is intrinsically new.
- The Jacobian argument proves quasi-smoothness.  It deliberately does not
  erase the possible relative boundary of the Tate domain or assert
  boundaryless analytic etaleness.
- P06.1 remains active; the Chapter 72 count is unchanged.

## Independent hostile review

GPT-6 Astra reviewed the statement, proof, example, and manuscript
integration.  Its first pass identified two scope defects: the relative
Jacobian presentation had been described too strongly as analytic etale, and
the inverted coordinate `U` had been treated as a nonunit in the example.
Both were corrected.  The final review verdict was PASS, including the tube
identification, kernel decay, Newton reduction, relative-cone application,
ordinary-interior localization, example, and stated firewalls.

## Source check

The quasi-smoothness step was checked against Antoine Ducros, *Families of
Berkovich Spaces*, Asterisque 400 (2018), DOI 10.24033/ast.1050: Definitions
5.2.2 and 5.2.4 for Jacobian presentations and quasi-smoothness, Section
5.2.13 for composition, and Section 5.2.8 for the distinction involving
relative boundary.

## Mechanical verification

- Full `latexmk` build: PASS, 3624 pages.
- Undefined references: none.
- Undefined citations: none.
- Multiply defined labels: none.
- Open-problem inventory checker: PASS, 48 active atomic questions in 14
  formal Chapter 72 problem environments, tier counts `(0,5,9,17,17)`.
- `git diff --check`: PASS.
