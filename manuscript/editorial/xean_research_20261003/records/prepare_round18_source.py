"""Prepare reviewed curve-recognition paper; exact PASS/read attestation required."""
from pathlib import Path
import datetime, hashlib, json, re

ROOT = Path('/workspace/research')
REVIEW = ROOT/'campaigns/round-13/P06.2-arbitrary-field-curve-recognition-review'
OUT = ROOT/'deliverables/round-18'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
run = json.loads((REVIEW/'run.json').read_text())
result = run['campaign']['result']
attestation = json.loads((REVIEW/'review-read-attestation.json').read_text())
binding = json.loads((REVIEW/'source-artifact-binding.json').read_text())
assert run['campaign']['status'] == 'completed' and result['verdict'] == 'PASS'
assert attestation['publish_exact_scope'] and attestation['full_report_premises_and_passages_read']
assert attestation['run_sha256'] == sha(REVIEW/'run.json')
source = Path(binding['source_tex']).read_text()
assert sha(Path(binding['source_tex'])) == binding['source_tex_sha256']
edits = []

def replace(before, after, reason, count=1):
    global source
    assert source.count(before) == count, (before, source.count(before))
    edits.append({'before': before, 'after': after,
                  'expected_occurrences': count, 'reason': reason})
    source = source.replace(before, after)

replace('pdfauthor={Unverified research draft; author self-audit only}',
        'pdfauthor={Xean research manuscript}', 'Publication metadata only.')
replace(r'\author{Unverified research draft; author self-audit only}',
        r'\author{Xean research manuscript}', 'Publication metadata only.')
replace(r'\setmainfont[]{DejaVu Serif}', r'\setmainfont{Latin Modern Roman}',
        'Portable native-editor text font; no mathematical change.')
replace(r'\setmonofont[]{DejaVu Sans}', r'\setmonofont{Latin Modern Mono}',
        'Portable native-editor monospace font; no mathematical change.')

start = source.index(r'\section{Appendix S. Primary bodies, extracted by newline')
bib = source[source.index(r'\section{Bibliography}', start):]
old = source[start:]
new = r'''\section{Appendix S. Source audit and complete supplement}

The accompanying frozen argument
\texttt{P06.2-arbitrary-field-curve-recognition-argument.md} retains
all complete primary statements and proof bodies embedded in the exact
independently reviewed input. The paper retains the entire reconstructed
mathematical proof and moves the source-data appendix to that supplement.
The review receipt records every stated external premise, its quoted
passage and the exact artifact bindings. Publication metadata, source
inventory, fonts and alphabet grouping are the only editorial changes.
No new mathematical premise or argument is introduced.

The sixty-one extracted primary blocks are matched to their exact cached
files using newline boundaries. Page form feeds are removed solely for
quotation display. The completed-algebraic transport bodies match the
corrected packet accompanying the earlier curve-ascent paper. The
original appendix-selection defect and earlier review remain preserved
in their historical checkpoints. The newly used curve-recognition and
harmonicity sources and their applications are separately included in
this paper's frozen review argument.

The proof uses polyhedrality and the upper dimension bound, rather than
the universal dimension-equality phrase in CLD 12.2.4. It uses compact
cutoffs, rather than the broad fixed-index formulation in CLD 15.2.9.
It does not use the unsupported S1 reduction in CLD 16.7.5. Component
weights and actual nonreduced structures are retained for integration.
An algebraic ordinary test on a Wanner chart is used as an analytic
ordinary test; the converse equality of the two test sheaves is not
assumed.

The root read the complete mathematical core directly or matched its
reused bodies exactly to previously fully read proofs. New applications
and all source-block bindings were checked. This does not assert a
fresh line-by-line reading of every unused quotation in the entire
source-data appendix. Independent source-aware review is a mathematical
audit, not formal verification or priority certification. Original
P06.2 in arbitrary ambient dimension remains open as specified above.

''' + bib
replace(old, new,
        'Move source-data quotations and primary transcription into the intact frozen argument accompanying the paper. Mathematical core retained.')

start = source.index('The authoritative file is ')
end = source.index(r'\section{Appendix S.', start)
old = source[start:end]
new = r'''The complete frozen argument and source supplement accompany this paper,
together with the exact-scope independent review receipt. Xean's native
Codex path used \texttt{gpt-6.1-sol} with \texttt{xhigh} reasoning. The
review report, every premise and every supporting passage were read,
and the proof/source artifact bindings were checked before publication.
The recorded source and build checks bind bytes and typesetting; they
are not mathematical proof certificates. Historical author drafts,
failed attempts and earlier checkpoints are preserved.

'''
replace(old, new, 'Replace historical author self-audit/build instructions by accurate publication provenance.')

# Point mathematical-core citations at the complete external supplement.
core_end = source.index(r'\section{Appendix S.')
core = source[:core_end]
updated_core = re.sub(r'Appendix\s+S',
                      'the complete source supplement indexed in Appendix S', core)
replace(core, updated_core,
        'Accurate location of unchanged complete source proof bodies; appendix heading preserved.')

# Native unicode-math requires braced alphabet and script arguments.
for token in sorted(set(re.findall(r'\\(?:mathbb|mathcal|mathfrak)\s*[A-Za-z]', source)),
                    key=len, reverse=True):
    command, letter = re.fullmatch(r'(\\(?:mathbb|mathcal|mathfrak))\s*([A-Za-z])', token).groups()
    replace(token, command+'{'+letter+'}',
            'Harmless alphabet grouping for native unicode-math.', source.count(token))
for token in sorted(set(re.findall(r'[_^]\\(?:mathbb|mathcal|mathfrak)\{[A-Za-z]\}', source))):
    replace(token, token[0]+'{'+token[1:]+'}',
            'Harmless script grouping for native unicode-math.', source.count(token))

assert source.count(r'\end{document}') == 1
OUT.mkdir(exist_ok=False)
tex = OUT/'P06.2-arbitrary-field-curve-recognition.tex'
tex.write_text(source)
(REVIEW/'publication-edits.json').write_text(json.dumps(edits, ensure_ascii=False, indent=2)+'\n')
record = {
    'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'tex': str(tex), 'sha256': sha(tex), 'governing_review': str(REVIEW),
    'publication_edits_sha256': sha(REVIEW/'publication-edits.json'),
    'native_compilation_pending': True,
}
(ROOT/'deliverables/round-18-source-preparation.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
