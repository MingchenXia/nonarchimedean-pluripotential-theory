#!/usr/bin/env python3
"""Build only this assignment's own notes and complete uncompiled TeX."""
import datetime
import hashlib
import json
import pathlib
import platform
import sys

O = pathlib.Path(__file__).resolve().parent

def escape(s):
    table = {'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$',
             '#':r'\#','_':r'\_','{':r'\{','}':r'\}',
             '~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
    return ''.join(table.get(c,c) for c in s)

def main():
    metadata = json.loads((O/'note-metadata.json').read_text())
    notes = []
    for row in metadata:
        note = dict(row)
        note['text'] = (O/(row['id']+'.md')).read_text()
        notes.append(note)
    result = {'notes':notes,'candidate':False}
    encoded = json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    (O/'final-notes.json').write_text(encoded)
    assert json.loads(encoded) == result
    companion = '# Generated finite-energy analytic operators on the concrete quotient\n\nUnverified scoped proof draft. Original P16.7 incomplete.\n\n'
    companion += '\n\n'.join(note['text'] for note in notes)
    companion += '\n\n'+(O/'source-application-ledger.md').read_text()
    (O/'proof-companion.md').write_text(companion)
    preamble = r'''\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\setlength{\emergencystretch}{5em}
\title{Generated finite-energy analytic Monge--Ampere operators}
\author{Independent unverified scoped proof draft}
\date{9 October 2026; uncompiled}
\begin{document}
\maketitle
Original P16.7 remains incomplete. The following contains all current
proofs, declared foundations, audit limitations and reproduction evidence.
'''
    lines = []
    for line in companion.splitlines():
        if line.startswith('# '):
            lines.append(r'\section*{'+escape(line[2:])+'}')
        else:
            lines.append(escape(line))
    paper = preamble+'\n'.join(lines)+'\n'+r'\end{document}'+'\n'
    (O/'generated-E1-paper.tex').write_text(paper)
    for note in notes:
        assert note['text'] in companion
    verdict = {'candidate':False,'status':'unverified scoped theorem',
               'new_domain':'all-direction E1_downarrow on the actual quotient',
               'new_gates':['every bounded continuous decreasing presentation','all continuous analytic tests',
                  'mixed weak products','full raw mass two','generated clamp identification',
                  'generated comparison and first variation','moving-measure L1 convergence'],
               'remaining':['entire older/source/book audit','full intrinsic E1 recognition',
                  'separated energy-sublevel compactness','analytic envelopes and orthogonality',
                  'existence for every admissible arbitrary-support measure','full uniqueness'],
               'geometry_scope':'whole390 named published foundations retained, not newly recursively certified',
               'compiled':False,'accepted':False,'published':False}
    (O/'scoped-verdict.json').write_text(json.dumps(verdict,indent=2)+'\n')
    env = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'python':sys.version,'platform':platform.platform(),'cwd':str(O),
           'supplied_programs_executed_or_imported':False,'subagents':0,
           'heavy_compute':False,'supervised_compute_facility':'not supplied; not needed',
           'compiler_invoked':False,'network_or_auth_changes':False,
           'model_selection':'configured user request; not independently introspectable',
           'cloud_environment_status_tool':'not present in callable tool metadata'}
    (O/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
    names = ['final-notes.json','proof-companion.md','generated-E1-paper.tex','scoped-verdict.json']
    report = {'serialization_roundtrip':True,'all_five_proof_bodies_in_companion':True,
              'complete_own_companion_encoding':True,'candidate':False,'compiled':False,
              'artifacts':[{ 'name':name,'bytes':(O/name).stat().st_size,
                 'sha256':hashlib.sha256((O/name).read_bytes()).hexdigest()} for name in names]}
    (O/'build-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()
