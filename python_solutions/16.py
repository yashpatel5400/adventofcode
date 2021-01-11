with open("input_16.txt", "r") as f:
    lines = f.readlines()

names = []
restrictions = []
for line in lines:
    if len(line.strip()) == 0:
        break

    names.append(line.strip().split(": ")[0])
    values = line.strip().split(": ")[1]
    ranges = values.split(" or ")
    restrictions.append([
        [int(x) for x in ranges[0].split("-")],
        [int(x) for x in ranges[1].split("-")]
    ])

nearby_tickets = []
start_adding = False
for line in lines:
    if start_adding:
        cleaned = line.strip().split(",")
        nearby_tickets.append([int(x) for x in cleaned])

    if "nearby tickets:" in line:
        start_adding = True

not_satisfied = []

valid_tickets = []

for ticket in nearby_tickets:
    valid_ticket = True
    for field in ticket:
        fulfills_restriction = False
        for restriction in restrictions:
            if (restriction[0][0] <= field <= restriction[0][1]) or (restriction[1][0] <= field <= restriction[1][1]):
                fulfills_restriction = True
                break

        if not fulfills_restriction:
            not_satisfied.append(field)
            valid_ticket = False
    if valid_ticket: 
        valid_tickets.append(ticket)

fields = [[valid_ticket[i] for valid_ticket in valid_tickets] for i in range(len(valid_tickets[0]))]

field_to_possibilities = []
for field in fields:
    possible_restrictions = []
    for i, restriction in enumerate(restrictions):
        fulfills_restriction = True
        for ticket in field:
            if not ((restriction[0][0] <= ticket <= restriction[0][1]) or (restriction[1][0] <= ticket <= restriction[1][1])):
                fulfills_restriction = False
                break            
        if fulfills_restriction:
            possible_restrictions.append(i)
    field_to_possibilities.append(possible_restrictions)

remaining = set(range(len(fields)))
fields = ["" for _ in fields]
while len(remaining) > 0:
    for i, possibilities in enumerate(field_to_possibilities):
        if len(possibilities) == 1:
            chosen = possibilities[0]
            chosen_idx = i
            break
    for possibilities in field_to_possibilities:
        if chosen in possibilities:
            possibilities.remove(chosen)
    fields[chosen_idx] = names[chosen]
    remaining.remove(chosen)
print(fields)

idxs = [idx for idx, val in enumerate(fields) if val.startswith("departure")]

your_ticket = "151,71,67,113,127,163,131,59,137,103,73,139,107,101,97,149,157,53,109,61"
your_ticket_vals = [int(val) for val in your_ticket.split(",")]

ans = 1
for idx in idxs:
    ans *= your_ticket_vals[idx]
print(ans)