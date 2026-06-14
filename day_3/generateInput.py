import random

with open("input1.txt", "w") as f:
    for _ in range(1000):
        row = ''.join(str(random.randint(1, 9)) for _ in range(10_000))
        f.write(row + "\n")