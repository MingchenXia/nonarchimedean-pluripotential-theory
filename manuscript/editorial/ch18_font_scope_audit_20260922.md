# Chapter 18 table font scope — 22 September 2026

## Cause and correction

The complete Chapter 60 build used 8.5-point body type with a
10-point baseline, while the scoped build used the template's
10-point body type with a 12-point baseline. A temporary copy of
the complete build input closure was instrumented at each
draftinclude entry and exit.

The first change occurs in Chapter 18: entry is 10/12 and exit is
8.5/10. All subsequent chapter and appendix boundaries inherit
8.5/10. A lexical check of font declarations in the actual TeX
closure identifies two declarations at top level, both in Chapter
18's comparison ledger (original lines 8213 and 8266). Each small
declaration precedes a longtable without an enclosing group.

The production correction consists of exactly four inserted lines:
begingroup and endgroup around each of those two tables. Their
small type remains local to the tables. No text, formula, theorem,
proof, citation or source import is edited.

The temporary after-correction trace checks 186 boundaries, covering
93 included files. Every entry and exit is now 10/12. The before
and after values are preserved in
[the trace table](font_scope_trace_20260922.tsv).
This is an actual TeX execution trace, not an assumption based only
on brace counting.

## Complete build

The production full build succeeds with 3,913 pages and
18,565,709 bytes. The page increase from 3,407 comes from restoring
the intended body size, not from adding mathematical content.
All references and citations resolve. There are eight horizontal
overflows and no vertical overflows, compared with 38 horizontal
overflows before the font-scope correction.

The remaining eight locations are:

- Chapter 9, line 1088: the contraction identity display;
- Chapter 14, line 2432: the pushforward/J identity display;
- Chapter 15's imported p031 proper-open persistent-anchor v58 proof,
  lines 37–43: one prose line;
- Chapter 18, line 5090: the open-polyannulus parameter display;
- Chapter 18, line 5342: the mixed-polycylinder parameter display;
- Chapter 18's imported interleaved-polyannulus/mixed-tower statement,
  line 41: a parameter display;
- Chapter 50, line 1889: the layer-cake identity display;
- Chapter 70's imported CONDUCTOR_IDEALS.tex, line 111: a paired definition.

These source locators refer to this snapshot. They are recorded for
the next layout pass, not hidden by enlarging the warning tolerance.

Physical pages 1413–1416 (printed 1345–1348) were rendered and
inspected for the two longtables, their continuation headers and
the return to normal body type. Page 1425 (printed 1357) confirms
the restored Chapter 19 opening. Physical pages 3323, 3325 and
3326 (printed 3255, 3257 and 3258) check the entropy statement,
proof and source note after reflow.

The closure still has 389 TeX files and 11,486 labels, with no
missing input, duplicate, dangling reference or structure defect.
The inventory still has 46 active atoms in 14 environments, tiers
(0,5,8,16,17). The source diff is whitespace-clean. No writing audit
is represented as necessary for these four grouping-only lines.
All frozen statement/proof bytes, including the author-supplied
CURVE_PSH.tex and Chapter 71, are unchanged.

PDF SHA-256:
`1aa7e12e7f76dc5b06ba9706c42c861398d496ab0901d9f7c2e09f908d7f7df5`

Chapter 18 SHA-256:
`98137a0d1a091e251fd54f7ac9dab5c8ffbe4991a8a92e59e3f9a8c0973cc6c7`

Chapter 18 is the only production file changed since 6146f45.
The next work is to resolve the eight remaining long lines while
preserving the exact frozen proof objects and their audit history.
