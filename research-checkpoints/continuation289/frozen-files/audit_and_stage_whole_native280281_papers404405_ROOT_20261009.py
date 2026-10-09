from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,re,shutil
R=Path('/workspace/research');K=R/'root-checks'
A=R/'campaigns/round-280/P16.7-whole400398399-unbounded-uniqueness-and-compactness/artifacts/codex-4885oo'
B=R/'campaigns/round-281/P12.3-whole401-toric-and-general-envelope-residual/artifacts/codex-wbMyyv'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def constant_assignment(program,name):
    # Syntax-only parsing of inert native code, never import/eval/execute it.
    tree=ast.parse(program.read_text());values=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in node.targets):
            if isinstance(node.value,ast.Constant) and isinstance(node.value.value,str):values.append(node.value.value)
    assert len(values)==1;return values[0]
mapping={'\\':'\\textbackslash{}','{':'\\{','}':'\\}','$':'\\$','&':'\\&','#':'\\#','%':'\\%','_':'\\_','~':'\\textasciitilde{}','^':'\\textasciicircum{}'}
def escape280(text):
    out=[];code=False
    for c in text:
        if c=='`':out.append('}' if code else '\\texttt{');code=not code
        elif code and c=='/':out.append('/\\allowbreak ')
        else:out.append(mapping.get(c,c))
    return ''.join(out)
def render281(text):
    out=[]
    for part in re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',text,flags=re.S):
        if part.startswith(('\\[','\\(')):out.append(part)
        else:
            for line in part.splitlines(True):
                if line.startswith('# '):out.append('\\section{'+''.join(mapping.get(c,c) for c in line[2:].strip())+'}\n')
                elif line.startswith('## '):out.append('\\subsection{'+''.join(mapping.get(c,c) for c in line[3:].strip())+'}\n')
                else:out.append(''.join(mapping.get(c,c) for c in line))
    return ''.join(out)
body=A.joinpath('proof-companion.tex').read_text();ledger=A.joinpath('source-application-reading-ledger.md').read_text()
md='# Complete independent proof companion\n\nThis is the complete authored mathematical body, including old-chain reconstruction, new finite-extension and unbounded-probe proofs, and the scoped residual. The TeX below is preserved exactly from proof-companion.tex. External-source readings and deeper conventional dependencies are in the separate exact ledger. No old note is a correctness grant.\n\n```latex\n'+body+'```\n'
assert A.joinpath('proof-companion.md').read_text()==md
lt=[]
for line in ledger.splitlines():
    if line.startswith('<!--'):continue
    if line.startswith('## '):lt.append('\\subsection*{'+escape280(line[3:])+'}')
    elif line.startswith('# '):lt.append('\\section*{'+escape280(line[2:])+'}')
    else:lt.append(escape280(line))
head=constant_assignment(A/'build_deliverable.py','head')
assert A.joinpath('standalone.tex').read_text()==head+body+'\n\\clearpage\n'+'\n'.join(lt)+'\n\\end{document}\n'
raw280=load(K/'round280-raw-native-actual-FINAL.json');assert raw280['candidate'] is False
raw281=load(K/'round281-raw-native-actual-FINAL.json');expanded=load(B/'native-notes.json')
assert raw281==load(B/'actual-final.json') and expanded==load(B/'expanded-own-notes.json') and not expanded['candidate']
differences=[]
for a,e in zip(raw281['notes'],expanded['notes']):
    assert a['text']==B.joinpath('actual-return-'+a['id']+'.md').read_text() and e['text']==B.joinpath(e['id']+'.md').read_text()
    same={k:a[k]==e[k] for k in a};assert all(same[k] for k in ['id','summary','detailedSummary','support'])
    differences.append(dict(id=a['id'],fields_equal=same,actual_text_bytes=len(a['text'].encode()),expanded_text_bytes=len(e['text'].encode()),both_whole_bodies_ROOT_physically_read=True))
old=K/'public-P12.3-continuation401-toric-weight-envelopes-and-primary-correction-obstruction-unreviewed'
current=old.joinpath('P12.3-audit-and-toric-envelopes.tex').read_text();ret=B/'retained'
assert current==ret.joinpath('000-P12.3-audit-and-toric-envelopes.tex').read_text()
comp=old.joinpath('proof-companion.md').read_text();assert comp==ret.joinpath('015-proof-companion.md').read_text()
grant=load(ret/'incoming-G331.json');assert grant==load(B/'input.json')['notes'][0] and len(grant['text'].encode())==93375 and grant['text'] in current
own='\n\n'.join(n['text'] for n in expanded['notes'])
assert B.joinpath('proof-companion.md').read_text()==own+'\n\n# Entire retained active401 proof companion: historical DATA, not a premise\n\n'+comp+'\n\n# Entire incoming qualified G331, unchanged\n\n'+grant['text']
prefix=constant_assignment(B/'prepare_delivery.py','preamble');source=B.joinpath('P12.3-contact-envelopes.tex').read_text()
rendered=prefix+render281(own)+render281(B.joinpath('source-application-reading-ledger.md').read_text())+render281(B.joinpath('original-residual.md').read_text())
assert source.startswith(rendered)
task=load(B/'input.json')['task']
ending='\n\\appendix\n\\section{Exact original task and completion criteria, unchanged}\n\\begin{OriginalTaskDATA}\n'+task['problem']+'\n\n'+task['completionCriteria']+'\n\\end{OriginalTaskDATA}\n'
ending+='\\section{Exact actual final fields; expanded proof fields retained separately}\n\\begin{ActualFinalDATA}\n'+json.dumps(raw281,ensure_ascii=False,indent=2)+'\n\\end{ActualFinalDATA}\n'
ending+='\\section{Entire retained current401 standalone, including whole qualified appendices}\nThe following entire literal source is historical DATA. Only G331 is an incoming correctness grant; B341/E350 remain qualified historical data. Literal preservation does not assert a fresh whole historical audit.\n\\begin{WholeCurrentDATA}\n'+current+'\n\\end{WholeCurrentDATA}\n\\end{document}\n'
assert source==rendered+ending
assert B.joinpath('general-contact-proof.md').read_text() in expanded['notes'][0]['text']
tails=[]
for n,actual in [(280,raw280),(281,raw281)]:
    campaign=load(K/f'round{n}-terminal-actual-final-ROOT-retention-20261009.json')['campaign_result']
    assert campaign['candidate']==actual['candidate'] and len(campaign['notes'])==len(actual['notes'])
    for a,c in zip(actual['notes'],campaign['notes']):
        assert all(a[k]==c[k] for k in ['id','summary','detailedSummary','support']) and c['text'].startswith(a['text'])
        tails.append(dict(round=n,id=a['id'],tail=c['text'][len(a['text']):]))
now=datetime.now(timezone.utc).isoformat();Q=K/'round280281-ROOT-whole-serialization-and-first-mathematical-scope-audit-20261009.json'
programs=[A/x for x in ['build_deliverable.py','audit_packet.py','verify_rendering.py','check_source_units.py','check_deliverable.py','read_data.py','local_inputs.py','snapshot_inputs.py']]+[B/x for x in ['prepare_delivery.py','verify_delivery.py','contact_certificate.py']]
rec=dict(recorded_utc=now,actual_FINALs_ALL_five_fields_ROOT_physically_read=True,expanded281_differences=differences,whole280_formal_companion_ROOT_physically_read=True,whole281_all_four_expanded_proof_bodies_ROOT_physically_read=True,entire_both_standalone_component_rendering_identity=True,exact_existing401_and_G331_identity_not_independent_fresh_reading=True,all_unique_current_preambles_ledgers_residuals_ROOT_physically_read=True,terminal_campaign_tails=tails,programs_read_as_DATA=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in programs],native_or_supplied_programs_executed_or_imported=False,ROOT_mathematical_application_scope=['280 finite curve/surface extension normalizations and fixed-probe domination reconstructed under named analytic foundations','281 primary-blowup contact proof evaluated on valued QUOTIENT fields for ALL supports, normal-height-one containment and finite normalization','281 exact polyhedral/cancellation-sensitive any-field and Z_p examples reconstructed','No general nonisolated CE, actual sublevel compactness, arbitrary-support existence or original closure'],ROOT_source_location_correction_for280=dict(smooth_recognition='GRv2 unnumbered Section1.2',decreasing_closure_and_sheaf='Proposition4.2',local_maximum='Theorem6.1',affinoid_Shilov_maximum='Theorem6.4',native280_locations_4_2_6_1_6_4_interchanged=True,no_USC_regularization_theorem_in6_4=True,native_original_body_preserved_as_DATA=True),native_reading_ledgers_qualified_NOT_new_ROOT_recursive_primary_audit=True,source_bodies_units_pixels_books_LOCALONLY=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97),UNREVIEWED=True,accepted=False,original_closed=False,compiler_pending=True,protected_editor_OPEN_UNCHANGED=True)
write(Q,rec)
groups=[(404,280,A,'public-P16.7-continuation404-finite-extension-and-unbounded-probe-currents-unreviewed',['standalone.tex','proof-companion.tex','proof-companion.md','source-application-reading-ledger.md','scoped-verdict.json','original-residual.md']),
        (405,281,B,'public-P12.3-continuation405-excellent-germ-contact-and-nonmonomial-envelopes-unreviewed',['P12.3-contact-envelopes.tex','proof-companion.md','n1.md','n2.md','n3.md','n4.md','general-contact-proof.md','native-notes.json','expanded-own-notes.json','actual-final.json','actual-expanded-own-report.json','source-application-reading-ledger.md','original-residual.md','contact-input.json','contact-output.json'])]
staged=[]
for paper,n,a,label,names in groups:
    d=K/label;assert not d.exists();d.mkdir()
    for name in names:shutil.copyfile(a/name,d/name)
    shutil.copyfile(K/f'round{n}-raw-native-actual-FINAL.json',d/'raw-native-actual-FINAL.json')
    shutil.copyfile(K/f'round{n}-terminal-actual-final-ROOT-retention-20261009.json',d/'terminal-actual-FINAL-retention.json')
    shutil.copyfile(Q,d/'ROOT-whole-serialization-and-first-scope-audit.json')
    (d/'ROOT-review-scope.md').write_text(f'Whole working paper {paper}; UNREVIEWED. Original problem remains OPEN. Entire actual five-field FINALs and all distinct expanded/current unique mathematical bodies were ROOT physically read. Every full standalone is verified against its complete component rendering; inherited exact identities are not fresh historical proof readings. Native programs were read as DATA and never imported/executed. Compiler pending. Counts16solved26OPEN97accepted scopedpapers.\n\nNative280 GR source locations were interchanged in its formal classical-recognition paragraph and ledger: exact correction is in the accompanying ROOT audit. Proposition4.2 is sheaf/decreasing closure; Theorem6.1 local maximum; Theorem6.4 affinoid Shilov maximum, without a separate USC regularization theorem there. The source designation is unnumbered Section1.2. This source-location correction governs ROOT use; native original bodies remain intact. For paper405 the corrected earlier isolated chain is retained historical DATA and only full qualified G331 is an incoming grant. All source bodies/literal units/pixels/books remain LOCALONLY. No original acceptance or closure is implied.\n')
    files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(d.iterdir()) if p.is_file()]
    write(d/'ROOT-whole-proof-source-scope-and-binding.json',dict(recorded_utc=now,paper=paper,round=n,public_files=files,ROOT_audit=dict(path=str(Q),sha256=sha(Q)),UNREVIEWED=True,accepted=False,original_closed=False,compiler=dict(kind='pending'),counts=rec['counts'],primary_bodies_not_published=True,protected_editor_OPEN_UNCHANGED=True))
    staged.append(dict(paper=paper,directory=str(d),files=len(files)+1))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,native280281_whole_unreviewed_papers404405=dict(audit=str(Q),sha256=sha(Q),staged=staged),next_work='Compile whole404405. Prepare frozen282 whole402403404 original P16.7 generated uniqueness audit and actual compactness/existence; frozen283 whole405 arbitrary P12.3 residual. Publish regular verified NONFORCE checkpoint289 including exact GR citation revisions. No count change.')
    write(p,x)
print(json.dumps(dict(audit=str(Q),staged=staged,terminal_tails=tails,all_unique_math_read=True,standalone_identities=True,native_programs_executed=False,UNREVIEWED=True,original_closed=False),ensure_ascii=False,indent=2))
