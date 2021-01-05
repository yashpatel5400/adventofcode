import copy

def does_infinite_loop(lines):
    accum = 0
    line_idx = 0
    history = set()

    while True:
        if line_idx in history:
            return accum, True
        if line_idx == len(lines):
            return accum, False

        history.add(line_idx)

        line = lines[line_idx]
        op, val = line.split(" ")
        val = int(val)
        if op == "nop":
            line_idx += 1
        elif op == "acc":
            accum += val
            line_idx += 1
        elif op == "jmp":
            line_idx += val

with open("input_8.txt", "r") as f:
    lines = f.readlines()

lines_with_jmp = [i for i, line in enumerate(lines) if "jmp" in line]

for line_with_jmp in lines_with_jmp:
    new_lines = copy.deepcopy(lines)
    new_lines[line_with_jmp] = new_lines[line_with_jmp].replace("jmp", "nop")
    acc, did_infloop = does_infinite_loop(new_lines)
    if not did_infloop:
        print(acc)