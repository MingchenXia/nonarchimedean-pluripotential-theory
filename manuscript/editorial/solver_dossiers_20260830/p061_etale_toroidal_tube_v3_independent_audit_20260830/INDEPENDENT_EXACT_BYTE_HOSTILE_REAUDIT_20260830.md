# Independent exact-byte hostile re-audit: P06.1 v3

Date: 2026-08-30  
Audited frozen dossier:
`../p061_etale_toroidal_tube_v3_20260830/`

## Verdict

**PASS** as a frozen research candidate in its stated scope.

- Critical errors: **0**
- Mathematical/proof gaps: **0**
- Source-scope/provenance gaps: **0**
- Frozen-byte mismatches: **0**
- Independent compile failures: **0**

The unique v2 audit gap is closed in the exact v3 bytes.  Rank zero is now
separated before any nonzero-generator estimate; every coefficient error is
literally zero; and the only remaining `max_i` occurs after the proof has
assumed positive rank.  The dense torus orbit is explicitly routed to this
rank-zero branch.  Regression checking found no deterioration in any item
that passed the v2 audit.

This report does not modify or authorize modification of the frozen dossier,
the live manuscript, or any production record.  No production verifier was
called.

## 1. Exact frozen-byte gate

Running `shasum -a 256 -c FROZEN_SHA256` in the audited dossier returned
`OK` for every listed artifact.  The principal hashes are exactly the
requested values:

| Artifact | SHA-256 |
|---|---|
| v3 statement | `fbb294c435dffacf8153a076846586d2bdf2ee68a6e7268f94d2a12241629c34` |
| v3 proof | `10d188621a07242ea278c5699a27ef25488605365c953f94ddf0d08bb4ec9729` |

The complete frozen ledger also verifies:

| Artifact | SHA-256 |
|---|---|
| `README.md` | `6afa2cedfd453a8993d2fa4d328c440d90ce9b3c5fe4d3c004db8b8cdcdccada` |
| `REPAIR_LEDGER.md` | `011d8ba839330a17628de9fd5331be48b9b75a6b2252b992ed65154c65aba275` |
| `SCOPE_FIREWALL.md` | `ae03a936dd98abd8a0d943f739832758f8c8b2692c29042c6eaebcb83b2bd9b5` |
| `DEPENDENCY_PROVENANCE.md` | `5cc9f945523bc64f8d5bee3927aba7e2eae5791f14c1e09eecb8d46751aca90d` |
| `SOURCE_MATRIX.md` | `237773893111dfd22d65f5fba6c87add123531894a10c25ef6bb4ad94b43e3cb` |
| `SELF_AUDIT.md` | `c6f988d3b8523d9077245bcc3009e7e7a2c4c33d0fb88c5741fb101ff0030dd2` |
| compile wrapper | `3fac21b03d49d34b19aafa024a36dc46d7c95e98e288324d617b8ff4fc33b99b` |
| frozen PDF | `e90b6833655162169b942c79ce3927bb644d72c57dcf33676b6c9d82f6d8a03b` |
| quasi-smooth statement excerpt | `f4d9ea3b80cb2763d8a8960b2f63b9400ad09e26108a9515d3893e14075a596b` |
| descent statement excerpt | `5ad0a1873f43bf21ce72bc8fb4dac5a998dc4a0d305cf79d21ec0a1d6167d59f` |
| quasi-smooth proof excerpt | `6fe55d02ef2adbd4a95d4a1eef10a3373359695bae8f237e95c270775e4d98c6` |

The check was repeated after writing this sibling report and again returned
`OK` throughout.

The manifest file itself has SHA-256
`b8fec626b87ab030af06e98a0a6aad78150a6b76d88ae36461ac9182bbc2d75e`.

## 2. Controlling v2 audit and exact v2 preservation

The controlling v2 independent audit has hash
`d884005655ff604eea9e45d90c243f8751ed8505d92700033d90ac2ef8ae4d10`.
It found zero critical errors and exactly one proof gap: for a permitted
rank-zero lattice, the coefficient-decay display contained an undefined
maximum over an empty family of nonzero monoid generators.

The frozen v2 principal files remain unchanged:

- statement:
  `ad8ecd1a3f1197e9ba2234595f4f43e40099bcd5b04cfe925a53865f452b94bd`;
- proof:
  `b18a0274e52e6f74ede7ca22e1d9d70ed68bff076f6768e15ff2b972d5c4fb96`.

An exact unified diff shows that the v3 statement changes only the version
comment and internal v2-to-v3 labels/references.  Its mathematical statement
is unchanged.  The v3 proof changes labels mechanically, inserts the
rank-zero branches described below, and inserts the dense-orbit routing
sentence.  The positive-rank argument and all previously audited proof
blocks are otherwise unchanged.

## 3. Closure of the sole v2 gap

The exact repair ranges have the following independently recomputed hashes:

| Exact range | SHA-256 |
|---|---|
| proof lines 208--229 | `85a3900c05d461ff6fc36d28334605b33e6debc31428c2bf4e7e4bbd3f80ab76` |
| proof lines 264--270 | `a6971b1a3053d2a981d4a9d3a00b8b109db8052aa2b111402d20b112adb523b3` |
| proof lines 359--388 | `9685cdd8252b2a759669ebb918f7891d916466614e151ed48202e3333b9955f7` |
| proof lines 462--464 | `d47bd8a9647c26b9c77d2d42413a25d486fda2635aa7e4fe910c89576361773b` |
| all-orbits dependency proof lines 183--228 | `2d0a9026c0bd286ad0ac7e8d5e632abf8a42f21017410797c7b2237c07a64bda` |

### 3.1 Cone, monoid, and weighted domains

Frozen proof lines 208--229 now begin with an actual case split.  In rank
zero they record

`N=0`, `rho={0}`, `S={0}`, and `Z=Spec K`,

put `v=0`, and observe that every `U_k` is the one-point strict affinoid
`M(K)`.  In the zero-dimensional ambient space, `{0}` is full-dimensional,
strongly convex, and rational, and its interior is `{0}`.  Thus this branch
is compatible with every hypothesis of the proposition.  The one-point
domains are trivially cofinal among ordinary neighbourhoods of their unique
point.

### 3.2 Banach algebras and structural maps

At proof lines 259--293, `R_k=O(U_k)=K`; hence the displayed completed
tensor products identify canonically as

`A=R_m completed_tensor_K B=B` and
`A_n=R_(m+n) completed_tensor_K B=B`.

The proof takes `q=0` and equips all three copies with the fixed Banach norm
of `B`.  Under these canonical identifications, the section, retraction,
restriction, and evaluation maps are identities and therefore contractions.
No generator is selected in this branch.

### 3.3 Kernel and coefficient errors

Proof lines 359--388 split again before the positive-rank augmentation-ideal
calculation.  In rank zero,

`J=ker(A->B)=0`.

For every coefficient `a` of `g` or `h`, the retraction and section are
identities, so

`a^circ=a-iota(epsilon(a))=0`

in every `A_n`.  The finite coefficient maximum in the standard-etale lemma
therefore equals zero for every `n`, proving its contraction hypothesis
directly.  The proof explicitly states that this uses no maximum over an
empty generator family and only then assumes positive rank.  Consequently,
the `max_i` at proof lines 377--381 ranges over the nonempty positive-rank
generator list.  The later `max_s` in the fibre Gauss norm is harmless in
rank zero because `S={0}` is a singleton, not an empty set.

### 3.4 Completion of the rank-zero product argument

With `A=A_n=B`, the source algebras `C_n`, the fixed-fibre algebra `D`, and
`E_n=A_n completed_tensor_B D` are the same standard-etale strict affinoid
algebra under the stated presentations.  The general four-root lemma applies
because its coefficient errors are zero.  It returns the required product
with the one-point toric factor.  The ordinary-interior argument also
specializes correctly: the point is the interior of `M(K)`, while the strict
`T` and `U` inequalities supply the source neighbourhood.  Finally,
`H(d_0)<S>=H(d_0)` when `S={0}`, so every fibre is a one-point affinoid with
singleton Shilov boundary.

### 3.5 Dense torus orbit

Proof lines 450--470 now say explicitly that, at the dense torus orbit, the
transverse pointed factor furnished by monoid localization has rank zero and
is `Z_tau=Spec K`.  It is therefore handled by the branch just proved.  The
rank-zero case is not merely present abstractly; the global source-Zariski
corollary actually routes its boundary case to it.

The sole v2 mathematical gap is therefore closed.

## 4. Regression audit of all previously passing items

### 4.1 GJR scope and factorization layering

The general singleton-Shilov proposition still concludes only fibrewise
factorization over an arbitrary complete field.  The separate real-PL
corollary still adds nontrivial valuation and good strict source and target
before invoking GJR Lemma 5.4(1).  No rational/integral-PL counterexample is
imported.

### 4.2 Common fourfold Newton radius

The quantitative Newton block is unchanged apart from v3 labels.  It bounds
all fixed and perturbed derivative inverses and all higher Taylor
coefficients, chooses one radius satisfying `MHr<1` and `Lr<1`, and applies
that same radius to

1. `(E_n,g,t)`,
2. `(E_n,g_0,t)`,
3. `(C_n,g_0,T)`, and
4. `(C_n,g,T)`.

The exact-root uniqueness assertions (2) and (4) still prove the two crossed
composites.  The central `D` uniqueness estimate still makes the reduced
isomorphism the identity.  Both localization inverses retain norm at most
one.

### 4.3 Standard-etale chart and actual strict neighbourhoods

The proof still uses Stacks Tag 025C only for the algebraic open immersion,
chooses a principal open inside its image, puts `H=G'F`, and constructs the
source by a bounded relative disc followed by a rational inverse domain.
The quotient Gauss and projective tensor norms make all structural maps
contractive.  Strict inequalities at the chosen point and target interiors
show that every deeper `C_n` and the fixed fibre `D` are actual ordinary
affinoid neighbourhoods, not merely formal completions.

### 4.4 Positive-rank semigroup contraction and Shilov fibres

After the new case split, the positive-rank normalized-generator proof is
the v2 proof verbatim modulo labels.  Every generator acquires a scalar
factor of norm tending to zero, so the finite coefficient set contracts.
After every residue-field extension, the semigroup residue algebra is a
domain; hence the normalized Gauss norm is multiplicative and its point is
the singleton Shilov boundary.  The same final argument includes rank zero
as noted above.

### 4.5 Harmonicity and source-Zariski localization

The product factor remains the retained quasi-smooth fixed-fibre cover `D`,
not the smooth target `V`.  The exact quasi-smooth dependency gives real-PL
regularity and GJR harmonicity on `D`; factorization and pullback transfer
the real-PL statement; and GR Theorem 4.3 applied to both classical-psh signs
gives GJR harmonicity.  At arbitrary toric orbits, exact monoid localization
splits off a torus that joins the smooth factor.  No descent from an
unmaterialized etale cover is claimed.

### 4.6 Scope firewall

The firewall still excludes trivially valued fields, non-good or non-strict
extensions of the GJR step, bare log-etale/Kummer charts, formal-only
products, analytic-local-isomorphism claims at general nonrigid points, and
gluing of independent standard-etale trivializations.  Allowing the proved
rank-zero pointed factor weakens none of these restrictions.

## 5. Dependency and source regression

The three local quasi-smooth excerpts are byte-identical to their v2 copies.
The exact dependency and source hashes remain:

| Artifact | SHA-256 |
|---|---|
| all-orbits statement | `05bda70eb1cf7ebbcc95d1831feadd946afa168f64a7298171381b9f1e865e60` |
| all-orbits proof | `21c44c47a91a28469fb91a6c00569ed56d12699bae9c956c68c33ad493825b03` |
| all-orbits production response | `718044118ee65e0d76b7c02b8b553552b8da974367513aa5ed4d57e8b6231f7d` |
| quasi-smooth full statement | `0b1b4d161e3b85d342d7be88234a8ed27bfe74be4d24a639ff0456373a7a39e9` |
| quasi-smooth full proof | `fdc6abcc4988644656892172fbdbda4178cb86ca710fd0122a90947e598b0b8b` |
| quasi-smooth production response | `2ee6f3ed4f7242b0988ae8a79c8a574a75377e339c2c6965cf3d1b8e55ffce7e` |
| Gubler--Rabinoff PDF | `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726` |
| Gubler--Jell--Rabinoff PDF | `572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42` |
| Stacks etale PDF | `cfe0581a0bfe38522726f6a233ab4cd30d5f283bef86c4f136fc2ee34c8ecc99` |

The quasi-smooth theorem/descent ranges remain exact; the unrelated
counterexample ranges remain excluded.  The all-orbits and quasi-smooth
responses still record `correct` with zero critical errors and zero gaps.
No new external source is needed for the elementary rank-zero branch.

## 6. Independent compile

The frozen wrapper was compiled independently with `latexmk -pdf`, with all
generated files redirected to
`/private/tmp/p061_v3_independent_audit_build_20260830/`.  The stable second
pass completed with no undefined references, overfull or underfull boxes,
multiply defined labels, or fatal errors.

| Independent artifact | SHA-256 |
|---|---|
| PDF | `4720afed15f14efe030e7f1b3a053fb303c9c520f55d441019dcdcb5ef4c664b` |
| final log | `c2b4daf2ab50126ef6d13526740e22040e0cbbd7d7047665a02167a89175d598` |

These independent outputs are outside the frozen dossier.

## 7. Release decision

The exact v3 candidate passes independent hostile re-audit.  This closes the
v2 FAIL-CLOSED mathematical gate.  The dossier remains quarantined until a
separate dependency-closed production verification passes; this audit by
itself does not authorize live-book integration.
