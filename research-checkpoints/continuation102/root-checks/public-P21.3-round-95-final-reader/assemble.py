#!/usr/bin/env python3
import hashlib,json,pathlib,re
R=pathlib.Path(__file__).resolve().parent
m=json.loads((R/'source-manifest.json').read_text()); byid={u['id']:u for u in m['units']}
core=(R/'P21.3-core.md').read_text()
blocks=re.findall(r'\*\*Premise (\d+):.*?(?=\n\*\*Premise \d+:|\nWe use bounded convergence)',core,re.S)
chunks=re.findall(r'\*\*Premise \d+:.*?(?=\n\*\*Premise \d+:|\nWe use bounded convergence)',core,re.S)
assert [int(x) for x in blocks]==list(range(9))
links={
0:['cld-ordinary-domain','cld-analytic-calculus','cld-cutoffs-density'],
1:['cld-generated-psh'],
2:['cld-positive-decomposition','cld-middle-positivity','cld-positive-wedges','cld-face-positive-wedges','cld-geometric-positive-wedges'],
3:['cld-positive-scalar-measures','cld-ordinary-product'],
4:['cld-middle-matrix','cld-current-topology','cld-compact-moment-image','cld-chart-images','cld-face-positivity'],
5:['cld-form-leibniz','cld-current-sheaf','cld-current-differentials','cld-smooth-multiplier'],
6:['cld-analytic-calculus','cld-current-differentials','cld-generic-lengths','cld-top-measures'],
7:['gr-field','gr-pluriharmonic','gr-maximum-proof'],
8:['gr-classical-definition','gr-inclusion','gr-limits-semistable','gjr-field','gjr-weak-harmonic','gjr-strong-current']}
app={0:'Original good separated pure boundaryless X and every ordinary open; no global paracompactness or valuation restriction.',1:'No continuity imposed on predecessors; ordinal exhaustion, USC, bounded final selection and cone operations are freshly proved.',2:'Compact tests on good, hence almost-good, ordinary analytic opens satisfy the theorem support scope. Middle cone is retained.',3:'Only positive coefficient measures and differences used; locally bounded Borel product continuity freshly proved.',4:'Finite moment presentations of actual ordinary test families; middle matrix domination only. Only polyhedrality, not the printed dimension equality in 12.2.4, is used.',5:'Both closedness equations are imposed; identities are ordinary current identities on the original open.',6:'Original calibration retained without nilreduction; actual generic lengths remain.',7:'Only already classical pluriharmonic functions on fixed compact affinoid; GR allows trivial valuation and singular/nonreduced affinoids.',8:'Diagnostic scope only; no recognition, semistable model existence, arbitrary-current lift or compatibility assumed.'}
prem=[]
for i,chunk in enumerate(chunks):
 prem.append({'index':i,'statement':chunk.strip(),'applicability':app[i],'role':'core premise' if i<8 else 'scope diagnostic','passages':[dict({'premise':i},**byid[u]) for u in links[i]]})
(R/'premises.json').write_text(json.dumps(prem,ensure_ascii=False,indent=2)+'\n')
e=['# Literal selected primary evidence\n\nFull sources were not read. Source hashes establish byte provenance, not mathematical correctness. The browser snapshots are not original PDF bytes. All LF intervals below are inclusive and counted using UTF8 decoding and split(\\n).\n']
for p in prem:
 e.append(f'\n## Premise {p["index"]}\n\n{p["statement"]}\n\nApplicability: {p["applicability"]}\n\nLiteral units: '+', '.join(u['id'] for u in p['passages'])+'.\n')
for u in m['units']:
 b=(R/u['path']).read_bytes();assert hashlib.sha256(b).hexdigest()==u['sha256']
 e.append(f'\n## {u["id"]}\n\nPrimary: {u["url"]}.\n\nSource UTF8 LF {u["lf_first"]}--{u["lf_last_inclusive"]}; unit SHA256 `{u["sha256"]}`; source SHA256 `{u.get("source_sha256")}`.\n')
 if u['source']=='gr-web':e.append(f'\nGR numbering refers to LF of this saved literal unit; original public browser numbering is zero-based {u["web_zero_based_line_first"]}--{u["web_zero_based_line_last_inclusive"]}. Original PDF bytes were unavailable.\n')
 e.append('\n```text\n'+b.decode('utf8')+'\n```\n')
ev=''.join(e);(R/'P21.3-primary-evidence.md').write_text(ev)
(R/'P21.3-argument.md').write_text(core+'\n\n# Primary evidence appendix\n\n'+ev)
original=json.loads((R/'input-original.json').read_text())
assert original['notes']==[]
assert json.loads((R/'task-original.json').read_text())==original['task']
assert (R/'assignment-original.txt').read_text()==original['assignment']
freeze={'input-original.json':hashlib.sha256((R/'input-original.json').read_bytes()).hexdigest(),'task-original.json':hashlib.sha256((R/'task-original.json').read_bytes()).hexdigest(),'assignment-original.txt':hashlib.sha256((R/'assignment-original.txt').read_bytes()).hexdigest()}
(R/'input-manifest.json').write_text(json.dumps(freeze,indent=2)+'\n')
status={'id':'P21.3','status':'partial','exact_result':'Locally bounded real generated CLD Psh sections have positive doubly closed ordinary multipliers for every original field, ordinary open and allowed middle-positive doubly closed current; full sheafified ordinal proof and Borel product audit. Also, linear subspaces of classical pluriharmonic functions on a fixed compact affinoid are closed under pointwise convergent nets, with uniform convergence. No universal pair equality or analytic counterexample.','proof_file':'P21.3-argument.md','concrete_gaps':['No construction makes both signs of an arbitrary continuous generated-Psh equal-curvature pair difference generated Psh on a fixed ordinary neighbourhood.','No preservation theorem for general exact signed curvature dependencies against an arbitrary allowed singular ordinary current.','No analytic curve restriction or transcendental scalar-current ascent of the ambient ordinary Hessian equality is proved.','No all-refinement-compatible positive doubly closed regularization/density theorem for arbitrary currents is proved.','No actual analytic admissible pair, current and compact smooth test with a nonzero product difference is constructed.']}
(R/'status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
print(f'Assembled {len(prem)} fully indexed premise records and {len(m["units"])} literal units; P21.3 partial.')
