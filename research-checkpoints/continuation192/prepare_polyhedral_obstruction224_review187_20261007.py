from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'; D=K/'public-P05.2-continuation224-strict-growth-obstruction'
C=R/'campaigns/round-187/P05.2-U34-strict-growth-contact-obstruction-independent-partial-review'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not C.exists()
repro=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert repro['whole_saved_source_root_read'] and repro['fresh_clean_local_builds']==2 and repro['local_warning_count']==0
assert sha(D/'P05.2-paper.tex')=='49c87b02c5fd2269eaae85f4d16537d462ddf1413ab80cbefd4deb8ea6ef5aae'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
old=next((R/'campaigns/round-184').iterdir()); C.mkdir(parents=True)
(C/'original-task.json').write_bytes((old/'original-task.json').read_bytes())
assert sha(C/'original-task.json')=='310b2ca93dadefd8d75089b5df3ddf286718986da1ce68ea65378f310047b99c'
task=dict(problem='''Independently reconstruct and audit ALL new mathematics in the entire nine-page P05.2 U(3,4) strict-growth contact-obstruction paper, its complete argument and the three complete author notes. There are NO caller mathematical grants. The unchanged originalP05.2 and its control-glyph-preserving repair are scope data, not source theorems. This audit concerns the exact whole partial theorem and does not classify all general balanced polyhedral pairs.

Retrieve literal primary BMPS arXiv:2603.08664v1 and read full pertinent definitions/proof units, including essential ungranted dependencies. Import source definitions precisely, while independently reconstructing every geometry, local-support, convexity, refinement, envelope and raw-intersection assertion used by this paper. Do not certify source proofs by excerpts or author ledger flags. Distinguish integral slopes/rational constants, explicit real finite-PA formulas on rational subdivisions, and arbitrary PC endpoints whose operator is not defined. The full regularization theorem is not granted. The source's strict PC wording admits zero coefficients; audit the disclosed active-coefficient interpretation and explicit strict local supports without silently claiming a literal stronger source theorem.

Check saturated tangent lattices and primitive inward normal lifts, fine U(3,4) matroid description, all top-face weights and balancing, constant cancellation, refinement independence of the actual finite operator and absence of hidden factorials. Audit local ambient supports implying segment/PCC Jensen inequalities and intersection positivity against every nonnegative balanced local cycle. Check at zero, singleton rays, pair rays and new bent edges, and verify that plane supports extend ambiently as required.

For all real A>=0,B>0,C>B and rational epsilon>0, audit Gamma=A eta+B h, U=C u_epsilon, all shared-face values, strict local reference supports and positive growth, actual PA domain of P=Gamma+B u_epsilon and the precise endpoint regularization antecedent. Independently prove maximality against EVERY PC competitor in the actual source envelope, with rational endpoint/PCC constraints and all irrational centers. Verify each proposed rational subdivision and simplex argument, not merely the displayed ansatz. Compute the genuine raw masses 4(A+B)^2 at zero and B(4A+3B) at each special vertex; audit global first-cycle balances, absence of additional atoms, exact reference degree 4A^2+16AB+10B^2 and contact integral -4(C-B)epsilon(A+B)^2. Check local Alexandrov-area factor2 only at complete plane germs; never substitute ambient volume at the singular origin.

Audit the separate literal-regularity failure for Gamma=h, obstacles v_n=min(1/n,(1-h)_+) and exact envelope Q_n=max(h,(1-1/n)h+1/n). Check all-obstacle hypotheses, the convex integer-slope restriction along a primitive segment and the uniform gap >=1/(4n) for every literal PA PC approximant. Do not assign a regularizable MA to Q_n. Check the logical distinction between contact failure at a genuine PA endpoint and exclusion from simultaneous pair-level regularity/universal orthogonality, especially because the simplest literal pair itself is nonregular.

Finite numerical checks and compiler/provenance success do not prove continuum statements. Audit exact reported evidence and scope without requiring an operational re-run in this read-only shell-disabled review. The nine-page paper is new unreviewed mathematics; full originalP05.2 remains open unless the exact original classification is independently proved, which the author explicitly does not claim. Do not read other campaigns/private streams/raw SQLite or send hot feedback. Keep the existing protected editor and all runtime/auth/account/sandbox settings unchanged.''',
completionCriteria='PASS only if every theorem and proof in the ENTIRE partial manuscript is sound in its precise operator/category/regularity domain, with all essential ungranted generated dependencies reconstructed or exactly primary-source checked. No caller mathematical grants. FAIL for material errors, INCONCLUSIVE for unresolved essential premises. State the exact proved scope and the unchanged original classification gap. Preserve literal source version, every premise and passage with valid zero-based bindings; no synthetic evidence or inferred original closure.')
(C/'task.json').write_text(json.dumps(task,ensure_ascii=False,indent=2)+'\n')
s=json.loads(next((R/'campaigns/round-185').iterdir()).joinpath('settings.json').read_text()); s['usagePrefix']='catalogue-20261003/r187/P05.2-U34-strict-growth-review'
(C/'settings.json').write_text(json.dumps(s,indent=2)+'\n')
units=[('UNCHANGED WHOLE ORIGINAL TASK; SCOPE DATA',C/'original-task.json'),('CONTROL-GLYPH-PRESERVING REPAIRED AUTHOR TASK; DATA',old/'task.json'),('ENTIRE UNREVIEWED NINE-PAGE PAPER',D/'P05.2-paper.tex'),('ENTIRE UNREVIEWED COMPLETE ARGUMENT',D/'argument.md'),('ENTIRE THREE CANONICAL AUTHOR NOTES; UNREVIEWED DATA',K/'P05.2-round184-completed-actual-author-result-20261007.json'),('WHOLE QUOTE-FREE SOURCE APPLICATION LEDGER; DATA',D/'source-application-ledger.md')]
argument='# Whole partial-paper independent review; no caller mathematical grants\n\n'; index=[]
for label,p in units:
    argument+='BEGIN COMPLETE BODY '+label+'\n'; start=len(argument.split('\n')); body=p.read_text(); argument+=body if body.endswith('\n') else body+'\n'; end=len(argument.split('\n'))-1
    index.append(dict(label=label,source=str(p),sha256=sha(p),bytes=p.stat().st_size,argument_inclusive_lf=[start,end])); argument+='END COMPLETE BODY '+label+'\n\n'
(C/'argument.md').write_text(argument); (C/'mathematical-data-bindings.json').write_text(json.dumps(index,indent=2)+'\n')
f=dict(prepared_utc=datetime.now(timezone.utc).isoformat(),round=187,atom='P05.2',continuation=224,directory=str(C),task_sha256=sha(C/'task.json'),argument_sha256=sha(C/'argument.md'),argument_bytes=(C/'argument.md').stat().st_size,settings_sha256=sha(C/'settings.json'),original_task_sha256=sha(C/'original-task.json'),only_mathematical_grants=[],route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,entire_source_root_read=True,partial_correctness_only=True,new_accepted_paper=False,original_closed=False,no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged=True)
(C/'freeze.json').write_text(json.dumps(f,indent=2)+'\n')
launcher=(R/'launch_frozen_partial_review185_20261007.py').read_text().replace('round-185','round-187').replace('round=185','round=187').replace('+[185]','+[187]')
launcher=launcher.replace('(173,175,176,177,178,179,180,181,182,184)', '(173,175,176,177,178,179,180,181,182,184,185,186)')
launcher=launcher.replace("only_mathematical_grants=['O','D','N','T']", 'only_mathematical_grants=[]')
launcher=launcher.replace('Entire222 seven-page all-complete-field actual projective-line kernel equation, allpoint existence/every-solution uniqueness/intrinsic target/variational value/rational bundles; four whole accepted grants O217/D214/N220/T171, all new proofs ungranted.', 'Entire224 nine-page U(3,4) strict-growth contact obstruction and literal regularity failure, all definitions and generated proof dependencies; no caller grants and no original classification closure.')
(R/'launch_frozen_partial_review187_20261007.py').write_text(launcher)
print(json.dumps(f,indent=2))
