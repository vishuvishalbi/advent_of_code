"""
--- Day 5: Cafeteria (Part 2) --- Optimized Solution

APPROACH: Interval Merging → Sum of lengths
============================================

Part 2 doesn't need to query individual IDs. It asks:
  "How many integers are covered by ANY range in total?"

Step 1 — Parse all ranges as (start, end) integer tuples.
Step 2 — Sort by start.                           O(n log n)
Step 3 — Merge overlapping/adjacent ranges.       O(n)
Step 4 — Sum (end - start + 1) for each merged range. O(n)

WHY THIS WORKS:
  After merging, every merged range is non-overlapping. Summing their lengths
  gives the exact count of unique integers covered, with no double-counting.

TIME COMPLEXITY:
  - O(n log n) — sort dominates
  - O(n)       — single merge pass
  - O(n)       — single sum pass
  → Total: O(n log n)

SPACE COMPLEXITY: O(n) for merged ranges

EXAMPLE:
  Input:  3-5, 10-14, 16-20, 12-18
  Sorted: (3,5), (10,14), (12,18), (16,20)
  Merged: (3,5), (10,20)
  Count:  (5-3+1) + (20-10+1) = 3 + 11 = 14  ✓
"""

import os


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Sort and merge all overlapping or adjacent ranges into a minimal list."""
    ranges.sort()
    merged = [ranges[0]]
    for s, e in ranges[1:]:
        if s <= merged[-1][1]:          # overlaps or is adjacent
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return merged


ranges: list[tuple[int, int]] = []

with open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt") as f:
    for line in f.read().splitlines():
        if "-" in line:
            a, b = line.split("-")
            ranges.append((int(a), int(b)))

merged = merge_ranges(ranges)
total = sum(e - s + 1 for s, e in merged)
print("Total fresh IDs:", total)
