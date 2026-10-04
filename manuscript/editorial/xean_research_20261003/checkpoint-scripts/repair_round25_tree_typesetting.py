"""Repair only publication paragraph layout; preserve first render evidence."""
from pathlib import Path
import datetime, hashlib, json, shutil
r=Path('/workspace/research');out=r/'deliverables/round-25'
d=r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization-review'
tex=out/'P06.2-specified-semistable-tree-regularization.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
archive=out/'preparation-v2-evidence';archive.mkdir(exist_ok=False)
for p in [tex,tex.with_suffix('.pdf'),out/'export-evidence.json',out/'first-page.png',r/'deliverables/round-25-native-verification.json',r/'deliverables/round-25-source-preparation.json',d/'publication-edits.json']:
    shutil.copyfile(p,archive/p.name)
source=tex.read_text();edits=json.loads((d/'publication-edits.json').read_text())
for before,after,reason in [
 ('\\paragraph{Review and supporting evidence.}','\\section*{Review and supporting evidence}','Avoid overfull run-in paragraph heading with model identifier.'),
 ('\\begin{thebibliography}{99}','\\begin{thebibliography}{99}\n\\raggedright','Use ragged-right reference entries for long French titles and hashes.')]:
    assert source.count(before)==1
    source=source.replace(before,after)
    edits.append({'before':before,'after':after,'expected_occurrences':1,'reason':reason})
tex.write_text(source)
p=d/'publication-edits-v3.json';assert not p.exists();p.write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tex':str(tex),'sha256':sha(tex),
 'governing_review':str(d),'publication_edits_sha256':sha(p),'publication_edits':str(p),
 'native_compilation_pending':True,'full_original_atom_solved':False,
 'previous_render_preserved':str(archive),'reason':'One run-in-heading overflow and ragged bibliography repaired; no mathematical edits.'}
p=r/'deliverables/round-25-source-preparation-v3.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n')
original=(r/'export_round25_tree.py').read_text()
original=original.replace('round-25-native-verification.json','round-25-native-verification-v3.json').replace("out/'export-build'","out/'export-build-v3'").replace("out/'export-evidence.json'","out/'export-evidence-v3.json'")
p=r/'export_round25_tree_v3.py';assert not p.exists();p.write_text(original)
print(json.dumps(record,indent=2))
