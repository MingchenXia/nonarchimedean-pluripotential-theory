# P11: a moving-center counterexample to global Radon--Riesz

## Later projective-space strengthening

The `P^2` theorem below remains a verified baseline.  It has now been
strengthened, without changing its conclusion, to every `P^n`, `n >= 2`, by
using a fixed linear line as the moving-center locus.  The transverse
initial form of each numerator and denominator fails only at finitely many
points of that line.  Guarded production run
`20260825T044839Z_326e2035bbb9`, item
`pi_9e222887262acc5d9fbc740a`, returned `final/correct` under
`gpt-5.6-sol`/`xhigh`, with 0 critical errors and 0 gaps.  The generalized
statement/proof/request hashes are respectively
`326e2035bbb9dd6b3d705f085c19d293da2e58b2998f3452b654c2d75d6d42f3`,
`7c9317bce0cb53b5767eb63e053c4f0e94ab23b88292e17cb481a1cdba914585`,
and `d186c1e5b96ebb91370a15155b5d6b8f4e355b04740db69bd4ccf60b1ed0b2f7`.
No live integration is claimed here.

## Status

The mathematical candidate was independently audited on 25 August 2026.
The source hash and TeX delimiters were minimally repaired before production.
Production round one then correctly rejected an insufficient residue-unit
argument for weak convergence: cancellation on the residue curve need not
make the divided rational function a unit in the surface local ring.  The
proof now uses the support of the residual divisor, as detailed below, and
was re-frozen for round two.  The exact packet passed a clean two-pass
minimal TeX compile and byte-for-byte request-embedding check.  Guarded
production run `20260825T042017Z_948e2b7cde7d`, item
`pi_0b7126d51ccabcab1920a96d`, returned `final/correct` under
`gpt-5.6-sol`/`xhigh`, with 0 critical errors and 0 gaps.  Both process
guards completed and the wrapper returned code 0.  Live integration remains
separate and was not performed by this audit.

Round-two frozen SHA-256 values are statement
`948e2b7cde7dc32411bea2acb46f6fa821e65afaa8cb8a546ec01759416cfb6c`,
proof `46875db7cbe7869e95195f6345989df85031c82d0b52df298e0427515100e959`,
and exact request
`882f866c365ddf88206c9d1df32a7b399e2de5f9deaf64bdc10eec689e3144e0`.

## Construction

Work on \(X=\mathbf P^2_k\) with \(L=\mathcal O(1)\), over an algebraically
closed trivially valued field.  Fix a line \(D\), choose pairwise distinct
points \(p_j\in D(k)\), and compare

\[
                         v_j=\operatorname{ord}_{p_j}
             \quad\text{with}\quad
                         v=\operatorname{ord}_D.
\]

The valuation \(v_j\) is the exceptional divisorial valuation of the blowup
at \(p_j\).  For each fixed rational function, write
\(\operatorname{div}(f)=rD+E\), with \(D\) not a component of \(E\).
The set \(D\cap\operatorname{Supp}(E)\) is finite.  Away from it one has
\(f=x^ru\), with \(x\) a local equation of \(D\) and \(u\) a unit.  Thus
\(v_j(f)=r=v(f)\) eventually and \(v_j\to v\) weakly.

The maximal order of a degree-\(m\) plane curve at a point is \(m\), and its
maximal multiplicity along a line is also \(m\).  Hence
\(T_\omega(v_j)=T_\omega(v)=1\).  On the other hand, the moving line through
\(p_j\) and distinct from \(D\) has valuation \(1\) at \(v_j\) and \(0\) at
\(v\).  The exact section formula for \(d_{\infty,\omega}\) therefore gives
\(d_{\infty,\omega}(v_j,v)\geq1\).

## Primary-source gates

The proof uses only Boucksom--Jonsson, Definition 1.26, Lemma 4.46,
Proposition 11.6, Lemma 11.7, and Question 11.16.  The local PDF is
`tmp/pdfs/bj22_global_trivial.pdf`, SHA-256
`8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52`.

## Scope

- The sequence escapes every fixed dual complex, so it does not contradict
  the verified fixed-complex theorem.
- The construction uses a smooth projective surface and works in arbitrary
  characteristic.
- The proof gives a sequence, not merely a net.
- No novelty or priority claim is made.

## Preserved rejection

Guarded production run `20260825T040646Z_948e2b7cde7d` returned
`final/wrong` on the earlier residue-unit argument.  Its response, manifest,
item verification and log, both completed process guards, and the rejected
statement/proof bytes are preserved under
`manuscript/editorial/rethlas_receipts_20260825/` and remain controlling for
that superseded proof.

## Production receipt

The round-two API response, aggregate manifest and verification, item log
and verification, both process guards, and the exact production receipt are
preserved in `manuscript/editorial/rethlas_receipts_20260825/`.  The stored
copies were compared byte-for-byte with the verifier result files.
