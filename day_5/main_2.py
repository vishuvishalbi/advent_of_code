"""
--- Part Two ---
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?


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
    

def mergeInRange():
    loop = len(linear_arr) -1
    i = 0
    while i < loop:
        if isNumberIntersect(linear_arr[i], linear_arr[i + 1]):
           linear_arr[i] =  getNewRangeNum(linear_arr[i], linear_arr[i + 1])
           linear_arr.pop(i+1)
           loop = len(linear_arr) -1
        else:
            i += 1


def countTotal():
    total = 0 
    for x in linear_arr:
        nums = x.split(".")
        total += int(nums[1]) - int(nums[0]) + 1
    
    print(total)

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
            mergeInRange()
            countTotal()
            exit(0)


# text ="""3-5
# 10-14
# 16-20
# 12-18

# """

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
#         mergeInRange()
#         countTotal()
#         exit(0)

# print("Total ", total)

