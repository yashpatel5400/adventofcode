with open("input_4.txt", "r") as f:
    lines = f.readlines()

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.

people = []
acc = []
for line in lines:
    if len(line.strip()) == 0:
        people.append(acc)
        acc = []
    else:
        acc.append(line)

num_valid = 0
for person in people:
    d = {}
    for line in person:
        properties = line.split(" ")
        for prop in properties:
            prop_name, prop_value = prop.split(":")
            d[prop_name] = prop_value.strip()

    required = set([
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        "cid",
    ])
    present = set(d.keys())
    diff = required - present
    if len(diff) == 0 or (len(diff) == 1 and list(diff)[0] == "cid"):
        if len(d["byr"]) != 4 or int(d["byr"]) < 1920 or int(d["byr"]) > 2002:
            continue
        
        if len(d["iyr"]) != 4 or int(d["iyr"]) < 2010 or int(d["iyr"]) > 2020:
            continue

        if len(d["eyr"]) != 4 or int(d["eyr"]) < 2020 or int(d["eyr"]) > 2030:
            continue

        if not d["hgt"].endswith("cm") and not d["hgt"].endswith("in"):
            continue

        if d["hgt"].endswith("cm"):
            if int(d["hgt"][:-2]) < 150 or int(d["hgt"][:-2]) > 193:
                continue

        if d["hgt"].endswith("in"):
            if int(d["hgt"][:-2]) < 59 or int(d["hgt"][:-2]) > 76:
                continue

        valid_hair = True
        for i, c in enumerate(d["hcl"]):
            if i == 0:
                if c != "#":
                    valid_hair = False
                    break
            else:
                valid_vals = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                if c not in valid_vals:
                    valid_hair = False
                    break

        if not valid_hair:
            continue

        valid_eye_colors = [
            "amb",
            "blu", 
            "brn", 
            "gry", 
            "grn", 
            "hzl", 
            "oth",
        ]

        if d["ecl"] not in valid_eye_colors:
            continue

        if len(d["pid"]) != 9:
            continue

        num_valid += 1
print(num_valid)