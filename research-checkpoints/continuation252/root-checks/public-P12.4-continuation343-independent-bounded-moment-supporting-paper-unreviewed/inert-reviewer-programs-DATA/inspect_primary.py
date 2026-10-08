#!/usr/bin/env python3
"""Render five explicitly bound primary pages. No supplied code is imported."""
import json, subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
entries=json.loads((HERE/'inputs/private-primary-packet-bindings.json').read_text())
book=next(x['path'] for x in entries if x['path'].endswith('Swanson-Huneke-author-book.pdf'))
bfj=next(x['path'] for x in entries if x['path'].endswith('BFJ-valuations-psh.pdf'))
jobs=[(book,154,'SH-printed140'),(book,369,'SH-printed355'),(book,373,'SH-printed359'),(book,374,'SH-printed360'),(bfj,32,'BFJ-printed480')]
log=[]
for source,page,name in jobs:
    target=HERE/'evidence/source-pages'/name
    command=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-r','100','-png',source,str(target)]
    result=subprocess.run(command,capture_output=True,text=True,check=True)
    log.append({'command':command,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'output':str(target)+'.png'})
(HERE/'evidence/page-inspection-commands.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps({'rendered_pages':len(log),'compilation':False}))
