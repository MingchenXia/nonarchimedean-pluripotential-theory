# Source audit

Date: 20 September 2026

Status: local source match passed for the infinite-star input.

The local text of Chambert--Loir--Ducros, section 6.7.3, was checked at the
archived source copy used elsewhere in the manuscript.  It states all of the
features imported through the frozen exact-star dependency:

- `X_B` is compact and has the cofinite-branch topology, strictly coarser
  than the quotient topology when the branch set is infinite;
- a domain through the node has only finitely many non-full branches;
- a smooth function is branchwise smooth and constant near every included
  `-infinity` endpoint;
- at the node only finitely many branches fail to be full and constant;
- the almost-zero sum of the node derivatives is exactly zero.

The new theorem defines its product generator sheaf explicitly.  It does not
silently identify a larger or different nonambient product structure with
that sheaf.  Its other mathematical inputs are the exact frozen
infinite-star theorem and the exact frozen Stone--Euclidean theorem; both were
included in full in the accepted dependency-closed verifier request.
