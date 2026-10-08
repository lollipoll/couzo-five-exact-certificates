from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,subprocess,sys
r=Path(__file__).resolve().parent
c=json.loads((r/'comparison.json').read_text())
assert hashlib.sha256((r/'n105.cert.json').read_bytes()).hexdigest()==c['source_sha256']
assert Q(c['historical_our_exact'])-Q(c['ry_xu_exact'])==Q(c['our_minus_ry_xu_exact'])>0
subprocess.run([sys.executable,'-B',str(r/'verify_seed.py'),str(r/'n105.cert.json'),'--n','105'],check=True)
print('Exact supersession comparison PASS:',c['our_minus_ry_xu_exact'])
