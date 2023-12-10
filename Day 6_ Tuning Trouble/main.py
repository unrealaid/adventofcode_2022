# Imports
from typing import List
# -------

# Common functions
# ----------------

# Part one
def part_one(input_array: List[str]) -> None:
    result = 0

    for input_row in input_array:
        char_idx = 0
        result = 0
        while result == 0:
            sub_row = input_row[char_idx:char_idx + 4]
            if len(sub_row) == len(set(sub_row)):
                result = char_idx + 4
                break
            char_idx += 1
        print(result)
# --------

# Part two
def part_two(input_array: List[str]) -> None:
    result = 0

    for input_row in input_array:
        char_idx = 0
        result = 0
        while result == 0:
            som_packet = input_row[char_idx:char_idx + 4]
            if len(som_packet) == len(set(som_packet)):
                som_full = input_row[char_idx:char_idx + 14]
                if len(som_full) == len(set(som_full)):
                    result = char_idx + 14
                    break
            char_idx += 1
        print(result)
# --------

# Main wrapper
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

part_one(input_array)
print("------------")
part_two(input_array)
# ------------