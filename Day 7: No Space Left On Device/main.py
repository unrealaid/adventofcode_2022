# Imports
from typing import List
# -------

# Common functions
# ----------------

# Part one
def part_one(input_array: List[str]) -> None:
    result = 0

    directories = {}
    current_path = []
    for input_row in input_array:
        if input_row.startswith("$"):
            commands = input_row.replace("$ ", "").split(" ")
            if commands[0].strip() == "cd":
                path_requested = commands[1].strip()
                if path_requested == ".." and len(current_path) > 0:
                    current_path.pop()
                elif path_requested == "/":
                    current_path.append("")
                else:
                    current_path.append(path_requested)
            elif commands[0].strip() == "ls":
                directories["/".join(current_path)] = 0
            else:
                print("Unknown command")
        else:
            output = input_row.split(" ")
            if output[0] != "dir":
                directories["/".join(current_path)] += int(output[0])
    for dir in directories.keys():
        paths = dir.split("/")
        paths.pop()
        while len(paths) > 0:
            directories["/".join(paths)] += directories[dir]
            paths.pop()
    for dir_size in directories.values():
        if dir_size < 100000:
            result += dir_size
    print(result)
# --------

# Part two
def part_two(input_array: List[str]) -> None:
    result = 0

    directories = {}
    current_path = []
    for input_row in input_array:
        if input_row.startswith("$"):
            commands = input_row.replace("$ ", "").split(" ")
            if commands[0].strip() == "cd":
                path_requested = commands[1].strip()
                if path_requested == ".." and len(current_path) > 0:
                    current_path.pop()
                elif path_requested == "/":
                    current_path.append("")
                else:
                    current_path.append(path_requested)
            elif commands[0].strip() == "ls":
                directories["/".join(current_path)] = 0
            else:
                print("Unknown command")
        else:
            output = input_row.split(" ")
            if output[0] != "dir":
                directories["/".join(current_path)] += int(output[0])
    for dir in directories.keys():
        paths = dir.split("/")
        paths.pop()
        while len(paths) > 0:
            directories["/".join(paths)] += directories[dir]
            paths.pop()
    total_mem = 70000000
    update_mem_req = 30000000
    space_available = total_mem - directories[""]
    max_del_size = update_mem_req - space_available
    result = directories[""]
    for dir_size in directories.values():
        if dir_size < result and dir_size > max_del_size:
            result = dir_size
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