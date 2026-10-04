#!/usr/bin/env python3
"""Rebuild the proof, canonical notes, twice-compiled PDF and local audits."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,subprocess,sys,shutil
from native_note_texts import TEXTS

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run(args,log):
    r=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    Path(log).write_text(r.stdout)
    commands.append({'argv':args,'returncode':r.returncode,'log':log})
    if r.returncode:
        print(r.stdout[-6000:])
        raise RuntimeError(f'Failed command; see {log}')
    return r.stdout

commands=[]
stamp=datetime.now(timezone.utc).isoformat()
run([sys.executable,'verify_sources.py'],'source-check.log')
run([sys.executable,'coefficient_check.py'],'coefficient-check.log')
proof_parts=[Path(f'n{i}.md').read_text() for i in range(1,5)]
front='# P15.1: minimum auxiliary references on a common genuine finite-energy domain\n\n'
front+='Authoritative single-worker research draft, 4 October 2026. Status: partial; original atom remains open.\n\n'
proof=front+'\n\n'.join(proof_parts)
Path('proof-body.md').write_text(proof)
Path('P15.1-argument.md').write_text(proof+'\n\n'+Path('source-annex.md').read_text())

metadata=[
 ('n1','Reconstructed bounded actual-type energy and exactly scoped foundations; no prior proof or review verdict is assumed.',
  'For every connected compact Kähler n-fold, pseudoeffective zero-volume class and actual theta-psh reference, proves form-independent actual degree d<n, mixed degree>d vanishing, bounded cocycle/concavity, class-polynomial leading energy and representative/gauge invariance. Exact BEGZ, DDNL, Vu, DGMS and capacity hypotheses are stated, source convention and defects checked. This reconstruction is supporting material, not original-atom closure.',[]),
 ('n2','Proves auxiliary-independent full-mass and genuine F1 domains for a fixed actual type, with full finite-energy truncation/cocycle reconstruction.',
  'Scalar DDNL deficits against omega1^j(A omega0-omega1)^(m-j) are nonnegative and sum to zero, proving common full mass across all auxiliary forms/classes, including d=0. Positive fixed-form comparison gives common joint linear finiteness. Convexity yields all mixed full masses and mixed-weight integrability; exact locality plus equal mass yields truncation identities, finite energy equivalence, decreasing continuity, concavity, unbounded cocycle, anchor and gauge invariance. The domain contains an explicit unbounded P1xP1 potential. No uncontrolled moving-form perturbation extension is made.',['n1']),
 ('n3','Proves coefficientwise polynomial extension and the exact finite-dimensional minimum energy-family reference on the entire common F1 domain.',
  'Finitely many Kähler powers span Sym^m H^(1,1), giving unisolvent evaluations. Finite truncation values at those classes force coefficientwise convergence for every F1 potential. Explicit mixed integral functionals are representative independent, and all unbounded functionals span exactly the bounded S. Two Kähler references give every anchored F1 energy equally iff their m-powers agree in Q=Sym^m V/Ann(S). Constants retain the positive raw-mass polynomial; bounded-equivalent anchors and theta gauges preserve S/K/domain. Universal factorization, quotient topology and decreasing coefficient continuity are proved. This is family-relative minimality, not a universal geometric classification or lower-dimensional carrier theorem.',['n1','n2']),
 ('n4','Reconstructs the same-class unbounded concentration counterexample, records actual-degree/class-volume mismatch, and leaves original P15.1 partial.',
  'On P1xP1 a full degree-one F1 potential with radial exponent 0<a<1/2 has finite full relative top energy at every positive perturbation. Smooth fixed-class auxiliary bump forms at radius exp(-epsilon^(-2/a)) force the rescaled top energy to minus infinity, while a fixed form yields the finite degree-one value. Thus n3 quotient continuity cannot imply the refuted joint perturbation assertion. A divisor reference in the same nef class has actual d=0 although the numerical dimension is one, and actual versus class-volume leading exponents differ. Full original path/minimum-reference closure remains unproved. Audit records source pins, exact finite diagnostics and twice-compiled document as observations, not mathematical certification.',['n1','n2','n3'])
]
notes=[dict(id=i,summary=s,detailedSummary=d,text=t,support=support)
       for (i,s,d,support),t in zip(metadata,TEXTS)]
Path('notes.json').write_text(json.dumps({'notes':notes,'candidate':False},ensure_ascii=False,indent=2)+'\n')

gaps=[
 'Original P15.1 remains open: the proved minimum is relative to a prescribed actual bounded type and this particular common F1 energy family, not an independently geometric universal minimum reference for every zero-volume theory.',
 'The unrestricted unbounded class-convergent moving-representative leading perturbation assertion is false by the reconstructed analytic concentration example; general moving unbounded-potential or joint limits require a separate valid prescription and proof.',
 'Degree-d finite joint energy has not here been proved to control all lower-degree weighted perturbation coefficients, even for arbitrary fixed forms and reference types; no unrestricted unbounded path/differential calculus or increasing continuity is claimed.',
 'The leading scale uses actual-current mass coefficients, not a general leading class-volume coefficient theorem or an identification of actual degree with class numerical dimension.',
 'The carrier is explicitly X of dimension n with product bidegree (d,d); no geometric d-dimensional carrier or general geometric/factorwise kernel classification is constructed. P15.2/P15.3 and optional d=0 rigidity are not investigated.'
]
status=dict(id='P15.1',status='partial',exact_result='For every actual reference in a pseudoeffective zero-volume class on connected smooth compact Kähler X, the degree-d full-mass and joint linear finite-energy domains are common to all auxiliary Kähler classes/forms. On this genuine F1 domain, finite truncation/cocycle energies extend coefficientwise to homogeneous degree-(n-d) class polynomials. Their functional span equals the bounded-type span, giving the exact necessary/sufficient minimum energy-family reference q(lambda^(n-d)) in Sym^(n-d)H^(1,1)/Ann(S), retaining raw mass and compatible with same-type anchors, theta gauge and decreasing coefficient continuity. The uncontrolled unbounded moving-form perturbation assertion remains false; original closure is not claimed.',proof_file='P15.1-argument.md',concrete_gaps=gaps)
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
Path('status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')

author=dict(recorded_utc=stamp,requested_model='native Codex gpt-6.1-sol',requested_reasoning='xhigh',
            backend_attestation='Not exposed; exact requested backend/effort not independently authenticated.',
            additional_models=False,subagents=False,independent_worker_feedback=False,
            old_artifact_writes=False,network=False,installs=False,external_messages=False,
            auth_proxy_CA_changes=False,HOME_CODEX_HOME_changes=False,SQL_runtime_edits=False,
            heavy_computation=False,supervised_heavy_compute_needed=False,
            managed_runtime_skill_read=True,environment_status_tool='Unavailable',
            proof_status='Unverified research draft; no literature-priority or independent certification claim.')
Path('author-audit.json').write_text(json.dumps(author,indent=2)+'\n')
research=dict(recorded_utc=stamp,target='P15.1 only',supplied_proposal_status='UNVERIFIED, independently reconstructed',
              proved_proposal_items=[1,2,3],operator_proposal_item_4='Outside this P15.1-only implementation',
              optional_degree_zero_rigidity='No claim',substantive_new_content=['common all-auxiliary full-mass domain',
              'common genuine finite-linear-energy domain','coefficientwise unbounded polynomial extension',
              'same bounded/unbounded functional span and necessary/sufficient whole-domain reference'],
              supporting_reconstruction=['bounded primitive and representative invariance','exact truncation identity',
              'finite-energy cocycle and decreasing continuity','analytic concentration obstruction'],
              limitations=gaps,essential_external_theorems_exactly_stated_in='n1.md',
              complete_literal_primary_bodies_in='P15.1-argument.md',
              source_defects=['GZ Proposition 3.7 is bounded: use 3.6,3.10,Corollary 3.8 with truncation',
              'Vu v3 Theorem 3.3 product factors are bounded: truncate and exhaust finite loci',
              'Cutoff nonzero locus, not necessarily closed support, lies in strict comparison set',
              'Intrinsic Dirichlet identity has mandatory 1/2; source repeated missing factors preserved',
              'Unused Vu v1 m/n, subscripts and printed Cauchy-Schwarz defects preserved'],
              proof_methods='Analytic literature applications plus full new algebra/domain proofs; no numerical proof of analytic claims.')
Path('research-audit.json').write_text(json.dumps(research,ensure_ascii=False,indent=2)+'\n')

versions={}
for cmd in [['python','--version'],['pandoc','--version'],['pdflatex','--version'],['pdftotext','-v']]:
    r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    versions[cmd[0]]=r.stdout.splitlines()[:3]
run(['pandoc','proof-body.md','--from=markdown-superscript+tex_math_single_backslash','--to=latex','--standalone',
     '--include-in-header=proof-header.tex','--metadata=title:P15.1: minimum references on a common finite-energy domain',
     '--metadata=date:4 October 2026','--output=P15.1-partial.tex'],'pandoc.log')
for i in (1,2):
    run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P15.1-partial.tex'],f'pdflatex-pass{i}.log')
run(['pdftotext','P15.1-partial.pdf','P15.1-partial-extracted.txt'],'pdftotext.log')
extracted=Path('P15.1-partial-extracted.txt').read_text()
checks={needle:needle in extracted for needle in ['n1. Foundations','n2. One full-mass domain','n3. Coefficientwise extension',
                                                   'n4. Analytic limitation','unisolvent','Candidate is false']}
assert all(checks.values()),checks
audit=json.loads(Path('source-audit.json').read_text())
assert all(x['pin_matches'] and x['supplied_literal_present'] for x in audit['units'])
assert Path('input.json').read_bytes()==Path('input-original.json').read_bytes()
assert json.loads(Path('input.json').read_text())['assignment']==Path('assignment-original.txt').read_text()
assert all(set(note['support']).issubset({x['id'] for x in notes[:i]}) for i,note in enumerate(notes))
report=dict(recorded_utc=stamp,platform=platform.platform(),python_executable=sys.executable,
            working_directory=str(Path.cwd()),versions=versions,commands=commands,
            source_pins_matching=len(audit['units']),finite_checks=json.loads(Path('coefficient-check.json').read_text()),
            pdflatex_successful_passes=2,pdf_text_structure_checks=checks,input_preserved=True,
            sha256={str(p):sha(p) for p in sorted(Path('.').glob('*')) if p.is_file() and p.name!='build-audit.json'},
            limitations='Compilation, hashes and exact finite diagnostics do not certify analytic correctness.')
Path('build-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Build complete: 24 source pins, finite exact diagnostics, two successful pdflatex passes, all PDF structure checks passed. Original P15.1 partial; candidate=false.')
