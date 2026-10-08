"""Deterministic source-derived Markdown; preserves all body proof prose/math."""
import hashlib
from pathlib import Path
import re
root=Path(__file__).resolve().parent
raw=(root/"P05.1-paper.tex").read_bytes()
text=raw.decode()
text=text.split("\\begin{abstract}",1)[1].split("\\begin{thebibliography}",1)[0]
text=text.replace("\\end{abstract}","\n")
text=re.sub(r"\\section\{([^{}]*)\}",r"\n## \1\n",text)
text=re.sub(r"\\label\{([^{}]*)\}",r" <a id=\"\1\"></a>",text)
text=re.sub(r"\\ref\{([^{}]*)\}",r"[\1](#\1)",text)
text=re.sub(r"\\begin\{(theorem|lemma|proposition)\}(?:\[([^\]]*)\])?",lambda m:"\n**"+m[1].title()+(": "+m[2] if m[2] else "")+".** ",text)
text=re.sub(r"\\end\{(?:theorem|lemma|proposition)\}","\n",text)
text=text.replace("\\begin{proof}","\n**Proof.** ").replace("\\end{proof}"," ∎\n")
text=text.replace("\\begin{align*}","$$\n\\begin{aligned}").replace("\\end{align*}","\\end{aligned}\n$$")
text=text.replace("\\[","$$").replace("\\]","$$")
for src,dst in [(r"\R",r"\mathbb{R}"),(r"\Q",r"\mathbb{Q}"),(r"\Z",r"\mathbb{Z}"),(r"\PA",r"\mathrm{PA}"),(r"\PC",r"\mathrm{PC}")]:
    text=re.sub(re.escape(src)+r"(?![A-Za-z])",lambda m:dst,text)
for name in ["conv","cone","epi","rec","aff","ri","dist"]:
    operator="relint" if name=="ri" else name
    text=re.sub(r"\\"+name+r"(?![A-Za-z])",lambda m:r"\operatorname{"+operator+"}",text)
text=re.sub(r"\\emph\{([^{}]*)\}",r"*\1*",text)
text=re.sub(r"\\texttt\{([^{}]*)\}",lambda m:"`"+m[1].replace(r"\_","_")+"`",text)
text=text.replace("~"," ").replace("--","–")
header="# Compatible references and sharp uniform restriction obstruction\n\nOwn source-derived proof manuscript. Unreviewed; original P05.1/P05.2 remain OPEN; candidate=false.\n\nDerived from `P05.1-paper.tex`, SHA256 `"+hashlib.sha256(raw).hexdigest()+"`, by `python3 make_argument.py`. All theorem/proof prose and mathematical displays in the body are retained. Markdown conversion is presentation, not an independent correctness certificate.\n\n"
(root/"argument.md").write_text(header+text.strip()+"\n")
print("Wrote argument.md; source SHA256",hashlib.sha256(raw).hexdigest())
