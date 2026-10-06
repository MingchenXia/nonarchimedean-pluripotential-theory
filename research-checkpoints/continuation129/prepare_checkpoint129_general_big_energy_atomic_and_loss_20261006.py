from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,x):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation128.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='a4938bb324497fe931854a332799f625d7de7698'
assert sha(G/'upload-manifest-continuation128.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
notes=[K/'P16.5-general-big-entire-genuine-relative-energy-and-weak-compactness-draft-20261006-continuation145.md',
       K/'P16.5-general-big-finite-divisorial-equations-draft-20261006-continuation146.md',
       K/'P16.5-fixed-section-energy-loss-and-relative-regularization-gate-draft-20261006-continuation147.md']
assert sha(notes[0])=='303a41a8556fef890ac484e96c3e793734270a88f5c0576c8e2028508a50da23'
C126=R/'campaigns/round-126/P16.5-original-general-big-relative-operator-and-equation-research'
C127=R/'campaigns/round-127/P16.5-general-big-continuous-obstacle-operator-independent-review'
assert sha(C126/'input.json')=='1c64769676bd26ada2357d53b701bf14499388fcd13d311c55d773943787d76d'
freeze127=json.loads((C127/'freeze.json').read_text())
assert sha(C127/'argument.md')==freeze127['argument_sha256']
assert not (C126/'work.sqlite').exists() and not (C127/'review.sqlite').exists()
binding={'recorded_utc':now,'own_notes':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
         'independently_accepted':False,'original_closed':False,
         'scope':'Own145 entire genuine general-big relative energy and compact normalized cost sublevels; own146 finite rational divisorial target equations and entire-cone variational attainment, including zero weights on extra model vertices; own147 explicit moving-volume gap forces fixed-system FS energy minus infinity. Entire-E1 operator, comparison and all-target inverse uniqueness remain open.',
         'primary_local_BJ_sha256':sha(R/'shared-sources/P16-arxiv-1801.08229-20261004.txt'),
         'primary_complete_pertinent_local_literal_LF_root_read':[[922,931],[724,755],[6767,6857]],
         'BHJ_primary_url':'https://numdam.org/item/10.5802/aif.3096.pdf',
         'BHJ_complete_Theorem4_6_and_Lemma4_7_proofs_root_read_rendered_lines':[2473,2525],
         'all_recursive_Fujita_Hodge_Zariski_or_resolution_foundations_reproved':False,
         'active_native_inputs_or_frozen126_127_modified':False,'hot_feedback_sent':False,
         'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,
         'source_scope_audits':[
             {'url':'https://arxiv.org/pdf/2510.03044','read_scope':'Introduction and complete generic-domain setup; compact complex manifold with Kahler generic class retained. No general-big original generic bundle equation imported.','full_paper_or_all_proofs_read':False},
             {'url':'https://arxiv.org/pdf/2512.10466','read_scope':'Introduction and complete Theorems1.1/1.3 statements and bounded-norm domain; complex projective big bundles and minimal-singularity envelopes. No NA entire-E1 equation or original carrier identification imported.','full_paper_or_all_proofs_read':False}]}
B=K/'P16.5-root-continuation145-147-whole-proofs-and-exact-scope-binding-20261006.json'
save(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;a=json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
    assert [i['round'] for i in a['current_small_batch']['items']]==[124,125]
    a.update({'updated_utc':now,'continuation145_147_general_big_energy_atomic_and_loss_candidate':binding,'github_pending_checkpoint':'continuation129 frozen'})
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        cols=line.split('\t')
        cols[2]='Original123 PARTIAL; independent124/125 active. General-big obstacle operator143/144, entire genuine relative energy145, finite divisorial equations and variational attainment146, and fixed-system energy-loss obstruction147 are unreviewed. Original126/scoped127 prepared. Entire general-big E1 operator, comparison and all-target unique inverse remain open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation129-publication-records';D.mkdir(exist_ok=False)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_originals':35,
                              'historical_reviewed_scoped_papers':47,'new_unreviewed_support':[145,146,147],
                              'current_native_small_batch':[124,125],'prepared_only_native_work':[126,127],
                              'original_closed':False,'existing_editor_unchanged':True,
                              'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.pdf','.aux','.log'} and 'LOCALONLY' not in p.name
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation129/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in notes+[B,K/'P16.5-root-continuation145-whole-proof-and-exact-scope-binding-20261006.json',previous,Path(__file__)]:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation129.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
        'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
        'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
        'historical_reviewed_scoped_papers':47,
        'commit_message':'Record genuine general-big relative energy and finite divisorial variational equations',
        'scope':binding['scope']+' All new mathematics unreviewed. Seven originals solved,35open,47 independently accepted scoped papers. Frozen native126127 unchanged; native124125 active.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'originals_solved':7,'originals_open':35,'reviewed_scoped_papers':47},indent=2))
