# Version 2 correction record — frozen version 1 preserved

Date: 1 September 2026.
Author: /root/p082_independent_reaudit.
Reviewer who identified and confirmed the correction: /root/p213_skeletal_hostile.

## Exact revision boundary

The mathematical proof file differs from frozen version 1 by EXACTLY the two prose substitutions reproduced below. No statement, hypothesis, model, formula, sign, degree, equation tag, conclusion, or other proof byte is changed. The read-only checker computes these substitutions from the exact original and verifies that reversing them reproduces version 1 byte-for-byte.

Version 1 remains at:
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_two_cluster_positive_transport_research_20260901

Its principal pins are:
- RESEARCH_NOTE.md: 292087eb0b34072f15f7bb2426e8adf27fe03858aa85f30107538adf0962e4bf.
- MANIFEST.json: 0bda4e908fa42e8b683ef96fbe61ae34298482829d77fae645adab157dab717b.
- SHA256SUMS: 162116e70eb80c6f4f844e5e7a826f39b15e29116e0546215db8c81aa3c95e4d.

The reviewer correctly flagged the version-1 Section 8 sentence “Away from the bad tubes the same identity holds.” Read after the preceding differential identity, that asserts too much: at a generic residual point, the pointwise value t=0 does not imply ordinary-local constancy of t or vanishing of its differential. The proof actually needs chi'(t)=0 there, which follows because chi is constant near zero and t is continuous.

On the entire SHALLOW collar of an order-zero bad closed point, in contrast, the norm identity does hold on an actual ordinary open set, so d''t=0 there is legitimate. This distinction is now explicit.

The reviewer approved BOTH exact proposed substitutions before this version was written/frozen. That approval is not a full final independent audit of version 2; the final exact-byte review remains separate.

## Substitution 1: Section 5 clarification

Old:
~~~text
Off the bad tubes \(t=0\).
~~~

New:
~~~text
Off the bad tubes \(t=0\), so \(\chi'(t)=0\) on an ordinary neighborhood of each such point because \(\chi\) is constant near zero; this makes no assertion that \(\mathrm d''t=0\) there.
~~~

The old Section 5 sentence did not itself make the erroneous differential assertion; the added explanation records the actual support argument and prevents the same ambiguity.

## Substitution 2: Section 8 required correction

Old:
~~~text
At the order-zero bad point 1 the entire shallow collar has \(|\zeta|=1\), hence \(\mathrm d''t=0\). Away from the bad tubes the same identity holds.
~~~

New:
~~~text
At the order-zero bad point 1, the entire shallow collar is an actual ordinary open set on which \(|\zeta|=1\); hence \(\mathrm d''t=0\) there. Away from the bad tubes we use only \(t=0\): since \(\chi\) is constant on a neighborhood of zero, \(\chi'(t)=0\) on an ordinary neighborhood of each such point. No vanishing of \(\mathrm d''t\) near the generic residual center is asserted.
~~~

## Preservation and status

The original source ledger and authored validation are retained with short appended version-2 notices. The new check script adds the frozen v1 manifest/sums, original-proof pin, exact forward-substitution check and exact reverse-substitution check. These ancillary changes record the correction rather than silently rewriting its history.

L/O/Q and displayed R remain explicit conditional premises, with the same exact principal inputs as version 1. The author-related O premise remains disclosed. No new scope, general accessibility, whole-current conclusion, priority, production acceptance, or P21.3 retirement is claimed.

