# Criterion 1 — Mobility and mechanical design

## Mechanical problem
The Future Engineers car must be a four-wheeled vehicle with a mechanically connected driving axle and a separate steering actuation method. Differential-wheel steering is not permitted in the 2026 regulations. The challenge includes narrow and wide corridors, four corners per lap, changing track configurations and sign avoidance. These constraints reward low turning radius, predictable wheel grip, minimal lateral oscillation and repeatable stop distances more than theoretical top speed alone.

## Discussed V2 changes (design intentions — not a finalized build record)

1. **Sharper steering travel.** Greater usable wheel angle could shorten corner paths, but must be verified for linkage collision, servo load, tire scrub and understeer.
2. **Slimmer tires and lighter body.** The goal is to lower rolling resistance and rotational inertia, while retaining corner grip and structural stiffness; actual tradeoffs require data.
3. **Low front LiDAR mounting.** Better distance coverage to track walls may increase floor reflections or miss signs taller/shorter than scan height; this must be tested.
4. **Higher-torque / controlled-speed transmission.** Target balance between 1300–1360 motor RPM, possible gearing to ~800 wheel RPM, and acceleration capacity.
5. **More deliberate mass placement.** Battery and motor positioning should minimize pitch, roll and steering oscillation.

These statements record *what the team discussed*, not assertions that each change was manufactured or performed better.

## Dimensional data to photograph/measure

| Parameter | Value | Method |
|---|---|---|
| Overall length / width / height | TO MEASURE | caliper + annotated front/side/top photo |
| Vehicle mass | TO MEASURE | digital balance with battery installed |
| Wheelbase | TO MEASURE | front axle center to rear axle center |
| Front / rear track widths | TO MEASURE | wheel-center distances |
| Actual rolling wheel diameter | 54 mm discussed; TO MEASURE | 5-revolution floor roll / caliper |
| Min left/right turn radius | TO MEASURE | floor marker test |
| Max left/right steering angle | TO MEASURE | angle gauge and steering linkage |
| Motor torque and reduction | TO VERIFY | motor marking + gearbox specification |
| Tire material and tread | TO VERIFY | photos + supplier link |

## Speed and gearing — analytical estimates
For a wheel of diameter `D` meters and shaft rotation `n` RPM, wheel-surface velocity is `v = π D n / 60`. At 54 mm and 800 RPM, `v_ideal ≈ 2.262 m/s`. A discussed 1360-to-800 RPM reduction is `i = 1360/800 ≈ 1.70:1`. If 1300 RPM is the correct motor speed, ratio becomes `1.625:1`. These are *unloaded kinematic calculations*. Note that the motor's published RPM may already be the gearbox output speed: adding another reduction is only valid if the stages are correctly identified.

A rough 18 m full-course estimate yields `18/20 = 0.90 m/s` and `18/18 = 1.00 m/s` average speed requirements for 20 s and 18 s respectively. This is a user-discussed approximation, **not a fixed WRO course measurement**. Estimate turn losses and braking rather than claiming a 2.26 m/s race speed.

## Steering reasoning
A kinematic bicycle model gives approximate turn radius `R = L/tan(δ)` with wheelbase `L` and effective steering angle `δ`. This is a simplified model: actual front linkage geometry, tire slip and fast motion can change it. Enter a measured wheelbase and steering angle, compute expected R, then compare with a circle test. Never invent a dimensioned Ackermann drawing. Add the actual link lengths and servo geometry once measured.

## Tests that would support a high evaluation score
- Track speed versus drive PWM and battery voltage; measure loaded wheel speed, not just theoretical no-load speed.
- Repeated left/right minimum-radius tests at low, medium and high speed.
- Straight tracking drift over a known baseline; lateral deviation should be measured.
- Acceleration and emergency braking distance from at least three initial speeds.
- Vibration / wheel-slip evaluation on real WRO mat material.
- Component strain check (servo current, axle load, motor temperature and cable retention).

## Decision tradeoffs to record
Speed versus stopping precision; low mass versus stiffness; narrow tire drag versus grip; tighter steering versus traction and servo load; gearing reduction versus free speed; low sensor center of gravity versus the ability to see all required obstacles. Record the alternatives, measurements and final choice in [decision log](05_systems_decisions_and_risks.md).

**Required final artifacts:** STL/STEP if applicable, dimensions and mounting drawing, photos of mechanical linkages, real BOM, gear calculation and actual test data. None of these are provided as original evidence in this draft.
