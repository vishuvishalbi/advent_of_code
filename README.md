# Advent of Code 2025

Practicing Advent of Code 2025 solutions.

## Day 1: Secret Entrance

### Part 1

**Problem:** The North Pole base's password is locked in a safe with a circular dial (0-99). Given a sequence of rotations (left/right with distance), determine how many times the dial lands on 0 at the end of a rotation.

**Solution:** Track the dial position, counting each time it lands on 0 after a rotation. Answer: **1089**

**Implementation:** [day_1/main_1.py](day_1/main_1.py)

### Part 2

**Problem:** Same dial, but now count every single click that causes the dial to point at 0 — both during a rotation and at the end.

**Solution:** For each rotation, compute how many times 0 is crossed using integer division. Key edge case: rotating left from position 0 uses `distance // 100` (not the standard formula) to avoid counting the starting position as a click. Answer: **6530**

**Implementation:** [day_1/main_2.py](day_1/main_2.py)
