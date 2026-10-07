"""Resolve full Pandoc argument references using the compiled paper's labels."""
import json
import re
import subprocess
from pathlib import Path

aux = Path('P05.2-paper.aux').read_text()
labels = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux))
path = Path('argument.md')
md = path.read_text()
refs = []
pattern = r'\[(?:\\\[[A-Za-z0-9_-]+\\\]|\d+)\]\(#[^)]+\)\{reference-type="(eqref|ref)" reference="([A-Za-z0-9_-]+)"\}'

def reference(match):
    kind, name = match.groups()
    value = labels[name]
    refs.append({'label':name,'number':value,'kind':kind})
    return '('+value+')' if kind == 'eqref' else value

md = re.sub(pattern, reference, md)
tagged = []

def equation(match):
    body = match.group(1)
    names = re.findall(r'\\label\{([^}]+)\}', body)
    assert len(names) <= 1
    body = re.sub(r'\\label\{[^}]+\}', '', body).replace(r'\notag','')
    if names:
        name = names[0]
        body += r'\tag{'+labels[name]+'}'
        tagged.append({'label':name,'number':labels[name]})
    return '$$'+body+'$$'

md = re.sub(r'\$\$(.*?)\$\$', equation, md, flags=re.S)
tex = Path('P05.2-paper.tex').read_text()
bib = re.search(r'\\begin\{thebibliography\}\{[^}]+\}(.*?)\\end\{thebibliography\}',tex,re.S).group(1)
items = []
for n, match in enumerate(re.finditer(r'\\bibitem\{([^}]+)\}\s*(.*?)(?=\\bibitem|\Z)',bib,re.S),1):
    key, body = match.groups()
    result = subprocess.run(['pandoc','--from=latex','--to=markdown','--wrap=none'],
                            input=body,text=True,capture_output=True,check=True)
    items.append(f'{n}. [{key}] '+result.stdout.strip())
assert len(items) == 6
md = re.sub(r'::: thebibliography\n.*?\n:::',
            '# References\n\n'+'\n\n'.join(items),md,flags=re.S)
assert 'reference-type=' not in md and r'\label{' not in md
path.write_text(md)
Path('evidence/markdown-normalization.json').write_text(json.dumps(
    {'resolved_references':refs,'numbered_equations':tagged,'bibliography_items':len(items),
     'scope':'Full argument retained; only generated reference and bibliography presentation normalized.'},indent=2)+'\n')
print(f'Resolved {len(refs)} references, numbered {len(tagged)} equations, retained all six bibliography entries.')
