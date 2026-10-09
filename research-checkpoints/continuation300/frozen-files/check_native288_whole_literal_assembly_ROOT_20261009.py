"""Verify whole literal components without executing or importing native programs."""
from pathlib import Path
import hashlib, json

C = Path('/workspace/research/campaigns/round-288/P12.3-whole413-general-excellent-and-characteristic-envelope-residual')
A = C / 'artifacts/codex-mpzScc'
K = Path('/workspace/research/root-checks')
math = json.loads((C / 'mathematical-packet-bindings.json').read_text())
raw = json.loads((K / 'round288-raw-native-actual-FINAL.json').read_text())
native = json.loads((A / 'notes.json').read_text())
inp = json.loads((A / 'input.json').read_text())
g = next(n for n in inp['notes'] if n['id'] == 'G331')
assert len(g['text'].encode()) == 93375
for a, b in zip(raw['notes'], native['notes']):
    assert {k: a[k] for k in a if k != 'text'} == {k: b[k] for k in b if k != 'text'}
    assert b['text'] == a['text'] + '\n'
def esc(s):
    table = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '$': r'\$', '&': r'\&', '#': r'\#', '%': r'\%', '_': r'\_', '^': r'\textasciicircum{}', '~': r'\textasciitilde{}'}
    return ''.join(table.get(c, c) for c in s)
source = (A / 'P12.3-surface-envelopes.tex').read_text()
texes = [(A / ('n' + str(i) + '.tex')).read_text() for i in range(1, 5)]
head = source[:source.index(texes[0])]
paper = head + '\n'.join(texes)
for title, name in [('Exact source/application/reading ledger', 'source-application-reading-ledger.md'), ('Separate scoped verdict', 'scoped-verdict.md'), ('Unchanged original residual', 'original-residual.md')]:
    paper += '\n\\section*{' + esc(title) + '}\n' + esc((A / name).read_text()) + '\n'
paper += '\n\\appendix\n\\section{Entire qualified incoming G331, with all qualifications}\n\\begin{QualifiedGrantDATA}\n' + g['text'] + '\n\\end{QualifiedGrantDATA}\n'
paper += '\n\\section{Entire current413 actual and distinct expanded proof DATA}\n'
actual413 = json.loads(Path(math[18]['path']).read_text())
for j, n in enumerate(actual413['notes'], 1):
    paper += '\n\\subsection*{Audited current413 actual FINAL ' + esc(n['id']) + '}\n' + esc(json.dumps(n, ensure_ascii=False, indent=2)) + '\n'
    paper += Path(math[2*j+3]['path']).read_text() + '\n'
paper += '\n\\section{Entire unchanged original task and criteria}\n' + esc(json.dumps(inp['task'], ensure_ascii=False, indent=2)) + '\n\\end{document}\n'
assert paper == source
comp = '# ENTIRE proof companion; unverified scoped draft, candidate=false\n\n'
for n, t in zip(native['notes'], texes):
    comp += '\n## Own actual FINAL ' + n['id'] + '\n\n' + json.dumps(n, ensure_ascii=False, indent=2) + '\n\n## Entire literal authoritative actual text ' + n['id'] + '\n\n' + n['text'] + '\n\n## Distinct expanded TeX ' + n['id'] + '\n\n' + t + '\n'
comp += '\n## ENTIRE qualified G331\n\n' + g['text'] + '\n'
for i in [18, 5, 7, 9, 11, 13, 20, 19, 16, 0, 17]:
    p = Path(math[i]['path'])
    comp += '\n## ENTIRE retained current413 DATA ' + p.name + '\n\n' + p.read_text() + '\n'
for name in ['source-application-reading-ledger.md', 'scoped-verdict.md', 'original-residual.md', 'original-task.json']:
    comp += '\n## ENTIRE own ' + name + '\n\n' + (A / name).read_text() + '\n'
assert comp == (A / 'proof-companion.md').read_text()
record = dict(whole_source_exact_ROOT_literal_reconstruction=True, whole_companion_exact_ROOT_literal_reconstruction=True, current_actual_note_serialization_difference='Exactly ONE trailing LF in each native artifact note versus captured actual settled FINAL; all other five fields equal', new_actual_and_distinct_expanded_all_four_ROOT_physically_read=True, current413_and_G331_whole_retention_identity_not_extra_fresh_reading=True, native_programs_executed_or_imported=False, source_bytes=len(source.encode()), source_sha256=hashlib.sha256(source.encode()).hexdigest(), companion_bytes=len(comp.encode()), companion_sha256=hashlib.sha256(comp.encode()).hexdigest(), original_closed=False, accepted=False)
Q = K / 'round288-whole-literal-assembly-and-serialization-ROOT-check-20261009.json'
assert not Q.exists()
Q.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, indent=2))
