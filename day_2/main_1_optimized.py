"""
Day 2 - Optimized Solution

Instead of iterating every number in each range, we pre-generate all
"repeated" numbers (e.g. 1010, 9999, 123123) up front, then use binary
search to sum those that fall within each range.

Time: O(C log C + R log C)  where C = ~45k candidates, R = number of ranges
vs brute force: O(R * range_width)
"""
import os
import bisect


def generate_candidates(max_half_digits=5):
    result = []
    for k in range(1, max_half_digits + 1):
        for x in range(10 ** (k - 1), 10**k):
            s = str(x)
            result.append(int(s + s))
    result.sort()
    return result


def sum_in_range(candidates, lo, hi):
    l = bisect.bisect_left(candidates, lo)
    r = bisect.bisect_right(candidates, hi)
    return sum(candidates[l:r])


candidates = generate_candidates()
with open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt") as f:
    line = f.read().strip()

pairs = [r.split("-") for r in line.split(",")]
print(sum(sum_in_range(candidates, int(a), int(b)) for a, b in pairs))
