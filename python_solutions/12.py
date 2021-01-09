with open("input_12.txt", "r") as f:
    lines = f.readlines()

cardinal = ["E", "N", "W", "S"]
facing = 0

pos = [0, 0]

def move(direction, amount):
    if direction == "E":
        pos[0] += amount
    elif direction == "W":
        pos[0] -= amount
    elif direction == "N":
        pos[1] += amount
    elif direction == "S":
        pos[1] -= amount

for line in lines:
    cleaned = line.strip()
    direction = cleaned[0]
    amount = int(cleaned[1:])

    move_direction = None
    if direction == "F":
        move_direction = cardinal[facing]
    elif direction == "L":
        turn = amount // 90
        facing = (facing + turn) % len(cardinal)
    elif direction == "R":
        turn = amount // 90
        facing = (facing - turn) % len(cardinal)
    else:
        move_direction = direction

    if direction != "R":
        move(move_direction, amount)

print(abs(pos[0]) + abs(pos[1]))