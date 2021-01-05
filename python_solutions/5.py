with open("input_5.txt", "r") as f:
    lines = f.readlines()

def convert_to_ranges(s):
    seat_range_fb = [0, 128]
    seat_range_lr = [0, 8]
    for c in s:
        if c in ['F', 'B']:
            dist = seat_range_fb[1] - seat_range_fb[0]
            update = seat_range_fb[0] + dist // 2
            if c == 'F':
                seat_range_fb[1] = update
            elif c == 'B':
                seat_range_fb[0] = update
        if c in ['L', 'R']:
            dist = seat_range_lr[1] - seat_range_lr[0]
            update = seat_range_lr[0] + dist // 2
            if c == 'L':
                seat_range_lr[1] = update
            elif c == 'R':
                seat_range_lr[0] = update
    return seat_range_fb, seat_range_lr

def convert_to_id(s):
    fb, lr = convert_to_ranges(s)
    return fb[0] * 8 + lr[0]

all_possible_seats = set(range(128 * 8))

max_seat_id = -1
for line in lines:
    seat_id = convert_to_id(line.strip())
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    all_possible_seats.remove(seat_id)

print(all_possible_seats)