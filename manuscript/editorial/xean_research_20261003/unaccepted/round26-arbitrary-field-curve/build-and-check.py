#!/usr/bin/env python3
"""Assemble deliverables and record bounded integrity/build observations."""
import hashlib
import json
import platform
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def dump(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

COMMANDS = []
def run(args, log):
    p = subprocess.run(args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    (ROOT / log).write_text(p.stdout)
    COMMANDS.append(dict(argv=args, cwd=str(ROOT), output_file=log, exit_code=p.returncode))
    if p.returncode:
        raise RuntimeError(f'Command failed ({p.returncode}), see {log}: {args}')
    return p.stdout

FIELD_NOTE = r'''Let K be complete and nontrivially valued. Give every finite subfield E of an algebraic closure Kbar its unique extending absolute value. The exact standard foundation is BGR, Non-Archimedean Analysis, 3.2.4/2: a finite algebraic extension of a complete non-Archimedean field has a unique extending absolute value and is complete; no separability hypothesis is needed. This same finite-field result is proved in supplied n701 Section 3.1. Norms agree on intersections and composita, hence define a compatible norm on Kbar. Its completion C is a field: for any nonzero limit a of a_m, eventually |a_m|=|a|>0 and |a_m^-1-a_j^-1|=|a_m-a_j|/(|a_m||a_j|), so inverses converge. C is complete, contains K isometrically, and retains any element of K of nonunit absolute value.

Here is a complete elementary algebraic-closure proof. For monic P(T)=T^d+sum_{i<d} a_i T^i in C[T], let R=max(1,max_i|a_i|). Choose monic P_m in Kbar[T] with coefficient errors at most delta_m=2^(-md) R^(-(d-1)). Every root has norm at most R, since a larger root would give a strictly dominant leading term. Choose b_1 a root of P_1. If b_m is a root of P_m, then |P_{m+1}(b_m)|<=delta_m R^(d-1)=2^(-md). Factoring P_{m+1} into d linear factors in Kbar, at least one root b_{m+1} has |b_{m+1}-b_m|<=2^(-m). The ultrametric inequality makes b_m Cauchy. The limit b in C satisfies P(b)=lim P_m(b_m)=0 by coefficient convergence and the uniform root bound. Every nonconstant polynomial thus has a root (divide by its leading coefficient), so C is algebraically closed. This works with inseparable and repeated roots and in every characteristic.

For any analytic extension L/K, embed Kbar into an algebraic closure Lbar over K: use a maximal partial embedding on intermediate fields, extending by a root of a minimal polynomial if an algebraic element remains. The unique norms on finite K-subfields make it isometric. With F=completion(Lbar), the embedding extends isometrically C->F, and L embeds isometrically too, agreeing on K. This is an actual joint complete nontrivially valued field. It does not assert that C completed-tensor_K L is a field. Any use of this amalgamation below concerns already harmonic/subharmonic functions, not continuous-current transport. Full new proofs appear in P06.2-argument.md (Lemmas 1 and 2); rerun bash reproduce.sh. No finite computation establishes these field lemmas.'''

THEOREM_NOTE = r'''New exact special-scope theorem for P06.2. Let K be ANY complete nontrivially valued non-Archimedean field, and let X be an actual good separated strict boundaryless pure one-dimensional K-analytic space. If h:X->R is finite continuous and D[h]=d'd''[h]=0 against every ordinary compact smooth scalar test, using canonical CLD integration with all actual generic Artinian lengths, then h is GR-harmonic and classically pluriharmonic. It is real PL in the G-local strict-analytic-unit convention, and GJR-harmonic. This includes imperfect/positive-characteristic K, singularities, nilpotents and unequal actual generic lengths. It holds on every ordinary open. For every analytic extension L/K, every L-analytic curve Y (separated, pure dimension one, with no extra strictness/smoothness/reducedness assumption), and every analytic map f:Y->X_L, h o pi_{L/K} o f is GR-harmonic; if Y is smooth strict it is Thuillier-harmonic.

Complete integration proof. By n1, C=completion(valued algebraic closure K) is algebraically closed, complete, nontrivially valued and contains K isometrically. Apply the exact n701 Theorems A/B with M=Kbar, completion C, n=1. Its hypotheses match X and h without reducedness, perfectness or separability. It gives the ACTUAL X_C=M(A completed-tensor_K C) locally, good separated strict boundaryless and pure one-dimensional, and D[h_C]=0 against ALL ordinary compact scalar tests. Purity is n701's componentwise/local proof, not total dimension alone. Its geometry proof uses affinoid neighbourhoods, strict presentations, the base-changed closed diagonal and the relative-interior base-change inclusion; it does not identify arbitrary absolute interiors.

For every compact ordinary scalar beta upstairs, n701 gives beta=q_E^*alpha_E as smooth sections for a single finite embedded E subset Kbar and compact ordinary alpha_E on X_E. The finite-stage gate makes D[h_E]=0. Then D beta=q_E^*D alpha_E and canonical smooth-top-measure projection gives integral_{X_C} h_C D beta = integral_{X_E} h_E D alpha_E=0. Supports are compact, and the continuous multipliers are bounded there. CLD arXiv:1204.6277v2 Proposition 15.3.1 is used only on the differentiated SMOOTH top form; no continuous-current pullback is defined. n701's exact all-test proof supplies the step that a mere pushforward identity could not supply.

Actual Artinian lengths are retained: for a finite Artinian H-algebra B of dimension d and complete H'/H, B tensor_H H' is finite-dimensional and already complete. Its local factors B_j satisfy d=sum_j length_{B_j}(B_j)[kappa_j:H'] by their composition series. Thus the canonical moment-degree sums are preserved, including inseparable residue degrees and nilpotents (CLD 13.3.3,14.3.6; n701 Section 10). Scalar top-measure projection has NO field-degree factor. The distinct same-carrier finite restriction rule mu_K=[E:K]mu_E in CLD 14.4.3 is not substituted for it. Unequal generic weights are not divided out.

Apply n700 Theorem A to X_C over C: every good separated strict boundaryless pure curve there is in its intrinsic recognition scope, including singular/nonreduced structures. It recognizes h_C as GR-harmonic. We use that theorem, not its separate ambient ground-field probe result. Its reduction and normalization gates handle actual unequal lengths and punctures; no smoothness of normalization over the original imperfect K is assumed.

Published function theorem: GR, Classically psh and pluriharmonic functions on Berkovich spaces, arXiv:2506.13548v2, 17 September 2025, Proposition 3.14(6) says: for any k-analytic curve Z and continuous u:Z->R, and every analytic extension field E/k, u is harmonic iff u o pi_{E/k} is harmonic on Z_E. A curve here is separated and pure dimension one (GR3.1); an analytic extension is complete and isometric (2.1-2.2). There is no smoothness, reducedness, perfectness or algebraicity restriction. Apply it with Z=X,u=h,E=C AFTER upstairs recognition. All hypotheses hold, so h is GR-harmonic.

This is a theorem about recognized FUNCTIONS. Its full primary scalar proof, GR3.5(7), LF827-885, is retained in the authoritative argument. It compares already subharmonic functions over a joint field (the actual joint field for C and any L is proved in n1), uses Thuillier harmonic-function scalar pullback on smooth strict probes, boundary projection GR Lemma2.12, and scalar surjectivity. No current on that joint field is used. Finite values remove the -infinity component alternative. The exact published Proposition3.14, Proposition3.15 and GR4.1/4.2 full units are also embedded and hash-bound; a source ending is never a tool truncation.

By GR Definition3.13, both h and -h are subharmonic. GR4.1.2 states exactly that on ANY analytic curve classical psh equals GR-subharmonicity; its proof uses scalar extension3.5(7) and forward curve pullback3.5(8). Apply it to each sign. Definition4.1 gives, for every analytic L/K and every curve map f:Y->X_L, subharmonicity of each sign of the finite continuous composite. Definition3.13 gives GR-harmonicity on Y. The further field/probe quantifiers inside Definition3.4 are retained. Definition7.1 gives classical pluriharmonicity on X. No equation on X_L or Y, no arbitrary transcendental-current ascent, and no finite-map converse in GR4.2(6) is used.

For real PL/GJR, GR Proposition3.15 has the exact scope: a continuous function on ANY strict analytic curve over a nontrivially valued field is harmonic iff it is R-PL and every residual class L_h(x) is numerically trivial. Apply it only after recognition. GR2.16 fixes G-local finite real sums of logarithms of analytic units on strict analytic domains. GJR arXiv:2111.05741v3, 7 March2025, field convention2.2, Definition5.1, Definition7.2 and Remark7.3(1) require complete nontrivial K and good strict space, and identify the real-PL residual numerical-triviality condition with GJR harmonicity. These hypotheses all hold on X. This supplies no ordinary CLD-smooth regularity.

An ordinary open Omega in X is an analytic domain, is good separated strict boundaryless, and has pure local dimension one (CLD11.1.7,11.2.3,11.4.1,11.7.7). Every compact scalar test on Omega extends by zero smoothly to X: its support is compact closed in Hausdorff X and contained in Omega, so exterior points have zero neighbourhoods. Differential and canonical-integration domain compatibility restrict the equation (CLD14.3.5,15.7.2,Section7.7). Apply the same proof to Omega. This covers actual ordinary opens at every analytic point.

Scope and evidence. Authoritative full new proof/applications: P06.2-argument.md; standalone paper: P06.2-partial.tex and twice-compiled P06.2-partial.pdf; five-key status.json; author-audit.md; research-notes.md; exact source/support manifests and review copies. Rerun bash reproduce.sh. n700 exact controlling expanded proof SHA256 8c46bccc1c2dd4286d3ccfc42aea70698ef8e449b9e57f962d707ecffd953a04; n701 authoritative round21 main SHA256 e7c350a209fa4b40875fa15a65875d210c306919a089cdc7b8cf918c895dbd42, separately bound expanded review wrapper SHA256 f1577176fe748c3ee6ddd18e3feae02221aba4d4ed60d7acaadb6f8dde93d7e6. Both old draft metadata and later exact-scope receipts remain unchanged. The supplied proof bodies are mathematical support; prior verdicts do not certify the new chain.

Relative to the catalogue this removes the algebraic-closure restriction for intrinsic recognition on EVERY actual curve with the original strict boundaryless pure ambient hypotheses, rather than only published algebraic curve opens or coordinate products. It is still a dimension-one special case. Original arbitrary-dimensional P06.2 remains open, status partial/candidate=false; P05.2 is not addressed. No first-stage ordinary CLD-smooth decreasing psh approximation, general positive-current regularization, general all-extension zero-current characterization, or higher-dimensional recognition is claimed. Those stronger constructions are separate from this recognition-only theorem. No round23 incomplete/nullproof or inconclusive all-K recognition is used; round25 smoothing is not modified. This is a new unverified integration draft, not independently reviewed or formally verified.'''

def main():
    for d in ('build', 'evidence'):
        (ROOT / d).mkdir(exist_ok=True)
    core = (ROOT / 'argument-core.md').read_text()
    assert '+not' not in core
    (ROOT / 'P06.2-argument.md').write_text(core + '\n\n' + (ROOT / 'sources/primary-bodies.md').read_text())
    status = dict(id='P06.2', status='partial',
        exact_result='Complete new integration draft: every finite continuous ordinary CLD zero-Hessian function on every actual good separated strict boundaryless pure analytic curve over any complete nontrivially valued field is GR-harmonic and classically pluriharmonic, with every analytic extension and every analytic curve-map quantifier; also G-local real PL and GJR-harmonic. Singularities, imperfect/positive-characteristic fields, nilpotents and unequal actual generic Artinian lengths are included. Original arbitrary-dimensional P06.2 remains open.',
        proof_file='P06.2-argument.md', concrete_gaps=[
            'Original P06.2 remains open in arbitrary-dimensional residual nonproduct domains and analytic germs; this theorem has dimension one.',
            'Ordinary CLD-smooth decreasing psh approximation on this full curve scope and general positive-current regularization are separate stronger constructions, not proved or required here.',
            'No new general transcendental-current ascent, reverse-current equivalence, or all-extension zero-current theorem is claimed.',
            'The new integration has an author audit only; its supporting gates retain their earlier exact-scope reviews, but no earlier verdict certifies these new bytes.'])
    dump('status.json', status)
    notes = [
        dict(id='n1', summary='Completion of the valued algebraic closure is proved algebraically closed in every characteristic; an actual joint field with any analytic L/K is constructed. Function-level use only.',
             detailedSummary='Using the exact finite complete-field norm foundation (also proved in n701), compatible norms on finite fields define the valued algebraic closure. A successive-root argument with coefficient errors 2^(-md)R^(-(d-1)) proves its completion algebraically closed without separability or spherical completeness. A maximal partial field embedding into an algebraic closure of any L/K is isometric and extends on completions. No current ascent through this joint field is asserted.',
             text=FIELD_NOTE, support=['n701']),
        dict(id='n2', summary='Integration proves arbitrary-field ordinary-zero-Hessian recognition on every good separated strict boundaryless pure analytic curve, including imperfect K, singularities and nilpotents. GR harmonic/classical pluriharmonic, all field/curve-map quantifiers; original P06.2 remains partial.',
             detailedSummary='Apply n701 exactly to completion of valued algebraic closure K, retaining actual pure-curve geometry and all ordinary compact tests/Artinian lengths; apply n700 intrinsic recognition there; use published GR3.14(6) only after harmonicity is recognized. GR4.1.2/Definition4.1 supplies both signs for all analytic extensions and all curve maps, and exact GR3.15/GJR hypotheses give G-local real PL and GJR harmonicity. Holds on actual ordinary opens. No ordinary smooth psh approximation, general positive-current regularization, arbitrary-transcendental current transport or arbitrary-dimensional recognition follows. This is an unverified new integration draft supported by exact reviewed gates.',
             text=THEOREM_NOTE, support=['n700','n701','n1']),
    ]
    env = dict(python=sys.version, platform=platform.platform(),
               pandoc=run(['pandoc','--version'],'evidence/pandoc-version.txt').split('\n')[0],
               pdflatex=run(['pdflatex','--version'],'evidence/pdflatex-version.txt').split('\n')[0],
               pdftotext=run(['pdftotext','-v'],'evidence/pdftotext-version.txt').split('\n')[0])
    dump('evidence/environment.json',env)
    run(['pandoc','argument-core.md','--standalone','--from=markdown+tex_math_single_backslash',
         '--to=latex','--number-sections','--output=P06.2-partial.tex'], 'evidence/pandoc-output.txt')
    # Allow provenance paths to wrap. All mathematical prose is unchanged.
    tex = (ROOT / 'P06.2-partial.tex').read_text()
    tex = tex.replace('\\begin{document}', '\\usepackage{xurl}\n\\begin{document}',1)
    tex = re.sub(r'\\texttt\{(/workspace/[^{}]+)\}',
                 lambda m: r'\path{' + m.group(1).replace(r'\_', '_') + '}', tex)
    tex = re.sub(r'\\texttt\{([a-f0-9]{64})\}', lambda m: r'\nolinkurl{' + m.group(1) + '}', tex)
    (ROOT / 'P06.2-partial.tex').write_text(tex)
    for n in (1,2):
        run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
             '-output-directory=build','P06.2-partial.tex'],f'evidence/pdflatex-pass-{n}.txt')
    (ROOT / 'P06.2-partial.pdf').write_bytes((ROOT / 'build/P06.2-partial.pdf').read_bytes())
    pdfinfo = run(['pdfinfo','P06.2-partial.pdf'],'evidence/pdfinfo.txt')
    run(['pdftotext','-layout','P06.2-partial.pdf','evidence/paper-extracted.txt'],'evidence/paper-extraction-output.txt')
    paper = (ROOT / 'evidence/paper-extracted.txt').read_text()
    assert 'arbitrary-field intrinsic curve recognition' in paper.lower()
    assert 'classically pluriharmonic' in paper.lower()
    assert 'partial' in paper.lower()
    assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
    assert status['id']=='P06.2' and status['status']=='partial'
    assert (ROOT / status['proof_file']).is_file()
    incoming = json.loads((ROOT / 'input.json').read_text())
    assert (ROOT/'original-problem.txt').read_text()==incoming['task']['problem']
    assert (ROOT/'completion-criteria.txt').read_text()==incoming['task']['completionCriteria']
    assert (ROOT/'assignment-verbatim.txt').read_text()==incoming['assignment']
    manifest=json.loads((ROOT / 'sources/manifest.json').read_text())
    for m in manifest:
        assert digest((ROOT / m['artifact']).read_bytes())==m['sha256']
    units=json.loads((ROOT / 'sources/primary-units.json').read_text())
    for u in units:
        assert digest((ROOT / u['artifact']).read_bytes())==u['body_sha256']
        source=(ROOT/'sources'/u['source']).read_bytes().split(b'\n')
        assert (ROOT/u['artifact']).read_bytes()==b'\n'.join(source[u['first_lf_line']-1:u['last_lf_line']])
    warnings=[line for line in (ROOT/'build/P06.2-partial.log').read_text().split('\n')
              if 'Warning' in line or 'Overfull' in line or 'Missing character' in line]
    pages=re.search(r'Pages:\s+(\d+)',pdfinfo).group(1)
    notes.append(dict(id='n3',
        summary='Reproducible proof package built twice; exact support/source hashes and LF extraction bindings pass. Partial five-key status and canonical note schemas checked; these are artifact observations, not proof certification.',
        detailedSummary=f'Preserved original problem, criteria and assignment exactly. Copied 23 read-only support/source/review files and extracted 16 primary units, including all three hash-bound GR selected bodies. Installed pandoc/pdfLaTeX generated and twice compiled a {pages}-page standalone PDF. Source, status and ID-only support schema checks passed. The package contains no independent review of its new integration and does not solve the arbitrary-dimensional atom.',
        text=f'Observed artifact result: bash reproduce.sh copies immutable sources, verifies six declared whole-file hashes and the three operator-selected LF-body hashes, assembles P06.2-argument.md, and builds P06.2-partial.tex and P06.2-partial.pdf with two successful pdfLaTeX passes. The PDF has {pages} pages. Exactly 23 read-only files and 16 primary units were retained; status.json has exactly id,status,exact_result,proof_file,concrete_gaps, with id=P06.2,status=partial,proof_file=P06.2-argument.md. Original problem, completion criteria and assignment strings compare equal to input.json. Canonical new notes use only supplied/earlier note IDs in support; candidate=false. Source/commands/environment/build logs are in sources/manifest.json, sources/primary-units.json, evidence/commands.json, evidence/environment.json and evidence/pdflatex-pass-1.txt and -2.txt. Author application audit and rejected-route gaps are in author-audit.md and research-notes.md. Artifact SHA256 records are in evidence/artifact-manifest.json. Programs are prepare.py, build-and-check.py and finalize-manifest.py; rerun bash reproduce.sh from this workspace. Compilation, finite schema diagnostics and authentication of cached source bytes do not prove the mathematical claims. No new model/subagent/network/install/external message, old-artifact write, database/authentication/environment change or resource-heavy computation was used. No supervised heavy-compute service was supplied or needed. The optional independent review of the new integration remains outstanding; earlier n700/n701 receipts stay at their own scopes.',
        support=['n2']))
    result=dict(notes=notes,candidate=False)
    prior={x['id'] for x in incoming['notes']}
    for n in notes:
        assert re.fullmatch(r'n[1-9][0-9]*',n['id'])
        assert set(n)=={'id','summary','detailedSummary','text','support'}
        assert all(s in prior for s in n['support'])
        prior.add(n['id'])
    dump('notes.json',result)
    checks=dict(status_keys=list(status),status='partial',candidate=False,notes=len(notes),
                support_schema='passed',original_input_strings='exact',source_files=len(manifest),
                primary_units=len(units),pdflatex_successful_passes=2,pdf_pages=int(pages),
                warnings=warnings,mathematical_verification=False)
    dump('evidence/checks.json',checks)
    dump('evidence/commands.json',COMMANDS)
    paths=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='artifact-manifest.json' and '.git' not in p.parts]
    dump('evidence/artifact-manifest.json',[
        dict(artifact=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p.read_bytes()))
        for p in sorted(paths)])
    print(f'Built {pages}-page standalone PDF in two passes; schemas, exact input strings, 23 sources and 16 LF units checked.')
    print(f'Build warnings: {len(warnings)}; see evidence/checks.json. Mathematical verification: not claimed.')

if __name__=='__main__':
    main()
