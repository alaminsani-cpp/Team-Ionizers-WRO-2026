# Criterion 4 — Systems thinking, decisions, risk register

This section distinguishes **discussed engineering reasoning** from **decisions actually made**. A development journal is stronger when it explains why a choice was made, what alternatives were considered, what was measured and what failed.

## Design decisions under consideration
| Topic | Alternative A | Alternative B | Motivation | Decision status |
|---|---|---|---|---|
| Main compute | Raspberry Pi 4 (8 GB discussed) | Raspberry Pi 5 (8 GB considered) | compute headroom vs power/mass/thermal budget | **TO VERIFY** |
| Control topology | Single SBC | SBC + ESP32 wired control | deterministic motor response vs complexity | **TO VERIFY** |
| Mobility | high output RPM | reduction to ~800 wheel RPM | torque/traction vs maximum speed | **TO VERIFY** |
| Sensor mounting | front LiDAR higher | front LiDAR low | wall scan coverage vs occlusion/sign height | **TO VERIFY** |
| Drive profile | one fixed profile | Safe/Medium/Max parameters | robustness vs lap time | **TO VERIFY** |
| Corner handling | immediate reactive steering | anticipation from range geometry | correction latency vs complexity | **TO VERIFY** |
| Vision | fixed color threshold | calibrated and tracked color/height | speed of development vs reliability | **TO VERIFY** |

## Risk table
| Risk | Observable symptom | Severity | Proposed mitigation | Evidence needed |
|---|---|---|---|---|
| White boundary / black wall return errors | unwanted steering / reversing | High | investigate range validity and recovery | error logs + actual fix |
| Unregulated 4S on 12 V drive | driver/motor stress | High | rated regulator and measured peak | electrical test |
| Pi brownout during servo transient | reboot / sudden loss of control | High | separate regulated rails, transient reserve | voltage scope logs |
| Long-running high-speed turns | tire slip, side contact | High | speed shaping, angle limits, grip tests | telemetry + video |
| Low 50 mm Surprise Rule sign | unrecognized modified marker | High | perspective-calibrated camera/height check | labeled real camera examples |
| High 150 mm sign appears inverted | obey wrong visible color | High | robust modified-sign classifier | 50/150 mm pass tests |
| Missing/mislabeled code | impossible to reproduce | High | publish original runnable software | build & run log |
| Photos/video missing | documentation points lost | Medium/High | capture full evidence | publicly accessible URLs |
| Historical commits missing | rule noncompliance | High | retain genuine old git history; disclose missing | git log |
| Battery / wire strain | resets, short circuits | High | secure mounts, fuse, strain relief | inspection & readings |

## Previously discussed issue: reverse loops
A white border / black corner detection problem was described in discussions; the team later reported it had been corrected. The *specific root cause, code fix, before/after measurements and timestamps are not in this archive*. To turn this into credible iteration evidence, include:
1. Exact configuration when fault was observed.
2. Evidence: timestamped scan, code revision, recorded video.
3. One or more competing hypotheses.
4. Actual correction — reference function and commit.
5. Repeat trials under comparable light and layout.
6. Remaining limitations and a fallback mode.

## Decision records
For each major final choice, add one short file or entry with: date, owner, requirement, alternatives, weighted tradeoff, measured evidence, final selection, affected files, and test results. Do not retroactively invent meeting notes or decision dates. New entries may be dated honestly at the time written.
