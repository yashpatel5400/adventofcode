import copy

with open("input_11.txt", "r") as f:
    lines = f.readlines()

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

def pretty_print(l):
    for r in l:
        print("".join(r))
    print("====================================")

grid = [list(line.strip()) for line in lines]
new_grid = copy.copy(grid)
iters = 0
start = True
while start or new_grid != grid:
    grid = copy.deepcopy(new_grid)
    start = False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cur = grid[row][col]
            
            adjacents_seats = {
                "L": 0,
                "#": 0,
                ".": 0,
            }

            part_1 = False
            if part_1:
                if col > 0:
                    adjacents_seats[grid[row][col-1]] += 1
                    if row > 0:
                        adjacents_seats[grid[row-1][col-1]] += 1
                    if row < len(grid) - 1:
                        adjacents_seats[grid[row+1][col-1]] += 1
                if col < len(grid[row]) - 1:
                    adjacents_seats[grid[row][col+1]] += 1
                    if row > 0:
                        adjacents_seats[grid[row-1][col+1]] += 1
                    if row < len(grid) - 1:
                        adjacents_seats[grid[row+1][col+1]] += 1
                if row > 0:
                    adjacents_seats[grid[row-1][col]] += 1
                if row < len(grid) - 1:
                    adjacents_seats[grid[row+1][col]] += 1
            else:
                dirs = [
                    (-1,  0), # up
                    (-1, -1), # up, left
                    (-1,  1), # up, right

                    ( 1,  0), # down
                    ( 1, -1), # down, left
                    ( 1,  1), # down, right
                    
                    ( 0, -1), # left
                    ( 0,  1), # right
                ]

                for direction in dirs:
                    cur_pos = [row, col]
                    while True:
                        cur_pos[0] += direction[0]
                        cur_pos[1] += direction[1]

                        if cur_pos[0] < 0 or cur_pos[0] >= len(grid) or cur_pos[1] < 0 or cur_pos[1] >= len(grid[row]):
                            break

                        looking_at = grid[cur_pos[0]][cur_pos[1]]
                        if looking_at != ".":
                            adjacents_seats[looking_at] += 1
                            break

            if cur == "L":
                if adjacents_seats["#"] == 0:
                    new_grid[row][col] = "#"
            elif cur == "#":
                if adjacents_seats["#"] >= 5:
                    new_grid[row][col] = "L"
            elif cur == ".":
                new_grid[row][col] = "."

occupied = 0
for row in grid:
    for col in row:
        if col == "#":
            occupied += 1
print(occupied)