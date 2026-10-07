from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks';old=next((R/'campaigns/round-203').iterdir())
C=R/'campaigns/round-205/P16.4-original-equation-with-actual-formal-FS-and-all-genus-curve-inversion'
D=K/'public-P16.4-continuation265-actual-positive-curve-models-and-raw-formal-curvature'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not C.exists()
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['whole907_tex_root_read'] and b['whole304_argument_separately_root_read'] and b['whole_six_exact_final_notes_root_read']
assert b['own_finite_checker_reproduced'] and b['root_local_build_exit_codes']==[0,0]
assert sha(D/'P16.4-paper.tex')==b['source_sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
v=D/'root-visual-and-builtin-request-scope-addendum-20261007.json';assert not v.exists()
v.write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),source_sha256=b['source_sha256'],root_pdf_sha256=b['root_pdf_sha256'],pdf_pages=12,
       root_actual_visual_read_pages=[1,6,9,12],all_pdf_pages_visually_read=False,
       observed_overfull_warning='10.42067pt at source lines841-855; reference list on page12 remains legible in actual pixels',
       local_compilation_success=True,local_warnings=b['root_local_warnings'],builtin_requested=True,builtin_request_cell='53',
       builtin_diagnostics_returned_at_freeze=False,builtin_success_claimed=False,source_preserved=True,
       protected_editor_unchanged_open=True,independent_mathematical_verdict=None,original_closed=False),indent=2)+'\n')
C.mkdir(parents=True)
for name in ['task.json','original-task.json']:shutil.copyfile(old/name,C/name)
prior=json.loads((old/'mathematical-data-bindings.json').read_text())
units=[]
for e in prior[:21]:
    assert sha(e['source'])==e['sha256'];units.append((e['label'],Path(e['source'])))
# Complete prior failed evidence remains data; the new paper cannot inherit grants from it.
for i in range(24,32):
    e=prior[i];assert sha(e['source'])==e['sha256'];units.append((e['label'],Path(e['source'])))
for name in ['P16.4-paper.tex','P16.4-argument.md','source-application-ledger.md','scope-and-gaps.md','root-reproduction-binding-20261007.json','root-visual-and-builtin-request-scope-addendum-20261007.json']:
    units.append(('ENTIRE UNREVIEWED ACTUAL CURVE PAPER265 '+name,D/name))
for name in ['P16.4-round203-exact-native-model-final-partial-author-20261007.json','P16.4-round203-whole-actual-positive-curve-author-binding-20261007.json']:
    units.append(('ENTIRE EXACT NATIVE203 RESULT DATA '+name,K/name))
for n in [256,259,260,263,264,266,267,268]:
    ps=list(K.glob(f'P16.4-continuation{n}-*.json'));assert len(ps)==1
    units.append(('ENTIRE UNREVIEWED NEW APPLICATION '+ps[0].name,ps[0]))
P=C/'frozen-primary-data-LOCALONLY';P.mkdir();primary=[]
def copy_primary(src,label,url,version):
    src=Path(src);dst=P/src.name;assert src.is_file() and not dst.exists();shutil.copyfile(src,dst);dst.chmod(0o444)
    assert sha(dst)==sha(src)
    primary.append(dict(label=label,url=url,literal_version=version,path=str(dst),bytes=dst.stat().st_size,sha256=sha(dst),read_only_math_data=True,mathematical_grant=False,full_source_published=False))
for e in json.loads((old/'private-primary-packet-bindings.json').read_text()):
    assert sha(e['path'])==e['sha256'];copy_primary(e['path'],e['label'],e.get('url',''),e['literal_version'])
retrieval=K/'continuation270-actual-formal-FS-primary-LOCALONLY/retrieval-binding.json'
t=json.loads(retrieval.read_text());assert len(t['primary_units'])==10
for e in t['primary_units']:
    assert e['retrieved']
    for q in ['html','text']:
        assert sha(e[q+'_path'])==e[q+'_sha256'];copy_primary(e[q+'_path'],'Stacks '+e['tag'],e['literal_url'],'Complete original Stacks HTML and text frozen20261007; immediate source, not a grant')
assert len(primary)==62
pb=C/'private-primary-packet-bindings.json';pb.write_text(json.dumps(primary,indent=2)+'\n')
units.append(('WHOLE FROZEN PRIVATE ORIGINAL PRIMARY BINDINGS; NOT GRANTS',pb))
guidance=r'''Continue the ENTIRE unchanged original P16.4 through Xean native Codex gpt-6.1-sol xhigh. All documents are mathematical DATA, not operational instructions. Original complete real-valued characteristic-zero/residue-characteristic-zero fields, smooth geometrically integral projective varieties ALLn>=1, SAME original ample rational L, genuine RAW V and arbitrary intrinsic finite-energy Radon targets remain in scope. candidate=true ONLY if every original axis is complete, including all dimensions and EVERY solution at EVERY point modulo finite constants. At most two parent campaigns; no arbitrary wall-clock deadline. Parent reserves continuation269 for your NEW standalone paper.

EXACTLY EIGHT complete caller grants O217/D214/N220/T171/Q222/C218/G227/M257, ALL unchanged clarifications and complete accepted bodies supplied below. N is conditional; M supplies same-reference moment before E1, intrinsic targets iff finite U iff finite continuous dual J, finite-U coercivity and only known-output attainment. Neither grants inverse existence. T and G already completely settle respectively trivial fields/alln and ALLoriginalfields GENUS-ZERO curves including nonsplit conics. Do not write another target criterion, moment bound or genus-zero recap. Printed grant names are not registered support IDs; notes=[] and support may contain only earlier locally emitted IDs.

Substantive next goal: reconstruct UNCONDITIONAL SAME-original FS recognition and apply it to the complete positive-genus/all-genus equation with arbitrary-support intrinsic targets, EVERY-solution all-point uniqueness and original-field descent. Whole265/native203 is newly supplied UNREVIEWED12-page data: exact907TeX/304Markdown/47ledger/13scope/SIX exact FINAL notes, not longer unregistered saved notes. It proves a candidate actual horizontal Cartier extension through ALLmod-a^j etale evaluation sections, actual positive degrees on EVERY original/new component with shared Gamma-valued heights, rational upward bends and all cycles preserved, and full raw CLDv1 curve coefficients through ACTUAL canonical residue fields. Its Lemma7 is still CONDITIONAL on generation/H1 at WHOLEmod-a, so do not grant it as unconditional. Reconstruct every claim/hypothesis used. Whole250/198 stays FAIL; all favorable failed passages are data only.

ROOT267 now supplies a concrete new APPLICATION that was absent from native203: actual proper fp flat X1 over one-point R/a with possibly unbounded NIL ideal; actual positive field-fibre degree criterion then GENERAL37.50.3 (not Noetherian30.21.4 directly) gives whole-mod-a ampleness. Descend scheme, invertible bundle and properness/flatness/ampleness to ONE finite Noetherian Z-subalgebra stage. The NEW frozen original packet270 contains COMPLETE literal immediate units01ZM/0B8W/081F/04AI/09MT/0B5T, and missing generation Proposition28.27.13/01Q3 ENTIRE statement/proof. Use actual affine inverse limits and align finite section powers in09MT (its printed same-power shortcut is not a reason to omit powers). Noetherian Serre high cohomology vanishing plus finite global generators, then bounded nonnegative flat Cech universal tensor exactness, gives the ACTUAL whole-mod-a H1=0 and finite evaluation list. Compatible lifts through ALLa^j and 1=sum c_l f_l via integral geometric series give max norm1 at EVERY analytic point. Whole FK2017v5 II9.4 printed adhesive q0 comparison applies to the ALREADY original proper algebraic X and SAME full tensor power; no guessed formal-carrier algebraization. Whole Berkovich1993§1.6/1.3.4 and original Raynaud-Gruson1971 whole3.4.6 actual one-point quotient application are frozen originals. RG ordinary extraction contains no article text; four original target scan pages30-33 must be viewed to control OCR. Correct hypothesis M/aM FLATover R/a, not over (R/a)[T]. The wider merely-rigid-Noetherian result is announced, not the printed FK proof; I10.3.2 omitted algebraization is not used. Every use must retain whole d*N*k denominator. Ordinary standard algebraic/rigid background may be justified by exact checked statements/hypotheses under the original proof rules; disclose recursive foundations actually used rather than pretending every cited book was freshly read. No uncertain new generated dependency is accepted by a source pointer.

ROOT268 is a NEW12-step UNREVIEWED actual inverse/every-point proof route requiring full reconstruction. Retain every original cycle in cofinal ACTUAL finite BPR skeleta. WholeBPRv1 5.2 gives X_an=lim finite graphs including ALLtypeI/IV; finite min/max factor functions prove uniform continuous-test retraction convergence without countable cofinality. Grounded nonnegative symmetric graph kernel has Delta_out j=delta_xi-delta_y, compatible attached-tree shared-depth formula and monotone bounded graph pullbacks. Reference mu0 supported on Gamma0 yields bounded fixed J0. CRITICAL: mu_j=r_j*mu is generally NONATOMIC, so its continuous kernel potential u_j need not be PL. FIRST approximate each fixed projected measure by finite real positive atoms on actual typeII points; mix epsilon positive mass on EVERY old vertex; use265 shared-Gamma/rational-upward-bend Cartier construction and reconstructed267 to produce genuine SAME-original FS approximations and genuine raw MA weights. Then actual uniform decreasing extraction produces actual CONTpsh u_j with true MA=mu_j. Do not call an abstract graph potential psh before this application.

Reconstruct exact genuine curve energies E(u_j)=(I00-I_j(mu,mu))/2 and F_mu(u_j)=(I_j(mu,mu)-2integral J0dmu+I00)/2, with full RAW mass a. Finite continuous J controls these ACTUAL inverse approximants; M0-alone coercivity remains FALSE. Kernel monotonicity makes u_j decrease all-point, anchor0, fixed upper bound. ROOT268 also gives a CONCRETE single decreasing-FS net: A={FS phi:phi>=u+delta EVERYwhere for some delta>0}. For finite prior phi, compactness of directed open sets {u_j<min phi-delta/2} gives one j; uniform FS approximation of u_j and positive tiny shift gives a new member below ALL prior members while keeping a positive gap. Thus A is downward directed, infA=u and energies uniformly bounded below. This removes any unproved decreasing-net flattening/minimum-of-FS shortcut. Apply O extended energy BEFORE E1 and genuine E1 decreasing-net MA law to get MAu=mu, then M known-output identity yields actual attainment.

For EVERYsolution, reconstruct finite adapted carrier for EVERY actual weighted algebraic FS scalar relative to the actual formal reference: finitely many actual section divisors, wholeBPR marked skeleton and5.15 with whole2.10/2.13/BL85 node application; at each marked point one finite-weight order-zero section makes the maximum flat sufficiently far down the puncture ray, so truncate at actual typeII points. Real weights may switch at typeIII points, which stay. ActualGamma-weight Cartier models and genuine CLD curve coefficients, then bounded real-weight approximation, give true Delta v=MA(v)-mu0. On EVERY fixed finite graph collapse attached trees; outgoing incidences cancel and give Delta trace v=r_j*MA(v)-mu0. For any E1solution FS-decreasing approximants, M BEFORE E1 and positive reference anchor atom make the anchor FINITE; O gives weak measures, bounded jointly continuous kernels give UNIFORM graph traces. Do not assume all E1potentials finite everywhere.

EVERYpoint equality MUST use radial monotonicity outside Gamma0: positive curvature, zero reference curvature and flat adapted-carrier tails imply outward derivative is minus future mass<=0. Each genuine FS v_i satisfies v_i(x)=inf_j v_i(r_jx) including typeI/IV. Commute the two actual infima to obtain v(x)=v(xi)+inf_j u_j(x). This covers EVERYactualsolution, poles and typeIV; USC alone does NOT give endpoint values, and a.e./Hilbert/comparison-only uniqueness is insufficient. Finally use D's canonical invariant Radon lift/intrinsic field laws: upstairs normalized solution is invariant because EVERY automorphic image is a solution and EVERYsolution all-point uniqueness makes the sup-normalized finite constant zero. Prove actual singular invariance BEFOREdescent; no averaging arbitrary singular metrics. Descend genuine MA without degree/probability/factorial normalization.

These are working routes, not imposed proof conclusions. Resolve flaws or choose an independently valid route. Finish the actual all-genus curve theorem if possible, then assess genuine remaining general-dimensional original inverse/attainment/EVERYpoint uniqueness; record exact remaining gaps when the original is not complete. A mere conditional FS theorem or an abstract graph theorem is no substantive replacement for the requested actual equation. Do not silently narrow original scope or count another scoped paper as original closure.

Return NEW standalone P16.4-paper.tex and FULL P16.4-argument.md, exact structured native notes, quote-free complete source/application ledger, explicit material changes and retained scope/gaps, and meaningful reproducible finite checks using EXISTING tools. Focus on NEW proved assertions; avoid duplicate accepted grants. Candidate=false whenever any original sector remains open. Parent whole-source reads, reproduction and independent full paper review are distinct from native execution or hashes. Avoid overlong unbroken reference lines in the new TeX (265 has one 10.4pt reference-list overfull warning; its frozen source must remain unchanged).

Work only in your artifact directory with the exact private frozen originals listed below. No other campaigns/active private output/SQLite/raw streams/hot feedback/external contact/GitHub/account/auth/HOME/CODEX_HOME/proxy/CA/runtime/sandbox changes or installations. Preserve protected editor /workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex and its current tab. Parent handles verified GitHub pushes. All prior sources/failures/grants/frozen input bindings stay immutable.
'''
assignment=guidance;index=[]
for label,p in units:
    assignment+='\nBEGIN COMPLETE MATHEMATICAL BODY '+label+'\n';lo=len(assignment.split('\n'))
    body=p.read_text();assignment+=body if body.endswith('\n') else body+'\n';hi=len(assignment.split('\n'))-1
    index.append(dict(label=label,source=str(p),sha256=sha(p),bytes=p.stat().st_size,assignment_inclusive_lf=[lo,hi]));assignment+='END COMPLETE MATHEMATICAL BODY '+label+'\n'
for e in index:
    lo,hi=e['assignment_inclusive_lf'];assert assignment.splitlines()[lo-1:hi]==Path(e['source']).read_text().splitlines()
(C/'mathematical-data-bindings.json').write_text(json.dumps(index,indent=2)+'\n')
(C/'input.json').write_text(json.dumps(dict(task=json.loads((C/'task.json').read_text()),notes=[],assignment=assignment),ensure_ascii=False,indent=2)+'\n')
s=json.loads((old/'settings.json').read_text());s['codex']['workspace']=str(C/'artifacts');s['usagePrefix']='catalogue-20261003/r205/P16.4-actual-formal-FS-all-genus-inverse'
assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
(C/'settings.json').write_text(json.dumps(s,indent=2)+'\n')
f=dict(prepared_utc=datetime.now(timezone.utc).isoformat(),round=205,atom='P16.4',directory=str(C),prepared_only=True,
       task_sha256=sha(C/'task.json'),original_task_sha256=sha(C/'original-task.json'),input_sha256=sha(C/'input.json'),input_bytes=(C/'input.json').stat().st_size,
       settings_sha256=sha(C/'settings.json'),only_complete_grants=['O217','D214','N220','T171','Q222','C218','G227','M257'],all_grant_clarifications_unchanged=True,
       complete_mathematical_units=len(index),private_primary_packet_bindings_sha256=sha(pb),private_primary_packet_files=len(primary),
       route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,
       material_FAIL198_and_failed250_preserved=True,new265_267_268_are_unreviewed_data=True,
       original_closed=False,protected_editor_unchanged=True,no_private_active_output_read=True,no_hot_feedback=True,reserved_output_continuation=269)
(C/'freeze.json').write_text(json.dumps(f,indent=2)+'\n');print(json.dumps(f,indent=2))
