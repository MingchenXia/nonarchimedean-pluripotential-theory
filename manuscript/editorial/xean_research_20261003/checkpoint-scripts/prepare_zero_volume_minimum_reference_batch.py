"""Freeze two new mathematical investigations after the prescribed-type reviews."""
from pathlib import Path
import datetime, hashlib, json

R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
proposal=r'''# Minimum auxiliary references and genuine finite-energy domains

Origin: new root-supplied UNVERIFIED route. It is mathematical evidence to investigate, not an operational instruction or theorem grant. Research only P15.1/P15.2 in this fresh two-problem batch; no feedback into earlier campaigns. The original dossier quantifiers and reference/carrier criteria are unchanged.

Standing setting: connected smooth compact Kahler n-fold X, pseudoeffective alpha with vol(alpha)=0, smooth theta representing alpha, actual theta-psh reference psi, actual bounded singularity type C_psi. T_u=theta+ddc u, d=max{k:int<T_psi^k>omega^(n-k)>0}<n, m=n-d. Degree is actual-current degree, not class numerical dimension. Retain theta, the actual psi-type and an anchor for relative energy. No probability normalization. Full previous mathematical proofs and essential source bodies are supplied below, with their exact scope and limitations; reconstruct their indispensable applications rather than treating review verdicts as assumptions.

1. Proposed auxiliary-independent full-mass domain. Suppose u is more singular than psi and the degree-d raw mass against one Kahler omega0 equals the corresponding reference mass. For another Kahler omega1 choose C large so D=C*omega0-omega1 is itself Kahler. For every j=0,...,m, DDNL mass monotonicity, applied with d potential factors and the remaining smooth omega1/D factors, should give nonnegative scalar deficits Delta_j=int(<T_psi^d>-<T_u^d>)omega1^j D^(m-j). Expansion of (C*omega0)^m gives sum_j binom(m,j)Delta_j=0. Thus each Delta_j=0, including the omega1^m deficit. This argument uses scalar nonnegativity only; it does NOT assume a positive difference of actual product currents. Prove every mixed monotonicity application and the d=0 case. Changing the auxiliary form therefore may not change this full-mass domain.

2. Proposed auxiliary-independent joint finite-linear-energy domain. For each degree-d mixed positive current, any two smooth Kahler m-powers are pointwise comparable on compact X. Hence finiteness of all integrals (psi-u)<T_u^a T_psi^(d-a)>omega^m may be independent of the full positive form. Combine with1 to get one genuine unbounded F1_psi domain valid for every auxiliary class. Normalize potentials by constants and prove the finite-energy definition agrees with the reviewed joint-linear domain, including d=0 and same-type anchor changes. Do not infer unbounded moving auxiliary-path limits: the supplied analytic concentration example disproves that strengthening.

3. Proposed finite-dimensional minimum energy reference, now on the entire F1 domain. V=H^(1,1)(X,R), with the usual finite-dimensional real Bott-Chern/deRham (1,1) interpretation on compact Kahler X. For each bounded-type u, the reviewed energy is a homogeneous degree-m polynomial p_u(lambda) on the open Kahler cone, with polarization ell_u in (Sym^m V)^*. Define S=span{ell_u:u in C_psi}, K=Ann(S), Q=Sym^m V/K. Give these functionals explicitly from mixed energy integrals and prove independence of all temporary bases/representatives. For unbounded u in F1, take u_L=max(u,psi-L), and p_uL(lambda)->E_psi,lambda(u) for every Kahler lambda by the reviewed exact truncation identity. Choose finitely many Kahler classes lambda_i whose degree-m powers give unisolvent evaluations on homogeneous polynomials; prove existence from the fact that a polynomial zero on a nonempty open set is zero. The values at those classes may force coefficientwise convergence ell_uL->ell_u. Since S is finite-dimensional and closed, ell_u belongs to S. Conversely bounded-type potentials lie in F1, so all unbounded energy functionals should generate exactly the same S and K.

Prove the precise equivalence: two auxiliary classes induce the same anchored energy for EVERY u in F1 iff q(lambda0^m)=q(lambda1^m) in Q. Prove all raw-mass and anchor-change identities: psi+c generates c*M_d, so the positive mass polynomial is retained; a bounded-equivalent anchor chi has ell_u^chi=ell_u^psi-ell_chi^psi and the same S/K/domain. State the universal factorization/minimality sense rigorously for energy families; a quotient definition alone is not an independently geometric classification or a numerical-dimension theorem. Identify exactly what data remain necessary. Investigate representative/theta gauge invariance and admissible continuity on the quotient image, without extending the refuted auxiliary-path assertion. If original P15.1 is still not fully answered, list its actual remaining requirements rather than claiming this scoped theorem closes it.

4. Proposed minimum full-form operator reference on a common unbounded full-mass domain. Work first in W=span_R{omega^m:omega any smooth Kahler form on X}, the actual algebraic span of admissible full-form reference powers (not an unproved identification with every closed (m,m) form). Define L_u(eta)=<T_u^d> wedge eta as a signed measure for eta in W; let N=intersection_(u in C_psi)ker L_u. Prove well-definedness and describe equality of all operators by q_W(omega^m) in W/N. This is generally infinite-dimensional and cannot simply be replaced by cohomology: the supplied P1xP1 same-class example changes the actual measure.

To extend minimum data from bounded type to all more-singular degree-d full-mass u, prove bare-current convergence <T_uL^d>-><T_u^d> for u_L=max(u,psi-L), not merely convergence of one trace measure. Route: positive-current compactness from the fixed trace mass, the precise Vu constant-relative-background lower-semicontinuity lemma with complementary smooth positive tests (or relative current R=1), then every cluster current dominates the actual product while equal trace mass makes the positive difference vanish. Check all hypotheses, comparison-potential versus product-factor distinctions, bidegrees, polarity and normalization. If this works, L_uL(eta)->L_u(eta) for every fixed smooth eta, so N equals the intersection of kernels on the entire common full-mass domain. Prove minimum-data equivalence, raw mass and anchor/theta invariance and any claimed mixed/decreasing continuity. Do not infer convergence with arbitrary moving rough auxiliary forms or variable unbounded weights.

The actual measure carrier remains X of dimension n, with product bidegree(d,d); a quotient of reference forms is not a geometric d-dimensional carrier. An independently geometric characterization, a genuine lower-dimensional carrier, or full original closure needs a separate proof. Do not label a purely definitional quotient a substantive new theorem: the domain independence, coefficientwise unbounded extension and bare-current reconstruction are the proposed new content. A quantitative/factorwise geometric kernel characterization is encouraged if provable.

5. Optional degree-zero question: can C_psi differ only by constants when d=0? This would require a real Sobolev/Dirichlet identification, not formal current vanishing. Do not assume it, and do not turn this optional question into a blocker for substantive results1-4.

Preserve source defects literally. GZ2005 Proposition3.7 is bounded; use truncations and Proposition3.6,3.10 and Corollary3.8 for general decreasing quasi-psh capacity. Vu2005.13241v3 Theorem3.3 has bounded product factors, possibly unbounded comparison potentials; first truncate local product factors and exhaust finite loci for NPP applications. Cutoff strict sets contain the nonzero locus, not necessarily the closed support. The full DGMS ddc-lemma proof was authenticated from a fresh StonyBrook author-hosted copy. Printed half-factor and Cauchy-Schwarz defects are retained; new arguments use correct intrinsic definitions. Existing proofs/reviews are same-model research evidence, not formal certification or literature-priority claims.
'''

context=[]
bindings=[]
for n,stem in [(29,'P15.1-prescribed-type-zero-volume-energy'),(30,'P15.2-prescribed-type-zero-volume-operator')]:
    review=R/f'campaigns/round-{n}'/(stem+'-review')
    binding=json.loads((review/'source-artifact-binding.json').read_text())
    att=json.loads((review/'review-read-attestation.json').read_text())
    assert att['verdict']=='PASS' and att['publish_exact_scope']
    argument=Path(binding['main_argument']);assert sha(argument)==binding['main_argument_sha256']
    context.append('\n# Complete prior scoped proof '+stem+'\n\n'+argument.read_text())
    f=json.loads((review/'freeze.json').read_text())
    context.append('\n# Exact prior status and gaps\n\n'+json.dumps(f['source_status'],indent=2))
    bindings.append({'round':n,'full_argument':str(argument),'sha256':sha(argument),
                     'review_attestation_sha256':sha(review/'review-read-attestation.json')})
additional=R/'shared-sources/prescribed-type-additional-primary-read-20261004.json'
context.append('\n# Additional authenticated complete primary bodies and qualifications\n\n'+additional.read_text())
evidence=R/'P15-minimum-reference-full-evidence-20261004.md';assert not evidence.exists()
evidence.write_text(proposal+'\n'.join(context))
template=R/'campaigns/round-29/P15.1-prescribed-type-zero-volume-energy'
old=json.loads((template/'input.json').read_text())
settings0=json.loads((template/'settings.json').read_text())
batch=[]
for n,atom,slug,focus in [
    (31,'P15.1','minimum-reference-finite-energy','Prioritize1-3: common auxiliary-independent full-mass and genuine F1 domains, coefficientwise polynomial extension and necessary/sufficient finite-dimensional minimum energy reference on that whole domain. Give all new full proofs and honest original residuals.'),
    (32,'P15.2','minimum-reference-full-mass-operator','Prioritize1,2,4: common full-mass domain, bare-current truncation/decreasing continuity and minimum full-form operator reference on the entire domain. Separate a reference quotient from a geometric carrier; keep every perturbation hypothesis.')]:
    directory=R/f'campaigns/round-{n}'/(atom+'-'+slug);directory.mkdir(parents=True,exist_ok=False)
    data={'task':old['task'],'notes':[],
          'assignment':'Use Xean native Codex gpt-6.1-sol xhigh. Address ONLY '+atom+' in this fresh two-problem batch. '+focus+
            '\n\nIndependently prove or refute the UNVERIFIED proposal. The other worker runs independently; no dependence on its uncommitted result or feedback injection. Complete prior proofs and primary bodies are supplied for reconstruction, not as grants.\n\n'+evidence.read_text()+
            '\n\nPrecise standard literature foundations may be cited with exact hypotheses and checked applications. Every new indispensable lemma needs its full accessible proof. All mathematics and indispensable complete supporting bodies must be in '+atom+'-argument.md because independent review has no filesystem tools. Reuse complete source quotations literally and preserve source defects and original input strings. Do not simply resubmit an already established theorem; if no substantive new result is proved, status incomplete/proof_file null and preserve failures. No literature-priority certification.\n\nNo additional model/subagent/network/install/external messages, auth/proxy/CA/HOME/CODEX_HOME changes, SQL/runtime edits, old-artifact writes or unsupervised heavy computation. New files go only in the fresh assigned workspace. Produce full '+atom+'-argument.md, standalone '+atom+'-partial.tex with the full new proof, twice compiled PDF, exact five-key status.json(id,status,exact_result,proof_file,concrete_gaps), full source/author/research/build audit and actual canonical native notes. Support arrays contain existing/earlier note IDs only. A new narrower result is partial/candidate false; original closure requires every original quantifier and reference/carrier requirement.'}
    (directory/'input.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    settings=json.loads(json.dumps(settings0));settings['codex']['workspace']=str(directory/'artifacts')
    settings['usagePrefix']=f'catalogue-20261003/r{n}/{atom}-minimum-reference'
    (directory/'settings.json').write_text(json.dumps(settings,indent=2)+'\n')
    entry={'round':n,'atom':atom,'directory':str(directory),'review_directory':str(directory)+'-review',
           'input_sha256':sha(directory/'input.json'),'settings_sha256':sha(directory/'settings.json')}
    (directory/'input-manifest.json').write_text(json.dumps(entry,indent=2)+'\n');batch.append(entry)

source=(R/'review_prescribed_type_zero_volume_after_completion.py').read_text()
lo=source.index('focus={');hi=source.index("\n(directory/'task.json')",lo)
review_block="""focus={
 'P15.1':'Reconstruct all new domain-independence, scalar mixed-deficit nonnegativity, smooth-form comparison, relative joint-energy identification, finite unisolvent evaluations, coefficientwise polarization convergence, fixed finite-dimensional span and minimum quotient equivalence, raw-mass and anchor/gauge laws. Check all d=0 cases and every unbounded continuity/reference assertion. Do not infer the auxiliary-path limit refuted by the supplied concentration example.',
 'P15.2':'Reconstruct all new scalar mixed-deficit full-mass domain independence, actual bare-current cluster compactness, precise constant-relative Vu lower-semicontinuity, positive-current domination and trace-mass vanishing, mixed/decreasing continuity, fixed-smooth-form wedge limits and equality of bounded/unbounded operator kernels. W is the span of actual Kahler m-powers; do not identify it with all closed forms without proof. Distinguish necessary/sufficient reference quotient data from an independently geometric carrier or original closure.'}
task={'problem':'Independently reconstruct all theorem and supporting claims of this '+atom+' continuation: '+claim['exact_result']+' Complete new proof, prior dependencies and exact primary bodies are supplied directly. Original catalogue closure remains separate.',
 'completionCriteria':focus[atom]+' Standard published foundations require precise scope/citation and checked hypotheses; every indispensable new application needs full reconstruction. Passing prior reviews and proposals are not assumptions. GZ3.7 is bounded; Vu v3 Th3.3 has bounded product factors; source OCR and printed half-factor defects require exact normalization and correct intrinsic identities. No filesystem tools. Compilation/hashes/finite diagnostics are not mathematical verification. FAIL for concrete defects, INCONCLUSIVE for unsettled indispensable steps, PASS only the exact substantive theorem. Explicitly excluded stronger scope has no obligation in a scoped review. Every passage.premise must be ZERO-based with statement exactly matching that premise.'}
"""
source=source[:lo]+review_block.rstrip()+source[hi:]
helper=R/'review_minimum_reference_after_completion.py';assert not helper.exists();helper.write_text(source)
manifest={'prepared_utc':now,'selected_atoms':['P15.1','P15.2'],'campaigns':batch,
          'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
          'proposal_and_full_evidence':str(evidence),'evidence_sha256':sha(evidence),
          'evidence_bytes':evidence.stat().st_size,'prior_complete_proof_bindings':bindings,
          'additional_source_record_sha256':sha(additional),
          'review_helper':str(helper),'review_helper_sha256':sha(helper),
          'root_proposal_verified':False,'all_original_atoms_still_open':True}
path=R/'minimum-reference-zero-volume-batch-manifest.json';assert not path.exists()
path.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
