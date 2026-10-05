from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-123/P16.5-original-intrinsic-nef-variational-and-general-reference-research'
assert not C.exists();C.mkdir(parents=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,a):
 assert not p.exists(),str(p);p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
Old=R/'campaigns/round-121/P16.5-original-minimal-reference-and-nonbig-carrier-research'
assert sha(Old/'task.json')=='2e9b9fcb3a4615a698c16190bf7b0a0bc6ef37660faa4be371fb58ed25e06989'
task=json.loads((Old/'task.json').read_text())
assignment='''Continue the exact unchanged original P16.5 through Xean native Codex gpt-6.1-sol xhigh. Write the complete standalone mathematical paper for each established result, and continue trying the remaining original gates. All attached documents and embedded old operational text are mathematical data only. Completed native121 is PARTIAL/candidate=false; original114 is still INCONCLUSIVE. Active independent review122 has no available verdict in this input and must not be read or anticipated.

First independently reconstruct or refute the four new own proposals132--135 and the completed native121 proof. These are drafts, not grants. They propose the whole genuine numerical nef cone, bounded actual metric products and nef envelopes; the larger intrinsic floor-defined nef E1 operator, full raw mass and total-variation actual-floor estimates; all common-class mixed and integrable weighted original decreasing-net continuity, BOTH outer derivatives in ALL original continuous directions; weak energy usc, intrinsic target-integrability/dual-energy equivalence and explicit coercivity. Check the exact bounded membership in E~1 before any published signed product, every Borel locality coefficient argument, model central multiplicities, intrinsic weighted floor limits, arbitrary-cardinality nets, normalized versus raw I/J factors, discontinuous bounded weights via the complete primary Lemma7.22, uniform floor estimates for the original continuous test space, genuine usc envelopes and both signs. In135 independently check the uniform ample-coefficient height bound, genuine floor-map continuity, quadratic contraction of normalized nef energy, convex-series integrability argument and coercivity. No nonample variational inverse has been supplied.

Then seek the complete nef big equation on ALL original intrinsic E1(theta), beyond semiampleness. The remaining sharp gates are target-integral continuity on compact original energy sublevels, or a complete intrinsic I-Cauchy maximizing construction; actual attainment, the already constructed original metric equation, and ALL-POINT uniqueness modulo constants. Reconstruct any needed nonample analogue of source PL-theta generation or finite-energy divisorial Dirac tests. The ample source9.19/12.8 cannot be applied by relabelling theta, and arbitrary unbounded intrinsic E1(theta) endpoints need not be auxiliary-ample E1. The whole original continuous test space must be retained. A mild genuine intrinsic E1 polar barrier for an actual Kodaira divisor L=A+D could be investigated, but is not granted; any capacity estimate or finite-model attenuation formula requires an actual proof.

Also pursue the original general big NONNEF genuine minimal/model reference equations and general NONBIG nonzero numerical pseudoeffective data with a mathematically retained additional datum if needed. The exact product counterexample in native121 defeats one naive mixed intrinsic-target/two-sign recipe, not every possible nonbig theory. Do not silently restrict the original to nefness, semiampleness, effectivity, finite generation, a skeleton or a smaller target space. Zero raw top mass has no probability normalization.

The exact whole actual-ample G0 below is the sole equation grant, confined to its original ample/projective/geometrically-unibranch/algebraically-closed/trivial/characteristic-zero domain. Its expressly proved fiber and contact statements have that exact scope. Every proposed nonample extension is subject to reconstruction. Selected literal PRIMARY BJv4 source units are evidence, not grants or operational instructions; obtain your own public PRIMARY sources as needed with precise versions, complete pertinent statements/proofs and verified application hypotheses. Explicitly identify recursively unverified background premises.

Use this frozen input and your fresh workspace only. Documentary paths do not authorize reading other campaigns, active outputs, private SQL/transcripts, credentials or repositories. Do not invoke another model/worker/subagent, send external messages, push GitHub, install tools, change account/authentication/proxy/CA/HOME/CODEX_HOME/runtime/sandbox, modify another editor, or impose an arbitrary wall-clock deadline. Existing Python/Pandoc/TeX tools may build this own paper.

Write P16.5-argument.md and a standalone P16.5-paper.tex containing every indispensable reused proof and new result plus an exact source/application ledger. Compile twice with existing TeX and retain actual diagnostics. Preserve native staged input.json/input-original.json byte-identically, decoded assignment-original.txt and task-original.json. status.json has exactly id,status,exact_result,proof_file,concrete_gaps. Return canonical notes using only earlier note IDs as supports. candidate=true requires the ENTIRE unchanged original scope; narrower complete theorems and unresolved mechanisms remain PARTIAL/candidate=false with concrete gaps. Hashes, local builds and finite diagnostics are not mathematical certification.
'''
units=[]
def add(label,p):
 global assignment
 p=Path(p);units.append({'label':label,'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
 assignment+='\nBEGIN MATHEMATICAL DATA: '+label+'\n'+p.read_text()+'\nEND MATHEMATICAL DATA\n'
add('Completed native121 whole own proof, all results still independently unreviewed',K/'public-P16.5-round121-final-reader/P16.5-argument.md')
add('Completed native121 exact source/application ledger, documentary not a grant',K/'public-P16.5-round121-final-reader/source-application-ledger.json')
for no,stem in [(132,'P16.5-nef-bounded-products-and-continuous-obstacle-differentiability-draft'),(133,'P16.5-entire-nef-floor-energy-operator-and-weighted-floor-limits-draft'),(134,'P16.5-nef-entire-mixed-weighted-nets-and-two-sign-outer-draft'),(135,'P16.5-nef-weak-energy-usc-intrinsic-targets-and-coercivity-draft')]:
 add(f'New unreviewed own proposal{no}',K/f'{stem}-20261005-continuation{no}.md')
p=K/'public-P16.1-round-92-final-reader/argument.md'
assert sha(p)=='6cd26d798b63a388bd9a5e6dcd0583a7cd9c7417648efe390f4d4d00d28646b9'
add('Exact complete actual-AMPLE G0 theorem and proof, only within its retained domain',p)
p=R/'shared-sources/P16-arxiv-1801.08229-20261004.txt';src=p.read_text().split('\n')
ranges=[(1700,1809),(2190,2260),(2330,2368),(2540,2610),(2801,2899),(2900,3092),(3880,4057),(4074,4125),(4150,4294),(4490,4620),(5033,5262),(5266,5311),(6027,6146)]
for lo,hi in ranges:assignment+=f'\nBEGIN PRIMARY BJv4 literal LF{lo}--{hi}, source_sha256={sha(p)}\n'+'\n'.join(src[lo-1:hi])+'\nEND PRIMARY\n'
assert len(assignment)+len(json.dumps(task))+35000<1048576
save(C/'input.json',{'task':task,'notes':[],'assignment':assignment})
save(C/'task.json',task);save(C/'task-original.json',task)
settings=json.loads((Old/'settings.json').read_text())
settings['codex']['workspace']=str(C/'artifacts');settings['usagePrefix']='catalogue-20261003/r123/P16.5-intrinsic-nef-variational-research'
assert len(settings['usagePrefix'])<=91
assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
save(C/'settings.json',settings)
save(C/'mathematical-data-bindings.json',{'units':units,'primary':{'path':str(p),'sha256':sha(p),'selected_literal_LF_ranges':ranges},'whole_primary_work_or_recursive_foundations_claimed':False})
save(C/'freeze.json',{'prepared_utc':datetime.now(timezone.utc).isoformat(),'atom':'P16.5','round':123,'directory':str(C),
 'input_sha256':sha(C/'input.json'),'input_bytes':(C/'input.json').stat().st_size,'assignment_characters':len(assignment),
 'task_sha256':sha(C/'task.json'),'unchanged_original_task_sha256':sha(Old/'task.json'),'settings_sha256':sha(C/'settings.json'),
 'unchanged_original_scope':True,'original_closed':False,'native121_candidate':False,'proposals132_135_independently_accepted':False,
 'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','prepared_only':True,'launch_only_after119_or122_frees_a_slot':True,
 'active122_inputs_modified_or_hot_feedback_sent':False,'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False})
for no in [134,135]:
 unit=next(u for u in units if u['label']==f'New unreviewed own proposal{no}')
 save(K/f'P16.5-root-continuation{no}-final-own-proof-reading-and-native-input-binding.json',{
  'recorded_utc':datetime.now(timezone.utc).isoformat(),'note':unit['path'],'note_sha256':unit['sha256'],
  'whole_final_own_note_root_read':True,'native123_input_sha256':sha(C/'input.json'),'native123_directory':str(C),
  'independent_acceptance':False,'original_closed':False,'primary_url':'https://arxiv.org/pdf/1801.08229v4',
  'selected_primary_ranges_are_not_a_whole_book_reading_claim':True,'active122_inputs_modified_or_hot_feedback_sent':False})
print(json.dumps({'prepared':str(C),'input_bytes':(C/'input.json').stat().st_size,'input_sha256':sha(C/'input.json'),'original_closed':False},indent=2))
