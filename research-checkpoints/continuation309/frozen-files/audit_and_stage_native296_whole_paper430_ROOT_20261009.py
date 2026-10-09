"""Passive ROOT literal reconstruction; supplied/native programs stay inert DATA."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, ast

R=Path('/workspace/research')
K=R/'root-checks'
C=R/'campaigns/round-296/P12.3-whole425426-same-centre-and-normal-quotient-envelopes'
A=C/'artifacts/codex-UtG3R5'
D=K/'public-P12.3-continuation430-formal-group-quotients-and-wild-separable-conductors-unreviewed'
raw=K/'round296-raw-native-actual-FINAL.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(raw)=='87b30e0412eb2b8cdfb900a8dac39514413725598be35f54989eedcebf97e79a'
assert not D.exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['current_active_batch']==[297] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==308
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
actual,assembled=load(raw),load(A/'notes.json')
assert actual['candidate'] is False and assembled['candidate'] is False
assert len(actual['notes'])==len(assembled['notes'])==5
known,differences={'G331'},[]
for n,m in zip(actual['notes'],assembled['notes']):
    assert set(n)==set(m)=={'id','summary','detailedSummary','text','support'}
    assert n['id']==m['id'] and n['support']==m['support'] and set(n['support'])<=known
    known.add(n['id'])
    assert (A/'notes'/f"{m['id']}.txt").read_text().strip()==m['text']
    differences.append(dict(id=n['id'],different_fields=[k for k in n if n[k]!=m[k]]))
bindings=load(C/'mathematical-packet-bindings.json')
private=load(C/'private-primary-packet-bindings.json')
assert len(bindings)==44 and len(private)==1260
for e in bindings:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
data=lambda i:Path(bindings[i]['path']).read_bytes()
for i,name in [(29,'original-completion-criteria.txt'),(30,'original-residual.md'),(31,'original-task.json')]:
    assert (A/name).read_bytes()==data(i)
assert sha(A/'original-residual.md')=='a4009cba9440ceed821cd6736c6b6b18f172298a9300288a2c09f7fe4fa669a2'
# AST is parsed as DATA only. Extract one literal string; no eval/import/exec of code.
parsed=ast.parse((A/'build_delivery.py').read_text())
headers=[n.value.value for n in parsed.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='header' for t in n.targets) and isinstance(n.value,ast.Constant) and isinstance(n.value.value,str)]
assert len(headers)==1
source=headers[0].replace(',breaklines=false','')+'\n'.join((A/'notes'/f'n{i}.tex').read_text() for i in range(1,6))
source+='\n\\appendix\n'
escape={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}','|':r'\textbar{}'}
for name in ['source-application-reading-ledger.md','scoped-verdict.md']:
    rendered=''.join(escape.get(c,c) for c in (A/name).read_text())
    source+='\\section{Exact scope attachment: '+name+'}\n'+rendered+'\n'
source+='\\end{document}\n'
assert source==(A/'P12.3-quotients-and-wild-conductors.tex').read_text()
assert not any(ord(c)<32 and c not in '\n\t\r' for c in source)
assert sum((A/'notes'/f'n{i}.tex').stat().st_size for i in range(1,6))==43201
assert sum((A/'notes'/f'n{i}.tex').read_bytes().count(b'\n') for i in range(1,6))==787
parts=[b'# ENTIRE mathematical companion; unverified scoped progress, candidate=false.\n']
for name in ['notes.json','P12.3-quotients-and-wild-conductors.tex','source-application-reading-ledger.md','scoped-verdict.md']:
    parts += [('\n===== CURRENT WHOLE '+name+' =====\n').encode(),(A/name).read_bytes(),b'\n']
for e in bindings:
    parts += [('\n===== EXACT WHOLE INCOMING '+Path(e['path']).name+' =====\n').encode(),Path(e['path']).read_bytes(),b'\n']
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
    parts += [('\n===== BINDING METADATA ONLY '+name+' =====\n').encode(),(C/name).read_bytes(),b'\n']
assert b''.join(parts)==(A/'proof-companion.txt').read_bytes()
primary=private[1244:1260]
assert len(primary)==16
assert all(Path(e['path']).read_bytes() not in source.encode() and Path(e['path']).read_bytes() not in (A/'proof-companion.txt').read_bytes() for e in primary)
P=R/'primary-data-LOCALONLY/P12.3-ROOT413-algebraic-field-root-descent-source-20261009'
names=['BFJ-1.10-1.15-whole-immediate-chain.txt','BFJ-2.1-2.8-whole-immediate-chain.txt','BFJ-3.1-3.14-whole-immediate-chain.txt','BFJ-3.15-3.25-whole-model-envelope-and-immediate-proofs.txt','BFJ-setting-and-modification-domain.txt','BFJ-simple-modification-domain.txt']
assert {sha(P/n) for n in names}=={e['sha256'] for e in private[1246:1252]}
D.mkdir()
public=[]
def retain(p,name=None):
    q=D/(name or p.name)
    shutil.copyfile(p,q)
    assert sha(p)==sha(q)
    public.append(q)
retain(raw,'native296-actual-FINAL-all-five-fields.json')
retain(A/'notes.json','native296-assembled-notes-separate-from-actual.json')
retain(A/'P12.3-quotients-and-wild-conductors.tex','native-standalone-DATA.tex')
assert source.count(',qquad')==2
reader=source.replace(',qquad',',\\qquad')
root_source=D/'P12.3-quotients-and-wild-conductors.tex'
root_source.write_text(reader)
public.append(root_source)
for n in actual['notes']:
    p=D/('actual-'+n['id']+'-all-five-fields.json')
    write(p,n)
    public.append(p)
    retain(A/'notes'/f"{n['id']}.tex")
    retain(A/'notes'/f"{n['id']}.txt",'native-assembled-'+n['id']+'.txt')
for name in ['source-application-reading-ledger.md','scoped-verdict.md','original-residual.md','original-task.json','original-completion-criteria.txt','exact-check-input.json']:
    retain(A/name)
for name in ['prepare_inert.py','exact_checks.py','build_delivery.py','verify_delivery.py']:
    retain(A/name,'native-program-'+name+'.DATA.txt')
for name in ['actual-assembled-exact-differences.json','command-evidence.json','environment.json','exact-checks.json','input-byte-audit.json','own-hashes.json','verification.json']:
    retain(A/'reports'/name,'native-report-'+name)
retain(K/'round296-terminal-actual-final-ROOT-retention-20261009.json')
now=datetime.now(timezone.utc).isoformat()
scope=dict(recorded_utc=now,paper=430,atom='P12.3',UNREVIEWED=True,accepted=False,original_closed=False,candidate=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),
    actual_FINAL=dict(path=str(raw),sha256=sha(raw),all_five_actual_notes_ALLfivefields_physically_ROOT_read=True,reading_output='b10d92, whole28994-byte7249-token JSON untruncated'),actual_vs_assembled_note_field_comparison=differences,assembled_notes_retained_separately=True,
    all_five_distinct_formal_proofs787LF43201bytes_physically_ROOT_read=True,formal_reading_outputs=['98d050','b47942','c08c44','f87a0b'],
    complete_unique_current37LFheader_ledger_verdict_residual_task_completion_physically_ROOT_read=True,unique_scope_reading_outputs=['12f08f','6a520a','c3cd0d'],
    all_FOUR_current_native_programs_physically_ROOT_read_ONLY_as_DATA=True,program_reading_outputs=['020f08','dda556'],supplied_or_native_programs_executed_or_imported=False,
    source_ROOT_passive_literal_reconstruction=True,native_companion_ROOT_passive_literal_reconstruction=True,
    ROOTreader_math_separator_errata='Only TWO literal ,qquad misspellings changed to ,\\qquad in ROOTreader. Exact native standalone and all five native formal versions retained unchanged separately. No mathematical proof alteration.',
    sole_correctness_grant='ENTIRE qualifiedG331 ALLFIVEfields and everymandatorymodel/support/radial/source/historical-audit qualification. Entirebody physically ROOTread420; exact currentapplications rejudged. All current native/rootpapers remainDATA; independent428429 not correctness grants.',
    all_six_complete_immediate_BFJ_units_freshly_ROOT_physically_reread=[dict(path=str(P/n),bytes=(P/n).stat().st_size,sha256=sha(P/n),literal_body_LOCALONLY=True) for n in names],
    current_primary_reading_outputs=['f18572 (1.10-1.15 and2.1-2.8 ENTIRE)','8af234 (3.1-3.14 ENTIRE)','90c81b (3.15-3.25, setting, simple-modifications ENTIRE)'],
    exact_source_application='SmoothAFFINE CLOSEDalgclosedCHAR0 and its completion ONLY. Whole3.18 realt=m+C, thinness bounded onFIXEDcomplex, substantiveCLOSEDsimplex3.11 and ALLretraction infima extendevery support. Exact primarycontraction; formalprimary models algebraize by finiteTaylortruncation. Complete3.9/3.10 immediateproofs in3.15-3.25. Ambiguous3.13 exponent extraction notnewpremise; G331 corrected unit/bottom/exponents retained. Published principalization/multiplier-subadditivity/Izumi and conventional excellence/normalDVR/finitecompletion foundations remain disclosed, not fullrecursiveaudit.',
    entire_inherited_current906751byte426_source_and7085210byte_companion_NOT_current_end_to_end_physically_read=True,
    all44_whole_mathematical_bodies_retained_NOT_reading_credit=True,native_admitted_entire_current_audit_INCOMPLETE=True,full_recursive_source_book_and_pixel_audit_NOT_complete=True,
    complete_new_scoped_deductions=[
        'All-support orbitfibre theorem for excellentREDUCEDlocal finite invariant inclusions in ANYcharacteristic, no grouporder invertibility orfaithfulness. Coefficientnorms use finiteR-MODULEgens, quotient-supportGauss values, compactdifference-lattice density and finitepositiveorbitmeasures.',
        'EVERYcontinuoussigned obstacle on normal smoothAFFINEfixedpointquotient or invariant ring of ANYcontinuousfinite formalregular-germ action overalgclosedCHAR0 has continuousgreatestC/D. Formalinvariants finiteNoetheriancompleteexcellentnormal viaorbitcoefficientformalA0 and recursivefinitebasis, noactionalgebraization.',
        'Exact envelopepullback, canonicalcontractionJ_mcapR, everydegreeuniformconvergence and signedPRIMARYmodelrate d(K+M1)/m includingl<d, allsupportsactualprimarypositivity beforelimits. No arbitrarycontinuousrate/FG.',
        'Conditional samecentreconductorobstruction needs fullfibre, finiteconductorapproachingnet and ALLDOWNSTAIRSprimarycomparison. Obstacleconductorprofiles and actualprimaryT_n prove noC/Dgreatest, nonUSCraw andeverycanonicalgap; no sourceCEneeded.',
        'ANYfield, formal u=P(t), ordP=e>=2,Pprime!=0, R=A+yS, one regularnormalizationcentre, exactconductoryS; finitefreebasis, separablecharacteristicpolynomialunitidentity, completefiniteDVRconjugatearc andALLELEMENTGausspath, ALLdownstairsprimarymonomialcomparisonK1 proved.',
        'NEWwildcharp family P=t^p+t^(p+1), evenimperfectfields; conjugatecontacta=p/(p-1),L4 givesexactp(o)=h_m(o)=-4 EVERYm anduniformerror>=3-p/(p-1)>=1, stable2epsilon belowgap. Nonnormal only; no normalCEcounterexample.'],
    native_finite_checks_ONLY_observations=load(A/'reports/exact-checks.json'),
    residual=['General excellentNORMALdim>=3, arbitraryconductor intrinsicclassification and highercharp/mixedsourceCE OPEN.','WholeoriginalP12.3 and complete entire-current/deeperrecursiveaudit OPEN; products/energy/fulloperators/radial separate.'],
    compiler='NOT_YET_INVOKED_FOR430',native297_ACTIVE_math_NOT_read_or_supplied=True,hot_feedback=False,all16_complete_immediate_primary_carriers_excluded_from_public=True,primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
sp=D/'ROOT-whole-proof-source-application-scope-and-residual.json'
write(sp,scope)
public.append(sp)
rootparts=[b'WHOLE ROOT430 mathematical proof packet. UNREVIEWED, originalP12.3 OPEN. Literal primary bodies LOCALONLY. Retention not reading/correctness.\n']
for p in public:
    rootparts += [('\n===== WHOLE CURRENT '+p.name+' =====\n').encode(),p.read_bytes()]
records=[]
for i,e in sorted(enumerate(bindings),key=lambda pair:pair[1]['bytes'],reverse=True):
    b=data(i)
    present=any(b in part for part in rootparts)
    if not present:
        rootparts += [('\n===== WHOLE INCOMING '+str(i)+' '+Path(e['path']).name+' =====\n').encode(),b]
    records.append(dict(index=i,bytes=len(b),sha256=e['sha256'],whole_body_retained=True,contained_in_existing_whole_body=present,fresh_reading_credit=0))
comp=D/'proof-companion.txt'
comp.write_bytes(b'\n'.join(rootparts))
whole=comp.read_bytes()
assert all(data(i) in whole for i in range(44))
assert all(Path(e['path']).read_bytes() not in whole for e in primary)
public.append(comp)
cp=D/'ROOT-whole-companion-containment-ledger.json'
write(cp,dict(storage_only_NOT_reading_or_correctness_credit=True,records=records,all16_complete_immediate_primary_carriers_excluded=True,native_companion=dict(path=str(A/'proof-companion.txt'),bytes=(A/'proof-companion.txt').stat().st_size,sha256=sha(A/'proof-companion.txt'),exact_literal_reconstruction_checked=True,literal_primary_carriers_NOT_present=True)))
public.append(cp)
B=D/'ROOT-whole-proof-source-scope-and-binding.json'
write(B,dict(recorded_utc=now,paper=430,whole_source=dict(path=str(root_source),bytes=root_source.stat().st_size,sha256=sha(root_source)),exact_native_source=dict(path=str(D/'native-standalone-DATA.tex'),bytes=len(source.encode()),sha256=sha(D/'native-standalone-DATA.tex')),whole_companion=dict(path=str(comp),bytes=comp.stat().st_size,sha256=sha(comp)),public_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in public],UNREVIEWED=True,accepted=False,original_closed=False,compiler=scope['compiler'],counts=scope['counts'],protected_editor_OPEN_UNCHANGED=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    y.update(updated_utc=now,ROOT430_whole_unreviewed=dict(binding=str(B),sha256=sha(B)),next_work='Wholeactual296ALLfivefields,5distinctformalproofs,exactuniqueledgers/task/residual/4inertprograms and6completeBFJunits physicallyROOTread; ROOT430 passivelyliteralreconstructed plus2separatorerrata. Independent429alreadyretained. Compile430, freeze smallnextnativeP12.3 residual or neworiginal batch withwhole qualifiedpacket, NONFORCE309 next. Native297isolatedactive; maxTWO; counts/editor unchanged.')
    write(p,y)
print(json.dumps(dict(paper=430,source_bytes=root_source.stat().st_size,source_LF=reader.count('\n'),native_source_bytes=len(source.encode()),native_companion_bytes=(A/'proof-companion.txt').stat().st_size,ROOT_companion_bytes=comp.stat().st_size,public_files=len(public)+1,actual_vs_assembled=differences,every44_math_body_retained_whole=True,all16literal_primary_carriers_excluded=True,accepted=False,original_closed=False,binding=str(B)),indent=2))
