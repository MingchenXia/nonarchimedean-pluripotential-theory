# Post-repair hostile audit of the toric zero-mass proof

**Date:** 24 August 2026  
**Chapter 55 source:** parts/part5/ch55_okounkov_dh.tex  
**Chapter 55 SHA-256:** ae6290a12abee4a2eefeda0c842967de506156b02a56c37b39eba5d1f6adb1dc  
**Chapter 69 source:** parts/part6/ch69_verified_extensions.tex  
**Chapter 69 SHA-256:** 39e5caa017d1181696a3a3757848980b989809b2b30aac598ebf7a6032f9be14

## Verdict

**PASS.**  The three must-fix items in
ch55_toric_zero_mass_hostile_audit_20260824.md are resolved in the exact
source snapshots identified above.  No new must-fix item was found in the
repaired proof.  This document is a human hostile re-audit, not a Rethlas
receipt.  Subsequently, however, the source-attested exact Chapter 55 block
passed production run `20260824T052605Z_703e3b501202`, and the current Chapter
69 integration passed `20260824T070302Z_d706dc98ccca`; both returned final
`correct`, zero critical errors, and zero gaps.  Their receipt files, rather
than this audit, control production status.

## Repair-by-repair verification

1. **Weight normalization.**  Chapter 55 now defines the global toric
   functions \(F_T,F_A\) as norm weights in logarithmic coordinates.  If
   \(\Phi_\sigma\) is the book's local squared-norm weight, it explicitly
   sets \(\psi_\sigma=\Phi_\sigma/2\) and records
   \[
     \mathcal I(m\varphi)|_{U_\sigma}
       =\mathcal I(m\Phi_\sigma)
       =\mathcal I_{\mathrm G}(m\psi_\sigma).
   \]
   The last ideal uses \(\rme^{-2m\psi_\sigma}\), so the displayed identity
   exactly converts the convention of Chapter 51 to Guenancia's convention.
   The local Newton body remains on the character-lattice scale; no factor
   two is introduced.

2. **Closure versus interior.**  The source now distinguishes the possibly
   nonclosed local Newton set \(P(\psi_\sigma)\) from its closure
   \(K-d_\sigma+\sigma^\vee\).  This closure is full-dimensional, and the
   source invokes the correct convex fact
   \[
     \operatorname{int}P(m\psi_\sigma)
       =\operatorname{int}\bigl(m(K-d_\sigma)+\sigma^\vee\bigr).
   \]
   Guenancia's strict-interior criterion is therefore applied to the correct
   set.

3. **Holomorphicity of the local exponent.**  For
   \(\alpha_\sigma=u-md_\sigma-m\varepsilon a_\sigma\), the source now
   records
   \[
     K\subseteq P_D
       =\bigcap_\tau(d_\tau+\tau^\vee).
   \]
   Consequently
   \(m(K-d_\sigma)+\sigma^\vee\subseteq\sigma^\vee\).  If
   \(\alpha_\sigma+\kappa_\sigma\) lies in the strict interior, then every
   smooth-chart coordinate satisfies
   \(\alpha_{\sigma,j}+1>0\).  Integrality gives
   \(\alpha_{\sigma,j}\geq0\), so the Laurent coefficient is automatically a
   holomorphic monomial.  The character equivalence and the subsequent count
   of \(E_{m,\varepsilon}\) are now logically complete.

4. **Chapter 69 synchronization.**  Its delegated proof now explicitly says
   that Chapter 55 performs the squared-norm/norm-weight conversion, the
   closure/interior comparison, and the holomorphicity check before invoking
   Guenancia.

5. **Provenance typography.**  Both 64-character SHA-256 values in the
   Chapter 55 provenance section remain complete and are now set as separate,
   centered, small monospaced lines.  The forced line-break commands and
   paragraph stretching around split hashes are gone.

## Full proof-chain recheck

- The Cartier convention
  \(D|_{U_\sigma}=\operatorname{div}(\chi^{-d_\sigma})\) gives local exponent
  \(u-md_\sigma-m\varepsilon a_\sigma\); the sign is correct.
- The local Newton translation is
  \(K-d_\sigma+\sigma^\vee\), and Guenancia's Jacobian shift is
  \(+\kappa_\sigma\).
- Cancelling \(md_\sigma\) and using
  \(Q+\sigma^\vee=a_\sigma+\sigma^\vee\) gives
  \[
    u+\kappa_\sigma\in
    \operatorname{int}\bigl(m(K+\varepsilon Q)+\sigma^\vee\bigr).
  \]
- Completeness of the fan gives
  \(B=\bigcap_\sigma(B+\sigma^\vee)\) with the separation inequality in the
  correct direction.
- The shifted intersections are uniformly bounded; their inner compact
  exhaustion and outer-neighborhood containment justify the lattice squeeze.
- Covolume-one normalization gives
  \(\#(mC\cap M)/m^n\to\lambda_M(C)\), including along the rational
  divisibility subsequence.  There is correctly no \(n!\) in Cao's normalized
  section count.
- Clearing a denominator scales \(K\) homothetically and leaves both its
  dimension and the vanishing degrees of Cao's products unchanged.
- Cao's general inner quantity is a limsup with the ordinary multiplier
  ideal.  The toric lattice argument proves that it is an actual positive
  limit before substitution.
- If \(d=\dim K\), the two-sided estimate
  \(\lambda_M(K+\varepsilon Q)\asymp\varepsilon^{n-d}\) is valid also for
  \(d=0,n\).  Thus Cao's logarithmic criterion yields
  \(\nu_{\mathrm{Cao}}(T)=d\).

The repaired theorem is therefore mathematically ready for exact-source
Rethlas verification.
