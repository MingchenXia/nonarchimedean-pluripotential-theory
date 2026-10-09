from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,difflib
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-278/P12.3-whole396-corrected-formal-CE-and-original-residual'
A=C/'artifacts/codex-FagtMv'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
actual=load(K/'round278-raw-native-actual-FINAL.json');expanded=load(A/'native-notes.json')
retention=load(K/'round278-terminal-actual-final-ROOT-retention-20261009.json')
assert retention['public_status']['status']=='completed' and not actual['candidate'] and len(actual['notes'])==7
comparisons=[]
for a,b,t in zip(actual['notes'],expanded['notes'],retention['campaign_result']['notes']):
    assert a['id']==b['id']==t['id']
    assert set(a)==set(b)=={'id','summary','detailedSummary','text','support'}
    assert b['text']==(A/(b['id']+'.md')).read_text()
    fields={k:a[k]==b[k] for k in a}
    differences={k:dict(actual=a[k],expanded=b[k]) for k in a if k!='text' and not fields[k]}
    diff=list(difflib.unified_diff(a['text'].splitlines(keepends=True),b['text'].splitlines(keepends=True),fromfile='ACTUAL',tofile='EXPANDED',n=3)) if not fields['text'] else []
    assert t['text'].startswith(a['text'])
    comparisons.append(dict(id=a['id'],fields_equal=fields,metadata_differences=differences,text_difference=''.join(diff),actual_text_bytes=len(a['text'].encode()),expanded_text_bytes=len(b['text'].encode()),terminal_text_tail=t['text'][len(a['text']):],literal_double_backslash_occurrences=a['text'].count('\\\\')))
proof=(A/'proof-companion.md').read_text()
assert proof=='\n'.join(n['text'] for n in expanded['notes'])
escape={'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
def prose(s):return ''.join(escape.get(c,c) for c in s)
def render(s):
    out=[];display=False
    for line in s.splitlines():
        if line==r'\[':display=True
        if display:
            out.append(line)
            if line==r'\]':display=False
        elif line.startswith('# '):out.append(r'\section{'+prose(line[2:])+'}')
        elif line.startswith('## '):out.append(r'\subsection{'+prose(line[3:])+'}')
        else:out.append(prose(line))
    assert not display
    return '\n'.join(out)+'\n'
tex=(A/'P12.3-audit-and-toric-envelopes.tex').read_text();body=render(proof)
for name in ['source-application-ledger.md','whole-reading-ledger.md','coverage.md','independent-scoped-verdict.md','original-residual.md']:body+=render((A/name).read_text())
assert tex.count(body)==1
at=tex.index(body);prefix=tex[:at];suffix=tex[at+len(body):]
inp=load(C/'input.json');grants=[]
assert suffix.startswith('\\appendix\n')
expected='\\appendix\n'
for note in inp['notes']:
    expected+='\\section{Entire qualified '+note['id']+'; unchanged source and qualifications}\n'+'\\begin{QualifiedInput}\n'+note['text']+'\n\\end{QualifiedInput}\n'
    grants.append(dict(id=note['id'],bytes=len(note['text'].encode()),sha256=hashlib.sha256(note['text'].encode()).hexdigest(),duplicate_exact_inherited_qualified_grant=True,independent_fresh_historical_reading=False))
expected+='\\end{document}\n'
assert suffix==expected
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=278,raw_actual_FINAL_sha256=sha(K/'round278-raw-native-actual-FINAL.json'),expanded_notes_sha256=sha(A/'native-notes.json'),comparisons=comparisons,whole_proof_companion_exact_expanded_join=True,standalone_whole_math_and_ledgers_contiguous_complete_render_identity=True,standalone=dict(path=str(A/'P12.3-audit-and-toric-envelopes.tex'),bytes=len(tex.encode()),sha256=sha(A/'P12.3-audit-and-toric-envelopes.tex')),unique_standalone_prefix=prefix,qualified_appendix_identity=grants,entire_actual_notes_all_five_fields_ROOT_physically_read=True,source_ledgers_ROOT_physically_read_as_native_evidence_NOT_fresh_recursive_ROOT_audit=True,all_six_native_programs_entirely_READ_AS_DATA_not_executed_or_imported=True,new_toric_proofs_independently_reconstructed_at_named_conventional_foundations=True,UNREVIEWED=True,accepted=False,original_closed=False,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
q=K/'round278-ROOT-whole-serialization-and-toric-first-audit-20261009.json';assert not q.exists();q.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
