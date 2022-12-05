import re

# Part one
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

crates_state = {}
raw_crates = []
for input_row in input_array:
    if input_row.strip().startswith("["):
        raw_crates.append(input_row)
    elif input_row == "\n":
        for row in raw_crates:
            step_a = re.sub(r" {3,4}", "[*]", row).replace("][", "] [")
            step_b = step_a.split(" ")
            for idx, crate in enumerate(step_b):
                if f"stack_{idx + 1}" not in crates_state:
                    crates_state[f"stack_{idx + 1}"] = []
                if crate.strip()[1:2] != "*":
                        crates_state[f"stack_{idx + 1}"].insert(0, crate.strip()[1:2])
    elif input_row.startswith("move"):
        instruction = input_row.replace("move ", "").strip()
        amount_of_crates = int(instruction.split(" ")[0])
        crates_from = instruction.split(" ")[2]
        crates_to = instruction.split(" ")[4]
        for i in range(amount_of_crates):
            a = crates_state[f"stack_{crates_from}"][-1]
            crates_state[f"stack_{crates_from}"].pop()
            crates_state[f"stack_{crates_to}"].append(a)
print("".join([val[-1] for val in crates_state.values()]))

# Part two
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

crates_state = {}
raw_crates = []
for input_row in input_array:
    if input_row.strip().startswith("["):
        raw_crates.append(input_row)
    elif input_row == "\n":
        for row in raw_crates:
            step_a = re.sub(r" {3,4}", "[*]", row).replace("][", "] [")
            step_b = step_a.split(" ")
            for idx, crate in enumerate(step_b):
                if f"stack_{idx + 1}" not in crates_state:
                    crates_state[f"stack_{idx + 1}"] = []
                if crate.strip()[1:2] != "*":
                        crates_state[f"stack_{idx + 1}"].insert(0, crate.strip()[1:2])
    elif input_row.startswith("move"):
        instruction = input_row.replace("move ", "").strip()
        amount_of_crates = int(instruction.split(" ")[0])
        crates_from = instruction.split(" ")[2]
        crates_to = instruction.split(" ")[4]
        a = []
        for i in range(0, amount_of_crates):
            a.insert(0, crates_state[f"stack_{crates_from}"][-1])
            crates_state[f"stack_{crates_from}"].pop()
        crates_state[f"stack_{crates_to}"] += a
print("".join([val[-1] for val in crates_state.values()]))