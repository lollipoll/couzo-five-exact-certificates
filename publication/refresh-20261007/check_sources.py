"""Replay retrieved Daniel/SQUISH certificates using the retained support checker.

No decimal conversion: source (x,y,t) in [0,S]^2 becomes (x-S/2,y-S/2,t).
The half-angle map gives u=((1-t*t)/(1+t*t),2*t/(1+t*t)), v=(-u_y,u_x).
Every unit frame, wall and unordered pair is checked over Fraction, tolerance 0.
The checker is independent of the source producers; this adapter is not a new
independent geometry implementation. Run without -O / -OO.
"""
import argparse
import hashlib
import importlib.util
import json
import platform
import time
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled')
    ap = argparse.ArgumentParser()
    ap.add_argument('--support-checker', type=Path, required=True)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location('retained_support', args.support_checker)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    manifest = json.loads((args.root / 'source-manifest.json').read_text())
    results = []
    for source in manifest:
        path = args.root / source['file']
        if not (path.name.endswith('.cert') or path.name.endswith('.cert.json')):
            continue
        started = datetime.now(timezone.utc).isoformat()
        start = time.monotonic()
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == source['sha256'], f'Hash mismatch: {path}'
        if path.suffix == '.cert':
            lines = [line for line in raw.decode().splitlines() if line.strip() and not line.lstrip().startswith('#')]
            n, side = lines[0].split()
            n, side = int(n), F(side)
            poses = [tuple(map(F, line.split())) for line in lines[1:]]
        else:
            data = json.loads(raw)
            n, side = data['n'], F(data['s_exact'])
            poses = [tuple(map(F, row)) for row in data['squares']]
        assert type(n) is int and n > 1 and len(poses) == n and side > 0
        squares = []
        for x, y, t in poses:
            u = ((1-t*t)/(1+t*t), 2*t/(1+t*t))
            v = (-u[1], u[0])
            assert u[0]**2+u[1]**2 == v[0]**2+v[1]**2 == 1
            assert u[0]*v[0]+u[1]*v[1] == 0
            squares.append((x-side/2, y-side/2, u, v))
        report = module.geometry(side, squares)
        assert report['valid'] and report['pairs'] == n*(n-1)//2 and report['tolerance'] == '0'
        results.append(dict(**source, n=n, side=str(side), unit_frames_checked=n,
                            **report, started_utc=started, seconds=time.monotonic()-start))
        print(path.name, n, 'PASS', report['pairs'], str(side), flush=True)
    # The actual retained geometry must accept contact and refuse exact tiny defects.
    u, v = (F(1), F(0)), (F(0), F(1))
    touching = [(-F(1,2), F(0), u, v), (F(1,2), F(0), u, v)]
    module.geometry(F(2), touching)
    rejected = 0
    for dx in (-F(1,10**100), F(1,10**100)):
        bad = [touching[0], (touching[1][0]+dx, F(0), u, v)]
        try:
            module.geometry(F(2), bad)
        except ValueError:
            rejected += 1
    assert rejected == 2
    receipt = dict(valid=True, python=platform.python_version(), assertions_enabled=__debug__,
                   method=__doc__, support_checker_sha256=hashlib.sha256(args.support_checker.read_bytes()).hexdigest(),
                   adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   controls={'touching_accepted': True, 'overlap_and_wall_1e-100_rejected': rejected}, results=results)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2)+'\n')


if __name__ == '__main__':
    main()
