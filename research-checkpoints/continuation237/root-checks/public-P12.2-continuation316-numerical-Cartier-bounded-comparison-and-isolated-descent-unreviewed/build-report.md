# Standalone build and diagnostic report

All four observed TeX runs exited successfully (exit 0 in native tool results). No initial build failure occurred. All initial warning output is retained; no supplied builder was executed. The separate failed own edit is preserved in evidence/edit-report.md.

Final paper: `14` pages. Engine: `pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian)`. Shell escape was disabled.

| Run | Successful PDF output | Fatal errors | Warnings retained |
|---|---|---|---|
| build/pass1.stdout | True | False | Overfull \hbox (22.96107pt too wide) in paragraph at lines 345--354; Package rerunfilecheck Warning: File `P12.2-paper.out' has changed. |
| build/pass2.stdout | True | False | none |
| build/pass3.stdout | True | False | none |
| build/pass4.stdout | True | False | none |

The initial build has one 22.96107pt overfull box and an outline-rerun warning. Its log and PDF are preserved as `build/pass1.log` and `build/pass1.pdf`. The source record and scope clarification were then expanded and the footer reflowed; corrected-source runs pass2 and pass3 report no warnings or overfull boxes. The final finite-real-cone comparison expansion was built in pass4, also without warnings or overfull boxes. All logs are preserved separately. The current `build/P12.2-paper.log` is the final log.

Own exact diagnostics: seven node correction cases at k=1,2,3,4,8,16,32 and the valuation sign example (retracted value 1, actual value 2). All exact assertions passed. Note schema/support validation also passed. These are finite diagnostics and structural checks, not exhaustive geometry, independent review, or mathematical correctness certification.

Rerun the commands in README.md and commands.md. PDF metadata and source-range hashes are in environment.json and evidence/source-units.json.
