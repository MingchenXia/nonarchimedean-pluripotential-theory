from pathlib import Path
import datetime, hashlib, json

ROOT = Path('/workspace/research')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def validate(name, expected_counts, publish, assessment):
    p = ROOT/'campaigns/round-05'/name
    campaign = json.loads((p/'run.json').read_text())['campaign']
    r = campaign['result']
    f = json.loads((p/'freeze.json').read_text())
    b = json.loads((p/'source-artifact-binding.json').read_text())
    assert campaign['status'] == 'completed' and r['verdict'] == 'PASS'
    assert (len(r['premises']),len(r['passages'])) == expected_counts
    assert sha(p/'argument.md') == f['argument_sha256'] == b['review_argument_sha256']
    assert sha(Path(b['source_tex'])) == f['source_tex_sha256'] == b['source_tex_sha256']
    assert sha(Path(b['declared_proof_file'])) == f['declared_proof_sha256'] == b['declared_proof_sha256']
    if 'main_argument' in b:
        assert sha(Path(b['main_argument'])) == f['main_argument_sha256'] == b['main_argument_sha256']
    for passage in r['passages']:
        assert type(passage['premise']) is int
        assert 0 <= passage['premise'] < len(r['premises'])
        assert passage['statement'] == r['premises'][passage['premise']]
    a = dict(recorded_utc=now,run_sha256=sha(p/'run.json'),verdict='PASS',
             full_report_premises_and_passages_read=True,bindings_validated=True,
             publish_exact_scope=publish,premises=len(r['premises']),passages=len(r['passages']),
             frozen_argument_sha256=f['argument_sha256'],source_tex_sha256=b['source_tex_sha256'],
             full_original_atom_solved=False,assessment=assessment)
    (p/'review-read-attestation.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
    return p,b

p05,b05 = validate('P05.2-real-universal-embedded-evidence-review',(6,8),True,
    'Root read the complete report and all six premises / eight passages, including the reconstructed full n100 positive proof. Accept only the all-real-reference regularizability-and-contact criterion on the stated direct-lattice rank-one balanced ray-star products times complete affine space, on finite rational spatial domains. The new finite local-support and exact rational-reference decomposition remove the former ambient-extension hypothesis. Complete negative defects have PAPC envelopes; no whole-pair negative regularity, arbitrary balanced-pair classification, literal integral-slope classification, formal verification or priority certification is inferred. Original P05.2 remains open.')
p06,b06 = validate('P06.2-finite-galois-ascent-continuation-review',(9,10),True,
    'Root read the complete principal report and all nine premises / ten passages. Accept only Theorems A/B and Corollary C at their explicit quadratic Galois unit-distance hypothesis, the ordinary zero-Hessian equivalence on good separated strict boundaryless pure analytic curves including singular/nonreduced curves, finite towers of such stages, and the separately proved finite-separable reverse implication. The scalar polynomial lemma in larger dimension does not establish higher-bidegree form ascent. Source scopes are smooth Euclidean coefficient functions, generic coherent-module lengths (O_X for structural multiplicity), and compact F with finite cover for fixed-index compact cutoffs. No inseparable support note is needed. General scalar ascent, ordinary two-sign regularization and original P06.2 recognition remain open.')
supp,_ = validate('P06.2-finite-galois-ascent-embedded-review',(23,46),False,
    'Root read the full supplemental report and all 23 premises / 46 bound passages. Native PASS is preserved verbatim. Its premise at zero-based index 10 overstates fixed-cover-index compact-support cutoffs for arbitrary countable-at-infinity closed F; a one-set cover of noncompact F shows this generality cannot be certified. This broad premise is unused by the main quadratic theorem, which uses compact F and finite covers only. Publication is governed by the independently reconstructed principal 9-premise / 10-passage review and the explicit compact-specialization source clarification. The appended inseparable theorem is supplemental and is not a dependency of the quadratic proof. Do not treat this supplemental receipt as certifying every broad premise.')

def edits_for(p,b):
    original = Path(b['source_tex']).read_text()
    edits=[]
    def add(before,after,reason,count=1):
        assert original.count(before) == count,repr(before)
        edits.append(dict(before=before,after=after,reason=reason,expected_occurrences=count))
    return original,edits,add

s,e,add = edits_for(p05,b05)
add('Unverified P05.2 research draft','P05.2 reviewed partial result','Publication status metadata',2)
add('addition of their rational-domain modifications. No independent review,\nformal verification, or priority claim is made for this draft.',
    'addition of their rational-domain modifications. The exact proof and\nits complete supporting argument received the source-aware independent\nPASS accompanying this paper. The original classification remains open;\nno formal verification or priority certification is claimed.',
    'Record exact-scope independent review without closing the original atom')
add('Definitions 2.18--2.20 use saturated tangent lattices',
    'Definition 2.1 fixes saturated tangent lattices; Definitions 2.18--2.20 use',
    'Locate the tangent lattice definition precisely')
add('class. Proposition 3.22 and Definition 3.23 describe real\nregularizability here by uniform decreasing real PAPC approximation. In',
    'class. We use the real analogue of Proposition 3.22 and Definition\n3.23, with real regularizability explicitly defined here by uniform\ndecreasing real PAPC approximation. In',
    'Real coefficient regularizability is defined and proved here, not imported from the literal source category')
add('\\texttt{sources/prior-*}; none is a supporting theorem. The running\nreview\'s SQLite files are not accessed or mutated, and no later PASS is\nused for changed bytes.',
    '\\texttt{sources/prior-*}; none is a supporting theorem. The present\nexact-scope review reconstructed the full unchanged positive supporting\nproof embedded in its argument, together with the new converse. Both\narguments and the complete review receipt accompany this paper.',
    'Replace launch chronology with accessible full proof provenance')
add('candidate is \\textbf{false}. The new proof has an author self-audit\nonly; the old exact-scope PASS is not a certificate for it.',
    'candidate is \\textbf{false}. The new proof has its own source-aware\nindependent PASS; the older exact-scope receipt is not substituted for\nthat review. The original classification remains open.',
    'Update independently reviewed partial status')
add('in this workspace. It executes small finite diagnostics, generates',
    'in the preserved worker workspace\n\\path{/workspace/research/campaigns/round-05/P05.2-real-reference-universal-continuation/artifacts/codex-o8EmFf}.\nIt executes small finite diagnostics, generates',
    'Give the actual reproduction location')
(p05/'publication-edits.json').write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')

s,e,add = edits_for(p06,b06)
add('Author-audited research draft','P06.2 reviewed partial result','Publication status metadata',2)
add('This packet proves a new special-case scalar-ascent gate. It does not\nsolve P06.2, does not give a counterexample, and does not assert an\nindependent review, formal verification, or priority claim. All new\nmathematical claims are unverified author drafts.',
    'This paper proves a special-case scalar-ascent theorem. Its exact proof\nreceived the source-aware independent PASS accompanying the paper. The\noriginal P06.2 recognition problem remains open. No formal verification\nor priority certification is claimed.',
    'Update reviewed scope and retain original-atom limitations')
add('CLD Corollary 15.1.2 states the local smooth-function criterion using a',
    'CLD Corollary 15.1.2, together with Proposition 15.1.1(b) and the\ncoefficient definitions, gives the local smooth-function criterion using a',
    'Make the Euclidean smooth-coefficient source dependency explicit')
add('CLD §15.2.2 states that a good topologically separated analytic space is\nlocally holomorphically separated. Corollary 15.2.9 states: for a\nlocally holomorphically separated analytic space, a closed subset \\(F\\)\ncountable at infinity (in particular compact), and an ordinary open\ncover \\((U_i)\\) of \\(F\\), there is a locally finite family of\nnonnegative smooth \\(\\theta_i\\), each of compact support contained in\n\\(U_i\\), whose sum is one near \\(F\\). We apply it only to finite covers\nof compact sets. This requires no global paracompactness.',
    'CLD §15.2.2 states that a good topologically separated analytic space is\nlocally holomorphically separated. The compact-set specialization of\nCorollary 15.2.9 and its supporting cutoff construction gives, for a\ncompact subset \\(F\\) and a finite ordinary open cover \\((U_i)\\) of\n\\(F\\), nonnegative smooth \\(\\theta_i\\), each with compact support\ncontained in \\(U_i\\), whose sum is one near \\(F\\). Only this\ncompact-set, finite-cover statement is used. It requires no global\nparacompactness.',
    'Restrict the citation to the compact specialization actually proved and used')
add('13.2.8 computes generic lengths under scalar extension by tensoring a\nlength filtration; no reduction is silently taken in that argument.',
    '13.2.8 computes the generic lengths of a coherent module under scalar\nextension by tensoring a length filtration; the structural multiplicity\nuses \\(F=\\mathcal O_X\\). No reduction is silently taken in that\nargument.',
    'Identify the coherent module underlying structural generic lengths')
add('Run \\texttt{python\\ build-and-check.py} in this directory to re-extract',
    'Run \\texttt{python\\ build-and-check.py} in the preserved worker workspace\n\\path{/workspace/research/campaigns/round-05/P06.2-finite-galois-ascent-continuation/artifacts/codex-9cNAFU}\nto re-extract',
    'Give the actual reproduction location')
add('Execution success checks artifact integrity, exact finite identities,\nand typesetting only. It does not establish correctness of the\nmathematical draft. The author self-audit is not independent review.',
    'Execution success checks artifact integrity, exact finite identities,\nand typesetting. The unchanged frozen argument and complete principal\nreview receipt accompany this independently reviewed partial paper. The\nreceipt certifies the compact cutoff specialization used in the proof;\nan overbroad, unused cutoff statement in a separate supplemental review\nis recorded as a caveat in the publication records. Independent\nsame-model review is not formal verification. The native editor did not\nreturn; built-in compilation is unverified. Two installed pdfLaTeX\npasses check the standalone publication source.',
    'State actual review evidence, supplemental limitation and compilation provenance')
(p06/'publication-edits.json').write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')

active=json.loads((ROOT/'active-work.json').read_text())
for c in active['continuations']:
    if c['directory'].endswith('P05.2-real-reference-universal-continuation'):
        c['state']='Exact all-real-reference product PASS fully read and bound; publication edits prepared; original classification open'
        c['review_state']='PASS 6 premises / 8 passages; complete supporting proof reconstructed'
    if c['directory'].endswith('P06.2-finite-galois-ascent-continuation'):
        c['state']='Restricted quadratic curve theorem principal PASS fully read and bound; compact source clarification prepared; original open'
        c['review_state']='Principal PASS 9 premises / 10 passages; supplemental broad unused cutoff premise caveat preserved'
    if c['directory'].endswith('P05.2-graph-cylinder-continuation'):
        c['state']='Draft completed, candidate=false, full proof and author audit read; exact embedded review running; original open'
        c['worker_workspace']=str(ROOT/'campaigns/round-06/P05.2-graph-cylinder-continuation/artifacts/codex-7OSCU6')
        c['argument_sha256']='9a0fb60210ba33ae3aa7e50ccd0b305e3c07e3b7ae506057e7bd74d52f3dc772'
active['updated_utc']=now
(ROOT/'active-work.json').write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'publication_reviews':[str(p05),str(p06)],'supplemental_review_preserved_with_caveat':str(supp)}))
