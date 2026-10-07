from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,hashlib
repo=Path(__file__).resolve().parents[1]
src=repo/'publication/sources'
spec=importlib.util.spec_from_file_location('support',repo/'reviewed/code/review_support.py'); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results=[]
for path in list(sorted(src.glob('daniel-live-*.cert')))+[src/'daniel-candidate-n272.cert',src/'squish-n130.cert.json']:
 start=time.monotonic();data=path.read_bytes()
 if path.suffix=='.cert':
  lines=[l for l in data.decode().splitlines() if l and not l.startswith('#')]
  n,side=lines[0].split();n=int(n);side=F(side)
  poses=[tuple(map(F,line.split())) for line in lines[1:]]
 else:
  d=json.loads(data);n=d['n'];side=F(d['s_exact']);poses=[tuple(map(F,r)) for r in d['squares']]
 assert len(poses)==n
 sq=[]
 for x,y,t in poses:
  u=((1-t*t)/(1+t*t),2*t/(1+t*t));v=(-u[1],u[0]);assert u[0]*u[0]+u[1]*u[1]==1
  sq.append((x-side/2,y-side/2,u,v))
 report=m.geometry(side,sq)
 report.update(n=n,side=str(side),file=path.name,sha256=hashlib.sha256(data).hexdigest(),seconds=time.monotonic()-start,method='Reused reviewed support-function checker on source rational centers and half-angle parameters, translating [0,side]^2 to its centered frame; not a new implementation')
 results.append(report)
 print(path.name,n,'PASS',float(side),report['pairs'],flush=True)
(repo/'publication/receipts/refreshed-source-checks.json').write_text(json.dumps({'valid':True,'results':results},indent=2)+'\n')
