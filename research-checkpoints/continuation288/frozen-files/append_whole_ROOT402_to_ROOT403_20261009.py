from pathlib import Path
import hashlib,json
R=Path('/workspace/research');K=R/'root-checks'
p=K/'P16.7-continuation403-generated-uniqueness-by-two-actual-Gauss-fibres-working-paper-20261009.tex'
q=K/'P16.7-continuation402-bounded-atomic-tests-and-Shilov-point-lower-bounds-working-paper-20261009.tex'
digest=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
assert digest(q)=='69236b72acdfd53fc29a6187ff2747f932c5c5fcfbaa59d3ba543ae0f5ff3b99'
assert digest(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
a=p.read_text();s=q.read_text();marker='% ROOT402_WHOLE_MATHEMATICAL_APPENDIX_INSERTION'
assert a.count(marker)==1 and a.count('\\end{document}')==1
body=s[s.index('\\section{The actual analytic object'):s.index('\\end{document}')]
prefix=r'''\clearpage
\appendix
\section*{Whole mathematical body of point-atom working paper 402}
The following is the exact mathematical body of paper 402,
including its historical scope and residual statements. Those
statements describe what paper 402 alone establishes; the new
generated uniqueness argument is the main part of this paper.
Its inclusion supplies the full bounded Green, local atomic,
all-stage recognition and pointwise reconstruction proofs rather
than an external project-file dependency. Exact identity is not
an additional independent primary-source reading.
'''
p.write_text(a.replace(marker,prefix+body))
assert p.read_text().count('\\begin{document}')==1 and p.read_text().count('\\end{document}')==1
print(json.dumps(dict(paper=str(p),bytes=p.stat().st_size,sha256=digest(p),exact_appendix_bytes=len(body.encode()),appendix_sha256=hashlib.sha256(body.encode()).hexdigest(),UNREVIEWED=True,original_closed=False),indent=2))
