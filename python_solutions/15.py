line = "0,20,7,16,1,18,15"

starting_nums = [int(x) for x in line.strip().split(",")]

cur_iter = 0

prev_val = None

history = {}
while cur_iter != 30_000_000:
    if cur_iter < len(starting_nums):
        if prev_val is not None:
            history[prev_val] = cur_iter
        prev_val = starting_nums[cur_iter]
    else:
        if prev_val in history:
            new_val = cur_iter - history[prev_val]
        else:
            new_val = 0
        history[prev_val] = cur_iter
        prev_val = new_val
    cur_iter += 1
print(prev_val)