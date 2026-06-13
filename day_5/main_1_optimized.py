"""
--- Day 5: Cafeteria (Part 1) --- Optimized Solution

APPROACH: Interval Merging + Binary Search
===========================================

Step 1 — Parse all ranges as (start, end) integer tuples.
Step 2 — Sort ranges by start value.          O(n log n)
Step 3 — Merge overlapping/adjacent ranges.   O(n)
Step 4 — For each query ID, binary search the merged ranges. O(log n) per query

WHY MERGE FIRST?
  Instead of checking every range for every query (O(R*Q)), merging collapses
  all overlapping ranges into a minimal set. Binary search then locates the
  right merged range in O(log R) instead of scanning all R ranges.

TIME COMPLEXITY:
  - Building merged ranges: O(n log n)  — dominated by sort
  - Each query:             O(log n)    — binary search over merged ranges
  - Total:                  O(n log n + Q log n)

SPACE COMPLEXITY: O(n) for merged ranges list

vs. Original approach:
  - list.insert() inside binary search = O(n) per range insertion
  - Incomplete merge (only handles one overlap per insertion)
  - String-based "10.14" range format = repeated parse overhead
"""

import os
import bisect


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


def is_fresh(merged: list[tuple[int, int]], val: int) -> bool:
    """
    Binary search: find the rightmost range whose start <= val,
    then check if val also falls within its end.
    bisect_right gives insertion point for val among starts;
    we check the range just to the left.
    """
    starts = [s for s, _ in merged]
    idx = bisect.bisect_right(starts, val) - 1
    if idx < 0:
        return False
    return merged[idx][0] <= val <= merged[idx][1]


ranges: list[tuple[int, int]] = []
ids: list[int] = []
is_range_section = True

with open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt") as f:
    for line in f.read().splitlines():
        if is_range_section and "-" in line:
            a, b = line.split("-")
            ranges.append((int(a), int(b)))
        elif line.strip() == "":
            is_range_section = False
        elif line.strip().lstrip("-").isnumeric():
            ids.append(int(line))

merged = merge_ranges(ranges)
total = sum(1 for x in ids if is_fresh(merged, x))
print("Total fresh:", total)
