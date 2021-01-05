with open("input_2.txt", "r") as f:
    lines = f.readlines()

num_valid = 0
for line in lines:
    policy = line.split(":")
    password = policy[1]
    vals = policy[0].split(" ")
    ranges = vals[0]
    range_min, range_max = [int(r) for r in ranges.split("-")]
    c = vals[1]

    part_1 = False
    if part_1:
        count = 0
        for wc in password:
            if wc == c:
                count += 1

        if range_min <= count and count <= range_max:
            num_valid += 1
    else:
        if  (password[range_min] == c and password[range_max] != c) or (password[range_min] != c and password[range_max] == c):
            num_valid += 1

print(num_valid)