import string


def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1


# Part one
gen = infinite_sequence()
priorities_map = dict.fromkeys(string.ascii_lowercase + string.ascii_uppercase)
for key in priorities_map.keys():
    priorities_map[key] = next(gen)

input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

priorities_sum = 0
for rucksack in input_array:
    a = list(rucksack.strip())[:int(len(rucksack.strip()) / 2)]
    b = list(rucksack.strip())[int(len(rucksack.strip()) / 2):]
    for item_a in a:
        if item_a in b:
            priorities_sum += int(priorities_map[item_a])  # type: ignore
            break
print(priorities_sum)

# Part two
gen = infinite_sequence()
priorities_map = dict.fromkeys(string.ascii_lowercase + string.ascii_uppercase)
for key in priorities_map.keys():
    priorities_map[key] = next(gen)

input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

priorities_sum = 0
limiter = 3
group_rucksacks = []
for rucksack in input_array:
    if limiter > 0:
        group_rucksacks.append(rucksack.strip())
        limiter -= 1
    if limiter == 0:
        limiter = 3
        for item_a in group_rucksacks[0]:
            if item_a in group_rucksacks[1] and item_a in group_rucksacks[2]:
                priorities_sum += int(priorities_map[item_a])  # type: ignore
                group_rucksacks = []
                break
print(priorities_sum)