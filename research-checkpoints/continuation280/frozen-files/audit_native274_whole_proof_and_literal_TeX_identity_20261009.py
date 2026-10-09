from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
R=Path('/workspace/research'); K=R/'root-checks'
A=R/'campaigns/round-274/P12.3-whole386-Jensen-completion-and-original-residual/artifacts/codex-gTwO5f'
O=K/'round274-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not O.exists()
actual=json.loads((K/'round274-actual-native-final.json').read_text()); expanded=json.loads((A/'native-notes.json').read_text())
assert len(actual['notes'])==len(expanded['notes'])==5 and not actual['candidate'] and not expanded['candidate']
comp=(A/'whole-proof.md').read_text(); completion=(A/'completion-proof.md').read_text(); review=(A/'independent-review.md').read_text()
assert comp==completion+'\n'+review and sha(A/'whole-proof.md')=='865cc3b84e16df873a9b7ac2c5adcb81857bf8d07422d763754dce0784fb9afd'
table={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','#':r'\#','$':r'\$','%':r'\%','&':r'\&','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
def escape(s):return ''.join(table.get(c,c) for c in s)
math=re.compile(r'(\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|\$[^$]*?\$)',re.S)
def prose(s):
    out=[]
    for line in s.splitlines(keepends=True):
        heading=re.match(r'^(#{1,6}) (.*?)(\n?)$',line)
        if heading:out.append('\\'+('section' if len(heading[1])<=2 else 'subsection')+'{'+escape(heading[2])+'}\n')
        else:out.append(escape(line))
    return ''.join(out)
def encode(s):return ''.join(t if math.fullmatch(t) else prose(t) for t in math.split(s))
tex=(A/'P12.3-completion-and-formal-lifting.tex').read_text(); begin='% BEGIN OWN COMPLETE MATH/PROSE\n'; end='% END OWN COMPLETE MATH/PROSE\n'
a=tex.index(begin); b=tex.index(end,a+len(begin)); assert tex[a+len(begin):b]==encode(comp)
eb='% BEGIN EXAMINED MATH/PROSE\n'; ee='% END EXAMINED MATH/PROSE\n'; c=tex.index(eb,b); d=tex.index(ee,c+len(eb))
exam=next((A/'inputs-LOCALONLY/math').glob('257-*')); assert tex[c+len(eb):d]==encode(exam.read_text())
uniques=[tex[:a+len(begin)],tex[b:c+len(eb)],tex[d:]]
appendices=[]
for title,p in [('Own full source/application ledger',A/'source-application-ledger.md'),('Own full coverage',A/'coverage.md'),('Own unchanged original residual',A/'original-residual.md'),('Own exact decision',A/'scope-and-decision.json')]+[('Entire qualified '+n+' unchanged',A/'inputs-LOCALONLY/grants'/(n+'.txt')) for n in ['G331','B341','E350']]:
    body=p.read_text(); assert body in uniques[2]
    start='\\section{'+escape(title)+'}\n\\begin{QualifiedData}\n'; frame=start+body+('' if body.endswith('\n') else '\n')+'\\end{QualifiedData}\n'
    assert frame in uniques[2]; uniques[2]=uniques[2].replace(frame,'',1)
    appendices.append(dict(title=title,path=str(p),bytes=p.stat().st_size,sha256=sha(p),whole_literal_body_in_TeX=True,duplicate_not_new_physical_reading=True))
comparisons=[]; outside=[]
for i,(aa,ee_) in enumerate(zip(actual['notes'],expanded['notes'])):
    assert aa['id']==ee_['id'] and (A/(ee_['id']+'.md')).read_text()==ee_['text']
    if i<3:assert ee_['text'].split('\nArtifacts:')[0].strip() in completion
    if i==3:assert ee_['text'].split('\nArtifacts:')[0].strip()==review.strip()
    comparisons.append(dict(id=ee_['id'],actual_text_sha256=hashlib.sha256(aa['text'].encode()).hexdigest(),expanded_text_sha256=hashlib.sha256(ee_['text'].encode()).hexdigest(),DIFFERENT=aa['text']!=ee_['text'],expanded_bytes=len(ee_['text'].encode())))
    outside.append({k:v for k,v in ee_.items() if k!='text'})
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=274,paper_sha256=sha(A/'P12.3-completion-and-formal-lifting.tex'),proof_sha256=sha(A/'whole-proof.md'),actual_FINAL_sha256=sha(K/'round274-actual-native-final.json'),expanded_sha256=sha(A/'native-notes.json'),all_five_entire_actual_fields_ROOT_physically_read_untruncated=True,entire43457character_companion_ROOT_physically_read_untruncated=True,character_intervals=[[0,18000],[17700,36500],[36200,43457]],truncated_combined_second_display_repaired_by_individual_full_read=True,expanded_n5_and_entire_ledger_coverage_residual_ROOT_physically_read_untruncated=True,whole_companion_and_examined386_exact_math_preserving_TeX_encoding=True,appendices=appendices,entire_unique_TeX_segments=uniques,comparisons=comparisons,completion_scope_correction='Accepted G331 already contains full normalized completion and C/D invariance. Envelope/Jensen transport is a corollary, not new original closure or general CE.',native_assemble_delivery_entirely_read_AS_DATA_only=True,supplied_or_native_programs_executed_or_imported=False,new_accepted=False,whole_original_solved=False)
O.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(audit=str(O),audit_sha256=sha(O),record=record,all_five_entire_expanded_outside_fields=outside),ensure_ascii=False,indent=2))
