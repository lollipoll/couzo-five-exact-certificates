**Publication correction — 7 October 2026, 23:18 UTC. Active ceiling requests: n=105 and n=292 only.** All five counts were refreshed against pinned public sources and relevant pending issues. Our n=130, n=263 and n=272 certificates remain valid historical supporting evidence; do not use them to replace smaller ceilings. Register review of this package remains pending.

| n | Current request | Comparison establishing status |
| --- | --- | --- |
| 105 | Ceiling review | Our exact witness is below Daniel's retrieved certificate by `1.0806077865428479601254726e-19`. |
| 130 | Historical support only | SQUISH: `6701628168660175/562949953421312`; exact replay, 8,385 pairs. |
| 263 | Historical support only; ceiling request withdrawn | Newer SQUISH: `9424018478849569/562949953421312`; exact replay, 34,453 pairs. |
| 272 | Historical support only | Daniel: `2121013768221200063125669904449/125000000000000000000000000000`; exact replay, 36,856 pairs. |
| 292 | Ceiling review | Our exact witness is below Daniel's retrieved certificate by `1.75972493911608141407373443e-19`. |

The newly replayed [SQUISH n=263 certificate](https://github.com/itsnaka/squish-certs/blob/e63e4e52b1728b6671b2f263c5e02a4aa79a39d3/squish-submission-2026-10-07b/n263/n263.cert.json) from [issue #422](https://github.com/jlevy/squares/issues/422) has SHA256 `8e32094d935b7445f98c889305ed8fd018f06c59f7d4bf8f7f0957a70a992e7c` and exact side `9424018478849569/562949953421312`. It is smaller than our n=263 witness by exactly `29609319780496598656674709139966634789451387/16000000000000000000000000000000000000000000000` (about 0.0018505824862810374). The register now carries SQUISH's earlier n=263 certificate; the pending newer source is smaller still.

[SQUISH n=130](https://github.com/itsnaka/squish-certs/blob/e63e4e52b1728b6671b2f263c5e02a4aa79a39d3/squish-submission-2026-10-06/n130/n130.cert.json) and [Daniel n=272](https://github.com/evand/square-packing/blob/6069054020e1c78a395aa90a689332b4a1e6e2cd/search/exact/results/sw2/rd1_n272.cert) also passed fresh exact replay. Every source unit frame, wall and unordered pair was checked by the retained independent support-function implementation, using integer/Fraction arithmetic and zero tolerance. The exact adapter translates source centers `(x,y)` to `(x-S/2,y-S/2)` and leaves rational half-angle parameters unchanged. This reuses an independent geometry implementation; it is not an additional independently authored checker or human peer review.

The source pins are register `2af487e7cfe85d84b2a67fa984e2d36a77548d97`, Daniel `6069054020e1c78a395aa90a689332b4a1e6e2cd`, Couzo `6042c56b43b64c09fe5a32c64879e698f399beaf`, and SQUISH `e63e4e52b1728b6671b2f263c5e02a4aa79a39d3`. [Dated source hashes, retrieval times, replay commands and receipts](https://github.com/lollipoll/couzo-five-exact-certificates/blob/main/publication/refresh-20261007/README.md); [all five exact comparisons](https://github.com/lollipoll/couzo-five-exact-certificates/blob/main/PUBLICATION_STATUS.json). These are comparisons to retrieved evidence, not a worldwide-priority assertion. Daniel's pending n=105/n=292 certificates were checked as well as the register columns.

Refinement work: **Seth Rehwaldt, with assistance from OpenAI Codex**. Francisco Couzo supplied the five starting constructions; Evan Daniel, Nate Chaoweeraprasit (SQUISH), and the earlier contributors documented in the package retain their respective credit. **No unrestricted lower-bound change is requested.**

The scientific package, v1.0.0 tag target, reviewed archive, attached assets and their hashes are unchanged. The original dated comparisons below are historical evidence; this correction governs the active requests.

<details>
<summary>Original v1.0.0 release notes — historical comparison and request wording</summary>

Exact rational certificate refinements of Francisco Couzo’s five existing square packings. The reviewed archive is unchanged; no new arrangement or unrestricted optimality is claimed.

**n130 is a historical refinement superseded by SQUISH** at `6701628168660175/562949953421312`. **n272 is also historical**, superseded by [Evan Daniel’s smaller source certificate](https://github.com/evand/square-packing/blob/1b7e2cbebca0a0b26418d9210793b10c7c14da53/search/exact/results/sw2/rd1_n272.cert) at `2121013768221200063125669904449/125000000000000000000000000000`. The retrieved n272 register case still lists its older ceiling. Only n105, n263 and n292 qualify for ceiling-review requests against the 7 October retrieved records and sources. Daniel’s newer n105/n292 certificates narrow the respective differences to about 1.08e-19 and 1.76e-19.

| n | Exact witness side (terminating decimal) | Request |
| --- | --- | --- |
| 105 | `10.80607786551970463257490535044771520398745274` | Ceiling review |
| 130 | `11.911187706535762355538876013812043902764970249` | Historical support only |
| 263 | `16.742270262025057558060247617073276618363915907` | Ceiling review |
| 272 | `16.968165867852158332724454987487270539732089833` | Historical support only |
| 292 | `17.597249391156465040471442005510391858592626557` | Ceiling review |

[Repository](https://github.com/lollipoll/couzo-five-exact-certificates), source commit `bc389ddf7d65277cd19a9b08fb285d86346d6806`. See its top-level PUBLICATION_STATUS.json for exact comparisons, retained snapshots and provenance; these update the status wording in the immutable reviewed package. [Reviewed archive](https://github.com/lollipoll/couzo-five-exact-certificates/releases/download/v1.0.0/couzo-five-exact-reviewed-20261007.tar.gz), [SHA256](https://github.com/lollipoll/couzo-five-exact-certificates/releases/download/v1.0.0/couzo-five-exact-reviewed-20261007.tar.gz.sha256), [verification receipts](https://github.com/lollipoll/couzo-five-exact-certificates/releases/download/v1.0.0/couzo-five-exact-verification-receipts-20261007.tar.gz).

Archive SHA256: `d1185848ddac327f0ed8bf7f7d458e065362b47f1989c75e4b4cab2146de1614`.

```sh
tar -xzf couzo-five-exact-reviewed-20261007.tar.gz
cd couzo-five-exact-reviewed-20261007
python3 verify.py
python3 code/review_support.py
```

Python 3.11+ standard library; offline with assertions enabled. The three packaged geometry implementations passed all five witnesses (15 decisions, 382,920 pairs), all controls and the separately scoped n105 dual in 173.13s. The additional independent support-function implementation passed all five witnesses (127,640 pairs) in 9.21s. Both smaller superseding source certificates also passed the reused support checker locally. The ChatGPT/Codex implementation review is not human peer review or register-side verification.

The n105 lower theorem fixes orientations and selected separators; **it is excluded from unrestricted lower-bound claims**.

Francisco Couzo supplied all five starting constructions. Evan Daniel supplied intervening exact certificate refinements (the retained October 5 n263/n272 ceilings and newer n105/n130/n292 certificates) and the smaller current n272 certificate. Nate Chaoweeraprasit’s SQUISH supersedes n130. Historical catalogue credit includes Thomas Schadt, David Ellsworth, David W. Cantrell, Erich Friedman, Lars Cleemann, M.Z. Arslanov, S.A. Mustafin, Z.K. Shangitbayev, Tej Stead and Karoly Hajba; Tej Stead’s entry also credits Claude Fable 5. The package’s METHODS_AND_CREDIT.txt maps these credits to counts and does not assert a square-by-square identity with every older construction. Joshua Levy and the squares project maintain the comparison register. Codex assisted the local campaign and publication; ChatGPT supplied the implementation review. Existing licence notices are retained; no blanket source licence is invented.

</details>
