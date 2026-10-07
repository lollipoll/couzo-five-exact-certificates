# Exact certificate refinements of five Couzo square packings

[Release v1.0.0](https://github.com/lollipoll/couzo-five-exact-certificates/releases/tag/v1.0.0) includes the unchanged reviewed archive, SHA256 sidecar and fresh verification receipts. [Registration issue #425](https://github.com/jlevy/squares/issues/425) requests review for n105, n263 and n292; register review is pending.

Five exact rational upper-bound witnesses for **n = 105, 130, 263, 272, 292**, refining Francisco Couzo’s constructions. No new arrangement or unrestricted optimality is claimed.

**Publication comparison, 7 October 2026:** only **105, 263 and 292** qualify for ceiling requests against the retrieved records and source certificates. **130 is historical**, superseded by Nate Chaoweeraprasit’s SQUISH side `6701628168660175/562949953421312`. **272 is also historical**, superseded by Evan Daniel’s source certificate at `2121013768221200063125669904449/125000000000000000000000000000`; the retrieved register case still lists an older bound. Both smaller certificates passed the retained support-function check during publication preparation. See [exact comparisons and provenance](PUBLICATION_STATUS.json).

The [reviewed scientific package](reviewed/README.md) is preserved byte for byte, including its dated comparisons and original drafts. The publication update above and [registration draft](publication/drafts/FRONTIER_SUBMISSION.md) supersede their publication-status wording. The downloaded reviewed archive is preserved unchanged for the release asset.

Reproduce offline with Python 3.11+ and its standard library, with assertions enabled:

```sh
cd reviewed
python3 verify.py
python3 code/review_support.py
```

The [reproduction guide](reviewed/REPRODUCIBILITY.txt), [review report](reviewed/EXTERNAL_REVIEW.txt), and [fresh verification receipts](publication/receipts/) describe all checks. The package’s three geometry implementations and additional support-function implementation passed all five witnesses. The ChatGPT/Codex implementation review is not human peer review or verification by the register.

Credit: **Francisco Couzo** for all five starting constructions; **Evan Daniel** for intervening exact refinements, including newer n105/n292 certificates and the smaller n272 result; **Nate Chaoweeraprasit** for SQUISH’s smaller n130 result. [Methods and historical credit](reviewed/METHODS_AND_CREDIT.txt) name preceding authors and agent assistance. The n105 dual theorem fixes orientations and selected separators; it supplies **no unrestricted lower-bound change**.

[Existing licence notices](reviewed/LICENSE_NOTICES.txt) are retained. No blanket source licence is assigned. Daniel’s copied certificates retain his [MIT notice](publication/sources/daniel-LICENSE.txt); the refreshed register data is credited to Joshua Levy and the squares project.
