import os
import bisect


def generate_candidates(max_digits=10):
    result = set()
    for k in range(1, max_digits + 1):
        for r in range(2, max_digits // k + 1):
            if k * r > max_digits:
                break
            for x in range(10 ** (k - 1), 10**k):
                result.add(int(str(x) * r))
    return sorted(result)


def sum_in_range(candidates, lo, hi):
    l = bisect.bisect_left(candidates, lo)
    r = bisect.bisect_right(candidates, hi)
    return sum(candidates[l:r])


candidates = generate_candidates()

with open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt") as f:
    line = f.read().strip()

pairs = [r.split("-") for r in line.split(",")]
print(sum(sum_in_range(candidates, int(a), int(b)) for a, b in pairs))
