# Criterion 5 — Reproducing Team Ionizers' competition robot

**Current state: blocked by missing original source and actual build files.** This checklist identifies exactly what needs to be included for a judge or another student team to rebuild the car.

## Bill of materials
Complete `schemes/BOM.csv`: item, actual purchased part no., quantity, installed revision, supplier, units, cost, function, evidence, replacement alternatives. Do not assume a candidate part is final. Include any 3D-printed material/filament specification, batteries, servo horns, bearings, fasteners, motor couplers and connectors.

## Mechanical reproduction
- Actual CAD/STEP/STL, with orientation, print tolerances, material and infill where applicable.
- Chassis plan showing axle separation, track widths and ground clearance; body dimensions with battery attached.
- Motor gearbox shaft/axle mounting description, wheel attachment and steering linkage geometry.
- Actual tuning measurements (wheel diameter, servo center, left and right stops).

## Wiring reproduction
- Real netlist: exact device model, label, pin name, destination pin, wire gauge, signal voltage, measured rail and connector.
- Actual protection parts (fuse and switch), buck supply types and current ratings.
- Motor current path, encoder input conditioning, servo supply and SBC-to-MCU wired protocol.
- An electrical schematic beyond the general conceptual blocks in `schemes/system_architecture.svg`.

## Firmware and software
- `src/esp32/`: all sketches/framework projects, PlatformIO/Arduino/ESP-IDF version info and library locking.
- `src/raspberry_pi/`: actual Python source, requirements with exact tested versions, configuration, calibration data, services/start scripts and camera/LiDAR drivers.
- Document flash commands, physical serial connection and permissions, startup commands, shutdown behavior, update instructions and safe reset procedure.
- Source MUST be the actual work used on the competition robot; do not replace it with conceptual snippets.

## Validation for a fresh build
1. Verify power rails unloaded and loaded without connecting sensitive logic first.
2. Verify servo control and motor polarity with wheels lifted off the ground.
3. Verify encoder speed if installed and sensor frame/scan geometry.
4. Verify firmware/libraries and communication packet timeout.
5. Calibrate center steering and color/range on known targets.
6. Complete Open/Obstacle rounds from varying starts, then parking.
7. Record the actual build commit and link videos to match it.

## Reproducibility evidence
Include a software versioning policy, official public repo URL, at least three **authentic** development commits per WRO timeline, full photo coverage and real YouTube demonstrations. The project must stay public for 12 months after the international event. Bring a hard copy of the Engineering Journal to the International Final.
