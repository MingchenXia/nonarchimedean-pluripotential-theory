from pathlib import Path
from datetime import datetime,timezone
import ast,difflib,hashlib,json,re,shutil,textwrap
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-283/P12.3-whole405-contact-and-arbitrary-envelope-residual'
A=C/'artifacts/codex-SZjDaw';I=C/'immutable-mathematical-DATA'
D=K/'public-P12.3-continuation408-canonical-obstacle-filtration-and-finite-generation-envelopes-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
raw=load(K/'round283-raw-native-actual-FINAL.json');expanded=load(A/'notes.json');incoming=load(C/'input.json')
assert raw['candidate'] is expanded['candidate'] is False and len(raw['notes'])==len(expanded['notes'])==4
assert incoming==load(A/'input.json') and len(incoming['notes'])==1 and incoming['notes'][0]['id']=='G331'
known={'G331'};differences=[]
for a,e in zip(raw['notes'],expanded['notes']):
    assert set(a)==set(e)=={'id','summary','detailedSummary','text','support'}
    equal={k:a[k]==e[k] for k in a};assert all(equal[k] for k in ['id','summary','detailedSummary','support'])
    assert e['text']==(A/(e['id']+'.md')).read_text() and set(e['support'])<=known
    known.add(e['id'])
    delta=''.join(difflib.unified_diff(a['text'].splitlines(True),e['text'].splitlines(True)))
    if a['id']=='n2':assert e['text']==a['text'].replace('p(f)=sup{u in D:u<=f}','p(f)=sup\\{u in D:u<=f\\}')
    else:assert a['text']==e['text']
    differences.append(dict(id=a['id'],fields_equal=equal,actual_bytes=len(a['text'].encode()),expanded_bytes=len(e['text'].encode()),all_actual_fields_ROOT_physically_read=True,distinct_expanded_body_ROOT_physically_read=True,diff=delta))
task=incoming['task'];assert task==load(A/'original-task.json')
assert (A/'original-problem.txt').read_text()==task['problem'] and (A/'original-completion-criteria.txt').read_text()==task['completionCriteria']
old=K/'public-P12.3-continuation405-excellent-germ-contact-and-nonmonomial-envelopes-unreviewed'
inherited_source=(I/'000-P12.3-contact-envelopes.tex').read_text();inherited_comp=(I/'017-proof-companion.md').read_text()
assert inherited_source==(old/'P12.3-contact-envelopes.tex').read_text() and inherited_comp==(old/'proof-companion.md').read_text()
actual_data=(I/'006-actual-final.json').read_text();expanded_data=(I/'009-expanded-own-notes.json').read_text()
assert json.loads(actual_data)==load(old/'actual-final.json') and json.loads(expanded_data)==load(old/'expanded-own-notes.json')
grant=incoming['notes'][0]['text'];assert len(grant.encode())==93375 and grant in inherited_source
ledger=(A/'source-application-reading-ledger.md').read_text();residual=(A/'original-residual.md').read_text()
own='\n\n'.join(n['text'] for n in expanded['notes'])
companion='# Entire own proof companion and inherited DATA retention\n\n'+own+'\n\n'+ledger+'\n\n'+residual
companion+='\n\n# ENTIRE incoming qualified G331 (grant, all qualifications attached)\n\n'+grant
companion+='\n\n# ENTIRE actual405 five-field FINAL DATA, distinct from expansion\n\n'+actual_data
companion+='\n\n# ENTIRE expanded405 five-field notes DATA\n\n'+expanded_data
companion+='\n\n# ENTIRE inherited405 proof companion DATA (not a fresh whole audit)\n\n'+inherited_comp
companion+='\n\n# ENTIRE inherited405 standalone source DATA (not newly accepted)\n\n'+inherited_source
assert (A/'proof-companion.md').read_text()==companion
# Inert syntax inspection extracts one constant; native program is never evaluated, imported or executed.
values=[]
for node in ast.walk(ast.parse((A/'build_artifacts.py').read_text())):
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='preamble' for t in node.targets):
        assert isinstance(node.value,ast.Constant) and isinstance(node.value.value,str);values.append(node.value.value)
assert len(values)==1
mapping={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
def escape(s):return ''.join(mapping.get(c,c) for c in s)
def render(s):
    out=[]
    for b in re.split(r'(\\\[.*?\\\])',s,flags=re.S):
        if b.startswith('\\['):out.append(b)
        else:
            for p in b.split('\n\n'):
                if p.startswith('# '):out.append('\\section{'+escape(p[2:])+'}')
                elif p.startswith('## '):out.append('\\subsection{'+escape(p[3:])+'}')
                else:out.append(escape(p))
    return '\n\n'.join(out)
def retained(title,data):
    assert '\\end{RetainedDATA}' not in data
    wrapped='\n'.join('\n'.join(textwrap.wrap(line,140,replace_whitespace=False,drop_whitespace=False,break_long_words=True,break_on_hyphens=False)) if line else '' for line in data.splitlines())
    return '\n\\section*{'+escape(title)+'}\n\\begin{RetainedDATA}\n'+wrapped+'\n\\end{RetainedDATA}\n'
tex=values[0]+'\n'.join(render(n['text']) for n in expanded['notes'])+render(ledger)+render(residual)+'\n\\appendix\n'
units=[('Entire qualified G331, including every annotation and ledger',grant),('Entire unchanged original problem and completion criteria',task['problem']+'\n\n'+task['completionCriteria']),('Entire actual405 FINAL DATA; distinct expanded texts follow',actual_data),('Entire expanded405 notes DATA',expanded_data),('Entire inherited405 companion DATA; unread inherited parts are not audited',inherited_comp),('Entire inherited405 standalone DATA; historical grants are not renewed',inherited_source)]
tex+=''.join(retained(t,d) for t,d in units)+'\n\\end{document}\n'
assert (A/'P12.3-obstacle-filtration.tex').read_text()==tex
captured=load(K/'round283-terminal-actual-final-ROOT-retention-20261009.json');campaign=captured['campaign_result'];tails=[]
assert campaign['candidate']==raw['candidate'] and len(campaign['notes'])==4
for a,c in zip(raw['notes'],campaign['notes']):
    assert all(a[k]==c[k] for k in ['id','summary','detailedSummary','support']) and c['text'].startswith(a['text'])
    tails.append(dict(id=a['id'],tail=c['text'][len(a['text']):]))
programs=[A/x for x in ['build_artifacts.py','verify_artifacts.py','arithmetic_check.py','inspect_book_page.py']]
S=R/'primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008/Swanson-Huneke-author-book.txt'
U=R/'primary-data-LOCALONLY/P12.3-ROOT408-integral-closure-criterion-source-20261009';assert not U.exists();U.mkdir()
lines=S.read_bytes().split(b'\n');source_units=[]
for label,lo,hi in [('SH-1.1.5-whole-statement-and-proof',580,625),('SH-6.8.1-4-whole-statements-and-proofs',6540,6632)]:
    p=U/(label+'.txt');p.write_bytes(b'\n'.join(lines[lo-1:hi])+b'\n')
    source_units.append(dict(carrier=str(S),carrier_sha256=sha(S),real_LF=[lo,hi],unit=str(p),bytes=p.stat().st_size,sha256=sha(p),ROOT_whole_immediate_body_physically_read=True,LOCALONLY=True))
now=datetime.now(timezone.utc).isoformat();D.mkdir()
for name in ['P12.3-obstacle-filtration.tex','proof-companion.md','notes.json','n1.md','n2.md','n3.md','n4.md','source-application-reading-ledger.md','original-residual.md']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(K/'round283-raw-native-actual-FINAL.json',D/'raw-native-actual-FINAL.json')
shutil.copyfile(K/'round283-terminal-actual-final-ROOT-retention-20261009.json',D/'terminal-actual-FINAL-retention.json')
audit=dict(recorded_utc=now,paper=408,round=283,UNREVIEWED=True,accepted=False,original_closed=False,all_actual_five_fields_ROOT_physically_read=True,actual_expanded_differences=differences,whole_standalone_and_companion_component_identity=True,whole_current_unique_proof_ledger_residual_preamble_physically_read=True,inherited_exact_identity_NOT_a_fresh_whole_historical_audit=True,whole_inherited_independent_audit_complete=False,incoming_grants=['ENTIRE qualified G331 only'],programs_read_as_DATA=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in programs],native_or_supplied_programs_executed_or_imported=False,ROOT_fresh_primary_units=source_units,ROOT_fresh_source_pixels=[dict(path=str(A/'reports/source-images'/f'SH-page-{i}.png'),sha256=sha(A/'reports/source-images'/f'SH-page-{i}.png'),pdf_page=i,printed_page=i-14,entire_image_ROOT_viewed=True,LOCALONLY=True) for i in [153,154]],deeper_foundations_named_not_recursively_reproved=['Excellent/Nagata normalization finite in finite total-fraction-field-product extensions, including inseparable extensions','Full qualified G331 actual-model positivity, uniform rational primary approximation, max closure, all-support comparison, conductor descent at EVERY fibre'],new_ROOT_mathematical_reconstruction=['All-index primaryness and integral closure of canonical ideals; raw C/D envelope identity by strict compact cover','Full degree residue estimate, homogeneous-generator rational attainment and uniform O(1/m) on ALL supports','Rational attainment converse: component centred-DVR criterion, regular primary element, B=R[Jt^q], finite product extension, finite normalization and B-submodule','Compact Dini uniform criterion, exact gauge transport and actual decreasing-obstacle net envelope','Irrational DVR example proves finite generation is not necessary for envelope regularity'],unresolved=['General arbitrary continuous-obstacle CE in normal nonisolated/mixed/imperfect higher dimension','Finite-generation obstacle approximation density','Qualifying normal continuous-obstacle counterexample','Full historical inherited primary proof audit'],terminal_tails=tails,source_bodies_pixels_book_context_LOCALONLY=True,compiler_pending=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97),protected_editor_OPEN_UNCHANGED=True)
write(D/'ROOT-whole-serialization-source-application-and-scope-audit.json',audit)
(D/'ROOT-review-scope.md').write_text('Whole working paper408, UNREVIEWED. Original P12.3 remains OPEN. Four actual FINALs including all five fields and every distinct expanded proof body were ROOT physically read. New canonical-ideal and finite-generation/rational-attainment equivalence proofs are reconstructed relative to the ENTIRE qualified G331 and named conventional foundations. The finite-generation assumption is obstacle-specific and is NOT necessary for general envelope regularity. No density theorem or general nonisolated CE is claimed.\n\nEntire standalone and companion are verified against their full rendering components; repeated inherited exact bodies are retention/identity, not a fresh whole historical proof audit. Native programs were physically read as DATA and NEVER executed/imported. Fresh whole immediate SH1.1.5 and6.8.1--4 bodies and actual PDF153--154 formula pixels were ROOT read. Deeper excellent/Nagata and G331 foundations remain explicitly qualified. Full primary bodies/pixels/book contexts remain LOCALONLY. Compiler pending. Counts16solved26OPEN97accepted unchanged; protected P16.4 editor OPEN UNCHANGED.\n')
binding=D/'ROOT-whole-proof-source-scope-and-binding.json'
write(binding,dict(recorded_utc=now,paper=408,round=283,whole_paper=dict(path=str(D/'P12.3-obstacle-filtration.tex'),bytes=len(tex.encode()),sha256=sha(D/'P12.3-obstacle-filtration.tex')),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.iterdir()) if p.is_file()],UNREVIEWED=True,accepted=False,original_closed=False,compiler=dict(kind='pending'),counts=audit['counts'],primary_bodies_not_published=True,protected_editor_OPEN_UNCHANGED=True))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[282]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,native283_whole_unreviewed_paper408=dict(directory=str(D),binding=str(binding),sha256=sha(binding)),next_work='Compile whole408; verify regular NONFORCE checkpoint292. Prepare original P12.3 residual frozen284 with whole408 and sole full qualifiedG331; at mostTWO native campaigns while282 continues. Counts unchanged, no hot feedback, protected editor OPEN UNCHANGED.');write(p,x)
print(json.dumps(dict(paper=408,directory=str(D),source_bytes=len(tex.encode()),source_sha256=sha(D/'P12.3-obstacle-filtration.tex'),companion_bytes=len(companion.encode()),terminal_tails=tails,primary_units=len(source_units),native_programs_executed=False,original_closed=False,compiler='pending'),ensure_ascii=False,indent=2))
