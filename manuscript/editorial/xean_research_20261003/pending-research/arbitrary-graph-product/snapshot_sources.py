"""Copy read-only evidence into this fresh workspace; record origins and scope."""
from pathlib import Path
import hashlib, json, platform, shutil, subprocess, sys

HERE=Path(__file__).resolve().parent
OLD=Path('/workspace/research/campaigns/round-20/P05.2-fixed-real-reference-continuation/artifacts/codex-UZmUll')
BOOK=Path('/workspace/research/book-source/manuscript')
origins={
 'higher-relation-proposal.md':Path('/workspace/research/P05.2-higher-relation-graph-product-proposal.md'),
 'rank-one-argument.md':OLD/'P05.2-argument.md',
 'rank-one-generated.tex':OLD/'P05.2-partial.tex',
 'rank-one-accepted.tex':Path('/workspace/research/deliverables/round-20/P05.2-fixed-real-reference-graph-products.tex'),
 'rank-one-run.json':OLD.parent.parent/'run.json',
 'BMPS2603.08664v1.txt':OLD/'sources/BMPS2603.08664v1.txt',
 'BMPS2603.08664v1.pdf':OLD/'sources/BMPS2603.08664v1.pdf',
 'ch72_major_open_problems.tex':BOOK/'parts/part6/ch72_major_open_problems.tex',
 'appM_ch18_frontiers.tex':BOOK/'appendices/appM_ch18_frontiers.tex',
 'one-dimensional-STATEMENT.tex':BOOK/'editorial/solver_dossiers_20260925/p052_graph_accessible_mass_classification_v2_20260925/STATEMENT.tex',
 'one-dimensional-PROOF.tex':BOOK/'editorial/solver_dossiers_20260925/p052_graph_accessible_mass_classification_v2_20260925/PROOF.tex',
 'rank-one-local-recursion.py':OLD/'local-recursion.py',
 'rank-one-local-input.json':OLD/'local-input.json',
 'rank-one-real-sum-diagnostic.py':OLD/'real-sum-diagnostic.py',
}
dest=HERE/'sources';dest.mkdir(exist_ok=True)
records=[]
for name,origin in origins.items():
 data=origin.read_bytes();(dest/name).write_bytes(data)
 records.append({'file':'sources/'+name,'origin':str(origin),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(HERE/'source-hashes.json').write_text(json.dumps(records,indent=2)+'\n')
run=json.loads((dest/'rank-one-run.json').read_text())
(dest/'canonical-rank-one-notes.json').write_text(json.dumps(run['campaign']['result']['notes'],ensure_ascii=False,indent=2)+'\n')
task=json.loads((HERE/'input.json').read_text())
(HERE/'task.json').write_text(json.dumps(task['task'],ensure_ascii=False,indent=2)+'\n')
(HERE/'original-scope.txt').write_text(task['task']['problem']+'\n\n'+task['task']['completionCriteria']+'\n')
(HERE/'assignment.txt').write_text(task['assignment']+'\n')
env=['platform: '+platform.platform(),'python: '+sys.version]
for cmd in [['pandoc','--version'],['xelatex','--version']]:
 r=subprocess.run(cmd,capture_output=True,text=True);env.append('command: '+repr(cmd)+'\n'+r.stdout+r.stderr)
(HERE/'environment.txt').write_text('\n'.join(env)+'\n')
print(json.dumps({'snapshots':len(records),'origins_read_only':True,'canonical_notes':len(run['campaign']['result']['notes'])}))
