"""Independent audit: center/support-function exact tests, no campaign imports."""
import json, hashlib, time
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'verification-output' / 'external-review'
OUT.mkdir(exist_ok=True, parents=True)
SIGNS = [(-1,-1),(1,-1),(1,1),(-1,1)]

def load_pose(path, expected):
    raw=path.read_bytes(); d=json.loads(raw)
    if d['schema']!='packing-n/exact-v1' or type(d['n']) is not int or d['n']!=expected or len(d['squares'])!=expected:
        raise ValueError('Inventory/schema mismatch')
    side=Q(d['container_side'])
    if side<=0: raise ValueError('Invalid container')
    sq=[]
    for r in d['squares']:
        x,y,t=[Q(r[k]) for k in ('x','y','t')]
        u=((1-t*t)/(1+t*t),2*t/(1+t*t)); v=(-u[1],u[0])
        if u[0]*u[0]+u[1]*u[1]!=1 or u[0]*v[0]+u[1]*v[1]!=0: raise ValueError('Not an exact unit frame')
        sq.append((x,y,u,v))
    return side,sq,hashlib.sha256(raw).hexdigest()

def product(a,b): return a[0]*b[0]+a[1]*b[1]

def geometry(side,sq):
    walls=min(side/2-max(abs(x),abs(y))-(abs(u[0])+abs(u[1]))/2 for x,y,u,v in sq)
    least=None; pairs=0
    for i,(x,y,u,v) in enumerate(sq):
        for X,Y,U,V in sq[:i]:
            delta=(x-X,y-Y)
            separation=max(abs(product(delta,a)) for a in (u,v,U,V))
            threshold=(1+abs(product(u,U))+abs(product(u,V)))/2
            gap=separation-threshold
            least=gap if least is None else min(least,gap)
            if gap<0: raise ValueError('Overlapping squares')
            pairs+=1
    if walls<0: raise ValueError('Outside container')
    return dict(valid=True,pairs=pairs,wall_gap=str(walls),pair_gap=str(least),tolerance='0')

def audit_dual(side,sq,w):
    n=len(sq); choices=w['choices']; pcount=n*(n-1)//2
    if len(choices)!=pcount: raise ValueError('Incomplete separators')
    seen=set(); smallest=None
    for owner,other,axis,sign in choices:
        if not (0<=owner<n and 0<=other<n and owner!=other and axis in (0,1) and sign in (-1,1)): raise ValueError('Bad selector')
        pair=tuple(sorted((owner,other)))
        if pair in seen: raise ValueError('Duplicate selector')
        seen.add(pair)
        x,y,u,v=sq[owner]; X,Y,U,V=sq[other]
        direction=tuple(sign*z for z in (u,v)[axis])
        margin=product(direction,(X-x,Y-y))-(1+abs(product(direction,U))+abs(product(direction,V)))/2
        smallest=margin if smallest is None else min(smallest,margin)
        if margin<0: raise ValueError('Infeasible selected separator')
    coeff=[Q(0) for _ in range(2*n)]; constant=Q(0); sidecoeff=Q(0)
    ids=w['dual_rows']; weights=list(map(Q,w['dual_weights']))
    rows=4*pcount+16*n
    if len(ids)!=len(weights) or len(set(ids))!=len(ids) or any(not 0<=k<rows for k in ids) or min(weights)<0: raise ValueError('Invalid multipliers')
    for row,weight in zip(ids,weights):
        if row<4*pcount:
            owner,other,axis,sign=choices[row//4]
            direction=tuple(sign*z for z in sq[owner][2+axis])
            a,b=SIGNS[row%4]; U,V=sq[other][2:]
            offset=tuple((a*U[k]+b*V[k])/2 for k in (0,1))
            constant+=weight*(product(direction,offset)-Q(1,2))
            for k in (0,1):
                coeff[2*other+k]+=weight*direction[k]
                coeff[2*owner+k]-=weight*direction[k]
        else:
            q=row-4*pcount; i=q//16; r=q%16; vertex=r//4; dim=(r%4)//2; sign=(-1,1)[r%2]
            a,b=SIGNS[vertex]; U,V=sq[i][2:]
            constant+=weight*sign*(a*U[dim]+b*V[dim])/2
            coeff[2*i+dim]+=weight*sign
            sidecoeff+=weight/2
    correction=sum(abs(c) for c in coeff)/2
    K=sidecoeff+correction
    if K<=0: raise ValueError('Nonpositive objective coefficient')
    low=-constant/K; gap=side-low
    if correction!=Q(w['residual_center_bound_correction']) or K!=Q(w['objective_coefficient']) or low!=Q(w['lower_bound']): raise ValueError('Dual metadata inconsistent')
    if not 0<=gap<Q(1498,10**48): raise ValueError('Restricted bound fails')
    return dict(valid=True,rows=rows,terms=len(ids),lower=str(low),upper=str(side),gap=str(gap),gap_float=float(gap),selected_separator_min=str(smallest))

def main():
    start=time.monotonic(); results=[]
    claims=json.loads((ROOT/'COMPARISONS.json').read_text())['claims']
    if [c['n'] for c in claims]!=[105,130,263,272,292]: raise ValueError('Bad claim inventory')
    for item in claims:
        side,sq,digest=load_pose(ROOT/item['witness'],item['n'])
        if side!=Q(item['upper_exact']) or side!=Q(item['upper_decimal']) or digest!=item['witness_sha256']: raise ValueError('Headline/identity mismatch')
        r=geometry(side,sq); r.update(n=item['n'],side=str(side),sha256=digest)
        for row in item['comparisons']:
            gain=Q(row['verified_ceiling'])-side
            if gain<=0 or gain!=Q(row['decrease']) or gain!=Q(row['decrease_decimal']): raise ValueError('Improvement mismatch')
        r['gain']=str(gain)
        if item['n']==105:
            r['restricted_dual']=audit_dual(side,sq,json.loads((ROOT/'restricted/n105-dual.json').read_text()))
        results.append(r); print('Independent support-function checker PASS:',item['n'],r['pairs'],flush=True)
    tiny=[(-Q(1,2),Q(0),(Q(1),Q(0)),(Q(0),Q(1))),(Q(1,2),Q(0),(Q(1),Q(0)),(Q(0),Q(1)))]
    geometry(Q(2),tiny)
    rejects=0
    for delta in (-Q(1,10**100),Q(1,10**100)):
        pose=list(tiny); s=pose[1];pose[1]=(s[0]+delta,*s[1:])
        try: geometry(Q(2),pose)
        except ValueError: rejects+=1
    if rejects!=2: raise ValueError('Negative controls failed')
    summary=dict(valid=True,results=results,negative_controls=rejects,wall_seconds=time.monotonic()-start,method='Exact center/support-function separation; no package code imported')
    (OUT/'support-checker.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('ALL PASS',summary['wall_seconds'],flush=True)

if __name__=='__main__': main()
