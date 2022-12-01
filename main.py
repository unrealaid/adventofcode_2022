# Part one
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

max_calories = 0
curr_calories = 0
for item in input_array:
    if item.strip() == "":
        if curr_calories > max_calories:
            max_calories = curr_calories
        curr_calories = 0
    else:
        curr_calories += int(item.strip())

print(max_calories)

# Part two
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

top1_calories = 0
top2_calories = 0
top3_calories = 0
curr_calories = 0
for item in input_array:
    if item.strip() == "":
        if curr_calories > top3_calories:
            top3_calories = curr_calories
        if top3_calories > top2_calories:
            top2_calories, top3_calories = top3_calories, top2_calories
        if top2_calories > top1_calories:
            top2_calories, top1_calories = top1_calories, top2_calories
        curr_calories = 0
    else:
        curr_calories += int(item.strip())

print(top1_calories)
print(top2_calories)
print(top3_calories)
print(top1_calories+top2_calories+top3_calories)