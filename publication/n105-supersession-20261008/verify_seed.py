"""Check a supplied [0,S]^2 rational half-angle seed with both exact checkers."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, importlib.util, json, sys

ROOT=Path(__file__).resolve().parent
def module(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'verifiers'/file)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj

def main():
    if sys.flags.optimize:raise RuntimeError('Run with assertions enabled.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--n',type=int,required=True)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    raw=args.certificate.read_bytes();source=json.loads(raw,parse_float=str)
    if type(source['n']) is not int or source['n']!=args.n or len(source['squares'])!=args.n:
        raise ValueError('Square inventory differs from externally specified n.')
    side=Q(source['s_exact'])
    adapted={'schema':'packing-n/exact-v1','n':args.n,'container_side':str(side),
             'squares':[{'x':str(Q(q['x'])-side/2),'y':str(Q(q['y'])-side/2),
                         't':str(Q(q['t']))} for q in source['squares']]}
    polygon=module('seed_polygon','polygon.py').verify(adapted,args.n)
    support=module('seed_support','support.py').check(adapted,args.n)
    if not polygon['valid_exact'] or not support['valid']:raise ValueError('Exact geometry check failed.')
    result={'valid':True,'source_sha256':hashlib.sha256(raw).hexdigest(),
            'n':args.n,'side':str(side),'adapter':'Translate centers by (-S/2,-S/2); preserve rational t.',
            'polygon':polygon,'support':support}
    output=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(output)
    else:print(output,end='')
if __name__=='__main__':main()
