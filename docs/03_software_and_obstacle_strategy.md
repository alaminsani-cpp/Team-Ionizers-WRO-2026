# Criterion 3 — Software architecture and obstacle strategy

**Status:** Software architecture is a reasoned design proposal from team discussions. The repository has **no original competition control source** yet; do not state that the following algorithms have been implemented or validated.

## Proposed layered architecture

| Layer | Inputs | Outputs | Verification evidence |
|---|---|---|---|
| Acquisition | LiDAR scans, camera frames, IMU/encoder (if fitted) | time-stamped measurements | actual drivers + recorded data |
| Perception | range / pixels | corridor geometry, pillar color, confidence | validation video frames / metrics |
| State estimation | landmarks, heading, odometry | heading, section, lap confidence | logs vs known track |
| Planner | challenge mode, state, rules | target path and speed | code + plots / cases |
| Motor/steer control | desired trajectory, measured state | servo angle, motor command | low-level firmware + bench results |
| Safety | lost sensor data, watchdog, undervoltage | bounded stop | fault injection logs |

**Interface contract to supply:** message encoding, units, checksum, valid range, timestamp behavior, command timeouts, electrical UART/USB wiring, publish frequency, actuator ramp rate, code files and dependency versions. No guessed ESP32 GPIO assignment is included.

## Proposed state model

`POWER_OFF -> READY -> INITIALIZE -> FIND_DIRECTION -> FOLLOW_STRAIGHT / TAKE_CORNER / PASS_SIGN -> COUNT_LAP -> PARK or STOP -> HALT`

States and transition guards must be tested. A counter increment triggered solely by visual corner changes can be fooled by missed/duplicate corners; investigate correlation with known track sections, heading and odometry. Track start orientation and finish location carefully; 2026 rules provide precise completion/stop conditions.

## Open Challenge concept
1. Observe LiDAR walls and check scan validity.
2. Estimate lane center and upcoming corner; choose wall weighting appropriate for corridor width.
3. Use a bounded steering controller and preemptive speed shaping before the corner.
4. After turn exit, return to stable straight following.
5. Track sections/corners/laps, cross-check with heading and motion if those sensors are present.
6. On three completed laps, stop within the permitted region as required by the official rules.

**Risky edge cases:** black/white edge response, wall corner sudden discontinuity, sensor dropout, wheel slip, reverse-loop recovery, lateral position ambiguity and near-wall navigation. Which specific recovery strategies were finally coded is unverified.

## Obstacle Challenge concept
1. Detect candidate red/green pillar in camera and estimate relative position using vision, range, or their fusion.
2. Apply WRO passing-side requirement: red -> pass **right** of sign; green -> pass **left** of sign.
3. Generate curvature-limited path with a sufficient lateral margin and avoid touching signs.
4. Maintain object identities across frames; do not toggle plan on a single-color false positive.
5. After passing, return to a valid lane corridor. At lap completion, approach parking and execute a separately tuned parallel-parking maneuver.
6. Use uncertainty to lower speed before a difficult sign rather than driving blind.

**Important:** This is a candidate control pipeline and not proof of installed vision algorithms, a trained model or parking completion. Replace it with actual source-linked function descriptions and measurable results.

## Surprise Rule extension (November 2026)
For the optional modified sign, a nonstandard-height **50 mm or 150 mm** pillar appears with its color inverted relative to the original. The correct passing side follows the **original** color. A candidate algorithm is:

1. Detect color and object position with ordinary pipeline.
2. Estimate sign height relative to its distance and camera calibration; test against known 100 mm standards.
3. If high-confidence 50 or 150 mm, treat object as modified and **invert the visible color's required side**.
4. Otherwise apply ordinary red-right / green-left interpretation.
5. Treat uncertain height explicitly and decide before the attempt whether participating is responsible. The participation choice is given to judges before the attempt, not selected by the vehicle mid-round.

A LiDAR located above the top of a 50 mm object could miss it entirely; video-based height inference needs perspective correction and near-object visibility. Actual solutions must be tested to claim this capability.

## Control-loop considerations
- Constrain steering angle and command rate to avoid saturation.
- Smooth noisy measurements with bounded latency; over-filtering can cause missed corners.
- Limit acceleration and braking to avoid wheelspin and brownouts.
- Keep the safety stop independent of high-level perception where possible.
- Log all state transitions with timestamps and sensor confidence in bench trials.
- Parameter profiles Safe / Medium / Max are planned variants; finalize and version the real parameter files.

## Software-release reproducibility
Document OS distribution, compiler, firmware core and libraries, camera/LiDAR driver versions, image-processing libraries and calibration files **only once read from the actual controller**. Capture exact commands for flash and start. Store machine-readable environment freeze and checksums. Mark competition-ready commits with authentic tags, not fabricated backdated commit timestamps.
