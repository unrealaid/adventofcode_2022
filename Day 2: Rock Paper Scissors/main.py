# A for Rock        - 1 point
# B for Paper       - 2 points
# C for Scissors    - 3 points

# X for Rock        - 1 point
# Y for Paper       - 2 points
# Z for Scissors    - 3 points

# 0 if you lost
# 3 if the round was a draw
# and 6 if you won

# Part one
res_map = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3
    },
}
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

my_score = 0
for round in input_array:
    opponent_move = round.split(' ')[0].strip()
    my_move = round.split(' ')[1].strip()
    my_score += res_map[opponent_move][my_move]

print(my_score)

# Part two
res_map_g2 = {
    "A": {
        "X": 3 + 0,
        "Y": 1 + 3,
        "Z": 2 + 6
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6
    },
    "C": {
        "X": 2 + 0,
        "Y": 3 + 3,
        "Z": 1 + 6
    },
}
input_array = []
with open("input.txt", "r") as f:
    input_array = f.readlines()

my_score = 0
for round in input_array:
    opponent_move = round.split(' ')[0].strip()
    my_move = round.split(' ')[1].strip()
    my_score += res_map_g2[opponent_move][my_move]

print(my_score)