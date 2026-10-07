**Claim.** Please review the exact finite-witness upper bounds for n = **105, 263 and 292** below as ceiling refinements of existing Couzo constructions, against the dated 7 October 2026 refresh. No new arrangement or unrestricted optimality claim is made. Our n130 and n272 certificates accompany the work only as historical refinements; **do not replace a smaller bound with either**.

| n | Exact witness side (terminating decimal) | Request |
| --- | --- | --- |
| 105 | `10.80607786551970463257490535044771520398745274` | Ceiling review |
| 130 | `11.911187706535762355538876013812043902764970249` | Historical support only |
| 263 | `16.742270262025057558060247617073276618363915907` | Ceiling review |
| 272 | `16.968165867852158332724454987487270539732089833` | Historical support only |
| 292 | `17.597249391156465040471442005510391858592626557` | Ceiling review |

The freshly retrieved register columns and source certificates differ:

| n | Retrieved register ceiling | Smallest retrieved source/register side |
| --- | --- | --- |
| 105 | `1350759733192571/125000000000000` | `5403038932759852316341483064551/500000000000000000000000000000` |
| 130 | `6701628168660175/562949953421312` | `6701628168660175/562949953421312` |
| 263 | `3348454052405011536751578555669/200000000000000000000000000000` | `3348454052405011536751578555669/200000000000000000000000000000` |
| 272 | `8484082933926079166447068323083/500000000000000000000000000000` | `2121013768221200063125669904449/125000000000000000000000000000` |
| 292 | `17597249391199519/1000000000000000` | `8798624695578232520323707249711/500000000000000000000000000000` |

In particular, n130 is superseded by SQUISH’s exact `6701628168660175/562949953421312`. n272 is superseded by [Evan Daniel’s current certificate](https://github.com/evand/square-packing/blob/1b7e2cbebca0a0b26418d9210793b10c7c14da53/search/exact/results/sw2/rd1_n272.cert), exact side `2121013768221200063125669904449/125000000000000000000000000000`, although the retrieved n272 case still shows the older ceiling. Both smaller source certificates passed the reviewed support-function checker locally. No ceiling change for our n130 or n272 is requested.

The n105/n292 witnesses are also below Daniel’s newer source certificates, by approximately 1.08061e-19 and 1.75972e-19 respectively; n263 is below its retrieved ceiling by approximately 1.25698e-16. Exact differences, full witness fractions, hashes and source links are in PUBLICATION_STATUS.json at the source revision below. If the register or sources have changed since this refresh, please treat any no-longer-improving certificate as dated historical evidence, retaining the smaller ceiling.

**Certificate.** [Repository](https://github.com/lollipoll/couzo-five-exact-certificates), source revision `bc389ddf7d65277cd19a9b08fb285d86346d6806`; [release v1.0.0](https://github.com/lollipoll/couzo-five-exact-certificates/releases/tag/v1.0.0); [unchanged reviewed archive](https://github.com/lollipoll/couzo-five-exact-certificates/releases/download/v1.0.0/couzo-five-exact-reviewed-20261007.tar.gz); [SHA256 sidecar](https://github.com/lollipoll/couzo-five-exact-certificates/releases/download/v1.0.0/couzo-five-exact-reviewed-20261007.tar.gz.sha256); [verification receipts](https://github.com/lollipoll/couzo-five-exact-certificates/releases/download/v1.0.0/couzo-five-exact-verification-receipts-20261007.tar.gz).

Archive SHA256: `d1185848ddac327f0ed8bf7f7d458e065362b47f1989c75e4b4cab2146de1614`. Five witnesses contain rational centers `(x,y)` and half-angle parameters `t`. The exact half-angle map gives orthonormal unit frames; exact containment and separating axes prove all required pairs disjoint in their interiors. Touching is allowed. No blanket licence is assigned; existing notices accompany the files.

**Checking.** Extract the release archive, then run:

```sh
cd couzo-five-exact-reviewed-20261007
python3 verify.py
python3 code/review_support.py
```

Python 3.11+ standard library, assertions enabled, offline. The fresh publication replay used Python 3.12.3: `verify.py` passed in 173.13 seconds, with 146 static hashes, 15 geometry decisions, 382,920 pair tests, all containment checks, ten controls per implementation, three preserved historical comparison epochs, and the separately scoped n105 dual. The retained `independent_verify.py` and `published_verify.py` reconstruct polygons separately; `legacy_exact_verify.py` uses center/basis projections. Their pair inventories are respectively 5,460, 8,385, 34,453, 36,856 and 42,486 for the five counts. The additional `review_support.py` replay passed all 127,640 pairs, exact containment and unit frames, near-boundary controls and independent dual reconstruction in 9.21 seconds. All deciding arithmetic is Python integer/Fraction arithmetic with zero acceptance tolerance. Logs and machine-readable receipts are attached to the release.

**What the checkers share.** The witness schema, rational half-angle parameterization, separating-axis theorem, Python interpreter and Fraction arithmetic. The first three are retained agent-assisted campaign implementations, not three outside reviewers. The support-function implementation imports no campaign geometry code; this publication run reruns it rather than claiming another independently authored checker. `publication/check_refreshed_sources.py` reuses that same support checker for the refreshed Daniel/SQUISH sources, with an exact coordinate translation.

**Not done.** No human peer review, proof-assistant formalization, independent arithmetic hardware check, worldwide-priority survey, new discovery replay, unrestricted optimality proof or register-side verification is claimed. The completed external ChatGPT/Codex implementation review and its original receipts are in EXTERNAL_REVIEW.txt and REVIEW_STATUS.json. The refreshed older Couzo corner certificates were acquired and matched to the register’s digests and exact sides; their old geometry was not replayed here. Pinned-ref shell downloads failed; ordinary authenticated default-branch case downloads succeeded and are retained by SHA256, with the register HEAD observed as `be8172aa3d4dec86b62b38c0779a8c83332e5251` before and after. The n272 register/source mismatch is explicit. Current claims are restricted to this dated retrieved evidence.

The n105 theorem fixes every orientation and recorded directed separator while allowing centers to vary: `U - 1498/10^48 < L_* <= U` in that restricted family. Its 103-term dual checks 23,520 halfplanes. **Do not enter this theorem into the unrestricted s(105) lower-bound column. No unrestricted lower-bound change is requested at any count.**

**Lineage and credit.** Francisco Couzo supplied all five starting constructions. Evan Daniel supplied intervening exact certificate refinements (the retained October 5 n263/n272 ceilings and newer n105/n130/n292 certificates) and the smaller current n272 certificate. Nate Chaoweeraprasit’s SQUISH supersedes n130. Historical catalogue credit includes Thomas Schadt, David Ellsworth, David W. Cantrell, Erich Friedman, Lars Cleemann, M.Z. Arslanov, S.A. Mustafin, Z.K. Shangitbayev, Tej Stead and Karoly Hajba; Tej Stead’s entry also credits Claude Fable 5. The package’s METHODS_AND_CREDIT.txt maps these credits to counts and does not assert a square-by-square identity with every older construction. Joshua Levy and the squares project maintain the comparison register.

**AI assistance.** The local refinement campaign, rational export, package/checker tooling, publication preparation and this submission were assisted by Codex. The separate ChatGPT implementation review supplied the support-function checker and reviewed the five witnesses; it was not human peer review. Constructor/source credits remain distinct from agent-assisted certificate refinements. No verification by jlevy/squares is claimed before its own import process.
