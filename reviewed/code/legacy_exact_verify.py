#!/usr/bin/env python3
"""Independent verifier for packing-n/v1 and packing-n/exact-v1 files.

This file deliberately imports no optimizer or geometry code. It uses polygon-edge
axes for floating-point SAT and Fraction arithmetic for exact certificates.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
from typing import Any


def _vertices_float(q: dict[str, Any]) -> list[tuple[float, float]]:
    x, y, theta = float(q["x"]), float(q["y"]), float(q["theta"])
    c, s = math.cos(theta), math.sin(theta)
    u, v = (c, s), (-s, c)
    return [
        (x + (su * u[0] + sv * v[0]) / 2, y + (su * u[1] + sv * v[1]) / 2)
        for su, sv in ((-1, -1), (1, -1), (1, 1), (-1, 1))
    ]


def _axis_gap_float(a: list[tuple[float, float]], b: list[tuple[float, float]], axis: tuple[float, float]) -> float:
    pa = [x * axis[0] + y * axis[1] for x, y in a]
    pb = [x * axis[0] + y * axis[1] for x, y in b]
    return max(min(pb) - max(pa), min(pa) - max(pb))


def _pair_gap_float(a: list[tuple[float, float]], b: list[tuple[float, float]]) -> float:
    best = -math.inf
    for polygon in (a, b):
        for k in (0, 1):
            dx = polygon[k + 1][0] - polygon[k][0]
            dy = polygon[k + 1][1] - polygon[k][1]
            norm = math.hypot(dx, dy)
            axis = (-dy / norm, dx / norm)
            best = max(best, _axis_gap_float(a, b, axis))
    return best


def verify_float(data: dict[str, Any]) -> dict[str, Any]:
    side = float(data["container_side"])
    polygons = [_vertices_float(q) for q in data["squares"]]
    half = side / 2
    edge_errors = []
    wall_gaps = []
    for polygon in polygons:
        for k in range(4):
            x1, y1 = polygon[k]
            x2, y2 = polygon[(k + 1) % 4]
            edge_errors.append(abs(math.hypot(x2 - x1, y2 - y1) - 1.0))
        for x, y in polygon:
            wall_gaps.extend((x + half, half - x, y + half, half - y))
    pair_gaps = []
    worst_pair = None
    for i in range(len(polygons)):
        for j in range(i + 1, len(polygons)):
            gap = _pair_gap_float(polygons[i], polygons[j])
            pair_gaps.append(gap)
            if worst_pair is None or gap < worst_pair[2]:
                worst_pair = (i, j, gap)
    min_pair = min(pair_gaps, default=math.inf)
    min_wall = min(wall_gaps, default=math.inf)
    max_edge_error = max(edge_errors, default=0.0)
    # No tolerance is silently converted into validity: raw signs are reported.
    return {
        "mode": "independent_float_polygon_sat",
        "n": len(polygons),
        "container_side": side,
        "all_unit_sides_within_1e-12": max_edge_error <= 1e-12,
        "max_unit_side_error": max_edge_error,
        "minimum_wall_clearance": min_wall,
        "minimum_pairwise_separating_clearance": min_pair,
        "worst_pair": worst_pair,
        "valid_strict_float": max_edge_error <= 1e-12 and min_wall >= 0.0 and min_pair >= 0.0,
    }


def _f(value: Any) -> Fraction:
    if isinstance(value, dict):
        return Fraction(int(value["numerator"]), int(value["denominator"]))
    return Fraction(value)


def _vertices_exact(q: dict[str, Any]) -> tuple[list[tuple[Fraction, Fraction]], tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    x, y, t = _f(q["x"]), _f(q["y"]), _f(q["t"])
    den = 1 + t * t
    c = (1 - t * t) / den
    s = 2 * t / den
    u, v = (c, s), (-s, c)
    vertices = [
        (x + (su * u[0] + sv * v[0]) / 2, y + (su * u[1] + sv * v[1]) / 2)
        for su, sv in ((-1, -1), (1, -1), (1, 1), (-1, 1))
    ]
    return vertices, u, v


def _pair_gap_exact(a, au, av, b, bu, bv) -> Fraction:
    best = None
    for axis in (au, av, bu, bv):
        pa = [x * axis[0] + y * axis[1] for x, y in a]
        pb = [x * axis[0] + y * axis[1] for x, y in b]
        gap = max(min(pb) - max(pa), min(pa) - max(pb))
        best = gap if best is None else max(best, gap)
    assert best is not None
    return best


def verify_exact(data: dict[str, Any]) -> dict[str, Any]:
    side = _f(data["container_side"])
    items = [_vertices_exact(q) for q in data["squares"]]
    half = side / 2
    wall = [half - abs(c) for vertices, _, _ in items for vertex in vertices for c in vertex]
    gaps: list[Fraction] = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            gaps.append(_pair_gap_exact(*items[i], *items[j]))
    min_wall = min(wall, default=Fraction(10**9))
    min_pair = min(gaps, default=Fraction(10**9))
    valid = min_wall >= 0 and min_pair >= 0
    return {
        "mode": "exact_rational_sat",
        "n": len(items),
        "container_side": str(side),
        "unit_directions_exact": True,
        "minimum_wall_clearance": str(min_wall),
        "minimum_pairwise_separating_clearance": str(min_pair),
        "valid_exact": valid,
    }


def verify_file(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text())
    if data.get("schema") == "packing-n/exact-v1":
        return verify_exact(data)
    return verify_float(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("packing")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = verify_file(args.packing)
    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n")
    return 0 if report.get("valid_exact", report.get("valid_strict_float", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())

