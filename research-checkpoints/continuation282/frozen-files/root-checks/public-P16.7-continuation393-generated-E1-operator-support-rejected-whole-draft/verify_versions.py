#!/usr/bin/env python3
"""Own bounded byte, serialization, encoding and source-unit observations."""
import hashlib
import json
import pathlib
import re

BASE = pathlib.Path('/workspace/research/campaigns/round-275/P16.7-whole390388389-general-E1-operator')
D = BASE / 'immutable-mathematical-DATA'
O = pathlib.Path(__file__).resolve().parent

def pick(prefix):
    found = list(D.glob(prefix + '*'))
    assert len(found) == 1
    return found[0]

def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()

def escape(s):
    table = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
             '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
             '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(table.get(c, c) for c in s)

def main():
    actual = json.loads(pick('191').read_bytes())
    expanded = json.loads(pick('190').read_bytes())
    assert len(actual['notes']) == len(expanded['notes']) == 4
    comp = pick('215').read_text()
    paper = pick('188').read_text()
    report = {'notes': [], 'candidate_actual': actual['candidate'],
              'candidate_expanded': expanded['candidate']}
    for i, (a, b) in enumerate(zip(actual['notes'], expanded['notes'])):
        raw = pick(str(201 + 2 * i)).read_text()
        long = pick(str(202 + 2 * i)).read_text()
        assert raw == a['text'] + '\n'
        assert long == b['text']
        assert b['text'] in comp
        report['notes'].append({'id':a['id'], 'actual_text_chars':len(a['text']),
                               'expanded_text_chars':len(b['text']),
                               'different':a['text'] != b['text'],
                               'actual_text_sha256':digest(a['text']),
                               'expanded_text_sha256':digest(b['text']),
                               'expanded_companion_offset':comp.index(b['text'])})
    ledger = pick('226').read_text()
    assert ledger in comp
    report['ledger_companion_offset'] = comp.index(ledger)
    cursor = 0
    gaps = []
    failures = []
    for i, line in enumerate(comp.splitlines(), 1):
        if not line:
            continue
        if line.startswith('### '):
            encoded = r'\subsubsection*{' + escape(line[4:]) + '}'
        elif line.startswith('## '):
            encoded = r'\subsection*{' + escape(line[3:]) + '}'
        elif line.startswith('# '):
            encoded = r'\section*{' + escape(line[2:]) + '}'
        else:
            encoded = escape(line)
        where = paper.find(encoded, cursor)
        if where < 0:
            failures.append(i)
            continue
        gap = paper[cursor:where]
        if gap.strip():
            gaps.append({'before_companion_line':i, 'text':gap})
        cursor = where + len(encoded)
    if paper[cursor:].strip():
        gaps.append({'after_last_line':True,'text':paper[cursor:]})
    report['encoding_missing_lines'] = failures
    report['encoding_unique_gaps'] = gaps
    src = pathlib.Path('/workspace/research/primary-data-LOCALONLY/P16.7-native264-whole-primary-and-retrieval-evidence-20261008/sources/CLD-v2-whole.txt').read_text()
    report['source_sha256'] = digest(src)
    report['ROOT388_source_units'] = []
    records = json.loads(pick('184').read_text())['new_full_read_primary_units']
    for row in records:
        unit = pathlib.Path(row['path']).read_text()
        start, end = row['literal_LF_inclusive']
        lf = '\n'.join(src.split('\n')[start-1:end])
        all_breaks = '\n'.join(src.splitlines()[start-1:end])
        heads = re.findall(r'(?:Définition|Proposition|Lemme|Corollaire|Exemple|Théorème)\s+\d+\.\d+\.\d+', unit)
        report['ROOT388_source_units'].append({'filename':pathlib.Path(row['path']).name,
                    'claimed_content':row['content'], 'headings_actually_in_unit':heads,
                    'equal_claimed_LF':unit.strip()==lf.strip(),
                    'equal_python_splitlines':unit.strip()==all_breaks.strip()})
    (O/'version-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    for key, value in report.items():
        print(key, json.dumps(value,ensure_ascii=False))

if __name__ == '__main__':
    main()
