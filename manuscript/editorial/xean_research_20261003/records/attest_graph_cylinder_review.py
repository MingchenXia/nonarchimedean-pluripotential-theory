from pathlib import Path
import datetime,hashlib,json

r=Path('/workspace/research');p=r/'campaigns/round-06/P05.2-graph-cylinder-embedded-review'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((p/'run.json').read_text())['campaign'];result=c['result']
f=json.loads((p/'freeze.json').read_text());b=json.loads((p/'source-artifact-binding.json').read_text())
assert c['status']=='completed' and result['verdict']=='PASS'
assert (len(result['premises']),len(result['passages']))==(3,7)
for key in ['main_argument','source_tex','declared_proof_file']:
 hashkey={'main_argument':'main_argument_sha256','source_tex':'source_tex_sha256','declared_proof_file':'declared_proof_sha256'}[key]
 assert sha(Path(b[key]))==f[hashkey]==b[hashkey]
assert sha(p/'argument.md')==f['argument_sha256']==b['review_argument_sha256']
for q in result['passages']:
 assert type(q['premise']) is int and 0<=q['premise']<len(result['premises'])
 assert q['statement']==result['premises'][q['premise']]
a={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'run_sha256':sha(p/'run.json'),'verdict':'PASS',
   'full_report_premises_and_passages_read':True,'bindings_validated':True,
   'publish_exact_scope':True,'premises':3,'passages':7,
   'frozen_argument_sha256':f['argument_sha256'],'source_tex_sha256':b['source_tex_sha256'],
   'main_argument_sha256':b['main_argument_sha256'],'full_original_atom_solved':False,
   'assessment':'Root read the full native proof notes, author audit and research notes, then the complete report and all three premises / seven passages. Exact bindings and main/review/declared/TeX hashes match. Accept only the specified unit-weight two-vertex balanced graph in Z^2 times complete R^m, every m>=0, all positive-growth real-PA PC references and bounded real-PA obstacles on finite rational spatial structures: actual PAPC envelope, bounded reference growth and full recursive contact support. The saturated unimodular lifted local maps preserve all actual PCCs and primitive-normal recursive cycles, and the global proof controls remote competitors and every noncontact atom. The second-vertex leaf support is clarified with its actual intercept below k(a), not erroneously anchored at k(a). The unused n100 proof and its source-presentation limitations are preserved in the unchanged expanded argument and full review. No arbitrary finite graph/cycle/weighted nonsaturated junction classification, literal integral-slope theorem, analytic realization, formal verification or priority certification follows. Original P05.2 remains open.'}
(p/'review-read-attestation.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
s=Path(b['source_tex']).read_text();edits=[]
def add(before,after,reason,count=1):
 assert s.count(before)==count,repr(before)
 edits.append(dict(before=before,after=after,reason=reason,expected_occurrences=count))
add('Unverified P05.2 research draft','P05.2 reviewed partial result','Publication metadata',2)
add('The original classification P05.2 remains open. The following is a new,\nnonconical special-case theorem claimed in this unverified draft. It\nincludes every reference and obstacle specified in the assignment,\nwithout a separability assumption. No independent verification, formal\nverification, or priority claim is made.',
    'The original classification P05.2 remains open. The following\nnonconical special-case theorem has received the source-aware independent\nPASS accompanying this paper. It includes every reference and obstacle\nstated below. No formal verification or priority certification is claimed.',
    'Record the proof-specific independent review and exact partial status')
add('support/decomposition arguments are not imported. No review result for\nold or changed bytes is used.',
    'support/decomposition arguments are not imported. The present proof has\nits own independent review; no older receipt is substituted for it.',
    'Replace launch chronology with actual proof review provenance')
add('leaf. For a second leaf use \\(p(a)=p_1\\), anchor at \\(a\\), and\ninterchange the vertex roles; the endpoint support with slope \\(p_1\\)\nbounds the edge, and (S) bounds the first leaves.',
    'leaf. For a second leaf point \\(a+td\\), choose\n\\(\\beta\\in\\partial k_d(t)\\), set \\(p(a)=p_1\\),\n\\(p(d)=\\beta\\), \\(p(e)=p_1-\\beta\\), and give the affine\nsupport its value \\(k_d(t)-\\beta t\\leq k(a)\\) at \\(a\\).\nInterchanging the vertex roles completes the construction: the endpoint\nsupport with slope \\(p_1\\) bounds the edge, and (S) bounds the first leaves.',
    'Clarify the reviewed second-vertex support intercept without changing the construction')
add('with \\texttt{bash\\ rerun.sh} from this workspace. It runs exact small',
    'with \\texttt{bash\\ rerun.sh} from the preserved worker workspace\n\\path{/workspace/research/campaigns/round-06/P05.2-graph-cylinder-continuation/artifacts/codex-7OSCU6}.\nIt runs exact small',
    'Give the actual reproduction location')
anchor='\\subsection{Reproduction, evidence, and\nbibliography}\\label{reproduction-evidence-and-bibliography}'
add(anchor,anchor+'\n\nThe unchanged expanded review argument, standalone publication source,\nindependently compiled PDF and complete source-aware review receipt\naccompany this paper. The full appended n100 proof is unused by the\ngraph-cylinder theorem; its older rational-reference restriction is\nretained. The native editor connection did not return; built-in\ncompilation remains unverified. Two installed pdfLaTeX passes check\nthe publication source.',
    'State accessible review/dependency provenance and compilation status')
(p/'publication-edits.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'premises':3,'passages':7,'edits':len(edits)}))
