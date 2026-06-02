"""
--- Day 2: Gift Shop ---
You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.
Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs?

Solution: Few things I have noticed that duplication can only come if the length of the number is even. Else for odd there is no repetition.So, we need to check both the numbers in the range if they are even.
Also if the range has some repetition. I mean if range has some number more than once. for example 38593856 here 3,8,5 is repetitive in same sequence.
So, the possiblity of getting same repetition is high because we only need to match one number. Also if the difference between the range also needs to be checked.


"""
import os


def can_have_invalid_id(start: str, end: str) -> bool:
    if len(start) % 2 != 0 and len(end) % 2 != 0:
        return False
    return True


def can_have_palindrome(start: str, end: str) -> int:
    s = int(start)
    e = int(end)
    r = e - s  # Unused variable matching your original Go code

    if len(start) % 2 == 0:
        mid = len(start) // 2  # // performs integer division (automatically floors)

        # Recreating your precise index building logic:
        # Initializing a list of the same length to modify by index
        n_list = [""] * len(start)
        for i in range(mid):
            n_list[i] = start[i]
            n_list[mid + i] = start[i]

        n_str = "".join(n_list)

        # Comparing string values matching your original logic
        if start <= n_str <= end:
            return int(n_str)

    if len(end) % 2 == 0:
        mid = len(end) // 2

        n_list = [""] * len(end)
        for i in range(mid):
            n_list[i] = end[i]
            n_list[mid + i] = end[i]

        n_str = "".join(n_list)

        if start <= n_str <= end:
            return int(n_str)

    return 0


def main():
    # Gets the absolute path of this current Python script file
    exe_path = os.path.abspath(__file__)
    exe_dir = os.path.dirname(exe_path)

    # Safely creates the path to input.txt in the same directory
    file_path = os.path.join(exe_dir, "input.txt")
    print("File path :", file_path)

    try:
        with open(file_path, "r") as file:
            data = file.read()
    except FileNotFoundError as err:
        raise err

    # Split the text by comma
    formatted_data = data.split(",")
    print(data)
    total = 0
    # Loop with index and value
    for i, val in enumerate(formatted_data):
        # Skip empty items if they occur at the end of a file line
        val = val.strip()
        if not val:
            continue

        # print(f"Index : {i}, Value: {val}")

        # Split the current value by dash (e.g., "10-20")
        arr = val.split("-")
        start = arr[0]
        end = arr[1]

        if can_have_invalid_id(start, end):
            total += can_have_palindrome(start, end)
            # print(f"Start: {start} Ends: {end}")
        else:
            pass
    print("total : ", total)


def count_invalids_binary(start: str, end: str) -> int:
    s, e = int(start), int(end)
    total = 0
    
    for length in [len(start), len(end)]:
        if length % 2 == 0:
            mid = length // 2
            # Smallest doubled number of this length
            min_half = 10**(mid-1)
            max_half = 10**mid - 1
            
            # Find valid range of first halves
            for half in range(min_half, max_half + 1):
                doubled = int(str(half) + str(half))
                if s <= doubled <= e:
                    total += doubled
    return total

if __name__ == "__main__":
    # main()
    print(count_invalids_binary('2', '39'))
