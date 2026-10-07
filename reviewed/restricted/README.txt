Separate restricted n105 lower-bound result

Let U be the side in ../witnesses/n105.json. Fix all 105 orientations to its
exact rational half-angle values. For every unordered pair, fix the directed
supporting edge recorded in n105-dual.json: owner, other square, axis u or v,
and sign. Require every vertex of the other square to lie outside that edge.
Allow ALL 210 center coordinates to vary and allow the container side L to
vary, subject to these pair inequalities and all wall inequalities.

For this restricted family, its infimum L_* satisfies
  U - 1498/10^48 < L_* <= U.
This does not fix centers or assume rigidity, and does not assert attainment
at U. The exact lower rational is stored as lower_bound in n105-dual.json.
The restrictions exclude neither other orientations nor alternate separators
from the unrestricted packing problem; this is not a lower bound for s(105).

The unchanged ../code/verify_fixed_angle.py reconstructs 4 inequalities per
pair plus 16 per square, totaling 23,520. Its 103 selected row weights are
nonnegative exact rationals. Their weighted sum is c.X+c_L L+b >= 0.
Containment implies |X_j| <= L/2, hence
  0 <= c.X+c_L L+b <= (c_L + ||c||_1/2)L+b.
The positive exact coefficient K=c_L+||c||_1/2 proves L >= -b/K. The residual
center coefficients are paid for; no numerical rank or KKT tolerance is used.
The primal witness satisfies every selected pair constraint and every wall.
The release driver checks the exact gap is nonnegative and below 1498/10^48,
checks row indices, and rejects a negative-weight control.

This theorem was retained in the original campaign and the user reports its
external ChatGPT review completed. Rechecking it here is local certification
replay. It is included separately from the five unrestricted upper bounds.
