# Engineering Journal
## Team Ionizers | Bangladesh | WRO Future Engineers 2026

**Edition:** Documentation draft, 14 November 2026  
**Team leader:** Al Amin Sani  
**Competition:** International Final, Puerto Rico  
**Evidence status:** This journal was compiled from the team's discussed design and official rules. It is a structured **draft**, not an authenticated laboratory notebook. Original physical measurements, photos, source, dated design history, CAD and videos have **not** been supplied. All pending evidence is explicitly identified. It must be updated and reviewed by the team before being represented as a record of their actual implemented robot.

## Executive summary
Team Ionizers represents Bangladesh in the 2026 WRO Future Engineers International Final. The team's aim is to develop an autonomous four-wheeled steering vehicle capable of three-lap Open and Obstacle challenges, including sign-aware path planning and parking. In discussions the team explored a Raspberry Pi 4 to Raspberry Pi 5 upgrade, an ESP32 low-level controller, RPLIDAR C1, Pi camera, geared motor, steering servo, wheel encoder, IMU and battery options. Target times of 18–20 seconds (Open) and under 30 seconds (Obstacle) are **targets, not verified results**. The documented V2 ideas emphasize tight-turn capability, low mass and torque-sensitive speed selection. The actual final hardware, software and achieved performance are not yet available to this journal.

This journal is structured to match the five 2026 evaluation criteria: mobility and mechanical design; power and sensor architecture; software and obstacle strategy; systems thinking and engineering decisions; and reproducibility/GitHub quality. We also include the revised November 2026 optional modified traffic-sign rule. The overall technical ambition is coherent, but a defensible judging score depends on genuine experimental proof and original program publication, not documentation length.

## 1. Engineering mission and constraints
The 2026 Future Engineers track requires the vehicle to autonomously complete three laps under randomized directions, start positions and track layouts. The vehicle must have four wheels, one physically connected driving axle and distinct steering; differential drive is prohibited. The maximum allowed dimensions are 300 × 200 × 300 mm, and maximum weight is 1.5 kg. Wireless functions must be disabled during official runs; only wired onboard component communication is allowed. Open driving requires legal completion and stopping. The obstacle event requires correct red/right and green/left passage plus parking. A printed journal and a public GitHub documentation repository form part of the team's deliverables.

**Measured current robot dimensions, weight, speed and final validated sensor set: TO VERIFY.** The proposed architecture is evaluated below as a design record, not as proof of built hardware.

## 2. Mobility and mechanical design
Our discussed mobility direction favors sharp steering, low rotational inertia and favorable drive torque. A 54 mm wheel and approximate motor speed of 1300–1360 RPM were considered, with a proposed 800 RPM output target at the wheel. If the motor is at 1360 RPM and the wheel target is 800 RPM, the external ratio would be 1.70:1; with 1300 RPM it would be 1.625:1. Confirm whether the motor's published RPM already includes a gearbox before specifying total gearing.

The ideal tangential wheel speed is `v = π D n / 60`. At D = 0.054 m and n = 800 RPM, v = 2.26 m/s. This value is theoretical; full-course completion depends on corner slowdowns, motor load, acceleration, available grip, voltage and steering geometry. A discussed approximate 18 m three-lap route requires average 0.9 m/s for 20 seconds or 1.0 m/s for 18 seconds, but real layouts have varied distances.

Proposed improvements include a sharper but bounded servo steering angle, thinner tires, reduced chassis mass and lower LiDAR mount. Each intervention has tradeoffs: larger wheel angles can cause scrub; narrower tires may reduce grip; a low-mounted sensor may lose tall/short object coverage; reduction gearing increases torque while limiting ideal top speed. We must provide genuine drawings, wheelbase measurements, turn radii, torque estimates, mount photos and controlled before/after tests for these discussions to count as verified engineering decisions.

**Required evidence:** actual dimensions, weight, motor marking, gear ratio, axle linkage, six-view photo set, custom CAD, steering geometry and repeatable turn/acceleration tests. **Evidence currently missing.**

## 3. Power and sensing architecture
A possible architecture places higher-level LiDAR/camera perception on a Raspberry Pi, with real-time actuator output on an ESP32 linked by wire. Candidate parts discussed include RPLIDAR C1, Pi camera, IMU/encoder, BTS7960 driver, MG90S steering servo and 4S LiPo. Pi 4 (8 GB) was discussed; Pi 5 (8 GB) was considered. Installed parts and exact models remain **TO VERIFY**. A true electronic schematic is not yet supplied.

Power distribution should isolate traction peaks from sensitive logic rails. A 4S LiPo candidate is nominal 14.8 V and reaches 16.8 V fully charged. A nominal 12 V motor must not be assumed compatible with direct raw pack power; actual motor and driver ratings, switching and regulation must be checked. The power budget requires measured idle and peak current for motor acceleration, steering under load, SBC, MCU and sensors. Without component selection and real readings, no total current or battery runtime claim is appropriate.

LiDAR can estimate clearance and corners but may return misleading ranges near reflective, black or white boundaries. Camera perception must cope with lighting changes, motion blur and different visible sign heights. IMU and encoder may stabilize heading/speed estimation if fitted and calibrated. Team discussion reported unwanted reversal loops near white boundary/black corner situations and later said the problem was fixed; the exact fix and tests have not been shared, so this is recorded as an **unverified but relevant engineering iteration**.

**Required evidence:** true circuit with net labels, converter/fuse ratings, pinmap, measured power budget, LiDAR positioning/calibration, camera calibration frames, sensor-failure tests and original software references. **Evidence currently missing.**

## 4. Software architecture and obstacle strategy
Proposed modules are: acquisition; LiDAR/camera perception; state estimation and corridor/section tracking; high-level trajectory choice; ESP32 motor/servo interface; watchdog/fault handling and testing logs. A proposed state machine has READY, INITIALIZE, FIND_DIRECTION, FOLLOW_STRAIGHT, CORNER, PASS_SIGN, LAP_COUNT, PARK and STOP states. The team's actual program and state transition logic have not been provided. The diagram included is a **proposal**, not an extracted program design.

Open Challenge would track walls, classify corners and section progression, control speed by curvature, and stop after three completed laps. The previously reported reverse-loop behavior near white borders and black corners makes stale/unreliable range handling an important test case. Safe, Medium and Max tuning profiles were discussed as a robustness/speed strategy; no actual code or profile values were supplied. The strategy cannot be claimed as implemented without verified config files and logs.

Obstacle Challenge must obey the 2026 rule: red signs passed on their right, green signs on their left. A plausible approach is camera-based class recognition with temporal stability, object tracking and clearance-aware path planning, with slowed approach when confidence is weak. Then a parking controller must place the car legally. The team must supply their true perception, planner and parking functions and test data, not invented algorithms.

The optional Surprise Rule published 9 November replaces one sign (not the first encountered) with a visible opposite-color sign of 50 or 150 mm height, compared with standard 100 mm. The passing side follows original color, so a robust system might infer the unusual height and reverse the usual visible-color choice. Participation is optional before each attempt. The rule adds up to 15 points; the official maximum overall rises to 137. Height classification has real camera geometry and low-LiDAR-height risks; this approach is a **proposed test direction** and has no asserted success result.

**Required evidence:** original source files for every controller, dependency versions, pin maps and serial protocols, true state machine, optical processing proof, corner/lap counter tests, obstacle and parking results, two autonomous YouTube videos. **Evidence currently missing.**

## 5. Systems thinking, tradeoffs and lessons
The project sits at the intersection of mechanical design, sensor placement, computational power, battery supply and reliable control. Faster wheel RPM increases possible straight speed but can worsen corner overshoot. Lower mass aids acceleration but poor stiffness affects camera/LiDAR geometry. Separating real-time control onto an MCU may reduce actuator jitter but adds protocol and power failure modes. A Pi 5 may provide performance headroom relative to Pi 4 while creating additional power and thermal requirements. A low LiDAR plane may improve wall scans but completely miss the short 50 mm Surprise Rule sign.

The most concrete user-reported engineering issue is a boundary/corner interpretation problem that caused reverse-loop behavior, later described as fixed. A complete journal must include the bad scan/camera evidence, the commit containing the actual fix, and repeated tests in the same lighting and track layouts. We cannot responsibly fill in a root cause or numerical improvement without original evidence. Maintain an explicit decision log and risk register, stored in separate documentation files.

Our testing philosophy should compare success rate, median time, p90 time, collision frequency, sign-passage compliance and legal final stopping, rather than quoting only a fastest single run. Proposed tests include varied start positions, both race directions, corridor widths, lighting, low/full battery, mixed sign colors, close sign spacings, parking entry offsets and 50/100/150 mm targets. Log both failed and successful attempts. No experimental results have been invented.

## 6. Reproducibility and GitHub quality
The documented repository layout includes a main README exceeding 5000 characters, an engineering journal in Markdown and printable PDF, `src/` folders for both controllers, conceptual diagrams, CSV forms for actual wiring/BOM and testing, vehicle/team media folders and a rules checklist. The repository must be upgraded with genuine final hardware evidence, original competition source, CAD and electrical schematics, two real videos of at least 30 seconds of autonomous driving (one per challenge), and current vehicle photographs from all six sides plus a team photograph.

The original WRO 2026 regulations require meaningful code commits with genuine dates at least two months, one month and two weeks before the competition. **A new ZIP on 14 November cannot create those past commits.** Preserve existing real commit history if it exists, and disclose gaps honestly. A separate team email states that a repository URL and robot profile must be submitted to the National Organizer by 14 November 2026. The repository must be public and remain accessible at least 12 months after the International Final, and a hard copy of the journal is required.

The present archive is intended to reduce documentation work quickly without misrepresenting the robot. Full reproducibility remains blocked pending original programs, actual wiring and physical build evidence. The launch checklist in `START_HERE.md` identifies the remaining tasks.

## 7. Evidence-to-rubric crosswalk
| WRO criterion | Evidence in this draft | Missing evidence for stronger score |
|---|---|---|
| Mobility / mechanical | formulas, change proposals, tradeoffs | final chassis dimensions/CAD, measured steering and gear tests |
| Power / sensors | conceptual architecture, risk reasoning | actual pin-level schematic, sensor calibration, measured power |
| Software / obstacle | state diagram, proposed mission flows, Surprise Rule plan | original runnable source, logged state transitions, real tests |
| Systems / decisions | candidate alternatives, risk list, earlier issue context | genuine dated decision records and before/after proof |
| Reproducibility / GitHub | detailed README, structured archive, checklist, printable journal | original code/CAD, real photos/videos, authentic past Git history |

## 8. Immediate next additions
1. Confirm actual Pi/ESP32/drive/steering parts and materials in the robot profile.
2. Copy original competition code and configuration; link architecture description to real functions.
3. Add accurate wiring and dimensioned CAD, plus physical six-view and team images.
4. Upload YouTube Open and Obstacle 30-second autonomous demonstrations.
5. Add genuine timed logs, before/after iteration evidence, and final challenge performance.
6. Publish public repository, retain original commit history, send link/profile to organizer, prepare printed hard copy.

## Reference documents
- World Robot Olympiad, 2026 Future Engineers General & Game Rules, particularly §7, §11 and Appendix C: https://wro.ba/wp-content/uploads/2026/01/WRO-2026-Future-Engineers-Self-Driving-Cars-General-Rules-Final-1.pdf
- WRO, Future Engineers Surprise Rule, version 9 November 2026: https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Extra-Task.pdf
- WRO 2026 Season: https://wro-association.org/competition/2026-season/
- WRO Q&A: https://wro-association.org/competition/questions-answers/

*End of engineering journal draft. All technical claims must be checked by Team Ionizers before public submission.*
