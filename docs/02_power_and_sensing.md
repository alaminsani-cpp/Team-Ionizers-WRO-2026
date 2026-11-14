# Criterion 2 — Power, electrical architecture and sensor management

## Electrical design status
Raspberry Pi 4/5, ESP32, RPLIDAR C1, camera, encoder, IMU, BTS7960-class motor driver, MG90S steering servo and 4S LiPo were considered during V2 discussions. **Each is pending confirmation from the assembled machine.** The diagrams in `schemes/` express candidate architecture; they do not contain authentic pins or certified voltage values.

## Power domains

- Battery input: 4S LiPo **candidate**. Nominal approximately 14.8 V; fully charged approximately 16.8 V. Do not assume all 12 V motors or nominal 5 V modules can take the full battery voltage.
- Logic rail: battery -> appropriately rated buck regulator -> SBC / ESP32 / LiDAR as required by their exact datasheets. Each rail must be measured *under load*.
- Actuator rail: appropriately rated motor/driver branch and servo regulator / BEC if required. Motors and servos can create transient voltage sag; protect sensitive 5 V rail.
- Grounding and signals: reference logic/control lines correctly, avoid ground loops and high-current return through fragile sensor ground. Check motor EMI and input filtering.
- Protection: suitable fuse near battery, physical main power switch, insulated terminals and strain relief. Observe LiPo storage and charging practices.

**Danger:** The included block diagram is explicitly non-wiring-specific. Do not connect hardware from this diagram alone. Complete `schemes/pinmap.csv` with all measured connections and a true net-level schematic after verifying pin voltage tolerances.

## Preliminary current budget template

| Device | Rail | Idle A | Peak A | Basis |
|---|---|---:|---:|---|
| Pi installed model | TO VERIFY | — | — | official datasheet + bench reading |
| ESP32 installed model | TO VERIFY | — | — | measured |
| RPLIDAR C1 | TO VERIFY | — | — | datasheet and test |
| Camera | TO VERIFY | — | — | datasheet and test |
| Steering servo | TO VERIFY | — | — | measured stall/rapid-turn peak |
| Drive motor through driver | TO VERIFY | — | — | acceleration/stall analysis |
| IMU, encoders, auxiliaries | TO VERIFY | — | — | measured |

Compute worst-case regulator current from sum of simultaneous peaks with a margin. Measure minimum voltage at the Pi during servo transients. Convert battery energy from Wh `= nominal voltage × capacity Ah`; do not infer runtime from capacity without measured current and safe discharge floor.

## Sensor reasoning and calibration plan
**LiDAR:** Verify mounting height and sensor yaw, sweep alignment, min/max usable distance, reflective black wall returns, white border returns and packet-loss behavior. Store at least 30 seconds of raw scans for representative corners. Test LiDAR with different sensor heights if modified signs need to be detected.

**Camera:** Verify exact module and lens, fixed exposure/white balance strategy (if adopted), color calibration under event lighting, field of view and undistortion (if needed). Record annotated red/green test frames and confusion matrix on varied illumination backgrounds.

**IMU (if fitted):** Estimate stationary bias, drift with motor vibration, orientation, rate versus rotation reference, and failure response on missing readings. Do not claim fusion unless actual code demonstrates it.

**Encoder (if fitted):** Determine ticks per effective wheel revolution, direction polarity and loaded wheel speed. Record slipping and odometry drift, especially through turns.

## White border / black corner issue
Earlier discussions described a LiDAR or border/corner perception failure that led to reverse loops. The team reported subsequently resolving it; no commit or log proving the fix is available. This should become a genuine case study: `before` trace; root cause (e.g. specular/no-return behavior *if confirmed*); actual conditional change; test cases; failure frequency before/after. Do not invent a specific filtering technique or a percentage improvement.

## Fail-safe behavior to verify on the actual controller
- If SBC heartbeat disappears: reduce propulsion to zero by the verified driver safe state.
- If camera/LiDAR data are stale: choose bounded safe behavior rather than uncontrolled steering.
- If battery voltage sags: prevent unstable motor commands and controller resets.
- If motor driver is overheated/over-current: stop and record fault after tests.
- If source is rebooted during a round: follow the genuine competition start rules, do not rely on external control.

## 2026 operational requirements
The vehicle must be autonomous. Wired communication between onboard components is permitted, but wireless devices/protocols must be turned off during official rounds. There must be the required separate power/starting controls, and the car must fit within size and mass limits. Check exact regulations and judge Q&A before finalizing wiring.
