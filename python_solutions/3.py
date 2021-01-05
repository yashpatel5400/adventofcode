with open("input_3.txt", "r") as f:
    lines = f.readlines()

slopes = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1),
]

num_trees_per_slope = []
for slope in slopes:
    num_trees = 0
    i = 0
    j = 0

    while i < len(lines) - slope[0]:
        i += slope[0]
        j = (j + slope[1]) % len(lines[0].strip())
        c = lines[i][j]
        if c == "#":
            num_trees += 1
    num_trees_per_slope.append(num_trees)

ans = 1
for num_trees in num_trees_per_slope:
    ans *= num_trees
print(ans)