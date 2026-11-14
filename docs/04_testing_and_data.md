# Criterion 3/4 — Test design, metrics and iteration

## Status
No original measurement logs or competition videos were provided for this archive. The below is a reproducible **planned test protocol**, not performed experiments.

## Data capture standard
Every row in `tests/trial_log_TEMPLATE.csv` is one genuine run. Record run ID; local timestamp; robot and software revision; Git commit; Open/Obstacle/Surprise; lighting type; battery start/end voltage; camera settings; start configuration; direction; profile; observed elapsed seconds; completed laps; sign mistakes; contacts; final stop and parking status; fault signature; tester; evidence URL and next change. Do not alter elapsed times after scoring.

## Minimum testing matrix
| Test | Variants | Useful measure |
|---|---|---|
| Motor/steering bench | 3 battery states × 3 speed commands | speed, overshoot, stall, temperature |
| Corner handling | clockwise/counterclockwise × inner wall layouts | completion %, collisions, average corner time |
| Border appearance | black wall, white boundary, reflections | false turns, reverse-loop count |
| Open Challenge | >=10 trials per selected profile/layout | full-run success %, median/p90 time |
| Color classification | red/green × near/far × light conditions | per-class precision/recall, wrong-side events |
| Obstacle spacing | single/two signs; both colors/orderings | clearance/contact events |
| Parallel parking | start offset/angle/battery variation | valid park %, final offset, elapsed time |
| Surprise sign | red and green, 50/100/150 mm, perspective/lighting | modified-sign recognition precision and correctness |
| Fault handling | remove LiDAR frames/serial link, simulate camera timeout | controlled stopping and recovery |

**These counts are recommendations, not claims of trials performed.** If using fewer runs because of time constraints, report the limitation and show actual N. Maintain raw logs and describe any discarded runs.

## Score-aware metrics
- `Full-run success rate = successful 3-lap runs / attempts`
- `Wrong-side rate = wrong-side pillar passages / total judged pillar passages`
- `Contact rate = collisions or sign moves / attempts`
- `Median`, `p90`, and `best` elapsed time from **completed valid** runs
- `Stop compliance rate = legal final stops / eligible runs`
- `Surprise modified-sign detection recall/precision` based on actual labeled frames and known signs

A 20-second race completed in only one of ten attempts may be less valuable than consistently legal 23-second attempts. Balance time and scoring with actual evidence; do not choose a profile solely on its single best run.

## Experiment record / iteration template

| Field | Fill from actual test |
|---|---|
| Observation | [e.g. wrong range near corner; only if observed] |
| Hypothesis | [cause based on evidence] |
| Controlled change | [one parameter, component or algorithm] |
| Baseline | [exact run IDs, N, median, failure count] |
| Comparison | [exact run IDs, same conditions, N] |
| Tradeoff | [what degraded when improvement made] |
| Decision | [accept/revert and reason] |
| Supporting files | [CSV, video, commit SHA] |

## Acceptance criteria before official run
Ensure measurement of size <300×200×300 mm, weight <=1.5 kg, four wheels and correct axle/steering, wireless disabled, correct start behavior, valid all-three-lap stopping, obstacle passing, parking, safe power delivery and distinct full video demos. Use judge rules, not an invented pass threshold.
