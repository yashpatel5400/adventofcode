import math

with open("input_13.txt", "r") as f:
    lines = f.readlines()

earliest = int(lines[0].strip())
intervals = [int(time) if time != "x" else None for time in lines[1].strip().split(",")]

part_1 = False
if part_1:
    earliest_times = [math.ceil(earliest / interval) * interval if interval is not None else None for interval in intervals]

    min_time = float("inf")
    min_idx = None

    for idx, earliest_time in enumerate(earliest_times):
        if earliest_time is not None and earliest_time < min_time:
            min_time = earliest_time
            min_idx = intervals[idx]

    print("({} {}) : {}".format(min_time, min_idx, (min_time - earliest) * min_idx))
else:
    # cur = 1
    # while True:
    #     found = True

    #     for idx, interval in enumerate(intervals):
    #         if interval is not None and (cur + idx) % interval != 0:
    #             found = False

    #     if found:
    #         print(cur)
    #         break
    #     cur += 1

    interval_idx = [(interval, idx) for idx, interval in enumerate(intervals) if interval is not None ]
    
    cur = 0
    multiplier = interval_idx[0][0]

    for interval in interval_idx[1:]:
        found = False
        for j in range(interval[0]):
            print(((multiplier * j) + cur) % interval[0])
            if ((multiplier * j) + cur) % interval[0] == ((interval[0]-interval[1]) % interval[0]):
                print((multiplier * j) + cur, interval[0])
                found = True
                break
        cur += multiplier * j
        multiplier *= interval[0]
    print(cur)