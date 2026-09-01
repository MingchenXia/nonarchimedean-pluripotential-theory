# P14.8 noncircular dependency packet v3

Date: 1 September 2026.

Status: **authored static source stage; ready for independent hostile audit,
but not yet a production receipt and not authorized for live integration**.

The target is the unchanged P14.8 statement/proof pair:

- statement: 2,900 bytes,
  9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715;
- proof: 3,884 bytes,
  adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9.

## Accepted Chapter 51 dependency

The no-pluripolar-charge proof used in this packet is bound to production run
20260901T143740Z_9b8ffa07bc57_69cb27d9.  The host status was accepted;
the verifier verdict was correct; its critical-error and gap lists were
empty.  The run used gpt-5.6-sol at xhigh.  The independent receipt audit
has verdict PASS.

The immutable evidence is in
ch51_npp_no_pluripolar_charge_production_archive_v2_20260901.  Its
independent machine summary, independent report, and top-level manifest have
SHA-256 values

- 9bb022221ae30d321e00a4569bf9e2a0c19ee4252b3e26b2be7ca44c994a2930;
- e18d900b8361c63e969cf24cc01e5ca9e159fb298fb038af6a5c02bd9ee955a0;
- 1087f356dbdcd04e1cd76943015ddc4ee48a7da3c9023909c949a340d30fa8f7.

This binding certifies the isolated Chapter 51 no-charge argument.  It does
not reinterpret the whole Chapter 51 source as having received that
production verdict.

## Exact finite-index correction

The accepted postimage has 4,516 lines, 195,756 bytes, and SHA-256
4db4d9028c80b47994143172c356c39419954471af222b8a4f9740b9b5fcf834.
The internal Cantor lemma literally combined \(\ell_0=1\) with
\(\ell_m=\mathrm e^{-4^m}\) at \(m=0\).  The frozen corrected source in this
packet changes only lines 3775, 3776, 3784, 3785, and 3786.  It retains
\(\ell_0=1\), puts \(\ell_m=\mathrm e^{-4^m}\) for \(m\geq1\), checks
\(\ell_1/\ell_0=\mathrm e^{-4}\leq1/2\) separately, and for \(m\geq1\)
checks
\[
 \frac{\ell_{m+1}}{\ell_m}
 =\mathrm e^{-3\cdot4^m}\leq\frac12,
 \qquad
 2^{-m}\log\frac1{\ell_m}=2^m.
\]
Thus the series still diverges.  There is no line shift.  The corrected source
has 4,516 lines, 195,880 bytes, and SHA-256
b31c01ebe39eff954e322a5924ef5814b64337d389605ed247ddd38f71279965.

## Exact ten-span source

p148_ch51_dependency_v3.txt is the ordered exact concatenation of ten
spans from the corrected source:

| source lines | packet lines | role | SHA-256 |
|---:|---:|---|---|
| 316--342 | 1--27 | \(\mathbf P^1\) normalization and Green kernel | 404bcc3586c64bf7460f1b9bb8240b25fd476bf4c25bb66e4e33453ad16c4246 |
| 734--758 | 28--52 | Choquet reduction | 2f1e3e47d3d7490c01a6ad50288e5bfdb1d2805c6f950fec2a35caa76b29e45b |
| 940--1169 | 53--282 | Lelong and directed-supremum calculus | 968d5799b5d0a7f85ac8f04ef61d0fb7fd157e3e47671d395d3a3024745ca00c |
| 1556--1692 | 283--419 | strong openness and valuative package | 94146ac17f59efce4e4209b8556250c2816adc51c0bc0423d0c233bf7ac77622 |
| 2051--2104 | 420--473 | nonpluripolar truncation/global interface | f93b54536f01e99d09d4a27cdaa89c8ff60c52e6894e0283f4ecdd6903c16f3b |
| 2118--2151 | 474--507 | bidegree-one restriction | 0e8be6133daf6bf60d8edc5c435ce5b33beed4ce7aa67cf83d955c7b671fb24f |
| 2171--2272 | 508--609 | accepted no-charge ledger | 8434f257ede2d6c3741b641891d35a9c2b929f12c2212d12541f337937376a59 |
| 3215--3286 | 610--681 | \(\mathcal I\)-preorder calculus | b91a8133a7182fe5f63e972c38724f249265c596468f330d3dcc382493040069 |
| 3288--3301 | 682--695 | definition-only \(\mathcal I\)-envelope interface | 6f88ee1baa59594bb4c637cdac959842d97441dd0b303053009fce59714ee2c1 |
| 3762--3850 | 696--784 | corrected Cantor/Green construction | 53a0e2367da9f67d396947b6ad733f8d56eb7deba53e0a5f3c262dc22ba06297 |

The packet has 784 LF-terminated lines, 34,444 bytes, and SHA-256
c2404ea689ed09cf80fb8059145bc74bab123fd39c7e1d3b70f2f37b4c484fce.
The ninth span is exactly the fourteen requested source lines 3288--3301.  It
defines \(P_\theta[\varphi]_{\mathcal I}\) and ends before the theorem at
line 3303.

The packet excludes thm:complex-i-projection,
eq:complex-i-projection, their proof, the all-mass family, the zero-mass
conclusion, and every P14.8 marker.  In particular, the definition is present
but no reconstruction theorem is imported.  The old all-mass conclusion
remains source lines 3949--3968 and has SHA-256
047d2f1f25d4c7d9d88b4a3f492d753fa530044170cd902fa667199aada41282;
it is absent from the packet.

The already pinned Boucksom notes provide the Lelong/Siu/Demailly witness
needed by the target argument, while the pinned Kellay--Mashreghi text states
the generalized-Cantor zero-capacity criterion as formula (3.4).  No new
external source is needed for mathematical closure.  The exact historical
page attribution to Carleson is not itself certified by this stage.

The sibling runtime source stage is
/private/tmp/rethlas_hardened_v3_3_3_r5_p148_retry1_stage_20260901.
It is an authored pre-smoke stage only.  It has not been installed, launched,
submitted, or used for live integration.
