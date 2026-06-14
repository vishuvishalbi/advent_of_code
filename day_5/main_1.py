"""
--- Day 5: Cafeteria ---
As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
"""

from decimal import Decimal
import os


linear_arr = []


def binary_search(sorted_list: list, target: int) -> bool:
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        # Calculate the midpoint using the formula
        mid = low + (high - low) // 2
        
        if isNumberInRange(target, sorted_list[mid]):
            return True   # Target found
        elif int(float(sorted_list[mid])) < int(target):
            low = mid + 1  # Search right half
        else:
            high = mid - 1 # Search left half

    return False  # Target not found

def isNumberInRange(num,rangenum):
    
    start, end = rangenum.split(".")
    
    return int(num) >= int(start) and int(num) <= int(end)

def isNumberIntersect(num, rangenum) -> bool:
    nums = num.split(".")
    ranges = rangenum.split(".")
    startNum = False
    if isNumberInRange(nums[0], rangenum):
        startNum = True
    elif isNumberInRange(nums[1], rangenum):
        startNum = True
    elif isNumberInRange(ranges[0], num):
        startNum = True
    elif isNumberInRange(ranges[1], num):
        startNum = True
    
    if startNum:
        return True
    return False


def getNewRangeNum(num: str, rangenum: str) -> str:
    nums = num.split(".")
    ranges = rangenum.split(".")
    
    # min() picks the lower starting number, max() picks the higher ending number
    startNum = min(nums[0], ranges[0], key=int)
    endNum = max(nums[1], ranges[1], key=int)
    
    return f"{startNum}.{endNum}"

def shouldGoRight(num, rangenum):
    return int(Decimal(num)) > int(Decimal(rangenum))
    



def createLinearArr(rnum:str):
    num = rnum.replace("-" , ".")

    if len(linear_arr)  == 0:
        linear_arr.append(num)
        return
    l = 0;
    r = len(linear_arr) -1
    mid = -1 
    isInserted = False

    while l <= r:
        mid =  l + (r-l)//2

        if isNumberIntersect(num, linear_arr[mid]):
            linear_arr[mid] = getNewRangeNum(num, linear_arr[mid])
            isInserted = True
            break;
        elif int(float(linear_arr[mid])) < int(float(num)):
            l = mid+1 #search right
        else:
            r = mid - 1 #serarch left

    if not isInserted:
        if shouldGoRight(num, linear_arr[mid]):
            linear_arr.insert(mid+1, num)
        else:
            linear_arr.insert(mid, num)
        

def isFresh(num) -> bool:
    return binary_search(linear_arr, num)


isRange = True
total = 0
with open(f"{os.path.dirname(os.path.abspath(__file__))}/input.txt") as f:
    for r in f.read().splitlines():
        if isRange and "-" in r:
            createLinearArr(r)
        elif r.isnumeric():
            if isFresh(r):
                total += 1
        else:
            isRange = False
            linear_arr.sort(key=lambda x: int(float(x)))


# text ="""3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""

# for r in text.splitlines():
#     if isRange and "-" in r:
#         createLinearArr(r)
#     elif r.isnumeric():
#         print(linear_arr)
#         if isFresh(r):
#             total += 1
#     else:
#         isRange = False
#         linear_arr.sort(key=lambda x: int(float(x)))

print("Total ", total)

