# Imports
from typing import List
# -------

# Common functions
def check_visible(x, y, size, input_matrix) -> bool:
    row: list = list(input_matrix[x].strip())
    col: list = [row[y] for row in input_matrix]
    from_left = False
    from_right = False
    from_top = False
    from_bot = False
    from_left = (True if all(row[i] < size for i in range(y)) else False)
    from_right = (True if all(row[i] < size for i in range(y + 1, len(row))) else False)
    from_top = (True if all(col[i] < size for i in range(x)) else False)
    from_bot = (True if all(col[i] < size for i in range(x + 1, len(col))) else False)
    # print(f"[{x}][{y}] visible - left: {from_left}, right: {from_right}, top: {from_top}, bot: {from_bot}")
    return any([from_left, from_right, from_top, from_bot])

def check_dist(x, y, size, input_matrix) -> int:
    def count(array) -> int:
        res = 0
        for i in array:
            res += 1
            if not i:
                break
        return res
    
    row: list = list(input_matrix[x].strip())
    col: list = [row[y] for row in input_matrix]
    from_left = count([row[i] < size for i in range(y)][::-1])
    from_right = count([row[i] < size for i in range(y + 1, len(row))])
    from_top = count([col[i] < size for i in range(x)][::-1])
    from_bot = count([col[i] < size for i in range(x + 1, len(col))])
    # print(f"[{x}][{y}] visible - left: {from_left}, right: {from_right}, top: {from_top}, bot: {from_bot}")
    return from_left * from_right * from_top * from_bot
# ----------------

# Part one
def part_one(input_array: List[str]) -> None:
    result = 0

    # initial amount of trees visible from outside
    result += (len(input_array[0].strip()) * 2) + ((len(input_array) - 2) * 2)
    inner_visible_trees = 0
    for x in range(1, len(input_array) - 1):
        for y in range(1, len(input_array[0].strip()) - 1):
            result += check_visible(x, y, input_array[x][y], input_array)
    result += inner_visible_trees
    print(result)
# --------

# Part two
def part_two(input_array: List[str]) -> None:
    result = 0

    for x in range(1, len(input_array) - 1):
        for y in range(1, len(input_array[0].strip()) - 1):
            tmp = check_dist(x, y, input_array[x][y], input_array)
            if tmp > result:
                result = tmp
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