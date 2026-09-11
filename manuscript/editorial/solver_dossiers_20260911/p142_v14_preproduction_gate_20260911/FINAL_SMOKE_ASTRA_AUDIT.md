# Independent V14 final-smoke hostile audit

Auditor: `gpt-6-astra`, `xhigh`
Date: 11 September 2026
Disposition: **PASS**
Critical errors: **0**
Material gaps: **0**

The auditor replayed the complete final release checker against the 62-row
manifest and recomputed its digest as
`73489c6753340007c92debb76eb915b63cef5471db52c96c53d98bebfca53d1a`.
It independently verified the four smoke hashes recorded in
`V14_RELEASE_SHA256SUMS`.

The receipt is `passed`, has an empty error array, exit code zero, total elapsed
time 347.227544625 seconds, and exactly one completed MCP wait lasting
310.005920208 seconds.  The seven stdout records consist of the one exact
allowlisted skills-budget diagnostic, a non-overlapping start/completion pair
for the fixed TTL tool, one exact agent status after the completed call, and the
current five-key usage record.  No premature status is present.  The thirteen
stderr records are exact startup state-database warnings.  The 24 process
samples consist of 23 live samples and one terminal sample, with the required
roles and cadence.

The final tree was read-only and contained no bytecode cache, unexpected file,
or nonempty smoke workspace.  The auditor separately confirmed that the one
source-stage test that cannot be rerun *inside the final tree* is stopped by the
intentional anti-rerun gate after its temporary copy inherits an existing
`STATIC_MODEL_LONG_SMOKE` directory; the same test passed in the audited source
tree.  The complete final release checker passed again after that diagnostic.
This audit establishes only the infrastructure preflight, not a mathematical
production verdict.
