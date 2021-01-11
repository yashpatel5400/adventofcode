import copy

with open("input_14.txt", "r") as f:
    lines = f.readlines()

max_pos = -1
for line in lines:
    # mem[35042] = 207010
    if line.startswith("mem["):
        pos = int(line.split("mem[")[1].split("]")[0])
        if pos > max_pos:
            max_pos = pos

arr = {}

cur_mask = None
for line in lines:
    if line.startswith("mask = "):
        cur_mask = line.strip().split("mask = ")[1]
    else:
        pos = int(line.split("mem[")[1].split("]")[0])
        value = int(line.split(" = ")[1].strip())
        binary_value = bin(pos)[2:].zfill(len(cur_mask))
        
        new_binary = []
        x_poses = []

        for i, c in enumerate(binary_value):
            if cur_mask[i] == '0':
                new_binary.append(c)
            elif cur_mask[i] == '1':
                new_binary.append('1')
            else:
                new_binary.append('X')
                x_poses.append(i)


        possible_binaries = [new_binary]
        for x_pos in x_poses:
            dups = copy.deepcopy(possible_binaries)
            for i in range(len(possible_binaries)):
                possible_binaries[i][x_pos] = '0'
            for i in range(len(dups)):
                dups[i][x_pos] = '1'

            possible_binaries += dups

        for binary in possible_binaries:
            arr[int("".join(binary), 2)] = value
print(sum(arr.values()))