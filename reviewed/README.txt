REVIEW UPDATE, 7 October 2026

All five witnesses passed the package replay and an additional independent
support-function checker; see EXTERNAL_REVIEW.txt and its retained receipts.
The public n130 case page now reports the smaller certified SQUISH side
6701628168660175/562949953421312 (safe display 11.9044830325168772). Our n130
certificate refines a superseded construction. Historical comparisons remain
unchanged as historical records. Refresh present comparisons before claiming
current frontier improvements; see PUBLICATION_STATUS.json.

This is a separately reviewed copy; the original uploaded archive is unchanged.
Run python3 verify.py for the original complete three-checker replay.
Run python3 code/review_support.py for the additional independent check.
Both require only the standard library and run offline.

Exact certificate refinements for five Couzo square packings
Local review draft, 7 October 2026

This package certifies upper bounds for n=105,130,263,272,292 unit squares
in a square. These are tighter exact certifications of existing Francisco
Couzo constructions, with contact polishing and export repair. Evan Daniel's
intervening October 5 refinements supply the comparison ceilings for n263
and n272. No new arrangement, worldwide priority, or unrestricted local or
global optimality is claimed.

From this extracted directory, run one command:

    python3 verify.py

Use ordinary Python 3.11 or later, with assertions enabled (not -O or -OO).
Only the standard library is used. No network, original project, optimizer,
installed package, or environment is needed. Allow several minutes. The
command verifies SHA256SUMS and original input hashes, all five witnesses
with three exact implementations, all three comparison epochs, ten controls
per checker, and the separately scoped n105 dual. Reports go to
verification-output/. It refuses optimized Python and fails on any mismatch.

Start with BOUNDS.txt for the full exact decimals, fractions and decreases.
COMPARISONS.json is the single authoritative five-count comparison manifest;
COMPARISONS.csv is a convenient rendering. Every headline decimal denotes
exactly the rational side in its complete witnesses/nN.json file.

All checks use zero tolerance and every unordered pair: respectively 5,460,
8,385, 34,453, 36,856 and 42,486 pairs per implementation, plus containment.
The first two checkers explicitly test unit edges and right angles; the
legacy checker constructs exact unit directions by the half-angle identity.
Its inventory is checked by the release wrapper. See METHODS_AND_CREDIT.txt
for shared assumptions and authorship; three implementations are not three
independent external reviews.

The external ChatGPT/Codex implementation review is now completed for all
five witnesses and the restricted n105 dual. See EXTERNAL_REVIEW.txt. This is
not human peer review or verification by the public register. The original
three packaged checkers remain unchanged; a fourth support-function checker
and its receipts are included separately.

Both historical October 7 comparison epochs and a fresh permitted web-reader
retrieval are saved. All five fresh ceilings are unchanged. Direct HTTP
retrieval failed DNS; the public HEAD could not be authenticated. Snapshots
are labelled web-reader responses/extractions, not raw upstream bytes. A
register's "verified" column is distinguished from its "reported" column
and from a source file's side header. Earlier public certificates were not
independently reverified in this release. See SOURCES_AND_REPAIRS.txt.

restricted/README.txt states the extra hypotheses for the n105 lower bound.
REPRODUCIBILITY.txt distinguishes this offline certification replay from the
continuation's retained numerical discovery replay. NEXT_RESEARCH.txt assesses
the completed screens; no new search campaign was run. drafts/ contains a
local announcement and proposed register submission, neither sent nor posted.
The separate n68 v1.1.0 result is referenced in SOURCES_AND_REPAIRS.txt and is
not changed or included as a sixth result.

INPUTS.json maps copied files to original project-relative paths and hashes.
Those paths record provenance, not runtime dependencies. SHA256SUMS covers
all static package files except itself; the archive has a separate sidecar
digest. Original scientific files and original hash manifests are unchanged.
Existing notices are retained; see LICENSE_NOTICES.txt for the limits of the
available licensing record. No new blanket license is asserted.
