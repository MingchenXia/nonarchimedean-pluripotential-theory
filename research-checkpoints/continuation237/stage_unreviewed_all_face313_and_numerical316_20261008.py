from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
specs=[(231,'P05.1',313,'all-face-nontermination-and-simultaneous-linear-certificate-unreviewed','codex-kyWw2M','round231-unregistered-actual-native-final.json','round231-whole-draft-ROOT-reading-and-next-research-20261008.json'),(232,'P12.2',316,'numerical-Cartier-bounded-comparison-and-isolated-descent-unreviewed','codex-11ngIL','round232-actual-native-final.json','round232-whole-draft-ROOT-reading-binding-and-qualifications-20261008.json')]
out=[]
for n,atom,paper,title,workspace,final,binding in specs:
 C=next((R/f'campaigns/round-{n}').iterdir());A=C/'artifacts'/workspace;D=K/f'public-{atom}-continuation{paper}-{title}';assert not D.exists();D.mkdir();E=D/'evidence';E.mkdir()
 b=json.loads((K/binding).read_text());assert not b['original_closed'] and not b['new_accepted_paper']
 names=[atom+'-paper.tex','argument.md','source-application-ledger.md','scope-and-gaps.md','proof-coverage.md' if n==231 else 'whole-proof-coverage.md']
 if n==232:names += ['original-scope-decision.md','build-report.md','own-hashes.json']
 else:names += ['artifact-hashes.json']
 for name in names:shutil.copyfile(A/name,D/name)
 pdf=A/(atom+'-paper.pdf' if n==231 else 'build/'+atom+'-paper.pdf');shutil.copyfile(pdf,D/(atom+'-paper.pdf'))
 shutil.copyfile(K/final,E/'exact-actual-native-FINAL.json');shutil.copyfile(K/binding,E/'ROOT-reading-binding-and-qualifications.json')
 if n==231:shutil.copyfile(K/'round231-unregistered-final-and-reference-failure-binding-20261008.json',E/'ROOT-reference-registration-failure-binding.json')
 record=dict(staged_utc=datetime.now(timezone.utc).isoformat(),original_atom=atom,continuation=paper,native_round=n,native_workspace=str(A),source_sha256=sha(D/(atom+'-paper.tex')),PDF_sha256=sha(D/(atom+'-paper.pdf')),exact_actual_FINAL_sha256=sha(E/'exact-actual-native-FINAL.json'),source_copied_without_mutation=True,math_and_source_status='UNREVIEWED draft; ROOT whole-source reading and bindings do not confer independent acceptance',original_closed=False,new_accepted_paper=False,built_in_compiler_status='not yet requested at staging',own_programs_not_executed_or_imported=True,author_checker_build_claims_not_ROOT_execution=True,external_primary_images_and_full_source_bodies_not_copied=True)
 if n==232:record['mandatory_qualification']='In source Section8 only the infinite-conductor-value stratum is closed; its finite-value complement is open and need not be closed. Historical source retained. BFJ zero/unit exception must remain explicit.'
 else:record['mandatory_qualification']='Native generation completed but Xean registry rejected missing external support S306 because ROOT input.notes was empty. This is unregistered UNREVIEWED DATA, not an accepted or mathematical-failure result. New233 registers all FIVE full previously accepted qualified Notes.'
 (D/'ROOT-public-draft-status-20261008.json').write_text(json.dumps(record,indent=2)+'\n')
 (D/'README.md').write_text(atom+' research draft, continuation'+str(paper)+'\n\nOriginal remains OPEN; this paper is not counted as an accepted result. Complete authoritative source and author PDF are retained without mutation, with the exact actual FINAL and ROOT whole-reading/hash bindings. See ROOT-public-draft-status-20261008.json and its mandatory qualification. Native build/checker reports are author evidence only unless a separate ROOT reproduction record is present. No full external primary source text or page image is included. The protected P16.4 editor is unchanged.\n')
 out.append(dict(atom=atom,directory=str(D),source_sha256=record['source_sha256'],PDF_sha256=record['PDF_sha256']))
print(json.dumps(out,indent=2))
