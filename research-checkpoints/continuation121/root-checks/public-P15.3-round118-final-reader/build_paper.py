"""Generate standalone TeX and retain two real compiler runs and their logs."""
from pathlib import Path
import json
import shutil
import subprocess
import hashlib
import re

ROOT=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def run(cmd,stem):
 result=subprocess.run(cmd,cwd=ROOT,capture_output=True)
 (ROOT/(stem+'.stdout')).write_bytes(result.stdout)
 (ROOT/(stem+'.stderr')).write_bytes(result.stderr)
 return {'command':cmd,'exit_code':result.returncode,'stdout':stem+'.stdout','stderr':stem+'.stderr'}

def escape(s):
 mapping={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','%':r'\%','&':r'\&','#':r'\#','_':r'\_\allowbreak{}','^':r'\textasciicircum{}\allowbreak{}','~':r'\textasciitilde{}','$':r'\$','-':r'-\allowbreak{}','/':r'/\allowbreak{}','=':r'=\allowbreak{}'}
 return ''.join(mapping.get(c,c) for c in s)

def inline(s):
 parts=[]; pos=0
 for m in re.finditer(r'`[^`]*`|\*\*[^*]*\*\*|\$[^$]*\$',s):
  parts.append(escape(s[pos:m.start()])); token=m.group()
  if token.startswith('`'):parts.append(r'\texttt{'+escape(token[1:-1])+'}')
  elif token.startswith('**'):parts.append(r'\textbf{'+inline(token[2:-2])+'}')
  else:parts.append(token)
  pos=m.end()
 parts.append(escape(s[pos:])); return ''.join(parts)

def generate_tex():
 lines=(ROOT/'P15.3-argument.md').read_text().split('\n')
 out=[r'''\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setmonofont{DejaVu Sans Mono}
\usepackage{amsmath,amssymb}
\usepackage{fvextra}
\usepackage[unicode,colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\tolerance=5000
\setlength{\emergencystretch}{4em}
\setlength{\parskip}{0.4em}
\title{'''+inline(lines[0].removeprefix('# '))+r'''}
\author{Unverified research draft}
\date{}
\begin{document}
\maketitle
''']
 i=1; list_kind=None
 def close_list():
  nonlocal list_kind
  if list_kind:out.append(r'\end{'+list_kind+'}');list_kind=None
 while i<len(lines):
  l=lines[i]
  if not l.strip():out.append('');i+=1;continue
  numbered=re.match(r'^(\d+)\. (.*)',l)
  if l.startswith('- ') or numbered:
   kind='itemize' if l.startswith('- ') else 'enumerate'
   if list_kind!=kind:close_list();out.append(r'\begin{'+kind+'}');list_kind=kind
   out.append(r'\item '+inline(l[2:]) if kind=='itemize' else r'\item['+numbered.group(1)+'.] '+inline(numbered.group(2)))
   i+=1;continue
  close_list()
  if l.startswith('    '):
   block=[]
   while i<len(lines) and lines[i].startswith('    '):block.append(lines[i][4:]);i+=1
   out.append(r'\begin{Verbatim}[breaklines=true,fontsize=\small]');out.extend(block);out.append(r'\end{Verbatim}');continue
  if l.startswith('$$'):
   assert l.endswith('$$') and len(l)>4
   out.append(r'\['+l[2:-2]+r'\]');i+=1;continue
  head=re.match(r'^(#+) (.*)',l)
  if head:
   command={1:'section',2:'subsection',3:'subsubsection'}.get(len(head.group(1)),'paragraph')
   out.append('\\'+command+'{'+inline(head.group(2))+'}');i+=1;continue
  out.append(inline(l));i+=1
 close_list();out.append(r'\end{document}')
 (ROOT/'P15.3-paper.tex').write_text('\n'.join(out)+'\n')
 (ROOT/'paper-generation.stdout').write_text('Standalone TeX generated in Python from the entire P15.3-argument.md.\n')
 (ROOT/'paper-generation.stderr').write_text('')
 return {'operation':'Python generate_tex() in build_paper.py','source':'P15.3-argument.md','exit_code':0,'stdout':'paper-generation.stdout','stderr':'paper-generation.stderr'}

def main():
 tex=shutil.which('xelatex')
 if not tex:raise RuntimeError('Required existing XeLaTeX unavailable; no installation authorized.')
 manifest={'generation':generate_tex(),'compilations':[]}
 for n in (1,2):
  rec=run([tex,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','P15.3-paper.tex'],f'compile-{n}')
  log=ROOT/'P15.3-paper.log'
  if log.exists():
   dest=ROOT/f'compile-{n}.tex.log'; dest.write_bytes(log.read_bytes());rec['tex_log']=dest.name
  manifest['compilations'].append(rec)
 manifest['artifact_sha256']={p:sha(ROOT/p) for p in ['P15.3-argument.md','P15.3-paper.tex','P15.3-paper.pdf'] if (ROOT/p).exists()}
 (ROOT/'build-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps(manifest,indent=2))
 if any(x['exit_code'] for x in manifest['compilations']):raise RuntimeError('At least one compilation failed; see retained actual logs.')

if __name__=='__main__':main()
