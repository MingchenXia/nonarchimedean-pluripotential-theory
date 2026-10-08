"""Owned byte-only audit. Supplied programs are never imported or executed."""
from pathlib import Path
import hashlib, json, platform, shutil, sys

BASE = Path('/workspace/research/campaigns/round-253/P12.6-original-geometric-finite-projection-and-conductor-envelope-compatibility')
ROOT = Path(__file__).resolve().parent
def main():
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'attachments').mkdir(exist_ok=True)
    rows=[]
    for name in ('mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json'):
        data=json.loads((BASE/name).read_text())
        shutil.copyfile(BASE/name,ROOT/'attachments'/name)
        for entry in data:
            p=Path(entry['path']); b=p.read_bytes()
            digest=hashlib.sha256(b).hexdigest()
            rows.append({'path':str(p),'bytes':len(b),'sha256':digest,'matches':len(b)==entry['bytes'] and digest==entry['sha256']})
            if name=='mathematical-packet-bindings.json':
                shutil.copyfile(p,ROOT/'attachments'/p.name)
    env={'python':sys.version,'platform':platform.platform(),'cwd':str(ROOT),
         'compute':'Bounded standard-library arithmetic only; no supervised facility exposed or needed.',
         'compiler_run':False,'supplied_programs_executed_or_imported':False,
         'subagents_or_native_jobs':False,'model_override':'Requested designation cannot be independently attested or changed from this session.'}
    result={'inputs':rows,'all_match':all(x['matches'] for x in rows),'count':len(rows),'environment':env}
    (ROOT/'reports/input-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'count':len(rows),'all_match':result['all_match']}))
if __name__=='__main__': main()
