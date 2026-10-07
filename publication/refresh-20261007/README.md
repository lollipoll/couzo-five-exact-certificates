# Publication refresh, 7 October 2026

Prepared at 2026-10-07T23:18:26.535004+00:00. Active requests in issue #425: **105 and 292**. Historical: **130, 263, 272**. No certificate, released archive or scientific claim has been altered.

[Source manifest](source-manifest.json) records the full Git commits, retrieval completion times, paths, immutable URLs and SHA256 values. Git fetch retrieved the source trees and `git show COMMIT:PATH` extracted the bytes without conversion. Relevant pending issues and comments are retained under `sources/`. The [exact status](../../PUBLICATION_STATUS.json) compares each witness with both the current register and retrieved source certificates. The smallest verified retrieved sources govern the request status.

The [source replay receipt](source-replays.json) records exact sides, minimum margins, all pair counts, source/checker hashes and times. [check_sources.py](check_sources.py) adapts rational source centers in `[0,S]^2` to centered coordinates by subtracting `S/2`; rational `t` is unchanged. It reconstructs `u=((1-t²)/(1+t²),2t/(1+t²))`, `v=(-u_y,u_x)` exactly and checks both unit norms and orthogonality. The retained `reviewed/code/review_support.py` then checks containment and **every unordered pair**, with no floating broad phase, symmetry omission or decimal tolerance. This checker imports no producer geometry code. Both rely on Python Fraction, the half-angle map and the separating-axis theorem.

From the repository root, Python 3.11+ standard library, no `-O`/`-OO`:

```sh
python3 -B publication/refresh-20261007/check_sources.py --support-checker reviewed/code/review_support.py --output /tmp/couzo-source-replays.json
```

SQUISH n263: exact `9424018478849569/562949953421312`, hash `8e32094d935b7445f98c889305ed8fd018f06c59f7d4bf8f7f0957a70a992e7c`, 263 unit frames, all walls and 34,453 pairs accepted in 1.217 seconds. Its printed decimal is not used as an exact ceiling. SQUISH n130: 8,385 pairs. Daniel's newer n272: 36,856 pairs. The adapter also replays the other retrieved Daniel certificates, including duplicate candidate paths; timings and decisions are bound to individual source files. Contact is permitted. Tiny exact overlap and wall-protrusion controls of size `10^-100` were rejected; exact touching was accepted.

[Reused witness checks](reused-witness-checks.json) bind the unchanged five released witnesses to the original successful receipts, including the independent support checker. The new replay is independent of the producers, but is a reuse of that implementation rather than another newly independent checker. No human peer review is claimed.

At register `2af487e7cfe85d84b2a67fa984e2d36a77548d97`, n263 already has SQUISH's earlier exact side `1688127953620802672872096218104440928487712119/100841274193809894793232914114737381771837440`; issue #422's newer source is still smaller. The register n272 ceiling still trails Daniel's verified retrieved source. Daniel's exact-form table leaves all six counts considered in this refresh open; its current rational certificates were compared separately. Couzo's six current decimal source headers were inspected as historical construction sources, not newly certified exact geometry.

Scope: public source heads and relevant pending issues retrieved on 7 October 2026; later, private or unindexed results are not ruled out. No optimization or discovery replay was run. [Historical status](historical-publication-status-2240UTC.json), [original issue body](sources/issue-425-original.json), and the reviewed package preserve the earlier comparisons. [Updated issue text](issue-425-update.md) and [editable release notes](release-notes-update.md) make only 105/292 active. No unrestricted lower-bound change is requested.
