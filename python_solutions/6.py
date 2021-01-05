with open("input_6.txt", "r") as f:
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

groups = []
acc = []
for line in lines:
    if len(line.strip()) == 0:
        groups.append(acc)
        acc = []
    else:
        acc.append(line.strip())

if len(acc) != 0:
    groups.append(acc)

num_questions = 0
for group in groups:
    questions = {}
    for person in group:
        for q in set(person):
            if q not in questions:
                questions[q] = 0
            questions[q] += 1
    for q in questions:
        if questions[q] == len(group):
            num_questions += 1

print(num_questions)