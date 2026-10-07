"""Independent standard-library verification of a translational LP dual bound.
Reconstructs all supporting half-planes directly from the certificate's vertices.
"""
from fractions import Fraction as F
from pathlib import Path
import json,time,hashlib,sys
sys.set_int_max_str_digits(100000)

def verify(data,witness):
 sq=data['squares'];count=data['n'];assert count==len(sq) and count>0;L=F(data['container_side']);xy=[tuple(F(s[k]) for k in ['x','y']) for s in sq];edges=[];offsets=[]
 for s in sq:
  t=F(s['t']);c,d=(1-t*t)/(1+t*t),2*t/(1+t*t);u,v=(c,d),(-d,c);edges.append((u,v));offsets.append([((a*c-b*d)/2,(a*d+b*c)/2) for a,b in [(-1,-1),(1,-1),(1,1),(-1,1)]])
 rows=[];pairs=[]
 for owner,other,axis,sign in witness['choices']:
  assert 0<=owner<count and 0<=other<count and owner!=other and axis in [0,1] and sign in [-1,1];pairs.append(tuple(sorted((owner,other))));n=tuple(sign*x for x in edges[owner][axis])
  for v in offsets[other]:
   A={2*owner:-n[0],2*owner+1:-n[1],2*other:n[0],2*other+1:n[1]};b=sum(x*y for x,y in zip(n,v))-F(1,2);rows.append((A,b))
 assert len(pairs)==(count*(count-1)//2) and len(set(pairs))==(count*(count-1)//2)
 for i in range(count):
  for v in offsets[i]:
   for d in range(2):
    for sign in [-1,1]:rows.append(({2*i+d:F(sign),(2*count):F(1,2)},sign*v[d]))
 point=[x for p in xy for x in p]+[L];gaps=[sum(a*point[k] for k,a in A.items())+b for A,b in rows];assert min(gaps)>=0
 weights=list(map(F,witness['dual_weights']));ids=witness['dual_rows'];assert len(ids)==len(weights)==len(set(ids)) and all(w>=0 for w in weights)
 combo=[F(0)]*(2*count+1);constant=F(0)
 for i,w in zip(ids,weights):
  A,b=rows[i]
  for j,a in A.items():combo[j]+=w*a
  constant+=w*b
 correction=sum(abs(v) for v in combo[:-1])/2
 coefficient=combo[-1]+correction;assert coefficient>0
 assert correction==F(witness['residual_center_bound_correction']) and coefficient==F(witness['objective_coefficient'])
 lower=-constant/coefficient;assert lower==F(witness['lower_bound']) and lower<=L
 return dict(valid=True,all_halfplanes_checked=len(rows),pairs=(count*(count-1)//2),dual_terms=len(ids),lower_bound=str(lower),upper_bound=str(L),gap=str(L-lower),gap_float=float(L-lower),minimum_primal_slack=str(min(gaps)),scope=witness['scope'],proof='Let c.x + cL*L + b be the exact nonnegative weighted constraint sum. Containment implies every center coordinate has absolute value <= L/2. Thus 0 <= sum <= (cL + ||c||_1/2)*L+b. The positive coefficient gives L >= -b/(cL+||c||_1/2). The exact certificate attains the stated upper bound in the SAME selected-separator family.')

def main():
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('witness',type=Path);ap.add_argument('output',type=Path);a=ap.parse_args()
 d=json.loads(a.certificate.read_text());w=json.loads(a.witness.read_text());t=time.monotonic();r=verify(d,w);r['seconds']=time.monotonic()-t;r['certificate_sha256']=hashlib.sha256(a.certificate.read_bytes()).hexdigest();a.output.write_text(json.dumps(r,indent=2)+'\n');print({k:r[k] for k in ['valid','all_halfplanes_checked','dual_terms','gap_float','seconds']})
if __name__=='__main__':main()
