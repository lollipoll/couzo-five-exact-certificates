#!/usr/bin/env python3
"""Offline exact certification replay. Python 3.11+ standard library only."""
import sys
sys.dont_write_bytecode = True
if not __debug__:
    raise SystemExit('Refusing optimized Python: retained checkers use assertions. Run python3 verify.py.')

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import time

ROOT = Path(__file__).resolve().parent
EXPECTED_COUNTS = (105, 130, 263, 272, 292)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local(name):
    p = (ROOT / name).resolve()
    require(p.is_relative_to(ROOT), 'Path outside package: ' + name)
    return p


def read(name):
    return json.loads(local(name).read_text(), parse_float=str)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(out, name, value):
    p = out / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2) + '\n')


def hashes():
    rows = local('SHA256SUMS').read_text().splitlines()
    seen = set()
    for row in rows:
        expected, name = row.split('  ', 1)
        require(name not in seen, 'Duplicate hash entry')
        require(digest(local(name)) == expected, 'Hash mismatch: ' + name)
        seen.add(name)
    # Check every proof input before importing the retained code.
    for name in ['verify.py', 'CONTROLS.json', 'COMPARISONS.json', 'INPUTS.json',
                 'restricted/n105-dual.json']:
        require(name in seen, 'Unhashed input: ' + name)
    for name in ('independent_verify', 'published_verify', 'legacy_exact_verify', 'verify_fixed_angle'):
        require('code/' + name + '.py' in seen, 'Unhashed checker')
    for n in EXPECTED_COUNTS:
        require(f'witnesses/n{n}.json' in seen, 'Unhashed witness')
    for row in read('INPUTS.json')['copied_files']:
        require(digest(local(row['path'])) == row['sha256'], 'Original input hash mismatch')
    return len(rows)


def inventory(data, n):
    require(type(n) is int and n > 0, 'External positive count required')
    require(data['schema'] == 'packing-n/exact-v1', 'Unexpected schema')
    require(type(data['n']) is int and data['n'] == n == len(data['squares']), 'Wrong inventory')
    require(F(data['container_side']) > 0, 'Nonpositive container side')
    for q in data['squares']:
        for k in ('x', 'y', 't'):
            require(isinstance(q[k], str), 'Rational coordinate string required')
            F(q[k])


def table_rows(text):
    result = {}
    for line in text.splitlines():
        match = re.search(r'\| \[`(\d+)`\]', line)
        if match:
            fields = line[line.index('|'):].split('|')
            result[int(match[1])] = (fields[2].strip().strip('`'), fields[3].strip().strip('`'))
        else:
            # Original rendered GitHub responses replace the first-column
            # Markdown link with a citation marker; retain the same tokens.
            match = re.search(r'†`(\d+)`[^|]*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`', line)
            if match:
                result[int(match[1])] = (match[2], match[3])
    return result


def comparisons(claim):
    n = claim['n']
    data = read(claim['witness'])
    inventory(data, n)
    U = F(data['container_side'])
    require(U == F(claim['upper_exact']) == F(claim['upper_decimal']), 'Headline decimal mismatch')
    require(digest(local(claim['witness'])) == claim['witness_sha256'], 'Witness identity mismatch')
    source = local(claim['source_file'])
    require(digest(source) == claim['source_sha256'], 'Source hash mismatch')
    header = re.search(r'# s = (\S+)', source.read_text()).group(1)
    require(header == claim['source_reported_header'], 'Source header mismatch')
    continuation = table_rows(local('sources/historical/continuation/STATUS-table-extracted.txt').read_text())
    require(len(continuation) == 324, 'Incomplete historical table')
    historical = {
        'original-campaign': read('sources/historical/original/comparison_targets.json'),
        'continuation': read('sources/historical/continuation/comparison_targets.json'),
    }
    require([r['epoch'] for r in claim['comparisons']] == ['original-campaign', 'continuation', 'release-refresh'], 'Missing comparison epoch')
    for row in claim['comparisons']:
        snapshot = local(row['snapshot'])
        require(digest(snapshot) == row['snapshot_sha256'], 'Snapshot hash mismatch')
        R = F(row['verified_ceiling'])
        require(R == F(row['verified_ceiling_decimal']), 'Ceiling decimal mismatch')
        require(R - U == F(row['decrease']) == F(row['decrease_decimal']) > 0, 'Exact decrease mismatch')
        if row['epoch'] == 'release-refresh':
            recorded, ceiling = table_rows(snapshot.read_text())[n]
        else:
            target = historical[row['epoch']][str(n)]
            recorded, ceiling = target['reported_side'], target['verified_side']
            # The retained complete STATUS extraction independently binds these
            # unchanged dated values; earlier acquisition manifests are retained.
            require(F(ceiling) == F(continuation[n][1]), 'Historical table discrepancy')
            if row['epoch'] == 'original-campaign':
                snapshot_reported, snapshot_ceiling = table_rows(snapshot.read_text())[n]
                require(F(snapshot_reported) == F(recorded) and F(snapshot_ceiling) == F(ceiling), 'Original response discrepancy')
        require(F(recorded) == F(row['reported_upper']) and F(ceiling) == R, 'Source-column comparison mismatch')
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'verification-output')
    args = parser.parse_args()
    out = args.output.resolve()
    # Generated output cannot overwrite static proof material.
    if out.is_relative_to(ROOT):
        require(out == ROOT / 'verification-output', 'Inside package, use the default output directory')
    out.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    hash_count = hashes()
    print(f'PASS: {hash_count} package hashes and unchanged input hashes', flush=True)
    sys.path.insert(0, str(ROOT / 'code'))
    from independent_verify import exact_check
    from published_verify import verify as second
    from legacy_exact_verify import verify_exact as legacy
    from verify_fixed_angle import verify as dual

    def third(data, n):
        inventory(data, n)
        result = legacy(data)
        # Legacy loops enumerate all pairs but do not expose a runtime counter.
        result.update(externally_expected_n=n, pairs_by_loop_inventory=n*(n-1)//2,
                      pair_count_note='Derived from the two full loops in unchanged legacy source; not an instrumented counter.',
                      acceptance_tolerance='0')
        return result

    checkers = [('first', exact_check, 'valid'), ('second', second, 'valid_exact'), ('legacy', third, 'valid_exact')]
    claims = read('COMPARISONS.json')['claims']
    require(tuple(c['n'] for c in claims) == EXPECTED_COUNTS, 'Release inventory differs')
    records = []
    for claim in claims:
        data = comparisons(claim)
        n = claim['n']
        for label, checker, valid_key in checkers:
            t = time.monotonic()
            report = checker(data, n)
            require(report[valid_key], f'n{n} {label} invalid geometry')
            require(F(report['container_side']) == F(claim['upper_exact']), 'Checker side mismatch')
            if 'pairs_checked' in report:
                require(report['pairs_checked'] == n*(n-1)//2, 'Incomplete pair enumeration')
            if label == 'first':
                require(report['acceptance_tolerance'] == '0', 'Nonzero tolerance')
                require(report['wall_inequalities_checked'] == 16*n, 'Incomplete walls')
            report.update(witness_sha256=claim['witness_sha256'], checker_sha256=digest(ROOT/'code'/({'first':'independent_verify.py','second':'published_verify.py','legacy':'legacy_exact_verify.py'}[label])), seconds=time.monotonic()-t)
            save(out, f'n{n}-{label}.json', report)
            print(f'PASS: n={n}, {label}, all {n*(n-1)//2} pairs and containment, exact', flush=True)
        records.append(dict(n=n,upper_exact=claim['upper_exact'],sha256=claim['witness_sha256'],pairs_per_checker=n*(n-1)//2))

    controls = []
    for case in read('CONTROLS.json'):
        results = []
        for label, checker, valid_key in checkers:
            try:
                inventory(case['data'], case['expected_n'])
                accepted = bool(checker(case['data'], case['expected_n'])[valid_key])
            except (ValueError, AssertionError, KeyError, ZeroDivisionError):
                accepted = False
            require(accepted == case['accept'], f"Control {case['name']} failed with {label}")
            results.append(dict(checker=label,accepted=accepted))
        controls.append(dict(control=case['name'],expected=case['accept'],results=results))
    save(out, 'controls.json', controls)
    print(f'PASS: {len(controls)} controls on all three checkers', flush=True)

    data = read('witnesses/n105.json')
    witness = read('restricted/n105-dual.json')
    require(F(witness['certified_upper']) == F(data['container_side']), 'Dual upper mismatch')
    require(all(type(i) is int and 0 <= i < 23520 for i in witness['dual_rows']), 'Invalid dual row')
    report = dual(data, witness)
    require(report['valid'] and report['all_halfplanes_checked'] == 23520 and report['dual_terms'] == 103, 'Dual inventory failure')
    require(0 <= F(report['gap']) < F(1498,10**48), 'Restricted theorem gap failure')
    report.update(witness_sha256=digest(local('witnesses/n105.json')),dual_sha256=digest(local('restricted/n105-dual.json')))
    save(out, 'n105-restricted-dual.json', report)
    bad = copy.deepcopy(witness)
    bad['dual_weights'][0] = '-1'
    try:
        dual(data, bad)
    except (AssertionError, ValueError):
        pass
    else:
        raise ValueError('Negative dual multiplier was accepted')
    print('PASS: n105 restricted dual, 23,520 halfplanes, 103 terms; negative-weight control', flush=True)
    summary = dict(valid=True,kind='offline certification replay; not discovery replay or external review',claims=records,geometric_checker_passes=15,total_pair_tests=3*sum(r['pairs_per_checker'] for r in records),controls_per_checker=len(controls),restricted_dual=True,negative_dual_control=True,exact_comparison_epochs=3,package_hashes=hash_count,python_version=sys.version.split()[0],seconds=time.monotonic()-started)
    save(out, 'summary.json', summary)
    print('PASS: five exact upper bounds, historical/fresh exact comparisons, controls, and separately scoped n105 dual.', flush=True)


if __name__ == '__main__':
    main()
