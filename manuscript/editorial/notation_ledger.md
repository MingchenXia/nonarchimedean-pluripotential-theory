# Notation ledger

This ledger is normative. A chapter-specific notation may shadow none of the
entries below without an explicit warning.

| Symbol | Meaning | First definition | Normalization warning |
|---|---|---|---|
| \(|\cdot|\) | multiplicative absolute value | Ch. 2 | ultrametric in NA parts |
| \(v=-\log|\cdot|\) | associated additive valuation | Conventions, Ch. 2 | larger \(v\) means smaller norm |
| \(X^{\mathrm{an}}\) | Berkovich analytification | Ch. 4 | retains nonzero-support points over a trivial valuation |
| \(X^\beth\) | MP tropical semivaluation space of a complex space | Ch. 58 | not notation for ordinary complex analytification |
| \(\operatorname{Sk}(\mathcal X)\) | skeleton of a suitable model | Ch. 5 | model and normalization recorded locally |
| \(\mathrm{PL}\) | piecewise linear/affine class | Chs. 5--6 | integral/rational/real slope must be specified |
| \(\mathrm{FS}\) | Fubini--Study metrics/functions | Chs. 6, 34 | algebraic grading specified locally |
| \(dd^c\) | complex curvature operator | Conventions | \((i/2\pi)\partial\bar\partial\) |
| \(d'd''\) | Lagerberg/CLD operator | Ch. 9 | never silently identified with complex \(dd^c\) |
| \(\operatorname{MA}\) | Monge--Ampère operator | Ch. 6 onward | unnormalized mass unless “probability” is explicit |
| \(E\) | Monge--Ampère energy | Chs. 26, 46 | zero at chosen reference metric |
| \(\mathcal E^1\) | finite-energy class | Chs. 26, 47, 61 | ambient theory shown when ambiguous |
| \(P\) | psh/rooftop envelope | Chs. 23, 36, 51 | obstacle and singularity envelopes distinguished |
| \(\mathcal I\) | multiplier-ideal singularity relation/envelope | Ch. 51 | not an arbitrary ideal unless calligraphic context says so |
| \(\operatorname{Tr}\) | trace/restriction operator | Ch. 54 | domain condition displayed |
| \(\operatorname{DH}\) | Duistermaat--Heckman measure | Chs. 33, 55 | probability versus mass normalization displayed |

## Sign audit

The final draft must make the following square commute with one fixed sign:

```text
vertical Cartier divisor D  ->  model metric/potential phi_D
          |                               |
          v                               v
piecewise affine function  ->  dd^c phi_D / curvature measure
```

The local equation convention for \(\mathcal O(D)\), the canonical section,
and the relative metric must be written together. Effective divisors are not
assumed to yield positive or negative functions without specifying this
choice.

