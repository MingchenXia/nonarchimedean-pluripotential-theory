# Production verification receipt

**Candidate:** curve-specific curvature-domination proof that every
parlinear metrized line bundle is globally dpsh.

**Verifier:** production Rethlas endpoint, `gpt-5.6-sol` at `xhigh`.

**Verdict:** `correct`; zero critical errors; zero gaps.

The endpoint assigned no run or item identifier.  Its report explicitly
checked the P08.1 theorem, P08.2 algebraization transfer, CLD/Thuillier
comparison, curvature signs and degree formula, prescribed finite atomic
curvature, Wanner comparison, and the literal CLD globally-psh diagonal
argument.  It also confirmed that the isolated sign defect in Thuillier's
printed Definition 3.4.17 is correctly firewalled.

## Exact-byte ledger

| Artifact | SHA-256 |
|---|---|
| statement | `ae3042f558e649bfd2f54a00287901978558defa6a6aa4be52e63f9461c466be` |
| proof and scope remark | `5a35c88f774aca391fa6c38acbbc5cb0c7ea5956efbdc370d129fbdc365bec80` |
| repaired source matrix | `b408df8fcca255d0bf5de6aaddafdd8e31ed93b9b618e5da8091ab8957ae2df8` |
| independent hostile audit | `adf392d4d9e59f5d5d755a7e13fad39c51a60dba849d3229c22acdb3eb2e6cca` |
| post-audit repair ledger | `b3c9ac9361a6b0b5743e79958dfeacddbfbe420f35bfef708b31d33bfb1e8826` |
| production request | `86cd317fc3dce5cd29fc0dd03668d1f99b4694522a09f62c1980c7d3728f98d3` |
| production response | `00561848978d7ef9ca781ffb48eb507ba928d53507dea96e7ea2b34e5cb4add7` |
| response headers | `eb6c70e6a1f88bdf6aeabf00b1b1ca2e64c10a585be96d473f9ccbde1faf8720` |

## Priority and scope firewall

CLD Corollary 17.8.9 already states the final global-dpsh conclusion for a
parlinear metric on the analytification of a projective variety.  This
packet supplies an alternative curve-specific, dependency-explicit proof;
it makes no novelty or priority claim and retires no additional inventory
atom.  Its direct proof is confined to smooth proper connected strict
curves over algebraically closed complete nontrivially valued fields.
