# 2026 Surprise Rule — Modified Traffic Sign (dated 9 November 2026)

**Official source:** https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Extra-Task.pdf

## What is added
The optional modified traffic-sign task applies to an **Obstacle Challenge** attempt. Judges select one existing traffic sign **other than the first in the prescribed driving direction**. They replace it with a sign of the **opposite color**, **50 mm or 150 mm height** in place of the normal 100 mm. The **50×50 mm base and physical sign position stay the same**. Teams must tell the judge whether they opt in before the attempt.

## Critical passing rule
The modified marker must be obeyed according to its **original** color rather than its visible color. Ordinary signs continue using their visible color:

| Sign identity | Visible color | Height | Correct passing side |
|---|---|---|---|
| Normal | Red | 100 mm | **Right** of sign |
| Normal | Green | 100 mm | **Left** of sign |
| Modified, originally green | Red | 50 or 150 mm | **Left** of sign |
| Modified, originally red | Green | 50 or 150 mm | **Right** of sign |

The 15 extra points are 5 for each correct passage of the single modified sign, up to three, **even if not all laps are completed**. Passing on the wrong side is penalized under standard rules and can end the attempt. The maximum Obstacle Challenge score with this rule is **77**, and total is **137** (official document).

## Possible camera-led implementation plan — NOT VERIFIED
If the team opts in, a correctly designed perception system must distinguish visible color from *original color inferred from anomalous height*. A robust pipeline would estimate 3D size using camera geometry: collect camera intrinsics; establish lower and upper sign image points; estimate object distance or ground-plane scale; normalize observed height for perspective; classify into short/normal/tall with uncertainty; and only then decide whether to invert the passing side. Sensor placement and motion blur may make 50 mm objects challenging. Record false-positive/false-negative rates against 100 mm normal signs.

**Do not rely on these ideas as evidence that the feature is already working.** Test real printed sign heights and all four combinations before telling the judge you are participating.

## Proposed acceptance experiments
- At least three distances × two lighting conditions × two heights × two visible colors, plus 100 mm controls.
- Track camera view and LiDAR scan plane relative to 50 mm short signs.
- Measure detection latency versus available braking distance.
- Test two adjacent markers and sign occlusion.
- Verify when height is uncertain: team must choose a legally valid safety strategy and understand that no score can be guaranteed.

## Team operational choice
Surprise participation is optional and is decided before an official obstacle attempt. A failed modified-sign recognition can terminate a high-scoring standard run; choose based on verified evidence rather than possible maximum score. Keep program logic and actual training/calibration results in the original `src/` folders.
