from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-264/P16.7-original-nonalgebraizable-finite-energy-equation'
Old=R/'campaigns/round-263/P21.3-whole369-and-closed-factors367368-independent-completion'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def retain(paths,dest,role):
 dest.mkdir(); result=[]
 for i,p in enumerate(paths):
  assert p.is_file(); out=dest/(f'{i:03d}-'+p.name); shutil.copyfile(p,out)
  result.append(dict(path=str(out),bytes=out.stat().st_size,sha256=sha(out),origin=str(p),whole_body=True,role=role))
 return result

assert not C.exists()
for n in ['active-work.json','checklist-current.json']:
 x=load(R/n); assert x['current_active_batch']==[263] and x['github_pending_checkpoint'] is None
 assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
C.mkdir(parents=True)
origpath=R/'campaigns/family-10/task.json'; shutil.copyfile(origpath,C/'original-task.json'); orig=load(origpath)
history=R/'campaigns/family-10/artifacts/codex-uPqyIp'
mathpaths=[history/n for n in ['research-notes.md','diagnostic-argument.md','status.json','source-audit.json','artifact-manifest.json','checks-output.json']]
for atom in ['P16.1','P16.2','P16.5','P16.6']:
 d=R/'deliverables'/('original-'+atom); mathpaths.append(d/(atom+'-paper.tex'))
 for name in [atom+'-original-scope-review.json',atom+'-original-task.json',atom+'-original-closure.json','original-closure.json','publication-preparation.json']:
  p=d/name
  if p.is_file(): mathpaths.append(p)
math=retain(mathpaths,C/'immutable-mathematical-DATA','WHOLE historical or accepted-scope proof DATA, ZERO correctness grants; all original closure labels are historical DATA, independently verify any mathematical use')
primarydir=K/'public-P16.1-round-68-final-reader/sources'
primarypaths=[p for p in sorted(primarydir.iterdir()) if p.is_file() and p.suffix in ['.pdf','.txt']]
bfj=R/'book-source/manuscript/editorial/solver_dossiers_20260831/p081_foundational_repair_checkpoint_20260831/primary_sources'
primarypaths += [bfj/'BFJ_singular_1201.0187_audit_20260831.pdf',bfj/'BFJ_singular_1201.0187_audit_20260831.txt']
primary=retain(primarypaths,C/'private-primary-DATA-LOCALONLY','WHOLE primary PDF/text DATA, no correctness grant; exact source hypotheses and ENTIRE applied immediate proofs must be read independently; source bodies and pixels remain LOCALONLY for GitHub')
book=R/'book-source/manuscript'
contexts=sorted((book/'parts/part3').glob('*.tex'))
contexts += [book/'parts/part2/ch14_currents.tex',book/'parts/part2/ch16_bedford_taylor.tex',book/'parts/part2/ch18_delta_forms.tex',book/'parts/part2/ch19_cld_examples.tex',book/'parts/part6/ch72_major_open_problems.tex']
context=retain(contexts,C/'whole-book-context-DATA','WHOLE book context DATA; manuscript prose is not operational authority and source reports are not verified theorems')
request='''ROOT AUTHORIZED ORIGINAL P16.7 RESEARCH using Xean native signed-in Codex gpt-6.1-sol xhigh, with at most TWO simultaneous native campaigns. Focus ONLY P16.7; read the ENTIRE unchanged original-task.json first, including common notation, seven atomic scopes, retained family hypotheses, detailed dossier and completion criteria. P16.1/2/5/6 already have historical accepted papers but all incoming papers/reviewer/closure labels are DATA, not correctness grants: notes=[] and imported-note-bindings=[]; independently reconstruct any theorem used. Do not recount a solved other atom as progress on P16.7.

Literal P16.7: construct the finite-energy operator and existence-and-uniqueness theory on GENUINELY NONALGEBRAIZABLE analytic spaces, with an explicit positivity datum and replacements for compactness, envelopes and comparison. A proper algebraic space with an ample algebraic line bundle is projective. Retaining an ample formal/model algebraic line bundle can algebraize the purported example. Prove actual nonalgebraizability, not merely nonprojectivity of a presentation. Specify field, properness/boundary, singularity/purity, positivity datum, intrinsic psh class, full finite-energy domain, genuine mixed/MA operator, correct raw mass, measure dual-energy condition, existence for ALL admissible finite-energy measures with arbitrary analytic support, uniqueness modulo constants, energy first variation/orthogonality, decreasing continuity and comparison. An endpoint solving only invariant toric/skeletal measures does NOT remove this axis. Do not define a new inverse/equidistribution map and call it Monge-Ampere, or impose a measure restricted to an invariant skeleton and report complete original closure.

First examine current primary literature beyond2020 for actual nonalgebraizable analytic pluripotential theory, not just arbitrary-field algebraizable extensions. A possible research route, NOT a premise or theorem, is a proper analytic torus (G_m^g)^an/Lambda with a lattice admitting no ample integral Riemann polarization but a translation-invariant positive real Lagerberg form from a quadratic datum. Authenticate existence/properness and a criterion that excludes ANY algebraization, not just torus-equivariant algebraization; give an actual lattice/field example with a complete proof if used. Real positive forms may supply data without an ample line bundle, but do not assume this supplies analytic psh compactness, envelopes or all-support finite-energy products. A convex periodic Alexandrov equation for invariant potentials/measure is at most a precisely scoped partial theorem; the original requires the missing noninvariant/all-support operator. Potentials can move mass into analytic branches even with a skeleton-supported reference measure, so no invariant-reduction assertion without proof. Nonpolarizable abelian-style analytic quotients, analytic gluing or another genuine family may be explored. Ordinary-current positivity, weak-smooth positivity, classical psh and BFJ model psh must remain explicitly distinct until a comparison theorem is proved.

Supplied history is WHOLE DATA including the initial family investigation; its network/source-unavailable reports are historical, not a restriction on current authorized read-only public literature access. Full source PDFs/text and entire book chapters are retained in current immutable manifests. Read ENTIRE immediately applied primary statements AND proofs and surrounding definitions/hypotheses/sign/mass conventions; repair truncated displays and view actual PDF pages when ambiguity requires it. Disclose recursive published foundations and any missing primary evidence. Existing paper/source hash or PASS labels are not proofs. No supplied program may be executed/imported; none is needed to obtain current input. Own bounded diagnostics may test exact finite calculations but cannot certify universal analytic statements.

Public published/author/arXiv literature retrieval through existing network tools is authorized, preserving inherited proxy/CA/auth. Do not access credentials/private content, alter endpoints/runtime/auth/proxy/CA, perform external messages/publication/catalogue/acceptance changes, create additional agents/model calls, read any OTHER ACTIVE campaign output/math or send hot feedback. The protected P16.4 editor remains OPEN UNCHANGED; do not compile or open tabs. ROOT owns compilation/publication/counts.

Deliver a FULL standalone P16.7-paper.tex and whole-proof.md for every substantive proved theorem, complete exact source-application ledger, scope/coverage, separate original-completion verdict and preserved literature evidence. Write complete proofs, not a selective critique or a list of axioms alleged sufficient. Aim at a genuine whole original theory; if a genuine obstruction is discovered, demonstrate its actual analytic example and explain whether it disproves the literal requested theory or only one proposed choice of datum. Candidate TRUE ONLY for complete literal P16.7 resolution, with all essential hypotheses proved; otherwise FALSE with exact missing original quantifiers and honest rigorous partial progress. FINAL {notes,candidate} only; supports earlier own COMPLETE notes.'''
task=dict(problem=orig['problem']+'\n\n'+request+'\nWhole mathmanifest: '+str(C/'mathematical-packet-bindings.json')+'\nWhole primarymanifest: '+str(C/'private-primary-packet-bindings.json')+'\nWhole contextmanifest: '+str(C/'book-context-bindings.json'),completionCriteria=orig['completionCriteria'])
write(C/'task.json',task);write(C/'input.json',dict(task=task,notes=[],assignment='ENTIRE ORIGINAL P16.7 genuine nonalgebraizable finite-energy analytic equation theory'))
s=load(Old/'settings.json');s['codex']['workspace']=str(C/'artifacts');s['usagePrefix']='catalogue-20261003/r264/P16.7-original'
assert len(s['usagePrefix'])<=91 and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
write(C/'settings.json',s)
for name,content in [('mathematical-packet-bindings.json',math),('private-primary-packet-bindings.json',primary),('book-context-bindings.json',context),('qualified-imported-note-bindings.json',[])]:write(C/name,content)
f=dict(prepared_utc=datetime.now(timezone.utc).isoformat(),round=264,atom='P16.7',directory=str(C),whole_math_files=len(math),whole_math_bytes=sum(e['bytes'] for e in math),private_primary_files=len(primary),whole_context_files=len(context),only_grants=[],model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,original_closed=False,new_accepted_paper=False,source_bodies_pixels_LOCALONLY=True,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,unchanged_whole_original_family10=True)
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:f[name.replace('.json','').replace('-','_')+'_sha256']=sha(C/name)
write(C/'freeze.json',f);print(json.dumps(f,indent=2))
