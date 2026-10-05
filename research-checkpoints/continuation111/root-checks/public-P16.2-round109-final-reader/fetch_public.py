"""Attempt public primary retrieval, preserving success or failure literally."""
import datetime
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
(ROOT/'logs').mkdir(exist_ok=True)
(ROOT/'public').mkdir(exist_ok=True)
url='https://stacks.math.columbia.edu/tag/0BFP'
argv=['curl','--location','--fail','--max-time','30','--dump-header','public/0BFP.headers','--output','public/0BFP.html',url]
r=subprocess.run(argv,cwd=ROOT,text=True,capture_output=True)
record=dict(url=url,argv=argv,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,
            meaning='Observation of public retrieval only; no mathematical implication. A nonzero exit does not yield a source body.')
(ROOT/'logs/public-fetch.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
