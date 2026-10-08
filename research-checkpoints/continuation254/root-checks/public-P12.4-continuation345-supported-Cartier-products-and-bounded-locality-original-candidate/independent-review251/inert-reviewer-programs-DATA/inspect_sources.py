"""Owned bounded PDF page rendering; primary images stay local."""
import json,pathlib,subprocess,hashlib
ROOT=pathlib.Path(__file__).resolve().parent
PAGES=[('/workspace/research/primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008/Swanson-Huneke-author-book.pdf',362,'sh348'),('/workspace/research/primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008/Swanson-Huneke-author-book.pdf',367,'sh353'),('/workspace/research/primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008/Swanson-Huneke-author-book.pdf',369,'sh355'),('/workspace/research/primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008/Swanson-Huneke-author-book.pdf',370,'sh356'),('/workspace/research/campaigns/round-232/P12.2-original-excellent-singular-geometric-cone-and-model-nef-comparison/frozen-primary-data-LOCALONLY/BFJ-valuations-psh.pdf',32,'bfj480'),('/workspace/research/campaigns/round-232/P12.2-original-excellent-singular-geometric-cone-and-model-nef-comparison/frozen-primary-data-LOCALONLY/BFJ-valuations-psh.pdf',33,'bfj481')]
def main():
    out=ROOT/'evidence'/'source-images-LOCALONLY';out.mkdir(parents=True,exist_ok=True)
    logs=[]
    for src,page,label in PAGES:
        cmd=['pdftoppm','-f',str(page),'-l',str(page),'-r','110','-singlefile','-png',src,str(out/label)]
        r=subprocess.run(cmd,capture_output=True,text=True,check=True)
        b=(out/(label+'.png')).read_bytes()
        logs.append({'command':cmd,'stdout':r.stdout,'stderr':r.stderr,'image':str(out/(label+'.png')),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'interpretation':'Rendering evidence only; actual visual inspection is recorded separately in pixel-inspection.md.'})
    (ROOT/'evidence'/'source-rendering.json').write_text(json.dumps(logs,indent=2)+'\n')
    print('Rendered',len(logs),'bound pages locally.')
if __name__=='__main__':main()
