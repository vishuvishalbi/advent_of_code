"""
--- Day 3: Lobby ---
--- Part Two ---
The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

Consider again the example from before:

987654321111111
811111111111119
234234234234278
818181911112111
Now, the joltages are much larger:

In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.
"""


from operator import index
import os
import timeit

def createBigNumberMap(num):
    numMap = {}
    for i in range(1,10):
        numMap[i] = []
    for k,v in enumerate(num):
        numMap[int(v)].append(k)
    
    return numMap

def createBigNumber(numbers, initialCount):
    start = -1
    count = initialCount
    incrementCount = initialCount - 1
    numMap = createBigNumberMap(numbers)
    finalNumber = 0
    while count > 0:
        end = len(numbers) - count
        num = 9
        while num > 0:
            arr = numMap[num]
            for a in arr:
                if start < a <= end:
                    finalNumber +=  (10 ** incrementCount) * int(numbers[a])
                    incrementCount -= 1
                    count -= 1
                    start = a
                    end += 1
                    num = 10 

                    if incrementCount <0:
                        return finalNumber
                    break

            num -= 1

    return finalNumber



def main():
    total = 0
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/input1.txt") as f:
        for r in f.read().splitlines():
            total += createBigNumber(r, 12)
    # print(total)

t = timeit.timeit(lambda: main(), number=1)
print(f"{t/1 * 1e6:.2f}µs per call")
# print(createBigNumber('987654321111111', 12) == 987654321111, createBigNumber('987654321111111', 12))
# print(createBigNumber('811111111111119', 12) == 811111111119, createBigNumber('811111111111119', 12))
# print(createBigNumber('234234234234278', 12) == 434234234278, createBigNumber('234234234234278', 12))
# print(createBigNumber('818181911112111', 12) == 888911112111, createBigNumber('818181911112111', 12))