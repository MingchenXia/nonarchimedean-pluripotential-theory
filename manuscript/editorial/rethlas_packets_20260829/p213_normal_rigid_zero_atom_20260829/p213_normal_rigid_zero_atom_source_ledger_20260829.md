# P21.3 normal rigid-point zero atom: source ledger

Date: 29 August 2026

Status: **production-verified quarantine theorem; not yet a live-book
input.** No novelty or priority claim is made.

## Exact candidate boundary

- `K` is complete, nontrivially valued, and non-Archimedean.
- `X` is good, separated, and strict.
- the chosen open neighborhood `Omega` of the rigid point `y` is purely
  one-dimensional; no global equidimensionality of `X` is used.
- `y` lies in `Int(X/K)`; global boundarylessness is not assumed.
- only the ordinary analytic local ring `O_{X,y}` is normal. Geometric
  normality and rig-smoothness are not assumed.
- the psh function is continuous on the pure one-dimensional open
  neighborhood `Omega` of `y`;
  the positive curvature measure is formed on the boundaryless open set
  `Omega^circ = Omega intersect Int(X/K)`.

The conclusion is only
`d'd''[u|_{Omega^circ}]({y})=0`. It does not classify currents on the
complement of `y` and does not by itself settle the remaining P21.3 atom.

The label `lem:p21p3-componentwise-normal-rigid-zero-atom` intentionally
matches the isolated conditional target in the componentwise P21.3 packet.
The repaired componentwise packet imports this exact statement once; it does
not redeclare the label.

## Primary sources

### Chambert-Loir--Ducros, version 2

Primary PDF:
`/private/tmp/p21_bridge_sources/cld25.pdf`, SHA-256
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.

Extracted text:
`/private/tmp/p21_bridge_sources/cld25.txt`, SHA-256
`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

Exact uses:

1. Section 11.1.10 (printed pages 301--302): at a good analytic point the
   ordinary analytic local ring is noetherian, henselian, and excellent;
   this section also defines rigid points.
2. Formula (11.5.5.1) (printed page 315): for a good germ,
   `dim_cent(X,y)+dim_Krull O_{X,y}=dim_y X`. At a rigid point of a strict
   affinoid the Zariski closure is a closed point, hence the central
   dimension is zero.
3. Formula (11.4.1.3) and Example 11.4.2 (printed pages 310--311): boundary
   composition and the boundary of a closed disc. These justify replacing
   the ambient space by a boundaryless open neighborhood of an interior
   point and locate the outer boundary of the finite tube.
4. Lemma 11.6.5(a) (printed page 318): a relative-dimension-zero morphism at
   a point of the relative interior is finite at that point.
5. Section 11.4.4, Remark 11.4.7, and Section 11.6.3 (printed pages
   311--317): finiteness at a point makes the local algebra finite; at a
   point of the relative interior, module-flatness of the local algebra
   implies analytic flatness; and a finite-flat germ admits compact
   finite-flat neighborhoods with a singleton central fibre.
6. Corollary 15.1.2 (printed page 422): a smooth function is locally a
   smooth function of tropicalizations of analytic units. This validates
   the radial cutoff on the punctured tube and its constant extensions.
7. Lemma 13.3.8 and Proposition 14.4.2 (printed pages 380 and 409--410):
   finite-flat degree equals calibrated degree, and canonical calibrated
   pushforward under a morphism with finite fibres multiplies by that
   calibrated degree.  On each transition annulus the resulting factor is
   therefore the total finite-flat degree `d`, including residue-degree
   factors.  Neither statement assumes rig-smoothness.
8. Section 7.7.4 and Lemma 7.7.5 (printed page 188): the integration current
   of a boundaryless space is closed, and
   `<d'd''S,alpha>=<S,d'd''alpha>`.
9. Proposition 7.2.8 (printed pages 161--162): a positive current of bidimension
   `(0,0)` is a Radon measure.
10. Lemma 8.5.5 (printed page 207): if `T` is positive and closed and `u` is
    continuous psh, then `d'd''(uT)` is positive and closed.

### Stacks Project

Official stable source:
<https://stacks.math.columbia.edu/tag/00PD>, checked 29 August 2026.

Tag 00PD, Lemma 10.119.7, states the equivalence among a discrete valuation
ring, a one-dimensional regular local ring, and a one-dimensional
noetherian normal local domain. It is used only after CLD has supplied
noetherianity and the one-dimensional local-ring calculation.

## Relation to the production-verified proof

The local radial estimate is adapted from the exact live proof
`manuscript/editorial/rethlas_packets_20260828/
p21p3_curve_rigidity_arbitrary_field_reduced_proof_live_20260828.tex`,
SHA-256
`01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`.
Its controlling production run was
`20260828T042906Z_f2a1c1b9f2a3`, `gpt-5.6-sol`/`xhigh`, final `correct`,
zero critical errors, and zero gaps. That verdict does **not** verify the
present altered hypotheses or bytes.

The new logical input is exactly:

`normal O_{X,y}` + `dim O_{X,y}=1` + noetherianity
`=> O_{X,y} is a DVR`.

Everything after construction of the finite flat coordinate tube is the
same radial mechanism, rewritten here in full.  Before constructing that
tube, finite torsion-freeness proves ordinary module-flatness, and CLD
Remark 11.4.7 supplies the separate implication to analytic flatness at the
relative-interior point.  The proof therefore does not use the bare phrase
“torsion-free hence flat” as though it alone were the analytic flatness
definition.

## Promotion record

The exact statement and proof hashes are
`469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`
and
`661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`.
Independent hostile audit returned `PASS`.  Production Rethlas
service-evidence run `20260829T060048Z_469024d04e8e`, item
`pi_0d4235a44db2b33950f8dd55`, used `gpt-5.6-sol` at `xhigh` and returned
final `correct`, zero critical errors, and zero gaps.  Request, response,
safe headers, service manifest, item log, process guards, and exact hashes
are archived in the packet.  Live use still requires the intended-placement
build and rendered-page audit; until that gate, P21.3 and every open-problem
count remain unchanged.
