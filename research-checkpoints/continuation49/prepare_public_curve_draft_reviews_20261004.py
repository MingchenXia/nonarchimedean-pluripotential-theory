from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

R=Path('/workspace/research')
for n,atom,stem in [(39,'P03.2','P03.2-public-source-CLD-envelope-stages'),
                    (40,'P03.3','P03.3-public-source-general-curve-continuity')]:
    author=R/'campaigns'/f'round-{n}'/stem
    reader=R/'root-checks'/f'public-curves-CLD-round-{n}-final-reader'
    read=json.loads((reader/'complete-root-read.json').read_text())
    assert read['full_argument_read'] and read['all_actual_canonical_notes_read']
    result=json.loads((author/'run.json').read_text())['campaign']['result']
    notes=json.loads((reader/'actual-canonical-notes.json').read_text())
    assert result['notes']==notes and result['candidate'] is False
    proof=reader/f'{atom}-argument.md'
    assert proof.read_bytes()==(Path(result['workspace'])/proof.name).read_bytes()
    status=json.loads((reader/'status.json').read_text())
    prov=json.loads((reader/'source-extracts/source-provenance.json').read_text())
    criteria = (
        'Review the entire exact draft, including its subsidiary Theorem C and all canonical notes. The accompanying root check gives a specific strict/non-strict G-site gap: independently assess that accessible counterexample. Do not PASS the whole claimed paper while that indispensable premise remains false or unproved. Separately identify whether Theorems A/B and the full node calculation survive. Check every usc obstacle, the entire union, baseline-anchored directed finite maxima, Thuillier local boundedness, countable local topology and actual sequence extraction on a fixed ordinary neighborhood, GJR ordinary/weak sheaf equality, smooth positive current-to-form comparison, homeomorphic normalization and local constancy at all finite-residue rigid points, ordinary smooth descent, exact projective-space class and raw/regularized-envelope descent, fiber infimum rather than minimum for usc obstacles, all scalar and curve quantifiers and the no-relative-boundary scope. Reconstruct the exact branch obstacle and global LFS minorants. No collapse of ordinal stages or broad classification may be silently asserted.' if n==39 else
        'Reconstruct the complete sufficient theorems and counterexample. Verify actual global real-PL realization via local legal vertical Cartier star metrics, etale/nonrational node descent, positive-genus residue Picard classes, cycles with real slopes, proper/nonproper reduction-component degree rules and omitted/type-4 points. Check the greatest finite graph obstacle and the compact maximum-locus argument bounding EVERY analytic competitor; all scalar extensions, actual relative boundary and affinoid connected components. Check finite-separable ambient curve embedding, arbitrary continuous-obstacle density, legal breakpoint approximation in dense and discrete value groups, strict semistable base change, finite Galois averaging with divisible coefficients and actual semipositive descent. Verify arbitrary analytic extensions using a common complete extension and scalar surjectivity, not general scalar openness. Check actual completed-residue fibers, proper torsion comparison in degree zero, connectedness, maximum principle, exact whole-family descent without a rational point, proper and smooth maps, continuous fiber minimum and scalar minimum identity. Check the ground-field normalization sector without adding scalar family equality, and the full node computation and projective propagation. The higher-dimensional sharp classification is not claimed.'
    )
    task={'problem':'Independently verify this exact completed '+atom+' draft, every actual canonical note and the supplied literal published sources. This local preparation is not a provider submission. The original sharp classification remains open.',
          'completionCriteria':criteria+' Use exact published versions and hypotheses; fully reconstruct every indispensable new application. PASS only for an entirely correct and complete claimed scope; FAIL for a substantive defect; INCONCLUSIVE for an unresolved indispensable premise. Do not use hashes, compilation or earlier reviews as proof certificates. Use Xean native Codex gpt-6.1-sol/xhigh. No other model, worker or subagent, installation, runtime/account/auth changes, external messages, private transcripts/SQL, other draft workspaces or blocked review payloads. Original closure is separate.'}
    pieces=['# Exact final status\n\n',json.dumps(status,ensure_ascii=False,indent=2),
            '\n\n# Entire final proof\n\n',proof.read_text(),
            '\n\n# Every actual native canonical note\n\n',json.dumps(notes,ensure_ascii=False,indent=2)]
    if n==39:
        pieces+=['\n\n# Root mathematical gap check on this exact final proof\n\n',
                 (R/'root-checks/P03.2-round39-final-strict-PL-gap-20261004.md').read_text()]
    metadata=json.loads(json.dumps(prov))
    for s in metadata['sources']:
        for p in s.get('selected_pages',[]): p.pop('literal_pdf_text',None)
    pieces+=['\n\n# Published source versions, provenance and application checks\n\n',json.dumps(metadata,ensure_ascii=False,indent=2)]
    units=[]
    for s in prov['sources']:
        if n==39:
            pages=Path(s['literal_extract']).read_text().split('\f')
            for u in s['literal_pages']:
                p=reader/u['file']; text=p.read_text(); assert text==pages[u['pdf_page']-1]
                pieces+=['\n\n## '+s['id']+' PDF page '+str(u['pdf_page'])+'\n\n',text]
                units.append({'source':s['id'],'pdf_pages':[u['pdf_page']],'file':str(p)})
        else:
            for u in s['selected_pages']:
                p=reader/u['artifact']; text=p.read_text(); assert text==u['literal_pdf_text']
                pieces+=['\n\n## '+s['id']+' PDF pages '+str(u['pdf_first'])+'-'+str(u['pdf_last'])+'\n\n',text]
                units.append({'source':s['id'],'pdf_pages':[u['pdf_first'],u['pdf_last']],'file':str(p)})
    review=author.with_name(stem+'-review'); review.mkdir(exist_ok=False)
    (review/'task.json').write_text(json.dumps(task,ensure_ascii=False,indent=2)+'\n')
    (review/'argument.md').write_text(''.join(pieces))
    settings=json.loads((R/'campaigns/round-36/P03.3-original-envelope-continuity-review/settings.json').read_text())
    assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
    settings['usagePrefix']=f'catalogue-20261003/r{n}/{atom}-exact-public-curve-review'
    (review/'settings.json').write_text(json.dumps(settings,indent=2)+'\n')
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    freeze={'prepared_utc':datetime.now(timezone.utc).isoformat(),
            'argument_sha256':sha(review/'argument.md'),'argument_bytes':(review/'argument.md').stat().st_size,
            'task_sha256':sha(review/'task.json'),'settings_sha256':sha(review/'settings.json'),
            'author_argument_sha256':sha(proof),'actual_canonical_notes_sha256':sha(reader/'actual-canonical-notes.json'),
            'root_read_record_sha256':sha(reader/'complete-root-read.json'),
            'literal_published_units':units,'earlier_blocked_review_payload_included':False,
            'private_transcripts_sql_auth_included':False,'provider_submission_attempted':False,
            'automatic_review_rejected_this_new_packet':False,
            'state':'Prepared locally only; not submitted while specific generated-material export permissions remain pending.',
            'original_atom_solved':False,'R39_TheoremC_gap_attached':n==39}
    (review/'freeze.json').write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'round':n,'directory':str(review),'argument_bytes':freeze['argument_bytes'],
                      'freeze_sha256':sha(review/'freeze.json'),'provider_submission_attempted':False}))
