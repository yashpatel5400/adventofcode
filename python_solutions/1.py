# part 1

with open("input_1.txt", "r") as f:
    lines = f.readlines()
num_lines = [int(line) for line in lines]

target = 2020
for i, num1 in enumerate(num_lines):
    for j, num2 in enumerate(num_lines[i+1:]):
        if num1 + num2 == target:
            print("{} x {} = {}".format(num1, num2, num1 * num2))

# part 2

with open("input_1.txt", "r") as f:
    lines = f.readlines()
num_lines = [int(line) for line in lines]

target = 2020
for i, num1 in enumerate(num_lines):
    for j, num2 in enumerate(num_lines):
        for k, num3 in enumerate(num_lines):
            if i >= j or j >= k:
                continue

            if num1 + num2 + num3 == target:
                print("{} x {} x {} = {}".format(num1, num2, num3, num1 * num2 * num3))