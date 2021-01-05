with open("input_1.txt", "r") as f:
    lines = f.readlines()
num_lines = [int(line) for line in lines]

target = 2020
for i, num1 in enumerate(num_lines):
    for j, num2 in enumerate(num_lines[i+1:]):
        if num1 + num2 == target:
            print("{} x {} = {}".format(num1, num2, num1 * num2))