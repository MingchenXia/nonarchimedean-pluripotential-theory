from pathlib import Path
import subprocess,json
pdf='/workspace/research/primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008/Swanson-Huneke-author-book.pdf'
prefix='LOCALONLY/source-pixels/SH-370'
Path(prefix).parent.mkdir(parents=True,exist_ok=True)
cmd=['pdftoppm','-f','370','-singlefile','-scale-to','1600','-png',pdf,prefix]
r=subprocess.run(cmd,capture_output=True,text=True)
Path('evidence/source-rendering.json').write_text(json.dumps({'command':cmd,'exit_code':r.returncode,'stderr':r.stderr,'page':'PDF370 printed356','pixels_viewed_in_session':True,'purpose':'literalSH17.4.7 omitted quotient; no mathematical verification'},indent=2)+'\n')
print('source render exit',r.returncode)
