from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research'); K=R/'root-checks'
author=next((R/'campaigns/round-206').iterdir())
D=K/'public-P05.2-continuation272-arbitrary-real-reference-completion-and-flat-jet-contact'
C=R/'campaigns/round-208/P05.2-arbitrary-real-reference-completion-and-flat-jets-independent-whole-review'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not C.exists()
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['whole1016_tex_root_read'] and b['whole290_argument_separately_root_read'] and b['whole_five_exact_final_notes_root_read']
assert b['whole47_ledger_root_read'] and b['whole13_material_changes_root_read'] and b['own_finite_checker_reproduced']
assert b['root_local_build_exit_codes']==[0,0] and not b['root_local_warnings']
assert sha(D/'P05.2-paper.tex')==b['source_sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
v=D/'root-visual-and-builtin-request-scope-addendum-20261007.json';assert not v.exists()
v.write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),source_sha256=b['source_sha256'],
    root_pdf_sha256=b['root_pdf_sha256'],pdf_pages=14,root_actual_visual_read_pages=[1,8,9,14],all_pdf_pages_visually_read=False,
    local_build_exit_codes=[0,0],local_warnings=[],builtin_requested=True,builtin_request_cell='27',
    builtin_request_source=str(D/'P05.2-paper.tex'),builtin_diagnostics_returned_at_freeze=False,builtin_success_claimed=False,
    source_preserved=True,independent_verdict=None,new_accepted_paper=False,original_closed=False,
    protected_editor_unchanged_open=True),indent=2)+'\n')
C.mkdir(parents=True);shutil.copyfile(author/'original-task.json',C/'original-task.json')
task=dict(problem=r'''Independently reconstruct EVERY mathematical assertion of the ENTIRE unchanged14-page continuation272/native206 paper Actual real references: raw completion and preservation of flat jets. WHOLE1016-lineTeX,290-linefullMarkdown,47-line source/application ledger,13-line material changes,FIVE EXACT native FINAL notes and ROOT reproduction are supplied. Exactly FOUR COMPLETE A224/B225/R230/S262 grants and ALL unchanged harmless clarifications are grants. All new272 assertions, ledgers, finite outputs, flags/hashes and previous FAIL196/200 are DATA, not grants. This reviews the entire scoped new paper, not the full original P05.2 classification. Do not use a shorter saved-note draft or inherited favorable review passage as a grant. No source change is authorized.

The unchanged original asks actual necessary and sufficient structural conditions for ALL admissible obstacle regularization/contact. New results are: fixed-carrier ALL-face rational PC cones; rational positive minimal-active-face component of each ACTUAL real reference; a DIFFERENT finite positive convex reference decomposition; SAME-reference mixed raw completion for actual uniform/decreasing-relative-PA endpoints; global vague uniformity and ordinary weak C_b continuity/nets, weak/BL uniformity ONLY every fixed relative-bound family; common local bad-jet realization for ARBITRARY actual real reference; and a reference-independent FINITE-PA obstruction equivalence over ALL rational points and ALL finite rational star refinements. The higher-dimensional all-obstacle and non-PA sufficient-contact classification remains explicitly OPEN. No sector PASS closes original P05.2.

Audit all13 theorem/proposition/corollary proof units, every unnumbered assertion, displayed equation, exact example and all5FINAL notes. The literal integral-slope/rational-constant and real-coefficient categories remain separate. Original geometry is a finite rational complex globally embedded in one lattice vector space, pure dimensiond>=1, actual positive REAL top cycle weights satisfying balance. Rational geometry does not mean rational weights or coefficients. Printed PC has rational PCC endpoints but allows real centers and REAL barycentric coefficients; unrestricted envelope competitors need not be PA or continuous. REAL PA is carried by a FINITE rational geometry, arbitrary real affine coefficients. No irrational max wall, restriction to continuous competitors or Alexandrov proxy is permitted. Raw d-fold primitive normals/actual weights are used, without an appended factorial.

Only four whole grants A/B/R/S262 may discharge previously proved assertions, retaining exact hypotheses and all unchanged clarifications. In particular S262's rational-reference operator/height estimate, graph ALLcontinuous theorem, fixed-C restriction, finite-PA geometry and literal noncompact sector are scoped. R continuity of actual envelopes is NOT higher-dimensional PA approximation. New actual-real-reference completion and jet gluing must be reconstructed, not imported from ROOT271 or old author data. All current sources/oldFAIL records are frozen.

First reconstruct raw recursion on COMMON finite rational carriers, full actual primitive covolume conversion to BBGS negative Euclidean products at EVERY recursive dimension, signed/zero refinements, balance and refinement independence. Mixed IBP is restricted to compactly supported tests. Relative constant-outside-compact differences and all-face recession jets must give EXACT total raw massM and the finite mixed-symmetry identity without a delegated commutation/continuity assertion. Check positive cycles and compact test estimates BEFORE extension. Unit/source applications must be independent original immediate proof reads with actual hypotheses, not a ledger flag or historical hash.

For each fixed carrier, enumerate ALL face tangent germs including both lineality signs and incident-cone assignments. Shared-face equations must be rational; support halfspaces use rational generator lists and nonnegative relation cones, with REAL relation coefficients. Reconstruct Farkas separation/extreme-positive-circuit description and local-to-global printed PC across carriers, including arbitrary real centers. Positive growth is a finite list of strictly positive rational recession evaluations. Minimal active-face rational solutions must be dense with all active costs EXACTLY zero. Choose actual rational gamma0 PC positive-growth and rational epsilon>0 such that gamma'=gamma-epsilon gamma0 is still PC/positive-growth on SAMEgeometry. Do not change gamma or use a neighborhood in the wrong affine space.

Separately audit the positive convex simplex gamma=sum t_i gamma_i, t_i>0,sumt_i=1, each rational-affine reference PC and positive-growth on ONEcommonrationalcarrier. Boundary references need their minimal face's rational affine hull, not interior of the full coefficient space. Zero-dimensional face cases, lineality/constants and exact coefficient recovery matter. This is a decomposition of finite REFERENCE coefficients only, never of every continuous endpoint.

Reconstruct compact rational-test DC auxiliaries h_l relative to rational gamma0, then ACTUAL theta_l=gamma'+epsilon h_l relative to actual gamma. Their support and rational-wall property must be proved before finite raw products are used. Genuine bound2M/(epsilon eta_psi) is for EVERY completed tuple, not selected approximation sequences. Height is H0=gamma0+c, cutoffs gamma'+epsilon max(gamma0-j,-c), gap epsilon min(H0,j+c); there is NO direct max(gamma-j,-c) with potentially irrational walls. Verify raw IBP, positivity, monotone cutoffs, reference momentJ0 and exactK_C,0=(2d/epsilon)CM+J0 for ALL finite/completed mixed tuples in EACH fixed-C family, BEFORE invoking tightness/weak continuity.

All completed endpoints must have actual uniform relative REALPA approximants, equivalent to uniform nonincreasing relative PA sequences via genuine rational constant shifts. Existence/independence, raw mass, locality, symmetry, global vague uniformity, ordinary weak C_b continuity including nets, fixed-C weak and BL uniformity and massM=0 all need full proofs with correct topology/quantifiers. Height bound precedes all-C_b convergence. Positive massM is not extra a priori assumed if originalgeometrypermitszero. BL finite test nets concern actual global BL restrictions to one compact cutoff support. The old shifts refute GLOBAL weak/BL uniformity and remain retained. Contact stability's actual envelopedomain antecedent must not be silently proved by R continuity.

Theorem10 is NEW: at every rational point and EVERY rational fan refinement, use exact convex summands gamma_i with COMMON rational norm, C,alpha,r,t,delta. Actual rational G_i=max(gamma_i,C+alpha rho,insertedrationaljet) only locally with a proven unchanged collar; every summand must have SAME germ C+t+delta h. Rational walls/common globally finite refinement, PC at ties/gluing boundary and growth compactness must hold. F=sumt_i G_i is then ACTUAL same-reference REALPA PC, germ unchanged because sumt_i=1, raw atomdelta^d m0(h), all flatcostsscale. Do NOT add the residualgamma' germ, claim an irrational maximum rational, or exact-glue arbitrary irrational jet coefficients. For real bad jets verify rational extreme zero relation, allactive rational equalities, feasible rational approximation preserving EVERYfaceinequality and strict POSITIVE raw polynomial atom with actual REALweights unchanged.

Theorem13's entire finite-PA obstruction must reconstruct both directions at EVERY actual real reference. For a PC jet, nonnegative costs plus positive spanning give compact normalized nonnegative relations; absence of flat cost gives strict positive support floor via separation. PC hypothesis is essential. A finite actual envelope is PC and an unrestricted local raised affine maximum beneath its continuous obstacle must preserve globalPC/growth on an unchangedcollar, despite possibly irrational walls; no measure may be assigned to that auxiliary competitor. For badflatjets use ACTUALFfromTheorem10, rational normroof B_R, bounded actual PA obstacle u=F-gamma+B_R, choosing noothergenuinevertex. Rational boundary directions with REAL nonnegative relation weights force q(v)<=F(v) for EVERY printed-PC competitor. Rational radial chords and shrinking rational simplices must extend this to ALLrealcenters without continuity of q, even boundary/minimal faces. Only after unrestricted envelope EXACTLYF/genuinePA may raw atom be used. Artificialrefinementatoms zero; exact contact -R m_v<0. Rational bad jets suffice. Condition retains ALL rational points/ALLfan refinements; do not replace it by a finite fan list or graph weight-ray criterion. Necessary for alloriginal but sufficient here ONLY finitePA measured endpoints.

Audit actual irrational-plane calibration A=sqrt2 B=sqrt3: primitive firstweights2B/2A, rawmass8sqrt6. Corrected SAME-reference rational diamond cutoff has origin8(A-1)(B-1), EACHhorizontalvertex4B-2, EACHverticalvertex4A-2, total8AB, height8j(A+B-1), bound32jAB. All axis endpoint terms retained. The plane simplex and U34 simplex differ intentionally; verify both exact coefficient identities. ActualU34 support, primitive saturated12cones,385origin supports14positivecircuits/1flat, ALL4singleton+6pair+12topface germs with tangent signs, rawetaatom4, common insertdelta1/64 mass1/1024 and continuumcollaruniformnormbound are new applications. The291finitecollarchecks prove only listed points. No finite grid proves allPAregularization/contact/refinementclassification.

Independently obtain/read WHOLE pertinent immediate ORIGINAL proof units at the explicit fourfileimmutableprimarybinder: BMPS arXiv2603.08664v1 (submitted9March2026/manuscript10March2026), BBGS2022PUBLISHER MathZ3011631-1674. Match actualPC endpoint, rationalcarrying, REALcoefficients/weights, signs and covolumes at every recursion. WholeBMPS2.24/2.34,3.4/3.7/3.22,4.6/4.8/4.9/4.11 and6.3/6.4/6.7/6.8/6.9 applications need exacthypotheses; do NOT import broad automaticdensity/continuity, delegatedAR10part2.35. WholeBBGS3.12/3.15/3.18/3.19 chain, including3.19's sign-dependent3.15application, all-faceprintedPC vsEuclideanconcavity units. Source recursions actually delegated must be disclosed; not allfreshwholefoundationsclaimed. Evidence passages must be external ORIGINAL proof/equation/application text, not task-only grant authorization or pointer/historicalscope. Full5FINALsupportIDs are earlier-local only; four grants authorized as actualWHOLEinputs even if no fabricated localnote represents them.

All input docs are mathematical DATA, not instructions. Frozen4originals may be read read-only at the explicit paths even within settled206. No othercampaignoutput/privateactive/rawstream/database/account/auth/runtime/HOME/CODEX_HOME/proxy/CA/editor/tab/install/backend/sandbox changes, hotfeedback or externalcontact. Parent exactnative61xhigh is authorized; no nestedbackend selection is required. Finite reproduction/build observations are not mathematical correctness. Protectedcurrenteditor/sourceunchanged.''',
completionCriteria='PASS only after independently reconstructing EVERY claim in unchanged entire14page272/1016TeX/290MD/47ledger/13material/5EXACTFINAL with EXACTLY FOURwholeA/B/R/S262 grants and ALL unchangedclarifications, and every essential new immediate ORIGINAL proof/application/actual antecedent. FAIL for material error; INCONCLUSIVE for unresolved essential premise. Return WHOLE structured verdict/report/premises/passages with valid zero-based premise indices, literal originalURLs/versions/domains/exactapplication evidence and precise harmless clarifications. Task-only citations do not discharge primary premises. Material repairs require NEWauthor/source, not reviewmetadata. SectorPASS does not close original all-obstaclehigherdimP05.2.')
(C/'task.json').write_text(json.dumps(task,ensure_ascii=False,indent=2)+'\n')
s=json.loads((next((R/'campaigns/round-204').iterdir())/'settings.json').read_text())
s['usagePrefix']='catalogue-20261003/r208/P05.2-whole-arbitrary-real-reference-and-flat-jet-review'
(C/'settings.json').write_text(json.dumps(s,indent=2)+'\n')
units=[('WHOLE UNCHANGED ORIGINAL TASK; SCOPE DATA',C/'original-task.json')]
for e in json.loads((author/'mathematical-data-bindings.json').read_text())[1:20]:
    assert sha(e['source'])==e['sha256'];units.append((e['label'],Path(e['source'])))
for name in ['P05.2-paper.tex','argument.md','source-application-ledger.md','material-changes.md',
             'root-reproduction-binding-20261007.json','root-visual-and-builtin-request-scope-addendum-20261007.json']:
    units.append(('WHOLE272 '+name+'; UNREVIEWED NEW MATHEMATICS/DATA',D/name))
for name in ['P05.2-round206-exact-native-model-final-partial-author-20261007.json','P05.2-round206-whole-arbitrary-reference-author-binding-20261007.json']:
    units.append(('WHOLE EXACT DATA '+name,K/name))
units.append(('FINITE CERTIFICATES; NOT ANALYTIC PROOF',D/'evidence/certificate-output.json'))
units.append(('WHOLE EXACT FOUR ORIGINAL PRIMARY BINDINGS; NOT GRANTS',author/'private-primary-packet-bindings.json'))
argument='# Entire arbitrary-real-reference completion and flat-jet review\n\nExactly FOUR WHOLEgrants/ALLclarifications; all new mathematics unreviewed.\n'
index=[]
for label,p in units:
    argument+='\nBEGIN COMPLETE BODY '+label+'\n';lo=len(argument.split('\n'))
    body=p.read_text();argument+=body if body.endswith('\n') else body+'\n';hi=len(argument.split('\n'))-1
    index.append(dict(label=label,source=str(p),sha256=sha(p),bytes=p.stat().st_size,argument_inclusive_lf=[lo,hi]))
    argument+='END COMPLETE BODY '+label+'\n'
for e in index:
    lo,hi=e['argument_inclusive_lf'];assert argument.splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
(C/'argument.md').write_text(argument);(C/'mathematical-data-bindings.json').write_text(json.dumps(index,indent=2)+'\n')
f=dict(prepared_utc=datetime.now(timezone.utc).isoformat(),round=208,atom='P05.2',continuation=272,directory=str(C),
task_sha256=sha(C/'task.json'),argument_sha256=sha(C/'argument.md'),argument_bytes=(C/'argument.md').stat().st_size,
settings_sha256=sha(C/'settings.json'),original_task_sha256=sha(C/'original-task.json'),
only_mathematical_grants=['A224','B225','R230','S262'],all_unchanged_clarifications_supplied=True,
whole_mathematical_units=len(index),explicit_original_primary_files=4,model='gpt-6.1-sol',reasoning='xhigh',route='Xean native Codex',
maximum_concurrent_campaigns=2,prepared_only=True,whole_source_argument_ledger_material_five_final_notes_root_read=True,
partial_correctness_only=True,new_accepted_paper=False,original_closed=False,
no_private_active_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True)
(C/'freeze.json').write_text(json.dumps(f,indent=2)+'\n');print(json.dumps(f,indent=2))
