"""Own byte/body diagnostics; no supplied module is imported or executed."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
records = json.loads((ROOT / 'reports/input-hashes.json').read_text())
paths = {r['key']: ROOT / r['local'] for r in records}

def untex(s):
    # Exactly the display substitutions observed in this bound paper.
    for a, b in [('\\textasciicircum{}', '^'), ('\\_', '_'), ('\\&', '&'), ('\\%', '%'),
                 ('\\#', '#'), ('\\{', '{'), ('\\}', '}')]:
        s = s.replace(a, b)
    return s

current = json.loads(paths['m61'].read_text())
actual = json.loads(paths['m62'].read_text())
argument = paths['m60'].read_text()
paper = paths['m58'].read_text()
rows = []
for i, n in enumerate(current['notes']):
    body = n['text']
    plain = untex(paper)
    # Published equations use TeX math instead of the already-read text notation.
    paragraphs = [p for p in body.split('\n\n') if p.strip()]
    missing = [p for p in paragraphs if p not in plain]
    rows.append({'id': n['id'], 'exact_expanded_in_argument': body in argument,
                 'exact_expanded_note_file': body == paths[f'm{70+i}'].read_text(),
                 'actual_equals_expanded': actual['notes'][i]['text'] == body,
                 'tex_nonliteral_paragraphs': len(missing)})
    d = ROOT / 'review-data/current-extra'; d.mkdir(parents=True, exist_ok=True)
    (d / f'{n["id"]}-tex-nonliteral.txt').write_text('\n\n'.join(missing))

# The Markdown paper appends scope/coverage. Check and extract ONLY its extra data.
md = paths['m59'].read_text()
md_extra = md.replace(argument, '') if argument in md else md
(ROOT / 'review-data/current-paper-md-extra.txt').write_text(md_extra)

# Current typesetting body paragraphs are matched explicitly to the read argument.
arg_paras = [untex(p) for p in argument.split('\n\n')]
tex_extra = []
for p in paper.split('\n\n'):
    q = untex(p).strip()
    if not q: continue
    if q in arg_paras: continue
    if q.startswith('\\section{'): continue
    tex_extra.append(p)
(ROOT / 'review-data/current-paper-tex-extra.txt').write_text('\n\n'.join(tex_extra))

historical = json.loads(paths['m34'].read_text())
harg = paths['m33'].read_text()
hrows=[]
for i,n in enumerate(historical['notes']):
    hrows.append({'id':n['id'], 'exact_body_in_historical_argument':n['text'] in harg,
                  'exact_note':n['text']==paths[f'm{42+i}'].read_text()})

report={'current_eleven': rows, 'historical_seven':hrows,
        'current_actual_fields_read_separately':True,
        'historical_reading_duplicates_is_seven_254_not_current_eleven_257':True,
        'markdown_argument_exact_duplicate':argument in md,
        'matching_is_not_fresh_reading_or_correctness':True}
(ROOT / 'reports/reading-bindings.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'current_bodies':len(rows),'historical_bodies':len(hrows),
                  'md_exact_argument':argument in md,
                  'tex_extra_chars':sum(map(len,tex_extra))}))
