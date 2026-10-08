"""Artifact consistency checks only, never mathematical acceptance."""
from pathlib import Path
import hashlib, json, re
ROOT=Path(__file__).resolve().parent
def main():
    required=['P12.6-paper.tex','argument.md','source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md','acceptance-decision.json','native-notes.json','bounded-evidence-input.json','audit_inputs.py','bounded_checks.py','build_delivery.py']
    checks={name:(ROOT/name).is_file() for name in required}
    notes=json.loads((ROOT/'native-notes.json').read_text()); seen={'G331','G345'}
    for note in notes['notes']:
        checks[note['id']+'_supports']=set(note['support'])<=seen
        seen.add(note['id'])
    proof=(ROOT/'proof.tex').read_text(); paper=(ROOT/'P12.6-paper.tex').read_text()
    checks['entire_new_proof_in_paper']=proof in paper
    checks['candidate_false']=notes['candidate'] is False
    checks['tex_control_characters_absent']=all(ord(c)>=32 or c in '\n\t\r' for c in paper)
    for env in ('theorem','proposition','proof'):
        checks[env+'_balanced']=proof.count('\\begin{'+env+'}')==proof.count('\\end{'+env+'}')
    checks['grants_all_fourteen_literal_bodies']=all(p.read_text() in paper for p in (ROOT/'attachments').glob('*') if re.match(r'^(?:0[0-9]|1[0-3])-',p.name))
    hashes=[]
    for p in sorted(ROOT.iterdir()):
        if p.is_file():
            b=p.read_bytes(); hashes.append({'file':p.name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    result={'checks':checks,'all_artifact_checks_pass':all(checks.values()),'files':hashes,'meaning':'Artifact consistency only; not mathematical verification or TeX compilation.'}
    (ROOT/'reports/final-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_artifact_checks_pass':result['all_artifact_checks_pass'],'checks':len(checks),'meaning':result['meaning']}))
if __name__=='__main__': main()
