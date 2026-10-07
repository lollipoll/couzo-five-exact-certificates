# SQUISH certs

certified packings of n unit squares in a square, found with SQUISH (SQuare-packing Using Iterative Shrink-Hopping), with exact rational certificates and the outputs of checks run. registration request: [jlevy/squares#401](https://github.com/jlevy/squares/issues/401)

## current packings

our smallest certified packing for each n, against the best known side before ours (from the [Squares Project tracker](https://jlevy.github.io/squares/), read 2026-10-07; where the tracker already lists our packing, the one before it):

| n | our side | best known before ours | below it by | status | certificate |
|---|---|---|---|---|---|
| 88 | 9.882451030482 | 9.888153053759 (Kingbird catalogue) | 5.702e-03 | submitted | [`2026-10-07b/n088`](squish-submission-2026-10-07b/n088/) |
| 108 | 10.909940073445 | 10.925919390161 (Kingbird catalogue) | 1.598e-02 | registered (an earlier packing of ours) | [`2026-10-07b/n108`](squish-submission-2026-10-07b/n108/) |
| 123 | 11.600907778516 | 11.601384658376 (Francisco Couzo) | 4.769e-04 | submitted | [`2026-10-07/n123`](squish-submission-2026-10-07/n123/) |
| 126 | 11.773303606607 | 11.774735132388 (Kingbird catalogue) | 1.432e-03 | registered (an earlier packing of ours) | [`2026-10-07/n126`](squish-submission-2026-10-07/n126/) |
| 129 | 11.879375206711 | 11.881306218090 (Kingbird catalogue) | 1.931e-03 | registered (an earlier packing of ours) | [`2026-10-07/n129`](squish-submission-2026-10-07/n129/) |
| 130 | 11.904483032517 | 11.911187706549 (Francisco Couzo) | 6.705e-03 | registered | [`2026-10-06/n130`](squish-submission-2026-10-06/n130/) |
| 153 | 12.879679373333 | 12.881666757009 (Kingbird catalogue) | 1.987e-03 | registered | [`2026-10-07/n153`](squish-submission-2026-10-07/n153/) |
| 154 | 12.926562245854 | 12.931663721167 (Francisco Couzo) | 5.101e-03 | registered (an earlier packing of ours) | [`2026-10-07/n154`](squish-submission-2026-10-07/n154/) |
| 155 | 12.952503202605 | 12.955619592134 (Francisco Couzo) | 3.116e-03 | registered (an earlier packing of ours) | [`2026-10-07/n155`](squish-submission-2026-10-07/n155/) |
| 179 | 13.883795490512 | 13.895341069976 (Kingbird catalogue) | 1.155e-02 | submitted | [`2026-10-07b/n179`](squish-submission-2026-10-07b/n179/) |
| 180 | 13.917653417451 | 13.927888140498 (Francisco Couzo) | 1.023e-02 | registered (an earlier packing of ours) | [`2026-10-07b/n180`](squish-submission-2026-10-07b/n180/) |
| 199 | 14.617572173598 | 14.618988956899 (Francisco Couzo) | 1.417e-03 | submitted | [`2026-10-07b/n199`](squish-submission-2026-10-07b/n199/) |
| 207 | 14.887992258308 | 14.893954634237 (Francisco Couzo) | 5.962e-03 | submitted | [`2026-10-07b/n207`](squish-submission-2026-10-07b/n207/) |
| 208 | 14.924518772033 | 14.926534459699 (Francisco Couzo) | 2.016e-03 | submitted | [`2026-10-07/n208`](squish-submission-2026-10-07/n208/) |
| 209 | 14.949617952202 | 14.953939011857 (Francisco Couzo) | 4.321e-03 | registered | [`2026-10-06/n209`](squish-submission-2026-10-06/n209/) |
| 236 | 15.867800839426 | 15.872219025607 (Francisco Couzo) | 4.418e-03 | submitted | [`2026-10-07b/n236`](squish-submission-2026-10-07b/n236/) |
| 237 | 15.903676235191 | 15.911191683002 (Francisco Couzo) | 7.515e-03 | submitted | [`2026-10-07/n237`](squish-submission-2026-10-07/n237/) |
| 238 | 15.926146857012 | 15.931725503591 (Francisco Couzo) | 5.579e-03 | registered (an earlier packing of ours) | [`2026-10-07/n238`](squish-submission-2026-10-07/n238/) |
| 239 | 15.949313169729 | 15.953819333481 (Francisco Couzo) | 4.506e-03 | submitted | [`2026-10-07/n239`](squish-submission-2026-10-07/n239/) |
| 258 | 16.563448002139 | 16.571067811865 (Kingbird catalogue) | 7.620e-03 | submitted | [`2026-10-07/n258`](squish-submission-2026-10-07/n258/) |
| 263 | 16.740419679539 | 16.742270262025 (Francisco Couzo) | 1.851e-03 | submitted | [`2026-10-07b/n263`](squish-submission-2026-10-07b/n263/) |
| 302 | 17.881306218096 | 17.885993892530 (Francisco Couzo) | 4.688e-03 | submitted | [`2026-10-07b/n302`](squish-submission-2026-10-07b/n302/) |
| 303 | 17.920312372920 | 17.924341009851 (Francisco Couzo) | 4.029e-03 | registered | [`2026-10-06/n303`](squish-submission-2026-10-06/n303/) |

## folders

| folder | contents |
|---|---|
| [`squish-submission-2026-10-06/`](squish-submission-2026-10-06/) | the first request (2026-10-06): 10 packings, n = 108, 126, 129, 130, 154, 155, 180, 209, 238, 303 |
| [`squish-submission-2026-10-07/`](squish-submission-2026-10-07/) | the first update (2026-10-07): 13 new or smaller packings, n = 123, 126, 129, 153, 154, 155, 179, 208, 237, 238, 239, 258, 263 |
| [`squish-submission-2026-10-07b/`](squish-submission-2026-10-07b/) | the second update (2026-10-07): 9 new or smaller packings, n = 88, 108, 179, 180, 199, 207, 236, 263, 302 |

earlier folders are never changed: when a smaller packing is found, it goes in a new folder, and the table above says which one is current.

## what the second update (2026-10-07b) changed

**new (5 n):** 88, 199, 207, 236, 302. none of these were in an earlier folder.

**smaller packings for 4 n**, which replace the ones in the earlier folders (those stay there, still valid but no longer our smallest):

| n | before (folder) | now | smaller by |
|---|---|---|---|
| 108 | 10.920658939403 (`2026-10-06`) | 10.909940073445 | 1.072e-02 |
| 179 | 13.891312565741 (`2026-10-07`) | 13.883795490512 | 7.517e-03 |
| 180 | 13.923635004252 (`2026-10-06`) | 13.917653417451 | 5.982e-03 |
| 263 | 16.740446480043 (`2026-10-07`) | 16.740419679539 | 2.680e-05 |

**unchanged:** every other count keeps the certificate in the folder the table above links.

## files in each `nNNN/` folder

| file | contents |
|---|---|
| `nNNN.cert.json` | the exact certificate: n unit squares with rational centres (x, y) and rational t = tan(θ/2), inside the box [0, s]², with `s_exact` the exact side as a fraction |
| `nNNN.cert.txt` | the same packing at 40 digits in David Ellsworth's text format (box centred at the origin): the input of his `check_packing.py` |
| `nNNN.cert50.txt` | the same at 50 digits, which the SVG is drawn from |
| `nNNN.svg` | a drawing of the packing |
| `nNNN_vs_record.png` | the packing beside the best known one |
| `check_packing_output.txt` | the output of `check_packing.py` on `nNNN.cert.txt` at ε = 1e-40 (VALID for every one) |

to check one yourself: `python check_packing.py nNNN.cert.txt` from inside its folder, with Ellsworth's `check_packing.py`.
