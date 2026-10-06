from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess

K = Path('/workspace/research/root-checks')
T = K/'P16.5-exceptional-big-cone-entire-relative-equation-candidate-20261006-continuation185.tex'
U = K/'P16.5-exceptional-relative-equation-proof-unit-20261006-continuation185.txt'
D = K/'public-P16.5-continuation185-exceptional-equation-reader'
B = D/'publication-binding.json'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
old = json.loads(B.read_text())
assert sha(T) == old['tex_sha256'] == '7ca0a8a8f8770ab42ae052d759c569d6de3ba2178be548fe578412b1c3fda714'
assert sha(U) == '286c6417774f2d8694aa4bcb941141e240bd2b4ba529e282edbaece713a6d77e'
history = D/'initial-duplicate-numbering-build-LOCALONLY.json'
assert not history.exists()
history.write_text(json.dumps(old, indent=2)+'\n')
body = U.read_text()
body = re.sub(r'\\tag\{(1[1-9]|2[0-3])\}', lambda m: '\\tag{'+str(int(m[1])+3)+'}', body)
body = re.sub(r'\((1[1-9]|2[0-3])\)', lambda m: '('+str(int(m[1])+3)+')', body)
heading = '\\section{The full ample equation premise, now used in its exact domain}'
statement = r'''\section{Main relative equation statement}
\begin{theorem}[Unreviewed entire exceptional-class equation]
For every retained datum in (1), let $\sigma_c$ be the actual
canonical exceptional potential. The entire genuine cone is
$\sigma_c+\pi^*\PSH(Y,A)$, with intrinsic minimal reference
$\sigma_c$. Its relative finite-energy space is precisely
$\mathcal E_L^1=\sigma_c+\pi^*\mathcal E^1(Y,A)$.
The actual moving-intersection operator constructed below has raw
mass $V=A^n=\vol(L)>0$, independent of the regularizing net, and
satisfies mixed weighted decreasing convergence, comparison,
domination and uniqueness modulo constants. Its outer relative
energy has both directional derivatives in every
$f\in C^0(X^{\rm an})$, equal to $\int_X f\,\MA_L(u)$.

For every positive Radon measure $\nu$ on the original $X^{\rm an}$
with mass $V$, the equation $\MA_L(u)=\nu$ has an actual solution
$u\in\mathcal E_L^1$ if and only if the intrinsic compensator
dual energy in (24) is finite. Such a solution attains the relative
variational supremum, and all solutions differ by a constant.
\end{theorem}
\begin{proof}
The full structural argument precedes this statement. The following
sections construct the operator before the equation, prove the
polar exclusion and both outer derivatives, and finally establish
the exact target criterion, attainment and uniqueness.
\end{proof}

'''
assert body.startswith(heading)
U.write_text(statement+body)
whole = T.read_text()
prefix = whole.split(heading, 1)[0]
T.write_text(prefix+U.read_text()+'\n\\end{document}\n')
tags = re.findall(r'\\tag\{(\d+)\}', T.read_text())
assert len(tags) == len(set(tags)) == 26 and set(map(int, tags)) == set(range(1,27))
argv = ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
        '-output-directory='+str(D),str(T)]
builds = []
for n in (1,2):
    r = subprocess.run(argv,capture_output=True,text=True)
    (D/f'final-build-{n}.stdout').write_text(r.stdout)
    (D/f'final-build-{n}.stderr').write_text(r.stderr)
    builds.append({'argv':argv,'returncode':r.returncode})
    if r.returncode:
        raise RuntimeError(r.stdout[-4000:])
log = (D/(T.stem+'.log')).read_text()
pdf = D/(T.stem+'.pdf')
info = subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
old.update({'recorded_utc':datetime.now(timezone.utc).isoformat(),
            'tex_sha256':sha(T),'whole_final_tex_root_read':False,
            'builds':builds,'overfull':log.count('Overfull'),
            'undefined':log.count('undefined'),'warnings':log.count('Warning'),
            'pdf_sha256':sha(pdf),'actual_visual_pages':[],
            'pages':int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:'))),
            'equation_tags_unique':True,'numbering_repair':'Structural equations 1--13 and relative equation equations 14--26; exact main statement added.',
            'root_read_of_pre_repair_whole_tex':True,
            'root_read_of_pre_repair_whole_unit':True})
old['proof_units'][1].update({'sha256':sha(U),'whole_unit_root_read':False})
B.write_text(json.dumps(old,indent=2)+'\n')
print(json.dumps({k:old[k] for k in ['tex_sha256','pdf_sha256','pages','overfull','undefined','warnings','equation_tags_unique']},indent=2))
