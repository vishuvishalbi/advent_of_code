# Advent of Code 2025

Practicing Advent of Code 2025 solutions.

## Day 1: Secret Entrance

**Problem:** The North Pole base's password is locked in a safe with a circular dial (0-99). Given a sequence of rotations (left/right with distance), determine how many times the dial lands on 0 during the process.

**Solution:** Track the dial position as it rotates, counting each time it points to 0. The dial wraps around using modulo arithmetic (0-99 is circular).

**Implementation:** [day_1/main.py](day_1/main.py) - reads rotation instructions from input.txt and calculates the password.
