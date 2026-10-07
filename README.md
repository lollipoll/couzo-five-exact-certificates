# Exact certificate refinements of five Couzo square packings

**Publication status corrected 7 October 2026, 23:18 UTC:** [issue #425](https://github.com/jlevy/squares/issues/425) requests ceiling review for **n=105 and n=292 only**. Our **n=130, n=263 and n=272** certificates are valid historical supporting work. Register review is pending.

| n | Current request | Comparison establishing status |
| --- | --- | --- |
| 105 | Ceiling review | Our exact witness is below Daniel's retrieved certificate by `1.0806077865428479601254726e-19`. |
| 130 | Historical support only | SQUISH: `6701628168660175/562949953421312`; exact replay, 8,385 pairs. |
| 263 | Historical support only; ceiling request withdrawn | Newer SQUISH: `9424018478849569/562949953421312`; exact replay, 34,453 pairs. |
| 272 | Historical support only | Daniel: `2121013768221200063125669904449/125000000000000000000000000000`; exact replay, 36,856 pairs. |
| 292 | Ceiling review | Our exact witness is below Daniel's retrieved certificate by `1.75972493911608141407373443e-19`. |

The newer [SQUISH n263 certificate](https://github.com/itsnaka/squish-certs/blob/e63e4e52b1728b6671b2f263c5e02a4aa79a39d3/squish-submission-2026-10-07b/n263/n263.cert.json) in [issue #422](https://github.com/jlevy/squares/issues/422) is smaller than ours by exactly `29609319780496598656674709139966634789451387/16000000000000000000000000000000000000000000000`. Its complete exact support-function replay passed. The same checker freshly confirmed [SQUISH n130](https://github.com/itsnaka/squish-certs/blob/e63e4e52b1728b6671b2f263c5e02a4aa79a39d3/squish-submission-2026-10-06/n130/n130.cert.json) and [Daniel n272](https://github.com/evand/square-packing/blob/6069054020e1c78a395aa90a689332b4a1e6e2cd/search/exact/results/sw2/rd1_n272.cert). The current register already shows an earlier SQUISH n263 result; the latest source is smaller still. See [all exact comparisons](PUBLICATION_STATUS.json) and [pinned sources, retrieval times and replay receipts](publication/refresh-20261007/README.md).

Refinement and certification work: **Seth Rehwaldt with assistance from OpenAI Codex**. **Francisco Couzo** supplied all five starting constructions. **Evan Daniel** supplied intervening exact refinements and the smaller n272 certificate; **Nate Chaoweeraprasit** supplied SQUISH's smaller n130 and n263 certificates. [Methods and historical credit](reviewed/METHODS_AND_CREDIT.txt) retain the earlier contributors. No new arrangement, worldwide discovery priority, human peer review, register acceptance or unrestricted optimality is claimed.

[Release v1.0.0](https://github.com/lollipoll/couzo-five-exact-certificates/releases/tag/v1.0.0) preserves the original reviewed archive, SHA256 sidecar and verification receipts. Its tag still targets `bc389ddf7d65277cd19a9b08fb285d86346d6806`. The [reviewed scientific package](reviewed/README.md), original archive bytes, attached asset hashes and original dated comparisons are unchanged. This is a publication-status correction, not a new scientific release. [The earlier 22:40 UTC status](publication/refresh-20261007/historical-publication-status-2240UTC.json) is retained as historical evidence.

Reproduce the five witnesses offline with Python 3.11+ and its standard library, assertions enabled:

```sh
cd reviewed
python3 verify.py
python3 code/review_support.py
```

From the repository root, replay the refreshed source certificates:

```sh
python3 -B publication/refresh-20261007/check_sources.py --support-checker reviewed/code/review_support.py --output /tmp/couzo-source-replays.json
```

The [reproduction guide](reviewed/REPRODUCIBILITY.txt), [implementation review](reviewed/EXTERNAL_REVIEW.txt), and [original successful receipts](publication/receipts/) describe the unchanged witness checks. Those receipts are reused by witness/checker hash; new source replay receipts are linked above. The ChatGPT/Codex review was not human peer review or register verification. The n105 dual theorem fixes orientations and selected separators: **no unrestricted lower-bound change is requested at any count**.

[Existing licence notices](reviewed/LICENSE_NOTICES.txt) are retained; no blanket source licence is assigned. Daniel's copied certificates retain his [MIT notice](publication/refresh-20261007/sources/daniel/LICENSE). Register snapshots are credited to Joshua Levy and the squares project.
