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
