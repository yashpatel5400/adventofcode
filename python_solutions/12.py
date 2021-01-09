import math

with open("input_12.txt", "r") as f:
    lines = f.readlines()

cardinal = ["E", "N", "W", "S"]
facing = 0

ship_pos = [0, 0]
waypoint_pos = [10, 1]

def move(direction, amount):
    if direction == "E":
        waypoint_pos[0] += amount
    elif direction == "W":
        waypoint_pos[0] -= amount
    elif direction == "N":
        waypoint_pos[1] += amount
    elif direction == "S":
        waypoint_pos[1] -= amount

for line in lines:
    cleaned = line.strip()
    direction = cleaned[0]
    amount = int(cleaned[1:])

    if direction == "F":
        for _ in range(amount):
            ship_pos[0] += waypoint_pos[0]
            ship_pos[1] += waypoint_pos[1]
    elif direction in ["L", "R"]:
        angle = amount
        if direction == "R":
            angle *= -1
        new_waypoint = [0, 0]
        new_waypoint[0] = round(math.cos(angle / 180 * math.pi) * waypoint_pos[0] - math.sin(angle / 180 * math.pi) * waypoint_pos[1])
        new_waypoint[1] = round(math.sin(angle / 180 * math.pi) * waypoint_pos[0] + math.cos(angle / 180 * math.pi) * waypoint_pos[1])
        waypoint_pos = new_waypoint
    else:
        move(direction, amount)

print(abs(ship_pos[0]) + abs(ship_pos[1]))