# Maximal-destabilizer quantization — 5 October 2026

Chapter 68 adds the known finite Chow minimization, symmetry and
saturation results and a conditional route to maximal K-destabilizers.
The limit retains the source's continuity, general two-term expansion
and minimizer-convergence assumptions. Appendix L records source and
verification scope. This is an ordinary import of identified mathematics,
not an original general theorem or a fresh independent model certificate.

The baseline is work-branch commit
294afec3470109f85832c627ac7bdf0f8449c946. The preceding frozen Snapper
exports and all 42 complete open-problem statuses are preserved.

## Controlling source and actual reading

Yi Yao, *The maximal destabilizers for Chow and K-stability*,
arXiv:2511.16401v1, submitted 20 November 2025 at 14:18:02 UTC.
The 43-page PDF was acquired on 5 October 2026 at
13:32:37.678557 UTC, HTTP 200, 802,355 bytes, SHA-256
969e2143543693aa7df1331291a5a138860bc344a52fe5ae922e26d6a5eecd59.
All 2,210 extracted split lines were read, including references, in
bounded contiguous ranges. Fourteen actual pages were viewed:
5, 11, 18–19, 26–29 and 33–38. The separate page-33 view and the
paired-sheet view both confirm the bars and norm powers in
Proposition 44 and equation (7.4). No normalization error in that
formula is alleged. The current arXiv metadata exposes only version one.

Two dependencies were selectively read, not read in full:

- Boucksom–Jonsson, *On the Yau–Tian–Donaldson conjecture for weighted
  cscK metrics*, arXiv:2509.15016v1, submitted 18 September 2025 at
  14:46:28 UTC. Acquired 5 October at 13:37:57.137237 UTC, HTTP 200,
  84 pages, 1,000,611 bytes, SHA-256
  86dc379beae2dd0517edf52cd36fc21509156e050afd1794befd63710753443e.
  Text ranges 280–410, 2990–3140 and 3540–3577, with actual pages
  6–7, 60 and 68, check Theorem C, entropy Theorem 7.5 and weighted
  Mabuchi Theorem 8.7.
- Darvas–Zhang, *A YTD correspondence for constant scalar curvature
  metrics*, arXiv:2509.15173v2, revised 3 November 2025 at
  15:43:32 UTC. Acquired 5 October at 13:37:58.059405 UTC, HTTP 200,
  52 pages, 733,538 bytes, SHA-256
  9f57d15e391eafc6a3c06bcef8c9579da3c329f841435de2036f74f1a801fc94.
  Text ranges 280–320, 2000–2115 and 2114–2178, with actual pages
  7, 38 and 39, check equation (14) and Corollaries 8.2–8.4.

Twenty-one actual primary pages were viewed in eleven sheets. Full
controlling-text reading, selective dependency reading and actual page
inspection are distinct claims. Extraction diagnostics are empty.
Acquisition JSON, reading records and metadata results are retained in
the ignored source_material/maximal_destabilizer_followup_20261005 cache;
the final manifest pins their bytes. A separate toric follow-up cited by
Yao was not acquired; it supplies no input. Search results and seminar
notices do not prove that no such paper exists.

## Known proof inputs and mathematical boundaries

Theorem 20 proves finite minimizer existence using the compact sphere
of self-adjoint initial velocities in a fixed Hermitian tangent space.
The spectral-norm sphere is compact in that Euclidean topology; the
Chow slope is lower semicontinuous as a supremum of continuous
finite-time quotients. No local compactness of the non-Archimedean norm
metric is assumed. The common-basis uniqueness argument needs strict
p-norm convexity and a negative minimum. Remark 21 retains the centered
formulation for the semistable case. Theorem 23 obtains group invariance
from Chow-weight and norm invariance and uniqueness up to positive scale.

Theorem 33 gives the normalized energy definition of Chow weight.
For the kL embedding its energy is k times E_L(FS_k chi); this factor
must precede the average jump. Proposition 35 gives the sup-norm/FS
adjunction and image identities. Theorem 36 centers the L2 optimizer and
gives saturation SN_k FS_k chi=chi. Its quadratic-penalty proof clips
the canonical spectrum at one and then uses SNFS raising weights in
that range, with fixed FS energy and uniqueness. No raw Chow-form norm
constant is independently certified here.

The maximal geodesic ray used by Theorem 37 is an identified existing
Xia input; no new full audit of that external proof is claimed. Definition
39 defines its non-Archimedean K-direction. A1 is the radial Mabuchi
equality on maximal finite-energy rays; the selected BJ25/Darvas–Zhang
sources supply it in the smooth complex projective ample scope. This
does not certify the whole weighted correspondence or extend it to
singular, nonample, positive-characteristic or nonprojective objects.
The older dated Trusiani account remains a separate source account.

A2 requires continuity of the maximal direction. Theorem 45 identifies
its L2 norm from scaled section-norm second moments for continuous
metrics, using known Duistermaat–Heckman and uniform approximation
inputs. A3 asks for the first energy error on every continuous metric.
Theorem 46 proves that error only on ample test-configuration metrics,
with O(k^-2) remainder along divisible degrees. The proof uses normalized
ramified base change to reduced central fibre, the section filtration
identification, and the two-term weight expansion with DF=M in the
reduced case. This is a known source theorem, not a newly certified
general expansion beyond those metrics.

A4 assumes convergence of the minimizers. Theorem 4 explicitly depends
on A1–A4; Proposition 47's geodesic convexity does not remove A4.
The controlling source does not name a fixed topology for A4. The
chapter consequently adds no uniform, d1 or d2 convergence conclusion.
Compactness, lower bounds and approximation along varying minimizers
would have to be established in a chosen topology. Pointwise A3 is
not enough by itself. No active atomic problem is declared solved.

## Convention audit and exact diagnostics

The book uses s=-log|tau| and squared potentials; Yao uses t=2s.
At the corresponding squared potential, Yao's analytic K-energy is twice
the book's analytic Mabuchi functional. Thus M_Yao/t=M_book/s has
the same non-Archimedean limit. The radial L2 speed in Yao's t units is
half the book's s-speed. The new section keeps these units explicit.
The existing book convention is not asserted to be erroneous.

The radial penalty M+a^2 norm^2/2 selects scale -M/norm^2. The finite
penalty 2 M_Chow+norm^2/(2k^2) selects -2k^2 M_Chow/norm^2. These
give norm(phi-flat)^2=-M(phi-flat) and
norm(chi-flat)^2=-2k^2 M_Chow(chi-flat), respectively. Exact rational
checks cover 45 radial and 180 finite penalty identities.

For 240 integer degrees the checker also verifies spectral lattice
benchmarks: lambda_j=min(j,k-j) has sum floor(k^2/4), normalized energy
sum/(k(k+1)) and parity-dependent first error 2k(1/4-E_k), tending
to 1/2. Its scaled second moment tends to 1/12. The centered product
spectrum lambda_j=j-k/2 has second moment (k+2)/(12k). These are exact
arithmetic diagnostics, not an independently certified general toric
construction or a maximal-destabilizer convergence example. They remain
outside active TeX.

The auxiliary Theorem 11 injectivity proof's literal inference from a
unitary spectral-flag-preserving basis change to a diagonal matrix must
allow repeated-eigenvalue blocks. The checker uses the identity operator
and a nondiagonal orthogonal rotation: conjugation preserves the operator.
The corrected block interpretation still yields the same self-adjoint
operator. No isometry or Chow-minimization theorem counterexample is
claimed; that literal diagonal inference is not imported.

No new production-model calls or receipts are recorded. The normal
work-branch publication is authorized by the persistent user request.
Main, the catalogue, all 108 protected M/N inputs, the 42 inventory
statuses and all prior frozen releases are preserved. Final source,
build, navigation, actual-page and archive-byte checks are recorded in
the integration manifest and separate artifact-hash record.
