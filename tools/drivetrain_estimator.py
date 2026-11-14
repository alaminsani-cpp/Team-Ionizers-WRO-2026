#!/usr/bin/env python3
"""Documentation-only no-load speed calculator for discussed Team Ionizers dimensions.

NOT actual robot control software; do not describe it as competition firmware.
"""
import argparse
import math

def linear_speed_mps(wheel_diameter_mm: float, wheel_rpm: float) -> float:
    if wheel_diameter_mm <= 0 or wheel_rpm < 0:
        raise ValueError("Wheel diameter must be positive and RPM nonnegative")
    return math.pi * (wheel_diameter_mm / 1000.0) * wheel_rpm / 60.0

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diameter-mm', type=float, default=54.0)
    parser.add_argument('--wheel-rpm', type=float, default=800.0)
    parser.add_argument('--motor-rpm', type=float, default=1360.0)
    parser.add_argument('--course-m', type=float, default=18.0)
    args = parser.parse_args()
    speed = linear_speed_mps(args.diameter_mm, args.wheel_rpm)
    print(f'Ideal no-load wheel peripheral speed: {speed:.3f} m/s')
    print(f'Illustrative motor-to-wheel reduction: {args.motor_rpm / args.wheel_rpm:.3f}:1')
    print(f'Ideal straight-line course time (no turns/acceleration): {args.course_m / speed:.2f} s')
    print('WARNING: motor loaded RPM, actual wheel rolling circumference, grip, turns,')
    print('battery sag and WRO course variation make measured results different.')

if __name__ == '__main__':
    main()
