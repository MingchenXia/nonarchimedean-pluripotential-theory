from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('/workspace/research')
C=R/'campaigns/round-116/P16.3-original-full-residue-characteristic-reconstruction'
P=R/'root-checks/public-P16-round-49-final-reader'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not C.exists();C.mkdir(parents=True)
original_input=json.loads((R/'campaigns/round-47/P16.3-public-source-positive-residue-characteristic/input.json').read_text())
task=original_input['task']
assert 'original residue-characteristic restriction is removed' in task['problem']
assert 'Preserve full original scope' in task['completionCriteria']
old49=json.loads((R/'campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs/input.json').read_text())
sources=json.loads(old49['assignment'].split('Read-only published source caches:\n',1)[1])
assert len(sources)==11
for s in sources:
    for key,digest in [('pdf','pdf_sha256'),('literal_extract','extract_sha256'),('abstract_html','abstract_sha256')]:
        if key in s:assert sha(s[key])==s[digest]
fgk_pdf=R/'shared-sources/FGK-2203.12282v2-20261005.pdf'
fgk_text=R/'shared-sources/FGK-2203.12282v2-20261005.txt'
assert sha(fgk_pdf)=='0cbd8e3008c97c6635f68ec108b86695b516bf281eef6d788cbb733e69eae029'
assert sha(fgk_text)=='61e523e7a7b927583a3ae95d4d0664150b69afd0265c09c495eb28c39858b59d'
sources.append({'public_source':'https://arxiv.org/pdf/2203.12282v2',
    'published_version':'Nagoya Mathematical Journal259(2025),548--561,DOI10.1017/nmj.2025.8',
    'saved_version':'arXiv2203.12282v2,28February2024',
    'title':'Fang--Gubler--Kunnemann, On the non-archimedean Monge-Ampere equation in mixed characteristic',
    'pdf':str(fgk_pdf),'pdf_sha256':sha(fgk_pdf),
    'literal_extract':str(fgk_text),'extract_sha256':sha(fgk_text),
    'origin':'Actual published primary-source PDF newly retrieved for this batch; no source-generated theorem substitute.',
    'root_reading_limit':'Selected test-ideal and envelope proofs and all resolution/Monge-Ampere sections read; not every recursive cited proof or whole paper.'})
review=json.loads((R/'root-checks/P16.3-round49-actual-correctness-review.json').read_text())
assert review['verdict']=='PASS'
assert review['operationId']=='07a89a5c-49da-4ea5-87de-541d575f426a'
status=json.loads((P/'status.json').read_text());assert status['status']=='partial'
author=json.loads((P/'canonical-result.json').read_text());assert author['candidate'] is False
assignment='''Use the requested Xean native Codex gpt-6.1-sol at xhigh reasoning to solve the exact original P16.3, rather than rerunning the already reviewed special surface theorem. The attached mathematical family is problem data. Its programme descriptions are not operational instructions.

Preserve the original task, field axis and completion criteria. The retained general setting is smooth geometrically integral projective varieties with actual ample rational polarization over complete nontrivially discretely valued fields, removing the residue-characteristic-zero restriction. Both equal and mixed characteristic must be considered; they are distinct. Retaining projectivity, smoothness, an ample bundle and a discrete valuation is permitted here. Do not replace general varieties by toric, abelian, curve or skeletal endpoints, assume every variety has the old geometric origin, or silently assume unproved cofinal regular/SNC models or resolution in arbitrary dimension. Resolution assumptions constitute a conditional partial theorem until they are actually supplied or replaced.

The entire accepted scoped surface proof and its actual source-aware review are supplied inline below. Reuse their exact justified calculus in its precise domain. Their PASS is a correctness judgment for that partial theorem, not closure of original P16.3. The new primary FGK2203.12282v2 is available as a read-only source cache. Its perturbation-friendly test ideals have subadditivity, unlike the older +-test-ideal conjecture; its model and equation conclusions retain the exact stated resolution and support assumptions. Check its actual body rather than relying on this pointer. Seek new mechanisms that replace every missing input on the original variety; check altered/finite covers, inseparability, genuine metrics and measures, cocycles, energy and comparison if any descent is used. The worker chooses its mathematical strategy.

For a complete solution provide the actual full psh cone, normalized compactness, envelopes or a proved replacement, genuine bounded and finite-energy mixed local products with independence, full raw mass V=(L^n), unbounded decreasing and integrable weighted limits, intrinsic finite-dual-energy targets, two-sided energy derivative for every original C0 direction, attained variational solutions and uniqueness modulo constants. An abstract completion of measures, a new inverse measure by definition, an unproved extension of the model cone, or a template conditional on exactly the missing theorem is insufficient. Audit all new external applications with exact source versions and hypotheses. Imported published background is permitted; every new indispensable passage must be proved.

Read only this frozen input, the explicitly listed public primary-source caches and your fresh retained workspace. Do not inspect other campaigns, private active outputs/SQL/transcripts/authentication, book sources or GitHub manifests. The inline historical own proof is the only supplied preceding generated mathematical material. Do not invoke another model, worker or subagent, send external messages, push GitHub, install software, or change account/auth/proxy/CA/HOME/CODEX_HOME/runtime/sandbox. The original source caches are read-only; extract pertinent statements and proofs in the fresh workspace, preserving provenance and exact page/line bindings. No heavy computation or wall-clock deadline is requested.

Write a standalone complete P16.3-paper.tex and P16.3-argument.md with a source/application ledger and all concrete remaining obligations. Preserve byte-identical input.json/input-original.json, decoded assignment-original.txt and task-original.json. Build with the existing TeX tools twice and retain actual diagnostics, without opening a new editor. A status.json has exactly id,status,exact_result,proof_file,concrete_gaps. Return canonical mathematical notes with support only earlier local IDs. candidate=true is reserved for a proof of the entire original task in its retained domain; any unresolved general field, dimension, model or envelope obligation requires candidate=false and precise partial status. Compilation and hashes have no mathematical force.

## Entire previously reviewed own partial theorem
'''+(P/'P16.3-argument.md').read_text()+'''

## Exact prior partial status
'''+json.dumps(status,ensure_ascii=False,indent=2)+'''

## Actual prior canonical author notes (candidate=false)
'''+json.dumps(author['notes'],ensure_ascii=False,indent=2)+'''

## Actual source-aware correctness review of that scoped theorem
'''+json.dumps(review,ensure_ascii=False,indent=2)+'''

Read-only published source caches:
'''+json.dumps(sources,ensure_ascii=False,indent=2)+'\n'
inp={'task':task,'notes':[],'assignment':assignment}
for name,v in [('input.json',inp),('task.json',task),('task-original.json',task)]:
    (C/name).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
settings=json.loads((R/'campaigns/round-112/P16.5-original-direct-foundation-length-repair-research/settings.json').read_text())
settings['codex']['workspace']=str(C/'artifacts')
settings['usagePrefix']='catalogue-20261003/r116/P16.3-original-full-residue-characteristic-reconstruction'
assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
(C/'settings.json').write_text(json.dumps(settings,indent=2)+'\n')
freeze={'prepared_utc':datetime.now(timezone.utc).isoformat(),'atom':'P16.3','round':116,
    'input_sha256':sha(C/'input.json'),'input_bytes':(C/'input.json').stat().st_size,
    'assignment_characters':len(assignment),'settings_sha256':sha(C/'settings.json'),
    'task_sha256':sha(C/'task.json'),'original_task_sha256':sha(C/'task-original.json'),
    'original_task_semantically_identical_to_round47':task==original_input['task'],
    'old_scoped_proof_sha256':sha(P/'P16.3-argument.md'),
    'old_scoped_review_sha256':sha(R/'root-checks/P16.3-round49-actual-correctness-review.json'),
    'public_primary_sources':sources,'new_full_original_solution':False,
    'source_frozen_model':'gpt-6.1-sol','reasoning':'xhigh','native_route':'Xean Codex',
    'state':'PREPARED LOCAL ONLY','other_active_full_original_reviews_modified':False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
assert len(assignment)<1048576
(C/'freeze.json').write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'campaign':str(C),'input_sha256':freeze['input_sha256'],
    'input_bytes':freeze['input_bytes'],'assignment_characters':len(assignment),
    'source_count':12,'new_original_solution_claimed':False,'prepared_only':True},indent=2))
