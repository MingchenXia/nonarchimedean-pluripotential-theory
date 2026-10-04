from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
original=R/'dossiers/family-10.txt'
assert sha(original)=='3da065a00ba15e63143f03929cc442380a1b43a67cf0b85776cb01e6a1107ee9'
previous=R/'campaigns/round-47/P16.3-public-source-positive-residue-characteristic'
prior=json.loads((previous/'input.json').read_text())
sources=json.loads(prior['assignment'].split('Read-only published source caches:\n',1)[1])
assert len(sources)==10
public_manifest=R/'shared-sources/P16-completion-envelopes-public-cache-20261004.json'
assert sha(public_manifest)=='7f3b3baf4ff4319ac5f6b2ae6bd736a5124d2d6cab4ac4308dabd6c17720d806'
additional=next(s for s in json.loads(public_manifest.read_text())['sources'] if s['arxiv_id']=='1712.00980')
assert additional['saved_version']=='1712.00980v3'
sources.append(additional)
for source in sources:
    for key,digest_key in [('pdf','pdf_sha256'),('literal_extract','extract_sha256'),('abstract_html','abstract_sha256')]:
        if source.get(key):assert sha(source[key])==source[digest_key]
directory=R/'campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs'
directory.mkdir(parents=True,exist_ok=False)
common=prior['assignment'].split('Use Xean native Codex',1)[1].split('Read-only published source caches:\n',1)[0]
common='Use Xean native Codex'+common
common=common.replace('ten public primary-source pointers','eleven public primary-source pointers')
assignment='''Investigate the original P16.3 positive-residue-characteristic equation axis using the original problem and public primary sources only. A newly supplied exact primary source is Gubler--Jell--Kunnemann--Martin arXiv:1712.00980v3 (Appendix authors Burgos Gil and Sombra), on continuity of envelopes and test ideals. Determine its actual field, geometric-origin, resolution, dimension and measure hypotheses from the PDF. Seek a genuine finite-energy operator and an arbitrary-support existence/uniqueness theorem in nontrivially valued positive residue characteristic, replacing every characteristic-zero geometric input used. Make a precise distinction among equal characteristic, mixed characteristic, conditional resolution assumptions and cases where these assumptions are proved. Do not present a solely trivial-valuation theorem as the nontrivial-valued target. Do not infer finite-energy surjectivity from completion of measures. Prefer a concrete proved theorem over an abstract conditional template, and distinguish it from what is already in the source. Any remaining original obligations must be explicitly preserved. No earlier generated proof or review verdict is supplied.

'''+common+'Read-only published source caches:\n'+json.dumps(sources,ensure_ascii=False,indent=2)+'\n'
task=dict(prior['task'])
task['completionCriteria']='Solve original P16.3 under explicitly retained geometric and field hypotheses with the genuine E1 operator, mass, target finite energy, compactness, envelopes or proved substitutes, differentiation, comparison, and existence/uniqueness. Reconstruct every new source application. Judge complete coverage from the unchanged original family, not from an earlier author label. A narrower result or an indispensable unproved resolution/realization premise remains partial with candidate=false.'
inp={'task':task,'notes':[],'assignment':assignment}
(directory/'input.json').write_text(json.dumps(inp,ensure_ascii=False,indent=2)+'\n')
settings=json.loads((previous/'settings.json').read_text())
settings['codex']['workspace']=str(directory/'artifacts')
settings['usagePrefix']='catalogue-20261003/r49/P16.3-positive-residue-public-geometric-inputs'
assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
(directory/'settings.json').write_text(json.dumps(settings,indent=2)+'\n')
record={'prepared_utc':datetime.now(timezone.utc).isoformat(),'round':49,'atom':'P16.3','directory':str(directory),
    'input_sha256':sha(directory/'input.json'),'settings_sha256':sha(directory/'settings.json'),
    'original_dossier_sha256':sha(original),'public_source_count':11,
    'additional_primary_version':'1712.00980v3','generated_preceding_mathematical_payload_included':False,
    'state':'PREPARED LOCAL ONLY; not launched. Await a free slot in the current two-item native batch.',
    'fully_solved_original_atom':False}
(directory/'input-manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
