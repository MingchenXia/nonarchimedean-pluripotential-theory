from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
R = Path('/workspace/research')
K = R / 'root-checks'
A276 = R / 'campaigns/round-276/P12.3-whole391392-formal-BIG-diagonal-and-original-residual/artifacts/codex-9EYfi9'
A277 = R / 'campaigns/round-277/P16.7-whole393-intrinsic-compactness-and-equation/artifacts/codex-9XWoHU'
out = K / 'round276277-ROOT-whole-serialization-and-unique-framing-audit-20261009.json'
assert not out.exists()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
escapes = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '#': r'\#', '$': r'\$', '%': r'\%', '&': r'\&', '_': r'\_', '^': r'\textasciicircum{}', '~': r'\textasciitilde{}'}
def escaped(s):
    return ''.join(escapes.get(c, c) for c in s)
def prose276(s):
    out = []
    for line in s.splitlines(True):
        h = re.fullmatch(r'(#{1,6}) ([^\n]*)(\n?)', line)
        if h:
            out.append('\\' + ('section' if len(h[1]) <= 2 else 'subsection') + '{' + escaped(h[2]) + '}\n')
        else:
            out.append(escaped(line))
    return ''.join(out)
def encode276(s):
    p = re.compile(r'\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|\$[^$]*?\$', re.S)
    pos = 0
    out = []
    for m in p.finditer(s):
        out.extend([prose276(s[pos:m.start()]), m[0]])
        pos = m.end()
    return ''.join(out) + prose276(s[pos:])
def line277(line):
    h = re.match(r'^(#{1,3}) (.*)$', line)
    if h:
        return '\\' + ['section', 'subsection', 'subsubsection'][len(h[1])-1] + '*{' + escaped(h[2]) + '}'
    out = []
    for f in re.split(r'(\$[^$\n]*\$|`[^`\n]*`)', line):
        if f.startswith('$') and f.endswith('$'):
            out.append(f)
        elif f.startswith('`') and f.endswith('`'):
            out.append(r'\texttt{' + escaped(f[1:-1]) + '}')
        else:
            out.append(escaped(f))
    return ''.join(out)
def encode277(s):
    return ''.join(f if f.startswith(r'\[') else '\n'.join(line277(line) for line in f.split('\n')) for f in re.split(r'(\\\[[\s\S]*?\\\])', s))
def remainder(tex, blocks, dest):
    intervals = []
    evidence = []
    for name, body in blocks:
        start = tex.find(body)
        assert start >= 0, name
        intervals.append((start, start+len(body)))
        evidence.append(dict(name=name, entire_exact_match=True, chars=len(body)))
    merged = []
    for a, b in sorted(intervals):
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(b, merged[-1][1])
        else:
            merged.append([a,b])
    chunks = []
    cursor = 0
    for a,b in merged:
        chunks.append(tex[cursor:a])
        cursor = b
    chunks.append(tex[cursor:])
    dest.write_text('\n\n'.join(chunks))
    return dict(matches=evidence, unique_framing_path=str(dest), unique_framing_sha256=sha(dest), unique_framing_chars=sum(map(len,chunks)), unique_framing_NOT_yet_physically_read=True)
actual276 = json.loads((K/'round276-raw-native-actual-FINAL.json').read_text())
artifact276 = json.loads((A276/'native-notes.json').read_text())
assert actual276 == artifact276 and not actual276['candidate']
proof = '\n\n'.join(n['text'].rstrip() for n in actual276['notes']) + '\n'
assert proof == (A276/'whole-proof.md').read_text()
blocks = [('whole-seven-actual-mathematical-bodies', encode276(proof))]
for name in ['whole-reading-ledger.md','whole-source-application-ledger.md','coverage.md','independent-scoped-verdict.md','original-residual.md']:
    blocks.append((name, encode276((A276/name).read_text())))
appendix = next((A276/'inputs/mathematical').glob('257-*'))
blocks.append(('entire-historical386-appendix-identity-only', encode276(appendix.read_text())))
for name in ['G331','B341','E350']:
    blocks.append(('entire-literal-qualified-'+name+'-identity-only', (A276/'inputs/grants'/f'{name}.txt').read_text()))
r276 = remainder((A276/'P12.3-formal-BIG-and-envelope.tex').read_text(), blocks, K/'round276-ROOT-entire-unique-TeX-framing-20261009.txt')
actual277 = json.loads((K/'round277-raw-native-actual-FINAL.json').read_text())
expanded277 = json.loads((A277/'final-notes.json').read_text())
assert not actual277['candidate'] and not expanded277['candidate'] and len(expanded277['notes']) == 5
for n in expanded277['notes']:
    assert n['text'] == (A277/(n['id']+'.md')).read_text()
comp = '# Independent generated operator and strictness on the nonalgebraizable quotient\n\nUnverified scoped proof draft. Original P16.7 remains unresolved.\n\n' + '\n\n'.join(n['text'] for n in expanded277['notes']) + '\n\n' + (A277/'source-application-ledger.md').read_text()
assert comp == (A277/'proof-companion.md').read_text()
r277 = remainder((A277/'scoped-paper.tex').read_text(), [('entire-five-expanded-bodies-ledger-and-companion-framing', encode277(comp))], K/'round277-ROOT-entire-unique-TeX-framing-20261009.txt')
rec = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), status='Exact entire serialization identity only; no mathematical certification', native276=r276, native277=r277, actual277_differs_from_artifact277=[dict(id=a['id'], entire_note_equal=a==b, text_equal=a['text']==b['text']) for a,b in zip(actual277['notes'],expanded277['notes'])], full_actual_final_bodies_and_all_five_fields_previously_physically_ROOT_read=True, expanded277_mathematical_texts_and_both_application_ledgers_now_physically_ROOT_read_untruncated=True, historical_appendix_and_literal_grants_are_identity_only_NOT_new_recursive_source_reads=True, native_or_supplied_programs_executed_or_imported=False, accepted=False, original_closed=False)
out.write_text(json.dumps(rec, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(rec, ensure_ascii=False, indent=2))
