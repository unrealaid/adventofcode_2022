def make_range(input: str):
    start = int(input.split("-")[0].strip())
    end = int(input.split("-")[1].strip()) + 1
    return set(range(start, end, 1))


# Part one
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

count = 0
for assignments in input_array:
    a = assignments.split(",")[0]
    b = assignments.split(",")[1]
    range_a = make_range(a)
    range_b = make_range(b)
    if range_a.issubset(range_b) or range_b.issubset(range_a):
        count += 1
print(count)

# Part two
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

count = 0
for assignments in input_array:
    a = assignments.split(",")[0]
    b = assignments.split(",")[1]
    range_a = make_range(a)
    range_b = make_range(b)
    if not range_a.isdisjoint(range_b):
        count += 1
print(count)