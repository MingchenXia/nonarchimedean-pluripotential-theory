from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
R=Path('/workspace/research');K=R/'root-checks'
A=R/'campaigns/round-279/P16.7-whole397394395-full-uniqueness-and-compactness/artifacts/codex-lAR38i'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
raw=K/'round279-raw-native-actual-FINAL.json';actual=json.loads(raw.read_text())
expanded=json.loads((A/'final-notes.json').read_text())
ret=json.loads((K/'round279-terminal-actual-final-ROOT-retention-20261009.json').read_text())
assert sha(raw)==ret['raw_actual_FINAL']['sha256'] and len(actual['notes'])==len(expanded['notes'])==5
records=[];bodies=[]
for a,e in zip(actual['notes'],expanded['notes']):
    md=A/(a['id']+'.md');s=md.read_text().rstrip('\n');bodies.append(s)
    records.append(dict(id=a['id'],md_sha256=sha(md),md_equal_actual_text=s==a['text'],md_equal_expanded_text=s==e['text'],all_five_fields_equal={k:a[k]==e[k] for k in a},double_backslashes=a['text'].count('\\\\'),single_display_open_lines=sum(x==r'\[' for x in a['text'].split('\n')),double_display_open_lines=sum(x==r'\\[' for x in a['text'].split('\n'))))
    assert s==a['text']==e['text']
ledger=(A/'source-application-reading-ledger.md').read_text().strip();residual=(A/'original-residual.md').read_text().strip()
comp=(A/'proof-companion.md').read_text();expected='# New standalone scoped proof companion\n\n'+'\n\n'.join(bodies)+'\n\n'+ledger+'\n\n'+residual+'\n'
assert comp==expected
def escape(s):
    tab={'&':r'\&','%':r'\%','#':r'\#','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}','{':r'\{','}':r'\}'}
    return ''.join(tab.get(c,c) for c in s)
def prose(s):
    out=''
    for part in re.split(r'(`[^`]*`|\$[^$]*\$)',s):
        if part.startswith('`') and part.endswith('`'):out+=r'\texttt{'+escape(part[1:-1]).replace('/',r'/\allowbreak ')+'}'
        elif part.startswith('$') and part.endswith('$'):out+=part
        else:out+=escape(part)
    return out
lines=[];math=False
for line in comp.split('\n'):
    if line.startswith('# '):lines.append(r'\section*{'+prose(line[2:])+'}')
    elif line.startswith('## '):lines.append(r'\subsection*{'+prose(line[3:])+'}')
    elif line.strip()==r'\[':math=True;lines.append(line)
    elif line.strip()==r'\]':math=False;lines.append(line)
    elif math:lines.append(line)
    else:lines.append(prose(line))
assert not math
encoded='\n'.join(lines);main=(A/'paper-main.tex').read_text();tex=(A/'scoped-paper.tex').read_text()
assert tex==main+encoded+'\n\\end{document}\n'
campaign=ret['campaign_result']['notes'];third=[]
for a,c in zip(actual['notes'],campaign):
    third.append(dict(id=a['id'],fields_equal={k:a[k]==c[k] for k in a},actual_text_is_prefix=c['text'].startswith(a['text']),extra_tail=c['text'][len(a['text']):] if c['text'].startswith(a['text']) else None))
out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=279,actual_FINAL_sha256=sha(raw),actual_vs_expanded_fields=records,campaign_result_distinct_serialization=third,whole_companion_exact_components=True,whole_companion_unique_framing='# New standalone scoped proof companion\n\n',whole_tex_exact_components=True,whole_tex_unique_prefix=dict(path=str(A/'paper-main.tex'),sha256=sha(A/'paper-main.tex'),bytes=len(main.encode()),ROOT_entire_framing_physically_read=True),whole_tex_unique_suffix='\n\\end{document}\n',entire_actual_notes_all_five_fields_ROOT_physically_read=True,entire_ledger_and_residual_ROOT_physically_read=True,all_three_native_programs_ROOT_physically_read_as_DATA=True,native_programs_executed_or_imported=False,identity_is_not_a_fresh_duplicate_mathematical_reading=True,independent_math_review='Countable constrained diagonal reconstructed step by step; compact strict USC domination, simultaneous finite continuous bounds, summable correction, exact pointwise infimum and monotone canonical energy are valid under reconstructed foundations. Full original closure is not claimed.',all_primary_source_bodies_pixels_books_LOCALONLY=True,UNREVIEWED=True,accepted=False,original_closed=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
P=K/'round279-ROOT-whole-serialization-and-constrained-diagonal-first-audit-20261009.json';P.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(P),actual_vs_expanded_fields=records,whole_companion_exact_components=True,whole_tex_exact_components=True,whole_unique_framing=out['whole_companion_unique_framing'],tex_suffix=out['whole_tex_unique_suffix'],original_closed=False),ensure_ascii=False,indent=2))
