from pathlib import Path
import datetime,hashlib,json

root=Path('/workspace/research')
p=root/'campaigns/round-06/P06.2-curve-recognition-embedded-evidence-review'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((p/'run.json').read_text())['campaign'];r=c['result']
f=json.loads((p/'freeze.json').read_text());b=json.loads((p/'source-artifact-binding.json').read_text())
assert c['status']=='completed' and r['verdict']=='PASS'
assert (len(r['premises']),len(r['passages']))==(38,66)
assert sha(p/'argument.md')==f['argument_sha256']==b['review_argument_sha256']
assert sha(Path(b['main_argument']))==f['main_argument_sha256']==b['main_argument_sha256']
assert sha(Path(b['source_tex']))==f['source_tex_sha256']==b['source_tex_sha256']
assert sha(Path(b['declared_proof_file']))==f['declared_proof_sha256']==b['declared_proof_sha256']
assert sha(Path(f['extra_primary_evidence']['path']))==f['extra_primary_evidence']['sha256']
for x in r['passages']:
    assert type(x['premise']) is int and 0<=x['premise']<len(r['premises'])
    assert x['statement']==r['premises'][x['premise']]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
a={'recorded_utc':now,'run_sha256':sha(p/'run.json'),'verdict':'PASS',
   'full_report_premises_and_passages_read':True,'bindings_validated':True,
   'publish_exact_scope':True,'premises':38,'passages':66,
   'frozen_argument_sha256':f['argument_sha256'],'source_tex_sha256':b['source_tex_sha256'],
   'main_argument_sha256':b['main_argument_sha256'],'full_original_atom_solved':False,
   'assessment':'Root read the complete report, all 38 premises, and all 66 bound passages in untruncated reads; exact zero-based bindings and all main/review/declared/TeX/primary-body hashes match. Accept intrinsic ordinary zero-Hessian recognition only over algebraically closed complete nontrivially valued fields on good separated strict boundaryless pure analytic curves, including singular/nonreduced curves, with GR harmonic/classical pluriharmonic/G-local real PL/GJR harmonic conclusions. Separately accept actual local rigid constant branches or finite pure closed curve images with bounded normalization lifts over arbitrary complete nontrivially valued fields, and ground-field harmonic probes in pure zero-current ambients over algebraically closed K. The full unchanged n100 restriction/normalization/puncture proof was embedded and reconstructed; genuine primary Thuillier and Berkovich proof bodies repaired accessibility, not mathematical content. The previous INCONCLUSIVE is preserved. No arbitrary-field intrinsic recognition, general ambient scalar ascent, universal ambient classical conclusion, higher-dimensional two-sign regularization, formal verification or priority certification follows. Original P06.2 remains open.'}
(p/'review-read-attestation.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
source=Path(b['source_tex']).read_text();edits=[]
def add(before,after,reason,count=1):
    assert source.count(before)==count,repr(before)
    edits.append(dict(before=before,after=after,reason=reason,expected_occurrences=count))
add('Author self-audited partial research draft','P06.2 reviewed partial result','Publication status metadata',2)
add('This is a new, unverified partial submission for P06.2. Its proof bytes\nhave an author self-audit only. No old review verdict is transferred to\nthem, and no formal verification or priority claim is made. The original\natom remains open. The blocked preceding workspace has been preserved\nwithout edits.',
    'This paper gives independently reviewed partial results for P06.2. The\nexact proof, its complete supporting argument and authentic primary\nsource bodies received the source-aware PASS accompanying this paper.\nThe original problem remains open. No formal verification or priority\ncertification is claimed; earlier failed and inconclusive records are\npreserved.',
    'Record the new proof-specific full-evidence review without closing the original atom')
add('The local copy equals that hash. Its complete proof and exact-scope\nreview are preserved as \\texttt{sources/closed-curves-argument.md} and\n\\texttt{sources/closed-curves-review.json}. The precise results used',
    'The local copy equals that hash. Its complete proof and earlier exact-scope\nreview remain preserved as \\texttt{sources/closed-curves-argument.md} and\n\\texttt{sources/closed-curves-review.json}. The present review argument\nalso embeds and independently reconstructs the entire supporting proof;\nthe expanded argument and full review receipt accompany this paper.\nThe precise results used',
    'Provide the accessible complete dependency chain')
add('It is a strict affinoid domain\nalgebra, with an injective bounded map',
    'It is a strict affinoid algebra\nthat is an integral domain, with an injective bounded map',
    'Distinguish an integral domain algebra from an affinoid analytic domain')
add('Rerun from this directory:',
    'Rerun from the preserved worker workspace\n\\path{/workspace/research/campaigns/round-04/P06.2-curve-recognition-submission-repair/artifacts/codex-bcowsD}:',
    'Give the actual reproduction location')
add('resource-heavy computation is needed for these proofs.',
    'resource-heavy computation is needed for these proofs. The standalone\npublication source is also compiled twice with installed pdfLaTeX.\nThe native editor connection did not return, so built-in compilation\nremains unverified; the source and independently compiled PDF are\npreserved.',
    'Record actual publication compilation and editor availability')
(p/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'premises':38,'passages':66,'publication_edits':len(edits),'source_tex_unchanged':sha(Path(b['source_tex']))==b['source_tex_sha256']}))
